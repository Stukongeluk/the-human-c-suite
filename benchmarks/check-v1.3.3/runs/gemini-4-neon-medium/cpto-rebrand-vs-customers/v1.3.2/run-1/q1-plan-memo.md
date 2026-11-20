# Q1 Product & Engineering Plan: Rebrand and Customer Retention

**Prepared for:** CEO  
**Prepared by:** Head of Product (with Engineering, Customer Success, and Finance inputs)  
**Decision needed:** Approve the Q1 capacity split between the post-merger rebrand and the top three customer-retention fixes.

---

## Recommendation

**Adopt Option B (Split Q1):** deliver a visible, customer-ready rebrand in Q1—new name in the app, new domain, and a new marketing site led by Marketing/agency—while dedicating the remaining roadmap capacity to fixing slow invoicing, the broken accounting integration, and missing reports. Phase the full design-system rebuild across Q2–Q3 as teams touch each product area.

This delivers one brand to the market in Q1 without leaving our highest-risk customer problems unresolved for another quarter after a 24-point drop in NPS (from +28 to +4).

---

## Why This Trade-Off Matters Now

A unified post-merger brand is important for sales momentum, market clarity, and board confidence. At the same time, customer health has deteriorated sharply:

| Signal | Current state | Source to confirm |
|---|---|---|
| Net Promoter Score (NPS) | Fell from **+28 to +4** (−24 points) | Customer survey / CS tool |
| Top open complaints | Slow invoicing, broken accounting integration, missing reports (open for months) | Support / Jira |
| Renewals at risk in Q1–Q2 | `[Insert $ ARR and % of Q1–Q2 renewals]` | CRM / Billing |
| Support load from top 3 issues | `[Insert % of monthly tickets / CS hours]` | Support platform |
| Churned accounts citing these issues | `[Insert count and $ ARR over last 2 quarters]` | CRM churn reasons |

Launching a new brand while core billing and accounting workflows remain broken risks accelerating Q1–Q2 churn and turning the rebrand into a negative customer moment.

---

## Real Q1 Capacity

Before committing to dates, Engineering and Product should size net roadmap capacity from actual availability rather than headline headcount:

| Capacity bucket | Share of total engineering time (illustrative baseline) | Notes |
|---|---|---|
| Planned leave, holidays, onboarding | 15% | Fixed from HR/team calendars |
| Unplanned work, incidents, on-call, support | 20% | Based on last 2 quarters' actuals |
| Reliability, security, and core tech debt | 15% | Prevents incident spikes during domain/app cutover |
| **Net roadmap capacity available for Q1** | **50%** | **100% of roadmap commitments fit inside this bucket** |
| **Total** | **100%** | **No overtime assumed** |

*(Replace illustrative shares with last quarter's actuals from Jira, incident logs, and team calendars before finalising dates.)*

---

## Q1 Options Compared

All percentages below are shares of **Net roadmap capacity (100%)**.

| Dimension | Option A: Full Rebrand | Option B: Split Q1 *(Recommended)* | Option C: Customer Fixes First |
|---|---|---|---|
| **Roadmap split** | 100% Rebrand / 0% Customer fixes | 40% Rebrand / 60% Customer fixes | 15% Rebrand prep / 85% Customer fixes |
| **What ships in Q1** | New app name, new domain, new marketing site, full design-system rebuild | New app name, new domain, new marketing site (Marketing/agency-led); fixes for slow invoicing, accounting integration, and priority missing reports | All 3 customer fixes + reliability hardening; rebrand launches in Q2 |
| **What moves to Q2–Q3** | All 3 customer fixes | Full design-system rebuild (rolled out incrementally) | New app name, domain, and marketing site |
| **Market & sales impact** | Strongest visual launch | Achieves unified brand in-market on Q1 timeline | Delays unified brand by one quarter |
| **Retention & revenue risk** | **High** — core workflows stay broken for 6+ months total; high risk to Q1–Q2 renewals | **Managed** — stops the bleeding on top churn drivers while landing the new brand | **Low** on retention; **medium** on post-merger sales narrative |
| **Delivery & quality risk** | **High** — full design-system rewrite in one quarter risks UI regressions and slips | **Low–Medium** — smaller cutover surface; product engineers stay off marketing site work | **Low** |
| **Reversibility** | Low once teams commit and renewals pass | High — design-system pace can accelerate in Q2 once retention stabilises | Medium — rebrand date slips visibly |

---

## Execution Guardrails (Option B)

1. **Keep product engineers off the marketing site.** Marketing and an external agency/CMS own the marketing site; Engineering provides domain/DNS, redirects, and tracking hooks only.
2. **Scope the Q1 rebrand to what customers and prospects see first:** app name, logo, domain cutover, email templates, and billing/invoice branding.
3. **Commit only to team-estimated dates.** Engineering leads size the three customer fixes and the domain/app cutover before external dates are announced.
4. **No hidden trade-offs.** If Option A is chosen instead, we explicitly accept and budget for the Q1–Q2 renewal and support risk rather than asking teams to absorb both through overtime.

---

## Metrics and Week-6 Checkpoint

Review at **Q1 Week 6** with Product, Engineering, CS, Sales, and Finance:

- **Customer outcomes:** NPS trend, Q1 renewal/churn rate on affected accounts, weekly support ticket volume for invoicing, accounting integration, and reporting.
- **Delivery:** Readiness of name/domain cutover and marketing site; milestone status on the three customer fixes; production incident rate.
- **Team health:** Share of unplanned work vs. plan; sustained overtime (target: zero).

**Decision trigger:** If renewal risk or ticket volume on the top three issues rises further by Week 6, hold non-essential visual polish until those workflows are stable.

---

## Key Assumptions & What Would Change This Recommendation

- **Assumptions:** (1) There is no legal or contractual deadline requiring a full design-system rebuild—rather than name, logo, and domain—by the end of Q1. (2) Marketing can own the marketing site with agency support. (3) CRM data confirms the top three complaints materially affect Q1–Q2 renewals.
- **What would change this:** A hard legal deadline requiring full UI replacement in Q1, or CRM/churn data showing that the NPS drop is driven by something other than these three issues.
