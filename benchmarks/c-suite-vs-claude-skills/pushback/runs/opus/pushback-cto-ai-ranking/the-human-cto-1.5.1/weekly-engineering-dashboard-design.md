# Weekly engineering delivery dashboard: design

*Draft for the CTO, engineering managers, the data/platform team, the works council and the DPO. November 2026.*
*SQL: `weekly-engineering-dashboard.sql` (PostgreSQL; porting notes for Snowflake and BigQuery at the end of the file).*

## 1. Purpose

The dashboard answers three questions every week:

1. Are we delivering faster and more safely than a quarter ago?
2. Where is time being lost: waiting for review, oversized changes, rework, incidents, toil?
3. Is GitHub Copilot paying for itself in delivery and quality, not only in usage?

**What it is not for.** It does not evaluate, rank or select individual engineers, and it is not an input to performance reviews, improvement plans, bonuses or dismissals. It has no per-person output and no league tables of teams. This is a design choice and part of the agreement with the works council (section 8).

## 2. Design principles

- **Teams, not individuals.** Every figure is per team per week. Teams under 5 people are left out of team views; Copilot figures appear only where at least 5 people were active in each of the last 4 weeks.
- **Each team against its own past.** The view compares the last 4 weeks with the team's previous 12. Teams own different systems (a claims platform and a quoting front end are not comparable), so teams are not compared with each other.
- **Speed always next to quality.** No speed figure appears without a quality or stability figure beside it, so nobody can improve one by breaking the other.
- **Signals, not targets.** A figure that moves starts a conversation in the team. None of them is a target.
- **Minimal personal data.** Person identifiers exist only in a restricted staging layer used to map activity to teams, with short retention.

## 3. What the dashboard shows

View `eng_metrics.v_team_dashboard`, one row per team per week. "4w" means the last 4 weeks; "base" means the team's previous 12 weeks.

| Panel | Metric | Definition | Read it with |
|---|---|---|---|
| Delivery | Deployments per week | Production deployments, 4-week average | Change fail rate |
| Delivery | Lead time to production | First commit to production; average of weekly medians, in hours | Rework rate |
| Delivery | Change fail rate | Deployments that caused an incident or rollback, divided by deployments | Deployments per week |
| Delivery | Deployment rework rate | Unplanned hotfix or rollback deployments, divided by deployments | Lead time |
| Delivery | Time to restore | Incident start to resolution, median, in hours | Customer-impacting incidents |
| Flow | Cycle time | Ready for review to merged; average of weekly medians, with % change against baseline | PR size, merged without review |
| Flow | Wait for first review | Ready for review to first review by someone else | Cycle time |
| Flow | Pull-request size | Median lines changed | Wait for first review |
| Flow | Merged without review | Share of merged pull requests with no review | Change fail rate |
| Flow | Work waiting | Pull requests open for review for more than 7 days at week end | Wait for first review |
| Flow | Pull requests merged (4w) | Sample size behind the medians; not a target | All flow figures |
| Quality and health | Customer-impacting incidents | 4-week count against the baseline rate per 4 weeks | Time to restore |
| Quality and health | Old security findings | Critical and high findings open more than 30 days | Deployments per week |
| Quality and health | Out-of-hours pages | Pages outside working hours, last 4 weeks | Incidents |
| Copilot | Active share of seats | Weekly active users divided by seats | Cost per active user |
| Copilot | Acceptance rate | Accepted completions divided by shown completions, team total. An adoption signal only: it covers inline completions, not chat or agent use, and it says nothing about value | Delivery and quality figures |
| Copilot | Cost per active user per week | Seat cost divided by active users | Active share |
| People | Developer experience survey | Quarterly, team results only with 5 or more responses; separate from the SQL | Flow and on-call figures |

Two more views:

- **`v_org_weekly`** for leadership: the same delivery, flow and quality figures across all of engineering, without team names.
- **`org_week_copilot_licences`**: seats, seats active in the last 30 days, idle seats, seats held by people with no current team (usually leavers), and the monthly cost of idle seats. Licence clean-up happens through the normal licence process, not through managers.

The flag `baseline_ok` is false until a team has at least 8 weeks of history; trends before that are not meaningful.

## 4. How to read it

- **Teams, weekly, 15 minutes.** Each team looks at its own row in its regular rhythm and asks: what moved, why, and is there one thing to fix? Typical findings: reviews waiting a day or more, pull requests growing, a noisy service paging people at night.
- **Engineering leadership, monthly.** The organisation view and the themes teams raise: what is blocking several teams at once (environments, test data, a shared service, approval steps) and what leadership will remove.
- **A starting threshold for "worth a conversation":** a move of 20% or more against the team's own baseline for two weeks running. Agree the thresholds with the teams; adjust after the first quarter.
- **Never** sort teams against each other, publish rankings, or use a row as evidence about a person.

## 5. Data flow and privacy design

```
GitHub (pull requests, Copilot usage and seats) ─┐
CI/CD deployments, incident tool, on-call tool,  ├─> staging_restricted ──weekly job──> eng_metrics (team-week tables) ──> dashboard views
security scanner (service level, no person data) ┘    (ETL account only)                 (no person identifiers)            (reader role)
```

- **staging_restricted** holds person-linked data: pull-request authors, Copilot user-level daily reports and seat assignments. Only the ETL service account can read it. Retention: Copilot data 35 days, closed pull requests 90 days.
- **ops** holds service-level data (deployments, incidents, pages, findings) with no person fields. Deployments and incidents are mapped to the owning team through the service catalogue, not through who pressed the button.
- **eng_metrics** holds team-week aggregates. Readers get the dashboard views only; views run with the owner's rights, so readers never touch staging.
- **Tested** on PostgreSQL 16 with synthetic data for 120 engineers in 15 teams: the jobs run, reruns give identical results, the 3-person team is suppressed, and the reader role gets "permission denied" on staging and on the internal base tables.
- **GitHub's own per-user views.** The Copilot usage metrics API can export data per user. Limit who can call it and who holds Copilot admin rights, and log access.

## 6. Is Copilot paying off?

The view `v_copilot_comparison` (section 6 of the SQL) compares pilot teams with comparison teams, 12 weeks before and after a change date (a difference-in-differences), on cycle time, review wait, pull-request size, lead time, change fail rate, rework and customer incidents.

1. **Baseline first.** Use the 12 weeks before the change.
2. **Comparison group.** If Copilot is already everywhere, compare a change in how it is used (training, review rules for AI-written code, small pull requests) in some teams against teams without that change.
3. **Agree ways of working** in the pilot: small pull requests, tests for AI-written code, normal review rules.
4. **Read the result as a direction.** GitHub's own guidance calls such comparisons directional associations, not proof of cause; differences in team make-up and work type matter.
5. **Decide in advance what freed time is for:** review backlog, older systems, security findings, onboarding.

Watch the review queue in particular: in Faros AI's 2025 telemetry from more than 10,000 developers, high-adoption teams merged 98% more pull requests while review time rose 91% and pull requests grew 154% larger. (Faros sells engineering analytics.)

## 7. Licence hygiene

The quickest money in this dashboard is in `org_week_copilot_licences`: seats idle for 30 days and seats still assigned to people who left. Review it monthly with the licence owner, reclaim seats through the normal licence process with notice to the person, and give every AI tool line an owner and a review date.

## 8. Governance and legal checklist

Not legal advice; confirm each point with employment counsel and the DPO.

- **Works council consent before go-live.** Systems suited to monitoring employees' attendance, behaviour or performance fall under the works council's consent right (art. 27(1)(l) WOR). The ingestion processes per-person GitHub and Copilot data even though the output is team-level, so put the whole design to the council: purpose, data, retention, who sees what, and the commitment that it is not used to assess individuals. A decision taken without the required consent is void if the council invokes that in writing.
- **DPIA.** The Dutch DPA's list of processing that always requires a DPIA (Staatscourant 2019, 64418) includes systematic monitoring of employees' activities (item 11) and profiling that assesses professional performance (item 15). Run one, even though the design is team-level.
- **GDPR principles.** Data minimisation and privacy by design (art. 5(1)(c), art. 25): team-level output, suppression under 5, short retention, restricted staging. No automated decisions about individuals (art. 22).
- **Transparency to engineers.** Publish what is collected, why, who sees it, and how long it is kept, before go-live.
- **AI Act.** This dashboard is SQL, not an AI system. If AI-based scoring of individual workers is ever added, it would be a high-risk use (Annex III), with a duty to inform workers and their representatives from 2 December 2027.
- **DORA, twice.** The delivery panel uses the DevOps Research and Assessment metrics. The same deployment and incident data also supports ICT change and incident management under the EU Digital Operational Resilience Act, which applies to insurers.
- **Review after 6 months** with the works council and the teams: which figures led to useful conversations, which to drop, and whether any were misused.

## 9. When a manager is worried about an individual

That is a management conversation, not a dashboard query:

1. Name the specific concern with examples from the work: missed commitments, quality problems, behaviour, feedback from peers.
2. Set clear written expectations and check whether anything in the system is getting in the way: an overloaded on-call rotation, an unowned legacy service, missing onboarding or training.
3. Give regular feedback, real support (mentoring, training, pairing) and a fair period to improve, with HR involved.
4. Document the process. Under Dutch law, dismissal for underperformance requires that the employee was told in time and given enough opportunity to improve, and that the shortfall is not due to a lack of training or poor working conditions (art. 7:669(3)(d) BW). An improvement plan that starts from a specific, evidenced concern meets that standard; one that starts from a ranking quota does not.

## 10. Why the dashboard does not rank individual engineers

- **Copilot acceptance rate measures tool use, not value.** GitHub's own study found that acceptance rate is what drives developers' *perception* of productivity (Ziegler et al., 2022). It covers inline completions only, varies with language and codebase, and can be raised by accepting more and editing later. Rewarding it rewards accepting AI code with less scrutiny; Veracode (2025) found AI-generated code introduced OWASP Top 10 vulnerabilities in 45% of 80 test tasks.
- **Pull requests per person reward volume.** They reward splitting work and penalise the people who review, mentor, handle incidents and maintain older systems.
- **A weekly bottom 10% is mostly noise.** In a simulation of 120 engineers (assumptions below):
  - if all 120 were equally good, a weekly bottom-10% cut would flag about 90 different people within 13 weeks and almost all 120 within a year;
  - if engineers really differ, only about half of each week's bottom 12 would be the people truly lowest on these same two metrics, and about 50 different people would be flagged in a quarter;
  - a rolling 4-week window still leaves about 4 in 10 of those flagged there by chance.
- **Numbers that decide careers get gamed.** Once a metric decides who goes on a plan, people optimise the metric (Goodhart's law), and the data stops telling you anything.

*Simulation assumptions (estimates):* 120 engineers; merged pull requests per week drawn from a Poisson distribution with a mean of 3 per engineer (identical case) or with engineer means spread log-normally around 3 (σ = 0.5, real-differences case); Copilot acceptance of 30% for everyone (identical case) or spread per engineer as Beta(12, 28), mean 30%, on about 150 shown completions a week with a log-normal spread (σ = 0.6) (real-differences case); combined score = sum of the two ranks; bottom 12 flagged each week; 400 to 500 runs per scenario. "Truly lowest" means lowest on the same two metrics, which is not the same as lowest in value.

## 11. Rollout

| When | What |
|---|---|
| Weeks 0–2 | Share purpose and draft with the works council and engineers; DPO starts the DPIA; agree retention, access and suppression |
| Weeks 2–4 | Build ingestion (GitHub, CI/CD, incident and on-call tools, scanner, Copilot API); backfill 26 weeks; validate figures with 2–3 teams |
| After consent | Go live; teams review their own row weekly; leadership reviews the organisation view monthly |
| Weeks 4–16 | Copilot comparison (section 6) |
| Month 6 | Review the dashboard with the works council and teams; drop what nobody used |

## 12. Sources

- GitHub Docs, [About Copilot usage metrics](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics) and [Interpreting Copilot metrics](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/interpret-copilot-metrics), read November 2026
- Ziegler et al., [Productivity assessment of neural code completion](https://arxiv.org/abs/2205.06537) (2022)
- DORA metrics, [dora.dev](https://dora.dev/guides/dora-metrics/history/)
- Faros AI, [The AI Productivity Paradox Report 2025](https://www.faros.ai/blog/ai-productivity-paradox-report-2025)
- Veracode, [2025 GenAI Code Security Report](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)
- Autoriteit Persoonsgegevens, list of processing operations requiring a DPIA, [Staatscourant 2019, 64418](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)
- Wet op de ondernemingsraden, art. 27; Burgerlijk Wetboek, art. 7:669; GDPR arts. 5, 22, 25 and 35; EU AI Act, Annex III and art. 26(7)
