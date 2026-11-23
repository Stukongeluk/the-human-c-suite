# Business case: AI agents, QA and second-line support

**An evidence-gated restructuring of QA (6 roles) and second-line support (10 of 20 roles)**

| | |
|---|---|
| Prepared for | CEO, for leadership and board discussion |
| Status | Draft for decision |
| Date | 23 November 2026 |
| Basis | No company data was provided. Every company figure below is a placeholder marked [ASSUMED]. Swap in real payroll, ticket and ARR data before this goes to the board. External evidence is marked [VERIFIED] and linked in section 12. |

---

## 1. Decision requested

Approve **Option B**:

1. An 8 to 10 week independent measurement of the AI agents against pass/fail gates agreed before measuring starts.
2. A reversible freeze on backfilling second-line support roles while the measurement runs, lifted if service levels slip.
3. A decision meeting in March 2027 that reduces QA and second-line support to whatever level the evidence supports. That could be the full 16 roles, part of them, or none. Redeployment and voluntary routes come first.

**Not approved by this case:** announcing or making redundancies now on the strength of the claim "our AI agents are basically never wrong".

---

## 2. Executive summary

- **The savings are real if the claim is true.** Cutting 6 QA and 10 second-line roles saves about **$1.45M a year gross** and about **$1.08M net over 18 months** once severance, extra AI spend and the work others absorb are counted. [ASSUMED payroll figures]
- **The claim has not been measured, and the plan removes the people who measure it.** QA and second-line support are where AI mistakes get caught today. After the cut, nobody would be counting those mistakes, and they would go straight to customers. If the CTO is right, a measurement will show it within a quarter.
- **The outside view is not kind to cut-first plans.** Klarna and Commonwealth Bank reversed AI-driven support cuts. 55% of leaders who made redundancies because of AI say they got those decisions wrong. Forrester expects about half of AI-attributed layoffs to be reversed. [VERIFIED]
- **Gating costs about $0.29M if the CTO is right**, which is roughly three months of delayed savings. **It saves a reversal plus customer damage if the CTO is wrong.** At a reference-class chance of about 50% that the cut gets reversed, gating comes out ahead once a bad year would cost more than **about $0.7M in gross profit**. That is about $0.9M of ARR at a 75% margin, or one or two mid-size customers.
- **Recommendation: Option B.** It lands in the same place about three months later if the agents are as good as claimed. It costs about $30k if they are not.

---

## 3. The claim, restated so it can be tested

"Basically never wrong" has to be turned into a number before it can carry a decision about 16 jobs and the customer base. It has to mean all of the following:

- **A severity-weighted error rate.** A wrong refund promise, a leaked customer record or a missed security flaw does not count the same as a clumsy reply to a password reset.
- **Measured on the actual work mix.** Second-line support gets the hardest tickets by definition. An error rate measured on first-line tickets says nothing about second-line work. Agent success falls sharply as tasks get longer and more conversational: leading agents scored about 58% on single-turn CRM tasks and about 35% on multi-turn tasks in Salesforce's 2025 CRMArena-Pro benchmark. [VERIFIED, 2025 models; yours may do better, which is what the measurement is for]
- **Graded blind, by someone independent.** The team that built the agents should not grade them. Nor should the QA team, whose jobs depend on the result. Both sides have a stake in the answer, so the grading needs a neutral owner and gates agreed in advance.
- **Compared against today's human baseline** on the same tickets and releases.

**How many checks it takes to back the claim.** This is standard statistics (the "rule of three"). If a sample shows zero errors, the most you can claim with 95% confidence is:

| Independent, blind-checked cases with zero errors | Error rate you can claim (95% confidence) |
|---|---|
| 60 | under 5% |
| 300 | under 1% |
| 3,000 | under 0.1% |

So if the claim rests on "we looked at a few dozen and they were all fine", the evidence supports "under about 5%". At second-line volume, that could be hundreds of wrong answers a month, each delivered with confidence.

**Why "it feels right" isn't enough.** In METR's early-2025 randomised trial, experienced developers took 19% longer with AI tools but believed AI had made them 20% faster. METR's later data suggest AI tools now speed developers up. The lasting lesson is that people's own sense of AI performance was off by about 40 points, so the decision should rest on measurement. [VERIFIED]

### Questions to put to the CTO

Frame these as help: you want to make the CTO's case strong enough for the board. If the agents are as good as claimed, a measurement is the CTO's best evidence.

1. What does "wrong" mean here, and how is severity graded?
2. What was the sample: how many tickets or releases, over what period, and from which categories?
3. Who checked the outputs, and did they know which answers came from the AI?
4. What is the error rate on second-line-type tickets specifically, as opposed to all tickets?
5. Which defects has QA caught in AI-written code over the last six months? What would have shipped without QA?
6. What happens to change failure rate and escaped defects if AI-written tests replace human QA sign-off?
7. How do the agents handle confidential data, prompt injection and policy exceptions such as refunds and goodwill credits?
8. What does the AI cost per resolved ticket, including human review time, and how does that grow with volume?

---

## 4. What the two teams do today, and what goes with them

| Function | What it does today | What replaces it under Option A | Gap to close |
|---|---|---|---|
| **QA (6)** | Catches defects before release, runs regression and exploratory testing, signs off releases, tests AI-written code | AI-generated tests plus developers doing their own testing | Who checks the AI's tests? When the same kind of model writes both the code and the tests, the two share blind spots. [ASSUMED, inference] DORA 2025 found that more change volume without strong automated testing and fast feedback leads to instability. [VERIFIED] In Veracode's 2025 tests, AI-written code introduced security flaws in 45% of cases. [VERIFIED] |
| **Second-line support (10 of 20)** | Handles escalations from first line and from the AI, complex multi-system issues, bug reproduction for engineering, customer-specific setups, judgement calls on refunds and exceptions | AI agents plus the remaining 10 engineers | The hardest cases fall on a team half the size. The company is liable for what its AI tells customers (Air Canada, 2024). [VERIFIED] When Commonwealth Bank cut its call centre, the union reported more overtime and managers answering phones. [VERIFIED, union claim] |

**Metrics to collect before the decision meeting (fill in):**

| Metric | Current value | Source |
|---|---|---|
| Defects caught by QA per release (by severity) | ___ | Defect tracker |
| Escaped defects per month; change failure rate | ___ | Incident log, CI/CD |
| Second-line ticket volume per week, by category | ___ | Helpdesk |
| Second-line 7-day reopen rate; time to resolution | ___ | Helpdesk |
| CSAT on second-line tickets | ___ | Helpdesk / survey |
| Share of second-line tickets escalated to engineering | ___ | Helpdesk / Jira |
| Customers or ARR touched by second-line tickets per quarter | ___ | CRM |
| AI cost per resolved ticket (including review time) | ___ | AI billing |

---

## 5. Options

Each option is rated for upside, downside, reversibility and second-order effects.

| | **A. Cut 16 roles now** | **B. Gate first, then cut to the evidence** (recommended) | **C. No cuts; AI absorbs growth** |
|---|---|---|---|
| What happens | 6 QA and 10 second-line roles exit at the end of month 1 | Freeze second-line backfills now, measure for 8 to 10 weeks, decide category by category in March 2027, redeploy and offer voluntary exits first | Keep the team, freeze backfills, move QA into AI evaluation, and let the AI handle volume growth without new hires |
| Upside | Fastest savings: about $1.08M net over 18 months if the claim holds | About $0.78M net over 18 months if the claim holds, so the same end state about 3 months later | About $0.23M of avoided hiring over 18 months. Lowest risk |
| Downside | If the claim fails, a likely partial reversal (about $0.37M net before customer damage), plus customer and incident losses that nobody would see coming | About $0.29M of delayed savings if the CTO is right. About $30k if the claim fails | No cut to the P&L. May not be enough if cost pressure is acute |
| Reversibility | Low. People, knowledge and trust are gone | High until the decision meeting, then the same as A for any roles cut | High |
| Second-order effects | Remaining staff get the hardest work and overtime, and good people leave. The CTO's credibility becomes tied to an unmeasured claim. The board will ask "how do we know?" | Builds an AI quality capability the company needs anyway. Gives the board evidence. Some uncertainty for staff while the measurement runs | Matches what most service organisations are doing. Gartner found only 20% have cut agent staffing because of AI, while 55% held staffing steady as volumes grew [VERIFIED] |

---

## 6. Financial model (illustrative)

### Assumptions [ASSUMED: replace with real figures]

| Input | Value |
|---|---|
| QA engineer, fully loaded | $100k a year (6 roles = $600k) |
| Second-line support engineer, fully loaded | $85k a year (10 roles = $850k) |
| Severance and notice | 3 months' cost (= $362.5k) |
| Legal, HR and outplacement | $50k one-off |
| Extra AI usage and tooling once AI absorbs the work | $150k a year |
| Work absorbed by developers and remaining staff | 2 FTE-equivalents at $125k = $250k a year |
| Rehire cost if roles come back | 35% of annual cost per role (recruiting plus ramp-up) |
| Reversal pattern (Option A, claim fails) | Half the roles (8) rehired from month 10 |
| Measurement cost (Option B) | $30k (tooling plus reviewer time) |
| Gross margin, for ARR equivalents | 75% |

### Results

| Scenario | Year-1 net | 18-month net | Run-rate after month 18 |
|---|---|---|---|
| A, claim holds | $550k | **$1,075k** | $1,050k a year |
| A, claim fails (half rehired from month 10) | $146k | **$371k** before customer damage | about $450k a year |
| B, gates pass (cuts take effect after month 4) | $258k | **$783k** | $1,050k a year |
| B, gates fail (no cut) | −$30k | **−$30k** | $0 |
| C, no cut (4 growth hires a year avoided) | $61k | **$229k** | about $435k a year in avoided cost |

**Sensitivity (A, claim holds):** if no extra work lands on others, the 18-month net is $1.43M. If 4 FTE-equivalents of work land on others, it is $0.72M. The work others absorb is the biggest swing factor after the claim itself. Have the CFO and the CTO estimate it together.

### Break-even: when does gating pay?

- On payroll alone, cutting now beats gating even when the cut is later reversed. Cutting now is ahead by about $0.4M in the bad case and $0.29M in the good case. **The case for gating rests on what AI mistakes cost when nobody is left to catch them.**
- Call the probability that a cut-first plan gets reversed *p*. Reference-class sources put it near 50% (section 10). Gating then comes out ahead once a bad year costs more than:

| Probability the cut fails (*p*) | Damage at which gating comes out ahead (gross profit) | Equivalent ARR at 75% margin |
|---|---|---|
| 25% | about $1.28M | about $1.7M |
| 50% | about $0.69M | about $0.9M |

- **For scale:** losing about $0.73M of ARR wipes out the first-year net saving of Option A. The average data breach cost $4.44M globally in 2025 ($10.22M in the US). [VERIFIED] One escaped security flaw in AI-written code can cost more than several years of the savings.
- **The question for the CFO:** would a year of thinner support and less-tested releases cost more than one or two mid-size customers? If the honest answer is "possibly", gate first.

**Left out of the model:** churn and SLA credits, incident and legal costs, attrition among the remaining staff, AI price changes, and the cost of rebuilding knowledge that leaves with experienced people.

---

## 7. Evidence gates (agree before measuring starts)

**Design rules**
- A neutral owner runs the measurement, outside both the CTO's and QA's reporting lines, for example the CFO's office or Customer Success.
- Graders are blind: they score AI and human answers without knowing which is which.
- Gates are written down and signed off by the CEO, CTO and CFO before the first sample is drawn.
- The baseline covers normal-volume weeks. The holiday period distorts ticket mix and release cadence.
- Gates apply per category. The AI may be excellent at configuration questions and poor at billing disputes, so the staffing decision can differ by category.

| Area | Metric | Example gate | Sample |
|---|---|---|---|
| Second-line support (shadow mode: AI drafts, humans send) | Severity-weighted error rate vs human baseline | AI no worse than human, 95% upper bound included | At least 300 tickets per major category |
| Second-line support | Critical errors (wrong policy or financial promise, data exposure) | **Zero** in the sample. Any critical error fails that category | Same |
| Second-line support (limited live segment after shadow mode) | 7-day reopen rate; CSAT | Reopen rate no higher than baseline; CSAT at least baseline minus 2 points | 4 weeks of live tickets |
| QA (AI-only QA running alongside human QA on 2 to 3 services) | Defects found by humans that the AI missed | No Sev-1 or Sev-2 misses, no missed security findings, low-severity misses below an agreed threshold per release | All releases in the window |
| QA | Change failure rate and escaped defects on pilot services | No worse than the trailing 6-month baseline | Pilot window |
| Security and confidentiality | Red-team test for data leakage and prompt injection | Zero leaks | Structured test set |
| Economics | AI cost per resolved ticket, including review time | Below the human cost per ticket | Billing plus time logs |

**Decision rules:** if every gate in a category passes, reduce that category to the staffing the AI has shown it can cover. If some gates pass, reduce only the categories that passed. If gates fail, make no reduction, fix the agents and retest next quarter. **A minimum QA and AI evaluation function stays in every scenario,** because someone has to keep checking the agents.

---

## 8. People plan

**Now**
- Do not announce cuts. Tell both teams plainly what is being measured, why, how it will be decided, and that redeployment comes first. Uncertainty pushes the best people out first. In Orgvue's survey, 34% of leaders said employees quit as a direct result of AI. [VERIFIED]
- The backfill freeze in second-line support is reversible. Lift it automatically if queue times or SLA breaches cross an agreed threshold.

**If the gates pass (in this order)**
1. **Redeploy.** Move QA people into AI evaluation and quality engineering: evaluation suites for the agents, red-teaming, and production quality monitoring. Move second-line people into knowledge-base and agent-training content, escalation quality review, or open roles elsewhere. Gartner found 42% of service organisations are hiring specialised AI roles. [VERIFIED]
2. **Voluntary exits** on fair terms.
3. **Compulsory redundancies only for any remaining gap.** Use a fair selection process, proper severance and outplacement support.

**Before any announcement:** the GC checks redundancy and collective-consultation rules for 16 roles in every jurisdiction where you employ people, including works council duties where they apply, and the rules on telling customers they are dealing with AI.

**If the gates fail:** QA becomes the AI quality team, second-line backfills resume, and the AI keeps absorbing volume growth (Option C).

---

## 9. Risk register

| Risk | Trigger | Mitigation | Owner |
|---|---|---|---|
| Measurement theatre | The builders or the affected team grade the AI | Neutral owner, blind grading, gates agreed in advance | CFO |
| Best people leave during the measurement | Rumours, silence | Open communication, a visible redeployment path, retention conversations with key engineers | CEO + HR |
| Service slips under the freeze | Queue times or SLA breaches above threshold | Automatic lift of the freeze | Head of Support |
| Customer-facing AI error with financial or legal effect | Wrong policy or refund promise, data exposure | Human approval on financial commitments, logging, a clear liability position | GC + Head of Support |
| Security flaw in AI-written code ships | QA thinned before evidence | Keep security testing in QA's scope in every scenario | CTO |
| Cost pressure is more urgent than this timeline | Runway under about 6 months | Rework the case around faster levers that keep error detection (vendor and contractor spend, AI spend review, hiring freeze across the company) | CEO + CFO |

---

## 10. Reference class (the outside view)

| Source | What happened | Lesson |
|---|---|---|
| Klarna (2024–2025) | Claimed its AI did the work of about 700 agents. In May 2025 its CEO said AI service was cheaper but "lower quality" and began investing in human support again | Cost-only evaluation missed quality |
| Commonwealth Bank of Australia (2025) | Cut 45 customer service roles for an AI chatbot, then reversed and said "The Bank was wrong". The union reported call volumes rose | Volume forecasts and the hard tail of cases were wrong |
| Orgvue survey (April 2025, 1,163 leaders) | 39% cut jobs because of AI. 55% of those say they made wrong decisions | Cut-first plans are often regretted |
| Forrester, Predictions 2026 (Oct 2025) | Expects about half of AI-attributed layoffs to be reversed, often offshore or at lower pay | Reversal is a common outcome |
| Gartner (June and Dec 2025) | Predicts 50% of organisations planning large service-headcount cuts will drop those plans by 2027. Only 20% have cut agent staffing because of AI | Augmentation is the norm |
| Moffatt v. Air Canada (Feb 2024) | The tribunal held the airline liable for its chatbot's wrong answer | The company owns the AI's mistakes |

---

## 11. Assumption register and confidence

| Finding | Status | Confidence |
|---|---|---|
| The rule-of-three sample sizes | VERIFIED (statistics) | High |
| External evidence (Veracode, DORA, CRMArena-Pro, METR, Gartner, Orgvue, Forrester, Klarna, CBA, Air Canada, IBM) | VERIFIED (sources below) | Medium. Studies and benchmarks are not your agents |
| Payroll, severance, AI cost, absorbed work, rehire pattern | ASSUMED | Low until the CFO replaces them |
| Reversal probability of about 50% | ASSUMED from the reference class | Medium |
| The AI's actual error rate on your second-line and QA work | **Unknown.** This is the gap the measurement closes | n/a |
| ARR, churn sensitivity, runway, jurisdictions | Not provided | n/a |

More than half of the company-specific inputs are assumptions. **Confidence in the method is high. Confidence in the figures is low until real data replaces the placeholders.**

**Not yet checked by:** the CFO (math with real payroll and ARR), an independent reviewer (the AI error data), the GC (redundancy and consultation law), HR (redeployment capacity and selection process).

### Critic screen (on this recommendation)

- **Weakest point:** if the CTO is right, Option B costs about $0.29M and a quarter of delay, and it may look like a lack of confidence in the CTO.
- **Missing perspective:** actual ARR, churn sensitivity and runway were not provided, so the break-even rests on placeholders.
- **If wrong, the cost is:** about $0.3M of delayed savings under B, against a likely partial reversal plus unmeasured customer and incident damage under A.
- **Proceed:** with the risks noted, once the CFO has put in real payroll and ARR.

---

## 12. Sources

- Veracode, GenAI Code Security Report (July 2025): https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
- Google Cloud, 2025 DORA State of AI-assisted Software Development: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Salesforce AI Research, CRMArena-Pro (May 2025): https://arxiv.org/abs/2505.18878
- METR, early-2025 developer study: https://metr.org/blog/2025-07-10-early-2025-AI-experienced-os-dev-study ; Feb 2026 update: https://metr.org/blog/2026-02-24-uplift-update/
- Gartner, 50% will abandon customer service workforce reduction plans (June 2025): https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai
- Gartner, only 20% report AI-driven headcount reduction (Dec 2025): https://www.gartner.com/en/newsroom/press-releases/2025-12-02-gartner-survey-finds-only-20-percent-of-customer-service-leaders-report-ai-driven-headcount-reduction
- Orgvue, 55% admit wrong redundancy decisions (April 2025): https://www.orgvue.com/news/55-of-businesses-admit-wrong-decisions-in-making-employees-redundant-when-bringing-ai-into-the-workforce/
- The Register on Forrester Predictions 2026 (Oct 2025): https://theregister.com/2025/10/29/forrester_ai_rehiring
- Entrepreneur on Klarna (May 2025): https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
- The Register on Commonwealth Bank (Aug 2025): https://www.theregister.com/2025/08/22/commonwealth_ban_chatbot_fail_rehiring/
- American Bar Association on Moffatt v. Air Canada (Feb 2024): https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/
- IBM, Cost of a Data Breach Report 2025: https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls
