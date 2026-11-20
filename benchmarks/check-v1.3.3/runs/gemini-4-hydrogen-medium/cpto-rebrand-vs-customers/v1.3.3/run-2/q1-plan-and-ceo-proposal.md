# Q1 Plan & Executive Proposal: Stabilise Retention While Delivering the Rebrand Core

## 1. The Situation & Real Problem
After last year's merger, leadership wants one name and one story in the market. That makes sense. The risk is spending 100% of Q1 product and engineering capacity on a full rebrand (in-app name, new design system, new domain, new marketing site) while:
- **NPS has dropped 24 points**, from **+28 to +4**.
- **Three core customer workflows**—slow invoicing, a broken accounting integration, and missing reports—have been broken or missing for months.

A new name and design system will not retain an unhappy customer whose invoicing is slow or whose accounting integration is broken. Falling satisfaction today becomes churn and lower net revenue retention in Q2 and Q3.

At the same time, the CEO's instinct for speed ("any decision beats no decision") is right for reversible choices, but locking the entire engineering organisation into a full design system rewrite for a quarter is expensive to unwind if renewals slip.

---

## 2. The Proposal: Split the Rebrand and Fix the Top 3 Customer Pains in Q1

Instead of an all-or-nothing Q1, separate **what must ship for one-brand clarity** from **what can be phased or handled outside core product engineering**:

| Workstream | In Q1 (Committed Core) | Deferred / Phased (Q2+) or Decoupled |
|---|---|---|
| **Rebrand** | New product name & copy in app, domain migration & redirects, legal/billing/email sender strings | Full new design system rollout across all screens; marketing site built by marketing/web (or agency) without blocking product engineers |
| **Customer Retention** | 1. Fix slow invoicing latency<br>2. Repair the broken accounting integration<br>3. Ship the top missing reports | Secondary UI polish and non-critical feature requests |
| **Platform & Unplanned Work** | Explicit buffer for post-merger incidents, on-call, and tech debt | — |

### Why this works for both sides
- **For the CEO & Sales:** You still go to market under the new name, domain, and marketing site in Q1. Prospects see one company.
- **For Customers & Retention:** Existing customers see their top three pain points fixed in Q1, stopping the NPS slide from +28 to +4 before it hits renewals.
- **For Engineering:** Teams work on clear outcomes without a forced 100% design-system rewrite, and without burning out on hidden unplanned work.

---

## 3. How to Plan Q1 Capacity (Before Committing Dates)

Do not commit Q1 delivery dates until the engineering leads and teams have sized the work against **real available capacity**:

1. **Calculate net capacity per team:** Headcount minus planned leave, holidays, onboarding, on-call/support rotation, and recent unplanned incident load (check the last 8–12 weeks in Jira/incident logs).
2. **Reserve slack:** Never plan teams to 100%. Leave room for post-merger integration surprises and reliability.
3. **Ring-fence the rebrand core:** Have a small, dedicated group estimate the minimum viable rebrand (in-app strings, domain/redirects, billing/legal entities). Keep the marketing site out of product engineering's critical path.
4. **Assign the 3 customer fixes to dedicated outcome teams:** Each fix gets one clear owner, a target metric, and an engineering-validated estimate before Q1 starts.

### Draft Q1 Outcomes & Measures (Fill in targets with Engineering & Support)

| Outcome | Owner | Success Measure | Target / Review Date |
|---|---|---|---|
| **1. Customers can invoice without delay** | *[Product + Eng Lead]* | p95 invoicing page/job latency; support tickets for slow invoicing | *[e.g., < 2s p95; -70% tickets by Week 8]* |
| **2. Accounting integration syncs reliably** | *[Product + Eng Lead]* | Sync success rate; failed-sync support volume | *[e.g., > 99.5% success by Week 6]* |
| **3. Top missing reports are live** | *[Product + Eng Lead]* | Usage of top *[N]* requested reports; closed-loop NPS feedback | *[Shipped by Week 10]* |
| **4. One brand in market & app** | *[Marketing + Rebrand Pod]* | New domain live with redirects; in-app name/legal strings updated; new marketing site live | *[End of Q1]* |

*Everything not on this list waits until Q2, with an explicit review date.*

---

## 4. How to Raise This With the CEO (Private First)

Go to the CEO **one-on-one before any wider leadership or all-hands meeting**. Do not challenge the authority to decide; bring the customer evidence and a way to achieve the CEO's goal faster and with less risk.

### Talking Points / Draft Note
> "I'm fully behind getting us to one brand in Q1. Looking at our numbers, NPS has dropped from +28 to +4, and slow invoicing, the broken accounting integration, and missing reports have been open for months. If we put 100% of product and engineering on a full design system and rebrand for Q1, we risk losing renewals before the new brand lands.
>
> We can still launch the new name, domain, and marketing site in Q1 if we separate the must-have brand cutover from a full design-system rewrite, and put dedicated teams on those three customer fixes at the same time. Before we lock Q1, I'd like 48 hours with engineering to size both options so you can see the exact trade-offs."

### Questions to Ask If Pushback Continues
- *"Which renewal or revenue risk are we willing to accept if invoicing and the accounting integration stay broken until Q2?"*
- *"Can we decouple the marketing site and full design system from the Q1 name-and-domain cutover?"*
- *"What would need to be true in the data for us to allocate capacity to the top three customer fixes this quarter?"*

---

## 5. Operating Rhythm & Review

- **Bi-weekly check-in:** Review delivery against the 4 outcomes, support ticket volume on the 3 complaints, and post-fix NPS trend.
- **No-surprises rule with teams:** Share the problem (NPS +28 to +4, merger brand deadline) and the draft split with product managers and tech leads so they can validate estimates and flag dependencies before anything is announced.
- **What would change this plan:** If engineering's sizing shows the minimal rebrand core takes >50% of Q1 capacity, or if churn data shows another issue is driving the NPS drop more than these three complaints.
