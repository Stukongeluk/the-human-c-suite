**My recommendation:** take the board a plan that cuts engineering cost by about **12% on a run-rate basis by the end of next year** (range 8–18%) with no redundancies, plus a mid-year gate that can take it to **roughly 17–24% by the end of year two**, but only if the AI gain still shows up once we measure it on our own work. I wouldn't commit to 25% in one year on the strength of "twice as fast".

Why "2x" doesn't get you to 25% next year:

- **The arithmetic.** Writing code is only part of an engineer's week. My estimate is 30–40%, and we should measure it. If AI doubled coding speed, the team would get 18–25% more capacity at most, and that's before the extra review and testing work that comes with more and bigger pull requests. Measured team-level results so far are smaller and mixed. The sources are in the plan.
- **The size.** If the 25% came out of people alone, it would mean losing about a third of all engineers and contractors.
- **The timing.** Say you added ~12 redundancies on top of everything else. Next year's spend would still fall only about 9.5%, because consultation, notice and severance use up most of the first-year saving wherever European-style rules apply. The 25% would only show up as the run-rate at year-end. It would come with high delivery and reliability risk, and the company would likely end up rehiring.

The trap: when a savings target comes from a headline speed-up, it usually gets met by cutting what's easiest to count. The bill comes a year later as slower delivery, incidents and rehiring.

The board does have a fair point. AI changes the economics, there's almost always real waste in engineering spend, and teams that use AI well do get faster on specific tasks. The plan below takes all three seriously.

Two answers would change the plan most:
1. **What is the 25% for?** Cash runway, a margin target, a valuation or a peer comparison? If it's runway, I'd build a cash forecast first and order the measures by how fast they move cash.
2. **25% of what, compared with what?** Next year's total spend or the run-rate at year-end? This year's actual spend or next year's budget, including planned hires? Depending on the answer, the gap can be two or three times bigger or smaller.

The draft below uses an illustrative €10M engineering budget. Swap in your actuals and every line scales.

---

# Engineering cost plan for next year

**Decision needed:** approval of the savings plan and the mid-year AI gate · **Owner:** CTO, with the CFO · **Status:** draft. All figures are estimates on an illustrative baseline, to be replaced with actuals before the board meeting.

## The problem in one sentence

The board wants engineering to cost 25% less next year because it expects AI to make developers twice as fast. This paper sets out what we can commit to now, what has to be proven first, and what each alternative really costs.

## What the evidence says about AI and engineering speed

| Finding | Source |
|---|---|
| AI magnifies the strengths of high-performing engineering organisations and the dysfunctions of struggling ones. In 2024, each 25% rise in AI adoption went with an estimated 1.5% drop in delivery throughput and a 7.2% drop in stability. In 2025 the throughput link turned positive, but the instability remained. | DORA, State of AI-assisted Software Development 2025 (nearly 5,000 respondents); DORA 2024 |
| On high-adoption teams, developers completed 21% more tasks and merged 98% more pull requests, but review time rose 91% and pull requests were 154% larger. The publisher sells engineering analytics. | Faros AI, AI Productivity Paradox Report 2025 (10,000+ developers) |
| Experienced developers took 19% longer with early-2025 AI tools, while believing they had been faster. METR says newer tools may do better. The lasting lesson is that self-reported speed-ups are unreliable. | METR randomised trial, July 2025; update February 2026 |
| AI-generated code introduced OWASP Top 10 vulnerabilities in 45% of test tasks. | Veracode, GenAI Code Security Report 2025 |
| Two in three companies that cut jobs because of AI were already rehiring, and 52% of those rehires came within six months. | Careerminds, survey of 600 HR leaders, February 2026 |

**What this means for us:** AI gains on specific tasks are real. None of these studies shows teams doubling their total output. If AI doubled coding speed and coding is 30–40% of the week (our estimate, to be measured), capacity rises by 18–25% at most, before the extra review load. We will measure our own figure before any part of this plan depends on it.

## Baseline (illustrative)

| Line | €k per year |
|---|---|
| Employees (60 FTE, fully loaded) | 6,600 |
| Contractors and outsourced work (8) | 1,200 |
| Cloud and infrastructure | 1,500 |
| Tools, SaaS and AI seats | 450 |
| Other (recruiting, travel, events) | 250 |
| **Total** | **10,000** |

25% of this is €2,500k. If that came from people alone, it would be 32% of all engineers and contractors. The actuals will come from cloud billing, the licence and SaaS inventory, contractor contracts and their notice dates, aggregated payroll and attrition history, and delivery metrics from CI/CD and the issue tracker.

## Options

| | Next year's spend vs baseline | Run-rate at year-end | One-off costs | Risk to delivery and reliability | Reversible? |
|---|---|---|---|---|---|
| A. Do nothing | +€230k (+2%, from pay rises) | +2% | none | low now, but the waste stays | yes |
| B. Recommended: spend, focus, contractors, attrition, measured AI | −€817k (−8%) | −€1,230k (−12%; range 8–18%) | small (cloud commitments, pilot) | low to moderate, managed through the gate | mostly |
| C. 25% now: B plus ~12 redundancies | −€947k (−9.5%) | −€2,550k (−25.5%) | €530k (severance, notice, outplacement, legal) | high: 20% of employees leave before any AI gain is proven | no |

Assumptions behind C: exits from the start of Q3, after consultation and notice, at €37.5k one-off per person plus €80k in advisory fees. With exits at the end of Q1 and lower severance, next year's spend would fall about 15%. That is still not 25%. C's net saving is also overstated, because two costs are left out. A 1% workforce reduction has been associated with 31% more voluntary turnover the following year (Trevor & Nyberg, Academy of Management Journal, 2008). Replacing an employee costs one-half to two times their annual salary (Gallup).

## Recommended plan (Option B)

| Workstream | Run-rate saving, €k (low / mid / high) | Next year, €k (mid) | When | Owner |
|---|---|---|---|---|
| Cloud: idle resources, rightsizing, storage, then commitments | 225 / 300 / 450 | 225 | Q1–Q2 | Platform lead |
| Tools and SaaS: unused seats, overlapping tools, renegotiation | 45 / 90 / 135 | 54 | at each renewal | Engineering ops, procurement |
| AI tools: pilot, then scale what works (added cost) | −150 / −100 / −50 | −70 | pilot Q1, scale Q3 | CTO |
| Contractors: end contracts where the work stops or the team can absorb it, with full notice | 300 / 450 / 600 | 338 | notices in Q1 | Engineering managers |
| Hiring freeze with exceptions: 3–5 of ~6 expected leavers not replaced; junior intake and critical roles still hired | 330 / 440 / 550 | 220 | through the year | CTO, HR |
| Recruiting fees, travel, events (training budget kept) | 30 / 50 / 80 | 50 | Q1 | Engineering ops |
| **Total** | **780 / 1,230 / 1,765** | **817** | | |
| **Share of baseline** | **7.8% / 12.3% / 17.6%** | **8.2%** | | |

**Focus makes this safe.** By the end of Q1, product and engineering agree a list of low-value projects to stop or simplify. That list is what lets contractor work end and leavers go unreplaced without delivery slipping. It isn't counted as a separate saving.

**Year two.** If the mid-year gate shows a measured capacity gain, we leave another 4–6 leavers unreplaced in year two. That brings the run-rate saving to about 17–24% by the end of year two, with no redundancies. If the gain doesn't show, we stop at about 12% and report that plainly.

## Measuring AI, and the mid-year gate

- **Baseline (Q1):** for both pilot and comparison teams, from existing data: change lead time, cycle time per stage, review wait time, change failure rate, escaped defects, security findings and developer experience.
- **Pilot (8–12 weeks):** 2–3 teams use AI tools with training and agreed rules: small pull requests, tests required, and review plus security scanning for AI-written code. 2–3 comparison teams carry on as before. Self-reported speed-ups are recorded separately.
- **Decision rule, agreed before results:** scale if lead time improves by at least an agreed percentage and neither change failure rate nor escaped defects gets worse. Otherwise, change the approach or stop.
- **Where freed capacity goes, decided now:** first to absorb the work of ended contracts and unreplaced roles, then to tech debt and reliability. We will not reduce review, testing or security capacity on the strength of the pilot.
- **Board gate, end of Q2:** the measured AI effect, savings delivered against the table above, and the attrition target for year two.

## What we protect

- **Junior hiring and mentoring time.** Today's juniors are the seniors we will need in three to five years.
- **Training, security work, and review and test capacity.**
- **On-call rotas that don't depend on overtime.**

## People and communication

- Engineers hear the target and this plan from their own managers before the board decides, while their input can still change it. They know where the waste is, and that knowledge is the fastest route to the cloud and tools savings.
- Where a works council or employee representatives exist, we involve them now, at the problem stage. We also involve them before introducing any AI tool that changes how work is monitored. Notice and consultation rules are checked with counsel.
- Contractors and suppliers get honest, timely notice within their contract terms.
- What we tell staff: "This plan contains no redundancies. If the mid-year results show a gap, we will come back with options before anything is decided."
- Engineering leadership bonuses next year depend on delivery, quality and retention as well as cost. If results fall short, leadership bonuses are reduced before anything else.

## How we'll know it's working

We review these monthly and report them to the board each quarter:

- **Money:** savings per line against plan, and AI spend per team.
- **Delivery:** change lead time, deployment frequency, review wait time.
- **Quality:** change failure rate, escaped defects, incidents, security findings.
- **People:** regretted attrition, developer experience, on-call load.

## Assumptions, and what would change this plan

- The baseline mix and the size of each saving are estimates until actuals replace them. Cloud and contractor shares vary a lot between companies.
- If the 25% is about cash runway rather than margin, the plan starts with a cash forecast and orders the measures by how fast they move cash.
- If the pilot shows a large, measured gain with no loss of quality, the year-two reduction through attrition can go faster.
- If the 25% is measured against next year's budget, including planned hires, rather than this year's actual spend, part of the gap closes simply by not making those hires.

## Questions for the board

1. What does the 25% protect: cash, margin, a valuation, or a comparison with peers?
2. Is the target next year's total spend or the run-rate at year-end, and is it measured against this year's actual spend or next year's budget?
3. Would a lower cost per unit of delivered work, with more delivered for the same budget, meet the goal as well as a lower total?

What are we missing, and what would make this plan wrong?
