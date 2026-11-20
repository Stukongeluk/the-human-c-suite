**Don't let the platform lead go, and don't offer anyone's job as the answer to the board.** A 9-hour, €2 million outage is a failure of the system the migration ran in, and as CTO that system is yours. Say so first. Firing the person who knows most about what went wrong loses that knowledge and teaches every engineer to hide the next problem.

The board is right that €2 million needs a visible, accountable response. Give them one, just not a name.

**This week**

1. **Tell the board the result is yours,** and give a fixed date for the review's findings.
2. **Talk to the lead yourself, today, in private.** They are probably devastated. Tell them no decision about them follows from the board's suggestion, and ask for their help finding the causes. Give the team recovery time after that weekend, not more heroics.
3. **Run a blameless review within two weeks,** led by someone outside the platform team. Build the timeline from the incident channel, change ticket, deploy logs and monitoring. Ask how the system made this possible: was the rollback tested on production-sized data? Was there a go/no-go point and an abort time? Who set the window, under what pressure? Why did recovery take 9 hours, not one?
4. **Break down the €2 million** into lost revenue, SLA credits, recovery cost and estimates; the board will ask. Pause risky changes to that database until the review is done.
5. **Report back with actions, each with an owner, a date and a measure** that shows it worked, such as a timed rollback rehearsal before every migration.

If the board wants a signal, offer one from your side, such as your own bonus this year, not someone else's job.

**A line for the board**

"This migration failed on my watch, and the accountability is mine. Removing the person who knows most about why it failed would make the next migration less safe. On [date] I'll bring you the review, the fixes with owners and dates, and how we'll prove they work."

**What would change my answer**

If the review shows the lead skipped agreed steps, ignored warnings or hid information, that is a separate, fair performance conversation based on those facts, not on the outage alone. In most of Europe, dismissing someone over one failed change without a prior process is also hard to defend legally; check with an employment lawyer first (this isn't legal advice).

So two questions: did the lead follow the process you gave them? And was a tested way back part of the plan?

Want me to draft the board note or the review template? And what am I missing?
