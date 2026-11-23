I'd still not build that one, because a name column that managers can open is the individual ranking with an extra click. Everything I said about the data still applies, and the anonymised front page adds nothing: the people at the bottom are named the moment a manager opens the column. Even without it, with teams of 6 to 10 people, an "anonymous" rank is easy to guess. It also changes the legal position. It is a per-person performance record, so the works council consent question (art. 27(1)(l) WOR) and a GDPR purpose and impact assessment become harder, not easier. I'd tell the works council exactly what you are proposing before you decide, because "anonymised, but managers can open names" is the first thing they will ask about.

**What I'd build for the managers instead**

1. **The team dashboard from reply 2, unchanged.** It shows where delivery is stuck and which teams are drifting from their own baseline.
2. **A manager drill-down by work item, not by person.** For a flagged team, the manager sees the slowest-reviewed PRs, the biggest PRs, the rework chains and the incidents. This shows what is behind the trend (a queue, a hard service, an overloaded reviewer), and the manager already knows who worked on it.
3. **For a real concern about a person,** the manager looks at that person's actual work in the Git host and the review comments, asks peers, and sets clear expectations with a review date. This is a conversation with HR, and the evidence is specific and defensible. A rank in a column is neither.

SQL for point 2, per flagged team (untested, adjust to your schema):

```sql
SELECT pr.id, pr.repo, pr.lines_changed,
       extract(epoch FROM pr.first_review_at - pr.opened_at)/3600 AS review_wait_h,
       extract(epoch FROM pr.merged_at - pr.first_commit_at)/3600 AS lead_time_h,
       pr.is_fix_of_recent_change AS is_rework
FROM pull_requests pr
WHERE pr.team_id = :team_id
  AND pr.merged_at >= current_date - interval '4 weeks'
ORDER BY review_wait_h DESC NULLS LAST
LIMIT 20;
```

I deliberately leave out the author column. If a manager wants to know who wrote a PR, the Git host already shows it, and they have the context to read it.

If your aim is accountability, I'd make the team lead the accountable role for the team's trends, with a quarterly review against each team's own baseline.

What would make this wrong: if you have a specific engineer or group you already believe is a problem, the right route is point 3, and I can help you prepare it. Is that the case, and what am I missing?
