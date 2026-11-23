**Recommendation: don't commit to a flat 25% on the strength of "2x faster". Commit to a measured plan that can credibly deliver about 10% in-year and about 14% run-rate without layoffs, and decide the rest on evidence in Q3.** The board's pressure is real, so here is the plan in a form you can take to them. I've built it on an illustrative budget because I have no figures yet; swap in yours.

## The trap, in one sentence
A target with no diagnosis ends with cutting whatever is easiest to count, which is people, and "2x faster" is a vendor headline until it is measured on your own work.

## Why "2x" can't carry a headcount number yet
- DORA 2025 found AI magnifies what's already there; in 2024 higher AI adoption went with lower delivery stability.
- METR's 2025 trial found experienced developers were 19% slower with AI while believing they were faster. METR said in Feb 2026 that this reflects early-2025 tools, so treat it as proof that feeling and measuring differ, not as today's speed.
- Faros (10,000+ developers): 21% more tasks, but review time up 91% and pull requests 154% larger. Writing code is only part of the week; the bottleneck moves to review.
- GitClear and Veracode report more duplicated code and more security flaws in AI-written code. Those costs return later as rework.

Even a real 2x on coding is nowhere near 2x on delivery, and it doesn't make 25% of the team surplus.

## Illustrative model (all figures are estimates, in EUR millions per year)
Assumed base: people 6.5, contractors 1.5, cloud 1.2, tools and licences 0.5, other 0.3 = **10.0**. A 25% target = **2.5**.

| Lever | Basis (estimate) | In-year | Run-rate |
|---|---|---|---|
| Idle cloud, right-sizing | 20% of 1.2 | 0.24 | 0.24 |
| Unused seats, overlapping tools | 15% of 0.5 | 0.08 | 0.08 |
| Contractors ended or converted | 40% of 1.5, net 30% for conversion and handover | 0.42 | 0.42 |
| Hiring freeze and natural attrition | about 10% attrition, half a year in-year, not backfilled | 0.30 | 0.65 |
| **Total** | | **1.04 (10.3%)** | **1.39 (13.9%)** |
| **Gap to 2.5** | | **1.47** | **1.11** |

Notes: stopping low-value projects (focus) frees capacity but saves cash only through the contractor and attrition lines, so I have not counted it twice. AI seats will add cost; budget about 0.1 for them, which trims the in-year total to about 0.94. Attrition savings only hold if the work they carried is stopped or absorbed, and unplanned departures hit your best people as often as anyone.

## The plan
**Now to month 2: waste and baseline**
1. Inventory cloud, licences and AI spend: tool, owner, seats paid, weekly active users, cost. No owner, no renewal.
2. Review every contractor engagement: what it delivers, what it costs, and whether it can be converted or ended with proper notice.
3. Baseline delivery per team: lead time, review wait, change failure rate, rework, escaped defects, developer experience.

**Months 2 to 5: prove the AI gain on your own work**
4. Run an 8 to 12 week pilot with a comparison group, on real work, with agreed rules (small pull requests, tests, review of AI code). Measure the same metrics as the baseline and discount self-reported speed-ups.
5. Agree before the pilot what freed time is for: debt, reliability, the roadmap, onboarding.

**Months 3 to 9: flow and toil**
6. Cut work in progress and review queues, and automate the toil that eats capacity. This is what turns faster typing into faster delivery.

**Q3: decide on the gap**
7. If the pilot shows a sustained gain, absorb growth without hiring and let attrition carry the rest. If it doesn't, tell the board the 25% was premised on a gain the data doesn't support.

## Human impact
- Keep hiring and mentoring juniors. Replacing them with AI is a decision about your 2030 seniors, not a saving.
- No ranking of engineers by commits, pull requests or AI usage. Measure teams.
- If the board still requires a number that only people can deliver, leaders and executives carry the first and largest cut, and any reduction is a one-time, decently funded step after the options above are exhausted. In the Netherlands and most of Europe, works council consultation and notice periods mean savings arrive months later than announced; this is not legal advice, so involve counsel and the works council early.

## What to tell the board
"We will deliver about 10% this year and about 14% run-rate through waste, contractors and attrition. Whether AI can fund the remaining 11% depends on a measured pilot reporting in Q3. We won't cut a headcount number from a benchmark."

## Two questions that would change the answer
1. What is the actual problem behind the 25%: cash, margin, a promise to investors, or a belief about AI? A different problem points to different levers, possibly pricing or revenue.
2. What is your real split between people, contractors, cloud and tools, and how many contractors and open roles are there today?

## Assumptions and pushback
Assumptions: the illustrative base above, attrition near 10%, contractor and cloud percentages from typical ranges, no change in demand on engineering. What am I missing, and what would make this wrong? If your cloud and contractor spend is already lean, or attrition is lower, the 10% shrinks; if you have large contractor or licence sprawl, it grows. Send me the real figures and I'll rebuild the table by quarter.
