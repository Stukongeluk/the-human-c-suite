# Engineering health dashboard: design

**Status:** proposal, to go through the DPIA and the works council (OR) before go-live
**Scope:** 120 engineers. Assumes GitHub with Copilot, a CI/CD tool, an incident tool and a PostgreSQL-compatible warehouse.
**SQL:** `engineering_health_dashboard.sql` (tested on PostgreSQL 16, see section 9)

---

## 1. What it answers

Three questions, refreshed weekly, per team:

1. **Where is delivery getting stuck?** The DORA metrics (deployment frequency, lead time, change failure rate, time to restore) and PR flow.
2. **Is Copilot being adopted, and is it helping or hurting delivery and stability?**
3. **Which teams should I talk to this week, and about what?** The "where to look" view.

It does not answer "who is the weakest engineer". That is a manager's call, made with evidence (section 7).

## 2. What changed from the original request

| Requested | Replaced with | Why |
|---|---|---|
| Rank every engineer | Team-level rows. No figure describes fewer than 5 people | One person's weekly numbers are mostly noise (leave, on-call, part-time, kind of work). Individual monitoring needs OR consent and a DPIA. A ranking gets gamed within weeks |
| Copilot acceptance rate per person | Team adoption, the team's accept ratio as context, and a stability guardrail | Acceptance shows whether people trust the suggestions, not what they deliver. GitHub's per-user data has no acceptance-rate field and is incomplete when IDE telemetry is off |
| Merged PRs per person | Team flow: cycle time, wait for first review, PR size, reverts. Throughput per FTE as context only | Counts reward splitting PRs and penalise reviewers, incident responders, mentors and legacy work |
| Bottom 10% go on a PIP | A process led by managers, with specific evidence. A formal improvement plan (verbetertraject) only where there is a real gap | Forced distribution creates "failures" on a quota. A rank-triggered PIP doesn't support dismissal on grounds of unsuitability (BW 7:669(3)(d)) and runs into GDPR art. 22 |
| Weekly | Weekly refresh of rolling 4-week windows | Teams need a trend they can act on. Weekly snapshots swing on single events |

## 3. Panels and metric definitions

Every metric is a **rolling 4-week window ending with the week shown**, per reporting group (normally a team; small teams are combined).

### Panel A: Delivery (DORA), for services the team owns

| Metric | Definition | Watch out for |
|---|---|---|
| Deploys per week | Production deployments that went live (`success` or `rolled_back`) ÷ 4 | Batch-release teams (e.g. a mainframe bridge) will be low by design. Compare each team with its own trend |
| Median lead time (h) | Deployment finished minus the oldest commit it shipped | Needs `oldest_commit_at` from the pipeline |
| Change failure rate | Share of live deployments that were rolled back or caused an incident | Depends on incidents being linked to deployments. If they aren't yet, it counts rollbacks only |
| Sev 1–2 incidents, median time to restore (h) | Resolved sev 1–2 incidents on the team's services | Open incidents are left out until they close |

### Panel B: PR flow, from PRs by the team's members (bots excluded)

| Metric | Definition | Watch out for |
|---|---|---|
| Merged PRs per FTE per week | Context only, never a target | Shown only if at least 5 people contributed in the window |
| Median PR cycle time (h) | Created → merged | |
| Median hours to first review | Created → first review | Long waits usually mean review load is concentrated on a few seniors |
| Median PR size, share over 400 lines | Additions plus deletions | Large PRs predict slow reviews and failed changes |
| Revert share | Merged PRs that are reverts | |

### Panel C: Copilot, at team level

| Metric | Definition | Watch out for |
|---|---|---|
| Active share | Average weekly active Copilot users ÷ team members | |
| Chat/agent share | Active users who used chat or agent mode | |
| Accept ratio | Team acceptances ÷ team generations, from GitHub's per-user report summed to team level | Mixes completions and chat code blocks. Higher is not better. Read it next to change failure rate |
| Telemetry coverage | Share of active users whose IDE sent telemetry all week | Below 80%, treat the Copilot figures as incomplete |

Copilot figures are written only for weeks where at least 5 team members were active. Weeks are processed after GitHub's three-day finalisation window, so the job runs on Thursdays.

### Panel D: Where to look this week

For the latest week, `rpt.v_engineering_health_attention` lists the signals that moved against the team's own baseline (the median of weeks 4–16 before) or crossed a fixed guardrail:

- Lead time up more than 25% against the team's own baseline
- Change failure rate above 15%, or up 50% against baseline
- PRs waiting more than a day for first review
- More than 30% of PRs over 400 changed lines
- **Copilot acceptance up while stability got worse.** This is the check that matters for AI in regulated systems: it points you at how AI-written code is reviewed.
- Copilot telemetry incomplete

Thresholds are starting points. Tune them after the pilot.

### Panel E: quarterly, outside this SQL

- A short developer-experience survey: time lost, tooling friction, whether Copilot helps and where. Anonymous, reported only for groups with at least 5 responses.
- On-call load per team.

## 4. Rules of use (write these into the OR agreement)

1. **Team level only.** No figure describes fewer than 5 people. The SQL enforces this and suppresses smaller groups.
2. **Each team against its own baseline.** No league tables. The dashboard sorts by team name.
3. **Not an input to individual assessment, pay or PIPs.** This is what makes OR consent achievable, and what stops the numbers being gamed.
4. **Teams see their own dashboard first.** A flag opens a conversation with the team about the system they work in.
5. **Quarterly metric review.** Any metric that is being gamed or misread gets changed or dropped.
6. **Purpose limitation.** The data is used to improve delivery and to evaluate AI tooling, and nothing else.

## 5. Data flow and privacy design

```
GitHub PRs ───────────┐
CI/CD deployments ────┼─> source schemas (org, gh, cd, ops) ─> stg (restricted) ─┐
Incidents ────────────┘                                                         ├─> rpt (team level) ─> BI tool
Copilot users-1-day report ─> copilot_raw (restricted, 35 days) ─> copilot.group_week (team-week, k=5) ─┘
```

- **Per-user Copilot rows** land in `copilot_raw`. Only the ingestion service account can read them, and they are deleted after 35 days, which is just enough to re-aggregate finalised weeks. Log access to this schema.
- **Login → team mapping** comes from HR or the identity provider. FTE is only ever summed per team.
- **BI access:** role `eng_dashboard_reader` can select the two `rpt` views and nothing else. Tested: it is refused on `stg`, `copilot` and `copilot_raw`.
- **Retention** for team aggregates: suggest 24 months.
- **DPIA inputs:**
  - *Purpose:* delivery improvement and evaluating AI tooling.
  - *Necessity and proportionality:* aggregation replaces individual monitoring.
  - *Minimisation:* k=5 and 35-day raw retention.
  - *Access:* restricted roles.
  - *Transparency:* a notice to engineers.
  - *Data subject rights:* raw rows exist for 35 days, so access requests are answerable.
- **OR consent request:** cover the processing of employee data (WOR 27(1)(k)) and a system suitable for monitoring performance (27(1)(l)), and attach the rules from section 4. Aggregate data with these rules is a far easier request than individual rankings.

## 6. Copilot: what the data can and cannot tell you

- **What GitHub provides:** per-user daily and 28-day reports. Fields include `code_generation_activity_count`, `code_acceptance_activity_count`, `used_agent`, `used_chat` and `client_telemetry_present`. There is no per-user acceptance-rate field.
- **Gaps:** when a developer's IDE telemetry is off, their detailed activity is missing. Recent days are incomplete until they finalise, within three full UTC days. CLI usage is counted separately from IDE metrics.
- **What acceptance means:** GitHub describes it as showing whether suggestions "are relevant and trusted". GitHub's own research found it tracks how productive developers *feel*. It is not output.
- **How to judge whether Copilot pays off:**
  - Compare each team's DORA and flow trend before and after rollout.
  - Add the quarterly survey: where it saves time, where it creates rework.
  - Compare teams doing similar work.
  - Treat a rise in acceptance alongside a rise in change failure rate as a warning, not a win.

## 7. Underperformance: the route that works and holds up

1. **The manager names the concern,** with concrete examples measured against the role's expectations (career framework): designs, PRs, incident handling, peer feedback.
2. **Rule out the system first.** Check for legacy or on-call load, onboarding, unclear expectations, part-time hours and team changes. If health may be involved, go through the company doctor (bedrijfsarts), not the manager.
3. **Set clear expectations, provide support and hold time-boxed check-ins,** all documented and shared with the engineer.
4. **If the gap persists, start a formal verbetertraject** with HR and employment counsel. It needs specific goals, real support (coaching, training, a mentor), a realistic duration (usually months, not weeks) and recorded progress. This is what a subdistrict court (kantonrechter) looks for under BW 7:669(3)(d).
5. **Data:** use work the manager has reviewed, never a rank. If individual metrics are ever used, they must be covered by the OR-approved assessment arrangement (WOR 27(1)(g)) and visible to the engineer. They provide context and never trigger the process.

## 8. Rollout

| When | What | Owner |
|---|---|---|
| By 14 Dec 2026 | Ingestion jobs and SQL in the warehouse. Pilot dashboard with two teams that volunteer | Platform/data lead |
| By 14 Dec 2026 | DPIA draft and transparency notice | DPO (FG) + HR |
| January 2027 | OR consent request with the rules of use. Adjust after pilot feedback | CTO + HR |
| After consent | Roll out to all teams. Each team walks through its own view first | Engineering managers |
| End of Q1 2027 | First quarterly metric review and first Copilot impact read | CTO |

## 9. How the SQL was tested

- **Setup:** PostgreSQL 16.15, synthetic data for 40 engineers in 7 teams over 200 days (about 2,000 PRs, 1,200 deployments, 85 incidents and 4,300 Copilot user-days). It included one team move and a 3-person team. Two small teams were combined into one reporting group.
- **Suppression:** the 3-person team came back suppressed with no metrics. No row with fewer than 5 members carries a metric.
- **Access:** the reader role can read both `rpt` views and is refused on `stg`, `copilot` and `copilot_raw`. No `rpt` column carries a login.
- **Idempotency:** the DDL and the Thursday refresh both run twice cleanly. The purge left 35 days of raw rows.
- **Planted problems:** the attention view flagged all of them. These were a change-failure spike together with higher Copilot acceptance (Pricing), slow first reviews (Policy) and a lead-time jump (Digital).
- **Speed:** the attention view ran in about 0.3 s.

## 10. Assumptions

- 🔴 GitHub Enterprise Cloud with Copilot Business or Enterprise, and access to the usage-metrics reports.
- 🔴 A PostgreSQL-compatible warehouse. On Snowflake, BigQuery or Fabric, adapt `date_trunc`, `AT TIME ZONE` and `percentile_cont`.
- 🔴 Every service has an owning team, and incidents can be linked to the deployment that caused them.
- 🔴 Teams of roughly 5–10 people. Smaller teams are combined through `org.team.reporting_group`.
- 🟢 You have a works council: one is required at 50 or more people.

## 11. Legal and research notes

- 🟢 **OR consent:** consent is required for arrangements on processing employee personal data and for facilities "aimed at or *suitable* for" monitoring attendance, behaviour or performance. A decision taken without consent is void if the OR invokes that within one month (Dirkzwager on the AP's OR guide). The sub-letters (g, k, l) are cited from the WOR text as I know it; confirm with counsel.
- 🟢 **DPIA:** mandatory under the AP's list (Stcrt. 2019, 64418). Item 11 covers "stelselmatig monitoring van activiteiten van werknemers". Item 15 covers profiling that includes "beoordeling van beroepsprestaties".
  - The AP consulted on a revised list in 2026 and I could not read the new version, so have your DPO check it.
  - GDPR art. 35(3)(a) separately requires a DPIA for systematic evaluation of people on which significant decisions are based.
- 🟡 **GDPR art. 22:** a PIP that follows automatically from a rank is a decision based solely on automated processing with significant effect. Rubber-stamping it does not count as meaningful human involvement. The Amsterdam Court of Appeal applied art. 22 to automated deactivation of Uber drivers in 2023.
- 🟡 **BW 7:669(3)(d):** dismissal for unsuitability requires that the employee was told in time and given enough opportunity to improve. **BW 7:648:** no distinction on working hours without objective justification, which matters because raw counts disadvantage part-timers.
- 🟡 **EU DORA** (the Digital Operational Resilience Act, which is not the DORA metrics) has applied to insurers since January 2025, including ICT change management. Incentivising less review of AI-written code works against it.
- 🟡 **EU AI Act:** a plain SQL ranking is unlikely to be an "AI system". An ML model that scores engineers' performance would fall in the Annex III employment category (high-risk).
- 🟡 **Research** (published findings as I know them; not re-checked in this session):
  - GitHub's Copilot productivity study (Ziegler et al.): acceptance rate was the best predictor of *perceived* productivity.
  - METR's 2025 randomised trial: experienced open-source developers were 19% slower with AI tools, while believing they were faster.
  - DORA's 2024 report: each 25% increase in AI adoption was associated with an estimated 1.5% drop in delivery throughput and 7.2% drop in delivery stability.

## 12. Sources

- GitHub Docs: [About Copilot usage metrics](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics)
- GitHub Docs: [Copilot usage metrics reference (per-user report fields)](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics)
- GitHub Docs: [Reconciling usage metrics (telemetry gaps, three-day finalisation)](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/reconciling-usage-metrics)
- Dirkzwager: [Instemmingsrecht van de OR volgens het OR-privacyboekje van de AP](https://www.dirkzwager.nl/kennis/artikelen/instemmingsrecht-van-de-or-volgens-het-or-privacyboekje-van-de-ap)
- Autoriteit Persoonsgegevens: [Lijst verwerkingen waarvoor een DPIA verplicht is, Stcrt. 2019, 64418](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)
- Eurofound: [Employee monitoring and surveillance, Netherlands](https://apps.eurofound.europa.eu/legislationdb/employee-monitoring-and-surveillance/netherlands)
- Microsoft Learn: [Understand limitations and measure impact of GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/5-understand-limitations-measure-impact)
