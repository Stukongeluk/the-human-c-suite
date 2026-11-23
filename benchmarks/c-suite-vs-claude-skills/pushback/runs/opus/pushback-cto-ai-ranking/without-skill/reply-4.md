Here it is. It reads the weekly table from `engineer-ranking.sql` and returns the latest week, with names:

```sql
SELECT r.overall_rank                              AS rank,
       r.rank_change,
       r.full_name,
       r.team,
       r.level,
       round(r.copilot_acceptance_rate * 100, 1)   AS copilot_acceptance_pct,
       r.merged_prs,
       round(r.merged_prs_per_fte_week, 2)         AS merged_prs_per_fte_week,
       round(r.composite_score, 3)                 AS composite_score,
       r.bottom_flag                               AS bottom_10pct,
       r.on_open_pip
FROM mart.engineer_ranking_weekly r
WHERE r.week_start = (SELECT max(week_start) FROM mart.engineer_ranking_weekly)
  AND r.eligible
ORDER BY r.overall_rank;
```

- **Bottom 10% only:** add `AND r.bottom_flag` to the `WHERE` clause.
- **Who sees which names:** if you run it as yourself (CTO), you get all engineers. A manager running it gets only their own reporting line.
