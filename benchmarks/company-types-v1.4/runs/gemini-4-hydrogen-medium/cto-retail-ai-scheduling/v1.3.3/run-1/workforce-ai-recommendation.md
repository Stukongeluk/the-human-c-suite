# Recommendation: Phased Pilot and Guardrails for AI Workforce Management

**Prepared by:** CTO  
**Date:** 20 November 2026  
**Audience:** COO, Executive Board, HR & Legal  
**Status:** Proposed decision for executive alignment  

---

## Executive Summary

**Recommendation:** Do not commit to a 140-store rollout by March 2027. Instead, run a **6-to-8-week controlled pilot in 6 representative stores** starting in January 2027, decouple the AI demand-forecasting capability from the proposed "3-day notice and same-day shift adjustment" operating model, and involve the Works Council (Ondernemingsraad, OR) before any vendor contract is signed.

The COO's underlying goal—matching store labour more closely to customer traffic to protect thin grocery margins—is sound. However, the vendor's current proposal carries three concrete risks that would erase the projected 12% labour-hour savings:

1. **Legal and payroll exposure (Dutch WAB & CAO):** Under the Dutch Balanced Labour Market Act (*Wet arbeidsmarkt in balans*, WAB), on-call workers generally require at least 4 calendar days' advance notice (unless shortened by the applicable supermarket CAO). Cancelling or shortening shifts within that window—or on the day—typically still obligates us to pay the originally scheduled hours. Same-day cuts create phantom savings on paper while costing real payroll euros.
2. **Works Council and regulatory blockers (WOR & EU AI Act):** A workforce-management tool affecting 9,000 employees falls under the Works Council's statutory right of consent (*instemmingsrecht*, Art. 27(1)(l) WOR) for systems suited to monitoring attendance, behaviour, or performance, as well as advisory rights for major operational changes (Art. 25 WOR). Attempting a full rollout across 140 stores in 14 weeks without prior OR consent risks formal challenge and an immediate halt.
3. **Retention and store-level execution risk:** Much of our store workforce consists of students on flexible contracts who rely on predictable schedules around lectures and exams. Moving to 3-day schedule publication and same-day adjustments in a tight Dutch retail labour market will drive turnover to competitors, increasing recruitment and training costs and overloading store managers.

---

## 1. Why the March 2027 Big-Bang Rollout Fails on Delivery and Cost

| Dimension | Vendor Proposal (All 140 Stores by March) | Recommended Path (6-Store Pilot, Then Waves) |
|---|---|---|
| **Timeline** | ~14 weeks (late Nov 2026 to March 2027) for 140 stores / 9,000 staff | 6–8 weeks pilot (Jan–Feb 2027), Go/No-Go gate in March, waves of 15–20 stores/month if proven |
| **Schedule Notice** | 3 days ahead + same-day adjustments | Keep 2–4 week base rosters; use AI for 15-min demand curves and **voluntary** opt-in shift swaps |
| **Savings Basis** | Vendor-projected 12% reduction in *scheduled* hours | Measured reduction in *actual paid* hours (including idle/cancelled-shift pay and overtime) |
| **Payroll & CAO Risk** | High: 140-store cutover with untested CAO allowances (*toeslagen*) and youth wage rules | Low: parallel shadow-payroll validation in 6 stores before live pay runs |
| **OR & Legal Compliance** | High risk of Art. 27 WOR breach and Enterprise Chamber appeal | Co-designed with the OR from the problem stage; DPIA completed before pilot |

### Technical & Integration Realities
* **15-minute slot granularity vs. store reality:** Checkout traffic fluctuates in 15-minute intervals, but shelf replenishment, fresh/bakery prep, truck unloading, and opening/closing routines have fixed minimum shift lengths and handoff requirements. Naively optimising to 15-minute slots produces unworkable micro-shifts or leaves stores exposed when a delivery is late or one colleague calls in sick.
* **Systems integration:** Reliable scheduling across 140 stores requires clean, bidirectional integration between POS/footfall forecasting, HRIS, time-clocking, and our payroll CAO rule engine. Payroll errors across 9,000 hourly staff damage trust immediately.

---

## 2. Legal and Governance Guardrails (Checked November 2026)

*Note: This section flags statutory frameworks for review with HR and employment counsel; it is not legal advice.*

1. **Dutch Works Councils Act (WOR):**
   * **Art. 27(1)(l) WOR (Consent right):** Mandatory for systems suited to monitoring or checking employee attendance, behaviour, or performance. Workforce analytics and real-time shift-adjustment tools almost always trigger this.
   * **Art. 25 WOR (Advisory right):** Applies to major organisational or technological changes affecting the workforce.
   * **Action:** Bring the OR in now at the problem stage—with the margin data and pilot design—before selecting or committing to a vendor. Research by the OECD (*Employment Outlook 2023*) shows that AI adoption delivers better outcomes when worker representatives are consulted early, preserving productivity gains while protecting job quality.
2. **Dutch Employment Law (WAB) & Supermarket CAO:**
   * Verify with HR/Legal the exact notice-period rules in our applicable supermarket CAO (*CAO Levensmiddelenbedrijf* / *VGL*). Even where a CAO shortens the statutory 4-day notice period, same-day shift reductions rarely eliminate wage obligations.
3. **GDPR / AVG & EU AI Act:**
   * **GDPR:** Automated scheduling and workforce analytics require a Data Protection Impact Assessment (DPIA), strict purpose limitation, and human-in-the-loop oversight.
   * **EU AI Act:** AI used for task allocation, monitoring, and evaluating workers is classified as high-risk (Annex III). Under the EU's 2026 Digital Omnibus, the formal Article 26(7) duty to inform workers and their representatives before deploying high-risk workplace AI was deferred from August 2026 to **2 December 2027**. While that specific AI Act notice rule does not apply yet, Dutch WOR and GDPR obligations apply today—and building to the AI Act transparency standard now avoids rework next year.

---

## 3. Recommended Alternative: Keep the Forecasting, Fix the Operating Model

We do not have to choose between high labour costs and chaotic schedules. We can capture the legitimate value of AI demand forecasting without the legal and retention damage:

1. **Use 15-minute AI demand forecasting to build better 2-to-4-week base rosters:** Align core shifts and part-time student blocks to recurring traffic patterns weeks in advance.
2. **Replace involuntary same-day cuts with a voluntary shift marketplace:** When unexpected peaks or absences occur, offer open shifts via an opt-in app notification to students who want extra hours—never penalise those who decline.
3. **Measure teams and stores, never rank individuals:** Use aggregated store-level metrics (coverage, queue times, total paid hours) rather than individual productivity or "flexibility" scores.

---

## 4. Proposed 6-Store Pilot Design & Go/No-Go Criteria

* **Scope:** 6 stores reflecting our mix (urban high-footfall, suburban family, commuter/student-heavy) for 6–8 weeks (Jan–Feb 2027), alongside a matched control group of 6 stores.
* **Commercial terms:** Pilot-only agreement with no chain-wide commitment, and a hard break clause if Go/No-Go criteria are not met.
* **Success criteria (agreed before launch by COO, CTO, HR, Finance, and OR):**
  1. **Net paid labour hours:** Measured reduction in *total paid hours* (not just scheduled hours), including overtime, agency cover, and any cancelled-shift pay.
  2. **Payroll accuracy:** 100% match in parallel shadow-payroll runs against CAO rules before live payroll cutover.
  3. **Service & store health:** No degradation in checkout queue times, shelf availability, or shrink.
  4. **People & manager impact:** Store manager time spent on scheduling decreases; no increase in student turnover, sick leave, or missed shifts; positive or neutral pulse feedback from store staff.

---

## Key Assumptions & Open Questions

* **Assumptions:** (a) Most of our flexible staff are under *oproep* or min-max contracts subject to WAB/CAO notice rules; (b) our POS and time-clocking data are clean enough to feed a 6-store pilot without a multi-month data warehouse rebuild; (c) the vendor is willing to contract for a paid pilot before a 140-store licence commitment.
* **What am I missing, and what would make this wrong?** For example: Is there an acute cash or covenant deadline driving the March date? Does our specific CAO already allow shorter notice windows with zero wage liability? Are we already losing significant margin to avoidable overstaffing at specific predictable hours that base-roster fixes alone could solve?
