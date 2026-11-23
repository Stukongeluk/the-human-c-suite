# Decision memo: AI fraud-risk scoring for welfare recipients

**For:** the CIO, to support written advice to the alderman and the college
**Date:** 2026-11-23
**Status:** Proposed
**Not yet checked by:** your FG (data protection officer), legal counsel, finance, the head of Work & Income
**Tags used:** [VERIFIED] means checked against a cited source. [ASSUMED] means my estimate or reading, to be confirmed.

---

## 1. Decision record (ADR-001: Algorithmic fraud-risk targeting in Work & Income)

### Context and problem

The council wants a vendor system that gives a fraud-risk score to every welfare recipient. The score would draw on data from the benefits, debt-counselling and housing systems. Investigators would then concentrate on the top 10%. The vendor claims "90% accuracy", and the alderman wants it live within six months.

The underlying problem is real and legitimate. Investigators have limited capacity, and the council wants that capacity spent where it does the most good.

### Decision drivers

- Lawfulness: GDPR, Article 8 ECHR, the AI Act, equal-treatment law and the Awb (General Administrative Law Act)
- Measured effectiveness compared with today's selection, rather than the vendor's own claim
- Impact on residents who depend on the municipality, and on use of debt help
- Investigator capacity and time to value
- Reversibility, vendor dependency and the cost of exit
- Political and reputational exposure. Every document, the variable list and the model itself are likely to become public through a Woo (freedom of information) request, as happened in Rotterdam.

### Options considered

**Option A: buy as specified, live in six months.**

Pros:
- Visible, fast answer to the council.
- Some help in prioritising cases, if the model works.

Cons:
- Very likely unlawful in part, because of the debt-counselling data (section 4).
- The accuracy claim cannot be checked as stated.
- The timeline leaves no room for a DPIA, a FRIA or an independent test.
- It repeats the Rotterdam design almost exactly: score everyone, send the top decile to investigators.
- High lock-in once three source systems are integrated.

**Option B: rule out algorithmic targeting.**

Pros:
- Lowest legal risk.
- No new spend.

Cons:
- The investigator-capacity problem is not solved.
- Today's selection process stays unmeasured, and it may be biased as well; Amsterdam found its caseworkers were.
- Politically it reads as obstruction.

**Option C (recommended): six-month evidence and improvement track, then go/no-go.**

Pros:
- Delivers concrete improvements within the alderman's six months.
- Produces the first honest baseline of prevalence and of bias in current selection.
- Any later tool can be judged against real numbers.
- Fully reversible.

Cons:
- No AI system in six months.
- It needs investigator time for the random sample, taken from existing capacity.
- The alderman may experience it as a "no".

### Three-year cost view [ASSUMED: order-of-magnitude ranges. Replace them with the vendor quote and your own rates, and have finance check them.]

| Cost item | Option A: buy as specified | Option B: no algorithm | Option C: evidence track (first 6 months) |
|---|---|---|---|
| Licence | Vendor quote (unknown, ask for it) | 0 | 0 |
| Integrating 3 source systems | €100–250k | 0 | 0 |
| DPIA, FRIA, IAMA, legal, FG time | €40–100k | 0 | €10–30k |
| Independent bias and performance audit | €30–80k, plus €20–40k a year | 0 | €30–60k (sandbox test, only if pursued) |
| Model governance and monitoring (0.5–1 FTE) | €50–100k a year | 0 | 0.5 FTE analyst for 6 months: €30–50k |
| Prevention (communication, easier income reporting) | 0 | 0 | €5–20k |
| Investigator time | Same capacity, but most of it spent on innocent people (section 2) | Unchanged | About 200 random-sample checks from existing capacity |
| Tail risk | Not estimable. Precedents: Amsterdam spent an estimated €500k+ on a pilot it stopped; DUO set aside €61m for refunds (national scale); AP fines | Low | Low |
| **Indicative 3-year total, excluding licence and tail risk** | **About €0.35–0.8m** | **About €0** | **About €75–160k** for the first 6 months. If month 6 says "go", option-A-type costs follow for a narrower scope. |

**IAMA** is the Dutch government's human rights and algorithms impact assessment (Impact Assessment Mensenrechten en Algoritmes).

### Decision outcome

**Chosen option: C.** It is the only option that meets the legitimate goal (better use of investigator time), that can be defended in court and in the council, and that produces the evidence needed to judge any tool.

- **Consequences:** No go-live in six months, but measurable improvements and a founded decision by month 6.
- **Reversibility:** Fully reversible. Nothing is integrated, and no resident data goes to the vendor before the DPIA.
- **Review date:** Month 6 go/no-go (section 6).

---

## 2. Why "90% accurate" tells you almost nothing

The table below uses these inputs:

- 3,000 recipients [ASSUMED for a mid-sized municipality]
- the top 10% investigated, which is 300 cases a year
- three assumed prevalences of an unlawful overpayment (2%, 5% and 10%)
- a standard model (binormal, equal variance) to translate AUC into results

AUC is the probability that the model ranks a true case above a non-case. 0.5 is random.

**How many of the 300 flagged people are innocent, and what "accuracy" the model would report:**

| Model quality | Prevalence 2% | Prevalence 5% | Prevalence 10% |
|---|---|---|---|
| Random selection (AUC 0.50) | 294 innocent; accuracy 88% | 285 innocent; 86% | 270 innocent; 82% |
| AUC 0.70 | 283; 89% | 259; 88% | 222; 85% |
| AUC 0.75 | 278; 89% | 249; 88% | 205; 86% |
| AUC 0.85 | 267; 90% | 222; 90% | 161; 89% |
| 90% sensitivity and 90% specificity (AUC about 0.965) | 247; 92% | 173; 93% | 77; 95% |

What the table shows:

- A model that "flags nobody" scores 95% accuracy at 5% prevalence.
- Random selection already scores 82–88% accuracy.
- A model that is 90% accurate can still leave three out of four flagged people innocent.
- "Innocent" here means no unlawful overpayment found. Many true hits will be honest mistakes, such as late reporting of small income, rather than intent.
- Rotterdam's model, which also sent the top decile to investigators, was judged by experts to perform little better than random ([Lighthouse Reports](https://www.lighthousereports.com/?p=1399)).

**The numbers that do matter:**

- precision in the top 10%: of those flagged, how many had an unlawful overpayment, and how many of those were intentional
- recall: how many of all real cases the model finds
- AUC, measured on recent data the model has not seen
- false-positive rates for each group of residents
- all of these compared with a random sample and with today's selection

**The label problem.** Training data usually comes from past investigations, and those people were chosen by an earlier, possibly biased process. The model learns who was investigated before, not who commits fraud. It then sends investigators back to the same groups, which produces more "confirmed" cases in those groups. This is a feedback loop.

---

## 3. What the Dutch precedents show [VERIFIED]

| Case | What happened | Lesson for you |
|---|---|---|
| Rotterdam (2017–2021) | Every one of about 30,000 recipients got a 0–1 risk score, and the top decile went to investigators (about 1,000 a year). It used 315 variables, including language skills, gender and caseworker comments, and was built with Accenture. It discriminated by ethnicity, age, gender and parenthood and was little better than random ([Lighthouse Reports](https://www.lighthousereports.com/?p=1399)). | This is the same design as the proposal. |
| SyRI (court ruling, Feb 2020) | The Hague District Court ruled that the SyRI legislation violated Article 8 ECHR: insufficiently transparent and verifiable, and no fair balance ([Rechtspraak](https://www.rechtspraak.nl/organisatie-en-contact/organisatie/rechtbanken/rechtbank-den-haag/nieuws/2020/02/syri-legislation-in-breach-of-european-convention-on-human-rights)). | Combining data from several sources to profile welfare recipients needs a very strong legal basis and transparency. |
| Amsterdam Smart Check (pilot March–November 2023) | It screened applications only, with 15 characteristics, no gender, nationality or age, bias tests, reweighting and a Deloitte review. Bias came back in live use, against Dutch nationals, women and parents. The alderman stopped it after about 1,600 applications and an estimated €500k+ ([MIT Technology Review](https://www.technologyreview.com/2025/06/11/1118233/amsterdam-fair-welfare-ai-discriminatory-algorithms-failure/amp/)). | Even best practice on a narrower scope failed. Expect "no-go" to be a likely and legitimate result. |
| DUO student grant checks (2012–2023) | It used only age, distance and education level. Students with a migration background were six times as likely to get a home visit. This was ruled indirect discrimination, and €61m was set aside for refunds ([Rijksoverheid](https://www.rijksoverheid.nl/actueel/nieuws/2024/11/11/gecontroleerde-oud-studenten-met-uitwonendenbeurs-krijgen-geld-terug)). | Leaving out sensitive variables does not prevent discrimination through proxies. |
| Belastingdienst (childcare benefits) | The AP fined the tax authority €2.75m for unlawful, discriminatory processing of dual nationality, including in its fraud-risk system ([NOS](https://nos.nl/artikel/2408587-boete-voor-belastingdienst-van-2-7-miljoen-voor-discriminatie-toeslagenouders)). | The regulator does enforce this. |
| Five Utrecht-region municipalities (2023) | Nieuwegein, Houten, IJsselstein, Lopik and Veenendaal used systems that flagged benefit-fraud risk based on, for example, type of work and neighbourhood. After complaints from the FNV union, the AP demanded an explanation ([Binnenlands Bestuur](https://www.binnenlandsbestuur.nl/digitaal/wmo-en-mantelzorg/ap-wil-uitleg-over-inzet-fraudealgoritme)). | Municipalities are directly in scope of AP scrutiny. |

---

## 4. Legal checklist (for the FG and legal to confirm)

The sources here are verified. Applying them to this case is my reading [ASSUMED], so your lawyers have the final word.

| Area | Question for this proposal | My reading |
|---|---|---|
| **AI Act Art. 5(1)(c): social scoring (applies since 2 Feb 2025)** | Does a fraud score built partly on debt-counselling and housing data lead to unfavourable treatment, such as an investigation, based on data from an unrelated context? Is that treatment out of proportion? | Real risk of a prohibited practice. The Commission's guidance lists welfare agencies scoring fraud risk on unrelated data as prohibited. Fraud detection on relevant data within the service context, with proportionate follow-up, falls outside the ban ([FPF summary](https://fpf.org/blog/red-lines-under-the-eu-ai-act-unpacking-social-scoring-as-a-prohibited-ai-practice)). |
| **AI Act Annex III 5(a): high-risk** | Is it a system used by a public authority to "grant, reduce, revoke, or reclaim" benefits? | Yes, very likely. The 2026 draft Commission guidelines treat flagging benefit claims for investigation as high-risk, because flagging affects scrutiny, delay, suspension or refusal. That holds even when a caseworker takes over after the flag. Profiling also rules out the Art. 6(3) exemption ([Annex III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3); [draft guidelines](https://www.dirittobancario.it/wp-content/uploads/2026/05/Draft-Guidelines-on-the-classification-of-high-risk-AI-Annex-III.pdf)). |
| **Deployer duties (from 2 Dec 2027 after the Omnibus, Regulation (EU) 2026/1744)** | Can you meet Art. 26 (competent human oversight, relevant and representative input data, monitoring, logs kept for at least 6 months, informing every affected resident), Art. 27 (FRIA before use) and Art. 49(3) (registering your use in the EU database)? | These are required. Build them in now, because the system would be running when they apply ([Art. 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26); [Art. 49](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-49); [Omnibus dates](https://www.cuatrecasas.com/en/portugal/intellectual-property/art/digital-omnibus-ai-has-been-published)). |
| **Transition trap** | Under Art. 111(2), a system put into service before the application date is caught only on significant change, and public-authority deployers must comply by 2 Aug 2030 ([Art. 111](https://artificialintelligenceact.eu/article/111/)). | Do not use this as a reason to rush. Retraining may count as a significant change, and the GDPR, the ECHR, equal-treatment law and Art. 5 apply now. |
| **GDPR Art. 22 + UAVG Art. 40** | If investigators rely heavily on the score, the score itself can count as an automated decision: the CJEU's SCHUFA ruling covers scores given "a determining role" ([CJEU](https://curia.europa.eu/jcms/jcms/p1_4213242/en)). The Dutch exception in UAVG Art. 40 excludes decisions based on profiling ([UAVG Art. 40](https://omgevingsweb.nl/wetgeving/uitvoeringswet-algemene-verordening-gegevensbescherming/hoofdstuk-4-uitzonderingen-en-beperkingen/artikel-40-uitzonderingen-op-verbod-geautomatiseerde-individuele-besluitvorming/)). | Design the process so the score never decides on its own. Investigators record their own reasons, and the score never triggers a suspension. Even then, have legal check this. |
| **GDPR purpose limitation (Art. 5(1)(b), 6(4)), Wgs/Bgs (debt-help law and decree)** | May debt-counselling data be reused for fraud scoring? | Probably not. The VNG guide ties processing to the debt-help purpose. It allows fraud-related data only if the council's debt-help policy plan includes it, and it advises restraint ([VNG](https://vng.nl/sites/default/files/2025-10/handreiking-schuldhulpverlening.pdf)). Debt data may also contain health data (GDPR Art. 9). **Exclude it in every scenario.** |
| **GDPR Art. 35–36: DPIA and prior consultation** | Large-scale profiling of a vulnerable group. | A DPIA is mandatory, with the FG involved. If high risk remains, prior consultation with the AP is required: up to 8 weeks, extendable by 6. |
| **ECHR Art. 8 (SyRI)** | Is the intrusion transparent, verifiable and proportionate? | Scoring the entire population continuously, on data from three sources, is the hardest version to defend. |
| **Equal treatment (Art. 1 of the Constitution, AWGB) and Awb (careful preparation and stated reasons, Art. 3:2 and 3:46)** | Indirect discrimination through proxies; being able to explain each selection to the resident and to a judge. | Test error rates for each group independently. The vendor must make every score explainable. |
| **Procurement law** | Is the contract value above the EU threshold? | If it is, a direct award is not possible, and a tender takes months [ASSUMED]. |

---

## 5. Twelve questions for the vendor (no answers, no further talks)

1. **"90% accurate":** which metric, on which dataset, which period and which municipality? Provide the confusion matrix at a 10% cut-off.
2. **Precision in the top 10%:** compared with random selection and with the customer's previous selection method.
3. **Labels:** what counts as "fraud" in the training data (established intent, any overpayment, any investigation outcome)? How were the training cases selected?
4. **Error rates by group:** false-positive rates by gender, age, nationality or migration background, household type (including single parents), language and neighbourhood. Will they be tested on our data by an auditor we choose?
5. **Variables:** the full variable list, the source of each data element, and an analysis of proxies (postcode, language, household type).
6. **Explainability:** can every individual score be explained to the resident and in an objection or appeal?
7. **AI Act provider duties:** will the system be conformity-assessed as high-risk before 2 Dec 2027? Can they provide the technical documentation, instructions for use, logging, human-oversight design and accuracy metrics?
8. **Social scoring:** has the vendor assessed Art. 5(1)(c), specifically for debt-counselling and housing data? Ask for it in writing.
9. **Data handling:** hosting, sub-processors and BIO compliance (the Dutch government security baseline). Is our data used to train models for other clients?
10. **Audit access:** full access to the model, code and training data for an independent auditor, the Rekenkamer (local audit office) and the AP. Agreement to publication in the national algorithm register.
11. **Exit terms:** we own our data and outputs. We can terminate without penalty if an auditor, the FG or a regulator says no. Escrow and a migration path.
12. **References:** which Dutch municipalities use the system, what their audited hit rates are, and whether there has been any AP, court or Rekenkamer involvement.

---

## 6. Six-month plan (Option C) and go/no-go criteria

| Month | Action | Owner |
|---|---|---|
| 0–1 | Written advice to the alderman and the college. FG opinion and AI Act classification. Vendor questions sent. No resident data to the vendor, not even for a "demo". Consult the investigators and the client council (Cliëntenraad). | CIO, FG, legal, alderman |
| 1–4 | Random-sample review of about 200 files, from existing capacity. It measures prevalence, mistakes versus intent, and bias in today's selection (the head of Work & Income sets the sample size with a statistician). In parallel: clear the backlog of existing lawful signals (Inlichtingenbureau matches, BRP changes), prioritised by size and age of the discrepancy. These are explainable rules, not a score per person. | Head of Work & Income, enforcement team leader, analyst |
| 1–4 | Prevention: clearer letters on the duty to report changes, easy income-change reporting and reminders. Fewer honest mistakes means fewer "fraud" cases. | Head of Work & Income, communications |
| 2–5 | Only if the council wants to keep exploring: write requirements for a narrow tool (no debt-counselling data, no score for every resident), draft the DPIA, FRIA and IAMA, and run a market consultation. Commission an independent sandbox test of the vendor model on historical data, once the DPIA allows it. | CIO, procurement, FG |
| 6 | Go/no-go memo to the council: baseline figures, legal opinions, audit results and a recommendation. "No-go" is a legitimate outcome. | Alderman, on the CIO's advice |

**Criteria for "go". All of them must hold; the thresholds are proposals for the college to set.**

1. The FG and legal confirm a legal basis for every data element, no Art. 5 issue, and no debt-counselling data.
2. The DPIA residual risk is acceptable, or the AP prior consultation is complete. The FRIA is done.
3. An independent test on your own data shows top-10% precision clearly above both the random-sample baseline and today's selection. Proposed threshold: at least 1.5x.
4. False-positive rates for each group stay within an agreed tolerance. Proposed: no group above 1.25x the average. Bias testing may itself need special-category data, so arrange a legal basis for it first.
5. The score never decides alone. Investigators record their own reasons, and no suspension is based on the score.
6. Residents are informed, the use is published in the algorithm register, and there is an objection route.
7. The contract includes audit access, exit without penalty and no reuse of your data.
8. A monitoring plan is in place: quarterly error-rate review per group, an annual independent audit, a named owner and a kill switch.

---

## 7. Talking points for the alderman

- **"Your goal is right."** Investigators should spend their time where it matters. This plan delivers that within your six months.
- **"In six months you can say three things."** We target better, we measured fraud honestly for the first time, and we did not repeat Rotterdam.
- **"No one can defend the vendor's 90% figure."** Random selection already scores 86%. We will judge any tool on how many innocent residents it sends us, not on a sales figure.
- **"Debt-counselling data stays out."** People must be able to ask for debt help without becoming fraud suspects.

---

## 8. Critic pre-screen (high-stakes decision)

- **Weakest point:** This advice assumes the vendor's model performs like Rotterdam's. A modern model on cleaner data could genuinely beat today's selection. *Mitigation:* the recommendation is conditional. The month-6 test measures exactly this.
- **Missing perspectives:**
  - The investigators and residents (client council) have not been asked yet.
  - Fraud savings may already be booked in the budget. If they are, a "no-go" opens a budget gap, so ask finance now.
- **If this advice is wrong, the cost is:** a useful tool arrives about 12 months later, with some recoveries missed. That is modest next to Option A's downside: fines, refunds, court cases, a possible prohibited practice and lasting loss of trust.
- **Verdict:** Proceed, with the risks noted above.

---

## 9. Assumptions to verify

| Assumption | Verify with |
|---|---|
| 3,000 recipients; prevalence 2–10% | Work & Income (the random sample replaces this with a real figure) |
| 12–18-month realistic timeline | Procurement, FG, IT integration lead |
| Cost ranges in section 1 | Finance, vendor quote |
| Legal readings (Art. 5, Annex III, Art. 22/UAVG 40, Wgs) | Legal counsel, FG |
| Debt-help avoidance effect | Debt-help team, client council |
