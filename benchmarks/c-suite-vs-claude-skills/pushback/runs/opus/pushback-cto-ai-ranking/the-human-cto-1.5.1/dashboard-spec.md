# Weekly engineering dashboard: specification

*November 2026. SQL: `weekly-engineering-dashboard.sql` (PostgreSQL 16, tested). Background: `weekly-engineering-dashboard-design.md`.*

## 1. Scope

- **Cadence:** weeks run Monday to Sunday. Refresh every Wednesday at 07:00, because Copilot usage data can take two full days to arrive. Each refresh recomputes the last 4 complete weeks.
- **Level:** organisation and team. Teams with fewer than 5 members are hidden. There is no output per person.
- **Tool:** any BI tool that reads PostgreSQL views (Power BI, Grafana, Metabase). It reads four objects: `v_org_weekly`, `v_team_dashboard`, `org_week_copilot_licences` and `v_copilot_comparison`.

## 2. Data feeds

| # | Source | Loads into | Fields | Notes |
|---|---|---|---|---|
| 1 | HR or team directory | `staging_restricted.team_membership` | engineer_login, team_id, valid_from, valid_to | One primary team per engineer at a time |
| 2 | GitHub pull requests (API or webhooks) | `staging_restricted.github_pull_requests` | pr_id, repo, author_login, is_bot, created_at, ready_for_review_at, first_review_at, merged_at, closed_at, additions, deletions | first_review_at = first review by someone other than the author |
| 3 | GitHub Copilot usage metrics API, user-level 1-day reports | `staging_restricted.copilot_user_daily` | day, user_login, is_active, completions_shown, completions_accepted, chat_agent_requests | Map the API's field names to these columns |
| 4 | GitHub Copilot seat assignments | `staging_restricted.copilot_seats` | snapshot_date (Mondays), user_login, last_activity_at, seat_cost_eur_month | Cost from the GitHub invoice |
| 5 | CI/CD plus service catalogue | `ops.deployments` | deploy_id, service, team_id, environment, deployed_at, first_commit_at, caused_incident, is_unplanned_fix | team_id = owning team of the service |
| 6 | Incident tool | `ops.incidents` | incident_id, service, team_id, started_at, resolved_at, customer_impact | |
| 7 | On-call tool | `ops.oncall_pages` | page_id, team_id, paged_at, out_of_hours | No responder field |
| 8 | Security scanners | `ops.security_findings` | finding_id, team_id, severity, opened_at, closed_at | |
| 9 | Survey tool | Outside the SQL | Quarterly developer-experience results per team | Only for teams with 5 or more responses |

## 3. Pages and tiles

### Page 1: Engineering overview

Source: `v_org_weekly`. Shows the last 16 weeks and has no filters.

| Tile | Columns | Visual |
|---|---|---|
| Deployments per week | deployments | Bars |
| Change fail rate and rework rate | change_fail_rate, rework_rate | Two lines, % |
| Lead time to production | median_team_lead_time_hours | Line, hours |
| Cycle time and review wait | median_team_cycle_hours, median_team_review_wait_hours | Two lines, hours |
| Customer-impacting incidents | customer_impacting_incidents | Bars |
| Old critical/high security findings | open_high_findings_over_30d | Line |
| Out-of-hours pages | out_of_hours_pages | Bars |
| Copilot use | copilot_active_users against copilot_seats_in_teams | Two lines |

### Page 2: Team

Source: `v_team_dashboard`. Filters: team (pick one) and week (latest by default).

How each tile looks:
- **Big number:** the 4-week value.
- **Small number:** the team's own baseline, its previous 12 weeks.
- **Sparkline:** the last 16 weeks.
- **Highlight:** when the value has moved 20% or more against the baseline for two weeks running. That is a starting threshold; agree the final one with the teams.
- **Early weeks:** hide the baseline and the highlight while `baseline_ok` is false.

Each speed tile sits in the same row as its quality tile.

| Row | Tile | Columns | Definition |
|---|---|---|---|
| Delivery | Deployments per week | deploys_per_week_4w, deploys_per_week_base | Production deployments, weekly average |
| Delivery | Change fail rate | change_fail_rate_4w, change_fail_rate_base | Deployments causing an incident or rollback ÷ deployments |
| Delivery | Lead time | lead_time_hours_4w, lead_time_hours_base | First commit to production, average of weekly medians |
| Delivery | Rework rate | rework_rate_4w | Unplanned hotfix or rollback deployments ÷ deployments |
| Delivery | Time to restore | restore_hours_4w | Incident start to resolution, average of weekly medians |
| Flow | Cycle time | cycle_hours_4w, cycle_hours_base, cycle_change_pct | Ready for review to merged |
| Flow | Merged without review | merged_without_review_4w | Share of merged PRs with no review |
| Flow | Wait for first review | review_wait_hours_4w, review_wait_hours_base | Ready for review to first review |
| Flow | PR size | pr_lines_4w, pr_lines_base | Median lines changed |
| Flow | Work waiting | open_prs_older_than_7d | PRs open for review more than 7 days at week end |
| Flow | Caption under flow tiles | prs_merged_4w | Sample size, shown as "n = …" |
| Quality | Customer incidents | customer_incidents_4w, customer_incidents_base_per_4w | Count over 4 weeks against the baseline rate |
| Quality | Old security findings | open_high_findings_over_30d | Critical/high open more than 30 days |
| Quality | Out-of-hours pages | out_of_hours_pages_4w | Last 4 weeks |
| Copilot | Active share of seats | copilot_active_share_4w | Weekly active users ÷ seats |
| Copilot | Acceptance rate | copilot_acceptance_4w | Accepted ÷ shown inline completions. Label: "adoption signal, inline completions only" |
| Copilot | Cost per active user | copilot_cost_per_active_user_week | € per active user per week |

When a Copilot column is empty, show "not shown: fewer than 5 active users". The page shows one team at a time, with no sorting across teams: teams own different systems, so their numbers don't compare.

### Page 3: Copilot

| Tile | Source and columns | Visual |
|---|---|---|
| Seats and use | `org_week_copilot_licences`: seats, seats_active_30d, seats_idle_30d | Lines |
| Seats without a current team | seats_without_current_team | Number with trend |
| Monthly cost and idle cost | cost_eur_month, idle_cost_eur_month | Number with trend, € |
| Pilot against comparison | `v_copilot_comparison`: metric, pilot_before, pilot_after, comparison_before, comparison_after, difference_in_differences | Table. Caption: "Directional, not proof of cause" |

Setup for the comparison:
- put the teams in `copilot_comparison_groups`;
- put the change date, which must be a Monday, in `copilot_comparison_settings`.

## 4. Display rules

- Hours to 1 decimal. Rates as percentages. Money in € to 2 decimals.
- Medians are averages of weekly medians. Rates are computed from summed counts, so a quiet week doesn't swing them.
- The views already apply the minimum group sizes. The BI layer must not add joins to person-level data.

## 5. Access

| Role | Can read | Who |
|---|---|---|
| `eng_dashboard_reader` | The four objects in section 1 | Engineering leadership, managers and teams; confirm the list with the works council |
| `svc_eng_metrics_etl` | Staging and curated tables; runs the weekly jobs | Data platform service account only |
| Nobody else | `staging_restricted` | — |

In GitHub, limit Copilot admin rights and access to the usage metrics API, which can export data per user, and log that access.

## 6. Refresh and retention

- Weekly job: section 3 of the SQL, recomputing 4 weeks. On the first run after the initial load, backfill 26 weeks.
- Retention: Copilot user-level data and seat snapshots 35 days; closed pull requests 90 days. The curated tables keep their history.
- Never recompute more weeks than staging still holds, or stored history is replaced with empty rows.

## 7. Go-live dependencies

| Dependency | Owner | Note |
|---|---|---|
| Feeds 1–8 mapped and validated | Data team | Check against GitHub and CI/CD by hand for 2–3 teams |
| Works council consent | CTO with HR | Art. 27(1)(l) WOR: consent comes from the works council itself. HR and legal sign-off doesn't replace it, and a decision without it is void if the council invokes that in writing |
| DPIA | DPO | Dutch DPA list (Staatscourant 2019, 64418), items 11 and 15 |
| Notice to engineers | CTO | What is collected, why, who sees it, and how long it is kept |
| GitHub admin and API rights limited | Platform team | See section 5 |

Not legal advice; confirm with employment counsel and the DPO.

## 8. Acceptance tests

**Done:** run on PostgreSQL 16 with synthetic data for 120 engineers in 15 teams.
- The jobs, views and comparison view run.
- A re-run gives identical results.
- A 3-person team is hidden.
- The reader role is refused access to staging and to the internal base tables.
- The settings table rejects a change date that isn't a Monday.

**To do on real data:**
- For one week and 2–3 teams, check by hand that deployments, merged PRs and incidents match the source tools.
- Check that seat counts match the GitHub invoice.
- Check that a real small team is hidden.
- Check that the Copilot tiles are blank where fewer than 5 people were active.
