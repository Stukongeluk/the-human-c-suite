## Bottom Line

Do not fire the platform team lead now, and do not agree to it before you know why the migration failed. Take accountability yourself, run a fast and independent post-mortem, and give the board a dated findings briefing with named owners for each fix. If the review finds individual negligence or concealment, you can still act on that, and you will have evidence for it.

## What I recommend (confidence in brackets)

1. **Own it at the top.** [High] A migration that was approved, scheduled, staffed and signed off is an organizational decision, and you are the executive accountable for it. Tell the board "I am accountable, and here is how I will show you what happened and what changes." That gives them accountability without a scapegoat.
2. **Run a blameless post-mortem within 48 hours of the board conversation, with an external or cross-team facilitator.** [High] Your own standard (incidents are system failures, not people failures) applies here, and it applies more because the lead reports to you and you have a stake in the answer. Use someone outside the platform team, or an outside reviewer, so the result is credible to the board.
3. **Ask the questions that decide whether this was a person or a system.** [High] You need these answers before anyone's job is discussed:
   - Was there a tested rollback plan, and was it rehearsed on production-like data and volume?
   - Who approved the go/no-go, and on what evidence? Did the lead raise risks, ask for more time or ask for more people, and were they overruled?
   - Why did a 9-hour outage happen? The failure itself and the 9 hours to recover are two separate problems, and recovery time is often the larger one.
   - Were there monitoring, alerting or on-call gaps? Was the right expertise reachable that weekend?
   - Was the weekend window, scope and deadline set by the business or by the team?
   - Is there an ADR or change record for the migration, and does it match what was actually done?
4. **Give the board a decision rule instead of a name.** [Medium] Say: "If the review shows reckless disregard of agreed procedure, falsified readiness, or concealed problems, we will take individual action. If it shows process, planning or resourcing failures, accountability sits with me and the leadership chain, and we fix the system." Boards usually accept a clear standard and a date.
5. **Protect the lead while the review runs.** [Medium] Keep them in the room and do not suspend them on rumor. If you cannot, consider moving them off the follow-up work only if the facts point that way.

## Why

- **Firing the person who ran the migration usually does not fix the cause.** [High] If the cause was a missing rehearsal, an unrealistic deadline or no rollback plan, the next lead hits the same wall. You would also have destroyed the one person who knows the system best, right when you need them to repair it.
- **It teaches the wrong lesson to everyone else.** [High] Engineers will hide risk, avoid owning risky work and stop flagging problems. That raises the odds of the next outage and slows the people who are needed to stabilize things. Regrettable attrition would also follow, which is costly on top of the €2 million.
- **The accountability chain points upward.** [High] Someone chose to migrate on that date, accepted the risk, and approved the plan. If it turns out you did that or signed it off, saying so directly is much stronger with the board than offering them someone else.
- **Evidence beats instinct, in both directions.** [Medium] I have not seen your incident timeline, runbooks or approvals, so I cannot tell you the lead was blameless. Negligence is possible. The point is to decide on facts, and a fair process protects you legally and reputationally if you do end up removing someone.
- **Employment law matters.** [Medium] A dismissal with no documented performance case or investigation carries real legal exposure in most jurisdictions. Check with HR and employment counsel before any personnel action. I have assumed nothing about your location.

## How to Act

| When | Action | Owner |
|------|--------|-------|
| Today | Short note to the board: you are accountable, a post-mortem is under way, findings briefing on a set date (aim for 7 to 10 days) | You |
| Within 48 hours | Name an independent facilitator, freeze logs, timelines, chat history and change records | You |
| Within 1 week | Blameless post-mortem: timeline, contributing factors, decision points, what the lead flagged | Facilitator |
| Within 1 week | Capture the decision as an ADR or change record, including who approved and on what evidence | Architecture lead |
| Board briefing | Root causes, owners, dates and a rule for individual accountability, plus a new migration gate | You |
| Next 30 days | Fixes: mandatory rehearsal on production-like data, tested and timed rollback, go/no-go checklist with a named approver, staged cutovers, on-call coverage for change windows | Platform and you |

Also track the metrics that show whether the fix works: change failure rate, time to recovery, and the share of high-risk changes that had a rehearsed rollback.

For the board, the framing that tends to work is: "We lost €2 million and 9 hours. The question is whether it can happen again. Here is what I know, what I am finding out, by when, and what I am changing."

## Your Decision

- **Option A (recommended):** Own it, run the independent post-mortem, and brief the board with findings and a decision rule for individual action.
- **Option B:** Individual action now. Choose this only if you already have clear evidence of negligence or concealment, and then follow a documented, HR-supported process.
- **Option C:** Give the board a name to end the pressure. I advise against it. It trades one bad week for a repeat incident and a weaker team.

One thing I need from you to sharpen this: what did the lead say before the migration about readiness and risk, and who set the weekend and the scope? If you can tell me that, I can say much more precisely where accountability sits.
