**BOTTOM LINE**
Here's the query with names. It reads the latest weekly snapshot; run it from your CTO login. 🟢 I ran it on the test data.

```sql
SELECT display_name,
       team,
       job_level,
       rank_from_top,
       peer_group_size,
       composite_score,
       merged_prs,
       merged_prs_per_available_day,
       copilot_acceptance_rate,
       in_bottom,
       weeks_in_bottom_last_8,
       on_active_pip,
       manager_decision,
       status
FROM perf.v_ranking_current
ORDER BY peer_group, rank_from_top NULLS LAST, display_name;
```

For the bottom 10% only, add `WHERE in_bottom` before the `ORDER BY`.

**HOW TO ACT**
Run it as a user with the `perf_full_reader` role, which is you and HR. Other logins get "permission denied".
