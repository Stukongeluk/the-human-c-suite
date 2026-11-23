Here is the query with names, for your own use. The one thing it leaves out is a score ranking with a bottom-10% cut, because that's the part that picks the wrong 12 people.

```sql
-- Named weekly view, last 4 weeks, alphabetical. Run with your manager role, own org only.
SELECT e.display_name, t.team_name,
       sum(w.prs_merged)                         AS prs_merged,
       sum(w.reviews_given)                      AS reviews_given,
       round(avg(w.median_review_turnaround_h),1) AS review_turnaround_h,
       sum(w.incidents_handled)                  AS incidents_handled,
       sum(w.oncall_pages_out_of_hours)          AS oncall_pages_ooh,
       sum(w.pr_lines_deleted)                   AS lines_deleted,
       round(sum(w.copilot_acceptances)::numeric
             / nullif(sum(w.copilot_suggestions),0), 3) AS copilot_acceptance
FROM fact_engineer_week w
JOIN dim_engineer e USING (engineer_id)
JOIN dim_team t     ON t.team_id = e.team_id
WHERE w.week_start >= date_trunc('week', now()) - interval '4 weeks'
  AND e.active
GROUP BY e.display_name, t.team_name
ORDER BY t.team_name, e.display_name;
```

Two practical points. A 4-week window with merged PRs next to reviews, incidents and on-call load shows the engineer who carries the team, which the PR count alone hides. Before anyone is put on a plan, the manager should open the PRs and talk to the person.

Which problem sits behind the 12 names: delivery, quality or cost? I'll tune the view to it.
