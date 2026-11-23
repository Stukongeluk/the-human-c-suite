# Customer support and AI: plan to end of Q2

Draft for the executive team and, once agreed, the works council (OR). Figures marked (est.) are placeholders until measured in Phase 0.

## 1. The decision in one paragraph

By the end of Q2 we put an AI agent in front of customers and have it resolve a measured share of contacts at quality at least equal to today's. We do not decide on the size of the support team in this plan. That decision comes after two quarters of measured results, and the first answer to "what happens to freed capacity" is attrition, redeployment and growth, not exits. The 25 people are the knowledge the agent will be built from, and they are who will judge whether it is good enough.

## 2. Problem and outcome

**Customer problem.** Customers want fast, correct answers and a way to reach a person when it matters.
**Business outcome.** Lower cost to serve per resolved contact, with no loss in customer satisfaction, retention or first-contact resolution.
**Do nothing:** cost to serve grows with the customer base and we are slower than competitors who automate routine contacts.

What we still need to establish (Phase 0):

| Question | Source |
|---|---|
| Contact volume by type, and the share that is routine, repeatable and answerable from documentation | Ticketing system, 3 to 6 months, sampled and labelled by the support team |
| Resolution time, first-contact resolution, CSAT, reopen rate today | Ticketing system |
| Contacts caused by our own product (bugs, unclear UX, onboarding) | Tag review with support and product |
| What the 25 people do besides answering tickets (onboarding calls, escalations, bug triage, customer success work) | Interviews, team lead |
| Current cost: salaries, tooling, plus expected AI cost per resolved contact | Finance |
| Churn reasons that mention support | CRM |

## 3. Options

| Option | What it is | Customer effect | People effect | Reversible? |
|---|---|---|---|---|
| A. Do nothing | Keep the current model | Unchanged | None | Yes |
| B. AI-assisted agents | AI drafts replies and finds answers for the 25; humans send | Faster, same quality | Work changes, nobody leaves | Yes |
| C. AI first line, humans behind it (recommended) | Agent resolves routine contacts in chat and email, hands over with full context; humans handle the rest and improve the agent | Faster on routine, human for the rest | Work shifts; headcount via attrition and redeployment | Mostly |
| D. Full replacement by end of Q2 | Agent handles all contact, team ends | Highest risk: no human route, liability for wrong answers | 25 roles end | No |

Why not D. Three reasons from outside evidence:

- Klarna said in 2024 its AI did the work of 700 agents, then in 2025 its CEO said cost had been weighted too heavily, quality suffered, and it started hiring human agents again.
- In a 2025 survey of over 1,000 senior leaders, 55% of those who made AI-related redundancies said they had made wrong decisions (vendor survey; a strong signal, not a precise rate).
- A company is liable for what its AI tells customers (Moffatt v. Air Canada, 2024).

IKEA's Ingka Group is the better model: its assistant handled 47% of call-centre queries, and about 8,500 staff were retrained as remote design advisers, a business reported at about EUR 1.3 billion revenue in 2022.

## 4. Recommended path: C, in gated phases

Dates assume a start in December 2026 and are to be confirmed with the team that builds it.

### Phase 0: Measure (Dec to mid Jan)
- Label a sample of historical contacts with the support team: routine or not, answerable from our knowledge base or not.
- Build the evaluation set: real cases with correct answers, including hard and sensitive ones.
- Inform the OR (see section 6) and start talking to the 25.
- **Gate:** we know the realistic automatable share, cost per contact today, and the baseline for quality.

### Phase 1: Shadow mode (mid Jan to end Feb)
- The agent drafts answers to live contacts; nobody sees them except support staff, who rate each draft.
- Fix the knowledge base gaps that support staff find.
- **Gate:** accuracy on the evaluation set at or above the target we set in Phase 0, and no serious failures (wrong refund, wrong legal or security statement, data exposure) in the sample.

### Phase 2: Design partners and limited beta (Mar to Apr)
- Live for one contact type and a small set of consenting customers. Clear disclosure that they are talking to an AI, and a one-step route to a person.
- Staff review a sample of conversations daily and can pause the agent.
- **Gate:** CSAT and first-contact resolution not below human baseline for the same contact types, escalation hand-over works, cost per resolved contact (est.) below human cost.

### Phase 3: Gradual expansion (May to June)
- Add contact types one at a time, each passing the same gate. Keep a visible "talk to a person" option throughout.
- **End of Q2 outcome:** the agent live on the contact types that passed their gates, with the measured share of contacts it resolves reported honestly, whatever it is.

### After Q2: decide on capacity with data
Only after at least a full quarter of live results do we decide what the freed capacity is used for. Order of use:
1. Contacts we can remove at the source: fix the product issues that generate them (support and product work together here).
2. Move people to work customers want and we lack capacity for: proactive onboarding, customer success, complex-case and key-account support, training and quality of the agent, knowledge-base ownership.
3. Absorb growth in customers without hiring.
4. Attrition and not refilling roles.
5. Only if the data shows a structural surplus after all of the above: a separate decision, with the OR, following the Dutch consultation process, and with support for each person (section 7).

## 5. Quality, safety and compliance

- **Evaluation.** Maintained test set of real cases; measured accuracy per contact type; named failure modes; weekly review of sampled live conversations after launch.
- **Human route.** Always available, one step, and never punished by a worse queue.
- **Escalate by default** for: cancellations and disputes over money, security incidents, data-protection requests, complaints, vulnerable-customer signals, anything the agent is unsure about.
- **Transparency.** The AI Act (Article 50, applicable since August 2026) requires telling people they are dealing with an AI unless it is obvious. We do this plainly in every conversation.
- **Data protection.** Customer data sent to a model provider needs a processor agreement, a documented lawful basis, retention limits, and a DPIA to be run with the privacy officer. Counsel to confirm.
- **Cost per use.** Model and infrastructure cost per resolved contact, tracked monthly, including re-contacts caused by wrong answers.
- **Kill switch.** Product and support leads can switch the agent off per contact type immediately.

This is a planning document, not legal advice; legal and HR to confirm every Dutch and EU rule cited.

## 6. Works council and employment law (Netherlands)

- With 350 employees we have a works council (OR). It has an advisory right on major decisions such as reorganisations (art. 25 WOR), which must be asked for while it can still influence the plan, and a consent right on systems that can monitor or assess employee behaviour or performance (art. 27(1)(l) WOR). The agent's quality scoring of staff conversations falls under the second: we agree up front that review is of the agent and of teams, not a ranking of individuals.
- Any scenario in the "after Q2" list that ends roles needs HR and counsel before anyone is told. Ending 20 or more jobs in one UWV area within three months triggers the collective-dismissal procedure (WMCO: notify UWV and unions, consult). 25 is above that line.
- The employees are told first, by their own manager, in person, before it is public. No mass mail.
- If there is a collective agreement or sector rules, those also apply. HR to confirm.

## 7. People plan

- **From day one, for all 25:** a named lead for questions, a monthly open Q&A, and an honest summary of where the numbers stand.
- **Co-design.** Support staff are on the design team for the agent: they label data, write the escalation rules and have a veto on launching a contact type if quality fails the gate.
- **Learning on paid time.** Each person gets an agreed number of hours per month and a learning budget (amount to be set with the OR) towards new skills: customer success, product knowledge, prompt and knowledge-base work, data analysis.
- **Career conversations** with every person in the first 60 days: what they want to do, what they are good at, what constraints they have.
- **Support for people if roles ever end,** and we say this now rather than later: paid coaching, training and job-search help from the first day of notice, priority for internal vacancies and rehiring. Leadership's variable pay for this programme is tied to quality and retention results, not to headcount reduction.
- **Pulse.** Monthly short survey and tracking of attrition, absence and regretted exits next to cost savings.

## 8. Measures and review

Reviewed monthly by the CPTO, head of support, CFO and an OR representative.

| Area | Indicator | Target |
|---|---|---|
| Customer | CSAT, first-contact resolution, reopen rate, customer effort, escalation-to-human rate | At or above human baseline per contact type |
| Quality | Accuracy on evaluation set, serious failures in sampled conversations | Target set in Phase 0; zero tolerated for money, security and legal categories |
| Cost | Cost per resolved contact including AI, tooling and re-contacts | Below baseline (est.), reviewed per gate |
| Delivery | Contact types live, share of contacts resolved by agent | Reported as measured, no target before Phase 0 |
| People | Pulse score, attrition, absence, hours of paid learning used | No unplanned drop; reviewed with the OR |
| Business | Churn and renewal rate for accounts with support contacts | No worsening |

Team and process measures only. No ranking of individual support staff.

## 9. Risks and what would change this plan

| Risk | Early sign | Response |
|---|---|---|
| Automatable share lower than hoped | Phase 0 labelling | Smaller scope, AI assist (option B) |
| Wrong answers, liability | Failures in sampled review | Pause the contact type, fix, rerun the gate |
| CSAT drops | Gate metrics | Stop expansion; revert to humans on that type |
| Best support people leave | Pulse, resignations | Talk earlier, retention conversations, share the plan |
| Product bugs drive contacts | Tag review | Fix at source; this is also a saving |
| Model/vendor cost or terms change | Monthly cost per contact | Second provider evaluated before Phase 3 |

What would change the recommendation: Phase 0 shows more than we expect can be automated safely (we could move faster); or shows much less (we stay with B).

## 10. Decisions needed

1. Agree the outcome: measured share at equal quality by end of Q2, not a headcount target.
2. Brief the works council before Phase 1.
3. Name an owner for support, an owner for the agent, and a finance partner for the cost model.
4. Fund Phase 0 and 1.
5. Agree that the capacity decision comes after one quarter of live results.

## 11. Assumptions

- Support contacts are mostly written (chat, email, tickets), not phone.
- A knowledge base exists in some form and can be improved.
- The 25 are employees, not contractors.
- The build is done by a team that estimates its own capacity; if not, dates move.
