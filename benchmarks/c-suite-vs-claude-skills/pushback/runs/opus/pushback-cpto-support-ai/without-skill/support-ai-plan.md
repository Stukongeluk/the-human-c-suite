# AI-first customer support: plan to 30 June 2027

Draft v0.4, 23 November 2026. For the CPTO. To review with the CEO, CFO, the owner of support, HR and Dutch employment counsel.

**Changes in v0.4:** Appendix A adds a week-by-week timeline.

**Changes in v0.3:**
- The support team isn't told until the vendor contract is signed. They hear on signing day, before the customer notices go out, together with a retention offer.
- The works council (OR) is briefed in confidence before signing (art. 20 WOR), and the vendor contract is made conditional on the OR process. Whether to brief the OR before signing is still open for the CPTO to decide.
- The replay test is graded by the support lead and team leads instead of senior agents.

**Changes in v0.2:** there is no separate pilot phase any more. The vendor is chosen on a two-week replay test of your own tickets, then traffic is ramped from 10% to 100% over four weeks, with a stop rule at each step. The AI reaches full volume on chat and email by mid-February 2027, about four months earlier than in v0.1.

---

## 1. Summary

**Q2 2027 goal.** By 30 June 2027 an AI agent is the first line of support on every channel. It resolves most routine conversations from start to finish, with customer satisfaction at least as good as today. The support team has been reshaped around complex work, key accounts and running the AI. Interim milestone: the AI handles full volume on chat and email for routine questions by mid-February 2027.

**What this plan does not do** is commit today to removing all 25 support roles. Team size is decided on production data, and there are two ways to time that decision:
- **Recommended:** decide at Gate 2 (end of April 2027). The formal works council (OR) request goes in early March, by which point there are 3 or more weeks of data at full volume.
- **For exits by 30 June:** decide by early February, with about three weeks of data from the ramp. Section 7 covers what that option takes and what it puts at risk.

**Why it's gated:**
- The AI will take the routine work, not all of it. The work it leaves behind is the longest and the most sensitive for revenue.
- Dutch process (works council, collective dismissal rules, UWV or settlement agreements, notice periods) means that reaching zero by 30 June would require committing by early February, with only a few weeks of partial-volume data.
- The current team is both the source of the knowledge the AI needs and the fallback if it underperforms.

**Baseline to complete in Phase 0:**

| Metric | Today |
|---|---|
| Inbound conversations per month, by channel (chat, email, phone, portal) | _tbd_ |
| Share of tickets and of handle time by category (see 4.0a) | _tbd_ |
| CSAT, overall and by customer tier | _tbd_ |
| Median first response time and time to resolution | _tbd_ |
| Recontact or reopen rate | _tbd_ |
| Escalations to engineering per week | _tbd_ |
| Fully loaded team cost per year, and cost per resolved contact | _tbd_ |
| Support attrition, last 12 months | _tbd_ |

---

## 2. Principles

1. **Measure resolved problems and retained revenue,** not deflected tickets or headcount.
2. **Prove first, then reduce.** Human capacity comes down only after the AI has held its metrics at full volume for 4–6 weeks.
3. **Buy the agent, build the integrations.** Use a mature AI agent platform and spend engineering time on the account actions and data access only you can build.
4. **We own every answer.** Answers come only from approved knowledge, with hard rules for escalation, and are audited every week. (In 2024 a Canadian tribunal held Air Canada liable for wrong information its chatbot gave a customer.)
5. **Do the people side properly and early.** Communicate honestly, involve the works council (OR) from the start, and use attrition, redeployment and voluntary arrangements before any forced redundancy.

---

## 3. Success metrics and guardrails

| Metric | Definition | Proposed Q2 target |
|---|---|---|
| Verified AI resolution rate | Closed with no human touch **and** no recontact on the same issue within 7 days | ≥ 50% of inbound conversations (reset at Gate 1 using ramp data) |
| CSAT on AI-resolved conversations | Same survey as for human-handled ones | ≥ human baseline for the same categories |
| Overall CSAT | All conversations | Guardrail: never more than 2 points below baseline over a 2-week window |
| Time to resolution | Median, all conversations | Better than baseline |
| Handoff quality | Share of escalations where the human didn't have to ask the customer again for information | ≥ 90% |
| Critical errors | Wrong information on pricing, contracts, security, personal data or legal matters in the audited sample | Zero tolerance: any occurrence triggers a review of that category |
| Key accounts | CSAT and escalations for the top customer tier | No deterioration; a human route always available |
| Revenue | Gross revenue churn and NRR by cohort | No deterioration attributable to support |
| Engineering interrupts | Support escalations to engineering per week | Not above baseline |

**Rollback rule:** if a guardrail is breached two weeks running, pause expansion, restore human capacity in the affected category, fix the cause, then resume.

---

## 4. Phases

| Phase | Dates | Outcome | Gate |
|---|---|---|---|
| 0. Baseline and groundwork | 24 Nov – 18 Dec 2026 | Know where the work is; legal, contract and people tracks started | Business case v1 to CEO/CFO (early January) |
| 1. Select and ramp | 1 Dec 2026 – 12 Feb 2027 | Vendor chosen on your own tickets by 18 Dec; live from week of 18 Jan; 100% of chat and email by mid-February | **Gate 1** (mid-February): full volume reached and metrics holding |
| 2. Scale | 15 Feb – 30 Apr 2027 | Account actions and remaining channels added; new team designed; formal OR advice requested | **Gate 2** (end of April): decide team size |
| 3. Transition | 1 May – 30 Jun 2027 | AI is the front door everywhere; new team shape in place | End-of-Q2 review (30 June) |

**The pilot isn't what sets the go-live date.** Three things do:
- the vendor's security review and DPA;
- customer subprocessor notices (often 30 days under your DPAs);
- the first integrations.

The replay test fits inside that wait, and the ramp is simply how traffic gets switched on.

### 4.0 Phase 0: Baseline and groundwork (24 Nov – 18 Dec 2026)

This runs in parallel with vendor selection. The holiday period starts right after, so everything is front-loaded into December.

**a) Ticket analysis** (data team with the support lead). Take 12 months of tickets and break them down by category, channel, language, customer tier, handle time, reopens, CSAT and escalation to engineering. Put every category into one of four buckets:

| Bucket | Examples | Q2 scope |
|---|---|---|
| A. Answerable from documentation | How-to questions, "where is X", plan and feature questions | AI resolves |
| B. Simple account action via API | Password/2FA resets, invoice copies, user management, status checks | AI resolves, behind strict authentication |
| C. Investigation or judgement | Bugs, configuration, integrations, data issues | Human-led, AI-assisted |
| D. Relationship or commercial | Billing disputes, cancellations, complaints, enterprise escalations | Human |

The key output is the share of **handle time** in each bucket, not just the share of tickets. That figure drives the sizing model in section 5.

**b) Knowledge audit.** Check whether the answers for bucket A are written down, current and correct. The support team knows where the gaps are, so they fix them, and that work is part of the project rather than extra work on top.

**c) Contracts and compliance** (legal, DPO, security):
- Customer SLAs: response times, named support, phone support, and any commitment to human support.
- DPAs: subprocessor clauses (notice period, right to object) and customer-specific restrictions on AI or data processing.
- A DPIA for the AI agent, plus the vendor DPA, data residency and retention.
- AI disclosure: customers must be told clearly that they're talking to an AI. The EU AI Act's transparency rules (Article 50) require this for AI systems that interact with people.

**d) Stakeholders.** CEO, CFO, the owner of support (if that's not you, they co-own this plan), HR, Dutch employment counsel, CISO/DPO and customer success leadership.

**e) Works council (before signing, in confidence).** Brief the OR chair or daily board before the vendor contract is signed, and impose confidentiality under art. 20 WOR. Present it as a proposed decision: direction, vendor selection, timeline, and how and when the formal advice request will follow.
- **Why before signing:** introducing a significant technology and reorganising support both fall under the advice right in art. 25 WOR. The advice must be requested while it can still materially influence the decision. If the OR's first sight is a signed contract, they have strong grounds to say they were consulted too late, and the Enterprise Chamber can order the decision to be withdrawn and its consequences undone.
- **Contract protection:** make the vendor contract conditional on the OR process, or give it a break clause, so that signing doesn't lock in the outcome.
- **Monitoring:** if the AI tooling will also monitor agents' performance, art. 27 (consent right) may apply as well.
- **Counsel:** ask employment counsel to confirm which steps need formal advice.

**f) Support team (on signing day).** The team isn't told before the vendor contract is signed, apart from the support lead and team leads, who work under confidentiality.
- **Signing day, about 18 December**, in this order:
  1. Sign the conditional contract.
  2. Hold the team meeting, with the retention offer ready.
  3. Send the customer subprocessor notices.
- **Why notices go last:** the team must not learn about it from a customer.
- **In the meeting**, tell the team honestly what's happening, what has and hasn't been decided, how decisions will be made and what support they'll get. Ask the team to help with the ramp and with tuning the AI, and recognise that work.
- **Holding statement:** have one ready in case the news gets out before signing day.
- **Backfills:** stop backfilling leavers from now on, using temporary cover if needed.

**f2) Retention.** Before signing day, identify the people you can't lose through mid-February, and ideally through Q2. They are likely the senior agents, tier-2 specialists and the people who know the knowledge base best.
- **Bonus:** offer them a retention bonus paid on a fixed date (for example 30 June). It is paid even if their role is later made redundant; otherwise nobody will believe it.
- **Terms:** set out redeployment chances and exit terms from day one.
- **Everyone else:** other voluntary departures don't threaten the plan, because there is no backfilling anyway.

**g) Vendor shortlist.** Pick two vendors. Start with the native AI agent of your current helpdesk (for example Intercom Fin, Zendesk AI agents, Salesforce Agentforce or Freshworks Freddy) and add one specialist (for example Decagon, Sierra or Ada). Write the replay-test protocol this week (see Phase 1).

**Deliverable:** a baseline report and business case v1 (section 6) for the CEO and CFO by early January.

### 4.1 Phase 1: Select and ramp (1 Dec 2026 – 12 Feb 2027)

There is no separate pilot. Verification happens inside the selection work and the rollout, so it adds no time to the calendar.

**1–18 December: replay test, security and paperwork, all in parallel.**
- Give each of the two vendors about 500 anonymised historical conversations from bucket A, in Dutch and English, and keep back a held-out set they haven't seen.
- The support lead and team leads grade the answers blind, under confidentiality, for correctness, completeness, tone and whether escalation was handled correctly. Senior agents can join after signing, to grade the ramp samples. Weight confident wrong answers heavily; an average score hides them.
- Run the security review and DPA at the same time.
- Choose the vendor and sign a contract conditional on the OR process by 18 December, after the confidential OR briefing. On signing day, tell the team first and send the subprocessor notices to customers straight after (see 4.0f). Those notices, not the test, decide the earliest live date.

**Early January: configuration.** Load the knowledge base and set up handoff routing. The AI must tell customers clearly that they're talking to an AI, and customers need a one-click route to a human.

**Ramp, one step a week:**

| Week of | Live traffic |
|---|---|
| 18 Jan | 10% of chat, bucket A |
| 25 Jan | 30% of chat |
| 1 Feb | 60% of chat, plus email |
| 8 Feb | 100% of chat and email for bucket A |

The top customer tier joins at the last step, or earlier only if they opt in.

**Stop rule at each step.** Move to the next step only if all of these hold for the previous week:
- No unresolved critical errors (wrong answers on pricing, contracts, security or personal data) in the reviewed sample of about 100 conversations.
- CSAT on AI conversations isn't clearly below the human baseline for the same categories.
- Handoffs to humans work without customers having to repeat themselves.

If a step fails, hold for a week, fix the cause and try again. The project carries on.

**Account actions (bucket B) come after the ramp,** in Phase 2, and only once a security red-team has passed: prompt injection, attempts to reach other customers' data, and social engineering of resets. Use strict authentication, least-privilege API access and per-customer data scoping. Irreversible or financial actions (refunds, plan changes) need human approval throughout Q2.

**Gate 1 (mid-February)**, attended by the CEO, CFO and the owner of support:
- Is full volume reached on chat and email for bucket A?
- What are the verified resolution rate, CSAT and critical-error record at full volume?

The first data-based sizing scenario also comes out of Gate 1.

### 4.2 Phase 2: Scale (15 Feb – 30 Apr 2027)

- Add bucket B account actions once the red-team has passed, then add the remaining channels (portal, and phone if relevant). Cover off-hours, and support Dutch and English (plus other languages your customers use).
- Give humans an AI copilot for buckets C and D: conversation summaries, draft replies and suggested knowledge.
- **Design the organisation** (owner of support, HR and counsel). A draft target shape:
  - **AI operations** (2–3 people): knowledge management, conversation review and QA, tuning, reporting.
  - **Tier-2 product specialists:** bugs, configuration and integrations, working in a tight loop with engineering.
  - **Key-account support:** named support for the top tier.
  - **Team lead.**
- **Map redeployment options** across the company: customer success, onboarding and implementation, QA and testing, technical writing, solutions engineering, sales development. Support people bring deep product and customer knowledge to all of these.
- **Formal OR advice request** (target early March, by which point there are 3 or more weeks of full-volume data), based on that data and the sizing scenarios. If you take the 30 June exit option in section 7, the request goes in in early February instead. Plan for several weeks before the OR advises. They may bring in an expert, at the company's cost.
- Check for an existing social plan or CAO, and prepare terms with HR.

**Gate 2 (end of April):** decide the target team size using about ten weeks of full-volume data, and approve the reorganisation once the OR has given its advice.

**Legal point that shapes the design:** in a partial reduction, Dutch law selects who leaves within interchangeable roles using the reflection principle (afspiegelingsbeginsel). That means by age group and length of service, not by performance. Whether the new roles (AI operations, tier-2, key accounts) count as interchangeable with today's roles determines who can be placed where. Settle this with counsel before anyone assumes who stays.

### 4.3 Phase 3: Transition (1 May – 30 Jun 2027)

- The AI agent is the front door on all channels by 1 May at the latest. Humans own buckets C and D and the key accounts.
- Implement the new team, in this order:
  1. Placements into the new roles.
  2. Redeployment, with training.
  3. Voluntary arrangements.
  4. Only then, any forced redundancy, through the proper procedure.
- Keep a capacity buffer until the guardrails have held for 4–6 weeks at full volume.
- **30 June: end-of-Q2 review** of metrics against targets, followed by the H2 plan (automating parts of bucket C, and voice if relevant).

**On dates:** if departures are needed beyond attrition and voluntary arrangements, the last working days will typically fall in Q3, because of the OR advice, any UWV procedure and notice periods. That's expected. The Q2 milestone is the AI and the new team shape, not the last day of the last person.

---

## 5. Team sizing model

```
Remaining queue FTE = current FTE × (1 − r × h) × (1 − p) × (1 + g)
Total team          = remaining queue FTE + AI operations (2–3 FTE)
```

- **r**: verified AI resolution rate.
- **h**: handle time of AI-resolved conversations relative to the average. This is usually well below 1, because the AI takes the short conversations.
- **p**: productivity gain for humans from AI assistance on the remaining work.
- **g**: growth in volume over the planning period.

**Illustrative only.** These are my assumptions, not benchmarks, with flat volume (g = 0):

| Scenario | r | h | p | Queue FTE | AI ops | Total (today: 25) |
|---|---|---|---|---|---|---|
| Cautious | 35% | 0.5 | 10% | ~19 | 2 | **~21** |
| Expected | 55% | 0.6 | 15% | ~14 | 2–3 | **~16–17** |
| Strong | 70% | 0.7 | 20% | ~10 | 3 | **~13** |

**What the model shows:**
- **The resolution rate overstates the saving.** In the expected case, 55% resolution removes about a third of the workload.
- **Growth changes the picture.** With 20% volume growth, the expected case needs about 19–20 people, where you would otherwise need about 30. That is roughly ten hires you avoid, with no dismissals.
- **Coverage-driven staffing is extra upside.** If part of today's team exists to cover hours or languages, AI coverage outside business hours can lower the number further.
- **Zero isn't a realistic Q2 outcome.** Reaching it would need r × h close to 1, meaning the AI resolves essentially everything, including bugs, disputes and enterprise escalations. Vendors' own published average resolution rates (roughly half to two-thirds of conversations in 2025, on their own definitions of "resolved") leave a large share for humans, and complex B2B products usually start below those averages.

Phase 0 data replaces h. Gate 1 and Gate 2 data replace r and p.

---

## 6. Business case structure

**Annual run-rate**

| Line | |
|---|---|
| + FTE reduced × fully loaded cost | Salary, holiday allowance, employer charges, pension, equipment, management overhead |
| + Avoided hiring from growth | Often the larger number |
| − AI platform fees | Usually per resolution or per conversation, plus platform fees. Check current pricing, volume caps and overage terms, and model 2× volume. |
| − AI operations and integration maintenance | Including engineering time |

**One-off costs**
- Implementation and integration build.
- Retention bonuses for the people needed through the transition.
- Redeployment training.
- Statutory transition payments (one-third of a monthly salary per year of service) and any settlement premiums.
- Contributions to employees' legal fees for settlement agreements (customary).
- Employment counsel, and the OR's expert if they appoint one.

**Risk sensitivity**
- **Break-even churn = net annual saving ÷ ARR.** This is the rise in gross revenue churn that would wipe out the saving. For example (illustrative), a €0.5M net saving on €40M ARR disappears with a 1.25-point rise in churn. Track churn for cohorts by how much support they use.
- Per-resolution pricing grows with volume, so the saving shrinks as you grow unless the contract caps it.

---

## 7. Option: full replacement by 30 June 2027

If you decide to go this way, this is what it takes.

**What it requires**
1. **Decide by early February**, when there are only about three weeks of ramp data at partial volume, and request OR advice at that point. Art. 25 WOR requires the request to come while the advice can still influence the decision. If you then decide against the OR's advice, there is a one-month suspension and the OR can appeal to the Enterprise Chamber (Ondernemingskamer).
2. **Notify UWV and the relevant unions** under the Collective Dismissal Notification Act (WMCO), because 20 or more contracts end within three months in one UWV region. Terminations by mutual consent count towards the 20. UWV won't process permit applications for a month after notification unless the unions declare they have been consulted. Failing to comply can make the terminations voidable.
3. **End each contract** either by UWV permit on economic grounds or by settlement agreement (vaststellingsovereenkomst). Technological change counts as an economic ground, but UWV checks the case, your redeployment efforts and your vacancies. Notice periods are 1–4 months depending on length of service; UWV processing time can be deducted, as long as at least one month remains. To hit 30 June you'd realistically need settlement agreements for most people, at a premium above the statutory transition payment.
4. **Redeployment obligation.** You must offer suitable vacancies, with training, including any AI-operations or escalation roles you create. A claim of "zero support staff" won't stand up if you're hiring people to run the AI or handle escalations.
5. **Customer contracts.** Confirm there are no commitments to human support, and renegotiate where there are.

**What it puts at risk**
- **Escalations move to CSMs and engineers,** your most expensive people, and roadmap capacity drops.
- **There's no fallback if the AI underperforms.** Hiring and training a support team again takes months. Klarna said in 2024 that its AI was doing the work of 700 agents. In 2025 its CEO said the focus on cost had lowered quality, and the company started recruiting human agents again. Commonwealth Bank of Australia reversed 45 redundancies it had attributed to an AI voice bot in 2025, after admitting it had misjudged whether the roles were still needed.
- **Knowledge walks out.** The people best able to train and correct the AI have the most options, so they leave first.
- **Customers may churn,** especially enterprise accounts.
- **Your reputation and employer brand suffer** in a tight Dutch tech labour market.
- **Legal challenges** from the OR or a WMCO process can delay the timeline.

**My view:** I wouldn't take this option. If you do, bring counsel in from day one and set up an explicit fallback, such as a support outsourcing partner contracted on standby.

---

## 8. Risks and mitigations

| Risk | Mitigation |
|---|---|
| The AI gives wrong answers on pricing, contracts, security or data, and you're liable | Answers only from approved knowledge; hard handoff for disputes, legal and security topics; weekly audits; zero-tolerance categories |
| Prompt injection or data leakage through account actions | Strong authentication; least-privilege, per-customer scoped APIs; no irreversible actions without a human; red-teaming; security review before go-live |
| CSAT or churn falls, especially for key accounts | Human route for the top tier; churn and NRR tracked by cohort; rollback rule |
| Best agents leave early and take the knowledge with them | Honest early communication; involve them in building the AI; retention bonuses; visible redeployment paths |
| OR or legal delays | Brief the OR in Phase 0; counsel in from the start; Q2 target set on the AI rather than on end dates |
| Customers object as subprocessors, or SLA conflicts | Contract review in Phase 0; send notices early; carve out customers who object |
| Engineers become de facto support | Tier-2 capacity sized explicitly; engineering interrupt load tracked as a guardrail |
| Vendor lock-in and per-resolution costs rising with volume | Data export rights, price caps and volume tiers in the contract; integrations kept on your side |
| Hype-driven targets (deflection counted as resolution) | Verified resolution with a 7-day no-recontact check; independent grading |

---

## 9. Governance

| Role | Owner |
|---|---|
| Executive sponsor | CPTO |
| Business owner | Head of Support, or COO/CCO if support reports there |
| Programme lead | _tbd_ (full-time for Q1–Q2) |

| Workstream | Owner |
|---|---|
| AI platform and integrations | Engineering |
| Knowledge and conversation design | Support |
| Measurement | Data |
| Customers and contracts | Legal and customer success |
| People and OR | HR and employment counsel |
| Security and privacy | CISO / DPO |

**Cadence:** weekly programme review, fortnightly steering, and Gates 1 and 2 with the CEO and CFO.

---

## 10. Open decisions for the CPTO

1. **What is the primary goal?** Lower cost, absorbing growth without hiring, or faster and 24/7 service? Each one changes the headline metric.
2. **When to decide team size?** Either decide at the end of April on full-volume data (recommended), or decide by early February so that people can leave by 30 June (section 7).
3. **People principles.** For example: no forced redundancies until attrition, redeployment and voluntary routes are exhausted.
4. **Ownership.** Who owns support today, and are they co-owning this?
5. **Budget envelope for one-off costs,** including retention bonuses.
6. **Confidential OR briefing before signing?** Recommended. If not, counsel must review the contract structure before anything is signed.

## 11. Next two weeks

1. Name the programme lead and confirm the owner of support.
2. Shortlist two vendors, write the replay-test protocol and start their security reviews.
3. Pull 12 months of ticket data, and select about 500 bucket A conversations for the replay test plus a held-out set.
4. Start the contract and DPA review, and prepare the subprocessor notice so it can go out as soon as the vendor is chosen (by 18 December).
5. Engage Dutch employment counsel to map the OR track and any WMCO track. Ask them specifically to confirm the early-February versus early-March timing.
6. Brief the OR chair or daily board in confidence (art. 20 WOR) before signing, and have counsel make the vendor contract conditional on the OR process.
7. Brief the support lead and team leads under confidentiality; they grade the replay test.
8. Prepare for signing day: draw up the retention list and offer, the team announcement and a holding statement in case of a leak.
9. Stop backfilling in support.

---

## Appendix A: Week-by-week timeline (added in v0.4)

This follows the recommended path: a confidential OR briefing before signing, and the team-size decision at Gate 2 (end of April). Public holidays shown are for the Netherlands.

The first table runs to mid-February, when the AI is handling full volume on chat and email. Each traffic step from 25 January onwards goes ahead only if the previous week passed the stop rule (no critical wrong answers, CSAT holding, handoffs working). If a step fails, hold it for a week.

| Week of | What happens |
|---|---|
| **23 Nov** | Name the programme lead and confirm who owns support. Engage employment counsel. Shortlist two vendors, write the replay-test protocol and send the security questionnaires. The data team pulls 12 months of tickets. Stop backfilling support roles. |
| **30 Nov** | Replay test starts: about 500 routine historical conversations plus a held-out set go to both vendors. Brief the support lead and team leads under confidentiality; they do the grading. Start the ticket and handle-time analysis and the contract/DPA review. |
| **7 Dec** | Grade the replay test. Run the security review and negotiate the DPA. **Brief the OR chair or daily board in confidence (art. 20 WOR).** Counsel drafts the clause that makes the vendor contract conditional on the OR process. HR drafts the retention list and offer. |
| **14 Dec** | **Vendor decision.** **Signing day (Thu 17 or Fri 18 Dec):** sign the conditional contract, hold the team meeting with the retention offer, then send the customer subprocessor notices. The 30-day notice period sets the go-live date. |
| **21 Dec** | Christmas week. Vendor onboarding starts and the knowledge base is imported. HR is available for one-to-ones. Prepare answers to customer questions about the notice. |
| **28 Dec** | Holiday week, skeleton crew only. |
| **4 Jan** | Configure the agent: knowledge gaps fixed by the support team, handoff routing, AI disclosure, CSAT survey. Retention agreements signed. Baseline report and business case v1 go to the CEO and CFO. |
| **11 Jan** | Internal dry run: the team tests the agent and fixes its answers. Set up dashboards and the weekly review sample of about 100 conversations. Plan the security red-team for account actions. |
| **18 Jan** | **Go live on 10% of chat**, routine questions only. The notice period ends around 17 January. |
| **25 Jan** | 30% of chat. First weekly review. |
| **1 Feb** | 60% of chat, plus email. |
| **8 Feb** | **100% of chat and email** for routine questions, top customer tier included. The red-team on account actions starts. |

From mid-February the work moves to account actions, the other channels, the new team design and the formal OR advice.

| Week of | What happens |
|---|---|
| **15 Feb** | **Gate 1** (CEO, CFO, support owner): review the full-volume metrics and the first sizing scenario. The AI copilot goes live for humans on complex tickets. |
| **22 Feb** | First account actions live at a small share of traffic, once the red-team has passed. The support owner, HR and counsel start the organisation design. |
| **1 Mar** | **Formal OR advice request**, with 3+ weeks of full-volume data and the sizing scenarios. **Collective dismissal notification** to UWV and the unions if 20 or more departures are possible. Ramp up account actions. |
| **8 Mar** | The OR deliberates and may bring in an expert. Map redeployment options across the company. Prepare the remaining channels (portal, and phone if relevant). |
| **15 Mar** | The OR process continues. HR prepares the terms (social plan, or check the CAO). The remaining channels go live at 10%. |
| **22 Mar** | The OR process continues. Ramp up the remaining channels. |
| **29 Mar** | Easter Monday falls this week. Account actions at full scope. The collective dismissal waiting period ends around 1 April. |
| **5 Apr** | The OR process continues. |
| **12 Apr** | **OR advice expected.** Allow 4–6 weeks from the request; it could slip a week or two. |
| **19 Apr** | Finalise the organisation design with the OR's advice incorporated. **All channels at 100%.** |
| **26 Apr** | **Gate 2: decide team size and the reorganisation.** (King's Day is on 27 April.) If the decision deviates from the OR's advice, implementation has to wait one month. |

May and June are for putting the new team in place and checking that the setup holds.

| Week of | What happens |
|---|---|
| **3 May** | Announce the decision to the team and hold individual conversations. Place people into the new roles and open the redeployment roles. Ascension Day is on 6 May. |
| **10 May** | Window for voluntary arrangements and settlement agreements opens. More individual meetings. |
| **17 May** | Whit Monday falls this week. Voluntary window continues. Prepare UWV applications for any remaining forced redundancies. |
| **24 May** | Voluntary window closes. File the UWV applications, if any are needed. |
| **31 May** | **New team shape live:** AI operations, tier-2 specialists, key-account support. Keep a capacity buffer. |
| **7 Jun** | Stability check: guardrails at full volume on all channels. |
| **14 Jun** | Stability check continues. Start drafting the H2 plan (automating complex tickets, voice). |
| **21 Jun** | Prepare the end-of-Q2 review. |
| **28 Jun** | **30 June: end-of-Q2 review.** Settlement exits end on this date where they have been agreed. Exits through UWV and longer notice periods run into Q3. |

**30 June exit option (instead of the March track above):**
- **Week of 1 Feb:** OR advice request and collective dismissal notification, based on about three weeks of ramp data.
- **Mid-March:** OR advice.
- **Week of 22 Mar:** decision.
- **April:** announcement and voluntary window. Most people would need settlement agreements, signed by the end of April and ending on 30 June.
- **After that:** anyone going through UWV, or with a long notice period, still leaves in Q3.

The two dates that drive everything are the customer notice period (which sets go-live) and the OR advice (which sets the team decision). Have counsel confirm the legal dates before 7 December.

---

_Note: I couldn't run live checks while drafting this. The legal points (WOR, WMCO, dismissal law, the EU AI Act), vendor references and the examples come from my own knowledge and haven't been verified for this document. Have Dutch employment counsel confirm the legal track before anything goes to the OR or the team, and check vendors' current pricing and capabilities directly._
