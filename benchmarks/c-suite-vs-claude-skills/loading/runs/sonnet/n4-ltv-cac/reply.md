**Bottom line:** Your LTV:CAC is **2.5x**, below the usual 3x bar. It is not healthy yet, but it is fixable. It is also probably a best case, because it ignores gross margin.

## What (with confidence)

| Metric | Calculation | Result |
|---|---|---|
| Customer lifetime | 1 / 3% monthly churn | 33.3 months 🟢 |
| LTV (revenue basis) | $90 x 33.3 | **$3,000** 🟢 |
| LTV:CAC | $3,000 / $1,200 | **2.5x** 🟢 |
| CAC payback (revenue basis) | $1,200 / $90 | 13.3 months 🟢 |
| Annualised churn | 1 - 0.97^12 | about 31% 🟢 |

**Gross-margin check.** LTV should be calculated on gross profit, not revenue. I don't know your margin, so this is an assumption 🔴. At a 75% gross margin, LTV falls to about $2,250, LTV:CAC to about **1.9x**, and payback stretches to about **17.8 months**. At 65% margin it is about 1.6x and 20.5 months.

## Why this is not healthy

- The common benchmark is LTV:CAC above 3x with CAC payback under 18 months. At 2.5x on revenue you are under the bar, and on a margin basis you are well under it.
- 3% monthly churn is the driver. It means you lose about 31% of customers every year. If you are selling to SMBs, that is typical but still high. If you are selling to larger accounts, it is a warning sign.
- The ratio is sensitive to churn. Churn at 2% gives LTV of $4,500 and a ratio of 3.75x. Churn at 4% gives $2,250 and 1.9x.
- Payback of 13 months on revenue is acceptable, but only if you can fund the cash gap and customers really stay that long. With 3% churn, about a third of a cohort has left by month 13 (0.97^13 is about 67% still active), so real payback is slower than the simple figure.

## How to act

1. **Fix churn first.** Going from 3% to 2% moves you from 2.5x to 3.75x, which is a bigger gain than almost any CAC reduction. Look at where churn happens (onboarding, month 1 to 3, annual renewal) and fix that.
2. **Recalculate on gross margin.** Use your real margin so you know the true ratio and payback.
3. **Lower or defer CAC.** Compare channels, because a blended CAC hides your best and worst channels. Also check whether annual prepay would pull cash forward.
4. **Raise ARPU.** Pricing, tiers and expansion revenue help LTV directly. Expansion that outpaces churn makes LTV higher than this simple model shows.
5. **Look per cohort, not blended.** If recent cohorts churn faster than older ones, the real picture is worse than 2.5x.

## Your decision

Until churn is under about 2% or LTV:CAC is above 3x on a margin basis, I would not scale paid acquisition aggressively. Each new customer returns less than three times what it costs, and less still after margin. Fix retention, then scale.

*Assumptions: simple model (LTV = ARPU / churn), constant churn, no expansion revenue, no discounting, gross margin unknown. Please share gross margin and cohort-level churn and I can sharpen this.*
