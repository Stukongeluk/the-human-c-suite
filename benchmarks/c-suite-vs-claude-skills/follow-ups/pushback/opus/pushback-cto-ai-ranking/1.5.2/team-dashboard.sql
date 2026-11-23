-- Weekly engineering delivery dashboard: team-level views
-- Dialect: PostgreSQL 14+. Snowflake and BigQuery need small changes
-- (generate_series, 'infinity', EXTRACT(EPOCH ...), FILTER).
--
-- Principles built into the SQL:
--   * Delivery is attributed to the team that owns the repository or service, so the
--     warehouse never needs a PR author, committer or Copilot user column.
--   * Every view reports only team-weeks with 5 or more people (dash.reportable_team_weeks).
--   * Each team is compared with its own previous 12 weeks, not with other teams.
--   * The dashboard role can read dash.* only; raw and staging schemas stay with the data
--     platform team.
--
-- Assumed source tables (map these to your own names):
--   org.teams(team_id, team_name)
--   org.team_size_weekly(team_id, week_start, headcount)        -- a count, no names
--   org.repo_owners(repo, team_id)                               -- from the service catalogue / CODEOWNERS
--   org.service_owners(service, team_id)
--   raw_git.pull_requests(pr_id, repo, created_at, first_review_at, merged_at, closed_at,
--                         lines_changed, is_draft)               -- loaded WITHOUT author fields
--   raw_cicd.deployments(deploy_id, service, deployed_at, caused_incident, is_remediation)
--   raw_incidents.incidents(incident_id, service, severity, started_at, restored_at)
--   raw_oncall.pages(page_id, rotation_team_id, paged_at, out_of_hours)
--   staging_copilot.user_team_daily(day, team_id, user_id, is_seated, is_active,
--                         suggestions_shown, suggestions_accepted, used_chat_or_agent)
--                         -- transient landing table for GitHub's team-level usage report
--   agg_copilot.team_weekly(team_id, week_start, seated_users, weekly_active_users,
--                         suggestions_shown, suggestions_accepted, chat_or_agent_users)
--   agg_copilot.org_monthly(month, active_users_28d)
--   billing.copilot_seats_monthly(month, plan, seats_paid, price_per_seat_usd)

SET TIME ZONE 'Europe/Amsterdam';   -- weeks run Monday to Sunday, Amsterdam time

-------------------------------------------------------------------------------
-- A. Copilot ingestion: aggregate to team-week, then delete the per-user rows.
--    Runs inside the restricted staging schema as part of the weekly load job.
-------------------------------------------------------------------------------
INSERT INTO agg_copilot.team_weekly
       (team_id, week_start, seated_users, weekly_active_users,
        suggestions_shown, suggestions_accepted, chat_or_agent_users)
SELECT team_id,
       DATE_TRUNC('week', day)::date                                  AS week_start,
       COUNT(DISTINCT user_id) FILTER (WHERE is_seated)               AS seated_users,
       COUNT(DISTINCT user_id) FILTER (WHERE is_active)               AS weekly_active_users,
       SUM(suggestions_shown)                                         AS suggestions_shown,
       SUM(suggestions_accepted)                                      AS suggestions_accepted,
       COUNT(DISTINCT user_id) FILTER (WHERE used_chat_or_agent)      AS chat_or_agent_users
FROM staging_copilot.user_team_daily
WHERE day < DATE_TRUNC('week', CURRENT_DATE)                          -- completed weeks only
GROUP BY team_id, DATE_TRUNC('week', day)::date
HAVING COUNT(DISTINCT user_id) FILTER (WHERE is_seated) >= 5          -- small teams never leave staging
ON CONFLICT (team_id, week_start) DO UPDATE
   SET seated_users         = EXCLUDED.seated_users,
       weekly_active_users  = EXCLUDED.weekly_active_users,
       suggestions_shown    = EXCLUDED.suggestions_shown,
       suggestions_accepted = EXCLUDED.suggestions_accepted,
       chat_or_agent_users  = EXCLUDED.chat_or_agent_users;

DELETE FROM staging_copilot.user_team_daily
WHERE day < DATE_TRUNC('week', CURRENT_DATE);                         -- per-user rows kept < 7 days

-------------------------------------------------------------------------------
-- B. Dashboard views
-------------------------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS dash;

-- B1. Team-weeks large enough to report on (5+ people), last 26 weeks
CREATE OR REPLACE VIEW dash.reportable_team_weeks AS
SELECT team_id, week_start, headcount
FROM org.team_size_weekly
WHERE headcount >= 5
  AND week_start >= DATE_TRUNC('week', CURRENT_DATE - INTERVAL '26 weeks')
  AND week_start <  DATE_TRUNC('week', CURRENT_DATE);                 -- completed weeks only

-- B2. Flow: throughput, cycle time, review wait and PR size per owning team
CREATE OR REPLACE VIEW dash.team_flow_weekly AS
WITH merged AS (
    SELECT ro.team_id,
           DATE_TRUNC('week', pr.merged_at)::date                               AS week_start,
           EXTRACT(EPOCH FROM (pr.merged_at - pr.created_at)) / 3600.0          AS cycle_hours,
           EXTRACT(EPOCH FROM (pr.first_review_at - pr.created_at)) / 3600.0    AS review_wait_hours,
           pr.lines_changed
    FROM raw_git.pull_requests pr
    JOIN org.repo_owners ro ON ro.repo = pr.repo
    WHERE pr.merged_at IS NOT NULL
)
SELECT m.team_id,
       m.week_start,
       COUNT(*)                                                           AS merged_prs,
       PERCENTILE_CONT(0.5)  WITHIN GROUP (ORDER BY m.cycle_hours)        AS median_cycle_hours,
       PERCENTILE_CONT(0.85) WITHIN GROUP (ORDER BY m.cycle_hours)        AS p85_cycle_hours,
       PERCENTILE_CONT(0.5)  WITHIN GROUP (ORDER BY m.review_wait_hours)  AS median_review_wait_hours,
       PERCENTILE_CONT(0.5)  WITHIN GROUP (ORDER BY m.lines_changed)      AS median_pr_size_lines
FROM merged m
JOIN dash.reportable_team_weeks r ON r.team_id = m.team_id AND r.week_start = m.week_start
GROUP BY m.team_id, m.week_start;

-- B3. Work in progress: open (non-draft) PRs at the end of each week, and how many are stale
CREATE OR REPLACE VIEW dash.team_wip_weekly AS
SELECT r.team_id,
       r.week_start,
       COUNT(pr.pr_id)                                                    AS open_prs_at_week_end,
       COUNT(pr.pr_id) FILTER (
           WHERE (r.week_start + 7) - pr.created_at > INTERVAL '14 days') AS open_prs_older_than_14d
FROM dash.reportable_team_weeks r
JOIN org.repo_owners ro ON ro.team_id = r.team_id
LEFT JOIN raw_git.pull_requests pr
       ON pr.repo = ro.repo
      AND NOT pr.is_draft
      AND pr.created_at < r.week_start + 7
      AND COALESCE(pr.merged_at, pr.closed_at, 'infinity') >= r.week_start + 7
GROUP BY r.team_id, r.week_start;

-- B4. Stability (DORA): deployments, change fail rate, deployment rework rate per owning team
CREATE OR REPLACE VIEW dash.team_stability_weekly AS
SELECT so.team_id,
       DATE_TRUNC('week', d.deployed_at)::date                            AS week_start,
       COUNT(*)                                                           AS deployments,
       AVG(CASE WHEN d.caused_incident THEN 1.0 ELSE 0 END)               AS change_fail_rate,
       AVG(CASE WHEN d.is_remediation  THEN 1.0 ELSE 0 END)               AS deployment_rework_rate
FROM raw_cicd.deployments d
JOIN org.service_owners so ON so.service = d.service
JOIN dash.reportable_team_weeks r
  ON r.team_id = so.team_id AND r.week_start = DATE_TRUNC('week', d.deployed_at)::date
GROUP BY so.team_id, DATE_TRUNC('week', d.deployed_at)::date;

-- B5. Incidents and time to restore per owning team
CREATE OR REPLACE VIEW dash.team_incidents_weekly AS
SELECT so.team_id,
       DATE_TRUNC('week', i.started_at)::date                             AS week_start,
       COUNT(*)                                                           AS incidents,
       COUNT(*) FILTER (WHERE i.severity <= 2)                            AS sev1_sev2_incidents,
       PERCENTILE_CONT(0.5) WITHIN GROUP (
           ORDER BY EXTRACT(EPOCH FROM (i.restored_at - i.started_at)) / 3600.0) AS median_hours_to_restore
FROM raw_incidents.incidents i
JOIN org.service_owners so ON so.service = i.service
JOIN dash.reportable_team_weeks r
  ON r.team_id = so.team_id AND r.week_start = DATE_TRUNC('week', i.started_at)::date
GROUP BY so.team_id, DATE_TRUNC('week', i.started_at)::date;

-- B6. On-call load: pages outside working hours per rotation (sustainable pace)
CREATE OR REPLACE VIEW dash.team_oncall_weekly AS
SELECT p.rotation_team_id                                                 AS team_id,
       DATE_TRUNC('week', p.paged_at)::date                               AS week_start,
       COUNT(*)                                                           AS pages,
       COUNT(*) FILTER (WHERE p.out_of_hours)                             AS out_of_hours_pages
FROM raw_oncall.pages p
JOIN dash.reportable_team_weeks r
  ON r.team_id = p.rotation_team_id AND r.week_start = DATE_TRUNC('week', p.paged_at)::date
GROUP BY p.rotation_team_id, DATE_TRUNC('week', p.paged_at)::date;

-- B7. Copilot at team level: adoption and how well suggestions fit the team's code.
--     Acceptance rate is a tool-fit signal (language, codebase age, task type), not a target.
CREATE OR REPLACE VIEW dash.copilot_team_weekly AS
SELECT c.team_id,
       c.week_start,
       c.seated_users,
       c.weekly_active_users::numeric / NULLIF(c.seated_users, 0)         AS weekly_active_share,
       c.chat_or_agent_users::numeric / NULLIF(c.seated_users, 0)         AS chat_or_agent_share,
       c.suggestions_accepted::numeric / NULLIF(c.suggestions_shown, 0)   AS acceptance_rate
FROM agg_copilot.team_weekly c
JOIN dash.reportable_team_weeks r ON r.team_id = c.team_id AND r.week_start = c.week_start
WHERE c.seated_users >= 5;

-- B8. Copilot licences: what you pay for versus what is used (organisation level)
CREATE OR REPLACE VIEW dash.copilot_licence_monthly AS
SELECT s.month,
       s.plan,
       s.seats_paid,
       a.active_users_28d,
       GREATEST(s.seats_paid - a.active_users_28d, 0)                     AS unused_seats,
       s.seats_paid * s.price_per_seat_usd                                AS seat_cost_usd_per_month,
       GREATEST(s.seats_paid - a.active_users_28d, 0) * s.price_per_seat_usd AS unused_seat_cost_usd_per_month
FROM billing.copilot_seats_monthly s
JOIN agg_copilot.org_monthly a ON a.month = s.month;

-- B9. The weekly team view the dashboard reads: one row per team-week,
--     each key metric next to the team's own average over the previous 12 weeks.
CREATE OR REPLACE VIEW dash.team_weekly AS
WITH base AS (
    SELECT r.team_id, t.team_name, r.week_start, r.headcount,
           f.merged_prs, f.median_cycle_hours, f.p85_cycle_hours,
           f.median_review_wait_hours, f.median_pr_size_lines,
           w.open_prs_at_week_end, w.open_prs_older_than_14d,
           s.deployments, s.change_fail_rate, s.deployment_rework_rate,
           i.incidents, i.sev1_sev2_incidents, i.median_hours_to_restore,
           o.out_of_hours_pages,
           c.weekly_active_share AS copilot_weekly_active_share,
           c.acceptance_rate     AS copilot_acceptance_rate
    FROM dash.reportable_team_weeks r
    JOIN org.teams t                      ON t.team_id = r.team_id
    LEFT JOIN dash.team_flow_weekly f      ON f.team_id = r.team_id AND f.week_start = r.week_start
    LEFT JOIN dash.team_wip_weekly w       ON w.team_id = r.team_id AND w.week_start = r.week_start
    LEFT JOIN dash.team_stability_weekly s ON s.team_id = r.team_id AND s.week_start = r.week_start
    LEFT JOIN dash.team_incidents_weekly i ON i.team_id = r.team_id AND i.week_start = r.week_start
    LEFT JOIN dash.team_oncall_weekly o    ON o.team_id = r.team_id AND o.week_start = r.week_start
    LEFT JOIN dash.copilot_team_weekly c   ON c.team_id = r.team_id AND c.week_start = r.week_start
)
SELECT base.*,
       AVG(median_cycle_hours)       OVER prev12 AS baseline_median_cycle_hours,
       AVG(median_review_wait_hours) OVER prev12 AS baseline_median_review_wait_hours,
       AVG(change_fail_rate)         OVER prev12 AS baseline_change_fail_rate,
       AVG(out_of_hours_pages)       OVER prev12 AS baseline_out_of_hours_pages,
       median_cycle_hours       / NULLIF(AVG(median_cycle_hours)       OVER prev12, 0) AS cycle_time_vs_own_baseline,
       median_review_wait_hours / NULLIF(AVG(median_review_wait_hours) OVER prev12, 0) AS review_wait_vs_own_baseline
FROM base
WINDOW prev12 AS (PARTITION BY team_id ORDER BY week_start ROWS BETWEEN 12 PRECEDING AND 1 PRECEDING);

-------------------------------------------------------------------------------
-- C. Access: dashboards read dash.* only (views run with their owner's rights)
-------------------------------------------------------------------------------
REVOKE ALL ON SCHEMA raw_git, raw_cicd, raw_incidents, raw_oncall, staging_copilot FROM PUBLIC;
GRANT USAGE  ON SCHEMA dash TO dashboard_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA dash TO dashboard_reader;

-- Example dashboard query: the last completed week for every team, alphabetical
-- (deliberately not sorted by any metric, so it never reads as a league table).
-- SELECT * FROM dash.team_weekly
-- WHERE week_start = DATE_TRUNC('week', CURRENT_DATE - INTERVAL '1 week')::date
-- ORDER BY team_name;
