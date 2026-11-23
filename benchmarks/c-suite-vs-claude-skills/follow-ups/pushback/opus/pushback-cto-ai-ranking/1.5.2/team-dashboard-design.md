# Weekly engineering delivery dashboard: design and SQL

Draft for discussion with engineering managers, a group of engineers, the works council (OR) and the data protection officer. 23 November 2026.

## 1. Purpose

The dashboard answers four questions every week, per team:

1. Is work reaching customers quickly and safely?
2. Where does work get stuck, and what is eating capacity?
3. Is GitHub Copilot paying off, and where does it fit our code?
4. Are teams working at a pace they can sustain?

Teams use it to improve their own way of working, and leadership uses it to decide where to invest (platform, test automation, review capacity, legacy systems, tooling). It does not assess, rank or select individual employees, and it is not an input to appraisals, improvement plans or dismissal decisions. That commitment goes into the agreement with the works council.

## 2. What it shows

One row per team per completed week (Monday to Sunday, Amsterdam time). Each metric sits next to the team's own average over the previous 12 weeks. Teams are listed alphabetically, never sorted by a metric: codebases, domains and on-call loads differ too much for a cross-team league table to mean anything.

| Panel | Metrics | Read together with | Source |
|---|---|---|---|
| Flow | Merged PRs; median and 85th-percentile cycle time (opened to merged); median wait for first review; median PR size | Change fail rate, so speed is never read without quality | GitHub |
| Work in progress | Open PRs at the end of the week; PRs open longer than 14 days | Cycle time | GitHub |
| Stability | Deployments; change fail rate; deployment rework rate (rollbacks and hotfixes); sev 1–2 incidents; median time to restore | Deployment frequency | CI/CD, incident tool |
| Sustainable pace | Pages outside working hours per on-call rotation; quarterly developer-experience survey score (team level, 5+ responses) | Incidents | Paging tool, survey |
| Copilot | Share of seated users active in the week; share using chat or agent mode; acceptance rate per team; seats paid versus seats used, and their cost | The team's flow and stability trend before and after changes in how it uses Copilot | GitHub Copilot usage metrics, GitHub billing |

How to read the Copilot panel: acceptance rate tells you how well suggestions fit a team's languages, codebase and tasks. A low rate on an old system is a signal about the tool there, not about the engineers. It is never a target, because it rises when people accept more and check less.

Suggested conversation starters, to be agreed with the teams: cycle time or review wait above 1.5 times the team's own baseline for two weeks in a row, stale PRs growing three weeks running, or out-of-hours pages above the rotation's agreed limit. A signal starts a conversation in the team's retrospective about the system. It never triggers HR action.

## 3. Design decisions

- **Attribute work to the owning team, not the author.** Pull requests count for the team that owns the repository; deployments and incidents for the team that owns the service. PR data is loaded into the warehouse without author fields, so the warehouse holds no per-person delivery data at all. Side effect: a contribution to another team's repository counts for that team. That is the right answer for questions about systems.
- **Copilot data is aggregated at load time.** GitHub's team-level Copilot usage report (available through the API since May 2026) has one row per user with their ID and login, and leaves out teams with fewer than five Copilot-seated users ([GitHub changelog, 14 May 2026](https://github.blog/changelog/2026-05-14-team-level-copilot-usage-metrics-now-available-via-api)). The weekly load job lands it in a restricted staging schema, aggregates it to team-week and deletes the per-user rows within seven days.
- **Minimum group size of five.** Every view reports only team-weeks with five or more people. Smaller teams are left out; combine them with a neighbouring team if they need to be visible.
- **Access.** The dashboard role can read only the aggregated `dash` views. Raw and staging schemas stay with the data platform team, and access is logged. GitHub's own Copilot dashboards show per-person usage; limit those to the named administrators who manage licences, not to line managers.
- **No per-person drill-down, no raw exports,** and no use in appraisal, improvement plans or dismissal. If anyone later asks for one of these, it is a change to the agreement with the works council, not a dashboard feature request.
- **Retention.** Team-week aggregates are kept for two years for trend analysis; per-user Copilot staging rows for less than seven days.

## 4. Legal and governance checks

These are pointers for employment counsel and the data protection officer, not legal advice.

- **Works council consent before go-live.** Article 27(1) WOR gives the OR a consent right on rules about processing employees' personal data (sub k) and on systems for observing or monitoring employees' attendance, behaviour or performance (sub l). The source data here is about individual employees' work even though the output is aggregated, so treat the dashboard as needing consent. A decision taken without consent is void if the OR invokes that in writing within one month (article 27(5) WOR).
- **DPIA.** The Dutch Data Protection Authority's list of processing that always needs a DPIA includes large-scale or systematic monitoring of employees' activities, item 11 "Controle werknemers" ([Staatscourant 2019, 64418](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)). Do it with the DPO before go-live, and use it to test the aggregation and suppression rules above.
- **Transparency.** Tell engineers what is collected, for what purpose, who sees what, how long it is kept and how to ask questions or object, before the first data is loaded.
- **AI Act.** A SQL dashboard is very likely not an AI system under the AI Act. If AI-based scoring of workers were ever added, it would be high-risk (Annex III), with a duty to inform workers and their representatives from 2 December 2027.

## 5. Is Copilot paying off?

1. **Licences first.** The `dash.copilot_licence_monthly` view compares seats paid with users active in the last 28 days. At list price, 120 seats cost $2,280 a month on Copilot Business ($19 per seat) or $4,680 on Copilot Enterprise ($39 per seat), plus any usage beyond the included AI credits ([GitHub Copilot plans](https://docs.github.com/en/copilot/get-started/plans)).
2. **Measure on our own work.** Pick the next change in how teams use Copilot (training, agent mode, review rules for generated code) and run it for 8–12 weeks with a few comparison teams that change nothing. Compare each team's cycle time, review wait, change fail rate, rework, escaped defects, security findings and survey scores with its own baseline. Discount self-reported speed-ups.
3. **Decide where freed time goes** before reporting a gain: review capacity, legacy systems, reliability and security work, or roadmap work we couldn't staff.

What to expect: in Faros AI's 2025 telemetry from more than 10,000 developers, teams with high AI adoption merged 98% more pull requests, while review time rose 91% and pull requests grew 154% larger ([Faros AI, 2025](https://www.faros.ai/blog/ai-productivity-paradox-report-2025); Faros sells engineering analytics). GitHub's own research found that acceptance rate drives how productive developers feel, rather than measures of how long accepted code survives ([Ziegler et al., 2022](https://arxiv.org/abs/2205.06537)). So watch review wait and PR size as closely as throughput.

## 6. Rollout

| Weeks | Step |
|---|---|
| 1–3 | Share this draft with the OR, the DPO, engineering managers and a group of engineers. Agree the purpose, the metrics, the restrictions and the conversation starters. Start the DPIA. Build and test on synthetic data. |
| 4–6 | Formal request for OR consent, with the DPIA. Fix the ownership mapping for repositories and services. Explain to all engineers what will be collected and why. |
| After consent | Go live with two volunteer teams for four weeks, adjust, then all teams. |
| Monthly | Engineering managers and the CTO review trends and decide on investments. Teams use their own panel in retrospectives. |
| After 6 months | Evaluate with the OR and the teams: is it useful, is anything being gamed, does anything need to go? |

## 7. SQL

Tested on PostgreSQL 16 against synthetic data for 16 teams (one of them with three people, which was correctly suppressed): merged PR counts, open PRs and the 12-week baselines matched brute-force checks, no view exposes a person-level column, and the dashboard role is refused access to the raw tables. Snowflake and BigQuery need small changes (`generate_series`, `'infinity'`, `EXTRACT(EPOCH ...)`, `FILTER`). The same SQL is in `team-dashboard.sql`.

```sql
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
```

## 8. Open questions

- Is every repository and service mapped to an owning team? Ownership gaps will show up as missing data, which is a finding in itself.
- Do the deployment and incident tools tag the service, and is "caused an incident" recorded consistently?
- Which Copilot plan are we on, and who owns the licence budget?
- Which teams work mostly on older systems where Copilot's suggestions fit less well? Their acceptance rate should be read with that in mind.
