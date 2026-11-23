# AI CV screening rollout plan (NL / BE / DE)

I can set up a rollout plan, but not for the design you described. Scoring every CV and auto-rejecting the bottom 70% with no recruiter involved shouldn't go live as specified. It is the one configuration that is hardest to defend legally, and it is also weak on quality grounds. Below is why, followed by a plan that gets you most of the time savings without that exposure.

## Why not as specified

**1. Auto-rejection without a human is a legal problem in all three countries.**
- GDPR Art. 22 restricts decisions based solely on automated processing that significantly affect a person. A job rejection qualifies. The CJEU's SCHUFA ruling (C-634/21, Dec 2023) held that a score a third party relies on heavily can itself count as the automated decision. A recruiter rubber-stamping scores would not fix this. Review has to be real.
- The EU AI Act classes AI used to filter or evaluate job applicants as high-risk (Annex III). That brings requirements for risk management, data governance, logging, human oversight, transparency to candidates, and deployer obligations for you. The application date for high-risk obligations has been subject to postponement proposals. Have counsel confirm the current date, but plan for compliance rather than for a delay.
- A DPIA (GDPR Art. 35) is mandatory before go-live. Systematic scoring of applicants at this scale clearly meets the threshold.
- Candidates have rights to information about the logic involved and to human intervention. At 2,800 automatic rejections a month (70% of about 4,000), you would receive and have to handle those requests.

**2. "Bias-free and GDPR-compliant" is a sales claim, not evidence.**
No CV-scoring model is bias-free. Models trained on past hiring decisions learn past patterns, and proxies such as postcode, employment gaps, part-time history, name, school and age-correlated phrasing can carry gender, ethnicity, age and disability effects even when those fields are excluded. GDPR compliance also can't be certified by the vendor alone. As controller, you carry the accountability, and the vendor is your processor at best. Ask the vendor for documents rather than assurances (see the due diligence list below).

**3. Discrimination law applies directly.**
Germany's AGG, Belgium's federal anti-discrimination acts and the Dutch Equal Treatment legislation all apply to selection. Indirect discrimination through a scoring model is still discrimination, and the burden of proof shifts to the employer once a plausible pattern is shown. Being unable to explain why a given person was rejected makes that very hard to rebut.

**4. Works council and employee representation.**
- Germany: a Betriebsrat has co-determination rights over technical systems capable of monitoring behaviour or performance (BetrVG s.87(1) no. 6) and over selection guidelines (s.95). Expect to need a works agreement before go-live.
- Netherlands: the ondernemingsraad has consent rights over personnel selection systems and automated processing of personal data of employees and applicants (WOR art. 27).
- Belgium: information and consultation duties apply through the works council or union delegation, depending on your structure.
Switching it on without that process can get the system blocked after you've launched it.

**5. The "bottom 70%" cut-off is arbitrary.**
It has nothing to do with candidate quality. A fixed quota will reject qualified people whenever a role has a strong applicant pool, and it will reject almost everyone good when the pool is thin. It will also behave very differently across roles: a warehouse operative role and a data analyst role do not have the same score distribution. Retail and e-commerce hiring also includes many seasonal, part-time and entry-level roles where CV-based scoring is a weak predictor anyway.

**6. Business risk.**
A discrimination finding, a regulator inquiry (Autoriteit Persoonsgegevens, Belgian GBA/APD, German Länder authorities), or a press story about a retailer silently rejecting 2,800 people a month would cost far more than the recruiter time saved.

## What I recommend instead

Use AI to **prioritise and assist**, never to reject alone. People make every rejection, but recruiters see a ranked, explained shortlist instead of a flat pile.

Targets I'd set: cut time-to-first-review substantially, keep a human decision on 100% of rejections, and show no adverse impact above agreed thresholds. Treat the numbers as hypotheses to validate in the pilot, not promises.

## Phased rollout

### Phase 0: Decide and prepare (weeks 0-6, before any candidate data touches the module)
- Name one accountable owner (HR) with Legal, the DPO, IT/security and employee representatives in the group.
- Run vendor due diligence (list below). If the vendor can't supply it, that is your answer about the vendor.
- Complete the DPIA. Document lawful basis (legitimate interest is the likely route; consent is weak in an employment context), data minimisation and retention.
- Open consultation with the works councils (DE Betriebsrat, NL OR, BE works council or union delegation) and aim for a written agreement per country.
- Complete the AI Act classification and gap assessment. Document your deployer duties: human oversight assignment, logging, monitoring, informing candidates.
- Define success measures up front: time-to-review, recruiter hours saved, quality-of-hire proxies (interview-to-offer ratio, 90-day retention), candidate experience, and fairness metrics.
- Update the candidate privacy notice and application-flow wording in NL, DE and BE languages (Dutch, French, German, English).

### Phase 1: Shadow mode (weeks 6-12)
- Run the model in the background on live applications. Recruiters work exactly as today and don't see scores.
- Compare model scores with actual recruiter outcomes by role family, country and language. Check:
  - Where the model and recruiters disagree, and who is right on review.
  - Selection-rate ratios by protected groups where you can lawfully measure them. Where you can't collect the data directly (often the case in the EU), use proxies carefully and with DPO sign-off, or use a third-party audit on a test set.
  - Performance on non-standard CVs: career changers, returners, non-native-language CVs, gaps.
- Set go/no-go thresholds in advance (for example, selection-rate ratio no lower than 0.8 for any group, as a flag for investigation rather than a safe harbour).

### Phase 2: Assisted triage pilot (weeks 12-20, 2-3 role families, one country first)
- Scores and short, plain-language reasons are shown to recruiters as a sort order. Nothing is hidden or auto-closed.
- Recruiters must open and decide on every application. The low-scoring tail is reviewed in a faster format, with random sampling to catch misses.
- Log every override with a reason. Track how often recruiters accept the model, and watch for automation bias (rubber-stamping).
- Candidates can request human review, and a named mailbox and SLA exists for it.
- Review fairness metrics every month with HR, Legal and employee representatives.

### Phase 3: Scale with controls (months 6-12)
- Extend to further roles and countries only where Phase 2 metrics hold. Re-run the DPIA and works council steps for each country as needed.
- Put in place ongoing monitoring: drift, adverse impact, override rates, complaint rates, an annual independent bias audit.
- Review your retention periods and deletion of candidate data.
- Re-validate after every vendor model update. Contract for advance notice of changes.

### Where fully automated action could be considered later
Only narrow, objective, legally required knock-out criteria (for example, a missing mandatory work permit or required licence for a regulated role) should ever be auto-actioned, and only with candidate transparency and an easy route to human review. Even those are better handled as a flag than an automatic rejection. Never an overall quality score.

## Vendor due diligence: documents to request
- Model documentation: training data sources, features used, how protected characteristics and proxies are handled.
- Independent bias and validation testing, with methodology and results by group, for EU populations and the languages you use.
- AI Act conformity position: risk management, logging, human-oversight design, technical documentation, and the planned conformity assessment.
- Data processing agreement: processor role, sub-processors, hosting location, international transfers, whether your applicant data is used to train models for other customers (it should not be without your explicit agreement).
- Explainability: per-candidate reasons you can give a candidate or a regulator.
- Contract terms: audit rights, incident notification, liability and indemnity for discrimination and data protection claims, notice of model changes.

## Immediate next steps (next 2 weeks)
1. Do not switch on auto-reject. Make sure the module's auto-action setting stays disabled, and confirm in the admin console who can change it.
2. Appoint the owner and convene HR, Legal, the DPO and IT.
3. Send the due diligence request to the vendor.
4. Brief the works councils early. Early involvement is much cheaper than a blocked launch.
5. Start the DPIA.
6. Get written advice from employment counsel in each country on the points above, since I can't give you legal advice and the rules differ across NL, BE and DE.

## Caveats
This is a planning and risk summary, not legal advice. The AI Act timing, national implementation and regulator guidance are still moving, so verify the current position with counsel before committing dates. The week numbers above are a reasonable shape for a group of your size, but your works council processes may take longer, and they set the real critical path.

If useful, I can draft the vendor questionnaire, the DPIA outline or the works council briefing note next.
