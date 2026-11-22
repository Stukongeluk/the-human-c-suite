# AI business case for the finance and back-office team (90 FTE)

## Bottom line

I built the case, but I can't build it to say "30% in one year". The numbers support a smaller first-year reduction and a 3-year path toward the board's target. Putting 30% in front of the board as a year-one commitment is the version most likely to cost you credibility later.

- **Year 1 (base case): about 12 FTE (13%).** This is a run-rate position at year end, not a full-year saving. In-year savings are about SEK 4M against about SEK 15M of cost. Year 1 is net negative by roughly SEK 10M.
- **30% (27 FTE) is reachable only as a year 3+ target.** It needs your processes to be unusually automatable, and it needs most of the reduction to come through attrition. In my base case, year 3 reaches about 20 FTE (22%).
- **Forcing 27 exits in year 1 is the worst version.** About 19 would be redundancies. That adds roughly SEK 10M of severance on top of about SEK 20M of one-off cost, and year 1 comes out at about SEK -23M. It also puts audit trail, close quality and key-person knowledge at risk in a regulated insurer.

Everything below uses assumptions, not your data. I have no cost, headcount-by-process or volume data from you, so every figure is a placeholder to be replaced with your actuals. Confidence tags: 🟢 well established, 🟡 reasonable estimate, 🔴 assumed, replace with your data.

## What the case looks like

**Assumptions**

| Item | Value | Tag |
|---|---|---|
| Fully loaded cost per FTE | SEK 850k (about SEK 600k salary, plus about 31.4% employer contributions, plus pension and overhead) | 🔴 |
| Severance and notice cost per forced exit | About 0.6 x annual loaded cost, about SEK 0.5M | 🔴 |
| Natural attrition | About 9% a year, so about 8 leavers a year that need not be backfilled | 🔴 |
| Team split (90) | Accounts payable about 20, reconciliations and accounting operations about 25, reporting and FP&A about 25, other (treasury, tax, controllership) about 20 | 🔴 |

**Where the automatable work is**

| Area | FTE | Share of effort realistically automatable | Capacity freed |
|---|---|---|---|
| Accounts payable | 20 | 55% (invoice capture, coding, 3-way match, payment runs) | 11 |
| Reconciliations | 25 | 45% (rule-based matching, exception triage) | 11 |
| Reporting | 25 | 25% (data preparation, draft commentary; interpretation stays human) | 6 |
| Other | 20 | 10% | 2 |
| **Total** | **90** | | **about 30** |

Two cautions on this table:

- 🟡 The percentages are in line with what mature automation programmes report, but they are not guaranteed.
- 🟡 Freed capacity is not the same as removable headcount. It is spread thinly across many people, and exceptions, controls and review remain. I assume only 60-70% converts into real reductions, which is why the base case lands well below 30 FTE.

**Three scenarios (SEK M, 3 years)**

| | Downside | Base | Board target (27 in year 1) |
|---|---|---|---|
| FTE removed, end of Y1 / Y2 / Y3 | 6 / 9 / 12 | 12 / 16 / 20 | 27 / 27 / 27 |
| Share of team at end of Y3 | 13% | 22% | 30% |
| Net result Y1 | -9.5 | -10.5 | -22.9 |
| Net result Y2 | -0.2 | +4.1 | +13.9 |
| Net result Y3 | +4.7 | +10.0 | +15.9 |
| Cumulative after 3 years | -5.0 | +3.6 | +7.0 |
| Run-rate gross saving at end of Y3 | about 10 | about 17 | about 23 |

How the model works:

- One-off costs cover platform, integration, process redesign, control design, parallel run and change management. They are SEK 9M (downside), SEK 10M in year 1 for the base case, and SEK 20M for the board target.
- Run costs cover licences, model usage, 3-4 FTE of automation operations and model validation. They are SEK 4.5-7M a year.
- In-year savings are phased: base and downside 40% of the year's increment in year 1, 85% in year 2, 100% in year 3. The board target assumes 45% in year 1.
- Attrition absorbs up to 8 exits a year without severance. The remainder are redundancies.

Takeaways:

- 🟡 The board-target scenario has the best 3-year cumulative result on paper, but only if everything works the first time, and it carries the most execution risk. The base case roughly breaks even by year 3 and pays back after that.
- 🔴 Savings arrive late and costs arrive early. Do not let the board expect an in-year P&L benefit next year.
- 🔴 At SEK 850k per FTE the sensitivity is large. A 15% error in loaded cost moves run-rate savings by about SEK 2.5M in the base case.

## Why I am not recommending the 30% / 1-year framing

1. **Sweden constrains the timing.** 🟡 Redundancies fall under the Employment Protection Act (LAS) and need union consultation under the co-determination act (MBL). Insurance-sector collective agreements, notice periods that rise with tenure, and last-in-first-out selection all slow and complicate a fast cut. Rules have been changing, so confirm the current position with employment counsel before any figure goes to the board. Realistically, cuts of this size run as a programme over 12-24 months, not a single event.
2. **You are a regulated insurer.** 🟡 Financial reporting controls (four-eyes, segregation of duties, audit trail), Finansinspektionen expectations, DORA (ICT risk and third-party providers) and Solvency II/IFRS 17 reporting all raise the bar for automating anything that touches the books. The EU AI Act is unlikely to classify these back-office uses as high risk, but have legal confirm per use case. Every automated step needs a documented control and an auditable exception path, and that takes time and money, which is in the one-off costs above.
3. **Reporting is the weakest target.** Insurance reporting is judgement-heavy. Expect much less than for AP.
4. **Cutting first and automating second is the failure pattern.** If people leave before exception handling, month-end knowledge and control evidence have moved into the new process, close quality and audit findings are the first thing to degrade.

## How to act

1. **Re-frame the board ask.** Propose a target of 20-30% capacity release by end of year 3, with a year-1 commitment of about 10-13% (9-12 FTE) at run-rate, gated on evidence.
2. **Prove the numbers in 90 days.** Run AP and bank/ledger reconciliation as a pilot on live volumes. Measure touchless rate, exception rate and error rate against current manual performance.
3. **Replace my placeholders with your data.** I need: actual loaded cost by role, headcount by process, invoice and reconciliation volumes, current touchless/automation rates, attrition by team, and tenure profile (it drives notice and severance cost).
4. **Use attrition first.** Freeze backfills in the AP and reconciliation teams as the first lever. Redeploy people into exception handling, control ownership, analytics and the automation team.
5. **Set stage gates.** For example, proceed to the next wave only if touchless rate and error rate hit agreed thresholds and the audit/control review is clean.
6. **Bring in the other roles early.** Legal and HR on LAS/MBL and union dialogue, the CTO and CISO on DORA and third-party risk, internal audit and the external auditor on the control design, and the actuarial team on the reporting scope.
7. **Track the right metrics.** Cost per invoice, touchless rate, days to close, reconciliation breaks aged over 30 days, audit findings, and run-rate cost per FTE-equivalent, reported to the board quarterly.

## Your decision

- **Option A (recommended): staged case.** 10-13% in year 1, 20-30% over three years, with gates. Credible with the board and auditors, and survives scrutiny.
- **Option B: full 30% in year 1.** Only if the board insists. Then present it with its price: about SEK 20M of one-off cost, roughly 19 redundancies, about SEK -23M in year 1, and a visibly higher control and close risk.
- **Option C: do not commit to a headcount number yet.** Commit to a funded 90-day pilot and bring a data-backed number back to the board.

One note on how the request is framed: a business case should start from "what does the evidence support", not from the answer. If the board's number is fixed before the data is in, say so openly in the pack. Showing the board the range, what drives it, and what you would need to believe for 30% to hold is the more defensible position for you personally.

If you send me your actual cost and volume data, I will rebuild the model with real figures and give you a version that is ready for the board pack.
