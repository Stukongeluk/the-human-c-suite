**Short version:** don't plan Q1 as "rebrand versus customers", and don't reopen whether to rebrand. That's decided, and after a merger you probably do need one name. The open question is how the rebrand is staffed and in what order, and proposing that is your job. Size both pieces of work, put the revenue at risk next to them, and bring leadership one decision with a deadline. Then commit to whatever they choose, with the trade-off written down.

The strongest plan has the rebrand launch *with* the fixes. "New name, and here's what we fixed" beats "new name, same problems".

## Why putting the whole org on the rebrand is a weak plan, even by leadership's own goals

- **The new name launches on a broken product.** Under the new name, customers will first notice slow invoicing and a broken accounting integration. A 24-point NPS drop in the year after a merger usually means customers are asking whether the merger was good for them. The rebrand is when they'll decide.
- **The domain move touches the things that are already broken.** New domain means new OAuth redirect URIs and webhook URLs registered with the accounting providers. It may also mean re-listing the integration under the new name in their marketplaces, so check their review lead times now. And invoice emails will go out from a domain with no sending reputation. Do this carelessly and the integration and invoicing complaints get worse. Do it well and fixing the integration becomes part of the migration.
- **The work can't be split across the whole org at once.** A design system needs a small core team to build tokens and core components before product teams can move any screens. Put everyone on it in week one and you get idle teams, collisions in the same UI code, and rework. That early stretch is exactly where the customer fixes fit.
- **Your teams know what's broken.** Asking engineers to restyle buttons while complaints they've watched for months sit untouched costs you trust, and eventually people. That matters more when two companies' teams are still getting used to each other.

## How I'd plan it

### 1. Get the facts in the first two weeks (or before Q1 starts)

- **Break the rebrand into workstreams, size each one and give each an owner:**
  - In-app name: strings, logos, emails, generated PDFs such as invoices, legal pages.
  - Design system: the foundations, which screens move in Q1, and which move later.
  - Domain: DNS, certificates, SSO/SAML, OAuth, API base URLs, webhooks, cookies, SPF/DKIM/DMARC and warming up the new sending domain, redirects, customer allowlists.
  - Marketing site: mostly marketing and an agency, plus a few web engineers.
- **Size the three complaints.** Complaints that stay open for months usually have no owner. Give each one an owner and a one-week root-cause investigation. Some may be smaller than they look. Slow invoicing, for example, sometimes comes down to a single query or a missing background job.
- **Put money next to the NPS**, because leadership can wave NPS away on its own. Pull:
  - ARR renewing in Q1–Q2 at accounts that raised these issues.
  - Churn and downgrade reasons since the merger.
  - Support tickets and hours spent on the three themes.
  - Whether the drop is concentrated in one of the legacy customer bases.

  Ask the CRO, CFO and head of customer success to check the figures. Then they're backing them in the meeting, and you're not the only one carrying the bad news.

### 2. Bring leadership one decision, not a debate

Put the options on one page. I've drafted it for you in `q1-decision-memo.md`. The core of it:

| | A: As decided | B: Recommended | C: Minimum |
|---|---|---|---|
| Rebrand | Whole org | Staffed to its sizing, same launch date | Whole org minus one squad |
| Customer fixes | After Q1 | Ring-fenced squad(s), roughly 20–25% of capacity | One squad, integration only |
| Launch story | New name | New name plus three fixes | New name plus integration fix |
| Main risk | [€ ARR] renews on a broken product | Rebrand scope held to what was sized | Invoicing and reports wait until Q2 |

Use the CEO's own words. "Any decision beats no decision": agreed, and those three complaints are the biggest *non*-decision in the company right now. You're asking leadership to make it. "Leadership decides, teams execute": also fine. Your part is making sure leadership decides with the costs in front of it. Be explicit that you're not reopening *whether* to rebrand, only *how it's staffed*. Walk the CEO through it one-to-one before the group meeting so nothing surprises them, and ask for the decision in the meeting.

### 3. Shape the quarter (option B)

As a starting split: about 60% rebrand, 25% customer fixes, 15% keeping the lights on and handling incidents. That last slice exists whatever the plan says. Adjust the split once the sizing is in.

- **Weeks 1–4.**
  - Rebrand: a core design-system team builds the foundations. If you can, staff it with people from both legacy companies; it becomes the merged product's shared language. The platform team plans the domain move and starts the partner re-registrations and email warm-up. Someone lists every place the old names appear.
  - Customer squad: fixes the accounting integration first, since the domain move depends on it anyway. Finds the root cause of slow invoicing. Ships an interim export for the missing reports.
- **Weeks 5–9.**
  - Rebrand: product teams move the most-used screens to the new design system. Both domains run side by side in staging.
  - Customer squad: builds the missing reports *on* the new design system. A real feature is the best test of a design system, and the two tracks become one piece of work. Ships the invoicing fix.
- **Weeks 10–13.** Launch the name in the app, the new domain and the new site. Keep the old domain, API base URLs and webhooks working for at least a year. Lead the launch announcement with the fixes, and keep extra support cover for two weeks afterwards.
- **Not in Q1:** moving every last screen to the new design system. Teams move the rest when they next touch those screens. Write that down so the rebrand doesn't quietly take over Q2.

### 4. Tell customers now, not at launch

Have customer success contact the detractors and the at-risk accounts with honest dates for the three fixes. Going back to the people who complained is a big part of winning them back, not only shipping the fix. B2B customers also need several weeks' notice to allowlist a new domain for email and firewalls. Otherwise your invoices land in spam on launch day.

### 5. Measure what actually moves, and agree tripwires up front

- **Weekly:** integration sync success rate, invoice generation time (p95), tickets on the three themes, renewal outcomes at the flagged accounts, rebrand milestones.
- **NPS:** run it again about six weeks after the fixes ship, not before.
- **Mid-quarter review:** agree it with leadership now. If named accounts signal churn, or the rebrand slips, the split gets revisited at that review instead of argued over along the way.

## If leadership still says "everyone on the rebrand"

Then deliver it well, and:

- Write the decision down with the trade-off and the ARR at risk, and agree a date to review it.
- Do the integration and email work the domain move really requires, and say openly that it's there and why. Don't run a hidden roadmap. When it surfaces, it costs you the credibility you'll need for the next argument.
- Give customers honest dates, even if they're in Q2.
- Don't let the teams pay for the plan with overtime. If the scope doesn't fit, cut scope, not weekends.
- Bring the renewal numbers to that review.

You'll likely be held responsible for NPS and retention either way. Making the trade-off explicit isn't disloyalty to the CEO's decision. It's what your role is for.
