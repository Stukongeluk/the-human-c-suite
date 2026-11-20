Don't let the platform team lead go on the board's suggestion. Take the accountability yourself, run an independent, blameless review over the next two weeks, and go back to the board with the causes, the verified cost and the fixes, each with an owner and a date. When one migration can take you down for 9 hours and cost around €2 million, the safeguards around the change failed: rehearsal, rollback, abort criteria, approval or staffing. Firing the person who ran it fixes none of those.

**Why firing now is the wrong move**

- **The cause stays.** If there was no tested rollback, no abort point or no time to rehearse, the next lead runs into the same problem.
- **You lose the person who knows the most** about what went wrong, just when the review and the next attempt need it.
- **Everyone else learns to hide risk.** When engineers see someone fired for an honest failure, they escalate later, report fewer near-misses and stop volunteering for risky changes. Google's Project Aristotle found psychological safety was the most important of five dynamics in effective teams. DORA's 2023 report found 30% higher organisational performance in high-trust cultures.
- **It's irreversible and decided under pressure, before the facts are in.** If the review shows the plan was approved above them, or that they raised risks and were overruled, you can't take it back.
- **It may not hold up legally.** In the Netherlands, for example, dismissal for poor performance needs a documented chance to improve first, and dismissal on the spot needs an urgent reason. A single honest failure is unlikely to meet either test, so expect a costly settlement. Talk to employment counsel before anyone says anything to the lead. This isn't legal advice.

**Where the board is right.** €2 million needs an owner, and the board needs confidence it won't happen again. But accountability means owning the explanation, the fix and the follow-through. That owner is you. Note your own interest too: you're in the chain of accountability, so defending the lead can look like defending yourself. An independent facilitator and owning the outcome in public answer that.

**What I'd do**

1. **Today: talk to the lead yourself,** before the rumours reach them. Be honest about where they stand: no decision about their job is being made on a board suggestion, and the review is about how the system failed. Don't promise more than you can keep. People who fought a 9-hour outage also need rest.
2. **Over the next two weeks: a blameless review led by someone outside the platform team.** Build the timeline from incident logs, chat, change records, the migration plan and monitoring. I haven't seen any of these, and they decide what's true here. The questions that matter:
   - Was the migration rehearsed on production-sized data?
   - Was there a tested rollback with a time limit, and who could call an abort?
   - Where did the 9 hours go: noticing the problem, deciding what to do, or restoring?
   - Were risks raised beforehand, and who accepted them?
   - Who chose the weekend window, and was there deadline pressure?
3. **Check the €2 million.** Split it into lost revenue, SLA credits, recovery costs and revenue that will come back. The board should get a number that holds up.
4. **Go back to the board within about three weeks,** and offer a progress report at 90 days.
5. **Fix the system.** These are candidates until the review confirms them: mandatory rehearsals, go/no-go criteria with a named person who can call an abort, zero-downtime patterns or waves instead of a big-bang cutover, and enough people on the change that nobody runs it exhausted.
6. **Measure it:** change failure rate, time to restore, repeat causes, and a team pulse question: "I can raise risks without fear."

**What to tell the board**

> "I'm accountable for this outage. The platform team works within processes I own. In two weeks you'll have an independent review: what happened, why our safeguards didn't stop it, the verified cost, and the changes with owners and dates. We'll report progress at 90 days. If the review shows misconduct by anyone, I'll act on it through a proper process. I won't let someone go before we know what happened, because that makes the next incident more likely, not less."

If the board wants a visible consequence, let it fall on you, for example by giving up part of your own bonus this year. It signals ownership but fixes nothing, so pair it with the plan.

**What would change my mind.** The review should separate three things. Honest error calls for fixing the system. Shortcuts that had become normal call for fixing the pressures and coaching. Reckless or dishonest conduct, such as knowingly skipping agreed safeguards, ignoring an abort call or misreporting status, is the only case for consequences for an individual, and then through a fair, documented process, not because the board asked. Any earlier performance concerns are a separate matter, judged on their own facts.

Two answers would change my advice the most. Did the team raise risks or ask for more time before the weekend? And who approved the go-ahead and the window?

What am I missing, and what would make this wrong? I can draft the board note and a review template if that helps.
