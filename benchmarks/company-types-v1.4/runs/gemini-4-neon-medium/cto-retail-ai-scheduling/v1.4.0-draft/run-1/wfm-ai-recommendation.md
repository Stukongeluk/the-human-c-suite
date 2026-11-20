# Recommendation: AI Workforce-Management Proposal (140 Stores)

**Date:** 20 November 2026  
**To:** Executive Team (COO, CEO, CFO, CHRO)  
**From:** CTO  
**Status:** Draft for alignment with COO, HR, Legal, and Works Council (OR)

---

## 1. Executive Recommendation

**Do not approve a March all-store rollout or the vendor's 15-minute / three-day / same-day shift-adjustment model.**

Instead, **run a controlled 8–12 week pilot in 6–10 stores starting in March 2027** (after the December trading peak and after Works Council consultation), using demand forecasting to improve advance roster planning while **keeping predictable schedules (at least 14 days' notice, or the applicable CAO floor if stricter) and store-manager decision authority**.

Two realities drive this recommendation:
1. **The vendor's 12% labour-hour claim is untested on our data and conflicts with retail evidence.** In a randomised trial across 28 stores, more predictable schedules—not shorter notice—raised median sales by **7%** and labour productivity by **5%** (Williams, Lambert, Kesavan et al., 2018).
2. **The proposed mechanics and March timeline carry high legal and operational risk.** Rolling out a workforce-monitoring and scheduling system across 140 stores and ~9,000 staff in 3.5 months across Sinterklaas and Christmas leaves no realistic path for Dutch Works Council consent, CAO/statutory compliance, or safe POS/payroll integration.

---

## 2. The Problem Worth Solving

The COO's underlying goal is sound: labour is our largest controllable cost, grocery margins are thin, and better alignment between customer traffic and store staffing can reduce both quiet-hour overstaffing and peak checkout/restocking bottlenecks.

The trap is treating a **people, legal, and store-operations change** as a fast software deployment driven by a vendor's headline savings number. We should separate **better demand forecasting** (high potential value, reversible) from **15-minute micro-rostering and same-day shift cuts** (high legal, churn, and store-availability risk).

---

## 3. Why the Current Proposal Fails Legal, Commercial, and Technical Tests

### A. Dutch Employment Law, Co-Determination, and EU Regulation
*Note: This is an operational risk flag, not legal advice. HR and employment counsel must verify every item against our current Supermarket CAO before any commitment.*

- **Works Council (OR) consent right:** In the Netherlands, a works council is mandatory from 50 employees. Under **Article 27(1)(l) WOR**, the OR has a **consent right (*instemmingsrecht*)** over systems suited to monitoring employee attendance, behaviour, or performance, and under **Article 27(1)(b) WOR** over working-hours and rostering arrangements (alongside advisory rights under **Article 25 WOR** for major operational changes). Deploying without OR consent risks nullification and serious industrial-relations damage.
- **Notice periods and paid cancellations (WAB, in force since 2020):** Under the *Wet arbeidsmarkt in balans*, on-call workers (*oproepkrachten*) must be called at least **four days in advance** or may refuse, and shifts cancelled or altered inside that window **must still be paid**. A collective agreement (CAO) can shorten the statutory four-day window to no less than 24 hours, while fixed/part-time schedules often carry longer CAO notice rules. Even where shorter notice is permitted, **same-day shift cuts** either trigger paid-but-unworked hours (eroding the 12% business case) or breach statutory/CAO rules.
- **Tightening flex-work legislation:** The *Wet meer zekerheid flexwerkers* passed the Dutch Senate on 7 July 2026 (intended to take effect **1 January 2028**; confirm exact date with counsel). It replaces zero-hour contracts with bandwidth contracts (a guaranteed minimum plus at most 30% flexibility), with an exception for pupils' and students' side jobs (*bijbanen*). Building our core scheduling model on extreme short-notice flexibility runs against the direction of Dutch law and will not apply cleanly to non-student flexible staff.
- **EU AI Act and GDPR:** Under **Annex III of the EU AI Act**, AI systems used for task allocation or monitoring/evaluating workers are **high-risk**. The employer obligation to inform workers' representatives and affected workers before deployment (**Article 26(7)**) takes effect on **2 December 2027** (moved from August 2026 by the 2026 Digital Omnibus)—well within this tool's operating life. Under **GDPR**, a Data Protection Impact Assessment (DPIA) and meaningful human oversight of automated decisions affecting staff are required now.

### B. Commercial and Store-Floor Reality
- **Predictability drives store performance:** Evidence from retail operations shows that erratic, short-notice schedules raise absenteeism and turnover, while stable schedules lift both productivity and sales (Williams et al., 2018). High-performing grocers such as Mercadona and Costco keep labour costs competitive through cross-training, simplified store processes, and modest operational slack rather than quarter-hour rationing (Ton, 2014; 2023).
- **Hidden costs that erode the 12% headline:**
  - *Student retention and no-shows:* Students balance lectures, exams, and competing part-time jobs. Three-day notice and same-day cuts drive last-minute dropouts, higher turnover, and constant recruitment/onboarding costs.
  - *Physical store cadence:* Deliveries, cold-chain restocking, shelf replenishment, and checkout waves do not start and stop neatly in 15-minute increments. Removing buffer capacity typically surfaces as empty shelves, longer queues, higher shrink, and lost basket sales.
  - *Net savings vs. gross vendor claims:* Vendor benchmarks rarely net out licence fees, implementation and integration costs, paid cancellations, store-manager override hours, and replacement hiring.

### C. Technical and Rollout Risk (140 Stores by March)
- **Peak trading collision:** Between late November and early January, store managers and IT are focused on Sinterklaas, Christmas, and New Year's trading. Attempting a 140-store rollout across peak invites operational disruption.
- **Data readiness:** AI demand forecasts are only as reliable as the underlying POS, promotional calendar, delivery schedule, weather, and attendance data. Deploying chain-wide before validating forecast accuracy against our own historical store data risks systematic under- or over-staffing across all 140 stores simultaneously.
- **Integration scope:** Connecting POS, HRIS, time-and-attendance, and payroll across 140 stores—with offline fallback and shift-hour support—cannot be safely completed and tested in 14 weeks.

---

## 4. Options Considered

| Option | Description | Expected Impact | Legal & People Risk | Reversibility | Recommendation |
|---|---|---|---|---|---|
| **1. Upgrade existing forecasting inputs** | Improve promo, weather, and local-event inputs inside our current rostering process before buying a new AI tool | Modest, steady labour-fit gains; low licence cost | Low | High | Strong fallback / Phase 0 benchmark |
| **2. Controlled pilot with stable schedules** | Validate forecasting on historical data, then pilot in 6–10 stores (Mar–May 2027) with >=14-day notice, voluntary swap pools, and human manager sign-off | Proven, net-of-cost labour savings measured against sales, availability, and churn | Low–Medium (managed via early OR & HR co-design) | High | **Recommended** |
| **3. Vendor's March all-store rollout** | 140 stores live by March with 15-minute slots, 3-day notice, and same-day adjustments | Unproven 12% gross claim; high risk of churn, stock-outs, and paid cancellations | Very High (OR consent, WAB/CAO, AI Act readiness) | Low | **Do not proceed** |

---

## 5. Proposed Plan (November 2026 – June 2027)

1. **Phase 0 — Baseline & Alignment (Nov–Dec 2026):**
   - Pull read-only, **store-level aggregated** baseline metrics from our systems of record: POS hourly sales/footfall, planned vs. actual worked hours, overtime/agency spend, on-shelf availability, store-level turnover, and sickness absence.
   - Confirm exact CAO notice and rostering rules with HR and employment counsel.
   - Brief the **Works Council (OR)** at the problem stage—before any vendor contract is signed—and invite them to co-design the pilot guardrails. (OECD research finds AI adoption delivers better outcomes for both productivity and job quality when worker representatives are consulted early.)
2. **Phase 1 — Fair Evaluation & Pilot Design (Jan–Feb 2027):**
   - Agree fixed evaluation criteria and weights *before* scoring the vendor (including total cost of ownership, forecast accuracy on our own historical POS data, CAO compliance, data privacy, and store-manager usability). Compare against upgrading our existing tool.
   - Co-design the workflow with 6–10 store managers and frontline staff.
   - Hard guardrails for the pilot:
     - **Forecast to plan, not to cut on the day:** AI recommends staffing envelopes; store managers review and publish rosters.
     - **Predictable notice:** Publish schedules at least 14 days ahead (or CAO minimum if longer). Handle same-day peaks through a **voluntary extra-hours / shift-swap pool**, not unilateral cancellations.
     - **Store-level metrics only:** No individual worker productivity rankings or surveillance dashboards.
3. **Phase 2 — Controlled Pilot (Mar–May 2027, 8–12 weeks):**
   - Run in 6–10 representative stores (urban/suburban mix, varying student share) alongside matched control stores.
   - Audit forecast error, manager override rates, and payroll accuracy weekly.
4. **Phase 3 — Evidence-Based Decision (Jun 2027):**
   - Review balanced scorecard results with the Executive Team, store managers, and the OR.
   - Proceed to phased regional rollout only if net labour savings hold **without** degrading store availability, customer scores, or staff retention, and once formal OR consent is in place.

---

## 6. Balanced Scorecard (Agreed Up Front, Store-Level Only)

| Dimension | Metric (Store-Level Aggregated) | Guardrail / Target |
|---|---|---|
| **Efficiency** | Net labour hours as % of sales (including paid cancellations & tool cost) | Measurable improvement vs. control stores |
| **Forecast quality** | Mean absolute forecast error by hour/department | Validated against baseline before go-live |
| **Commercial** | On-shelf availability, checkout wait / customer score, shrink | No degradation vs. control stores |
| **People** | Store-level turnover, sickness absence, no-show rate | Stable or improved vs. control stores |
| **Schedule health** | % of shifts changed within 14 days; store-manager rostering hours | Reduced last-minute changes & admin load |

---

## 7. Key Assumptions & What Would Change This Recommendation

**Assumptions:**
- Our current POS, HRIS, and payroll systems have not yet been audited for 15-minute forecast accuracy or automated roster integration.
- The OR has not yet been formally consulted on this tool.
- Our Supermarket CAO does not permit unpaid same-day shift cancellations for the bulk of our 9,000 staff.

**What would change this recommendation:**
- If our baseline data shows severe, chronic overstaffing on predictable days that can be solved simply by adjusting shift templates in our current WFM tool (making a new AI vendor unnecessary).
- If HR and counsel confirm our CAO already grants specific, agreed flexibility mechanisms that the OR supports testing in a pilot.
- If the vendor refuses to run a paid/capped pilot measured on net store-level outcomes—in which case we should walk away.

---

## 8. Sources

- Joan C. Williams, Susan J. Lambert, Saravanan Kesavan et al., *Stable Scheduling Increases Productivity and Sales* (Center for WorkLife Law / University of Chicago, 2018).
- Zeynep Ton, *The Good Jobs Strategy* (2014) and *The Case for Good Jobs* (2023).
- OECD, *Employment Outlook 2023* (AI adoption and worker consultation).
- Netherlands: Works Councils Act (*Wet op de ondernemingsraden*, Art. 25 & Art. 27); *Wet arbeidsmarkt in balans* (WAB, 2020); *Wet meer zekerheid flexwerkers* (Eerste Kamer, 36.746, passed 7 July 2026, intended effective date 1 January 2028).
- European Union: AI Act (Regulation (EU) 2024/1689, Annex III & Article 26(7), with high-risk deployer obligations moved to 2 December 2027 under the 2026 Digital Omnibus).
