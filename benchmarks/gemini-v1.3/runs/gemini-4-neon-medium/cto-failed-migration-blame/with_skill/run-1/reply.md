**Don't let the platform lead go.** Take accountability yourself as CTO, and give the board real accountability: a factual root-cause review and a remediation plan with owners, dates, and verifiable tests.

The board's reaction is understandable—9 hours of downtime and €2 million in losses is a serious business hit, and they need confidence it won't happen again. Offering a name feels decisive, but it solves the wrong problem. A 9-hour outage is a system failure: a migration without a tested, fast rollback, a gap between staging and production, or weak sign-off controls. Those are CTO responsibilities. Firing the lead removes the person who now understands the failure best, fixes none of the underlying gaps, and teaches every engineer to hide risk instead of escalating it—making the next outage more likely. In most European jurisdictions, dismissing someone over an operational incident without gross negligence also carries real employment-law risk (check with counsel and HR—this isn't legal advice).

### What to do next

1. **Own it with the board today.** Tell the chair plainly that the 9 hours and €2 million are on you as CTO, not the platform lead. If the board wants a visible executive consequence, put your own bonus on the line before anyone else's job.
2. **Pull the raw evidence.** Run a blameless post-mortem from the incident timeline, migration logs, runbook, rollback tests, and approval trail to see how the system allowed a 9-hour recovery. Only treat this as a conduct issue if evidence shows someone deliberately bypassed agreed safeguards.
3. **Bring the board measurable fixes.** Within a week, deliver a short plan where every action has an owner, a deadline, and proof it worked—such as a timed rollback rehearsal in a production-like environment, stricter migration gates, and a hard recovery-time target. Report progress at the next two board meetings.
4. **Protect the lead and the team.** Tell the lead privately that you have their back, involve them in the post-mortem and fixes, and give the weekend responders recovery time.

### A line you can use with the board

> "The 9-hour outage and the €2 million loss are on me—our migration controls and rollback readiness are my responsibility. Firing the platform lead won't fix why recovery took 9 hours, and it will make engineers hide risk instead of flagging it. Give me until Friday to bring you the root cause and a remediation plan with owners, dates, and a timed rollback rehearsal, and hold me accountable for delivering it."

**Key assumption:** the lead acted in good faith within your existing process, rather than ignoring explicit warnings or bypassing controls.

If you'd like, I can draft the one-page board note or a blameless post-mortem template next. What am I missing, and what would make this wrong?
