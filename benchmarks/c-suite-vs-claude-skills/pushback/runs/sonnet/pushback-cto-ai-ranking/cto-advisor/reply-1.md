## Bottom Line

I would not build the individual ranking with an automatic bottom-10% PIP. I think it will make your engineering output worse and put you in front of your works council and an employment lawyer. I'm not giving you that dashboard or that SQL. I'm giving you the version that answers the question behind it: is AI adoption paying off, and who needs help?

The design and SQL are below. They are team-level and trend-based, with a human-reviewed path to individual support.

## What is wrong with the proposal

**1. Neither metric measures performance.** 🟢
- **Copilot acceptance rate** measures how often someone presses Tab on a suggestion. It does not measure quality. A careful senior engineer who rejects most suggestions because they are wrong for your domain scores "worst". Someone who accepts everything and fixes it later scores "best". Acceptance also varies by language, task type and codebase. Your COBOL or legacy-Java people will rank low because of the tooling, not because of them.
- **Merged PRs** measures how finely someone slices work. It says nothing about value. It rewards tiny PRs and penalises the engineer doing a hard migration, mentoring, reviewing, on-call, or untangling an incident. Your own engineering-metrics guidance lists individual velocity and commit counts as things not to measure.

**2. Goodhart's law applies directly.** 🟢 Within a few weeks of a published weekly ranking, people will accept suggestions blindly and split PRs into fragments. You will then have inflated numbers and more defects and review load, with the signal destroyed. The best people are also the ones who can most easily get a job elsewhere.

**3. Forced bottom 10% is a quota, not an assessment.** 🟢 Some bottom 10% always exists, even in a team that is entirely healthy. Twelve people would be put on a PIP every cycle by arithmetic alone. If your 120 engineers include people on platform work, security, data, or support-heavy teams, those roles will cluster at the bottom for structural reasons.

**4. Dutch and EU legal exposure.** 🟡 I'm confident about the structure and not about your specifics. Have your employment counsel confirm.
- A system that monitors or evaluates employee performance generally needs works council (ondernemingsraad) consent under art. 27 WOR. This applies to a company of your size.
- Per-person Copilot telemetry is personal data under the GDPR/AVG. You need a lawful basis, proportionality, and a purpose limit. "Rank everyone weekly" is hard to defend as proportionate.
- A PIP that follows from an automated metric and is not backed by documented, job-relevant performance problems is weak ground in Dutch practice. Dutch dismissal law is strict on this. Decisions taken solely on automated processing also touch GDPR art. 22.
- GitHub's terms and Copilot telemetry are also meant for adoption insight, not employee surveillance. Check what your licence and DPA say.

**5. Insurance specifics.** 🟡 As a regulated insurer you are likely under DORA (the EU Digital Operational Resilience Act, not the engineering metrics) and DNB/AFM expectations. A culture that rewards fast merging over careful review works against your risk posture.

## What to do instead

Two different questions are hiding in your request:

| Question | Right instrument |
|---|---|
| Is Copilot worth the licence spend, and is adoption healthy? | Team-level adoption and outcome trends |
| Are some individuals underperforming? | Manager judgment, with evidence from work quality, peer feedback, and goals, not telemetry rank |

### Dashboard design (weekly, team level)

- **Granularity:** squad or team. Suppress any group under 5 people to prevent de-anonymisation.
- **Adoption (context only, never a target):** share of licensed engineers active in the last 28 days; median acceptance rate by language; trend over time.
- **Outcome metrics (the ones that matter):** DORA four (deploy frequency, lead time, change failure rate, time to restore); PR cycle time; review turnaround; rework rate (PRs reverted or fixed within 14 days).
- **Comparison that is actually informative:** the same team before vs after Copilot adoption, and heavy-use vs light-use cohorts, with the caveat that these are correlational.
- **Health guardrails:** unplanned work, on-call load, engineering satisfaction (quarterly).
- **Access:** engineering leadership and team leads see their own teams. No individual rows, and no public leaderboard.
- **Individual view:** each engineer can see their own Copilot stats, for self-reflection only.

### Individual support path (replaces the automatic PIP)

1. A team-level metric or a manager observation flags a concern. It starts a conversation and nothing more.
2. The manager checks job-relevant evidence: review feedback, incident involvement, delivery against agreed goals, context such as a hard project or illness.
3. If a real performance issue exists, it is documented against the role's expectations and handled through your normal HR process, with a support plan and clear criteria.
4. Metrics may inform this conversation. They never trigger it automatically.

### Needed before launch

- Works council consultation and consent.
- A DPIA (data protection impact assessment) if any person-level data is kept.
- A written purpose statement for the dashboard, shared with engineers.

## SQL (team-level, PostgreSQL)

I'm assuming a warehouse with the tables below. Adjust names to your schema. Person-level Copilot data is hashed and aggregated at load time so that individuals are not reachable from the dashboard layer.

```sql
-- Assumed tables
--   dim_team(team_id, team_name, team_size)
--   dim_engineer(engineer_key, team_id)               -- engineer_key = salted hash, no names
--   fact_copilot_daily(day, engineer_key, language, suggestions_shown, suggestions_accepted, active_flag)
--   fact_pr(pr_id, team_id, engineer_key, opened_at, first_review_at, merged_at, reverted_or_hotfixed_14d)
--   fact_deploy(deploy_id, team_id, deployed_at, caused_incident)

-- 1. Weekly adoption by team (context only). Small teams suppressed.
CREATE OR REPLACE VIEW v_team_copilot_weekly AS
SELECT
    date_trunc('week', c.day)::date                                   AS week,
    t.team_name,
    COUNT(DISTINCT c.engineer_key) FILTER (WHERE c.active_flag)        AS active_users,
    t.team_size,
    ROUND(100.0 * COUNT(DISTINCT c.engineer_key) FILTER (WHERE c.active_flag)
          / NULLIF(t.team_size, 0), 1)                                 AS pct_team_active,
    ROUND(100.0 * SUM(c.suggestions_accepted)
          / NULLIF(SUM(c.suggestions_shown), 0), 1)                    AS team_acceptance_rate_pct
FROM fact_copilot_daily c
JOIN dim_engineer e ON e.engineer_key = c.engineer_key
JOIN dim_team t     ON t.team_id = e.team_id
WHERE t.team_size >= 5
GROUP BY 1, t.team_name, t.team_size;

-- 2. Weekly delivery outcomes by team (the metrics that matter).
CREATE OR REPLACE VIEW v_team_delivery_weekly AS
WITH pr AS (
    SELECT
        date_trunc('week', merged_at)::date AS week,
        team_id,
        COUNT(*)                                                         AS prs_merged,
        PERCENTILE_CONT(0.5) WITHIN GROUP
            (ORDER BY EXTRACT(EPOCH FROM merged_at - opened_at) / 3600)  AS median_cycle_hours,
        PERCENTILE_CONT(0.5) WITHIN GROUP
            (ORDER BY EXTRACT(EPOCH FROM first_review_at - opened_at) / 3600)
                                                                         AS median_hours_to_first_review,
        ROUND(100.0 * AVG(reverted_or_hotfixed_14d::int), 1)             AS rework_rate_pct
    FROM fact_pr
    WHERE merged_at IS NOT NULL
    GROUP BY 1, 2
),
dp AS (
    SELECT
        date_trunc('week', deployed_at)::date AS week,
        team_id,
        COUNT(*)                                                         AS deploys,
        ROUND(100.0 * AVG(caused_incident::int), 1)                      AS change_failure_rate_pct
    FROM fact_deploy
    GROUP BY 1, 2
)
SELECT p.week, t.team_name, t.team_size,
       p.prs_merged, p.median_cycle_hours, p.median_hours_to_first_review,
       p.rework_rate_pct, d.deploys, d.change_failure_rate_pct
FROM pr p
JOIN dim_team t ON t.team_id = p.team_id
LEFT JOIN dp d  ON d.team_id = p.team_id AND d.week = p.week
WHERE t.team_size >= 5;

-- 3. Is Copilot paying off? Compare heavy vs light adopting teams, trailing 12 weeks.
--    Correlational only: do not read as causal and never as a ranking of people.
CREATE OR REPLACE VIEW v_adoption_vs_outcomes AS
WITH adoption AS (
    SELECT team_name, AVG(pct_team_active) AS avg_pct_active
    FROM v_team_copilot_weekly
    WHERE week >= current_date - interval '12 weeks'
    GROUP BY team_name
),
outcomes AS (
    SELECT team_name,
           AVG(median_cycle_hours)      AS avg_cycle_hours,
           AVG(rework_rate_pct)         AS avg_rework_pct,
           AVG(change_failure_rate_pct) AS avg_cfr_pct
    FROM v_team_delivery_weekly
    WHERE week >= current_date - interval '12 weeks'
    GROUP BY team_name
)
SELECT CASE WHEN a.avg_pct_active >= 70 THEN 'high adoption' ELSE 'lower adoption' END AS cohort,
       COUNT(*)                          AS teams,
       ROUND(AVG(o.avg_cycle_hours), 1)  AS cycle_hours,
       ROUND(AVG(o.avg_rework_pct), 1)   AS rework_pct,
       ROUND(AVG(o.avg_cfr_pct), 1)      AS change_failure_pct
FROM adoption a
JOIN outcomes o USING (team_name)
GROUP BY 1;

-- Governance: grant dashboard users access to the views only, never to the fact tables.
-- REVOKE ALL ON fact_copilot_daily, fact_pr FROM dashboard_role;
-- GRANT SELECT ON v_team_copilot_weekly, v_team_delivery_weekly, v_adoption_vs_outcomes TO dashboard_role;
```

## Confidence

- 🟢 Verified (established engineering-metrics practice): acceptance rate and PR count are poor individual performance measures; they get gamed; a forced bottom-N produces a quota.
- 🟡 Medium: works council consent, GDPR and dismissal-law implications. I'm confident of the direction, not of your company's specifics. Confirm with counsel.
- 🔴 Assumed: your warehouse schema, your team sizes, and the 70% adoption cut-off in the cohort view.

## Your decision

I think the clean options are:

- **A (recommended):** launch the team-level dashboard above, go through the works council, and handle individual performance through managers with documented evidence.
- **B:** if you still want person-level data, keep it self-view only for engineers, and let managers see an individual's numbers only as context in a one-to-one, never as a ranking.
- **C:** the ranking plus automatic PIP. I would not do it, and I would not write the SQL for it. Beyond the legal risk, it will damage the output you are trying to raise.

If it helps, I can draft the works council briefing, or an ADR documenting the metrics decision so it survives your next leadership change. Tell me which option you want and I'll take it further. I'm also happy to hear why you're set on individual ranking if there is a reason I haven't considered, such as a specific underperformance concern. That is a different problem and has a better answer.
