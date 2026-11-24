# Engineering metrics that help, and the ones that hurt

Read this when choosing, reviewing or being asked for engineering metrics: productivity questions, "who are our weakest engineers", dashboards for the board, or measuring an AI tool.

## Contents

- 1. Principles
- 2. What to measure
- 3. Metrics that mislead
- 4. "Which engineers are underperforming?"
- 5. Answering "how much should we invest in engineering?"
- 6. Sources

## 1. Principles

- **Measure the system, not the person.** Software is built by teams through reviews, pairing, on-call and shared code. Individual activity counts don't capture who made the team better.
- **Pair every speed metric with a quality or health metric,** so nobody can hit one target by breaking something else.
- **Use metrics to ask better questions, not to rank people.** Once a number decides bonuses or layoffs, people optimise the number.
- **Compare a team with its own past,** not teams with each other: different codebases, domains and on-call loads make cross-team comparisons misleading.
- **Ask the engineers.** Developer experience surveys catch friction that no pipeline metric shows.
- **Agree it with the people measured.** Engineering analytics and AI-usage dashboards that can show individual performance are monitoring systems. That includes the AI vendors' own admin consoles, which often show per-person usage by default, so limit who can see the per-person views. In Germany and the Netherlands they usually need works council agreement before rollout, and everywhere the agreement makes the numbers more honest. More: [european-and-nordic-practice.md](european-and-nordic-practice.md).

## 2. What to measure

| Question | Metrics | Source |
|---|---|---|
| How fast and safely do we deliver? | DORA: change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate | CI/CD, deployment logs, incident tool |
| Where does work get stuck? | Cycle time per stage, work in progress per team, blocked time, review wait time, pull-request size | Jira, Linear, Git hosting |
| How much capacity goes to the past? | Share of unplanned work, incidents per service, time spent on toil and maintenance | Jira labels, incident tool, surveys |
| Is the system healthy? | Availability against SLOs, error budgets burnt, open security findings by age, dependency freshness | Observability, security scanners |
| Are people OK? | On-call pages outside working hours per rotation, engagement and developer experience scores, regretted attrition, time to onboard | Incident tool, surveys, HR aggregates |
| Does it matter to customers? | Adoption of what shipped, customer-reported defects, outcome metrics agreed with product | Product analytics, support |

SPACE is a useful check that you cover satisfaction, performance, activity, communication and efficiency, not activity alone.

## 3. Metrics that mislead

| Metric | Why it misleads | Use instead |
|---|---|---|
| Story points, velocity | A team's own estimate; inflates under pressure; not comparable between teams | Cycle time, items delivered, outcomes |
| Lines of code, commits, pull requests per person | Rewards volume; AI makes volume cheap; punishes deletion and simplification | Change lead time, rework rate, code health trends |
| Tickets closed per person | Rewards easy tickets, discourages helping others | Team flow plus customer result |
| Utilisation, hours logged | Full utilisation creates queues and kills improvement | Flow efficiency, sustainable pace |
| AI suggestion acceptance rate, "% of code written by AI" | Measures tool usage, not value; can rise while quality falls | Delivery and quality metrics before and after, with a comparison group |
| Number of features shipped | Most shipped features are rarely used | Adoption and outcome of what shipped |

## 4. "Which engineers are underperforming?"

Don't produce a ranking from activity data. Answer the question behind it:

1. **What is the real concern?** Delivery is slow, quality is poor, a specific person's work worries a manager, or costs must come down. Each has a different answer.
2. **Look at the system first.** Long review queues, high work in progress, unplanned work, unclear ownership and painful on-call explain most "slow teams".
3. **For a real individual concern,** the manager handles it through clear expectations, regular feedback, support and a fair chance, with HR involved where needed. Evidence comes from the work and from peers, not from a dashboard.
4. **Say plainly why activity rankings fail:** they punish the people who review, mentor, fix incidents and remove code, and they invite gaming.

## 5. Answering "how much should we invest in engineering?"

Leaders who ask about productivity often want to know whether engineering spend is paying off. Answer that question directly: what engineering delivered against agreed outcomes, what it costs per outcome area, where capacity is lost (unplanned work, waiting, toil) and what investment would recover it.

## 6. Sources

- DORA metrics, including deployment rework rate: [dora.dev](https://dora.dev/guides/dora-metrics/history/)
- SPACE framework: Forsgren et al., [ACM Queue (2021)](https://queue.acm.org/detail.cfm?id=3454124)
- Gergely Orosz and Kent Beck, ["Measuring developer productivity? A response to McKinsey"](https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity) (2023): the real executive question is how much to invest in engineering, and narrow measurement invites gaming
