Don't let the platform team lead go. Take ownership of the failure yourself, and give the board an accountability they can see: a blameless review with a dated fix plan, and you as the named owner. Firing one person doesn't remove the cause of a 9-hour outage. A migration that costs €2 million and needs one person to run it points at the system: the plan, the rehearsals, the rollback, the go/no-go decision. You were part of that system, so the first sentence to the board is "this was our failure, and it is mine as CTO".

**Why firing is the wrong move**
- It teaches everyone to hide risk before the next migration. You lose the person who knows the system best, and the next incident gets reported late.
- It probably won't satisfy the board for long. If the cause was a missing rollback test or an approval nobody owned, the same failure can happen again with a new lead.
- If your jurisdiction is the Netherlands (I'm guessing, given the €), dismissing someone for one failed project without prior warnings and a documented performance process is legally risky. Get employment counsel before anything is said to anyone. This isn't legal advice.

**What to do this week**
1. **Run a blameless post-incident review, led by someone outside the platform team.** Build the timeline from logs, change tickets, runbooks and chat. Ask what was decided, on what information, who approved it, and what was rehearsed. Did a dry run happen on production-sized data? Was there a tested rollback? Was the weekend window a business deadline, and who set it?
2. **Talk to the platform lead first and privately,** before the board sees anything. Hear their account, tell them what you're proposing, and tell them they are not being scapegoated. Support them. They are probably in bad shape.
3. **Give the board accountability in a form they can use.** Bring a short paper with the facts, the root causes found, the changes with owners and dates, and what you personally are accountable for. Name the control that failed, not the person. If the review does find a real individual failure, such as a skipped approval or ignored warnings, deal with it through a fair, documented process afterwards. That is a different path from firing someone in response to pressure.
4. **Fix the controls:** go/no-go checklists, mandatory rehearsals, rollback tests, a second approver on irreversible changes, and a business owner for the downtime budget.
5. **Quantify the €2M properly** (lost revenue, SLA credits, recovery labour). It makes the board conversation about prevention rather than blame.

**A line for the board:** "The failure was ours and I'm accountable for it. Here is what went wrong, here are the five changes with owners and dates, and here is how you will see whether they worked. Removing one person would not have prevented this and would make the next one more likely."

**Where the board has a fair point:** a €2M loss deserves consequences, and "no one is accountable" is not an acceptable answer. Offering your own accountability and a verifiable plan meets that. If they still insist, you can offer them an independent review of the findings.

Assumptions: I haven't seen the incident timeline, so I don't know yet whether this was a planning failure, an execution slip or a rushed deadline. The review answers that, and it could change my view if it shows negligence.

What am I missing, and what would make this wrong? If you share the timeline, I can draft the board paper or the review brief.
