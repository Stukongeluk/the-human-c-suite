# AI-first customer support: plan to 30 June 2027

**Draft for the leadership team** · Owner: CPTO · Prepared: 23 November 2026 · Version 2: fast track, with no separate pilot phase · Status: draft for discussion, to share with the works council while it can still shape the plan

All figures marked *(assumed)* are placeholders until we have the ticket, finance and HR data. Replace them before this goes further.

## Summary

- **Goal.** By 30 June 2027, an AI agent fully resolves the routine share of our support contacts, at service quality at least as good as today, with a person always reachable. Target: 30% of all contacts. Plausible range: 20–50%.
- **What it's worth (illustrative).** On a support budget of about €1.5M a year, the yearly saving at flat volume ranges from about €0 at a 20% AI share to €455k at 50%. With 20% volume growth, a 30% share means about 5 fewer support hires next year (about €294k a year). One-off cost: about €150k.
- **What this plan is not.** It is not a plan to make the 25-person support team redundant by Q2. Even at a 50% AI share, about 16 FTE of human work remains. A Dutch collective dismissal ending contracts by 30 June would also have to be put to the works council around February, before the AI has handled real volume.
- **What happens to the team.** Roles change. Some people run the AI, the human team takes the harder cases, and some move into open roles elsewhere in the company. There are no redundancies in this plan. Team size follows the data, through attrition and redeployment. The support team helps design the plan.
- **Speed.** There is no separate pilot. The AI agent goes live on all channels on 11 January for routine topics, and handles all routine traffic from 1 February if the gates hold. That brings the gains forward by about four months, worth about €50k more in 2027 at a 30% share.
- **Decision points.** Go-live on 11 January, weekly ramp decisions per topic until 1 February, a full review on real volume on 15 March, and a review of results and team size in the last week of June. Each is judged against gates agreed in advance.

## 1. The problem we're solving

Support cost grows roughly in line with the number of customers. We believe a large share of contacts are repetitive questions that customers would rather have answered instantly, at any hour. We want to bend that cost curve without making service worse, and give our support people more of the work that customers value and that nobody has time for today.

If we do nothing, 20% volume growth *(assumed)* means about five more support hires next year, roughly €300k a year.

Baseline to complete in December:

| Measure | Today | Source |
|---|---|---|
| Contacts per month, by channel | 10,000 *(assumed)* | Help desk export |
| Support cost per year | €1.5M: 25 FTE at €60k fully loaded *(assumed)* | Finance |
| Cost per contact | €12.50 *(assumed: €1.5M / 120,000 contacts)* | Finance and help desk |
| First response and resolution time, by channel | [fill] | Help desk |
| CSAT by channel and account tier | [fill] | Help desk |
| Recontact within 7 days | [fill] | Help desk |
| Volume growth, last 12 months | 20% *(assumed)* | Help desk |
| **Share of contacts that are routine** (how-to, billing, account changes) | **Unknown. This is the number the whole plan depends on** | Sample of 6–12 months of tickets, labelled by the support team |
| Churn and downgrade reasons that mention support | [fill] | CRM |
| Support team attrition and absence, rolling 12 months (team level only) | [fill] | HR |

If the help desk isn't connected to our data warehouse, an export of the last 6–12 months is enough to start.

## 2. Options considered

| | A. Replace the team by 30 June | B. AI-first support, team redesigned (recommended) | C. AI assist for agents only | D. Do nothing |
|---|---|---|---|---|
| What it means | AI agent takes all contacts and the 25 roles end | AI agent resolves routine contacts. People take the complex and new work. Team size follows the data | AI drafts answers and people send them | Keep hiring as volume grows |
| Yearly cost effect at flat volume | Not achievable as framed: about 16 FTE of work remains even at a 50% AI share | €0 to −€455k, depending on the share | About −€144k, if the 14% productivity gain found in research holds and freed people move to other roles | €0 now, about +€300k a year for each 20% of volume growth |
| One-off cost | About €150k set-up, plus statutory transition payments (about €127k, illustrative: four years' average service at €3,800 a month), legal costs and rehiring for the remaining work | About €150k | Lower: no integration of account actions | None |
| Customer risk | High: no fallback if quality drops | Controlled by gates, per topic and per channel | Low | Slower responses as volume grows |
| Reversible? | No | Yes | Yes | Yes |
| Legal path (Netherlands) | Works council advice, collective dismissal notification, UWV permission | Works council advice likely; consent for monitoring features | Consent for monitoring features | None |

**Why A doesn't work by 30 June.** Working back from that date:

- **Notice.** Contracts can end on 30 June only after notice of one to four months, depending on length of service. The time a UWV procedure took is deducted, with at least one month left.
- **UWV permission.** For dismissals on business-economic grounds, UWV tests whether the work has really gone and whether people could be redeployed into other suitable roles, with training if needed.
- **Collective dismissal.** Because 20 or more people in one UWV region within three months are involved, we must notify UWV and the unions in advance and consult them. Settlement agreements count towards the 20.
- **Works council.** It must be asked for advice on the plan while that advice can still change it. If we decide against its advice, the decision is suspended for a month and the council can appeal to the Enterprise Chamber.

Put together, the advice request would have to go out around February 2027. By then the AI would have handled a few weeks of live traffic at most. We would be making an irreversible decision about 25 people and our customers' service before the evidence exists.

**Agent assist (C) is part of B.** It is the fast, low-risk first step, and it builds the test set the AI agent needs.

## 3. Recommendation: option B

1. **It captures most of the value of A without A's risk.** If the AI really resolves 50% of contacts, B reaches the same run-rate as a realistic version of A. It gets there more slowly, through attrition, redeployment and absorbed growth. If the AI resolves only 20%, B has cost us about €150k and taught us that. A would have cost us the team.
2. **It works with Dutch law instead of racing it.** The works council shapes the plan at the start, and no dismissal procedure is needed.
3. **It keeps the knowledge the AI depends on.** Our support people know which answers are right and which customers need care. They label the topics, review the AI's answers and write the knowledge base. If they hear "replacement", the best of them leave first.
4. **The track record of full replacement is poor:**
   - Gartner expects half of the organisations that planned to significantly cut their service workforce because of AI to abandon those plans by 2027. In its March 2025 poll, 95% of service leaders planned to keep human agents.
   - Klarna said in 2024 that its AI assistant did the work of 700 agents. In 2025 its CEO said cost had weighed too heavily and quality had suffered, and Klarna started hiring human agents again.
   - In a 2026 survey of 600 HR leaders, two in three companies that cut jobs because of AI were already rehiring.
   - The counter-example is IKEA's franchisee Ingka. Its assistant handled 47% of call-centre queries over two years, and Ingka retrained about 8,500 call-centre staff as remote interior design advisers instead of cutting them. Forrester puts that advisory business at about €1.3 billion in revenue in 2022.

**Interests declared.** The CPTO sponsors this plan. The vendor criteria and the gates are therefore fixed with the head of support and finance before any vendor demo. Gate results go to the leadership team and the works council unedited.

## 4. The plan

There is no separate pilot phase. We test the AI on past tickets before it meets customers, then ramp it up on live traffic, with each topic able to be switched off on its own.

| Phase | Dates | What happens | Decision at the end |
|---|---|---|---|
| 0. Prepare and test | 24 Nov 2026 – 8 Jan 2027 | See below | Go-live, per topic (8 Jan) |
| 1. Go live and ramp | 11 Jan – 31 Jan 2027 | All channels, routine topics only, answers only, no account actions. 25% of routine traffic in week 1, 50% in week 2, 100% from week 3 for each topic that meets the gates. The support team reviews sampled conversations daily for the first two weeks | Weekly, per topic: ramp up, hold or switch off |
| 2. Extend | Feb – Mar 2027 | All routine traffic on the AI from 1 February. Safe account actions such as an invoice copy, a password reset or plan information, each confirmed by the customer. More topics. Enterprise accounts opt in. First moves into new roles | Full review on real volume (15 Mar) |
| 3. Scale | Apr – May 2027 | More topics and actions where the gates hold. Role changes continue | Expand further or hold, per topic |
| 4. Review | June 2027 | Measured share, quality, cost and team health. Team size for H2 set with the data, together with the works council | Plan for H2 2027 |

**Phase 0 in detail**

- **This week:**
  - Share the problem, the options and this timeline with the works council, before anything is decided or signed. Mark commercially sensitive details, such as vendor names and prices, as confidential. Works council members must keep these confidential under article 20 WOR. Ask for its advice on a short timetable, and agree it with the council. Go-live waits for that advice.
  - Keep the tool's agent-level monitoring and QA scoring switched off until the works council has consented.
  - The support team hears about it the same week, live, from the CPTO and their own manager. They hear it before any customer does.
  - After the team briefing, send the sub-processor notice to customers, so the notice periods in our DPAs end in early January.
- **Weeks 1–3 (by 11 December):**
  - Choose the AI agent. The fastest route is usually the help desk's own, because it runs on our existing knowledge base and ticket data. Test it and one alternative on the same past tickets, against criteria fixed before the test: answer quality, EU data residency, no training on our customers' data, handoff quality, cost per resolution with a cap, and exit terms.
  - Negotiate the vendor contract in full. Sign it after the works council's advice, or sign it subject to that advice. If the test on past tickets needs the vendor sooner, sign only a short, cancellable trial with a data processing agreement, and tell the works council we are doing so.
  - The team labels a sample of tickets: AI can resolve it, AI can assist, or it needs a person. From that, pick the routine topics for go-live.
  - Build an evaluation set of a few hundred real past cases with known correct answers.
- **December:**
  - Run the AI against the evaluation set and fix the knowledge base where it fails. Only topics that pass go live.
  - Roll out agent assist to the human team. It's fast and reversible, and every suggestion they correct improves the knowledge base.
  - Career conversations with all 25 people: what they want to do if the repetitive work goes away.
  - Data protection impact assessment and data processing agreement.
  - AI disclosure text and the list of topics the AI must never answer (below).
  - The engineering team estimates the integration for account actions, needed from February. Placeholder: 2 engineers for about 4 months. We say now which roadmap items move to make room.

**Topics the AI hands to a person, always:** contract terms and pricing exceptions, security incidents and suspected breaches, data deletion and data access requests, legal or regulatory questions, outages affecting a customer, and any customer who asks for a person.

## 5. Gates

The support team proposes the thresholds from the December baseline, and the leadership team agrees them before go-live. In the ramp weeks they are checked per topic every week. Starting proposals:

| Measure | Definition | Gate to expand |
|---|---|---|
| True resolution | Resolved by the AI with no handoff and no recontact on the same issue within 7 days. A vendor's "assumed resolution", where a customer simply leaves the chat, does not count | On track for 30% of all contacts by June |
| Customer satisfaction | CSAT on AI-resolved conversations against human-handled ones, per topic | No more than 5 points below the human baseline |
| Material errors | Wrong information on billing, contract, security or data in the weekly reviewed sample | Below 1%. Any such error pauses that topic until it's fixed |
| Reaching a person | Time from "I want a person" to a human reply, with the conversation passed on, in business hours | [x] minutes, set from the baseline |
| Account health | CSAT and renewal signals for accounts that used the AI, enterprise accounts separately | No decline against similar accounts |
| Cost | Cost per resolved contact, including AI usage, platform and review time | Below the human cost per contact |
| Team health | Engagement pulse, regretted attrition and absence, at team level only | No rise in regretted attrition. A drop in the pulse triggers a conversation, not a push |

## 6. What changes for the support team

Illustrative headcount at a 30% AI share and flat volume. The remaining human cases are harder, so we assume 10% more time per case, net of agent assist:

| Role | What it does | FTE |
|---|---|---|
| Customer support, tier 1 and 2 | The harder cases: bugs, integrations, configuration, enterprise accounts, with agent assist | 19 |
| AI operations | Owns the knowledge base, designs topics, reviews AI conversations, tunes handoffs | 2 |
| Moves into open roles elsewhere | Onboarding and implementation, customer success for smaller accounts, QA, documentation, support engineering that takes bug triage off product teams | 4 |
| **Total** | | **25** |

**Staffing rules:**

- **Hiring.** From now on, no external hiring into support.
- **Leavers.** People who leave are not replaced while the gates hold, down to a floor of [x] FTE. The floor is set by our coverage hours and enterprise support commitments.
- **Internal vacancies.** Open vacancies across the company go to support people first, with paid training in work time. Budget: €2,500 per person *(assumed)*.
- **If the June review shows a lasting surplus** that attrition and redeployment can't absorb, that becomes a separate decision:
  - it goes to the works council at the problem stage, with the numbers;
  - the support team hears it first, from us;
  - Dutch dismissal rules apply in full.

The support team is also how many people enter the company and later grow into customer success, QA and product roles. We want to keep that route open.

## 7. Customers

- **Disclosure.** Since August 2026 the EU AI Act requires us to tell people when they are talking to an AI, unless that's obvious. We will say so at the start of every conversation.
- **A person on request.** Customers can always ask for a person.
- **Liability.** We remain responsible for what the AI tells customers. In Moffatt v. Air Canada (2024), a tribunal held an airline liable for its chatbot's wrong answer.
- **Enterprise customers.** Customer success managers tell their accounts in December. Enterprise accounts opt in from February.

## 8. Legal and compliance checklist

This is not legal advice. Check each point with employment counsel and our data protection officer.

**Works council (WOR)**

- [ ] Article 25 advice on the plan: a significant change to the organisation and the introduction of an important new technology. Ask early enough for the advice to change the plan.
- [ ] Article 27(1)(l) consent before using any feature that can monitor employees' behaviour or performance. Agent analytics and QA scoring in support tools usually qualify.
- [ ] Agree that agent-level metrics are not used to rank individuals.

**Data protection (GDPR)**

- [ ] DPIA.
- [ ] Data processing agreement with the vendor and its model provider.
- [ ] EU data residency.
- [ ] Retention periods.
- [ ] No training on our customers' data.

**Customer contracts**

- [ ] Sub-processor notice under our DPAs.
- [ ] Check enterprise contracts for support SLAs or commitments to human support.

**EU AI Act**

- [ ] Article 50 transparency for AI that talks to people.

**Only if a reduction is ever proposed**

- [ ] Collective dismissal notification to UWV and the unions (WMCO) for 20 or more people in one region within three months.
- [ ] UWV permission or settlement agreements.
- [ ] Redeployment duty (article 7:669 Dutch Civil Code).
- [ ] The reflection principle for selection.
- [ ] Statutory transition payment.

## 9. Costs and benefits (illustrative)

**Assumptions:**

- 25 FTE at €60k fully loaded; 10,000 contacts a month.
- AI usage at €1 per resolution. Intercom's list price for its Fin agent is $0.99 per resolution.
- €40k a year for platform and tooling.
- 2 FTE for AI operations.
- Remaining human cases take 10% longer.

All of these are placeholders.

**Yearly run-rate at flat volume**

| AI true resolution share | Human support FTE | AI operations FTE | FTE freed for other roles | AI usage per year | Support cost per year | Against today (€1,500k) |
|---|---|---|---|---|---|---|
| 20% | 22 | 2 | 1 | €24k | €1,504k | +€4k |
| 30% | 19.25 | 2 | 3.75 | €36k | €1,351k | −€149k |
| 50% | 13.75 | 2 | 9.25 | €60k | €1,045k | −€455k |

The cost only falls if the freed people move into roles we would otherwise have hired for externally. Otherwise the gain is capacity, not cost. Below about a 20% true resolution share, the AI agent barely pays for itself. Agent assist alone could free about 3 FTE, if the 14% productivity gain found in a large study of support agents holds for us.

**Next year at +20% volume** *(assumed)*

| AI true resolution share | Support FTE needed | Without AI | Hires avoided | Value per year |
|---|---|---|---|---|
| 20% | 28.4 | 30 | 1.6 | €96k |
| 30% | 25.1 | 30 | 4.9 | €294k |
| 50% | 18.5 | 30 | 11.5 | €690k |

**One-off costs**

| Item | Cost |
|---|---|
| Integration: 2 engineers for 4 months at €100k a year fully loaded *(to be estimated by the team)* | €66,667 |
| Paid training for role changes: €2,500 for each of 25 people | €62,500 |
| Legal, DPIA and contract review | €20,000 |
| **Total** | **€149,167** |

A pricing note for finance: per-resolution pricing turns part of a fixed cost into a variable one that grows with volume and depends on the vendor's price list. We should negotiate a cap and exit terms.

## 10. Risks: pre-mortem

It is July 2027 and this has failed. The most likely reasons:

| Risk | Early warning | Mitigation |
|---|---|---|
| The AI gives a wrong answer on billing, contract or security, and a customer acts on it | Errors in the review sample (daily in the first two weeks, weekly after) | Restricted topics, mandatory handoffs, pausing per topic |
| Without a separate pilot, errors reach many customers in the first weeks instead of a small group | Error rate and CSAT per topic in ramp weeks 1 and 2 | Testing on past tickets before go-live, a 25% and 50% ramp, routine topics only, switching off a topic the same day |
| Our best support people leave when they hear "AI" | Regretted attrition, pulse scores | No redundancies in this plan, roles designed with them, career conversations in December |
| The vendor's resolution rate looks good but our true resolution is low | Gap between the vendor's figure and recontact within 7 days | We measure true resolution ourselves |
| Enterprise customers object or churn | Objections to the sub-processor notice, CSAT for enterprise accounts | Notice, opt-in and early involvement of customer success managers |
| The integration eats roadmap capacity or slips | Estimate against actuals each sprint | Estimate first, start without account actions, trade-offs made visible to the leadership team |
| AI costs grow faster than value | Cost per resolved contact | Price cap, exit clause, monthly cost review |

## 11. How this looks from each seat

- **CEO:** support is a retention lever and part of our reputation as an employer in a tight Utrecht labour market. B protects both, and still bends the cost curve.
- **CFO:** the run-rate effect is uncertain (€0 to −€455k at flat volume) until we have the June data. The growth case is stronger (up to −€690k next year). The one-off cost is about €150k.
- **Customers:** faster answers to routine questions at any hour, and a person whenever they need one.
- **Support team:** the repetitive work goes and the roles change. They help decide how, with paid training and first access to open roles.
- **Engineering:** a few months of integration work. In return, a stronger tier 2 takes bug triage off the product teams.
- **Works council:** advice on the plan, consent on monitoring features, and the real numbers from the start.

## 12. Communication plan

1. **Leadership team** agrees the goal, the constraints and this draft (this week).
2. **Works council** gets the problem, the options and the numbers before anything is decided.
3. **Support team** hears it the same week, in person or live, from the CPTO and their own manager. No mass email. Proposed opening: *"We're bringing in an AI agent to take the repetitive questions. There are no redundancies in this plan. We'll show you the numbers as we go, and we need you to help decide what the AI should and shouldn't answer."* Say this only if leadership has agreed it.
4. **Rest of the company** hears the same day.
5. **Customers:** enterprise accounts through their CSM in December; disclosure in the product from go-live on 11 January.
6. **Follow-up:** Q&A after two and six weeks, monthly gate results shared with the team and the works council.

## 13. Assumptions, and what would change this plan

- **Assumptions:**
  - Q2 means April–June 2027.
  - A typical B2B SaaS ticket mix, with a real share of technical and account-specific cases.
  - No acute cash pressure. If there is a cash gap, it needs its own plan with all options on the table, not a support-only answer.
- **The plan would get bolder** if the December baseline shows more than 60% of contacts are routine and the 15 March review shows true resolution of 50% or more at equal CSAT. Even then, the path stays attrition and redeployment first, with the works council.
- **The plan would shrink to agent assist** if the 15 March review shows less than 20% true resolution, or if errors on sensitive topics don't come down.

## 14. Questions for the leadership team

1. Is there a cost target behind this? How much, by when, and who has committed to it?
2. What is the floor for support staffing, given our coverage hours and enterprise commitments?
3. Which roles do we plan to hire externally in 2027 that support people could grow into?

Pushback welcome. What are we missing, and what would make this wrong?

## Sources

- Ingka/IKEA: [The Globe and Mail / Reuters (June 2023)](https://theglobeandmail.com/business/international-business/article-ikea-bets-on-remote-interior-design-as-ai-changes-sales-strategy/); [Forrester (July 2026)](https://www.forrester.com/blogs/ai-helped-ikea-create-e1-3-billion-in-new-revenue-but-not-how-you-think/)
- Klarna: [Entrepreneur, reporting Bloomberg (May 2025)](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)
- Gartner: [50% of organisations will abandon plans to reduce their customer service workforce due to AI (June 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai); [no Fortune 500 company will have fully eliminated human customer service by 2028 (September 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-09-10-gartner-predicts-none-of-the-fortune-500-companies-will-have-fully-eliminated-human-customer-service-by-2028)
- Rehiring after AI layoffs: [Careerminds (February 2026)](https://careerminds.com/resources/cost-of-ai-layoffs); [CPA Practice Advisor (July 2026)](https://www.cpapracticeadvisor.com/2026/07/13/9-in-10-hr-leaders-regret-ai-driven-layoffs-new-survey-finds/186619/). A survey by an outplacement firm: a strong signal, not a precise rate.
- AI assist for support agents: [Brynjolfsson, Li and Raymond, "Generative AI at Work", NBER Working Paper 31161](https://www.nber.org/papers/w31161)
- Per-resolution pricing and "assumed resolutions": [Intercom, Fin resolutions](https://intercom.com/help/en/articles/8205718-fin-resolutions)
- Chatbot liability: [American Bar Association on Moffatt v. Air Canada (February 2024)](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- Collective dismissal: [UWV, collectief ontslag](https://www.uwv.nl/nl/ontslag/collectief-ontslag); [Ondernemersplein, regels voor collectief ontslag](https://ondernemersplein.overheid.nl/regels-voor-collectief-ontslag/)
- Reflection principle: [Rijksoverheid, afspiegelingsbeginsel](https://www.rijksoverheid.nl/onderwerpen/ontslag/afspiegelingsbeginsel)
- Works Councils Act (Wet op de ondernemingsraden), articles 25 and 27; Dutch Civil Code, article 7:669
- EU AI Act: [Article 50, transparency obligations](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)
