# Q1 Product & Engineering Plan: Rebrand and Customer Retention

**Prepared for:** CEO & Executive Team  
**Date:** [Date]  
**Status:** Proposed options for Q1 lock  

## 1. The problem we are solving

One year after the merger, we need one brand in the market so customers, prospects and investors see one company. At the same time, core product reliability is slipping:

- **NPS fell 24 points**, from **+28 to +4**.
- **Three core workflow issues** have remained open for months: slow invoicing, a broken accounting integration and missing reports.
- **Revenue and support load:** `[X]` open support tickets in the last 90 days and `[€Y ARR / Z accounts]` flagged at renewal risk are tied directly to these three issues.

A new name and design system will not retain an account that cannot invoice or close its books. Spending 100% of Q1 product and engineering capacity on the rebrand leaves these three issues unresolved for another quarter, turning a drop in satisfaction into churn that shows up in Q2–Q3 renewals.

## 2. Real Q1 capacity

Before committing scope, Engineering and Product sized net Q1 capacity across the organisation:

| Capacity bucket | Share of total hours | Notes |
|---|---:|---|
| Planned leave, holidays, onboarding | `[15%]` | Known Q1 absences and ramp |
| On-call, incidents, support escalations | `[15%]` | Based on last 2 quarters' actuals |
| Mandatory maintenance, security & reliability | `[10%]` | Keeping production stable |
| **Net capacity available for Q1 roadmap** | **`[60%]`** | **100% of roadmap capacity below** |
| **Total** | **100%** | |



We will not close a scope gap with overtime or by skipping testing—that creates incidents and slows Q2 down further.

## 3. Options for Q1

| Dimension | Option A: Full rebrand in Q1 | Option B: Must-have rebrand + top 3 customer fixes (Recommended) |
|---|---|---|
| **Net roadmap capacity split** | 100% Rebrand (in-app name, full design system, domain, marketing site); 0% Customer fixes | 30% Must-have rebrand; 60% Top 3 customer fixes; 10% Buffer for unplanned escalation/discovery |
| **Brand outcome in Q1** | Complete visual overhaul and new design system live in Q1 | One unified brand live in Q1: new name & logo in-app, new domain + redirects, legal/billing entities updated, new marketing site (led by Marketing/agency) |
| **Design system** | Built and rolled out in Q1 | Scoped in Q1, rolled out incrementally in Q2 alongside product work |
| **Customer & revenue impact** | Slow invoicing, accounting integration and missing reports wait until Q2+; high risk of further NPS drop and Q2–Q3 churn | Top 3 customer complaints resolved in Q1; measurable recovery in support volume, renewal confidence and NPS |
| **Delivery & team risk** | High: big-bang design system migration touches every surface at once; engineers carry mounting customer escalations alongside rebrand | Low to moderate: small, reversible rebrand slice ships cleanly; teams work on clear customer outcomes |
| **Reversibility** | Low: three months of churn and delayed fixes cannot be undone | High: design system polish is easy to sequence into Q2 once core workflows work |

## 4. What ships in Q1 under Option B (and what waits)

**In Q1:**
1. **Must-have rebrand (30% of net roadmap capacity):** In-app name, logo and email/invoice branding updates; domain migration with redirects; legal/billing entity alignment. Marketing leads the new marketing site with external/agency support so product engineering stays focused on the app.
2. **Core customer fixes (60% of net roadmap capacity):**
   - **Slow invoicing:** Bring invoice generation latency under `[target, e.g. 2s p95]`.
   - **Broken accounting integration:** Restore reliable sync with `<[target]%` error rate and clear retry/error visibility.
   - **Missing reports:** Ship the `[top 3–5]` reports most cited in support and renewal calls.
3. **Operational buffer (10% of net roadmap capacity):** Reserved for merger-related edge cases and urgent customer escalations.

**Explicitly deferred to Q2 (with review date):**
- Full new design system rollout across all existing screens (begins Q2, applied screen-by-screen rather than as a freeze).
- Secondary rebrand cosmetics that do not block one unified market presence.

## 5. How we will know it is working

We will review progress at **Week 6** (mid-quarter gate) against four measures:

1. **Brand launch readiness:** New domain, in-app name, billing/legal text and marketing site on track for Q1 launch date.
2. **Customer health:** Weekly ticket volume on invoicing, accounting integration and reporting down by `[target, e.g. 50%]`; NPS trending back toward `+20` by end of Q2.
3. **Renewal protection:** Zero churn attributed to the three resolved issues in Q2 renewals.
4. **Delivery health:** Planned work completed without sustained overtime or rising incident counts.

## 6. Questions to align on

1. Is there a legal, contractual or board deadline that requires the full design system—not just the name, domain and marketing site—to be live in Q1?
2. Can Marketing own the new marketing site with agency support so Product & Engineering focus on the in-app rebrand and the three customer fixes?
3. What evidence at Week 6 would cause us to adjust the 30/60/10 split?
