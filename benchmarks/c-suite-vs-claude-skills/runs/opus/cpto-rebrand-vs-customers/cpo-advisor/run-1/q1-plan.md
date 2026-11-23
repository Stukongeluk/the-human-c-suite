# Q1 2027 plan: rebrand and customer recovery

*Draft by the Head of Product. Status: proposal for leadership. Numbers in [brackets] get filled in from the evidence pack and sizing, due by 11 Dec. Assumptions are listed in section 9.*

---

## 1. One-page memo for the CEO

**Decision needed (week of 14 Dec):** how product and engineering capacity is split in Q1.

**Context**
- We are rebranding in Q1: a new name in the app, a new design system, a new domain and a new marketing site. Leadership has decided this, and the plan delivers it.
- NPS has fallen from +28 to +4. The top three complaints have been open for months: slow invoicing, a broken accounting integration and missing reports. Accounts raising them represent [€X ARR], and [€Y] of that renews in H1.
- The new domain affects the same areas customers complain about: invoice emails, the accounting integration and SSO.

**Options**

| | Ships in Q1 | Waits | Customer impact | Main risk |
|---|---|---|---|---|
| A. Everyone on the rebrand | Full rebrand, including the design system on every screen | All three fixes, until Q2 at the earliest | Launch on an unchanged product. Complaints stay open at least another quarter on top of the months already open | H1 renewals among unhappy accounts. Launch messaging gets drowned out by "same bugs, new name" |
| **B. Rebrand core + protected recovery** | Name, theme, domain and site. Integration fixed, invoicing faster, top reports shipped | Remaining screens move to the new component library in Q2–Q3 | Launch with proof: "new name, and we fixed what you asked for" | Two tracks need tight coordination. Mixed old and new components inside the app for a while |
| C. Fix first, rebrand Q2 | The three fixes | Whole rebrand | Best short term | Reverses a leadership decision. Two-brand confusion runs longer |

**Recommendation: B.** It delivers the rebrand in Q1 and gives the launch something real to announce. Cost: full visual consistency on every screen arrives in Q2–Q3, not Q1.

**What I need from you**
1. A decision between A, B and C by 18 Dec.
2. A confirmed launch date, and confirmation of whether anything external fixes it (trademark, merger agreement, contracts).
3. Agreement that the [N] teams owning invoicing, integrations and reporting are protected for Q1, with a rebalancing checkpoint on 26 Feb.

---

## 2. Before Q1 starts (23 Nov – 1 Jan)

| When | What | Owner | Output |
|---|---|---|---|
| Week of 23 Nov | Call 10 detractors yourself. Pull the last 6 months of NPS comments and tag them by theme | Head of Product, Customer Success | Do the three complaints explain most of the drop? |
| By Fri 4 Dec | Evidence pack: revenue and renewal dates per affected account, ticket volumes, integration failure rate by error type, invoice-time baseline (p50/p95) | Head of Product, RevOps, Data, Support | One-page evidence summary |
| By Fri 11 Dec | Bottom-up sizing. Rebrand split into launch core vs full design-system migration. The three fixes sized | VP Eng/CTO, Head of Design, Platform lead, team leads | Capacity table: team, track, weeks |
| By Fri 11 Dec | Score the rebrand workstreams and the three fixes on one sheet (RICE: reach, impact, confidence, effort, with revenue affected as reach) | Head of Product | One ranked list, not two competing ones |
| Week of 14 Dec | Decision meeting with the CEO (memo above) | Head of Product | Written decision, recorded with its accepted risks |
| By Fri 18 Dec | Teams turn the decision into Q1 plans and confirm owners | Track owners | Q1 plan per team |

---

## 3. Q1 tracks (Q1 runs from 4 Jan, week 1, to 31 Mar, week 13)

### Track 1: Rebrand (owner: [rebrand program lead])

| Workstream | Scope | Who | Notes |
|---|---|---|---|
| Brand foundations | Design tokens (the shared colour, type and spacing values), logo, icons. Applied as a theme to existing components | Design system team | Changes the look across the app quickly, without rebuilding every screen |
| Name in product | In-app text, transactional emails, PDF templates, help center, API docs, legal pages, mobile store listings | A text sweep across feature teams (days per team, not weeks), plus docs and legal | Mobile store review and legal sign-off have lead times |
| Domain | See the checklist in section 4 | Platform team, plus the integrations team for its own cutover | The riskiest workstream. Start in week 1 |
| Marketing site | Content, design, build, SEO redirects | Marketing, with a web team or agency | Product and engineering only for the signup, login and pricing hand-offs |
| Design-system migration | Component library v1 (most-used components) in Q1. Screens migrate in Q2–Q3 | Design system team, then each team as it touches screens | Screens rebuilt for Track 2 go first |

**Milestones**
- **Weeks 1–3:** tokens and theme finished. Domain basics in place: DNS, certificates, and email authentication (SPF/DKIM/DMARC). Warm-up of the new sending domain starts with low-risk email, not invoices.
- **Weeks 3–6:** theme rolled out app-wide behind a flag. Text, emails and PDF templates updated. SSO and OAuth (the accounting providers' login settings) accept both domains. Notice goes to enterprise customer IT in week 4, at least 6 weeks before cutover.
- **Weeks 7–9:** internal staff use the new domain first. Beta with 10–20 friendly customers. Marketing site on staging.
- **Weeks 10–11:** gradual cutover. The web app moves to the new domain and browser traffic from the old domain is redirected. API and webhooks keep working on both domains.
- **Week 12 (from 22 Mar), or the date leadership sets:** public launch.
- **After Q1:** screens move to the new components in Q2–Q3. Invoice emails switch to the new domain once warm-up numbers are healthy.

### Track 2: Customer recovery (owner: [recovery track lead])

The order below is provisional; confirm it with the evidence pack.

**1. Accounting integration: broken, so treat it as a defect, not a feature** (integrations team)
- Weeks 1–2: measure sync success and failure by error type and provider. Find the root causes of the top failures (start in December if possible).
- Weeks 3–6: ship fixes behind a flag to affected accounts. Reconcile any data that failed to sync, and tell those customers exactly what was fixed.
- Weeks 7–10: roll out to everyone. Do this team's domain cutover in the same window, so one team owns all of the integration's risk.
- Target: sync success from [baseline]% to [target]%, and integration tickets down [Y]%.

**2. Slow invoicing** (team that owns invoicing)
- Weeks 1–2: measure the invoicing flow end to end (create, generate, send, batch runs) and find the bottleneck.
- Weeks 3–8: fix the biggest bottleneck, ship it, and measure the result. Then fix the next one.
- Rebuild the invoicing screens you touch in the new design system.
- Target: p95 invoice time from [baseline] to [target], and invoicing tickets down [Y]%.

**3. Missing reports** (team that owns reporting)
- Weeks 1–3: discovery with 8–10 customers who asked for reports, with PM, designer and tech lead together. Find out which 2–3 reports cover most requests. Consider an export or API as a stopgap.
- Weeks 4–6: test a prototype with 5–8 customers.
- Weeks 7–11: build the reports in the new design system, and include them in the launch story.
- Target: [2–3] reports shipped, and the share of report-related tickets down [Y]%.

**Week 13:** measure everything. Send an NPS pulse to the affected accounts and the detractors you called. Feed the results into Q2 planning.

### Shared rhythm
- **Weekly:** one 30-minute review across both tracks, using the scorecard in section 5, with cross-track risks first.
- **Fri 26 Feb (end of week 8):** rebalancing checkpoint with leadership. Move capacity based on progress and renewal data.
- **Protected capacity:** on-call, incidents and security work are planned explicitly at [10–20]%, not taken quietly from either track.

---

## 4. Domain migration checklist

- [ ] **Old domain stays alive for years, not weeks.** Invoices already sent contain payment and view links, and customers have API scripts and bookmarks pointing at it.
- [ ] **Browser traffic:** permanent redirects, mapped page by page, including deep links.
- [ ] **API and webhooks:** serve on both domains. Many API clients don't follow redirects on POST requests. Announce a long deprecation window.
- [ ] **SSO:** SAML and OIDC settings (ACS URLs, redirect URIs, entity IDs) accept both domains. Enterprise customers' IT teams must update their identity provider settings, so give at least 6 weeks' notice and offer help.
- [ ] **Accounting provider apps:** register the new redirect URIs alongside the old ones, and check whether a changed name or listing triggers a marketplace review (which can take weeks).
- [ ] **Email:** set up SPF, DKIM and DMARC on the new domain and warm it up gradually. Keep invoices and payment reminders on the proven domain until deliverability is confirmed.
- [ ] **Sessions:** cookies don't move across domains. Plan for users being logged out, and for SSO re-login and password-manager prompts.
- [ ] **Customer allowlists:** firewalls, email allowlists and embedded widgets (content security policy) at customer sites. Include this in the customer notice.
- [ ] **Mobile:** universal links and deep links, app store listings, any review lead times.
- [ ] **Infrastructure:** certificates, CDN, CORS (rules on which other sites can call your servers), content security policy headers, monitoring and alerting on both domains.
- [ ] **SEO:** a redirect map for the marketing site, plus the change-of-address tool in Google Search Console.
- [ ] **Rollback plan:** you can point traffic back to the old domain within minutes.

---

## 5. Q1 scorecard (weekly to leadership)

| Area | Metric | Baseline | Q1 target | Owner |
|---|---|---|---|---|
| Rebrand | Launch milestones on track | — | Launch week 12 | Rebrand lead |
| Rebrand | Serious incidents (Sev1/Sev2) caused by the migration | — | 0 | Platform lead |
| Rebrand | Enterprise SSO customers moved to the new domain | 0% | [90]% by launch | Platform lead + Customer Success |
| Rebrand | Invoice email deliverability (bounces, spam complaints) | [ ] | No worse than baseline | Platform lead |
| Recovery | Accounting sync success rate | [ ]% | [ ]% | Integrations lead |
| Recovery | Invoice time, p95 | [ ] | [ ] | Invoicing lead |
| Recovery | Tickets on the three themes per week | [ ] | −[Y]% | Support lead |
| Recovery | Revenue renewing in H1 from affected accounts that is still at risk | [€ ] | Falling month on month | Customer Success |
| Lagging | NPS (monthly, plus affected accounts separately) | +4 | Upward trend. Don't promise +28 back in one quarter | Head of Product |

**North star proposal for after Q1:** weekly active accounts that create invoices and sync them to accounting without errors. This measures the customer value the product exists for, and every team can influence it. *(Assumed: invoicing is the core job. Adjust it to your product.)*

---

## 6. Customer communication

- **Now (December):** tell accounts with open complaints when the fixes will come, and in which quarter. Don't let the rebrand announcement be the first thing they hear from you.
- **Week 4:** technical notice to enterprise IT contacts about the domain, covering SSO, allowlists, API and webhooks.
- **Launch:** "New name, and here is what we fixed": the integration, invoicing speed and the new reports, each with a concrete before-and-after.
- **Week 13:** go back to the detractors you called and show them what changed.

---

## 7. Teams and ways of working

- Explain the *why* for both tracks to every team. When teams understand the goal, they often find cheaper ways to get there, for example a theme instead of a full rebuild of every screen.
- Put people from both legacy companies on both tracks. The rebrand is also a chance to make one team out of two.
- Whatever leadership decides, execute it openly. No side roadmap and no quietly slowing down the rebrand. If the plan needs to change, raise it at the 26 Feb checkpoint with data.
- Hold one 30-minute review across both tracks every week, not a separate status meeting for each.

---

## 8. If leadership chooses A (everyone on the rebrand)

- Execute it fully and well.
- Ask explicitly, in the open, for a small named team to handle the broken integration as a defect. A core money flow that fails is not roadmap work.
- Tell affected customers now when the Q2 fixes will come.
- Record the accepted risk in the decision, and review it on 26 Feb against renewal and ticket data.
- Do the reports discovery interviews in Q1 anyway (a few days of PM and design time), so Q2 starts with a validated plan.

---

## 9. Assumptions and what would change the plan

| Assumption | Confidence | How to verify | If wrong |
|---|---|---|---|
| The three complaints explain a large part of the NPS drop | Medium | Tag detractor comments by theme; call detractors | Follow the real cause (for example, merger migration pain) and re-rank Track 2 |
| There is one product, or the legacy products are already merged | Assumed | Product inventory | If two apps are still live, the rebrand roughly doubles in cost and Option B matters even more |
| The Q1 date is not fixed by a legal or contractual constraint | Assumed | Ask the CEO and legal | The launch core is fixed. Track 2 then sizes around it |
| Invoices are emailed from your domain, you offer SAML SSO, and the integration uses OAuth with accounting providers | Assumed | Platform lead | Drop the checklist items that don't apply |
| The brand identity (name, logo, colours) is already designed | Assumed | Brand or marketing lead | If not, tokens slip, so start the domain and Track 2 first |
| Q1 = calendar Q1, 4 Jan – 31 Mar 2027 | Assumed | Finance calendar | Shift the dates |
| On-call, incidents and security work take 10–20% of capacity | Assumed range | Last two quarters' data | Use the real number in the capacity table |
| About a quarter of capacity sits in the teams that own the three problem areas | Assumed (starting guess) | Sizing on 11 Dec | Use the sized number. The principle of protecting those teams stays the same |

**What would make me drop Option B:** the evidence shows the three complaints don't drive dissatisfaction or renewal risk, *and* sizing shows the full design-system migration genuinely needs the whole organisation to land in Q1.

**Still to validate with:** CFO and Customer Success (revenue at risk), VP Eng (sizing and timeline), CMO (launch date and messaging), Legal (any fixed rebrand deadline).
