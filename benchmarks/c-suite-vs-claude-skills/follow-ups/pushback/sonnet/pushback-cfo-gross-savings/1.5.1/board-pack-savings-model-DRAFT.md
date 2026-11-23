# Board pack draft: 80 redundancies, savings model for FY2027 (NL and BE)

**DRAFT for the CFO. Every figure marked (E) is my estimate from the figures you gave (900 people, NL and BE); none comes from your ledger or payroll yet. Replace the inputs in `savings_model.py` and the tables recalculate. Not legal advice: Dutch and Belgian employment counsel must confirm every timing and cost assumption below.**

## 1. The answer in two numbers

- **FY2027 net effect of the 80 redundancies: about EUR 0 (range -1.2M to +0.5M).** Gross saving is only about EUR 2.0M in 2027 because people leave months after the decision, and one-off costs land before the savings do.
- **2028 run-rate net saving: about EUR 4.0M (range 3.2M to 4.6M).** That is a real saving, but it is not EUR 6M, and it arrives a year later.

Why EUR 6M is out of reach: 80 people at my estimated blended fully loaded cost of EUR 65,100 (E) is EUR 5.2M a year even if all 80 left on 1 January at zero cost. EUR 6M needs EUR 75,000 per head, and nobody leaves on 1 January: it is late November 2026 and the board pack goes out next week.

## 2. The model: net effect by quarter, FY2027 (EUR thousand)

Inputs (E): 56 roles NL at EUR 63,000 loaded, 24 roles BE at EUR 70,000 loaded; revenue EUR 120M, contribution margin 22%. Base case: NL employment ends end of June (works council advice, union notification, UWV procedure, notice), BE employment ends end of October (information-and-consultation phase, then notice by length of service).

| Line (base case) | Q1 | Q2 | Q3 | Q4 | FY2027 | Source / assumption |
|---|---|---|---|---|---|---|
| Gross saving, from actual exit dates | 0 | 0 | 882 | 1,162 | 2,044 | Payroll aggregate by country; exit dates (E) |
| Work still to be done (overtime, agency), 12% of gross | 0 | 0 | -106 | -139 | -245 | Delivery plan; estimate |
| Rehired roles, 8% of roles refilled from month 10 | 0 | 0 | 0 | -104 | -104 | Hiring history; estimate |
| Severance, transition and social-plan payments | 0 | -560 | 0 | -144 | -704 | NL: statutory transition payment about EUR 10k per head (E); BE: top-up beyond notice EUR 6k (E) |
| Outplacement and transition support, EUR 5k per head | -200 | -200 | 0 | 0 | -400 | Quotes needed; paid from day of notice |
| Legal, adviser and works-council costs | -245 | -105 | 0 | 0 | -350 | Counsel and adviser quotes |
| Rehiring fees | 0 | 0 | 0 | -77 | -77 | EUR 12k per refilled role (E) |
| Extra voluntary attrition, 12 extra leavers | 0 | -54 | -54 | -54 | -162 | Attrition data; EUR 18k replacement each (E) |
| Revenue at risk, 0.3% of revenue at 22% margin | 0 | 0 | -20 | -20 | -40 | CRM, account owners (E) |
| **Net effect, approx. cash** | **-445** | **-919** | **702** | **624** | **-38** | |

Net P&L differs from cash in timing only: if the board decides and announces in December, the restructuring provision (about EUR 1.5M of the one-off lines) may have to be booked in FY2026 while the cash leaves in 2027. Agree this with your auditor before the pack goes out.

## 3. Three timing cases

| Case | Assumption | FY2027 gross | FY2027 net | 2028 net |
|---|---|---|---|---|
| Fast | NL exits end April via settlement agreements at a 1.5x premium; BE end August; low leakage | 2.9M | +0.5M | 4.6M |
| Base | as above | 2.0M | about 0 | 4.0M |
| Slow | NL exits end September; BE end December; high leakage and attrition | 0.9M | -1.2M | 3.2M |

Sensitivities on the base case (FY2027 net): NL exit month April / June / September: +0.47M / -0.04M / -0.79M. Leakage 6% / 12% / 20%: +0.08M / -0.04M / -0.20M. The base case is roughly break-even in 2027 before any revenue loss, so any revenue lost in 2027 makes it negative.

## 4. What drives the timing (to confirm with counsel)

- **Netherlands:** works council advice (art. 25 WOR) before the decision is final; 20 or more dismissals in one UWV work area within three months trigger union notification and consultation (WMCO), and settlement agreements you initiate count towards the 20; then UWV permission, or settlement agreements; notice of one to four months; a statutory transition payment. Who goes follows the reflection principle (afspiegelingsbeginsel), per group of interchangeable jobs, by age band and then service: you cannot choose the 80 by performance or cost.
- **Belgium (as I understand it, verify):** a collective dismissal triggers the Renault procedure: information and consultation with employee representatives before any notice is given, notification to the authorities, and a possible social plan negotiation. Notice or indemnity in lieu runs by length of service and can be many months. Outplacement duties and protected representatives apply. Thresholds depend on the size of each establishment.
- **Both:** a country split matters; I assumed 56/24 (E).

## 5. Last year's restructuring

- Check what last year's programme actually delivered against what was promised (net, after rehiring and attrition). That is the best evidence for this model's leakage and rehiring inputs.
- If last year's charges were reported as "one-off" and adjusted out of EBITDA, a second programme in consecutive years makes them recurring. Reconcile adjusted to reported EBITDA, name each adjustment, and do not call this year's charge one-off in the pack.
- Survivors: expect higher voluntary attrition after a second round. My base case adds 12 extra leavers (E); the research pattern is that downsizing goes with more voluntary exits (Trevor and Nyberg, 2008).

## 6. Options side by side, FY2027 (EUR M; all levers are estimates scaled to 900 people and about EUR 120M revenue)

| Option | FY2027 net | Run-rate 2028 | Human impact | Notes |
|---|---|---|---|---|
| Do nothing | 0 | 0 | none | Gap remains; I do not yet know what the EUR 6M is for |
| 80 redundancies (base) | about 0 (-1.2 to +0.5) | about 4.0 | 80 jobs; survivors | Net cost in H1, break-even by year-end |
| Purchasing, subcontractor and agency rates (2-4% of about EUR 45M third-party spend) | 0.45 to 0.9 | 0.9 to 1.8 | low | |
| Pricing and revenue leakage (0.5-1.0% of revenue) | 0.36 to 0.72 | 0.6 to 1.2 | low | |
| Freeze on indirect backfill, non-renewal of flex contracts (15-25 roles via attrition) | 0.35 to 0.65 | 0.7 to 1.3 | low to moderate | Overlaps with the redundancies: counts once |
| Voluntary exits, net of payments (15-25 people) | 0.14 to 0.32 | 0.4 to 0.9 | moderate, voluntary | |
| Leadership bonus waiver and perks | 0.6 to 1.0 | 0 (one year only) | none to staff | Temporary: not in the run-rate |
| **Package without compulsory redundancies** | **1.9 to 3.6** | **2.6 to 5.2** | | Carries its own costs: negotiation, review, some workload |

One-off cash, not P&L: collecting five days of receivables on EUR 120M revenue frees about EUR 1.6M (E), a one-time cash effect.

## 7. Recommendation

1. Do not put EUR 6M in 2027 in the pack: it is not supported. Put the base case and its range in.
2. Adopt the no-compulsory-exit package first (section 6), with leaders' bonuses and perks going first.
3. Keep a compulsory programme as a gated option with a named trigger: if by the end of Q1 2027 the package is tracking below EUR 2M annualised, or volumes have fallen, start works council consultation for a smaller, work-based reduction (cutting the work first, not just the people).
4. Start the works council and employee-representative conversations now with the real numbers, so that whichever path is chosen, consultation time is not the bottleneck.

## 8. The CEO's case, steelmanned

If volumes have structurally fallen or the cost base is simply too high, the EUR 4M run-rate is real, delay is costly, and a clean single round is kinder than repeated trimming. The gate in point 3 keeps that route open without committing to a number the timeline cannot deliver.

## 9. Key assumptions, and what would change this

Assumptions: 56/24 NL/BE split; EUR 65,100 blended loaded cost; exit dates; 12% leakage; 8% rehiring; 12 extra leavers; 0.3% revenue loss. The answer changes materially if: the BE share is higher (longer notice, later savings), roles are in a single closing site (reflection principle may not apply), average loaded cost is above EUR 75k, or the EUR 6M is a covenant or valuation number with a fixed date.

**What am I missing, and what would make this wrong?**

## Appendix: one-page gross view (base case, EUR thousand, estimates)

| | Q1 | Q2 | Q3 | Q4 | FY2027 | 2028 full year |
|---|---|---|---|---|---|---|
| **Gross saving** | 0 | 0 | 882 | 1,162 | 2,044 | 5,208 |
| Known one-off costs: severance, transition payments, outplacement, advisers | -445 | -760 | 0 | -144 | -1,349 | 0 |
| **Gross saving after known one-off costs** | -445 | -760 | 882 | 1,018 | 695 | 5,208 |

Gross saving excludes overtime and agency cover, rehired roles, extra attrition and revenue at risk; section 2 shows them. Gross saving is not a net saving and the pack should not call it one.
