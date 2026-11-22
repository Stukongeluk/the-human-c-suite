# AI in Finance and Back Office: Business Case 2027–2029

**Board paper, draft v0.1 for CFO review.** Prepared 21 November 2026.

**Status:** The method and the legal and regulatory facts have been checked. Most SEK figures rest on stated assumptions. Re-run them on actual payroll, attrition and process data before this goes to the board (Section 12).

**Tags used:** **[Verified]** means checked against a cited source. **[Medium]** means one source or a reasoned inference. **[Assumed]** means my assumption, to be replaced with your data.

---

## 1. Decision requested

The board is asked to:

1. **Approve a gated programme** to automate accounts payable (AP), reconciliations and reporting with AI. The 2027 budget is SEK 16.1m: SEK 12.0m one-off plus SEK 4.1m running costs. Only about SEK 2m is committed before Gate 0.
2. **Set the target as capacity, not as a headcount cut in 12 months.**
   - The target is at least 25% of the team's capacity released by end-2029, with a stretch target of 30% or more.
   - The 2027 hard targets are 8–9 roles removed (9–10%), mainly by not backfilling leavers, plus the measured capacity and quality KPIs in Section 10.
3. **Approve the stage gates and stop rules** in Section 9. Savings count only when a role has actually left the cost base.

The original ask was 30% of 90 roles (27 people) replaced by AI in 2027. It is modelled in full in Section 6.3. It costs more and delivers less than the recommended path in every scenario tested.

---

## 2. Summary

- **No version makes money in 2027.** The recommended path nets **−SEK 13.5m** in 2027. The 27-redundancy version nets **−SEK 30.3m**, because severance and the consultants covering work the tools cannot yet do outweigh the half-year of savings. [Assumed inputs; method shown in Appendix A]
- **27 roles in 2027 is not reached even in the upside.** The upside frees 18.8 FTE of capacity (21%) by end-2027, which converts to about 14 removable roles. The base case is 11.3 FTE of capacity and 8–9 roles. [Assumed]
  - External evidence points the same way. Gartner predicted that by 2026, 90% of finance functions would deploy at least one AI-enabled solution, "but less than 10% of functions will see headcount reductions". [Verified]
  - In AP, even best-in-class teams process only 49.2% of invoices touchless. [Verified]
- **Over five years the recommended path is worth more.** Five-year NPV at 8%:
  - Recommended path: **+SEK 4.9m** (base) and **+SEK 22.7m** (upside).
  - 27-redundancy version: **−SEK 24.7m** (base).
  - If the downside shows at Gate 1 and we stop, the recommended path's five-year loss is capped at about **−SEK 12.6m**. [Assumed]
- **Swedish law sets the timetable for any redundancy.**
  - MBL negotiation must come first, then at least 4 months' notice to Arbetsförmedlingen (varsel) for 26–100 affected staff, then 1–6 months' individual notice under LAS.
  - Selection is last in, first out (LIFO), with at most three exemptions.
  - Laid-off staff have priority for re-employment for 9 months after they leave.
  - So the first exits come mid-2027 at the earliest, and they will not be the people whose work was automated. [Verified; your collective agreement may change details]
- **The recommended path reaches about 22 roles (24%) by end-2029 in the base case and 30 roles (34%) in the upside.** It needs about one forced exit, because attrition and redeployment do most of the work. [Assumed: 8% attrition]

---

## 3. The proposal as tabled vs what the evidence supports

| The ask assumes… | What the evidence and the model show |
|---|---|
| 27 roles gone in 2027 | Base: 8–9 roles (11.3 FTE of capacity). Upside: about 14 roles. [Assumed] |
| SEK 23m saving next year (27 × SEK 0.85m average) | 2027 gross saving is at most SEK 10.3m, because exits fall from May to September. Net 2027 is −SEK 30.3m after severance, backfill and programme costs. [Assumed] |
| AI does the work | Even best-in-class AP still handles about half of invoices manually ([Ardent Partners](https://www.apexanalytix.com/resources/blog/ardent-partners-key-ap-metrics-2025/)). IFRS 17 and Solvency II reporting need human judgement and sign-off. [Verified / Medium] |
| We choose who leaves | LAS 22 § requires LIFO within each selection unit, with at most three exemptions ([LAS](https://data.riksdagen.se/dokument/sfs-1982-80.text)). [Verified] |
| Savings start in January | Exits cannot come sooner: MBL negotiation, then 4 months' varsel ([Arbetsförmedlingen](https://arbetsformedlingen.se/for-arbetsgivare/anmal-varsel-och-permittering)), then 1–6 months' notice ([LAS 11 §](https://data.riksdagen.se/dokument/sfs-1982-80.text)). [Verified] |
| If it doesn't work, we hire back | Re-employment priority runs for 9 months after a person leaves (LAS 25 §), so dismissed staff must be offered the jobs first. [Verified] |

Other companies have reversed AI cuts in public:

- **Klarna**, a Swedish company, said its AI could do the work of about 700 customer-service agents. It has since scaled back and is hiring human agents again.
- **Commonwealth Bank of Australia** cut 45 roles on the strength of an AI chatbot. Weeks later it rescinded the cuts and apologised ([ITPro](https://www.itpro.com/business/business-strategy/australias-biggest-bank-cut-staff-for-ai-then-it-backtracked-and-its-one-of-many-scrapping-plans-for-automated-customer-support-teams)). [Verified]

---

## 4. Baseline: the 90-person team and its cost

| Team | FTE | Avg monthly salary (SEK) [Assumed] | Loaded cost per FTE (SEK k) | Team cost (SEK m) |
|---|---:|---:|---:|---:|
| AP and supplier payments | 14 | 38,000 | 657 | 9.2 |
| Reconciliations and accounting operations | 22 | 45,000 | 778 | 17.1 |
| Reporting (IFRS 17/statutory, Solvency II, management, tax) | 22 | 57,000 | 986 | 21.7 |
| Other finance and back office (treasury, payroll, premium accounting, FP&A, controllers) | 32 | 52,000 | 899 | 28.8 |
| **Total** | **90** | | **853 avg** | **76.8** |

**Loaded cost formula:** monthly salary × 12.2 (includes holiday supplement) × (1 + 31.42% employer contributions + 3% other employment costs) + monthly salary × 12 × 6% pension × (1 + 24.26% special payroll tax on pensions).

- The 31.42% and 24.26% rates are the 2026 rates from [Skatteverket](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026). [Verified]
- The 6% pension rate and 3% other costs are [Assumed]. Replace them with your actual FTP/ITP costs.
- Worked example for AP: 38,000 × 12.2 = 463,600, and × 1.3442 = 623,171. Pension is 38,000 × 12 × 6% × 1.2426 = 33,997. The total is **SEK 657k**, about 1.44× annual base salary.

**Two conservative choices:**

- **The saving per role is below the team average.** Automatable work sits mostly in AP and reconciliations, the lowest-cost roles. Each role removed saves about SEK 0.74–0.81m, not the SEK 0.85m average.
- **No premises or overhead is counted as saved.** Those costs do not leave when one person does.

---

## 5. Where AI takes out work: process by process

| Process | What AI and automation can take | What stays human | Share of team hours freed: end-2027 (Downside / Base / Upside) | End-2029 (D / B / U) |
|---|---|---|---|---|
| **AP** (14 FTE) | Invoice capture, coding of non-PO invoices, 2/3-way matching, duplicate detection, first-line supplier queries | Exceptions, supplier master-data changes (a fraud control), payment approval (segregation of duties), disputes | 15% / 30% / 45% | 30% / 50% / 65% |
| **Reconciliations** (22 FTE) | Auto-matching of high-volume recs (bank, premium collections, claims payments), suggestions for resolving exceptions, commentary drafts | Reinsurance, intercompany and suspense-account investigations; sign-off | 8% / 20% / 35% | 25% / 40% / 55% |
| **Reporting** (22 FTE) | Data preparation, validation checks, cross-checks of Solvency II reporting templates (QRTs), drafts of variance commentary and disclosures | Judgement areas (IFRS 17 measurement, Solvency II technical provisions inputs), sign-off, contact with the regulator (FI) and auditors | 0% / 5% / 10% | 8% / 20% / 30% |
| **Other** (32 FTE) | Analysis copilots, payroll checks, cash forecasting support | Most of the work | 2% / 5% / 8% | 5% / 12% / 18% |
| **Total FTE-equivalent** | | | **4.5 / 11.3 / 18.8** (5% / 13% / 21%) | **13.1 / 24.0 / 33.6** (15% / 27% / 37%) |

All capacity percentages are [Assumed]. They are informed by the AP benchmarks above, but they are not measured. Gate 0 exists to replace them with measurements.

Reporting is slow on purpose. The first full annual cycle on the new tools is FY2027: the annual report plus Solvency II annual reporting in spring 2028. No reductions should be made in the reporting team before that cycle is done.

**From capacity to roles.** Freed time arrives in fragments spread across many people. It becomes a removable role only when work is pooled again. Conversion rates are 75% in 2027, 85% in 2028 and 90% in 2029. [Assumed]

| Roles removable (cumulative) | End-2027 | End-2028 | End-2029 |
|---|---:|---:|---:|
| Downside | 3.4 | 7.9 | 11.8 (13%) |
| Base | 8.5 | 15.7 | 21.6 (24%) |
| Upside | 14.1 | 22.7 | 30.2 (34%) |

---

## 6. Financial case

### 6.1 Programme costs (SEK m) [Assumed: replace with vendor quotes]

| | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| **One-off** | **12.0** | **4.0** | **2.0** |
| of which: AP automation implementation and integration | 2.5 | | |
| of which: reconciliation platform | 3.5 | | |
| of which: reporting data layer and GenAI tooling | 2.0 | | |
| of which: process redesign and data clean-up | 1.5 | | |
| of which: compliance and assurance (DORA third-party assessment and contracts, GDPR impact assessment (DPIA), auditor review of automated controls, AI literacy training) | 1.0 | | |
| of which: backfill for internal experts seconded to the programme | 1.0 | | |
| of which: change management and training | 0.5 | | |
| **Running: licences and AI usage** | 2.0 | 4.0 | 4.5 |
| **Running: 3 automation and controls roles at SEK 0.95m, from Q2 2027** (fill from internal staff where possible) | 2.1 | 2.85 | 2.85 |

There is no contingency line. The sensitivity table in 6.5 shows a 50% cost overrun instead.

### 6.2 Recommended path: automate first, shrink through attrition, gated (SEK m)

Figures are rounded to one decimal, so rows may not add exactly. Totals come from the unrounded model.

**Mechanics:**

- Roles leave mainly by not backfilling leavers and by redeployment within the group.
- Natural capacity is 90 × 8% attrition × 75% non-replaceable + 2 redeployments = **7.4 exits per year**. [Assumed]
- Any shortfall is closed with voluntary packages worth 9 months' loaded cost.
- Savings are counted as full-year for roles already gone and half-year for roles leaving in the current year.

**Downside first:**

| Downside | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| Roles removed (cumulative) | 3.4 | 7.9 | 11.8 |
| Savings | 1.2 | 4.3 | 7.7 |
| One-off | −12.0 | −4.0 | −2.0 |
| Running | −4.1 | −6.9 | −7.4 |
| Voluntary packages | 0.0 | 0.0 | 0.0 |
| **Net** | **−14.9** | **−6.5** | **−1.7** |
| Cumulative | −14.9 | −21.4 | −23.1 |

The run-rate from 2030 is only +SEK 1.8m a year. **This is why the stop rule exists.** If Gate 1 shows this path and wave 2 is cancelled, the five-year total is about −SEK 13m.

| Base | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| Roles removed (cumulative) | 8.5 | 15.7 | 21.6 |
| of which voluntary packages | 1.1 | 0.0 | 0.0 |
| Savings | 3.3 | 9.5 | 14.9 |
| One-off | −12.0 | −4.0 | −2.0 |
| Running | −4.1 | −6.9 | −7.4 |
| Voluntary packages | −0.6 | 0.0 | 0.0 |
| **Net** | **−13.5** | **−1.3** | **+5.6** |
| Cumulative | −13.5 | −14.8 | −9.2 |

Run-rate from 2030: **+SEK 10.0m a year** (21.6 roles × SEK 0.80m − SEK 7.35m running costs).

| Upside | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| Roles removed (cumulative) | 14.1 | 22.7 | 30.2 |
| of which voluntary packages | 6.7 | 1.2 | 0.1 |
| Savings | 5.5 | 14.6 | 21.3 |
| One-off | −12.0 | −4.0 | −2.0 |
| Running | −4.1 | −6.9 | −7.4 |
| Voluntary packages | −3.9 | −0.7 | −0.1 |
| **Net** | **−14.5** | **+3.0** | **+11.9** |
| Cumulative | −14.5 | −11.5 | +0.4 |

Run-rate from 2030: **+SEK 17.0m a year**.

### 6.3 The board's version: 27 redundancies in 2027 (SEK m)

**Mechanics:**

- 27 roles go, weighted to AP and reconciliations at SEK 0.76m each.
- Exits average mid-year, so 2027 gets 6 months of savings.
- A negotiated package of 6 months' pay is assumed. [Assumed: verify with labour counsel and against market practice]
- The programme is the same but compressed, with a 15% cost premium in 2027.
- The work the tools cannot yet do is covered by consultants at SEK 1.2m per FTE-year. [Assumed]

| With base-case automation | 2027 | 2028 | 2029 |
|---|---:|---:|---:|
| Gross saving | 10.3 | 20.5 | 20.5 |
| Severance packages | −10.3 | 0.0 | 0.0 |
| Backfill of work AI cannot yet do | −12.4 (10.3 FTE-yr) | −17.9 (14.9) | −10.0 (8.3) |
| One-off (compressed) | −13.8 | −4.0 | −2.0 |
| Running | −4.1 | −6.9 | −7.4 |
| **Net** | **−30.3** | **−8.2** | **+1.2** |
| Cumulative | −30.3 | −38.5 | −37.4 |

If the remaining 63 people absorb half of the gap instead of consultants, the five-year NPV improves to −SEK 2.7m. The extra workload then falls on a smaller team during the FY2027 year-end close, which is where quality risk is highest.

There is also a legal risk. Using consultants to do the same tasks after redundancies can invite a union challenge that the shortage of work was not genuine. [Medium: check with labour counsel]

### 6.4 Five-year comparison (2027–2031; 2030–31 held at the 2029 run-rate; NPV at 8%)

| Automation delivers… | Board version (27 redundancies in 2027) | Recommended path | Recommended is better by |
|---|---:|---:|---:|
| Downside | ≈ −58.7 (gap covered by consultants) | −18.1, or −12.6 if stopped at Gate 1 | ≈ +40 to +46 |
| Base | −24.7, or −2.7 if half the gap is absorbed | **+4.9** | +7.6 to +29.6 |
| Upside | +0.7 | **+22.7** | +22.0 |

The two paths spend the same on technology. The recommended path wins because it does not pay severance for exits that attrition would bring at no cost within three years. It also does not pay premium rates for work the tools cannot yet do.

### 6.5 Sensitivity: recommended path, base case, five-year NPV at 8% (SEK m)

| Capacity achieved vs base plan | One-off cost ×0.75 (13.5m) | ×1.0 (18m) | ×1.5 (27m) |
|---|---:|---:|---:|
| 60% | −9.5 | −13.5 | −21.6 |
| 80% | 0.0 | −4.0 | −12.1 |
| **100%** | 9.0 | **4.9** | −3.1 |
| 120% | 16.9 | 12.9 | 4.8 |

**Breakeven needs about 85–90% of base-plan capacity at the planned cost.** Capacity release is the number that decides this case, and nobody has measured it yet.

Attrition sensitivity:

- At **5%** attrition, base-case forced exits rise to about 5.5 over three years and NPV falls to +SEK 2.6m.
- At **11%** attrition there are no forced exits and NPV is +SEK 5.5m.

### 6.6 Not in the numbers (quantify before submission)

**Upside not counted:**

- Cuts in consultant and temporary staff in finance. This is often the first real cash saving and needs no redundancies.
- Faster close.
- Fewer post-close adjustments.
- Duplicate payments prevented.
- Early-payment discounts captured.
- Hiring avoided as premium volumes grow.

**Costs not counted:**

- Retention payments for about 10 critical IFRS 17 and Solvency II specialists.
- The productivity dip while processes change.
- Management time.
- A possible higher audit fee in year 1 for testing new automated controls.

---

## 7. Swedish legal and regulatory path

| Requirement | Rule | Effect |
|---|---|---|
| **Negotiate before deciding** | MBL primary negotiation duty. An employer with a collective agreement must call the union to negotiate *before* deciding on a major change to the business, or on changes to working conditions ([Företagarna](https://www.foretagarna.se/driva-eget-foretag/hrpersonalfragor/mbl-medbestammandelagen-vad-galler-for-dig-som-arbetsgivare/)). [Verified] | This applies to rolling out the AI tools themselves, not only to redundancies. Plan it into Q1 2027 either way. |
| **Varsel to Arbetsförmedlingen** | At least 2 months for 5–25 people, 4 months for 26–100 and 6 months for more than 100, counted to the first person's last day ([Arbetsförmedlingen](https://arbetsformedlingen.se/for-arbetsgivare/anmal-varsel-och-permittering)). [Verified] | 27 roles means at least 4 months. 25 or fewer means at least 2. |
| **Selection order** | LAS 22 §: LIFO within each selection unit (turordningskrets), with at most three exemptions. Collective agreements often allow a negotiated order instead ([LAS](https://data.riksdagen.se/dokument/sfs-1982-80.text), [verksamt.se](https://verksamt.se/en/employees-recruitment/termination-employment-notice-period/shortage)). [Verified] | The leavers will be the shortest-tenure staff. They are often the most digitally fluent, and they are not the people whose work was automated. |
| **Notice periods** | LAS 11 §: 1 month for under 2 years' service, rising to 6 months for 10 years or more. [Verified] | Exits spread from May to September 2027. |
| **Redeployment duty** | You must look at open vacancies the person is qualified for, and accept a reasonable training period. [Verified] | Vacancies elsewhere in the insurer must be offered first. |
| **Re-employment priority** | LAS 25 §: during notice and for 9 months after employment ends. [Verified] | If AI underdelivers, the dismissed staff get first right to the jobs until about mid-2028. |
| **DORA** | Applies since 17 January 2025, including ICT third-party risk and key contract terms for ICT services that support critical or important functions ([ESMA](https://www.esma.europa.eu/digital-operational-resilience-act-dora)). [Verified] | AI and SaaS vendors that support financial reporting are likely in scope. You need a pre-contract risk assessment, an entry in the register of information, contract clauses and an exit plan, and must keep FI informed as DORA requires. [Medium: CRO/CISO to confirm classification] |
| **GDPR** | Invoices and supplier records contain personal data. [Medium] | A DPIA is needed, plus data-residency terms with the vendors. |
| **EU AI Act** | Back-office finance uses are generally not high-risk. The AI-literacy duty (Article 4) applies already. [Medium] | Training is budgeted in 6.1. |
| **External audit and Solvency II governance** | New automated controls must be tested and relied on. FY2027 is the first annual cycle using them. [Medium] | No reductions in the reporting team before the FY2027 annual cycle is complete. |

**Timeline for the recommended path:**

| When | What |
|---|---|
| Dec 2026 | Board approves the gated programme. Vacancy control starts. Unions are informed. |
| Jan–Feb 2027 | **Gate 0:** time study, proof of value (PoV) on our own data, DORA assessment, DPIA, MBL negotiation on the change in working methods. |
| May–Jun 2027 | AP goes live, run in parallel through the June close. |
| Jul 2027 | **Gate 1:** capacity measured after the Q2 close. |
| Sep–Oct 2027 | Reconciliations go live through the Q3 close. Reporting tools are piloted on Q3. |
| Jan–Apr 2028 | FY2027 year-end close and annual report, plus Solvency II annual reporting, as the first full annual cycle on the new tools. |
| Apr 2028 | **Gate 2:** wave 2 decision and team redesign. If attrition is short of plan, voluntary packages are agreed through MBL. |

---

## 8. People plan (recommended path)

1. **Vacancy control now.** No role in the 90 is backfilled without CFO sign-off. Fixed-term and consultant contracts are not renewed where the work is being automated. Each role not backfilled saves SEK 0.66–0.99m a year. This is the cash-management principle of a hiring freeze: immediate effect, and nobody is laid off.
2. **No forced redundancies because of AI in 2027.** Agree this in the MBL process in exchange for co-operation on process change.
   - It is cheap. In the base case it covers about 1 forced exit (SEK 0.6m). In the upside, the people affected can staff wave 2.
   - It protects what the programme depends on: the experts who know the exceptions must stay to configure and test the tools.
3. **Reskill and redeploy first.**
   - Fill the 3 automation and controls roles internally.
   - Offer vacancies in claims, finance analytics and compliance before any package.
4. **Involve the people who do the work in Gate 0 and in the process design.** Make teams accountable for both the time they save and where that time goes. Gartner's [Nov 2026 guidance to CFOs](https://www.gartner.com/en/newsroom/press-releases/2026-11-04-gartner-idnetifies-three-steps-for-cfos-to-turn-ai-time-saavings-into-business-value) says the same: build redeployment of saved time into performance management. [Verified]
5. **Message discipline.** Say "We will automate AP and reconciliations, we will not refill roles where the work is gone, and nobody loses their job to AI in 2027." Do not say "AI will replace 30%".

---

## 9. Stage gates and stop rules

| Gate | When | Pass criteria [Assumed thresholds: confirm] | If it fails |
|---|---|---|---|
| **Gate 0: proof of value** | End Feb 2027 | AP at least 60% touchless on 3 months of our own invoices. Top-10 high-volume reconciliations at least 80% auto-matched. Error rate no worse than today. Baseline time study complete. | Stop at about SEK 2m spent, or go ahead with AP only. |
| **Gate 1: production** | Jul 2027, after the Q2 close | Measured capacity at least 70% of the base plan in AP and reconciliations. No material close errors. Auditor comfortable with the design of the automated controls. | Below 50% of plan: cancel wave 2 and keep AP. This caps the five-year downside at about −SEK 13m. |
| **Gate 2: scale** | Apr 2028, after the FY2027 annual cycle | Capacity at or above plan across waves. Close quality stable. Attrition on track. | Resize wave 2. Hold any structural team changes. |

---

## 10. KPIs for the board each quarter

- Capacity released (FTE-equivalent, measured) vs plan. Roles removed, split by route: not backfilled, redeployed, voluntary package, forced.
- Cash savings booked (roles actually gone only) vs programme spend to date.
- AP: touchless rate, cost per invoice, duplicate payments caught.
- Reconciliations: auto-match rate, unreconciled items older than 30 days.
- Close: working days to close (month, quarter, year), post-close adjustments, audit findings.
- AI quality: override rate, errors found in review.
- People: voluntary attrition among critical-skill staff, internal redeployments, reskilling completed.

---

## 11. Top risks

| Risk | Trigger | Consequence | Mitigation |
|---|---|---|---|
| Capacity below plan | Gate 1 below 70% | At 60% of plan, five-year NPV is −SEK 13.5m | Gate 0 PoV on our own data; stop rule at Gate 1 |
| Close or reporting error during the transition | New tools in the Q3 2027 and FY2027 closes | Findings from FI or the auditor; restatement | Parallel runs; no reporting-team cuts before the FY2027 annual cycle is done |
| Key-person flight | Announcement worded as "AI replaces X%" | Loss of IFRS 17 and Solvency II know-how just when it is needed | Message discipline, the 2027 job-security commitment, targeted retention |
| Delay from DORA, GDPR or audit work | Vendor contract misses DORA requirements | One quarter of delay roughly halves 2027 savings | Run the assessments in Gate 0, in parallel with the PoV |
| Freed time not converted into savings | Capacity rises but roles do not fall | Programme cost with no saving | Vacancy control; time savings and their redeployment tracked as KPIs |
| Vendor concentration or lock-in | One platform covering AP and reconciliations | Exit cost; DORA exit-plan findings | Exit plan in the contract; data portability |

---

## 12. Before submission: replace these assumptions

| Data | Owner | By |
|---|---|---|
| Payroll by team: salary, pension plan, employment costs | Head of HR | 11 Dec 2026 |
| Attrition over 36 months, age profile, retirements due 2027–29 | Head of HR | 11 Dec 2026 |
| Volumes: invoices a year, % PO-backed, current touchless rate; number of reconciliations and current auto-match rate; close calendar; manual journals | Head of Accounting / Finance Operations | 11 Dec 2026 |
| Current tools and contracts. If AP automation is already in place, AP upside is smaller. | CIO | 11 Dec 2026 |
| Finance consultant and temp spend, last 12 months | Financial Controller | 11 Dec 2026 |
| Review of the plan against the collective agreement: selection order, packages, MBL | General Counsel + labour counsel | 18 Dec 2026 |
| DORA classification of finance processes and vendors | Chief Risk Officer + CISO | 18 Dec 2026 |
| Indicative vendor quotes for the 6.1 cost lines | CIO + Procurement | 18 Dec 2026 |

---

## Appendix A: Method and formulas

- **Loaded cost per FTE:** m × 12.2 × (1 + 0.3142 + 0.03) + m × 12 × 0.06 × (1 + 0.2426), where m is monthly salary.
- **Capacity (FTE) in year y:** Σ (team FTE × share of hours freed in year y).
- **Roles removable in year y:** capacity in year y × conversion rate (0.75, 0.85, 0.90).
- **Natural exits per year:** 90 × attrition rate × non-replaceable share + redeployments = 90 × 0.08 × 0.75 + 2 = 7.4.
- **Forced exits in year y:** max(0, new roles in year y − natural exits).
- **Savings in year y:** roles at end of year y−1 × weighted cost + new roles in year y × weighted cost × 0.5. The weighted cost is the cost of the roles freed, by team mix: SEK 0.74–0.81m.
- **Packages:** forced exits × weighted cost × 9/12.
- **Net:** savings − one-off − running − packages.
- **Board version:**
  - Savings: 27 × SEK 0.76m × (6/12 in 2027, full year after).
  - Severance: 27 × 0.76 × 6/12.
  - Backfill: (27 − roles the AI covers on average in the period) × SEK 1.2m. In H2 2027, roles covered are taken as 75% of the end-2027 level.
- **Five-year view:** 2030–31 held at the 2029 exit run-rate, with no further gains. NPV is at 8%, discounting each year from 2027 as year 1.
- **Conservative choices:**
  - Savings count only when roles leave.
  - The saving per role uses the lower-cost team mix, not the average.
  - No overhead is counted as saved.
  - Downside is shown first.

## Appendix B: Sources

- Gartner (Sept 2024), 90% of finance functions to deploy AI by 2026, less than 10% to see headcount reductions: [gartner.com](https://gartner.com/en/newsroom/press-releases/2024-09-12-gartner-predicts-that-90-percent-of-finance-functions-will-deploy-at-least-one-ai-enabled-tech-solution-by-2026)
- Gartner (Mar 2025), CFOs should reset expectations on AI productivity and headcount and question assumed savings in AI business cases: [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2025-03-25-gartner-says-cfos-should-reset-expectations-about-ais-impact-on-workforce-productivity-and-headcount)
- Gartner (Nov 2026), 23% of functional leaders report AI-related headcount reductions and 17% report increases; three steps for turning saved time into value: [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2026-11-04-gartner-idnetifies-three-steps-for-cfos-to-turn-ai-time-saavings-into-business-value)
- Ardent Partners AP metrics 2025 (touchless 32.6% average, 49.2% best-in-class; cost per invoice USD 9.40 average, 2.78 best-in-class): [apexanalytix.com](https://www.apexanalytix.com/resources/blog/ardent-partners-key-ap-metrics-2025/)
- LAS (SFS 1982:80), sections 11, 22 and 25: [riksdagen.se](https://data.riksdagen.se/dokument/sfs-1982-80.text)
- Arbetsförmedlingen, varsel lead times: [arbetsformedlingen.se](https://arbetsformedlingen.se/for-arbetsgivare/anmal-varsel-och-permittering)
- Verksamt.se, termination due to shortage of work: [verksamt.se](https://verksamt.se/en/employees-recruitment/termination-employment-notice-period/shortage)
- Företagarna, MBL primary negotiation duty: [foretagarna.se](https://www.foretagarna.se/driva-eget-foretag/hrpersonalfragor/mbl-medbestammandelagen-vad-galler-for-dig-som-arbetsgivare/)
- Skatteverket, 2026 rates (employer contributions 31.42%, special payroll tax on pensions 24.26%): [skatteverket.se](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026)
- ESMA, DORA applies from 17 January 2025, ICT third-party risk: [esma.europa.eu](https://www.esma.europa.eu/digital-operational-resilience-act-dora)
- ITPro, Commonwealth Bank of Australia and Klarna reversals: [itpro.com](https://www.itpro.com/business/business-strategy/australias-biggest-bank-cut-staff-for-ai-then-it-backtracked-and-its-one-of-many-scrapping-plans-for-automated-customer-support-teams)
