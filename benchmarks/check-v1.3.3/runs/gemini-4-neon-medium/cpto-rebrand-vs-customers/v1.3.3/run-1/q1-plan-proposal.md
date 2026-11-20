# Decision Memo: Q1 Product & Engineering Plan — Phased Rebrand and Customer Retention

**Decision needed by:** Before Q1 kickoff · **Decision owner:** CEO & Leadership Team · **Prepared by:** Head of Product

## The problem in one sentence

Customer satisfaction has dropped 24 points (NPS from +28 to +4) while three core customer problems—slow invoicing, a broken accounting integration, and missing reports—remain unresolved; dedicating 100% of Q1 product and engineering capacity to a full rebrand pushes those fixes to Q2 and compounds renewal risk.

## What the data says

| Signal | Current value | Source & date |
|---|---|---|
| Net Promoter Score (NPS) | +4 (down from +28; −24 pts) | Customer survey, current |
| Top open customer complaints | Slow invoicing, broken accounting integration, missing reports (open for months) | Support & CS feedback |
| ARR at risk / Q1–Q2 renewals citing these issues | `[Pull from CRM: accounts & ARR]` | CRM |
| Support ticket volume from these 3 issues | `[Pull from support tool: % of monthly tickets]` | Support system |
| Engineering capacity required for full design system vs. must-have rebrand | `[Validate with Engineering Leads before locking dates]` | Engineering sizing |

## Options considered

### Option A: Full rebrand in Q1 (current plan)
- **Scope:** New name in the app, new domain and redirects, new marketing site, and a full new design system.
- **Customer & revenue impact:** Unified brand in market in Q1, but slow invoicing, broken accounting, and missing reports wait until Q2 at the earliest. A new name does not resolve active customer pain; falling NPS typically surfaces as churn one to two quarters later.
- **Capacity & quality:** Absorbs 100% of product and engineering roadmap capacity. A big-bang design system rewrite carries high regression risk and crowds out reliability work.
- **Reversibility:** Hard to recover churned accounts once customers switch.

### Option B: Phased rebrand + top 3 customer fixes in Q1 (Recommended)
- **Scope:**
  1. **Must-have rebrand in Q1:** New brand name, logo, legal/billing strings in the app, new domain and redirects, and the new marketing site (led by marketing/web, with minimal product engineering dependencies).
  2. **Customer retention fixes in Q1:** Fix slow invoicing, repair the accounting integration, and deliver the highest-demand missing reports.
  3. **Design system phased into Q2+:** Define core tokens and components in Q1, then roll out incrementally as teams touch screens—avoiding a full-quarter freeze on customer value.
- **Customer & revenue impact:** Delivers one unified brand name and web presence in Q1 while directly addressing the three drivers of the 24-point NPS drop.
- **Capacity & quality:** Fits real engineering capacity without overtime or skipped QA. Keeps teams focused on measurable customer outcomes.
- **Reversibility:** High. If market data shows the full design system is blocking enterprise deals, we can accelerate it in Q2.

### Option C: Customer fixes only; defer all rebrand work to Q2
- **Scope:** 100% of roadmap capacity on the three customer problems and post-merger reliability.
- **Customer & revenue impact:** Fastest relief for existing customers, but leaves post-merger brand confusion active in sales and marketing for another quarter.

## Proposed Q1 capacity allocation

Capacity starts from real availability (excluding planned leave, onboarding, and holidays) and reserves baseline operational capacity first—based on last quarter's actuals for unplanned work, incidents, on-call/support, and essential tech debt (typically 30–40% of total engineering time; to be confirmed from Jira and incident logs).

The remaining **roadmap capacity** (100% of net roadmap hours) is split as follows:

| Workstream | Share of roadmap capacity | Target outcome |
|---|---|---|
| Top 3 customer retention fixes | 65% | Resolve slow invoicing, restore accounting sync reliability, ship core missing reports |
| Must-have rebrand (name, domain, redirects, marketing handoff) | 25% | Launch unified brand name and domain cleanly in Q1 |
| Q2 design system foundations & discovery | 10% | Establish tokens and incremental migration plan without halting product delivery |
| **Total roadmap capacity** | **100%** | |

*Firm delivery dates will be set only after the building teams estimate the scoped work. We will not close capacity gaps with overtime or reduced testing.*

## Q1–Q2 outcome roadmap

| Horizon | Outcome | Customer / business evidence | Key bets | Confidence | How we'll know it worked |
|---|---|---|---|---|---|
| **Now (Q1)** | Stop the NPS slide and protect Q1–Q2 renewals | NPS +28 → +4; months-old complaints on core workflows | Invoicing performance fix; accounting integration repair; top missing reports | High (once sized) | Support tickets on these 3 areas cut by >50%; invoicing p95 latency target met; NPS stabilising |
| **Now (Q1)** | Present one unified brand post-merger | Post-merger sales & market clarity | In-app name/logo/strings update; domain migration + redirects; marketing site launch | High | Zero broken redirects or auth regressions; unified brand live by end of Q1 |
| **Next (Q2)** | Cohesive UI across merged products | Post-merger visual inconsistency | Incremental design system rollout tied to active product areas | Medium | New/updated flows ship on shared components without freezing feature delivery |
| **Health (Ongoing)** | Sustainable delivery and reliability | Post-merger system complexity | Baseline incident/debt allocation protected in every sprint | High | Unplanned work share stable or falling; zero planned overtime |

**Explicitly not in Q1:** A full, big-bang design system rewrite across all legacy screens.
**What sales and CS can promise:** Unified brand name and domain in Q1, plus concrete delivery windows (once engineering estimates) for invoicing, accounting, and reporting fixes.

## How we'll measure Q1

We will review three sets of indicators monthly at the leadership level:
1. **Customer:** NPS trend, monthly support volume for the three workflows, invoicing speed, accounting sync error rate, and Q1–Q2 renewal/churn rate.
2. **Delivery:** Rebrand cutover milestones met without major incidents, deployment stability, and share of unplanned work.
3. **Team health:** Sustainable hours (no planned overtime) and a short team pulse on clarity of priorities.

## Assumptions, and what would change this recommendation

- **Assumptions:** (1) The marketing site can be built primarily by marketing/web resources without pulling core product engineers; (2) there is no legal or contractual requirement to replace the entire UI component library in Q1; (3) the three open complaints are major contributors to the 24-point NPS drop.
- **What would change my mind:** A hard legal/regulatory deadline requiring a full UI rebuild in Q1, or CRM evidence showing that ARR at risk from the three product gaps is minor compared to net-new pipeline blocked specifically by the old UI.

## Questions for leadership

What are we missing, and what would make Option B the wrong call?
