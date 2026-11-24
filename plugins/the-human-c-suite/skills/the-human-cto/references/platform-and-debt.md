# Platform health, technical debt and sustainable on-call

Read this when reliability, tech debt, platform teams, on-call or team structure come up, or when "quick wins" would come out of the long-term health of the system and the people running it.

## Contents

- 1. Technical debt is a budget line
- 2. Reliability without heroics
- 3. Humane on-call
- 4. Platform teams
- 5. Team structure and reorgs
- 6. Outsourcing engineering work

## 1. Technical debt is a budget line

- In Stripe's Developer Coefficient survey (2018), developers estimated they spent 13.5 hours of a 41-hour week on technical debt and another 3.8 on bad code. It's a survey estimate, but every engineer recognises the pattern.
- Make debt visible: hotspots, unplanned work per team, incident causes, time to onboard, and what the teams themselves say slows them down.
- Fund it explicitly: a fixed share of capacity, a debt item in every planning cycle, or a dedicated stream. Agree it with product so it isn't cut first when the roadmap is full.
- Pay down the debt that slows the most people or causes the most incidents first. Not all debt needs paying.
- Unplanned work above roughly a quarter of a team's time is a warning sign: the team is serving the past instead of building the future.

## 2. Reliability without heroics

- Agree service level objectives with product and the business, and use error budgets to decide when reliability work takes priority over features.
- Run blameless post-mortems: focus on how the system made the failure possible, not who pressed the button. People who fear blame hide problems. End every post-mortem with actions that each have an owner, a date and a measure that shows they worked, such as a timed rollback rehearsal or a lower change failure rate, and report those to whoever asked for accountability.
- Track repeat causes and fix them; repeated incidents are toil you can remove.
- A team that keeps the lights on through heroics is a risk, not a success story.

## 3. Humane on-call

- Rotations big enough that nobody is on call every other week (six or more people per rotation is a common rule of thumb).
- Pages outside working hours are measured per rotation and reduced deliberately. Noisy alerts are fixed or removed.
- On-call is paid or compensated, and time off after a heavy night is normal.
- The people on call have the authority and time to fix what wakes them up.
- New people join on-call with shadowing and runbooks, not alone.

## 4. Platform teams

- A platform team exists to make other teams faster and safer: paved roads, self-service, good defaults. Measure it by its users' experience and their delivery metrics.
- Platforms have costs too. DORA 2024 found that teams using an internal developer platform reported higher productivity, yet throughput fell 8% and change stability 14%, which the report linked to extra hand-offs between teams and systems. So make the platform self-service and the easy choice rather than a mandate, and measure delivery before and after teams move.
- Platform teams carry heavy on-call and unplanned work. Watch their health first when a migration or consolidation lands on them.

## 5. Team structure and reorgs

- Conway's law: systems mirror the communication structure of the organisations that build them. Change team boundaries and you change the architecture over time, and the reverse.
- Size teams so their cognitive load is manageable: a team should be able to understand, change and run what it owns. Team Topologies (Skelton and Pais, 2019) is a useful vocabulary: stream-aligned, platform, enabling and complicated-subsystem teams.
- Reorganise only to solve a named problem (handoffs, unclear ownership, overload), in phases, with the people affected involved early. Each reorg costs weeks of lost context and trust.
- Never use a reorg to hide a layoff, or a layoff to fix a structure problem.

## 6. Outsourcing engineering work

- Keep core and quality-critical work, and the knowledge of how your system really works, in-house. Commodity work can be bought.
- Count the full cost: hand-offs, rework, management overhead, lost knowledge, lock-in and the cost of bringing work back.
- If you outsource, keep an in-house owner who understands the system, set quality metrics, and plan how the internal team grows rather than shrinks.

## Sources

- Stripe, [The Developer Coefficient](https://stripe.com/files/reports/the-developer-coefficient.pdf/) (2018)
- DORA 2024 platform engineering findings, as reported by [TechTarget](https://www.techtarget.com/it-infrastructure/news/366615375/Google-DORA-issues-platform-engineering-caveats); see also [DORA's platform engineering capability page](https://dora.dev/capabilities/platform-engineering/)
- Matthew Skelton and Manuel Pais, *Team Topologies* (2019)
