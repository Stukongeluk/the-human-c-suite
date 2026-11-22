# AI and Automation in Finance & Back Office: Business Case

**Board paper, draft for discussion**
Prepared for: CFO | Scope: finance and back-office team (90 FTE), covering accounts payable, reconciliations and close, reporting, and other finance operations | Horizon: 2027–2031

> **Status of the numbers.** Every figure in this paper comes from planning assumptions (team split, loaded cost, attrition, vendor costs). None of it is company data yet. The structure and conclusions hold across a wide range of inputs, but the board should not approve headcount figures until the 8-week baseline in section 11 has replaced the assumptions with actuals. The accompanying model (`business-case-model.xlsx`) recalculates everything once you enter real figures.

---

## 1. Executive summary

**The proposal tested.** Use AI to replace 30% of the 90-person finance and back-office team (27 roles) during 2027, mainly in accounts payable, reconciliations and reporting.

**What the analysis shows:**

1. **The size of the target is about right. The timing is not.** Automation and AI can realistically remove around 26 FTE of work from this function (range 17–33). After the roughly 3 roles needed to run and control the automation, that leaves about 24 roles (range 14–30) that can come out. 30% is achievable in the upper half of the range, by 2029.
2. **By the end of 2027 the tools will have removed only about 8 FTE of work** (range 6–10). Cutting 27 roles in 2027 means letting go of about 22 people whose work still exists. That work then has to be done by consultants at about 1.5x the cost, or by a smaller team during year-end close and the first Solvency II reporting cycle under the amended rules.
3. **None of the options saves money in 2027.** In every option, 2027 is an investment year. The real choice is how much money and control risk the company takes on in getting to the same end state.
4. **Reducing headcount only as fast as the work disappears beats cutting first in every scenario we modelled**, including the most optimistic one.

**Options (mid case, SEK million)**

| | **A. Board ask:** 27 redundancies in 2027 | **B. Recommended:** automate, prove, then reduce | **C. Attrition and redeployment only** |
|---|---|---|---|
| Roles removed by end 2027 | 27 | 5 | 5 |
| Work still to be covered by consultants, Q4 2027 | about 23 FTE | none | none |
| Roles removed by end 2029 | 27 | 23.5 | 20 |
| People exiting with paid packages | 27 | about 5 | 0 |
| Net cash effect 2027 | **−36.5** | **−20.8** | −20.8 |
| Net annual benefit at run rate (2030) | 15.5 | 15.8 | 15.0 |
| Cumulative net 2027–2031 | −4.8 | **+15.9** | +12.3 |
| NPV 2027–2031 at 8% | **−12.1** | **+6.6** | +3.8 |
| Payback | after 2031 | 2031 | 2031 |

**Recommendation: Option B.** Keep the 30% ambition, but set it as an end-2029 target with a firm checkpoint in 2028, not as a 2027 headcount line. Compared with the board ask, B loses about SEK 16m less in 2027, is about SEK 19m better on 5-year NPV, needs about 22 fewer paid exits, and leaves year-end close and regulatory reporting fully staffed while the new tools prove themselves.

**Decisions requested from the board**

1. Approve the programme: about SEK 28m one-off over 2027–28 (including 15% contingency) and about SEK 6m a year in run costs, released in tranches at each stage gate.
2. Approve the principle that in-scope roles are not backfilled once a process's automation is live and has proven its capacity.
3. Approve the stage-gate framework in section 7, including delegated authority to run a voluntary exit programme at the Q3 2028 gate, sized to proven capacity.
4. Approve the KPIs in section 10 as the basis for quarterly reporting to the board or audit committee.
5. Note that redundancies can only be decided after MBL negotiations (section 5). The board approves the programme and the direction now. Decisions about individual roles come later.

---

## 2. What we tested, and how

- **Bottom-up by process.** For each process (AP, reconciliations and close, reporting, other) we estimated the share of work automation can remove at full effect, and how fast it ramps up.
- **Capacity is not headcount.** A role is only saved once its work has actually gone. Before that point, removing the person creates a gap that someone has to fill.
- **Quarterly, 2027–2031.** Three automation scenarios (Low, Mid, High) are crossed with three options (A, B, C). We used a 5-year NPV at an 8% discount rate with **no terminal value**, which is conservative because the run-rate benefit continues after 2031.
- **The model is equally fair to every option.** All options carry the same one-off and run costs. Option A is given no extra cost for a compressed timeline, although in practice doing everything in 2027 would cost more.

---

## 3. Baseline (planning assumptions, to be replaced in the 8-week baseline)

| Process | FTE | Typical work |
|---|---|---|
| Accounts payable & expenses | 18 | Invoice receipt and coding, matching, approvals, supplier queries, payment runs, travel and expenses, supplier master data |
| Reconciliations, GL & close | 24 | Bank, sub-ledger and intercompany reconciliations, journals, accruals, month- and year-end close |
| Financial, regulatory & management reporting | 22 | IFRS 17, Solvency II QRTs, SFCR/RSR, statutory accounts, management reporting, commentary |
| Other finance & back office | 26 | Premium and reinsurance accounting, treasury, tax, controlling, finance systems, leadership |
| **Total** | **90** | |

**Loaded cost:** SEK 850k per FTE in 2027. This assumes an average salary of about SEK 47k a month, 31.42% employer contributions, FTP pension, benefits and workplace costs, rising 3% a year. On this basis the function costs about **SEK 76.5m a year**, and 27 roles equal about SEK 23m a year in payroll.

**Attrition:** 7.5 FTE a year leave naturally (about 8%: resignations, retirements and internal moves). This is one of the most important inputs. Insurers often have older, long-tenured back-office teams, so the retirement profile over 2027–2029 matters a great deal.

---

## 4. Where the work can come out

| Process | FTE | Share of work removed at full effect: Low / **Mid** / High | Mid FTE | What automates well | What does not | Full effect by |
|---|---|---|---|---|---|---|
| Accounts payable & expenses | 18 | 40% / **55%** / 65% | 9.9 | E-invoice and PDF capture, ML coding, 2- and 3-way matching, approval routing, GenAI for supplier queries | Non-PO spend, supplier master data, payment controls, fraud checks | 2028–29 |
| Reconciliations, GL & close | 24 | 25% / **40%** / 50% | 9.6 | High-volume bank, sub-ledger and intercompany matching, recurring journals, auto-certifying low-risk accounts | Reinsurance, suspense items, judgemental accruals, year-end adjustments | 2029 |
| Reporting | 22 | 10% / **20%** / 25% | 4.4 | Data preparation, consistency checks, first-draft variance commentary and narrative | Judgement, actuarial interfaces, sign-off, new regulatory requirements | 2029 |
| Other | 26 | 5% / **10%** / 15% | 2.6 | Selective: treasury forecasting support, tax data preparation, controlling packs | Most of it | 2029 |
| **Gross work removed** | 90 | 17 / **26.5** / 33 FTE | 26.5 | | | |
| Less: new run and control roles | | | −3 | Automation and process owners, finance data, AI and controls. Filled by redeploying existing staff | | |
| **Net roles that can come out** | | 14 / **23.5** / 30 | 23.5 | That is 15% / **26%** / 33% of the team | | |

**Why these ranges are credible:**
- **AP is the most mature area.** Ardent Partners' 2025 benchmarks put average cost per invoice at USD 9.40, against USD 2.78 for best-in-class organisations ([WEX, citing Ardent Partners](https://www.wexinc.com/resources/blog/what-does-it-cost-to-process-an-invoice-ap-benchmarks-every-finance-team-should-know/)). Sweden's high e-invoicing adoption makes invoice capture easier. The remaining limits are coding, exceptions and supplier data.
- **Time to value is months, not weeks.** Gartner reports that simpler finance tasks such as payables automation typically reach expected value in nine to ten months, while complex work takes longer ([CFO Dive, Sep 2026](https://www.cfodive.com/news/cfos-need-realistic-ai-time-to-value-expectations-gartner/831315/)). In Gartner's March 2026 survey, 63% of finance organisations said their 2025 AI implementation was slower than expected ([Gartner, May 2026](https://www.gartner.com/en/newsroom/press-releases/2026-05-28-gartner-says-cfos-must-stop-mistaking-finance-ai-deployment-for-value-creation)).
- **Reporting demand goes up in 2027.** The amended Solvency II Directive applies from 30 January 2027. Annual reporting deadlines are extended, the SFCR is split into a policyholder section and a market-professional section, and member states must introduce an audit requirement for the Solvency II balance sheet ([William Fry](https://www.williamfry.com/knowledge/solvency-ii-reform-key-changes/)). Part of any capacity freed in reporting during 2027–28 will go to this new work. This is why the reporting ramp is slow.
- **"AI" here means a mix of tools.** Much of the AP and reconciliation gain comes from proven automation (capture, matching rules, workflow). GenAI and agentic tools add value on exceptions, queries and narrative. Presenting the programme as "automation and AI" keeps the case from being judged by the hype cycle.

---

## 5. Why 27 roles in 2027 does not work

**5.1 The work will not be gone yet.** In the mid case, the cumulative work removed is:

| End of quarter | Q1 2027 | Q2 2027 | Q3 2027 | Q4 2027 | Q2 2028 | Q4 2028 | Q4 2029 |
|---|---|---|---|---|---|---|---|
| Gross FTE of work removed | 2.1 | 4.2 | 6.2 | 8.3 | 14.2 | 20.1 | 26.5 |
| Net, after run and control roles | 0 | 1.1 | 3.2 | 5.3 | 11.2 | 17.1 | 23.5 |

Under Option A, an average of about 23 FTE of work is still there in Q4 2027, and about 16 FTE on average through 2028. That gap falls exactly on the 2027 year-end close, IFRS 17 year-end and the first Solvency II annual submission under the amended rules.

**5.2 The Swedish process sets the earliest date.** These timings should be confirmed with employment counsel and FAO.
- **MBL §11:** the employer must negotiate with the unions *before* deciding on an important change in the business. A board resolution that "27 roles will go" made before negotiations is a breach risk. The board approves the programme, and management negotiates before any decision on roles.
- **Varsel:** when 26–100 people are affected, the employer must notify Arbetsförmedlingen at least four months in advance ([Arbetsförmedlingen](https://arbetsformedlingen.se/for-arbetsgivare/anmal-varsel-och-permittering)).
- **Notice (LAS §11):** up to six months for employees with ten or more years of service ([SFS 1982:80](https://data.riksdagen.se/dokument/sfs-1982-80.text)). Collective agreements may add to this. A long-tenured back office means most leavers will be at the long end.
- **Result:** even if negotiations start in January, payroll savings begin around Q4 2027. The model assumes Option A exits take effect on 1 October 2027, with average packages of 6 months' loaded cost (negotiated severance and work-exempt notice).

**5.3 You may not lose the people whose work disappeared.** Selection for redundancy follows length of service within each selection group (turordningskrets). Since the 2022 reform, the employer can exempt at most three employees ([LAS §22](https://data.riksdagen.se/dokument/sfs-1982-80.text); [Företagarna](https://www.foretagarna.se/juridisk-faq/uppsagning/hur-manga-anstallda-far-jag-undanta-fran-turordningen/)). Longer-serving staff whose work is automated can move into remaining roles if they have sufficient qualifications. In practice, a cut of 27 removes the shortest-tenured people, who are often the most digitally fluent and the most useful in the new set-up. The alternative is a negotiated selection list (avtalsturlista), which usually costs more in packages. Our gap estimate assumes the leavers line up neatly with the automated roles, so it probably *understates* the disruption.

**5.4 Backfilling is legally and practically difficult.** Anyone dismissed for redundancy who has worked more than 12 months in the last three years has a right to re-employment priority. It lasts from the notice until nine months after their employment ends ([LAS §25](https://data.riksdagen.se/dokument/sfs-1982-80.text)). Under MBL §38 the employer must also negotiate before bringing in contractors to do work. Covering the gap with consultants while former staff hold re-employment rights should be expected to draw union challenge.

**5.5 Companies that cut ahead of the evidence often regret it.** In Orgvue's 2025 survey of 1,163 senior leaders, 39% had made employees redundant because of AI, and 55% of those said they had made wrong decisions about those redundancies ([Orgvue](https://www.orgvue.com/news/55-of-businesses-admit-wrong-decisions-in-making-employees-redundant-when-bringing-ai-into-the-workforce/)). Closer to home, Klarna's CEO said in May 2025 that its AI-first customer service had produced "lower quality" and that it was hiring human staff again ([Entrepreneur](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)). That was a different function, but it is the same lesson, and a Swedish board will know the story.

---

## 6. Options and financials

### 6.1 Option definitions
- **A. Board ask.** 27 redundancies take effect in Q4 2027. Any work that has not yet been automated is covered by consultants at 1.5x loaded cost in 2027–28, then by rehiring at 1.1x from 2029.
- **B. Recommended.** Automate first. From each go-live, leavers are not replaced once capacity is proven, and staff move into open roles elsewhere in the group. At the **Q3 2028 gate**, any remaining gap between headcount and *proven* capacity is closed with voluntary packages. Compulsory redundancy is a last resort. Roles never come out faster than the work does.
- **C. Attrition and redeployment only.** As B, but with no packages, so reductions follow natural exits.

### 6.2 Annual view, mid case (SEK million)

| Option A: Board ask | 2027 | 2028 | 2029 | 2030 | 2031 | Total |
|---|---|---|---|---|---|---|
| Payroll savings | 5.7 | 23.6 | 24.3 | 25.1 | 25.8 | 104.6 |
| Gap cover (consultants, then rehiring) | −7.3 | −20.8 | −6.7 | −3.6 | −3.7 | −41.9 |
| Exit packages | −12.8 | – | – | – | – | −12.8 |
| One-off implementation | −19.2 | −9.0 | – | – | – | −28.2 |
| Run costs | −3.0 | −5.5 | −6.0 | −6.0 | −6.0 | −26.5 |
| **Net** | **−36.5** | **−11.6** | **11.7** | **15.5** | **16.1** | **−4.8** |

| Option B: Recommended | 2027 | 2028 | 2029 | 2030 | 2031 | Total |
|---|---|---|---|---|---|---|
| Payroll savings | 1.4 | 8.9 | 18.3 | 21.8 | 22.5 | 72.9 |
| Gap cover | – | – | – | – | – | – |
| Exit packages (about 5 people, H2 2028) | – | −2.3 | – | – | – | −2.3 |
| One-off implementation | −19.2 | −9.0 | – | – | – | −28.2 |
| Run costs | −3.0 | −5.5 | −6.0 | −6.0 | −6.0 | −26.5 |
| **Net** | **−20.8** | **−7.9** | **12.3** | **15.8** | **16.5** | **+15.9** |

Option C nets −20.8 / −6.9 / 8.6 / 15.0 / 16.5, a total of +12.3. It reaches the same 23.5 roles as B about six months later, and runs about 5 roles behind B through 2028.

**Why A is worse even though it books more payroll savings:** in 2027–28 it pays SEK 1.50 for every SEK 1.00 of salary it removes ahead of the automation, and it pays exit packages for 27 people instead of about 5. In the mid case it also carries a permanent gap of about 3.5 FTE, because 27 is more than the work that actually disappears.

### 6.3 Scenarios: 5-year NPV at 8% (SEK million)

| | Low (17 FTE gross) | **Mid (26.5 FTE gross)** | High (33 FTE gross) |
|---|---|---|---|
| A. Board ask | −39.3 | **−12.1** | +1.2 |
| B. Recommended | −14.2 | **+6.6** | +14.9 |
| C. Attrition only | −14.2 | **+3.8** | +8.7 |

- B is the best option in every scenario.
- In the Low case no option pays back within five years *if the full programme is spent*. That is the main reason for stage gates: if Gate 1 points to the Low case, the reporting and "other" workstreams are cut back before the 2028 money is committed.
- **What would have to be true for A to beat B:** the High case *and* roughly 75–80% of its potential live and stable by Q4 2027, meaning every workstream, including reporting, at nearly full effect within about nine months. In the mid case A never catches B, even with the full mid-case potential live by end-2027, because 27 is more than the work that disappears.

### 6.4 Sensitivity of Option B (mid case, NPV SEK million, base +6.6)

| Change | B NPV | A NPV, for comparison |
|---|---|---|
| Loaded cost −15% / +15% | −1.4 / +14.5 | −17.4 / −6.8 |
| One-off cost +30% | −1.1 | −19.8 |
| Run cost +30% | +0.4 | −18.3 |
| Automation ramp 2 quarters late | −2.0 | −23.6 |
| Natural exits 4.5 / 10 per year | +2.5 (about 11 paid exits) / +8.4 | −12.1 / −12.1 |
| Exit packages 12 months instead of 6 | +4.8 | −22.7 |
| Discount rate 10% | +4.8 | −13.4 |

**How to read this:** B is a solid but not spectacular 5-year case. Its value is a durable net benefit of about SEK 16m a year from 2029, against a gross payroll reduction of about SEK 22m a year, or 26% of the function's cost. It is most exposed to delivery delays and implementation cost overruns, which is what the gates are designed to control. If your ERP already has AP capture and matching built in, one-off costs could be meaningfully lower.

---

## 7. Recommended plan and stage gates

| When | What happens | Gate decision |
|---|---|---|
| **Dec 2026 – Jan 2027** | Board approves the programme and tranche 1. MBL §11 negotiation on the programme. Open communication to staff (see section 8). Vendor shortlist. DORA and outsourcing classification. DPIA started. | — |
| **Q1 2027** | 8-week baseline: time study, process mining, volumes, current touchless and match rates, age and attrition profile. Model re-run on actuals. Vendor selection. | **Gate 0 (end Q1):** confirm the scenario range and the 2027–28 budget. |
| **Q2–Q3 2027** | AP wave live, plus expenses. Reconciliation platform build. Leavers in AP not backfilled once capacity is proven. | **Gate 1 (end Q3):** AP KPIs against plan, a go/no-go for reconciliation and reporting scale-up, and release of tranche 2. |
| **Q4 2027 – Q1 2028** | Reconciliations live for year-end 2027. Reporting automation runs *in parallel* on Q4 and the annual Solvency II and IFRS 17 cycles. | — |
| **Q2 2028** | Review after year-end close and the first annual Solvency II submission under the amended rules. | **Gate 2:** re-forecast end-state capacity on measured data. |
| **Q3 2028** | Size the voluntary programme as proven capacity minus expected attrition. MBL negotiation. Compulsory redundancy only for any remaining gap. | **Gate 3:** approve the size of the programme. |
| **Q1 2029** | End-state review. | **Gate 4:** confirm 27 roles, or reset the target to what the evidence supports. |

**Rule throughout:** a role comes out only when the work it did has measurably gone, as shown by KPI evidence and verified hours, not by vendor claims.

---

## 8. People plan

- **Commitment to staff.** We will automate, and the team will get smaller over time. Reductions will come first through attrition, retirements and internal moves. Nobody's role will be made redundant until the automation that replaces their work has been proven, and voluntary options will come before any compulsory steps. This is the single most important lever for keeping the process experts the programme depends on. Announcing "30% will go" up front tends to make the best people leave first.
- **Redeployment.** LAS already requires the employer to consider redeployment before any redundancy. Make it a programme workstream: map open roles across the group (claims, risk and compliance including DORA, data, customer operations) and offer reskilling into them.
- **New roles.** About 3 FTE of automation and process owners, finance data and AI controls, filled from the current team.
- **Reskilling and AI literacy.** This is also a legal duty under the EU AI Act (Article 4, in force since February 2025). Budgeted in the one-off costs.
- **Retaining key people.** Targeted retention for process experts through the 2027 and 2028 year-end cycles.
- **Transition support** for anyone who leaves: the sector's omställningsavtal, the public omställningsstudiestöd (via CSN), and outplacement (budgeted).
- **Work environment.** A documented risk assessment before each change, under Arbetsmiljöverket's rules on systematic work environment management.
- **Unions.** Involve the local Forena and Saco union clubs early, starting with the technology change and not only at the redundancy stage. Under B, a negotiated, mostly voluntary path is realistic. Under A, expect disputes.

---

## 9. Controls, risk and regulation

- **Finansinspektionen and Solvency II.** If an AI or automation vendor ends up performing a critical or important function (financial reporting probably qualifies), Solvency II requires the insurer to notify the supervisor in advance. Plan this into the vendor timeline.
- **DORA** (applies since January 2025). AI and automation SaaS counts as ICT third-party service. That brings register-of-information entries, mandatory contract terms, exit strategies, and advance notice to FI of planned contracts that support critical or important functions.
- **EU AI Act.** AP, reconciliation and reporting uses are not high-risk. In insurance, the high-risk category is risk assessment and pricing for life and health insurance. Document the classification anyway, and meet the AI literacy duty.
- **GDPR.** Invoices and expense claims contain personal data (sole traders, employees). A DPIA is needed, plus data residency and no-training terms for any GenAI tools.
- **Internal control and audit.** Bots and agents need their own identities, least-privilege access and segregation of duties. Set posting and payment thresholds that require human approval, and keep full audit trails and change control over rules and prompts. AI drafts narrative reporting, and named people sign it. Involve the external auditor in Q1 2027, because they will test IT general controls over the new tools. The Swedish Bookkeeping Act's archiving requirements apply to automated records.
- **Key programme risks.** Delivery slippage (the largest sensitivity), data quality, vendor lock-in, loss of key staff, new regulatory workload absorbing capacity, and rising AI usage costs. Each one has a named owner and is reported at every gate.

---

## 10. KPIs and benefits tracking (reported quarterly)

| Area | KPI |
|---|---|
| AP | Touchless invoice rate, cost per invoice, invoices per AP FTE, exception rate, duplicate or erroneous payments, cycle time |
| Reconciliations & close | Auto-match rate, % of reconciliations auto-certified, close duration (working days), late or reopened journals |
| Reporting | QRT/SFCR/IFRS 17 deliverables on time, resubmissions, audit adjustments, hours per reporting cycle |
| Capacity | Verified hours released per process (time study, not vendor estimates), roles removed against proven net capacity (must never be negative) |
| Control | Audit findings on automated processes, control failures, AI exceptions overridden by people |
| People | Attrition of key staff, internal moves, engagement in the affected teams, completion of reskilling |
| Financial | Payroll run-rate against plan, one-off spend against tranche, run cost per process |

---

## 11. Assumptions to validate in the first 8 weeks

| Assumption (default) | Why it matters | How to validate |
|---|---|---|
| FTE split by process (18 / 24 / 22 / 26) | Determines the size of the opportunity | Time study across all 90 people, 2 weeks |
| Loaded cost of SEK 850k per FTE | NPV moves about ±8m for each ±15% | HR payroll extract including pension and benefits |
| Natural exits of 7.5 a year | Decides whether B needs packages | 3-year attrition history, age and retirement profile, internal mobility |
| Current automation level | Low current automation means higher potential | Invoice volumes, PO share, e-invoice share, current touchless and match rates |
| One-off of SEK 28m, run cost of SEK 6m a year | NPV moves about ±7m for each ±30% | Two or three vendor quotes, ERP-native options, IT estimate |
| Ramp speed | A 2-quarter delay turns B's NPV slightly negative | Vendor references from Nordic insurers, pilot results |
| Notice periods and package levels | Size of exit costs | Employment counsel, FAO, the tenure profile of the in-scope population |

---

## 12. Sources

- Arbetsförmedlingen, rules for notifying redundancies (varsel): https://arbetsformedlingen.se/for-arbetsgivare/anmal-varsel-och-permittering
- Employment Protection Act (LAS, SFS 1982:80), §§ 7, 11, 22, 25: https://data.riksdagen.se/dokument/sfs-1982-80.text
- Företagarna, exemptions from the selection order after the 2022 reform: https://www.foretagarna.se/juridisk-faq/uppsagning/hur-manga-anstallda-far-jag-undanta-fran-turordningen/
- William Fry, Solvency II reform key changes (Directive (EU) 2025/2): https://www.williamfry.com/knowledge/solvency-ii-reform-key-changes/
- CFO Dive on Gartner, finance AI time to value (Sep 2026): https://www.cfodive.com/news/cfos-need-realistic-ai-time-to-value-expectations-gartner/831315/
- Gartner, "CFOs must stop mistaking finance AI deployment for value creation" (May 2026): https://www.gartner.com/en/newsroom/press-releases/2026-05-28-gartner-says-cfos-must-stop-mistaking-finance-ai-deployment-for-value-creation
- WEX, citing Ardent Partners' 2025 AP Metrics That Matter: https://www.wexinc.com/resources/blog/what-does-it-cost-to-process-an-invoice-ap-benchmarks-every-finance-team-should-know/
- Orgvue, 2025 survey on AI-driven redundancies: https://www.orgvue.com/news/55-of-businesses-admit-wrong-decisions-in-making-employees-redundant-when-bringing-ai-into-the-workforce/
- Entrepreneur, Klarna rehiring human customer service staff (May 2025): https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
- Regulatory references (MBL §§ 11 and 38, Solvency II Art. 49, DORA Art. 28, AI Act Art. 4 and Annex III, GDPR, AFS 2023:1) are summarised from the legal texts and should be confirmed by legal counsel and compliance before the board meeting.
