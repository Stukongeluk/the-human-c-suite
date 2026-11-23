That works, and it is a better design than named-by-default. Two things to know before the spec, because they change how you build it:

- **This is pseudonymised, not anonymous.** Because managers can reverse it, the data is still personal data under the AVG/GDPR, so the access rules and logging matter more than the masking. I'd also tell the OR and the DPIA that this is the design, since "managers can open names" is exactly the part they will ask about.
- **The main view must not carry identifying columns.** With 120 engineers, team + FTE + tenure + rank identifies most people at a glance. So the main view shows only the pseudonym, a team-size-safe grouping and rounded values. Team, exact FTE and tenure move to the restricted view.

## Spec

**Main view (all authorised dashboard users)**
- Pseudonym (for example `E-7F3A`), rotated every quarter so people can't be tracked across long periods by guesswork.
- Composite score band, PRs per FTE-week (rounded), acceptance rate (rounded to 1 percentage point), trend arrow, bottom-decile flag, rank.
- No team, no name, no tenure, no FTE. A division-level filter is allowed only when the group has at least 15 people.

**Restricted view (managers only)**
- Adds name, team and the manager's own reports only. A manager sees names for the people in their own reporting line, not the whole company. The CTO and the HR business partner see everyone.
- Opening names requires a stated reason (free text, or a pick from a list: "performance review", "calibration", "support request"). Every reveal is written to an audit log with who, when, which people and why.
- Quarterly review of the audit log by someone outside engineering (HR or the DPO).

**Controls**
- The pseudonym key lives in a separate table that the dashboard role cannot select directly; names are reachable only through a logged function.
- Reveal is limited to the bottom-decile population plus a person's own direct reports, so nobody can browse the full roster of names against scores.
- Engineers can request their own row (their own score, their own pseudonym).

## SQL (PostgreSQL)

This builds on the leaderboard query from the previous reply (call its output the `ranking_snapshot` table, with `login`, `team_id`, `run_date`, `composite_score`, `prs_per_fte_week`, `acceptance_rate`, `in_bottom_decile`).

```sql
-- 1) Pseudonym key, in a restricted schema the dashboard role cannot read.
CREATE SCHEMA IF NOT EXISTS restricted;

CREATE TABLE restricted.pseudonym_map (
    quarter      date    NOT NULL,                -- first day of the quarter
    login        text    NOT NULL,
    pseudonym    text    NOT NULL,
    PRIMARY KEY (quarter, login),
    UNIQUE (quarter, pseudonym)
);

-- Fill once per quarter with random, non-derivable IDs.
INSERT INTO restricted.pseudonym_map (quarter, login, pseudonym)
SELECT date_trunc('quarter', current_date)::date,
       e.login,
       'E-' || upper(substr(md5(gen_random_uuid()::text), 1, 4))
FROM engineers e
WHERE e.end_date IS NULL
ON CONFLICT DO NOTHING;
-- Check for rare collisions on the 4-character id; the UNIQUE constraint will reject them. Re-run to fill the gaps.

-- 2) Main view: pseudonym only, rounded values, no team or tenure.
CREATE VIEW public.engineer_ranking_main AS
SELECT
    s.run_date,
    pm.pseudonym,
    round(s.prs_per_fte_week, 1)        AS prs_per_fte_week,
    round(s.acceptance_rate, 2)         AS acceptance_rate,   -- 1 percentage point
    round(s.composite_score, 2)         AS composite_score,
    rank() OVER (PARTITION BY s.run_date ORDER BY s.composite_score DESC) AS overall_rank,
    s.in_bottom_decile
FROM ranking_snapshot s
JOIN restricted.pseudonym_map pm
  ON pm.login = s.login
 AND pm.quarter = date_trunc('quarter', s.run_date)::date;

-- The view is owned by a privileged role; the dashboard role gets SELECT on the view only,
-- and no privileges on restricted.pseudonym_map.
GRANT SELECT ON public.engineer_ranking_main TO dashboard_reader;

-- 3) Audit log for reveals.
CREATE TABLE restricted.reveal_log (
    id            bigserial PRIMARY KEY,
    revealed_at   timestamptz NOT NULL DEFAULT now(),
    requested_by  text        NOT NULL,       -- session_user
    pseudonym     text        NOT NULL,
    reason        text        NOT NULL CHECK (length(reason) >= 10)
);

-- 4) Managers-only reveal function (SECURITY DEFINER, so the manager role never touches the map).
--    manager_reports(manager_login, report_login) tells who may be revealed to whom.
CREATE OR REPLACE FUNCTION public.reveal_engineer(p_pseudonym text, p_reason text)
RETURNS TABLE (pseudonym text, name text, team_name text)
LANGUAGE plpgsql SECURITY DEFINER
SET search_path = restricted, public
AS $$
DECLARE
    v_login text;
BEGIN
    SELECT pm.login INTO v_login
    FROM restricted.pseudonym_map pm
    WHERE pm.pseudonym = p_pseudonym
      AND pm.quarter = date_trunc('quarter', current_date)::date;

    IF v_login IS NULL THEN
        RAISE EXCEPTION 'Unknown pseudonym';
    END IF;

    -- Authorisation: own direct reports, or an HR/CTO role.
    IF NOT (
        EXISTS (SELECT 1 FROM manager_reports mr
                WHERE mr.manager_login = session_user AND mr.report_login = v_login)
        OR pg_has_role(session_user, 'hr_or_cto', 'member')
    ) THEN
        RAISE EXCEPTION 'Not authorised to reveal this person';
    END IF;

    INSERT INTO restricted.reveal_log (requested_by, pseudonym, reason)
    VALUES (session_user, p_pseudonym, p_reason);

    RETURN QUERY
    SELECT p_pseudonym, e.name, t.team_name
    FROM engineers e
    JOIN teams t ON t.team_id = e.team_id
    WHERE e.login = v_login;
END;
$$;

REVOKE ALL ON FUNCTION public.reveal_engineer(text, text) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION public.reveal_engineer(text, text) TO manager_role, hr_or_cto;

-- 5) Quarterly audit report (for HR/DPO, not engineering).
SELECT date_trunc('month', revealed_at)::date AS month,
       requested_by,
       count(*)                               AS reveals,
       count(DISTINCT pseudonym)              AS distinct_people
FROM restricted.reveal_log
GROUP BY 1, 2
ORDER BY 1 DESC, reveals DESC;
```

Implementation notes:
- If your BI tool connects with one shared service account, `session_user` will not identify the manager. In that case pass the signed-in user through (for example `SET LOCAL app.current_user`, then use `current_setting('app.current_user')` in the function) or put the reveal behind your app's own SSO login.
- The "hidden column" in the BI tool should not be a hidden column over the same table, because anyone who can edit the report or export the dataset can unhide it. That is why the names sit behind the function and the separate schema.
- Reveals are scoped to direct reports, so a manager cannot cross-check a ranking against the whole company's names.

## Limits of this approach

- With rounded scores and a published rank, a manager who knows their own reports can often work out who is who in the main view anyway. Treat the pseudonym as protection against casual browsing, not against a determined reader.
- The reveal log tells you who looked, not whether the decision made afterwards was fair. Keep the manager's written context with each flagged person, as before.

If it helps, I can write the access-model section for the DPIA or the explanation for the OR, since those will be the first questions on this design.
