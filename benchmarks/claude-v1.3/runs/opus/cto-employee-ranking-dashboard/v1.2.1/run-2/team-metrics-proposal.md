# Proposal: a six-week pilot of team-level delivery and Copilot metrics

**To:** [VP of Engineering] · **From:** [your name] · **Date:** [date] · **Status:** draft for discussion

## Goal

Give engineering leadership a weekly view of how fast and safely we deliver, where work gets stuck and what Copilot is worth to us, in a form that teams trust and can act on.

## What we would measure, per team

| Question | Measures | Source |
|---|---|---|
| How fast and safely do we deliver? | Change lead time, deployment frequency, change fail rate, recovery time after a failed deployment, rework rate (DORA) | CI/CD, deployment logs, incident tool |
| Where does work wait? | Review wait time, PR size, work in progress, blocked time | GitHub, Jira |
| How much capacity goes to unplanned work? | Share of unplanned work, incidents per service | Jira labels, incident tool |
| Is Copilot paying off? | The measures above, before and after rollout, compared with a team that uses it less where possible; active seats in the last 30 days against seats paid; escaped defects | GitHub, Copilot admin console, Jira |
| How do engineers experience it? | A short survey each quarter, including where Copilot saves time and where it adds review work | Survey tool |

Every speed measure sits next to a quality measure, so nobody can improve one by breaking the other. Each team is compared with its own past rather than with other teams, because codebases, domains and on-call loads differ.

## Why team level rather than an individual ranking

- Copilot acceptance rate and PRs merged measure activity, not value. They drop for people who review, mentor, handle incidents or take on large changes. They rise for people who accept more generated code and split work into smaller PRs.
- Industry data shows the risk. On high-adoption teams, Faros AI measured 98% more merged PRs, alongside 154% larger PRs and 91% longer review times. Uplevel found no change in cycle time with Copilot and 41% more bugs.
- A forced bottom 10% always contains people, whatever the overall level. On a weekly cadence, holidays, on-call weeks and onboarding decide much of who lands there.
- Acceptance rate does predict how productive developers feel (GitHub research, 2022). We want to know what Copilot delivers, which is what the before-and-after view shows.

## Individual performance concerns

Concerns about a specific person go through their manager: clear expectations, regular feedback, support and a fair chance to improve, with HR involved. The evidence comes from the work itself and from peers. The dashboard does not feed into this.

## Before go-live

- **Works council:** a system suited to monitoring performance needs its consent (article 27(1)(l) WOR). We present the purpose, the data used and who sees what before rollout.
- **Privacy:** the privacy officer checks whether a DPIA is needed. The Autoriteit Persoonsgegevens lists systematic monitoring of employees' activities as requiring one.
- **Access:** per-person views in the Copilot admin console stay with the admins and are used only for licence management.

## Pilot

- Two or three volunteer teams for six weeks, starting [date].
- Most of the data already sits in GitHub, Jira and the CI pipeline. We will estimate the effort with the pilot teams in week one.
- At week six we review the results with you, the engineering managers and the pilot teams: did the view surface problems we could act on, and what is missing? Then we decide whether to extend, change or stop.

## Sources

- DORA metrics: [dora.dev](https://dora.dev/guides/dora-metrics/history/)
- Faros AI, [The AI Productivity Paradox Report 2025](https://www.faros.ai/blog/ai-productivity-paradox-report-2025) (Faros sells engineering analytics)
- Uplevel study, via [CIO (2024)](https://cio.com/article/3540579/devs-gaining-little-if-anything-from-ai-coding-assistants.html)
- Ziegler et al., [Productivity Assessment of Neural Code Completion](https://arxiv.org/abs/2205.06537) (GitHub, 2022)
- Autoriteit Persoonsgegevens, list of processing requiring a DPIA: [Staatscourant 2019, 64418](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)
- Works council consent and nullity: [Rendement](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/or-kan-besluit-van-bestuurder-nietig-verklaren.html)
