# Q1 Plan & CEO Alignment Memo: Rebrand Launch + Retention Defense

> **How to use this document:** Part 1 is the internal Q1 operating plan (capacity, workstreams, milestones). Part 2 is a 1-page executive memo template you can adapt and put in front of your CEO before the Q1 kickoff.

---

## Part 1: Q1 Operating Plan

### 1. Core Thesis
Do **not** fight the rebrand decision. Instead, **right-size the rebrand's engineering footprint** so it actually ships on time, and use the freed-up capacity to fix the three customer pain points that would otherwise turn the Q1 rebrand launch into a churn event.

### 2. Capacity Allocation (Recommended: 55 / 35 / 10)

| Track | % of P&E | Who Owns It | Scope & Done Criteria |
| :--- | :---: | :--- | :--- |
| **Track A: Rebrand Launch** | **55%** | Platform/Infra, Design Systems, Brand Tiger Team + small slice of feature squads | New domain live (with redirects & SSO/webhook continuity), new brand name/assets across app/emails/PDFs, token-based visual refresh (Phase 1 design system). Marketing site outsourced to agency + Marketing. |
| **Track B: Retention Defense ("The Big 3")** | **35%** | 2–3 dedicated product/backend squads | (1) Accounting integration rebuilt/stabilized, (2) Invoicing latency cut to target SLA, (3) Top 3–5 missing reports shipped (or clean export unblock). |
| **Track C: KTLO & Launch Buffer** | **10%** | Rotating / on-call | Sev-1/Sev-2 incidents, security, post-cutover hypercare. |

### 3. Right-Sizing the 4 Rebrand Deliverables

1. **New Marketing Site → Outsource / Marketing-led**
   - **Trap:** Pulling product engineers onto CMS/marketing pages.
   - **Plan:** Marketing + external web agency/contractors. P&E provides only DNS handoff, signup/login CTA links, and analytics/tracking review (0.5–1 eng-week total).

2. **New Domain → Platform/Infra Pod (Highest Technical Risk)**
   - **Trap:** Treating a domain swap as a late-quarter DNS flip.
   - **Plan:** Start Week 1. Audit SSO/SAML callbacks, OAuth redirect URIs (especially for accounting & third-party integrations), webhooks, API base URLs, CORS, cookies/sessions, and email deliverability (SPF/DKIM/DMARC warming on the new domain). Keep old domain redirecting cleanly for 6–12 months.

3. **New Name in the App → Centralized Sweep**
   - **Trap:** Every squad hunting strings ad hoc.
   - **Plan:** Audit copy, logos, favicons, transactional emails, billing receipts, and invoice PDFs. Centralize brand tokens/strings so future changes are config-driven.

4. **New Design System → Phased (Theme First, Components Second)**
   - **Trap:** Rewriting every screen across two merged codebases in 12 weeks.
   - **Plan:**
     - **Q1 (Launch):** Design tokens (colors, typography, spacing, logo), unified top-level navigation/shell, and component refresh on the top ~20% highest-traffic screens.
     - **Q2+:** Progressive component migration as squads touch surfaces for roadmap work.

### 4. Bundling "The Big 3" Into the Rebrand

| Customer Issue | Natural Tie-In to Rebrand | Pragmatic Q1 Target |
| :--- | :--- | :--- |
| **Broken accounting integration** | Domain migration already requires OAuth/webhook/endpoint updates—touching it once avoids double disruption. | Zero silent sync failures; clear error states/retry UI; top 2 accounting connectors rock-solid. |
| **Slow invoicing** | Invoice PDFs and billing UI must be rebranded anyway; fix the query/generation bottleneck in the same pass. | Reduce p95 invoice creation/load time by 70%+ (or <2s target). |
| **Missing reports** | Launch narrative: *"New brand, plus the reporting you've been asking for."* | Ship the top 3–5 reports driving 80% of CS escalations and renewal blockers (defer custom report builder to Q2/Q3). |

### 5. 12-Week Execution Cadence

- **Weeks 1–2 (Lock & De-risk):**
  - Finalize Q1 scope & squad assignments.
  - Complete domain/auth/webhook RFC and begin new-domain email warming.
  - Lock Phase 1 design tokens and app-shell spec.
  - Kick off marketing site agency.
  - Confirm root causes and acceptance criteria for invoicing, accounting, and top reports.
- **Weeks 3–8 (Parallel Build):**
  - Rebrand pods execute domain prep, token theming, and brand string sweep.
  - Retention pods execute Big 3 fixes.
  - **Week 6–7 Early Win:** Roll out accounting integration fix and faster invoicing to a beta cohort of vocal NPS detractors to stop bleeding *before* launch.
- **Weeks 9–10 (Hardening & Enablement):**
  - Staging domain cutover dry runs (SSO, webhooks, API redirects, billing).
  - Full regression & performance verification.
  - Arm CS and Sales with launch messaging: *"Welcome to [NewBrand] — a new look, plus faster invoicing, reliable accounting sync, and new reporting."*
- **Weeks 11–12 (Launch & Hypercare):**
  - Staged rollout of rebrand + Big 3.
  - Monitor error rates, accounting sync health, invoice latency, and support ticket volume daily.
  - Lock Q2 roadmap (Design System Phase 2 + post-merger consolidation).

---

## Part 2: 1-Page CEO Alignment Memo (Template)

**To:** [CEO Name]  
**From:** [Your Name], Head of Product  
**Subject:** Q1 Execution Plan: Delivering the [NewBrand] Launch Without Triggering a Churn Wave

### Bottom Line
We are fully committed to launching **[NewBrand]** in Q1—new name in-app, refreshed visual system, new domain, and new marketing site. 

After scoping the work with Engineering, **putting 100% of Product & Engineering on the rebrand will not make it ship faster—and will expose $[X]M in Q1/Q2 renewals to avoidable churn.** 

Below is the execution plan that hits our Q1 rebrand deadline with high quality while neutralizing our top three churn drivers so the launch lands as a win with customers.

### Why 55% of P&E Delivers a Better Rebrand Than 100%
- **Marketing site** should be executed by Marketing + an external web agency, not core product engineers.
- **Domain migration** (DNS, SSO, OAuth, webhooks, email deliverability) is specialized Platform/Infra work; adding feature squads creates coordination risk, not speed.
- **Design system** via a token/theme layer + unified shell in Q1 gives customers a cohesive new look on launch day without a high-risk rewrite of every legacy screen.

### The Commercial Risk We Must Neutralize Before Launch
- NPS has dropped from **+28 to +4** over the past [X] months.
- **[X] accounts representing $[Y]M in ARR** (including **$[Z]M up for renewal in Q1/Q2**) have open escalations on three issues: slow invoicing, broken accounting integration, and missing reports.
- Launching a cosmetic rebrand and a disruptive domain change *without* fixing these three items creates high backlash risk (*"You spent a quarter on a logo while my accounting sync is still broken"*).

### Proposed Q1 Allocation
- **55% — Rebrand Launch:** Domain cutover, in-app name/emails/PDFs, Phase 1 design system (theme + shell + key screens).
- **35% — Launch-Ready Customer Fixes:** Fix accounting integration (bundled with domain OAuth/webhook work), fix invoicing performance (bundled with invoice rebrand), ship top [3–5] missing reports.
- **10% — KTLO & Cutover Buffer:** Production stability and launch hypercare.

### The Launch Story
Instead of asking frustrated customers to absorb a name and domain change for zero functional benefit, we launch **[NewBrand]** as a genuine upgrade: **new brand, new experience, faster invoicing, fixed accounting sync, and the reports they've been waiting on.**

### Decision Needed Today
Approve this **55 / 35 / 10** Q1 execution plan so Engineering, Product, Design, and CS can lock sprint commitments by [Date].

*(Alternative: If we allocate 100% of P&E to the rebrand, we will pause all invoicing, accounting, and reporting work until April 1. In that scenario, I recommend we explicitly align CS and Finance on the $[Z]M renewal risk and prepare detractors for a Q2 fix timeline.)*
