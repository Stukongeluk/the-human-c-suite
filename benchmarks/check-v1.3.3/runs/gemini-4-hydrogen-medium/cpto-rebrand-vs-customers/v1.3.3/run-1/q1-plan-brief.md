# Q1 Plan & Options Brief: Post-Merger Rebrand vs. Customer Retention

## 1. The Situation
Following last year's merger, leadership wants 100% of product and engineering capacity in Q1 dedicated to the rebrand: a new in-app name, a new design system, a new domain, and a new marketing site.

At the same time, NPS has fallen **24 points (from +28 to +4)**, and three core customer complaints have been open for months:
1. **Slow invoicing**
2. **A broken accounting integration**
3. **Missing reports**

Putting 100% of Q1 into a rebrand means customers wait at least another quarter for fixes to daily financial workflows. A new name and design system will not stop frustrated customers from churning; it risks making them more vocal when the new brand launches onto a broken core experience.

## 2. Separating Must-Have Rebrand Scope from Discretionary Scope
After a merger, presenting one name, one domain, and one story to the market is a legitimate business goal. The question is not *whether* to rebrand, but *how much* of it must happen in Q1:

- **Q1 Must-Have (Minimum Viable Rebrand):** New domain and redirects, new marketing site, and updated brand name/logo/colors in the app shell and customer communications.
- **Q2–Q3 Phased Work:** Full design system rewrite and component-by-component UI migration across every product surface.

## 3. Q1 Capacity Options

| Option | Capacity Split (Roadmap + Buffer) | What Ships in Q1 | Customer & Revenue Impact | Key Risk |
|---|---|---|---|---|
| **A. Current Plan (All-In Rebrand)** | 85% Full Rebrand + Design System / 0% Top Fixes / 15% Support & Incidents | New domain, site, name, and full design system | Invoicing, accounting integration, and reports stay broken; +4 NPS likely drops further | Accelerates churn; teams burn out shipping cosmetic work while knowing customers are hurting |
| **B. Phased Rebrand + Customer Fixes (Recommended)** | 35% Minimum Rebrand / 50% Top 3 Customer Fixes / 15% Support, Incidents & Debt | New domain, site, in-app name/shell **plus** fixes for invoicing, accounting, and key reports | Directly addresses the +4 NPS drivers while still launching the unified brand externally | Design system rollout takes 2 quarters instead of 1 |
| **C. Customer Fixes First** | 10% Rebrand Prep / 75% Top 3 Customer Fixes / 15% Support, Incidents & Debt | Fixes for all three customer complaints; domain/brand prep only | Fastest stabilization of NPS and renewal risk | Delays the post-merger external brand launch to Q2 |

*Note: Exact percentages must be calibrated against each team's actual Q1 capacity (see Section 4) before committing to dates.*

## 4. Building a Realistic Q1 Capacity Model
Before locking Q1 commitments with leadership or sales, calculate real available capacity per team:
1. **Gross headcount** minus planned leave, public holidays, and onboarding time.
2. **Non-roadmap deductions:** historical share of unplanned work, incidents, on-call rotation, and support escalations.
3. **Health & debt:** an explicit allocation for reliability, security, and mentoring—not "if there's time."
4. **Team estimates:** ask the teams doing the work to size the Minimum Rebrand and the three customer fixes using their recent throughput, not top-down target dates.
5. **Slack:** do not plan teams at 100% capacity, and do not close scope gaps with overtime or skipped testing.

## 5. Q1 Success Measures (Reviewed Bi-Weekly)
- **Customer:** Support ticket volume on invoicing, accounting integration, and reporting; NPS recovery from +4; renewal/churn save rate on affected accounts.
- **Delivery:** Unplanned work share, incident rate/recovery time, and on-time milestone delivery for the minimum rebrand.
- **Team Health:** Overtime hours (target: zero sustained overtime) and a short bi-weekly team pulse on clarity and confidence.

## 6. Assumptions & What Would Change This Plan
- **Assumptions:** The +4 NPS drop is driven primarily by the three open complaints rather than brand confusion; the marketing site and domain can be decoupled from a full in-app design system rewrite.
- **What would change this:** A hard contractual/legal deadline requiring full UI component replacement in Q1, or data showing churn is concentrated in non-affected accounts.
- **Review date:** Mid-Q1 (Week 6) checkpoint with CEO, Product, Engineering, and Marketing to review NPS/ticket trends and rebrand progress.
