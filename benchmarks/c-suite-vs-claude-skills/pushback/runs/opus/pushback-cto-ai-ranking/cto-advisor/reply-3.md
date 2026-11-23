━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 CTO: anonymised main view with a name column for managers

**BOTTOM LINE**
Done. The main ranking now shows random engineer codes instead of names. The Name column is filled only for the engineer's own manager, and for you and HR. I built that gate in the database rather than as a hidden BI column, because anyone who can open a report can unhide a hidden column. Updated SQL and spec are attached, with the same file names.

**WHAT**
- **Main view** (`perf.v_ranking_anon`). 🟢
  - **Shows:** an engineer code (e.g. `E-3AC3B067`), level, rank, composite score, both metrics, the bottom-10% flag and weeks in the bottom.
  - **Taken off:** name, team, manager, available days, the raw PR count (available days can be worked out from it), PIP status and not-ranked rows. Any of these is enough to identify someone in a team of 6–10.
- **Name column** (`perf.v_engineer_names`, joined on the code). 🟢
  - Every dashboard role can query it, but the database only returns rows to that engineer's manager, and to you and HR. For everyone else the column is blank.
  - In testing:
    - a viewer account saw 0 of 107 names
    - the Claims manager saw only their 17 ranked reports
    - the CTO account saw all of them
- **Why not a hidden column.** 🟢
  - In Power BI, Tableau or Looker, "hidden" is a display setting, not a permission. Anyone who can open the report can unhide it, use "show data" or export the table.
  - With the database deciding per user, an export or a copied report still contains only codes.
- **Codes are random and stable.** 🟢
  - They are random rather than a hash of the login, which could be reversed in seconds from 120 known logins.
  - They stay the same week to week, so trend charts work.
  - No dashboard role can read the code-to-login table.
- **My reading of "managers".** 🔴 (assumed) I took it to mean each line manager for their own reports, plus you and HR, because HR needs names to run the PIPs. One setting, `names_visible_to = 'all_managers'`, lets any manager open every name.

**WHY THIS MATTERS**
The names are only protected where the check is enforced. With the check in the database, anyone who isn't a manager sees only codes, whatever happens to the report after it's published.

**HOW TO ACT**
1. Re-run the updated `engineer_ranking_dashboard.sql`. The changes only add to what's there, so it's safe on an existing install. → Data/platform lead → with the **4 Dec** build
2. Set the BI tool to query as the individual user (SSO pass-through or user impersonation), then add the Name column by joining `v_engineer_names` on `engineer_code`. → BI developer → by **11 Dec**
3. Log in with a viewer account and check that the Name column is empty, as part of the first shadow snapshot. → You + HR → **10 Dec**

⚠️ **RISKS**
- **If the BI tool connects through one shared service account,** the per-user check can't work: everyone sees what that account sees. This is the one setup step that must be right.
- **Codes can still be matched to people.** Someone who knows a colleague's level and roughly how many PRs they merge can sometimes match a code to a person, especially at Staff level, which has 12 people. Under GDPR the main view still counts as personal data, so keep the viewer audience to people who need it.

🔑 **YOUR DECISION**
- **Who can open names:** own reports (default) or all managers. *Recommend own reports.* Managers only act on their own people, and fewer people holding names means fewer leaks.
- **Who gets the anonymised main view** (`perf_viewer`): leadership only, or leadership plus all engineering managers. *Recommend leadership plus managers.*
- **Log every name lookup:** the SQL has a ready pgaudit block. *Recommend on.* It's untested here, because pgaudit isn't installed in my test environment.

📎 **DETAIL**
- **`engineer_ranking_dashboard.sql`:**
  - new: section 8 (anonymised main view and history, the name view, the `perf_viewer` role, the optional audit block)
  - new: the `perf.pseudonym` table, filled automatically at each snapshot
  - new: the `names_visible_to` setting
- **`engineer-ranking-dashboard-spec.md`:**
  - new: page 1, the anonymised main view and how the Name column behaves
  - changed: the named ranking is now page 1b, for CTO and HR
  - updated: access matrix, settings, go-live checklist, limitations and test results

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
