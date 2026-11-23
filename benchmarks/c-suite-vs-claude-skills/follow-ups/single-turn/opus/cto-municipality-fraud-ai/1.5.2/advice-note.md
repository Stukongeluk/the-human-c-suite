# Advice: AI fraud-risk scoring in income support

**Status:** draft for discussion · **For:** the alderman for [Work and Income] and the college · **Prepared by:** CIO, with [the data protection officer, Legal Affairs, the head of Work and Income and the head of Enforcement] · **Date:** 23 November 2026 · **Decision needed by:** [college meeting date]

## Recommendation

Do not buy the proposed fraud-risk scoring system, and do not commit to a go-live within six months. Instead, approve a six-month programme with the same aim, putting our limited investigation capacity where it finds real fraud. The programme measures how well our current selection works, fixes the main causes of overpayment and introduces explainable checks on verifiable facts. In [June 2027] the council decides, on our own data, whether a narrowly scoped model would add anything, and under which safeguards.

## The question in one sentence

How do we focus [n] investigators on the cases where benefits are wrongly received, fairly and lawfully, without treating everyone on benefits as a suspect?

## What we know and what we still need

| Fact | Value | Source and date | Confidence |
|---|---|---|---|
| Households receiving income support | [n] | [benefits system, date] | to fill in |
| Investigations per year, and share that find an overpayment | [n], [x%] | [enforcement records, year] | to fill in |
| Share of findings that are deliberate fraud vs reporting mistakes | [x% / y%] | [file review] | unknown, to be measured |
| Amount recovered per year, and the cost of investigating | [€ / €] | [finance] | to fill in |
| How cases are selected now | [tips, Inlichtingenbureau signals, own judgement: shares] | [enforcement team] | to fill in |
| The vendor's claim | "90% accurate"; metric, data and test method not specified | vendor, [date] | unverified |

## Why "90% accurate" does not answer the question

An accuracy figure says how often the model is right across everyone. What matters for us is how many of the people it sends to investigators have actually done something wrong. That depends on how rare fraud is.

The illustration below assumes 3,000 households and the most generous reading of the claim: the model catches 90% of fraud and clears 90% of honest households.

| Real fraud rate | Households committing fraud | Flagged by the model | Of whom did nothing wrong | Share of flagged who did nothing wrong | Fraud cases missed | "Accuracy" of a model that flags no one |
|---|---|---|---|---|---|---|
| 2% | 60 | 348 | 294 | 84% | 6 | 98% |
| 5% | 150 | 420 | 285 | 68% | 15 | 95% |
| 10% | 300 | 540 | 270 | 50% | 30 | 90% |

Three further problems make the real picture worse than this table:

- **The model learns from past investigations,** so it learns who we chose to investigate, not who committed fraud, and repeats those choices.
- **What is recorded as fraud is often a mistake.** Many findings under the Participatiewet are a breach of the duty to report changes, frequently by people with irregular income, complicated households or limited Dutch.
- **Linked data brings in proxies.** Address, household composition, neighbourhood and debt history correlate with origin, income and disability, so a model can discriminate without ever using a protected characteristic.

## What has happened in the Netherlands

- **Childcare benefits.** The Tax Administration's risk classification, which used nationality, contributed to more than 20,000 families being wrongly accused of fraud. The cabinet resigned in January 2021, and in December 2021 the Dutch Data Protection Authority fined the Tax Administration €2.75 million for its processing of applicants' nationality.
- **SyRI.** The national system linked data from several government bodies to flag benefit fraud risks. On 5 February 2020 the District Court of The Hague ruled that its legal basis breached Article 8 of the European Convention on Human Rights, because it was insufficiently transparent and verifiable (ECLI:NL:RBDHA:2020:865).
- **Rotterdam.** The city used a risk-scoring model for income support until 2021, when it stopped after the Rotterdam Court of Audit's report "Gekleurde technologie". In 2023 Lighthouse Reports and WIRED showed that variables such as age, gender and Dutch language proficiency drove the scores.
- **DUO.** Risk-based checks on student grants for students living away from home were stopped in 2023; in 2024 the minister apologised after an audit found indirect discrimination against students with a migration background.

The common thread: people were selected on their circumstances rather than their conduct, could not see why, and the institution's trust took years to recover.

## Legal and governance points

To be confirmed in writing by Legal Affairs and the data protection officer. This note is not legal advice.

1. **AI Act ban on social scoring (Article 5(1)(c)), applying since 2 February 2025.** It prohibits evaluating people on their behaviour or personal characteristics where the score leads to unfavourable treatment in a context unrelated to the one in which the data was collected, or treatment out of proportion to the behaviour. Using debt-counselling and housing data to select benefit recipients for fraud investigation is the clearest risk in this proposal.
2. **High-risk AI (Annex III, point 5(a)).** AI used by public authorities to assess eligibility for public assistance, or to reduce, revoke or reclaim it, is high-risk. After the 2026 Digital Omnibus these obligations apply from 2 December 2027: a fundamental-rights impact assessment before use (Article 27), human oversight, logging, informing the people affected and registration in the EU database. A system going live in mid-2027 would have to be designed for these duties from the start.
3. **GDPR.** A data protection impact assessment is required before processing begins. Debt-counselling data was collected under the Wet gemeentelijke schuldhulpverlening to help people; re-using it for fraud selection needs a specific legal basis and a compatibility test. In the SCHUFA case (C-634/21, 7 December 2023) the EU Court of Justice held that a score can itself be an automated decision under Article 22 when the decision-maker relies on it heavily.
4. **Equal treatment.** Article 1 of the Constitution and the General Equal Treatment Act apply. Indirect discrimination through proxies has to be tested for and justified, not assumed away.
5. **Transparency.** Any algorithm used for selection belongs in the national algorithm register. The Ministry of the Interior's human-rights and algorithms impact assessment (IAMA) is the standard tool for the assessment.
6. **Procurement.** A contract of this size will most likely need a European tender. Criteria and weights are fixed before any bid is scored, and anyone with a link to a vendor declares it and steps out of the decision.
7. **Participation.** The works council has an advisory right on introducing major new technology (article 25 WOR) and a consent right on systems that can monitor staff performance (article 27 WOR). The client council for the Participatiewet should help shape any selection method that affects residents on benefits.

## Options considered

| Option | What it means | Time | Main risks | Reversible? |
|---|---|---|---|---|
| A. Buy as proposed | Score all households using benefits, debt-counselling and housing data; investigators work the top 10% | Vendor says six months; a tender, DPIA, legal opinion and works council advice make that unrealistic | Possible breach of the social-scoring ban; GDPR purpose limitation; discrimination through proxies; most people investigated have done nothing wrong; residents avoid debt counselling | Hard: the harm to residents and to trust remains after the system is switched off |
| B. Change nothing | Keep the current selection | None | Our current selection may also be biased or inefficient; we don't know | Yes |
| C. Measure, fix causes, explainable checks (recommended) | Baseline and random file review; fix the main causes of overpayment; fact-based checks with human review; legal opinion | Six months | Slower visible result; the random review takes investigator time | Yes |
| D. Narrow model with full safeguards | Only if C shows a clear gap that rules and random selection can't close | 12–18 months after C | Must beat random selection plus rules without gaps between groups; cost | Partly |

Costs: [to be estimated with Finance. Option A: licence, integration with three systems, assessments, legal review. Option C: mainly own staff time, about [x] FTE-months].

## Six-month plan

| When | What | Owner | Output |
|---|---|---|---|
| Months 1–2 | Baseline: how cases are selected now, hit rate per source, intent vs mistake, amounts involved | Head of Enforcement, Information Management | Baseline report |
| Months 1–2 | Random review of about 200 files: a desk review, not a home visit, explained to residents as a random check, not a suspicion | Head of Enforcement | The real error and fraud rate (within about 3 points at a 5% rate) and the benchmark any method must beat |
| Months 1–3 | Legal opinion on the AI Act, GDPR, the Wgs and equal treatment | Legal Affairs, data protection officer | Written opinion |
| Months 1–2 | Written questions to the vendor (below) | CIO, Procurement | Answers on file |
| Months 2–5 | Fix the three most common causes of overpayment, such as changing income from flexible work: simpler reporting, clearer letters, earlier help with debts | Work and Income, with case managers and the client council | Changes in place, measured monthly |
| Months 3–5 | Explainable checks on verifiable facts, such as payroll income from Suwinet or Inlichtingenbureau signals that wasn't reported, each reviewed by a person, alongside random selection | Enforcement, Information Management, with investigators | Published in the algorithm register; residents informed |
| Month 6 | Report to the council | Alderman, CIO | Decision on whether a narrow model is worth exploring |

## Who is affected

- **Residents on benefits, about [n] households.** Under option A each would carry a risk score they don't know about, and most of those investigated would have done nothing wrong. Under option C fewer people are investigated without cause, and selection can be explained.
- **Residents in debt counselling.** Their trust in the service depends on their information not being used against them.
- **Investigators and case managers.** Under option A most of their visits would be to households that did nothing wrong. Under option C they get better-founded cases and help design the checks.
- **Debt counsellors.** Their working relationship with clients is at stake.
- **The council and the alderman.** Every Dutch precedent above ended in political and legal consequences for the people in charge.

## If a model is considered after month 6: minimum conditions

- No debt-counselling data; no nationality, origin or language, and no proxies for them; every variable justified in writing.
- A DPIA and an IAMA before procurement; the fundamental-rights impact assessment before use.
- An independent bias audit, with error rates per group published.
- A shadow run in which scores are calculated but not used, compared with random review and rule-based checks.
- An investigator decides; a score is never on its own a reason to investigate, and the reasons are recorded.
- Residents are told they are being assessed, can see their data and score, and can object and challenge it.
- The client council and investigators help design it; the works council is consulted.
- Stop criteria agreed in advance, such as error-rate gaps between groups above [x] or a hit rate no better than random selection plus rules.
- Published in the algorithm register and reviewed every year.

## Questions for the vendor

1. "90% accurate" by which measure: accuracy, precision in the top 10%, recall or AUC? On which population, over which period, and tested by whom?
2. What was the "fraud" label in the training data: proven intent, any recovered payment, or the outcome of an investigation?
3. What are the error rates by gender, age, household type (including single parents), migration background, disability and neighbourhood?
4. Which variables does the model use, and can each individual score be explained to the resident and to a court?
5. Will you accept an independent audit, carry the AI Act's obligations as provider, and agree exit terms that return our data and documentation?

## Communication

- Discuss this note with the alderman first, before any wider meeting.
- After the college decides: a council information letter setting out the aim, the plan and the dates.
- Inform the client council and the works council at the start, with the real figures, while they can still shape the plan.
- Staff in Work and Income and Enforcement hear about it from their own managers before the council letter.
- Explain the random review and the checks to residents in plain language.

## Assumptions, and what would change this advice

- The 3,000 households and the fraud rates in the table are illustrations; the baseline will give our real figures.
- If the vendor shows, on independent Dutch data, a high share of genuine fraud among flagged cases with no gaps between groups, option D deserves a fair evaluation.
- If the baseline shows our current selection has a low hit rate, and a narrow, explainable model beats random selection plus rules in a shadow run, and Legal confirms a legal basis, a limited model may be justified.

## Questions for the college

1. Which outcome matters most to the council: money recovered, fewer wrongful payments, or public confidence that fraud is handled fairly?
2. Are we prepared to explain to every resident on benefits how they were selected for a check? If not, we should not use the method.

## Sources

- Dutch Data Protection Authority, fine of €2.75 million to the Tax Administration for processing nationality in childcare benefit applications (December 2021); *The Guardian*, 15 January 2021, on the cabinet's resignation.
- District Court of The Hague, 5 February 2020, ECLI:NL:RBDHA:2020:865 (SyRI).
- Rekenkamer Rotterdam, "Gekleurde technologie" (April 2021); Lighthouse Reports and WIRED, "Inside the Suspicion Machine" (March 2023).
- DUO student grant checks: the minister's letter of apology to parliament (2024).
- Regulation (EU) 2024/1689 (AI Act), Articles 5, 26, 27 and 49 and Annex III; the 2026 Digital Omnibus on AI for the revised application dates.
- Court of Justice of the EU, C-634/21 *SCHUFA Holding (Scoring)*, 7 December 2023.
- Ministry of the Interior and Kingdom Relations, Impact Assessment Mensenrechten en Algoritmes (IAMA, 2021).
