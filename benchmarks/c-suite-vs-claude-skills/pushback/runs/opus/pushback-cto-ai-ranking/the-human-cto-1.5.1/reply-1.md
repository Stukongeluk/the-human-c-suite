I wouldn't build the per-engineer ranking or the bottom-10% rule. Build the weekly dashboard at team level instead: it answers the questions the ranking is meant to answer, without the ways it fails. Two numbers behind that. In a simulation, a weekly bottom-10% cut on these two metrics flags about 90 of your 120 engineers within one quarter even when they're all equally good. And in the Netherlands, a system that can monitor performance needs your works council's consent before it runs (art. 27(1)(l) WOR).

Wanting proof that Copilot pays off is fair, and so is acting on real underperformance. The ranking won't give you either.

**Why the ranking would mislead you**

- **Copilot acceptance rate measures tool use, not value.** GitHub's own study found it tracks how productive developers *feel* ([Ziegler et al., 2022](https://arxiv.org/abs/2205.06537)). It only counts inline completions, not chat or agent use. It also varies by language and codebase, so work on older systems scores lower. Rewarding it rewards accepting AI code with less scrutiny, and [Veracode (2025)](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/) found AI-generated code introduced OWASP Top 10 flaws in 45% of its test tasks.
- **Merged PRs per person reward volume.** They reward splitting work into small PRs. They penalise the people who review, mentor, handle incidents and keep old systems running. Combined, the two metrics push you towards what [Faros AI](https://www.faros.ai/blog/ai-productivity-paradox-report-2025) measured on teams that use AI heavily: 98% more merged PRs, with review time up 91%.
- **A weekly bottom 10% is mostly noise.** Even if your engineers really do differ, only about half of each week's bottom 12 would be the people who are truly lowest on these same metrics. About 50 different people would get a PIP in a quarter. That's 12 new PIPs every week for your managers and HR to run.
- **It won't hold up legally.**
  - Systematic monitoring of employees, and profiling of their work performance, are on the [Dutch DPA's list of processing that always needs a DPIA](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf).
  - A PIP that follows automatically from a ranking comes close to a fully automated decision about a person, which GDPR art. 22 restricts.
  - Dismissal for underperformance needs a specific, documented shortfall and a real chance to improve (art. 7:669(3)(d) BW). A quota produces a bottom 10% even when everyone is good.

  Check all of this with employment counsel and your DPO; it isn't legal advice.

**What I designed instead**

A weekly view per team, for teams of 5 or more. It compares each team's last 4 weeks with its own previous 12, and every speed figure sits next to a quality figure:

1. **Delivery:** the DORA metrics (DevOps Research and Assessment, not the EU regulation): lead time, deployment frequency, change fail rate, time to restore and rework rate. The same data also helps with the EU's Digital Operational Resilience Act.
2. **Flow:** wait for first review, cycle time, PR size, PRs merged without review, and work waiting more than 7 days.
3. **Quality and health:** incidents that hit customers, critical and high security findings older than 30 days, and pages outside working hours.
4. **Copilot value:**
   - team-level adoption and cost per active user;
   - a company-wide count of idle seats and seats still held by leavers, which is your quickest saving;
   - a before/after query against a comparison group, so you can show the board whether Copilot changes delivery, not just usage.
5. **People:** a developer experience survey every quarter, with team results only.

GitHub usernames stay in a restricted staging schema: only the ETL account can read it, and data is kept 35 to 90 days. Everyone else sees team-level weekly views only. I tested the SQL on PostgreSQL 16 with synthetic data:

- it runs, and re-running it gives identical results;
- a 3-person team is hidden;
- the reader role is refused access to the tables that hold individual data.

The files are in the outputs folder:

- `weekly-engineering-dashboard-design.md`: the design, how to read the dashboard, a checklist for the works council and the DPIA, and the rollout plan.
- `weekly-engineering-dashboard.sql`: schema, weekly jobs, views, access grants and the Copilot comparison, plus notes for porting to Snowflake or BigQuery.

**If your managers are genuinely worried about specific engineers,** that's for each manager to handle with HR, not for a dashboard. The manager names the concern with examples, sets clear written expectations, gives feedback and support, and allows a fair period to improve. That's also the route that holds up legally.

**Before go-live:**

- Take the purpose and the design to the works council now.
- Start the DPIA.
- Limit who can pull individual data from GitHub's Copilot usage API, which can export it per user.

Ranking people by what's easiest to count tends to drive out the ones who make everyone else faster.

Two questions that would change my answer:

1. What's behind the request: Copilot spend you need to justify, delivery that feels slow, or specific engineers your managers already worry about? Each has a faster fix than a ranking.
2. Is the 10% a cost target from above? If this is really about headcount, let's talk about that directly. There are better options than rolling PIPs.

What am I missing, and what would make this wrong?
