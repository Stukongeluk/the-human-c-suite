# Business Case: AI Adoption in Finance & Back-Office Operations

**Prepared by:** Chief Financial Officer  
**For:** Board of Directors & Executive Management  
**Date:** November 2026  
**Status:** Draft for Board Discussion (contains illustrative cost estimates; see Assumptions)

---

## 1. Executive Summary & Recommendation

**Recommendation:** Reject a target of 30% (27 FTE) forced headcount reductions next year. Instead, approve a **phased, task-first AI rollout** starting in Accounts Payable and Reconciliations, paired with a **selective hiring freeze, natural attrition, contractor reduction, and internal redeployment**.

- **Why the 30% Year-1 cut fails the financial test:** Under Swedish employment law (MBL consultation, a 4-month advance notice to *Arbetsförmedlingen* for 26–100 redundancies, and 1–6 month LAS notice periods), forced exits cannot take effect until late in Year 1. With upfront implementation, licensing, and transition costs, a 27-FTE cut produces an estimated **net cash outflow of SEK −3.3M in Year 1**, while exposing statutory reporting (Solvency II, IFRS 17) to uncontrolled skill loss under LAS seniority rules.
- **Why the phased path wins:** By targeting tasks rather than headcount—automating high-volume invoice matching and sub-ledger reconciliations first—the company can achieve an estimated **net positive cash impact of SEK +0.5M in Year 1** and **SEK +12.9M/year in steady-state savings by Year 2**, while keeping institutional knowledge and redeploying 6–10 experienced staff into higher-value margin and risk work (e.g., claims leakage, broker analytics, and regulatory reporting).

> **Note on estimates:** All SEK figures below use an illustrative fully loaded Swedish finance/back-office cost of **SEK 850k per FTE/year** (base salary, ~31.42% employer social fees, occupational pension, and overhead) and **SEK 76.5M** total team cost for 90 FTEs. Actual payroll, tenure distribution, and vendor quotes must be plugged in before final budget sign-off.

---

## 2. Clarifying the Objective

"Replace 30% of 90 people with AI next year" is a headcount target, not a business problem. Before committing capital or initiating union negotiations, the Board and management should align on which outcome we are optimising for:

1. **Combined-ratio / expense-ratio reduction** (durable net cost savings over 2–3 years without increasing operational risk), or
2. **Faster close and higher control quality** (fewer manual reconciliation breaks, cleaner audit trails, faster Solvency II / IFRS 17 reporting), or
3. **Capacity for growth** (handling higher policy and claims volume without adding back-office headcount).

External base rates urge caution against headcount-first AI mandates:
- **MIT NANDA (2025)** reported that roughly **95% of enterprise generative AI pilots** showed no measurable P&L impact yet.
- **Gartner (2025)** forecasts that **over 40% of agentic AI projects** will be cancelled by the end of 2027 due to escalating costs, unclear value, or inadequate risk controls.
- **Careerminds (2026)** surveyed 600 HR leaders who carried out layoffs for AI: **two in three were already rehiring** (52% within six months), only **8.4%** would repeat the restructure unchanged, and for **30.9%** rehiring costs exceeded savings.

---

## 3. Task-Level Assessment: Where AI Works and Where Liability Stays

AI replaces *tasks*, not whole roles. Even where AI resolves routine items, it handles the shortest, simplest cases first and creates new oversight work (exception handling, knowledge-base maintenance, and output verification).

| Function | Current Work | Realistic AI Automation Potential (12–18 mo) | What Must Remain Human |
|---|---|---|---|
| **Accounts Payable (AP)** | Invoice capture, PO matching, GL coding, payment runs | **High (40–60% of routine volume):** OCR/AI extraction, automated 3-way matching, coding suggestions | Exception resolution, vendor fraud/sanctions checks, dual-signoff on disbursements, disputed supplier terms |
| **Reconciliations** | Bank, premium, claims, and reinsurance sub-ledger matching | **Medium-High (30–50% of matching):** Automated pattern matching and break flagging | Investigating complex breaks, reinsurance treaty disputes, balance-sheet substantiation, audit sign-off |
| **Financial & Regulatory Reporting** | Monthly close, IFRS 17, Solvency II QRTs/SFCR, board packs | **Low-Medium (15–25% of prep):** Drafting variance commentary, automated data pulls and formatting | Judgement calls, actuarial/accounting assumptions, Finansinspektionen sign-off, statutory accountability |

**Liability cannot be delegated to a model:** As established in *Moffatt v. Air Canada* (2024), organisations remain legally liable for errors produced by their AI tools. In regulated Swedish insurance, responsibility for accurate financial and Solvency II reporting sits with the CFO, CEO, and Board.

---

## 4. Strategic Options & Financial Comparison

All figures in **SEK millions (estimates)**. Steady-state (Year 2) reflects full-year run-rate.

| Option | Year 1 Gross Savings | Year 1 Costs (Impl / Ops / Exit) | Year 1 Net Cash Impact | Year 2 Net Savings / yr | People Affected & How | Reversible? | Key Risks |
|---|---|---|---|---|---|---|---|
| **0. Do Nothing (Baseline)** | 0.0 | 0.0 | **0.0** | **0.0** | 90 FTEs; normal ~8% attrition backfilled | Yes | Manual toil persists; miss genuine AP/rec efficiency |
| **1. Board Target: Forced 30% Cut (27 FTEs)** | +5.7 *(~3 mo active saving after notice)* | −9.0 *(5.0 impl, 1.5 ops, 2.5 exit/transition)* | **−3.3** | **~+19.0** *(after 1.5 ops + ~2.5 backfill risk)* | 27 involuntary exits via LAS seniority order | **No** *(9-mo rehire priority; skill loss)* | Audit/close failures; survivor turnover (+31% per 1% cut, Trevor & Nyberg 2008); union conflict |
| **2. Recommended: Phased AI + Attrition & Redeployment** | +5.0 *(3.0 from ~7 FTE attrition + 2.0 temp/waste cut)* | −4.5 *(3.0 phased impl, 1.0 ops, 0.5 reskilling)* | **+0.5** | **+12.9** *(14 cum. FTE attrition + 2.5 vendor cut − 1.5 ops)* | ~14 FTEs via natural attrition over 24 mo; 6–10 redeployed; **0 forced exits** | **Yes** *(wave-gated)* | Slower headline headcount drop; requires discipline to hold hiring freeze |
| **3. Phased AI + Voluntary Exit Window (Late Yr 1)** | +5.0 to +6.5 | −5.5 to −7.0 *(adds voluntary packages)* | **−1.0 to +0.5** | **~+17.0 to +19.0** | Natural attrition + voluntary exits (~8–10 FTEs) if pilot proves capacity | Partially | Risk of losing top performers to voluntary package; still needs MBL alignment |

### View from Each Seat
- **Customer & Broker:** Option 1 risks delayed claims/broker payments and billing errors (similar to Klarna's 2024–2025 experience, where cost-first automation degraded service quality and forced a return to human hiring). Option 2 protects payment timeliness and frees staff to resolve complex broker/policyholder queries.
- **Finance & Audit:** Option 1 forces exits by LAS seniority rather than skill, risking the loss of IFRS 17/Solvency II specialists. Option 2 keeps control sign-off intact while cleaning up reconciliation backlogs.
- **Technology:** Option 1 requires a high-risk "big bang" integration across all three functions at once. Option 2 sequences AP and reconciliations first, proving data quality before touching reporting.
- **People:** Option 1 triggers anxiety, union friction, and elevated voluntary exits among remaining staff. Option 2 follows the Ingka/IKEA model: pair automation with a clear commitment that nobody loses their job *because* of AI, turning staff into co-designers of the new workflow.

---

## 5. Swedish Legal, Union & Regulatory Requirements

Any restructuring or AI deployment in Sweden must comply with the following legal floor (to be verified with HR and employment counsel before action):

1. **Co-determination Act (MBL):** Mandatory negotiation with relevant unions *before* making major operational or organisational changes—including introducing AI systems that materially alter work or staffing. Engaging unions at the problem stage improves design and speeds implementation (OECD, 2023).
2. **Employment Protection Act (LAS):** Redundancies for lack of work follow strict **seniority order (*turordning*)** per operational unit and collective agreement area (employers may exempt up to three employees since the 2022 reform, unless a union-agreed list is negotiated). **Management cannot simply select which 27 individuals leave.**
3. **Notice & Public Notification:**
   - **Arbetsförmedlingen:** Dismissing 26–100 employees requires formal advance notice of **at least 4 months**.
   - **Individual notice:** 1 to 6 months depending on length of service and collective agreement.
   - **Re-employment priority:** Dismissed employees with >12 months' service in the past 3 years hold a **9-month priority right** to re-employment.
4. **Transition Support (TRR & *Omställningsstudiestöd*):** Private-sector white-collar staff are covered by **TRR** (job security council), which provides coaching and transition support from day one of notice (helping over 85% of displaced Swedish workers into new jobs within a year, OECD 2015). Additionally, Sweden's public **transition study support** covers ~80% of salary (up to a ceiling) for upskilling, supporting internal or external transitions without forced layoffs.
5. **EU AI Act:** General AI transparency rules took effect in August 2026. Under Article 26(7) (deferred to **2 December 2027** by the 2026 Digital Omnibus), employers must formally inform workers' representatives and affected workers before deploying high-risk AI for task allocation or performance monitoring. **No AI tool may be used for individual productivity ranking.**

---

## 6. Phased Implementation Plan & Governance

Rather than committing to 27 exits today, we propose a gated 12-month programme:

| Phase | Timeline | Scope & Actions | People & Union Actions | Gate / Exit Criteria |
|---|---|---|---|---|
| **1. Prepare** | Months 1–2 | Map tasks (not jobs) in AP & Reconciliations; verify baseline hours, error rates, and ERP data readiness. | Open MBL dialogue with unions; announce "no forced layoffs from AI" for Year 1; invite frontline staff to co-design. | Baseline hours verified; union consultation complete; pilot scope signed off. |
| **2. Pilot** | Months 3–5 | Deploy AI matching/coding in AP (1–2 ledgers) with full human review; track *actual* hours freed net of review work. | Paid training time for pilot team; weekly feedback loops; no individual activity tracking. | Error rate ≤ baseline; net hours freed ≥ 15% in pilot scope; staff feedback positive. |
| **3. Expand** | Months 6–10 | Scale AP automation; roll out automated reconciliation matching; hold hiring freeze on routine backfills. | Begin reskilling 6–10 staff into analytics/claims-leakage/control roles; use natural attrition (~7 FTEs). | Close cycle time maintained or faster; audit trail verified by Internal Audit. |
| **4. Review & Decide** | Months 11–12 | Measure Year-1 P&L impact and quality; decide whether to hold Option 2 (attrition) or add Option 3 (voluntary exits) in Year 2. | Career 1:1s for all staff; joint review with unions on workload and engagement. | Board review of verified Year-1 savings before any Year-2 headcount targets are set. |

### Balanced Scorecard (Reviewed Monthly)
- **Financial:** Net cash impact vs. budget; external contractor/temp spend; cost per invoice/reconciliation.
- **Quality & Control:** Close cycle days; reconciliation break ageing; audit findings; AI error/override rate.
- **People:** Voluntary turnover among key specialists; sick-leave absence; team workload/engagement pulse.

---

## 7. Key Assumptions & Questions for the Board

**Key Assumptions (if these change, the recommendation changes):**
1. The company is solvent and profitable—this is an efficiency mandate, not a 90-day liquidity crisis.
2. Fully loaded FTE cost averages SEK 850k/yr, and natural attrition runs ~8%/yr (~7 FTEs/yr).
3. ERP and sub-ledger data in AP and Reconciliations are structured enough for AI matching without a multi-year core system replacement.

**Pre-Mortem — If this fails 12 months from now, why?**
- We automated messy upstream data, creating *more* reconciliation breaks for a smaller team.
- Key IFRS 17 / Solvency II specialists resigned due to restructuring uncertainty.
- We counted pilot "resolution rates" as FTE savings without deducting human review and exception handling.

**Questions for the Board:**
1. Is the primary goal a **SEK 12–19M/year cost-ratio improvement by Year 2**, or is there an unstated liquidity/capital pressure requiring cash in Year 1?
2. Which **unmet finance or risk work** (e.g., claims leakage, fraud detection, broker profitability) would the Board rather redeploy freed capacity into?
3. *What am I missing, and what would make this wrong?*
