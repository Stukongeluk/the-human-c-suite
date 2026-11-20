Don't fire the platform team lead now. Give the board accountability through a fast, blameless, evidence-based review with a hard deadline, and take the ownership yourself. A €2 million, nine-hour outage is almost never one person's fault. The review can still find individual responsibility; it will do so on facts, not on a board's appetite for a name.

**Why not fire now**

- **You don't know the cause yet.** Firing before the review means picking the person first and finding the reasons later. That is the wrong order for a decision you can't undo.
- **Migrations fail at the system level.** Usual causes are a rollback that was never rehearsed, a cutover window with no abort criteria, a go/no-go approved above the team lead, a schedule pushed by the business, thin staging, and nobody checking the plan independently. If one of those is the cause, firing the lead removes the one person who understands the system and fixes nothing.
- **The rest of your engineers will draw their own conclusion.** If the person who ran the migration is fired, nobody will report a risk before the next risky change. Your next incident will then be both harder to see and harder to recover from.
- **You approved this.** The migration ran with your sign-off, your timeline and your staffing. Accountability sits with the person who owns the decision, and that is you before it is the team lead. The board should hear that from you, not discover it.

**What to do this week**

1. **Open a review with a fixed date.** Two to three weeks, led by someone who was not on the migration, ideally with an outside reviewer. It builds a dated timeline from the real records: change tickets, the pipeline, monitoring, the incident channel. It answers four questions: what failed, which decisions were taken and by whom, what information they had at the time, and why the safeguards (rehearsal, rollback, abort criteria) didn't hold.
2. **Support the team lead meanwhile.** Keep them in role, tell them directly that the review is blameless, and make sure they hear the plan from you before anyone else does. They also carry nine hours of stress. Check how they are doing.
3. **Tell the board what you will deliver and when.** Offer: findings on a set date, named owners for every fix, a public account of your own decisions in this, and one question put to them directly: "If the review shows a process or planning failure rather than negligence, would a dismissal still be the right outcome?"
4. **Fix the system, with dates.** Likely actions: mandatory rollback rehearsal for any change of this size, written abort criteria, an independent go/no-go, and capacity reserved for migrations instead of being squeezed in.

**What the board is really asking**

They want to know this won't happen again and that someone takes it seriously. A name is the quickest answer, not the best one. Steelmanning them: €2 million and nine hours is a serious loss, and a board that sees no consequence may fear nothing will change. Your answer to that is credible accountability: you own it, the review has a date, fixes have owners, and the next large change has a visible gate.

**When individual consequences are legitimate**

If the review finds that someone ignored explicit warnings, hid a known risk, or skipped agreed safeguards knowingly, then a conversation about individual consequences is fair. Even then, the response should be proportionate: coaching, a changed role, a formal warning, before dismissal. In the Netherlands, dismissing an employee for a failed project is legally hard unless there is culpable conduct or a documented performance process, and a works council may have a say if the team is affected. Involve HR and an employment lawyer before any step. This is not legal advice. If the lead is a freelancer rather than an employee, the contract rules differ.

**Facts I haven't seen**

I haven't read your incident timeline, change records or the migration plan, so this rests on how such failures usually go. Connect the incident tooling and the repository history and I can build the timeline with you.

**Assumptions:** the lead did not act against explicit instructions; the plan was reviewed and approved above them; the board's view is not yet fixed.

Two questions would change my answer: who approved the go-live and the cutover window, and had a rollback been tested beforehand? If the answers are "nobody above the lead" and "no", the picture shifts, and so does what you owe the board.

What am I missing, and what would make this wrong?
