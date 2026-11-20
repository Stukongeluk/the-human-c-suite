Don't let the platform lead go, at least not now and not for this. Take the accountability yourself, commission a blameless review run by someone outside the platform team, and come back to the board within three weeks with causes, fixes and owners. €2M over 9 hours is roughly €220k per hour of downtime, so the most valuable question is why you couldn't roll back within the first hour. Firing one person doesn't answer that.

**Why firing the lead is the wrong trade**

- **It doesn't remove the cause.** If one migration can take you down for 9 hours, the system was missing something: a rehearsal on production-sized data, a tested rollback, a hard go/no-go point, or early detection. Those gaps stay after the person goes.
- **You'd throw away the lesson you just paid €2M for.** The board wants to remove the person who knows best where it broke and how to stop it happening again.
- **Everyone else learns the wrong thing.** Engineers will stop volunteering for risky work and report problems later, so the next incident runs longer. Google compared 180 teams and found psychological safety (the belief that you won't be punished for raising a mistake) was the strongest of five dynamics behind effective teams.
- **The accountability sits in the wrong place.** The migration, its timing and its risk were approved above the person who ran it. A company decision belongs to the leaders who approved it, and that includes you.
- **It's legally weak.** In most of Europe, one good-faith mistake in an approved change is thin grounds for dismissal. In the Netherlands a dismissal needs a reasonable ground, and for conduct it goes to the subdistrict court. In Germany a conduct-based dismissal normally needs a prior written warning first. Expect a costly settlement or a dispute. Check with employment counsel; this isn't legal advice.

The board's underlying need is fair: confidence it won't happen again, a named owner, and proof that leadership takes it seriously. Give them all three.

**What I'd do this week**

1. **Talk to the platform lead first, in private.** They're probably exhausted and expecting the worst. Tell them where you stand: the review is about how the system failed, and you want their help fixing it. Promise a fair process, not an outcome you can't guarantee. Lighten on-call for a week or two for everyone who worked those 9 hours.
2. **Tell the board the accountability is yours.** For example:
   > "I approved the migration, so the accountability is mine. I won't fire anyone before we know what failed: that would throw away the knowledge we just paid €2M for and teach engineers to hide problems. Within three weeks you'll get an independent review with the timeline, root causes, and fixes with owners and dates. If it shows anyone ignored agreed safeguards or hid problems, we'll deal with that through the normal process."
3. **Commission the review.** Have someone outside the platform team run it, such as a senior engineer from elsewhere or an external SRE. The lead contributes fully but doesn't review their own work. The review should answer:
   - Was the migration rehearsed on production-sized data, and was the rollback tested?
   - Was there a go/no-go criterion and a deadline for rolling back no matter what? Where did the 9 hours go: detecting the problem, deciding to roll back, or restoring?
   - Who set the window and the scope? Was the team under time pressure or short-staffed? Were concerns raised and overruled?
   - What makes up the €2M: lost revenue, SLA credits, recovery work, churn risk?
4. **Separate error from recklessness.** An honest mistake inside a weak process is a system problem. Knowingly skipping agreed checks or hiding what was happening is a conduct issue, handled fairly once the facts are in. Right now you don't know which this was.
5. **Fix it and report back.** Typical fixes: a standard for high-risk changes (rehearsal, tested rollback, a hard rollback deadline), staged migrations instead of a big-bang cutover, and faster detection. Give each an owner and a date, and report progress to the board.

**If the board still wants a visible consequence**

Offer your own, such as part of your bonus or a clear public statement that you own the failure. It costs the company little and says more than a dismissal would. After the 3DS sold poorly in 2011, Nintendo's Satoru Iwata halved his own salary rather than cut staff. It's your call, not a requirement.

**Precedents you can show the board**

- **AWS, February 2017:** an authorised engineer following an established playbook mistyped a command and took S3 down in US-East-1 for about four hours. Amazon fixed the system: the tool now removes capacity more slowly and won't take a subsystem below its minimum capacity. ([AWS post-event summary](https://aws.amazon.com/message/41926))
- **GitLab, January 2017:** an engineer accidentally deleted the primary production database. GitLab kept him and went ahead with the promotion he had already earned. It wrote that it would rather learn from mistakes "than punish honest and talented people for mistakes that can happen to anyone." ([GitLab](https://about.gitlab.com/blog/how-is-team-member-1-doing). This is the company's own account.)

**My assumptions:** the lead acted in good faith, the plan was approved above them, and this isn't a repeat of an earlier failure of the same kind. If any of these is wrong, my answer changes.

Two questions would change my advice most. Did anyone raise concerns before the migration that were overruled? And was there a rollback plan that wasn't used, or no rollback plan at all?

What am I missing, and what would make this wrong?
