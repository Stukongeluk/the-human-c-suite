# Proposal: Measuring Engineering Delivery & AI Impact Without Individual Rankings

**Context:** Leadership wants weekly visibility into engineering productivity and Copilot return on investment. Using individual Copilot acceptance rates and PRs merged to rank engineers—and placing the bottom 10% on performance improvement plans—carries high delivery, quality, and compliance risks.

**Recommendation:** Track **team-level delivery and quality metrics** alongside **aggregated Copilot adoption**, and run a 6–8 week baseline before making any decisions about performance or tooling ROI.

---

## 1. Why Individual Copilot & PR Rankings Backfire

Individual activity metrics measure volume, not value, and quickly get gamed when tied to consequences:

- **More PRs ≠ faster delivery:** In Faros AI's 2025 telemetry across 10,000+ developers, high-AI-adoption teams merged **98% more PRs**, but **PRs grew 154% larger** and **code review time rose 91%**.
- **Acceptance rate ≠ quality:** Uplevel's 2024 study (~800 developers) found no significant improvement in cycle time or throughput with Copilot, alongside **41% more bugs**.
- **Perverse incentives:** Ranking individuals on PRs and Copilot acceptance penalizes senior engineers who spend time reviewing code, mentoring, resolving incidents, and deleting dead code—and encourages splitting trivial PRs or accepting poor AI suggestions just to stay out of the bottom 10%.

---

## 2. Compliance Note (Netherlands)

In a 300-person Dutch company, a works council (*ondernemingsraad*, OR) is mandatory under the Works Councils Act (*Wet op de ondernemingsraden*, WOR).

- **Consent right (Article 27(1)(l) WOR):** The OR generally has a right of consent (*instemmingsrecht*) over any system suited to monitoring employee attendance, behaviour, or performance. Per-person Copilot usage dashboards and individual PR rankings used for PIPs fall squarely in this area.
- **Practical impact:** Rolling out individual tracking without OR consent risks formal challenge and delays. Aggregated, team-level reporting avoids individual surveillance while giving leadership the operational visibility it needs.

*(Note: This is an operational flag, not legal advice; confirm specifics with HR and legal counsel.)*

---

## 3. What to Measure Instead (Team & System Level)

Following the **DORA** and **SPACE** frameworks, pair every speed metric with a quality and health check:

| Question | Team Metric | Source |
|---|---|---|
| **How fast and safely do we ship?** | Change lead time, deployment frequency, change fail rate, failed deployment recovery time | CI/CD, Git, incident tool |
| **Where does work get stuck?** | Cycle time per stage, review wait time, PR size, work in progress (WIP) | Git hosting, Jira/Linear |
| **Is Copilot helping?** | Team-level active seats + before/after trends in lead time, rework, and escaped defects | Copilot admin (aggregated), CI/CD |
| **How are individual concerns handled?** | Clear role expectations, regular 1:1 feedback, peer/code evidence via managers—never a dashboard | Engineering managers & HR |

---

## 4. Proposed Next Step

1. **Aggregate Copilot and Git metrics at the team level** (limit per-person admin views).
2. **Baseline for 6–8 weeks** on the four DORA/flow metrics above to spot where work is actually waiting (often review queues or unplanned work).
3. **Review monthly with engineering managers** to remove system bottlenecks, while handling genuine individual performance issues through normal management and HR processes.

---

### Sources
- DORA, *2025 State of AI-assisted Software Development* & DORA metrics guide (`dora.dev`)
- Forsgren et al., *The SPACE of Developer Productivity*, ACM Queue (2021)
- Faros AI, *The AI Productivity Paradox Report* (2025)
- Uplevel study on Copilot impact, via CIO (2024)
- Wet op de ondernemingsraden (WOR), Article 27(1)(l)
