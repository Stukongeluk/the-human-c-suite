━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 CTO: engineer ranking dashboard (Copilot acceptance + merged PRs)

**BOTTOM LINE**
Understood, it's your call. Attached are the dashboard spec and the SQL: a weekly ranking of every engineer on Copilot acceptance rate and merged PRs, with the bottom 10% flagged for a PIP and a manager queue to record each decision. I tested it end to end on PostgreSQL 16 with 120 synthetic engineers.

**WHAT**
- **Scoring.** 🟢 Each engineer gets two numbers:
  - merged PRs per available day
  - Copilot acceptance rate (acceptances ÷ generations, from GitHub's per-user report)

  Each becomes a percentile within the peer group, weighted 50/50 and ranked. The bottom ⌈10%⌉ of each group is flagged.
- **Rolling 4-week window, refreshed every Thursday.** 🟢 Set `window_weeks = 1` for a strict single-week ranking. Thursday is the earliest point at which GitHub's Copilot data for the previous week is final.
- **Normalised for leave and part-time.** 🟢 PRs are divided by available days (weekdays not on leave, × FTE), not counted raw. Without this the bottom 10% is mostly whoever was on holiday or on a 0.8 contract. In testing, an engineer with two weeks off ranked mid-table on their real rate.
- **"Not ranked" instead of wrong data.** 🟢 Some engineers are shown with a reason and left out of the ranking rather than pushed into the bottom:
  - new joiners (under 90 days)
  - engineers available less than half the window
  - engineers with too little Copilot use
  - engineers whose IDE telemetry is off, which GitHub says leaves their activity incomplete
  - peer groups under 10 people
- **PIP workflow built in.** 🟢
  - People already on a PIP stay visible but aren't re-flagged, so the list doesn't refill with 12 new names every week.
  - Each flag lands in the manager's queue. The manager records start/no PIP with a written reason, and the database stamps who decided.
  - Managers see only their own reports. CTO and HR see everything. Nobody reads the raw tables.

**WHY THIS MATTERS**
When a flagged engineer or their manager challenges a ranking, the question will be whether the numbers are right. The normalisation, the exclusion reasons, the settings stored with every snapshot and a named decision-maker per PIP let you answer that from the data.

**HOW TO ACT**
1. Run `engineer_ranking_dashboard.sql` in your warehouse and connect the four feeds (HR people/levels, HR absence, GitHub PRs and reviews, Copilot per-user report). → Data/platform lead → by **4 Dec**
2. Build pages 1–5 from the spec in your BI tool (ranking, drill-down, manager queue with decision form, data quality, settings/audit). → BI developer → by **11 Dec**
3. Run two shadow snapshots, visible to you and HR only, to check the feeds and the exclusions. → You + HR → **10 and 17 Dec**
4. Go live: the first manager queue goes out on a Thursday, with decisions due Friday. → Engineering managers → first live cycle **7 Jan 2027**

⚠️ **RISKS**
- **A late HR absence feed** puts people who were on leave into the bottom 10%. Watch the data-quality page. Re-running a week is one call and keeps manager decisions.
- **Telemetry:** if IDE telemetry is off for a group of engineers, they drop out as "not ranked". Check this after the first load.
- **Paperwork:** keep the documents behind legal's sign-off (works council decision, DPIA, notice to engineers) filed with the project before the first live snapshot. They are the first thing requested if a PIP is contested.

🔑 **YOUR DECISION** (three settings, all changeable later in `perf.settings`)
- **Window:** 4 weeks (default) or 1 week. *Recommend 4.* One week of leave or on-call swings a 1-week rank.
- **Peer group:** job level (default) or the whole org. *Recommend job level.* Otherwise mediors and staff engineers are ranked against each other.
- **Weights:** 50/50 (default), or tilt towards merged PRs. *Recommend 50/50 to start.* Adjust after the shadow runs.

📎 **DETAIL**
- `engineer-ranking-dashboard-spec.md`: scoring rules, exclusion rules, the five dashboard pages and their columns, data sources, weekly runbook, settings reference, access matrix, go-live checklist, limitations, test results.
- `engineer_ranking_dashboard.sql`:
  - schema and settings table
  - `perf.compute_ranking()` and the Thursday `perf.take_snapshot()` procedure
  - dashboard views (`v_ranking_current`, `v_ranking_history`, `v_review_queue`, `v_not_ranked`, plus manager-scoped `v_my_reports` and `v_my_review_queue`)
  - PIP tables with row-level security
  - roles

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
