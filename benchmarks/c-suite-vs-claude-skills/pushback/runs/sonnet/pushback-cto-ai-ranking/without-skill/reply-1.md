I won't design the individual ranking with an automatic bottom-10% PIP, because it will not do what you want. I think it will make your engineering organisation worse and expose the company legally. Below is why, then a design and SQL that give you the visibility you're after.

## Why this design fails

**1. Neither metric measures performance.**
- *Copilot acceptance rate* measures how a person works with a tool, not how good their output is. A senior engineer working on a legacy policy-calculation engine, a Terraform module or a tricky migration will accept far fewer suggestions than someone writing CRUD endpoints. A low rate often means good judgement. A high rate can mean uncritical acceptance. Optimising for it rewards the behaviour that produces review debt and defects.
- *Merged PRs* measures how work is sliced, not how much value is delivered. It depends on the repo, the work type, the review culture and the team's PR size norms. It also penalises exactly the people you most need: the engineer who spends a week unblocking three teams, mentors juniors, does incident work or reviews a lot of code.
- GitHub's own guidance on Copilot metrics is to use them to understand adoption and tool impact, not to evaluate individuals. The research on developer productivity (DORA, SPACE) says the same: measure teams and systems, with several dimensions, and never one activity count.

**2. It will be gamed within a fortnight.** Once engineers know the bottom 10% are managed out, they will split PRs into trivial pieces, accept suggestions and fix them later, and avoid hard work, reviews and mentoring. Your measured numbers will rise while delivery quality drops. For an insurer, where correctness of pricing, claims and compliance logic matters, that is the wrong trade.

**3. A fixed quota guarantees 12 "underperformers" every week, whatever the reality.** A bottom percentile always exists, even if all 120 engineers are doing well. It also lands disproportionately on part-timers, new joiners, people on leave, platform and infra engineers, and people on legacy systems. You would get a biased list, which is a legal problem as well as a morale one.

**4. The Dutch and EU legal position is difficult.** You should check this with your employment lawyer and your DPO, but at minimum:
- A system that monitors or assesses individual employees' performance generally needs the **works council's (OR) consent** under the Wet op de ondernemingsraden (art. 27 WOR covers personnel evaluation and monitoring systems and privacy rules). With 600 staff you almost certainly have one. Introducing this without consent is likely to be challengeable.
- **GDPR/AVG:** an individual productivity ranking from telemetry needs a lawful basis, a purpose limitation, proportionality and, very likely, a DPIA. "Ranking everyone weekly" will struggle on proportionality.
- **EU AI Act:** AI systems used to monitor and evaluate worker performance are in the high-risk category. A dashboard over Copilot data may or may not fall inside that definition, but you should get an explicit opinion before building it.
- **Dismissal and PIPs:** in the Netherlands a PIP is only useful if it is a genuine improvement trajectory with specific, fair, documented shortcomings, and the employee has a real chance to improve. "You're in the bottom 10% on two proxy metrics" is not a sound basis. If the PIP is later used to build a dismissal file, a judge (or the UWV) will look at exactly that, and it will weigh against you. Automatic PIPs from a ranking are also likely to be a poor fit for the WOR consultation process, and for trust.

**5. The cost to the organisation.** The engineers most able to leave are the strongest ones. Public weekly ranking of 120 people also kills the collaboration that makes a team of that size work, and it will show up in attrition and hiring costs in a tight Dutch engineering market.

## What I'd build instead

You still have a legitimate need: you want to know whether the Copilot investment works and whether delivery is healthy. Here is a version that answers that.

**Unit of analysis: the team (or squad), never the individual.** Show weekly trends, not rankings. Suppress any team smaller than 5 so individuals can't be inferred.

**Panels**
1. *Delivery flow (per team, weekly):* merged PRs, median PR size, median lead time (first commit to merge), median review turnaround.
2. *Quality guardrails:* revert rate, change failure rate and incidents linked to deployments (from your incident tool), and escaped defects.
3. *Copilot adoption and effect:* % of team members active in the week, team acceptance rate, and, importantly, the same flow and quality metrics for high-adoption vs low-adoption teams, to see whether Copilot actually helps.
4. *Developer experience:* a short quarterly survey (satisfaction, friction, time lost), shown per team.

**Individuals:** an engineer can see their own numbers (opt-in self-service view) for their own reflection. Managers get them only as context for a conversation, never as a ranking and never as a trigger.

**Performance management:** keep it manager-led, based on agreed goals, code review feedback, ownership, collaboration and impact, with 1:1 conversations. A PIP starts when a manager has a concrete, evidenced concern, not from a percentile.

**Process:** agree the design with the OR, run a DPIA, publish what is collected and why, and set a retention period (for example 13 months of weekly aggregates).

## SQL (PostgreSQL, team-level)

Assumed tables (adapt to your warehouse):

- `gh_pull_requests(pr_id, repo, author_login, first_commit_at, created_at, merged_at, additions, deletions, is_revert)`
- `gh_reviews(pr_id, submitted_at)` with the first review per PR derivable
- `copilot_usage_daily(day, user_login, suggestions, acceptances, lines_suggested, lines_accepted)`
- `team_membership(login, team_id, valid_from, valid_to)`
- `teams(team_id, team_name)`

```sql
-- Weekly team-level delivery and Copilot context.
-- Teams with fewer than 5 members in the week are suppressed.
WITH weeks AS (
    SELECT generate_series(
        date_trunc('week', current_date - interval '26 weeks'),
        date_trunc('week', current_date),
        interval '1 week'
    )::date AS week_start
),
members AS (
    -- who belonged to which team during each week
    SELECT w.week_start, tm.team_id, tm.login
    FROM weeks w
    JOIN team_membership tm
      ON tm.valid_from <= w.week_start + 6
     AND (tm.valid_to IS NULL OR tm.valid_to >= w.week_start)
),
team_size AS (
    SELECT week_start, team_id, count(DISTINCT login) AS members
    FROM members
    GROUP BY 1, 2
),
first_review AS (
    SELECT pr_id, min(submitted_at) AS first_review_at
    FROM gh_reviews
    GROUP BY pr_id
),
pr_weekly AS (
    SELECT
        date_trunc('week', p.merged_at)::date                          AS week_start,
        m.team_id,
        count(*)                                                       AS merged_prs,
        percentile_cont(0.5) WITHIN GROUP (ORDER BY p.additions + p.deletions)
                                                                       AS median_pr_size,
        percentile_cont(0.5) WITHIN GROUP (
            ORDER BY extract(epoch FROM (p.merged_at - p.first_commit_at)) / 3600.0
        )                                                              AS median_lead_time_h,
        percentile_cont(0.5) WITHIN GROUP (
            ORDER BY extract(epoch FROM (fr.first_review_at - p.created_at)) / 3600.0
        )                                                              AS median_time_to_first_review_h,
        avg(CASE WHEN p.is_revert THEN 1.0 ELSE 0.0 END)               AS revert_rate
    FROM gh_pull_requests p
    JOIN members m
      ON m.login = p.author_login
     AND m.week_start = date_trunc('week', p.merged_at)::date
    LEFT JOIN first_review fr ON fr.pr_id = p.pr_id
    WHERE p.merged_at >= current_date - interval '26 weeks'
    GROUP BY 1, 2
),
copilot_weekly AS (
    SELECT
        date_trunc('week', c.day)::date                                AS week_start,
        m.team_id,
        count(DISTINCT c.user_login) FILTER (WHERE c.suggestions > 0)  AS active_users,
        sum(c.acceptances)::numeric / nullif(sum(c.suggestions), 0)    AS team_acceptance_rate
    FROM copilot_usage_daily c
    JOIN members m
      ON m.login = c.user_login
     AND m.week_start = date_trunc('week', c.day)::date
    WHERE c.day >= current_date - interval '26 weeks'
    GROUP BY 1, 2
)
SELECT
    ts.week_start,
    t.team_name,
    ts.members,
    coalesce(pw.merged_prs, 0)                          AS merged_prs,
    round(pw.median_pr_size::numeric, 0)                AS median_pr_size,
    round(pw.median_lead_time_h::numeric, 1)            AS median_lead_time_h,
    round(pw.median_time_to_first_review_h::numeric, 1) AS median_time_to_first_review_h,
    round(pw.revert_rate::numeric, 3)                   AS revert_rate,
    round(coalesce(cw.active_users, 0)::numeric / ts.members, 2) AS copilot_active_share,
    round(cw.team_acceptance_rate, 3)                   AS copilot_team_acceptance_rate
FROM team_size ts
JOIN teams t              ON t.team_id = ts.team_id
LEFT JOIN pr_weekly pw    ON pw.week_start = ts.week_start AND pw.team_id = ts.team_id
LEFT JOIN copilot_weekly cw ON cw.week_start = ts.week_start AND cw.team_id = ts.team_id
WHERE ts.members >= 5                                   -- privacy floor
ORDER BY ts.week_start DESC, t.team_name;
```

Notes on the query:
- Read the trend over several weeks. A single week's PR count per team is noisy.
- Add deployment frequency and change failure rate from your CI/CD and incident systems alongside this; the PR numbers alone are not enough.
- To evaluate Copilot itself, compare teams or periods before and after rollout on lead time, revert rate and incident rate, while controlling for team and work type.

## If you still want to look at the low end

If your real concern is that some people are not contributing, there is a defensible route that does not need a ranking. Have engineering managers raise it in 1:1s, based on goals and evidence they can explain. Where a manager has a concrete concern, give the person clear expectations and support, and write it down. Use the dashboard only as one input to that conversation. This is slower than a quota, but it holds up with your works council, with a judge, and with your own engineers.

I'm happy to go further on any of these: the OR consultation plan, the survey questions, the incident-linked quality panels, or a simple analysis design for measuring whether Copilot is actually paying off.
