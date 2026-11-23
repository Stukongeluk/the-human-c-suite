I wouldn't use the Jira export to find underperforming developers, and it can't really show you that anyway. A drop from 62 to 44 points (18 points, about 29%) is a team-level signal. Story points are the team's own estimates, so the first question is what changed in the work and the conditions around it, not who. A 29% drop does need explaining, especially if someone above you is asking, so here is the fastest way to explain it.

The trap: ranking people by points or tickets punishes the ones who review, unblock others and handle incidents, often the very people who absorbed whatever caused the drop. And from the next sprint on, everyone estimates higher.

**What usually explains a drop like this** (all of it can be checked in the export):

- **Less capacity than it looks.** Leave, sickness, someone leaving or joining (new people cost the team time before they add any), people lent to another project. Compare points per available person-day, not per sprint.
- **Unplanned work.** Bugs, incidents and support requests that are unpointed or pointed low. Compare the mix of issue types before and after the drop.
- **Carry-over.** Points only count when a story is done. One 13-point and one 5-point story slipping past the sprint boundary is already 18 points, and the next sprint then looks great. Compare committed with completed, and how much spilled over.
- **Waiting.** Time in review, QA or "blocked", and dependencies on other teams. Time-in-status from the changelog shows where work piles up.
- **Different work.** A migration, tech debt or discovery work that isn't pointed the way features are.
- **Estimation drift.** Re-calibrated points, a new estimator, stories split differently.
- **Noise.** If the last ten sprints ranged from 40 to 65, one or two low ones aren't a trend yet.

**What I'd do this week**

1. Share the export and I'll do the team-level analysis: the last 8 to 10 sprints, with issue type, story points, sprint, status-change history and created and resolved dates. Delete the assignee column first; I don't need names for this.
2. Ask the team in the next retro: "What slowed us down over the last few sprints?" Engineers usually know within ten minutes, and that's faster than any dashboard.
3. From now on, track cycle time, work in progress and the share of unplanned work, paired with a quality measure such as escaped defects or change fail rate. Velocity is useful for the team's own planning, but it's a poor performance measure.

**If the real worry is one specific person,** that needs a different route, and a dashboard isn't it. Their manager sets clear expectations, gives regular and specific feedback, offers support and a fair chance to improve, and brings in HR where needed. The evidence comes from the work itself and from peers, not from points. Also, using Jira data to judge individuals counts as performance monitoring. That raises data-protection questions everywhere, and in countries like the Netherlands and Germany it usually needs works council agreement.

My assumptions: the team, the way you estimate and your definition of done stayed roughly the same, and nobody has a concern about a specific person yet. What am I missing, and what would make this wrong?
