Do not let the platform team lead go; take responsibility for the 9-hour, €2 million outage yourself and give the board a system fix with measurable gates instead.

The board is right to demand accountability for a €2 million failure. Firing the lead is the wrong answer for three reasons: a 9-hour recovery is a system failure (missing rollback rehearsals, unclear abort thresholds, or weak staging parity), not a one-person mistake; you need that lead’s database knowledge right now to stabilise the platform; and scapegoating teaches every other engineer to hide risk rather than escalate it—the exact opposite of the high-trust culture that DORA research links to reliable systems.

Here is what to do next:

1. **Own the outcome first.** Tell the board plainly that as CTO you own the engineering system, the migration sign-off, and the recovery standards.
2. **Check the facts before judging anyone.** Review logs, approvals, and pre-migration warnings. Unless there was deliberate misconduct or concealed risk, keep the lead in place.
3. **Run a blameless post-mortem within 5 business days.** Focus on how the system allowed a 9-hour outage. End with concrete fixes—each with an owner, a date, and a measurable test, such as a timed rollback rehearsal in staging.
4. **Give the board verifiable gates.** Commit to a 30-day follow-up showing completed fixes, mandatory pre-migration abort criteria, and updated reliability metrics before any major migration runs again.

**A line you can use with the board:**
> "A €2 million, 9-hour outage is unacceptable, and as CTO I own it. Firing the lead who ran the migration won't fix why our process allowed a 9-hour failure—it strips out the knowledge we need to harden the system and teaches teams to hide problems. Give me five days to bring you the factual timeline, the system gaps behind the 9-hour recovery, and dated, testable controls—starting with mandatory timed rollback rehearsals."

I've saved a ready-to-send board memo in [board-accountability-note.md](file:///G:/agy-bench/ws/1d5fb5d36e29/board-accountability-note.md).

**Key assumptions:** No deliberate negligence or ignored warnings occurred, and the 9-hour / €2 million figures are confirmed. What am I missing, and what would make this wrong?
