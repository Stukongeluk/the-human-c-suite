I'd build the weekly dashboard at team level and not rank the 120 engineers: ranking people by Copilot acceptance rate and merged PRs, with the bottom 10% (12 people) put on a PIP, would measure tool usage and PR volume rather than performance, and in the Netherlands it can't be introduced the way you describe. The design and SQL below give you the weekly view without those problems.

**Why the individual ranking fails**
- **Acceptance rate measures tool usage, not value.** It can rise while quality falls. DORA's 2025 report found AI amplifies what a team already is, and that instability stayed up even where throughput improved.
- **Merged PRs per person reward volume, and AI makes volume cheap.** In Faros AI telemetry from 10,000+ developers (2025), high-adoption teams merged 98% more PRs while review time rose 91%. Faros sells engineering analytics, so treat that as indicative.
- **The bottom 10% will be the wrong people.** They are the people who review, mentor, take on-call, fix incidents and delete code, and the platform and security engineers whose work doesn't produce merged PRs. Everyone else will learn to optimise the two numbers.
- **Dutch law.** At 600 employees you have a works council (OR). A system suited to monitoring individual behaviour or performance needs its consent (art. 27(1)(l) WOR). A PIP built on a dashboard score would also be hard to defend as a fair process. The AVG (GDPR) purpose-limitation and transparency rules apply too. I'm not a lawyer, so check this with HR and employment counsel.

**What I'd build: a weekly team health dashboard**

| Panel | Metrics | Compare with |
|---|---|---|
| Flow | change lead time, PR cycle time, review wait time, PR size, WIP | the team's own last 12 weeks |
| Quality | change fail rate, time to restore, rework rate, escaped defects | same |
| Health | out-of-hours pages per rotation, developer-experience survey score | same |
| AI adoption (diagnostic) | weekly active Copilot seats, team acceptance rate | quality and flow, not a target |

Design rules:
- **Grain.** Aggregate to team level on ingestion, and don't store per-user Copilot data in the warehouse. A minimum group of 5, so small teams are suppressed.
- **Display.** Trends against each team's own past, no cross-team league table.
- **Access.** Limit the per-person views in the GitHub admin console to the few admins who need them.
- **Agreement.** Agree purpose, data and access with the OR before launch.

**SQL (Postgres, assumed schema)**
Adjust the table and column names to yours.

```sql
-- Weekly team flow and quality; teams under 5 engineers are suppressed
WITH weeks AS (
  SELECT generate_series(date_trunc('week', now()) - interval '12 weeks',
                         date_trunc('week', now()) - interval '1 week',
                         interval '1 week') AS week_start
),
team_size AS (
  SELECT team_id, count(*) AS engineers
  FROM dim_engineer_team WHERE active GROUP BY team_id
),
pr AS (
  SELECT team_id, date_trunc('week', merged_at) AS week_start,
         count(*)                                                         AS prs_merged,
         percentile_cont(0.5) WITHIN GROUP
           (ORDER BY extract(epoch FROM merged_at - created_at)/3600)     AS median_cycle_h,
         percentile_cont(0.5) WITHIN GROUP
           (ORDER BY extract(epoch FROM first_review_at - created_at)/3600) AS median_review_wait_h,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY lines_changed)       AS median_pr_size
  FROM fact_pull_request
  WHERE merged_at >= now() - interval '13 weeks'
  GROUP BY 1, 2
),
dep AS (
  SELECT team_id, date_trunc('week', deployed_at) AS week_start,
         count(*)                                            AS deploys,
         avg((failed)::int)                                  AS change_fail_rate,
         percentile_cont(0.5) WITHIN GROUP
           (ORDER BY extract(epoch FROM restored_at - deployed_at)/3600)
           FILTER (WHERE failed)                             AS median_restore_h
  FROM fact_deployment
  WHERE deployed_at >= now() - interval '13 weeks'
  GROUP BY 1, 2
),
ai AS (   -- already aggregated per team at ingestion
  SELECT team_id, date_trunc('week', day) AS week_start,
         sum(acceptances)::numeric / nullif(sum(suggestions), 0) AS acceptance_rate,
         max(active_seats)                                        AS active_seats
  FROM fact_copilot_team_daily
  WHERE day >= now() - interval '13 weeks'
  GROUP BY 1, 2
)
SELECT t.team_name, w.week_start,
       pr.prs_merged, pr.median_cycle_h, pr.median_review_wait_h, pr.median_pr_size,
       dep.deploys, dep.change_fail_rate, dep.median_restore_h,
       ai.acceptance_rate, ai.active_seats
FROM dim_team t
JOIN team_size ts USING (team_id)
CROSS JOIN weeks w
LEFT JOIN pr  ON pr.team_id  = t.team_id AND pr.week_start  = w.week_start
LEFT JOIN dep ON dep.team_id = t.team_id AND dep.week_start = w.week_start
LEFT JOIN ai  ON ai.team_id  = t.team_id AND ai.week_start  = w.week_start
WHERE ts.engineers >= 5
ORDER BY t.team_name, w.week_start;
```

Chart each team against its own previous 12 weeks. Read acceptance rate next to change fail rate and review wait. If acceptance goes up while fail rate also goes up, that's the signal worth discussing.

**If the real concern is specific people**
Their manager handles it through clear expectations, regular feedback, support and a fair chance, with HR involved. The evidence comes from their actual work and from peers, not from a dashboard score. A PIP that follows a score can't explain itself to the person, to the OR or to a court.

**Two questions that would change my answer**
1. What is behind this: slow delivery, quality problems, a cost target, or a few specific people a manager worries about? Each has a different fix, and none of them is "rank everyone".
2. Does the OR already know about this plan? If not, I'd speak to them first, with these numbers.

**Assumptions:** the schema above is a guess, and I haven't seen your pipelines, incident data or GitHub admin settings. I'd start by connecting read-only to the Git host, CI/CD and incident tool. What am I missing, and what would make this wrong?
