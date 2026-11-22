# AI in finance and back office: a gated case for 2027–2031

**Board paper, draft for CFO review** · Prepared November 2026 · All amounts in SEK million unless stated

> Every figure in this paper is an **estimate** scaled to a 90-person team. It is built so that each estimate can be replaced with our own data (payroll aggregates, activity sampling, invoice and reconciliation volumes, vendor quotes, HR attrition data) before the board decides. The model behind every table is in `business_case_model.py`; each table adds up and was computed there.

---

## 1. Recommendation

**Approve a gated AI programme that frees capacity first and reduces headcount only through vacancies and voluntary internal moves; do not approve a 30% redundancy target for 2027.**

- AI can take on an estimated **11% of the team's hours by the end of 2027** (range 6–16%) and **about 25% at maturity in 2029** (range 13–36%). 30% is at the top of the range at maturity, not a 2027 outcome.
- **No version of this saves money in 2027.** The recommended route costs about **SEK 13.5m in 2027** and returns **about SEK 13.6m net over five years** (NPV +7.7m at 8%), paying back in 2030. Finance headcount falls from 90 to about **75 by end-2029** with no redundancies.
- Cutting 27 roles in 2027 alongside the rollout costs about **SEK 36m in 2027** and is **SEK 10.7m negative over five years**, because Swedish negotiation and notice rules move the exits into the second half of the year, severance comes first, and the AI is not yet doing the work those people did.

**Decisions asked of the board**
1. Release SEK 13.5m for 2027 in stages: about SEK 6m for the pilot half-year, the rest only if Gate 1 is passed.
2. Approve the gates and their criteria (section 7) now, before any results are known.
3. Agree that 2027 carries no redundancies because of AI, and that any later headcount step is decided at Gate 2 (October 2027) on measured results.

---

## 2. What the board asked, and the problem we are solving

The board asked for a case showing that AI can replace 30% of the 90-person finance and back-office team (accounts payable, reconciliations, reporting) next year. In money terms, the slide version of that ask is 27 roles × SEK 0.86m = **SEK 23m a year**.

That is a target, not yet a diagnosis. The right instrument depends on what the 30% is meant to achieve:

| If the real goal is… | Then the right answer is… |
|---|---|
| A long-term lower expense ratio and a more resilient finance function | This paper: a measured capacity programme, headcount through flows |
| A SEK figure in the 2027 plan | AI is not the 2027 lever under any option (section 5). Faster 2027 levers sit elsewhere: non-payroll spend in finance (consultants for reporting, legacy licences), claims leakage, pricing. Not sized here |
| A signal to owners that we are using AI seriously | A credible, gated programme with published measures is a stronger signal than a headcount number we would later have to walk back |

**Open questions that change the numbers most:** what the 30% must achieve and whether 2027 is a hard date; and the team's actual attrition, tenure and age profile.

---

## 3. What we know and what we have assumed

| Topic | Status |
|---|---|
| Organisation | Mid-sized Swedish insurer, supervised by Finansinspektionen under Solvency II; DORA applies. **Ownership not stated** (customer-owned, listed or part of a group): it changes how the board should weigh a 2027 number against long-term value |
| Team | 90 FTE across AP, reconciliations and close, external and regulatory reporting, management reporting, and other back office. **Split by area is an estimate** (section 4) |
| Cost per FTE | **Estimate:** average monthly salary SEK 48,000; on-costs from SCB's labour cost statistics for white-collar staff in finance and insurance (August 2025: total labour cost SEK 98,842 a month on wages of SEK 66,159, a factor of 1.49). Result: **SEK 0.86m per FTE-year**, team payroll SEK 77.4m |
| Attrition | **Estimate:** 9% a year (voluntary leavers plus retirements). Sensitivity: 6% and 12% |
| Unions and agreements | **Not stated.** Assumed: sector collective agreements and union clubs, so MBL negotiations apply. Earlier reorganisations and how they went: unknown |
| Systems | **Not stated:** ERP, AP platform, reconciliation tooling, invoice volumes, e-invoice share, close calendar |

**Data that would replace the estimates:** payroll in aggregate by team (HR/payroll system); four weeks of team-level activity sampling; invoice volumes, touchless rate and exception rate (AP system); reconciliation counts and auto-match rate; close days and manual journal count (ERP); attrition, tenure and age profile in aggregate (HRIS); open roles elsewhere in the company for 2027–28 (recruitment plan); vendor quotes and the integration estimate (IT).

---

## 4. Where the work is, and what AI can take on

Costs follow activities, not headcount. The sizing below is by task area. The share of hours AI can take on means **at the quality we need today, net of the human review its output still requires**, and has to be measured in our own pilots.

| Area | FTE (est.) | Share of hours AI can take on at maturity: low–high (base) | Net FTE-equivalent freed, after review: low / base / high | Wave |
|---|---|---|---|---|
| Accounts payable and supplier data | 16 | 35–65% (50%) | 3.6 / 6.0 / 8.3 | 1 |
| Reconciliations and close | 22 | 30–60% (45%) | 4.3 / 7.4 / 10.6 | 1 |
| External and regulatory reporting | 18 | 10–30% (20%) | 1.2 / 2.7 / 4.3 | 2 |
| Management reporting and analysis | 12 | 20–40% (30%) | 1.6 / 2.7 / 3.8 | 2 |
| Payments, collections, other back office | 22 | 10–30% (20%) | 1.4 / 3.3 / 5.3 | 2 |
| **Total** | **90** | | **12.1 / 22.1 / 32.3** (13% / 25% / 36%) | |

Review and exception handling takes back 35% / 25% / 20% of automated hours in the low / base / high case (estimate).

**Basis for these ranges (estimates, to be replaced by pilot results):**
- Invoice capture, coding and matching, and high-volume reconciliation matching, are the most mature uses; McKinsey estimated in 2018 that current technologies could fully automate 42% of finance activities and mostly automate another 19%, concentrated in transactional work. That is technical potential, not captured savings.
- Exceptions stay human: in Ardent Partners' 2025 benchmark the average AP exception rate was 18.4%.
- Regulatory reporting (Solvency II QRTs, SFCR/RSR, statutory and IFRS reporting) is mostly data pipelines, judgement and named accountability; AI helps with validation and first drafts of narrative, and the reviewer stays.
- Base rates: about 95% of enterprise generative AI pilots showed no measurable P&L impact in MIT NANDA's 2025 study (methodology criticised; read it as direction), and Gartner expects over 40% of agentic AI projects to be cancelled by end-2027. That is why the plan pays only for measured results.

**Capacity freed over time** (FTE-equivalent, quarter average; wave 1 starts in Q2 2027, wave 2 in Q3 2027):

| Case | Q4 2027 | Q4 2028 | Q4 2029 | Maturity |
|---|---|---|---|---|
| Low | 5.8 (6%) | 9.8 (11%) | 11.9 (13%) | 12.1 (13%) |
| Base | 10.2 (11%) | 17.7 (20%) | 21.7 (24%) | 22.1 (25%) |
| High | 14.7 (16%) | 25.7 (29%) | 31.6 (35%) | 32.3 (36%) |

Three of these FTE-equivalents are needed to run the tools: a small finance automation and AI controls team, staffed from the existing team.

---

## 5. Options, costed on the same basis

All options that use AI carry the same programme cost (estimate; vendor quotes needed): licences and usage about SEK 3m a year at run-rate, integration and data work SEK 7.5m in 2027 and SEK 2m in 2028, controls and assurance SEK 1.5m in 2027 and SEK 0.5m a year after, tool training SEK 1m in 2027. Effects are against today's cost base with flat volumes; wage drift affects every option equally and is left out.

- **A. Do nothing.** No programme cost, no saving: 0 by definition. Forgoes an estimated SEK 2–17m a year of net benefit from 2030, and leaves the team more exposed to retirements and rising volumes.
- **B. The board's ask as stated:** 27 redundancies decided in 2027 alongside the AI rollout.
- **C. Recommended: capacity first.** Hiring freeze with exceptions (30% of leavers in critical roles still replaced), vacancies left open only where measured AI capacity covers the work, voluntary moves into open roles elsewhere, 15% of freed capacity kept for quality and a faster close, and a paid learning budget.
- **D. C plus one redundancy round in 2028,** sized at the October 2027 gate to bring forward reductions that attrition would otherwise deliver later.

### Summary (base case)

| | 2027 | 2028 | 2029 | 5 years (2027–31) | NPV at 8% | Finance headcount end-2027 / 2029 | Redundancies |
|---|---|---|---|---|---|---|---|
| A. Do nothing | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 90 / 90 | 0 |
| B. 27 redundancies in 2027 | −36.3 | −3.6 | 8.6 | −10.7 | −15.8 | 63 / 71 (after rehiring 8) | 27 |
| **C. Capacity first (recommended)** | **−13.5** | **0.5** | **7.9** | **13.6** | **7.7** | **86 / 75** | **0** |
| D. C plus a 2028 round | −13.9 | −1.6 | 7.7 | 10.4 | 4.9 | 86 / 75 | 2 |

### Across the three capacity cases

| Case | B: 2027 / 5 yr / NPV | C: 2027 / 5 yr / NPV | D: 2027 / 5 yr / NPV | Headcount end-2029 B / C / D | Redundancies B / C / D |
|---|---|---|---|---|---|
| Low | −38.9 / −45.1 / −43.4 | −14.3 / −12.5 / −12.9 * | −14.3 / −12.5 / −12.9 | 81 / 83 / 83 | 27 / 0 / 0 |
| Base | −36.3 / −10.7 / −15.8 | −13.5 / 13.6 / 7.7 | −13.9 / 10.4 / 4.9 | 71 / 75 / 75 | 27 / 0 / 2 |
| High | −33.7 / 21.1 / 10.0 | −13.1 / 31.0 / 20.9 | −13.6 / 27.8 / 17.8 | 63 / 69 / 66 | 27 / 0 / 10 |

\* In the low case the gates would stop or shrink option C after the pilot, limiting the loss to about SEK 6m (the H1 2027 cost). The table shows the cost of running it to completion anyway.

**In none of the nine cases does a redundancy round beat the capacity route over five years.** Option B matches option C only if the AI could take on about 48% of the team's hours at maturity and about 20 FTE-equivalents by the end of 2027: 1.35 times our high case.

### Option B in detail (base case)

| Line | Q1 27 | Q2 27 | Q3 27 | Q4 27 | 2027 | 2028 | 2029 | 2030 | 2031 | 5 years |
|---|---|---|---|---|---|---|---|---|---|---|
| Gross payroll saving (from each actual exit date) | 0.0 | 0.4 | 1.9 | 4.2 | 6.5 | 20.9 | 20.9 | 20.9 | 20.9 | 90.1 |
| Severance packages incl. employer contributions | 0.0 | −1.5 | −4.5 | −4.2 | −10.2 | 0.0 | 0.0 | 0.0 | 0.0 | −10.2 |
| Outplacement top-up | 0.0 | −0.2 | −0.5 | −0.4 | −1.1 | 0.0 | 0.0 | 0.0 | 0.0 | −1.1 |
| Counsel, HR project, negotiations | −0.8 | −0.8 | 0.0 | 0.0 | −1.5 | 0.0 | 0.0 | 0.0 | 0.0 | −1.5 |
| Work still to be done: contractors and temporary cover | −0.4 | −5.7 | −5.6 | −6.0 | −17.6 | −9.5 | −1.7 | 0.0 | 0.0 | −28.8 |
| Rehiring: recruitment, ramp-up and rehired payroll | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | −9.2 | −6.9 | −6.9 | −6.9 | −29.8 |
| Extra voluntary attrition (replacement cost) | 0.0 | 0.0 | −0.2 | −0.2 | −0.4 | −0.4 | 0.0 | 0.0 | 0.0 | −0.8 |
| AI programme | −1.9 | −2.5 | −4.2 | −3.2 | −12.0 | −5.5 | −3.7 | −3.7 | −3.7 | −28.6 |
| **Net effect vs. today** | **−3.1** | **−10.3** | **−13.1** | **−9.9** | **−36.3** | **−3.6** | **8.6** | **10.3** | **10.3** | **−10.7** |

Why option B costs more than the slide suggests:
- **The Swedish process moves the savings.** MBL negotiations come before the decision; notifying 26–100 dismissals to Arbetsförmedlingen requires four months' notice before they take effect; LAS notice periods run from one to six months by length of service. Assumed timeline: notification and negotiations February–March, notices in April, exits June to October. Pay continues to each exit date, and half of those on notice are assumed to be released from work.
- **The AI is not doing the work yet.** In the base case it covers about 10 FTE-equivalents by Q4 2027 against 27 people gone and 3 running the tools: a gap of about 17 FTE-equivalents, covered by contractors at about SEK 850 an hour. That gap peaks at the year-end close and the annual Solvency II reporting in Q1 2028.
- **We cannot choose who leaves.** LAS sets the selection order by length of service per operational unit and collective agreement area (three exemptions per employer), so the people leaving are the most recently hired, not the ones whose tasks were automated. Agreeing a different list with the unions usually costs larger packages. Before any dismissal we must also offer suitable vacant roles (redeployment duty).
- **The AI never frees 27 FTE in the base case** (22 at maturity, minus 3 to run it), so about 8 roles are refilled in 2028. People dismissed for redundancy generally have priority for re-employment for nine months, so those roles go first to the people we let go.
- **People we want to keep leave next.** Trevor and Nyberg (2008) found a 1% downsizing associated with 31% more voluntary turnover the following year; we assume a far more modest rise (from 9% to 13.5% for a year) rather than extrapolate. Surveys of companies that cut jobs because of AI point the same way: in Orgvue's 2025 survey 55% of leaders who made AI redundancies said they had made the wrong decisions, and in Careerminds' 2026 survey two in three were already rehiring (both vendor surveys; read them as a signal).

Sensitivity: if the remaining team absorbed a third of the gap through overtime or dropped work, option B would still cost about SEK 30m in 2027 and be roughly break-even (−1.1) over five years in the base case.

### Option C in detail (base case, recommended)

| Line | Q1 27 | Q2 27 | Q3 27 | Q4 27 | 2027 | 2028 | 2029 | 2030 | 2031 | 5 years |
|---|---|---|---|---|---|---|---|---|---|---|
| Gross payroll saving (vacancies left open, internal moves) | 0.0 | 0.0 | 0.2 | 0.6 | 0.8 | 7.3 | 12.2 | 13.6 | 13.6 | 47.6 |
| Temporary cover while the automation team starts | −0.4 | −0.7 | 0.0 | 0.0 | −1.0 | 0.0 | 0.0 | 0.0 | 0.0 | −1.0 |
| AI programme | −1.9 | −2.5 | −4.2 | −3.2 | −12.0 | −5.5 | −3.7 | −3.7 | −3.7 | −28.6 |
| Learning budget, reskilling and redeployment | −0.3 | −0.3 | −0.3 | −0.3 | −1.3 | −1.3 | −0.6 | −0.6 | −0.6 | −4.4 |
| **Net effect vs. today** | **−2.6** | **−3.5** | **−4.4** | **−3.0** | **−13.5** | **0.5** | **7.9** | **9.3** | **9.3** | **13.6** |

Headcount: 90 → 86 (end-2027) → 78 (end-2028) → 75 (end-2029) → 74 (end-2031), through about 11–12 leavers not replaced and about 4 voluntary moves into open roles elsewhere. Cumulative effect turns positive in Q3 2030 (base), Q1 2030 (high). Option C is self-limiting: a vacancy stays open only when measured capacity covers the work, so if the AI underdelivers the saving shrinks but no service gap opens.

### Option D in detail (base case)

| Line | Q1 27 | Q2 27 | Q3 27 | Q4 27 | 2027 | 2028 | 2029 | 2030 | 2031 | 5 years |
|---|---|---|---|---|---|---|---|---|---|---|
| Gross payroll saving | 0.0 | 0.0 | 0.2 | 0.6 | 0.8 | 7.7 | 12.1 | 13.4 | 13.4 | 47.4 |
| Severance packages incl. employer contributions | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | −0.8 | 0.0 | 0.0 | 0.0 | −0.8 |
| Outplacement top-up | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | −0.1 | 0.0 | 0.0 | 0.0 | −0.1 |
| Counsel, HR project, negotiations | 0.0 | 0.0 | 0.0 | −0.4 | −0.4 | −0.4 | 0.0 | 0.0 | 0.0 | −0.9 |
| Work still to be done: contractors and temporary cover | −0.4 | −0.7 | 0.0 | 0.0 | −1.0 | −0.8 | 0.0 | 0.0 | 0.0 | −1.8 |
| Extra voluntary attrition (replacement cost) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | −0.3 | −0.1 | 0.0 | 0.0 | −0.5 |
| AI programme | −1.9 | −2.5 | −4.2 | −3.2 | −12.0 | −5.5 | −3.7 | −3.7 | −3.7 | −28.6 |
| Learning budget, reskilling and redeployment | −0.3 | −0.3 | −0.3 | −0.3 | −1.3 | −1.3 | −0.6 | −0.6 | −0.6 | −4.4 |
| **Net effect vs. today** | **−2.6** | **−3.5** | **−4.4** | **−3.4** | **−13.9** | **−1.6** | **7.7** | **9.1** | **9.1** | **10.4** |

A 2028 round brings exits forward by a year or so, but attrition and internal moves would absorb the same capacity soon after. It buys time, not savings, which is why it is a decision for Gate 2 on measured data, not for now.

---

## 6. Sensitivities and what would change the recommendation

| Assumption | Change | Effect |
|---|---|---|
| Attrition | 6% / 12% instead of 9% | Option C five-year net 12.2 / 14.1 (base 13.6); headcount end-2029 unchanged at 75, because measured capacity, not attrition, is the binding limit |
| Capacity kept for quality | 0% instead of 15% | Option C five-year net 22.6, headcount end-2029 71; the board's choice, at the cost of a slower close and thinner controls |
| AI programme cost | −30% / +30% | Option C five-year net 22.1 / 5.0; option B −2.1 / −19.3 |
| Option B work gap | A third absorbed by overtime or dropped work | Option B 2027 about −30; five years −1.1 (base), +30.0 (high, against C's 31.0) |
| Capacity | Low / high case | See section 5: the ranking does not change |

**What would change my recommendation:**
- Pilot results at or above the high case together with attrition well below 6%: capacity would then outrun what vacancies and moves can absorb, and a small voluntary programme in 2028 (option D, voluntary first) becomes worth costing at Gate 2.
- Vendor quotes far below the estimates, or existing licences we can reuse: the case improves; the ranking does not change.
- A hard 2027 cost commitment: AI cannot meet it under any option, and the paper would need different 2027 levers.

**Not counted, as upside:** hires avoided if volumes grow; faster close and fewer errors; no-regret moves any option can take (stop reports nobody reads, require e-invoices from suppliers, clean supplier master data, cut manual journals), which also make the AI work better.

---

## 7. The plan and its gates

Criteria are fixed and minuted before any results are known, with internal audit confirming the measurement.

| When | What happens | Gate criteria (illustrative; to be agreed) |
|---|---|---|
| Dec 2026–Feb 2027 | Baseline: four weeks of team-level activity sampling, volumes, error rates, close days, cost per invoice. MBL information and negotiation on introducing the tools; joint working group with union representatives. Vendor selection with DORA due diligence. Compliance assesses whether anything counts as outsourcing an important function | Baseline signed off by internal audit |
| Mar–Jun 2027 | Pilots: AP (capture, coding, matching) and reconciliations (bank and one sub-ledger) | **Gate 1 (end June):** scale if ≥25% of pilot-scope hours are freed net of review, with error rates no worse than baseline and no control findings; rescope at 15–25%; stop below 15% (sunk cost about SEK 6m) |
| Jul–Dec 2027 | Scale AP and reconciliations; start reporting pilots (data validation, first-draft commentary) | **Gate 2 (October, before the 2028 budget):** measured run-rate capacity sets the 2028 headcount plan. Base expects about 8 FTE-equivalents from wave 1 by Q4. This is where a headcount number becomes a commitment |
| 2028 | Wave 2 at scale | **Gate 3 (mid-2028):** reporting use cases; the medium-term range becomes a commitment |

**How freed capacity is used, in this order:** (1) quality and controls, a faster close, backlog (15%); (2) the three-person automation and AI controls team; (3) vacancies left unfilled, with exceptions for critical skills; (4) voluntary moves into open roles elsewhere in the company; (5) only if capacity still exceeds what these absorb, a voluntary programme, costed and negotiated, decided by the board at a gate.

**Controls we keep:** a person approves anything that moves money or posts to the ledger; segregation of duties; full audit trails for AI-prepared reconciliations and postings (bookkeeping and archiving rules apply); payment checks against duplicate and fraudulent invoices; supplier payment terms kept, small suppliers paid on time. The external auditor and the audit committee are briefed before go-live.

**Incentives:** no management target for headcount removed. Programme targets are capacity freed (measured), close days, error rates and audit findings, and regretted attrition.

**AI spend:** one owner, a budget with alerts, monthly review of active use against licences paid.

---

## 8. People

| Who | What changes | What we do |
|---|---|---|
| All 90 | Their work changes; nobody is dismissed because of AI in 2027 | Paid learning time and a learning budget; career conversations in Q1 2027; measurement by process and team, never by individual |
| AP and reconciliations (about 38) | The largest change: from keying and matching to exceptions, supplier contact, controls and automation | Training before go-live; old and new ways run side by side for a period; a named owner per team and a place to raise problems |
| About 11–12 leavers by 2031 | Their roles are not refilled where the AI covers the work | Normal leaving; no pressure to leave |
| About 4 internal moves, 3 into the automation team | New roles | Voluntary, with training (SEK 50,000 per move budgeted) |

- **Decide with the unions, not about them.** Bring union representatives in under MBL now, at the design stage, while they can still change the plan. The OECD finds that AI adoption tends to turn out better for workers where their representatives are consulted.
- **Protect the person.** For anyone who later chooses to leave or retrain, Sweden's job security councils step in from the day of notice (over 85% of displaced Swedish workers found new work within a year in the OECD's review, in a strong labour market), and transition study support (omställningsstudiestöd) pays about 80% of salary up to a ceiling for up to about a year of study.
- **Communicate honestly.** Staff should hear the plan from their own managers, with the real numbers and what is still open. Do not circulate "30%": the people with the most options leave first.
- **Promise only what we can keep:** no redundancies because of AI in 2027, and any later step decided on measured evidence with the unions. Not "never".

---

## 9. Law, regulation and assurance

This is not legal advice; employment counsel, compliance and the external auditor need to confirm each point.

- **Employment law:** MBL (SFS 1976:580) requires negotiation before major changes, including new systems that change how work is done and any reorganisation. LAS (SFS 1982:80): objective grounds, redeployment duty, selection order, notice of one to six months, nine-month re-employment priority. Notification of dismissals to Arbetsförmedlingen (SFS 1974:13): two, four or six months ahead for 5–25, 26–100 or more than 100 people. The sector collective agreements may add terms.
- **Finansinspektionen and Solvency II:** the system of governance and internal control apply to AI-supported processes; outsourcing critical or important functions requires notifying FI in advance (Solvency II, Article 49). Compliance should assess each vendor arrangement.
- **DORA (Regulation (EU) 2022/2554, applying since 17 January 2025):** AI vendors are ICT third-party providers: register of information, contract terms, exit plans and ICT risk management.
- **EIOPA's Opinion on AI governance and risk management (6 August 2025):** for AI systems that are neither prohibited nor high-risk, expects proportionate data governance, record-keeping, fairness, cyber security, explainability and human oversight. We adopt it as our standard.
- **EU AI Act:** finance back-office uses are generally not high-risk. Using AI to allocate tasks to, monitor or evaluate staff would be, with a duty to inform workers' representatives and the affected workers before use from 2 December 2027; this plan does not do that.
- **GDPR:** invoices and supplier records contain personal data; data protection impact assessment where needed; vendor data location and model-training terms checked.

---

## 10. What the board will see each quarter

| Money | Capacity and quality | People |
|---|---|---|
| Net programme effect against this plan | Hours freed (measured) by area | Regretted attrition |
| AI spend against budget; active use against licences | Touchless invoice rate, exception rate, auto-match rate | Engagement pulse in the affected teams |
| Contractor spend in finance | Close days, manual journals, errors and audit findings | Sickness absence |
| Cost per invoice | Regulatory reporting on time; suppliers paid on time | Internal moves, training days |

---

## 11. The board's view, fairly stated

The board is right on the essentials: AI in invoice processing and reconciliation is real and maturing, peers are moving, the expense ratio matters, and without a target nothing happens. Where this paper differs is the instrument and the timing. A redundancy target set before the tools are proven commits us to an irreversible step in 2027 on an assumed result; a measured capacity target with gates keeps the ambition, lets the evidence set the number, and makes the commitment in October 2027 when we know what the tools actually do.

**Key assumptions:** SEK 0.86m per FTE-year; 9% attrition; programme cost SEK 12m in 2027, SEK 5.5m in 2028 and about SEK 3.7m a year after; 25% of automated hours return as review; six months' severance on top of notice pay; contractors at SEK 850 an hour.

**What are we missing, and what would make this wrong?**

---

## Appendix A. Assumptions register

| Assumption | Value | Basis | Replace with |
|---|---|---|---|
| Team size | 90 FTE | Given | HR, at FTE level |
| Split by area | 16 / 22 / 18 / 12 / 22 | Estimate | Org chart and activity sampling |
| Average monthly salary | SEK 48,000 | Estimate for a mix of AP, accounting, reporting and controller roles | Payroll aggregate |
| On-cost factor | 1.49 | SCB, white-collar staff in finance and insurance, August 2025 | Our own payroll on-costs (pension plan, collective insurance) |
| Employer contributions on severance | 31.42% | Skatteverket, full rate 2026 | Payroll |
| Automatable share and review overhead | Section 4 | Estimate; McKinsey (2018), Ardent Partners (2025) as direction | Pilot results at Gate 1 and 2 |
| Ramp | Wave 1 from Q2 2027, wave 2 from Q3 2027 | Estimate | Vendor and IT plan |
| Attrition | 9% a year | Estimate | HRIS, last three years |
| Leavers replaced anyway | 30% | Estimate | Critical-skills list |
| Capacity kept for quality | 15% | Board choice | Board |
| Internal moves | About 4 by 2029 | Estimate | Recruitment plan, open roles |
| Programme cost | Section 5 | Estimate | Vendor quotes, IT estimate |
| Contractor cover | SEK 850 an hour, 1,650 hours a year | Estimate | Framework agreements |
| Severance (B, D) | Six months' salary plus employer contributions | Estimate; no statutory severance in Sweden, packages are negotiated | Counsel, earlier settlements |
| Notice and timing (B) | Exits 4 in Q2, 12 in Q3, 11 in Q4 2027; half released from work during notice | Estimate from LAS notice periods and the four-month notification | Tenure profile, counsel |
| Selection-order effect (B, D) | Leavers paid 10% below average | Estimate | Tenure and pay profile |
| Extra attrition after cuts | +4.5 points for a year (B), +2 (D) | Estimate, deliberately below a linear reading of Trevor and Nyberg | Our own history after earlier changes |
| Replacement cost per extra leaver | Half a year's salary | Gallup range (one-half to two times salary), low end | Recruitment data |
| Discount rate | 8% | Estimate | Our hurdle rate |

## Appendix B. Sources

- SCB, [Labour costs for white-collar workers, August 2025](https://www.scb.se/hitta-statistik/statistik-efter-amne/arbetsmarknad/loner-och-arbetskostnader/arbetskostnadsindex-for-arbetare-och-tjansteman-inom-privat-sektor-aki/pong/tabell-och-diagram/arbetskostnader-for-tjansteman-under-augusti-2025/)
- Skatteverket, [Arbetsgivaravgifter](https://skatteverket.se/arbetsgivaravgifter)
- McKinsey, [Bots, algorithms, and the future of the finance function (2018)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/bots-algorithms-and-the-future-of-the-finance-function)
- Ardent Partners, [State of ePayables 2025: AP benchmarks and best-in-class performance (January 2026)](https://payablesplace.ardentpartners.com/2026/01/state-of-epayables-part-nine-ap-benchmarks-and-best-in-class-performance/)
- MIT NANDA, "The GenAI Divide: State of AI in Business 2025", reported by [The Register (August 2025)](https://www.theregister.com/2025/08/18/generative_ai_zero_return_95_percent)
- Gartner, [Over 40% of agentic AI projects will be canceled by end of 2027 (June 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- Orgvue survey, via [HR Dive (2025)](https://www.hrdive.com/news/leaders-who-laid-off-workers-due-to-ai-regretted-it/746643/); [Careerminds (2026)](https://careerminds.com/resources/cost-of-ai-layoffs)
- Trevor, C.O. & Nyberg, A.J. (2008), "Keeping your headcount when all about you are losing theirs", *Academy of Management Journal* 51(2), 259–276
- Gallup, [This Fixable Problem Costs U.S. Businesses $1 Trillion](https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses.aspx)
- OECD, [Employment Outlook 2023](https://read.oecd.org/10.1787/08785bba-en); OECD (2015), [Back to Work: Sweden](https://www.oecd.org/employment/back-to-work-sweden_9789264246812-en)
- CSN, [Transition study support statistics for 2025 (February 2026)](https://www.csn.se/om-csn/press/pressmeddelanden/2026-02-04-studiestodet-2025---stor-okning-av-antalet-studerande-med-omstallningsstudiestod.html)
- EIOPA, [Opinion on AI governance and risk management (6 August 2025)](https://www.eiopa.europa.eu/eiopa-publishes-opinion-ai-governance-and-risk-management-2025-08-06_en)
- EU AI Act, [Article 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26); Digital Omnibus timing, [Orrick (2026)](https://www.orrick.com/en/Insights/2026/05/EUs-Digital-Omnibus-on-AI-7-Key-Changes-You-Need-to-Know)
- Swedish statutes: Co-determination Act (MBL, SFS 1976:580); Employment Protection Act (LAS, SFS 1982:80); Act on certain employment-promoting measures (SFS 1974:13). EU: Solvency II Directive 2009/138/EC; DORA, Regulation (EU) 2022/2554
