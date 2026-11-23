# Engineer ranking dashboard: spec

**What:** a weekly ranking of every in-scope engineer on Copilot acceptance rate and merged PRs. The bottom 10% are flagged for a PIP decision by their manager.
**Main view:** anonymised, showing engineer codes instead of names. The name column is filled only for the engineer's own manager, and for CTO/HR (section 2).
**SQL:** `engineer_ranking_dashboard.sql` (PostgreSQL 16, tested; see section 9)
**Run:** daily loads, a snapshot every Thursday, manager decisions by Friday

---

## 1. How the score works

| Step | Rule | Default (in `perf.settings`) |
|---|---|---|
| Window | Rolling window ending with the last completed Mon–Sun week | 4 weeks (`window_weeks`) |
| Metric A | Merged PRs ÷ available days. Available days are weekdays not marked unavailable, × FTE. Only human-authored PRs count | weight 0.5 |
| Metric B | Copilot acceptance rate: acceptances ÷ generations over the window, from GitHub's per-user report | weight 0.5 |
| Normalise | Each metric becomes a percentile (0 = lowest, 1 = highest) within the peer group | peer group = job level (`rank_within`) |
| Composite | Weighted sum of the two percentiles, then ranked within the peer group | |
| Bottom flag | Lowest ⌈10% × peer-group size⌉. All ties at the cut-off are included | `bottom_share` 0.10 |
| Active PIP | People already on a PIP are still ranked and shown. They are **not** re-flagged, so the list doesn't refill every week | |
| PIP decision | Each flagged engineer goes to their manager's queue. The manager records `start_pip` or `no_pip` with a written reason | |

**Why "per available day" and not raw merged PRs:** a raw count ranks leave and contract hours, not work. Someone back from two weeks' holiday, or on a 0.8 contract, would sit in the bottom 10% automatically. In testing, an engineer with two weeks' leave in the window ranked mid-table on the normalised rate.

### Who is not ranked, and why

On the named pages (CTO/HR, and each manager for their reports), every excluded engineer appears with the reason, so nobody is silently missing. The anonymised main view shows only the count per reason, because a reason like "joined less than 90 days ago" identifies the person.

| Status | Rule | Why |
|---|---|---|
| out of scope | `org.engineer.in_scope = false` | managers, contractors and similar |
| joined less than 90 days ago | start date within `new_joiner_days` | still onboarding, and the window is incomplete |
| available less than 50% of the window | `min_available_share` | too few days to rate |
| fewer than 50 Copilot generations | `min_copilot_generations` | no Copilot use, or not enough to compute a rate. This covers e.g. mainframe work with no Copilot |
| Copilot telemetry incomplete | any day in the window with `client_telemetry_present = false` | GitHub drops detailed IDE activity when telemetry is off, so the rate would be wrong |
| peer group under 10 people | `min_peer_group_size` | percentiles across fewer than 10 people swing on one person |

## 2. Dashboard pages

### Page 1: Main ranking, anonymised (everyone with dashboard access). Source: `perf.v_ranking_anon`

- **Columns:**
  - engineer code (e.g. `E-3AC3B067`)
  - peer group (level), rank (`rank_from_top` of `peer_group_size`), `rank_change`
  - composite score and both percentiles
  - PRs per available day, Copilot acceptance rate
  - bottom-10% flag, `weeks_in_bottom_last_8`
  - **Name**, the "hidden" column
- **Left out on purpose,** because each one can identify someone in a team of 6–10:
  - name, team and manager
  - available days, and the raw PR count (available days can be worked out from it)
  - PIP status and decisions
  - not-ranked rows
- **The Name column:** left-join `perf.v_engineer_names` on `engineer_code`. Every dashboard role may query it, but the database only returns rows to:
  - the engineer's own manager (`perf_manager`)
  - CTO and HR (`perf_full_reader`)

  For everyone else the column is blank. Set `names_visible_to = 'all_managers'` to let any manager see every name.
- **Why not a hidden column in the BI tool:** in Power BI, Tableau or Looker, a hidden column is a display setting, not a permission. Anyone who can open the report can unhide it, use "show data" or export the table. Here the database decides, per user.
- **Requirement:** the BI tool must query as the individual user, through SSO pass-through, user impersonation or per-user credentials. If it connects through one shared service account, everyone gets that account's view.
- **Default sort:** peer group, then rank. Filter: bottom only. Bottom rows red.
- **Trend:** `perf.v_ranking_anon_history` gives the 8-week rank and composite per engineer code. Codes are random and stay the same across weeks.

### Page 1b: Ranking with names (CTO, HR). Source: `perf.v_ranking_current`

- **Columns:**
  - rank (`rank_from_top` of `peer_group_size`)
  - name, team, level
  - composite score
  - merged PRs, available days, PRs per available day
  - Copilot acceptance rate and generations
  - reviews given (context, not scored)
  - `rank_change` against last week
  - `weeks_in_bottom_last_8`
  - PIP status, manager decision
- **Default sort:** peer group, then rank. Filters: team, level, status, bottom only.
- **Highlighting:** bottom-10% rows red. Rows on an active PIP get a separate marker. Not-ranked rows grey, with the reason.

### Page 2: Engineer drill-down with names (CTO, HR). Source: `perf.v_ranking_history`

- An 8-week line for rank and composite, and the two metrics as separate lines.
- Available days and reviews given per week alongside. These are what explain most drops.

### Page 3: Review queue (managers, own reports only). Sources: `perf.v_my_review_queue`, `perf.v_my_reports`

- Flagged engineers with no decision yet, with the context columns from page 1.
- A form writes to `pip.manager_review`: decision plus a reason of at least 20 characters.
- `decided_by` is set automatically and cannot be set to anyone else.
- On `start_pip`, the manager adds a row to `pip.enrolment` with the start date. Close it with `ended_on` and `outcome`.

### Page 4: Data quality (everyone with dashboard access; counts only). Source: `perf.v_not_ranked`

- Not-ranked counts by reason, per week. A jump in "telemetry incomplete" or "available less than 50%" usually means a broken feed, not a change in people.

### Page 5: Settings and audit

- Current `perf.settings`. Every snapshot stores the exact settings it used in `settings_used`, so any past ranking can be explained.

## 3. Data sources and loading

| Table | Source | Frequency | Notes |
|---|---|---|---|
| `org.engineer` | HR system export | nightly | login, employee ID, name, team, level, manager's database login, FTE, start/end, in scope |
| `org.unavailable_day` | HR leave/absence | nightly | one row per unavailable weekday (leave, sick, parental, training, public holiday). No reason stored |
| `gh.pull_request`, `gh.pr_review` | GitHub API or webhooks | nightly | mark bot accounts `is_bot = true` |
| `copilot_raw.user_day` | GitHub Copilot usage metrics, per-user 1-day report | daily | final after three full UTC days. Kept 120 days (`raw_retention_days`) |
| `pip.manager_review`, `pip.enrolment` | written by managers through the BI form or a small internal app | as decided | protected by row-level security |

## 4. Weekly runbook

| When | What | Who |
|---|---|---|
| Daily | Load the source tables | data pipeline |
| Thursday 06:00 | `CALL perf.take_snapshot();`, which snapshots the previous Mon–Sun week. It refuses to run earlier, because GitHub's Copilot data isn't final until then | scheduler |
| Thursday | Dashboard refresh. Managers get a notification if their queue isn't empty | BI tool |
| By Friday | Managers record a decision for every engineer in their queue | engineering managers |
| Monday | HR checks that every queue is empty | HR |

To re-run a past week (e.g. after a late HR feed): `CALL perf.take_snapshot('2026-11-09');`. This replaces that week's snapshot. Manager decisions are kept.

## 5. Settings reference

| Setting | Default | Effect of changing it |
|---|---|---|
| `window_weeks` | 4 | `1` gives a pure single-week ranking. It is noisier, and one week of leave knocks people out: in testing, 2 people were excluded for availability with a 1-week window, against 1 with 4 weeks |
| `bottom_share` | 0.10 | share flagged per peer group |
| `weight_merged_prs` / `weight_copilot` | 0.5 / 0.5 | must add up to 1 (enforced) |
| `rank_within` | `job_level` | `org` ranks everyone in one pool. Juniors and staff engineers are then compared directly |
| `min_peer_group_size` | 10 | smaller groups are shown but not ranked |
| `min_available_share` | 0.5 | |
| `min_copilot_generations` | 50 | per window |
| `new_joiner_days` | 90 | |
| `raw_retention_days` | 120 | per-user Copilot rows older than this are deleted at each snapshot |
| `names_visible_to` | `own_reports` | `all_managers` lets any manager open every name on the main view. CTO/HR always see all names |

## 6. Access

| Role | Sees | Can write |
|---|---|---|
| `perf_viewer` (anyone else you give the dashboard) | anonymised main view and history, not-ranked counts. The name column is empty | nothing |
| `perf_manager` (engineering managers) | everything `perf_viewer` sees, plus: names on the main view for their own reports, `v_my_reports` and `v_my_review_queue` | decisions and enrolments for their own reports only, as themselves |
| `perf_full_reader` (CTO, HR) | everything above, with all names: named ranking, history, all review queues, all decisions and enrolments | nothing |
| no role | nothing | nothing |

No role can read `org`, `gh`, `copilot_raw` or the code-to-login table `perf.pseudonym`. Give each person their own database login, or have the BI tool pass the user through, so that `current_user` scoping works. This matters most for the name column: it is the only thing standing between a viewer and the names.

To log every name lookup, enable the optional pgaudit block at the end of section 8 of the SQL. It was not tested, because pgaudit isn't installed in the test environment.

## 7. Go-live checklist

- [ ] HR absence feed live and backfilled for at least the first window. Without it, everyone who was on leave ranks low.
- [ ] Copilot IDE telemetry on for all engineers. Check page 4 after the first load.
- [ ] Bot accounts listed and marked.
- [ ] `manager_db_user` filled for every engineer, and every manager has a login with `perf_manager`.
- [ ] BI tool queries as the individual user, not a shared service account. Test it with a viewer account: the name column must be empty.
- [ ] Two shadow snapshots, seen only by CTO and HR, to check exclusions and the feeds before managers see the ranking.
- [ ] Paperwork behind legal's sign-off filed with the project: works council decision, DPIA, notice to engineers. This is the first thing asked for if a PIP is contested.

## 8. Known limitations

- `org.engineer` holds current state. Re-running an old week uses today's team and level, but snapshots already taken keep what they recorded.
- Copilot acceptance is GitHub's accept actions ÷ generations. It mixes inline completions and chat code blocks. Copilot CLI usage is not part of the IDE metrics.
- Only weekdays count. Public holidays and company closure days go in `org.unavailable_day`.
- All dates use Europe/Amsterdam time.
- The main view is pseudonymised, not anonymous. Team, manager, absence and PIP status are kept off it. Even so, someone who knows a colleague's level and roughly how many PRs they merge can sometimes match a code to a person, especially in small levels such as Staff. Under GDPR the main view still counts as personal data, so give `perf_viewer` only to people who need the ranking.
- `compute_ranking` took about 2.4 s for 120 engineers. That is fine for a weekly job. The dashboard views read snapshots and return in milliseconds.

## 9. Testing

Tested on PostgreSQL 16.15 with synthetic data: 120 engineers in 4 job levels, of whom 24 were 0.8 FTE. The data had about 4,000 PRs with reviews and about 9,300 Copilot user-days.

- **Data volume:** 9 weekly snapshots back-filled, 1,076 snapshot rows.
- **Bottom flag:** exactly ⌈10%⌉ flagged per peer group (5 of 45, 5 of 50, 2 of 12). The 8-person Lead group was shown but not ranked.
- **Exclusions** all came back with the right reason:
  - a new joiner
  - an out-of-scope engineer
  - an engineer away more than 50% of the window
  - a no-Copilot engineer
  - an engineer whose Copilot telemetry was off

  An engineer with two weeks' holiday in the window was ranked on the normalised rate, mid-table.
- **Active PIP:** an engineer on an active PIP stayed ranked and in the bottom group but was not a new candidate.
- **Manager access:** a manager saw only their 20 reports and could record a decision for their own report. The database rejected these with an error:
  - a decision for another team's engineer
  - a spoofed `decided_by`
  - a reason under 20 characters
  - reading the full ranking or the raw tables
- **CTO access:** the CTO role saw everything and could write nothing.
- **Settings and safety checks:**
  - Switching to a 1-week window, an org-wide pool and 0.7/0.3 weights gave 12 of 114 flagged.
  - Weights that don't add up to 1 were rejected.
  - A snapshot of a week that wasn't final was refused.
  - The DDL runs twice cleanly.
- **Anonymised main view and name column** (re-tested on a fresh build with the same data):
  - 120 engineers got 120 distinct random codes, and the codes were unchanged after another snapshot.
  - The main view returned 107 ranked rows with no name, login, team, manager, absence or PIP columns.
  - Viewer account: name column empty (0 of 107). Refused on the code-to-login table, the named ranking and the manager views.
  - Claims manager: names for their own 17 ranked reports only. With `names_visible_to = 'all_managers'`, all 107, while the viewer stayed at 0.
  - CTO account: all names.
  - Upgrade: applying this version on top of the previous one, with snapshots already taken, worked cleanly. The next snapshot filled the codes.
