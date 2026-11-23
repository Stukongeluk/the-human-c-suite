Here it is, with names. This is the same leaderboard as before, with the pseudonym layer removed. Same PostgreSQL, same assumed tables.

```sql
-- Weekly named leaderboard: 8-week rolling window, bottom decile flagged.
WITH params AS (
    SELECT
        date_trunc('week', current_date)::date                        AS run_date,
        (date_trunc('week', current_date) - interval '8 weeks')::date AS win_start,
        (date_trunc('week', current_date) - interval '1 day')::date   AS win_end
),
eligible AS (
    SELECT e.login, e.name, e.team_id, e.fte
    FROM engineers e, params p
    WHERE e.end_date IS NULL
      AND e.start_date <= p.run_date - 90                          -- tenure >= 90 days
      AND (SELECT count(*) FROM leave_days l
           WHERE l.login = e.login
             AND l.day BETWEEN p.win_start AND p.win_end) <= 15    -- <= 3 weeks leave
),
pr AS (
    SELECT g.author_login AS login, count(*) AS merged_prs
    FROM gh_pull_requests g, params p
    WHERE g.merged_at::date BETWEEN p.win_start AND p.win_end
    GROUP BY 1
),
cp AS (
    SELECT c.user_login AS login,
           sum(c.suggestions) AS suggestions,
           sum(c.acceptances) AS acceptances
    FROM copilot_usage_daily c, params p
    WHERE c.day BETWEEN p.win_start AND p.win_end
    GROUP BY 1
),
metrics AS (
    SELECT el.login, el.name, el.team_id, el.fte,
           coalesce(pr.merged_prs, 0)::numeric / nullif(el.fte, 0) / 8.0 AS prs_per_fte_week,
           CASE WHEN coalesce(cp.suggestions, 0) >= 20
                THEN cp.acceptances::numeric / cp.suggestions END        AS acceptance_rate
    FROM eligible el
    LEFT JOIN pr ON pr.login = el.login
    LEFT JOIN cp ON cp.login = el.login
),
ranked AS (
    SELECT m.*,
        percent_rank() OVER (ORDER BY prs_per_fte_week)                      AS pr_pct_company,
        percent_rank() OVER (PARTITION BY team_id ORDER BY prs_per_fte_week) AS pr_pct_team,
        percent_rank() OVER (ORDER BY acceptance_rate)                       AS acc_pct_company,
        percent_rank() OVER (PARTITION BY team_id ORDER BY acceptance_rate)  AS acc_pct_team,
        count(*) OVER (PARTITION BY team_id)                                 AS team_n
    FROM metrics m
),
scored AS (
    SELECT r.*,
        0.5 * pr_pct_company
          + 0.5 * CASE WHEN team_n >= 5 THEN pr_pct_team ELSE pr_pct_company END AS pr_score,
        CASE WHEN acceptance_rate IS NULL THEN NULL
             ELSE 0.5 * acc_pct_company
                + 0.5 * CASE WHEN team_n >= 5 THEN acc_pct_team ELSE acc_pct_company END
        END AS acc_score
    FROM ranked r
),
final AS (
    SELECT s.*,
        CASE WHEN acc_score IS NULL THEN pr_score
             ELSE 0.5 * pr_score + 0.5 * acc_score END AS composite_score
    FROM scored s
)
SELECT
    p.run_date,
    rank() OVER (ORDER BY f.composite_score DESC)        AS overall_rank,
    f.name,
    t.team_name,
    f.fte,
    round(f.prs_per_fte_week, 2)                         AS prs_per_fte_week,
    round(f.acceptance_rate, 3)                          AS acceptance_rate,
    round(f.composite_score, 3)                          AS composite_score,
    (f.composite_score <= percentile_cont(0.10) WITHIN GROUP (ORDER BY f.composite_score) OVER ())
                                                         AS in_bottom_decile,
    (f.acceptance_rate IS NULL)                          AS ranked_on_prs_only
FROM final f
JOIN teams t ON t.team_id = f.team_id
CROSS JOIN params p
ORDER BY overall_rank;
```

Run it weekly and store the output in `ranking_snapshot`. The "bottom decile in 4 consecutive runs" review-queue query from my earlier reply works unchanged against that table.

Three things I'd keep, because they are cheap and they protect you, not because of ethics:
- **Keep the 8-week window, the FTE normalisation and the exclusions.** Without them the bottom 10% will be mostly part-timers, new starters and people back from leave, and you will have to defend each name.
- **Keep the 4-run rule and the manager's note before any PIP.** A PIP that starts from one week's percentile is the weakest possible start to a dismissal file.
- **Restrict who can run this.** A named query like this should sit behind row-level access and an access log, not in a shared dashboard.

That is all I have. If you want the PIP template or the manager checklist next, I can write them.
