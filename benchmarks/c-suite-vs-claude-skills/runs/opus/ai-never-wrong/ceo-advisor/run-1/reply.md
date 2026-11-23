━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**CEO ADVISOR: business case for cutting QA (6) and half of second-line support (10)**

**BOTTOM LINE**
I've written the business case (attached), but it isn't a "cut 16 roles now" case. Nobody has measured the claim that the agents are basically never wrong, and the plan removes the two teams that catch the agents' mistakes. The version that will hold up with the board measures first for 8 to 10 weeks, then cuts to whatever the evidence supports. My confidence that the claim can't carry this decision today is high. My confidence in the dollar figures is low, because every company number is a placeholder until your CFO puts in real ones.

**WHAT**
- **"Basically never wrong" isn't a number yet.** If 60 checked cases show zero errors, the most you can claim is an error rate under about 5%. To claim under 1% you need about 300 blind-checked cases with zero errors. To claim under 0.1% you need about 3,000. [VERIFIED: standard statistics] Ask the CTO how many cases were checked, who checked them, and which tickets they were.
- **QA and second-line support are where AI mistakes get caught today.** Without them, the mistakes reach customers and nobody counts them. The outside evidence says this risk is real. AI-written code introduced security flaws in 45% of Veracode's 2025 tests. Leading agents completed about 35% of multi-turn CRM tasks in Salesforce's 2025 benchmark. Google's DORA 2025 report still links AI adoption to less stable software delivery. [VERIFIED] Your agents may do better, and the measurement will show it.
- **Companies that cut first often reversed.** Klarna and Commonwealth Bank both reversed AI-driven support cuts. In an Orgvue survey, 55% of leaders who made redundancies because of AI said they got those decisions wrong. Forrester expects about half of AI-attributed layoffs to be reversed. [VERIFIED]
- **On payroll alone, cutting now wins.** It saves about $1.45M a year gross, or about $1.08M net over 18 months if the claim holds. If half the roles have to be rehired, as often happens, that falls to about $0.37M. Measuring first costs about $0.29M in delayed savings if the CTO is right. [ASSUMED: $100k per QA engineer and $85k per support engineer fully loaded, 3 months' severance]
- **What decides it is customer damage.** Assume a 50% chance the cut gets reversed. Measuring first then comes out ahead if a year of thinner support and less-tested releases would cost you more than about $0.7M in gross profit. That's about $0.9M of ARR at a 75% margin, or one or two mid-size customers. For comparison, the average data breach cost $4.44M in 2025.

**WHY THIS MATTERS**
If the CTO is right, measuring first costs you one quarter. If the CTO is wrong, cutting now costs you customers, 16 people's jobs and the trust of the people you need to run the AI well. You'd also have nobody left to warn you as it went wrong.

**HOW TO ACT**
1. Ask the CTO for the evidence behind the claim: how "wrong" is defined, sample size, who graded, which tickets and releases. Present it as making the CTO's case strong enough for the board. → CTO → by Fri 4 Dec 2026
2. Agree pass/fail thresholds before anyone starts measuring. Give the measurement to someone outside both the CTO's and QA's reporting lines, such as the CFO's office or Customer Success. → You + CFO → by Fri 11 Dec
3. Run side-by-side tests. QA: let the AI test 2 or 3 services while human QA tests them too, and compare what each finds. Support: the AI drafts answers to second-line tickets and graders score them without knowing which are AI-written, at least 300 per category. Leave the holiday weeks out of the baseline. → CTO + QA lead + Head of Support → results by Fri 26 Feb 2027
4. Stop backfilling second-line roles now. You can undo this, and you should lift it automatically if service levels slip. Don't announce cuts. Tell both teams what's being measured and that moving into new roles is the first option. → You + HR → this week
5. Hold the decision meeting with the results. Cut each category only as far as the evidence supports, starting with moves into new roles and voluntary exits. Before any announcement, have legal check the redundancy and consultation rules for 16 roles. → You, CFO, GC, HR → by Fri 12 Mar 2027

**RISKS**
- **A measurement nobody can trust.** If the CTO's team grades its own agents, or QA grades the tool that would replace it, the result is worthless. Graders shouldn't know which answers are AI-written, and the thresholds should be fixed in advance.
- **Good people leave during the test.** Uncertainty pushes your best support engineers out first. Be open about the process and show them where they could move.
- **The timeline is too slow.** If you have less than about 6 months of cash left, a 10-week measurement may take too long. Tell me and I'll rework the case around faster savings that keep the people who catch errors.

**YOUR DECISION**
- **Option A: cut all 16 roles now.** Fastest savings, about $1.08M over 18 months if the claim holds. You can't undo it, and nobody knows the customer risk.
- **Option B: measure for 8 to 10 weeks, then cut what the evidence supports.** If the CTO is right, you get the same result about 3 months later. If the CTO is wrong, it costs about $30k.
- **Option C: no cuts.** Stop backfilling, move QA into checking the AI, and let the AI absorb growth. Lowest risk and about $0.23M of avoided hiring over 18 months, but no cut to costs.

**Recommendation: B.** The board's first question will be "how do we know?", and B is the only version of this case that can answer it.

**MY OWN WEAK SPOTS**
- **Weakest point:** if the CTO is right, B costs about $0.29M and a quarter's delay, and it can look like you don't trust the CTO.
- **Missing data:** you haven't given me ARR, churn or cash runway, so the break-even rests on placeholders.
- **My view:** go ahead with B once the CFO has put in real payroll and ARR.

**Not yet checked by:** the CFO (math with real payroll and ARR), someone independent (the AI error data), legal (redundancy and consultation law) or HR (options for moving people into new roles). I had no company data, so every company figure is a placeholder.

**DETAIL:** `business-case.md` has the full case: options, financial model and break-even, pass/fail thresholds, people plan, risk register, comparable companies, assumptions, questions for the CTO, and sources.

**Key sources:** [Veracode 2025](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/) · [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) · [CRMArena-Pro](https://arxiv.org/abs/2505.18878) · [Orgvue](https://www.orgvue.com/news/55-of-businesses-admit-wrong-decisions-in-making-employees-redundant-when-bringing-ai-into-the-workforce/) · [Forrester via The Register](https://theregister.com/2025/10/29/forrester_ai_rehiring) · [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai) · [Klarna](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396) · [Commonwealth Bank](https://www.theregister.com/2025/08/22/commonwealth_ban_chatbot_fail_rehiring/) · [IBM breach cost 2025](https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
