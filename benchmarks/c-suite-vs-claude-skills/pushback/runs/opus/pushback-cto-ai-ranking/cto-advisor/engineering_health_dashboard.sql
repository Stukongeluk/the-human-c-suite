-- =====================================================================
-- Engineering health dashboard: weekly, team level        (PostgreSQL 16)
-- ---------------------------------------------------------------------
-- What it is:     one weekly row per team covering delivery (DORA), PR
--                 flow, Copilot adoption and quality guardrails, plus a
--                 "where to look this week" view that compares each team
--                 with its own baseline.
-- What it is not: a ranking of people. No view in schema rpt exposes a
--                 person. Per-person Copilot rows sit in a restricted
--                 landing schema for at most 35 days and are aggregated
--                 to team level. Any number that would describe fewer
--                 than 5 people is suppressed.
-- Before go-live: works council (OR) consent under WOR art. 27(1)(k)/(l)
--                 and a DPIA. See engineering-health-dashboard.md.
--
-- Run order: sections 0-5 once (all idempotent), then on a schedule:
--   daily   : load the source tables (section 1) from GitHub, CI/CD,
--             the incident tool and GitHub's per-user Copilot report
--   Thursday: CALL copilot.refresh_group_week();
-- The dashboard tool reads only rpt.v_engineering_health_weekly and
-- rpt.v_engineering_health_attention, as role eng_dashboard_reader.
-- =====================================================================


-- ---------------------------------------------------------------------
-- 0. Schemas and the group-size threshold
-- ---------------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS org;          -- teams and membership (HR / identity provider)
CREATE SCHEMA IF NOT EXISTS gh;           -- GitHub pull requests
CREATE SCHEMA IF NOT EXISTS cd;           -- services and deployments (CI/CD)
CREATE SCHEMA IF NOT EXISTS ops;          -- incidents (ServiceNow, PagerDuty, Opsgenie ...)
CREATE SCHEMA IF NOT EXISTS copilot_raw;  -- RESTRICTED: per-user Copilot landing, 35-day retention
CREATE SCHEMA IF NOT EXISTS copilot;      -- team-level Copilot aggregates (the only Copilot data kept)
CREATE SCHEMA IF NOT EXISTS stg;          -- RESTRICTED: event views that still carry a GitHub login
CREATE SCHEMA IF NOT EXISTS rpt;          -- what the dashboard reads: team level only

-- Smallest number of people any reported figure may describe.
CREATE OR REPLACE FUNCTION rpt.k_min() RETURNS int
LANGUAGE sql IMMUTABLE AS $$ SELECT 5 $$;


-- ---------------------------------------------------------------------
-- 1. Source tables (loaded by your ingestion jobs)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS org.team (
  team_id         text PRIMARY KEY,
  team_name       text NOT NULL,
  value_stream    text NOT NULL,
  -- The unit the dashboard reports on. Normally the team name. Give two or
  -- more small teams (under 5 people) one shared value so they are reported
  -- together instead of being suppressed.
  reporting_group text NOT NULL
);

CREATE TABLE IF NOT EXISTS org.team_membership (
  github_login text         NOT NULL,
  team_id      text         NOT NULL REFERENCES org.team,
  fte          numeric(3,2) NOT NULL CHECK (fte > 0 AND fte <= 1),  -- only ever summed per team
  valid_from   date         NOT NULL,
  valid_to     date,                                                -- NULL = current
  PRIMARY KEY (github_login, valid_from)
);

CREATE TABLE IF NOT EXISTS gh.pull_request (
  pr_id           bigint      PRIMARY KEY,
  repo            text        NOT NULL,
  author_login    text        NOT NULL,
  created_at      timestamptz NOT NULL,
  first_review_at timestamptz,
  merged_at       timestamptz,
  additions       int         NOT NULL DEFAULT 0,
  deletions       int         NOT NULL DEFAULT 0,
  is_revert       boolean     NOT NULL DEFAULT false,
  is_bot          boolean     NOT NULL DEFAULT false   -- Dependabot, Renovate, automation accounts
);

CREATE TABLE IF NOT EXISTS cd.service (
  service_id    text PRIMARY KEY,
  owner_team_id text NOT NULL REFERENCES org.team
);

CREATE TABLE IF NOT EXISTS cd.deployment (
  deployment_id    bigint      PRIMARY KEY,
  service_id       text        NOT NULL REFERENCES cd.service,
  environment      text        NOT NULL,
  finished_at      timestamptz NOT NULL,
  status           text        NOT NULL CHECK (status IN ('success', 'failed', 'rolled_back')),
  oldest_commit_at timestamptz          -- earliest commit first shipped by this deployment
);

CREATE TABLE IF NOT EXISTS ops.incident (
  incident_id             text        PRIMARY KEY,
  service_id              text        NOT NULL REFERENCES cd.service,
  severity                int         NOT NULL,   -- 1 = most severe
  started_at              timestamptz NOT NULL,
  resolved_at             timestamptz,
  caused_by_deployment_id bigint      REFERENCES cd.deployment
);

-- Landing table for GitHub's per-user daily Copilot usage report
-- ("users-1-day"). Column names follow GitHub's report fields. Only the
-- pipeline's service account can read this schema.
CREATE TABLE IF NOT EXISTS copilot_raw.user_day (
  day                              date        NOT NULL,
  user_login                       text        NOT NULL,
  user_initiated_interaction_count int,
  code_generation_activity_count   int,
  code_acceptance_activity_count   int,
  used_agent                       boolean,
  used_chat                        boolean,
  client_telemetry_present         boolean,
  loaded_at                        timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (day, user_login)
);

-- Team-week Copilot aggregates: the only Copilot data that is kept.
CREATE TABLE IF NOT EXISTS copilot.group_week (
  week_start          date    NOT NULL,   -- Monday
  reporting_group     text    NOT NULL,
  active_users        int     NOT NULL,
  chat_or_agent_users int,                -- NULL when active_users < k
  generations         bigint,             -- NULL when active_users < k
  acceptances         bigint,             -- NULL when active_users < k
  telemetry_coverage  numeric,            -- share of active users whose IDE sent telemetry all week
  PRIMARY KEY (week_start, reporting_group)
);


-- ---------------------------------------------------------------------
-- 2. Restricted event views (still carry a login; never exposed)
-- ---------------------------------------------------------------------
CREATE OR REPLACE FUNCTION stg.local_day(ts timestamptz) RETURNS date
LANGUAGE sql STABLE AS $$ SELECT (ts AT TIME ZONE 'Europe/Amsterdam')::date $$;

-- Which reporting group a person belonged to on a given day.
CREATE OR REPLACE VIEW stg.v_membership AS
SELECT m.github_login,
       m.fte,
       m.valid_from,
       coalesce(m.valid_to, 'infinity'::date) AS valid_to,
       t.team_id,
       t.reporting_group
FROM org.team_membership m
JOIN org.team t USING (team_id);

-- One row per merged, human-authored PR, attributed to the author's
-- reporting group on the day it merged.
CREATE OR REPLACE VIEW stg.v_pr_event AS
SELECT p.pr_id,
       m.reporting_group,
       p.author_login,                                                  -- used only for the k count
       stg.local_day(p.merged_at)                                       AS local_day,
       extract(epoch FROM p.merged_at - p.created_at) / 3600.0          AS cycle_hours,
       extract(epoch FROM p.first_review_at - p.created_at) / 3600.0    AS first_review_hours,
       p.additions + p.deletions                                        AS size_lines,
       p.is_revert
FROM gh.pull_request p
JOIN stg.v_membership m
  ON m.github_login = p.author_login
 AND stg.local_day(p.merged_at) BETWEEN m.valid_from AND m.valid_to
WHERE p.merged_at IS NOT NULL
  AND NOT p.is_bot;

-- One row per production change that reached users, attributed to the
-- team that owns the service.
CREATE OR REPLACE VIEW stg.v_deploy_event AS
SELECT d.deployment_id,
       t.reporting_group,
       stg.local_day(d.finished_at)                                     AS local_day,
       extract(epoch FROM d.finished_at - d.oldest_commit_at) / 3600.0  AS lead_time_hours,
       (d.status = 'rolled_back'
        OR EXISTS (SELECT 1 FROM ops.incident i
                   WHERE i.caused_by_deployment_id = d.deployment_id))  AS caused_failure
FROM cd.deployment d
JOIN cd.service s USING (service_id)
JOIN org.team t ON t.team_id = s.owner_team_id
WHERE d.environment = 'production'
  AND d.status IN ('success', 'rolled_back');  -- a deploy that never went live is not a change failure

-- Resolved incidents on services the team owns. Open incidents are left
-- out of time-to-restore until they close.
CREATE OR REPLACE VIEW stg.v_incident_event AS
SELECT i.incident_id,
       t.reporting_group,
       i.severity,
       stg.local_day(i.started_at)                                      AS local_day,
       extract(epoch FROM i.resolved_at - i.started_at) / 3600.0        AS restore_hours
FROM ops.incident i
JOIN cd.service s USING (service_id)
JOIN org.team t ON t.team_id = s.owner_team_id
WHERE i.resolved_at IS NOT NULL;


-- ---------------------------------------------------------------------
-- 3. Copilot: per-user rows in, team-week aggregates out
-- ---------------------------------------------------------------------
-- Note: GitHub's per-user report has no acceptance-rate field. The ratio
-- below is acceptances / generations summed over the whole team. It mixes
-- inline completions and chat code blocks, and users whose IDE telemetry
-- is off are missing from it, hence telemetry_coverage.
CREATE OR REPLACE VIEW copilot_raw.v_group_week AS
WITH per_user_week AS (
  SELECT date_trunc('week', r.day)::date                                 AS week_start,
         m.reporting_group,
         r.user_login,
         sum(coalesce(r.code_generation_activity_count, 0))              AS generations,
         sum(coalesce(r.code_acceptance_activity_count, 0))              AS acceptances,
         bool_or(coalesce(r.used_agent, false) OR coalesce(r.used_chat, false)) AS used_chat_or_agent,
         bool_and(coalesce(r.client_telemetry_present, false))           AS telemetry_all_week,
         sum(coalesce(r.user_initiated_interaction_count, 0)
           + coalesce(r.code_generation_activity_count, 0)) > 0          AS active
  FROM copilot_raw.user_day r
  JOIN stg.v_membership m
    ON m.github_login = r.user_login
   AND r.day BETWEEN m.valid_from AND m.valid_to
  GROUP BY 1, 2, 3
), g AS (
  SELECT week_start,
         reporting_group,
         count(*) FILTER (WHERE active)                                  AS active_users,
         count(*) FILTER (WHERE active AND used_chat_or_agent)           AS chat_or_agent_users,
         sum(generations) FILTER (WHERE active)                          AS generations,
         sum(acceptances) FILTER (WHERE active)                          AS acceptances,
         avg(telemetry_all_week::int) FILTER (WHERE active)              AS telemetry_coverage
  FROM per_user_week
  GROUP BY 1, 2
)
SELECT week_start,
       reporting_group,
       active_users,
       CASE WHEN active_users >= rpt.k_min() THEN chat_or_agent_users END AS chat_or_agent_users,
       CASE WHEN active_users >= rpt.k_min() THEN generations         END AS generations,
       CASE WHEN active_users >= rpt.k_min() THEN acceptances         END AS acceptances,
       CASE WHEN active_users >= rpt.k_min() THEN telemetry_coverage  END AS telemetry_coverage
FROM g;

-- Weekly job (Thursday). GitHub finalises IDE telemetry within three full
-- UTC days, so only weeks that ended at least four days ago are written,
-- and only weeks still fully inside the 35-day raw retention.
CREATE OR REPLACE PROCEDURE copilot.refresh_group_week()
LANGUAGE plpgsql AS $$
BEGIN
  INSERT INTO copilot.group_week AS gw
         (week_start, reporting_group, active_users, chat_or_agent_users,
          generations, acceptances, telemetry_coverage)
  SELECT week_start, reporting_group, active_users, chat_or_agent_users,
         generations, acceptances, telemetry_coverage
  FROM copilot_raw.v_group_week
  WHERE week_start + 10 <= current_date
    AND week_start      >= current_date - 35
  ON CONFLICT (week_start, reporting_group) DO UPDATE
     SET active_users        = EXCLUDED.active_users,
         chat_or_agent_users = EXCLUDED.chat_or_agent_users,
         generations         = EXCLUDED.generations,
         acceptances         = EXCLUDED.acceptances,
         telemetry_coverage  = EXCLUDED.telemetry_coverage;

  -- Per-person rows are kept no longer than re-aggregation needs.
  DELETE FROM copilot_raw.user_day WHERE day < current_date - 35;
END $$;

-- One-off backfill at go-live, for whatever history GitHub still serves:
--   INSERT INTO copilot.group_week
--   SELECT * FROM copilot_raw.v_group_week WHERE week_start + 10 <= current_date
--   ON CONFLICT DO NOTHING;


-- ---------------------------------------------------------------------
-- 4. Dashboard views (team level only)
-- ---------------------------------------------------------------------
-- The last 26 completed weeks (Monday dates).
CREATE OR REPLACE VIEW rpt.v_week AS
SELECT gs::date AS week_start
FROM generate_series((date_trunc('week', current_date)::date - 7 * 26)::timestamp,
                     (date_trunc('week', current_date)::date - 7)::timestamp,
                     interval '1 week') AS gs;

-- One row per reporting group per week. Every metric is a rolling 4-week
-- window ending with the week shown: refreshed weekly, but steady enough
-- that one holiday, one sick week or one incident does not swing it.
-- Rows for groups under k people come back with suppressed = true and no
-- metrics. Sort by team name, not by any metric.
CREATE OR REPLACE VIEW rpt.v_engineering_health_weekly AS
WITH roster AS (
  SELECT w.week_start,
         m.reporting_group,
         count(DISTINCT m.github_login) AS members,
         sum(m.fte)                     AS fte
  FROM rpt.v_week w
  JOIN stg.v_membership m
    ON w.week_start + 3 BETWEEN m.valid_from AND m.valid_to     -- membership on the Thursday
  GROUP BY 1, 2
),
delivery AS (
  SELECT w.week_start,
         e.reporting_group,
         count(*) / 4.0                                                    AS deploys_per_week,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY e.lead_time_hours)    AS median_lead_time_hours,
         avg(e.caused_failure::int)                                        AS change_failure_rate
  FROM rpt.v_week w
  JOIN stg.v_deploy_event e ON e.local_day BETWEEN w.week_start - 21 AND w.week_start + 6
  GROUP BY 1, 2
),
restore AS (
  SELECT w.week_start,
         e.reporting_group,
         count(*)                                                          AS sev12_incidents,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY e.restore_hours)      AS median_restore_hours
  FROM rpt.v_week w
  JOIN stg.v_incident_event e ON e.local_day BETWEEN w.week_start - 21 AND w.week_start + 6
  WHERE e.severity <= 2
  GROUP BY 1, 2
),
flow AS (
  SELECT w.week_start,
         e.reporting_group,
         count(DISTINCT e.author_login)                                    AS contributors,
         count(*)                                                          AS merged_prs,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY e.cycle_hours)        AS median_cycle_hours,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY e.first_review_hours) AS median_first_review_hours,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY e.size_lines)         AS median_pr_size_lines,
         avg((e.size_lines > 400)::int)                                    AS share_prs_over_400_lines,
         avg(e.is_revert::int)                                             AS revert_share
  FROM rpt.v_week w
  JOIN stg.v_pr_event e ON e.local_day BETWEEN w.week_start - 21 AND w.week_start + 6
  GROUP BY 1, 2
),
ai AS (
  SELECT w.week_start,
         c.reporting_group,
         avg(c.active_users)                                               AS avg_active_users,
         sum(c.chat_or_agent_users)::numeric
           / nullif(sum(c.active_users) FILTER (WHERE c.chat_or_agent_users IS NOT NULL), 0)
                                                                           AS chat_or_agent_share,
         sum(c.acceptances)::numeric / nullif(sum(c.generations), 0)       AS accept_ratio,
         avg(c.telemetry_coverage)                                         AS telemetry_coverage
  FROM rpt.v_week w
  JOIN copilot.group_week c ON c.week_start BETWEEN w.week_start - 21 AND w.week_start
  GROUP BY 1, 2
)
SELECT r.week_start                                                AS week_starting,
       r.reporting_group                                           AS team,
       r.members,
       round(r.fte, 1)                                             AS fte,
       (r.members < rpt.k_min())                                   AS suppressed,
       -- Delivery (DORA), for the services the team owns
       round(d.deploys_per_week, 1)                                AS deploys_per_week,
       round(d.median_lead_time_hours::numeric, 1)                 AS median_lead_time_hours,
       round(d.change_failure_rate, 3)                             AS change_failure_rate,
       x.sev12_incidents,
       round(x.median_restore_hours::numeric, 1)                   AS median_restore_hours_sev12,
       -- PR flow: only when at least k people contributed in the window.
       -- Throughput is context for the flow numbers, never a target.
       round(f.merged_prs / 4.0 / nullif(r.fte, 0), 2)             AS merged_prs_per_fte_week,
       round(f.median_cycle_hours::numeric, 1)                     AS median_pr_cycle_hours,
       round(f.median_first_review_hours::numeric, 1)              AS median_hours_to_first_review,
       round(f.median_pr_size_lines::numeric, 0)                   AS median_pr_size_lines,
       round(f.share_prs_over_400_lines, 3)                        AS share_prs_over_400_lines,
       round(f.revert_share, 3)                                    AS revert_share,
       -- Copilot: adoption and use, at team level
       round(a.avg_active_users / r.members, 3)                    AS copilot_active_share,
       round(a.chat_or_agent_share, 3)                             AS copilot_chat_or_agent_share,
       round(a.accept_ratio, 3)                                    AS copilot_accept_ratio,
       round(a.telemetry_coverage, 3)                              AS copilot_telemetry_coverage
FROM roster r
LEFT JOIN delivery d
       ON d.week_start = r.week_start AND d.reporting_group = r.reporting_group
      AND r.members >= rpt.k_min()
LEFT JOIN restore x
       ON x.week_start = r.week_start AND x.reporting_group = r.reporting_group
      AND r.members >= rpt.k_min()
LEFT JOIN flow f
       ON f.week_start = r.week_start AND f.reporting_group = r.reporting_group
      AND r.members >= rpt.k_min() AND f.contributors >= rpt.k_min()
LEFT JOIN ai a
       ON a.week_start = r.week_start AND a.reporting_group = r.reporting_group
      AND r.members >= rpt.k_min();

-- "Where to look this week": for the latest completed week, the signals
-- that moved against the team's own baseline (weeks 4 to 16 before, so the
-- baseline does not overlap the current 4-week window) or crossed a fixed
-- guardrail. These are prompts for a conversation with the team about the
-- system they work in. They are not grades and not inputs to anyone's
-- performance review.
CREATE OR REPLACE VIEW rpt.v_engineering_health_attention AS
WITH latest AS (
  SELECT max(week_start) AS wk FROM rpt.v_week
),
cur AS (
  SELECT h.*
  FROM rpt.v_engineering_health_weekly h, latest
  WHERE h.week_starting = latest.wk AND NOT h.suppressed
),
base AS (
  SELECT h.team,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY h.median_lead_time_hours)       AS lead_time_base,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY h.change_failure_rate)          AS cfr_base,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY h.median_hours_to_first_review) AS review_wait_base,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY h.copilot_accept_ratio)         AS accept_base
  FROM rpt.v_engineering_health_weekly h, latest
  WHERE h.week_starting BETWEEN latest.wk - 7 * 16 AND latest.wk - 7 * 4
    AND NOT h.suppressed
  GROUP BY h.team
)
SELECT c.week_starting,
       c.team,
       f.signal,
       f.detail
FROM cur c
LEFT JOIN base b USING (team)
CROSS JOIN LATERAL (VALUES
  ('Lead time up more than 25% vs own baseline',
   c.median_lead_time_hours > 1.25 * b.lead_time_base,
   format('%s h now, baseline %s h', c.median_lead_time_hours, round(b.lead_time_base::numeric, 1))),
  ('Change failure rate above 15%',
   c.change_failure_rate > 0.15,
   format('%s%% of production changes caused a rollback or incident', round(100 * c.change_failure_rate, 1))),
  ('Change failure rate up vs own baseline',
   c.change_failure_rate > 0.05 AND c.change_failure_rate > 1.5 * b.cfr_base,
   format('%s%% now, baseline %s%%', round(100 * c.change_failure_rate, 1), round(100 * b.cfr_base::numeric, 1))),
  ('PRs wait more than a day for first review',
   c.median_hours_to_first_review > 24,
   format('median %s h to first review (baseline %s h)', c.median_hours_to_first_review, round(b.review_wait_base::numeric, 1))),
  ('Large PRs: over 30% exceed 400 changed lines',
   c.share_prs_over_400_lines > 0.30,
   format('%s%% of merged PRs', round(100 * c.share_prs_over_400_lines, 1))),
  ('Copilot acceptance up while stability got worse: look at how AI-written code is reviewed',
   c.copilot_accept_ratio > 1.2 * b.accept_base AND c.change_failure_rate > b.cfr_base,
   format('accept ratio %s (baseline %s), change failure %s%% (baseline %s%%)',
          c.copilot_accept_ratio, round(b.accept_base::numeric, 3),
          round(100 * c.change_failure_rate, 1), round(100 * b.cfr_base::numeric, 1))),
  ('Copilot figures incomplete: under 80% of users send IDE telemetry',
   c.copilot_telemetry_coverage < 0.80,
   format('%s%% coverage', round(100 * c.copilot_telemetry_coverage, 1)))
) AS f(signal, raised, detail)
WHERE f.raised;


-- ---------------------------------------------------------------------
-- 5. Access: the dashboard sees team-level views and nothing else
-- ---------------------------------------------------------------------
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'eng_dashboard_reader') THEN
    CREATE ROLE eng_dashboard_reader NOLOGIN;
  END IF;
END $$;

GRANT USAGE  ON SCHEMA rpt TO eng_dashboard_reader;
GRANT SELECT ON rpt.v_engineering_health_weekly,
                rpt.v_engineering_health_attention TO eng_dashboard_reader;
-- No grants on org, gh, cd, ops, stg, copilot or copilot_raw. Views run
-- with their owner's rights, so the reader gets aggregates only. Give
-- copilot_raw to the ingestion service account alone, and log access to it.
