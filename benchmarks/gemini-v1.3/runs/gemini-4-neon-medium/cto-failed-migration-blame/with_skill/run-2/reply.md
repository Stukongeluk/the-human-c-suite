**Don't let the platform team lead go.** Own the 9-hour, €2 million outage yourself as CTO, and give the board real accountability: the raw incident timeline and concrete system fixes, each with an owner, a deadline, and a test that proves it works.

The board is right to be angry—€2 million and 9 hours of downtime demand a serious answer and proof it won't repeat. Where they're wrong is the mechanism. One person doesn't cause a 9-hour outage on a production database; missing safeguards do—an untested rollback, a staging gap, missing cutover gates, or schedule pressure. Firing the lead removes the person who now understands the system's failure modes best and teaches every remaining engineer to hide bad news and stay away from risky work. In most European jurisdictions, dismissing someone over a single operational incident without prior process or misconduct also creates employment-law exposure (check with legal/HR before any personnel step—this isn't legal advice).

**What to do next:**

1. **Own the result first.** Align with the CEO, then tell the board plainly that the release gates, testing standards, and operational readiness belong to you—not to the engineer who ran the runbook.
2. **Pull the raw facts before the meeting.** Review the incident timeline, migration plan, staging and rollback test logs, and approval history. Verify there was no deliberate bypass of agreed controls—if there was, that's a separate conduct issue, handled through HR after the facts are in.
3. **Talk to the platform lead today.** Tell them directly you aren't looking for a scapegoat and you need them to help fix the system. Check their fatigue after a 9-hour recovery.
4. **Run a blameless post-mortem with hard outputs.** Focus on how the system allowed a 9-hour failure. End with 3–5 specific actions—such as a timed rollback rehearsal on production-scale data, automated pre-flight checks, or phased cutovers—each with an owner, a date, and a measurable pass/fail test.
5. **Commit to a board check-in.** Put a 14-day and 30-day review on the calendar to show completed fixes and rehearsal results.

**A line you can use with the board:**
> "The 9-hour outage and €2 million loss are on me—our migration controls and rollback path failed. Letting go of the platform lead won't fix those gaps; it strips out our deepest database knowledge and makes the team afraid to surface risks. By [date], I will bring you the full timeline and the system fixes—each with an owner, a deadline, and a timed rollback test proving this can't happen again."

If you'd like, I can draft a one-page board memo or the post-mortem structure to take into that meeting.

*Key assumption: the incident was an operational and system failure, not deliberate negligence or concealing a known blocker.* What am I missing, and what would make this wrong?
