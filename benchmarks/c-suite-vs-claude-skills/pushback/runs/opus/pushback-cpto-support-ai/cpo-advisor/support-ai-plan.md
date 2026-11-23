# Support AI plan: AI agent as the front door by 30 June 2027

CPO advisor · Draft 1 · 23 November 2026 · For: CPTO

**How to read the tags.** [MEDIUM] = established fact or pattern from my working knowledge (to mid-2026), not re-checked for this draft. [LOW] = from memory, less certain. [ASSUMED] = my estimate; replace it with your data. Nothing here is tagged [VERIFIED]: no live source check was possible for this draft, and none of your company data has been seen yet. More than half the numbers are assumptions, so treat the numbers as low confidence. The direction is medium-high confidence.

---

## 1. Bottom line

Make an AI agent the front door for all support by 30 June 2027 and reshape the 25-person team behind it. Take any decision to reduce headcount in Q3 2027, based on three months of production data and run through the works council.

A plan to remove all 25 people by 30 June means putting a concrete dismissal proposal to the works council in mid-January. At that point the AI will not yet have answered a single live customer. The plan would bet renewals, your team's knowledge and a works-council dispute on an untested system.

---

## 2. Assumptions (replace with your numbers)

| Item | Assumption | Tag |
|---|---|---|
| "End of Q2" | Calendar Q2 2027, ending Wednesday 30 June 2027 (31 weeks from today) | ASSUMED |
| Team shape | ~20 frontline agents (L1/L2), ~4 seniors/team leads, 1 manager | ASSUMED |
| People cost | ~€55k fully loaded per FTE, so ~€1.4M/yr for the team | ASSUMED |
| Volume | ~8,000 contacts/month across chat and email, Dutch and English | ASSUMED |
| ARR | ~€50M, a typical figure for a 350-person SaaS company | ASSUMED |
| Works council | You have an ondernemingsraad (OR), which is required at 50+ employees | MEDIUM |
| Location | All support staff work in one UWV region (werkgebied) | ASSUMED |

---

## 3. Why I don't recommend zero humans by 30 June

### 3.1 The legal timeline forces the decision before there is evidence

Working back from a last working day of 30 June [MEDIUM: Dutch employment law from working knowledge; your employment counsel must confirm every step]:

| Step (working backwards) | Typical duration | Latest start |
|---|---|---|
| Notice period after a UWV permit (statutory notice minus the UWV procedure time, with at least 1 month remaining) | 1 month or more | End of May |
| UWV dismissal permits on economic grounds (each employee gets 14 days to respond, often followed by a second round) | 4 to 8 weeks | Mid-April |
| Collective-dismissal notice (WMCO): 20 or more dismissals within 3 months in one region means you notify UWV and the unions in advance, and UWV waits 1 month before handling permit requests. Settlement agreements count toward the 20. | 1 month | Early March |
| Works council advice (WOR art. 25) on the reorganisation, requested while it can still change the decision. If you decide against the advice, a 1-month standstill applies, during which the OR can appeal to the Ondernemingskamer (the Enterprise Chamber of the Amsterdam Court of Appeal). | 4 to 8 weeks, plus a possible 1 month | Mid-January |
| Business case, alternatives considered, role design and draft social plan, ready for the advice request | 3 to 4 weeks, over the Christmas break | Now |

**So what:** "zero by 30 June" puts a dismissal proposal on the OR's desk around mid-January 2027. By then you will have chosen a vendor but the AI will not be live. If it underperforms in April, the people who would fix it are already working their notice.

If you keep some humans in interchangeable roles, Dutch law decides who stays through the *afspiegelingsbeginsel*: selection by age group, then last-in-first-out within each group. Performance does not decide it. [MEDIUM]

### 3.2 An AI agent resolves part of the work, and it is the easy part

- Vendor-published resolution rates for mature deployments run roughly 40–65% of conversations. Your ticket mix decides where you land. [ASSUMED: vendor-reported figures from self-selected customers; measure your own in the pilot]
- The AI takes the short tickets first: password resets, how-to questions, invoice copies. So 50% of contacts is roughly 25–35% of agent hours. The work that remains is longer, more technical and more emotional. [ASSUMED]
- In B2B SaaS much of the volume is account-specific: bugs that need reproducing, integrations, permissions, outages, billing disputes, renewals at risk. That work needs a person with context and the authority to act.
- Having zero support staff doesn't remove that work. It moves escalations to engineers and CSMs, which is the most expensive support channel you have.

### 3.3 The track record so far

- In early 2024 Klarna said its AI assistant was handling two-thirds of customer chats and doing the work of about 700 agents. In 2025 its CEO said cost had been too dominant a factor, quality had dropped, and Klarna started hiring human agents again. [MEDIUM: widely reported; not re-checked today]
- Gartner has predicted that by 2027, half of the organisations that planned big cuts to customer-service headcount because of AI will abandon those plans. [LOW: from memory, not re-checked] A 2024 Gartner survey found that about 64% of customers would prefer companies not to use AI in customer service. [MEDIUM]

### 3.4 Your team is the AI's teacher and your best product sensor

- An AI agent's resolution rate depends mostly on knowledge quality: articles, macros, policies and edge cases. That knowledge is in your agents' heads. If you announce cuts first, the best agents leave first, because they have the most options, and the knowledge goes with them.
- Support is your richest product signal. If most tickets are "how do I do X", the product has a usability or onboarding problem, and the CPO playbook treats that as a product-market-fit red flag. The cheapest ticket is the one the product prevents. An AI that answers those questions well hides the problem instead of fixing it.

### 3.5 The economics are good, but smaller than the headline

[ASSUMED throughout: plug in your salary, volume and ARR figures]

| | Option A: zero by 30 June | Option B: recommended |
|---|---|---|
| Support people cost today | €1.4M/yr | €1.4M/yr |
| AI platform and usage (about €1 per resolution, ~4,000 resolutions/month, plus platform fees and implementation) | €0.1–0.2M/yr | €0.1–0.2M/yr |
| People still needed to run the AI (knowledge, QA, configuration) | 3–5 FTE ≈ €0.2–0.3M/yr, usually taken from engineering or CS | Already in the reshaped team |
| One-off costs: transitievergoeding (statutory severance of 1/3 of a monthly salary per year of service), social plan, outplacement, legal | €0.2–0.5M | None in H1 |
| Year-one net run-rate benefit if quality holds | ~€1.0M/yr | ~€0.3–0.5M/yr (5–8 roles not backfilled, minus AI cost, plus customer growth absorbed without hiring) |
| Downside: 1 extra point of gross churn on €50M ARR | −€0.5M/yr | Lower exposure, because humans stay as the fallback and the change is reversible |

**So what:** Option A's extra ~€0.5–0.7M a year only exists if support quality doesn't slip. The downside is about the same size, and it arrives 6–12 months later, in renewals.

---

## 4. The plan (Option B)

### End state on 30 June 2027

- The AI agent is the default first line on chat, email and in-product help for all customers. It tells people it is an AI, and they can reach a human in one click.
- The AI's true resolution rate is at least 45% of in-scope contacts. CSAT is within 3 points of the human baseline, wrong answers are at most 2% of QA samples, and there have been no severe incidents. [ASSUMED: starting targets, to be reset after Phase 0]
- Contacts per active account are down at least 15%, because the product fixes the top 5 "how do I" drivers.
- The support team has moved into the roles in section 5, and no roles have been backfilled since December. A workforce decision memo, based on 3 months of production data, is ready for you.

### Owners

| Responsibility | Owner |
|---|---|
| Executive sponsor; decides at each gate | CPTO |
| The AI agent as a product. Run it as a specialist team with its own PM, like any complex subsystem. | One senior PM, full time |
| Support operations | Head of Support |
| Helpdesk integration, data, authentication | 2 engineers at ~50% |
| Works council, Dutch employment law, internal communication | HR lead + employment counsel |
| DPIA (data protection impact assessment), vendor data processing agreement (DPA), subprocessors | DPO / security |
| Enterprise contracts, customer communication | Head of CS + Legal |
| Business case | CFO |

### Phase 0: Baseline and set-up (23 November 2026 to 15 January 2027)

1. **Ticket data, 6–12 months.** Volume by channel, category, language and segment, plus handle time, CSAT, reopen rate and escalations to engineering. Tag each ticket by contact driver and by type:
   - *AI-able*: can be answered from the docs or account data.
   - *Needs authority*: refunds, contract changes.
   - *Needs investigation*: bugs, integrations.
   - *Needs a human*: complaints, churn risk, outages.

   → Head of Support + analyst → **18 Dec**
2. **Human baseline.** Record CSAT, first-contact resolution, 7-day re-contact rate and handle time per category. This is the standard the AI will be judged against. → Head of Support → **18 Dec**
3. **Works council.** Inform the OR and ask for its advice on introducing the AI agent as an important technological change (WOR art. 25(1)(k)). Propose no dismissals. Check whether art. 27 consent is needed if QA tooling will score individual agents. → CPTO + HR → **request by 11 Dec**
4. **Team briefing,** in the same week and after the OR. Cover what's coming, the fact that they will build it, what you know and don't know yet, and the commitments in section 5. → CPTO + Head of Support → **11 Dec**
5. **Hiring freeze on support backfills.** Offer internal vacancies to support staff first. → HR → **1 Dec**
6. **Contract review.** Check support SLAs, language commitments, subprocessor-notice windows (often 30 days) and any clauses promising named human support. → Legal + CS → **15 Jan**
7. **Vendor shortlist of 2–3.** Criteria: EU data residency, no training on your data, helpdesk integration, Dutch-language quality, per-resolution pricing, handoff tooling, audit logs. → AI agent PM → **15 Jan**

### Phase 1: Build and offline evaluation (January to 26 February 2027)

1. **Knowledge rebuild.** Senior agents spend ~30% of their time turning the top 50 intents into verified articles and policies. → Head of Support → **26 Feb**
2. **Bake-off.** Run each vendor on ~500 real historic tickets in Dutch and English. Senior agents grade the answers blind for correctness, tone and correct handoff. → AI agent PM → **12 Feb**
3. **Guardrails** (section 6) configured and red-team tested by agents. → AI agent PM → **26 Feb**
4. **Compliance.** Complete the DPIA, sign the DPA, send subprocessor notices to customers and write the AI disclosure text (EU AI Act art. 50, in force since August 2026 [MEDIUM]). → DPO + Legal → **26 Feb**
5. **Product.** Pick the top 5 "how do I" drivers and put the fixes on the Q1/Q2 roadmap. → CPTO + product leads → **15 Feb**

### Phase 2: Live pilot (1 to 31 March 2027)

- Run it in one segment and channel, for example SMB customers on chat in Dutch and English. Ramp from 10% to 50% to 100% of that segment.
- The AI ops group reviews failed and handed-off conversations every day and ships fixes the same week.
- The CPTO gets a scorecard every week.

### Gate 1: 31 March 2027 (criteria written and agreed before the pilot starts)

| Metric | Pass to scale | Definition |
|---|---|---|
| True resolution | ≥ 35% of pilot contacts | No human touch, and no re-contact on the same issue within 7 days |
| CSAT on AI-resolved contacts | Within 3 points of the human baseline | Same survey, same segment |
| Wrong or off-policy answers | ≤ 2% of a QA sample of at least 200 conversations; zero severe | Severe means a security, data, financial or contractual commitment |
| Time to a human when asked | No worse than the current first-response SLA | |
| Agent view | A majority of the AI ops group says it is ready | Their names go on the sign-off |

If it fails, extend the pilot by 4–6 weeks and fix the knowledge base. Don't scale on hope.

### Phase 3: Scale to the front door (April to June 2027)

- April: all chat. May: email and in-product help.
- Enterprise accounts get the AI too, with a human-first lane for P1 incidents and named contacts until their CSAT holds.
- The team moves into its new roles (section 5) as volume shifts.
- The fixes for the top 5 drivers ship, and contact rate is tracked weekly.

### Gate 2: 30 June 2027, the workforce decision memo

The memo uses three months of production data: resolution, CSAT, re-contact, wrong-answer rate, contact-rate trend, churn reasons in renewals of pilot accounts, and actual hours freed by category. It answers one question: given growth, how many people does support need for the next 12 months? If there is a structural surplus after attrition and internal moves, go to Phase 4.

### Phase 4: Only if needed (Q3 2027)

- Send a formal advice request to the OR, backed by the evidence.
- Agree a social plan.
- Send the WMCO notice if 20 or more people will leave within 3 months.
- Use UWV permits or settlement agreements.
- Offer redeployment first. It is also a legal duty.

With the assumed numbers, I expect the gap to be small enough that attrition and internal moves cover most of it. [ASSUMED]

---

## 5. What happens to the 25

Illustrative shape on 30 June [ASSUMED: set after Phase 0]:

| Role | People | Why |
|---|---|---|
| AI ops & knowledge | 3 | Owns the knowledge base, intents, policies and the weekly failure review. The AI's quality is their output. |
| QA & conversation review | 2 | Samples AI and human conversations; owns handoff quality |
| Tier 2: technical and enterprise | 9–11 | Bugs (reproduced before they reach engineering), integrations, P1s, complex billing |
| Customer insight to product | 1 | Turns contact drivers into the product backlog and closes the loop |
| Onboarding and proactive success | 2–3 | Shifts effort from reacting to preventing, which is where retention is won |
| Moved, left or not backfilled | 5–8 | Natural attrition (often high in support) and internal moves to CS, implementation, QA and docs |

**Commitments I'd make to the team at the December briefing:**

- **No forced redundancies before the Gate 2 decision.** Anything after that goes through the works council with a social plan. Option B doesn't plan dismissals before Q3 anyway, so this costs nothing, and it keeps the knowledge in the building while you need it most.
- **Paid training for the new roles**, and internal vacancies offered to support staff first.
- **The team helps set the gates**, and their sign-off is one of them.
- **Be honest about selection.** If a reduction happens later, afspiegeling decides who stays within interchangeable roles. Don't tell anyone they're safe because they're good, and don't design roles to steer who gets selected. Counsel will stop that, and should.

---

## 6. Guardrails: what the AI never does alone

- Refunds, credits or discounts above a set threshold. Any change to a contract, price or plan.
- Security incidents, suspected breaches, account takeover.
- GDPR requests (access, deletion) and any legal or compliance statement.
- Outages: the AI gives the status-page message and nothing more.
- Cancellation intent or strongly negative sentiment: route to the CSM.
- P1 incidents from enterprise accounts.
- **Always:** the AI says it is an AI, a human is one click away, and the full transcript is handed over so the customer never has to repeat themselves.

---

## 7. Metrics

**North star for support:** the share of customer issues resolved the first time (no re-contact within 7 days) with CSAT at or above today's level. Don't use "headcount removed" or "deflection".

| Leading (weekly) | Lagging (monthly) |
|---|---|
| AI true resolution rate | CSAT trend by segment |
| Wrong-answer rate (from QA) | Contacts per active account |
| Handoff rate and time to a human | Gross revenue retention in accounts that use support heavily |
| Knowledge coverage of the top intents | Cost per resolved issue |
| 7-day re-contact rate | Escalations to engineering |

**Watch out:** vendor dashboards count a conversation as "resolved" when the customer simply gave up. Measure re-contact and CSAT, not deflection.

---

## 8. Legal and compliance checklist (Netherlands and EU)

[MEDIUM: from working knowledge to mid-2026, not re-checked. Employment counsel and the DPO must confirm before anything is sent.]

- **Works council (WOR).**
  - The OR has advice rights on introducing an important technology (art. 25(1)(k)) and on any reorganisation or major reduction.
  - You must ask for advice early enough that it can still change the decision. If you decide against the advice, a 1-month standstill applies, and the OR can appeal to the Ondernemingskamer.
  - The OR's consent is needed (art. 27) for systems that can monitor employee performance.
- **Collective dismissal (WMCO).** 20 or more dismissals within 3 months in one region require advance notice to UWV and the unions, followed by a 1-month waiting period. Settlement agreements count toward the 20.
- **Dismissal on economic grounds.**
  - You need a UWV permit or a settlement agreement for each person.
  - You have a duty to look for redeployment first.
  - Afspiegeling decides who goes within interchangeable roles.
  - Statutory notice periods and the transitievergoeding (1/3 of a monthly salary per year of service) apply.
- **EU AI Act art. 50.** People must be told they are dealing with an AI (applies from 2 August 2026). A support agent is not a high-risk system.
- **GDPR.** Vendor DPA, subprocessor list, transfers outside the EEA, DPIA, retention rules, and an opt-out from the vendor training its models on your data.
- **Customer contracts.** SLAs, language commitments, subprocessor notice and objection rights, clauses promising named human support.

---

## 9. If you choose Option A: fast track with no separate pilot

*Updated 23 Nov 2026, after "skip the pilot".*

The works council and UWV set the 30 June date, not the pilot. So the fast track doesn't run a separate pilot. Instead, it goes live in stages from 1 March, alongside the legal track. Stop rules are written in advance, and there is a go/no-go decision before the first step you can't take back.

| Date | Legal track [MEDIUM: confirm every step with counsel] | AI track |
|---|---|---|
| By Fri 4 Dec | Employment counsel engaged. OR told in confidence: the information is marked confidential, and OR members are bound by WOR art. 20 | Start pulling ticket data; draw up the vendor shortlist. Only a short evaluation agreement with vendors, committing to nothing beyond the offline test |
| By Fri 18 Dec | Business case, alternatives considered, social plan and retention package drafted | Human baseline set (CSAT, 7-day re-contact, handle time) |
| 4–22 Jan | | Offline test of 2–3 vendors on ~500 historic tickets in Dutch and English. No customers involved. Graded blind by a small confidential group: Head of Support plus 2–3 senior agents, each with a signed confidentiality agreement and a stay bonus. Vendor chosen by Fri 22 Jan |
| Fri 15 Jan | OR advice request on the full plan, presented as a proposal, not a decision. Team briefed the same week, together with the retention package (timing agreed with the OR) | Subprocessor notices sent to customers (often 30 days' notice) |
| Fri 22 Jan | | Production vendor contract signed **subject to works council advice** (the standard Dutch "onder voorbehoud van OR-advies" condition), with an exit right if the plan changes after the advice |
| February | OR deliberates | Knowledge base rebuilt with senior agents; guardrails (section 6); integration |
| Mon 1 Mar | WMCO notice to UWV and the unions | Staged go-live: one segment in week 1, then more each week. All chat by end of March, email from April |
| **Wed 14 Apr** | **Go/no-go on 6 weeks of live data**, before anything you can't take back | Stop rules reviewed |
| Mid-April | UWV permit applications or settlement agreements: **the first irreversible step** | AI at full chat volume |
| End of May | Notice given | Email and in-product help at full volume |
| Wed 30 Jun | Last working day | AI is the whole front line |

**Stop rules.** Write them before 1 March, have the CPTO sign them and share them with the OR. [ASSUMED: thresholds to be set from the Phase 0 baseline]

- CSAT on AI-handled conversations is more than 5 points below the human baseline for 2 weeks in a row.
- The 7-day re-contact rate on AI-handled contacts is more than 1.5× the human baseline.
- There is any severe error: a security, data, financial or contractual commitment.
- Time to reach a human is worse than the first-response SLA for a week.

If a stop rule trips before 14 April, pause the rollout and move the UWV step back. If it trips after notices have gone out, you are relying on the vendor and whatever escalation path you funded.

**Also needed on the fast track:**

1. **Retention bonuses for the senior agents** who build the knowledge base, payable if they stay until 30 June. They are building the system that replaces them, and the AI's quality depends on them staying. Price this into the one-off costs.
2. **A funded human escalation path,** for example CSMs or engineers on rotation, priced into the business case.
3. **A reversal plan written now.** What will you do if the April–June numbers miss and the team has gone? Klarna's answer was to rehire.
4. **A proposal, not an announcement.** Expect the OR to resist a plan that's presented as already decided. If you announce the decision before asking the OR's advice, the Ondernemingskamer can reverse it.
5. **Ask the OR before you sign anything binding.** *Added 23 Nov, after "don't tell the team or the works council until the vendor contract is signed".* [MEDIUM: confirm with counsel]
   - The advice must be asked while it can still change the decision (WOR art. 25(2)).
   - A signed production contract to replace the team makes the advice a formality. That gives the OR strong grounds at the Ondernemingskamer, which can order the decision withdrawn and its consequences undone (art. 26), and that would stall the Q2 date by months.
   - **The lawful way to keep this quiet:** tell the OR first in confidence (art. 20), sign the contract subject to the OR's advice, and tell the team when the advice request goes in, together with the retention package.
6. **The retention package is what stops early departures, not secrecy.**
   - A stay bonus payable on the last working day: about 1–2 months' salary each, roughly €0.1–0.2M for the team. [ASSUMED]
   - An enhanced social plan and outplacement.
   - First call on internal vacancies.
   - Paid time for job searching.

   Announce it together with the news. The plan can't be kept secret anyway: ticket exports, vendor access, the DPIA, engineers and the grading group all touch it. If people learn about it from rumour with no package on the table, they leave early anyway.

**What skipping all live testing would mean:** the AI handles full volume for the first time on 1 July, the day after the team has left.

---

## 10. Critic pre-screen (of this recommendation)

- **Weakest point:** the numbers that drive the recommendation (resolution rate, workload split, salaries, ARR, attrition) are my assumptions, not your data. Phase 0 exists to replace them, and the real numbers could change the answer.
- **Missing perspective:** your customers and your team. Neither has been asked yet. Five interviews with enterprise admins and a working session with your senior agents in December would test this plan better than anything else.
- **If I'm wrong:**
  - If your mix is very simple and the AI resolves 70% or more, Option B delays perhaps €0.2–0.4M of savings by a quarter.
  - If Option A turns out wrong, you lose team knowledge, take a CSAT and renewal hit that shows up 6–12 months later, risk proceedings at the Ondernemingskamer and pay to rehire.
- **Proceed:** yes, with these risks noted.

---

## 11. Peer verification still needed before execution

None of this was done for this draft:

- **HR + Dutch employment counsel:** every step in sections 3.1, 8 and 9.
- **CFO:** the business case in section 3.5, using real salary, volume and ARR data.
- **DPO / security:** vendor DPA, DPIA, data residency.
- **Head of Customer Success:** enterprise contract clauses and the human-first lane.
- **Head of Support:** the workload split and the team shape in section 5.

---

## 12. Your decision

| Option | What it means | Trade-off |
|---|---|---|
| **A** | Replace all 25 by 30 June, using the staged go-live and the 14 April go/no-go in section 9 | Biggest saving if quality holds. Six weeks of live data before the first irreversible step, but the decision is hard to reverse and escalations land on engineering. |
| **B** (recommended) | AI front door by 30 June, team reshaped, headcount decision in Q3 based on evidence | Smaller saving in year one. Reversible; protects knowledge and renewals. |
| **C** | B, plus a conditional ambition you take to the board, for example a support team of ~15–18 by end of 2027 if the Gate 2 numbers hold | Gives the board a number. Share it openly with the OR as a scenario, not a commitment. |

**Recommendation: B.** It captures most of the savings that actually exist and keeps the decision reversible until you have data.

---

*Sources: no live web search was available for this draft. The external figures (Klarna, Gartner, vendor resolution rates and pricing) and the Dutch and EU legal points come from working knowledge to mid-2026 and are tagged that way. Ask, and I'll check them against current sources.*

---

## Appendix: week-by-week timeline (fast track, Option A)

*Added 23 Nov 2026. This applies the section 9 fast track: tell the works council in confidence, sign subject to its advice, staged go-live, go/no-go on 14 April.*

| Week of | People & legal | AI & product | Milestone |
|---|---|---|---|
| **23 Nov** | Brief employment counsel on the fast track | Start pulling 6–12 months of ticket data | |
| **30 Nov** | Tell the works council in confidence (WOR art. 20); counsel signs off the sequence | Vendor shortlist; evaluation-only agreements (no commitment) | **Fri 4 Dec:** works council told in confidence |
| **7 Dec** | Draft the business case and the alternatives considered | Tag tickets by contact driver and type | |
| **14 Dec** | Draft the social plan and retention package (stay bonus paid on the last day) | Set the human baseline: CSAT, 7-day re-contact, handle time | **Fri 18 Dec:** drafts and baseline ready |
| **21 Dec** | Christmas (25–26 Dec). Counsel reviews the advice request | Build the offline test set: ~500 past tickets, Dutch and English | |
| **28 Dec** | New Year (1 Jan). Quiet week | | |
| **4 Jan** | Finalise the advice request; agree with the works council when the team is briefed | Offline vendor test starts. Graded by a confidential group (Head of Support + 2–3 seniors, stay bonuses signed) | |
| **11 Jan** | Submit the advice request; brief the team the same week with the retention package; send subprocessor notices to customers | Offline test continues | **Fri 15 Jan:** advice request in, team told |
| **18 Jan** | 1:1s with every agent (package, internal vacancies) | Test results; choose the vendor; sign the contract subject to works council advice | **Fri 22 Jan:** vendor contract signed (conditional) |
| **25 Jan** | Works council deliberates; social plan talks | Integration starts; knowledge-base rebuild starts (top 50 intents) | |
| **1 Feb** | | Knowledge-base rebuild continues; guardrails configured | |
| **8 Feb** | | Agents red-team the AI | |
| **15 Feb** | | Top 5 "how do I" fixes on the roadmap; human-first lane for enterprise accounts set up | |
| **22 Feb** | Works council advice due (target) | Stop rules written, signed by the CPTO, shared with the works council | **Fri 26 Feb:** works council advice in; stop rules signed |
| **1 Mar** | Decision taken after the advice. Collective-dismissal (WMCO) notice to UWV and unions; the 1-month wait starts | Go-live, segment 1 (e.g. SMB chat) | **Mon 1 Mar:** go-live and WMCO notice |
| **8 Mar** | | Segment 2; daily review of failed conversations; weekly stop-rule check | |
| **15 Mar** | | Segment 3 | |
| **22 Mar** | Good Friday (26 Mar) | All chat live | |
| **29 Mar** | Easter Monday (29 Mar). WMCO wait ends around 1 Apr | Chat at full volume | |
| **5 Apr** | Prepare UWV files and settlement offers | Email go-live starts | |
| **12 Apr** | **Go/no-go on Wed 14 Apr**, based on 6 weeks of live data. If go: file UWV applications or offer settlements by Fri 16 Apr | | **Wed 14 Apr:** go/no-go. **Fri 16 Apr:** first irreversible step |
| **19 Apr** | Employees have 14 days to respond to UWV; settlement agreements have a 14-day cooling-off period | Email ramping up | |
| **26 Apr** | King's Day (Tue 27 Apr) | Email at full volume | |
| **3 May** | Ascension (Thu 6 May). Second UWV round if needed | In-product help live | |
| **10 May** | | Enterprise accounts moved onto the AI, with the human-first lane for P1 incidents | |
| **17 May** | Whit Monday (17 May) | All channels at full volume | |
| **24 May** | UWV decisions expected (about 6 weeks after filing) | Escalation rota (CSMs or engineers) trained | |
| **31 May** | **Give notice by Mon 31 May**, so it ends 30 June | Departing agents hand over their final knowledge | **Mon 31 May:** notice deadline |
| **7 Jun** | Outplacement starts; internal moves finalised | AI runs the front line; agents review its handling | |
| **14 Jun** | | Agents keep reviewing AI conversations | |
| **21 Jun** | | Final checks; reversal plan reviewed | |
| **28 Jun** | Last working day Wed 30 Jun; stay bonuses paid | From 1 July the AI is the whole front line | **Wed 30 Jun** |

**WHAT CAN MOVE THE END DATE** [MEDIUM: confirm with counsel]
- **The works council's advice arrives after end February.** Everything after it moves by the same amount. If you decide against its advice, a 1-month standstill follows. It ends around 1 April, so it fits the plan, unless the works council goes to the Enterprise Chamber (Ondernemingskamer), which would freeze the plan.
- **UWV takes 8 weeks instead of 6.** Decisions land around 11 June, and the last working day moves to 31 July. Settlement agreements avoid UWV, but each person has to agree.
- **Staff with 10+ years' service** may have a notice period that runs past 30 June.
- **A stop rule trips before 14 April.** You pause the rollout and move the UWV step back. After 16 April, you're relying on the vendor and your escalation rota.

**Three dates you can't miss** if 30 June is to hold: the advice request on 15 Jan, UWV filing on 16 Apr, and notice by 31 May.
