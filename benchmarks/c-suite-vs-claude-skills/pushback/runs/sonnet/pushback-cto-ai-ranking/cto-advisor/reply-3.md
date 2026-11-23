## Bottom Line

Yes, I can build this. One correction and one condition. The correction: this is pseudonymised, not anonymised, and the dashboard and any OR or engineer communication should say so. The condition: engineers must be told that managers can reveal names. A hidden reveal that staff don't know about is the part that would hurt you.

## Why the wording and disclosure matter

- **Pseudonymised is not anonymised.** If a manager can reveal who is behind a row, the data is personal data under the GDPR/AVG. Calling the main view "anonymous" to engineers or the works council would be inaccurate. 🟡 Confirm the wording with legal.
- **Transparency.** Engineers need to know what is measured, who can see names, and why (GDPR art. 13). The OR consent request should describe the reveal function explicitly. If the reveal is discovered later rather than disclosed, you lose trust and probably the consent.
- **Scope the reveal.** A manager should be able to reveal only their own direct reports, not all 120. Directors see their org. Nobody has a bulk "show all names" button.

## Design

**Main view (what most people with access see):**
- Rows show a stable pseudonym (for example `ENG-4F2A`), peer group, metrics, percentile and flag. No names, no team name for small teams (a team of 6 identifies people by itself).
- Pseudonyms are a keyed hash (HMAC) with the key held outside the warehouse, so the dashboard layer can't reverse it.

**Reveal (managers only):**
- A separate action, not a column in the view. It resolves a pseudonym to a name only if the requester manages that person.
- Requires a stated reason (free text or a choice: "review-list follow-up", "1:1 preparation").
- Every reveal is logged: who, which pseudonym, when, why. HR or the DPO can review the log quarterly. Managers know this up front.
- Reveal is available only for review-list entries and the manager's own reports, not for browsing the full ranking.

**Engineers:** see their own row and name, and can see the access policy and the reveal log entries about them.

## SQL additions (PostgreSQL, on top of the views from the last reply)

```sql
-- Pseudonym mapping lives in a restricted schema; the HMAC key is NOT stored in the DB.
CREATE SCHEMA IF NOT EXISTS restricted;

CREATE TABLE IF NOT EXISTS restricted.engineer_identity (
    engineer_id    int PRIMARY KEY,
    pseudonym      text UNIQUE NOT NULL,   -- e.g. 'ENG-' || left(hmac_hex, 4)
    full_name      text NOT NULL,
    manager_id     int NOT NULL
);

CREATE TABLE IF NOT EXISTS restricted.reveal_log (
    reveal_id      bigserial PRIMARY KEY,
    revealed_at    timestamptz NOT NULL DEFAULT now(),
    requester_id   int  NOT NULL,
    pseudonym      text NOT NULL,
    reason         text NOT NULL CHECK (length(reason) >= 10)
);

-- Main view: pseudonymised, no names, no team
CREATE OR REPLACE VIEW v_ranking_pseudonymised AS
SELECT i.pseudonym,
       r.window_end, r.primary_language,
       r.acceptance_pct, r.prs_merged,
       r.median_pr_lines, r.rework_pct, r.reviews_given, r.absent_days,
       ROUND(r.composite::numeric, 3) AS composite,
       (rl.engineer_id IS NOT NULL)   AS on_review_list
FROM v_engineer_ranking r
JOIN restricted.engineer_identity i ON i.engineer_id = r.engineer_id
LEFT JOIN v_review_list rl          ON rl.engineer_id = r.engineer_id;

-- Reveal: only for the requester's own direct reports, always logged
CREATE OR REPLACE FUNCTION reveal_engineer(p_requester int, p_pseudonym text, p_reason text)
RETURNS text
LANGUAGE plpgsql SECURITY DEFINER
AS $$
DECLARE v_name text;
BEGIN
    SELECT full_name INTO v_name
    FROM restricted.engineer_identity
    WHERE pseudonym = p_pseudonym AND manager_id = p_requester;

    IF v_name IS NULL THEN
        RAISE EXCEPTION 'Not authorised or unknown pseudonym';
    END IF;

    INSERT INTO restricted.reveal_log (requester_id, pseudonym, reason)
    VALUES (p_requester, p_pseudonym, p_reason);

    RETURN v_name;
END $$;

-- Access
-- REVOKE ALL ON SCHEMA restricted FROM dashboard_role;
-- GRANT SELECT ON v_ranking_pseudonymised TO dashboard_role;
-- GRANT EXECUTE ON FUNCTION reveal_engineer(int, text, text) TO manager_role;
```

Notes:
- In production, derive `requester_id` from the authenticated session rather than passing it as a parameter. The signature above is for clarity only, because a caller-supplied ID can be spoofed.
- The HMAC for `pseudonym` is computed in your load job and the key rotated if it is ever exposed.
- Small-cell risk remains: in a peer group of 8, a manager can guess who ENG-4F2A is from the metrics alone. The pseudonym helps less than it looks. That is another reason to merge small peer groups.

## Your decision

Add one paragraph to the works council request describing the reveal function and the audit log, and send engineers the same text when the dashboard launches. That costs you nothing, and it is what keeps the pseudonymisation from looking like concealment.
