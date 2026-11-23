# Selection: what I can and cannot give you

## Bottom line

I will not write a formula that ranks people by performance ratings and Copilot usage and cuts the lowest scorers. In a Dutch collective redundancy it is not a lawful selection method, and it would put the whole 60 at risk. Below is the selection method that is lawful, a scoring sheet you can run today, and the places where performance and tooling data can legitimately be used.

## Why that formula fails (these are the points that decide the outcome)

1. **Wrong selection rule.** For business-economic dismissals through UWV, selection must follow the afspiegelingsbeginsel: within each group of interchangeable roles, by age cohort, then shortest service first. UWV checks this. A selection by score is a deviation, and UWV will refuse the permits for everyone selected that way. Employees can also challenge in court, and a dismissal that rests on performance cannot be recast as a redundancy afterwards. (🟢 rule; confirm with your lawyer.)
2. **Copilot usage is not performance.** It measures tool activity, not output or quality. It penalises people who use other tools, work on non-code tasks, are in roles with little code, or work part-time. That is a weak and easily attacked basis even in a context where performance may count.
3. **Data and consultation problems.** Using individual usage telemetry for a dismissal decision is a new purpose for personal data, which raises GDPR (AVG) questions about purpose limitation and transparency. A system that monitors employees or assesses them also needs works council consent (WOR art. 27). If the OR did not agree to this use, the data is hard to use at all. (🟡: depends on what you agreed with the OR and what employees were told.)
4. **Last year's ratings.** Ratings given for development or pay purposes, without any expectation that they would decide a redundancy, are inconsistent across managers and will be examined for bias by age, gender, part-time status and sick leave. That adds discrimination risk to the file.

## The selection scoring sheet that works

Run this per department, per group of interchangeable roles.

1. **Define the group.** Roles that employees could take over from each other given their skills, level and pay (grouping decisions are yours and are reviewable; document the reasoning for each).
2. **Set the quota.** Cuts for the group = roles removed in that group (from your Phase 1 list).
3. **Split into cohorts.** 15-24, 25-34, 35-44, 45-54, 55+.
4. **Allocate cuts per cohort.** Cuts_cohort = Quota x (cohort headcount / group headcount). Round so the total equals the quota; allocate leftover seats to the cohorts with the largest remainders.
5. **Rank within cohort.** Order by length of service, shortest first. The first N in each cohort are selected.
6. **Apply documented exceptions.** A person may be kept out only if they hold a specific skill the company needs and cannot replace; the next person in the ranking takes their place. Record the reason per case.
7. **Lawyer sign-off** on groups, cohort counts and exceptions before anything is communicated.

A spreadsheet with these columns does it: person ID, group, birth date, cohort, start date, rank within cohort, selected (Y/N), exception reason.

## Where performance and Copilot data legitimately fit

- **Deciding which roles disappear (Phase 1).** Role selection is a business decision about the work, not the person. Usage, output and workload data at the team level can inform it. Do not tie roles to named individuals.
- **Documented exceptions.** If someone holds a critical skill, performance and delivery evidence can support keeping them, as a narrow per-person case.
- **Voluntary route.** In a voluntary-departure or settlement offer you may decline applications from people you cannot lose. You cannot push anyone into it on the basis of a score.
- **Where performance is the real issue.** Individuals with documented, long-standing performance problems go through a separate performance route (improvement plan, then dismissal for non-functioning). It is slower, it is separate from this 60, and a rushed attempt to fold it into the redundancy is the thing that creates the lawsuit.

## What happens if you do it your way

If UWV or an employee's lawyer sees that selection followed performance scores, the likely result is permits refused or dismissals annulled for those affected, a restarted process, back pay and legal costs, and a signal to the OR and unions that the whole procedure was not in good faith. The March date is then lost for all 60, not only for the people selected.

## What I need

- Whether the OR ever agreed to the Copilot telemetry and what the rating system was said to be used for.
- The HR data extract (ID, role, department, birth date, start date, contract) so the cohort table can be built.

If you give me the extract, I will produce the exact cohort allocation per group.

*Not legal advice; have your employment lawyer confirm before any selection is run.*
