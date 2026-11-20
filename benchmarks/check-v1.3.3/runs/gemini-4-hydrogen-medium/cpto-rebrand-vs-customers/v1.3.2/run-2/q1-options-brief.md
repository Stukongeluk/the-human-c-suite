# Q1 Plan & Options Brief: Rebrand + Customer Retention

**Prepared for:** CEO & Executive Leadership  
**Owner:** Head of Product  
**Context:** Post-merger Q1 planning (400-person SaaS organisation)

---

## 1. The Situation in Numbers

- **Customer sentiment:** NPS has dropped 24 points, from **+28 to +4**.
- **Open product blockers:** Three core workflows—**slow invoicing**, a **broken accounting integration**, and **missing reports**—have remained unresolved for months.
- **Current Q1 mandate:** Allocate 100% of product and engineering to the rebrand (in-app name change, new design system, new domain, new marketing site).

Shipping one unified brand after last year's merger is the right strategic signal for the market, sales, and the board. The risk is timing and scope: launching a new brand and marketing site while core billing and accounting workflows are broken will drive new traffic into a degraded product and accelerate churn among existing accounts.

In addition, not all engineering teams can meaningfully accelerate a marketing site, domain migration, or design system—putting backend, data, and integration engineers on frontend rebrand work creates hand-off overhead without speeding up the launch.

---

## 2. Q1 Capacity Options

Before committing Q1, we should allocate capacity realistically—leaving a 15% buffer for incidents, support escalations, and unplanned post-merger work so dates hold without overtime.

| Workstream | Option A: 100% Rebrand (Current) | Option B: Split Q1 (Recommended) |
|---|---|---|
| **Rebrand (in-app name, domain, marketing site)** | 55% | 45% (MVP brand tokens, domain, site) |
| **Full design system rewrite** | 30% | 0% (phased into Q2–Q3) |
| **Top 3 customer blockers (invoicing, accounting, reports)** | 0% | 40% |
| **Incidents, support escalations & reliability buffer** | 15% | 15% |
| **Total** | **100%** | **100%** |

### What Option B Delivers in Q1
1. **Rebrand ships on time:** Customers and prospects see the new name, updated brand tokens/shell in-app, the new domain with clean redirects, and the new marketing site.
2. **Design system is sequenced safely:** Instead of blocking Q1 on a full component-by-component rewrite, we ship the visual tokens (colours, typography, logo, navigation shell) in Q1 and migrate legacy components incrementally in Q2–Q3.
3. **Churn drivers are addressed before the launch push:** Dedicated backend, integration, and reporting squads fix invoicing latency, restore the accounting integration, and ship the highest-demand reports—matching people to the systems they already know.

---

## 3. Risks & Trade-offs

- **Option A (100% Rebrand):** Fastest path to a full design system, but leaves invoicing, accounting, and reporting broken for another 3+ months. High risk of further NPS decline and preventable churn right as the new brand goes live.
- **Option B (Split Q1):** Full design-system uniformity across every legacy screen moves to Q2–Q3. In exchange, the public rebrand still launches in Q1 *and* the three biggest sources of customer pain and support load are resolved.

---

## 4. Q1 Success Metrics (Reviewed Biweekly)

| Category | Metric | Q1 Target / Guardrail |
|---|---|---|
| **Customer** | NPS | Reverse the drop from +4 (track monthly cohort trend) |
| **Customer** | Accounting integration & invoicing | Zero critical integration sync failures; invoicing p95 latency within SLA |
| **Rebrand** | Launch milestones | New domain, marketing site, and in-app brand tokens live by end of Q1 |
| **Delivery & Health** | Unplanned work & overtime | Unplanned work held within the 15% buffer; zero planned overtime |

---

## 5. Immediate Next Steps

1. **Pull raw impact data (48 hours):** Attach ARR at risk, churned/downgraded accounts, and support ticket volume to the three open complaints (invoicing, accounting integration, missing reports).
2. **Confirm team-level capacity (Week 1):** Have engineering leads size the rebrand MVP (without a full design system rewrite) vs. the three customer fixes using recent throughput.
3. **Lock Q1 commitments & communicate clearly:** Publish what is in Q1, what moves to Q2 (full design system), and give sales/CS clear language on what customers can expect and when.
