# Recommendation: AI Workforce Management & Store Scheduling

**To:** Executive Committee (CEO, COO, CFO, CHRO)  
**From:** CTO  
**Date:** November 2026  
**Status:** For decision (before vendor contract commitment)

---

## Executive Summary

**Recommendation: Do not sign for a March 2027 all-store rollout. Instead, run a 12-week controlled pilot in 6–8 voluntary stores focused on demand forecasting and CAO-compliant scheduling, co-designed with our Works Council (OR) and measured against a matched control group.**

The COO's underlying goal—matching store labour hours more closely to customer demand across 140 stores—is right. In grocery retail, small improvements in labour fit matter. However, the vendor's headline promise of **12% fewer labour hours** relies on three practices (three-day schedule publication, same-day shift adjustments, and 15-minute micro-slots) that conflict with Dutch labour law, our collective agreement, and store-floor reality. Going live across 140 stores and ~9,000 staff in roughly 14 weeks also creates unacceptable payroll, compliance, and attrition risk.

---

## 1. Why the Vendor's March Plan Will Not Deliver the Promised 12%

### Legal and Works Council blockers (verify with HR and employment counsel)
*Note: The following is operational risk identification, not legal advice; HR and external employment counsel should confirm the exact clauses in our applicable CAO.*

- **Same-day shift changes do not save labour cost.** Under Dutch law (*Wet arbeidsmarkt in balans*, Art. 7:628a BW), on-call workers (*oproepkrachten*) require at least **4 days' (96 hours')** notice; cancelling or altering a shift inside that window still obligates us to pay the originally scheduled hours. Even where the Dutch supermarket collective agreement (*CAO Levensmiddelenbedrijf / VGL*) allows a shortened **24-hour** notice for *hulpkrachten/erbijbaners* in unforeseen circumstances, same-day cuts remain payable and cannot be enforced unilaterally.
- **Three-day schedule publication conflicts with CAO rules.** Under the *CAO Levensmiddelenbedrijf* (checked November 2026), full schedules must be published at least **one full week (7 days)** in advance (and rostered days off two weeks ahead). Publishing three days ahead breaches the CAO for regular staff and falls short of the 4-day statutory minimum for on-call staff outside the *erbijbaner* exception.
- **15-minute slot slicing hits minimum pay floors.** Flexible contracts without fixed hours or under 15 hours/week carry a **3-hour minimum pay per call-up** (Art. 7:628a BW), plus statutory break and youth-work rules under the *Arbeidstijdenwet*.
- **Mandatory Works Council consent (*instemmingsrecht*).** With ~9,000 staff, our OR has a statutory consent right over working-hour and scheduling arrangements (**Art. 27(1)(b) WOR**) and over any system suited to monitoring employee attendance, behaviour, or performance (**Art. 27(1)(l) WOR**). Proceeding without OR consent allows the OR to invoke nullity. A proper consent process typically requires 6–12 weeks, which alone makes a March all-store launch unrealistic.
- **GDPR and EU AI Act readiness.** Automated scheduling affecting hours and income requires a Data Protection Impact Assessment (DPIA) and clear human oversight under **GDPR (AVG) Art. 22**. Under the **EU AI Act (Annex III)**, AI used for task allocation or worker evaluation is classified as high-risk; the employer obligation to inform workers' representatives and affected staff before deployment (Art. 26(7)) takes effect on **2 December 2027** (as amended by the 2026 Digital Omnibus). While not yet in force, any platform we buy now must be audit-ready well before that date.

### Operational and technical risks
- **Hidden attrition cost.** A large share of our ~9,000 staff are students who choose employers that let them plan around lectures, exams, and sports. Three-day notice and same-day shift changes will increase turnover and no-shows in an already tight Dutch retail labour market—replacing the labour savings with recruiting, onboarding, and store-manager overhead.
- **Store-floor reality.** A 15-minute demand curve ignores shelf-replenishment waves, late truck deliveries, cash-office duties, and shift handovers. If store managers have to override the system daily to keep stores running, adoption collapses.
- **14-week integration risk across 140 stores.** Connecting a new WFM engine to POS, HRIS, time-and-attendance, and Dutch payroll rules (youth wage scales, evening/Sunday allowances, student hour caps) by March leaves no margin for parallel payroll runs. One broken payroll cycle for 9,000 staff is an immediate trust and operational crisis.

---

## 2. Options Evaluated

Criteria should be agreed by ExCo before scoring any vendor: **(1) verified net labour-cost impact after turnover, (2) legal/CAO/OR compliance, (3) store-manager usability and staff retention, (4) payroll and integration risk, and (5) 3-year total cost of ownership including exit.**

| Option | Scope & Timeline | Realistic Labour Impact (Est.) | Compliance & People Risk | Technical & Payroll Risk | Reversibility |
|---|---|---|---|---|---|
| **A. Optimise current WFM + forecasting** | Audit current tool, fix POS data feeds & scheduling hygiene (8–12 weeks) | Low–Moderate (2–4%, unverified until audited) | Low (stays within existing CAO & OR agreements) | Low (no payroll cutover) | High |
| **B. Controlled 12-week pilot (Recommended)** | 6–8 voluntary stores; AI demand forecasting + CAO-compliant scheduling (≥2 weeks notice, no same-day forced cuts, manager sign-off); OR involved from day 1 | Moderate (3–6% realistic once illegal cuts are stripped out; measured in pilot) | Low–Moderate (co-designed with OR; protects schedule predictability) | Low (isolated from 140-store payroll cutover) | High (exit after 12 weeks if targets missed) |
| **C. Vendor's March big-bang** | All 140 stores live by March 2027 with 3-day notice & same-day adjustments | Vendor claims 12%; net impact likely negative once cancelled-shift pay & turnover are counted | Critical (CAO/WAB breaches, OR nullity risk, student attrition spike) | Critical (no time for parallel payroll runs across 140 stores) | Low (multi-year lock-in, high switching cost) |

---

## 3. Recommended Plan (12-Week Pilot, Wave-Based Scaling)

### Phase 0: Baseline & Alignment (Weeks 1–3, Nov–Dec 2026)
1. **Pull internal evidence first** (before any vendor commitment):
   - 12-month store-level variance: scheduled vs. worked vs. forecast hours across all 140 stores.
   - Current WFM utilisation, licence terms, and whether unused forecasting features already exist.
   - Store turnover, absenteeism, and open-shift fill rates by contract type (*erbijbaners* vs. fixed).
2. **Bring the OR in at the problem stage** with the real numbers—not a signed contract—to co-design pilot guardrails.
3. **Require legal & security sign-off** from HR/employment counsel (CAO/WAB compliance) and DPO (DPIA, GDPR Art. 22, no individual worker scoring or ranking).

### Phase 1: Controlled Pilot (Weeks 4–15, Q1 2027)
- **Scope:** 6–8 voluntary stores (mix of urban student-heavy and suburban family stores) plus 6–8 matched control stores.
- **Hard guardrails:**
  - Schedules published **at least 14 days ahead** (or current CAO/store standard, never 3 days).
  - **No forced same-day shift cuts**; optional voluntary shift-swap / extra-hours marketplace only.
  - **Store managers retain final sign-off** on schedules; no automated disciplinary or individual performance rankings.
  - **Parallel payroll validation** before any live payroll feed.
- **Commercial terms:** Short, capped pilot fee with zero multi-year commitment and clear data-export clauses.

### Phase 2: Go / No-Go Review (Week 16, April 2027)
Scale in waves (e.g. 20 → 50 → 140 stores) **only** if the pilot beats the control group on all agreed indicators:
- **Cost:** Net labour hours per €1,000 turnover (including paid cancelled hours and overtime).
- **Operations:** On-shelf availability, checkout wait times, and store-manager hours spent on scheduling.
- **People:** Student and staff retention, absenteeism, shift-swap fill rate, and a short store-team pulse check.
- **Reliability:** Zero payroll discrepancies in parallel runs.

---

## 4. Key Assumptions & What Would Change This Recommendation

**Assumptions (to verify in Phase 0):**
- Our stores fall under the *CAO Levensmiddelenbedrijf* (or VGL equivalent) and have an active Works Council.
- Our current WFM/payroll stack is not already pre-integrated with this vendor.
- The March deadline is vendor-driven rather than tied to an expiring legacy contract.

**What would change this recommendation:**
- If our existing WFM contract terminates in March with no extension option (requiring a continuity plan, not a rushed AI feature rollout).
- If internal data shows our current WFM already has unused forecasting capability that can deliver 3–5% improvement without buying a new platform (in which case Option A beats Option B).
- If the vendor can demonstrate, with independent Dutch supermarket references, compliant net savings without 3-day publishing or same-day cuts—which would strengthen the case for Option B, still via a pilot rather than a big bang.

---

## Sources
- Dutch Civil Code (*Burgerlijk Wetboek*), Art. 7:628a (WAB: 4-day call-up/cancellation notice and 3-hour minimum pay per call-up) — [wetten.overheid.nl](https://wetten.overheid.nl)
- *CAO voor het Levensmiddelenbedrijf* (2024–2026): schedule publication (7 days), rostered days off (14 days), and 24-hour unforeseen call-up rule for *hulpkrachten/erbijbaners* — [vakcentrum.nl](https://www.vakcentrum.nl) / [officielebekendmakingen.nl](https://www.officielebekendmakingen.nl)
- Dutch Works Councils Act (*Wet op de ondernemingsraden*, WOR), Art. 27(1)(b) and Art. 27(1)(l) — [wetten.overheid.nl](https://wetten.overheid.nl)
- EU AI Act (Regulation (EU) 2024/1689), Annex III & Art. 26(7), and 2026 Digital Omnibus timeline (2 December 2027 for high-risk workplace notification) — [European Commission AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26)
- OECD Employment Outlook 2023: AI adoption and worker consultation — [OECD](https://read.oecd.org/10.1787/08785bba-en)
