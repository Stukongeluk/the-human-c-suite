# Redundancy savings model for the board pack

## Bottom Line

**The model does not support "€9 million of savings in 2027". 120 × €75,000 = €9.0m is the full-year run-rate, and it only starts to show up in 2028.** If the CEO announces next month, my base case for the 2027 P&L is about **€4.0m**, with a range of **€2.0m to €6.0m**. The programme also costs roughly **€5.4m** in one-off cash (range €4.2m to €7.2m), so 2027 net cash is likely **negative (about -€1.5m)**. I would not put the €9m in the board pack as a 2027 number. Present it as "€8.1m run-rate from 2028, about €4.0m in-year 2027".

To hit €9.0m inside 2027 on the same assumptions, you would need about **270 exits** in the base case, or about **180** in the fast case. Neither is on the table.

## What the model says (EUR, 120 heads, €75k fully loaded)

| | Fast | Base | Slow |
|---|---|---|---|
| Average months of 2027 saving per head | 8.4 | 5.85 | 3.2 |
| Share of loaded cost that is actually saved | 95% | 90% | 85% |
| **2027 in-year saving** | **€6.0m** | **€4.0m** | **€2.0m** |
| One-off cost per head | €35k | €45k | €60k |
| **One-off cost (total)** | **€4.2m** | **€5.4m** | **€7.2m** |
| **2027 net cash effect** | **+€1.8m** | **-€1.5m** | **-€5.2m** |
| Run-rate saving from 2028 | €8.6m | €8.1m | €7.7m |
| Payback of one-off cost once all exits are done | about 6 months | about 8 months | about 11 months |
| Cumulative break-even | during 2027 | about Feb 2028 | about Aug 2028 |

Exit timing assumptions behind the rows above (savings start on the contract end date, not on the announcement or the start of garden leave):
- **Fast:** 40% leave end of Feb, 40% end of Apr, 20% end of Jun.
- **Base:** 25% leave end of Mar, 45% end of Jun, 30% end of Sep.
- **Slow:** 20% leave end of Jun, 40% end of Sep, 40% end of Oct.

Confidence is tagged below. Everything marked assumed needs your actuals before this goes to the board. The spreadsheet `savings_model.xlsx` (same folder) has live formulas, with every assumption in a yellow cell, so you can replace the placeholders with real figures.

## Why (the maths, step by step)

1. **Run-rate:** 120 × €75,000 = €9.0m a year. 🟢 verified arithmetic.
2. **Timing:** savings only start when a contract ends. An announcement in December 2026 is followed by works council consultation, collective-dismissal procedures and notice periods in both countries, so the average exit lands somewhere around Q2 2027, not 1 January. In the base case the average head saves for 5.85 months of 2027, so 120 × €75k × 5.85/12 = €4.4m before realisation. 🟡 the exit dates are my assumption.
3. **Realisation:** "fully loaded" usually includes allocated overhead (facilities, IT, management time) that does not disappear when a person leaves, and some work gets backfilled by contractors or overtime. I took 90% as realisable in the base case: €4.4m × 90% = **€4.0m**. 🔴 assumed. Replace this with your real split between direct cost and allocated cost.
4. **One-off cost:** I assumed €45k per head all-in in the base case (severance or social plan, notice buy-out, outplacement, legal and advisers). That is about 0.6 of the loaded cost, and 120 × €45k = **€5.4m**. 🔴 assumed. This depends heavily on tenure, the German social plan negotiation and Dutch transition payments. For orientation only, the Dutch statutory transition payment is a third of a monthly salary per year of service, while German social plans commonly pay around half a month's gross salary per year of service. Both are often negotiated up, so check this with employment counsel in each country.
5. **Net 2027:** €4.0m saving − €5.4m cash cost = about **-€1.5m**. The accounting treatment may differ from the cash: if the plan is announced in December with enough detail to create a constructive obligation, IAS 37 may require the restructuring provision in FY2026, which would shift the charge out of the 2027 P&L but not the cash. Confirm with your auditors. 🟡

## What the model does not cover, and what the board will ask

- **Revenue and delivery risk.** This is an industrial services group, so cost sits close to billable capacity, service levels and safety-critical work. If the 120 roles include field or technical staff, any lost revenue or SLA penalties can wipe out the saving. I have not modelled this because I do not know where the 120 come from. Ask operations for a role-by-role list and the revenue each role supports. 🔴
- **Country split.** I have not split Germany and the Netherlands because I do not have the numbers. They run on different procedures: works council rights in both, the collective dismissal notification routes (UWV and the trade unions in NL, the employment agency in Germany), and different notice rules. Different timing and cost per head in each country should be modelled separately before the board sees a single number. Have counsel confirm what applies to your sites and thresholds before the announcement date is fixed. 🟡
- **Announcing before consulting.** In both countries, announcing a fixed number of redundancies before works council consultation can create legal and negotiation risk and weaken your position. Consider announcing a proposal and a target, not a decision. 🟡
- **Attrition and regretted loss.** Voluntary leavers after an announcement tend to be the people you most want to keep. Consider a retention budget for critical roles; I have not included one.
- **Cheaper levers first.** Before committing, compare against a hiring freeze, natural attrition (at 1,400 people you probably lose well over 100 a year anyway), contractor and agency spend, and non-people costs. The cost-cutting order of preference in my own framework is: non-productive spend first, then headcount in roles not tied to near-term revenue. Layoffs that are the last lever rather than the first tend to keep their savings.

## How to act

1. **Reframe the headline in the board pack:** "€8.1m annual run-rate from 2028; €4.0m in-year 2027 (range €2.0m–6.0m); one-off cost €5.4m (range €4.2m–7.2m); cash break-even about Q1 2028."
2. **If the board needs €9m in 2027,** it has to come from elsewhere: a larger programme (about 270 exits, which is 19% of the group, in the base case), non-people savings, or a shift of the target to 2028. Show these options side by side.
3. **Replace my three placeholder inputs** (realisable share of loaded cost, one-off cost per head, exit dates) with actuals from HR and counsel, split by country, and re-run `savings_model.xlsx`.
4. **Get role-level data** on revenue and capacity at risk before the numbers are final.
5. **Check the accounting** (provision timing, IAS 37) with your auditors and the covenant impact of the one-off charge, if you have covenants.

## Your decision

Do you take the honest 2027 number (about €4m in-year, €8m+ run-rate) to the CEO now, or ask for a larger programme or a later target? My recommendation is the first: a board pack that shows €9m for 2027 will be missed by roughly half in the very first quarterly review, and the finance director will own that miss.

I can extend the spreadsheet to split Germany and the Netherlands, add a monthly cash profile, or add a revenue-at-risk line once you send me the role list.

Files: `savings_model.xlsx` (the model) in the same folder as this reply.
