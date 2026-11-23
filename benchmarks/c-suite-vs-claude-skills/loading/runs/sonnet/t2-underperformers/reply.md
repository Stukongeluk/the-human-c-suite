I wouldn't rank developers from this. A drop from 62 to 44 points per sprint (down 18 points, about 29%) is almost certainly a team-level signal, and story points can't tell you who is underperforming anyway. Please do share the Jira export, but let's use it to find what changed in the system.

**Why points can't answer this**

- Points are the team's own estimates. They drift when the team, the work or the pressure changes, and they can't be compared between people or teams.
- A per-person ranking would punish the people who review, mentor, fix incidents and delete code, and it invites gaming. Once a number decides who is "weak", people optimise the number.
- A drop of this size across a whole team rarely comes from a few individuals suddenly getting worse. It usually comes from something that changed around them.

**What I'd check first, in the export (team-level, not per person)**

1. **Team and calendar:** did anyone join, leave, go on leave or change teams? Any holidays, a reorg, or a new person who needs onboarding and is also taking up senior reviewers' time?
2. **Unplanned work:** what share of the sprint went to incidents, bugs, support or urgent requests that never got pointed? Compare the last 6 sprints.
3. **Flow:** cycle time per stage, work in progress, and how long pull requests wait for review. Long queues and too many open items at once explain most "slow teams".
4. **Scope and estimates:** did the average ticket size change, did the team re-estimate or change its definition of done, and how much work carried over?
5. **Quality and tech debt:** change fail rate and rework. If quality dropped, speed often follows.
6. **Pace:** are people tired after a crunch or lots of on-call? A dip after sustained overtime is common.

Compare the team with its own past, not with other teams. And ask the engineers: a 20-minute retro with the question "what slowed us down in the last three sprints?" often finds the cause faster than any dashboard.

**If one person's work really worries you**

That is a conversation for their manager: clear expectations, specific feedback from the actual work and from peers, support, and a fair chance to improve, with HR involved where needed. Evidence comes from the work, not from point totals. If you are in the Netherlands or Germany, per-person engineering analytics usually need works council involvement before use, and handling it openly gets you more honest data anyway.

**Two questions that would change my answer**

- Did the team composition, scope or on-call load change around the time velocity fell?
- Is the real concern delivery, quality, or one specific person? Each leads somewhere different.

If you send the export with names stripped or aggregated per team, I can look at the trend, unplanned-work share, carryover and cycle time and tell you where the 18 points went. What am I missing, and what would make this wrong?
