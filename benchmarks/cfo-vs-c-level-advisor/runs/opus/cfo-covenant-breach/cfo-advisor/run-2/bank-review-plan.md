# Q2 leverage covenant: workings and plan for the bank review

Working document behind my reply. Every euro figure below is illustrative. I don't have your accounts, so I used a plausible profile for a 260-person Dutch furniture manufacturer. Put your own numbers into the formulas. The formulas and the conclusions about timing still hold.

Tags: [Verified] = checked against a source (listed at the end). [Medium] = reasoned inference. [Assumed] = my placeholder number.

---

## 1. The gap in euros

**Formulas** (leverage = net debt / LTM EBITDA, tested on 30 June 2027) [Assumed: calendar Q2, last-twelve-months basis; check your facility agreement]

```
Net debt reduction needed = (forecast ratio - target ratio) x LTM EBITDA
EBITDA needed            = net debt / target ratio
```

**Illustrative profile** [Assumed]: revenue EUR 45M, LTM EBITDA at Q2 EUR 4.0M, net debt EUR 14.4M, so 14.4 / 4.0 = 3.6x.

| Target | Net debt reduction needed (EBITDA held) | or EBITDA increase needed (net debt held) |
|---|---|---|
| 3.5x (the limit, zero headroom) | 14.4 - 3.5 x 4.0 = **EUR 0.40M** (2.8% of net debt) | 14.4 / 3.5 = 4.114, so **+EUR 114k** (+2.9%) |
| 3.2x (about 10% headroom, where a bank stops worrying) | 14.4 - 3.2 x 4.0 = **EUR 1.60M** | 14.4 / 3.2 = 4.500, so **+EUR 500k** (+12.5%) |

**So what:** the breach is 0.1x. That is smaller than normal forecast error, which is a reason to plan for headroom (3.2x) rather than for scraping under 3.5x.

---

## 2. What a 10% job cut does to the Q2 test

### Assumptions [Assumed]
- 26 FTE (10% of 260), average gross monthly salary EUR 3,400
- Loaded annual cost: 3,400 x 12 x 1.08 (holiday allowance) x 1.30 (employer social charges and pension) = **EUR 57.3k per FTE**
- Saving at full run-rate: 26 x 57.3k = **EUR 1.49M a year, or EUR 124k a month**
- Transition payment (transitievergoeding, statutory severance): 1/3 of a monthly salary including holiday allowance per year of service [Verified]. At 10 years' average tenure: 10 x 1/3 x (3,400 x 1.08) = **EUR 12.2k per person, EUR 318k in total**
- Add settlement premiums, employment lawyers, the works council's own adviser and lost productivity: **about EUR 0.5M one-off in total** [Assumed]
- The cost is booked when the plan is announced, under the accounting rules for restructuring provisions [Medium: confirm with your auditor]. The cash goes out when people leave.

### Realistic Dutch timeline if you start properly in mid-December

| Step | Duration | Lands around |
|---|---|---|
| Proposed decision to the works council (OR), advice requested while it can still influence the decision [Verified] | OR advice typically 4-8 weeks, longer over the holidays or if the OR hires an expert [Assumed] | late Jan - mid Feb 2027 |
| Collective dismissal notice to UWV and unions (26 people = 20 or more within 3 months in one UWV region) [Verified] | One-month waiting period before notices or settlement agreements take effect, unless the unions agree [Verified]. Runs in parallel. | mid Jan 2027 at the earliest |
| If the final decision deviates from the OR's advice | One-month suspension. The OR can appeal to the Enterprise Chamber (Ondernemingskamer). [Verified] | mid March 2027 |
| UWV permit route: part A, 14 days for settlement talks + 14 days cooling-off, then about 4 weeks of processing [Verified] | about 8 weeks | mid April 2027 |
| Notice period: about 1 month per 5 years of service, maximum 4. UWV procedure time can be deducted, but at least 1 month must remain. [Verified] | 1-4 months | **exits mid May - August 2027** |

Selection follows the reflection principle (afspiegelingsbeginsel): agency workers go first, then within each interchangeable job group and age band, generally the shortest service goes first [Verified]. You cannot use the cut to choose who leaves.

**Result:** on realistic timing, the 30 June LTM contains **0-2 months** of savings, but all of the one-off cost.

### Leverage at the Q2 test with a 10% cut (illustrative)

Net debt = 14.4 - savings + one-off cash (if people left before 30 June).

| Months of savings inside the LTM | Saving | Net debt | Leverage, restructuring cost **not** added back | Leverage, cost **added back** |
|---|---|---|---|---|
| 0 (exits after 30 June; cost booked, cash not yet paid) | 0 | 14.40 | 14.40 / 3.50 = **4.11x** | 14.40 / 4.00 = **3.60x** |
| 1 (exits end of May) | 0.124 | 14.78 | 14.78 / 3.62 = **4.08x** | 14.78 / 4.12 = **3.58x** |
| 2 (exits end of April, unlikely) | 0.248 | 14.65 | 14.65 / 3.75 = **3.91x** | 14.65 / 4.25 = **3.45x** |
| 3 (exits end of March, not realistic with a proper process) | 0.372 | 14.53 | 14.53 / 3.87 = **3.75x** | 14.53 / 4.37 = **3.32x** |

**So what:** the cut only helps the Q2 test if your facility allows restructuring add-backs **and** people are gone by the end of April. In every other case the Q2 number gets worse. If you really do have too much capacity, a cut helps the Q4 2027 and 2028 tests. That makes it a separate decision, to be made on its own merits.

This table also assumes output holds with 26 fewer people. If demand is intact, cutting production staff costs revenue, and the cut looks worse still.

---

## 3. Self-help levers you control by 30 June

| Lever | How | Illustrative impact | Hits | Owner |
|---|---|---|---|---|
| Inventory down 10 days | Slow movers, order quantities for board, timber, fabric and foam, finished goods for cancelled orders, discipline on make-to-order. On EUR 25M COGS one day = EUR 68k, so 10 days = EUR 0.68M. Counted at **EUR 0.6M**. | EUR 0.60M | net debt | Operations + purchasing |
| Receivables (DSO) down 5 days | Invoice on delivery day, enforce dealer terms, chase anything over 60 days, deposits on custom and project orders. On EUR 45M revenue one day = EUR 123k, so 5 days = EUR 0.62M. Counted at **EUR 0.5M**. | EUR 0.50M | net debt | Sales + finance |
| Capex timing | Defer non-critical capex to Q3. Tell the bank it is timing, not a saving. | EUR 0.30M | net debt | CFO |
| Flex layer | Cut agency hours by about 10 FTE-equivalents from January wherever volume has fallen, and don't renew fixed-term contracts where the work has gone (give the one-month notice of non-renewal, aanzegging). 10 x 55k / 12 x 6 months. People still lose work here, so do it deliberately. It is also the order the law expects. | EUR 0.275M | EBITDA (and cash) | Operations + HR |
| Hiring freeze | Don't backfill non-critical leavers (about 4 people x 3 months) | EUR 0.05M | EBITDA | HR |
| Price and procurement | Surcharge or price increase where the market allows, plus a 1% procurement saving on H1 material | EUR 0.20M | EBITDA | Sales + purchasing |
| **Total** | | **EUR 1.40M net debt + EUR 0.525M EBITDA** | | |

**Deliberately left out:**
- Stretching suppliers beyond agreed terms. It reverses in July, the bank sees it, and credit insurers notice.
- Quarter-end stock or invoicing tricks. These are window dressing.
- Factoring. Usually counted as debt.
- Sale-and-leaseback of the building. Expensive, irreversible, and it depends on how your covenant treats leases.

### Leverage at Q2 by how much of the plan lands

Net debt falls by the cash levers plus the EBITDA gain, because EBITDA is cash too.

| Plan delivered | EBITDA | Net debt | Leverage |
|---|---|---|---|
| 100% | 4.0 + 0.525 = 4.53 | 14.4 - 1.40 - 0.525 = 12.48 | **2.76x** |
| 50% | 4.26 | 13.44 | **3.15x** |
| 25% | 4.13 | 13.92 | **3.37x** |
| 0% | 4.00 | 14.40 | 3.60x |

**Bear case** (LTM EBITDA 5% below forecast, so EUR 3.8M; 3.79x without a plan):

| Plan delivered | Leverage |
|---|---|
| 50% | **3.31x** |
| 25% | **3.54x**, a breach |
| 25% + owner's EUR 0.5M subordinated loan (if excluded from net debt) | **3.41x** |

**So what:** half the plan gives about 3.15x in the base case and 3.3x in the bear case, without forced redundancies. If your stock and DSO are already lean, these numbers shrink. In that case the fallback agreement with the bank (section 5) becomes the main event.

---

## 4. The owner's contribution: the strongest signal to a bank

- No dividend and no management fee to the holding until headroom is back to at least 0.3x. Each euro paid out before 30 June adds a euro of net debt.
- A standby subordinated shareholder loan (achtergestelde lening), for example EUR 0.5M, with a subordination statement to the bank. Check whether the facility excludes it from net debt or counts it as an equity cure.
- The owner comes to the review and says this himself.

---

## 5. The bank pack (10 pages at most)

1. **One-page summary:** forecast, gap, plan, ask.
2. **Covenant forecast by quarter to Q2 2028**, using the facility agreement's definitions, base/bear/bull.
3. **EBITDA bridge** from the last test to Q2: volume, price, material cost, wages, energy. Is the decline cyclical or structural? This is the bank's real question.
4. **Net debt bridge:** working capital, capex, debt service.
5. **Self-help plan:** each measure with euros, owner, date and status, tracked monthly.
6. **Liquidity:** 13-week cash flow and revolving credit headroom by month.
7. **Shareholder support:** dividend stop, standby loan.
8. **Structural capacity review:** scope, decision date, and that any reduction goes through the works council.
9. **The ask:** "We expect to comply. Given the forecast uncertainty, we'd like to agree now what happens if Q2 lands between 3.5x and 4.0x: a one-off reset for the Q2 and Q4 2027 tests, or an equity cure right. In return we offer monthly reporting." Agreeing this before a breach is far cheaper than a waiver after one.
10. **Trigger table** (section 6).

---

## 6. Decision triggers (set them now, not in a crisis)

| Trigger | Action | By |
|---|---|---|
| Monthly covenant forecast from January | CFO reports it to the owner and the bank | 10th working day each month |
| End-March forecast above 3.4x | Draw the owner's standby loan | 15 April 2027 |
| End-March forecast still above 3.5x after that | Formal reset or waiver request to the bank, before the test | 30 April 2027 |
| Dec-Feb order intake structurally below capacity, confirmed by the review | Start works council consultation on a capacity reduction sized to the order book, not to a signal. Benefits land in the Q4 2027 and 2028 tests. | Decide whether to start by 15 January 2027 |

---

## 7. Questions the facility agreement must answer (by Wednesday 25 November)

- **Net debt:** does it include leases, subordinated shareholder loans, guarantees? Is cash netted in full?
- **EBITDA:** LTM or annualised? "Normalised"? Are restructuring and one-off costs added back, and is that capped? Are pro-forma savings allowed?
- **Test dates** and the deadline for the compliance certificate.
- **Equity cure:** amount, how often, and whether it counts in EBITDA or in net debt.
- **Other covenants:** DSCR and solvency. Restructuring costs hit both.
- **Information duty:** must you notify the bank of an expected breach?
- **Restrictions:** dividends and shareholder payments.

---

## 8. Talking points for the owner

- "The bank isn't testing how tough we are. It's testing whether we're under 3.5x on 30 June and whether we saw this coming."
- "A cut announced now puts its cost in the test period and its savings after it. On realistic Dutch timing it makes the Q2 number worse, not better."
- "Announcing before the works council has advised invites a dispute that can reverse the decision. That would hurt us more with the bank than the 0.1x itself."
- "If we really do have too much capacity, we decide that properly in January, sized to the order book. The bank will hear that it is under review."
- "The strongest signal to a bank is your own money behind a plan that holds."

---

## Sources

- UWV, collective dismissal (threshold, notifying UWV and unions, the one-month waiting period and its exceptions): [uwv.nl](https://www.uwv.nl/werkgevers/werkgever-en-ontslag/ik-wil-ontslag-aanvragen/detail/collectief-ontslag)
- Rijksoverheid, collective dismissal (20+ within 3 months in one region): [rijksoverheid.nl](https://www.rijksoverheid.nl/onderwerpen/ontslag/collectief-ontslag)
- Dirkzwager, works council advice, the one-month suspension, Enterprise Chamber, UWV refusing premature applications: [dirkzwager.nl](https://www.dirkzwager.nl/kennis/artikelen/geen-toestemming-voor-ontslag-zonder-positief-advies-van-de-or)
- Rijksoverheid, transition payment (1/3 monthly salary per year of service, maximum EUR 102,000 in 2026): [rijksoverheid.nl](https://www.rijksoverheid.nl/onderwerpen/ontslag/vraag-en-antwoord/hoe-hoog-is-de-transitievergoeding-als-ik-word-ontslagen)
- KHN, step-by-step plan for dismissal on business-economic grounds (UWV steps and timing, reflection principle, notice periods): [khn.nl](https://khn.nl/kennis/ontslag-om-bedrijfseconomische-redenen-een-stappenplan)
- UWV, notice period (procedure time deductible, at least 1 month must remain): [uwv.nl](https://www.uwv.nl/nl/ontslag/opzegtermijn)

The legal points are general information, checked against these sources. They are not legal advice. Have your employment lawyer confirm them, and check your collective labour agreement (cao) for reorganisation provisions, before anything is said internally.
