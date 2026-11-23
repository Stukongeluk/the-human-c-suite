I'd build a team-level Copilot dashboard that shows adoption next to delivery and quality, not a per-engineer ranking by acceptance rate. Acceptance rate measures how often someone presses Tab. It doesn't measure value, and it can rise while quality falls. A ranking would also reward the wrong people. Engineers who reject weak suggestions, review others' code, mentor or delete code would sit at the bottom, and everyone would learn to accept more.

I haven't seen your Copilot or repo data, so what follows is a design to build from, not a finished dashboard.

## What I'd build instead

**View 1: Adoption by team (the only place acceptance rate appears)**
- Seats paid, weekly active users and acceptance rate, per team and compared with that team's own past. Don't compare teams with each other, because codebases and domains differ.
- Seats unused for 30+ days, so you can right-size spend before buying more.

**View 2: Does it help? (the same teams, same period)**
- Change lead time, cycle time per stage, review wait time and pull-request size.
- Change fail rate, rework rate and escaping defects.
- Open security findings by age. AI-written code needs its own security gate.
- Pair every speed number with a quality number, so nobody can hit one by breaking the other.

**View 3: People**
- A short developer-experience pulse: where Copilot helps, where it gets in the way, and what people would change. Self-reported speed-ups are unreliable, so use this for friction rather than as proof of a gain.
- Time to onboard, and how juniors use it.

**Pilot design:** give a comparison group the same measures for 8 to 12 weeks, with agreed working rules (small PRs, tests, review for AI code). Only then decide what any gain is worth. Evidence so far says individual output often rises while review time and PR size grow with it (Faros AI, 2025), and DORA's 2025 report found AI amplifies the strengths and dysfunctions already in a team.

## Data and privacy
- Pull aggregated usage from the GitHub Copilot metrics API at team level, and join it to your CI/CD, Git host and incident data.
- GitHub's admin console shows per-person usage by default. Limit who can see those views.
- In the Netherlands, a tool that can show individual performance is a monitoring system, and it will likely need works council (OR) agreement. Agreeing the metrics up front with the engineers also makes the numbers more honest. This isn't legal advice.

## Two questions that would change my answer
1. What decision is this ranking meant to drive: renewing seats, finding who needs help adopting the tool, or judging performance? If it's seat spend, View 1 answers it. If it's performance, a dashboard is the wrong instrument, and a manager's conversations with the person and their peers are better.
2. What was the claim you need to test (for example, "Copilot makes us faster")? That tells me which View 2 metrics matter most.

If you still want individual numbers, a defensible compromise is for each engineer to see only their own usage, as a self-coaching tool, with no manager-visible ranking.

What am I missing, and what would make this wrong? If you already have team-level delivery data and an agreement with the engineers, I can turn this spec into queries and a first mock-up.
