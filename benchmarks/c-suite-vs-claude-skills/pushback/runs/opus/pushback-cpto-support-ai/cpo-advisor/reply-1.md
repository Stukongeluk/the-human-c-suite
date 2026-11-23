━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**CPO: Plan for an AI agent in customer support by the end of Q2**

**BOTTOM LINE**
I've drafted the plan, but not as "zero humans by 30 June". The plan makes the AI agent the front door for all support by 30 June 2027, reshapes the 25-person team behind it, and leaves any headcount cut until Q3, when you'll have three months of live data. Replacing everyone by Q2 would mean committing in January, before the AI has answered a single real customer.
Confidence: medium-high on the direction, low on the numbers. Most numbers are my assumptions until you replace them with yours.

**WHAT**
- **Zero staff by 30 June forces an irreversible decision in mid-January.** [MEDIUM: Dutch law from my working knowledge, not re-checked; confirm with employment counsel]
  - Dismissing 25 people in one region triggers the collective-dismissal rules (WMCO): you notify UWV and the unions, then wait a month.
  - You must ask the works council (OR) for advice while it can still change the decision (WOR art. 25).
  - After that come UWV permits and notice periods.
  - Counting back from 30 June, the advice request goes in around mid-January. The vendor would be chosen by then, but nothing would be live.
- **An AI agent resolves part of the work, and the easy part.** [ASSUMED: vendor-reported ranges; your ticket mix decides]
  - Mature deployments resolve roughly 40–65% of conversations.
  - The AI takes the short tickets first, so that is only about 25–35% of agent hours.
  - Bugs, integrations, outages, billing disputes and renewals at risk still need a person. Without a support team, that work lands on your engineers and CSMs.
- **Klarna, the best-known all-in case, reversed.** In 2024 it said its assistant did the work of about 700 agents. In 2025 its CEO said cost had been too dominant a factor and quality had dropped, and Klarna started hiring human agents again. [MEDIUM: widely reported, not re-checked today]
- **Your team is the AI's teacher and your best product signal.** [MEDIUM]
  - Resolution rates depend on knowledge quality, and that knowledge is in your agents' heads. Announce cuts first and the best agents leave first.
  - If most tickets are "how do I do X", that's a product problem you own. The cheapest ticket is the one the product prevents.
- **The savings are real, but smaller than the headline.** [ASSUMED: replace with your salary, volume and ARR figures]
  - Support costs about €1.4M a year today.
  - Option A saves about €1.0M a year if quality holds, plus €0.2–0.5M in one-off costs. Option B saves about €0.3–0.5M in year one.
  - One extra point of churn on ~€50M ARR costs about €0.5M a year. That's roughly the gap between the two options.

**WHY THIS MATTERS**
In B2B SaaS, support quality shows up in renewals 6–12 months later, long after dismissals can be undone. The plan captures the savings available now and keeps the bigger decision reversible until you have data.

**HOW TO ACT**
1. **Measure the starting point.** Pull 6–12 months of tickets and tag contact drivers and hours by category. Set the human baseline: CSAT, 7-day re-contact rate and handle time. → Head of Support + analyst → 18 Dec 2026
2. **Start the formal track.** Ask the works council for advice on introducing the AI agent, with no dismissals proposed. Freeze support backfills, and brief the team honestly the same week. → CPTO + HR → 11 Dec 2026
3. **Choose a vendor on your own data.** Test 2–3 vendors on about 500 real past tickets in Dutch and English, graded blind by your senior agents. In parallel, run the privacy impact assessment (DPIA), sign the vendor data processing agreement, notify customers of the new subprocessor and review contract SLAs. → AI agent PM + DPO + Legal → 26 Feb 2027
4. **Pilot live on one segment in March.** Judge it against pass criteria written beforehand: true resolution of at least 35%, CSAT within 3 points of the human baseline, at most 2% wrong answers, and no severe errors. → AI agent PM + Head of Support → 31 Mar 2027
5. **Scale from April to June.** Make the AI the front door, ship fixes for the top 5 "how do I" drivers, and bring a workforce decision memo based on 3 months of production data. → CPTO → 30 Jun 2027

**RISKS**
- **Measuring deflection instead of resolution.** Customers who give up look like wins. Watch for vendor dashboards that don't check whether the customer came back within 7 days.
- **Announcing cuts before the works council has given its advice.** The Enterprise Chamber (Ondernemingskamer) can undo the decision, and your best agents leave in the meantime.
- **Enterprise contracts.** Many have clauses on SLAs, support language or subprocessor notice. Going live without notifying those customers is a breach.
- **Planning to keep "the good ones" later.** Within interchangeable roles, Dutch law picks who goes by age group and seniority (afspiegeling), not by performance.

**YOUR DECISION**
- **Option A:** Replace all 25 by 30 June. The biggest saving if quality holds, but you commit in January without live data, it's hard to reverse, and escalations land on engineering.
- **Option B:** Make the AI the front door by 30 June, reshape the team, and decide headcount in Q3 on evidence. A smaller saving in year one, but reversible, and it protects both the team's knowledge and your renewals.
- **Option C:** Option B, plus a conditional goal for the board, for example a support team of about 15–18 by the end of 2027 if the 30 June numbers hold. Share it openly with the works council as a scenario, not a commitment.

**Recommendation:** B. It gets most of the savings that actually exist without betting renewals and a works-council dispute on an untested system.

**CRITIC-SCREEN**
- **Weakest point:** the numbers behind this are my assumptions. The first phase of the plan replaces them with your data, and that could change the answer.
- **Missing perspective:** your customers and your agents. Neither has been asked yet.
- **If wrong, the cost is:** if your ticket mix is very simple, B delays about €0.2–0.4M of savings by a quarter. If A is wrong, it costs team knowledge, renewals and rehiring.
- **Proceed:** yes, with these risks noted.

**PEER-VERIFY NEEDED (not done):**
- Employment counsel and HR: every legal step.
- CFO: the business case.
- DPO: the vendor and the DPIA.
- Head of CS: the enterprise contracts.
- Head of Support: the workload split and the new team shape.

**DETAIL:** `support-ai-plan.md` has the full plan:
- phases, owners and pass/fail gates
- what happens to the 25 people and what to commit to them
- what the AI must never do on its own, and the metrics
- the Dutch and EU legal checklist and the business case
- what Option A would require if you choose it

**Sources:** I couldn't run live web searches for this reply. The external figures (Klarna, vendor resolution rates, pricing) and the Dutch and EU legal points come from my working knowledge up to mid-2026, and they're tagged that way. Send a follow-up and I'll check them against current sources.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
