**Bottom line:** Your LTV:CAC is **2.5x on revenue**, and about **2.0x on gross profit**, assuming an 80% gross margin. The usual bar is 3x, so this is **not healthy yet**. It isn't broken, but it falls short, and 3% monthly churn is the main reason.

## The math

- Average customer lifetime = 1 / 0.03 = **33.3 months**
- Revenue LTV = $90 / 0.03 = **$3,000**
- LTV:CAC on revenue = $3,000 / $1,200 = **2.5x**

You pay back CAC out of gross profit, not revenue, so the version that matters is LTV = ARPU x gross margin / monthly churn. You didn't give a gross margin, so here is the range:

| Gross margin | LTV | LTV:CAC | CAC payback (CAC / (ARPU x GM)) |
|---|---|---|---|
| 100% (revenue view) | $3,000 | 2.5x | 13.3 months |
| 80% | $2,400 | 2.0x | 16.7 months |
| 75% | $2,250 | 1.875x | 17.8 months |
| 70% | $2,100 | 1.75x | 19.0 months |

Confidence:
- [verified] 2.5x on revenue comes straight from your three numbers.
- [assumed] 2.0x uses an 80% gross margin. Swap in your real margin.
- [assumed] The formula assumes churn stays at 3% every month, with no expansion revenue.

## Why it's not healthy

1. **It's under 3x even in the best case.** At a 100% gross margin, which no business has, you still only reach 2.5x.
2. **3% a month adds up.** 1 - 0.97^12 = **30.6% of customers lost per year**. If that 3% is revenue churn and you have no expansion, gross revenue retention is about 69%. For SMB SaaS, 85% or more is a reasonable floor.
3. **Payback is only just acceptable.** About 17 months at 80% margin, just under the usual 18-month limit. By month 17, only about 60% of a cohort is still paying (0.97^16.7 = 0.60). So **about 4 in 10 customers leave before they've paid back what it cost to get them**.
4. **The simple formula is optimistic.** It counts margin forever with no discounting. If you cap lifetime at 5 years, LTV is about $2,014 (1.68x). With a 10% annual discount rate it's about $1,896 (1.58x). [medium]

## What gets you to 3x (at 80% gross margin)

Any one of these on its own gets you there:

| Lever | Today | Needed for 3x | Change |
|---|---|---|---|
| Monthly churn | 3.0% | 2.0% | -1 point (2.5% gets you to 2.4x) |
| ARPU | $90 | $135 | +50% |
| CAC | $1,200 | $800 | -33% |

Churn is the cheapest lever and the one that compounds. Cutting churn by a third does the same job as raising price by half. ARPU is the only lever that improves both the ratio and the payback period. CAC improves both too, but it's usually the hardest to move.

## How to act

1. **Check that CAC is fully loaded.** It should include sales and marketing salaries, tools and agency fees, not just ad spend. If $1,200 is media spend only, your real ratio is lower than shown here.
2. **Get your real gross margin** (hosting, support, payment fees, third-party APIs) and recompute with it.
3. **Split everything by cohort and by channel.** A blended 2.0x can hide one channel at 4x and another at 1x. Fix or cut the 1x channels before you spend more.
4. **Find out when customers churn.** If most of it happens in months 1-3, the problem is onboarding or activation. That's usually the cheapest fix and moves the ratio the most.
5. **Test pricing and annual plans.** Annual prepay cuts churn and brings cash in up front, which makes payback close to immediate for those customers.
6. **Don't scale acquisition spend yet.** At about 2x, each dollar of CAC returns about $2 of gross profit spread over nearly three years, and 40% of customers leave before they've paid back. CAC also tends to rise as you spend more, so the next dollar will probably do worse than the average.

## Your decision

The real question is whether to grow acquisition now or fix retention first. The numbers point to retention first. Keep acquisition spend roughly flat, set a target of getting monthly churn from 3% to 2-2.5%, and raise spend once your cohorts show 3x on a gross-margin basis. If you have your gross margin, a breakdown of what's in the $1,200 and churn by customer age, the 2.0x can be replaced with a firm number.
