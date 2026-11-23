I'll skip the ethics. I still won't build the per-engineer ranking or the bottom-10% cut, because the numbers can't carry it. Acceptance rate and merged PRs don't measure performance, and a rank always yields 12 names whether or not anything is wrong. Legal and HR agreeing doesn't change that, and it doesn't cover one thing: individual performance data needs works council consent (art. 27(1)(l) WOR), so check whether the OR has actually signed off, not only HR and legal.

Here is the dashboard spec, built to be used on Monday. The base SQL is in my first reply; these are the additions.

**Dashboard spec (one page, refreshed Monday 06:00)**
1. **Top row, per team:** lead time, change fail rate, review wait, out-of-hours pages. Each shows the last 4 weeks against the team's own 12-week baseline, as an arrow plus a number. No team-vs-team ordering.
2. **Flow panel:** PR size and work in progress per team, which is where the Faros review bottleneck shows up.
3. **Copilot panel:** seat utilisation and acceptance rate per team, next to lead time and rework for the same weeks. Unused seats list by team, so you can cut licence spend.
4. **Attention list:** teams where two or more metrics worsened for 4 weeks in a row. The output is a conversation with the team lead, not a verdict.
5. **Access:** you and the engineering directors see all teams, team leads see their own, and nobody sees named individuals. Teams under 5 are suppressed.

**SQL addition: does Copilot help? (adopters vs non-adopters, same weeks)**

```sql
WITH adoption AS (
  SELECT team_id,
         CASE WHEN AVG(seat_utilisation) >= 0.6 THEN 'high' ELSE 'low' END AS adoption_group
  FROM   copilot_usage_by_team_week
  WHERE  week >= current_date - interval '12 weeks'
  GROUP  BY team_id
)
SELECT a.adoption_group,
       COUNT(DISTINCT w.team_id)             AS teams,
       AVG(w.median_lead_time)               AS lead_time,
       AVG(w.change_fail_rate)               AS change_fail_rate,
       AVG(w.rework_rate)                    AS rework_rate,
       AVG(w.median_review_wait)             AS review_wait
FROM   team_weekly_scorecard w
JOIN   adoption a USING (team_id)
WHERE  w.week >= current_date - interval '12 weeks'
GROUP  BY a.adoption_group;
```

Treat this as indicative only, since adopters may differ from non-adopters in other ways.

If specific people worry you, give each manager their own team's trend view and the conversation starts there, with evidence from the work and from peers.

What am I missing, and what would make this wrong?
