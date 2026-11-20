Don't fire the platform team lead now. Give the board accountability this week, but make it yours, and make it a fact-based answer rather than a name. At €2 million and 9 hours you can afford two weeks to find out what actually failed. A dismissal today is irreversible and would be decided before you know whether it was deserved.

**Why not the lead, yet**

- **Who is accountable.** You approved the plan, the weekend window, the staffing and the rollback readiness. In a failure this size, the person who ran the migration is rarely the root cause. More often a go/no-go was missed, rehearsals were skipped, the rollback was untested, or the team was under-resourced. Accountability sits with whoever owned those decisions, and that includes you.
- **What firing does.** Every other engineer will learn that running risky work gets you fired, and from then on problems get hidden. You also lose the one person who understands the failure best, in the middle of the recovery. Reliability research is consistent that people who fear blame stop reporting near-misses.
- **The legal side.** In the Netherlands, dismissing an employee for a single failed project, without a documented performance history, is hard to defend and can mean a long dispute and a transition payment. If the lead is a freelancer, it is simpler but still unfair. Check this with HR and an employment lawyer before anything is said to the board. This is not legal advice.

**What I would do instead**

1. **Take responsibility yourself, in the first sentence to the board.** "The migration was my decision and my responsibility. Here is what I know, what I don't, and the date you get the full answer." Boards usually want to see ownership and control more than a head.
2. **Run a blameless post-mortem in about two weeks, led by someone who was not on the migration.** Ideally an independent senior engineer, or an outside reviewer if the board needs more assurance. Build the timeline from the real record: change tickets, pipeline and deploy logs, monitoring, the chat from that weekend, and the go/no-go decision. The question is how the system allowed this, not who pressed the button.
3. **Sort the causes before judging anyone.**
   - Planning: was it rehearsed on production-sized data? Was there a tested rollback? Was the window long enough?
   - Decision: who agreed to go ahead, on what evidence, and with which warnings overruled?
   - Capacity: how many hours had the team worked, who was on call, were there enough people?
   - Execution: only after those three, was there an individual error that a reasonable engineer should not have made?
4. **Give the board a date and criteria now.** "By [date] you will have the root causes, the actions, the owners, and my assessment of individual performance. If the evidence shows a real conduct or competence problem, I will deal with it through the normal HR process."
5. **Look after the lead.** Tell them yourself, before they hear it from anyone else, that a review is happening, that it is about the system, and that you stand behind them until the facts say otherwise. They have probably not slept well for a week.
6. **Put the fixes in place.** Rollback rehearsals, a go/no-go checklist with a named decider, migrations in waves instead of one weekend, and a rule about staffing and rest for big changes. Fund this explicitly. That is what stops the next €2 million.

**What to tell the board that is not a name**

You can show accountability without a dismissal: you own the outcome, there is an independent review with a date, there is a list of changes to how you approve and run high-risk work, and you will report progress monthly. If they still want a personal consequence, offer the one that is yours to give: your own bonus, or a formal review of your own role in the decision. If the board insists on an individual before any facts exist, that is a governance question to raise with the chair, calmly and in writing: a decision to dismiss someone should rest on documented evidence.

**What would change my mind**

- The review shows deliberate or reckless behaviour, such as ignoring a clear no-go, falsifying test results, or hiding problems during the outage. That is a conduct issue, and it goes through a proper HR process.
- There is already a documented history of serious performance problems that predates this weekend.
- The lead had full authority, full resources and clear warnings, and still decided alone to proceed.

Two questions would sharpen this. Who made the final go decision, and was a rollback plan tested before the weekend? And has the lead worked on this team for long, with what record before this?

What am I missing, and what would make this wrong?
