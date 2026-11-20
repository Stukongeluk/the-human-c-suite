# Q1 Plan Proposal: Rebrand Delivery & Customer Retention

**Purpose:** Align on Q1 capacity allocation so we ship the post-merger rebrand on time without compounding churn from unresolved core product issues.

---

## 1. Context & What Is at Stake

Following last year's merger, unifying the company under one name, domain, and marketing site is necessary for market clarity and sales alignment. Moving decisively matters.

At the same time, our customer health data shows an acute retention risk:
- **NPS dropped 24 points**, from **+28 to +4**.
- **Three core workflow complaints** have remained open for months:
  1. Slow invoicing
  2. Broken accounting integration
  3. Missing reports
- **[Fill in before sharing]:** `[X]` support tickets/month, `[Y]` accounts at renewal risk (`$Z` ARR) citing these three issues.

If 100% of product and engineering capacity goes to the rebrand for all of Q1, those three issues will remain unresolved for another 13 weeks—and we will launch a new brand on top of a deteriorating customer experience.

---

## 2. Where Engineering Capacity Actually Goes

Before allocating Q1, we have to count non-discretionary load so commitments match real throughput:

| Capacity Bucket | Share of Q1 | Notes |
|---|---:|---|
| Unplanned work, incidents & on-call | 20% | Support escalations, production reliability |
| Discretionary product & engineering | 80% | Available for Q1 initiatives |
| **Total** | **100%** | |

*(Adjust the 20% baseline to match last quarter's actual incident and support load.)*

---

## 3. Q1 Options

### Option A: 100% Discretionary Capacity on Rebrand (Current Plan)
- **Allocation:** 80% Rebrand (in-app name, full design system, domain, marketing site), 0% Customer Blockers.
- **Outcome:** Full design system overhaul alongside brand launch.
- **Risk:** Zero progress on invoicing, accounting integration, and reporting for another quarter; high risk of continued NPS decline and preventable churn.

### Option B: Scoped Rebrand + Core Customer Fixes (Recommended)
- **Allocation:** 45% Rebrand, 35% Top 3 Customer Blockers (80% discretionary total).
- **How it fits:** Scope Q1 rebrand to what customers and prospects actually see on launch day—new name in app, new domain, new marketing site, and brand tokens/styling—while deferring non-visible design-system refactoring to Q2.
- **Outcome:** We hit the Q1 rebrand launch date *and* ship fixes for slow invoicing, the broken accounting integration, and the highest-impact missing reports.
- **Trade-off:** Internal component library cleanup waits until Q2.

### Option C: Phased Rebrand (External First, In-App Q2)
- **Allocation:** 25% Rebrand (domain + marketing site), 55% Customer Blockers & Reliability.
- **Outcome:** Fastest recovery on NPS and retention; in-app rebrand moves to Q2.
- **Trade-off:** Temporary mismatch between marketing site name and in-app name.

---

## 4. Recommended Q1 Commitments (Option B)

| Initiative | Owner | Target Outcome | How We Measure It |
|---|---|---|---|
| **Rebrand Launch** | `[Lead]` | New name in app, new domain, new marketing site live | Launch date met; zero P1 regressions on domain cutover |
| **Invoicing Performance** | `[Lead]` | Cut invoicing latency to target SLA | P95 invoice generation time; support ticket drop |
| **Accounting Integration** | `[Lead]` | Restore reliable sync for affected customers | Sync failure rate; affected accounts unblocked |
| **Missing Reports** | `[Lead]` | Ship top `[N]` requested reports | Report adoption; reduction in churn-risk flags |

**What is explicitly out of Q1:** Full internal design-system rewrite (scheduled for Q2), and new feature requests outside the four items above.

---

## 5. Decision & Review Rhythm

- **Decision needed:** Confirm Option B (or choose Option A/C with explicit acceptance of the trade-offs above).
- **Review cadence:** Bi-weekly check-in on rebrand launch readiness, P95 invoicing/sync metrics, and team capacity/incident load.
- **What would change this plan:** A major P1 incident or a scope increase on the rebrand—at which point we re-balance explicitly rather than absorbing it through overtime or skipped testing.
