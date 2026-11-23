-- =====================================================================
-- Engineer ranking dashboard: Copilot acceptance rate + merged PRs
-- PostgreSQL 16                     Spec: engineer-ranking-dashboard-spec.md
-- ---------------------------------------------------------------------
-- Weekly snapshot ranking every in-scope engineer on a composite of
--   (a) merged PRs per available working day, and
--   (b) Copilot acceptance rate (acceptances / generations),
-- each converted to a percentile within the peer group, then weighted.
-- The bottom share (default 10%) is flagged for manager review; a
-- manager records the PIP decision in pip.manager_review.
--
-- Main view (perf.v_ranking_anon) is anonymised: engineer codes, no names,
-- teams or absence data. Names come from perf.v_engineer_names, which the
-- database only fills for an engineer's own manager and for CTO/HR.
--
-- Run order: sections 0-8 once (idempotent). Then:
--   daily    : load org.*, gh.*, copilot_raw.user_day
--   Thursday : CALL perf.take_snapshot();   -- previous Mon-Sun week
--   Friday   : managers record decisions on perf.v_my_review_queue
-- =====================================================================


-- ---------------------------------------------------------------------
-- 0. Schemas
-- ---------------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS org;          -- engineers, availability (HR export)
CREATE SCHEMA IF NOT EXISTS gh;           -- GitHub PRs and reviews
CREATE SCHEMA IF NOT EXISTS copilot_raw;  -- GitHub per-user Copilot report (users-1-day)
CREATE SCHEMA IF NOT EXISTS perf;         -- settings, snapshots, dashboard views
CREATE SCHEMA IF NOT EXISTS pip;          -- manager decisions and PIP enrolments


-- ---------------------------------------------------------------------
-- 1. Settings (one row; change values here, not in the SQL)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS perf.settings (
  id                      boolean PRIMARY KEY DEFAULT true CHECK (id),
  window_weeks            int     NOT NULL DEFAULT 4    CHECK (window_weeks BETWEEN 1 AND 13),
  bottom_share            numeric NOT NULL DEFAULT 0.10 CHECK (bottom_share > 0 AND bottom_share < 0.5),
  weight_merged_prs       numeric NOT NULL DEFAULT 0.5  CHECK (weight_merged_prs BETWEEN 0 AND 1),
  weight_copilot          numeric NOT NULL DEFAULT 0.5  CHECK (weight_copilot BETWEEN 0 AND 1),
  rank_within             text    NOT NULL DEFAULT 'job_level' CHECK (rank_within IN ('job_level', 'org')),
  min_peer_group_size     int     NOT NULL DEFAULT 10,   -- smaller peer groups are not ranked
  min_available_share     numeric NOT NULL DEFAULT 0.5,  -- must be available >= 50% of contracted days
  min_copilot_generations int     NOT NULL DEFAULT 50,   -- per window
  new_joiner_days         int     NOT NULL DEFAULT 90,
  raw_retention_days      int     NOT NULL DEFAULT 120,  -- copilot_raw.user_day
  CHECK (weight_merged_prs + weight_copilot = 1)
);
-- Who can open names on the anonymised main view (section 8):
--   own_reports  : a manager sees names of their own reports only
--   all_managers : any manager sees every name
ALTER TABLE perf.settings ADD COLUMN IF NOT EXISTS
  names_visible_to text NOT NULL DEFAULT 'own_reports'
  CHECK (names_visible_to IN ('own_reports', 'all_managers'));
INSERT INTO perf.settings DEFAULT VALUES ON CONFLICT DO NOTHING;


-- ---------------------------------------------------------------------
-- 2. Source tables
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS org.engineer (
  github_login    text         PRIMARY KEY,
  employee_id     text         NOT NULL UNIQUE,
  display_name    text         NOT NULL,
  team            text         NOT NULL,
  job_level       text         NOT NULL,           -- e.g. Medior, Senior, Staff
  manager_db_user text,                            -- database login of the line manager
  fte             numeric(3,2) NOT NULL CHECK (fte > 0 AND fte <= 1),
  start_date      date         NOT NULL,
  end_date        date,
  in_scope        boolean      NOT NULL DEFAULT true   -- false: managers, contractors, etc.
);

-- One row per weekday a person was not available: leave, sickness,
-- parental leave, training, public holiday. The reason is not needed and
-- is not stored.
CREATE TABLE IF NOT EXISTS org.unavailable_day (
  github_login text NOT NULL REFERENCES org.engineer,
  day          date NOT NULL,
  PRIMARY KEY (github_login, day)
);

CREATE TABLE IF NOT EXISTS gh.pull_request (
  pr_id        bigint      PRIMARY KEY,
  repo         text        NOT NULL,
  author_login text        NOT NULL,
  created_at   timestamptz NOT NULL,
  merged_at    timestamptz,
  is_bot       boolean     NOT NULL DEFAULT false   -- Dependabot, Renovate, automation accounts
);

CREATE TABLE IF NOT EXISTS gh.pr_review (
  pr_id          bigint      NOT NULL REFERENCES gh.pull_request,
  reviewer_login text        NOT NULL,
  submitted_at   timestamptz NOT NULL,
  state          text        NOT NULL               -- APPROVED, CHANGES_REQUESTED, COMMENTED
);
CREATE INDEX IF NOT EXISTS pr_review_reviewer_idx ON gh.pr_review (reviewer_login, submitted_at);
CREATE INDEX IF NOT EXISTS pull_request_merged_idx ON gh.pull_request (merged_at);

-- GitHub per-user daily Copilot usage report. Column names follow GitHub's
-- report fields. There is no per-user acceptance-rate field; it is derived
-- below as acceptances / generations.
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


-- ---------------------------------------------------------------------
-- 3. PIP workflow tables
-- ---------------------------------------------------------------------
-- The manager's decision on each flagged engineer, per snapshot week.
CREATE TABLE IF NOT EXISTS pip.manager_review (
  github_login text        NOT NULL REFERENCES org.engineer,
  week_start   date        NOT NULL,
  decision     text        NOT NULL CHECK (decision IN ('start_pip', 'no_pip')),
  reason       text        NOT NULL CHECK (length(trim(reason)) >= 20),
  decided_by   text        NOT NULL DEFAULT current_user,
  decided_at   timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (github_login, week_start)
);

CREATE TABLE IF NOT EXISTS pip.enrolment (
  github_login text NOT NULL REFERENCES org.engineer,
  started_on   date NOT NULL,
  ended_on     date,
  outcome      text CHECK (outcome IN ('met_goals', 'extended', 'ended_other')),
  decided_by   text NOT NULL DEFAULT current_user,
  PRIMARY KEY (github_login, started_on)
);


-- ---------------------------------------------------------------------
-- 4. Ranking for one week (window ends on Sunday of p_week)
-- ---------------------------------------------------------------------
CREATE OR REPLACE FUNCTION perf.compute_ranking(p_week date)
RETURNS TABLE (
  github_login                 text,
  display_name                 text,
  team                         text,
  job_level                    text,
  manager_db_user              text,
  window_start                 date,
  window_end                   date,
  available_days               numeric,
  merged_prs                   int,
  merged_prs_per_available_day numeric,
  reviews_given                int,
  copilot_generations          bigint,
  copilot_acceptances          bigint,
  copilot_acceptance_rate      numeric,
  status                       text,
  peer_group                   text,
  peer_group_size              int,
  pct_merged_prs               numeric,
  pct_copilot                  numeric,
  composite_score              numeric,
  rank_from_top                int,
  in_bottom                    boolean,
  on_active_pip                boolean,
  new_pip_candidate            boolean
)
LANGUAGE sql STABLE AS $$
WITH win AS (
  SELECT s.*,
         (date_trunc('week', p_week)::date - 7 * (s.window_weeks - 1)) AS w_start,
         (date_trunc('week', p_week)::date + 6)                        AS w_end
  FROM perf.settings s
),
weekdays AS (
  SELECT d::date AS day
  FROM win, generate_series(win.w_start::timestamp, win.w_end::timestamp, interval '1 day') AS d
  WHERE extract(isodow FROM d) < 6
),
eng AS (
  SELECT e.*,
         -- contracted weekdays in the window (after start, before end date)
         (SELECT count(*) FROM weekdays w
           WHERE w.day >= e.start_date AND (e.end_date IS NULL OR w.day <= e.end_date)) AS contracted_weekdays,
         -- of those, the days the person was actually available
         (SELECT count(*) FROM weekdays w
           WHERE w.day >= e.start_date AND (e.end_date IS NULL OR w.day <= e.end_date)
             AND NOT EXISTS (SELECT 1 FROM org.unavailable_day u
                             WHERE u.github_login = e.github_login AND u.day = w.day)) AS available_weekdays
  FROM org.engineer e, win
  WHERE e.start_date <= win.w_end
    AND (e.end_date IS NULL OR e.end_date >= win.w_start)
),
prs AS (
  SELECT p.author_login AS login, count(*)::int AS merged_prs
  FROM gh.pull_request p, win
  WHERE NOT p.is_bot
    AND p.merged_at IS NOT NULL
    AND (p.merged_at AT TIME ZONE 'Europe/Amsterdam')::date BETWEEN win.w_start AND win.w_end
  GROUP BY 1
),
reviews AS (   -- context for the manager; not part of the score
  SELECT r.reviewer_login AS login, count(DISTINCT r.pr_id)::int AS reviews_given
  FROM gh.pr_review r
  JOIN gh.pull_request p ON p.pr_id = r.pr_id, win
  WHERE r.reviewer_login <> p.author_login
    AND (r.submitted_at AT TIME ZONE 'Europe/Amsterdam')::date BETWEEN win.w_start AND win.w_end
  GROUP BY 1
),
cop AS (
  SELECT c.user_login AS login,
         sum(coalesce(c.code_generation_activity_count, 0)) AS generations,
         sum(coalesce(c.code_acceptance_activity_count, 0)) AS acceptances,
         bool_and(coalesce(c.client_telemetry_present, false)) AS telemetry_complete
  FROM copilot_raw.user_day c, win
  WHERE c.day BETWEEN win.w_start AND win.w_end
  GROUP BY 1
),
base AS (
  SELECT e.github_login, e.display_name, e.team, e.job_level, e.manager_db_user,
         win.w_start, win.w_end,
         round(e.available_weekdays * e.fte, 1)                               AS available_days,
         coalesce(p.merged_prs, 0)                                            AS merged_prs,
         coalesce(p.merged_prs, 0) / nullif(e.available_weekdays * e.fte, 0)  AS prs_per_day,
         coalesce(r.reviews_given, 0)                                         AS reviews_given,
         c.generations, c.acceptances,
         c.acceptances::numeric / nullif(c.generations, 0)                    AS acceptance_rate,
         CASE
           WHEN NOT e.in_scope
             THEN 'not ranked: out of scope'
           WHEN e.start_date > win.w_end - win.new_joiner_days
             THEN format('not ranked: joined less than %s days before window end', win.new_joiner_days)
           WHEN e.available_weekdays < win.min_available_share * e.contracted_weekdays
             THEN 'not ranked: available less than ' || round(100 * win.min_available_share) || '% of the window'
           WHEN c.login IS NULL OR c.generations < win.min_copilot_generations
             THEN format('not ranked: fewer than %s Copilot generations', win.min_copilot_generations)
           WHEN NOT c.telemetry_complete
             THEN 'not ranked: Copilot telemetry incomplete'
           ELSE 'ranked'
         END                                                                  AS status,
         CASE win.rank_within WHEN 'job_level' THEN e.job_level ELSE 'all engineers' END AS peer_group,
         EXISTS (SELECT 1 FROM pip.enrolment pe
                 WHERE pe.github_login = e.github_login
                   AND pe.started_on <= win.w_end
                   AND (pe.ended_on IS NULL OR pe.ended_on >= win.w_end))     AS on_active_pip,
         win.bottom_share, win.weight_merged_prs, win.weight_copilot, win.min_peer_group_size
  FROM eng e
  CROSS JOIN win
  LEFT JOIN prs     p ON p.login = e.github_login
  LEFT JOIN reviews r ON r.login = e.github_login
  LEFT JOIN cop     c ON c.login = e.github_login
),
pct AS (
  SELECT b.github_login,
         count(*) OVER (PARTITION BY b.peer_group)                                  AS n,
         percent_rank() OVER (PARTITION BY b.peer_group ORDER BY b.prs_per_day)     AS pct_prs,
         percent_rank() OVER (PARTITION BY b.peer_group ORDER BY b.acceptance_rate) AS pct_cop
  FROM base b
  WHERE b.status = 'ranked'
),
scored AS (
  SELECT b.github_login, b.peer_group, p.n, p.pct_prs, p.pct_cop,
         b.weight_merged_prs * p.pct_prs + b.weight_copilot * p.pct_cop AS composite
  FROM base b JOIN pct p USING (github_login)
),
positioned AS (
  SELECT s.*,
         rank() OVER (PARTITION BY s.peer_group ORDER BY s.composite DESC) AS rank_top,
         rank() OVER (PARTITION BY s.peer_group ORDER BY s.composite ASC)  AS rank_bottom
  FROM scored s
),
grp AS (
  SELECT b.peer_group, count(*) AS n FROM base b WHERE b.status = 'ranked' GROUP BY 1
)
SELECT b.github_login, b.display_name, b.team, b.job_level, b.manager_db_user,
       b.w_start, b.w_end,
       b.available_days,
       b.merged_prs,
       round(b.prs_per_day, 3),
       b.reviews_given,
       b.generations, b.acceptances,
       round(b.acceptance_rate, 3),
       CASE WHEN b.status = 'ranked' AND g.n < b.min_peer_group_size
            THEN format('not ranked: peer group under %s people', b.min_peer_group_size)
            ELSE b.status END,
       b.peer_group,
       g.n::int,
       round(p.pct_prs::numeric, 3),
       round(p.pct_cop::numeric, 3),
       round(p.composite::numeric, 3),
       p.rank_top::int,
       coalesce(p.rank_bottom <= ceil(b.bottom_share * p.n), false),   -- ties at the cut-off are all included
       b.on_active_pip,
       coalesce(p.rank_bottom <= ceil(b.bottom_share * p.n), false) AND NOT b.on_active_pip
FROM base b
LEFT JOIN grp g ON g.peer_group = b.peer_group AND b.status = 'ranked'
LEFT JOIN positioned p
       ON p.github_login = b.github_login
      AND p.n >= b.min_peer_group_size;      -- groups that are too small get no rank
$$;


-- ---------------------------------------------------------------------
-- 5. Weekly snapshot (what the dashboard reads; history stays stable)
-- ---------------------------------------------------------------------
-- Stable random engineer code for the anonymised views. Random, not a hash
-- of the login: a hash of 120 known logins could be reversed in seconds.
-- No role is granted access to this table.
CREATE TABLE IF NOT EXISTS perf.pseudonym (
  github_login text PRIMARY KEY,
  engineer_code text NOT NULL UNIQUE
    DEFAULT 'E-' || upper(substr(md5(gen_random_uuid()::text), 1, 8)),
  created_at   timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS perf.weekly_snapshot (
  week_start                   date        NOT NULL,   -- Monday of the last week in the window
  github_login                 text        NOT NULL,
  display_name                 text        NOT NULL,
  team                         text        NOT NULL,
  job_level                    text        NOT NULL,
  manager_db_user              text,
  window_start                 date        NOT NULL,
  window_end                   date        NOT NULL,
  available_days               numeric,
  merged_prs                   int,
  merged_prs_per_available_day numeric,
  reviews_given                int,
  copilot_generations          bigint,
  copilot_acceptances          bigint,
  copilot_acceptance_rate      numeric,
  status                       text        NOT NULL,
  peer_group                   text,
  peer_group_size              int,
  pct_merged_prs               numeric,
  pct_copilot                  numeric,
  composite_score              numeric,
  rank_from_top                int,
  in_bottom                    boolean     NOT NULL,
  on_active_pip                boolean     NOT NULL,
  new_pip_candidate            boolean     NOT NULL,
  settings_used                jsonb       NOT NULL,   -- audit: exact settings behind this snapshot
  created_at                   timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (week_start, github_login)
);

CREATE OR REPLACE PROCEDURE perf.take_snapshot(p_week date DEFAULT NULL)
LANGUAGE plpgsql AS $$
DECLARE
  wk date := coalesce(date_trunc('week', p_week)::date,
                      date_trunc('week', current_date)::date - 7);
BEGIN
  -- GitHub finalises Copilot IDE telemetry within three full UTC days.
  IF wk + 10 > current_date THEN
    RAISE EXCEPTION 'Week % is not final yet; run on or after %', wk, wk + 10;
  END IF;

  INSERT INTO perf.pseudonym (github_login)
  SELECT github_login FROM org.engineer
  ON CONFLICT (github_login) DO NOTHING;

  DELETE FROM perf.weekly_snapshot WHERE week_start = wk;

  INSERT INTO perf.weekly_snapshot
  SELECT wk, r.*, (SELECT to_jsonb(s) - 'id' FROM perf.settings s), now()
  FROM perf.compute_ranking(wk) r;

  DELETE FROM copilot_raw.user_day
  WHERE day < current_date - (SELECT raw_retention_days FROM perf.settings);
END $$;


-- ---------------------------------------------------------------------
-- 6. Dashboard views
-- ---------------------------------------------------------------------
-- Latest snapshot, with movement and recent history per engineer.
CREATE OR REPLACE VIEW perf.v_ranking_current AS
WITH latest AS (SELECT max(week_start) AS wk FROM perf.weekly_snapshot),
hist AS (
  SELECT s.github_login,
         count(*) FILTER (WHERE s.in_bottom) AS weeks_in_bottom_last_8
  FROM perf.weekly_snapshot s, latest
  WHERE s.week_start > latest.wk - 7 * 8
  GROUP BY 1
),
prev AS (
  SELECT s.github_login, s.rank_from_top AS prev_rank
  FROM perf.weekly_snapshot s, latest
  WHERE s.week_start = latest.wk - 7
)
SELECT s.week_start,
       s.window_start,
       s.window_end,
       s.display_name,
       s.github_login,
       s.team,
       s.job_level,
       s.manager_db_user,
       s.status,
       s.peer_group,
       s.rank_from_top,
       s.peer_group_size,
       pv.prev_rank - s.rank_from_top     AS rank_change,    -- positive = moved up
       s.composite_score,
       s.merged_prs,
       s.available_days,
       s.merged_prs_per_available_day,
       s.pct_merged_prs,
       s.copilot_acceptance_rate,
       s.copilot_generations,
       s.pct_copilot,
       s.reviews_given,
       s.in_bottom,
       coalesce(h.weeks_in_bottom_last_8, 0) AS weeks_in_bottom_last_8,
       s.on_active_pip,
       s.new_pip_candidate,
       mr.decision                         AS manager_decision,
       mr.decided_by,
       mr.decided_at
FROM perf.weekly_snapshot s
JOIN latest ON s.week_start = latest.wk
LEFT JOIN hist h  ON h.github_login  = s.github_login
LEFT JOIN prev pv ON pv.github_login = s.github_login
LEFT JOIN pip.manager_review mr
       ON mr.github_login = s.github_login AND mr.week_start = s.week_start;

-- Weekly history for trend charts and the engineer drill-down.
CREATE OR REPLACE VIEW perf.v_ranking_history AS
SELECT week_start, github_login, display_name, team, job_level, manager_db_user,
       status, peer_group, rank_from_top, peer_group_size, composite_score,
       merged_prs, available_days, merged_prs_per_available_day,
       copilot_acceptance_rate, reviews_given, in_bottom, on_active_pip
FROM perf.weekly_snapshot;

-- New candidates in the latest snapshot without a manager decision yet.
CREATE OR REPLACE VIEW perf.v_review_queue AS
SELECT week_start, display_name, github_login, team, job_level, manager_db_user,
       rank_from_top, peer_group_size, weeks_in_bottom_last_8,
       merged_prs, available_days, merged_prs_per_available_day,
       copilot_acceptance_rate, reviews_given
FROM perf.v_ranking_current
WHERE new_pip_candidate AND manager_decision IS NULL;

-- Exclusions by reason, for the data-quality panel.
CREATE OR REPLACE VIEW perf.v_not_ranked AS
SELECT week_start, status AS reason, count(*) AS engineers
FROM perf.weekly_snapshot
WHERE status <> 'ranked'
GROUP BY 1, 2;

-- Manager-scoped versions: a manager sees only their own reports.
CREATE OR REPLACE VIEW perf.v_my_reports WITH (security_barrier) AS
SELECT * FROM perf.v_ranking_current WHERE manager_db_user = current_user;

CREATE OR REPLACE VIEW perf.v_my_review_queue WITH (security_barrier) AS
SELECT * FROM perf.v_review_queue WHERE manager_db_user = current_user;


-- ---------------------------------------------------------------------
-- 7. Access
-- ---------------------------------------------------------------------
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'perf_full_reader') THEN
    CREATE ROLE perf_full_reader NOLOGIN;      -- CTO, HR
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'perf_manager') THEN
    CREATE ROLE perf_manager NOLOGIN;          -- engineering managers
  END IF;
END $$;

GRANT USAGE ON SCHEMA perf, pip TO perf_full_reader, perf_manager;
GRANT SELECT ON perf.v_ranking_current, perf.v_ranking_history,
                perf.v_review_queue, perf.v_not_ranked TO perf_full_reader;
GRANT SELECT ON pip.manager_review, pip.enrolment TO perf_full_reader;
GRANT SELECT ON perf.v_my_reports, perf.v_my_review_queue TO perf_manager;
GRANT SELECT, INSERT, UPDATE ON pip.manager_review TO perf_manager;
GRANT SELECT, INSERT, UPDATE ON pip.enrolment      TO perf_manager;

-- Managers may record decisions and enrolments only for their own reports.
-- current_user is passed in from the policy: inside a SECURITY DEFINER
-- function it would be the function owner, not the manager.
CREATE OR REPLACE FUNCTION pip.is_my_report(p_login text, p_manager text) RETURNS boolean
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = pg_catalog, org AS $$
  SELECT EXISTS (SELECT 1 FROM org.engineer
                 WHERE github_login = p_login AND manager_db_user = p_manager)
$$;
REVOKE ALL ON FUNCTION pip.is_my_report(text, text) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION pip.is_my_report(text, text) TO perf_manager;

ALTER TABLE pip.manager_review ENABLE ROW LEVEL SECURITY;
ALTER TABLE pip.enrolment      ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS full_read ON pip.manager_review;
DROP POLICY IF EXISTS own_reports ON pip.manager_review;
CREATE POLICY full_read   ON pip.manager_review FOR SELECT TO perf_full_reader USING (true);
CREATE POLICY own_reports ON pip.manager_review FOR ALL    TO perf_manager
  USING (pip.is_my_report(github_login, current_user))
  WITH CHECK (pip.is_my_report(github_login, current_user) AND decided_by = current_user);

DROP POLICY IF EXISTS full_read ON pip.enrolment;
DROP POLICY IF EXISTS own_reports ON pip.enrolment;
CREATE POLICY full_read   ON pip.enrolment FOR SELECT TO perf_full_reader USING (true);
CREATE POLICY own_reports ON pip.enrolment FOR ALL    TO perf_manager
  USING (pip.is_my_report(github_login, current_user))
  WITH CHECK (pip.is_my_report(github_login, current_user) AND decided_by = current_user);
-- No grants on org, gh or copilot_raw for either role.


-- ---------------------------------------------------------------------
-- 8. Anonymised main view and the name column
-- ---------------------------------------------------------------------
-- Main ranking, anonymised. Ranked engineers only (not-ranked reasons
-- such as "joined less than 90 days ago" would identify people; their
-- counts are in perf.v_not_ranked). Left out on purpose: name, login,
-- team, manager, available days and the raw PR count (from which
-- available days can be worked out), and PIP status and decisions.
CREATE OR REPLACE VIEW perf.v_ranking_anon AS
SELECT c.week_start,
       c.window_start,
       c.window_end,
       p.engineer_code,
       c.peer_group,
       c.rank_from_top,
       c.peer_group_size,
       c.rank_change,
       c.composite_score,
       c.pct_merged_prs,
       c.merged_prs_per_available_day,
       c.pct_copilot,
       c.copilot_acceptance_rate,
       c.in_bottom,
       c.weeks_in_bottom_last_8
FROM perf.v_ranking_current c
JOIN perf.pseudonym p USING (github_login)
WHERE c.status = 'ranked';

-- Anonymised weekly history, for trend charts on the main view.
CREATE OR REPLACE VIEW perf.v_ranking_anon_history AS
SELECT s.week_start,
       p.engineer_code,
       s.peer_group,
       s.rank_from_top,
       s.peer_group_size,
       s.composite_score,
       s.pct_merged_prs,
       s.pct_copilot,
       s.in_bottom
FROM perf.weekly_snapshot s
JOIN perf.pseudonym p USING (github_login)
WHERE s.status = 'ranked';

-- The name column. Join it to the main view on engineer_code. Everyone with
-- dashboard access may query it, but the database only returns rows to:
--   CTO/HR (perf_full_reader)  : every engineer
--   a manager (perf_manager)   : their own reports, or everyone if
--                                perf.settings.names_visible_to = 'all_managers'
-- For anyone else it is empty, so the name column stays blank. This is
-- enforced here, not by hiding a column in the BI tool.
CREATE OR REPLACE VIEW perf.v_engineer_names WITH (security_barrier) AS
SELECT p.engineer_code,
       e.display_name,
       e.team
FROM perf.pseudonym p
JOIN org.engineer e USING (github_login)
CROSS JOIN perf.settings s
WHERE pg_has_role(current_user, 'perf_full_reader', 'MEMBER')
   OR e.manager_db_user = current_user
   OR (s.names_visible_to = 'all_managers'
       AND pg_has_role(current_user, 'perf_manager', 'MEMBER'));

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'perf_viewer') THEN
    CREATE ROLE perf_viewer NOLOGIN;           -- anyone who sees the anonymised main view
  END IF;
END $$;

GRANT USAGE  ON SCHEMA perf TO perf_viewer;
GRANT SELECT ON perf.v_ranking_anon, perf.v_ranking_anon_history, perf.v_not_ranked,
                perf.v_engineer_names
  TO perf_viewer, perf_manager, perf_full_reader;

-- Optional: log every name lookup (needs the pgaudit extension; not
-- available in the test environment, so untested here).
--   ALTER SYSTEM SET pgaudit.role = 'perf_auditor';   -- then reload
--   CREATE ROLE perf_auditor NOLOGIN;
--   GRANT SELECT ON perf.v_engineer_names, perf.v_ranking_current TO perf_auditor;
-- Every SELECT on those views is then written to the server log with the
-- user who ran it.
