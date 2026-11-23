I won't build that one. An anonymised main view with a manager-only column of names is the same individual ranking with a lock on it. The people ranked would still be scored on acceptance rate and merged PRs, and the bottom 10% would still be picked from it. The works council consent and "tell the people affected" points apply to the hidden column exactly as they do to a visible one.

What I can add that keeps your goal of managers knowing where to look:

**1. Manager view, own team only, trend not rank.** Each manager sees their team's lead time, review wait, change fail rate and out-of-hours pages against the team's own baseline. No names, no ordering of people.

**2. Engineers see their own data.** A personal page, visible only to that engineer: their merged PRs, reviews given, PR size, and their own Copilot usage. It is theirs to use in a 1:1, not a feed to management. This is the version that is easiest to agree with the works council, and it is what GDPR access rights already point towards.

**3. A conversation prompt for managers, built from the team view.** For example: "Review wait on your team went from 6 to 19 hours over 4 weeks. Ask the team what changed." Individual concerns then come from the manager's own knowledge of the work and from peer input.

**4. A fair route for individual concerns.** If a manager has a real concern about someone, it goes through expectations, regular feedback, support and a fair chance, with HR. The evidence is the person's work, such as reviews, incidents handled and delivered outcomes, not a rank.

SQL for the self-view (row-level security, so each engineer can only query their own row):

```sql
CREATE VIEW my_week AS
SELECT date_trunc('week', p.merged_at)::date AS week,
       COUNT(*)                              AS merged_prs,
       COUNT(*) FILTER (WHERE p.reviews_given > 0) AS prs_reviewed_help,
       percentile_cont(0.5) WITHIN GROUP (ORDER BY p.additions + p.deletions) AS median_pr_lines
FROM   pull_requests p
WHERE  p.author_login = current_setting('app.current_user')   -- set per session
GROUP  BY 1;
```

Is the aim to find out who needs support, or who to remove? If it's the first, the manager view plus the 1:1 does it. If it's the second, tell me which outcome you're trying to fix (delivery, quality or cost) and I'll build the evidence for that.

What am I missing, and what would make this wrong?
