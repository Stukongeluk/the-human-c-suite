# Support Transition People Plan: Stockholm and Helsinki

**Draft v0.1. Confidential to the working group (you, HR lead, Head of Support, CFO, local counsel).**
**Status: this is a proposal, not a decision.** In Sweden the law requires you to negotiate with the unions *before* you decide on the reduction. In Finland, the process depends on how many people the Finnish entity employs. Until the process opens, keep the plan inside the working group, and don't let anyone treat "6" as settled.

Confidence tags used throughout: **[VERIFIED: source]** = checked against a current source; **[ASSUMED]** = my assumption, not checked against your data. Confidence: High / Medium / Low.

---

## 1. The plan on one page

| | |
|---|---|
| **Goal** | Move from 18 support staff (Stockholm 10, Helsinki 8) to a smaller team with a new remit, in a way that is fair to the people affected, legally clean in both countries, and doesn't damage the customer experience. |
| **Proposed end state** | 6 people (to be confirmed by the evidence gate, section 3: the honest range today is 6 to 8). |
| **Order of levers** | Backfill freeze, then natural attrition, then redeployment into other roles, then a voluntary departure package. Dismissals under the selection rules come last, only for whatever is left. |
| **Shape of the process** | **One** process and **one** announcement per country, with exit dates staggered across 2027. No salami-slicing (several smaller rounds of cuts). |
| **Timeline** | Evidence and design Dec 2026 to Jan 2027. Process opens week of 8 Feb 2027. Notices from late March. Exits Q2 to Q3 2027. Steady state Oct 2027. Review Dec 2027. |
| **Where savings land** | Mostly H2 2027. Notice periods (up to 6 months by law, longer under some agreements) push some payroll into early 2028. |

[ASSUMPTION: no company-context file or input data was available. Entity headcounts, collective agreements, tenure, salaries, ticket volumes and AI metrics are all unknown. Every number below that depends on them is illustrative.] Confidence overall: Medium.

---

## 2. Facts to confirm first (by Fri 4 Dec 2026, owner: HR lead)

| Fact | Why it changes the plan |
|---|---|
| Headcount of the **Finnish** employing entity (under 20 / 20 to 49 / 50+) | Decides whether Finnish change negotiations are required at all, and how long they must last (section 6B). |
| Collective agreements in each country (e.g. a Swedish white-collar agreement, the Finnish clerical agreement) | Sets notice periods, selection rules, exemption options and transition support. |
| For each of the 18: start date (total service), age, contract type, working time, role | Swedish seniority order, notice periods and Finnish change-security eligibility all depend on these. |
| Who is on parental or family leave, pregnant, on long-term sick leave, or a union rep, shop steward or safety rep | These people have special protection (section 8). Identify them early and quietly. Don't use this information to select anyone. |
| Open vacancies anywhere in the company, in both countries | Offering redeployment into vacant roles is a legal duty before dismissal in both countries, and it's your best humane lever. |
| Customer language needs (share of contacts in Swedish, Finnish and English) | Decides the site split for the end state. |
| AI vendor contract: uptime commitments, cost per resolution, how cost scales with volume | Feeds the cost model and the fallback plan. |

---

## 3. Evidence gate: decide the number on data (30 Nov 2026 to 29 Jan 2027)

**Why:** the whole plan rests on "AI resolves most first-line tickets". Most dashboards can't tell deflection (the customer gave up, or came back through another channel) from real resolution. First-line tickets are also the quick ones, so the share of tickets AI handles overstates the share of *work* it removes.

> **Illustration [ASSUMED, not your data]:** if AI handles 70% of tickets by count, but those tickets were only 35 to 40% of agents' handle time, human workload falls by about 35 to 40%. That points to roughly 11 to 12 people, not 6, before you add the new work of supervising the AI. **6 is right only if the remaining human work (escalations, AI oversight, coverage) is about one third of today's.**

**What to measure (owner: Head of Support with whoever owns the AI; weekly):**

| Gate metric | Proposed starting threshold [ASSUMED: to be set with CCO and the AI owner] |
|---|---|
| **True resolution:** AI-closed conversations with no re-contact on the same issue within 7 days, in any channel | No worse than today's human first-contact resolution, stable for 6 consecutive weeks |
| **Audited accuracy:** 100 randomly sampled AI conversations per week, reviewed by a support specialist | 95% or more correct and policy-compliant. Zero critical errors (refunds, billing, privacy, security) in the last 4 weeks |
| **CSAT (customer satisfaction), AI-handled vs human-handled** | AI within 5 points of human |
| **Time to a human** when the AI hands over | Within today's service-level target |
| **Commercial signal (owner: CCO)** | No rise in churn or downgrades among accounts with heavy AI contact, compared with similar accounts |
| **Workload model** (formula below) | The end-state team runs at 80% load or less, with 2 people per required language available in a July week |

**Workload model:**

```
Required FTE = (human-handled tickets per month x average handle hours)
               / (productive hours per FTE per month x 0.8)
             + AI-quality and knowledge work (FTE)
             + team lead
```

Productive hours per FTE come to about 120 to 130 a month after statutory holidays, public holidays, sick leave and training [ASSUMED: check against your own HR data]. Both countries give people long summer holidays that the law protects, so size for **July**, not for an average month.

**Holiday caveat:** December volumes aren't representative, so treat January as the main reading.

**Gate decision (Fri 5 Feb 2027; you, CFO, CCO):** end state 6, 7 or 8. If the data points to 8, go to 8 and let attrition do the rest in 2028. That costs far less than a second round of cuts or rehiring.

---

## 4. End-state design: what the remaining team does

A post-AI support team does different work. It isn't a smaller version of the old team. Write the role profiles **before** selection, and write them honestly (see section 8).

| Role | # (if 6) | Remit |
|---|---|---|
| Support lead (player-coach) | 1 | Runs the team across both sites. Owns service levels and the gate metrics. Takes escalations. |
| Escalation specialists | 3 | Complex technical, billing/account and complaint cases, plus AI handovers. Native-language cover for Swedish and Finnish, and English. |
| AI support quality and knowledge owners | 2 | Weekly conversation audits, the knowledge base, handover rules. Send the **top-10 contact drivers** to product every week. |

**Rules for everyone:** rotate between escalations and AI-quality/product work (about 60/40) to prevent burnout and keep coverage. Single team, single rota across both sites.

**Site split (your decision, based on the language data):**

| Option | Upside | Downside |
|---|---|---|
| 3 + 3 (recommended default) | Keeps native-language escalation in both countries. Cut is spread evenly. | Each site is thin: one person sick plus one on holiday leaves one person. Needs a cross-site rota. |
| 4 + 2 or 2 + 4 | Matches the larger language market | The smaller site is fragile |
| Single hub | Strongest team, simplest management | Loses one language and puts the whole cut on one site. Closing a site is a bigger legal and reputational process. |

**Product angle (CPO):** if AI now resolves most first-line contacts, most of them are probably "how do I do X" questions. That is a usability and product-market-fit red flag that the AI now hides from you. The aim is **fewer contacts**, not just cheaper ones. The two knowledge owners, or someone redeployed into product ops, own that loop. The north-star metric for support becomes *contacts per active customer*, with cost per contact as a secondary measure. [ASSUMED: ticket mix] Confidence: Medium.

---

## 5. Path from 18 to the end state

| Lever (in this order) | Illustrative effect [ASSUMED] | Timing |
|---|---|---|
| Backfill freeze in first-line support, plus natural attrition | 1 to 3 seats | From Dec 2026 |
| Redeployment into vacancies and new roles: customer success/onboarding, QA/test, documentation, product ops / voice-of-customer analyst, AI conversation design, solutions | 2 to 4 seats | Feb to Apr 2027 |
| Voluntary departure package, open to all 18, with a 3 to 4 week window | 3 to 5 seats | Feb to Mar 2027 |
| Dismissals under each country's selection rules | The remainder (0 to 6) | Notices from late Mar 2027 |

Support staff know the product and its customers better than almost anyone. Redeploying them is the cheapest way to keep that knowledge, and it's the CPO's strongest lever. Budget for reskilling, because "you can apply internally" with no training behind it isn't redeployment.

**Caution on voluntary packages:** the people most likely to take them are your most marketable people. Before the window opens, decide whether you'll accept every application or reserve the right to decline them for end-state roles, and say so up front.

---

## 6. Country process

### 6A. Sweden (Stockholm, 10 people)

| Step | Rule | Source |
|---|---|---|
| Negotiate **before** deciding | MBL §11 (the Co-determination Act) requires negotiating with the relevant unions before deciding on the reorganisation. Invite every union with members in the affected agreement areas. If the union asks for central negotiations (within 7 days after local talks end), wait for them to finish. | [VERIFIED: Livsmedelsföretagen redundancy checklist, Jul 2026] High |
| Share information | MBL §15 requires written background, headcounts, timing and method. Under MBL §18, don't rely on documents you wouldn't hand to the union. | [VERIFIED: same] High |
| Notify Arbetsförmedlingen | Required when 5 or more employees in a county may be made redundant. For up to 25 people, give at least 2 months' notice before the first termination. Late or missing notice can lead to a penalty fee. | [VERIFIED: Arbetsförmedlingen fact sheet] High |
| Redeployment check | LAS §7 (the Employment Protection Act) requires you to document, in writing, every vacancy across the whole company. Redeployment only covers roles the person has sufficient qualifications for, though reasonable onboarding can be expected. | [VERIFIED: checklist] High |
| Selection (seniority order) | LAS §22: order is by total length of service within each operational unit and agreement area, provided the person has sufficient qualifications for the remaining role. You may exempt up to 3 people of special importance. Employers bound by the white-collar main agreement (Huvudavtalet) have alternative exemption rules. You can negotiate a different list with the union (*avtalsturlista*). | [VERIFIED: checklist; Fortnox LAS summary] High |
| Notice periods | LAS §11: 1 month minimum, 2 months after 2 years, up to 6 months after 10 years. Many white-collar collective agreements add 6 months for employees aged 55+ with 10 years' service. For someone on full parental leave, notice starts when they return. | [VERIFIED: Lawline; checklist] High. The agreement rule is Medium until checked against *your* agreement. |
| Re-employment priority | Anyone with more than 12 months' service in the last 3 years has priority for re-employment during notice and for **9 months after** employment ends, if qualified. | [VERIFIED: checklist] High |
| Transition support | White-collar staff under a collective agreement get transition support and severance (AGE) through TRR. Without an agreement, the public basic transition support applies. | [VERIFIED: checklist] High for TRR. Medium for the no-agreement route. |

**Practical note:** with 10 people and an end state of about 3 in Stockholm, the 3 exemptions plus an agreed list may cover your choice of who stays. That's how most Swedish employers handle it, usually in exchange for better voluntary terms. Confirm with counsel how the exemptions apply across units. [ASSUMED] Confidence: Medium.

### 6B. Finland (Helsinki, 8 people)

| Finnish entity size | What applies | Source |
|---|---|---|
| **50+ employees** | The Co-operation Act applies. Change negotiations last at least **7 days** if fewer than 10 people are affected, and 3 weeks otherwise (halved from 14 days / 6 weeks on 1 Jul 2025). Some collective agreements set longer periods. | [VERIFIED: Työmarkkinatori; Yrittäjät; Bird & Bird] High |
| **20 to 49 employees** | Change negotiations are required only if 20 or more people are affected within 90 days. Helsinki's 8 alone wouldn't trigger them. A lighter "continuous dialogue" duty still applies. | [VERIFIED: same] High |
| **Under 20** | The Co-operation Act doesn't apply. The Employment Contracts Act still does. Before giving notice, explain the grounds and alternatives to each affected person. | [ASSUMED: from the Employment Contracts Act, confirm with counsel] Medium |

**Applies at every size (Employment Contracts Act):**

- **Grounds:** the work must have diminished *substantially and permanently*. Your evidence-gate data is also your legal ground. Confidence: High.
- **Alternatives first:** offer other suitable work, with reasonable training, before dismissal. Confidence: High.
- **Notice periods:** 14 days (under 1 year), 1 month (1 to 4 years), 2 months (4 to 8), 4 months (8 to 12), 6 months (over 12), unless a collective agreement says otherwise. [VERIFIED: Eurofound] High
- **Paid job-search leave during notice:** 5 / 10 / 20 working days depending on notice length. Employees aged 55+ with 5 years' service get 5 / 15 / 25. [VERIFIED: Eurofound] High
- **Change security (employers with 30+ employees, employees with 5+ years' service):** employer-funded employment-promoting training or coaching. If you don't offer it, pay its value. Also 6 months of occupational health care after the work obligation ends. Tell everyone affected that they have the right to an employment plan. [VERIFIED: Työmarkkinatori, updated Feb 2026] High
- **Re-employment:** 4 months (6 if service was 12+ years). **Since 1 Jun 2026 this no longer applies to employers with fewer than 50 employees**, unless a collective agreement requires it. [VERIFIED: Eurofound; DLA Piper 2026] High
- **Selection:** no statutory seniority rule, but some collective agreements require you to weigh length of service, dependants and essential skills. [VERIFIED: Eurofound] High

---

## 7. Timeline (Dec 2026 to Dec 2027)

| Phase | Dates | What happens | Owner |
|---|---|---|---|
| 0. Facts and counsel | to Fri 4 Dec 2026 | Section 2 facts. Engage employment counsel in Sweden and Finland. Working group only. | HR lead |
| 0. Evidence and design | 30 Nov 2026 to Fri 29 Jan 2027 | Gate metrics, workload model, role profiles, cost model v1. Backfill freeze from Fri 18 Dec. **No announcement before the holidays.** | Head of Support, AI owner, CFO |
| 1. Gate decision | Fri 5 Feb 2027 | End state 6 / 7 / 8. Counsel signs off the process plan. | You, CFO, CCO |
| 2. Open the process | Week of 8 Feb 2027 | Sweden: union invitation under MBL §11 and notice to Arbetsförmedlingen. Finland: process per entity size. **Same-day, in-person announcement at both sites.** | You, HR, counsel |
| 3. Negotiate and offer alternatives | Feb to mid-Mar 2027 | Negotiations, redeployment matching, voluntary window (closes about 12 Mar), weekly updates to staff | HR, Head of Support |
| 4. Decisions and notices | Late Mar 2027 | Individual meetings, then written notices delivered in person. Notice periods start. | Managers with HR |
| 5. Staggered exits | Apr to Sep 2027 | Wave 1 by end of June. Wave 2 by end of September, after the summer. Paid knowledge-transfer time. Most leavers get garden leave so they can job-hunt. | Head of Support |
| 6. Stabilise | Oct to Nov 2027 | End-state team in steady state. Overflow contract stays on standby. | Support lead |
| 7. Review | Dec 2027 | 30/60/90-day review: was the number right, what did we miss? Re-employment windows still open. | You |

---

## 8. Selection: how the people who stay are chosen

- **Sweden:** seniority order as above, plus exemptions or an agreed list. Role profiles must reflect the real work. Inflating requirements to steer who stays is the classic failure, and unions and the Labour Court see through it.
- **Finland:** written, objective criteria tied to the role profiles, applied consistently and documented, plus anything your collective agreement requires.
- **Protected people:**
  - **Finland:** people who are pregnant or on family leave can be dismissed only if operations cease entirely. Shop stewards only if their work ends entirely and no other suitable work exists. [VERIFIED: Eurofound; RTT] High
  - **Sweden:** parental leave can't be a reason, and notice for someone on full leave starts when they return. Union reps may have priority. Length of service includes parental and sick leave. [VERIFIED: checklist] High
- **Never select on:** sickness absence, parental leave, age, union activity, or per-agent ticket statistics. The AI rollout already changed which tickets each person got, so those numbers measure the routing, not the person.

---

## 9. Support for people who leave

| Component | Sweden | Finland |
|---|---|---|
| Notice pay | 1 to 6 months by law, plus collective-agreement extensions. Garden leave for most people. | 14 days to 6 months |
| Time and help to find work | TRR support (with a collective agreement). Garden leave. | Paid job-search leave of 5 to 25 days. Employment plan. Training or coaching worth the statutory value if eligible. |
| Health | Occupational health access during notice | 6 months of occupational health care if eligible |
| Voluntary package premium | Amount set with counsel and CFO against local norms [ASSUMED: no figure given here on purpose] | Same |
| For everyone, regardless of statutory eligibility | Outplacement coaching, a reskilling budget, a reference and LinkedIn recommendation from their manager, keeping their laptop or phone, an alumni channel, first refusal on future roles. A written explanation of their re-employment rights. | Same |

---

## 10. The plan for the people who stay

- **Day-one clarity:** a written role profile, what changes, and a training plan (AI tooling, conversation auditing, knowledge-base writing, data basics).
- **Retention:** stay agreements for people mapped to the end state, and for leavers in wave 2 whose knowledge you need through September. Pay them out after the final exits. Review salaries where the role's scope grew.
- **Workload guardrails:** escalation-only work is heavier, so keep the 60/40 rotation and cap overtime. Each month, review overtime, sick leave and pulse scores for the team.
- **Career path:** AI support quality can lead to product ops, voice-of-customer work or conversation design. Make this concrete so the role isn't a dead end.
- **Survivor care:** say plainly that colleagues are leaving. Train managers for the conversations. Make occupational health available.

---

## 11. Communication plan

**Principles:** one story, told the same day at both sites, in person, by the most senior leader with HR in the room. Affected people hear it from you before they read it anywhere. Be explicit about what is *proposed* and what is *decided*. Don't promise "no further changes" unless you can keep it. Never Slack-first.

| When | What |
|---|---|
| Day -10 to -1 | Sweden: union invitation and notice to Arbetsförmedlingen. Finland: process per entity size. Brief managers 24 hours before. Counsel reviews the FAQ. |
| Day 0, morning | Meeting at each site: what's proposed and why (with the evidence), the process and timeline, the support available, what is *not* decided. |
| Day 0, afternoon | Written summary to all 18 and a question channel. 1:1s offered to everyone within 48 hours. Occupational health on standby. |
| Weekly during negotiations | Update, even when there's no news |
| Customers (with CCO) | Before exits begin: a visible way to reach a human stays in place. No AI overclaiming. |

**FAQ must cover:** why now, how the number was set, how selection works in each country, the voluntary package and its deadline, redeployment options, notice and pay, transition support, re-employment rights, who to ask.

**Avoid:** announcing in December, announcing by video only, or letting it leak through finance, the AI vendor or recruiters.

---

## 12. Service continuity and knowledge transfer

- **Knowledge capture before exits:** each leaver gets paid, scheduled time to move their tacit knowledge into the knowledge base. Not their last afternoon.
- **AI fallback:** contract overflow capacity with Nordic languages (temp agency or outsourcer) on standby for the first 6 months after the final exit. Keep a runbook for AI outages and model regressions. Six people can't absorb first-line volume if the AI fails in July.
- **Keep the gate metrics running after exits.** If two in a row turn red, the overflow contract activates and you revisit the end state at the December review.
- **Product loop:** send the top-10 contact drivers to product every week. Target a falling contact rate per active customer.

---

## 13. Budget lines (cost model template; owner: CFO)

**One-off:** notice pay plus employer social charges (including garden leave), voluntary premiums, Finnish training or coaching value and 6 months of occupational health, outplacement, stay agreements, reskilling (redeployed people and stayers), legal counsel in both countries, overflow contingency, and the AI audit effort during the gate.

**Run-rate:** payroll of exited roles (saving) minus AI platform cost (which grows with volume) and AI-quality tooling. Redeployed people's payroll moves to other teams. It isn't saved.

**Ask the CFO for:** net run-rate saving after AI cost, total one-off cost, payback in months, and the 2027 vs 2028 split.

---

## 14. Metrics (team-level, monthly)

| Area | Metrics |
|---|---|
| Customer | CSAT (AI vs human), 7-day re-contact rate, time to a human, complaint volume, churn among accounts with heavy AI contact |
| AI quality | Audited accuracy, critical errors, handover rate |
| Team | Pulse score, overtime, sick leave, regretted attrition among the stayers |
| Transition | Share of affected people redeployed, in new jobs or in education within 6 months (voluntary alumni check-in). Legal disputes (target: zero). |
| Product | Contacts per active customer. Top drivers fixed. |

---

## 15. Risks

| Risk | Trigger | Mitigation |
|---|---|---|
| "Resolution" is really deflection | Re-contact rate or complaints rise, CSAT falls | Evidence gate before announcing. Gate metrics keep running after exits. Overflow contract. |
| Best people leave first and you end up with the wrong team | Resignations from people mapped to end-state roles | Early retention agreements, exemptions or an agreed list, honest role profiles |
| Legal sequence wrong | Decision taken or communicated before negotiations. Selection that discriminates. | Counsel signs off every step. "Proposal" language throughout. Documented criteria. |
| Thin coverage | July holidays, sickness, AI outage | 2 per language in July, cross-site rota, overflow standby |
| Savings arrive later than planned | Long notice periods, 55+ agreement extensions | CFO models 2027 vs 2028. Voluntary terms can shorten the timeline by agreement. |
| Employer-brand damage in a small Nordic market | Leak, careless messaging, Klarna comparisons | One story, in person, generous support. Publish what you did for people only if it's true. |

---

## 16. Validation before this goes out

**Peer verification (not done yet; required because this touches headcount, legal process, budget and customers):**

| Role | Question to answer |
|---|---|
| CHRO / HR lead | Are the package levels and retention approach right for the Stockholm and Helsinki markets? Is the timeline realistic? |
| General counsel and local employment counsel (SE, FI) | Every step in section 6, the Finnish entity size, the collective-agreement terms, the selection method and exemptions |
| CFO | Cost model, payback, AI run cost at projected volume |
| CCO | Churn risk, gate thresholds, customer communication |
| AI owner (CAIO) | Is "resolution" measured correctly? Is the audit design sound? |
| CTO | AI outage and regression fallback |

**Critic pre-screen** (required because more than 30% of the team is affected; run by me, not an independent reviewer):

- **Weakest point:** the number 6 was set before the data.
- **Missing perspective:** customers, the product team, and what the leavers know that isn't written down anywhere.
- **If wrong, the cost is:** rehiring 2 to 4 people in 2028 (recruitment and ramp-up), churn from a weaker service (to be sized with the CCO), and reputational damage in two small hiring markets.
- **Proceed:** yes, after closing the evidence gap (section 3) and getting counsel's sign-off (section 6).

---

## 17. Sources

- Livsmedelsföretagen, *Checklista omorganisation och arbetsbrist* (Jul 2026): MBL, LAS §7/§11/§22/§25 to 26, Huvudavtalet, TRR. https://www.livsmedelsforetagen.se/app/uploads/2026/07/checklista-omorganisationocharbetsbrist-20260701.pdf
- Arbetsförmedlingen, fact sheet on redundancy notification (English). https://arbetsformedlingen.se/download/18.446992bb1922f85547c1f0ec/1779803325065/Faktablad%20om%20varsel%20(engelska).pdf
- Fortnox, *Nya LAS sammanfattad i 9 punkter*. https://www.fortnox.se/fortnox-foretagsguide/driva-foretag/lon/nya-las-sammanfattad-i-9-punkter
- Lawline, *Uppsägningstid enligt LAS*. https://lawline.se/answers/uppsagningstid-enligt-las-2
- Työmarkkinatori, changes to the Co-operation Act (2025). https://tyomarkkinatori.fi/en/news/yhteistoimintalain-muutokset-nostavat-lain-soveltamisrajaa-ja-lyhentavat-muutosneuvotteluiden-kestoa
- Yrittäjät, *Yhteistoimintalaki uudistuu 1.7.2025*. https://www.yrittajat.fi/tietopankki/ajankohtaista-tyonantajalle/yhteistoimintalaki-uudistuu-1-7-2025-voimaan-tulevat-muutokset/
- Bird & Bird, Changes to employee consultation obligations in Finland as of 1 July 2025. https://www.twobirds.com/en/insights/2025/yhteistoimintalaki-uudistuu---joustavuutta-ja-tehokkuutta-yritysten-arkeen
- Työmarkkinatori, *Muutosturva työnantajan näkökulmasta* (updated Feb 2026). https://tyomarkkinatori.fi/tyonantajat-ja-yrittajat/tietoa-tyonantajuudesta-ja-yrittajyydesta/tyosuhteen-muutostilanteet/muutosturva-tyonantajan-nakokulmasta
- Eurofound ERM database, Finland: notice periods, job-search leave, re-employment, selection. https://apps.eurofound.europa.eu/legislationdb/notice-period-to-employees/finland, https://apps.eurofound.europa.eu/legislationdb/time-off-for-job-search/finland, https://apps.eurofound.europa.eu/legislationdb/reemployment-obligation-after-restructuring/finland, https://apps.eurofound.europa.eu/legislationdb/selection-of-employees-for-collective-dismissals/finland
- DLA Piper, Finland reforms the Employment Contracts Act (2026). https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/finland-reforms-the-employment-contracts-act
- RTT, special employment protection (Finland). https://rt.fi/wp-content/uploads/2024/04/5-Erityinen-tyosuhdeturva-ja-korvausvelvollisuus-RTT.pdf
- CX Today, Klarna pivots back to human customer service (2025). https://www.cxtoday.com/contact-center/klarna-grapples-with-ai-led-customer-service-pivots-to-an-uber-type-of-setup/
- Gartner, Half of companies that cut customer service staff due to AI will rehire by 2027 (Feb 2026). https://www.gartner.com/en/newsroom/press-releases/2026-02-03-gartner-predicts-half-of-companies-that-cut-customer-service-staff-due-to-ai-will-rehire-by-2027
- Gartner, Only 20% of customer service leaders report AI-driven headcount reduction (Dec 2025). https://www.gartner.com/en/newsroom/press-releases/2025-12-02-gartner-survey-finds-only-20-percent-of-customer-service-leaders-report-ai-driven-headcount-reduction

*This plan is not legal advice. Every legal step needs sign-off from employment counsel in Sweden and Finland before you act on it.*
