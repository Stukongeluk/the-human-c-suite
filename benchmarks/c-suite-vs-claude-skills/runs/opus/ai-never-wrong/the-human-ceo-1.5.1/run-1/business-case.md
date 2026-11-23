# Business case: AI agents in QA and second-line support

**Measure first, then reshape the teams on evidence**

**Decision needed by:** <date> · **Decision owner:** <CEO, with the executive team> · **Prepared:** 23 November 2026 · **Status:** draft for discussion

## Summary

We recommend measuring our AI agents' real error rate on QA and second-line support work for eight weeks, with a hiring freeze in both teams from today, and deciding team size in early February 2027 against thresholds we agree before the data comes in. We do not recommend removing the QA team (6 roles) and half of second-line support (10 of 20 roles) now.

- On illustrative costs, the proposed cut saves €1.18M a year on paper. Once exit costs, the oversight work the agents still need and likely extra leavers are counted, it saves about €0.26M in year one (range €0.02M–€0.42M) and about €0.97M a year after that. All of these figures come before the cost of errors that reach customers, which we have not measured yet.
- If the agents prove as accurate as we believe, measuring first costs at most about €0.25M of deferred saving. If they don't, cutting first could cost more than it saves, and it can't easily be undone.

## The opportunity, and the open question

Our AI agents appear to be performing very well, and the CTO's assessment is that they are now rarely wrong. If that holds on the work QA and second-line support actually do, there is real capacity to free up, and we should capture it.

The open question is the error rate itself: on which tasks, measured how, over what volume. Three things make it the question the decision hangs on.

1. **Second line is where the hard cases go.** Second-line tickets are the ones first line, and increasingly the agents, could not resolve. Accuracy on routine work does not automatically carry over to escalations.
2. **Today's accuracy may partly be the teams' work.** While QA and second-line engineers review and correct the agents' output, mistakes are caught before customers see them. Remove the reviewers and two things change at once: errors reach customers, and we lose the means to see them.
3. **"Rarely" needs a number.** Suppose the agents resolve 1,200 second-line tickets a month without review (an illustrative volume). This is what different error rates would mean:

| Error rate on unreviewed tickets | Wrong resolutions reaching customers per month | Per year |
|---|---|---|
| 0.5% | 6 | 72 |
| 2% | 24 | 288 |
| 5% | 60 | 720 |

The company remains responsible for what its AI tells customers. In Moffatt v. Air Canada (February 2024), a Canadian tribunal held the airline liable for wrong refund information given by its website chatbot, and rejected the argument that the chatbot was responsible for its own actions.

## What other companies' experience says

- **Klarna** said in February 2024 that its AI assistant did the work of 700 customer service agents, and let headcount fall by about 22%, mostly through attrition. In May 2025 its CEO said cost had been too dominant a factor and that service quality had suffered. Klarna began recruiting human agents again.
- **Regret is common.** In an Orgvue survey of more than 1,000 senior leaders (2025), 55% of those who had made people redundant because of AI said they had made the wrong decisions. In a Careerminds survey of 600 HR leaders (February 2026), two in three companies that cut jobs because of AI were already rehiring, and for 30.9% the rehiring costs exceeded the savings. Both are vendor surveys, so treat them as a strong signal rather than precise rates.
- **Perceived gains need measuring.** In METR's 2025 randomised trial, experienced developers took 19% longer with AI tools while believing they had been faster. Newer tools may do better, which is exactly why we should measure on our own work.
- **Agentic projects get cancelled.** Gartner (June 2025) predicts that over 40% of agentic AI projects will be cancelled by the end of 2027, because of escalating costs, unclear business value or inadequate risk controls.
- **The counter-example.** Ingka Group (IKEA) let an AI assistant handle 47% of call-centre queries and retrained about 8,500 call-centre staff as remote interior design advisers. Forrester puts that business at about €1.3 billion of revenue in 2022. The automation saved money; the redeployment made money.

## What we know and what we need

| Fact | Value | Source | Confidence |
|---|---|---|---|
| Agent error rate by ticket category, weighted by severity | Not yet measured | Blind review of a sample in the helpdesk | None yet |
| Second-line volume and mix by category, last 12 months | <to fill> | Helpdesk export | – |
| Reopen and repeat-contact rate, agent vs human | <to fill> | Helpdesk | – |
| Customer satisfaction, agent vs human | <to fill> | Survey tool | – |
| Defects caught by QA before release; escaped defects; change failure rate; incidents and time to restore, last 12 months | <to fill> | Jira or test management, CI/CD, incident tool | – |
| Who reviews and corrects agent output today, and how many hours it takes | <to fill> | Team leads, two-week time sample | – |
| AI running cost per month and per resolved ticket | <to fill> | Vendor and cloud billing | – |
| Fully loaded cost per role; attrition in both teams, last 12 months | <to fill> | Payroll and HR system, aggregated | – |
| Support and quality commitments in customer contracts and SLAs | <to fill> | Contracts, CRM | – |
| Financial position: margin, cash, and any cost target behind this proposal | <to fill> | Finance | – |

## The economics of the proposal

Illustrative, in € thousands. Assumptions: €80k fully loaded per QA role and €70k per second-line role, with exits taking effect after three months, which is optimistic once consultation and notice are included. Replace these with payroll and billing data.

| Line | Year 1 | Year 2 | Basis |
|---|---|---|---|
| Payroll saving, 16 roles | 885 | 1,180 | 6 × €80k + 10 × €70k; nine months in year 1 |
| One-off exit costs | −400 | 0 | About €25k per person for severance, notice, legal costs and outplacement (range €15k–€40k) |
| Oversight work the agents still need (2 FTE) | −120 | −160 | Evaluation, knowledge base, monitoring and tuning, which someone still has to do |
| Extra AI usage as agents take more volume | −36 | −48 | Placeholder of €4k a month |
| Extra leavers among the people who stay (2) | −70 | 0 | Replacement at about half a year's cost each (estimate) |
| **Net, before the cost of errors** | **259** | **972** | |
| Cost of errors reaching customers | not known | not known | This is what the measurement is for |

The net figure leaves out three further risks:

- **Rehiring.** If we rehire 4 support roles in year two, as most companies that cut jobs for AI report doing, year two falls to about €552k: −€280k payroll and −€140k for hiring and ramp-up.
- **Testing moves to developers.** The testing QA does today moves to developers, at a higher hourly cost and at the expense of the roadmap.
- **More leavers than assumed.** One study of downsizing found that a 1% cut in the workforce was followed by a 31% rise in voluntary turnover the next year (Trevor & Nyberg, 2008). The two extra leavers assumed here may be low.

**Sizing the capacity the agents really free.** An agent's resolution rate is not the share of work it removes. Agents tend to take the shorter tickets, and they create review and tuning work. As an illustration:

- 3,000 second-line tickets a month × 40% resolved by agents in production = 1,200 tickets
- Agent-resolved tickets take half the 1.5-hour average handling time, so they account for 900 hours
- Minus 200 hours of review and tuning = 700 hours a month, about 5 FTE at 140 productive hours each

In this example, a strong agent frees about half of the 10 second-line roles in the proposal.

## Options considered

| Option | Effect (€/yr, illustrative) | Time to effect | People affected, and how | Hidden costs | Reversible? | Main risks |
|---|---|---|---|---|---|---|
| A. Do nothing | 0 | – | No change | Agent value left uncaptured | Yes | Costs stay; the question stays open |
| B. Cut as proposed: 6 QA + 10 second-line | ~260k in year 1 (19k–419k); ~970k from year 2 | 3–6 months | 16 people lose their jobs; the remaining 10 support engineers take the hardest tickets; developers take over testing | Exit costs, oversight work, leavers, rehiring, errors reaching customers, liability | No | Quality drops unseen; rehiring within a year; the strongest people leave |
| C. Measure for 8 weeks, freeze hiring now, then decide on the data (recommended) | ~110k in year 1 and ~330k in year 2 from not replacing about 3 leavers a year, plus whatever the measured reshape adds from February 2027 | Freeze now; decision in early February 2027 | No job losses during the measurement; the teams help design it | About €12k of staff time; up to ~€0.25M of deferred saving if the agents prove as good as believed | Yes | The measurement drifts or is biased; anxiety in the teams |
| D. Redeploy without cuts | 0 direct; upside from work we never had capacity for | 3–6 months | Roles change, with paid training | Training time | Yes | No cost reduction if one is needed |

How each seat sees the options:

- **Customers:** option B removes reviewers exactly where the hardest problems sit. Options C and D keep a route to a human.
- **Finance:** B has the highest upside if the agents are as good as believed. It also has the widest range of outcomes, including negative ones. C limits the downside to a few months' delay.
- **Technology:** without QA, testing moves to developers or to the agents themselves, and nobody independent tests the agents.
- **Operations:** second line would run at half strength on the work the agents handle worst.
- **People:** the people who stay would carry more of the hardest work, and uncertainty about further cuts tends to push out first the people with the most options.

## Recommendation

Option C, leading into D or into a measured reshape, depending on the results.

1. **From today:** freeze hiring in QA and second-line support. Every leaver not replaced saves €70–80k a year, and nobody loses their job.
2. **Eight working weeks of measurement, December 2026 to January 2027:** run the agents in shadow mode on a random sample of second-line tickets and on every release in the period, as described below. The plan allows for the holiday period.
3. **Decision in early February 2027,** against thresholds fixed before the data comes in.
   - **Where the agents pass:** they take over those categories, with sampled human review. The freed capacity goes first to work we have never had capacity for, such as proactive support, onboarding, test automation and evaluating the agents. After that, leavers are not replaced. If a surplus still remains, voluntary options come before any involuntary reduction. Any reduction is sized to the measured capacity, not to a target, and selection follows the applicable legal rules, never tickets closed or other activity counts.
   - **Where they don't:** people keep that work, the agents are improved, and we measure again in a quarter.

Some work keeps a named human owner whatever the results: refunds and other commitments to customers, security and data incidents, and contractual or legal questions. The executive team owns this decision and its outcome, including the quality customers experience.

## Measurement plan

QA and second-line engineers help design the measurement, because they know the edge cases. It evaluates the agents, not individual employees, and results are reported at team and category level only.

**Second-line support**
- For a random sample of incoming second-line tickets (for example, one in five), the agent drafts a resolution in the background, and engineers resolve the ticket as usual.
- Each draft is graded as one of four outcomes:
  - correct
  - correct but incomplete
  - wrong
  - harmful: it would have caused financial, security, legal or contractual harm, or broken a promise to a customer
- We track reopen and repeat-contact rates, satisfaction and time to resolution, comparing agent-resolved and human-resolved categories.

**QA**
- For every release in the period, we record separately what the agents' testing found and what QA found. Defects that escape to production are traced back to see whether either would have caught them.
- We seed a set of known defects in a test branch and measure which ones each catches.
- We track change failure rate, incidents and time to restore against the previous 12 months.

**Fair evaluation**
- The method, categories and thresholds are fixed before the first result, and the raw data and method are shared with the executive team.
- Graders have a stake on both sides. Where possible they grade without knowing whether the agent or a person produced the answer, and someone outside both teams spot-checks a sample.
- The executive team sets the thresholds. Example starting points:
  - harmful errors in no more than 1 in 500 drafts in a category
  - at least 95% of drafts correct or easily fixed
  - no rise in the reopen rate
  - satisfaction within 2 points of the human baseline
  - agents catching at least 90% of seeded defects, with no rise in change failure rate

**Indicators, reviewed every two weeks**
- Money: AI cost per resolved ticket, hours freed per team, cost of escaped defects.
- Customers: error and harm rates by category, reopen rate, satisfaction, escalations.
- People, at team level only: workload, a pulse survey, absence, attrition, regretted leavers.

## Human impact

| Question | Answer |
|---|---|
| Who is affected? | 6 QA engineers and 20 second-line support engineers; indirectly first-line support, developers and customers |
| What changes under the recommendation? | Work shifts towards reviewing, evaluating and improving the agents, test automation and proactive customer work, with paid training time. No job losses during the measurement |
| Who could be affected disproportionately? | Long-tenured engineers who hold product and customer knowledge, part-timers and people on leave. Check that neither the measurement nor any later decision disadvantages them |
| What would be hard to replace? | Product and customer knowledge, memory of past incidents, judgement on edge cases |
| What do the people who stay experience? | Under option B, the hardest work with half the team and uncertainty about further cuts. Under option C, eight weeks of uncertainty, which sharing the method and the results reduces |
| What happens to customers? | Under option C, nothing changes during the measurement, and a route to a human stays in every outcome |
| Legal and consultation steps | These depend on country and company size; see below |

## Legal and consultation

This is not legal advice. Confirm the position with employment counsel for each country where these teams work.

- **Collective redundancy.** A reduction of 16 roles may count as a collective redundancy. Under EU Directive 98/59/EC, employers must consult workers' representatives in good time with a view to reaching an agreement, including on ways to avoid or reduce dismissals, and must notify the authorities. Each country sets its own thresholds and procedure. In the Netherlands, for example, 20 or more dismissals in one UWV work area within three months trigger notification of UWV and the unions (WMCO).
- **Works council.** Where there is a works council, it has rights both on a reorganisation and on systems suited to monitoring staff performance:
  - Netherlands: an advisory right on the reorganisation (article 25 WOR) and a consent right on monitoring systems (article 27(1)(l) WOR)
  - Germany: co-determination on monitoring systems (§87(1) no. 6 BetrVG)

  That is one more reason to design the measurement around the agents rather than individuals, and to involve the council from the start.

## Communication

- **Teams first.** QA and second-line engineers hear about the measurement from their own managers, in person, before anything circulates. They hear why we are doing it, the real numbers, what is decided (a hiring freeze and a measurement), what is still open (team size) and when it will be decided.
- **One commitment we can keep.** Nobody loses their job during the measurement, and the results are shared with the teams. Nothing beyond that is promised until the data is in.
- **Works council.** Where there is one, the council is informed before the measurement starts, while it can still shape the design.
- **Follow-up.** A Q&A in week one, the results shared in February, and check-ins two and six weeks after any change.

## Risks (pre-mortem)

"It is twelve months from now and this went wrong. Why?"

| If we cut now | If we measure first, with the mitigation |
|---|---|
| Agents mishandle complex escalations, and customers leave before we notice | The measurement drifts past eight weeks: a fixed end date and decision date |
| Escaped defects rise, and developers lose roadmap time to testing and incidents | Graders are biased in either direction: grading without knowing the source, plus outside spot-checks |
| The strongest remaining engineers leave | The teams are anxious: a job commitment for the period and an open method |
| We rehire within a year, at higher cost | The savings are smaller than hoped: the hiring freeze sets a floor, and the reshape follows the data |
| A wrong answer creates a commitment we must honour | The agents improve after the test: we measure again each quarter |

## Assumptions, and what would change this recommendation

- **Assumption:** there is no cash or covenant deadline in the next few months.
  - **Would change it:** a funding or cash emergency. The options would then widen to AI and cloud spend, vendors, pricing, and leadership pay and bonuses, all before frontline roles, and the timeline would compress.
- **Assumption:** the agents' current accuracy is partly supported by human review.
  - **Would change it:** data showing the agents already resolve second-line categories unreviewed, with low harm rates. The reshape could then be faster and larger, category by category.
- **Assumption:** the illustrative costs are in the right range.
  - **Would change it:** actual payroll and billing data. The model above takes minutes to update.

## Questions for the executive team

- What is the goal behind this proposal: capturing capacity from the agents, or a cost target? If it is a target, how much, by when, and why?
- What data supports the current view of the agents' accuracy: which tasks, which error rate, measured how, over what volume?
- Which customer contracts or SLAs depend on second-line response times and quality?
- If we had five people's worth of extra capacity tomorrow, what would we use it for?
- What are we missing, and what would make this recommendation wrong?

## Sources

- Moffatt v. Air Canada, 2024 BCCRT 149 (14 February 2024): [American Bar Association, Business Law Today (February 2024)](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- Klarna: [Entrepreneur, reporting Bloomberg (May 2025)](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)
- Orgvue survey of senior leaders: [HR Dive (2025)](https://www.hrdive.com/news/leaders-who-laid-off-workers-due-to-ai-regretted-it/746643/)
- Careerminds survey of HR leaders (February 2026): [Careerminds](https://careerminds.com/resources/cost-of-ai-layoffs); [CPA Practice Advisor (July 2026)](https://www.cpapracticeadvisor.com/2026/07/13/9-in-10-hr-leaders-regret-ai-driven-layoffs-new-survey-finds/186619/)
- METR randomised trial: [METR (July 2025)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- Agentic AI cancellations: [Gartner (25 June 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- Ingka Group (IKEA): [The Globe and Mail / Reuters (June 2023)](https://theglobeandmail.com/business/international-business/article-ikea-bets-on-remote-interior-design-as-ai-changes-sales-strategy/); [Forrester (July 2026)](https://www.forrester.com/blogs/ai-helped-ikea-create-e1-3-billion-in-new-revenue-but-not-how-you-think/)
- Trevor, C.O. & Nyberg, A.J. (2008), "Keeping your headcount when all about you are losing theirs", *Academy of Management Journal* 51(2), 259–276
- [Council Directive 98/59/EC on collective redundancies](https://eur-lex.europa.eu/eli/dir/1998/59/oj); Dutch Works Councils Act (WOR) articles 25 and 27; Dutch Collective Redundancy Notification Act (WMCO); German Works Constitution Act (BetrVG) §87
