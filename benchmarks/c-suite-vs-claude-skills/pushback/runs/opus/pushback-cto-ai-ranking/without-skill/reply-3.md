Done. The main view is now pseudonymised. Names come from a separate lookup, and only managers (for their own people) can see them. Two points decide whether this actually protects anyone:

- **Don't build it as a hidden column in the report.** In Power BI, Tableau, Looker and Metabase, a hidden column is still in the dataset. Anyone who can export, use "show data", analyse in Excel or edit the report can get the names back. So the names stay in the database, and the database only returns the rows each viewer is allowed to see.
- **Under GDPR this is pseudonymised, not anonymised.** The data is still personal data, so the scope of the DPIA doesn't change.

## How it works

**Main view (`mart.ranking_anonymous`)**
- It lists every ranked engineer with:
  - a pseudonym (random and stable, e.g. `ENG-08C61476`)
  - rank and the change since last week
  - both metrics and their percentiles
  - the composite score
  - the bottom-10% flag and the "ranked on PRs only" flag
- Everyone with access to the main view sees all rows.
- It leaves out team, level, manager, FTE, availability and PIP status, as well as excluded engineers (new joiners, long leave). With those columns, most rows in a team of 6–8 can be identified, which defeats the point.
- Team-level counts stay on the coverage page, which is already limited to managers, the CTO and HR.

**Name column (`mart.ranking_names`)**
- It maps each pseudonym to name, team, level and manager.
- Row-level security decides what each viewer gets back:
  - **Managers:** their own reporting line, including skip-levels.
  - **CTO and HR:** everyone.
  - **Anyone else:** nothing.
- In the BI tool, relate it to the main view on `pseudonym` and put Name in the main table. Each manager then sees names for their own people and "—" for everyone else. A drill-through page from the pseudonym works too.

This is what the bottom of the ranking looked like for a team-A manager in my test:

| Rank | Pseudonym | Name | Score | Bottom 10% |
|---|---|---|---|---|
| 28 | ENG-08C61476 | — | 0.02 | yes |
| 27 | ENG-76F10832 | — | 0.12 | yes |
| 26 | ENG-C20E775F | Engineer 15 | 0.17 | yes |
| 25 | ENG-1DB8F7FD | Engineer 18 | 0.23 | no |

**Who sees what**

| Who | Main view | Names | Review queue and drill-down |
|---|---|---|---|
| `ranking_viewer` (anyone you add) | All rows, pseudonymised | No | No |
| Managers | All rows, pseudonymised | Own reporting line | Own reporting line |
| CTO, HR (`sees_all`) | All rows, pseudonymised | Everyone | Everyone |

I kept full name access for the CTO and HR, because HR runs the PIPs. If you meant literally only managers, set `sees_all = false` for HR. HR then sees no names at all. If you want HR to get names only once a manager confirms a PIP, I can add a small view of confirmed decisions for HR.

## BI setup

- **Connection:** use a live or DirectQuery connection that passes the viewer's own identity to the database. If the tool imports the data through a service account, the whole names table ends up in the data model. In that case, rebuild the visibility rule in the tool's own row-level security and turn off export and "show data" for that table.
- **Logging (optional):** if you want a record of who looks up names, enable pgaudit object logging on `mart.ranking_names`.
- **Weekly job:** add the pseudonym `INSERT` from section 1 to the start of the weekly job, so new joiners get a pseudonym before scoring.

## A fix to the previous script

While testing this, I found a problem in the last script. Its row-level security check ran a function once per row. With a year of history in my test, the CTO's queries took several seconds, and one didn't finish within two minutes. The new check works out the visible set once per query, and the same queries now run in well under a second.

Section 0 of the script below applies the fix. I've also updated `engineer-ranking.sql` in the folder, so running it again won't bring back the old version.

**Run order:**
1. `engineer-ranking.sql`
2. `engineer-ranking-anonymised.sql`

I tested both a fresh install and an upgrade from the previous version on PostgreSQL 16:
- **Viewer role:** sees the 28 ranked engineers pseudonymised. It can't reach the names, the snapshot table or the pseudonym key.
- **Names lookup:** one manager got names for their 10 people, a head of engineering for 20, and the CTO for all 30.
- **Decision rules:** managers still can't record a decision for someone outside their line.

```sql
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
```
