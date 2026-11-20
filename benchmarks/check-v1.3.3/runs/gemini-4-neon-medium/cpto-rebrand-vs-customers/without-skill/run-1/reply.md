Here is the short version of your strategy: **do not fight the decision to launch the rebrand in Q1. Fight the assumption that it takes 100% of Product & Engineering to do it.**

With a CEO whose operating lines are *"leadership decides, teams execute"* and *"any decision beats no decision,"* walking in to argue that you should delay the rebrand because NPS fell to +4 will get you labeled as someone relitigating a closed decision. You will lose that argument, and you will lose political capital you need for Q2.

Instead, match their energy: come back with a **decisive Q1 execution plan** that delivers the rebrand on time *and* neutralizes the churn bomb sitting underneath it.

---

### 1. Build Your Case on Two Things This CEO Cares About (Not NPS)

Before you walk into the CEO's office, spend 3–4 days doing quiet prep with **VP Engineering** and **VP CS / CRO**:

1. **Translate NPS (+28 → +4) into ARR at risk.** Pull the exact list of accounts with open escalations on slow invoicing, the broken accounting integration, and missing reports. Tally total ARR and specifically **Q1/Q2 renewals at risk**. A CEO who brushes off NPS will still pay attention to *"$X.XM in Q1/Q2 renewals is directly tied to these three bugs."*
2. **Use engineering physics, not emotion.** At a 400-person company, putting 100% of Product & Engineering on a rebrand doesn't make it faster—it makes it slower (merge conflicts, coordination overhead, QA bottlenecks). You aren't asking to "deprioritize the rebrand"; you are showing how to **right-size the rebrand team so it actually ships cleanly in 12 weeks.**

---

### 2. Right-Size the 4 Rebrand Workstreams (~55% of P&E)

Break the rebrand into its four parts so leadership can see why it doesn't need the whole org:

* **New marketing site → Outsource it.** Marketing + a web agency/contractors should own this. Core product engineers should spend near-zero time here—just DNS handoff, login/signup links, and tracking verification.
* **New domain → Dedicated Platform/Infra pod (start Week 1).** This is the highest-risk technical piece of a SaaS rebrand. DNS, SSL, SSO/SAML callbacks, OAuth redirect URIs, webhooks, API base URLs, and email deliverability (SPF/DKIM/DMARC warming on the new domain) will silently break customer workflows if rushed. Keep redirects running for 6–12 months. Throwing feature squads at this does not help.
* **New name in the app → Centralized sweep.** Logo, copy, favicons, transactional emails, billing receipts, and invoice PDFs. Put a small tiger team on centralizing brand strings/assets rather than having every squad hunt them ad hoc.
* **New design system → Phase it (this is the biggest trap).** Rebuilding every screen across two merged products in 12 weeks is how you ship a buggy, late Q1. Scope **Q1 = Theme/Token Layer + Unified Navigation Shell + Top ~20% Highest-Traffic Screens**. Customers see a cohesive new brand on Day 1; squads migrate legacy components progressively in Q2+ as they touch those surfaces.

---

### 3. Use the Freed-Up Capacity (~35%) to Bundle "The Big 3" Into the Launch

Here is the commercial argument that turns this into a win for the CEO:

> **Launching a cosmetic rebrand and a disruptive domain cutover on top of broken invoicing and accounting will trigger customer backlash** (*"You spent three months on a logo while my accounting sync is still broken"*). **Fixing them alongside the rebrand turns a high-risk migration into an actual product upgrade.**

Even better, two of the three fixes naturally overlap with rebrand work:
* **Broken accounting integration:** Domain migration already requires updating OAuth callbacks, webhooks, and endpoints. Dedicate an integrations squad to stabilize it *once* during the domain work instead of breaking it further.
* **Slow invoicing:** You already have to touch invoice templates/PDFs and billing UI for the new brand. Have a squad fix the underlying query/generation latency in the same pass.
* **Missing reports:** Apply the 80/20 rule. Don't build a reporting engine in Q1—ship the **top 3–5 specific reports** driving 80% of CS escalations and renewal blockers (or a clean data export unblock).

Hold the remaining **~10%** for KTLO, Sev-1s, and cutover hypercare.

**Bonus tactic:** Roll out the accounting fix and faster invoicing to a beta cohort of your loudest NPS detractors in **Weeks 6–7**. You start arresting churn *before* the rebrand even launches, and you enter launch week with proof points.

---

### 4. How to Pitch It to the CEO

Bring a **1-page decision memo**, not a slide deck debate:
* Open by affirming the decision: *"We are 100% locked in on launching [NewBrand] in Q1."*
* Show the capacity math (55% Rebrand / 35% Launch-Ready Fixes / 10% Buffer) and why 55% delivers a *cleaner, lower-risk* rebrand than 100%.
* Show the launch narrative upgrade:
  * **Without fixes:** *"New name, new URL, new colors—please update your bookmarks and SSO."*
  * **With fixes:** *"Welcome to [NewBrand]—a new look, plus faster invoicing, a rock-solid accounting sync, and the reports you've been asking for."*
* Ask for a clear yes/no on the **55 / 35 / 10** split today.

---

### 5. What If the CEO Still Says "No—100% on the Rebrand"?

Plan for this possibility upfront so you don't get caught flat-footed:

1. **Accept cleanly, document the risk in writing.** Send a calm, non-defensive follow-up: *"Understood—we're executing 100% on the rebrand for Q1 and pausing invoicing, accounting, and reporting fixes until April 1. Flagging for Finance and CS that $X.XM in Q1/Q2 renewals is currently tied to those open issues so we can align on customer messaging."* This isn't CYA for politics; it ensures the company isn't blindsided in Q2.
2. **Protect a 10% Sev-1/KTLO floor** so production doesn't melt during the domain cutover, and make doubly sure the domain migration doesn't break the accounting integration *worse*.
3. **Pre-scope the Big 3 in late Q1** (discovery, specs, technical spikes) so teams pivot cleanly on April 1 without losing another month.
4. **Watch morale—and take note for yourself.** Post-merger P&E teams are already bruised. Telling good engineers to ignore glaring customer pain for a full quarter to reskin CSS will cost you top talent. Be transparent with your leads about the constraint, protect them from scope creep on the design system, and privately weigh what it means if leadership consistently treats a 24-point NPS collapse as irrelevant.

---

I also wrote a companion working document you can adapt directly—it contains the full 12-week Q1 operating plan and a fill-in-the-blank 1-page CEO alignment memo: [q1-plan-and-ceo-memo.md](file:///G:/agy-bench/ws/efba8cf85237/q1-plan-and-ceo-memo.md).
