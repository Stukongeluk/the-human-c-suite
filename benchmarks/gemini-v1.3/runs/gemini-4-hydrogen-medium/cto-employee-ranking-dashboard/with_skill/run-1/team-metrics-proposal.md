# Proposal: Measuring Engineering Delivery and AI Impact at Team Level

**Purpose:** Give engineering leadership clear visibility into delivery speed, quality, and whether our Copilot investment is paying off—without introducing metrics that slow down code review, distort engineering behaviour, or create compliance risk under Dutch law.

---

## 1. Why Individual Activity Rankings Backfire

Ranking engineers weekly on **Copilot acceptance rate** and **PRs merged** measures individual activity, not software delivery. In practice, it creates three problems:

1. **It rewards the wrong work and punishes team glue.** Engineers who take on hard architecture problems, review others' PRs, mentor juniors, handle incidents, or delete dead code merge fewer PRs and accept fewer autocomplete suggestions. Under an individual ranking, those behaviours are penalised.
2. **It invites gaming and shifts the bottleneck to review.** When PR count and AI acceptance rate are tied to performance plans, engineers naturally split changes into trivial PRs and accept boilerplate suggestions.
   - **Faros AI (2025, telemetry from 10,000+ developers)** found that on high-AI-adoption teams, developers merged **98% more PRs**, but PRs grew **154% larger** and **review time rose 91%**.
   - **GitClear (2023–2026, 623 million code changes)** found code block duplication up **81%** alongside a sharp drop in refactoring.
   - **Uplevel (2024, ~800 developers)** found no significant improvement in cycle time or throughput with Copilot, alongside **41% more bugs**.
3. **Acceptance rate does not measure value.** Accepting a suggestion only means a developer pressed Tab; it says nothing about whether the code was correct, maintainable, or still there a week later.

---

## 2. Dutch Works Council & Compliance Check (Not Legal Advice)

At a 300-person company in the Netherlands, a works council (*ondernemingsraad*, OR) is mandatory (threshold: 50 employees). Before using per-person Copilot analytics or GitHub PR rankings for performance management or improvement plans:

- **Works Councils Act (WOR), Article 27(1)(l):** Systems suited to monitoring employee attendance, behaviour, or performance generally require **prior consent (*instemmingsrecht*)** from the works council. This applies to vendor admin consoles that expose individual AI usage when used to evaluate staff.
- **GDPR & Privacy:** Processing individual telemetry for automated or semi-automated performance ranking requires a clear legal basis, data minimisation, and transparency.
- **EU AI Act (for context):** Under Annex III and Article 26(7), AI systems used to monitor or evaluate workers or inform dismissal decisions are classified as high-risk; the EU-wide duty to inform workers and representatives applies from **2 December 2027**. National Dutch co-determination rules (WOR) already apply today.

*Recommendation: Have HR and legal counsel confirm WOR and GDPR requirements before enabling any individual-level reporting.*

---

## 3. Recommended Alternative: Team-Level Delivery & Flow Metrics

Instead of ranking individuals, measure **systems and teams** on a 4-week rolling basis, pairing every speed metric with a quality or health metric, and compare each team against its own baseline:

| Question | Metrics | Source |
|---|---|---|
| **Are we shipping faster and safely?** | **DORA:** Change lead time, deployment frequency, change fail rate, failed deployment recovery time, deployment rework rate | CI/CD, deployment logs, incident tool |
| **Where is work getting stuck?** | Cycle time per stage, **review wait time**, PR size, work in progress (WIP) per team | Git hosting, Jira/Linear |
| **Is Copilot actually helping?** | Compare team DORA + review wait time + escaped defects before/after adoption (or across a pilot vs. comparison group) | Git hosting, CI/CD, QA/support |
| **Is the team sustainable?** | Share of unplanned work, after-hours on-call pages, quarterly developer experience pulse (aggregated) | Incident tool, short anonymous survey |

### Handling Individual Underperformance
If a manager has a genuine concern about an individual engineer's work, that should be handled directly through clear expectations, regular feedback, peer and code-review evidence, and structured coaching—not through an automated weekly activity percentile.

---

## 4. Next Steps

1. **Limit individual views:** Configure Copilot and Git analytics dashboards so individual-level usage is restricted, and report only team/org aggregates.
2. **Agree a 6–8 week team baseline:** Track change lead time, review wait time, PR size, and change fail rate per team.
3. **Align with HR and the OR:** Confirm compliance with Article 27(1)(l) WOR before any performance-related tooling is rolled out.

---

### Sources
- DORA, *State of DevOps / State of AI-assisted Software Development* (2024, 2025) — [dora.dev](https://dora.dev)
- Faros AI, *The AI Productivity Paradox Report* (2025)
- GitClear, *Coding on Copilot / Code Quality Research* (2023–2026)
- Uplevel, *Copilot Effectiveness Study* (2024)
- Netherlands Works Councils Act (*Wet op de ondernemingsraden*, Art. 27(1)(l)); EU AI Act (Regulation (EU) 2024/1689, Art. 26(7) & Annex III, as amended by the 2026 Digital Omnibus).
