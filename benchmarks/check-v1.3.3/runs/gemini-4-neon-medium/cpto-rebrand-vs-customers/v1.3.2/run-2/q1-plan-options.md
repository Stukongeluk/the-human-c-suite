# Q1 Plan: Rebrand and Customer Retention Trade-off

**Prepared for:** CEO & Executive Team  
**Prepared by:** Head of Product (with Engineering Leadership)  
**Decision needed:** Scope of Q1 rebrand vs. customer-retention fixes before Q1 commitments are locked

---

## Recommendation

Adopt **Option A (Scoped Q1 Rebrand + Top-3 Retention Fixes)**. Ship the customer-facing rebrand in Q1—new name in the app, new domain, and new marketing site—while deferring the full design-system rebuild to Q2–Q3. Dedicate the freed product and engineering capacity to fixing the three issues driving our 24-point NPS drop (from **+28 to +4**): slow invoicing, the broken accounting integration, and missing reports.

---

## Why This Trade-off Matters Now

After last year's merger, presenting one unified brand to prospects, customers, and the board is urgent. At the same time, core product reliability is eroding retention:

- **NPS:** Fell from **+28 to +4** (-24 points).
- **Top unresolved customer complaints (open for months):** slow invoicing, broken accounting integration, missing reports.
- **Commercial exposure *(pull from CRM, Support, and Billing before the meeting)*:**
  - Q1–Q2 ARR up for renewal from accounts citing these three issues: `[€/$ X]`
  - Churned or downgraded ARR in the last two quarters citing these issues: `[€/$ Y]`
  - Monthly support tickets / engineering escalations tied to these issues: `[Z tickets/month]`

If product and engineering spend 100% of Q1 on the rebrand, those three issues remain unaddressed until at least Q2, and we take that renewal risk knowingly.

---

## Real Q1 Capacity

Before committing dates, engineering leads should confirm net roadmap capacity using last quarter's actuals (no overtime, no skipped QA/security):

| Capacity bucket | Share of Q1 *(confirm with Eng leads)* | Notes |
|---|---:|---|
| Planned leave, holidays, onboarding | `[~15%]` | Known calendar time |
| On-call, incidents, unplanned support | `[~20%]` | Based on last 90 days of Jira/incident logs |
| **Net available roadmap capacity** | **`[~65%]`** | **100% of what we can reliably commit** |

Within net roadmap capacity, the **new design system** is the largest engineering load—typically a multi-quarter platform migration—whereas updating the app name, domain, and marketing site is a bounded Q1 scope.

---

## Q1 Options

| Dimension | Option A: Scoped Rebrand + Core Fixes *(Recommended)* | Option B: Full Rebrand + Design System in Q1 |
|---|---|---|
| **Brand outcome in Q1** | New name in app, new domain, new marketing site live in Q1. Design system phased in Q2–Q3. | All four items (name, domain, site, full design system) attempted in Q1. |
| **Customer & revenue impact** | Stops bleeding on slow invoicing, accounting integration, and top missing reports; gives CS/Sales concrete dates for at-risk renewals. | Zero fixes on top three complaints until Q2+; high risk of further NPS decline and Q1–Q2 churn. |
| **Capacity & quality** | Fits real capacity (~50–60% scoped rebrand, ~40–50% core fixes) with engineering-estimated dates. | High risk of overrunning Q1 or forcing overtime/cut testing, increasing incidents and attrition. |
| **Reversibility** | High—design-system rollout can accelerate in Q2 once retention stabilises. | Low—lost customers and post-merger brand launch paired with broken core workflows are hard to recover. |
| **Explicitly not in Q1** | Full component-library / design-system migration (starts Q2). | Invoicing performance, accounting integration repair, missing reports. |

---

## Q1 Indicators and Review Rhythm

If we choose Option A, we track three sets of outcomes and review them at week 6 (mid-quarter) and end of Q1:

1. **Brand delivery:** New domain, marketing site, and in-app name live by target date, with zero critical launch regressions.
2. **Customer recovery:** Measurable reduction in invoicing latency (`[target ms/s]`), accounting integration sync error rate (`[target <X%]`), top missing reports shipped, ticket volume down, and NPS trend reversing.
3. **Team & system health:** Planned-to-done reliability, incident rate, and no sustained overtime.

---

## Key Assumptions and Open Questions

- **Assumptions:** There is no legal or contractual requirement to complete the full design-system rebuild (as distinct from the name and domain) in Q1; engineering leads confirm the scoped rebrand leaves enough capacity to resolve all three customer issues or the highest-impact slice of each.
- **What would change this recommendation:** A hard legal/commercial deadline requiring full visual-system parity in Q1, or CRM data showing that the three complaints represent negligible renewal risk.
- **Open question for leadership:** *What am I missing, and what would make this wrong?*
