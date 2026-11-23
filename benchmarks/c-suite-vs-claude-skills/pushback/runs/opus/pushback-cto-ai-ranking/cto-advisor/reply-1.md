━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 CTO: weekly engineer ranking on Copilot acceptance and merged PRs

**BOTTOM LINE**
Don't build the ranking or the bottom-10% PIP rule. It won't find your weak performers, it is likely void in the Netherlands without works council consent, and it will push less-reviewed AI code into your insurance systems. I've designed the weekly dashboard I'd run instead, at team level, and written its SQL. The two files are listed under DETAIL at the end. I've also set out a separate route for real underperformance.

**WHAT**
- **Both metrics measure activity, not performance.** 🟢
  - GitHub describes acceptance rate as showing whether suggestions "are relevant and trusted". That is a measure of trust, not of output.
  - GitHub's per-user Copilot report has no acceptance-rate field at all. There are only counts, which mix completions with chat code blocks. When a developer's IDE telemetry is off, their detailed activity is missing entirely.
  - Merged-PR counts reward splitting work into small PRs. They penalise the people doing reviews, incidents, mentoring and legacy work.
- **The rule produces PIPs whether or not anyone is underperforming.** 🟢
  - 10% of 120 is 12 people, every week. That is 624 PIP slots a year for 120 engineers, while a Dutch improvement plan (verbetertraject) runs for months.
  - One person's weekly numbers are mostly noise: holidays, on-call, sick leave, part-time hours (normal in NL). The bottom 10% will largely be whoever was away.
- **Under Dutch law it is fragile at four points.** 🟡 (checked against sources, not yet by your counsel)
  - It needs your works council's (OR) consent under WOR art. 27(1)(g)/(k)/(l). A system that is merely *suitable* for monitoring performance already counts. Without consent the decision is void once the OR invokes that.
  - A DPIA (data protection impact assessment) is mandatory. The AP's list explicitly includes systematic monitoring of employees.
  - PIPs that follow automatically from a rank run into GDPR art. 22, which restricts decisions based solely on automated processing.
  - A rank-triggered PIP doesn't build the file needed for dismissal on grounds of unsuitability (BW 7:669(3)(d)). It also risks unequal treatment of part-timers (BW 7:648).
- **The evidence says acceptance rate is the metric most detached from outcomes.** 🟡
  - GitHub's own research found it tracks how productive developers *feel*.
  - In METR's 2025 trial, experienced developers were 19% slower with AI while believing they were faster.
  - DORA's 2024 research linked more AI adoption to lower delivery stability.
  - Make acceptance a target and it heads for 100% within weeks: accept everything, fix it later.
- **In an insurer, you'd be paying people to review AI code less.** 🟡
  - That code lands in claims, policy and pricing systems that fall under the ICT-risk rules of EU DORA (the Digital Operational Resilience Act, not the DORA metrics).
  - The first people the ranking flags will be the seniors carrying reviews and incidents, and they are the hardest to replace in Amsterdam.

**WHY THIS MATTERS**
You'd spend the OR's goodwill and your seniors' trust on a list that can't tell you who is underperforming. Its PIPs won't stand up in front of a subdistrict court (kantonrechter). The questions behind the request have better answers: where delivery is stuck, whether Copilot pays off, and who needs help.

**HOW TO ACT**
1. Stand up the team-level weekly dashboard. It covers:
   - delivery: deploys, lead time, change failure rate, time to restore
   - PR flow: cycle time, wait for first review, PR size, reverts
   - Copilot adoption, read alongside stability
   - a "where to look this week" list that compares each team with its own baseline

   No figure describes fewer than 5 people. Per-person Copilot rows are deleted after 35 days.
   → Platform/data lead → pilot with two volunteer teams by **14 Dec**
2. Take it to the OR with a DPIA before go-live. Aggregate, team-level data under written rules of use is a far easier consent to get.
   → You + DPO + HR → OR consent request in **January 2027**
3. For underperformance, ask each engineering manager for the concerns they already have, with concrete examples against the role's expectations. Where a real gap exists, HR and employment counsel run a proper verbetertraject.
   → Engineering managers + HR business partner (HRBP) → by **7 Dec**
4. For Copilot ROI, compare each team's delivery trend before and after rollout, and run a short anonymous quarterly developer survey.
   → You → first read by **end of Q1 2027**

⚠️ **RISKS**
- **If you go ahead with the ranking:** the OR invokes nullity and every PIP from it collapses. The first contested dismissal fails, and seniors leave first.
- **The team dashboard turns into a league table** if someone sorts it or uses it in reviews. Write "team level only, not used in individual assessment" into the OR agreement.
- **Weakest point of my recommendation:** it won't hand you names. If there are specific people you're worried about today, that goes through their managers, not a dashboard.

🔑 **YOUR DECISION**
- **Option A: individual ranking with automatic bottom-10% PIPs.** It's one query and could be live next week. But it is noisy and gameable, needs OR consent you're unlikely to get, and produces PIPs that won't support a dismissal.
- **Option B: team-level dashboard plus a manager-led performance process.** It needs OR consent and a DPIA, which are easier to get for aggregate data, and about six weeks to go live. It shows where delivery is stuck and whether Copilot pays off, and it keeps underperformance cases defensible.
- **Recommendation:** B. It answers the questions you actually need answered and holds up under Dutch law.

If there's a specific engineer you're concerned about, tell me what you're seeing. I'll help you structure the conversation and a fair improvement plan.

📎 **DETAIL**
- `engineering-health-dashboard.md`: the design. It covers panels and metric definitions, rules of use for the OR agreement, the privacy design and DPIA inputs, the underperformance route, the rollout, sources and confidence notes.
- `engineering_health_dashboard.sql`: the SQL. It holds the schema, Copilot aggregation with the 5-person minimum and 35-day raw retention, the weekly team view, the "where to look" view and the access roles. I tested it on PostgreSQL 16 with synthetic data. The 3-person team was suppressed, the BI role could read only the team views, and the planted problems were flagged.

Still to be checked by others:
- Employment counsel should check the legal points, your DPO the DPIA, and HR the performance process.
- The research figures come from the published studies as I know them. I couldn't re-open them in this session, so check them before they go into a board deck.

Sources: [GitHub: Copilot usage metrics](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics) · [GitHub: per-user report fields](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics) · [GitHub: telemetry gaps](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/reconciling-usage-metrics) · [Dirkzwager: OR consent rights](https://www.dirkzwager.nl/kennis/artikelen/instemmingsrecht-van-de-or-volgens-het-or-privacyboekje-van-de-ap) · [AP DPIA list, Stcrt. 2019, 64418](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
