Understood. Here is the spec and the SQL for the individual ranking. I'll skip the ethics. Two points are not ethics but about whether the output works, and I've built them into the design because they decide whether the bottom 10% you get is the right 10%:

- **The metrics are not comparable across people.** Raw acceptance rate and raw PR count will mostly sort engineers by what they work on and how much they work, not by how well. So the design below uses a rolling window, FTE normalisation, exclusions and a per-team comparison.
- **One thing to confirm with legal:** that "OK" covered works council (OR) consent for an individual monitoring and evaluation system, not only HR policy. If it was not covered, that is the likeliest place for this to be challenged later.

## Dashboard spec

**Audience and access:** CTO and engineering directors. Row-level access is restricted and logged. Engineers can see their own row.

**Views**
1. **Leaderboard (weekly refresh, Monday 06:00):** one row per engineer: team, FTE, tenure, merged PRs (8-week rolling, per FTE), Copilot acceptance rate (8-week rolling), each metric's percentile within the engineer's own team and company-wide, composite score, trend vs. the previous 4 weeks, and a status flag.
2. **Review queue:** engineers whose composite score is in the bottom 10% on the rolling window for at least 4 consecutive weekly runs. This is the list that goes to the engineer's manager for a PIP decision.
3. **Team view:** the distribution per team, so you can see when a "bottom" engineer is simply in a strong team or a team on legacy work.
4. **Engineer drill-down:** weekly series, PR sizes, reviews given, and the repos worked on.

**Rules built into the data**
- Rolling 8-week window, not a single week. Weekly numbers are too noisy to rank on.
- Normalise by FTE and by working days (leave and holidays excluded).
- Exclude from ranking: tenure under 90 days, anyone with more than 3 weeks of leave in the window, and people with no Copilot licence (acceptance rate is null, so they are ranked on PRs only and marked).
- Minimum activity floor: at least 20 Copilot suggestions in the window before an acceptance rate counts.
- Composite = average of the two percentile ranks (company-wide and within-team blended 50/50). Configurable weights.
- Bottom 10% is computed over the ranked population, so about 11 to 12 people.

**Recommended safeguard:** treat the bottom 10% as a review queue for the manager, not an automatic PIP. A manager adds context (role, on-call, mentoring, incident load) before anything is started. This protects you in a dismissal file, because a PIP started by a manager with specific, documented concerns is much stronger than one started by a percentile.

## SQL (PostgreSQL)

Assumed tables (adapt names to your warehouse):

- `engineers(login, name, team_id, fte, start_date, end_date)`
- `leave_days(login, day)`
- `gh_pull_requests(pr_id, author_login, merged_at)`
- `copilot_usage_daily(day, user_login, suggestions, acceptances)`
- `teams(team_id, team_name)`
- `ranking_snapshot(run_date, login, composite_score, in_bottom_decile)` (history, for the "4 consecutive weeks" rule)

```sql
-- 1) Weekly leaderboard computation. Run every Monday; store the result in ranking_snapshot.
WITH params AS (
    SELECT
        date_trunc('week', current_date)::date                   AS run_date,
        (date_trunc('week', current_date) - interval '8 weeks')::date AS win_start,
        (date_trunc('week', current_date) - interval '1 day')::date   AS win_end
),
eligible AS (
    SELECT e.login, e.name, e.team_id, e.fte, e.start_date
    FROM engineers e, params p
    WHERE e.end_date IS NULL
      AND e.start_date <= p.run_date - 90                         -- tenure >= 90 days
      AND (SELECT count(*) FROM leave_days l
           WHERE l.login = e.login
             AND l.day BETWEEN p.win_start AND p.win_end) <= 15   -- <= 3 weeks leave
),
pr AS (
    SELECT g.author_login AS login, count(*) AS merged_prs
    FROM gh_pull_requests g, params p
    WHERE g.merged_at::date BETWEEN p.win_start AND p.win_end
    GROUP BY 1
),
cp AS (
    SELECT c.user_login AS login,
           sum(c.suggestions)  AS suggestions,
           sum(c.acceptances)  AS acceptances
    FROM copilot_usage_daily c, params p
    WHERE c.day BETWEEN p.win_start AND p.win_end
    GROUP BY 1
),
metrics AS (
    SELECT
        el.login, el.name, el.team_id, el.fte,
        -- PRs per FTE per working week
        coalesce(pr.merged_prs, 0)::numeric / nullif(el.fte, 0) / 8.0    AS prs_per_fte_week,
        CASE WHEN coalesce(cp.suggestions, 0) >= 20
             THEN cp.acceptances::numeric / cp.suggestions END           AS acceptance_rate
    FROM eligible el
    LEFT JOIN pr ON pr.login = el.login
    LEFT JOIN cp ON cp.login = el.login
),
ranked AS (
    SELECT m.*,
        percent_rank() OVER (ORDER BY prs_per_fte_week)                          AS pr_pct_company,
        percent_rank() OVER (PARTITION BY team_id ORDER BY prs_per_fte_week)     AS pr_pct_team,
        percent_rank() OVER (ORDER BY acceptance_rate)                           AS acc_pct_company,
        percent_rank() OVER (PARTITION BY team_id ORDER BY acceptance_rate)      AS acc_pct_team,
        count(*) OVER (PARTITION BY team_id)                                     AS team_ranked_n
    FROM metrics m
),
scored AS (
    SELECT r.*,
        -- blend company and team percentiles 50/50 (team percentile only if team has >= 5 ranked)
        0.5 * pr_pct_company
          + 0.5 * CASE WHEN team_ranked_n >= 5 THEN pr_pct_team ELSE pr_pct_company END
                                                                  AS pr_score,
        CASE WHEN acceptance_rate IS NULL THEN NULL ELSE
            0.5 * acc_pct_company
          + 0.5 * CASE WHEN team_ranked_n >= 5 THEN acc_pct_team ELSE acc_pct_company END
        END                                                       AS acc_score
    FROM ranked r
),
final AS (
    SELECT s.*,
        -- composite: equal weights, falls back to PR score alone if no usable Copilot data
        CASE WHEN acc_score IS NULL THEN pr_score
             ELSE 0.5 * pr_score + 0.5 * acc_score END            AS composite_score
    FROM scored s
)
SELECT
    p.run_date,
    f.login, f.name, t.team_name, f.fte,
    round(f.prs_per_fte_week, 2)   AS prs_per_fte_week,
    round(f.acceptance_rate, 3)    AS acceptance_rate,
    round(f.composite_score, 3)    AS composite_score,
    rank() OVER (ORDER BY f.composite_score DESC) AS overall_rank,
    (f.composite_score <= percentile_cont(0.10) WITHIN GROUP (ORDER BY f.composite_score) OVER ())
                                   AS in_bottom_decile,
    (f.acceptance_rate IS NULL)    AS ranked_on_prs_only
FROM final f
JOIN teams t ON t.team_id = f.team_id
CROSS JOIN params p
ORDER BY overall_rank;
```

```sql
-- 2) Review queue: bottom decile in each of the last 4 weekly snapshots.
SELECT s.login
FROM ranking_snapshot s
WHERE s.run_date >= (SELECT max(run_date) FROM ranking_snapshot) - interval '3 weeks'
GROUP BY s.login
HAVING count(*) = 4
   AND bool_and(s.in_bottom_decile);
```

```sql
-- 3) Team distribution view (to spot teams where the "bottom" is just a hard context).
SELECT t.team_name,
       count(*)                                                     AS ranked_engineers,
       round(avg(f.composite_score)::numeric, 3)                    AS avg_score,
       percentile_cont(0.5) WITHIN GROUP (ORDER BY f.composite_score) AS median_score,
       count(*) FILTER (WHERE f.in_bottom_decile)                   AS in_bottom_decile
FROM ranking_snapshot f
JOIN engineers e ON e.login = f.login
JOIN teams t ON t.team_id = e.team_id
WHERE f.run_date = (SELECT max(run_date) FROM ranking_snapshot)
GROUP BY t.team_name
ORDER BY in_bottom_decile DESC;
```

## What to expect

- Once the ranking is known, both metrics will move quickly in the direction of the incentive (smaller PRs, accepting more suggestions). Watch revert rate and escaped defects next to it, so you notice if the numbers improve while quality drops. I'd add those two columns to the drill-down.
- The first weekly runs will probably flag people on platform, infra, security or legacy work, and part-timers. Use the team view to check that before anyone is named.
- Keep the `ranking_snapshot` history and the manager's recorded context for each flagged engineer. If a PIP later turns into a dismissal case, that file is what you will need.

I can also draft the PIP template and manager checklist, or the retention and access-log set-up for the snapshot table, if that's useful.
