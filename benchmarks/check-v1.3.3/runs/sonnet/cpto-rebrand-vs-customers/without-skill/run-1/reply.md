# Planning Q1: rebrand and customer fixes together

The CEO is right that a decision beats no decision. The rebrand is decided, so you are not reopening it. What is still open is how Q1 capacity is split, in what order, and what "done" means for the rebrand. That is a product decision, and it is yours to bring to the CEO with evidence. I'd plan it as follows.

## 1. Don't frame it as rebrand versus customers

If you go in with "we shouldn't do the rebrand", you will lose, and you'll have used up credibility you need later. Go in with "we will do the rebrand, and here is the cheapest way to hit the dates without leaving customers stranded". The rebrand is mostly marketing and brand work plus a thin engineering layer. The expensive parts are the design system migration and the domain change. Both can be scoped.

## 2. Make the case with numbers before you plan anything

NPS going from +28 to +4 with the same three complaints open for months is a revenue-risk story. Spend the first week on these, because the CEO will respond to them far more than to opinion:

- Which accounts raised slow invoicing, the broken accounting integration and the missing reports? Pull ARR, renewal dates and churn or contraction since the merger.
- Of the NPS drop, how much is legacy customers of each merged company, and how much is these three themes? Read the verbatims, not just the score.
- What do support, CS and sales say about deals and renewals at risk this year? Get two or three named accounts.
- What does each of the three problems cost to fix, roughly? Slow invoicing may be one engineering team for six weeks. The integration may be a vendor API change. Reports may be a long tail. Get real estimates from the teams, not guesses.

Then put a number on it: "X ARR renews in H1, and the accounts that have complained are Y% of it." One page. If the numbers don't show a serious risk, I'm wrong and you should say so.

## 3. Propose a capacity split, not a switch

Offer the CEO two or three explicit options and a recommendation, so they are still deciding. Here is the shape I'd recommend:

- **Ring-fence a customer-fix squad.** Roughly 30 to 40% of product and engineering capacity stays on the three complaints for the whole quarter. This is a standing allocation with named owners, not whatever is left over.
- **Rebrand gets the rest, scoped to what has real deadlines.**
  - Name in the app, domain and marketing site: do these, they are mostly low engineering cost.
  - Design system: ship tokens, colour, typography and logo as a skin on the existing components. Defer the full component rebuild and any screen-by-screen redesign to Q2 and Q3, and do it incrementally.
- **Sequence for risk.** Put the fixes with the shortest path to customer-visible relief first (invoicing performance, then the integration). Reports go in a staged plan, with the top two or three reports by usage first.

Present the alternatives honestly: all-in rebrand (what leadership asked for), the split above, and fixes first with a rebrand in Q2. Say what each costs in churn risk, NPS and rebrand dates. Most CEOs will pick the middle option when it is laid out with the risk attached.

## 4. Watch for the hidden coupling: the domain change touches the integration

A new domain is not just DNS. It affects OAuth redirect URIs, webhook endpoints, allow-lists on the customer side, SSO and SAML config, email sending (SPF, DKIM, deliverability), API base URLs, embedded links, SEO and redirects. The accounting integration is already broken, and a domain cutover can break it again or make it harder to debug. So:

- Run the integration fix before the domain cutover, or at least agree a freeze window around it.
- Keep the old domain working with redirects and dual support for a long period. Don't hard-cut over.
- Warn customers with integrations early, and tell support exactly what is changing and when.

This is also your strongest practical argument for sequencing, because it is a technical dependency and not a preference.

## 5. A Q1 shape (adjust to your dates)

- **Weeks 1 to 2:** Gather the data above. Write the one-page options memo. Get decisions on the split. Name an owner for each customer problem and for the rebrand workstreams. Inventory every place the old name and domain appear (app, emails, docs, contracts, integrations, app store listings, partner pages).
- **Weeks 3 to 8:** The fix squad works on invoicing performance and the integration. The rebrand team builds the token-based design skin, name changes and the marketing site. Run a staging environment on the new domain, with redirects and integration tests, before any cutover.
- **Weeks 9 to 10:** Domain cutover with the freeze window, a rollback plan and a support runbook. Do not do this in the same week as a major invoicing release.
- **Weeks 11 to 13:** Launch the brand. Ship the first reports. Review results against the targets below, and plan Q2 (component migration, the remaining reports).

## 6. Targets that show whether the plan works

- Invoicing p95 latency (or whatever slow means in practice: time to generate, send or load) against an agreed target.
- Accounting integration: success rate and open tickets, and the number of affected accounts reconnected.
- Reports: the top-requested ones shipped, with usage tracked.
- A pulse NPS or CSAT on affected accounts mid-quarter, not just the next full survey.
- For the rebrand: milestones met, with no regressions in sign-in, billing or integration traffic after cutover.

Measure these at team level. Don't use them to rank individuals, because that will push people to game them and to avoid the hard fixes.

## 7. How to handle "leadership decides, teams execute"

Take it at face value and use it. Leadership has decided to rebrand, so the teams will execute it. Leadership has not yet decided how much customer risk it will accept to hit the date, so give it that decision explicitly, with the options and the numbers. That is leadership deciding, and it is better informed. Don't ask for permission to protect customers, and don't quietly slow the rebrand either. If the CEO still picks all-in on the rebrand, write down the risk you flagged and the metrics you will watch, so that if renewals soften you have a clear record and an agreed trigger to rebalance (for example, a named account at risk, or NPS falling again).

## Pushback and caveats

- I don't know your data. If the NPS drop is mainly integration pain from the merger (customers who were moved onto a different product), the fix is more urgent than for a general quality issue. If it's concentrated in a few large accounts, you can protect those directly.
- If the three problems have no clear owner or estimate, the first job is to get one. A plan that says "30% on fixes" with no owners won't hold.
- If the rebrand has a hard external date (legal, a contract or a trade event), that changes the split, and you should find out which dates are real and which are only preferences.

If you tell me the real dates, team sizes and the estimates for each complaint, I can turn this into a week-by-week capacity plan and draft the one-page memo for the CEO.
