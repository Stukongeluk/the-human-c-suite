The rebrand and the customer fixes can both happen in Q1, but not at full scope, and not if the rebrand takes the whole organisation. My recommendation is to split Q1 into two protected tracks, put a hard cap on the rebrand, and bring leadership a trade-off with numbers instead of a refusal.

## 1. Reframe it as a trade-off, not a defiance

"Leadership decides, teams execute" is fine. Your job is to make sure leadership is deciding with the real cost in front of it. "Any decision beats no decision" is also fine, as long as the decision is made explicitly: "we are choosing to leave invoicing broken for another quarter", with the risk written down, is a legitimate decision. Making it by default, because nobody said the cost out loud, is not.

So don't go in saying "the rebrand is wrong." Go in saying "the rebrand is decided, and here is what it costs and how I propose to deliver it without losing the base we just merged."

## 2. Build the case with data before the meeting

You need a one-page brief. Gather:

- **Churn exposure.** Which accounts mention invoicing, the accounting integration or reports in NPS verbatims, support tickets and churn or cancellation notes? Convert to ARR at risk. A fall from +28 to +4 is a lot, but "€X of ARR sits with accounts that named these three issues" is what moves an executive.
- **Merger context.** After a merger, customers are already deciding whether to stay. A rename plus a domain change plus a new design system lands on top of unresolved problems and signals that the company is busy with itself. Check whether any of the complaints are really merger fallout (migrated integrations, merged invoicing logic).
- **Real cost of the rebrand.** Break it into the four items: name in the app, design system, new domain, marketing site. Estimate engineering and design weeks for each. My guess is that the design system is the largest and least time-bound item, and the domain move carries the most hidden risk (SEO, email deliverability, SSO and OAuth redirect URIs, integration allowlists, customer firewall rules, API endpoints and webhooks).
- **Open issue cost.** For the three complaints: how big is each fix, and what is blocking it? "Broken accounting integration" may be a two-week fix or a vendor dependency. Know which before you commit.

## 3. Propose a split of Q1 with explicit capacity

A reasonable starting shape (adjust to your numbers):

| Track | Share of product and eng capacity | Scope |
|---|---|---|
| Customer recovery | about 40-50% | Invoicing performance, accounting integration fix, the highest-value missing reports |
| Rebrand, minimum viable | about 30-40% | Name and logo in the app, domain move with a proper redirect and migration plan, marketing site |
| Platform, support, run | remainder | Incidents, security, and the work that keeps the lights on |

What to defer to Q2: the full design system rollout. A design system is an investment in consistency, not something customers see on day one. Ship the new name, logo, colours and typography through tokens and a thin theme layer now, and migrate components progressively. That gets the brand visible in Q1 without rewriting every screen.

Be careful not to let the rebrand quietly absorb the "run" bucket. Merged companies usually have duplicated systems, and rebrand work touches everything.

## 4. Sequence to reduce risk

- **Weeks 1-2:** Scoping and diagnosis. Fix owners named for each of the three complaints, with a size estimate. Rebrand inventory: every place the old name and domain appear (app, emails, docs, API, integrations, SSO, billing descriptors, legal pages).
- **Weeks 3-8:** Customer fixes ship in increments, not as one big release. Rebrand work focuses on things that are safe and reversible: in-app strings, theming, marketing site build on the new domain in staging.
- **Weeks 9-11:** Domain cutover rehearsed in staging. Communicate to customers early, with dates. Do not cut over in the same fortnight as a major invoicing or integration release, so that when something breaks you know which change caused it.
- **Week 12:** Cutover, monitoring, rollback plan ready. Retro.

The principle: never change the thing customers rely on (invoicing, integration) in the same window as the thing that touches how they reach you (domain, SSO, email). One risky change at a time.

## 5. Make the customer work visible to customers

Tell affected accounts what you are fixing and when. Frame the rebrand announcement alongside concrete improvements: "new name, and here is what we fixed". A rebrand that arrives with visible fixes reads as a company getting better; one that arrives alone reads as a company distracted. Put a named owner on each of the three issues, publish a short status note, and give your customer success team something specific to say.

## 6. Measure so the quarter can be judged

Set a handful of numbers and report them to leadership every two weeks:

- Invoicing: p95 time to generate or send an invoice, and the number of related tickets.
- Integration: error rate and number of affected accounts.
- Reports: shipped or not, and usage among the accounts that asked.
- NPS or a lighter pulse survey on the affected segment, plus churn and downgrades.
- Rebrand: milestone completion, domain migration incidents, organic traffic and email deliverability after cutover.

Measure teams and outcomes, not individuals. Under a merger and a rebrand, people are already stretched and uncertain, so avoid ranking anyone's output.

## 7. How to take it to the CEO

Something like:

> "We are doing the rebrand. To protect the customer base we just merged, I'm proposing we do it in two tracks: the visible parts (name, logo, domain, marketing site) land in Q1, and the full design system migrates over Q2. Roughly half of product and engineering stays on the three issues driving NPS from +28 to +4, which put €X ARR at risk. I'd like to review progress every two weeks, and if the customer metrics are not moving by week 6, we re-decide together."

That respects "leadership decides" because leadership still owns the call and gets a checkpoint, and it respects "any decision beats no decision" because you are bringing a concrete plan, not a delay.

If the CEO insists on 100% rebrand: ask for the decision in writing as an explicit choice to defer the three fixes, with an agreed date for when they get picked up, and make sure the risk is on the record. Then plan the rebrand as carefully as possible (rehearsed cutover, redirect map, customer comms), and put customer success on notice about the likely complaints. You can lose the argument and still protect the outcome.

## 8. Risks to watch

- Scope creep in the rebrand. The design system is the usual culprit. Fix scope and a date.
- Domain migration side effects: SSO, OAuth callbacks, webhooks, email authentication (SPF, DKIM, DMARC), customer allowlists, SEO. Give this a named owner.
- Team morale after the merger. Say clearly why both tracks matter, so people working on fixes do not feel like second-class work and rebrand people do not feel they are the problem.
- Estimates. Treat all of the above percentages as a starting hypothesis and replace them with real sizing in the first two weeks.

If you share the effort estimates for the three fixes and the four rebrand items, I can turn this into a week-by-week plan with capacity numbers.
