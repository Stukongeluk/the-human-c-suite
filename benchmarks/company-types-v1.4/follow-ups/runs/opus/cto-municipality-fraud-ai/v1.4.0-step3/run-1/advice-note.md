# Advice note: AI risk scoring for welfare fraud investigations

**To:** Alderman for Social Affairs; college of mayor and aldermen
**From:** CIO
**Date:** November 2026, draft for discussion
**Status:** Before this goes to the council, the data protection officer (FG) and Legal Affairs must confirm the legal points and the dates in section 3.4.

## 1. Advice

We share the council's goal: investigators' time spent where it matters most, public money protected, and continued public support for the benefit scheme.

We advise against buying the proposed system, and against a go-live in six months. The system would give every benefit recipient a fraud-risk score, using data from the benefits, debt-counselling and housing systems. Instead we propose two steps:

1. **Months 0–6:** improve and measure the current enforcement process, and report the results to the council at month 6.
2. **Around months 9–12:** decide, on the measured results, whether a narrow and tested pilot of a risk model is justified, under the conditions in section 5.

This route gives the council results within the six months it asked for. It keeps a model possible if the evidence supports one. And it avoids a system that would put mostly innocent residents under investigation and that carries serious legal risk.

## 2. The question behind the request

The request names a solution. The question underneath it is: how do we find more real violations with the same investigation capacity, without harming people who did nothing wrong?

To answer that we need figures that are not yet collected in one place:

- the number of recipients and the number of investigations per year
- the share of investigations that find a violation, per selection route: tips, Inlichtingenbureau signals, file checks and random checks
- amounts recovered, and how many violations were deliberate and how many were mistakes
- the time an investigation takes, and the current investigation capacity

## 3. Assessment of the proposal

### 3.1 What "90% accurate" means

When violations are rare, accuracy is the wrong measure. The table uses illustrative figures, to be replaced with our own: 3,000 recipients and a violation rate of 5% or 2%. Here "90%" is read as catching 9 in 10 violations and clearing 9 in 10 people without one.

| | 5% violation rate | 2% violation rate |
|---|---|---|
| Recipients | 3,000 | 3,000 |
| People with a violation | 150 | 60 |
| Accuracy of a "model" that flags no one | 95% | 98% |
| "90%" model: violations flagged | 135 | 54 |
| "90%" model: people without a violation flagged | 285 | 294 |
| Share of flagged people who did nothing wrong | 68% | 84% |
| Investigating the top 10% | 300 people | 300 people |
| People without a violation among those 300, even with a perfect model | at least 150 | at least 240 |

The figures that matter are different. Of the people we investigate, how many actually committed a violation? How many violations do we miss? Do the errors fall more often on some groups than on others?

### 3.2 What a model like this learns

- **Past choices.** A model is trained on past investigations. Those reflect whom investigators chose to check, not the whole population. The model learns earlier selection patterns and repeats them.
- **Mistakes counted as fraud.** Under the Participatiewet, failing to report a change is a violation whether or not it was deliberate (the duty to provide information, article 17). Much of what the data records as "fraud" is therefore a mistake.
- **Vulnerability instead of dishonesty.** Together, these two effects mean the model tends to point at people with irregular income, complicated households or limited Dutch. Those characteristics often follow nationality, migration background, gender and age, which makes indirect discrimination likely unless it is tested for and prevented.

### 3.3 Data from debt counselling and housing

- **Debt counselling.** This data is collected under the Municipal Debt Assistance Act (Wgs) to help residents. Using it for fraud scoring is a different purpose. That needs its own legal basis, and we have not identified one. It would also discourage residents in debt from seeking early help, which works against our own early-intervention policy.
- **Housing.** Use housing data only where it ties directly to a benefit condition, such as household composition at an address, and only with a legal basis. It is not general input for a score.

### 3.4 Legal framework

This is not legal advice. It reflects the situation as of November 2026, and the FG and Legal Affairs must confirm it.

| Rule | What it means for this proposal | Applies |
|---|---|---|
| Article 8 ECHR, as applied in the SyRI judgment | Risk scoring of benefit recipients was struck down for lack of transparency and safeguards | Judgment of 5 February 2020 |
| AI Act, ban on social scoring (article 5(1)(c)) | Scoring people on data from an unrelated context, such as debt counselling, in a way that leads to worse treatment can fall under the ban | Since 2 February 2025 |
| AI Act, high-risk systems (Annex III, point 5(a)) | AI used to grant, reduce, revoke or reclaim public benefits is high-risk. Users must carry out a fundamental rights impact assessment (article 27), provide human oversight and keep logs (article 26), register the system (article 49), and give people a right to an explanation (article 86) | From December 2027, following the 2026 Digital Omnibus. A system bought now must meet these rules |
| GDPR | A data protection impact assessment (DPIA) is required before processing starts (article 35). Data may only be used for compatible purposes (articles 5(1)(b) and 6(4)). Under the SCHUFA judgment, a score that largely determines what happens to a person can count as an automated decision (article 22) | Now |
| Equal treatment (article 1 of the Constitution, General Equal Treatment Act) | Indirect discrimination through stand-ins for protected characteristics must be tested for and prevented | Now |
| General Administrative Law Act | Selection and decisions must be careful and explainable to the resident | Now |
| Works Councils Act, article 25 | The works council has an advisory right on introducing an important technological system | Now |
| Government standards | A human rights impact assessment (IAMA) and publication in the national algorithm register are expected for high-impact algorithms | Now |

### 3.5 Experience in the Netherlands

- **Childcare benefits:** risk profiling was part of a system that wrongly treated tens of thousands of families as fraudsters. The parliamentary inquiry called it "unprecedented injustice" (December 2020), and the cabinet resigned in January 2021. The Dutch Data Protection Authority fined the Tax Administration for processing nationality in its risk classification model.
- **SyRI (2020):** the national system for linking data to detect benefit fraud was struck down in court.
- **Rotterdam (2017–2021):** the city's risk score for welfare recipients used characteristics including language, gender and age. Rotterdam stopped using it after a critical report from its own court of audit (2021). A 2023 reconstruction by journalists showed who was scored as high-risk.
- **DUO (until 2023):** risk-based checks on the student living-away grant flagged students with a migration background far more often. The checks were stopped, and the minister apologised in 2024.

### 3.6 The six-month timeline

Before a system like this could lawfully be used, all of the following has to happen:

- a public tender, probably above the European threshold
- a DPIA and an IAMA
- a legal basis for each data source
- data-sharing arrangements
- validation on our own data
- an independent bias test
- advice from the works council and involvement of the client council
- registration
- training for investigators

Our estimate is 12 to 18 months, if it can be done lawfully at all. Holding to six months would mean skipping safeguards.

## 4. Options compared

| | A. Improve the current process (recommended) | B. Narrow pilot after A (conditional) | C. Buy and go live in 6 months |
|---|---|---|---|
| What the council gets at month 6 | A baseline, better use of existing signals, fewer mistakes at the source, and a report | A decision at months 9–12 | Possibly a live system, with safeguards incomplete |
| Effect on residents | No blanket scoring | A limited scope, with safeguards | Everyone on benefits is scored, and most of those investigated are innocent |
| Legal risk | Low | Manageable with a DPIA, an IAMA and a bias test | High: SyRI, the social scoring ban and the GDPR |
| Reversibility | Fully reversible | Time-limited, with stop criteria | Hard: a contract, data links and reputational damage |
| Cost | Mainly staff time, to be estimated | A pilot budget, to be estimated | The vendor price (not yet known) plus implementation |

## 5. Proposed approach

### Months 0–6

1. **Baseline (month 2).** Collect the figures listed in section 2.
2. **Random sample.** Run a light file review of a random sample spread over the period, for example 150 files, to measure the real violation rate. That rate is the benchmark every selection method must beat.
3. **Prevention.** Simplify how residents report changes in income and household. Where possible, offset income automatically using the income data we already receive. Contact the resident about a signal before treating it as fraud.
4. **Transparency.** Document the selection rules and signals we already use, and publish them in the algorithm register. Start the DPIA and IAMA for the selection process as a whole.
5. **Involvement.** Bring in the investigators, the client council and the works council from the start, while they can still shape the plan.
6. **Report to the council at month 6,** using the measures in section 7.

### Decision point, months 9–12

A model is worth piloting only if both of these hold:

- the baseline shows that current selection misses a substantial share of violations
- better rules, prevention or extra capacity cannot close that gap

### Conditions for any pilot

- **Purpose:** the score supports investigators' choice of cases. There are no automated decisions about benefits. Investigators can override the score, and they record why.
- **Data:** benefits data only. No debt-counselling data. Housing data only for a specific benefit condition, with a legal basis.
- **Excluded inputs:** no nationality, country of birth, language, postcode or other stand-ins for them, and a test for proxy effects.
- **Explanation:** both the investigator and the resident can see why someone was selected.
- **Independent bias test:** before the start and every quarter. It compares selection rates and hit rates by gender, age, household type, neighbourhood and migration background. Where we may not process a characteristic ourselves, the test uses aggregated statistics, for example from CBS.
- **Comparison:** the model is compared with current selection and with random selection.
- **Before the start:** the DPIA and IAMA (or fundamental rights impact assessment) are complete, the FG has given advice, and the system is registered.
- **Residents** are told that a model may be used in selection, and how to object.
- **Contract:** access to the model and its documentation, audit rights, liability and an exit, using the EU model contractual clauses for public procurement of AI as a starting point.
- **Stop criteria, agreed in advance:**
  - no better hit rate than current selection
  - a difference between groups beyond an agreed threshold
  - scores that cannot be explained
  - a rise in objections or complaints
- **Time limit:** continuing after the pilot requires a new decision by the college, with the council informed.

## 6. Questions for the vendor

Put these in writing before any further talks:

1. What does "90% accurate" measure: accuracy, precision within the top 10%, recall, or AUC? On which data, from which organisation and which year?
2. What counted as "fraud" in the training labels: proven deliberate fraud, any recovery claim, or being selected for investigation?
3. Of the people in the top 10%, what share had a confirmed violation?
4. What are the error rates by gender, age, household type, nationality or migration background, language and neighbourhood?
5. Which variables does the model use, and which could act as stand-ins for protected characteristics?
6. Can each score be explained to an investigator and to the resident?
7. Will you validate the model on our data, with an independent reviewer, before any contract?
8. Will we get access to the model, its documentation and its logs for an independent audit? How will you meet the AI Act's requirements for providers of high-risk systems?
9. Where else is the model in use? Has any organisation stopped using it, and why?
10. What are the terms on liability, exit and the return of data?

## 7. What we will report to the council

Every quarter, at team and process level:

- the number of investigations
- the share that found a violation, per selection route
- amounts recovered, and mistakes prevented
- investigations closed without a finding
- time per investigation and investigator workload
- objections and complaints
- selection rates and hit rates by group, aggregated

## 8. Assumptions and open questions

- The figures in 3.1 are illustrative and must be replaced with our own.
- The vendor's 90% has not been validated on our data.
- No legal basis has been identified for using debt-counselling data in fraud detection. The FG and Legal Affairs must confirm this.
- The AI Act dates follow the 2026 Digital Omnibus and must be confirmed.
- Still open:
  - the exact wording of the council's request
  - whether a budget has been reserved
  - current investigation capacity

## Sources

- Rechtbank Den Haag, 5 February 2020, ECLI:NL:RBDHA:2020:865 (SyRI)
- Regulation (EU) 2024/1689 (AI Act): article 5(1)(c), Annex III point 5(a), articles 26, 27, 49 and 86; application dates for high-risk obligations as amended by the 2026 Digital Omnibus
- Regulation (EU) 2016/679 (GDPR): articles 5, 6(4), 22 and 35; Court of Justice of the EU, 7 December 2023, C-634/21 (SCHUFA)
- Parlementaire ondervragingscommissie Kinderopvangtoeslag, *Ongekend onrecht* (December 2020); Autoriteit Persoonsgegevens, fine imposed on the Tax Administration for processing nationality in the childcare benefits system (December 2021)
- Rekenkamer Rotterdam, *Gekleurde technologie* (2021); Lighthouse Reports and WIRED, "Suspicion Machines" (March 2023)
- College voor de Rechten van de Mens, *Discriminatie door risicoprofielen: een mensenrechtelijk toetsingskader* (2021)
- Ministry of the Interior and Kingdom Relations, *Impact Assessment Mensenrechten en Algoritmes* (IAMA, 2021); national algorithm register, algoritmes.overheid.nl
- Participatiewet, article 17; Wet gemeentelijke schuldhulpverlening; Wet op de ondernemingsraden, article 25
- European Commission, Public Buyers Community, *EU model contractual AI clauses* (MCC-AI, 2023)
