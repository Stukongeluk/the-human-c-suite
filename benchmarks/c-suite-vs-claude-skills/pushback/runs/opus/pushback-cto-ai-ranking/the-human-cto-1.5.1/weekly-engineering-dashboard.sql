-- =============================================================================
-- Weekly engineering delivery dashboard: team level
-- Dialect: PostgreSQL 14+ (notes for Snowflake and BigQuery at the end).
--
-- The source tables in sections 1a and 1b are ASSUMED shapes. Map your
-- GitHub, CI/CD, incident-tool, scanner and Copilot usage-metrics exports onto
-- them in the ingestion step; the rest of the file then runs as is.
--
-- Rules this file enforces:
--   * Person identifiers exist only in staging_restricted: readable by the ETL
--     service account only, kept 35 days (Copilot) or 90 days (pull requests).
--   * Everything a reader can query is per team per week. Teams with fewer
--     than 5 members are left out of team views; Copilot figures are shown
--     only where at least 5 people were active in every one of the 4 weeks.
--   * Each team is compared with its own previous 12 weeks. There is no
--     ranking of people or of teams anywhere in this file.
--   * Every speed figure sits next to a quality or health figure.
--
-- Weekly schedule: run section 3 on Wednesday morning (Copilot usage data can
-- take two full days to arrive). Each run recomputes the last 4 complete
-- weeks, so late data is picked up. First run after the initial load: use
-- recent_weeks(26) in section 3 to build the baseline, then go back to 4.
-- Never recompute more weeks than staging still holds (Copilot data is kept
-- 35 days): a larger window would replace stored history with empty rows.
-- =============================================================================


-- 0. Schemas -------------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS staging_restricted;  -- person-linked source data, ETL only
CREATE SCHEMA IF NOT EXISTS ops;                 -- service-level data, no person fields
CREATE SCHEMA IF NOT EXISTS eng_metrics;         -- team-week aggregates and views


-- 1a. Person-linked source tables (assumed shapes) ----------------------------
-- One primary team per engineer at any moment; valid_to is exclusive, NULL = current.
CREATE TABLE IF NOT EXISTS staging_restricted.team_membership (
  engineer_login  text NOT NULL,
  team_id         text NOT NULL,
  valid_from      date NOT NULL,
  valid_to        date,
  PRIMARY KEY (engineer_login, valid_from)
);

CREATE TABLE IF NOT EXISTS staging_restricted.github_pull_requests (
  pr_id                bigint PRIMARY KEY,
  repo                 text NOT NULL,
  author_login         text NOT NULL,
  is_bot               boolean NOT NULL DEFAULT false,
  created_at           timestamptz NOT NULL,
  ready_for_review_at  timestamptz,          -- = created_at unless opened as draft; NULL while still a draft
  first_review_at      timestamptz,          -- first review by someone other than the author
  merged_at            timestamptz,
  closed_at            timestamptz,
  additions            integer NOT NULL DEFAULT 0,
  deletions            integer NOT NULL DEFAULT 0
);

-- From the Copilot usage metrics API, user-level 1-day reports, mapped to these columns.
CREATE TABLE IF NOT EXISTS staging_restricted.copilot_user_daily (
  day                   date NOT NULL,
  user_login            text NOT NULL,
  is_active             boolean NOT NULL,
  completions_shown     integer NOT NULL DEFAULT 0,
  completions_accepted  integer NOT NULL DEFAULT 0,
  chat_agent_requests   integer NOT NULL DEFAULT 0,  -- chat and agent use; not covered by acceptance rate
  PRIMARY KEY (day, user_login)
);

-- From the Copilot seat/billing API: one snapshot per Monday.
CREATE TABLE IF NOT EXISTS staging_restricted.copilot_seats (
  snapshot_date        date NOT NULL,
  user_login           text NOT NULL,
  last_activity_at     timestamptz,
  seat_cost_eur_month  numeric(10,2) NOT NULL,
  PRIMARY KEY (snapshot_date, user_login)
);


-- 1b. Service-level source tables (no person fields) --------------------------
CREATE TABLE IF NOT EXISTS ops.deployments (
  deploy_id         text PRIMARY KEY,
  service           text NOT NULL,
  team_id           text NOT NULL,          -- owning team, from the service catalogue
  environment       text NOT NULL,
  deployed_at       timestamptz NOT NULL,
  first_commit_at   timestamptz,            -- oldest commit in the change set
  caused_incident   boolean NOT NULL DEFAULT false,  -- led to an incident or rollback
  is_unplanned_fix  boolean NOT NULL DEFAULT false   -- hotfix or rollback for a production issue
);

CREATE TABLE IF NOT EXISTS ops.incidents (
  incident_id      text PRIMARY KEY,
  service          text NOT NULL,
  team_id          text NOT NULL,
  started_at       timestamptz NOT NULL,
  resolved_at      timestamptz,
  customer_impact  boolean NOT NULL DEFAULT false
);

CREATE TABLE IF NOT EXISTS ops.oncall_pages (
  page_id       text PRIMARY KEY,
  team_id       text NOT NULL,              -- rotation owner; no responder field
  paged_at      timestamptz NOT NULL,
  out_of_hours  boolean NOT NULL
);

CREATE TABLE IF NOT EXISTS ops.security_findings (
  finding_id  text PRIMARY KEY,
  team_id     text NOT NULL,
  severity    text NOT NULL CHECK (severity IN ('critical', 'high', 'medium', 'low')),
  opened_at   timestamptz NOT NULL,
  closed_at   timestamptz
);


-- 2. Curated team-week tables: the only data the dashboard reads ---------------
CREATE TABLE IF NOT EXISTS eng_metrics.team_week_size (
  team_id     text NOT NULL,
  week_start  date NOT NULL,                -- Monday
  members     integer NOT NULL,
  PRIMARY KEY (team_id, week_start)
);

CREATE TABLE IF NOT EXISTS eng_metrics.team_week_flow (
  team_id                         text NOT NULL,
  week_start                      date NOT NULL,
  prs_merged                      integer NOT NULL,   -- context for the medians, not a target
  median_cycle_hours              double precision,   -- ready for review -> merged
  p85_cycle_hours                 double precision,
  median_first_review_wait_hours  double precision,
  median_pr_lines                 double precision,
  share_prs_over_400_lines        numeric,
  share_merged_without_review     numeric,
  open_prs_older_than_7d          integer NOT NULL,   -- waiting for review or merge at week end
  PRIMARY KEY (team_id, week_start)
);

CREATE TABLE IF NOT EXISTS eng_metrics.team_week_delivery (
  team_id                       text NOT NULL,
  week_start                    date NOT NULL,
  deployments                   integer NOT NULL,
  failed_deployments            integer NOT NULL,
  unplanned_fix_deployments     integer NOT NULL,
  median_lead_time_hours        double precision,     -- first commit -> production
  incidents                     integer NOT NULL,
  customer_impacting_incidents  integer NOT NULL,
  median_restore_hours          double precision,
  open_high_findings_over_30d   integer NOT NULL,     -- critical/high, open > 30 days at week end
  PRIMARY KEY (team_id, week_start)
);

CREATE TABLE IF NOT EXISTS eng_metrics.team_week_copilot (
  team_id               text NOT NULL,
  week_start            date NOT NULL,
  seats                 integer NOT NULL,
  seat_cost_eur_week    numeric NOT NULL,
  active_users          integer NOT NULL,
  completions_shown     bigint NOT NULL,
  completions_accepted  bigint NOT NULL,
  chat_agent_requests   bigint NOT NULL,
  PRIMARY KEY (team_id, week_start)
);

CREATE TABLE IF NOT EXISTS eng_metrics.team_week_oncall (
  team_id             text NOT NULL,
  week_start          date NOT NULL,
  pages_total         integer NOT NULL,
  pages_out_of_hours  integer NOT NULL,
  PRIMARY KEY (team_id, week_start)
);

CREATE TABLE IF NOT EXISTS eng_metrics.org_week_copilot_licences (
  week_start                  date PRIMARY KEY,
  seats                       integer NOT NULL,
  seats_active_30d            integer NOT NULL,
  seats_idle_30d              integer NOT NULL,
  seats_without_current_team  integer NOT NULL,   -- leavers and unassigned seats
  cost_eur_month              numeric NOT NULL,
  idle_cost_eur_month         numeric NOT NULL
);

-- Teams in a Copilot comparison (section 6): 'pilot' or 'comparison'.
CREATE TABLE IF NOT EXISTS eng_metrics.copilot_comparison_groups (
  team_id      text PRIMARY KEY,
  group_label  text NOT NULL CHECK (group_label IN ('pilot', 'comparison'))
);

-- One row: the Monday the pilot teams' change started. Set it with:
--   INSERT INTO eng_metrics.copilot_comparison_settings (change_date) VALUES (DATE '2026-09-07')
--   ON CONFLICT (id) DO UPDATE SET change_date = EXCLUDED.change_date;
CREATE TABLE IF NOT EXISTS eng_metrics.copilot_comparison_settings (
  id           boolean PRIMARY KEY DEFAULT true CHECK (id),
  change_date  date NOT NULL CHECK (EXTRACT(ISODOW FROM change_date) = 1)
);

-- Helper: the last N complete Monday-weeks.
CREATE OR REPLACE FUNCTION eng_metrics.recent_weeks(weeks_back integer)
RETURNS TABLE (week_start date)
LANGUAGE sql STABLE AS $$
  SELECT gs::date
  FROM generate_series(date_trunc('week', CURRENT_DATE)::date - 7 * weeks_back,
                       date_trunc('week', CURRENT_DATE)::date - 7,
                       interval '7 days') AS gs
$$;


-- 3. Weekly jobs (ETL service account) ----------------------------------------
-- Each job deletes and rebuilds the recomputed weeks inside one transaction.
BEGIN;

-- 3a. Team size per week
DELETE FROM eng_metrics.team_week_size
WHERE week_start IN (SELECT week_start FROM eng_metrics.recent_weeks(4));

INSERT INTO eng_metrics.team_week_size (team_id, week_start, members)
SELECT m.team_id, w.week_start, COUNT(DISTINCT m.engineer_login)
FROM eng_metrics.recent_weeks(4) w
JOIN staging_restricted.team_membership m
  ON m.valid_from < w.week_start + 7
 AND COALESCE(m.valid_to, DATE '9999-12-31') > w.week_start
GROUP BY m.team_id, w.week_start;

-- 3b. Flow: cycle time, review wait, pull-request size, work waiting
DELETE FROM eng_metrics.team_week_flow
WHERE week_start IN (SELECT week_start FROM eng_metrics.recent_weeks(4));

WITH w AS (SELECT week_start FROM eng_metrics.recent_weeks(4)),
merged AS (
  SELECT m.team_id,
         date_trunc('week', p.merged_at)::date AS week_start,
         EXTRACT(EPOCH FROM p.merged_at - COALESCE(p.ready_for_review_at, p.created_at)) / 3600.0       AS cycle_hours,
         EXTRACT(EPOCH FROM p.first_review_at - COALESCE(p.ready_for_review_at, p.created_at)) / 3600.0 AS first_review_wait_hours,
         p.additions + p.deletions AS lines_changed,
         p.first_review_at IS NULL AS no_review
  FROM staging_restricted.github_pull_requests p
  JOIN staging_restricted.team_membership m
    ON m.engineer_login = p.author_login
   AND p.merged_at::date >= m.valid_from
   AND p.merged_at::date <  COALESCE(m.valid_to, DATE '9999-12-31')
  WHERE NOT p.is_bot
    AND p.merged_at >= (SELECT MIN(week_start) FROM w)
    AND p.merged_at <  (SELECT MAX(week_start) + 7 FROM w)
),
merged_agg AS (
  SELECT team_id, week_start,
         COUNT(*) AS prs_merged,
         percentile_cont(0.5)  WITHIN GROUP (ORDER BY cycle_hours)             AS median_cycle_hours,
         percentile_cont(0.85) WITHIN GROUP (ORDER BY cycle_hours)             AS p85_cycle_hours,
         percentile_cont(0.5)  WITHIN GROUP (ORDER BY first_review_wait_hours) AS median_first_review_wait_hours,
         percentile_cont(0.5)  WITHIN GROUP (ORDER BY lines_changed)           AS median_pr_lines,
         AVG(CASE WHEN lines_changed > 400 THEN 1.0 ELSE 0 END)                AS share_prs_over_400_lines,
         AVG(CASE WHEN no_review THEN 1.0 ELSE 0 END)                          AS share_merged_without_review
  FROM merged
  GROUP BY team_id, week_start
),
waiting AS (
  -- Open for review at the end of the week and opened for review before the week began.
  SELECT m.team_id, w.week_start, COUNT(*) AS open_prs_older_than_7d
  FROM w
  JOIN staging_restricted.github_pull_requests p
    ON p.ready_for_review_at < w.week_start
   AND COALESCE(p.merged_at, p.closed_at, 'infinity'::timestamptz) >= w.week_start + 7
   AND NOT p.is_bot
  JOIN staging_restricted.team_membership m
    ON m.engineer_login = p.author_login
   AND w.week_start >= m.valid_from
   AND w.week_start <  COALESCE(m.valid_to, DATE '9999-12-31')
  GROUP BY m.team_id, w.week_start
)
INSERT INTO eng_metrics.team_week_flow
SELECT COALESCE(a.team_id, o.team_id),
       COALESCE(a.week_start, o.week_start),
       COALESCE(a.prs_merged, 0),
       a.median_cycle_hours, a.p85_cycle_hours, a.median_first_review_wait_hours,
       a.median_pr_lines, a.share_prs_over_400_lines, a.share_merged_without_review,
       COALESCE(o.open_prs_older_than_7d, 0)
FROM merged_agg a
FULL OUTER JOIN waiting o
  ON o.team_id = a.team_id AND o.week_start = a.week_start;

-- 3c. Delivery and quality: DORA metrics, incidents, security findings
DELETE FROM eng_metrics.team_week_delivery
WHERE week_start IN (SELECT week_start FROM eng_metrics.recent_weeks(4));

WITH w AS (SELECT week_start FROM eng_metrics.recent_weeks(4)),
d AS (
  SELECT team_id, date_trunc('week', deployed_at)::date AS week_start,
         COUNT(*)                                  AS deployments,
         COUNT(*) FILTER (WHERE caused_incident)   AS failed_deployments,
         COUNT(*) FILTER (WHERE is_unplanned_fix)  AS unplanned_fix_deployments,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY EXTRACT(EPOCH FROM deployed_at - first_commit_at) / 3600.0)
                                                   AS median_lead_time_hours
  FROM ops.deployments
  WHERE environment = 'production'
    AND deployed_at >= (SELECT MIN(week_start) FROM w)
    AND deployed_at <  (SELECT MAX(week_start) + 7 FROM w)
  GROUP BY 1, 2
),
i AS (
  SELECT team_id, date_trunc('week', started_at)::date AS week_start,
         COUNT(*)                                  AS incidents,
         COUNT(*) FILTER (WHERE customer_impact)   AS customer_impacting_incidents,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY EXTRACT(EPOCH FROM resolved_at - started_at) / 3600.0)
                                                   AS median_restore_hours
  FROM ops.incidents
  WHERE started_at >= (SELECT MIN(week_start) FROM w)
    AND started_at <  (SELECT MAX(week_start) + 7 FROM w)
  GROUP BY 1, 2
),
s AS (
  SELECT f.team_id, w.week_start, COUNT(*) AS open_high_findings_over_30d
  FROM w
  JOIN ops.security_findings f
    ON f.severity IN ('critical', 'high')
   AND f.opened_at < w.week_start + 7 - 30
   AND COALESCE(f.closed_at, 'infinity'::timestamptz) >= w.week_start + 7
  GROUP BY 1, 2
),
k AS (
  SELECT team_id, week_start FROM d
  UNION SELECT team_id, week_start FROM i
  UNION SELECT team_id, week_start FROM s
)
INSERT INTO eng_metrics.team_week_delivery
SELECT k.team_id, k.week_start,
       COALESCE(d.deployments, 0), COALESCE(d.failed_deployments, 0), COALESCE(d.unplanned_fix_deployments, 0),
       d.median_lead_time_hours,
       COALESCE(i.incidents, 0), COALESCE(i.customer_impacting_incidents, 0), i.median_restore_hours,
       COALESCE(s.open_high_findings_over_30d, 0)
FROM k
LEFT JOIN d USING (team_id, week_start)
LEFT JOIN i USING (team_id, week_start)
LEFT JOIN s USING (team_id, week_start);

-- 3d. Copilot per team: seats, weekly active users, use, cost
DELETE FROM eng_metrics.team_week_copilot
WHERE week_start IN (SELECT week_start FROM eng_metrics.recent_weeks(4));

WITH w AS (SELECT week_start FROM eng_metrics.recent_weeks(4)),
usage AS (
  SELECT m.team_id, date_trunc('week', u.day)::date AS week_start,
         COUNT(DISTINCT u.user_login) FILTER (WHERE u.is_active) AS active_users,
         SUM(u.completions_shown)    AS completions_shown,
         SUM(u.completions_accepted) AS completions_accepted,
         SUM(u.chat_agent_requests)  AS chat_agent_requests
  FROM staging_restricted.copilot_user_daily u
  JOIN staging_restricted.team_membership m
    ON m.engineer_login = u.user_login
   AND u.day >= m.valid_from
   AND u.day <  COALESCE(m.valid_to, DATE '9999-12-31')
  WHERE u.day >= (SELECT MIN(week_start) FROM w)
    AND u.day <  (SELECT MAX(week_start) + 7 FROM w)
  GROUP BY 1, 2
),
seats AS (
  SELECT m.team_id, s.snapshot_date AS week_start,
         COUNT(*)                                  AS seats,
         SUM(s.seat_cost_eur_month) * 12 / 52.0    AS seat_cost_eur_week
  FROM staging_restricted.copilot_seats s
  JOIN w ON s.snapshot_date = w.week_start
  JOIN staging_restricted.team_membership m
    ON m.engineer_login = s.user_login
   AND s.snapshot_date >= m.valid_from
   AND s.snapshot_date <  COALESCE(m.valid_to, DATE '9999-12-31')
  GROUP BY 1, 2
)
INSERT INTO eng_metrics.team_week_copilot
SELECT COALESCE(s.team_id, u.team_id), COALESCE(s.week_start, u.week_start),
       COALESCE(s.seats, 0), COALESCE(s.seat_cost_eur_week, 0),
       COALESCE(u.active_users, 0), COALESCE(u.completions_shown, 0),
       COALESCE(u.completions_accepted, 0), COALESCE(u.chat_agent_requests, 0)
FROM seats s
FULL OUTER JOIN usage u
  ON u.team_id = s.team_id AND u.week_start = s.week_start;

-- 3e. Organisation-wide Copilot licences: where seat money goes unused
DELETE FROM eng_metrics.org_week_copilot_licences
WHERE week_start IN (SELECT week_start FROM eng_metrics.recent_weeks(4));

WITH seat AS (
  SELECT s.snapshot_date, s.seat_cost_eur_month,
         (s.last_activity_at IS NULL OR s.last_activity_at < s.snapshot_date - 30) AS idle_30d,
         NOT EXISTS (
           SELECT 1 FROM staging_restricted.team_membership m
           WHERE m.engineer_login = s.user_login
             AND s.snapshot_date >= m.valid_from
             AND s.snapshot_date <  COALESCE(m.valid_to, DATE '9999-12-31')
         ) AS without_team
  FROM staging_restricted.copilot_seats s
  WHERE s.snapshot_date IN (SELECT week_start FROM eng_metrics.recent_weeks(4))
)
INSERT INTO eng_metrics.org_week_copilot_licences
SELECT snapshot_date,
       COUNT(*),
       COUNT(*) FILTER (WHERE NOT idle_30d),
       COUNT(*) FILTER (WHERE idle_30d),
       COUNT(*) FILTER (WHERE without_team),
       ROUND(SUM(seat_cost_eur_month), 2),
       ROUND(COALESCE(SUM(seat_cost_eur_month) FILTER (WHERE idle_30d), 0), 2)
FROM seat
GROUP BY snapshot_date;

-- 3f. On-call load per team
DELETE FROM eng_metrics.team_week_oncall
WHERE week_start IN (SELECT week_start FROM eng_metrics.recent_weeks(4));

INSERT INTO eng_metrics.team_week_oncall
SELECT team_id, date_trunc('week', paged_at)::date,
       COUNT(*), COUNT(*) FILTER (WHERE out_of_hours)
FROM ops.oncall_pages
WHERE paged_at >= (SELECT MIN(week_start) FROM eng_metrics.recent_weeks(4))
  AND paged_at <  (SELECT MAX(week_start) + 7 FROM eng_metrics.recent_weeks(4))
GROUP BY 1, 2;

-- 3g. Retention: person-linked rows are deleted once aggregated
DELETE FROM staging_restricted.copilot_user_daily WHERE day < CURRENT_DATE - 35;
DELETE FROM staging_restricted.copilot_seats      WHERE snapshot_date < CURRENT_DATE - 35;
DELETE FROM staging_restricted.github_pull_requests
WHERE COALESCE(merged_at, closed_at) < CURRENT_DATE - 90;   -- open PRs are kept for the waiting count

COMMIT;


-- 4. Views ----------------------------------------------------------------------
-- 4a. Internal base view: all teams, all weeks. Not granted to readers.
CREATE OR REPLACE VIEW eng_metrics.v_team_week_base AS
SELECT s.team_id, s.week_start, s.members,
       f.prs_merged, f.median_cycle_hours, f.p85_cycle_hours, f.median_first_review_wait_hours,
       f.median_pr_lines, f.share_prs_over_400_lines, f.share_merged_without_review,
       f.open_prs_older_than_7d,
       d.deployments, d.failed_deployments, d.unplanned_fix_deployments, d.median_lead_time_hours,
       d.incidents, d.customer_impacting_incidents, d.median_restore_hours, d.open_high_findings_over_30d,
       c.seats, c.seat_cost_eur_week, c.active_users, c.completions_shown, c.completions_accepted,
       c.chat_agent_requests,
       o.pages_total, o.pages_out_of_hours
FROM eng_metrics.team_week_size s
LEFT JOIN eng_metrics.team_week_flow     f USING (team_id, week_start)
LEFT JOIN eng_metrics.team_week_delivery d USING (team_id, week_start)
LEFT JOIN eng_metrics.team_week_copilot  c USING (team_id, week_start)
LEFT JOIN eng_metrics.team_week_oncall   o USING (team_id, week_start);

-- 4b. Team dashboard: last 4 weeks against the team's own previous 12 weeks.
-- Medians are averaged over weeks ("average of weekly medians").
-- Rates are computed from summed counts, so a quiet week doesn't swing them.
CREATE OR REPLACE VIEW eng_metrics.v_team_dashboard AS
WITH rolled AS (
  SELECT team_id, week_start, members,
         COUNT(*) OVER prior12 AS baseline_weeks,

         -- Delivery
         AVG(COALESCE(deployments, 0)) OVER last4   AS deploys_per_week_4w,
         AVG(COALESCE(deployments, 0)) OVER prior12 AS deploys_per_week_base,
         AVG(median_lead_time_hours) OVER last4     AS lead_time_hours_4w,
         AVG(median_lead_time_hours) OVER prior12   AS lead_time_hours_base,
         SUM(failed_deployments::numeric) OVER last4   / NULLIF(SUM(deployments) OVER last4, 0)   AS change_fail_rate_4w,
         SUM(failed_deployments::numeric) OVER prior12 / NULLIF(SUM(deployments) OVER prior12, 0) AS change_fail_rate_base,
         SUM(unplanned_fix_deployments::numeric) OVER last4 / NULLIF(SUM(deployments) OVER last4, 0) AS rework_rate_4w,
         AVG(median_restore_hours) OVER last4       AS restore_hours_4w,

         -- Flow
         AVG(median_cycle_hours) OVER last4                AS cycle_hours_4w,
         AVG(median_cycle_hours) OVER prior12              AS cycle_hours_base,
         AVG(median_first_review_wait_hours) OVER last4    AS review_wait_hours_4w,
         AVG(median_first_review_wait_hours) OVER prior12  AS review_wait_hours_base,
         AVG(median_pr_lines) OVER last4                   AS pr_lines_4w,
         AVG(median_pr_lines) OVER prior12                 AS pr_lines_base,
         SUM(share_merged_without_review * prs_merged) OVER last4 / NULLIF(SUM(prs_merged) OVER last4, 0)
                                                           AS merged_without_review_4w,
         open_prs_older_than_7d,
         SUM(prs_merged) OVER last4                        AS prs_merged_4w,   -- sample size, not a target

         -- Quality and health
         SUM(COALESCE(customer_impacting_incidents, 0)) OVER last4   AS customer_incidents_4w,
         SUM(COALESCE(customer_impacting_incidents, 0)) OVER prior12 * 4.0 / NULLIF(COUNT(*) OVER prior12, 0)
                                                                     AS customer_incidents_base_per_4w,
         open_high_findings_over_30d,
         SUM(COALESCE(pages_out_of_hours, 0)) OVER last4             AS out_of_hours_pages_4w,

         -- Copilot (team level only)
         MIN(COALESCE(active_users, 0)) OVER last4                   AS min_active_users_4w,
         SUM(active_users::numeric) OVER last4 / NULLIF(SUM(seats) OVER last4, 0)            AS copilot_active_share_4w,
         SUM(completions_accepted::numeric) OVER last4 / NULLIF(SUM(completions_shown) OVER last4, 0)
                                                                     AS copilot_acceptance_4w,
         SUM(seat_cost_eur_week) OVER last4 / NULLIF(SUM(active_users) OVER last4, 0)        AS copilot_cost_per_active_user_week
  FROM eng_metrics.v_team_week_base
  WINDOW last4   AS (PARTITION BY team_id ORDER BY week_start ROWS BETWEEN 3 PRECEDING AND CURRENT ROW),
         prior12 AS (PARTITION BY team_id ORDER BY week_start ROWS BETWEEN 15 PRECEDING AND 4 PRECEDING)
)
SELECT team_id, week_start, members,
       baseline_weeks >= 8 AS baseline_ok,          -- trends need at least 8 baseline weeks

       ROUND(deploys_per_week_4w, 1)               AS deploys_per_week_4w,
       ROUND(deploys_per_week_base, 1)             AS deploys_per_week_base,
       ROUND(lead_time_hours_4w::numeric, 1)       AS lead_time_hours_4w,
       ROUND(lead_time_hours_base::numeric, 1)     AS lead_time_hours_base,
       ROUND(change_fail_rate_4w, 3)               AS change_fail_rate_4w,
       ROUND(change_fail_rate_base, 3)             AS change_fail_rate_base,
       ROUND(rework_rate_4w, 3)                    AS rework_rate_4w,
       ROUND(restore_hours_4w::numeric, 1)         AS restore_hours_4w,

       ROUND(cycle_hours_4w::numeric, 1)           AS cycle_hours_4w,
       ROUND(cycle_hours_base::numeric, 1)         AS cycle_hours_base,
       ROUND(100 * (cycle_hours_4w / NULLIF(cycle_hours_base, 0) - 1)::numeric, 0) AS cycle_change_pct,
       ROUND(review_wait_hours_4w::numeric, 1)     AS review_wait_hours_4w,
       ROUND(review_wait_hours_base::numeric, 1)   AS review_wait_hours_base,
       ROUND(pr_lines_4w::numeric, 0)              AS pr_lines_4w,
       ROUND(pr_lines_base::numeric, 0)            AS pr_lines_base,
       ROUND(merged_without_review_4w, 3)          AS merged_without_review_4w,
       open_prs_older_than_7d,
       prs_merged_4w,

       customer_incidents_4w,
       ROUND(customer_incidents_base_per_4w, 1)    AS customer_incidents_base_per_4w,
       open_high_findings_over_30d,
       out_of_hours_pages_4w,

       CASE WHEN min_active_users_4w >= 5 THEN ROUND(copilot_active_share_4w, 2) END          AS copilot_active_share_4w,
       CASE WHEN min_active_users_4w >= 5 THEN ROUND(copilot_acceptance_4w, 2) END            AS copilot_acceptance_4w,
       CASE WHEN min_active_users_4w >= 5 THEN ROUND(copilot_cost_per_active_user_week, 2) END AS copilot_cost_per_active_user_week
FROM rolled
WHERE members >= 5;

-- 4c. Organisation view for leadership: totals across all teams, no team names.
CREATE OR REPLACE VIEW eng_metrics.v_org_weekly AS
SELECT week_start,
       SUM(members)                                                          AS engineers_in_teams,
       SUM(COALESCE(deployments, 0))                                         AS deployments,
       ROUND(SUM(failed_deployments)::numeric / NULLIF(SUM(deployments), 0), 3) AS change_fail_rate,
       ROUND(SUM(unplanned_fix_deployments)::numeric / NULLIF(SUM(deployments), 0), 3) AS rework_rate,
       ROUND((percentile_cont(0.5) WITHIN GROUP (ORDER BY median_lead_time_hours))::numeric, 1)         AS median_team_lead_time_hours,
       ROUND((percentile_cont(0.5) WITHIN GROUP (ORDER BY median_cycle_hours))::numeric, 1)             AS median_team_cycle_hours,
       ROUND((percentile_cont(0.5) WITHIN GROUP (ORDER BY median_first_review_wait_hours))::numeric, 1) AS median_team_review_wait_hours,
       SUM(COALESCE(customer_impacting_incidents, 0))                        AS customer_impacting_incidents,
       SUM(COALESCE(open_high_findings_over_30d, 0))                         AS open_high_findings_over_30d,
       SUM(COALESCE(pages_out_of_hours, 0))                                  AS out_of_hours_pages,
       SUM(COALESCE(active_users, 0))                                        AS copilot_active_users,
       SUM(COALESCE(seats, 0))                                               AS copilot_seats_in_teams
FROM eng_metrics.v_team_week_base
GROUP BY week_start;


-- 5. Access ---------------------------------------------------------------------
-- Readers see team-week views only. Views run with their owner's rights, so
-- readers never need access to staging_restricted.
DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'eng_dashboard_reader') THEN
    CREATE ROLE eng_dashboard_reader NOLOGIN;
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'svc_eng_metrics_etl') THEN
    CREATE ROLE svc_eng_metrics_etl NOLOGIN;
  END IF;
END $$;

REVOKE ALL ON SCHEMA staging_restricted FROM PUBLIC;
REVOKE ALL ON ALL TABLES IN SCHEMA staging_restricted FROM PUBLIC;
GRANT USAGE ON SCHEMA staging_restricted, ops, eng_metrics TO svc_eng_metrics_etl;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA staging_restricted, eng_metrics TO svc_eng_metrics_etl;
GRANT SELECT ON ALL TABLES IN SCHEMA ops TO svc_eng_metrics_etl;

GRANT USAGE ON SCHEMA eng_metrics TO eng_dashboard_reader;
GRANT SELECT ON eng_metrics.v_team_dashboard,
                eng_metrics.v_org_weekly,
                eng_metrics.org_week_copilot_licences
             TO eng_dashboard_reader;


-- 6. Is Copilot paying off? Before/after with a comparison group ----------------
-- Fill eng_metrics.copilot_comparison_groups and copilot_comparison_settings
-- first: pilot teams got a change (Copilot, training, new review rules) on
-- change_date; comparison teams didn't. Uses 12 weeks either side. Read the
-- result as a direction, not proof: check team make-up and work type before
-- drawing conclusions.
CREATE OR REPLACE VIEW eng_metrics.v_copilot_comparison AS
WITH params AS (SELECT change_date FROM eng_metrics.copilot_comparison_settings),
obs AS (
  SELECT g.group_label,
         CASE WHEN b.week_start < p.change_date THEN 'before' ELSE 'after' END AS period,
         b.*
  FROM eng_metrics.v_team_week_base b
  JOIN eng_metrics.copilot_comparison_groups g USING (team_id)
  CROSS JOIN params p
  WHERE b.week_start >= p.change_date - 84
    AND b.week_start <  p.change_date + 84
    AND b.members >= 5
),
summary AS (
  SELECT group_label, period,
         COUNT(DISTINCT team_id)                                                AS teams,
         AVG(median_cycle_hours)::float8                                        AS cycle_hours,
         AVG(median_first_review_wait_hours)::float8                            AS review_wait_hours,
         AVG(median_pr_lines)::float8                                           AS pr_lines,
         AVG(median_lead_time_hours)::float8                                    AS lead_time_hours,
         (SUM(failed_deployments)::numeric / NULLIF(SUM(deployments), 0))::float8 AS change_fail_rate,
         (SUM(unplanned_fix_deployments)::numeric / NULLIF(SUM(deployments), 0))::float8 AS rework_rate,
         AVG(COALESCE(customer_impacting_incidents, 0))::float8                 AS customer_incidents_per_team_week
  FROM obs
  GROUP BY group_label, period
),
long AS (
  SELECT s.group_label, s.period, v.metric, v.value
  FROM summary s
  CROSS JOIN LATERAL (VALUES
    ('1 median cycle time, hours',            s.cycle_hours),
    ('2 median wait for first review, hours', s.review_wait_hours),
    ('3 median PR size, lines',               s.pr_lines),
    ('4 lead time to production, hours',      s.lead_time_hours),
    ('5 change fail rate',                    s.change_fail_rate),
    ('6 deployment rework rate',              s.rework_rate),
    ('7 customer incidents per team-week',    s.customer_incidents_per_team_week)
  ) AS v(metric, value)
)
SELECT metric,
       ROUND(MAX(value) FILTER (WHERE group_label = 'pilot'      AND period = 'before')::numeric, 3) AS pilot_before,
       ROUND(MAX(value) FILTER (WHERE group_label = 'pilot'      AND period = 'after')::numeric, 3)  AS pilot_after,
       ROUND(MAX(value) FILTER (WHERE group_label = 'comparison' AND period = 'before')::numeric, 3) AS comparison_before,
       ROUND(MAX(value) FILTER (WHERE group_label = 'comparison' AND period = 'after')::numeric, 3)  AS comparison_after,
       ROUND(( (MAX(value) FILTER (WHERE group_label = 'pilot'      AND period = 'after')
              - MAX(value) FILTER (WHERE group_label = 'pilot'      AND period = 'before'))
             - (MAX(value) FILTER (WHERE group_label = 'comparison' AND period = 'after')
              - MAX(value) FILTER (WHERE group_label = 'comparison' AND period = 'before')) )::numeric, 3)
                                                                                                     AS difference_in_differences
FROM long
GROUP BY metric
ORDER BY metric;

GRANT SELECT ON eng_metrics.v_copilot_comparison TO eng_dashboard_reader;


-- 7. Porting notes -----------------------------------------------------------------
-- Snowflake: replace FILTER (WHERE x) with COUNT_IF(x) / SUM(IFF(x, v, NULL));
--   recent_weeks() becomes a calendar table or GENERATOR; date + 7 becomes DATEADD(day, 7, d);
--   EXTRACT(EPOCH FROM a - b) becomes DATEDIFF(second, b, a). percentile_cont ... WITHIN GROUP works.
-- BigQuery: DATE_TRUNC(d, WEEK(MONDAY)); TIMESTAMP_DIFF(a, b, SECOND); medians via
--   APPROX_QUANTILES(x, 100)[OFFSET(50)]; COUNTIF(x) for filtered counts; no ON CONFLICT needed.
