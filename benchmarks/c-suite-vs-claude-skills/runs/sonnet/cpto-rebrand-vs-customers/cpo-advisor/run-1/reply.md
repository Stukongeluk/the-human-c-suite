## Bottom line

Don't plan Q1 as "everyone on the rebrand". Take a different decision to the CEO: the rebrand ships in Q1, but on a ring-fenced share of capacity. The rest goes to the three complaints that took NPS from +28 to +4. This is still a leadership decision, so it fits "any decision beats no decision". It just prices the trade-off the current plan leaves out.

Proposed split (a starting point, to be checked against real capacity): about 40-50% of product and engineering on the rebrand, about 40-45% on invoicing, the accounting integration and reports, and about 10% as buffer for incidents and merger integration work. Rebrand scope is cut to what is externally visible and contractually or legally necessary. The rest moves to Q2.

Confidence: medium on the direction, low on the exact percentages. I haven't seen your capacity, churn or renewal data.

## What I'm confident in, and what I'm not

- **[verified, from what you told me]** NPS fell from +28 to +4 while three specific complaints stayed open for months. A 24-point drop with named, unfixed causes is a retention problem that hasn't yet shown up in revenue.
- **[verified]** A full-org Q1 rebrand means zero capacity for those complaints for roughly a quarter on top of the months already lost. Customers will experience that as "they renamed themselves and still didn't fix invoicing".
- **[medium]** Post-merger, many customers are already unsettled. A new name, new domain and new design system add change they didn't ask for. Detractors are most likely to use that moment to evaluate alternatives. I'd expect renewal risk to be concentrated here, but you need to confirm it.
- **[assumed]** That the three complaints drive the NPS drop. Check this before committing (see step 1).
- **[assumed]** That the rebrand has a hard external date. If it does, I'd like to know what it is and why. If it doesn't, the case for protecting customer fixes gets stronger.

## Why this plan and not the alternatives

1. **"Everyone on the rebrand" bets the base to fix the brand.** The cost isn't visible in Q1. It appears in Q2-Q3 as churn, lower expansion and weaker renewals, once the decision can't be reversed.
2. **Doing only the customer fixes is also a mistake.** Running two brands and two domains post-merger has its own cost: confusion, duplicated marketing and a support burden. A split plan is cheaper than either extreme.
3. **A rebrand is highly parallelisable and mostly cosmetic.** Naming, design tokens, domain and marketing site need design, front-end and marketing capacity, and little of the deep backend work that invoicing speed and the accounting integration need. Splitting by skill, not by headcount, is realistic: designers and front-end lean to the rebrand, backend and integration engineers lean to the fixes. You will still have a shared bottleneck, so check it.
4. **"Teams execute" works better when leadership decides the outcome and constraints.** Leadership decides: the rebrand ships, the NPS recovers. Teams decide how to sequence work to get both. That keeps the CEO's principle intact.

## How to act

**Week 1-2: get the evidence (you can do this yourself)**
- Pull NPS detractor verbatims and tag them. What share mention invoicing, the integration or reports? Do the same for support tickets and churn-reason notes.
- Find out which accounts have affected renewals in the next two quarters and their ARR. Even a rough list of "at risk" ARR is the most persuasive number you can bring.
- Talk to 8-10 detractors yourself, including at least two high-ARR accounts. Per the skill's red flags, a CPO who hasn't spoken to a customer in 30+ days is guessing.
- Get real capacity per team from the engineering and design leads, and map which teams the rebrand actually needs.
- Diagnose each complaint, so the fixes are scoped honestly: why is invoicing slow (query, architecture, third-party)? What exactly is broken in the integration (API change, auth, mapping)? Which reports are missing, and which three matter most?

**Week 2: take a decision memo to the CEO**
One page: the NPS trend, at-risk ARR, the proposed split, and what the rebrand loses (list items moving to Q2). Frame it as "how do we land the rebrand without losing customers", not "should we do the rebrand". Offer the CEO a clear choice with the numbers:
- Option A (CEO's current plan): full rebrand, zero fixes, expected exposure of X ARR.
- Option B (recommended): the split above.
- Option C: fixes first, rebrand in Q2.

**Q1 structure**
- **Rebrand track (about 40-50%):** the new name in the app, the domain migration with redirects, SEO and email, and the marketing site. Ship a thin version of the design system (tokens, core components) and apply it to the highest-traffic screens first. Migrate the rest in Q2. Don't rewrite every screen.
- **Customer track (about 40-45%):** one team per complaint with a named owner and one measurable target each, such as invoice generation time, integration success rate and the top three reports shipped. Review progress every two weeks with customers who raised them.
- **Buffer (about 10%):** incidents, merger integration surprises and rebrand slippage.
- **Sequence:** fix the integration first, since "broken" is worse than "slow" or "missing". Pair the domain and name change with a customer communication plan, so that customers hear about the fixes and the new name together.
- **Metrics:** track NPS monthly (the skill's dashboard cadence), detractor themes, at-risk renewals, invoice latency and integration error rate. Measure teams, not individuals.
- **Checkpoint at week 6:** if the fixes are on track and capacity allows, pull more rebrand work forward. If not, re-balance. This is how you keep a decision firm while still reacting to evidence.

## Things to watch

- If the rebrand has a legal, contractual or regulatory deadline (for example, a merger agreement), that part is non-negotiable. Separate it from the nice-to-have parts.
- A new domain is where the real risk sits: SSL, email deliverability, SSO callbacks, integration redirect URIs (including the accounting integration), and customer allow-lists. Plan the cutover carefully and don't tie it to the same week as the integration fix.
- If capacity turns out to be much tighter than assumed, drop scope on the design system, not the customer fixes.
- If the CEO still says no, document your recommendation and the risk, then execute well. Make the cost visible monthly so the decision can be revisited with data.

## Your decision

1. Are you willing to take Option B to the CEO, with the evidence from weeks 1-2 behind it?
2. Is there a hard external date on the rebrand, and who set it?
3. Which of the three complaints has the biggest ARR attached? That one goes first.

If you share capacity per team, the at-risk renewal list and the detractor themes, I can turn this into a concrete team-by-team allocation and the CEO memo.
