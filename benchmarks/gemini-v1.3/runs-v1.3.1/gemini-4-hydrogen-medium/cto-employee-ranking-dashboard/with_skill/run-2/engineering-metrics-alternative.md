# Proposing a Better Alternative to Individual PR and Copilot Rankings

> **Note:** Employment law and works council rules depend on your company's structure and collective agreements. Treat the legal points below as a prompt to check with HR, your works council (*ondernemingsraad*), or employment counsel—not as legal advice.

## 1. Why the VP's proposal backfires (in terms a VP cares about)

Leaders usually ask for individual activity rankings because they want faster delivery, higher AI ROI, or visibility into where engineering is stuck. Weekly rankings by **Copilot acceptance rate** and **PRs merged** hurt all three goals:

* **It punishes the work that keeps delivery fast:** Senior engineers who spend time reviewing PRs, unblocking teammates, handling incidents, mentoring, or deleting dead code merge fewer PRs. Ranking by PR count pushes everyone toward small, isolated, low-risk PRs and away from reviews.
* **It rewards volume over quality:** AI makes generating code cheap. Measuring Copilot acceptance rate incentivises accepting suggestions uncritically, which increases rework and bugs. In a 2025 randomised trial by METR, experienced open-source developers actually took 19% longer on tasks when using AI tools—even though they believed they were faster—showing that AI usage alone does not equal delivery speed.
* **Bottom-10% PIPs destroy trust and retention:** Once a metric decides improvement plans, people optimise the metric (splitting PRs, accepting boilerplate) while your best collaborators quietly look for another job.

## 2. What to propose instead: system and team metrics

Offer a concrete dashboard that answers the VP's real questions without ranking individuals:

| Question | System / Team Metrics | What it tells the VP |
| :--- | :--- | :--- |
| **Are we shipping fast and safely?** | **DORA metrics:** change lead time, deployment frequency, change fail rate, failed deployment recovery time, deployment rework rate | Whether delivery speed is improving *without* breaking production |
| **Where is work getting stuck?** | PR review wait time, work in progress (WIP) per team, PR size, blocked time | Concrete bottlenecks (e.g. review queues or oversized PRs) that leadership can actually fix |
| **How much capacity goes to the past?** | Share of unplanned work, incidents per service, time spent on maintenance/toil | Why feature delivery feels slow |
| **Is AI actually helping?** | Team DORA metrics before vs. after rollout, paired with developer experience surveys | Real ROI on AI spend, rather than raw acceptance rate |

*(Sources: [DORA](https://dora.dev/guides/dora-metrics/history/); Forsgren et al., [SPACE framework, ACM Queue 2021](https://queue.acm.org/detail.cfm?id=3454124); Orosz & Beck, [Measuring developer productivity](https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity).)*

## 3. Governance in the Netherlands (your quietest lever)

At a 300-person company in the Netherlands, a works council (*ondernemingsraad*, OR) is mandatory (threshold: 50 employees).

* **Works council consent (*instemmingsrecht*):** Under **Article 27(1)(l) of the Dutch Works Councils Act (WOR)**, the works council has a right of consent over any system suited to monitoring employee attendance, behaviour, or performance. Per-person Copilot and GitHub activity dashboards used for performance management or improvement plans fall squarely in that territory.
* **EU AI Act context:** Automated systems used to monitor or evaluate workers are classified as high-risk under Annex III of the EU AI Act. Note that the specific duty under Article 26(7) to inform workers' representatives before using high-risk AI at work was moved by the 2026 Digital Omnibus to **2 December 2027**, so it is not in force yet—but Dutch WOR consent rules already apply today.

Asking *"Has HR / the OR reviewed the per-person tracking yet?"* is a routine compliance question, not rebellion.

## 4. A neutral message you can adapt

Use this 1-on-1 with your engineering manager or skip-level before the policy is finalised:

> "I want to make sure the new VP gets real visibility into how fast we're shipping and whether Copilot is paying off. My concern with a weekly individual ranking on PRs merged and Copilot acceptance rate is that it penalises people who do heavy code review, incident response, and architecture work—and it's easy to game with tiny PRs. Also, since we're 300 people in the Netherlands, individual performance tracking tied to PIPs usually needs works council (*OR*) consent under Article 27 WOR.
>
> Would you be open to me putting together a quick team-level view—DORA metrics, PR review wait times, and unplanned work—so we can offer the VP a cleaner way to spot bottlenecks?"
