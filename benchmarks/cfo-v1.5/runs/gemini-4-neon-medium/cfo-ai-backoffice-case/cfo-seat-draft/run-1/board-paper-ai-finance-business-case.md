# Board Paper: AI Business Case for Finance & Back-Office Operations

**To:** Board of Directors  
**From:** Chief Financial Officer  
**Date:** November 2026  
**Status:** Draft for Board discussion — financial figures are illustrative `[Estimate]` pending live extracts from payroll, general ledger, and vendor contracts.

---

## 1. Executive Summary & Recommendation

**Recommendation: Do not approve a 30% (27-FTE) AI-driven headcount reduction for next year. Approve Option B instead: a phased, task-level AI programme paired with immediate non-payroll spend reductions, process simplification, and managed natural attrition.**

The headline case for cutting 27 of 90 finance and back-office roles (accounts payable, reconciliations, reporting) shows **23.8 MSEK** in annualised gross payroll savings `[Estimate]`. When modelled honestly by quarter — including Swedish statutory notice and consultation timelines, AI implementation and recurring operating costs, controls, and realistic transition friction — **Option A costs 10.2 MSEK net cash in Year 1 and generates only 1.0 MSEK net cash over 24 months**, with a payback of roughly **23 months** `[Estimate]`.

By contrast, **Option B** delivers **+0.9 MSEK net cash in Year 1** and **+8.9 MSEK cumulative net cash over 24 months** — **7.9 MSEK ahead of Option A** — while preserving Finansinspektionen (FI), Solvency II, IFRS 17, and DORA controls, avoiding irreversible loss of institutional knowledge, and scaling AI only on measured pilot results.

### Options Summary (MSEK, Illustrative `[Estimate]`)

| Option | Year 1 Net Cash | Year 2 Net Cash | 2-Year Cumulative | End-of-Year 2 Net FTEs Reduced | Reversibility & Control Risk |
|---|---:|---:|---:|---:|---|
| **A. AI + 27 involuntary redundancies (Board prompt)** | -10.18 | +11.16 | +0.98 | 22 *(27 cut, 5 backfilled)* | Low reversibility; high FI/DORA/audit & turnover risk |
| **B. Phased AI pilots + spend/toil cuts + natural attrition (Recommended)** | +0.94 | +7.92 | +8.86 | 12 *(natural attrition & moves)* | High reversibility; quarterly stage gates; controls intact |
| **C. Non-payroll spend, toil cuts & hiring freeze (no AI capex)** | +4.12 | +6.92 | +11.04 | 4–5 *(natural attrition)* | High reversibility; defers automation capability |
| **D. Do nothing (baseline)** | 0.00 | 0.00 | 0.00 | 0 | Baseline; ~2.4 MSEK/yr wage drift `[Estimate]` |

---

## 2. Framing the Real Problem

The Board's push is grounded in real pressures: insurance expense ratios are tight, manual work in accounts payable, premium/claims reconciliations, and statutory reporting is high, and peers are investing in automation. Those pressures are genuine and require action.

However, **a headcount percentage by a calendar date is a solution, not a diagnosis**. Before committing to irreversible redundancies, we need to establish:
1. **What financial target we are solving for and by when** — Year 1 expense-ratio relief, Year 2–3 structural run-rate, or capacity to absorb growth without adding staff. (If the goal is Year 1 earnings or cash, Option A moves the needle in the wrong direction.)
2. **Where the hours actually go** — how much of the 90-FTE workload is repetitive data handling versus exception resolution, IFRS 17/Solvency II judgement, and internal control sign-off.
3. **What we can cut without losing people** — duplicate reporting tools, unused BI licences, external reporting consultants, and low-value internal reports that nobody acts on.

---

## 3. Baseline & Illustrative Assumptions

All figures below are `[Estimate]` and must be replaced with actuals from our systems of record before a binding decision (see Section 8).

- **Scope:** 90 FTEs across accounts payable (~30), reconciliations (~30), and financial/regulatory reporting & controlling (~30) `[Estimate]`.
- **Fully loaded FTE cost:** **0.88 MSEK/year** (**0.22 MSEK/quarter**), based on an illustrative average salary of 600 kSEK/year plus Swedish statutory employer social security (*arbetsgivaravgifter*, 31.42%), occupational pension (ITP/FTP) and payroll tax, and workspace/IT `[Estimate]`.
- **Baseline payroll:** **79.20 MSEK/year** (19.80 MSEK/quarter) `[Estimate]`.
- **Board target (30%):** **27 FTEs**, or **23.76 MSEK/year** (5.94 MSEK/quarter) gross annualised payroll `[Estimate]`.

---

## 4. Detailed Financial Models (Net Cash, by Quarter)

### Option A: AI + 27 Involuntary Redundancies Next Year `[Estimate]`

**Timing reality in Sweden:** Under the Co-determination Act (*MBL*), union negotiations must conclude before a final restructuring decision. Because 27 redundancies exceed the 26-person threshold, Sweden's Public Employment Service (*Arbetsförmedlingen*) must be notified at least **4 months in advance**. Combined with statutory/collective-agreement notice periods of **1 to 6 months** under *LAS*, no payroll savings land in Q1 or Q2; exits phase in during Q3 (avg 9 FTEs off payroll) and Q4 (avg 22 FTEs off payroll), reaching 27 FTEs entering Year 2.

| Line (MSEK) | Q1 | Q2 | Q3 | Q4 | Year 1 | Year 2 | Basis / Assumption `[Estimate]` |
|---|---:|---:|---:|---:|---:|---:|---|
| Gross payroll saving (from actual exit dates) | 0.00 | 0.00 | +1.98 | +4.84 | **+6.82** | **+23.76** | 0, 0, 9, 22 avg FTEs in Y1; 27 in Y2 × 0.22/qtr |
| AI build, ERP integration & data/DORA work | -1.50 | -2.50 | -1.50 | -0.50 | **-6.00** | **0.00** | Connectors, data hygiene, testing, audit trails |
| AI recurring licences, usage & monitoring | -0.20 | -0.50 | -0.70 | -0.70 | **-2.10** | **-2.80** | Enterprise licences, compute, model & control ops |
| Severance, *avtalsturlista* & legal/advisory | -0.40 | -0.80 | -2.00 | -1.60 | **-4.80** | **0.00** | ~0.15 MSEK/FTE transition/negotiation + 0.75 legal |
| Work still to be done (contractors, overtime) | 0.00 | -0.60 | -1.20 | -1.40 | **-3.20** | **-3.60** | Parallel runs, year-end close, exception handling |
| Extra voluntary attrition & ramp-up | 0.00 | 0.00 | -0.30 | -0.60 | **-0.90** | **-1.80** | 4 extra regretted leavers; replacement & ramp cost |
| Backfilled / rehired roles | 0.00 | 0.00 | 0.00 | 0.00 | **0.00** | **-4.40** | 5 FTEs refilled in Y2 for controls/exceptions (5 × 0.88) |
| **Net cash effect** | **-2.10** | **-4.40** | **-3.72** | **+0.04** | **-10.18** | **+11.16** | **2-Year cumulative: +0.98 MSEK** |

*P&L note:* Under IFRS (IAS 37), once a restructuring plan is formally committed (likely Q2), the full redundancy provision hits P&L immediately in Q2 rather than phasing across Q3–Q4. Cloud/SaaS AI configuration costs are typically expensed as incurred under IAS 38. Restructuring costs should **not** be stripped out of "adjusted" operating profit if further automation waves are anticipated within two years.

*Break-even & sensitivity (Option A):* Over 24 months, Option A's net cushion is **0.98 MSEK**. Any single variance — **one additional backfilled FTE** (0.88 MSEK/year), a **15% overrun** on AI integration (0.90 MSEK), a **one-quarter delay** in exits, or **one Solvency II / IFRS 17 audit remediation** (1–3 MSEK) — turns the 2-year net present value negative.

---

### Option B (Recommended): Phased Task-Level AI + Spend/Toil Cuts + Natural Attrition `[Estimate]`

Option B attacks non-payroll waste and low-value reporting immediately, runs two bounded AI pilots in Q1–Q2 (AP invoice processing and standard reconciliations) with union involvement and human sign-off, and uses a selective hiring freeze plus natural attrition (~8–10%/year typical turnover; replacing only critical roles) to reduce headcount by **6 net FTEs in Year 1** (avg 3 FTEs off payroll) and **12 net FTEs by end of Year 2** (avg 9 FTEs off payroll in Year 2), paired with reskilling.

| Line (MSEK) | Q1 | Q2 | Q3 | Q4 | Year 1 | Year 2 | Basis / Assumption `[Estimate]` |
|---|---:|---:|---:|---:|---:|---:|---|
| Non-payroll spend & toil reduction | +0.40 | +0.70 | +0.85 | +0.85 | **+2.80** | **+3.40** | Consolidate BI/reporting licences, external consultants, unused packs |
| Selective hiring freeze & natural attrition | +0.22 | +0.44 | +0.88 | +1.10 | **+2.64** | **+7.92** | 1, 2, 4, 5 avg FTEs in Y1; 9 avg FTEs in Y2 × 0.22/qtr |
| Phased AI pilots & integration (stage-gated) | -0.50 | -0.80 | -0.70 | -0.50 | **-2.50** | **-1.00** | 2 bounded pilots (AP & standard recs); scale only on proof |
| AI licences, usage & monitoring | -0.10 | -0.20 | -0.35 | -0.45 | **-1.10** | **-1.80** | Right-sized seats and model usage; monthly budget owner |
| Reskilling & internal redeployment | -0.15 | -0.25 | -0.25 | -0.25 | **-0.90** | **-0.60** | AI review, data quality, internal moves (plus *omställningsstudiestöd*) |
| Severance, extra attrition & rehiring | 0.00 | 0.00 | 0.00 | 0.00 | **0.00** | **0.00** | Zero involuntary redundancies in Y1–Y2 |
| **Net cash effect** | **-0.13** | **-0.11** | **+0.43** | **+0.75** | **+0.94** | **+7.92** | **2-Year cumulative: +8.86 MSEK** |

*Option B upside:* If the Q1–Q2 pilots prove >99% accuracy and measurable hours freed, Year 2–3 scaling can continue reducing headcount through natural attrition and voluntary transitions — reaching 15–20% lower headcount by Year 3 without a single forced redundancy or control breach.

---

## 5. Task-Level AI Feasibility & Insurance Control Boundaries

AI replaces **tasks**, not whole jobs. Sizing by function shows why a blanket 30% cut in 12 months is operationally unsafe:

| Function (`~30 FTEs` each `[Estimate]`) | Realistic Year 1 AI Scope | Must Remain Human-Owned | Pilot Metric Before Scaling |
|---|---|---|---|
| **Accounts Payable** | Invoice capture, PO/contract matching, coding suggestions, duplicate detection | Payment release, vendor master-data changes, segregation of duties, disputed claims/supplier invoices | Straight-through accuracy vs. baseline; zero duplicate/unauthorised payments |
| **Reconciliations** | High-volume bank, premium, and broker statement matching; variance flagging | Investigating breaks, reinsurance/claims ledger adjustments, root-cause fixes | Hours freed per close cycle; open aged breaks (>30 days) |
| **Reporting (IFRS 17 / Solvency II)** | First-draft variance commentary, data completeness checks, QRT validation rules | Judgemental estimates, actuarial/finance sign-off, FI submissions, audit committee explanations | Close-cycle days saved; zero audit adjustments or FI queries from AI errors |

**External evidence to keep in view:**
- **AI business-case base rates:** MIT NANDA (2025) found roughly 95% of enterprise generative AI pilots showed no measurable P&L impact (treat as directional, given methodological debate), and Gartner (2025) projected over 40% of agentic AI projects would be cancelled by end-2027 due to cost, unclear value, or weak controls. A 2025 randomised trial by METR showed experienced developers took 19% longer with AI tools while believing they were faster (with newer tools still requiring local measurement).
- **AI layoff regret & turnover:** In a 2026 Careerminds survey of 600 HR leaders, two-thirds of companies that cut jobs for AI were already rehiring (52% within six months), and 30.9% found rehiring costs exceeded savings; an Orgvue survey (2025) found 55% of leaders who made AI redundancies regretted the decisions (both are vendor surveys — treat as strong signals, not exact rates). Academic research (Trevor & Nyberg, 2008) links a 1% workforce downsizing to a 31% rise in voluntary turnover the next year, and Gallup estimates employee replacement costs at 0.5× to 2× annual salary.

---

## 6. Swedish Employment Law, Union Practice & Insurance Regulation

*Note: This section flags statutory and regulatory constraints for planning purposes. It is not legal, tax, or regulatory advice; Swedish employment counsel, HR, Compliance, and Internal Audit must review before any commitment.*

1. **Co-determination (*MBL*):** Major organisational changes and new workplace technologies require primary union negotiation *before* a decision is taken. Involving unions (e.g., Forena, Akavia, Unionen, per our collective agreements) at the pilot-design stage improves outcomes: OECD (2023) finds AI adoption produces better productivity and job-quality results when worker representatives are consulted early.
2. **Employment Protection Act (*LAS*):** Redundancies follow a strict length-of-service order (*sist in, först ut*) per operational unit and collective agreement area, with only **three statutory exemptions** allowed since 2022 unless an agreed list (*avtalsturlista*) is negotiated with the union. We cannot simply select the 27 people whose tasks are automated; strict LAS risks losing newer, data-fluent analysts needed to run and audit the AI.
3. **Advance notice to *Arbetsförmedlingen*:** Dismissing **26 to 100 people** requires at least **4 months' advance notice** (versus 2 months for 5–25). At 27 FTEs, Option A triggers the 4-month bracket.
4. **Notice periods & re-employment priority:** Statutory notice runs **1 to 6 months** by tenure (often extended by collective agreements). Dismissed staff with >12 months' service in the past 3 years hold **9 months' re-employment priority** (*företrädesrätt*), restricting external hiring if we need to backfill.
5. **Transition support (*TRR* & *omställningsstudiestöd*):** If any roles eventually become redundant, Sweden's job security councils (e.g., TRR, funded via collective agreements) step in from day of notice (OECD 2015 found >85% re-employment within a year). Under Option B, employees wishing to reskill can also access Sweden's transition study support (*omställningsstudiestöd*, ~80% of salary up to a ceiling for up to ~1 year of study; nearly 21,000 users in 2025).
6. **Regulatory governance (FI, Solvency II, DORA, EU AI Act):**
   - **Solvency II & DORA** (in force since January 2025) require documented ICT third-party risk management, resilience testing, segregation of duties, and human accountability for financial reporting and internal controls.
   - **EU AI Act:** Note that the Article 26(7) duty to inform workers and representatives before deploying high-risk workplace AI takes effect on **2 December 2027** (moved from August 2026 by the 2026 Digital Omnibus) — it does not yet apply, though Swedish *MBL* rules already require negotiation today.

---

## 7. Governance, Stage Gates & Indicators (Option B)

If the Board approves Option B, we will review progress quarterly against both financial and people/control indicators:

- **Financial:** Net cash vs. plan, AI total cost of ownership (licences + integration + monitoring), non-payroll spend saved, hours freed per workflow (booked as capacity first, not assumed payroll).
- **Control & Quality:** Reconciliation error rate, close-cycle days, IFRS 17/Solvency II audit findings, DORA incident/testing status.
- **People:** Regretted voluntary attrition, internal redeployment/reskilling count, engagement/workload score.
- **Stage-gate rule:** At the end of Q2, any pilot that does not beat baseline accuracy and deliver verifiable hours freed is stopped or redesigned before further spend is released.

---

## 8. Data Required from Systems of Record to Finalise This Case

Before the Board votes on final budgets, Finance and HR will replace every `[Estimate]` above with live extracts from:
1. **Payroll / HRIS (aggregated only — no individual names or salaries):** Exact fully loaded cost per functional band, tenure distribution (for LAS notice and seniority modelling), and 3-year historical voluntary attrition by sub-team.
2. **General Ledger & Vendor Contract Register:** Current spend on finance/BI/reporting software, external consultants, and upcoming renewal dates.
3. **Activity / Close-Cycle Logs:** Hours spent per month on AP, reconciliations, and reporting broken down by repetitive processing vs. exceptions and sign-off.
4. **Collective Agreements & Legal Review:** Applicable notice extensions, job security council terms, and *MBL* timeline confirmed by Swedish employment counsel.
5. **Audit & Compliance Register:** Current internal control matrix for AP, reconciliations, and FI reporting, plus DORA vendor-onboarding lead times.

---

## 9. Key Assumptions & Challenge

**Key assumptions that drive this recommendation:**
- Average fully loaded FTE cost is ~0.88 MSEK/year and voluntary attrition is ~8–10%/year.
- Full-scope AI implementation with DORA/FI controls takes 6–9 months and costs ~6 MSEK upfront plus ~2.8 MSEK/year ongoing.
- Under Swedish law (*MBL*, *LAS*, *Arbetsförmedlingen* 4-month notice), involuntary exits cannot generate net payroll savings before Q3.

**What am I missing, and what would make this wrong?**
- If the Board has an external solvency, covenant, or owner deadline that requires a specific Year 1 expense ratio regardless of Year 2 payback, we should state that target explicitly and look at non-payroll and leadership-cost levers first.
- If our actual voluntary attrition is much lower than 8%, or our ERP/data environment is already clean enough to deploy AP/reconciliation automation in under 90 days at lower cost, the numbers should be updated accordingly.
