**My advice: don't buy this system as specified, and don't commit to going live in six months. Go back to the alderman with a six-month plan for the same goal, putting scarce investigators on real fraud, without giving every resident on benefits a risk score.**

The "90%" answers the wrong question. Take 3,000 households on benefits (use your own figure) and assume 5% commit fraud. Read the claim as generously as possible: the model catches 90% of fraud and clears 90% of honest households. It then flags about 420 households, and 285 of them did nothing wrong. Two out of three people your investigators look into would be innocent. And if the true rate were 10%, a model that flags nobody at all would also be "90% accurate".

**Why not this version**

1. **The Netherlands has already run this experiment.** In the childcare benefits scandal, risk profiling helped wrongly accuse more than 20,000 families, and the cabinet resigned in January 2021. The Hague District Court struck down SyRI, which linked government data to flag welfare fraud, in February 2020 under Article 8 ECHR. Rotterdam dropped its welfare risk score in 2021 after a critical report by its court of audit, and journalists later showed it weighed age, gender and Dutch language skills. This proposal combines their core features: everyone scored, data from other domains, a ranked list.
2. **The debt-counselling and housing data are the biggest problem.** People open up their finances to debt counsellors to get help. Using that to rank them as suspects strains purpose limitation under the GDPR and very likely the Wgs. It also comes close to the AI Act's ban on social scoring, in force since February 2025: scoring people with data from an unrelated context in a way that leads to unfavourable treatment. And once word gets out, people in debt stop asking for help. Housing data (address, household make-up, neighbourhood) is a classic proxy for origin and income.
3. **The model learns who was investigated, not who committed fraud.** Its labels come from past investigations, so it repeats past choices. Much of what's recorded as fraud under the Participatiewet is a missed reporting duty, often an honest mistake by someone with irregular income or limited Dutch. The model will mostly find complicated lives.
4. **Six months doesn't reach the legal floor.** AI used to assess or reclaim public benefits is high-risk under the AI Act; after the 2026 Digital Omnibus those duties (a fundamental-rights impact assessment, human oversight, telling people they are scored) apply from 2 December 2027. A DPIA and equal treatment apply now. A European tender, a legal opinion, works council advice (the investigators' work changes) and the client council won't fit in six months. This isn't legal advice: get your privacy officer and legal team to answer in writing.

**What I'd propose instead: six months, same goal**

- **Months 1–2, baseline.** How cases are chosen now (tips, data matches, gut feeling), what share of investigations finds something, how much is intent versus mistake, and how much money is involved. Add a random review of about 200 files. At a 5% rate that pins the real rate to within about 3 points, and it's the fair benchmark any model would have to beat.
- **Fix the causes.** Tackle the top three causes of overpayment, often changing income from flexible work: simpler reporting, the income signals you already get through Suwinet and the Inlichtingenbureau, and earlier help with debts.
- **Explainable checks on facts**, such as payroll income that wasn't reported, each reviewed by a person, alongside random selection, and published in the national algorithm register.
- **Month 6: the council decides with data** whether a narrow model would add anything. If so: no debt-counselling data, a DPIA and a human-rights impact assessment (IAMA) first, an independent bias audit and a shadow run where scores aren't used. Residents are told and can see and challenge their score, an investigator always decides and the client council helps design it. That's realistically 12–18 months, and the honest answer may still be no.

**Ask the vendor in writing:** 90% of what (accuracy, precision in the top 10%, recall), on whose data, tested by whom? What are the error rates by gender, age, single parents, migration background and neighbourhood? Was the "fraud" label proven intent or any recovered payment? Can each score be explained to the resident and to a judge? Any purchase goes through a tender with criteria fixed before scoring.

**For the alderman, in private first:** "I want to tackle fraud as much as you do. This kind of system has been struck down by a court, helped bring down a cabinet and been dropped after an audit. I don't want your name on the fourth version. Give me six months and I'll bring you real numbers and an approach that will hold up."

The council has a point: investigators are scarce and gut feeling and tips are biased too. So the plan isn't "no technology"; it's measurement first.

**Assumptions:** the 3,000 households and 5% are illustrations; your files will give the real numbers. What would change my mind: a baseline showing current selection performs poorly, and a narrow, explainable model beating random checks in a shadow run with no gaps between groups.

I couldn't re-check sources online today; have legal confirm the case dates and AI Act timetable before this goes to the council. A draft advice note for the alderman and college is in `advice-note.md`, with blanks for your figures.

What am I missing, and what would make this wrong?
