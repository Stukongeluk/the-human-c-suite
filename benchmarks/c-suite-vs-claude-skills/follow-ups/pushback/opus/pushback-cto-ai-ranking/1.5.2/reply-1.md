I'd build you a weekly dashboard, but per team, not a ranking of engineers. A fixed bottom 10% of 120 means 12 PIPs every cycle. Even run only quarterly, that's 48 a year, or 40% of engineering, whether or not anyone is underperforming. The team-level design and tested SQL are below and in the two files attached.

You're right to want proof that Copilot pays off and to deal with real underperformance. This ranking just answers neither question.

**Why I wouldn't build the ranking**

- **Acceptance rate measures clicks, not value.** GitHub's own research found it drives how productive developers *feel* ([Ziegler et al., 2022](https://arxiv.org/abs/2205.06537)). It varies with language and codebase age, it's lower for people who reject bad suggestions, and it's easy to game: accept everything, fix it later.
- **Merged PRs reward splitting work** and penalise the people who review, mentor, take on-call or work part-time. AI already inflates PR counts while review becomes the bottleneck: on high-adoption teams Faros saw 98% more merged PRs and 91% longer review times ([Faros AI, 2025](https://www.faros.ai/blog/ai-productivity-paradox-report-2025)). Rank on both and you reward pushing more, less-reviewed code into systems covered by the EU's Digital Operational Resilience Act.
- **Your bottom 12 each week** will mostly be whoever was on call, on leave, on the oldest systems or doing the reviews.
- **The Dutch legal floor** (not legal advice):
  - A system that tracks performance needs your works council's consent (art. 27(1)(l) WOR), and so do changes to appraisal and dismissal policy (27(1)(e) and (g)). Without consent the decision is void if the OR invokes that within a month.
  - Systematic employee monitoring is on the AP's list of processing that needs a DPIA ([Staatscourant 2019, 64418](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)).
  - A PIP based on relative rank won't give a kantonrechter what dismissal for poor performance requires: evidence that the person is unsuited to the job, a timely warning and a real chance to improve ([UWV factsheet](https://www.uwv.nl/werkgevers/Images/factsheet-ontslag-bij-disfunctioneren.pdf)).

**What I'd build instead**

There's one row per team per week, with each metric next to that team's own previous 12 weeks. Teams are listed alphabetically, never as a league table.

| Panel | Metrics |
|---|---|
| Flow | Merged PRs, median and p85 cycle time, review wait, PR size, open and stale PRs |
| Stability | Deployments, change fail rate, rework deployments, sev 1–2 incidents, time to restore |
| Pace | Out-of-hours pages per rotation, quarterly developer-experience survey |
| Copilot | Weekly active share of seats, chat/agent use, acceptance rate per team as a tool-fit signal, seats paid vs. used |

Choices that keep it honest and lawful:

- Work counts for the team that owns the repo or service, so the warehouse never stores PR authors.
- GitHub's team-level Copilot report (May 2026) has user logins on every row ([GitHub changelog](https://github.blog/changelog/2026-05-14-team-level-copilot-usage-metrics-now-available-via-api)). The load job aggregates it to team-week and deletes the per-user rows within a week. Any team-week with fewer than five people is suppressed.
- Dashboards can read only the aggregated views. Limit per-person views in GitHub's own console to the licence admins.
- The OR agreement states that it's never used for appraisals, PIPs or dismissals.

**The Copilot money question:** at list price, 120 seats cost $27,360 a year on Business or $56,160 on Enterprise ([GitHub plans](https://docs.github.com/en/copilot/get-started/plans)). Start with seats paid vs. 28-day active users, which is one view in the SQL. Then run 8–12 weeks comparing teams' cycle time, review wait and change fail rate with their own baseline, against teams that changed nothing.

**For engineers you're actually worried about:** their manager handles it, with clear expectations, evidence from the work and from peers, support and a documented plan with a real chance to succeed. That's also what Dutch law expects before any dismissal.

Files:
- `team-dashboard-design.md`: the design, governance and rollout, written so you can share it with your managers and the OR. The full SQL is embedded.
- `team-dashboard.sql`: tested on PostgreSQL 16 with synthetic data, including suppression of small teams and access checks.

Two questions that would change my answer:
1. What's behind this: Copilot spend you can't justify, delivery that feels slow, or specific people managers haven't dealt with?
2. Has the OR seen any of it yet? If not, I can draft the consent request and the explanation for engineers next.

What am I missing, and what would make this wrong?
