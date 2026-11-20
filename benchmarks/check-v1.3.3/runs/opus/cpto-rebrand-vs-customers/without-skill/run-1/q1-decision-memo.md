# Q1 plan: staffing the rebrand and the top three customer issues

**Decision needed by:** [date] · **From:** [CEO and exec team] · **Prepared by:** [name], Head of Product
**Checked by:** [CRO], [CFO], [Head of Customer Success]

## Already decided (not up for discussion here)

We rebrand in Q1: the new name in the app, a new design system, a new domain and a new marketing site, launching [date].

## The decision we need

How we split Q1 product and engineering capacity between the rebrand and three customer issues that have been open for [N] months: slow invoicing, the broken [provider] accounting integration and missing reports.

## Facts

- **NPS:** +28 → +4 since [date]. Share of detractor comments by theme: invoicing [x]%, accounting integration [x]%, reports [x]%.
- **Revenue at risk:** €[x] ARR renews in Q1–Q2 at [n] accounts that raised these issues. Named at-risk accounts: [list].
- **Support load:** [n] tickets and [h] hours per month on these three themes.
- **Where it's concentrated:** [legacy customer base A / B / both].
- **Sizing (team-weeks):**
  - Rebrand: in-app name [x], design system foundations [x], first screens on the design system [x], domain [x], marketing site [x, mostly marketing].
  - Customer issues: integration [y], invoicing [y], reports [y].
- **Dependencies:**
  - The domain move means re-registering the accounting integration's OAuth redirects and webhooks, and possibly re-listing it in [provider] marketplaces (lead time: [x] weeks).
  - Invoice emails move to a new sending domain that needs warming up.
  - Customers need [x] weeks' notice to allowlist the new domain.

## Options

| | A: As decided | B: Recommended | C: Minimum |
|---|---|---|---|
| Rebrand staffing | Whole org | Staffed to its sizing | Whole org minus one squad |
| Customer fixes | After Q1 | Ring-fenced squad(s), roughly 20–25% of capacity | One squad, integration only |
| Rebrand launch date | [date] | [date], unchanged | [date], unchanged |
| Launch message | New name | New name plus three fixes | New name plus integration fix |
| Main risk | €[x] ARR renews on a broken product | Rebrand scope held to what was sized | Invoicing and reports wait until Q2 |

## Recommendation: option B

- **The launch date doesn't move.** For the first 4–5 weeks, only a small core team can work on the design system productively. That's when the customer squad takes the integration and invoicing fixes.
- **The integration fix is already a prerequisite for the domain move.** We'd have to touch the integration either way.
- **The missing reports are built on the new design system**, which makes them its first real test.
- **The rebrand launches with a reason for unhappy customers to come back,** not just a new name.

## What we're asking leadership to agree today

1. One option: A, B or C.
2. A mid-quarter review on [date], with these tripwires: [named accounts signal churn] / [rebrand milestone X slips by more than two weeks]. If either one trips, we revisit the split at that review.
3. That customer success can tell at-risk accounts these fix dates: [dates].
