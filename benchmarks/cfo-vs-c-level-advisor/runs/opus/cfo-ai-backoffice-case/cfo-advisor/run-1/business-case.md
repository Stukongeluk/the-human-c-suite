# AI in Finance & Back-Office: Business Case

**Board paper, draft for the CFO's review** · November 2026
**Scope:** 90 FTE in finance and back-office: accounts payable, reconciliations and accounting operations, reporting, plus leadership, systems and control
**Status:** Swedish law, tax rates and external evidence are checked against sources. **Every company figure is a placeholder** (marked 🔴) until it is replaced with actuals in `ai-backoffice-model.xlsx`.

Confidence tags: 🟢 verified against a source · 🟡 reasonable inference or single source · 🔴 assumption, replace with your data

---

## 0. Decision required

The board asked for a case showing that AI can replace 30% of the team (27 of 90 FTE) in 2027. This paper puts two options side by side:

| | **Option A: 27 compulsory redundancies in 2027** | **Option B: gated capacity programme** |
|---|---|---|
| What it is | Commit now. Run MBL, varsel and turordning in H1 2027. Exits around Sep 2027. | Freeze hiring into automatable roles. Pilot, then scale. Reduce through attrition and redeployment. Offer voluntary packages only for surplus the pilots have proven. |
| FTE out by end-2029 (base) | 27, but about 13 FTE of work is still uncovered and has to be bought back | 15.7 (17%), all of it backed by measured capacity |
| 2027 net cash (base) | −SEK 28.2m | −SEK 12.5m |
| 2027–29 net cash (base) | −SEK 34.6m | −SEK 3.3m |
| 5-year NPV at 8% (base) | −SEK 21.4m | +SEK 8.3m |
| Bear case, 5-year NPV | −SEK 67.1m (cannot be undone) | about −SEK 7.5m if stopped at the June 2027 gate |
| Bull case, 5-year NPV | +SEK 30.7m | +SEK 39.1m (30.6 FTE, 34%) |

**Recommendation: Option B, with 30% by end-2029 as a stretch target tied to gates.** On 3-year cash and on NPV it matches or beats Option A in every scenario. It also limits the downside to the cost of the pilot. Confidence: 🟡 medium. The structure and the legal constraints are solid. The automation rates are assumptions until the pilot measures them.

---

## 1. The question we can answer honestly

"AI will replace 30% next year" is a conclusion, and a business case should not start from one. The question this paper answers is: **how much work can AI take out of these processes, how fast, and how do we turn that capacity into lower cost without breaking the close or Solvency II reporting?**

The answer has two parts:

1. **Capacity.** In the base case AI can release about 17% of the team's work by end-2029, and 34% if everything goes right. It cannot release 30% inside 2027 under any scenario we can defend (section 4).
2. **Conversion to cost.** Swedish employment law sets the speed, the order and the reversibility of any reduction (section 5). Cutting ahead of capacity costs more than it saves (section 6).

---

## 2. Baseline: team and cost

### 2.1 Loaded cost per FTE (SEK, 2026 prices)

| Component | Rate | Source |
|---|---|---|
| Arbetsgivaravgift 2026 | 31.42% | Skatteverket 🟢 |
| Semestertillägg (about 0.8% × 25 days ÷ 12) | 1.67% | typical salaried agreement 🟡 |
| Occupational pension, blended FTP | 6.0% of salary | placeholder 🔴 |
| Särskild löneskatt on pension | 24.26% | statutory 🟡 |
| Collective insurances | 1.0% | placeholder 🔴 |

Multiplier = (1 + 1.67%) × (1 + 31.42%) + 6.0% × (1 + 24.26%) + 1.0% = 1.3361 + 0.0746 + 0.0100 = **1.4207**

Office and IT overhead is excluded on purpose, because it does not fall when headcount falls.

### 2.2 Team (placeholders anchored to SCB 2024 national averages: ekonomiassistenter SEK 38,100, redovisningsekonomer SEK 45,700, controllers SEK 58,900 per month 🟢)

| Sub-function | FTE | Avg monthly salary 🔴 | Loaded cost / FTE | Total loaded |
|---|---:|---:|---:|---:|
| Accounts payable | 22 | 40,000 | 681,938 | 15.0m |
| Reconciliations & accounting ops | 30 | 48,000 | 818,325 | 24.5m |
| Reporting (statutory, Solvency II, IFRS, management, tax) | 28 | 58,000 | 988,809 | 27.7m |
| Leadership, systems & control | 10 | 70,000 | 1,193,391 | 11.9m |
| **Total** | **90** | | **avg 879,699** | **SEK 79.2m** |

**The headline the board probably has in mind:** 27 FTE × SEK 0.88m = **SEK 23.8m a year.** Section 5 explains why Option A would actually save SEK 19.3m a year.

---

## 3. What AI can realistically take on

| Area | What automates well | What stays human | Steady-state share of hours automatable (bear / base / bull) 🔴 |
|---|---|---|---|
| Accounts payable | Invoice capture and coding, PO and contract matching, duplicate detection, supplier queries | Exceptions, disputes, new suppliers, payment approval and segregation of duties | 30% / 50% / 65% |
| Reconciliations & accounting ops | Bank and sub-ledger matching, suggested journals, variance flagging | Investigating breaks, judgemental accruals, insurance-specific accounting for claims, reinsurance and premiums | 20% / 35% / 50% |
| Reporting | Data collection, first-draft commentary, consistency checks across reports | Sign-off on Solvency II QRTs and SFCR/RSR, IFRS judgements, anything FI or the auditors read | 5% / 15% / 25% |
| Leadership | Fewer team leads once teams shrink | Accountability, control ownership | 0% / 10% / 20% |

Two more drivers matter as much as the automation rate:

- **Conversion (55% / 70% / 85%) 🔴.** Freed time is spread thinly across many people: 20 minutes a day saved for 30 people is not 1.25 people you can remove until the processes are redesigned around it.
- **Realisation by end-2027 (25% / 40% / 60%) 🔴.** Selecting a vendor, completing DORA due diligence and contracting, integrating, piloting and stabilising mean a realistic go-live around mid-2027.

**What the external evidence says:**
- 59% of finance functions used AI in 2025, little changed from 58% in 2024. 91% reported low or moderate initial impact. AP automation is one of the top use cases at 37% ([Gartner, Nov 2025](https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025)). 🟢
- Gartner explicitly tells CFOs to "reset expectations" on AI's impact on productivity and headcount, and to challenge cost and headcount savings in AI business cases ([Gartner, Mar 2025](https://www.gartner.com/en/newsroom/press-releases/2025-03-25-gartner-says-cfos-should-reset-expectations-about-ais-impact-on-workforce-productivity-and-headcount)). 🟢
- A field study of 79 firms and 277 accountants found that AI users closed the books 7.5 days faster. About 8.5% of accountant time moved from routine data entry to higher-value work, and 62% of the accountants worried about errors in AI output ([MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-can-make-accountants-more-productive)). 🟢
- MIT's NANDA research found that most enterprise GenAI pilots deliver "little to no measurable impact on P&L". The biggest ROI was in back-office automation, and bought specialist tools succeeded about 67% of the time, against roughly a third of that for internal builds ([Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)). 🟢 **Implication: buy specialist AP and reconciliation tools. Do not build.**

---

## 4. Capacity scenarios

Steady-state gross FTE release = Σ FTE × automatable share × conversion

| | Bear | Base | Bull |
|---|---:|---:|---:|
| AP | 22 × 30% × 55% = 3.63 | 22 × 50% × 70% = 7.70 | 22 × 65% × 85% = 12.16 |
| Reconciliations | 30 × 20% × 55% = 3.30 | 30 × 35% × 70% = 7.35 | 30 × 50% × 85% = 12.75 |
| Reporting | 28 × 5% × 55% = 0.77 | 28 × 15% × 70% = 2.94 | 28 × 25% × 85% = 5.95 |
| Leadership | 0.00 | 10 × 10% × 70% = 0.70 | 10 × 20% × 85% = 1.70 |
| **Gross steady state** | **7.70** | **18.69** | **32.56** |
| New AI/automation-ops roles (redeployed) 🔴 | −4 | −3 | −2 |
| **Net steady state** | **3.7 (4%)** | **15.7 (17%)** | **30.6 (34%)** |

Net FTE release at each year end (gross steady state × realisation − AI-ops roles):

| Year end | Bear | Base | Bull |
|---|---:|---:|---:|
| 2027 | −2.1 (−2%) | 4.5 (5%) | 17.5 (19%) |
| 2028 | 0.2 | 12.0 (13%) | 30.6 (34%) |
| 2029 | 2.2 (2%) | 15.7 (17%) | 30.6 (34%) |

### What you would have to believe

- **27 net FTE by Dec 2027:** gross release would have to be 27 plus the AI-ops roles, within months of go-live. With bull realisation (60%) and bull conversion (85%), that needs **63% of all team hours, reporting included, automatable.** With base realisation and conversion it needs 119%, which is impossible. Both figures sit far above the evidence in section 3. 🟡
- **27 net FTE by end-2029:** this needs the bull case in all three areas at once (AP 65%, reconciliations 50%, reporting 25%, 85% conversion). **It is a credible stretch target. It is not a plan.** 🟡

Value of one released FTE, weighted by where the work comes from (base): SEK 803,001.

---

## 5. Turning capacity into cost: the Swedish constraints

| Constraint | What it means for this programme | Source |
|---|---|---|
| **MBL 11 §** primary duty to negotiate | Negotiate with the unions before deciding on an important change. The redundancy decision cannot come before the negotiation. | 🟡 GC to confirm |
| **Varsel** (Lag 1974:13, 2 §) | For 26–100 affected employees, notify Arbetsförmedlingen at least **4 months** before the first exit | [Riksdagen](https://data.riksdagen.se/dokument/sfs-1974-13.text), [Arbetsförmedlingen](https://arbetsformedlingen.se/for-arbetsgivare/anmal-varsel-och-permittering) 🟢 |
| **Notice** (LAS 11 §) | At least 1 month, rising to 6 months after 10 years' service. Your FAO agreement may differ. | [LAS](https://data.riksdagen.se/dokument/sfs-1982-80.text) 🟢 |
| **Saklig grund and reassignment** (LAS 7 §) | A dismissal is not objectively justified if other work could reasonably be offered | [LAS](https://data.riksdagen.se/dokument/sfs-1982-80.text) 🟢 |
| **Turordning** (LAS 22 §) | Leavers are chosen by length of service, **not by whose work AI automated.** At most 3 people can be exempted. Those who stay must have sufficient qualifications for the remaining work, so retraining falls on us. | [LAS](https://data.riksdagen.se/dokument/sfs-1982-80.text), [Företagarna](https://www.foretagarna.se/juridisk-faq/uppsagning/hur-manga-anstallda-far-jag-undanta-fran-turordningen/) 🟢 |
| **Re-employment priority** (LAS 25 §) | For 9 months after leaving, people with more than 12 months' service in the last 3 years have priority if we hire again | [LAS](https://data.riksdagen.se/dokument/sfs-1982-80.text) 🟢 |
| **Omställning / severance** | Check what the FAO agreements with Forena and the Saco unions provide. A negotiated package is the usual price of an orderly process. | 🔴 HR / GC |

**Option A timeline if the board decides in December 2026:** MBL negotiation in Jan–Feb 2027 → varsel in Feb → turordning lists and reassignment checks in Mar–Apr → individual notices in Apr–May → exits Jun–Oct, **averaging about 1 Sep 2027** → re-employment priority until mid-2028. The redundancies would be decided **before the AI is live**, because realistic go-live is mid-2027. **We would be cutting on faith.**

**The turordning effect on savings:** the shortest-serving staff leave. They are often the most digitally fluent, and they are usually the cheapest. At an assumed SEK 42,000 a month 🔴, each leaver costs SEK 716,034 loaded, against a team average of SEK 879,699. **Option A therefore saves 27 × 0.716 = SEK 19.3m a year, not SEK 23.8m.**

---

## 6. Option A vs Option B: cash flows (base case, SEK m)

### Option A: 27 compulsory redundancies, exits around 1 Sep 2027

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Average net capacity released while leavers are gone (FTE) | 3.2 | 8.2 | 13.8 | 15.7 | 15.7 |
| **Uncovered work (FTE)** | **23.8** | **18.8** | **13.2** | **11.3** | **11.3** |
| Payroll saving (27 × 0.716; 4/12 in 2027) | +6.4 | +19.3 | +19.3 | +19.3 | +19.3 |
| Cover: consultants at SEK 1.44m/FTE-yr to 2028, rehires at SEK 0.716m from 2029 🔴 | −11.4 | −27.1 | −9.4 | −8.1 | −8.1 |
| Severance (27 × 42,000 × 6 × 1.3142) and recruitment of rehires | −8.9 | 0 | −1.0 | 0 | 0 |
| Programme cost (one-off SEK 10.5m + run SEK 3.8m/yr) | −14.3 | −3.8 | −3.8 | −3.8 | −3.8 |
| **Net** | **−28.2** | **−11.5** | **+5.1** | **+7.4** | **+7.4** |

2027–29: **−SEK 34.6m** · 5-year: −SEK 19.8m · NPV at 8%: **−SEK 21.4m**

The uncovered work is real work: the Q4 close, the year-end accounts, the Q4 QRTs. If it is not covered, the cost does not disappear. It turns into control failures and missed deadlines that FI and the auditors will see.

### Option B: gated, attrition and redeployment first

Non-backfilled attrition = 90 × 8% 🔴 × 75% absorbable 🔴 = 5.4 FTE a year. Reduction = the lower of net capacity released and cumulative attrition. At end-2028, voluntary packages are offered only for proven surplus (1.2 FTE in base).

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| FTE reduction at year end | 4.5 | 10.8 (+1.2 voluntary) | 15.7 | 15.7 | 15.7 |
| Payroll saving (average reduction × SEK 0.803m) | +1.8 | +6.1 | +11.1 | +12.6 | +12.6 |
| Voluntary packages (6 months, team-average salary) | 0 | −0.5 | 0 | 0 | 0 |
| Programme cost | −14.3 | −3.8 | −3.8 | −3.8 | −3.8 |
| **Net** | **−12.5** | **+1.9** | **+7.3** | **+8.8** | **+8.8** |

2027–29: **−SEK 3.3m** · 5-year: +SEK 14.3m · NPV at 8%: **+SEK 8.3m** · run-rate from 2030: SEK 12.6m gross, SEK 8.8m net a year

**2027 is an investment year under either option.** The board should hear that from us now, not in the Q3 forecast.

### All scenarios (SEK m)

| | Bear | Base | Bull |
|---|---:|---:|---:|
| A: 2027 net | −37.6 | −28.2 | −18.0 |
| A: 2027–29 | −70.6 | −34.6 | +11.0 |
| A: 5-year NPV | −67.1 | −21.4 | +30.7 |
| B: 2027 net | −21.0 (−7.5 if stopped at Gate 1) | −12.5 | −7.2 |
| B: 2027–29 | −31.0 (−7.5 if stopped) | −3.3 | +11.0 |
| B: 5-year NPV | −31.9 (about −7.5 if stopped) | +8.3 | +39.1 |

Option B's bear figure assumes we ignore our own gate. The design stops at Gate 1. The exposure is then 25% of implementation + compliance set-up + 25% of change costs + 6 months of licences = **SEK 7.5m**.

**Where A is genuinely better:** in the bull case, A is about SEK 16.5m ahead in 2028 (+12.4 vs −4.1), because B pays voluntary packages that year and its savings start in 2029. B catches up in 2029, and the 3-year totals are identical (+11.0 each).

---

## 7. Sensitivity

**Option B, base: 5-year NPV (SEK m).** Rows scale every automatable share; columns are conversion.

| Automatable share × | Net FTE at steady state (70% conversion) | 55% | 70% | 85% |
|---|---:|---:|---:|---:|
| × 0.6 | 8.2 | −13.4 | −7.9 | −2.5 |
| × 0.8 | 12.0 | −6.7 | +0.6 | +7.4 |
| **× 1.0** | **15.7** | **0.0** | **+8.3** | **+14.7** |
| × 1.2 | 19.4 | +6.4 | +14.3 | +21.1 |
| × 1.4 | 23.2 | +11.5 | +19.6 | +27.1 |

Option B breaks even at roughly 80% of the base automation rates. Below that, the gates should scale the programme down before the losses in the top-left cells occur.

**Option A, base: 5-year NPV (SEK m).** Rows are the cost of covering uncovered work; columns are the leavers' average monthly salary.

| Cover cost per FTE-year | SEK 38,000 | SEK 42,000 | SEK 51,600 (team avg) |
|---|---:|---:|---:|
| SEK 1.00m | −14.7 | −11.1 | −2.6 |
| **SEK 1.44m** | −25.0 | **−21.4** | −12.9 |
| SEK 1.80m | −33.4 | −29.9 | −21.3 |

Option A stays negative in the base case across the whole grid. With **no severance at all**, base Option A is still −SEK 25.7m over 3 years (NPV −SEK 13.1m).

**Attrition, Option B base:** 5% → 3-year −SEK 7.6m, NPV +SEK 4.5m (larger voluntary programme in 2028) · 8% → −SEK 3.3m / +SEK 8.3m · 11% → −SEK 2.4m / +SEK 9.1m.

---

## 8. Regulatory and control requirements (both options)

- **DORA**, fully applicable to insurers since 17 January 2025 ([Clyde & Co](https://www.clydeco.com/en/insights/2025/01/dora-is-fully-applicable-what-do-you-need-to-know) 🟢). AI vendors are ICT third-party providers, so they need a register-of-information entry, DORA-compliant contract terms and an exit strategy. Financial reporting is likely to count as supporting a critical or important function, which brings stricter terms. Budget 2–4 months for this before production use. 🟡
- **Solvency II outsourcing.** FI must be notified before a critical or important function is outsourced. GC should confirm whether an AI-run reconciliation or reporting service counts as outsourcing. 🟡
- **EU AI Act.** AP, reconciliations and reporting are not in the Annex III high-risk list. The insurance entry there covers risk assessment and pricing in life and health insurance. 🟡 The AI-literacy duty already applies, and the training budget covers it. A provisional deal of 7 May 2026 would defer Annex III obligations to 2 December 2027, subject to formal adoption ([Hogan Lovells](https://www.hlc.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules) 🟢). That matters only if AI later moves into underwriting or pricing.
- **GDPR.** Supplier invoices and expense claims contain personal data, so expect a DPIA, data processing agreements and EU/EEA data residency. 🟡
- **External audit.** The auditors will test ITGCs and the controls around AI-assisted processes. Agree the approach with them before go-live, not at year end. 🟡
- **Reporting deadlines do not move.** Quarterly QRTs and annual SFCR/RSR are where a capacity gap shows up first.

---

## 9. Gates and kill criteria (Option B)

| Gate | When | Pass criteria (set targets after the January baseline) | If it fails |
|---|---|---|---|
| 0 | Board, Dec 2026 | Approve programme and pilot budget (about SEK 5m base). Freeze hiring into AP and reconciliation roles, backfilling on fixed-term contracts only. Inform the unions under MBL. | — |
| Baseline | Jan 2027 | 4-week activity baseline of hours by task, invoice volumes, touchless rate, auto-match rate, close days, error rates | — |
| 1 | Jun 2027 | AP touchless rate and reconciliation auto-match rate meet the pilot targets. Error rate at or below baseline. No audit or control findings. DORA contract signed. | Stop or rescope. Exposure about SEK 7.5m. |
| 2 | Dec 2027 | Measured gross release ≥ 7.5 FTE run-rate (base trajectory). Close at least 2 days faster. Start reporting use cases. | Hold at AP and reconciliations, re-plan |
| 3 | Sep 2028 | If measured release exceeds what attrition can absorb, negotiate voluntary packages (MBL) for that proven surplus only | Continue attrition-only |
| Every quarter | — | Report to the board the FTE released, **measured in hours, not taken from vendor claims**, and FTE reduced | — |

---

## 10. People plan

- **Redeploy first.** Fill the 2–4 AI/automation-ops roles, exception handling, control ownership and analytics from inside the team. These people know where the bodies are buried in our processes.
- **Retrain everyone.** Give AI literacy training to all 90 and deeper training to the 15–20 people who will run the tools. Turordning makes this necessary anyway, because whoever stays must be qualified for the remaining work.
- **Bring the unions in early.** Information under MBL, and co-designed pilots. This lowers legal risk and raises the conversion rate.
- **Consider a commitment of no compulsory redundancies from this programme in 2027.** Conversion is the most sensitive driver in the model, and people help automate their own work only when it does not cost them their job. Trade-off: the board gives up the option of a fast headcount headline it could not have had anyway.

**Evidence from companies that went first:** of the 39% of leaders who made AI-driven redundancies, 55% say they made wrong decisions ([Orgvue, 2025, 1,163 leaders](https://www.orgvue.com/news/55-of-businesses-admit-wrong-decisions-in-making-employees-redundant-when-bringing-ai-into-the-workforce/)) 🟢. Forrester predicts that half of AI-attributed layoffs will be quietly reversed ([Forrester](https://www.forrester.com/blogs/future-of-work-predictions-2026-whats-coming-for-work-and-the-workforce)) 🟡. Klarna said in 2024 that its AI assistant did the work of 700 agents. In 2025 it began hiring human agents again, after its CEO said the cost drive had "gone too far" ([Bloomberg](https://www.bloomberg.com/news/articles/2025-05-08/klarna-turns-from-ai-to-real-person-customer-service)), and its headcount reduction had come mostly through attrition ([Entrepreneur](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)) 🟢.

---

## 11. Risks

| Risk | Trigger | Consequence | Mitigation |
|---|---|---|---|
| Capacity gap (Option A) | Base case materialises after 27 have left | About 24 FTE of work uncovered in Q4 2027. SEK 11.4m in 2027 and SEK 27.1m in 2028 to cover it, or missed deadlines. | Do not cut ahead of measured capacity |
| Re-employment priority | Rehiring within 9 months of exits | We must offer the jobs back to the people we dismissed | Same |
| Slow savings (Option B, bull case) | Pilots beat plan | 2028 about SEK 16.5m behind Option A; level by 2029 | Gate 3 brings voluntary packages forward to H1 2028 if Gate 2 shows bull rates |
| Low attrition | Below 8% | Option B slower (5%: NPV +SEK 4.5m) | Larger voluntary programme at Gate 3 |
| Vendor or concentration risk | Vendor outage or exit | Manual fallback needs people who still know the process | DORA exit plan; keep process knowledge in-house |
| Model error in reporting | AI-suggested journal or commentary is wrong | Misstatement, audit finding, FI attention | Human sign-off on everything external; control design agreed with the auditors |

---

## 12. Critic pre-screen

- **Weakest point.** Every automation rate is an assumption, not a measurement of our processes. The base case could be wrong in either direction.
- **Missing perspective.** Business growth. If volumes grow, hires we avoid are savings too, and this model does not count them, so it is conservative. The board may also want visible decisiveness, so Option B has to come with equally concrete commitments: dates, gates and a 30%-by-2029 stretch target.
- **Cost if wrong.** If B is chosen and the bull case is true, about SEK 16.5m of 2028 savings is deferred and recovered in 2029. If A is chosen and the base case is true, about SEK 35m is lost over three years, plus operational and regulatory exposure that cannot be undone.
- **Proceed:** ✅ with the noted risks, after the placeholders are replaced with actuals.

**Peer verification still needed before the board meeting:** GC (reading of LAS and MBL, the FAO agreements, Solvency II outsourcing, DORA), HR (attrition, severance norm, a trial turordning list), CIO/CTO (automation rates, vendor shortlist, integration cost), COO (close and reporting capacity).

---

## 13. Assumption register

| # | Assumption | Value (bear / base / bull where relevant) | Tag | Replace with |
|---|---|---|---|---|
| 1 | Team split and salaries | see 2.2 | 🔴 | Payroll extract by sub-function |
| 2 | Pension cost, blended | 6.0% of salary | 🔴 | Actual FTP cost |
| 3 | Automatable share by area | see 3 | 🔴 | Pilot measurements |
| 4 | Conversion to removable FTE | 55 / 70 / 85% | 🔴 | Post-pilot process redesign |
| 5 | Realisation by end-2027 | 25 / 40 / 60% | 🔴 | Vendor plan + Gate 1 |
| 6 | AI-ops roles | 4 / 3 / 2 FTE | 🔴 | Operating model design |
| 7 | One-off cost | 15.5 / 10.5 / 6.7 SEK m | 🔴 | Vendor and integrator quotes |
| 8 | Run cost | 5.5 / 3.8 / 2.7 SEK m a year | 🔴 | Vendor quotes |
| 9 | Attrition, share absorbable | 8%, 75% | 🔴 | HR data, last 3 years |
| 10 | LIFO leaver salary | SEK 42,000 a month | 🔴 | Trial turordning list |
| 11 | Severance | 6 months | 🔴 | HR practice, FAO agreement |
| 12 | Cover cost | SEK 900/h × 1,600 h | 🔴 | Interim market quotes |
| 13 | Discount rate | 8% | 🟡 | Your hurdle rate |
| 14 | No wage inflation | 2026 prices | 🟡 | Conservative for savings |

The model (`ai-backoffice-model.xlsx`) holds every input on the Assumptions tab, and the calculations are live formulas. Change a blue cell and the scenarios and the Summary update.

---

## Sources

- Skatteverket, arbetsgivaravgifter 2026: https://skatteverket.se/arbetsgivaravgifter
- Lag (1982:80) om anställningsskydd: https://data.riksdagen.se/dokument/sfs-1982-80.text
- Lag (1974:13) om vissa anställningsfrämjande åtgärder: https://data.riksdagen.se/dokument/sfs-1974-13.text
- Arbetsförmedlingen, varsel: https://arbetsformedlingen.se/for-arbetsgivare/anmal-varsel-och-permittering
- Företagarna, turordning exemptions: https://www.foretagarna.se/juridisk-faq/uppsagning/hur-manga-anstallda-far-jag-undanta-fran-turordningen/
- SCB lönestatistik (2024): https://www.scb.se/hitta-statistik/sverige-i-siffror/lonesok/Search/?lon=ekonom and https://www.scb.se/hitta-statistik/sverige-i-siffror/lonesok/Search/?lon=controller
- Gartner, CFOs should reset AI expectations (Mar 2025): https://www.gartner.com/en/newsroom/press-releases/2025-03-25-gartner-says-cfos-should-reset-expectations-about-ais-impact-on-workforce-productivity-and-headcount
- Gartner, finance AI adoption (Nov 2025): https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025
- MIT NANDA via Fortune (Aug 2025): https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
- MIT Sloan, GenAI and accountants: https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-can-make-accountants-more-productive
- Orgvue (Apr 2025): https://www.orgvue.com/news/55-of-businesses-admit-wrong-decisions-in-making-employees-redundant-when-bringing-ai-into-the-workforce/
- Forrester, Predictions 2026: https://www.forrester.com/blogs/future-of-work-predictions-2026-whats-coming-for-work-and-the-workforce
- Bloomberg on Klarna (May 2025): https://www.bloomberg.com/news/articles/2025-05-08/klarna-turns-from-ai-to-real-person-customer-service
- Entrepreneur on Klarna: https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
- Clyde & Co, DORA: https://www.clydeco.com/en/insights/2025/01/dora-is-fully-applicable-what-do-you-need-to-know
- Hogan Lovells, AI Act omnibus deal: https://www.hlc.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules
