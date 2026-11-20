# AI in finance and back office: business case 2027–2028

**Board paper, draft for discussion** · Prepared by the CFO · November 2026

All amounts are in SEK m at constant 2027 prices, net against "do nothing", and are **estimates** until we have replaced the assumptions in section 11 with our own payroll, ERP and reconciliation data. The model behind every table is `savings_model.py`; its full output, including the low and high cases, is in `model_output.md`.

---

## 1. Recommendation

**Approve a gated AI programme for accounts payable, reconciliations and reporting, starting in January 2027. Do not approve a commitment to replace 27 of 90 roles in 2027.** Headcount should follow the capacity the AI has been shown to free, through a hiring freeze, natural attrition and redeployment. Voluntary exits come in only at the end-2027 gate, and only for any surplus that is left.

The numbers behind it (base case):

- **Replacing 27 roles in 2027 costs about SEK 43m net in 2027 and SEK 51m over two years.** That is a loss, not a saving. The reason is that the AI can't take over the work by the time people leave. On our estimates it frees about 7 FTE of work by end-2027 (range 3–11), not 27. We would cover the gap with consultants and then rehire about 26 people in 2028.
- **The gated plan costs about SEK 14.5m in 2027,** which makes 2027 an investment year. It turns positive in 2028 (+2.2m). From 2029 it saves about SEK 10m a year in the base case and SEK 20m a year in the high case. Headcount falls from 90 to 73 (base) or 62 (high) by end-2028, without forced redundancies.
- **30% is reachable, but a year later than asked and only if the pilot shows it.** In the high case we reach 31% fewer heads by end-2028. In the base case the AI adds little over cheap process fixes, which is why the scale decision belongs at a gate, not in this paper.

## 2. What we are solving for

The ask is for AI to replace 30% of a 90-person team (27 FTE) next year. The team costs about **SEK 79m a year**, at an estimated loaded cost of SEK 0.88m per FTE: salary, the 31.42% employer contribution, occupational pension and the special payroll tax on it, and the IT that goes with each person. So the ask is worth at most **SEK 23.7m a year gross**, before any cost of getting there.

Before we lock the plan, the board should tell us which problem this is meant to solve, because the answer changes the work:

- **A cost or expense-ratio target by a date.** If so, this lever is too small and too slow to carry the target alone. We should size the rest of the operating cost base next to it: procurement, IT run costs, distribution and claims leakage.
- **A credible AI plan for finance operations.** That is what this paper delivers.
- **Both.** Then we need both pieces of work, and this paper covers only the second.

## 3. Where the work is: sizing tasks, not jobs

The team split below is an assumption until we load the real organisation chart. "Process fixes" are improvements that need no new AI: an e-invoicing drive, supplier consolidation, matching rules in tools we already own, and stopping reports nobody reads. Any option can capture them, so the AI case must not claim them.

| Team | FTE | Net FTE freed by end-2028: process fixes only (low / base / high) | Process fixes + AI (low / base / high) |
|---|---|---|---|
| Accounts payable and supplier data | 20 | 2.0 / 3.0 / 4.0 | 5.0 / 9.0 / 13.0 |
| Reconciliations (bank, premium, claims, reinsurance, intercompany) | 22 | 1.1 / 2.2 / 2.6 | 4.4 / 7.7 / 11.0 |
| Accounting and close | 16 | 0.5 / 0.8 / 1.3 | 1.6 / 3.2 / 4.8 |
| Reporting (IFRS/statutory, Solvency II, management) | 22 | 0.7 / 1.1 / 1.8 | 1.1 / 2.6 / 5.5 |
| Management, finance systems and controls | 10 | 0.0 / 0.0 / 0.0 | 0.0 / 0.0 / 0.5 |
| **Gross** | **90** | **4.2 / 7.1 / 9.7** | **12.1 / 22.5 / 34.8** |
| New work: reviewing AI output, exceptions, monitoring, control testing | | 0 | −2.0 / −3.0 / −4.0 |
| **Net capacity freed** | | **4.2 / 7.1 / 9.7 (5% / 8% / 11%)** | **10.1 / 19.5 / 30.8 (11% / 22% / 34%)** |

**Timing (estimate).** We pilot in the first half of 2027, scale in the second half and reach full effect by end-2028. Net capacity freed is about **6.8 FTE by end-2027** (3.5 low, 10.8 high) and 19.5 by end-2028.

**Why these shares, and not more:**

- **Accounts payable is where the evidence is strongest, and it still has limits.** In Ardent Partners' 2025 benchmarks, invoices processed without human touch averaged 32.6%, and 49.2% for best-in-class teams. So even the best teams still handle about half their invoices by hand. Our base case frees 45% of AP hours, which assumes we perform close to best-in-class. (The share of invoices processed untouched and the share of hours freed are different measures, but they move together.)
- **Reconciliations:** rule-based matching already exists. AI adds most value on exception triage and on suggesting the explanation for a break.
- **Reporting** has the tightest controls: Solvency II quantitative templates, the solvency and financial condition report, the regular supervisory report, and the IFRS/statutory accounts. AI helps with data checks, drafting variance commentary and preparation. People still prepare the figures we sign.
- **The base rate is sobering.** In September 2024, Gartner predicted that 90% of finance functions would deploy at least one AI-enabled solution by 2026, but that fewer than 10% would see headcount reductions. In Gartner's 2026 survey of 1,303 functional leaders, 23% reported AI-related headcount reductions and 17% reported increases. Its advice to CFOs was that "AI-generated capacity is a resource, not a return."

## 4. The options, costed on the same basis

Both options that use AI (A and B) carry the same AI programme cost: SEK 14.7m in 2027 and SEK 7.8m in 2028 (licences and usage, integration and data work, controls and audit, programme team, training). Option A gets the same AI results as B. Both choices favour A.

| Option | 2027 | 2028 | 2027–28 | Saving per year from 2029 | Heads end-2028 | Forced / voluntary exits | Reversible? |
|---|---|---|---|---|---|---|---|
| 0. Do nothing | 0.0 | 0.0 | 0.0 | 0.0 | 90 | 0 / 0 | n/a |
| A. 27 redundancies in 2027, alongside the AI programme (the board's ask) | **−43.1** | −7.7 | −50.8 | +10.5 | 73 (after ~26 rehires) | 27 / 0 | No |
| B. Gated AI programme; headcount follows proven capacity (**recommended**) | **−14.5** | +2.2 | −12.3 | +10.4 | 73 | 0 / 1 | Yes, until the gate |
| C. Process fixes only, no new AI | −0.1 | +5.3 | +5.2 | +5.7 | 83 | 0 / 0 | Yes |

**Range across the AI cases** (low / base / high):

| | 2027 | 2028 | From 2029 per year | Heads end-2028 |
|---|---|---|---|---|
| A | −44.6 / −43.1 / −41.4 | −14.7 / −7.7 / 0.0 | +3.7 / +10.5 / +16.5 | 81 / 73 / 66 |
| B | −15.9 / −14.5 / −13.7 | −0.8 / +2.2 / +0.6 | +3.7 / +10.4 / +19.9 | 81 / 73 / 62 |
| C | −0.7 / −0.1 / +0.4 | +3.0 / +5.3 / +7.3 | +3.3 / +5.7 / +7.7 | 86 / 83 / 81 |

In B's high case, 2028 is lower than in the base case because it includes 10 voluntary exit packages (about SEK 5.9m). In return it saves the most from 2029.

**What the AI adds on top of process fixes (B minus C):**

| AI case | 2027 | 2028 | Extra saving per year from 2029 | Years after 2028 to pay back |
|---|---|---|---|---|
| Low | −15.2 | −3.8 | +0.4 | more than 40 |
| Base | −14.4 | −3.1 | +4.6 | about 4 |
| High | −14.1 | −6.7 | +12.2 | about 2 |

This is the finding the board most needs to hear. **The AI is worth scaling only if it delivers clearly more than an average finance function gets.** For B to beat process fixes alone by end-2030, the AI needs to free at least about **17 FTE net by end-2028**. That is about 1.4 times our base estimate, or 24 FTE (27%) together with the process fixes. If the whole AI programme costs 30% less than we estimate, the base case is enough. We can't know any of this today. A six-month pilot on our own invoices and reconciliations can tell us.

## 5. Why the saving doesn't arrive in 2027 under option A

Swedish employment law sets the clock:

- **Co-determination Act (MBL):** we must negotiate with the unions before deciding on major changes. That takes January to February 2027.
- **Notice to Arbetsförmedlingen:** for 26 to 100 dismissals, it must come at least four months before the first affected employment ends. The earliest exits are therefore in June.
- **Employment Protection Act (LAS):**
  - Notice periods run from one to six months by length of service, and we assume most exits fall between June and September.
  - Selection follows length of service within each operational unit and agreement area, with three exemptions allowed. So the people who leave are the most recently hired, not necessarily those whose tasks the AI takes over. Those who stay must be retrained into the remaining roles.
  - People dismissed for lack of work have nine months' priority for re-employment.

**Option A, base case (SEK m):**

| Line | Q1 2027 | Q2 2027 | Q3 2027 | Q4 2027 | 2027 | 2028 |
|---|---|---|---|---|---|---|
| Gross payroll saving (from actual exit dates) | +0.2 | +0.5 | +3.3 | +7.3 | +11.3 | +16.6 |
| Severance and exit packages (6 months' pay, est.) | 0.0 | −4.2 | −6.4 | 0.0 | −10.6 | 0.0 |
| Outplacement and transition top-up | −1.1 | 0.0 | 0.0 | 0.0 | −1.1 | 0.0 |
| Legal and advisory | −0.8 | 0.0 | 0.0 | 0.0 | −0.8 | 0.0 |
| Work still to be done (consultants for the gap) | −2.6 | −6.2 | −8.5 | −10.6 | −27.9 | −10.2 |
| Recruitment vs baseline (none in 2027; rehiring and extra attrition in 2028) | +0.6 | +0.6 | +0.5 | +0.5 | +2.2 | −5.7 |
| Redeployment of later surplus | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | −0.3 |
| AI programme (all lines) | −2.0 | −4.1 | −4.6 | −4.0 | −14.7 | −7.8 |
| Process fixes | −0.3 | −0.5 | −0.5 | −0.2 | −1.5 | −0.3 |
| **Net cash effect** | **−6.0** | **−13.9** | **−16.2** | **−7.0** | **−43.1** | **−7.7** |
| **Net P&L effect** (severance provided for when the plan is announced) | **−16.7** | **−9.6** | **−9.8** | **−7.0** | **−43.1** | **−7.7** |
| Headcount at period end | 88 | 87 | 74 | 56 | 56 | 73 |
| Work gap covered by consultants (average FTE) | 7.2 | 17.3 | 23.4 | 29.1 | 19.3 | 7.0 |

- **The gap is the whole story.** By the fourth quarter about 29 FTE of work is uncovered, because 27 people have gone, about 7 have left through normal attrition and nobody has been hired, while the AI has freed about 6. For AP, that work means late payments. For reconciliations it means control findings, and for Solvency II reporting it means missed deadlines. None of that can simply be left undone.
- **Even if it were left undone, A doesn't beat B.** With no consultant cost at all, A's 2027 would be −15.2m, against −14.5m for B, with 19 FTE of work not done.
- **Rehiring early instead of using consultants doesn't rescue it.** It makes 2027 worse (−48.0m), because of recruitment costs, and it means rehiring people who have priority rights to their old roles.
- **Other companies' experience points the same way.** In a 2026 survey of 600 HR leaders, two in three companies that had cut jobs because of AI were already rehiring, and only 8.4% would repeat the restructuring unchanged. In a 2025 survey, 55% of leaders who had made AI-driven redundancies said they had made the wrong decisions. Both are vendor surveys, so read them as direction, not as precise rates.
- **The model includes one hidden cost and leaves out another.** It includes extra attrition among the people who stay: we assume 13% instead of 8% for 12 months. Research has found a 1% downsizing associated with 31% more voluntary turnover the next year. It leaves out the knowledge that goes with the 27 people, who are often the ones we'd need to configure and check the AI.

## 6. Option B: the recommended plan

| When | What happens | Decision |
|---|---|---|
| Jan 2027 | Process fixes start. Hiring freeze with exceptions in AP and reconciliations, using fixed-term cover where capacity isn't yet proven. Four-week baseline: hours by task, volumes, error rates. MBL information and negotiation on the programme, with union representatives in the design group. | — |
| Feb–Jun 2027 | Pilot in AP (capture, coding, matching) and reconciliations (matching, exception triage) on live data. A person approves every payment and posting. Controls are designed with internal audit and the external auditor, and the vendor goes through the DORA third-party assessment. Spend to the gate is about SEK 6.2m. | — |
| **Gate 1: end of June 2027** | Measured against the baseline: hours freed, error and exception rates, auditor comfort, firm vendor prices. | **Scale** if the results point to at least about 17 FTE of AI capacity by end-2028, or to the base case with firm programme costs about 30% below our estimate. Otherwise **narrow** the scope (for example AP only) or **stop**. If we stop, 2027 costs about SEK 7.5m and 2028 is +3.0m from the process fixes. |
| Jul–Dec 2027 | Scale in AP and reconciliations. Pilot in reporting (data checks, draft commentary), with people signing the figures. Redeployment into open roles elsewhere in the company starts from October. | — |
| **Gate 2: December 2027** | 2028 headcount plan built from measured capacity: attrition (about 7 a year), redeployment (about 5–7 people) and, only for surplus left after both, a voluntary programme negotiated with the unions. Base case about 1 person, high case about 10, leaving in September 2028. | Involuntary reductions only if the voluntary route fails. Then they happen once, under LAS, with support from the day of notice. |
| 2028 | Full run. Quarterly review to the audit committee; scale or stop on the evidence. | — |

**Option B, base case (SEK m):**

| Line | Q1 2027 | Q2 2027 | Q3 2027 | Q4 2027 | 2027 | 2028 |
|---|---|---|---|---|---|---|
| Gross payroll saving (leavers not replaced, redeployment) | 0.0 | +0.1 | +0.5 | +0.8 | +1.4 | +9.4 |
| Redeployment (reskilling, ramp-up in the new role) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | −0.7 |
| Voluntary exit packages (9 months' pay, est.) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | −0.6 |
| Temporary cover while old and new processes run side by side | 0.0 | −0.6 | −0.4 | 0.0 | −1.0 | 0.0 |
| Recruitment vs baseline (fewer replacements) | 0.0 | +0.3 | +0.5 | +0.5 | +1.3 | +2.2 |
| AI programme (all lines) | −2.0 | −4.1 | −4.6 | −4.0 | −14.7 | −7.8 |
| Process fixes | −0.3 | −0.5 | −0.5 | −0.2 | −1.5 | −0.3 |
| **Net cash effect** | **−2.3** | **−4.8** | **−4.5** | **−2.9** | **−14.5** | **+2.2** |
| **Net P&L effect** | **−2.3** | **−4.8** | **−4.5** | **−2.9** | **−14.5** | **+2.2** |
| Headcount at period end | 90 | 89 | 87 | 86 | 86 | 73 |

Two caveats on B's figures:

- About SEK 4.7m a year of B's saving from 2029 depends on the 5.3 people redeployed filling real vacancies that we would otherwise fill from outside. If they don't, that capacity goes to backlog and quality work, or into the voluntary offer at gate 2.
- The model leaves out volume growth. If volumes grow by about 3% a year, part of the freed capacity absorbs that growth instead of new hires. That is a cost avoided rather than a cut, and it makes B and C look better, not A.

## 7. Controls, regulation and law

- **Money controls stay human.** The AI proposes, and a person approves payments, postings and changes to supplier master data. Segregation of duties and audit trails stay as they are, and supplier-fraud controls get stronger, not weaker.
- **External audit.** The auditor needs to be able to rely on the automated controls (IT general controls and testing of the automated controls themselves). We bring them in during the pilot, not at year-end.
- **DORA** (Regulation (EU) 2022/2554, applying since 17 January 2025). AI vendors are ICT third-party providers: they go into the register of information, need a risk assessment and need contract terms that meet DORA. The requirements are heavier if they support a critical or important function.
- **Solvency II outsourcing** (Article 49). If a vendor performs a critical or important function, we must notify Finansinspektionen before the outsourcing starts. Compliance should confirm whether this applies to financial reporting tools.
- **EIOPA's Opinion on AI governance and risk management** (6 August 2025) sets risk-based, proportionate expectations on data governance, record-keeping, fairness, cybersecurity, explainability and human oversight. We will document the pilot to that standard.
- **EU AI Act.** These finance tools are not high-risk. Using AI to allocate work to individuals or to monitor and evaluate employees would be high-risk (Annex III), with a duty to inform workers from 2 December 2027. We will report on teams, not individuals, and we will never use the tools to rank people or choose who leaves.
- **Swedish employment law** (MBL, LAS, notice to Arbetsförmedlingen) applies to B as well. Changes to how work is organised need MBL negotiation even when no one is dismissed.
- This paper is not legal advice. Employment counsel, compliance and the external auditor should confirm these points before the board decides.

## 8. People plan

- **Unions in at the problem stage.** We share these numbers with our local union representatives before the board decides, and invite them into the design group. Their objections are free risk analysis.
- **Career conversations with all 90**, including the question: "if your current tasks were automated tomorrow, what would you most like to do instead?"
- **Paid learning time.** SEK 1.5m in 2027 and SEK 1.0m in 2028 is already in the model.
- **Redeployment first.** Internal vacancies are open to finance staff first, with reskilling. New roles are needed anyway: automation and exception analysts, controls, data quality, analysis.
- **If voluntary exits are needed after gate 2:**
  - an attractive package (we estimate 9 months' pay);
  - support from the day of notice through the job security council under our collective agreement, plus a company top-up (the OECD found that over 85% of displaced Swedish workers found a new job within a year);
  - help to apply for the state transition study support (omställningsstudiestöd, about 80% of salary up to a ceiling, for up to about a year).
- **Communication.**
  - Managers are briefed first and tell their own people in person.
  - No 30% figure is announced before the evidence exists.
  - Nothing is announced on a Friday afternoon or before holidays.
- **Incentives.** No management bonus is tied to FTE reduction. The programme's measures are cost per invoice, close days, error rates and regretted attrition.

## 9. Measures and review rhythm

Agreed now and reviewed quarterly with the audit committee:

- **Money:**
  - cost per invoice and the share of invoices processed without human touch;
  - hours per reconciliation and the age of open breaks;
  - close days;
  - finance cost per SEK of premium;
  - programme spend against budget;
  - consultant spend.
- **Quality and risk:**
  - error and duplicate-payment rate;
  - late payments;
  - audit findings;
  - regulatory filing timeliness.
- **People:**
  - regretted attrition;
  - engagement pulse;
  - absence;
  - internal moves;
  - training hours taken.

## 10. The board's view, taken seriously

The board is right on three points. The opportunity in AP and reconciliations is real. Competitors are automating. Waiting has a cost. A bold target also creates urgency, and B keeps that urgency: process fixes start in January and the pilot in February.

What changes is when headcount becomes a commitment: at the gate, on our own data. The best-known Swedish example points the same way. Klarna cut its headcount by about 22% mostly through a hiring freeze and attrition, then in 2025 began hiring human customer service staff again after its CEO said the cheaper AI service had produced "lower quality".

## 11. Key assumptions and what would change this paper

| Assumption | Value | Basis |
|---|---|---|
| Average salary, blended | SEK 50,000/month | Estimate. SCB 2024 averages: ekonomiassistenter SEK 38,100, redovisningsekonomer 45,700, controllers 58,900, then blended and uplifted |
| Loaded cost per FTE | SEK 0.88m/yr | Employer contribution 31.42% (Skatteverket, fact); pension 7% of salary plus 24.26% special payroll tax (estimate); IT and benefits SEK 25k |
| Voluntary attrition | 8%/yr (13% for 12 months after a 30% cut) | Estimate; replace with our three-year data |
| AI capacity, net | 6.8 FTE end-2027, 19.5 end-2028 (low 10.1, high 30.8) | Estimate from task shares (section 3) |
| AI programme cost | SEK 14.7m in 2027, 7.8m in 2028; about 4.3m/yr to run from 2029 | Estimate; replace with vendor quotes |
| Consultant cost | SEK 1.45m per FTE-year | Estimate (about SEK 850/hour) |
| Exit package | 6 months' pay (A), 9 months' pay (voluntary) | Estimate; not statutory in Sweden, negotiated in practice |
| Replacement hire | SEK 0.3m all-in | Gallup's lower bound of half a year's salary |

**Sensitivities on 2027.**

- **Option A:** −36.4m to −49.9m as the consultant rate moves from SEK 1.1m to 1.8m per FTE-year, and −37.8m to −53.8m as the exit package moves from 3 to 12 months.
- **Option B:** stays between −13.7m and −15.9m across every case.

**What would change my mind:**

- **The pilot shows the high case.** We accelerate, and the 30% becomes a firm commitment for end-2028.
- **A large part of the 90 are consultants or temporary staff.** Ending those contracts first is the fastest saving, and it costs no employee their job.
- **Attrition is well above 8%.** The no-forced-exit path gets faster.
- **The board's real target is a cost number by a date.** Then we need the full operating cost review alongside this plan.

**Data that replaces the estimates within four weeks:**

- the ERP/AP subledger: invoice volumes, touchless rate, exceptions, cycle time;
- the reconciliation tool: counts, auto-match rates, age of breaks;
- the close calendar and reporting deadlines;
- payroll and HR aggregates by team (cost per FTE, tenure bands for notice periods, three years of attrition), in aggregate only;
- consultant spend in finance;
- two weeks of activity sampling;
- vendor quotes.

---

## Sources

- Arbetsförmedlingen, [Anmäl varsel och permittering](https://arbetsformedlingen.se/for-arbetsgivare/anmal-varsel-och-permittering): notice periods counted to when the first affected employment ends
- Skatteverket, [Arbetsgivaravgifter](https://skatteverket.se/arbetsgivaravgifter): 31.42% full rate, 2026
- SCB, Lönesök ([controller](https://www.scb.se/hitta-statistik/sverige-i-siffror/lonesok/Search/?lon=controller), [redovisningsekonom](https://www.scb.se/hitta-statistik/sverige-i-siffror/lonesok/Search/?lon=redovisningsekonom), [ekonomiassistent](https://www.scb.se/hitta-statistik/sverige-i-siffror/lonesok/Search/?lon=ekonomiassistent)), 2024 statistics
- Lag (1982:80) om anställningsskydd (LAS); Lag (1976:580) om medbestämmande i arbetslivet (MBL); CSN on [omställningsstudiestöd (February 2026)](https://www.csn.se/om-csn/press/pressmeddelanden/2026-02-04-studiestodet-2025---stor-okning-av-antalet-studerande-med-omstallningsstudiestod.html)
- Gartner, [90% of finance functions will deploy AI by 2026; fewer than 10% will see headcount reductions (September 2024)](https://www.gartner.com/en/newsroom/press-releases/2024-09-12-gartner-predicts-that-90-percent-of-finance-functions-will-deploy-at-least-one-ai-enabled-tech-solution-by-2026)
- Gartner, [Three steps for CFOs to turn AI time savings into business value (November 2026)](https://www.gartner.com/en/newsroom/press-releases/2026-11-04-gartner-idnetifies-three-steps-for-cfos-to-turn-ai-time-saavings-into-business-value)
- Ardent Partners, *AP Metrics That Matter in 2025*, as summarised by [apexanalytix (March 2025)](https://www.apexanalytix.com/resources/blog/ardent-partners-key-ap-metrics-2025/)
- Careerminds, [The cost of AI layoffs (February 2026)](https://careerminds.com/resources/cost-of-ai-layoffs); [CPA Practice Advisor (July 2026)](https://www.cpapracticeadvisor.com/2026/07/13/9-in-10-hr-leaders-regret-ai-driven-layoffs-new-survey-finds/186619/)
- Orgvue survey, reported by [HR Dive (2025)](https://www.hrdive.com/news/leaders-who-laid-off-workers-due-to-ai-regretted-it/746643/)
- Trevor & Nyberg, "Keeping your headcount when all about you are losing theirs", *Academy of Management Journal* 51(2), 2008
- Gallup, [This fixable problem costs U.S. businesses $1 trillion](https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses.aspx)
- EIOPA, [Opinion on AI governance and risk management (6 August 2025)](https://www.eiopa.europa.eu/eiopa-publishes-opinion-ai-governance-and-risk-management-2025-08-06_en)
- Regulation (EU) 2022/2554 (DORA); Directive 2009/138/EC (Solvency II), Article 49; Regulation (EU) 2024/1689 (AI Act), Annex III and Article 26
- Klarna: [Entrepreneur, citing Bloomberg (May 2025)](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)
- OECD (2015), [Back to Work: Sweden](https://www.oecd.org/employment/back-to-work-sweden_9789264246812-en): over 85% of displaced Swedish workers re-employed within a year
