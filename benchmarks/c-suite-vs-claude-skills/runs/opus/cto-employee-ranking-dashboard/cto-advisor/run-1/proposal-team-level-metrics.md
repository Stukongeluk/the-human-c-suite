# Measuring the Copilot rollout and delivery health: a proposal

*Draft for discussion. Replace the [brackets] before sending.*

## What we want to know

1. **Is Copilot paying off?** Is it being used, and is delivery getting faster without getting less safe?
2. **Where is delivery getting stuck?** Which teams need help, tooling or more people?

We want to answer both in a way that engineers trust, so the numbers stay honest, and that holds up with HR, the privacy officer and the works council (OR).

## What we'd track

We'd look at weekly trends per team, reviewed monthly with the engineering managers, starting from a baseline taken before the Copilot rollout.

| Question | Metric | Source |
|---|---|---|
| Is Copilot being used? | Active users, acceptance rate per team and language (a sign of how well the tool fits, not a score for people) | GitHub Copilot usage metrics, aggregated to team level before anyone sees them |
| Is delivery faster? | Lead time for changes, deployment frequency, PR cycle time (open to merge), time PRs wait for review | GitHub, CI/CD |
| Is it still safe? | Change failure rate, time to restore service, reverted or reworked PRs | Incident tracker, CI/CD |
| How does it feel? | Short quarterly survey on perceived productivity and friction | Survey tool |

## What we wouldn't do, and why

- **No individual rankings.** The SPACE framework's authors, who include DORA's Nicole Forsgren, say activity metrics such as PR counts "should never be used in isolation either to reward or to penalize developers". They recommend reporting at team level only. ([ACM Queue](https://queue.acm.org/detail.cfm?id=3454124))
- **Acceptance rate is not a measure of performance.** GitHub describes it as a sign that suggestions are relevant and useful. In GitHub's own research it predicted *self-reported* productivity, and junior developers accepted more suggestions. ([GitHub Docs](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics), [CACM](https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity))
- **More AI use doesn't automatically mean better delivery.** The 2024 DORA report found that a 25% rise in AI adoption went with an estimated 1.5% drop in delivery throughput and a 7.2% drop in delivery stability. ([Google Cloud](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)) In METR's early-2025 randomised trial, experienced developers took 19% longer with AI tools while believing they had been 20% faster. METR's late-2025 follow-up points towards a speedup, but the result is inconclusive. ([METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [METR 2026 update](https://metr.org/blog/2026-02-24-uplift-update/)) This is why we'd measure delivery outcomes, not usage.
- **No automatic improvement plans.** A fixed bottom 10% always selects someone. Dutch courts expect a plan to rest on a clearly backed-up performance problem, with concrete and achievable goals and real support. ([UWV](https://www.uwv.nl/werkgevers/Images/factsheet-ontslag-bij-disfunctioneren.pdf), [HR Praktijk](https://www.hrpraktijk.nl/juridisch/ontslag/rechters-maken-duidelijk-waaraan-verbetertrajecten-moeten-voldoen/))

## Individual performance

Individual performance stays with line managers, based on regular 1:1s, concrete examples and peer feedback. Development comes first, and a formal improvement plan only follows through the HR process. A metric can prompt a question ("your PRs wait three days for review, what's going on?"), but it never decides the outcome.

## Before launch

- [ ] HR and the privacy officer have reviewed the design.
- [ ] A DPIA (privacy impact assessment) is done if any per-person data is processed. The AP lists systematic monitoring of employees as needing one. ([Dirkzwager](https://www.dirkzwager.nl/kennis/artikelen/definitieve-nederlandse-lijst-verwerkingen-waarbij-dpia-gegevensbeschermingseffectbeoordeling-verplicht-is-gepubliceerd))
- [ ] OR consent has been requested in writing under article 27 WOR, which covers assessment systems, the processing of personal data and performance-monitoring systems. ([Dirkzwager](https://www.dirkzwager.nl/kennis/artikelen/instemmingsrecht-van-de-or-volgens-het-or-privacyboekje-van-de-ap))
- [ ] Engineers have been told what is collected, why, and who can see it.

## Pilot

- **Scope:** 6 weeks with [2–3 teams], including the pre-rollout baseline.
- **Review in week 6:** the VP and the engineering managers decide whether to keep, change or stop it.
- **Test of the original idea (optional):** managers privately compare last quarter's "bottom 10%" on acceptance rate and PRs merged with who they actually see struggling. If the two lists don't match, that settles it.

## Offer

I'm happy to build the first version of the team dashboard with [platform team / names] within [two sprints], and to present it at the week-6 review.

[Your name]
