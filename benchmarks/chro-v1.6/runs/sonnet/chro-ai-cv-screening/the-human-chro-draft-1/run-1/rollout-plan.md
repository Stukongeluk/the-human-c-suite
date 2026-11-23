# AI-assisted CV screening: rollout plan (NL, BE, DE)

Status: draft for discussion with HR, Legal, the data protection officer and employee representatives. Not legal advice; local counsel should confirm the country points.

## What changes compared with the request

| Asked for | This plan |
|---|---|
| Score every CV | Yes. The score is used to sort and to show a recruiter why, not to decide. |
| Auto-reject the bottom 70% | No. Every rejection is made by a recruiter who has seen the application. Low scorers are read in a fast, structured review, not discarded. |
| Vendor says bias-free and GDPR-compliant | Treated as a claim to test, with our own data, before any live use. |

Why: an automatic rejection with no human is generally not allowed under GDPR Article 22 without a legal exception and safeguards, and a score a recruiter simply follows can count as the decision itself (CJEU, SCHUFA, C-634/21). CV screening is high-risk under the EU AI Act (Annex III); the deployer duties (human oversight, logs, monitoring, informing workers' representatives and candidates) apply from 2 December 2027 as currently scheduled, and it is cheaper to build them in now than to retrofit. A fixed 70% cut is also a quota: it rejects the same share whether the pool is strong or weak, and it is not tied to any job requirement.

## Phase 0: define the problem (weeks 1-3)

- Write down what we are solving: recruiter hours per month, time to first response, time to fill by role family, quality of hire, candidate drop-out. Get today's numbers from the ATS and HR system, in aggregate.
- Rough check to confirm: 4,000 CVs a month at about two minutes each is roughly 130 recruiter hours, around one full-time equivalent across three countries. If the real pain is store-manager or warehouse roles with very high volume, or slow replies, other fixes may beat scoring (shorter forms, knockout questions on legal must-haves such as work permit and availability, structured first-round questions, scheduling automation).
- Split volume by role family and country. Most retail and e-commerce roles (store, warehouse, customer service) need few CV-derived signals; the screening question differs a lot from tech or head-office roles.
- Name an accountable owner (Head of Talent Acquisition) and a data protection officer contact.

## Phase 1: legal and representative groundwork (weeks 1-8, in parallel)

Netherlands
- Works council (ondernemingsraad): consent right on recruitment and selection rules (WOR art. 27(1)(e)), on personal-data processing systems (27(1)(k)) and on systems suited to monitoring behaviour or performance (27(1)(l)). Bring it in at the problem stage, with the vendor's documentation and our baseline numbers, before choosing the configuration.

Germany
- Where a works council (Betriebsrat) exists: selection guidelines (section 95 BetrVG) and technical systems that can monitor behaviour or performance (section 87(1) no. 6 BetrVG) need its agreement. Ask which German entities have one rather than assuming. German candidates' data is also subject to the national employee data rules; counsel to confirm.

Belgium
- Check with Belgian counsel which works council or union delegation and which collective agreements apply (including rules on equal treatment in recruitment and on information about technology introduced at work). I have not verified the Belgian specifics; treat this as an open item.

All countries
- Data protection impact assessment (DPIA) completed and signed off by the DPO before any live use; lawful basis, retention periods for rejected candidates, and processor agreement with the vendor, including where the data and model run (EU or not).
- Confirm the module does no emotion recognition or inference of sensitive traits (prohibited in recruitment since 2 February 2025), and ask what features the model uses (for example name, photo, postcode, employment gaps, age proxies).
- One consistent candidate notice in Dutch, French, German and English: what is automated, what the score does, that a person decides, and how to reach a person and ask for review.

## Phase 2: test the vendor's claims on our own data (weeks 4-12)

Run the tool in shadow mode on past applications only (no effect on any candidate), under the DPIA.
1. Ask the vendor in writing for: model documentation and intended-use instructions, training data description, the bias audit and test data, and what it will log.
2. Compare score and "would be rejected" rates by gender, age band, part-time preference, nationality or migration background where lawful to analyse, disability where lawful, language, and country, at each stage. Use the four-fifths rule of thumb as a trigger for investigation, not as a pass mark.
3. Blind sample: have trained recruiters rate a few hundred CVs per role family without seeing the score; compare their shortlist with the tool's. Look for good candidates the tool rates low (false rejections), not only agreement.
4. Check proxy effects: employment gaps (parental leave, care), part-time history, foreign qualifications, non-linear careers, non-Dutch/German/French names.

Stop criteria agreed in advance: for example, any group's selection rate below 80% of the highest group without a job-related justification; recruiters judging more than an agreed share of low-scored CVs as worth interviewing; vendor unable to supply audit evidence. If a stop criterion trips, the module does not go live for that role family.

## Phase 3: pilot with a person on every rejection (months 3-6)

- Two or three role families, two countries to start, chosen with the works councils. A matched control group of roles screened the current way.
- How it works: the tool scores and shows the job-related reasons. Recruiters read the top band first. Lower bands go to a short structured review (a few minutes, same checklist for everyone), and a recruiter confirms each rejection. A random sample (for example 10% of low-scored CVs) is reviewed in full each week to catch what the tool misses.
- Candidates: told in the application flow; can ask for human review; rejection message names a contact. Candidates who ask for review get an answer within a set number of days.
- Recruiters: trained on what the score means and does not mean, with explicit authority to overrule it and no target that penalises overruling. Watch for automation bias (agreeing with the score by default) by tracking overrule rates.
- Log every score, reviewer decision and overrule for audit.

Measures, reported to the works councils monthly: selection rates by group at each stage; false-rejection rate from the weekly sample; recruiter hours saved; time to first response; time to fill; quality of hire at 6 months (retention, manager rating, in aggregate); candidate complaints and review requests.

## Phase 4: decide on scale (month 6-7)

Scale only the role families where the pilot beat the baseline on time saved with no adverse impact and equal or better quality of hire. Re-confirm consent or agreement from each works council for the final setup. Keep human confirmation of rejections as the standing rule; a different design (for example, fully automatic decisions) would need its own legal review and representatives' agreement, and I would not recommend it.

## Ongoing after go-live

- Quarterly adverse-impact review by group, owner named (Head of Talent Acquisition), with the DPO and works council receiving the results.
- Re-test after every vendor model update or change in job requirements.
- Keep logs for the period required by the AI Act and retention rules; delete rejected-candidate data on schedule.
- Annual review of whether the tool is still worth it.

## Cheaper options to run alongside or before

- Structured first-round questions and structured interviews (among the best predictors of job performance in Sackett et al., 2022), scored against criteria agreed beforehand.
- Knockout questions only for legal or practical must-haves.
- Scheduling and status-update automation, which cuts waiting time without judging anyone.
- Recruiter summaries: AI summarises an application for a recruiter who reads it.

## Roles

| Who | What |
|---|---|
| Head of Talent Acquisition | Owner; baseline, pilot, monitoring |
| CHRO | Sponsor; works council relationship, stop decisions |
| DPO and Legal | DPIA, candidate notice, vendor contract, country counsel |
| Works councils (NL, DE, BE as applicable) | Consent, design input, monthly results |
| Vendor | Documentation, bias audit, logs, support for our tests |
| Recruiters | Review, overrule, feedback on false rejections |
| Finance | Cost of tool versus recruiter hours, agency spend, vacancy cost |

## Open questions that would change this plan

1. Which entities have works councils or union delegations in each country?
2. What are the real monthly hires and the share of CVs that currently reach interview?
3. What does the vendor contract allow us to test and audit, and where is the data processed?
4. Is the real constraint recruiter hours, candidate response time, or agency cost?

## Key assumptions

- The vendor's documentation does not include emotion recognition or sensitive-trait inference.
- Recruiter time per CV and the current reject rate are estimates until the ATS data is pulled.
- AI Act deployer duties start on 2 December 2027 as currently scheduled; check for changes.
