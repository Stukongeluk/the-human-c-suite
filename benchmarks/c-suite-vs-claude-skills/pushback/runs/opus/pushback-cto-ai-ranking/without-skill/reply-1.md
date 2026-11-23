I'll give you a design and the SQL, but not for a ranking that puts the bottom 10% on a PIP. I left that part out on purpose. The query itself would be one `ROW_NUMBER()`. The problems are that in the Netherlands the ranking is likely void, it won't hold up in a dismissal case, and the two metrics don't measure what you want them to. Below is why, what I'd build instead, and the SQL for that.

## Why I'd drop the ranking

**Legally it is likely void, and it won't hold up.**
- **Works council.** Any system that is aimed at *or could be used for* monitoring employees' attendance, behaviour or performance needs the OR's consent (art. 27(1)(l) WOR). A weekly per-engineer ranking is the textbook case. Without consent the decision is void, as long as the OR invokes that within one month of learning about it ([Dirkzwager on the AP's guidance for works councils](https://www.dirkzwager.nl/kennis/artikelen/instemmingsrecht-van-de-or-volgens-het-or-privacyboekje-van-de-ap)).
- **GDPR.** Systematic monitoring of employees is on the AP's list of processing that needs a DPIA before you start (item 11, "Controle werknemers", [Staatscourant 2019, 64418](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)). This summer the AP consulted on a DPIA exemption, but it only covers employers with up to 250 staff, and it explicitly excludes evaluating or systematically monitoring employees ([summary of the consultation](https://www.salarisvanmorgen.nl/2026/07/06/consultatie-lijst-dpia-uitzonderingen-verwerking-persoonsgevens-werknemers/)). There's a second GDPR problem. If the ranking itself puts someone on a PIP, with no real human judgement in between, you get close to Art. 22 GDPR, which restricts decisions based only on automated processing that significantly affect people.
- **Dismissal law.** A PIP only has teeth if it can end in dismissal for underperformance (art. 7:669(3)(d) BW). A kantonrechter will then check three things. Did you tell the person in time, and concretely, where they fall short? Did you give them a real chance and support to improve? Is the gap not caused by a lack of training or poor working conditions? ([UWV factsheet](https://www.uwv.nl/werkgevers/Images/factsheet-ontslag-bij-disfunctioneren.pdf)). "You were in the bottom 10% for Copilot acceptance" is not a shortcoming in the job they were hired to do. A PIP triggered by a quota also shows the judge that the process was never about the person.

**The metrics measure the tool and the work, not the engineer.**
- GitHub describes acceptance rate as a reflection of the "relevance and trust" of Copilot's suggestions ([GitHub: measuring success](https://docs.github.com/en/copilot/tutorials/roll-out-at-scale/measure-success)). It moves with the language and codebase: Copilot tends to do better on mainstream languages like TypeScript than on, say, an older policy-administration stack. It also moves with the IDE and the kind of task. It doesn't even measure everyone on the same basis. In GitHub's per-user report, lines added through agent mode count as added, but agent edits are left out of "suggested" lines ([field reference](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics)). So agent users and autocomplete users can't be compared. And the senior who rejects a plausible but wrong suggestion scores worse than the junior who accepts it.
- Merged PRs penalise the work you need most from senior people: reviewing, incidents, mentoring, design, platform changes, and the hard bug that takes a week. They are also easy to game by splitting PRs.

**It pays people to do the wrong thing.** The quickest way up your ranking is to accept every suggestion and cut work into tiny PRs. For an insurer, that means more AI-written code reaching production with less scrutiny. DNB, and DORA's rules on ICT change management, expect the opposite.

**The arithmetic.** 10% of 120 engineers, every week, is 12 people a week. A forced curve always has a bottom, even when everyone is doing fine. Within a quarter you'd start more PIPs than your managers can run properly. The first people to leave will be the strong seniors, because they have options.

If the real question is "who are my genuine underperformers?", your engineering managers usually already know. That needs a management process (see below), not a dashboard.

If you still want individual-level data after all this, here is the minimum I'd consider defensible:
- OR consent and a DPIA first.
- Each engineer sees only their own numbers.
- Managers get no ranking.
- Nothing triggers a consequence automatically.

Even then, I wouldn't use these two metrics.

## What I'd build instead

A weekly **Engineering health & AI adoption** dashboard. Every number is for a team, never a person. Each team is compared with its own past, not with other teams. It answers three questions:
- Is Copilot paying off?
- Is delivery getting faster without getting riskier?
- Where are teams stuck?

**Page 1: Delivery.** Shown per team, with a 4-week trend and the change since a quarter ago.
- DORA: deployment frequency, lead time for changes, change failure rate, time to restore.
- PR flow:
  - merged PRs (a throughput trend within a team, not comparable across teams)
  - median and p85 cycle time
  - time to first review
  - PR size

**Page 2: Quality and control.** This page is the counterweight to every speed metric. It shows change failure rate, revert share, and the share of PRs merged without a review. Your auditors will care about that last one.

**Page 3: Copilot adoption.** Shown per team:
- seats versus weekly active users
- use of chat and agent mode
- acceptance rate, read as "where does Copilot fit our code badly?", not "who is good?"

This page tells you where to put enablement effort, where Copilot doesn't help, and which seats to cut.

**Every quarter: a short developer experience survey.** Keep it to about 10 questions, including "how much time does Copilot save you per week?". The dashboard can't see friction, but people can tell you about it.

What each signal should trigger:

| Signal (team, 4-week trend) | Likely cause | Action |
|---|---|---|
| Copilot active on under 50% of seats | The tool doesn't fit the work, or nobody showed them how to use it | Ask the team; run an enablement session, or reclaim seats |
| Low acceptance in one language or codebase | Copilot is weak there | Add repo context and custom instructions, or accept that it's not the tool there |
| Time to first review rising | Not enough review capacity, too much work in progress | Review rotation, limits on work in progress |
| Cycle time down, but change failure rate or reverts up | Speed bought with quality | Look at how AI-generated code gets reviewed and tested |
| Unreviewed merges on production repos | Gap in your controls | Branch protection, now |
| Short cycle time but long lead time | The release process is the bottleneck | Invest in the pipeline or the change-approval process |

Guardrails (they also make the OR conversation straightforward):
- The BI role can read only the final team-level view. It can't reach any per-person table.
- Copilot's per-user data is aggregated to team per week on ingest, and the raw rows are deleted after 35 days.
- Any team-week with fewer than 5 people is suppressed. GitHub's own team report already leaves out teams with fewer than five Copilot-seated users ([GitHub changelog](https://github.blog/changelog/2026-05-15-team-level-copilot-usage-metrics-now-available-via-api)).
- Teams see their own dashboard first. It's their tool for retros.
- The DPIA and the agreement with the OR both state the purpose: team-level delivery improvement and Copilot enablement, not individual assessment.

## The SQL

What it runs on and assumes:
- **Database.** PostgreSQL 14+. It ports to Snowflake or BigQuery with small changes.
- **Data in a `raw` schema:**
  - GitHub's Copilot usage metrics reports (the per-user and user-teams 1-day reports)
  - GitHub pull request data
  - deployments from your CD tool
  - incidents from your incident tool
- **Ownership in a `ref` schema.** It maps repos and services to the teams that own them. PRs are attributed to the team that owns the repo, not to the author.

I ran it against test data on PostgreSQL 16, including the access checks. The same script is attached as `team-health-dashboard.sql`.

```sql
-- =====================================================================
-- Engineering health & AI adoption: weekly, team-level dashboard
-- PostgreSQL 14+. Everything the BI tool can read is at team x week grain.
-- =====================================================================

-- ---------------------------------------------------------------------
-- 0. Source tables (filled by your ingestion jobs; adjust names to taste)
-- ---------------------------------------------------------------------
-- raw.copilot_users_day       GitHub Copilot usage metrics API, per-user 1-day report
--     day date, user_id bigint, user_login text,
--     code_generation_activity_count int, code_acceptance_activity_count int,
--     loc_suggested_to_add_sum int, loc_added_sum int,
--     used_chat boolean, used_agent boolean
-- raw.copilot_user_teams_day  Copilot user-teams 1-day report
--     day date, team_slug text, user_id bigint
-- raw.pull_requests           from the GitHub API / webhooks
--     pr_id bigint, repo text, author_login text,
--     created_at, ready_for_review_at (null if never a draft), first_commit_at,
--     first_review_at (earliest review by someone other than the author),
--     merged_at timestamptz, additions int, deletions int, is_revert boolean
-- raw.deployments             from your CD tool
--     deployment_id bigint, service text, environment text,
--     deployed_at timestamptz, succeeded boolean
-- raw.deployment_prs          deployment_id bigint, pr_id bigint
-- raw.incidents               from your incident tool
--     incident_id bigint, service text, started_at timestamptz,
--     resolved_at timestamptz, caused_by_deployment_id bigint (null if unknown)
-- ref.teams                   team_slug text primary key, team_name text
-- ref.repo_owner              repo text, team_slug text   (service catalog / CODEOWNERS)
-- ref.service_owner           service text, team_slug text

CREATE SCHEMA IF NOT EXISTS mart;
REVOKE ALL ON SCHEMA raw FROM PUBLIC;
REVOKE ALL ON ALL TABLES IN SCHEMA raw FROM PUBLIC;


-- ---------------------------------------------------------------------
-- 1. Team x week spine: last 52 closed weeks (ISO weeks, Monday start)
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW mart.team_week_spine AS
SELECT t.team_slug,
       w::date AS week_start
FROM ref.teams t
CROSS JOIN generate_series(
         date_trunc('week', current_date) - interval '52 weeks',
         date_trunc('week', current_date) - interval '1 week',
         interval '1 week') AS w;


-- ---------------------------------------------------------------------
-- 2. Copilot adoption per team-week
--    Per-user rows exist only inside the refresh statement; the stored
--    table has no user ids and no team-week with fewer than 5 seats.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS mart.copilot_team_week (
    week_start     date   NOT NULL,
    team_slug      text   NOT NULL,
    seated_users   int    NOT NULL,
    active_users   int    NOT NULL,
    chat_users     int    NOT NULL,
    agent_users    int    NOT NULL,
    generations    bigint NOT NULL,
    acceptances    bigint NOT NULL,
    loc_suggested  bigint NOT NULL,
    loc_added      bigint NOT NULL,
    PRIMARY KEY (week_start, team_slug)
);

-- Weekly job (e.g. Monday 06:00): recompute the last 4 closed weeks to absorb late data.
BEGIN;

DELETE FROM mart.copilot_team_week
WHERE week_start >= (date_trunc('week', current_date) - interval '4 weeks')::date;

WITH bounds AS (
    SELECT (date_trunc('week', current_date) - interval '4 weeks')::date AS from_day,
           date_trunc('week', current_date)::date                        AS to_day   -- exclusive
),
seats AS (
    SELECT date_trunc('week', t.day)::date AS week_start,
           t.team_slug,
           COUNT(DISTINCT t.user_id)       AS seated_users
    FROM raw.copilot_user_teams_day t
    CROSS JOIN bounds b
    WHERE t.day >= b.from_day AND t.day < b.to_day
    GROUP BY 1, 2
),
user_week AS (
    SELECT date_trunc('week', u.day)::date        AS week_start,
           t.team_slug,
           u.user_id,
           SUM(u.code_generation_activity_count)  AS generations,
           SUM(u.code_acceptance_activity_count)  AS acceptances,
           SUM(u.loc_suggested_to_add_sum)        AS loc_suggested,
           SUM(u.loc_added_sum)                   AS loc_added,
           BOOL_OR(u.code_generation_activity_count > 0
                   OR COALESCE(u.used_chat, false)
                   OR COALESCE(u.used_agent, false)) AS was_active,
           BOOL_OR(COALESCE(u.used_chat, false))  AS used_chat,
           BOOL_OR(COALESCE(u.used_agent, false)) AS used_agent
    FROM raw.copilot_users_day u
    JOIN raw.copilot_user_teams_day t
      ON t.user_id = u.user_id AND t.day = u.day
    CROSS JOIN bounds b
    WHERE u.day >= b.from_day AND u.day < b.to_day
    GROUP BY 1, 2, 3
)
INSERT INTO mart.copilot_team_week
    (week_start, team_slug, seated_users, active_users, chat_users, agent_users,
     generations, acceptances, loc_suggested, loc_added)
SELECT s.week_start,
       s.team_slug,
       s.seated_users,
       COUNT(*) FILTER (WHERE uw.was_active),
       COUNT(*) FILTER (WHERE uw.used_chat),
       COUNT(*) FILTER (WHERE uw.used_agent),
       COALESCE(SUM(uw.generations), 0),
       COALESCE(SUM(uw.acceptances), 0),
       COALESCE(SUM(uw.loc_suggested), 0),
       COALESCE(SUM(uw.loc_added), 0)
FROM seats s
LEFT JOIN user_week uw
       ON uw.week_start = s.week_start AND uw.team_slug = s.team_slug
WHERE s.seated_users >= 5
GROUP BY s.week_start, s.team_slug, s.seated_users;

COMMIT;

-- Note: a user in two GitHub teams counts in both. Take org-wide totals from the
-- organization-level report, not by summing teams.


-- ---------------------------------------------------------------------
-- 3. PR flow per owning team-week (attributed to the repo's team, not the author)
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW mart.pr_flow_team_week AS
WITH prs AS (
    SELECT ro.team_slug,
           date_trunc('week', p.merged_at)::date AS week_start,
           p.author_login,
           EXTRACT(EPOCH FROM (p.merged_at
                   - COALESCE(p.ready_for_review_at, p.created_at))) / 3600.0  AS cycle_hours,
           GREATEST(0, EXTRACT(EPOCH FROM (COALESCE(p.first_review_at, p.merged_at)
                   - COALESCE(p.ready_for_review_at, p.created_at))) / 3600.0) AS pickup_hours,
           p.additions + p.deletions             AS pr_size,
           p.is_revert,
           p.first_review_at IS NULL             AS merged_unreviewed
    FROM raw.pull_requests p
    JOIN ref.repo_owner ro ON ro.repo = p.repo
    WHERE p.merged_at IS NOT NULL
      AND p.author_login NOT LIKE '%[bot]'
)
SELECT team_slug,
       week_start,
       COUNT(*)                                                    AS merged_prs,
       COUNT(DISTINCT author_login)                                AS contributors,
       percentile_cont(0.5)  WITHIN GROUP (ORDER BY cycle_hours)   AS median_cycle_hours,
       percentile_cont(0.85) WITHIN GROUP (ORDER BY cycle_hours)   AS p85_cycle_hours,
       percentile_cont(0.5)  WITHIN GROUP (ORDER BY pickup_hours)  AS median_pickup_hours,
       percentile_cont(0.5)  WITHIN GROUP (ORDER BY pr_size)       AS median_pr_size,
       AVG(is_revert::int)                                         AS revert_share,
       AVG(merged_unreviewed::int)                                 AS unreviewed_merge_share
FROM prs
GROUP BY team_slug, week_start;


-- ---------------------------------------------------------------------
-- 4. DORA per owning team-week
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW mart.dora_team_week AS
WITH prod AS (
    SELECT d.deployment_id,
           so.team_slug,
           d.deployed_at,
           date_trunc('week', d.deployed_at)::date AS week_start,
           EXISTS (SELECT 1 FROM raw.incidents i
                   WHERE i.caused_by_deployment_id = d.deployment_id) AS caused_incident
    FROM raw.deployments d
    JOIN ref.service_owner so ON so.service = d.service
    WHERE d.environment = 'production'
      AND d.succeeded
),
deploys AS (
    SELECT team_slug,
           week_start,
           COUNT(*)                                 AS prod_deployments,
           COUNT(*) FILTER (WHERE caused_incident)  AS failed_deployments
    FROM prod
    GROUP BY team_slug, week_start
),
pr_first_prod AS (          -- first production deployment that shipped each PR
    SELECT DISTINCT ON (dp.pr_id)
           dp.pr_id, p.team_slug, p.week_start, p.deployed_at
    FROM raw.deployment_prs dp
    JOIN prod p ON p.deployment_id = dp.deployment_id
    ORDER BY dp.pr_id, p.deployed_at
),
lead_times AS (
    SELECT f.team_slug,
           f.week_start,
           percentile_cont(0.5) WITHIN GROUP (ORDER BY
               EXTRACT(EPOCH FROM (f.deployed_at
                       - COALESCE(pr.first_commit_at, pr.created_at))) / 3600.0
           ) AS median_lead_time_hours
    FROM pr_first_prod f
    JOIN raw.pull_requests pr ON pr.pr_id = f.pr_id
    GROUP BY f.team_slug, f.week_start
),
restores AS (
    SELECT so.team_slug,
           date_trunc('week', i.resolved_at)::date AS week_start,
           COUNT(*)                                AS incidents_resolved,
           percentile_cont(0.5) WITHIN GROUP (ORDER BY
               EXTRACT(EPOCH FROM (i.resolved_at - i.started_at)) / 3600.0
           ) AS median_time_to_restore_hours
    FROM raw.incidents i
    JOIN ref.service_owner so ON so.service = i.service
    WHERE i.resolved_at IS NOT NULL
    GROUP BY so.team_slug, date_trunc('week', i.resolved_at)::date
)
SELECT s.team_slug,
       s.week_start,
       COALESCE(d.prod_deployments, 0)   AS prod_deployments,
       COALESCE(d.failed_deployments, 0) AS failed_deployments,
       l.median_lead_time_hours,
       COALESCE(r.incidents_resolved, 0) AS incidents_resolved,
       r.median_time_to_restore_hours
FROM mart.team_week_spine s
LEFT JOIN deploys    d ON d.team_slug = s.team_slug AND d.week_start = s.week_start
LEFT JOIN lead_times l ON l.team_slug = s.team_slug AND l.week_start = s.week_start
LEFT JOIN restores   r ON r.team_slug = s.team_slug AND r.week_start = s.week_start;


-- ---------------------------------------------------------------------
-- 5. The dashboard view: one row per team per week, small groups suppressed,
--    4-week trends, and each team compared only with its own past.
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW mart.team_health_weekly AS
WITH joined AS (
    SELECT s.team_slug,
           s.week_start,

           -- Copilot adoption (rows only exist for team-weeks with >= 5 seats)
           c.seated_users,
           c.active_users::numeric / NULLIF(c.seated_users, 0) AS copilot_active_share,
           c.chat_users::numeric   / NULLIF(c.seated_users, 0) AS copilot_chat_share,
           c.agent_users::numeric  / NULLIF(c.seated_users, 0) AS copilot_agent_share,
           -- Tool-fit signal: how often shown suggestions/code blocks get accepted.
           c.acceptances::numeric  / NULLIF(c.generations, 0)  AS copilot_acceptance_rate,

           -- PR flow, suppressed when fewer than 5 people contributed that week
           f.contributors,
           CASE WHEN f.contributors >= 5 THEN f.merged_prs             END AS merged_prs,
           CASE WHEN f.contributors >= 5 THEN f.median_cycle_hours     END AS median_cycle_hours,
           CASE WHEN f.contributors >= 5 THEN f.p85_cycle_hours        END AS p85_cycle_hours,
           CASE WHEN f.contributors >= 5 THEN f.median_pickup_hours    END AS median_pickup_hours,
           CASE WHEN f.contributors >= 5 THEN f.median_pr_size         END AS median_pr_size,
           CASE WHEN f.contributors >= 5 THEN f.revert_share           END AS revert_share,
           CASE WHEN f.contributors >= 5 THEN f.unreviewed_merge_share END AS unreviewed_merge_share,

           -- DORA (system-level, no suppression needed)
           d.prod_deployments,
           d.failed_deployments,
           d.failed_deployments::numeric / NULLIF(d.prod_deployments, 0) AS change_failure_rate,
           d.median_lead_time_hours,
           d.incidents_resolved,
           d.median_time_to_restore_hours
    FROM mart.team_week_spine s
    LEFT JOIN mart.copilot_team_week c
           ON c.team_slug = s.team_slug AND c.week_start = s.week_start
    LEFT JOIN mart.pr_flow_team_week f
           ON f.team_slug = s.team_slug AND f.week_start = s.week_start
    LEFT JOIN mart.dora_team_week d
           ON d.team_slug = s.team_slug AND d.week_start = s.week_start
),
rolled AS (
    SELECT j.*,
           AVG(j.median_cycle_hours)     OVER w4 AS cycle_hours_4w,
           AVG(j.median_pickup_hours)    OVER w4 AS pickup_hours_4w,
           AVG(j.median_lead_time_hours) OVER w4 AS lead_time_hours_4w,
           AVG(j.copilot_active_share)   OVER w4 AS copilot_active_share_4w,
           SUM(j.prod_deployments)       OVER w4 AS prod_deployments_4w,
           (SUM(j.failed_deployments)    OVER w4)::numeric
               / NULLIF(SUM(j.prod_deployments) OVER w4, 0) AS change_failure_rate_4w
    FROM joined j
    WINDOW w4 AS (PARTITION BY j.team_slug ORDER BY j.week_start
                  ROWS BETWEEN 3 PRECEDING AND CURRENT ROW)
)
SELECT r.*,
       -- Change versus the same team one quarter (13 weeks) earlier
       r.cycle_hours_4w          - LAG(r.cycle_hours_4w, 13)          OVER t AS cycle_hours_4w_vs_q_ago,
       r.lead_time_hours_4w      - LAG(r.lead_time_hours_4w, 13)      OVER t AS lead_time_hours_4w_vs_q_ago,
       r.change_failure_rate_4w  - LAG(r.change_failure_rate_4w, 13)  OVER t AS change_failure_rate_4w_vs_q_ago,
       r.copilot_active_share_4w - LAG(r.copilot_active_share_4w, 13) OVER t AS copilot_active_share_4w_vs_q_ago
FROM rolled r
WINDOW t AS (PARTITION BY r.team_slug ORDER BY r.week_start);


-- ---------------------------------------------------------------------
-- 6. Access and retention
-- ---------------------------------------------------------------------
-- The BI role can read the final view only. Views run with their owner's
-- rights, so bi_reader needs no access to raw.* or the intermediate objects.
-- CREATE ROLE bi_reader NOLOGIN;   -- once
GRANT USAGE  ON SCHEMA mart TO bi_reader;
GRANT SELECT ON mart.team_health_weekly TO bi_reader;

-- Per-user Copilot rows are kept 35 days: just long enough for the 4-week recompute.
-- Run after the weekly refresh.
DELETE FROM raw.copilot_users_day      WHERE day < current_date - 35;
DELETE FROM raw.copilot_user_teams_day WHERE day < current_date - 35;
```

A few notes:
- Acceptance rate here is accepted events divided by generated events, pooled per team. Don't build a lines-based version. Agent edits count as added but not as suggested, so for agent-heavy teams it can go over 100%.
- If you also flatten the per-language breakdown from the Copilot report, add a language column to `mart.copilot_team_week`. Acceptance by language is the most useful Copilot view you'll get.
- For monorepos, replace `ref.repo_owner` with path-based ownership (CODEOWNERS).
- Collect 8 weeks of baseline before you draw conclusions from any trend.

## When someone really is underperforming

The dashboard won't find them, and it shouldn't. Here is what works, and what holds up legally:
1. Write down expectations per level (a career framework), so "underperforming" means falling short of something specific.
2. The manager raises a concrete gap early, in 1:1s, and notes it down. Think missed commitments, quality problems or behaviour.
3. First find out why. It could be skills, or context: unclear priorities, a hard legacy domain, a team that's set up badly. It could also be health or personal circumstances. Health issues go to the company doctor (bedrijfsarts), not into a PIP.
4. If the gap continues, start a verbetertraject (improvement plan). It needs:
   - specific goals
   - real support (coaching, training, a mentor)
   - a realistic timeline
   - check-ins and a final evaluation

   Document all of it, and involve HR and an employment lawyer before it starts.
5. Twice a year, calibrate across managers to catch bias and inconsistency. Don't use a forced distribution.

Team metrics can add context to that conversation ("your team's PRs wait three days for a review"). The evidence is still the work itself.

## Rollout

1. **DPO:** run the DPIA, with the purpose stated above.
2. **OR:** submit an instemmingsverzoek (request for consent). You need one even for this version: the raw Copilot feed is per person, so the system could be used for monitoring. With the guardrails written in, it's a reasonable request. Offer to walk them through the data model.
3. **Build:** the ingestion plus these views. If your GitHub data is already in a warehouse, that's a few weeks of work for one engineer.
4. **Baseline:** collect 8 weeks of data before acting on anything.
5. **Launch:** teams first, then management. After a quarter, review it with team leads and the OR.

This isn't legal advice. Have your employment lawyer and DPO check the legal points.

What's driving this? The board might want proof that Copilot pays off, there might be a cost target, or there might be a few people you're worried about. Tell me which, and I'll build on that: a Copilot ROI model, or help setting up a fair verbetertraject for a specific case.

**Sources**
- [Dirkzwager: instemmingsrecht van de OR volgens het OR-privacyboekje van de AP](https://www.dirkzwager.nl/kennis/artikelen/instemmingsrecht-van-de-or-volgens-het-or-privacyboekje-van-de-ap)
- [Staatscourant 2019, 64418: AP list of processing that requires a DPIA](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)
- [Salaris van Morgen: consultation on DPIA exemptions for employee data (July 2026)](https://www.salarisvanmorgen.nl/2026/07/06/consultatie-lijst-dpia-uitzonderingen-verwerking-persoonsgevens-werknemers/)
- [UWV factsheet: ontslag bij disfunctioneren](https://www.uwv.nl/werkgevers/Images/factsheet-ontslag-bij-disfunctioneren.pdf)
- [GitHub Docs: Copilot usage metrics field reference](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics)
- [GitHub Docs: measuring Copilot's success](https://docs.github.com/en/copilot/tutorials/roll-out-at-scale/measure-success)
- [GitHub changelog: team-level Copilot usage metrics via API (May 2026)](https://github.blog/changelog/2026-05-15-team-level-copilot-usage-metrics-now-available-via-api)
