# Proposal: Measuring Engineering Delivery and AI Impact at Team Level

**Goal:** Give engineering leadership clear visibility into delivery speed, code quality, and the return on our Copilot investment—without creating perverse incentives or compliance risk.

## Why individual activity rankings backfire

Ranking engineers weekly on **PRs merged** and **Copilot acceptance rate** measures activity, not outcomes:

- **PRs merged** rewards splitting work into tiny, noisy PRs and penalises engineers who do high-leverage work that doesn't show up as personal PR volume: thorough code reviews, mentoring, incident response, architecture work, and deleting dead code.
- **Copilot acceptance rate** measures how often suggestions are clicked, not whether the code is right or ships faster. Accepting more generated code can increase review load and rework while making the metric look better.
- **Tying rankings to PIPs** triggers Goodhart's Law: people optimise the number (fewer reviews for teammates, more trivial PRs, accepting boilerplate) while overall delivery slows down.

## Recommended alternative: Team-level DORA + Flow + Quality

Measure **systems and teams**, pair every speed metric with a quality metric, and compare teams against their own past rather than against each other:

| Question | Metrics (Team / System Level) | Source |
|---|---|---|
| **How fast and safely do we ship?** | Change lead time, deployment frequency, change fail rate, failed deployment recovery time, deployment rework rate (DORA) | CI/CD, deployment logs, incident tracker |
| **Where does work get stuck?** | PR review wait time, work in progress (WIP) per team, PR size | Git hosting, Jira / Linear |
| **Is Copilot helping?** | Team delivery & rework trends before/after adoption, paired with a brief developer experience pulse | CI/CD + quarterly survey |
| **How do we handle individual underperformance?** | Clear role expectations, regular 1:1 feedback, peer/manager evidence from actual work, and structured support via HR | Manager 1:1s, HR process |

## Governance note (Netherlands)

Because we have more than 50 employees in the Netherlands, our Works Council (*Ondernemingsraad*, OR) has a consent right (*instemmingsrecht*) under **Article 27(1)(l) of the Works Councils Act (WOR)** over systems suited to monitoring employee behaviour or performance. Using per-person GitHub/Copilot dashboards for performance management or PIPs without prior OR consent risks challenge and reversal. Aggregating metrics at the **team level** avoids individual surveillance while giving leadership the operational signal it needs. *(Note: confirm exact scope with HR and legal counsel.)*

## Suggested next step

Run a **6-week baseline** of team-level DORA and review-wait metrics across teams, plus an anonymous developer-experience check on where work slows down, before introducing any new performance-tracking tooling.

---
*References: [DORA Metrics](https://dora.dev/guides/dora-metrics/history/); Forsgren et al., "The SPACE of Developer Productivity", ACM Queue (2021); Gergely Orosz & Kent Beck, "Measuring developer productivity? A response to McKinsey" (2023).*
