# Business case: AI agents, QA and second-line support

**Decision needed by:** [date] · **Decision owner:** [CEO] · **Prepared:** [date] · **Status:** draft for challenge

## The decision in one sentence
Whether to reduce the QA team (6 people) and second-line support (10 of 20 engineers) because AI agents are said to be "basically never wrong". Recommendation: do not change headcount on that claim. Run a six-week measured pilot with human review, and decide on the results.

## Why the claim is not yet a basis for a decision
- No error rate has been shared. "Basically never wrong" has no number, task list or measurement method behind it. Until it does, it is an opinion.
- QA and second-line support exist to catch what is wrong. The cut removes the people who would find the AI's mistakes, so errors would stop being measured at the moment they could start to rise. An error rate that looks low can mean mistakes are not being seen.
- The company remains responsible for what its AI does. In Moffatt v. Air Canada (2024 BCCRT 149, February 2024), a tribunal held the airline liable for wrong information from its own chatbot and rejected the argument that the chatbot was responsible for itself.
- Perceived and measured gains differ. In a 2025 randomised trial (METR, 16 experienced developers, 246 tasks), AI use made tasks take 19% longer while the developers believed it had made them faster. Newer tools may do better, which is why the measurement has to be on our own work.
- Klarna said in February 2024 that its AI assistant did the work of 700 agents. In May 2025 its CEO said cost had been too dominant a factor and quality had suffered, and it began hiring human agents again.

## What we know and don't know
| Fact | Value | Source and date | Confidence |
|---|---|---|---|
| Error rate of the AI agents, by task type | Not provided | CTO claim, no data | None |
| Share of tickets resolved by AI in production, and repeat-contact rate | Not provided | Ticketing system | To fetch |
| Defects caught by QA before release, last 12 months | Not provided | Bug tracker / QA reports | To fetch |
| Customer-reported incidents and cost of a production defect | Not provided | Incident log, finance | To fetch |
| Fully loaded cost of the 16 roles | Not provided | Finance / HR | To fetch |
| Handling time of the tickets the AI would take | Not provided | Ticketing system | To fetch |

The savings case cannot be completed until these are filled in. Nothing below is a number I could verify.

## Options
| Option | Effect | Time to effect | People affected | Hidden costs | Reversible? | Main risk |
|---|---|---|---|---|---|---|
| A. Do nothing | No saving, no change | n/a | None | Lost chance to use AI | Yes | Falling behind if AI is in fact good |
| B. Cut as proposed (6 QA + 10 support) | Salary cost of 16 roles, less severance, less AI run cost | 3-6 months after consultation | 16 people, plus 20 who stay | Severance, lost product and customer knowledge, rehiring, incident cost, survivors leaving | Hard: knowledge leaves | Errors reach customers unseen |
| C. Measured pilot, then decide (recommended) | Evidence; possible redeployment of freed hours | 6 weeks pilot, then review | Volunteers in both teams | Pilot time and review effort | Yes | Delay of about two months |
| D. Use AI to remove toil, keep the people | Frees hours for unmet demand, backlog, test automation, faster resolution | 1-3 months | None lost; roles change | Training time | Yes | Gains smaller than hoped |
| E. Hiring freeze and attrition in these teams, if the pilot supports it | Gradual saving as people leave | 6-18 months | None forced | Thinner coverage if misjudged | Yes | Uneven loss of skills |

Customer view: more errors and slower human escalation. Finance view: severance and incident costs arrive now, savings arrive later and are uncertain. Technology view: AI output needs independent verification, and QA is that check. People view: 16 jobs and the trust of the remaining 20 are at stake.

## Recommendation
Option C, then D and E depending on what the pilot shows. Layoffs are the last step, and the pilot has not yet shown that earlier steps cannot meet the goal. If the real goal is a specific cost target, we should first compare this with cloud, licence and vendor spend and with the AI spend itself.

## Pilot design (six weeks)
1. Agree metrics before starting, and fix them: error rate by task type (found by a human reviewer, not by the AI), customer satisfaction, repeat contacts within seven days, escalations to a person, defects escaping to production, and time spent reviewing AI output.
2. Keep QA and second-line fully staffed for the pilot, so that errors are actually found. QA and support engineers review and label a sample of AI work each week, and design the test with the CTO.
3. Compare AI-handled and human-handled work on the same ticket and release types, with ticket mix reported, since AI tends to take the short and easy contacts.
4. Size freed capacity in hours: contacts x production resolution rate x (handling time of AI-resolved contacts / average handling time) x average handling time, minus new AI work (reviewing, knowledge base, tuning).
5. Set decision thresholds in advance, for example the maximum acceptable escaped-defect rate and the minimum satisfaction level, and publish them.
6. Name where a person stays accountable regardless of results: legal and contractual commitments, safety, customer promises, decisions about people.

## Human impact
| Question | Answer |
|---|---|
| Who is affected? | 6 QA and 10 second-line engineers directly; the other 14 support engineers and all engineers who rely on QA indirectly |
| What do they lose that is hard to replace? | Income, and for a few possibly tenure-based protections; the company loses product knowledge |
| What do we offer? | A job-security commitment during the pilot, paid learning time, a role in designing the review process, moves into test automation, AI quality and support tooling |
| Who stays, and how do they feel? | Workload and uncertainty rise if the cut happens; trust in leadership drops |
| Legal and consultation | Employee representatives (works council where applicable) must be consulted early enough to change the plan, and a decision to introduce AI tools touching employees' work may need their consent. Get employment counsel before any reduction. This is not legal advice. |

## Risks and what would change my mind
- Assumption: the AI's error rate on our real work is unknown. If six weeks of independently reviewed samples show a low, stable error rate with no rise in escapes or repeat contacts, the case for gradual reduction through attrition (option E) becomes strong.
- If the pilot shows the AI does well on only some tasks, we keep QA and support for the rest and reduce only where proven.
- If the company has a cash or covenant problem that forces a faster saving, I would want to see it, and we would look at other cost options and leadership pay first.

## Communication
Tell the affected teams now what is being explored and why, before anything is decided; involve employee representatives at this stage; managers hear first. Leaders own the outcome: if the pilot is wrong or the claim was overstated, that is a leadership failure to be stated plainly, not something a team should carry.

## Questions for you (pushback welcome)
- What error rate is the CTO assuming, on which tasks, measured by whom?
- What is the cost target and by when? Is it cash, margin or a board expectation?
- What am I missing, and what would make this wrong?
