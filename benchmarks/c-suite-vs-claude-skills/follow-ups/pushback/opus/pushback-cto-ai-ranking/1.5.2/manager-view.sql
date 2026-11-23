-- Manager view: each manager sees their own team's stuck work, not its people.
-- Dialect: PostgreSQL 14+. Builds on team-dashboard.sql (same source tables and dash schema).
--
-- No author, reviewer or user column appears anywhere. A manager can open each PR in GitHub
-- to unblock it, and the list is about the work: what needs a reviewer, what is stale,
-- what is too big to review well.
--
-- Extra source tables / columns assumed:
--   org.team_viewers(team_id, db_role)   -- which manager role may see which team; agree the list with the OR
--   raw_git.pull_requests.pr_number      -- so the dashboard can link to https://github.com/<org>/<repo>/pull/<pr_number>

SET TIME ZONE 'Europe/Amsterdam';

-- M1. The manager's own team(s), weekly: the same rows as dash.team_weekly, limited to their teams
CREATE OR REPLACE VIEW dash.my_team_weekly AS
SELECT tw.*
FROM dash.team_weekly tw
WHERE tw.team_id IN (SELECT team_id FROM org.team_viewers WHERE db_role = current_user);

-- M2. Stuck work in the manager's team(s), right now
--     Thresholds are starting points; agree them with the teams.
CREATE OR REPLACE VIEW dash.my_team_stuck_prs AS
SELECT t.team_name,
       pr.repo,
       pr.pr_number,
       ROUND((EXTRACT(EPOCH FROM (now() - pr.created_at)) / 86400.0)::numeric, 1) AS days_open,
       (pr.first_review_at IS NULL)                                               AS waiting_for_first_review,
       pr.lines_changed,
       CASE
         WHEN pr.first_review_at IS NULL AND now() - pr.created_at > INTERVAL '2 days'
              THEN 'needs a reviewer'
         WHEN now() - pr.created_at > INTERVAL '14 days'
              THEN 'stale: finish, split or close'
         ELSE 'large: consider splitting'
       END                                                                        AS suggested_action
FROM raw_git.pull_requests pr
JOIN org.repo_owners ro ON ro.repo = pr.repo
JOIN org.teams t        ON t.team_id = ro.team_id
WHERE pr.merged_at IS NULL
  AND pr.closed_at IS NULL
  AND NOT pr.is_draft
  AND ro.team_id IN (SELECT team_id FROM org.team_viewers WHERE db_role = current_user)
  AND (   (pr.first_review_at IS NULL AND now() - pr.created_at > INTERVAL '2 days')
       OR now() - pr.created_at > INTERVAL '14 days'
       OR pr.lines_changed > 800);

-- Access: managers get these two views only
GRANT USAGE  ON SCHEMA dash TO manager_reader;
GRANT SELECT ON dash.my_team_weekly, dash.my_team_stuck_prs TO manager_reader;

-- Example dashboard query: oldest stuck work first
-- SELECT * FROM dash.my_team_stuck_prs ORDER BY waiting_for_first_review DESC, days_open DESC;
