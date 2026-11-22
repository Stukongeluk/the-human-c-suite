# AI and the finance/back-office team: the business case

## Bottom line

I built the case, but not as "AI replaces 30% next year." I can't make that number hold up, and a board paper that says so will fail the first hard question from an audit committee member or the unions. What I can build is a case where 30% (27 of 90 FTE) is the ceiling scenario. A staged reduction of 12-16% inside 12 months, rising toward 25-30% over 24-36 months, is what I'd defend.

- **Year 1 is cash-negative in every scenario.** One-off costs (build, integration, parallel running, exit costs) land before the savings do. Savings only start once the new process has run clean through a month-end and a quarter-end.
- **Run-rate savings are real.** In my illustrative model the 30% scenario saves roughly SEK 11M a year net, and the base case roughly SEK 6M.
- **Calendar and law cap the speed.** In Sweden you can't announce a cut and execute it next quarter. Consultation obligations and notice periods put the first exits around month 6-9 at the earliest.

Confidence: medium on structure and direction. Low on the SEK figures, which rest on my assumptions below. Please replace them with your actuals.

## 1. What 30% means

- 30% of 90 is 27 FTE.
- At an assumed loaded cost of about SEK 750k per FTE, that is about SEK 20M a year in gross cost.
  - Basis: SEK ~520k salary + 31.42% employer contributions + ~8-10% pension and insurance. 🔴 assumed.
- The gross figure is not the saving. Subtract the run cost of the AI/automation stack, the people you keep to supervise it, and the one-off costs.

## 2. Where the 30% could come from

This split is my assumption, since I have no process data. Test each line against your own volumes and exception rates. 🔴 assumed.

| Area | Typical addressable share | Why |
|---|---|---|
| Accounts payable (invoice capture, coding, matching, payment runs) | 35-50% | Mature tooling. The tail of exceptions and supplier queries stays human. |
| Reconciliations (bank, intercompany, sub-ledger to GL) | 30-45% | Rule-based matching works. Breaks need judgement. |
| Management and regulatory reporting (first drafts, commentary, data prep) | 15-25% | Drafting is easy. Review, sign-off and Solvency II / IFRS 17 judgement are not. |
| Claims-related back-office finance (reserving inputs, reinsurance accounting) | 10-20% | Heavier controls, and errors are more costly. |

If the roughly 90 FTE split about 30 / 25 / 20 / 15 across these areas (the rest being management and other), a blended 30% would need nearly the top of every range, in every area, within a year. That is why I treat it as a stretch case.

## 3. Scenarios (SEK, illustrative)

Assumptions:
- Loaded cost SEK 750k per FTE.
- Exits phased from about month 8. Year 1 therefore captures about 30% of run-rate savings.
- Exit cost about 6 months of loaded cost per person leaving by redundancy (notice, collective-agreement support). This falls to near zero for people lost through attrition or redeployed.
- One-off costs: build, integration with ERP and claims systems, data work, parallel running, controls testing.

| | Conservative | Base | Board target |
|---|---|---|---|
| FTE reduction | 7 (8%) | 14 (15%) | 27 (30%) |
| Gross run-rate saving | 5.3M | 10.5M | 20.3M |
| Run cost of AI stack and oversight | 2.5M | 4.5M | 9.0M |
| Net run-rate saving | 2.8M | 6.0M | 11.3M |
| One-off build and integration | 6M | 12M | 26M |
| Exit cost (if all by redundancy) | 2.6M | 5.3M | 10.1M |
| Year 1 net | about -8.6M | about -16.8M | about -35.5M |
| Cumulative break-even | year 3-4 | year 3-4 | year 4+ |

Three things follow:
1. **The 30% case costs the most and pays back the slowest.** It needs the most integration and the most exits, and it carries the most execution risk. It is the largest bet.
2. **Attrition changes the economics.** If your finance turnover is around 8-12% a year (to be confirmed with HR), 7-11 roles open up naturally each year. Closing those roles, plus redeploying people, avoids most exit cost and most of the legal and reputational risk. Applied to the base case, it cuts year-1 cost by about SEK 2.5M and removes the redundancy process for half the roles.
3. **The numbers are very sensitive** to three inputs: the one-off cost, the share of work that is truly automatable, and the timing of exits. A 6-month slip in exits removes most of year-1 savings.

## 4. Swedish and insurance-specific constraints

Please have legal and HR confirm these. I am flagging them from general knowledge, not from your collective agreements. 🟡

- **Co-determination (MBL).** An employer must negotiate with the unions before major changes to the business and before decisions on redundancies. A decision taken before negotiation is a legal exposure. Allow 2-4 months.
- **Redundancy rules (LAS).** Redundancy needs objective grounds, and selection follows a seniority-based order of priority within each unit, unless you agree otherwise with the union. You cannot simply "pick the roles AI replaces" or the weakest performers. Notice runs 1-6 months by tenure.
- **Notification.** Large redundancy rounds need advance notice to the Swedish Public Employment Service. Many insurers use transition-support arrangements through collective agreements.
- **DORA and outsourcing.** Putting AI vendors into finance processes creates ICT third-party risk. Insurers need register, contract and exit-plan work. Budget for it.
- **Controls and audit.** Financial reporting controls (SOX-like internal control, Solvency II governance, IFRS 17) must be re-documented when a person is replaced by a model. Your auditors and the actuarial and risk functions will want to see this before go-live.
- **EU AI Act and GDPR.** Most finance back-office uses are not in the high-risk category. AI-literacy duties still apply, and any use touching customer or employee personal data needs a GDPR review.

## 5. Risks the board should see

- **Error cost.** An AP or reconciliation mistake is cheap. A wrong reserve input or regulatory report is not. Keep human review wherever the exposure is large.
- **Hollowing out.** If you remove the junior roles, you lose the people who grow into the senior ones. Check what the 30% does to your finance succession plan in 3-5 years.
- **Key-person and knowledge loss.** Departing staff hold the exception knowledge that the automation needs in order to work.
- **Morale.** Announcing a 30% target to 90 people triggers attrition among the people you want to keep, before any automation has been proven.
- **Vendor dependence** and model drift, which need a named owner.

## 6. What I recommend the board approves

1. **Quarter 1: measure, don't promise.** Process-mine and time-sample the actual work in AP, reconciliations and reporting. Establish volumes, touch time, exception rates and cost per invoice and per reconciliation. This turns my assumed split into your data.
2. **Quarters 1-2: pilot AP and one reconciliation stream** in parallel running. Set the exit criteria in advance: for example straight-through rate, error rate against the human baseline, and no new audit findings across a quarter-end.
3. **Hiring freeze on addressable roles now, and redeploy.** This is the cheapest and fastest lever. It starts delivering before the AI does.
4. **Open the MBL process early,** with the transformation plan rather than a headcount number.
5. **Stage-gate the target.** Approve the base case (about 15%), and commit to a decision on moving toward 25-30% only once the pilots meet their criteria. Present 30% as the upside scenario with the stated conditions.

Suggested decision triggers, to be set now rather than during a crisis:
- Straight-through AP rate below the plan by more than 10 points at month 6: stop expanding.
- Any audit or regulatory finding traced to the automation: pause and fix.
- Net run-rate savings tracking below 70% of plan at month 12: reassess the target.

## 7. What I need to firm this up

- Actual FTE and cost by team (AP, reconciliations, reporting, other), including contractors and consultants.
- Volumes: invoices per month, bank lines, number of reconciliations, report packs, and current exception rates.
- Current tooling and ERP (which determines the integration cost).
- Annual attrition and the average tenure of the 90 people.
- The collective agreements that apply.
- Any vendor quotes you already have.

## Your decision

The board asked for a case that AI can replace 30%. The honest answer is that AI can plausibly remove 12-16% of this team's work next year, and possibly 25-30% over two to three years if the pilots hold. I'd take that to the board as the plan, with 30% as the stated upside. Do you want me to turn this into a board paper with the staged plan, once you have the actual data from section 7?
