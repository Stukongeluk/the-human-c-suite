-- =====================================================================
-- Add-on to engineer-ranking.sql: anonymised main view + name lookup
-- Run once after engineer-ranking.sql. PostgreSQL 15+.
-- =====================================================================

-- ---------------------------------------------------------------------
-- 0. Fix to engineer-ranking.sql: set-based visibility check
--    The old check ran a function on every row, and that function was planned
--    on every call (sometimes with JIT), so full-history queries got slow.
--    This version works out the visible set once per query.
-- ---------------------------------------------------------------------
CREATE OR REPLACE FUNCTION mart.visible_employees(viewer name)
RETURNS SETOF bigint
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = pg_catalog
SET jit = off
AS $$
    SELECT o.employee_id                                  -- CTO / HR: everyone
    FROM ref.org_chart o
    WHERE EXISTS (SELECT 1 FROM ref.app_users au
                  WHERE au.db_role = viewer AND au.sees_all)
    UNION
    SELECT rl.employee_id                                 -- managers: whole reporting line
    FROM ref.app_users au
    JOIN ref.reporting_lines rl ON rl.manager_id = au.employee_id
    WHERE au.db_role = viewer
$$;
REVOKE ALL ON FUNCTION mart.visible_employees(name) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION mart.visible_employees(name) TO ranking_reader;

DROP POLICY IF EXISTS ranking_read ON mart.engineer_ranking_weekly;
CREATE POLICY ranking_read ON mart.engineer_ranking_weekly
    FOR SELECT
    USING (employee_id IN (SELECT mart.visible_employees(current_user)));

DROP POLICY IF EXISTS decisions_rw ON hr.pip_flag_decisions;
CREATE POLICY decisions_rw ON hr.pip_flag_decisions
    FOR ALL
    USING (employee_id IN (SELECT mart.visible_employees(current_user)))
    WITH CHECK (employee_id IN (SELECT mart.visible_employees(current_user))
                AND decided_by = current_user);



-- ---------------------------------------------------------------------
-- 1. Pseudonym key: random, not derived from employee_id
--    (a hash of a small id range can be reversed by trying every id)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hr.engineer_pseudonyms (
    employee_id bigint      PRIMARY KEY,
    pseudonym   text        NOT NULL UNIQUE
                DEFAULT 'ENG-' || upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 8)),
    created_at  timestamptz NOT NULL DEFAULT now()
);

-- Also add this INSERT to the start of the weekly job, so new joiners get a pseudonym.
INSERT INTO hr.engineer_pseudonyms (employee_id)
SELECT employee_id FROM ref.engineers
ON CONFLICT (employee_id) DO NOTHING;

-- Viewers only ever see the pseudonym rows for people they may see by name.
ALTER TABLE hr.engineer_pseudonyms ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS pseudonyms_read ON hr.engineer_pseudonyms;
CREATE POLICY pseudonyms_read ON hr.engineer_pseudonyms
    FOR SELECT
    USING (employee_id IN (SELECT mart.visible_employees(current_user)));


-- ---------------------------------------------------------------------
-- 2. Main view: every ranked engineer, no identifying columns
--    Plain view (runs with the owner's rights), so everyone with access
--    sees all rows. Team, level, manager, FTE, availability and PIP status
--    are left out on purpose: with them, most rows are identifiable.
--    Excluded engineers (new joiners, long leave) are left out for the same reason.
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW mart.ranking_anonymous AS
SELECT r.week_start,
       ps.pseudonym,
       r.overall_rank,
       r.rank_change,
       r.eligible_count,
       r.copilot_acceptance_rate,
       r.pct_copilot,
       r.has_copilot_data,
       r.merged_prs_per_fte_week,
       r.pct_prs,
       r.composite_score,
       r.bottom_flag
FROM mart.engineer_ranking_weekly r
JOIN hr.engineer_pseudonyms ps ON ps.employee_id = r.employee_id
WHERE r.eligible;


-- ---------------------------------------------------------------------
-- 3. Name lookup: the "column only managers can open"
--    security_invoker view, so row-level security decides which rows come back:
--    managers get their own reporting line, CTO/HR (sees_all) get everyone,
--    anyone else gets nothing.
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW mart.ranking_names WITH (security_invoker = true) AS
SELECT DISTINCT ON (ps.pseudonym)
       ps.pseudonym,
       r.employee_id,
       r.full_name,
       r.team,
       r.level,
       r.manager_employee_id
FROM hr.engineer_pseudonyms ps
JOIN mart.engineer_ranking_weekly r ON r.employee_id = ps.employee_id
ORDER BY ps.pseudonym, r.week_start DESC;      -- latest team/level/manager


-- ---------------------------------------------------------------------
-- 4. Roles
--    ranking_viewer: anonymised main view only (give this to anyone who should
--                    see the ranking without names)
--    ranking_reader: managers, CTO, HR (from engineer-ranking.sql); also gets
--                    the name lookup, filtered by row-level security
-- ---------------------------------------------------------------------
-- CREATE ROLE ranking_viewer NOLOGIN;   -- once
GRANT USAGE  ON SCHEMA mart TO ranking_viewer;
GRANT SELECT ON mart.ranking_anonymous TO ranking_viewer;
GRANT ranking_viewer TO ranking_reader;

GRANT SELECT ON hr.engineer_pseudonyms, mart.ranking_names TO ranking_reader;

-- Old per-row check from the first version of engineer-ranking.sql, no longer used.
DROP FUNCTION IF EXISTS mart.can_see_employee(bigint, name);
