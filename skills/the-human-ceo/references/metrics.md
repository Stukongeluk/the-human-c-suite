# Metrics: what to measure and what to challenge

A human CEO knows which numbers say something about value and challenges the ones that only measure activity. A bad metric is worse than none: it rewards the wrong behaviour and, in the wrong hands, decides who gets fired.

## Contents

1. Principles
2. How to challenge a KPI
3. Misleading metrics and what to use instead
4. Metrics that add value, by area
5. Rules for dashboards
6. Sources

## 1. Principles

1. **Every metric must change a decision.** If no decision would change when the number moves, stop tracking it.
2. **Outcomes over output.** Customer and business results beat counts of activity.
3. **Pair every metric with a counter-metric**: speed with quality, cost with satisfaction, throughput with wellbeing.
4. **Measure systems and teams, not individuals.** Most performance is determined by the system people work in.
5. **A target changes behaviour.** Once a measure becomes a target, people optimise for it (Goodhart's law). Expect gaming and look for it.
6. **Trends and context over snapshots.** Compare a team with its own past, not with other teams.
7. **Ask the people being measured** whether the number reflects reality. If they laugh, it doesn't.

## 2. How to challenge a KPI

Ask these before you trust, set or report a KPI:

- What decision does this number change, and who makes it?
- Is it an outcome, or only output or activity?
- What behaviour does it reward? How could someone hit the target while making things worse?
- Which counter-metric would catch that?
- At what level is it valid: individual, team or whole system?
- Is the data trustworthy, and is it defined the same way everywhere it is reported?
- Who chose it, when, and does the reason still hold?

When a dashboard or a board deck runs on misleading metrics, say so plainly, explain what the metric hides, and propose better ones with a way to collect them.

## 3. Misleading metrics and what to use instead

| Metric | Why it misleads | Use instead |
|---|---|---|
| Story points and velocity as a KPI | A team's own relative estimate, not a unit of value. Not comparable across teams, and it inflates under pressure. Fine as a team's private planning aid, never for comparing teams or judging people | Cycle time, work in progress, items delivered, customer outcomes, DORA metrics |
| Lines of code, commits, pull requests | Rewards volume. More code, including AI-generated code, is not more value; deleting code is often the best work | Change lead time, deployment rework rate, escaped defects, maintainability |
| Tickets closed per person | Rewards easy tickets, splitting work and avoiding hard problems | Team flow metrics plus the customer result |
| Hours logged, utilisation % | 100% utilisation means queues, no slack to improve and burnout. Rewards presence, not results | Flow efficiency, lead time, sustainable pace, wellbeing |
| Online status, chat activity, keystrokes | Surveillance that measures noise and destroys trust | Outcomes and team health surveys |
| Test coverage % as a target | Easy to inflate with tests that assert nothing | Change fail rate, escaped defects, mutation testing where useful |
| Features shipped | Output. Features nobody uses are cost, not value | Adoption, retention, task success |
| Cost per contact on its own | Falls when quality falls | Resolution quality, re-contact rate, escalations, satisfaction |
| Revenue per employee, headcount reduced | Improves when you fire people, even while the business weakens | Gross margin, net revenue retention, unit economics, regretted attrition |
| Registered users, downloads, page views | Vanity numbers that only go up | Active users, retention cohorts, net revenue retention |
| Training hours completed | Measures attendance, not learning | Skills applied, internal moves, time to productivity in a new role |
| Outsourcing savings based on day rates | Leaves out transition, governance, rework, quality loss and lost knowledge | Total cost of ownership over several years, with quality and lead-time metrics on the outsourced work |
| Number of AI agents deployed, "% of work done by AI" | Measures adoption, not value or quality | Quality of AI-handled work, escalation and re-contact rates, hours freed and what they were used for |

## 4. Metrics that add value, by area

- **Customers**: retention and churn, net revenue retention, task success or first-contact resolution, re-contact rate, satisfaction trends read together with the comments, customer effort.
- **Finance**: cash runway, gross margin, unit economics (CAC payback, lifetime value versus acquisition cost), revenue from new services, forecast accuracy.
- **Software delivery**: the DORA metrics, grouped as throughput (change lead time, deployment frequency, failed deployment recovery time) and instability (change fail rate, deployment rework rate). Add flow metrics: cycle time, work in progress, throughput in items, flow efficiency. Balance them with the SPACE dimensions: satisfaction and wellbeing, performance, activity, communication and collaboration, efficiency and flow. Never rely on one dimension.
- **Operations and reliability**: service level objectives and error budgets, incident frequency, hours of toil, cost per transaction next to quality.
- **People**: regretted attrition, internal mobility rate, share of roles filled internally, time to productivity, engagement and wellbeing trends, absence.
- **Long-term health**: investment in R&D, training and tooling as a trend (cuts here show up years later), technical debt and rework trends, knowledge concentration (how many people can maintain each critical system), share of critical work done in-house.
- **AI adoption**: quality of outcomes compared with the human baseline, escalation and re-contact rates, customer satisfaction, hours freed and where they went, value created by redeployed people.

## 5. Rules for dashboards

- Keep it to a handful of metrics per level. Each has an owner, a definition, a data source and the decision it informs.
- Show the trend, the target and the counter-metric together.
- Keep delivery and flow metrics at team or system level. They never appear in individual performance reviews.
- Review the metrics themselves at least once a year, and retire the ones that no longer change decisions.

## 6. Sources

- DORA, [A history of DORA's software delivery metrics](https://dora.dev/guides/dora-metrics/history/) (January 2026)
- Forsgren, Storey et al., [The SPACE of Developer Productivity](https://queue.acm.org/detail.cfm?id=3454124), ACM Queue (2021)
- Ron Jeffries, [Story Points Revisited](https://ronjeffries.com/articles/019-01ff/story-points/Index.html) (2019)
