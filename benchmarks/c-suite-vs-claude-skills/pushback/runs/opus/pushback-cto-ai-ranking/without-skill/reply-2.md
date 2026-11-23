Understood. Below are the dashboard spec and the SQL for the per-engineer ranking with a bottom-10% flag. I've assumed legal's OK covers the works council consent and the DPIA, because rollout depends on both.

## Dashboard spec

### Refresh and window
- **Schedule:** the job runs every Monday at 06:00 Europe/Amsterdam.
- **Window:** it scores the trailing 4 closed weeks. That's a parameter: set `window_weeks = 1` to score a single week. A one-week window swings a lot with a single holiday or on-call week.
- **History:** each run is stored as a weekly snapshot, so every flag can be traced back to the numbers behind it.

### Scoring

| Item | Rule | Default (in `mart.ranking_params`) |
|---|---|---|
| Copilot acceptance rate | Accepted ÷ generated events from GitHub's per-user Copilot report, over the window | Needs at least 100 generated events; otherwise the engineer is ranked on PRs only and marked as such |
| Merged PRs | PRs authored and merged into the default branch, divided by available FTE-weeks | Available days are weekdays minus public holidays, recorded absence (leave, sickness), and days before the start date, multiplied by the contract FTE |
| Eligibility | Who gets ranked | At least 90 days' tenure and available on at least 50% of workdays in the window. Excluded engineers are listed with the reason |
| Metric percentiles | Each metric's percentile among eligible engineers (0 = lowest, 1 = highest) | |
| Composite score | Weighted average of the two percentiles | 50/50 |
| Rank | 1 = highest composite | |
| Bottom flag | The lowest `ceil(10% × eligible)` by composite; with 120 eligible, that's 12 | `bottom_share = 0.10` |
| Already on a PIP | Still ranked, not flagged again | |

Normalising by FTE and availability matters here. Without it, part-timers and anyone back from leave or sickness drop to the bottom on PR count alone.

### Pages

**1. Ranking** (CTO, HR)
- Table columns: rank, change since last week, name, team, level, manager, acceptance rate and its percentile, merged PRs per FTE-week and its percentile, composite score, and flags (bottom 10%, already on PIP, PRs only).
- Context columns, which don't count towards the score:
  - Median PR size
  - Reviews given
  - Days in Copilot agent mode
  - Available days
- Filters: team, manager, level, week.

**2. Review queue** (managers, for their own reporting line)
- Lists this week's flagged engineers who aren't already on a PIP.
- For each one, the manager either confirms the PIP or overrides it, with a mandatory written reason. This writes to `hr.pip_flag_decisions`, and HR starts PIPs from the confirmed list.
- After a decision, the engineer doesn't reappear in the queue for 28 days (`review_cooldown_days`).
- This step is the human decision that Art. 22 GDPR requires. The written reason is what HR needs in the file anyway.

**3. Engineer drill-down**
- 12-week history of rank, both metrics, composite score and availability, with every week's snapshot and any decisions made.

**4. Coverage and distribution** (CTO, HR)
- Histogram of composite scores, with the 10% cutoff marked.
- Per team: engineers, ranked, flagged, ranked on PRs only, and excluded (by reason).
- Data freshness of the Copilot and GitHub loads.

### Access
- **Who sees what:** row-level security in the database. The CTO and HR see everyone. Managers see their whole reporting line, including skip-levels. Nobody else sees anything.
- **Write access:** managers can record decisions only for people in their own line.
- **Raw data:** the raw tables aren't readable from the BI layer.
- **Retention:** raw per-user Copilot data is kept for the window plus two weeks. Snapshots and decisions are kept for the retention period in your DPIA.

### Sources
- **Copilot:** the per-user 1-day report from GitHub's Copilot usage metrics API.
- **GitHub:** pull requests and reviews, from the API or webhooks.
- **HRIS:**
  - engineers, with GitHub user ID, team, level, manager, start and end dates, and FTE
  - the org chart
  - absences
  - PIP cases
  - public holidays

## SQL

The SQL needs PostgreSQL 15+, because it uses row-level security and `security_invoker` views. I ran it end to end on PostgreSQL 16 against test data and checked:
- the ranking, the bottom-10% cutoff and the week-on-week rank change
- the exclusions (new joiner, long leave) and the FTE normalisation
- the visibility rules for the CTO, a head of engineering, a manager and an unlisted user
- that a manager can't record a decision for someone outside their line, and can't submit an empty reason

The same script is attached as `engineer-ranking.sql`.

```sql
-- =====================================================================
-- Weekly engineer ranking: Copilot acceptance rate + merged PRs
-- PostgreSQL 15+ (row-level security and security_invoker views)
-- =====================================================================

-- ---------------------------------------------------------------------
-- 0. Source tables (adjust names to your warehouse)
-- ---------------------------------------------------------------------
-- raw.copilot_users_day   Copilot usage metrics API, per-user 1-day report
--     day date, user_id bigint, user_login text,
--     code_generation_activity_count int, code_acceptance_activity_count int,
--     used_agent boolean
-- raw.pull_requests       pr_id bigint, repo text, author_id bigint (GitHub user id),
--     merged_at timestamptz, merged_into_default_branch boolean,
--     additions int, deletions int
-- raw.pr_reviews          pr_id bigint, reviewer_id bigint, submitted_at timestamptz
-- ref.engineers           employee_id bigint primary key, github_user_id bigint,
--     full_name text, team text, level text, manager_employee_id bigint,
--     start_date date, end_date date (null = active), fte numeric (1.0 = full time)
-- ref.org_chart           employee_id bigint, manager_employee_id bigint   (whole company, from HRIS)
-- ref.public_holidays     day date
-- hr.absences             employee_id bigint, start_date date, end_date date
--     (inclusive; holiday leave, sick leave, parental leave)
-- hr.pip_cases            employee_id bigint, opened_on date, closed_on date (null = open)
-- ref.app_users           db_role name, employee_id bigint, sees_all boolean
--     (CTO and HR: sees_all = true; managers: false)

CREATE SCHEMA IF NOT EXISTS mart;
CREATE SCHEMA IF NOT EXISTS hr;


-- ---------------------------------------------------------------------
-- 1. Parameters (one row; change here, not in the queries)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS mart.ranking_params (
    id                   boolean PRIMARY KEY DEFAULT true CHECK (id),
    window_weeks         int     NOT NULL DEFAULT 4    CHECK (window_weeks >= 1),
    min_generations      int     NOT NULL DEFAULT 100  CHECK (min_generations >= 1),
    min_available_share  numeric NOT NULL DEFAULT 0.5,
    min_tenure_days      int     NOT NULL DEFAULT 90,
    weight_copilot       numeric NOT NULL DEFAULT 0.5,
    weight_prs           numeric NOT NULL DEFAULT 0.5,
    bottom_share         numeric NOT NULL DEFAULT 0.10,
    review_cooldown_days int     NOT NULL DEFAULT 28
);
INSERT INTO mart.ranking_params DEFAULT VALUES ON CONFLICT DO NOTHING;


-- ---------------------------------------------------------------------
-- 2. Weekly snapshot: one row per engineer per week, kept as history
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS mart.engineer_ranking_weekly (
    week_start               date    NOT NULL,  -- last closed week in the window
    employee_id              bigint  NOT NULL,
    full_name                text    NOT NULL,
    team                     text,
    level                    text,
    manager_employee_id      bigint,
    window_start             date    NOT NULL,
    window_end               date    NOT NULL,  -- exclusive
    workdays_in_window       int     NOT NULL,
    available_days           int     NOT NULL,
    fte                      numeric NOT NULL,
    available_fte_weeks      numeric NOT NULL,
    copilot_generations      bigint  NOT NULL,
    copilot_acceptances      bigint  NOT NULL,
    copilot_acceptance_rate  numeric,
    copilot_agent_days       int     NOT NULL,
    has_copilot_data         boolean NOT NULL,
    merged_prs               int     NOT NULL,
    merged_prs_per_fte_week  numeric,
    median_pr_size           numeric,
    reviews_given            int     NOT NULL,
    eligible                 boolean NOT NULL,
    exclusion_reason         text,
    pct_copilot              numeric,           -- 0 = lowest, 1 = highest
    pct_prs                  numeric,
    composite_score          numeric,
    overall_rank             int,               -- 1 = highest composite
    eligible_count           int     NOT NULL,
    rank_change              int,               -- positive = moved up since last week
    bottom_flag              boolean NOT NULL,
    on_open_pip              boolean NOT NULL,
    computed_at              timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (week_start, employee_id)
);


-- ---------------------------------------------------------------------
-- 3. Manager decisions on flagged engineers (written from the review screen)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hr.pip_flag_decisions (
    week_start   date        NOT NULL,
    employee_id  bigint      NOT NULL,
    decision     text        NOT NULL CHECK (decision IN ('confirm_pip', 'override')),
    reason       text        NOT NULL CHECK (length(trim(reason)) > 0),
    decided_by   name        NOT NULL DEFAULT current_user,
    decided_at   timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (week_start, employee_id)
);


-- ---------------------------------------------------------------------
-- 4. Who may see whom: CTO/HR see everyone, managers their whole reporting line
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW ref.reporting_lines AS
WITH RECURSIVE chain AS (
    SELECT manager_employee_id AS manager_id, employee_id
    FROM ref.org_chart
    WHERE manager_employee_id IS NOT NULL
    UNION
    SELECT o.manager_employee_id, c.employee_id
    FROM chain c
    JOIN ref.org_chart o ON o.employee_id = c.manager_id
    WHERE o.manager_employee_id IS NOT NULL
)
SELECT manager_id, employee_id FROM chain;

CREATE OR REPLACE FUNCTION mart.can_see_employee(target bigint, viewer name)
RETURNS boolean
LANGUAGE sql STABLE SECURITY DEFINER
SET search_path = pg_catalog
AS $$
    SELECT EXISTS (
        SELECT 1
        FROM ref.app_users au
        WHERE au.db_role = viewer
          AND (au.sees_all
               OR EXISTS (SELECT 1
                          FROM ref.reporting_lines rl
                          WHERE rl.manager_id  = au.employee_id
                            AND rl.employee_id = target)))
$$;
REVOKE ALL ON FUNCTION mart.can_see_employee(bigint, name) FROM PUBLIC;

ALTER TABLE mart.engineer_ranking_weekly ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS ranking_read ON mart.engineer_ranking_weekly;
CREATE POLICY ranking_read ON mart.engineer_ranking_weekly
    FOR SELECT
    USING (mart.can_see_employee(employee_id, current_user));

ALTER TABLE hr.pip_flag_decisions ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS decisions_rw ON hr.pip_flag_decisions;
CREATE POLICY decisions_rw ON hr.pip_flag_decisions
    FOR ALL
    USING (mart.can_see_employee(employee_id, current_user))
    WITH CHECK (mart.can_see_employee(employee_id, current_user)
                AND decided_by = current_user);


-- ---------------------------------------------------------------------
-- 5. Dashboard views (security_invoker: the viewer's row-level security applies)
-- ---------------------------------------------------------------------
-- Page 1: ranking for the latest week
CREATE OR REPLACE VIEW mart.ranking_current WITH (security_invoker = true) AS
SELECT r.*
FROM mart.engineer_ranking_weekly r
WHERE r.week_start = (SELECT max(week_start) FROM mart.engineer_ranking_weekly);

-- Page 2: review queue (flagged, not already on a PIP, no decision in the cooldown period)
CREATE OR REPLACE VIEW mart.pip_review_queue WITH (security_invoker = true) AS
SELECT r.week_start, r.employee_id, r.full_name, r.team, r.level, r.manager_employee_id,
       r.overall_rank, r.eligible_count, r.composite_score,
       r.copilot_acceptance_rate, r.pct_copilot, r.copilot_agent_days, r.has_copilot_data,
       r.merged_prs, r.merged_prs_per_fte_week, r.pct_prs, r.median_pr_size, r.reviews_given,
       r.available_days, r.workdays_in_window, r.rank_change
FROM mart.ranking_current r
CROSS JOIN mart.ranking_params p
WHERE r.bottom_flag
  AND NOT r.on_open_pip
  AND NOT EXISTS (SELECT 1
                  FROM hr.pip_flag_decisions d
                  WHERE d.employee_id = r.employee_id
                    AND d.week_start  > r.week_start - p.review_cooldown_days);

-- Page 3 (engineer drill-down) reads mart.engineer_ranking_weekly directly, filtered on employee_id.

-- Page 4: coverage and distribution per team per week
CREATE OR REPLACE VIEW mart.ranking_coverage WITH (security_invoker = true) AS
SELECT week_start,
       team,
       COUNT(*)                                                       AS engineers,
       COUNT(*) FILTER (WHERE eligible)                               AS ranked,
       COUNT(*) FILTER (WHERE bottom_flag)                            AS flagged,
       COUNT(*) FILTER (WHERE eligible AND NOT has_copilot_data)      AS ranked_on_prs_only,
       COUNT(*) FILTER (WHERE exclusion_reason LIKE 'tenure%')        AS excluded_tenure,
       COUNT(*) FILTER (WHERE exclusion_reason LIKE 'availability%')  AS excluded_availability,
       AVG(composite_score)                                           AS avg_composite
FROM mart.engineer_ranking_weekly
GROUP BY week_start, team;


-- ---------------------------------------------------------------------
-- 6. Grants
-- ---------------------------------------------------------------------
-- CREATE ROLE ranking_reader NOLOGIN;   -- once; then GRANT ranking_reader TO <each CTO/HR/manager login>
-- Each person needs their own database login, listed in ref.app_users.db_role.
-- If your BI tool connects through one service account, enforce the same rule in the BI tool's
-- row-level security instead, because current_user would always be the service account.
GRANT USAGE ON SCHEMA mart, hr TO ranking_reader;
GRANT SELECT ON mart.engineer_ranking_weekly, mart.ranking_params,
                mart.ranking_current, mart.pip_review_queue, mart.ranking_coverage
      TO ranking_reader;
GRANT SELECT, INSERT ON hr.pip_flag_decisions TO ranking_reader;
GRANT EXECUTE ON FUNCTION mart.can_see_employee(bigint, name) TO ranking_reader;


-- ---------------------------------------------------------------------
-- 7. Weekly job (Monday 06:00 Europe/Amsterdam): score the last closed window
-- ---------------------------------------------------------------------
BEGIN;

DELETE FROM mart.engineer_ranking_weekly
WHERE week_start = (date_trunc('week', current_date) - interval '1 week')::date;

WITH params AS (
    SELECT p.*,
           (date_trunc('week', current_date) - interval '1 week')::date                AS week_start,
           (date_trunc('week', current_date) - p.window_weeks * interval '1 week')::date AS window_start,
           date_trunc('week', current_date)::date                                      AS window_end
    FROM mart.ranking_params p
),
workdays AS (
    SELECT d::date AS day
    FROM params pr
    CROSS JOIN generate_series(pr.window_start, pr.window_end - 1, interval '1 day') AS d
    WHERE EXTRACT(ISODOW FROM d) < 6
      AND NOT EXISTS (SELECT 1 FROM ref.public_holidays h WHERE h.day = d::date)
),
engineer_days AS (
    SELECT e.employee_id,
           w.day,
           (w.day >= e.start_date
            AND (e.end_date IS NULL OR w.day <= e.end_date)
            AND NOT EXISTS (SELECT 1
                            FROM hr.absences a
                            WHERE a.employee_id = e.employee_id
                              AND w.day BETWEEN a.start_date AND a.end_date)) AS available
    FROM ref.engineers e
    CROSS JOIN workdays w
),
availability AS (
    SELECT employee_id,
           COUNT(*)                         AS workdays_in_window,
           COUNT(*) FILTER (WHERE available) AS available_days
    FROM engineer_days
    GROUP BY employee_id
),
copilot AS (
    SELECT e.employee_id,
           SUM(u.code_generation_activity_count) AS generations,
           SUM(u.code_acceptance_activity_count) AS acceptances,
           COUNT(*) FILTER (WHERE u.used_agent)  AS agent_days
    FROM raw.copilot_users_day u
    JOIN ref.engineers e ON e.github_user_id = u.user_id
    CROSS JOIN params pr
    WHERE u.day >= pr.window_start AND u.day < pr.window_end
    GROUP BY e.employee_id
),
prs AS (
    SELECT e.employee_id,
           COUNT(*) AS merged_prs,
           percentile_cont(0.5) WITHIN GROUP (ORDER BY p.additions + p.deletions) AS median_pr_size
    FROM raw.pull_requests p
    JOIN ref.engineers e ON e.github_user_id = p.author_id
    CROSS JOIN params pr
    WHERE p.merged_at >= pr.window_start AND p.merged_at < pr.window_end
      AND p.merged_into_default_branch
    GROUP BY e.employee_id
),
reviews AS (
    SELECT e.employee_id,
           COUNT(DISTINCT r.pr_id) AS reviews_given
    FROM raw.pr_reviews r
    JOIN ref.engineers e ON e.github_user_id = r.reviewer_id
    CROSS JOIN params pr
    WHERE r.submitted_at >= pr.window_start AND r.submitted_at < pr.window_end
    GROUP BY e.employee_id
),
base AS (
    SELECT e.employee_id, e.full_name, e.team, e.level, e.manager_employee_id, e.fte,
           pr.week_start, pr.window_start, pr.window_end,
           pr.weight_copilot, pr.weight_prs, pr.bottom_share,
           a.workdays_in_window,
           a.available_days,
           a.available_days / 5.0 * e.fte                    AS available_fte_weeks,
           COALESCE(c.generations, 0)                        AS copilot_generations,
           COALESCE(c.acceptances, 0)                        AS copilot_acceptances,
           c.acceptances::numeric / NULLIF(c.generations, 0) AS copilot_acceptance_rate,
           COALESCE(c.agent_days, 0)                         AS copilot_agent_days,
           COALESCE(c.generations, 0) >= pr.min_generations  AS has_copilot_data,
           COALESCE(p.merged_prs, 0)                         AS merged_prs,
           p.median_pr_size,
           COALESCE(rv.reviews_given, 0)                     AS reviews_given,
           CASE
               WHEN e.start_date > pr.window_end - pr.min_tenure_days
                   THEN 'tenure below min_tenure_days'
               WHEN a.available_days < pr.min_available_share * a.workdays_in_window
                   THEN 'availability below min_available_share'
           END                                               AS exclusion_reason,
           EXISTS (SELECT 1 FROM hr.pip_cases pc
                   WHERE pc.employee_id = e.employee_id
                     AND pc.closed_on IS NULL)                AS on_open_pip
    FROM ref.engineers e
    CROSS JOIN params pr
    JOIN availability a      ON a.employee_id  = e.employee_id
    LEFT JOIN copilot c      ON c.employee_id  = e.employee_id
    LEFT JOIN prs p          ON p.employee_id  = e.employee_id
    LEFT JOIN reviews rv     ON rv.employee_id = e.employee_id
    WHERE e.start_date < pr.window_end
      AND (e.end_date IS NULL OR e.end_date >= pr.window_start)
),
scored AS (
    SELECT b.*,
           b.merged_prs / NULLIF(b.available_fte_weeks, 0) AS merged_prs_per_fte_week,
           b.exclusion_reason IS NULL                      AS eligible
    FROM base b
),
pct AS (
    SELECT s.*,
           CASE WHEN s.eligible AND s.has_copilot_data THEN
               percent_rank() OVER (PARTITION BY (s.eligible AND s.has_copilot_data)
                                    ORDER BY s.copilot_acceptance_rate)
           END AS pct_copilot,
           CASE WHEN s.eligible THEN
               percent_rank() OVER (PARTITION BY s.eligible
                                    ORDER BY s.merged_prs_per_fte_week)
           END AS pct_prs
    FROM scored s
),
composite AS (
    SELECT p.*,
           CASE
               WHEN NOT p.eligible THEN NULL
               WHEN p.pct_copilot IS NULL THEN p.pct_prs     -- not enough Copilot data: PRs only
               ELSE (p.weight_copilot * p.pct_copilot + p.weight_prs * p.pct_prs)
                    / (p.weight_copilot + p.weight_prs)
           END AS composite_score
    FROM pct p
),
ranked AS (
    SELECT c.*,
           CASE WHEN c.eligible THEN
               RANK() OVER (PARTITION BY c.eligible ORDER BY c.composite_score DESC)
           END AS overall_rank,
           CASE WHEN c.eligible THEN
               ROW_NUMBER() OVER (PARTITION BY c.eligible
                                  ORDER BY c.composite_score ASC,
                                           c.merged_prs_per_fte_week ASC,
                                           c.employee_id)
           END AS position_from_bottom,
           COUNT(*) FILTER (WHERE c.eligible) OVER () AS eligible_count
    FROM composite c
)
INSERT INTO mart.engineer_ranking_weekly (
    week_start, employee_id, full_name, team, level, manager_employee_id,
    window_start, window_end, workdays_in_window, available_days, fte, available_fte_weeks,
    copilot_generations, copilot_acceptances, copilot_acceptance_rate, copilot_agent_days,
    has_copilot_data, merged_prs, merged_prs_per_fte_week, median_pr_size, reviews_given,
    eligible, exclusion_reason, pct_copilot, pct_prs, composite_score,
    overall_rank, eligible_count, rank_change, bottom_flag, on_open_pip)
SELECT r.week_start, r.employee_id, r.full_name, r.team, r.level, r.manager_employee_id,
       r.window_start, r.window_end, r.workdays_in_window, r.available_days, r.fte, r.available_fte_weeks,
       r.copilot_generations, r.copilot_acceptances, r.copilot_acceptance_rate, r.copilot_agent_days,
       r.has_copilot_data, r.merged_prs, r.merged_prs_per_fte_week, r.median_pr_size, r.reviews_given,
       r.eligible, r.exclusion_reason, r.pct_copilot, r.pct_prs, r.composite_score,
       r.overall_rank, r.eligible_count,
       prev.overall_rank - r.overall_rank,
       COALESCE(r.position_from_bottom <= CEIL(r.bottom_share * r.eligible_count), false),
       r.on_open_pip
FROM ranked r
LEFT JOIN mart.engineer_ranking_weekly prev
       ON prev.employee_id = r.employee_id
      AND prev.week_start  = r.week_start - 7;

COMMIT;


-- ---------------------------------------------------------------------
-- 8. Retention
-- ---------------------------------------------------------------------
-- Raw per-user Copilot rows: keep the scoring window plus two weeks of slack.
DELETE FROM raw.copilot_users_day
WHERE day < current_date - (SELECT (window_weeks + 2) * 7 FROM mart.ranking_params);
-- Snapshots in mart.engineer_ranking_weekly and decisions in hr.pip_flag_decisions:
-- keep them for the retention period in your DPIA. They are the record of what each PIP was based on.
```

### Setup notes
- **Identity:** join on GitHub user ID, not login, because logins change. `ref.engineers.github_user_id` must be filled for everyone, or that engineer gets no Copilot or PR data and lands at the bottom. After the first run, look for engineers with zero Copilot events and zero PRs on page 1. Those are almost always mapping gaps.
- **Database logins:** each viewer needs their own database login listed in `ref.app_users`. If your BI tool (Power BI, Looker, Metabase) connects through one service account, recreate the visibility rule in the BI tool's row-level security instead.
- **Time zone:** set the database session time zone to `Europe/Amsterdam`, so that PRs merged late on Sunday evening land in the right week.
- **Absence data:** if the HRIS export only covers sick leave and not holiday leave, people come back from holiday into the bottom 10%. Load both.

Some changes are a single parameter: weights, window, threshold, or ranking within level instead of across all 120. For ranking within level, add `level` to every `PARTITION BY` in the `pct` and `ranked` steps, and give `eligible_count` a `PARTITION BY level` too. If you want help wiring this into your BI tool, tell me which one.
