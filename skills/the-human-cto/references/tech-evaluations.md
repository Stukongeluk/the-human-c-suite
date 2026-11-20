# Fair technology decisions

Read this for platform, vendor, framework or architecture choices, build-versus-buy questions, consolidations and rewrites. These decisions shape people's work for years, and they are easy to tilt, by accident or on purpose.

## Contents

- 1. Set up the decision before anyone scores
- 2. Evidence that counts
- 3. Total cost, including the exit
- 4. When an evaluation looks tilted
- 5. Build, buy or keep
- 6. Rewrites
- 7. Migrations at human speed

## 1. Set up the decision before anyone scores

- **Write the problem down first.** What must the choice fix (cost, reliability, speed, a skills gap, a contract ending), and how will you know it worked a year from now?
- **Fix the criteria and weights before scoring starts,** and record who agreed them and when. Changing weights after the scores are known is the classic way a decision gets bent, often without anyone meaning to.
- **Declare interests, including your own.** If you, your team or a close colleague built one of the options, or someone has a relationship with a vendor, say so in writing and hand the scoring to people without that stake. Make this routine, not an accusation.
- **Include "keep what we have" and "do nothing yet"** as real options with their own costs.
- **Score in the open.** Each score has evidence attached, dissent is recorded, and the people who will live with the result are heard: the teams on call for it, security, support and finance.
- **Record the decision** in an architecture decision record (template in `templates.md`): context, options, criteria, the choice, consequences and what would make you revisit it.

## 2. Evidence that counts

Rank evidence from strongest to weakest:

1. **Production data from the options you already run:** incidents, change fail rate, recovery time, deployment frequency, cost per service, on-call pages, onboarding time for a new team.
2. **A proof of concept with your real workloads**, run by the teams who will use it, with success criteria agreed beforehand.
3. **References** from companies of similar size and context, ideally ones the vendor didn't pick for you.
4. **Analyst reports and benchmarks**, read with their funding and method in mind.
5. **Vendor demos and marketing:** never the only source.

Watch for options that look good because they are new and nobody has been paged for them yet.

## 3. Total cost, including the exit

Compare multi-year total cost of ownership, not the licence or day rate:

- Licences, infrastructure and support over three to five years
- Migration effort: engineering time, running two systems in parallel, data migration, testing
- Training and the productivity dip while people learn
- Operations: on-call, upgrades, security patching, the platform team that runs it
- Lock-in and exit: what it would cost to leave, and how portable your data and configuration are
- Risk: what happens to customers and teams if the migration slips by six months

## 4. When an evaluation looks tilted

Signals: weights or criteria changed after scores were visible; a sponsor who won't share the raw scores; production data that contradicts the ranking; an option favoured by the person who built it or sells it; pressure to decide before the evaluation is finished.

What to do:

- Re-run the scores under the original weights and under the new ones, and show whether the change flipped the result. Facts and dates, no speculation about motives.
- Propose a clean re-run: criteria and weights fixed in advance, scorers without a stake, production data as the main input.
- Pause irreversible steps (contract signatures, migrations, team changes) until the decision is settled.
- In documents the wider group reads, state the process, not the person: say what changed and when, not who changed it. Declare interests neutrally and for every option ("Beacon was built by the Platform team, whose lead chairs this group"), the same way you declare your own. Raise specific concerns privately with the decision owner, in a short neutral note.
- If someone's role or team is at risk because of the choice, make sure the decision is sound before anyone is told.

## 5. Build, buy or keep

- **Buy** commodity capabilities that don't make you different (payroll, ticketing, observability, CI), unless the integration cost exceeds the benefit.
- **Build** what makes customers choose you, and what you must be able to change quickly.
- **Keep** what works when the case for change rests on fashion. "Everyone is moving to X" is not a reason.
- For each option, name who owns it in three years and whether those people exist today.

## 6. Rewrites

Full rewrites are among the riskiest decisions in software: the old system keeps changing while the new one catches up, and knowledge embedded in old code (edge cases, fixes for incidents nobody remembers) is lost. Joel Spolsky called rewriting from scratch "the single worst strategic mistake" a software company can make, after Netscape's rewrite.

Prefer incremental replacement: the strangler-fig pattern, where new services take over one capability at a time behind a stable interface, with the old system retired piece by piece. Commit to a full rewrite only with evidence that incremental change can't work, a frozen scope, and a plan that keeps customers and on-call teams safe during the overlap.

## 7. Migrations at human speed

- Migrate in waves, starting with a willing team and a low-risk service. Learn, then expand.
- Budget real time: migrations done "on top of the roadmap" become overtime.
- Keep the old platform supported until the last team is off it, with a named owner.
- Pair the teams that know the old system with those who know the new one, so nobody's expertise becomes worthless overnight.
- Track people as well as progress: on-call load, unplanned work and the engagement of the teams doing the migration.

Sources: Joel Spolsky, ["Things You Should Never Do, Part I"](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) (2000); Martin Fowler, ["Strangler Fig Application"](https://martinfowler.com/bliki/StranglerFigApplication.html).
