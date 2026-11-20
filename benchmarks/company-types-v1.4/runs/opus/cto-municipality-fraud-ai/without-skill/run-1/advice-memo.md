# Advice note: proposed AI fraud-risk scoring of benefit recipients

**To:** Alderman [name], Social Affairs / College of B&W
**From:** CIO
**Copy:** Data protection officer (FG), Head of Legal, Head of Work & Income, Head of Debt Counselling, CISO
**Date:** [date]
**Status:** Draft, for discussion

---

## 1. Advice

1. **Do not procure the proposed system as specified.** It would score all benefit recipients for fraud risk using data from benefits, debt counselling and housing.
2. **Do not commit to a six-month go-live** for any algorithmic risk scoring of residents.
3. **Instead, approve the six-month plan in section 4.** It improves enforcement now, sets an evidence baseline, and comes back to the council with a reasoned go/no-go on any algorithmic support.

## 2. Background

The council has asked for an AI system that ranks all benefit recipients by fraud risk, so that investigators can focus on the top 10%. The vendor says the model is "90% accurate". It would combine data from our benefits, debt-counselling and housing systems. The alderman's target is go-live within six months.

The underlying goal is legitimate and shared: use limited investigator capacity well and protect public money. This note is about whether the proposed tool achieves that goal lawfully and effectively.

## 3. Assessment

### 3.1 Legal

| Issue | Assessment |
|---|---|
| **AI Act, Art. 5(1)(c): social scoring ban** (in force since 2 Feb 2025) | **Serious risk.** Fraud scoring as such is not prohibited. Scoring based on data from *unrelated contexts*, such as information residents gave the debt-counselling service to get help, can fall under the ban. The Commission's guidelines on prohibited practices discuss welfare-fraud scoring of this kind. A formal legal opinion is needed before any procurement step. |
| **AI Act, Annex III, point 5(a): high-risk** | **Applies.** As deployer we would need: a fundamental rights impact assessment (Art. 27); trained human oversight, monitoring and logging (Art. 26); registration in the EU database (Art. 49); informing residents that they are subject to the system (Art. 26(11)); and explaining individual outcomes on request (Art. 86). The vendor must show its conformity assessment and technical documentation. |
| **GDPR: purpose limitation** (Art. 5(1)(b), 6(4)) | **Likely incompatible for debt-counselling data.** The data was collected under the Wgs to help residents out of debt. Using it for fraud selection is a different purpose and very probably lacks a legal basis. Housing data needs its own assessment. |
| **GDPR: DPIA and prior consultation** (Art. 35, 36) | **DPIA mandatory.** Fraud prevention and profiling are on the AP's mandatory-DPIA list. Given the residual risk, prior consultation with the AP is likely, which takes up to 8 weeks plus 6 weeks extension. |
| **GDPR, Art. 22: automated decisions** | **Risk.** After CJEU *SCHUFA* (C-634/21, 2023), a score that in practice decides who is investigated can count as an automated decision, even if a human signs off. |
| **Art. 8 ECHR: SyRI precedent** | The District Court of The Hague (5 Feb 2020) struck down SyRI, which linked government data sets for fraud-risk profiling, as insufficiently transparent, verifiable and proportionate. The proposal is a municipal version of the same approach. |

*Note: the application date of the AI Act high-risk obligations (originally 2 August 2026) was proposed for postponement under the EU Digital Omnibus package. Legal to confirm the current position. Either way, a system procured now must comply for as long as we use it, and the Art. 5 prohibitions and the GDPR apply today.*

### 3.2 Effectiveness

- **"90% accurate" is not a meaningful claim for rare events.** At a 3% fraud rate, flagging nobody is 97% accurate.
- **Most of a top-10% list is innocent by construction**, whenever fraud prevalence is below 10%. That holds even for a perfect model. See Annex B.
- **Taking the vendor's claim at face value** (2,500 recipients, 3% prevalence, top 10% investigated), each run would find about 37 real cases. It would put about 212 households who did nothing wrong through an investigation, and miss about half of the real cases.
- **Training labels are biased by past selection.** The model learns whom we used to investigate, not who commits fraud, and creates a feedback loop.
- **Debt and housing data act as proxies** for poverty, household composition and often migration background. That raises the risk of indirect discrimination.

### 3.3 Precedent and reputational risk

- **Toeslagenaffaire:** a risk-classification model that used nationality, an AP fine, and the cabinet's resignation in January 2021.
- **SyRI:** struck down in 2020.
- **Rotterdam:** welfare risk model suspended in 2021 after criticism from the city's audit office (Rekenkamer). Public reporting in 2023 showed it rated women, young parents and people with limited Dutch as higher risk.
- **DUO:** student-grant risk profiling stopped after it disproportionately selected students with a migration background; the government apologised.
- **Amsterdam "Slimme Check":** developed as a deliberately responsible model, with explainability and bias correction, and shelved after the pilot still showed bias.

### 3.4 Timeline

A responsible route takes about 12–18 months for a suitable system: European tender, legal opinion, DPIA, fundamental rights impact assessment, possible AP prior consultation, local bias testing and a controlled pilot. A six-month go-live is only achievable by skipping some of these steps.

### 3.5 Impact on residents and services

- **The people most exposed are our most financially vulnerable residents.** An investigation brings stress, may suspend payments and costs them time, even when it ends with no finding.
- **Debt counselling depends on residents coming forward early.** If asking for help raises a fraud score, uptake will fall. That leads to more problematic debt, at higher cost to the municipality.
- **Investigators and caseworkers would work from a list they cannot explain** to residents or to the council.

## 4. Alternative: six-month plan

### Phase 1 (months 0–3): establish the facts

- **Baseline:** current enforcement capacity, hit rates, amounts recovered, and the split between intentional fraud and unintentional errors with the duty to report changes.
- **Random-sample check** of [300–500] files. This gives an unbiased error and fraud rate. It is non-discriminatory and defensible, and any future model has to be measured against it.
- **Legal opinion** from Legal and the FG, with external counsel if needed, on: AI Act Art. 5, the legal basis per data source, Art. 22, and the SyRI judgment.
- **Talk to investigators, caseworkers, the debt-counselling team and the client council** about where errors and fraud actually occur.

### Phase 2 (months 3–6): improve enforcement without profiling

- **Signal-based checks:** follow up concrete, verifiable discrepancies (e.g. Inlichtingenbureau/Suwinet income matches, BRP registrations at an address) rather than scoring people on who they are.
- **Prevention:** clearer letters, easy reporting of changes, and regular check-ins. This is in line with the direction of the national Participatiewet revision.
- **Prioritise tips and signals by capacity**, with documented, explainable criteria.

### Month 6: report to the council

- Results of Phases 1 and 2, the measured baseline, and the legal opinion.
- A reasoned recommendation: either no algorithm is needed, or a narrowly scoped one under the conditions in section 5.

## 5. Conditions for any future algorithmic selection

Only if the Phase 1–2 evidence shows a gap that better selection would close, and the legal opinion allows it:

1. No debt-counselling data. No protected characteristics (nationality, ethnicity, gender, etc.) or obvious proxies.
2. A clear, narrow purpose, with only data directly relevant to entitlement.
3. A DPIA and a fundamental rights impact assessment / IAMA, with the client council involved. AP consultation where required.
4. An independent bias and performance audit on our own data, before any use and periodically after.
5. A pilot with a random control group, so effectiveness and fairness are measured rather than assumed.
6. Human decision-making with recorded reasons. The score is never the sole ground for an investigation.
7. Transparency: registration in the algorithm register, information for residents, and individual explanations on request.
8. Contractual rights to audit, access to documentation, exit and liability. Vendor AI Act conformity confirmed.
9. An evaluation after 12 months and a sunset clause. The council decides on continuation.

## 6. Decision requested

The college is asked to:

1. Agree not to procure the proposed system as specified.
2. Approve the six-month plan in section 4, with [budget/capacity].
3. Instruct Legal and the FG to deliver the legal opinion by [date].
4. Inform the council of this approach by [raadsinformatiebrief / committee date].

---

## Annex A: Questions for the vendor

1. What exactly does "90% accurate" measure? Provide precision and recall at a 10% cut-off, the population tested, its fraud rate, and the test period.
2. On what labels was the model trained? How were those cases originally selected for investigation?
3. Which input variables are used? Does the model use nationality, country of birth, language, gender, age, postcode or household composition, or proxies for them?
4. What are the error rates per group (gender, age, migration background, household type, disability)? Will you permit an independent audit on our data before contract?
5. On the AI Act: are you the provider? What is the status of your conformity assessment? Provide the technical documentation and instructions for use, including for human oversight.
6. Can the system give an individual explanation of a score that investigators and residents can understand?
7. Which Dutch municipalities use the system, with what measured results? Did their DPIAs, and any AP prior consultation, clear?
8. Where is data processed and stored, who has access, and what are the retention, audit, exit and liability terms?

## Annex B: Worked example (illustrative; replace with our own figures)

Assumptions: 2,500 benefit recipients; 3% with a real issue (75 people); top 10% investigated (250 people).

| Scenario | Real cases found | Flagged people who did nothing wrong | Real cases missed |
|---|---|---|---|
| Vendor claim (90% accuracy at 10% cut-off) | ~37 | ~212 (85% of list) | ~38 |
| Perfect model | 75 | 175 (70% of list) | 0 |
| Random selection of 250 | ~7 | ~243 | ~68 |
| "Flag nobody" | 0 | 0 | 75 (and still 97% "accurate") |

Changing the assumed fraud rate changes the figures but not the pattern. Below 10% prevalence, most of a top-10% list is innocent.

---

*Sources to verify before external use: AI Act Arts. 5, 26, 27, 49, 86 and Annex III, and the current high-risk application dates; the Commission guidelines on prohibited AI practices (Feb 2025); the AP's mandatory-DPIA list; CJEU C-634/21; District Court of The Hague 5 Feb 2020 (SyRI, ECLI:NL:RBDHA:2020:865); public reporting on Rotterdam, DUO and Amsterdam "Slimme Check".*
