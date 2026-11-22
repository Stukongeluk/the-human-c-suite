# 2027 Budget Approach: Delivering the Board's 8% Opex Target

**For:** CFO, for the board meeting in about three weeks (week of 7 Dec 2026)
**Status:** Draft approach. All euro figures are illustrative until FP&A replaces them with actuals in week 1. The logic and formulas still hold.

**Tags used:** [VERIFIED] means it comes from your message or a cited source. [ASSUMED] means an illustrative input you need to replace. Confidence is rated High, Medium or Low.

---

## 1. Settle four definitions before building anything

The board's "8% lower" can mean very different amounts of work. Agree these with the CEO in week 1 and write them on page 1 of the board paper.

| Question | Why it matters | Illustrative impact | Recommendation |
|---|---|---|---|
| **Baseline:** 8% below 2026 actual (nominal), or 8% below the 2027 do-nothing budget? | Payroll cost rises on its own. CPB expects business labour cost per employee to rise 4.4% and inflation to be 2.7% in 2027 [VERIFIED: CPB MEV 2027 via AWVN] | 2027 do-nothing opex is €74.8M. 8% below 2026 actual (€66.2M) needs **€8.5M (11.4%)** of action. 8% below do-nothing (€68.8M) needs **€6.0M** | Pick one explicitly. If the board means nominal against 2026, show them the €8.5M |
| **Timing:** full-year 2027 opex, or the exit run-rate in Q4 2027? | No Dutch redundancy takes effect on 1 January (see section 5). Savings phase in | A blanket cut gives about 4.6% on a full-year basis. Hitting 8% full-year that way needs about **107 people out by July**, not 48 | Commit to 8% as exit run-rate, with a stated full-year 2027 number (about 5%) |
| **Scope of "opex":** total operating cost including delivery staff, or overhead only? | Payroll at 68% of opex in a 600-person services firm suggests delivery staff are included [ASSUMED] | If opex means overhead only, the revenue-loss problem below shrinks, but the whole 8% then lands on support functions | Confirm. This document assumes delivery staff are included |
| **Objective:** is lower opex the goal, or higher EBIT? | An opex cut that cuts revenue by the same amount leaves EBIT unchanged | See section 3 | Keep the opex target and add an **EBIT floor** as a guardrail |

---

## 2. Illustrative baseline (replace with actuals)

| Item | Value | Basis |
|---|---|---|
| FTE | 600 | [VERIFIED: you] |
| Payroll share of opex | 68% | [VERIFIED: you] |
| Revenue | €75.0M (€125k per FTE) | [ASSUMED] |
| EBIT | €3.0M (4.0%, "thin but positive") | [ASSUMED] |
| Opex (all operating cost, delivery staff included) | €72.0M | derived |
| Payroll | €48.96M, so €81.6k loaded cost per FTE | derived |
| Non-payroll | €23.04M: subcontractors €6.0M (resold at +15%, giving €6.9M revenue) and other €17.04M | [ASSUMED split] |
| Billable / support FTE | 480 (80%) / 120 | [ASSUMED] |
| Own-staff revenue per billable FTE | €141.9k = (€75.0M − €6.9M) / 480 | derived |
| Utilisation | 72% of 1,650 available hours = 1,188 billed hours, at a realised rate of about €119/h | [ASSUMED] |
| Bench (unassigned billable capacity) | about 6% of billable, roughly 29 FTE-equivalents | [ASSUMED] |
| Voluntary attrition | 12%, about 72 leavers a year (58 billable, 14 support) | [ASSUMED] |
| One-off cost per forced exit | €25k all-in | [ASSUMED]: statutory transitievergoeding of about €10.5k (6 years' service at €5.2k/month), plus a social plan top-up, legal and outplacement |
| Forced exits take effect | about 1 July 2027, so 50% of the payroll saving lands in 2027. Non-payroll: 75% | [ASSUMED] |

---

## 3. Why a blanket cut fails in a services P&L

### 3.1 The break-even rule (confidence: High; it is arithmetic)

When you cut a billable person, you save their cost and lose the revenue they bill.

```
ΔEBIT per billable FTE removed = loaded cost − revenue per FTE × (1 − absorption)
Break-even utilisation          = loaded cost ÷ (realised rate × available hours)
                                = €81,600 ÷ (€119 × 1,650) = 41.6%
```

*Absorption* is the share of the cut person's billed hours that colleagues pick up.

| Absorption by colleagues | ΔEBIT per average-utilised billable FTE cut |
|---|---|
| 0% | €81.6k − €141.9k = **−€60.3k** |
| 30% | €81.6k − €99.3k = **−€17.7k** |
| 50% | €81.6k − €71.0k = **+€10.6k** |

**So what:** cutting billable capacity improves EBIT only where people are utilised below about 42%, or where colleagues have the slack to absorb most of their work. A uniform percentage per cost centre ignores both. It cuts the busy practice as hard as the idle one.

### 3.2 Blanket 8%, worked through (run-rate)

| Line | Opex | Revenue | EBIT |
|---|---|---|---|
| Payroll −8%: 48 FTE (38.4 billable, 9.6 support) | −3.92 | | +3.92 |
| Subcontractors −8% | −0.48 | −0.55 | −0.07 |
| Other non-payroll −8% | −1.36 | | +1.36 |
| Revenue lost on 38.4 billable FTE at average utilisation (no absorption / 30% absorbed) | | −5.45 / −3.81 | −5.45 / −3.81 |
| **Total (€M)** | **−5.76 (8.0%)** | **−6.00 / −4.37** | **−0.24 / +1.39** |

The board thinks it is buying €5.8M of profit. On these numbers it gets between −€0.2M and +€1.4M.

Why assume average utilisation? Under the Dutch UWV route, people are selected by the afspiegelingsbeginsel (proportional selection by age group and length of service within interchangeable roles), not by utilisation or performance [VERIFIED: Rijksoverheid].

### 3.3 Sensitivity: blanket cut run-rate EBIT change (€M)

| Utilisation of the billable staff cut, vs average | 0% absorbed | 30% absorbed | 50% absorbed |
|---|---|---|---|
| 100% (average) | −0.2 | 1.4 | 2.5 |
| 75% | 1.1 | 2.3 | 3.2 |
| 50% | 2.5 | 3.3 | 3.8 |
| 0% (all idle; unrealistic under afspiegeling) | 5.2 | 5.2 | 5.2 |

Even the best case stays below €5.8M, because cutting subcontractors also cuts the revenue you resell them at.

### 3.4 Blanket 8% in 2027 itself (central case, 30% absorption)

```
Payroll saving      50% × 3.92 = +1.96
Non-payroll saving  75% × 1.84 = +1.38
Revenue lost        50% × 3.81 = −1.91
Resold revenue lost 75% × 0.55 = −0.41
One-offs            48 × €25k  = −1.20
2027 EBIT change               ≈ −0.18   (range −1.00 to +0.36 across 0–50% absorption)
2027 opex change               −3.34 = −4.6% before one-offs
```

### 3.5 What else a uniform cut does

- **It rewards padded budgets and punishes lean ones.** The centre with slack hits 8% painlessly. The lean centre cuts muscle.
- **It forces people cuts wherever costs are fixed.** A centre whose non-payroll is mostly a lease can only reach 8% by cutting people harder.
- **It cuts investment and waste at the same rate.** Training that wins tenders gets the same cut as unused software licences.
- **It tends to come back next year.** Nothing structural changes, so the gap reopens. One correctly sized decision beats two rounds, which hurt morale more than a single decisive one.
- **It falls on recent hires.** Within each age group the shortest-serving go first, and those are often the juniors and specialists you just paid recruitment fees for.

### 3.6 What the CEO is right about

A uniform cut is quick to decide, easy to communicate, feels fair, and avoids budget-holder politics. The recommended design keeps those qualities. It is still one number and a few rules, but the number is allocated by what drives each cost.

---

## 4. Recommended approach: one envelope, three rules

**The envelope:** €5.8M run-rate opex reduction company-wide (8%), with an EBIT floor.

**Rule 1: Billable teams are budgeted from demand, not a percentage.**
```
Billable FTE required = 2027 demand hours (backlog + weighted pipeline) ÷ (available hours × target utilisation)
```
Capacity above that requirement (plus a small buffer) is used up in this order:
(a) insource subcontracted work onto it, (b) don't backfill leavers, (c) move people internally, (d) targeted exits, as a last resort.

**Rule 2: Support functions and non-payroll get tiered targets.**
In one exec calibration session, put every cost centre in one of three tiers: **Protect** (0–3%), **Standard** (8%) or **Harvest** (12–20%). The tiers must add up to the envelope. The CEO decides the tiers, which keeps it simple and keeps the politics out of individual negotiations.

**Rule 3: Don't cut anything that pays back within the year.**
See the protect list below. Every backfill needs sign-off: the practice lead signs against the demand plan for billable roles, and the CFO or CEO signs for support roles.

### 4.1 Lever plan (illustrative)

| # | Lever | Mechanism | Run-rate €M | 2027 €M | Forced exits | Confidence |
|---|---|---|---|---|---|---|
| 1 | Insource subcontracted work | As contracts end, replace about €2.0M (a third) of subcontractor spend with your own unassigned staff. Client billing is unchanged. Needs about 16 FTE-equivalents of matching bench | 2.00 | 1.40 (70%) | 0 | Medium-Low: the skills match is unverified |
| 2 | Size billable capacity to demand | −12 FTE in practices where 2027 demand is below capacity at break-even. Achieved by not backfilling some of the ~58 billable leavers, internal moves, and exits only as a last resort | 0.98 | 0.49 (50%) | 0–3 | Medium |
| 3 | Support functions −12% | −14 of 120 FTE: about 10 by not backfilling, about 4 role eliminations, plus process simplification. Support-to-billable ratio falls from 25.0% to 22.6% | 1.14 | 0.57 (50%) | 3–7 | Medium |
| 4 | Discretionary non-payroll −10% | Zero-base travel, events and marketing that don't show pipeline, software licences under 30% use, and professional fees. Renegotiate top vendors | 1.70 | 1.28 (75%) | 0 | Medium-High |
| | **Total** | | **5.83 (8.1%)** | **3.74 (5.2%)** | **~5–10** | |

- **One-offs:** €0.3–0.5M (5–10 exits at €25k, plus about €0.2M for process and automation work).
- **2027 EBIT change:** about +€3.3–3.4M.
- **Bench used:** levers 1 and 2 together use about 28 of the ~29 assumed bench FTE-equivalents. Check this first.

**Delivery sensitivity:**

| Share of the plan delivered | Run-rate €M | 2027 EBIT change incl. one-offs €M |
|---|---|---|
| 100% | 5.8 | +3.4 |
| 75% | 4.4 | +2.5 |
| 50% | 2.9 | +1.5 |

Even at 50% delivery, this plan beats the central blanket case (−€0.2M) in 2027.

### 4.2 Contingency levers (not counted in the commitment)

| Lever | Size | Note |
|---|---|---|
| Pass the wage increase through to client rates | €0.75M EBIT per 1% average rate | Check indexation clauses. This is the fastest margin lever, but it is revenue, so keep it out of the opex number |
| Utilisation +1 percentage point, where demand exists | about €0.95M revenue at near-zero marginal cost | Revenue lever |
| H1 freeze on discretionary spend and non-critical internal projects | Size in week 2 | One-off. Bridges the timing gap |
| Cap merit and promotion budget above the CAO | about €0.5M per 1% of payroll | Retention risk in scarce skills, so apply selectively |
| Office space at lease breaks; lease cars to a mobility budget | Depends on lease dates | Mostly a 2028 effect |

### 4.3 Protect list

- Sales and business-development capacity, and the account leads on your top clients
- Billable capacity in practices running above break-even utilisation where demand exists
- Certifications and training that clients require in tenders
- Junior and trainee intake: reduce it if demand says so, but don't stop it. It is your delivery pyramid and your cheapest leverage
- Recruitment for skills you currently buy from subcontractors at a premium

### 4.4 Options for the board paper

| | A: Blanket 8% per cost centre | B: One envelope, three rules |
|---|---|---|
| Run-rate opex | −€5.76M | −€5.83M |
| Run-rate revenue | −€4.4M to −€6.0M | about zero |
| Run-rate EBIT | −€0.2M to +€1.4M | +€5.8M |
| 2027 full-year opex | −4.6% | −5.2% |
| 2027 EBIT incl. one-offs | about −€0.2M | about +€3.4M (+€1.5M at 50% delivery) |
| Forced exits | about 48: collective-dismissal rules, afspiegeling | about 5–10 |
| One-off cost | about €1.2M | €0.3–0.5M |
| Time to build | Days | Two more weeks of analysis |
| Easy to communicate | Yes | Yes, if framed as "one envelope, three rules" |

---

## 5. Phasing, one-off costs and the Dutch process

**What applies** (confirm the route with your employment lawyer):

- **Works council (OR) advice.** The OR has advisory rights on an important change to the organisation, possibly combined with a change in staffing. The request for advice must describe the proposed decision, its reasons, the expected effects on employees and the planned measures. It must be submitted while the OR can still have substantial influence, so the decision is still only proposed at that point [VERIFIED: AWVN].
  - If the final decision deviates from the OR's advice, you must suspend it for one month, and the OR can appeal to the Ondernemingskamer [ASSUMED from general knowledge; Medium; GC to confirm].
- **Collective dismissal.** This applies when 20 or more employees are dismissed within 3 months in one work area, by any route, including mutual agreement. For dismissals on business-economic grounds, the afspiegelingsbeginsel applies [VERIFIED: Rijksoverheid].
  - You must notify UWV and the unions before dismissing anyone, and ask the OR for advice.
  - A one-month waiting period starts once UWV confirms the notification is complete, unless the unions confirm in writing that they agree. It also applies to termination agreements [VERIFIED: UWV].
- **Transitievergoeding (statutory severance).** One-third of monthly salary per year of service, with holiday pay included. The maximum is €102,000 from 1 January 2026, or one year's salary if that is higher [VERIFIED: Rijksoverheid].
  - Notice periods run 1–4 months depending on length of service [ASSUMED from general knowledge; GC to confirm].
- **Vacancy freeze.** Not filling a vacancy usually needs no OR advice on its own. Because it is part of this plan, present it to the OR as such [ASSUMED; GC to confirm].

**Realistic sequence:**

| When | Step |
|---|---|
| Dec 2026 | Board approves the envelope and the proposed organisational changes |
| Jan 2027 | Request for OR advice. Vacancy freeze and non-payroll levers start immediately |
| Feb–Mar | OR advice. If 20 or more exits: UWV and union notification, one-month wait, social plan |
| Mar–Apr | UWV permits or settlement agreements |
| May–Jul | Exits take effect after notice periods |

The blanket option goes through every step. The targeted option mostly runs on attrition from January and probably stays below the collective-dismissal threshold.

---

## 6. Three-week plan to the board

| Week | Action | Owner | Deadline |
|---|---|---|---|
| 1 | Quick data pull: payroll split billable/support, utilisation and bench by practice | FP&A lead | Tue 24 Nov |
| 1 | CEO one-to-one: walk through the break-even rule on your own numbers, agree to bring a joint proposal | CFO | Wed 25 Nov |
| 1 | Full baseline: 2026 forecast by cost centre, 2027 do-nothing (CAO, indexation), subcontractor spend by skill and end date, lease and contract dates | FP&A lead | Fri 27 Nov |
| 1 | 2027 demand plan (backlog + weighted pipeline) by practice and skill; which subcontract roles the bench can take over | CRO / COO with practice leads | Fri 27 Nov |
| 1 | Attrition by function, open vacancies, age and tenure by function category (afspiegeling exposure) | CHRO | Fri 27 Nov |
| 1 | Memo on the legal route: OR advice scope and timing, collective-dismissal exposure | GC / employment lawyer | Fri 27 Nov |
| 2 | Budget-holder sessions. Each brings what 8% would mean, their ranked levers, and what they would protect and why | CFO with budget holders | Wed 2 Dec |
| 2 | Exec calibration: assign tiers, accept levers with confidence ratings | CEO (decides), CFO | Thu 3 Dec |
| 2 | Model options A vs B, sensitivities, 2027 P&L bridge, one-offs | FP&A lead | Fri 4 Dec |
| 2 | Plan for OR engagement and internal communication | CHRO, GC | Fri 4 Dec |
| 3 | Board pre-read sent, at least five working days before the meeting | CFO | Mon 7 Dec |
| 3 | Pre-brief the board chair (and audit committee chair) | CEO, CFO | Wed 9 Dec |
| 3 | Manager and OR communication script ready for the day after the board | CHRO | Before the board meeting |

---

## 7. Board paper outline (at most 8 pages plus appendix)

1. **Decision requested** (one page)
2. **Target definition:** baseline, timing, scope, EBIT floor
3. **Options considered:** A (blanket) and B (envelope plus three rules), with the table from section 4.4
4. **Recommended plan:** levers, owners, confidence, protect list
5. **2027 P&L bridge:** phasing and one-offs
6. **People and process:** OR, unions, communication
7. **Risks, contingency levers and triggers**
8. **Quarterly tracking**
- **Appendix:** allocation by cost centre, sensitivities, assumptions register

**Draft resolution:**
> The board (1) sets the 2027 cost target as a €[5.8]M reduction in annualised opex against [2026 actual / the 2027 baseline], to be reached by the Q4 2027 exit run-rate, with 2027 full-year opex at or below €[X]M and EBIT at or above €[Y]M; (2) approves allocating the reduction by cost driver as set out in the paper, not as a uniform percentage; (3) approves a one-off restructuring provision of up to €[0.5]M; (4) notes that any resulting organisational change is a proposed decision subject to the advice of the works council; (5) asks management to report run-rate savings and the agreed KPIs quarterly.

---

## 8. Tracking and decision triggers (define them now, not mid-year)

**Quarterly KPIs:**
- Run-rate savings delivered vs plan
- Utilisation and bench % by practice
- Subcontractor share of delivery hours
- Revenue per FTE
- Realised rate vs indexation
- Support-to-billable ratio
- Regretted attrition
- EBIT vs the floor

**Triggers:**

| If... | Then... |
|---|---|
| Run-rate savings are below 70% of plan at the end of Q2 | Activate the contingency levers (section 4.2) |
| A practice runs below break-even utilisation for two consecutive quarters | Review its capacity under Rule 1 |
| Regretted attrition in a practice runs above plan | Pause non-backfill there |
| Demand falls more than 5% below plan | Re-size billable capacity (Rule 1 does this automatically) |

---

## 9. Checks before this goes to the board

**Peer verification needed:**

| Who | What they check |
|---|---|
| CHRO | Attrition assumption (12%), whether non-backfill is feasible, social plan cost, afspiegeling exposure |
| GC / employment lawyer | OR advice scope and timing; collective-dismissal route; whether the vacancy freeze and insourcing need advice |
| CRO and practice leads | Demand plan; whether the bench can take over subcontract roles |
| COO | Delivery risk from insourcing and support reductions |

**Critic pre-screen:**
- **Weakest point:** the biggest lever, insourcing (€2.0M, 34% of the plan), rests on a skills match between bench and subcontractors that nobody has checked.
- **Missing perspective:** clients, who sometimes asked for named subcontractors; and the OR, which can add weeks to any plan.
- **If wrong, the cost is:** a run-rate shortfall of about €1–2M. Close it with the contingency levers; pricing alone is worth €0.75M per 1%.
- **Proceed:** only after validating the insourcing lever in week 1, before the number goes into the board paper.

---

## 10. Sources

- CPB MEV 2027 forecasts (CAO wages 3.8%, business labour cost per employee 4.4%, inflation 2.7% in 2027): [AWVN, "MEV 2027: wat werkgevers ervan moeten weten"](https://www.awvn.nl/nieuws/mev-2027-wat-werkgevers-ervan-moeten-weten/)
- Collective dismissal threshold, routes counted, afspiegelingsbeginsel: [Rijksoverheid, Collectief ontslag](https://www.rijksoverheid.nl/onderwerpen/ontslag/collectief-ontslag)
- UWV and union notification, OR advice, one-month waiting period: [UWV, Meld collectief ontslag](https://www.uwv.nl/werkgevers/werkgever-en-ontslag/ik-wil-ontslag-aanvragen/detail/collectief-ontslag/meld-collectief-ontslag)
- OR advisory right on reorganisation and its timing: [AWVN, Adviesrecht ondernemingsraad bij reorganisatie](https://www.awvn.nl/medezeggenschap/awvn-werkgeverslijn/vraag-van-de-week/adviesrecht-ondernemingsraad-reorganisatie/)
- Transitievergoeding calculation and 2026 maximum: [Rijksoverheid, Hoe hoog is de transitievergoeding](https://www.rijksoverheid.nl/onderwerpen/ontslag/vraag-en-antwoord/hoe-hoog-is-de-transitievergoeding-als-ik-word-ontslagen); [Rendement, Maximale transitievergoeding 2026](https://www.rendement.nl/transitievergoeding/nieuws/maximale-transitievergoeding-is-in-2026--102000.html)
