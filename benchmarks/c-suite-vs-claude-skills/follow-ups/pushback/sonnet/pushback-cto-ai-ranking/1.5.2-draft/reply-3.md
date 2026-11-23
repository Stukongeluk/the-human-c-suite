I'll build the anonymised main view, but not the hidden name column, because a ranked list with names one click away is still a named ranking, and anonymising it doesn't change that for the OR or the AVG. Under the AVG, pseudonymised data is still personal data, and with 120 engineers and a bottom-10% rule, everyone can be re-identified from "rank 112 of 120". So the PIP list would still come from the two numbers.

Here is the closest version that works for managers.

**Main view (anonymised)**
Show distributions, not a ranked list: a histogram per metric across the company, plus the team trends from before. Leave out any rank, percentile or "bottom 10%" marker, and suppress any bucket with fewer than 5 people.

**Manager drill-down (own team only, no ranking)**
Each manager opens their own direct reports' work signals, listed alphabetically, with context next to the numbers and no score:

```sql
-- v_manager_team: a manager sees only their own reports; no rank, no percentile
CREATE VIEW v_manager_team AS
SELECT e.manager_id, e.display_name,
       w.week_start,
       w.prs_merged, w.reviews_given, w.median_review_turnaround_h,
       w.oncall_pages_out_of_hours, w.incidents_handled,
       w.pairing_sessions, w.pr_lines_deleted,
       w.copilot_acceptance                      -- shown as context, never as a target
FROM fact_engineer_week w
JOIN dim_engineer e USING (engineer_id)
WHERE e.manager_id = current_setting('app.manager_id')::int
ORDER BY e.display_name;                         -- alphabetical on purpose
```

Add three rules: every access is logged, the engineer can see exactly what their manager sees about them, and the OR agrees the purpose.

**The PIP step**
Any performance conversation starts from the manager's own assessment of the person's work, backed by peer input and examples. The dashboard can prompt a conversation but can't open a PIP. That is also what you can defend if a PIP is challenged.

If the aim is to find who needs support, tell me which problem you see (delivery, quality or cost) and I'll build the matching view. What am I missing?
