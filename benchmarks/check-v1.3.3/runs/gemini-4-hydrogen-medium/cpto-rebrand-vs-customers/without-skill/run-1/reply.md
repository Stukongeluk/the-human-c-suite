You can’t win a frontal fight against *"leadership decides, teams execute."* Trying to talk the CEO out of the Q1 rebrand will just make you look like you’re relitigating a closed decision.

Instead, accept the **what** (the rebrand ships in Q1) and take ownership of the **how**. Your job is to show leadership that putting 100% of a 400-person org onto CSS, copy, and a marketing site won’t actually ship the rebrand faster—and that launching a new brand onto a broken product with +4 NPS will turn a flagship relaunch into a churn event.

Here is how to plan Q1.

---

### 1. Reframe the Org Split: "Rebrand Critical Path" vs. "Launch Readiness"
At 400 people, your P&E org probably has ~120–180 people. You cannot usefully put backend, data, and integration engineers onto a marketing site or a logo swap—you’ll just create coordination drag.

Split Q1 into two tracks, both framed around **making the Q1 rebrand succeed**:

* **Track A — Rebrand Critical Path (~65–70% of P&E: Web, Design, Frontend, Platform/Infra)**
  * New marketing site & new domain cutover
  * In-app name/copy/asset replacement, email templates, invoice/PDF templates
  * Design system **v1 skin** (see below)
  * DNS, redirects, SSO/OAuth callback updates, email domain warm-up
* **Track B — Launch-Ready Customer Trust (~30–35% of P&E: Backend, Integrations, Data)**
  * **Broken accounting integration:** A domain and app-name change breaks OAuth apps, webhooks, and API callbacks anyway. Fixing the integration *as part of* the domain cutover is cheaper and safer than migrating a broken integration.
  * **Slow invoicing:** You already have to touch invoicing templates for the new brand/logo. Fixing the latency bottleneck at the same time prevents sending freshly rebranded invoices slowly (or failing to send them).
  * **Missing reports:** Pick the top 1–2 reports blocking Q1/Q2 renewals (especially post-merger parity gaps) and ship them as "Day 1 New Brand" readiness.

> **The framing:** You are not asking to *skip* the rebrand. You are deploying the engineers who don’t accelerate the rebrand to make sure the new brand doesn’t launch onto a burning house.

---

### 2. Defuse the Design System Trap
"New name, new domain, new marketing site" are bounded. **"New design system" in one quarter is where Q1 dies.**

If you try to rebuild your component library and rewrite every post-merger screen in 13 weeks, you will miss Q1 and ship nothing else. Separate the work into two phases:

* **Q1 (Ship with Rebrand): Design Tokens & Theme Layer.** New colors, typography, logos, and spacing applied to your *existing* components, plus the core app shell/navigation and top-traffic screens. To customers, it looks like the new brand on Day 1.
* **Q2+: Structural Design System Migration.** Gradually consolidating underlying component libraries and legacy post-merger UI.

Get explicit sign-off on this definition of "done" in Week 1.

---

### 3. How to Pitch This to Your CEO
Match their operating style: decisive, concise, no whining, and focused on outcomes. Don’t lead with team morale or tech debt—lead with **launch risk and renewal math**.

Bring a 1-page proposal with two clear options:

1. **Option 1 (Literal 100% Rebrand):** All P&E on rebrand/design system. *Risk:* Backend/data engineers are under-utilized, design system overhaul threatens the Q1 date, and we launch the new brand at +4 NPS with broken invoicing and accounting—driving churn right when marketing is spending to announce the new company.
2. **Option 2 (Recommended — Rebrand + Launch-Ready Core):** 100% commitment to hitting the Q1 rebrand date via Track A (token-based UI refresh, domain, marketing site) while Track B fixes the 3 launch-blocking customer issues so the relaunch drives retention instead of backlash.

Ask for a single yes/no decision on the scope boundary. That honors *"any decision beats no decision."*

---

### 4. A Realistic 13-Week Q1 Schedule
Do **not** schedule a big-bang domain + rebrand cutover for the last week of the quarter. Aim to launch in **Week 11** so Weeks 12–13 are a stabilization buffer.

* **Weeks 1–2: Audit & Scope Lock**
  * Inventory every brand/domain touchpoint across both merged stacks (app UI, auth/SSO, OAuth apps, webhooks, transactional emails, PDFs/invoices, help center, status page).
  * Lock the Q1 Design System definition (tokens/theme vs. component rewrite).
  * Set concrete targets for Track B (e.g., invoicing p95 latency, accounting sync error rate, specific reports).
* **Weeks 3–8: Parallel Build (and Early Track B Releases)**
  * Track A builds marketing site, staging domain, and token-based re-skin behind feature flags.
  * **Ship Track B fixes continuously**—do not hold invoicing/accounting fixes for the Week 11 rebrand. Customers at +4 NPS need relief in January/February, not April.
* **Weeks 9–11: Cutover Rehearsal & Launch**
  * **Email warm-up:** Start warming up the new sending domain weeks before cutover, or your rebranded invoices and password resets will land in spam.
  * Test SSO/SAML, OAuth callbacks, and 301 redirects end-to-end.
  * Internal dogfooding and canary rollout in Week 10; full cutover in Week 11.
* **Weeks 12–13: Hypercare & Q2 Handoff**
  * Dedicated bug-bash for broken links, integration webhooks, and customer support escalations.
  * Publish Q2 roadmap focused on post-merger product consolidation and the rest of the NPS recovery plan.

---

### 5. Keep Your P&E Leaders Aligned
Your managers and senior engineers already know +4 NPS is a five-alarm fire. If you just relay the CEO’s mandate blindly, you’ll lose credibility; if you vent about leadership, you’ll create cynicism.

Tell them plainly:
> *"Leadership made the call to unify the brand in Q1—that clarity lets us stop debating and move fast. My job is to make sure we hit that date without throwing away our customers. So we’re scoping the design system to tokens for Q1, and keeping a dedicated track on invoicing, accounting, and key reports so the new brand lands on a product people actually want to use."*
