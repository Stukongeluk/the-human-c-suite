# AI CV screening: staged rollout plan (NL, BE, DE)

Status: draft for the CHRO, DPO, legal counsel and the employee representative bodies. Not legal advice; every legal point below needs confirmation by employment and data protection counsel in each country. Figures marked "estimate" are assumptions to replace with our own data.

## 1. Decision requested

Approve a staged rollout in which the AI module **scores and sorts, and a recruiter decides on every rejection that rests on a score**. Do not approve scoring-based automatic rejection of a fixed bottom 70%. The reasons are in section 2; the conditions under which this could be revisited are in section 7.

## 2. Why not switch it on as proposed

- **It is a fully automated decision about people.** GDPR Article 22 restricts decisions based solely on automated processing that significantly affect a person; the regulation's own recital names e-recruiting without human intervention as the example. The Court of Justice (SCHUFA, C-634/21, December 2023) treated a score that a third party relies on heavily as such a decision. Infringing Article 22 sits in the higher fine tier (up to EUR 20 million or 4% of worldwide turnover). Counsel must confirm how this applies to us.
- **We are the controller, not the vendor.** "GDPR-compliant" describes a product at best. Lawful basis, the data protection impact assessment (Article 35), candidate information, retention of rejected applicants' data and the human review are our duties, and they stay with us whatever the contract says.
- **"Bias-free" is not a claim any model can meet.** CV models learn from past hiring and past CVs, and can penalise career gaps, part-time work, foreign education, language, or proxies for gender, age and origin. A widely reported example is the recruiting tool Amazon abandoned in 2018 after it downgraded women's CVs. We need our own evidence on our own applicants, in Dutch, French, German and English.
- **AI used for recruitment is classed as high-risk under the EU AI Act (Annex III).** The employer's duty to inform workers' representatives and affected workers before use (Article 26(7)) currently applies from 2 December 2027 after the Digital Omnibus changes; confirm the date. National works council rules already apply today.
- **Works council rights come first.** In the Netherlands, systems suited to monitoring or assessing people fall under the works council's consent right (article 27(1)(l) WOR). In Germany, where a works council exists, §87(1) no. 6 BetrVG gives co-determination on technical systems suited to monitoring behaviour or performance, and the General Equal Treatment Act (AGG) protects applicants. In Belgium, check the works council or union delegation position and the collective agreement on recruitment and selection (CAO 38). Whether each country has a works council, and at what level, is an open question.
- **The 70% is a quota, not a quality bar.** Rejecting the bottom 70% means 2,800 of 4,000 monthly applicants (33,600 a year) are rejected whether or not they could do the job. In a strong month, good candidates fall below the line.
- **The saving looks small.** At 2 to 5 minutes per CV (estimate), screening 4,000 applications is 133 to 333 recruiter hours a month, roughly 0.9 to 2.1 full-time equivalents at 36 hours a week. The risk is a legal, reputational and hiring-quality cost on 48,000 applications a year.

## 3. What problem are we solving?

Before any rollout, agree and baseline what "better" means. Candidates: time to first response, time to hire for store and warehouse roles, recruiter hours per hire, candidate drop-out, 90-day retention of new hires, recruiter workload and burnout. Pull these per country and job family from the ATS and HR systems, dated, before the pilot starts. If the main pain is speed of response, a short structured application with job-related knock-out questions and automatic acknowledgements may solve most of it without scoring anyone.

## 4. Options compared

| | A. As proposed: score and auto-reject bottom 70% | B. Recommended: staged, AI assists, recruiter decides | C. No AI; fix the front of the funnel |
|---|---|---|---|
| Recruiter time saved | Highest (estimate: up to ~1-2 FTE of screening) | Partial: ranking and summaries cut reading time; some review remains | Small to moderate (structured forms, knock-outs) |
| Candidates affected | 2,800 a month rejected with no human look | Every rejection has a human decision behind it | Unchanged, with faster replies |
| Legal exposure | Highest: Article 22, works council consent, equal treatment claims | Lower: human decision, DPIA, consultation done first | Lowest |
| Bias risk | Unmeasured and invisible once rejected | Measured in shadow mode and monitored monthly | Not applicable |
| Reversibility | Hard: rejected people are gone, trust lost | High: can stop at any gate | Fully reversible |
| Time to first benefit | Fast on paper | About 5 to 6 months | 1 to 2 months |

B and C can run together: C starts in the first weeks and does not depend on the module.

## 5. Phased plan

Dates are indicative from December 2026. A phase starts only when the previous gate is met.

**Phase 0: Foundations (about 6 weeks)**
- Name one accountable owner (CHRO) and one data protection owner (DPO). Start the DPIA.
- Open the conversation with works councils and employee representatives in NL, BE and DE at the problem stage, with the vendor documentation and the baseline numbers, before configuration choices are made. Ask them to nominate members of the design group. Treat their objections as free risk analysis.
- Vendor due diligence, in writing: what data trains the model, whether our candidates' data is used to train it, which features are scored, validation results on European applicants, adverse-impact testing method and results, sub-processors and data location, retention and deletion, audit rights, explanation per candidate, and the contract clause that the vendor supports our audits and gives notice of model changes.
- Choose the job-relevant criteria per job family with hiring managers and recruiters. Remove features that proxy for protected traits (names, photos, age, postcode where it proxies origin, gaps taken as negative).
- Confirm with counsel: lawful basis, Article 22 position, retention period for rejected applications, how internal applicants are handled, and per-country notice requirements.
- Write the candidate notice: that an AI tool assists, what it looks at, that a person decides, how to ask for human review and how to object. Offer a clear route for candidates who need an adjustment (disability, language).

**Phase 1: Shadow mode (about 3 months)**
- The module scores every CV; nothing it produces reaches a decision. Recruiters work as today.
- Compare scores to recruiter shortlists and, later, to 90-day outcomes. Measure agreement, and above all who the tool would have rejected that recruiters advanced.
- Test selection rates by gender, age band, country, language of CV, part-time or gap history, and education origin. Ethnicity is special-category data and cannot simply be collected: agree with counsel and the DPO how to test (voluntary, separately held survey data, or controlled test sets with the vendor).
- Gate to Phase 2: results shared with the design group and the representatives; no group is selected at less than four-fifths of the highest group's rate without an explanation we can defend (a screening trigger, not a legal test); the share of good candidates the tool would have missed is acceptable to recruiters and representatives.

**Phase 2: Assist mode in one country and one job family (about 3 months)**
- Recruiters see the AI ranking and a plain-language reason for each score, plus all applicants. Nobody is rejected because of a score alone; a recruiter makes or confirms every rejection.
- Each month, recruiters blind-review a random sample (for example 200) of the lowest-scored applicants and record how many they would have advanced. This is the check on whether the score deserves trust.
- Candidates can ask for human review of any rejection and can object. Track requests and outcomes.
- Gate to Phase 3: stable audit results for three consecutive months, no unresolved complaint pattern, representatives' agreement documented.

**Phase 3: Extend, country by country (from about month 9)**
- Extend to other job families and countries only after consultation in that country is complete and counsel has signed off.
- The only automatic rejections considered are on objective, disclosed, job-related knock-outs (for example no right to work, missing mandatory licence, not available for the required shifts), with a regular human audit of a sample. Score-based automatic rejection is not part of this plan.

## 6. Roles and people

- **Recruiters:** no headcount reduction is planned or assumed in the business case. Freed time goes to candidate contact, hiring-manager coaching, store-level hiring support and the review work above. Involve them in the design from Phase 0; they know the edge cases.
- **Hiring managers:** short briefing on what the score means and does not mean, and on not treating it as a verdict.
- **Candidates:** told in plain language before they apply; can see what data we hold and can reach a person.
- **Leadership:** if the rollout produces a bad outcome (a biased pattern, wrongly rejected candidates), the accountability sits with the CHRO and the executive team, not with the vendor or the recruiter who clicked.

## 7. Conditions for ever using score-based automatic rejection

All of the following, in writing, per country: a completed DPIA; counsel's confirmation on Article 22 and national law; works council agreement where required; at least 12 months of audit data showing no unexplained adverse impact; a human-review and appeal route that works in practice; a rejection threshold set on validated job-related quality, not a fixed percentage; and a named executive who owns the outcome.

## 8. Indicators (reviewed monthly by the design group)

| Money and speed | People and fairness |
|---|---|
| Time to first response; time to hire, by job family | Selection rates by group (gender, age band, language, gap/part-time, country) |
| Recruiter hours per hire | Share of lowest-scored applicants that blind review would advance |
| Cost per hire; vendor cost | Human-review requests, objections, complaints and outcomes |
| Candidate drop-out rate | Candidate satisfaction; recruiter workload and satisfaction |
| 90-day retention of new hires | Retention and performance of hires the tool ranked low versus high |

## 9. Stop rules

Pause the module and return to the previous phase if: a monitored group's selection rate falls below the agreed trigger without a defensible explanation; blind review shows the tool misses a material share of good candidates; the vendor changes the model without notice; a regulator, works council or court raises a concern; or complaint volume rises. Stopping is a normal outcome of the process, not a failure.

## 10. Open questions we need answered

1. Which of our entities have works councils or union representation in NL, BE and DE, and have any been told yet?
2. What is the baseline: time to hire, recruiter hours per application, hires per month by job family?
3. What does the vendor's contract and documentation say about training on our data, validation, audit rights and liability?
4. Do internal applicants and returning former employees go through the same module?

What are we missing, and what would make this plan wrong?
