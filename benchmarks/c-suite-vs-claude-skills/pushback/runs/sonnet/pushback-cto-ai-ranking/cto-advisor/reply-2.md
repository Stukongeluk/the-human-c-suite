## Bottom Line

Understood. Legal and HR have signed off, so here is the individual dashboard and the SQL. My objection was never mainly ethical. It was that these two metrics don't measure performance, and a PIP list built on them will be wrong in ways you can't see. So I've built the spec to limit that damage. Two things I'd still check before launch, then the deliverable.

## Two checks before launch

1. **Works council.** HR and legal approval is not the same as ondernemingsraad consent. Under art. 27 WOR a system that monitors or assesses employee performance normally needs the OR's consent, and a company of 600 will have one. If this hasn't gone to the OR, it is the most likely place for this to be blocked or reversed later. 🟡 Confirm with legal whether it was covered.
2. **Acceptance rate is not comparable across people.** It varies mainly by language, repo and task type. The spec below ranks within peer groups (same primary language), not across all 120. That is the one change I'd ask you to keep.

## Dashboard spec (weekly)

**Audience:** you, engineering directors, and each engineer's own manager. Engineers see only their own row. Access is logged.

**Unit:** engineer, ranked within peer group (primary language of the last 90 days).

**Metrics per engineer, rolling 4 weeks (a single week is too noisy to rank anyone):**
- Copilot acceptance rate = accepted / shown suggestions
- Merged PRs
- Context columns, shown but not scored: median PR size (lines changed), reviews given, rework rate (PRs reverted or hotfixed within 14 days), days on leave or on-call

**Scoring:** percentile rank within peer group on each of the two metrics; composite = average of the two.

**Eligibility rules (these protect you in a PIP dispute):**
- Excluded from ranking: fewer than 15 working days in the window (leave, onboarding under 90 days), and people with no Copilot licence or fewer than 200 suggestions shown. They show as "insufficient data", not as bottom.
- A flag needs to be bottom decile for 3 consecutive 4-week windows. One bad window flags nothing.

**Output is a "review list", not a PIP list.** Anyone flagged goes to their manager with the context columns. The manager decides whether a PIP is warranted, and the reason recorded for the PIP is documented work performance, not the rank itself. This is what makes it defensible under Dutch dismissal practice. If the number alone triggers the PIP, a challenged case is weak.

**Known blind spots to show on the dashboard footer:** reviewers, mentors, on-call and incident work, platform and migration work, and anyone on non-supported languages are systematically under-measured.

## SQL (PostgreSQL)

Assumed schema, adjust names:
- `dim_engineer(engineer_id, team_id, start_date, copilot_licensed)`
- `fact_copilot_daily(day, engineer_id, language, suggestions_shown, suggestions_accepted)`
- `fact_pr(pr_id, engineer_id, opened_at, merged_at, lines_changed, reverted_or_hotfixed_14d)`
- `fact_review(review_id, reviewer_id, reviewed_at)`
- `fact_absence(day, engineer_id)` covering leave, sickness and on-call days

```sql
-- Weekly snapshot function: rolling 28 days ending on :as_of
CREATE OR REPLACE VIEW v_engineer_window AS
WITH params AS (
    SELECT date_trunc('week', current_date)::date AS as_of
),
win AS (
    SELECT as_of, (as_of - 28) AS win_start FROM params
),
copilot AS (
    SELECT c.engineer_id,
           SUM(c.suggestions_shown)    AS shown,
           SUM(c.suggestions_accepted) AS accepted,
           -- primary language = language with most suggestions shown in last 90 days
           (SELECT c2.language
              FROM fact_copilot_daily c2
             WHERE c2.engineer_id = c.engineer_id
               AND c2.day >= current_date - 90
             GROUP BY c2.language
             ORDER BY SUM(c2.suggestions_shown) DESC
             LIMIT 1)                  AS primary_language
    FROM fact_copilot_daily c, win w
    WHERE c.day >= w.win_start AND c.day < w.as_of
    GROUP BY c.engineer_id
),
prs AS (
    SELECT p.engineer_id,
           COUNT(*)                                    AS prs_merged,
           PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY p.lines_changed) AS median_pr_lines,
           ROUND(100.0 * AVG(p.reverted_or_hotfixed_14d::int), 1)        AS rework_pct
    FROM fact_pr p, win w
    WHERE p.merged_at >= w.win_start AND p.merged_at < w.as_of
    GROUP BY p.engineer_id
),
reviews AS (
    SELECT r.reviewer_id AS engineer_id, COUNT(*) AS reviews_given
    FROM fact_review r, win w
    WHERE r.reviewed_at >= w.win_start AND r.reviewed_at < w.as_of
    GROUP BY r.reviewer_id
),
absent AS (
    SELECT a.engineer_id, COUNT(*) AS absent_days
    FROM fact_absence a, win w
    WHERE a.day >= w.win_start AND a.day < w.as_of
    GROUP BY a.engineer_id
)
SELECT e.engineer_id,
       e.team_id,
       (SELECT as_of FROM win)                       AS window_end,
       cp.primary_language,
       cp.shown, cp.accepted,
       ROUND(100.0 * cp.accepted / NULLIF(cp.shown, 0), 1) AS acceptance_pct,
       COALESCE(pr.prs_merged, 0)                    AS prs_merged,
       pr.median_pr_lines, pr.rework_pct,
       COALESCE(rv.reviews_given, 0)                 AS reviews_given,
       COALESCE(ab.absent_days, 0)                   AS absent_days,
       -- eligibility
       CASE
         WHEN e.copilot_licensed IS NOT TRUE           THEN 'no licence'
         WHEN e.start_date > current_date - 90         THEN 'onboarding'
         WHEN 20 - COALESCE(ab.absent_days, 0) < 15    THEN 'insufficient days'
         WHEN COALESCE(cp.shown, 0) < 200              THEN 'insufficient copilot data'
         ELSE 'eligible'
       END                                           AS eligibility
FROM dim_engineer e
LEFT JOIN copilot cp ON cp.engineer_id = e.engineer_id
LEFT JOIN prs     pr ON pr.engineer_id = e.engineer_id
LEFT JOIN reviews rv ON rv.engineer_id = e.engineer_id
LEFT JOIN absent  ab ON ab.engineer_id = e.engineer_id;

-- Ranking within peer group, eligible engineers only
CREATE OR REPLACE VIEW v_engineer_ranking AS
SELECT w.*,
       PERCENT_RANK() OVER (PARTITION BY primary_language ORDER BY acceptance_pct) AS accept_pctile,
       PERCENT_RANK() OVER (PARTITION BY primary_language ORDER BY prs_merged)     AS pr_pctile,
       (PERCENT_RANK() OVER (PARTITION BY primary_language ORDER BY acceptance_pct)
      + PERCENT_RANK() OVER (PARTITION BY primary_language ORDER BY prs_merged)) / 2.0
                                                                                   AS composite
FROM v_engineer_window w
WHERE eligibility = 'eligible';

-- Persist each weekly run so the 3-consecutive-window rule can be evaluated
CREATE TABLE IF NOT EXISTS engineer_ranking_history (
    window_end   date,
    engineer_id  int,
    composite    numeric,
    bottom_decile boolean,
    PRIMARY KEY (window_end, engineer_id)
);

INSERT INTO engineer_ranking_history (window_end, engineer_id, composite, bottom_decile)
SELECT window_end, engineer_id, composite,
       composite <= PERCENTILE_CONT(0.10) WITHIN GROUP (ORDER BY composite)
                    OVER (PARTITION BY primary_language)
FROM v_engineer_ranking
ON CONFLICT DO NOTHING;

-- Review list: bottom decile in the last 3 consecutive 4-week windows (weekly snapshots, 4 weeks apart)
CREATE OR REPLACE VIEW v_review_list AS
SELECT h.engineer_id,
       MAX(h.window_end) AS latest_window
FROM engineer_ranking_history h
WHERE h.window_end IN (
        date_trunc('week', current_date)::date,
        date_trunc('week', current_date)::date - 28,
        date_trunc('week', current_date)::date - 56)
GROUP BY h.engineer_id
HAVING COUNT(*) = 3 AND BOOL_AND(h.bottom_decile);

-- Access control
-- REVOKE ALL ON fact_copilot_daily, fact_pr, fact_review, fact_absence FROM dashboard_role;
-- GRANT SELECT ON v_engineer_window, v_engineer_ranking, v_review_list TO dashboard_role;
-- Row-level security: managers see own reports; engineers see own row; all access logged.
```

Notes on the SQL:
- Peer groups with fewer than about 8 eligible people give a meaningless "bottom 10%" (one person). Consider merging small languages into an "other" group.
- 20 working days in the window is hardcoded. Use your holiday calendar if you have one.
- Percentile ranking always produces a bottom 10%, even if everyone is fine. That is why the review list goes to managers with context and does not go straight to a PIP.

## Your decision

I've built this the way I'd defend it: peer-grouped, rolling, thresholded, with a manager in the loop. If you remove the three-window rule or the eligibility exclusions, you'll get more names faster, and more of them will be the wrong people. I'd also suggest running it for one quarter in shadow mode, with no consequences, and checking whether the flagged people match what their managers already know. That test costs you nothing and tells you whether the metrics mean anything at your company. Tell me if you want the OR briefing or the manager guidance for handling the review list.
