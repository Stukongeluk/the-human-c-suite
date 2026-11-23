# AI CV screening: rollout plan (NL / BE / DE)

Draft v0.1, 23 November 2026. Proposed owner: Head of Talent Acquisition.

## 1. Decision and design principles

**Decision:** we roll out the ATS screening module as decision support. It never rejects anyone on its own.

1. **A person decides every rejection.** The AI can prioritise, summarise and fast-track. It never closes an application.
2. **Human review has to be real.** The reviewer sees the CV as well as the score. They have the authority and the time to override, overriding is treated as normal, and override rates are tracked. Rubber-stamping a score still counts as an automated decision under GDPR.
3. **Score against job-relevant criteria** defined per role family. Never score against "people like those we hired before", because that copies past bias forward.
4. **The model doesn't see what it must not use:** photo, name, date of birth or age, gender, nationality, marital status, full address. They are removed before scoring, not just hidden in the UI.
5. **Thresholds are absolute and set per role family,** not a fixed percentile. Low-volume and shortage roles get no filtering.
6. **Candidates are told** that AI is used, what it looks at, and how to ask a person for a second look.
7. **Prove it before relying on it** (shadow pilot), then keep checking it (monitoring with stop conditions).
8. **No go-live in a country** until that country's works council process is complete.

## 2. Target screening flow

| Step | What happens | Who decides |
|---|---|---|
| 1. Job ad and application | Must-haves are stated up front: right to work, any legally required minimum age, shift availability, required licences or certificates. A candidate who doesn't meet one sees that before submitting and can still apply or look at other roles. For frontline roles, the CV is optional and a short form replaces it. | Candidate (self-selection) |
| 2. Scoring | The model scores against the role family's criteria with the fields in principle 4 removed. It outputs a band, reason codes and a 3-line summary. | Nobody. This is input only. |
| 3a. Top band | Fast-track: a recruiter contacts the candidate within 48 hours. | Recruiter |
| 3b. Middle band | Standard review. | Recruiter |
| 3c. Bottom band ("recommended reject") | The recruiter opens each application, with the CV and reason codes side by side, and confirms or overrides it individually. There is no bulk-reject button. | Recruiter |
| 4. Rejection message | Sent within an agreed SLA, in NL/FR/DE/EN. It gives the outcome, the main reason category, how to ask for a second look, and a link to other vacancies. | Recruiter (from a template) |
| 5. Second look | Handled by a different recruiter, with an answer within 10 working days. | Second recruiter |

**Quality controls:**
- Each week, a second recruiter re-reviews 5% of bottom-band decisions without seeing the score.
- Override rates and time per decision are tracked at team level. The aim is to spot rubber-stamping, not to rate individual recruiters. Measuring recruiter activity is itself a works council topic, so the agreements must cover it.

## 3. Phases

### Phase 0: Hold and set up (weeks 0–1)
- The module stays off: no auto-reject, and no scoring of live applicants until the DPIA covers it.
- Name the owners:
  - Head of TA (business owner)
  - DPO
  - Employment counsel in NL, BE and DE
  - ATS administrator
  - People analytics (monitoring)
  - Works council liaison in each country
  - Vendor manager
- The steering group meets every two weeks until go-live.
- **Exit:** owners are named and HR leadership has signed off on the principles in section 1.

### Phase 1: Groundwork (weeks 1–10)

| Workstream | Weeks | Content |
|---|---|---|
| a. Vendor due diligence | 1–4 | Send the questions in section 4. Unanswered questions block the project. Run paired CV tests in the vendor's sandbox (see Phase 2). These use synthetic CVs, so no real applicant data is needed. |
| b. DPIA | 2–8 | Required, because this is a systematic evaluation of people at scale with significant effects. Cover the pilot and live use. Include the Art. 22 analysis, legal basis, data minimisation, retention, transfers and the legal basis for bias monitoring. On retention, the Dutch DPA expects applicant data to be deleted about 4 weeks after the procedure ends (1 year with consent). In Germany, data is commonly kept about 6 months to defend AGG claims. Keep scoring logs long enough to audit and defend decisions, and no longer. |
| c. Criteria per role family | 2–6 | TA and hiring managers agree 4–8 job-relevant criteria per role family. Legal then screens them for proxies, such as "native speaker", "recent graduate", "no CV gaps" or "lives within 5 km". |
| d. Works councils | from week 2 | See section 7. Propose a two-step agreement: approve the pilot now, and agree the rollout later on the basis of the pilot data. Germany is usually the critical path, so allow 2–4 months there. |
| e. Candidate transparency | 4–8 | Update the privacy notice. Add an AI notice to the application page. Write rejection templates in NL/FR/DE/EN and define the second-look process. |
| f. Recruiter training | 6–10 | This covers the AI Act's AI-literacy duty, which applies already. Topics: what the score does and doesn't measure, automation bias, when and how to override, how to document a decision. |

**Exit:**
- Vendor answers are acceptable
- The DPO has signed off the DPIA
- Works councils have agreed the pilot in the pilot countries
- Candidate notices are live

### Phase 2: Shadow pilot (about weeks 10–20, at least 8 weeks of data)
- **Scope:** three high-volume role families, one per country. For example: NL e-commerce customer service, DE warehouse/logistics, BE store staff. Aim for at least 2,000 scored applications.
- **How it works:** the model scores every application in scope. Recruiters can't see the scores and screen as they do today. Afterwards, compare the model's bands with what recruiters actually did.
- **Paired testing** (start this in Phase 1): submit matched synthetic CVs that differ in one thing only. Vary the name, age signals, gender, a career gap, a photo, the CV language (NL/FR/DE/EN) or the postcode. The scores should not move.

**What to measure:**
- **Miss rate:** the share of candidates recruiters invited to interview whom the model placed in the bottom band. Review every eventual hire who was in that band, one by one.
- **Agreement:** how often the bands match recruiters' decisions overall.
- **Group differences:** bottom-band rates by country, CV language, age band, gender, career gaps and part-time history, using whatever is available.
  - The data needs a legal basis set out in the DPIA. The amended AI Act now gives deployers a basis to process special-category data for bias detection where strictly necessary, with safeguards. Alternatively, run a voluntary, anonymous diversity survey kept separate from the selection decision.
- **Reason quality:** can recruiters understand the reason codes and check them against the CV?

**Go/no-go criteria (proposed; agree them with the DPO, counsel and works councils before the pilot starts):**
- **Miss rate:** at most 5% of interview-stage candidates fell in the bottom band, and every bottom-band hire has been reviewed and explained.
- **Group differences:** each monitored group's pass rate (the share not placed in the bottom band) is at least 80% of the best-scoring group's rate. There is also no statistically significant gap that the job criteria can't objectively justify. The 80% figure is a US rule of thumb and gives no safe harbour under EU law, so use it as a tripwire only.
- **Paired tests:** score differences stay within the model's normal noise.
- **Vendor documentation** is complete.
- **If it fails:** fix the criteria or the configuration and re-run, or don't use the module for that role family.

### Phase 3: Assisted go-live (about weeks 20–32)
- **Wave 1 (weeks 20–24):** the pilot role families go live in assisted mode (section 2), in countries where the works council process is complete.
- **Wave 2 (weeks 24–32):** other high-volume role families follow. Each gets a 4-week shadow check before switching to assisted mode.
- **Low-volume and shortage roles** (for example, fewer than about 30 applicants per vacancy) get summaries only, with no bands.
- **Exit:** 8 weeks live with all monitoring metrics within range.

### Phase 4: Run and AI Act readiness (ongoing)

| When | What |
|---|---|
| Weekly | Bottom-band override rate, second-look requests and their outcomes, time to first response |
| Monthly | Group-difference analysis, miss-rate sample, any vendor model or version changes |
| Quarterly | Steering review, plus reporting to works councils as agreed |
| Yearly, and after any vendor model update | DPIA review and re-validation |
| By mid-2027 | Gap check against the AI Act deployer duties that apply from 2 December 2027 |

The duties covered by that gap check:
- Named, trained oversight staff with authority to override
- Logs kept for at least 6 months
- Informing candidates that a high-risk system is used
- Monitoring, with suspension and reporting if the system misbehaves
- Explanations on request

## 4. Vendor due diligence: send these now

1. **Evidence behind "bias-free".** Independent bias audit results broken down by sex, age band, ethnicity or nationality proxies and disability (where tested), and by CV language (NL, FR, DE, EN) and country. Include method, dates and model version. If they sell in New York City they will have a Local Law 144 bias audit. Ask for it, but note it only covers US categories.
2. **What the model is.** Is it an LLM or a trained classifier? What inputs does it use and what does it ignore? Can photo, name, date of birth, gender, nationality and address be removed *before* scoring?
3. **Validity.** Evidence that scores predict job performance or retention in retail, logistics or e-commerce roles, not just similarity to past hires.
4. **Explanations.** Reason codes per candidate that recruiters can use and that can be given to candidates on request. Both GDPR access rights and the AI Act's right to explanation need this.
5. **Configuration.**
   - A recommend-only mode with auto-reject disabled
   - Thresholds per role
   - The option to switch it off for chosen roles
   - A shadow mode with scores hidden from recruiters
6. **AI Act.** Do they confirm they are the provider of a high-risk system (Annex III, point 4(a))? What is their plan for conformity assessment, CE marking, EU database registration and instructions for use before 2 December 2027?
7. **No emotion or biometric analysis.** Written confirmation that there is no emotion recognition and no analysis of photos, video or voice. Emotion recognition in hiring is already prohibited.
8. **Data handling.**
   - The data processing agreement (Art. 28) and sub-processors
   - Data location and transfers
   - Retention configurable per country
   - Whether our applicant data is used to train or improve models for other customers. This must be excluded by contract.
9. **Audit access.** Can we export scores, reason codes, model versions and decisions for our own monitoring?
10. **Change management.** Advance notice of model updates, the ability to pin a version, and support for re-validation.
11. **Incidents.** A two-way process for reporting malfunctions and bias findings.
12. **Contract.** Warranties and indemnities for discrimination and data-protection claims arising from the model, audit rights, and data deletion on exit.

**Red flags:**
- Test results withheld as "proprietary"
- "Bias-free" claimed with no numbers
- No way to exclude fields before scoring
- No recommend-only mode
- Training on customer data by default

## 5. Capacity estimate (illustrative; replace with your own numbers)

Assumptions:
- 4,000 applications a month
- A manual first screen takes about 3 minutes today
- A bottom-band check takes about 1 minute with the summary and reason codes
- About 150 productive hours per FTE-month

| Scenario | Top + middle (1,200) | Bottom (2,800) | Hours/month | vs. today |
|---|---|---|---|---|
| Today: all manual | 60 h | 140 h | 200 h | — |
| Assisted (this plan) | 60 h | 47 h | ~107 h | about −47% |
| Full auto-reject | 60 h | 0 h | 60 h | −70% |

The gap between assisted screening and full auto-reject is about 47 hours a month, roughly 0.3 FTE across the group. AI summaries will probably also shorten top and middle-band reviews. Because thresholds are absolute, band sizes will vary by role family and won't be exactly 30/70.

## 6. Stop conditions

Pause scoring for the affected role family and tell the steering group within 48 hours if any of these happen:
- The group-difference tripwire is breached in the monthly analysis.
- The miss-rate sample is above threshold two months in a row.
- The bottom-band override rate stays below about 1% for a month, which suggests rubber-stamping. An override rate above about 20% means the model isn't helping; investigate either way.
- The vendor changes the model without notice.
- A credible discrimination complaint comes in, a regulator makes an inquiry, or a works council objects.
- Evidence emerges that the module processes data it shouldn't, such as photos.

## 7. Legal and consultation checklist (confirm with counsel in each country)

| | Netherlands | Belgium | Germany |
|---|---|---|---|
| Works council | OR consent: WOR art. 27(1)(d) (hiring policy), plus (l) if recruiter activity is monitored. A decision made without consent can be voided. | Information and consultation: CAO/CCT 39 (new technology with collective consequences). CAO/CCT 38 (recruitment and selection conduct) applies regardless. | Co-determination: §87(1) no. 6 BetrVG (technical systems). §95 (selection guidelines; §95(2a) explicitly covers AI). §90 (information). §80(3) (the works council may bring in an AI expert). Expect a (Gesamt-/Konzern-)Betriebsvereinbarung. |
| Equal treatment | AWGB; College voor de Rechten van de Mens | Federal anti-discrimination laws of 2007; Unia | AGG: the burden of proof shifts once there are indications of discrimination (§22). Compensation for applicants who wouldn't have been hired anyway is capped at 3 months' pay (§15). Claims must be made within 2 months. |
| Data protection authority | Autoriteit Persoonsgegevens | GBA/APD | State DPAs |
| Applicant data retention | About 4 weeks after the procedure ends; 1 year with consent | Confirm with counsel | About 6 months is common, to cover AGG claims |

**All three countries:**
- **GDPR:** Art. 22 (automated decisions), Arts. 13–15 (transparency and access, including the logic involved), Art. 35 (DPIA).
- **AI Act:** recruitment screening is high-risk (Annex III, point 4(a)), and deployer duties apply from 2 December 2027. The AI-literacy duty (Art. 4) and the prohibited practices (Art. 5, including emotion recognition in hiring) already apply.
- **European Works Council:** if you have one, check whether this counts as a transnational matter.

## 8. Assumptions and open points

- I've assumed the module can run in recommend-only and shadow mode. If it can't, that is the first blocker to raise with the vendor.
- I've assumed you have works councils in all three countries. Where an entity has none, its consultation step drops and everything else stays.
- The capacity figures are illustrative.
- This plan reflects the legal frameworks as they stand in November 2026, but it isn't legal advice. Counsel in each country should confirm the specifics before Phase 1 closes.

## Sources

- AI Act Digital Omnibus: Council final approval and new high-risk dates ([EEAS / Council](https://www.eeas.europa.eu/delegations/chile/artificial-intelligence-council-gives-final-green-light-simplify-and-streamline-rules_en)); entry into force on 27 July 2026, the new Annex III date of 2 December 2027, and the bias-detection legal basis extended to deployers ([Lewis Silkin](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today)); summary of changes ([Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement))
- Emotion recognition ban covers hiring ([FPF](https://fpf.org/blog/red-lines-under-eu-ai-act-unpacking-the-prohibition-of-emotion-recognition-in-the-workplace-and-education-institutions/))
- GDPR Art. 22, Recital 71 and commentary on contract necessity and meaningful human review ([gdpr-text.com](https://gdpr-text.com/read/article-22/))
