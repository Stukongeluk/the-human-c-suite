Don't set Q1 up as "rebrand vs. customers". Set it up as "a rebrand that works", and make the case that a rebrand can't work if the new name goes out on a product whose NPS just dropped 24 points. Accept that the rebrand happens in Q1. Push back, with numbers, on one specific assumption: that it needs the *whole* organisation. Then take leadership a decision to make, not a debate to have.

Here's how I'd do it.

## 1. Separate what's decided from what's only assumed

**Decided:** there's a rebrand, and it's in Q1.

**Probably assumed, not decided:** that every team has to work on it; that all four parts (name, design system, domain, site) must land in full in Q1; that the customer issues wait until it's done.

Find out what the real deadline is and why it exists: a legal entity change, a contract on the old brand ending, a launch event, an investor milestone. That tells you which parts are fixed and which can flex. Often "the whole org on the rebrand" was a rough capacity guess, not a deliberate choice to leave customers waiting. Treat it that way until someone says otherwise.

## 2. Size the rebrand properly. It probably can't use the whole org.

The four parts are very different kinds of work:

- **New name in the app.** Lots of small changes everywhere: UI text, logos, emails, PDFs (invoices included), notifications, help centre, app store listings, and third-party listings. That includes your accounting integration's listing in the partner's marketplace, which usually has to go through the partner's review. Mostly inventory work: one or two teams, plus a few days from everyone else.
- **Design system.** Hard and slow. A realistic Q1 goal is design tokens, core components, and the most-used screens. Fully moving both legacy products onto it takes several quarters. Demanding a full redesign in Q1 is the biggest scope risk.
- **New domain.** A small team, high risk, and hard to undo. It touches SSO/SAML setups, OAuth redirect URIs (the accounting integration's too), API base URLs and webhooks that customers have hard-coded, cookies and sessions, CSP/CORS, and customers' IT allowlists. It also touches email: SPF/DKIM/DMARC and sender reputation. Invoices sent from a new, unwarmed domain can land in spam, and then "slow invoicing" becomes "missing invoices". Check your contracts for required notice periods. Keep the old domain and old API hosts working for a long time.
- **Marketing site.** Mostly marketing plus a web team or agency. Product engineering is only needed for signup, login and pricing links.

Ask each lead for an honest estimate in people-weeks. I expect the total to be well below "everyone". Past that point, adding people slows the work down: more coordination, more people editing the same components, more handoffs.

## 3. Put a price on the customer issues

Take a week or two and turn the complaints into numbers leadership will act on:

- Which accounts have raised each of the three issues, their ARR, and their renewal dates in H1.
- Churn, downgrades and lost deals since the merger that cite these issues.
- Support ticket volume and cost for these themes.
- NPS detractors and comments, split by legacy company and by theme. A merger drop and a product drop need different fixes.
- For the accounting integration: is it producing wrong or missing financial data? If it is, it's a defect with trust and possibly legal consequences, not a roadmap item, and roadmap freezes shouldn't apply to it.

The aim is one sentence: "X in ARR renews in H1 among accounts hit by these three issues."

## 4. Recommend an option

- **A. Everyone on the rebrand (the current plan).** The fixes slip to Q2 at the earliest, on top of the months they've already been open. The new name launches to customers who are currently near-neutral or unhappy. X ARR is at risk.
- **B. Rebrand plus a protected customer team (my recommendation).** Staff the rebrand at what it can actually use, likely around two-thirds to three-quarters of capacity. Give one or two named teams the integration and invoicing problems, with dated targets, and limit reports to the two or three customers ask for most. Keep roughly 10% for on-call and maintenance, which was never really zero anyway. Q1 still delivers the name, the design system foundation and the site. The domain switch happens at the end of Q1, or early Q2 if notice periods require it.
- **C. Fixes first, rebrand moved into Q2.** Only worth proposing if the data shows severe churn coming soon.

Why B makes the rebrand *better*, not just nicer for customers:

- **A rebrand is a promise.** Customers judge the new name by what using the product feels like. Bugs they've reported for months, now under a new logo, make the new brand stand for "same problems, new name". After a merger, a rename can also read as "the product we bought is going away".
- **It gives marketing a launch story:** "New name, and we fixed what you told us."
- **The rebrand touches invoicing and the integration anyway** (invoice templates, sender domain, marketplace listing, redirect URIs). Have the team fixing those areas also make the rebrand changes there: one team and one set of changes instead of two teams colliding.

## 5. Take it to the CEO in his own terms

Don't argue with "leadership decides, teams execute" or "any decision beats no decision". Use them. Bring a one-page proposal: the options, the cost of each, your recommendation, and a date you need the decision by. Open with something like:

> "I'm committed to delivering the rebrand in Q1, and here's the plan to do it. I need one decision from you: do we leave these three customer issues untouched for another quarter? Here's what that costs."

This respects his authority and turns a hidden trade-off into an explicit decision, which is exactly what he says he wants. If it comes up, "any decision beats no decision" holds for decisions you can reverse. The domain switch is the one part that deserves extra care. Make that point briefly and don't lecture.

Talk to the CRO/CFO and the head of Customer Success beforehand. They own renewals. If the revenue number is real, they'll make the case more forcefully than you can.

## 6. If the answer is still "everyone on the rebrand"

Then deliver it fully and well. A few safeguards:

- **Ask for the minimum carve-outs.** On-call and maintenance, plus the integration fix if it's corrupting financial data.
- **Write down the decision and the risk accepted.** Agree tripwires that reopen it, e.g. a top-20 account escalates, churn in the affected group passes X, or integration failures pass Y.
- **Get a dated Q2 commitment for the fixes** and let Customer Success give customers the honest date. A dated plan beats silence.
- **Tell your teams plainly what was decided and why.** Don't pass blame down.

## 7. The Q1 plan itself (assuming B)

**Weeks 1–2 (start in December if you can)**
- Rebrand sizing and the customer data.
- Leadership decision.
- Domain notices to customers if contracts require them.
- Design token decisions.
- Root-cause analysis on the integration.

**Weeks 3–8**
- Customer team:
  - Integration fix, plus repairing affected customers' data.
  - Invoicing profiling and quick wins.
  - The top two or three reports.
- Rebrand:
  - Text and asset inventory, with the rename behind a feature flag.
  - Design system foundation.
  - Domain dry runs on staging.
  - Email domain authentication and warm-up.
  - Accounting-marketplace resubmission started early.

**Weeks 9–13**
- Launch: name, site and the "what we fixed" message together.
- Domain switch in a quiet window, with long-lived redirects and the old API hosts still working.
- Design system on the top screens; the rest continues in Q2 and beyond.

**What to measure**

For the rebrand:
- Launched on the date.
- No severity-1 incidents from the domain switch.
- Email deliverability.
- Organic search traffic kept.
- Login/SSO tickets.

For customers:
- Integration sync failure rate.
- Invoice run time (p95).
- Ticket volume on the three themes.
- NPS among affected accounts.
- Renewal rate of the at-risk group.

Measure teams and outcomes, not individuals.

## 8. Use it to bring the merged org together

The design system is a natural place to mix designers and engineers from both former companies, so the new brand belongs to both sides. Don't let the customer team become the "B team". Pick strong people, state its goals as openly as the rebrand's, and celebrate its results at launch alongside the new name.

I've put a one-page draft of the leadership proposal, with blanks for your numbers, in `q1-proposal-draft.md`.
