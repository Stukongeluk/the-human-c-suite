# AI CV screening: rollout plan (Netherlands, Belgium, Germany)

Draft for decision · 23 November 2026 · Owner: CHRO · Sign-off needed: DPO, employment counsel NL/BE/DE

Tags: [Verified] = checked against the law or a named source (links at the end). [Likely] = sound reading of the law or a single source, which counsel should confirm. [Assumed] = not checked against your data.

---

## 1. What the system will and won't do

These are the operating rules for the recommended setup (Option B). Put them in the works-council agreements and the vendor contract.

1. **The AI never rejects anyone.** It ranks, explains its reasons and flags. Auto-reject is switched off and locked at tenant level.
2. **A trained recruiter confirms every rejection after seeing the CV**, not just the score. Advancing a candidate takes one click and needs no justification. Rejecting needs a reason code.
3. **Scores don't use** name, photo, date of birth or age, gender, nationality, address or postcode, or marital status. Career gaps are not penalised. Photos and dates of birth are stripped before scoring; this matters most for German CVs.
4. **Thresholds are set per job family from your shadow-mode data.** No fixed 70%. A fixed cut rejects qualified people in strong pools and passes unqualified ones in weak pools.
5. **Speed is the point.**
   - Top-ranked candidates hear from you within 2 working days.
   - Every applicant gets an answer within 5 working days. [Assumed targets]
6. **Every applicant can ask** how their application was assessed and request a second review by a different recruiter.
7. **Bias is monitored monthly,** with an automatic pause when a threshold is breached (section 9).
8. **No vendor model update goes live** until it has been re-tested (section 7).

## 2. Why not auto-reject the bottom 70%

| Issue | What it means for you | Tag |
|---|---|---|
| GDPR Art. 22 | People have the right not to be subject to a decision based solely on automated processing that significantly affects them. Recital 71 names "e-recruiting practices without any human intervention" as the example. The exceptions (necessity for a contract, authorisation by law, explicit consent) are narrow. "Necessary" fails when a less intrusive alternative works, and here one does at 0.3–0.6 FTE. Consent is rarely free for job applicants. Even when an exception applies, you owe human intervention, the right to give a view and the right to contest. | [Verified: Art. 22, Recital 71; Likely: consent point] |
| Token human review doesn't count | Human oversight has to be meaningful, and the reviewer must be able to override. In SCHUFA (C-634/21) the CJEU treated a score that the decision-maker relies on heavily as the decision itself. A click-through review queue would therefore carry the same Art. 22 risk as auto-reject. | [Verified: SCHUFA summary; Likely: application to hiring] |
| You are the controller | "GDPR-compliant vendor" covers only the vendor's processing. The DPIA (Art. 35(3)(a): systematic automated evaluation that decisions are based on), the transparency about the logic (Art. 13(2)(f)), and the explanation on request are yours. Under CJEU C-203/22 the explanation must cover the "procedure and principles actually applied"; handing over the algorithm is not enough. | [Verified: C-203/22; Likely: Art. 35/13] |
| Discrimination liability stays with you | Per the Netherlands Institute for Human Rights, employers cannot shift responsibility onto the algorithm or the vendor. That holds even when a self-learning system didn't discriminate at the start. | [Verified] |
| AI Act | CV filtering is high-risk under Annex III point 4(a). After the AI Omnibus (Regulation (EU) 2026/1744, in force since 27 July 2026), Annex III obligations apply from **2 December 2027**. The emotion-recognition ban at work has applied since February 2025. | [Verified] |
| Germany: AGG | A rejected applicant who wouldn't have been hired anyway can still claim compensation of up to three months' pay. Claims must be made in writing within two months of receiving the rejection. Once there are indications of discrimination, the burden of proof shifts to you (§22 AGG), so your logs and bias audits become your evidence. | [Verified: §15; Likely: §22] |
| Prediction quality | In the updated meta-analysis, structured interviews (.42), job knowledge tests (.40) and work samples (.33) top the validity rankings. A CV keyword score is not a validated predictor until the vendor shows criterion validity for your roles. | [Verified: SIOP summary of Sackett et al.] |

## 3. The economics

| | Option A (auto-reject) | Option B (human confirms) |
|---|---|---|
| Applications/month | 4,000 | 4,000 |
| Low-ranked bucket | 2,800 rejected unseen | 2,800 confirmed by a recruiter at 1–2 min each |
| Extra recruiter time vs. A | – | 47–93 h/month = 0.3–0.6 FTE ≈ €20–47k/year |
| Ranking benefit (top 30% handled first, contacted within 2 days) | Yes | Yes |
| Legal exposure | Art. 22 breach as designed; GDPR fine ceiling €20M or 4% of global turnover (Art. 83(5)); AGG claims; OR nullity in NL | Manageable with the controls below |

[Assumed: 150 productive hours per FTE per month; €65–75k fully loaded recruiter cost; 1–2 minutes per pre-sorted, low-ranked CV. Shadow mode will measure the real review time.]

The real business gain doesn't come from skipping reading. It comes from contacting the best candidates first and fast, which is what moves the targets: time to fill under 45 days and offer acceptance above 85%.

## 4. Phases, gates and owners

| Phase | Dates | What happens | Gate to move on | Owner |
|---|---|---|---|---|
| 0. Hold and prepare | 23 Nov 2026 – 22 Jan 2027 | Auto-reject locked off. Vendor evidence request (section 6). Synthetic paired-CV audit in the sandbox (section 7). DPIA. Privacy notice and rejection-email text (section 8). Works-council tracks opened (section 5). Recruiter training designed. | Vendor evidence complete. Paired audit shows no material gaps. DPIA signed by the DPO. Pilot agreement with the pilot country's works council. | Head of TA |
| 1. Shadow mode | 25 Jan – 2 Apr 2027 (pilot country, all job families) | The AI scores every application. Recruiters decide as today, with scores hidden. Analytics compares the two. | Thresholds in section 7.2 are met. Go/no-go meeting 2 Apr 2027. | Head of TA + TA analytics |
| 2. Assisted pilot | 5 Apr – 25 Jun 2027 (pilot country, 1–2 job families) | Ranking is visible. Recruiters work top-down. Every rejection is human-confirmed. Review link in all rejections. Monthly dashboard. | Section 9 metrics are in range for 12 weeks. Works-council review meeting held. | Head of TA + country HR Director |
| 3. Scale | From Jul 2027 | Roll out country by country as agreements land. Every new job family gets a 4-week shadow period first. | Same gates, per job family | Head of TA |
| 4. Six-month review | Sep 2027 | Results to the executive team and works councils. Decide on Option C (limited auto-reject on objective, candidate-declared hard requirements). | DPO and counsel sign-off if C is chosen | CHRO |
| 5. AI Act ready | By 2 Dec 2027 | Deployer obligations live (section 10) | Checklist complete | DPO + AI risk owner |

**Pilot country:** the Netherlands by default [Assumed: largest volume and the clearest consent route]. Switch to Belgium if its consultation finishes first. Germany goes last unless its works agreement (Betriebsvereinbarung) is signed early.

**For high-volume store and warehouse roles (Phase 3 improvement):** consider replacing CV scoring with 4–6 structured application questions: availability, location, right to work, and a short situational-judgement set. This is better validated than CV text. It also stops the filter from working against students, people returning to work and applicants without a polished CV. The same rules and works-council agreements apply to these questions.

## 5. Country tracks

### Netherlands
- **Works council (OR) consent** under Art. 27(1)(e) WOR: regulations on hiring policy, which covers general rules on recruitment and selection. [Verified] Sub (k) on personal data and sub (l) on systems that can monitor staff may apply on top, because recruiters' use of the tool and internal applicants are involved. [Likely]
- **What to submit:** a written consent request containing the section 1 operating rules, the DPIA summary, the vendor evidence, the monitoring plan and the kill switch.
- **If you go without consent:** the OR can invoke nullity in writing within a month, and the decision then counts as not taken. If the OR refuses, you can ask the subdistrict court for replacement consent. [Verified]
- **Discrimination:** equal treatment law, overseen by the Netherlands Institute for Human Rights. Their four points: algorithms can discriminate; you must be able to explain how they work; the process must be transparent, controllable and systematic; and you are legally responsible. [Verified]
- **Timing:** first meeting by 18 Dec 2026; consent decision targeted by 26 Feb 2027, ahead of the pilot gate. [Assumed]

### Belgium
- **CBA No. 39:** inform and consult employee representatives on new technology with significant collective consequences, before you implement and ideally before you buy. [Verified] Counsel should confirm the minimum notice period. [Likely: commonly cited as at least three months]
- **CBA No. 9:** inform the works council about personnel-policy rules and planned changes, including new AI recruitment tools. [Verified]
- **CBA No. 38 on recruitment and selection:** non-discrimination, respect for applicants' privacy and information to applicants. Check that the rejection flow complies. [Likely]
- **Languages:** validate the model separately for Dutch, French and German CVs, plus English. [Assumed]
- **Timing:** information and consultation start by 18 Dec 2026; earliest implementation follows the notice period counsel confirms.

### Germany
Applies wherever a works council (Betriebsrat) exists, at site, company or group level. [Assumed: at least some German entities have one]
- **§90(1) no. 3 BetrVG:** inform the works council in good time about AI planning, with documents, and consult. [Verified]
- **§80(3):** an external expert is deemed necessary when the council assesses AI. Budget for it; the legislator assumes about €833 per day including VAT. [Verified]
- **§87(1) no. 6:** co-determination over technical systems, which includes software- and web-based AI tools. No intent to monitor is required. [Verified] Monitoring recruiters' review times or override rates is itself covered by this, so agree it in the works agreement and report at team level only.
- **§95(1) and (2a):** selection guidelines need consent, also when AI is used to draw them up. [Verified]
- **§94:** if you add application questionnaires or chatbots, these can count as personnel questionnaires and need consent. [Verified]
- **§99 (individual hires):** have counsel confirm how AI-ranked and rejected applicants are handled in the application documents the works council receives. [Likely]
- **AGG:** see section 2. Keep per-decision logs for at least the claim window plus any proceedings. [Likely]
- **CV conventions:** photo and date of birth are common, so strip them before scoring.
- **Timing:** §90 information by 18 Dec 2026; works agreement targeted by 31 Mar 2027, realistically Q2. No shadow mode in Germany without a pilot agreement.

## 6. Vendor evidence request (ready to send)

Send by 4 Dec 2026; answers due 8 Jan 2027. Treat missing answers as "no".

1. **Model:** what kind of model is it (rules, machine learning, LLM)? Which version? How often is it updated? Will you notify us before changes, and can we pin a version?
2. **Training data:** what data was the model trained on? Does it include our historical hiring decisions? Are our applicants' data used to train or improve models, for us or for other clients? (We require no, unless agreed separately in writing.)
3. **Features:** which CV fields influence the score? Confirm that name, photo, date of birth or age, gender, nationality, address or postcode and marital status can be excluded, and that photos and dates of birth are stripped before scoring. How are career gaps treated?
4. **Bias testing:** send your adverse-impact results by gender, age band, ethnicity or migration-background proxies, and disability where available. On which data were they produced, and for which countries and languages? Was there an independent audit? Please send the report.
5. **Languages:** is performance validated separately for Dutch, French, German and English CVs?
6. **Validity:** what evidence shows that the score predicts job outcomes (performance, 90-day retention) for retail store, warehouse, customer-service and e-commerce office roles? Agreement with recruiters doesn't count as validity.
7. **Explanation:** what reasons does the recruiter see for each score? What could we give an applicant who asks, under GDPR Art. 15 and CJEU C-203/22?
8. **Logging:** do you log the inputs, score, model version and reviewer action for each application? For how long, and can we export them?
9. **Configuration:** can auto-reject be disabled and locked at tenant level? Can we set thresholds per job family?
10. **Prohibited features:** does any feature infer emotions, personality or traits from video, voice or photos? If so, confirm it is disabled.
11. **AI Act:** do you classify the module as high-risk under Annex III 4(a)? What is your timeline for conformity assessment, CE marking, EU database registration and instructions for use before 2 December 2027?
12. **GDPR:** the Art. 28 data processing agreement, sub-processors, hosting location, transfers outside the EEA and their legal mechanism, retention and deletion, and material to support our DPIA.
13. **Security:** ISO 27001 or SOC 2 reports, the latest penetration test summary, and incident notification terms.
14. **Contract terms:** audit rights, notice of model changes, cooperation on data-subject requests and explanations, and indemnity for claims attributable to the model.
15. **References:** which clients in NL, BE or DE run this module under a works-council agreement? Can we see an anonymised template?
16. **Exit:** how are data returned and deleted when the contract ends?

## 7. Testing protocol

### 7.1 Paired-CV audit (Phase 0, synthetic data, no applicant data needed)
- **Base set:** 30 base CVs for each of 4 job families (store associate, warehouse, customer service, e-commerce office role), so 120 base CVs.
- **Variants:** change one attribute at a time:
  - name origin: Dutch, Flemish or German vs. Moroccan, Turkish, Polish, Surinamese or Syrian, each in a male and a female version
  - age signals: graduation year or date of birth
  - a 12-month gap: labelled parental leave, illness, or unexplained
  - part-time history
  - photo vs. no photo
  - the same CV written in NL, FR, DE or EN
  - a foreign degree
- **Repeats:** score every variant 3 times, to catch run-to-run variance in LLM-based scoring.
- **Fail conditions:**
  - a consistent score gap on any attribute, or
  - more than 5% of pairs where the variant crosses the low-bucket threshold and the base CV doesn't. [Assumed threshold]
- **Owner:** TA analytics, with the DPO reviewing the method. Effort: about 2–3 analyst-weeks. [Assumed]

### 7.2 Shadow-mode thresholds (Phase 1 gate)
| Check | Pass level |
|---|---|
| Recruiter-advanced candidates that the AI put in the low bucket | ≤ 5% |
| Hires that the AI put in the low bucket | ≤ 2% |
| Selection-rate ratio for reaching the "not low bucket" outcome, for each monitored group (gender, age band, country, CV language) vs. the best-treated group | ≥ 0.8 |
| Same CV scored twice | Same bucket ≥ 95% of the time |
| Sample of 50 low scores | A recruiter can state the reason in one sentence from the system output |

[Assumed pass levels. Set final values with the DPO and the works councils.] The 0.8 ratio is a US rule of thumb (the "four-fifths rule"). Use it as an early warning, not as a legal defence: EU discrimination law has no safe-harbour ratio. The AI Omnibus extended the legal basis for processing special-category data for bias detection to deployers, with a strict necessity test. [Verified] Have the DPO design any voluntary self-identification survey for bias monitoring on that basis.

## 8. Candidate-facing text (draft; translate into NL, FR and DE)

**Privacy notice addition:**
> We use software from [vendor] to help us sort applications. It compares the information in your CV and your answers with the requirements of the vacancy, and suggests an order for our recruiters. It does not use your name, photo, age, gender, nationality or address. A recruiter reads and decides on every application. The software never rejects anyone on its own. You can ask us how your application was assessed, and ask for a different recruiter to review it.

Only publish the "does not use" sentence once the vendor has confirmed it in writing and the paired audit backs it up.

**Rejection email line:**
> A member of our recruitment team reviewed your application. If you would like to know why, or would like a second review, reply to this email or use [link] within 30 days. We will respond within 5 working days.

## 9. Human review standard, monitoring and kill switch

### What counts as a real review
- The reviewer sees the full CV and the reasons, not just a number.
- Each month, a second recruiter re-reviews a random 5% of confirmed low-bucket rejections without seeing the first decision. Their disagreement rate is a key metric.
- Recruiters are trained on automation bias and on when to override. Document the training: it is the AI-literacy measure under Art. 4 and the competence required under Art. 26(2) from Dec 2027.

### Monthly dashboard (pilot), quarterly after scale
| Metric | Target or band |
|---|---|
| Time to first response, top bucket / everyone | ≤ 2 / ≤ 5 working days [Assumed] |
| Time to fill (IC roles) | < 45 days |
| Offer acceptance rate | > 85% |
| 90-day voluntary turnover of hires | < 5% |
| Recruiter hours per hire | Down vs. baseline |
| Low-bucket override rate (team level) | 3–20%; outside the band, investigate [Assumed] |
| Median review time per low-bucket CV (team level) | Flag if < 15 seconds [Assumed] |
| Selection-rate ratios by monitored group | ≥ 0.8 |
| Second-review requests and the share reversed | Tracked; a reversal rate > 10% triggers recalibration [Assumed] |
| Discrimination complaints or claims | Every one reviewed by the DPO and counsel |

### Kill switch
Pause AI ranking for the job family and fall back to arrival order if any of these happens:
- a ratio below 0.8 for 2 months running
- a paired-audit failure after a model update
- a substantiated discrimination complaint
- a vendor model change made without notice
- a works-council agreement lapsing or being challenged

Owner: Head of TA. The DPO can trigger it independently.

## 10. AI Act deployer checklist (applies from 2 Dec 2027) [Likely: Art. 26/86/25; Verified: date and high-risk status]
- [ ] Use the system according to the provider's instructions for use (Art. 26(1)).
- [ ] Assign human oversight to named people with the competence, training and authority to override (Art. 26(2)).
- [ ] Make sure the job criteria and input data you configure are relevant and representative (Art. 26(4)).
- [ ] Monitor operation. Inform the provider and suspend use if a risk appears (Art. 26(5)).
- [ ] Keep the automatically generated logs for at least six months (Art. 26(6)).
- [ ] Inform workers' representatives and affected workers before putting the system into service (Art. 26(7)).
- [ ] Use the provider's information in the DPIA (Art. 26(9)).
- [ ] Tell applicants they are subject to a high-risk AI system (Art. 26(11)), and be ready to explain individual decisions (Art. 86).
- [ ] Don't fine-tune, rebrand or substantially modify the model yourselves. Doing so can make you the provider (Art. 25).
- [ ] Confirm the vendor's conformity assessment, CE marking and registration are complete before 2 Dec 2027.

## 11. Sign-offs needed before go-live

| Area | Who | What they check | By |
|---|---|---|---|
| GDPR, DPIA, Art. 22 analysis of Option B and any later Option C | DPO | DPIA, legal basis, notice text, review route | 22 Jan 2027 |
| Works councils and discrimination law | Employment counsel NL, BE, DE | Consent and consultation path, CBA 38/39 timing, §99, AGG exposure | 18 Dec 2026 (path); 31 Mar 2027 (agreements) |
| Vendor model claims and security | AI risk owner / CISO | Evidence pack, paired-audit method, security reports | 22 Jan 2027 |
| Budget | CFO / Finance | Analyst time, review time, external audit and German works-council expert | 18 Dec 2026 |

## 12. Where this plan could be wrong

- **Weakest point:** the 1–2 minute review estimate, and the assumption that recruiters will genuinely review. If the low-bucket queue turns into a click-through, Option B carries Option A's legal risk and costs more. The guards against this are the blind second review and the review-time flag.
- **Missing perspective:** candidates and store managers. Run a short candidate survey and two store-manager interviews during shadow mode.
- **If wrong, the cost:** a biased ranking still shapes decisions with a human in the loop, because people anchor on the score. That's why the paired audit and the monthly ratios stay mandatory under Option B.
- **Proceed:** yes, with these risks noted, and only after the Phase 0 gates.

## 13. Assumptions (no company context was available)
- Works councils exist in your NL and BE entities, and at least some German entities have a Betriebsrat.
- The ATS vendor is the AI Act "provider" and you are the "deployer". You don't fine-tune the model.
- Most of the 4,000 monthly applications are for store, warehouse and customer-service roles.
- The Netherlands is the largest-volume country.
- Recruiter fully loaded cost is €65–75k a year, with 150 productive hours per FTE per month.
- Reviewing a pre-sorted, low-ranked CV takes 1–2 minutes.
- All pass levels and bands marked [Assumed] are starting points to agree with the DPO and the works councils.

## Sources
- GDPR Art. 22 and Recital 71: [gdpr-text.com](https://gdpr-text.com/read/article-22/)
- CJEU C-634/21 SCHUFA, summary: [Bird & Bird](https://twobirds.com/en/insights/2023/global/key-takeaways-from-the-schufa-case-of-the-cjeu)
- CJEU C-203/22 Dun & Bradstreet Austria: [Court press release](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-02/cp250022en.pdf)
- AI Act Annex III: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/annex/3/)
- AI Omnibus in force, new dates: [White & Case](https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act); [Lewis Silkin](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today); [Sidley](https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/)
- AI and HR in the EU (2026): [Crowell](https://www.crowell.com/en/insights/client-alerts/artificial-intelligence-and-human-resources-in-the-eu-a-2026-legal-overview)
- Belgium, CBA 39 and CBA 9: [Osborne Clarke](https://www.osborneclarke.com/insights/what-should-employers-belgium-consider-when-using-ai-workplace)
- NL works council consent on hiring policy: [Rendement](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/instemmingsrecht-van-de-or-bij-personeelsbeleid.html); nullity and replacement consent: [Praxikon](https://www.praxikon.com/nl/posts/or-instemmingsrecht-ai-op-de-werkvloer)
- Netherlands Institute for Human Rights on employer responsibility: [HR Praktijk](https://www.hrpraktijk.nl/hr-tech/datagedreven-hr/werkgever-zelf-verantwoordelijk-voor-discriminerende-algoritmes-bij-sollicitatie-4-aandachtspunten/)
- §95 BetrVG: [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__95.html); BetrVG and AI (§§ 80, 87, 90, 94, 95): [CMS](https://cms.law/de/deu/legal-updates/einfuehrung-von-ki-im-unternehmen-einbindung-des-betriebsrats)
- §15 AGG: [gesetze-im-internet.de](https://www.gesetze-im-internet.de/agg/__15.html)
- AI CV ranking bias study (Wilson & Caliskan, 2024): [University of Washington](https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/)
- Selection-method validity (Sackett et al.): [SIOP](https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance)
