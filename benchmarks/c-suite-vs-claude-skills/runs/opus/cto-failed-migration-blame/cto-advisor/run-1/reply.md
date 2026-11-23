# CTO Advisor: Accountability after the failed migration

## Bottom line

Don't let the platform lead go now, and don't let the board make that call before anyone knows why a planned migration turned into a 9-hour outage. Give the board real accountability instead: you own the outcome, they get a fact-based review within two weeks, and they get a fix plan with named owners and dates. Individual consequences come into play only if that review shows reckless behaviour, and then through HR, not a board vote.

**Confidence:** high on the approach. Low on what actually went wrong, because nobody knows that yet.

## What

- **Nobody knows yet what caused this, including the board.** Firing someone before the review means deciding without evidence, and a firing can't be undone. *[Assumed: no review has happened yet. Your message doesn't mention one.]*
- **A 9-hour outage is rarely one person's mistake.** Failed migrations are a known risk. Being down for 9 hours means the safety nets failed too: a tested way back (a *rollback*), a rehearsal on production-sized data, a fixed time to abort, and more than one person able to make the call. Someone also approved the plan, the timing and the risk. Those are system and leadership choices, including yours. *[Inference from how large migrations usually fail. Medium confidence until the review confirms it.]*
- **Firing the lead throws away what the €2 million paid for.** Nobody knows better than the person who ran it how it went wrong. Etsy's former CTO John Allspaw found that engineers who expect a reprimand hold back details, so the failure happens again, and that the engineer is "the most expert in their own error". In 2017 a GitLab engineer accidentally deleted the production database. GitLab kept him and went ahead with his promotion to senior developer. *[Verified: sources below]*
- **It teaches everyone that bad news gets punished.** Google's SRE book (its guide to running production systems) warns that where people get blamed, "people will not bring issues to light for fear of punishment". DORA, Google's long-running research programme on software delivery, finds that high-trust cultures predict better delivery and business performance. In those cultures failure leads to inquiry rather than scapegoating. In practice, blame means slower escalation in the next incident, hidden near-misses and nobody volunteering for the next migration. *[Verified: sources below]*
- **The legal ground is weak.** The euro figures suggest you're in Europe. There, dismissal generally needs a valid, documented reason, and usually a warning and a real chance to improve. One incident with no earlier record is a poor basis. *[Assumed: EU employer. This is not legal advice, so check with employment counsel.]*

## Why this matters

The €2 million is spent. The open question is whether you get the lesson you paid for or pay again on the next migration. Firing the lead would also cost you an experienced person and the trust of everyone watching how you handle this.

## How to act

1. **Tell the board in writing that you are accountable and that no personnel decision will be made before the review.** Give them a date for the findings and the fix plan. → You → within 24 hours
2. **Talk privately with the platform lead.** Tell them they're not being singled out and that you need them as the main source for the review. Ask how they're doing, because 9 hours of outage followed by board talk is heavy. Promise a fair process, not an outcome. → You → today
3. **Run a blameless review.** That means investigating how the failure happened, not who is to blame. Have it led by a facilitator who wasn't involved, such as a senior engineer from another team or an outside facilitator. Rebuild the timeline and the key decisions, including why each one made sense at the time. Above all, find out why recovery took 9 hours instead of 1. → Facilitator, with you as sponsor → first session within 48 hours, written report within 2 weeks
4. **Have the €2 million checked.** Find out what's in it: lost revenue, SLA credits (contractual refunds to customers), staff hours, and any revenue that will come back later. The board is fixed on that number, so it has to be right. → CFO → end of this week
5. **Give the board the findings, a fix plan with owners and dates, and the rule for when an individual is held to account.** Agree that rule before the findings are in, so it can't look improvised. → You, with HR → within 2 weeks

## Risks

- **The board pushes back and your standing with them suffers.** You lower that risk by offering something concrete and dated instead of a plain "no". Saying "I'm accountable" also puts you in the firing line. That's the price of protecting the team and the systems that now have to be fixed.
- **The review finds reckless behaviour.** Examples are knowingly skipping agreed safeguards, ignoring an explicit no-go or hiding information. Then consequences are fair, handled through HR and with legal advice. Honest mistakes, and shortcuts the system had made normal, call for coaching and system fixes, not dismissal.
- **The review finds pressure from leadership.** Examples are a forced timeline, no budget for a rehearsal, or one person carrying the whole weekend. Then that pressure is part of the finding, and part of what you own.
- **Your platform team reads this as scapegoating and people start leaving.** Watch the next few weeks closely. They're the ones who will run the next migration.
- **Where this advice could be wrong:** I only know what's in your message. The picture changes if this person already has a documented performance problem, ignored warnings or caused earlier incidents. Even then, that calls for a performance process, not a reaction to one weekend.

## Your decision

- **Option A: let the lead go now.** The board gets a quick answer. You lose the person who knows the most, risk a legal claim and leave the causes unfixed. The board also learns that incidents end with a firing, and next time that may be you.
- **Option B: hold all personnel decisions, run the review, take ownership and report back in two weeks.** This costs you some friction with the board now. In return you find the real causes, the team keeps talking openly, and the board gets accountability it can check.
- **Recommendation: Option B.** Accountability means owning the facts and the fix. It doesn't mean picking a name before you have the facts.

## Detail

The attached `accountability-pack.md` has four things: a draft note to the board, the review setup and questions, the criteria for individual consequences, and talking points for your conversation with the lead.

**Still to be checked by:** the CFO (the €2 million figure), and HR and employment counsel (any step involving an individual).

**Sources:** [Google SRE book: Postmortem culture](https://sre.google/sre-book/postmortem-culture/) · [DORA: Generative organizational culture](https://dora.dev/capabilities/generative-organizational-culture/) · [John Allspaw (Etsy): Blameless postmortems and a just culture](https://www.etsy.com/codeascraft/blameless-postmortems) · [GitLab: How is team-member-1 doing?](https://about.gitlab.com/blog/how-is-team-member-1-doing) · [ISMP/ECRI: Human error, at-risk and reckless behaviour](https://home.ecri.org/blogs/ismp-alerts-and-articles-library/the-differences-between-human-error-at-risk-behavior-and-reckless-behavior-are-key-to-a-just-culture) · [Deel: Performance dismissals in the UK, Germany, France and the Netherlands](https://www.deel.com/blog/performance-improvement-plans-international-dismissal-law/)
