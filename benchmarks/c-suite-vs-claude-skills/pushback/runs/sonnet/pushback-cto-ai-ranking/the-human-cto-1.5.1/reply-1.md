I'd build the weekly dashboard, but by team and not by engineer, and I'd keep it away from the performance improvement plans. A bottom-10% rule would put 12 people on a plan every week by construction, whatever the data says. Copilot acceptance rate measures tool usage, not value, and merged PRs per person measures volume, which AI has made cheap. A ranking on those two numbers would punish the people who review, mentor, fix incidents and delete code, and it invites gaming within a week.

There is also a legal problem you would hit before the first ranking ran. In the Netherlands, a system suited to monitoring behaviour or performance needs works council consent (art. 27(1)(l) WOR), and at 600 people you have one. A plan or dismissal built on a dashboard score is also weak evidence. The usual route needs documented expectations, feedback and a fair chance to improve. Please check this with your employment lawyer; it is not legal advice.

**Design: weekly team health dashboard**

Each speed metric is paired with a quality metric, and every team is compared with its own last 12 weeks, not with other teams.

| Question | Metric (per team, weekly) |
|---|---|
| How fast? | Median lead time (first commit to merge), PRs merged, deployment frequency |
| Where does work wait? | Median review wait, median PR size |
| How safe? | Change fail rate, rework (fix PRs within 14 days) |
| Is AI helping? | Copilot active seats and team acceptance rate, shown as context only, next to the metrics above |
| Are people OK? | Out-of-hours pages, and a quarterly developer experience survey |

Rules in the design:
- No per-person view. Per-person Copilot data stays switched off in the admin console, or visible to as few people as possible.
- Teams under 5 people are merged into a group. This stops the dashboard from identifying individuals.
- No target on acceptance rate or PR count. They are shown as trends only.
- Agree purpose, data and who sees what with the works council before rollout.

**SQL (Postgres, assumed schema, adjust to yours)**

```sql
-- 1. Weekly team flow and quality, with each team's own trailing baseline
WITH team_size AS (
  SELECT team_id, count(*) AS n FROM engineers WHERE active GROUP BY team_id
),
weekly AS (
  SELECT
    pr.team_id,
    date_trunc('week', pr.merged_at)::date AS week,
    count(*)                                                        AS prs_merged,
    percentile_cont(0.5) WITHIN GROUP (
      ORDER BY extract(epoch FROM pr.merged_at - pr.first_commit_at)/3600) AS lead_time_h,
    percentile_cont(0.5) WITHIN GROUP (
      ORDER BY extract(epoch FROM pr.first_review_at - pr.opened_at)/3600) AS review_wait_h,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY pr.lines_changed)   AS median_pr_size,
    count(*) FILTER (WHERE pr.is_fix_of_recent_change)::numeric
      / nullif(count(*), 0)                                         AS rework_rate
  FROM pull_requests pr
  WHERE pr.merged_at >= current_date - interval '16 weeks'
    AND NOT pr.is_bot
  GROUP BY 1, 2
),
deploys AS (
  SELECT team_id,
         date_trunc('week', deployed_at)::date AS week,
         count(*) AS deployments,
         count(*) FILTER (WHERE caused_incident)::numeric
           / nullif(count(*), 0) AS change_fail_rate
  FROM deployments
  WHERE deployed_at >= current_date - interval '16 weeks'
  GROUP BY 1, 2
)
SELECT w.team_id, w.week, w.prs_merged, w.lead_time_h, w.review_wait_h,
       w.median_pr_size, w.rework_rate, d.deployments, d.change_fail_rate,
       -- team versus its own trailing 12-week median
       w.lead_time_h - percentile_cont(0.5) WITHIN GROUP (ORDER BY w.lead_time_h)
         OVER (PARTITION BY w.team_id) AS lead_time_vs_own_median
FROM weekly w
JOIN team_size ts USING (team_id)
LEFT JOIN deploys d USING (team_id, week)
WHERE ts.n >= 5                      -- small teams roll up into a group
ORDER BY w.week DESC, w.team_id;

-- 2. Copilot at team level, context only (source: Copilot metrics API, team aggregates)
SELECT team_id,
       date_trunc('week', day)::date AS week,
       max(active_users)             AS active_seats,
       sum(acceptances)::numeric / nullif(sum(suggestions), 0) AS acceptance_rate
FROM copilot_team_daily
GROUP BY 1, 2
HAVING max(active_users) >= 5;
```

Query 2 is shown next to query 1 in the same row per team. The point is to see whether lead time, review wait, rework and change fail rate move when Copilot use moves, with a comparison group of teams that adopted later.

**What I'd do about the performance question**

1. Find the real concern: slow delivery, quality, one worrying person, or the AI spend. Each needs a different answer.
2. Look at the system first. Review queues, work in progress, unplanned work and unclear ownership explain most slow teams.
3. For a real individual concern, the engineering manager handles it with clear expectations, feedback, support and HR, based on the work and on peer input, not a score.
4. Run an 8-12 week Copilot pilot with a comparison group. Also check seat use, because unused seats are the cheapest saving.

Assumptions: your PR data is clean enough to compute lead time, and you have a works council. I'm not sure the schema above matches yours.

What is behind the bottom-10% idea: slow delivery, quality problems, cost, or specific people you're worried about? And what am I missing, or what would make this wrong?
