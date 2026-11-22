# Business case: AI in finance and back-office (90 FTE)

I built the case so it holds up when the board, the unions and the auditors read it. That meant testing the 30% target before presenting it. My finding is that 30% (27 FTE) is reachable, but probably not as a net, in-year saving. A case that promises it in 12 months is the one most likely to fail under challenge. Below is what I would put in front of the board.

All numbers are planning assumptions I chose, because I have none of your data. They are marked (A). Replace them with your actuals before this goes anywhere. I have not seen your process volumes, tooling, ERP or headcount by role.

## 1. Recommendation

Present a staged target, not a single 30% number.

| Scenario | Capacity released by end of next year (run-rate) | By end of year 3 | Confidence |
|---|---|---|---|
| Conservative | 8-10 FTE (9-11%) | 15-18 FTE | High |
| Base | 12-16 FTE (13-18%) | 22-27 FTE (25-30%) | Medium |
| Stretch (board ask) | 27 FTE (30%) | n/a | Low |

The reasons 30% in 12 months is the stretch case:

1. **Time.** Selecting a vendor, integrating with the ERP and core insurance systems, running parallel controls for a quarter or two, and then releasing people takes most of a year. Most savings arrive in year 2.
2. **Swedish employment law.** A reduction of this size means redundancy notices (uppsägning på grund av arbetsbrist) under LAS. That involves:
   - negotiation obligations towards the unions under MBL before the decision is taken;
   - notice periods of 1-6 months depending on tenure;
   - last-in-first-out ordering (turordning) within the collective bargaining unit, which means you cannot choose which roles go. The people who leave are the shortest-tenured, not the ones whose tasks were automated;
   - sector agreements on redundancy support, and possibly a notification to the Arbetsförmedlingen if numbers are large.
   Confirm the exact obligations with employment counsel. Natural attrition and redeployment are faster and cheaper, and they avoid turordning problems.
3. **Regulation.** As an insurer you are under Finansinspektionen oversight. AI in financial reporting and reconciliations touches:
   - DORA (ICT risk and third-party/cloud providers);
   - the EU AI Act, where applicable, with deadlines to check;
   - GDPR where personal data is processed;
   - Solvency II reporting controls and your internal control framework, with auditor sign-off.
   Replacing a human control with a model-driven one needs documented validation. That slows the reporting and reconciliation work in particular.

## 2. Where the capacity is (illustrative split of 90 FTE, A)

| Area | FTE (A) | Realistic automation of effort | Released FTE |
|---|---|---|---|
| Accounts payable (invoice capture, coding, matching, payment runs) | 22 | 40-55% | 9-12 |
| Reconciliations (bank, intercompany, premium/claims sub-ledgers) | 18 | 30-50% | 5-9 |
| Reporting (management, statutory, regulatory data prep) | 20 | 15-30% | 3-6 |
| Other back-office (claims admin support, collections, master data) | 15 | 15-30% | 2-4 |
| Controllers, accounting leads, regulatory/actuarial interface | 15 | 0-10% | 0-1 |
| Total | 90 | | about 19-32 |

Read this as a range. Reaching 27 requires the top of nearly every row. AP and reconciliations are where the evidence is strongest. Reporting is weaker because most of that time goes to judgement, explanation, and answering questions from auditors and regulators. AI helps there with drafting and variance commentary, but it does not remove the reviewer.

## 3. Financials (all A, SEK, three-year view)

Assumptions:
- Fully loaded cost per FTE: SEK 800k (salary plus employer contributions around 31%, pension, overhead).
- Base scenario: 14 FTE released in year 1 (run-rate by year end, so only about 40% of the saving lands in-year), 25 FTE by year 3.

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Released FTE (run-rate, end of year) | 14 | 20 | 25 |
| Realised labour saving | 4.5m | 14m | 18m |
| One-off: implementation, integration, data cleanup | -7m | -3m | 0 |
| Recurring: licences, cloud, model usage | -2m | -3m | -3m |
| Governance, validation, monitoring, audit support (2-3 FTE equivalent) | -2m | -2m | -2m |
| Redundancy, notice and transition cost (about 0.5-1.0x annual cost per leaver where used) | -4m | -3m | -1m |
| **Net** | **-10.5m** | **+3m** | **+12m** |
| Cumulative | -10.5m | -7.5m | +4.5m |

Payback in about year 3 in the base case. If attrition covers most of the reduction, redundancy cost falls sharply and payback moves into year 2. The full 30% in year 1 would show roughly SEK 21.6m annual saving at run-rate, but with the same one-off costs and almost none of the in-year benefit. It does not pay back within the year.

The main sensitivities, in order of impact: speed of release, redundancy cost per leaver, rework and exception rates after go-live, and run costs of the AI components.

## 4. Risks the board should see

- **Error and control risk.** An AP or reconciliation model that is 98% accurate still sends wrong payments and misses breaks. Keep human review on exceptions and on material items, and measure error rates against today's baseline.
- **Fraud and payment risk.** Automated invoice processing raises exposure to invoice fraud and manipulation. Segregation of duties still applies.
- **Key-person and knowledge loss.** The people automation targets often hold the undocumented rules (accrual logic, claims edge cases). Capture them before anyone leaves.
- **Vendor and concentration risk.** DORA requires an exit plan and a register for critical ICT third parties.
- **Auditor and regulator acceptance.** If the external auditor does not accept the new controls, the manual process stays and the saving does not happen. Engage them early.
- **Morale and retention.** A public 30% target makes your best people leave first, which is the opposite of what you want. Announce it only after the plan, the union process and the redeployment options are ready.
- **Hidden demand.** Faster processing often creates new work (more reporting requests, more analysis). Decide in advance what freed capacity is for.

## 5. How to get to the number responsibly

1. **Weeks 0-6: baseline.** Measure volumes, touch time, exception rates and cost per invoice, per reconciliation and per report. Without this the savings cannot be verified.
2. **Weeks 6-12: select and pilot.** Start with AP (invoice capture, coding, three-way match) and bank/sub-ledger reconciliation. Run in parallel with the manual process.
3. **Quarters 2-3: scale.** Move to production with exception queues and human sign-off thresholds. Agree controls with the auditor.
4. **Quarters 3-4 onward: release capacity** through hiring freezes, attrition, redeployment into controlling, analytics and AI oversight roles, and retraining. Start MBL negotiations early if redundancies are likely.
5. **Gate each step on measured results.** Release headcount against realised, audited savings, not forecast ones.

Redeployment deserves weight in the case. Moving people into exception handling, controls, analytics and model oversight keeps the knowledge you need, lowers redundancy cost and makes the programme easier to defend.

## 6. What I need from you to firm this up

- Headcount, cost and tenure by team, and the collective agreement coverage.
- Annual volumes: invoices, reconciliations, reports, and current exception and error rates.
- Systems landscape (ERP, claims/policy platforms) and any automation already in place.
- Expected attrition (last 3 years) and hiring plans.
- Whether the board's 30% is a cost target, a capacity target, or both, and the deadline.

## 7. Suggested wording for the board

"We can release 25-30% of finance and back-office capacity within three years, with 13-18% achievable in the first year, subject to measured pilot results, auditor acceptance and the legally required employee-representation process. The programme reaches payback in year 2-3. We recommend approving phase 1 (baseline and AP/reconciliation pilots) now, with headcount decisions gated on results."

If it helps, I can turn this into a board deck or a spreadsheet model with the scenarios and sensitivities once you share your actual figures.
