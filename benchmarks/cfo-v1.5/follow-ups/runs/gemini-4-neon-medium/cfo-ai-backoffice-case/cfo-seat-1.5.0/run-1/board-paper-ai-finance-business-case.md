# Board Paper: AI in Finance & Back-Office — Honest Business Case & Options

**To:** Board of Directors  
**From:** Chief Financial Officer  
**Date:** November 2026  
**Status:** Draft for CFO review (labelled estimates to be replaced with internal ERP, payroll, and vendor data before board distribution)  
**Decision requested:** Approve an evidence-gated AI pilot paired with non-payroll spend cleanup (Option B + Option C), rather than committing to a 30% headcount reduction next year (Option A).

---

## 1. Executive Summary

**Recommendation:** Do not commit to replacing 30% (27 FTEs) of the 90-person finance and back-office team with AI next year. Under Swedish employment law and realistic AI implementation timelines, a 30% reduction next year is **net cash negative by SEK 15.10m in Year 1** and remains **SEK 5.98m underwater after two years**, while exposing Solvency II, IFRS 17, and DORA controls to severe operational risk.

Instead, approve a **two-part plan**:
1. **Option B (Evidence-Gated AI Pilot + Natural Attrition & Redeployment):** Run a 6-month controlled pilot in Accounts Payable and standard reconciliations with union and team involvement from day one. Book **zero payroll savings** until the Q2 gate proves freed hours at required accuracy. Capture proven capacity through natural attrition (~10%/year) and internal redeployment, targeting **15%–23% addressable capacity over 24–30 months** (~12–15 FTEs by Year 3, generating **SEK 8.1m–11.0m/year** net recurring savings once mature). Downside is capped at **SEK 3.20m** if the Q2 gate fails.
2. **Option C (Non-Payroll Spend & Process Cleanup):** Immediately cut redundant reporting/BI licences and manual audit-prep consultant spend, delivering **SEK +1.60m net cash in Year 1** and **SEK +3.20m in Year 2** with zero job losses.

Paired together (Option B + Option C), the company reaches **SEK +2.88m cumulative net cash positive within 24 months**, protects audit and regulatory compliance, and avoids involuntary redundancies.

---

## 2. Framing the Real Problem

The board is right to challenge our finance and back-office cost ratio. Manual invoice handling, fragmented reconciliations, and repetitive reporting consume skilled capacity that should go toward underwriting insight, capital efficiency, and faster close cycles.

However, **"replace 30% of headcount next year" is a target, not a plan.** Before committing to a headcount number, we should clarify the underlying financial objective (e.g., combined-ratio / expense-ratio improvement, target MSEK saving, and required date) and size what AI can actually do at task level—not job level—within a regulated Swedish insurer.

### What Must Be Verified From Systems of Record Before Finalising
All financial figures below are **labelled estimates** for a 90-person Swedish insurer finance team. Before board submission, Finance and HR should replace them with actuals from:
- **Payroll aggregates (no individual names/salaries):** true fully loaded cost per FTE by function, tenure distribution (for notice periods and LAS seniority order), and 3-year voluntary attrition rate.
- **General ledger & AP vendor ledger:** external audit overrun fees, interim finance consultant spend, and overlapping BI/reporting/reconciliation software licences.
- **Time/activity logs & incident registers:** actual hours spent on invoice matching, exception handling, reconciliation backlogs, and Solvency II/IFRS 17 reporting.
- **CTO / IT architecture assessment:** integration effort across legacy policy administration, claims systems, and ERP, plus DORA third-party ICT risk requirements.

---

## 3. Task-Level AI Sizing (Not Job-Level)

AI automates *tasks*, not whole roles. Even where a task is automated, a regulated insurer must retain segregation of duties, audit trails, exception handling, and named human sign-off for Finansinspektionen (FI) and external auditors.

| Function | Est. Headcount | Automatable Tasks | Human-Only Work (Controls & Judgment) | Realistic Addressable Capacity (Post-Pilot, Yr 2–3) |
|---|---|---|---|---|
| **Accounts Payable** | 20 FTE | Invoice capture, PO/3-way matching, coding suggestions | Vendor disputes, fraud/approval controls, master-data governance, exceptions | **25%–35%** (5.0–7.0 FTE-eq.) |
| **Reconciliations** (bank, premium, claims, reinsurance) | 35 FTE | Standard bank & sub-ledger matching, routine variance flagging | Unallocated premiums, broker bordereaux, reinsurance disputes, claims adjustments | **15%–25%** (5.0–9.0 FTE-eq.) |
| **Reporting & FP&A** (IFRS 17, Solvency II, management) | 35 FTE | Data aggregation, draft variance commentary, routine schedules | Technical provisions, Solvency II QRT sign-off, IFRS 17 judgment, audit defence | **10%–15%** (3.5–5.0 FTE-eq.) |
| **Total** | **90 FTE** | | | **15%–23% (13.5–21.0 FTE-eq.)** |

**Key takeaway:** Evidence-based task sizing supports **15%–23% capacity release over 24–30 months**, not 30% next year. Productivity gains are also not automatic: a 2025 randomised trial by METR found experienced practitioners actually took 19% longer on complex tasks with AI tools while believing they were faster—underscoring the need to measure error rates and cycle times on our own ledgers before changing headcount.

---

## 4. Swedish Employment Law & Regulatory Constraints

*Note: This section flags legal and regulatory constraints for planning; it is not legal advice. Swedish employment counsel and union representatives must be consulted before any formal proposal.*

1. **Co-determination (MBL):** Major organisational changes and new workplace technology require union negotiation (e.g., Forena, Akavia, Unionen) *before* a decision is made. Allow 4–8 weeks minimum before any notice can be issued.
2. **Advance notification (*varsel*) to Arbetsförmedlingen:** Dismissing **26–100 employees** requires at least **4 months' advance notice** (2 months for 5–25 employees). For 27 people, exits cannot take effect before late Q2/Q3 even if started on 1 January.
3. **Selection order (LAS *turordning*):** Redundancies follow length of service per operational unit and collective agreement area—not job category or individual performance—unless a local agreement (*avtalsturlista*) is negotiated with the union. Employers may exempt only **three** employees. Management cannot simply pick which 27 roles go, creating a high risk of losing recently hired data/AI-fluent specialists.
4. **Notice periods & re-employment priority (*företrädesrätt*):** Notice runs **1 to 6 months** by tenure (estimated 4-month average across this team). Dismissed staff with >12 months' service hold **9 months' priority for re-employment**, complicating rehiring if AI under-delivers.
5. **Transition support (TRR & *omställningsstudiestöd*):** White-collar collective agreements fund job security councils (e.g., TRR), which support displaced staff from day one of notice (OECD data shows >85% of displaced Swedish workers find new work within a year). Sweden's adult transition study support (*omställningsstudiestöd*, ~80% of salary up to a ceiling for up to ~1 year) also supports structured reskilling.
6. **EU AI Act & DORA:** Under the EU AI Act (as amended by the 2026 Digital Omnibus), the formal duty to inform worker representatives before deploying high-risk workplace AI (Article 26(7)) applies from **2 December 2027**, but Swedish MBL co-determination duties already apply today. Under **DORA** (in force since January 2025), any third-party AI vendor touching financial reporting or reconciliations requires ICT risk assessment, resilience testing, and exit planning.

---

## 5. Financial Comparison of Options (All Figures in SEK Million, Estimates)

### Shared Baseline Assumptions (Estimates)
- **Fully loaded cost per FTE:** **SEK 0.96m/year** (SEK 0.24m/quarter; SEK 0.08m/month), based on ~SEK 53k/month average gross salary plus ~50% employer social contributions (*arbetsgivaravgifter* 31.42%), occupational pension, holiday pay, and workspace/IT.
- **Total team payroll baseline:** 90 FTEs × SEK 0.96m = **SEK 86.40m/year** (SEK 21.60m/quarter).
- **Baseline natural attrition:** **10%/year** (~9 FTEs/year).
- **Accounting note:** All figures are shown on a consistent basis. Non-payroll savings (Option C) are modelled separately so they are not double-counted in Option B.

### Summary Comparison Side-by-Side (MSEK)

| Option | Year 1 Net Cash | Year 1 Net P&L | Year 2 Net Cash | 2-Yr Cumulative Cash | Reversibility | Regulatory & People Risk |
|---|---|---|---|---|---|---|
| **A. Board's Request: AI + 30% Cut Next Year (27 FTEs)** | **-15.10** | **-15.10** | **+9.12** | **-5.98** | Very low (LAS/re-hire lock-in) | **High** (control gaps, regretted exits, audit risk) |
| **B. Recommended: Gated AI Pilot + Attrition/Redeployment** | **-6.36** | **-6.36** | **+4.44** | **-1.92** | **High** (stop at Q2 gate: -3.20 max) | **Low** (dual-running, union co-design) |
| **C. Non-Payroll Spend & Process Cleanup (No AI/Layoffs)** | **+1.60** | **+1.60** | **+3.20** | **+4.80** | High | **Very low** |
| **B + C Combined (Recommended Package)** | **-4.76** | **-4.76** | **+7.64** | **+2.88** | **High** | **Low** |
| **D. Do Nothing (Baseline)** | **0.00** | **0.00** | **0.00** | **0.00** | N/A | **Medium** (persistent manual toil) |

---

### Option A Detail: AI + 30% Cut Next Year (27 FTEs) — MSEK

*Assumes MBL negotiations + 4-month Arbetsförmedlingen varsel + 4-month average paid notice delay payroll exits until Month 8 (Aug). Gross saving = 27 FTEs × SEK 0.08m/mo = SEK 2.16m/mo from Month 8.*

| Line | Q1 | Q2 | Q3 | Q4 | Year 1 | Year 2 | Basis / Assumption (Estimates) |
|---|---:|---:|---:|---:|---:|---:|---|
| Gross payroll saving (from actual exit dates) | 0.00 | 0.00 | +4.32 | +6.48 | **+10.80** | **+25.92** | 2 mo in Q3, 3 mo in Q4; full yr in Y2 |
| AI build, integration, licences & DORA controls | -2.80 | -3.50 | -2.30 | -1.30 | **-9.90** | **-3.20** | ERP/policy integration (-7.50 Y1) + licences/QA |
| Severance, legal/MBL & transition top-up | -0.50 | -0.90 | -5.40 | 0.00 | **-6.80** | **0.00** | *Avtalsturlista* packages (~0.20/FTE), counsel, support |
| Work still to be done (contractors, overtime, audit) | 0.00 | -0.40 | -2.40 | -3.60 | **-6.40** | **-6.00** | Interim cover for 10–12 FTE gap & year-end close |
| Rehiring & ramp-up (roles cut too deep) | 0.00 | 0.00 | 0.00 | 0.00 | **0.00** | **-4.80** | 6 roles refilled in Y2 (~0.80m salary + recruiting) |
| Extra voluntary attrition (regretted exits) | 0.00 | 0.00 | -0.60 | -1.20 | **-1.80** | **-1.80** | 6 extra exits over 18 mo × 0.60m replacement cost |
| Error / audit / operational risk allowance | 0.00 | 0.00 | -0.30 | -0.70 | **-1.00** | **-1.00** | Conservative allowance for recon/filing rework |
| **Net cash effect** | **-3.30** | **-4.80** | **-6.68** | **-0.32** | **-15.10** | **+9.12** | **2-Yr cumulative: -5.98 MSEK** |
| **Net P&L effect** | **-3.30** | **-10.20** | **-1.28** | **-0.32** | **-15.10** | **+9.12** | IAS 37 severance provision (-5.40) booked in Q2 |

*Evidence note:* Trevor & Nyberg (2008) found a 1% downsizing was associated with 31% higher voluntary turnover the following year; Gallup estimates employee replacement cost at 0.5×–2.0× annual salary (we use a conservative 0.625× above). Guthrie & Datta (2008) found downsizing is associated with lower subsequent profitability, and Bain's study of 470 companies found only 12% of cost transformations delivered sustained improvement.

---

### Option B Detail (Recommended): Evidence-Gated AI Pilot + Attrition & Redeployment — MSEK

*Assumes 6-month pilot (Q1–Q2) in AP & standard reconciliations with zero payroll saving booked pre-gate. Post-gate, natural attrition (~10%/yr) is selectively not backfilled: 2 FTEs in Q3, 4 FTEs in Q4, averaging 9 FTEs in Year 2 (reaching 12 FTE run-rate by Q4 Year 2).*

| Line | Q1 | Q2 | Q3 | Q4 | Year 1 | Year 2 | Basis / Assumption (Estimates) |
|---|---:|---:|---:|---:|---:|---:|---|
| Gross payroll saving (post-gate attrition only) | 0.00 | 0.00 | +0.48 | +0.96 | **+1.44** | **+8.64** | 0 in H1; 2 FTE Q3, 4 FTE Q4; avg 9 FTE Y2 |
| AI pilot, phased build, licences & controls | -1.20 | -1.20 | -1.80 | -1.50 | **-5.70** | **-2.80** | Scoped pilot (-2.40 H1); scale only if gate passes |
| Reskilling, training & change support | -0.15 | -0.25 | -0.40 | -0.40 | **-1.20** | **-0.80** | Co-design, reviewer training, redeployment |
| Dual-running, QA & exception cover | -0.20 | -0.20 | -0.20 | -0.10 | **-0.70** | **-0.40** | Parallel run during pilot; ongoing audit sampling |
| Severance / rehiring / extra attrition | 0.00 | 0.00 | 0.00 | 0.00 | **0.00** | **0.00** | No involuntary layoffs; gated scaling |
| Error / control risk allowance | 0.00 | 0.00 | -0.10 | -0.10 | **-0.20** | **-0.20** | Minimal residual risk with human-in-the-loop |
| **Net cash & P&L effect** | **-1.55** | **-1.65** | **-2.02** | **-1.14** | **-6.36** | **+4.44** | **2-Yr cumulative: -1.92; Yr 3 run-rate: +8.1–11.0/yr** |

---

### Option C Detail: Non-Payroll Spend & Process Cleanup (No AI / No Layoffs) — MSEK

*Can be executed standalone or paired immediately with Option B.*

| Line | Q1 | Q2 | Q3 | Q4 | Year 1 | Year 2 | Basis / Assumption (Estimates) |
|---|---:|---:|---:|---:|---:|---:|---|
| Vendor, licence & audit-prep spend reduction | 0.00 | +0.60 | +0.80 | +0.80 | **+2.20** | **+3.20** | Redundant BI/recon licences (1.2m), consultant spend (2.0m) |
| Cleanup & contract renegotiation cost | -0.40 | -0.20 | 0.00 | 0.00 | **-0.60** | **0.00** | Internal/procurement effort |
| **Net cash & P&L effect** | **-0.40** | **+0.40** | **+0.80** | **+0.80** | **+1.60** | **+3.20** | **2-Yr cumulative: +4.80 MSEK** |

---

## 6. Break-Even & Sensitivities

- **Option A break-even:** Option A **cannot break even in Year 1** under Swedish law—even if AI implementation were 50% cheaper (-4.95m), Year 1 remains **SEK -10.15m**. In Year 2, if just **9 additional roles** require contractor cover or rehiring (or if a regulatory/audit finding plus broker churn costs SEK 9.1m), the entire Year 2 saving (+9.12m) disappears.
- **Option B downside (pilot fails Q2 gate):** Stop spending at end of Q2; total net cost is capped at **SEK 3.20m**, with zero layoffs and zero control disruption.
- **Option B attrition sensitivity:** If natural attrition is 7%/year instead of 10%, Year 2 average non-backfilled FTEs drop from 9 to 6 (-2.88m), reducing Year 2 net cash from **+4.44m to +1.56m** (still cash positive in Year 2).
- **Option B upside:** If AI reaches the top of our task-sizing range (20% capacity = 18 FTEs by end of Year 3 via attrition/redeployment), Year 3 annual net saving reaches **SEK +13.88m/year** (17.28m gross minus 3.40m AI/QA/risk).

---

## 7. Governance, Controls & Quarterly Review Gates

1. **Q2 Pilot Gate (Go / No-Go Criteria):** Scale AI beyond the pilot *only* if:
   - Straight-through matching accuracy meets pre-set audit thresholds (e.g., ≥98% on AP coding, zero unflagged material reconciliation breaks).
   - Measured net hours freed (after human review and exception handling) exceed 15% in the pilot scope.
   - Internal Audit, CTO, and Compliance confirm DORA and Solvency II segregation-of-duties compliance.
2. **Union & Employee Co-Design:** Bring union representatives (MBL) and team leads into the pilot design in Month 1. OECD research (*Employment Outlook 2023*) shows AI adoption delivers better productivity and job quality when worker representatives are consulted early.
3. **Balanced Scorecard & Incentives:** Tie zero executive bonuses to headcount reduction. Track quarterly on one board page:
   - **Financial:** Net cash vs. budget, AI spend per active user/process, external audit & contractor fees.
   - **Quality & Risk:** Close cycle days, reconciliation aged items >30 days, error/rework rate, audit findings.
   - **People:** Regretted attrition, internal redeployment rate, training hours completed, team workload/engagement.

---

## 8. Key Assumptions & Questions for the Board

1. **What is the underlying target?** Is the board aiming for a specific expense-ratio reduction by a specific year, or testing AI's potential? If we need Year 1 cash, non-payroll spend (Option C) delivers immediately while AI does not.
2. **Risk appetite on controls:** Is the board willing to accept elevated Solvency II/IFRS 17 audit and DORA risk in Year 1 in pursuit of an unvalidated 30% headcount target?
3. **What would change this recommendation?** If the Q2 pilot proves >25% net hours freed at audit-grade accuracy *and* natural attrition falls below 5%, we would revisit redeployment and voluntary exit options with the unions in Q3—grounded in real data rather than a pre-set percentage.
