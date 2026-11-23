No hidden names column. An anonymised ranking that managers can unlock is the same per-engineer ranking with the names one click away, and under the GDPR pseudonymised data is still personal data.

What managers can open instead, new in `manager-view.sql` (tested on PostgreSQL 16):

- **`dash.my_team_stuck_prs`:** their own team's stuck work right now, meaning PRs waiting more than 2 days for a first review, PRs open more than 14 days, and PRs over 800 lines. Each row has the repo, PR number, days open and a suggested action ("needs a reviewer", "stale: finish, split or close", "large: consider splitting"). It has no author column, but they can open any PR in GitHub to unblock it.
- **`dash.my_team_weekly`:** the weekly team panel, limited to the teams that manager is mapped to.

Access is limited by role: each manager sees only their own team or teams and can't query the raw tables. In testing, the stuck-PR list matched a brute-force count exactly.

This is what a manager can act on on a Monday morning: assign reviewers, split big changes, close dead work. For a concern about a specific person, the improvement plan template from my last reply is the route, built on their work and their peers' feedback rather than a rank.

One question: what would managers do with the names that they can't already do from their 1:1s and the work itself? If there's a real gap there, I'd rather design for that.

What am I missing?
