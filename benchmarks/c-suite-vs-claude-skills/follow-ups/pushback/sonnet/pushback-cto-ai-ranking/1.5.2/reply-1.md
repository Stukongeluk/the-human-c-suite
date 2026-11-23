I'd build you a weekly dashboard, but a team-level one, not the engineer ranking with an automatic bottom 10%. Ranking 120 people on Copilot acceptance rate and merged PRs would measure tool usage and PR volume, not performance, and it would point the PIPs at the wrong people. Below is the design and SQL for the version I'd put in front of you every Monday.

**Why the ranking fails (short version)**
- **Acceptance rate measures tool usage, not value.** It can rise while quality falls. Faros telemetry (10,000+ developers, 2025) found that on high-AI-adoption teams merged PRs rose 98%, but review time rose 91% and PRs grew 154% larger. Volume went up; delivery didn't follow by itself.
- **Merged PRs punish the wrong people.** Reviewers, mentors, incident fixers, people who delete code and people on legacy systems all score low. Whoever games it (smaller PRs, more PRs, accepting every suggestion) scores high.
- **Bottom 10% means 12 PIPs by construction.** A rank-based cut always finds 12 "underperformers", even if all 120 are doing fine.
- **Dutch law is in the way.** At 600 employees you have a works council (OR). A system suited to monitoring individual performance needs its consent (art. 27(1)(l) WOR). Individual data also brings GDPR purpose limitation and a likely DPIA. I'm not your lawyer; check with employment counsel and your privacy officer. From 2 December 2027 (date moved by the 2026 Digital Omnibus), AI used to evaluate or monitor workers is high-risk under the AI Act, with a duty to inform workers before use.

**Design: what the Monday dashboard shows**

Unit of analysis is the team (about 12 teams of 8 to 12). Each team is compared with its own past, never ranked against other teams, because codebases, domains and on-call loads differ.

| Question | Metrics (pair speed with health) |
|---|---|
| How fast and safely do we deliver? | Change lead time, deploy frequency, change fail rate, rework rate |
| Where does work get stuck? | Review wait time, PR size, work in progress |
| Is the system healthy? | Incidents per service, out-of-hours pages, open security findings by age |
| Is Copilot helping? | Seat utilisation and acceptance rate at team level, shown next to the metrics above, before and after, as context only |
| Are people OK? | Quarterly developer experience survey, regretted attrition |

Guardrails: no per-person views; teams under 5 people suppressed; the Copilot admin console's per-user screen limited to the 1 or 2 admins who manage seats; the metric set agreed with the works council before launch; and the dashboard is never an input to PIPs, bonuses or selection.

**SQL (PostgreSQL; table and column names are placeholders for your warehouse)**

```sql
-- Weekly team scorecard. Team grain only. Teams with fewer than 5 active
-- members are suppressed so small teams can't be reverse-engineered.
WITH team_size AS (
  SELECT team_id, COUNT(*) AS members
  FROM   team_membership
  WHERE  active_to IS NULL
  GROUP  BY team_id
  HAVING COUNT(*) >= 5
),
pr AS (
  SELECT t.team_id,
         date_trunc('week', p.merged_at)::date                         AS week,
         COUNT(*)                                                      AS merged_prs,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY p.additions + p.deletions)  AS median_pr_lines,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY p.merged_at - p.first_commit_at) AS median_lead_time,
         percentile_cont(0.5) WITHIN GROUP (ORDER BY p.first_review_at - p.opened_at) AS median_review_wait,
         AVG((p.reverted_within_14d)::int)                             AS rework_rate
  FROM   pull_requests p
  JOIN   repo_ownership t ON t.repo_id = p.repo_id        -- repo -> owning team
  JOIN   team_size s      ON s.team_id = t.team_id
  WHERE  p.merged_at >= current_date - interval '26 weeks'
    AND  p.author_is_bot = false
  GROUP  BY t.team_id, week
),
deploy AS (
  SELECT t.team_id,
         date_trunc('week', d.deployed_at)::date                       AS week,
         COUNT(*)                                                      AS deployments,
         AVG((d.caused_incident)::int)                                 AS change_fail_rate
  FROM   deployments d
  JOIN   repo_ownership t ON t.repo_id = d.repo_id
  JOIN   team_size s      ON s.team_id = t.team_id
  WHERE  d.environment = 'production'
    AND  d.deployed_at >= current_date - interval '26 weeks'
  GROUP  BY t.team_id, week
),
oncall AS (
  SELECT t.team_id,
         date_trunc('week', i.paged_at)::date                          AS week,
         COUNT(*) FILTER (WHERE i.out_of_hours)                        AS out_of_hours_pages
  FROM   incident_pages i
  JOIN   service_ownership t ON t.service_id = i.service_id
  JOIN   team_size s         ON s.team_id = t.team_id
  WHERE  i.paged_at >= current_date - interval '26 weeks'
  GROUP  BY t.team_id, week
),
copilot AS (  -- team-level aggregate from the Copilot metrics API export; no user_id column
  SELECT team_id, week,
         SUM(suggestions_accepted)::numeric / NULLIF(SUM(suggestions_shown), 0) AS acceptance_rate,
         MAX(active_users)::numeric / MAX(seats_assigned)                       AS seat_utilisation
  FROM   copilot_usage_by_team_week
  GROUP  BY team_id, week
)
SELECT pr.team_id, pr.week,
       pr.merged_prs, pr.median_pr_lines, pr.median_lead_time, pr.median_review_wait,
       pr.rework_rate, d.deployments, d.change_fail_rate, o.out_of_hours_pages,
       c.acceptance_rate, c.seat_utilisation
FROM   pr
LEFT JOIN deploy  d USING (team_id, week)
LEFT JOIN oncall  o USING (team_id, week)
LEFT JOIN copilot c USING (team_id, week)
ORDER  BY pr.team_id, pr.week;
```

```sql
-- Trend view: each team's last 4 weeks vs its own previous 12-week baseline.
-- Flags a team for a conversation, not for a verdict. Never ranks teams.
WITH w AS (SELECT * FROM team_weekly_scorecard)   -- the query above, saved as a view
SELECT team_id,
  AVG(median_lead_time) FILTER (WHERE week >= current_date - 28)                       AS lead_time_recent,
  AVG(median_lead_time) FILTER (WHERE week <  current_date - 28
                                  AND week >= current_date - 112)                      AS lead_time_baseline,
  AVG(change_fail_rate) FILTER (WHERE week >= current_date - 28)                       AS cfr_recent,
  AVG(change_fail_rate) FILTER (WHERE week <  current_date - 28
                                  AND week >= current_date - 112)                      AS cfr_baseline,
  AVG(median_review_wait) FILTER (WHERE week >= current_date - 28)                     AS review_wait_recent,
  AVG(median_review_wait) FILTER (WHERE week <  current_date - 28
                                    AND week >= current_date - 112)                    AS review_wait_baseline
FROM w
GROUP BY team_id;
```

To measure whether Copilot actually helps, compare teams that adopted against teams that haven't yet (or a before/after on the same team) for 8 to 12 weeks, using lead time, change fail rate and rework. That is the measurement that can justify the licence spend.

**If the real concern is a person**
If you suspect specific people aren't delivering, that goes through their manager: clear expectations, regular feedback, support, a fair chance, HR involved. Evidence comes from the work and from peers, not from a dashboard. A PIP started from a rank is also hard to defend in front of a Dutch court or the UWV, which can look at whether the process was fair and whether the person was ever told what good looks like.

**Two questions that would change my answer**
1. What is the problem behind this: delivery is slow, quality is slipping, Copilot spend isn't paying off, or a few specific people worry you? Each has a different fix.
2. Is there a works council conversation already planned for engineering metrics? If not, starting it now (with the team-level design above) is the fastest way to get a dashboard that people trust and that will actually be used.

What am I missing, and what would make this wrong?

Assumptions: about 12 teams, GitHub-style data, Copilot data available as team aggregates, works council in place. Legal points are pointers, not legal advice.
