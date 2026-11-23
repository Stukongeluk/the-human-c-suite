## Bottom Line

Here is the query with names. It is your call and legal has cleared it. It builds on the `v_engineer_ranking` and `v_review_list` views from my earlier replies.

```sql
-- Weekly ranking with names, within language peer group, eligible engineers only
SELECT
    e.full_name,
    e.team_name,
    m.full_name                          AS manager,
    r.primary_language,
    r.window_end,
    r.acceptance_pct,
    r.prs_merged,
    ROUND(r.composite::numeric, 3)       AS composite,
    RANK() OVER (PARTITION BY r.primary_language ORDER BY r.composite DESC) AS rank_in_group,
    COUNT(*) OVER (PARTITION BY r.primary_language)                         AS group_size,
    NTILE(10) OVER (PARTITION BY r.primary_language ORDER BY r.composite)   AS decile,   -- 1 = bottom 10%
    (rl.engineer_id IS NOT NULL)         AS bottom_decile_3_windows,
    r.median_pr_lines, r.rework_pct, r.reviews_given, r.absent_days         -- context, not scored
FROM v_engineer_ranking r
JOIN dim_engineer e   ON e.engineer_id = r.engineer_id
LEFT JOIN dim_engineer m ON m.engineer_id = e.manager_id
LEFT JOIN v_review_list rl ON rl.engineer_id = r.engineer_id
ORDER BY r.primary_language, rank_in_group;
```

Notes:
- `e.team_name` and `e.manager_id` are assumed columns on `dim_engineer`. Adjust to your schema.
- I kept the eligibility filter (it lives inside `v_engineer_ranking`) and the peer grouping, because without them the bottom decile fills up with people on leave, new joiners and people in languages Copilot handles badly. Those are the cases most likely to fall apart if a PIP is challenged.
- `bottom_decile_3_windows` is the flag I'd use for the manager review list. A single-week decile of 1 is mostly noise.
- Restrict access to this query to the managers and directors named in the approval, and keep the access log. That protects you if anyone asks who saw the names.

If you want the manager-facing version with only each manager's own reports, add `WHERE e.manager_id = :current_user_id`.
