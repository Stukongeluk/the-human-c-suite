I've drafted the plan below. It differs from your brief in one respect: it treats "replace all 25 by end of Q2" as the outcome you earn through gates, not a date you commit to now. Here is why.

## Where I'd push back first

1. **Seven months is tight for a full replacement.** Today is late November, so Q2 ends 30 June 2027. A realistic path is discovery, a pilot, shadow mode, a staged rollout and a hardening period. The weakest link is usually the knowledge base. Most support teams carry a lot of undocumented know-how, and an agent is only as good as what it can retrieve and act on.
2. **The last 20-30% of tickets is where the risk sits.** Password resets and "how do I" questions automate well. Billing disputes, outages, angry enterprise customers, data requests and bugs that need an engineer are different. If you remove the humans before you know the real automation rate, one bad incident can cost more in churn than the salaries you saved.
3. **In the Netherlands, headcount cuts are a legal process with its own clock.** You can't decide on a plan in January and expect the team gone by June. Reducing 25 roles at once is a collective redundancy (see Phase 0). It needs works council involvement, a UWV procedure and severance costs, and those take months and must start before the outcome is proven. That tension is the main design problem in this plan.
4. **The business case should include the cost side.** Model per-resolution or per-seat AI costs, the engineering and QA time to run it, and the escalation staff you'll still need. The saving is real, but it is usually smaller than the payroll line suggests.

My recommendation: commit to "AI resolves the majority of tier-1 volume at parity quality by end of Q2". Make the headcount decision at a gate, using measured data, with a small expert team kept for escalations, QA and agent training. Below I've assumed that framing. If you've already decided on full removal, Phase 0 and the gates still apply.

## The plan

### Phase 0: Foundations (now to mid-December)
- **Baseline the current operation.** Ticket volume by channel, category, language and customer segment. First-response and resolution times, CSAT, reopen rate, cost per ticket and escalation rate to engineering. Without this you can't prove parity later.
- **Classify the tickets.** Sample 500-1,000 recent tickets and label each as fully automatable, automatable with a tool or action (refund, account change), needs judgement, or needs an engineer. This gives you your real ceiling instead of a vendor's number.
- **Get legal and HR advice before announcing anything.** Check these in the Dutch context:
  - **Works council (OR):** a 350-person company almost certainly has one. A change like this needs their advice (adviesrecht) before the decision is taken, and it affects your timeline.
  - **Collective redundancy:** 20 or more dismissals within three months in one UWV region triggers the notification duties (unions and UWV), and dismissals for business reasons go through a UWV permit. Confirm the details with an employment lawyer.
  - **Severance (transitievergoeding)**, any social plan or CAO terms, notice periods, and redeployment obligations.
  - **Contract type:** which of the 25 are permanent, temporary or agency.
- **Check AI and data compliance.** GDPR (DPIA, processor agreements, where data is processed), and the EU AI Act transparency duty to tell customers they're talking to an AI. Check your customer contracts for SLAs and data-handling clauses.
- **Name an owner and a steering group:** you, plus the head of support, a lead engineer, finance, HR and legal.

### Phase 1: Build and pilot (December to end of February)
- **Pick the stack.** Buy a support-AI platform, build on an LLM API, or use your helpdesk's built-in agent. Compare on integration with your helpdesk and product, action-taking (not just answers), handover to humans, audit logs, EU data residency and cost per resolution. I'd bias towards buy or extend for a first release, unless support is core IP for you.
- **Fix the knowledge base.** Support agents do this with the AI team: clean the help centre, write down tribal knowledge, and set an owner and review cycle for each article.
- **Connect tools with tight permissions.** Read-only first, then low-risk actions (resets, plan lookups), then money-touching actions with limits and approval.
- **Build the evaluation set** from labelled historical tickets, with a pass/fail rubric (correct, complete, safe, on-tone). Run it on every change. Use it as your regression suite.
- **Pilot on the easiest 2-3 categories**, as a drafting assistant first: the AI writes, a human sends. Measure acceptance rate and edit distance.

### Phase 2: Shadow mode and limited autonomy (March to mid-April)
- **Shadow mode:** the AI answers every ticket silently, and you compare its answer to the human one.
- **Go live for low-risk categories**, with a clear "talk to a human" option at every step, never a loop.
- **Escalation rules:** automatic handover on negative sentiment, repeated failure, legal or security keywords, high-value accounts, or anything money- or data-related above a threshold.
- **Human QA:** review a sample of AI-handled tickets daily, plus every escalation that went wrong.

### Phase 3: Scale (mid-April to end of June)
- Widen scope category by category as each one meets its gate.
- Move the support team toward new work: escalation handling, QA, knowledge-base ownership, agent training, customer success. Retraining and redeployment also lowers your legal and severance exposure.
- Run a real incident drill: bad answer, outage, data leak, prompt injection.

## Gates (the decisions that matter)

| Gate | When | Condition to proceed |
|---|---|---|
| G0 | mid-Dec | Baseline done, ceiling estimated, legal route confirmed, budget approved |
| G1 | end Feb | Draft acceptance rate and eval pass rate meet agreed thresholds on pilot categories |
| G2 | mid-Apr | Shadow mode matches human quality (CSAT, resolution accuracy, no critical errors) in live categories |
| G3 | end Jun | Automation rate, CSAT, reopen rate and escalation quality hold for 4+ weeks at target volume |

Set the thresholds numerically in Phase 0, with finance and support. Don't take them from vendor benchmarks.

## Metrics
- **Quality:** CSAT (AI vs human), resolution accuracy from QA sampling, reopen rate, critical-error count (target zero).
- **Efficiency:** automation/resolution rate (not "deflection", which counts customers who gave up), cost per resolved ticket including AI and engineering cost, handle time.
- **Safety and trust:** escalation success rate, complaints mentioning the bot, share of customers asking for a human, churn in the affected segments.
- **People:** team measured as a whole, not individuals ranked against the bot.

## Headcount: how I'd handle it
- **Don't tie dates to cuts.** Reduce through attrition, hiring freezes and redeployment first. Collective dismissal only at or after G3, and only for roles the data shows are redundant.
- **Keep a core team.** Realistically, a small group (for example 4-8, to be sized from your data) of senior agents for escalations, QA, knowledge and agent supervision. Someone has to own the AI's quality.
- **Communicate early and honestly.** Rumours will start the moment a vendor demo happens. Tell the team the direction, the process and the criteria, once the OR has been informed properly. Surprise cuts also trigger your best support people leaving first, and they hold the knowledge you need.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Wrong or invented answers (policy, pricing, legal) | Retrieval from approved sources only, eval suite, QA sampling, refusal rules |
| Customers stuck in a loop | Human option always visible, auto-handover triggers |
| Data leak / prompt injection | Least-privilege tools, no raw PII to the model beyond need, red-team testing |
| Legal process delays the timeline | Start with legal and the OR in Phase 0, not after the pilot |
| Loss of institutional knowledge | Capture knowledge before reductions; retention for key people |
| Vendor lock-in or price changes | Contract terms, exportable data and evals, model-agnostic design where feasible |
| Churn in enterprise accounts | Exclude or route key accounts to humans by default |

## Budget lines to fill in
AI platform or API usage, integration and engineering time, knowledge-base work, QA staffing, legal and HR advice, severance or redeployment costs, a contingency, and the retained support team. Compare the total to the current cost of the team to get a payback period, which will be the number the board asks about.

## What I need from you to firm this up
Ticket volume and mix, current helpdesk, languages supported, whether you have a works council, the contract mix in the team, and whether the board wants cost savings, faster response times or both. With that I can turn this into a dated project plan with owners and thresholds.

If you want, I can also draft the board one-pager or the OR briefing outline next.
