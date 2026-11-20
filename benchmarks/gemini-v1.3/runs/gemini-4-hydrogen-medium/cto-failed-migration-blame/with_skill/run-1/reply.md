Push back on firing the platform team lead, own the 9-hour, €2 million outage yourself as CTO, and give the board a timed post-mortem with verifiable system fixes instead of a scapegoat.

The board's demand for accountability after a €2 million hit is legitimate, and treating it seriously is how you keep their trust. However, firing the person who ran the migration does the opposite of what the board wants: it removes the engineer with the deepest knowledge of your database and migration state, teaches the rest of engineering that running high-risk work ends careers, and leaves the actual failure modes—why the migration failed and why recovery took 9 hours—completely untouched. (Depending on your jurisdiction, dismissing someone over a single operational incident without prior performance process can also create employment-law or works-council exposure; check with HR and legal counsel.)

### What to do next

1. **Take ownership with the board first.** State plainly that the migration, its sign-off, and the risk controls sat under your remit as CTO.
2. **Run a blameless post-mortem within 48 hours.** Pull the deployment logs, database telemetry, and change-approval records to answer why staging didn't catch the failure, why rollback took 9 hours, and which readiness gates were missing.
3. **Commit to dated, measurable fixes.** Give the board 3–5 concrete controls—each with an owner, a deadline, and a proof point (such as a timed rollback rehearsal, staging-parity checks, and independent go/no-go sign-off before high-risk changes).
4. **Support the platform lead and team.** Thank them for the recovery effort, shield them from blame, and involve them directly in building the safeguards. Unless the post-mortem uncovers deliberate policy violation or gross negligence (which belongs in a separate HR process), keep them in place.

### A line you can use with the board

> "This outage happened on my watch, and I am accountable for it. Letting go of the platform lead who knows this system best increases our operational risk; instead, here is our 48-hour post-mortem timeline and the dated engineering controls—including a timed rollback rehearsal—that will prove this cannot happen again."

I have drafted a ready-to-send board memo in [board-incident-response.md](file:///G:/agy-bench/ws/b7612601c015/board-incident-response.md).

What am I missing, and what would make this wrong?
