# AI CV screening rollout plan (NL / BE / DE)

## Bottom line

I can't give you a rollout plan for "score every CV and auto-reject the bottom 70% with no recruiter looking". That design is the one I'd stop. It is probably unlawful in all three countries, and the vendor's "bias-free and GDPR-compliant" claim doesn't change that. You are the controller and the deployer, so the liability is yours, not the vendor's.

I'd build the same module as a **ranking and triage tool with a human making every rejection decision**, switched on in phases with go/no-go gates. It still removes most of the manual reading. The plan is below.

Confidence tags: [verified] means well-established law or arithmetic. [medium] means I'm confident of the direction but the detail needs counsel. [assumed] means I'm inferring from what you told me.

## Why the current design doesn't work

1. **GDPR Art. 22 (solely automated decisions). [verified]** Rejecting an applicant with no human involvement is a decision with significant effects on that person. The CJEU read "decision" broadly in the SCHUFA case (C-634/21, Dec 2023). Even a score that a human merely rubber-stamps can count. Art. 22 allows this only with explicit consent, contractual necessity or a legal basis. With 4,000 applicants a month, consent is not freely given and "necessity" is hard to argue when a recruiter could read the CV. Candidates also get rights to be informed, to obtain human intervention and to contest the decision.

2. **EU AI Act. [verified on classification, medium on dates]** AI used to filter or evaluate job applicants is listed as high-risk (Annex III). That brings obligations for you as deployer: effective human oversight by trained people, logging, input-data controls, informing candidates and informing worker representatives. The headline application date was August 2026. There have been proposals to delay parts of it, so have counsel confirm the current date. Either way, build to the high-risk standard now. The AI-literacy duty is already in force.

3. **"Bias-free" is not a credible claim. [verified]** CV-scoring models learn from historic hiring data. They routinely pick up proxies for gender, age, ethnicity, disability and career breaks, such as postcode, name, gaps, part-time history and university. No honest vendor can promise zero bias. Ask for the evidence instead: validation studies, adverse-impact results by group, the training data description, and a contractual commitment to support audits. "GDPR-compliant" is also a statement about the vendor's own processing, not about your use of the tool.

4. **Worker-representative rights. [medium, confirm locally]**
   - **Netherlands:** a works council (OR) normally has a right of consent (instemmingsrecht) under the WOR over selection and assessment systems and over systems processing personnel data. Candidate data is likely in scope.
   - **Germany:** the Betriebsrat has co-determination rights on selection guidelines and on technical systems that monitor behaviour or performance (BetrVG). The AGG also eases the burden of proof for rejected candidates who can show indications of discrimination, which an opaque score makes hard to rebut.
   - **Belgium:** the recruitment rules and CAO 38 on non-discrimination, plus information and consultation duties to the works council or union delegation.
   - If you skip these steps, the works councils can block or unwind the rollout after you've launched it.

5. **Scale of the exposure. [verified arithmetic]** 4,000 a month × 70% is about 2,800 automated rejections a month, roughly 33,600 a year, with nobody accountable for any single one. Even a small adverse-impact skew shows up as a pattern in discrimination claims and regulator complaints. In retail and e-commerce many applicants are also customers, so a rejection can become a brand issue.

6. **The 70% cut is arbitrary. [assumed]** I don't know your vacancy count or hires per month. A cut-off should come from capacity and from validated score distributions, not from a fixed percentage. A fixed bottom-70% also rejects people in a slow month who would be shortlisted in a busy one.

## What I recommend instead

**Target design:** the model scores and ranks. Recruiters decide. The model can auto-reject only on objective, documented knock-out criteria that a human set and can explain, such as no right to work in the country, or a missing mandatory licence or certification. Everything else is "recommend" and never "decide".

### Phased rollout

| Phase | Timing | What happens | Gate to move on |
|---|---|---|---|
| 0. Foundations | Weeks 0-6 | See the checklist below. No candidate data goes through the module in production. | DPIA signed off. Works councils consulted or consented. Vendor evidence received. |
| 1. Shadow mode | Weeks 6-12 | The model scores every CV in the background. Recruiters work as today and can't see the score. Compare model vs recruiter shortlists. | Agreement with recruiters is acceptable. Adverse-impact ratios are within threshold for gender, age band, nationality or ethnicity proxy, and country. |
| 2. Assisted triage, one country and 2-3 job families | Weeks 12-20 | Recruiters see the score as a sorting aid. Every rejection is a recruiter action, with a one-click bulk reject for the low-ranked band. A sample of low-scored CVs is read in full. | Time saved is real. Quality-of-hire proxies don't drop. The sampled low-scored CVs don't contain good candidates at a rate above your tolerance. |
| 3. Scale-out | Weeks 20-36 | Extend to remaining job families and countries, sequenced by works council readiness. | Same gates, per country. |
| 4. Steady state | Ongoing | Quarterly bias audit, annual DPIA review, drift monitoring, periodic re-validation. | Standing governance, owned by HR with Legal and the DPO. |

Auto-reject on knock-out criteria only can start in Phase 2 for the narrow objective rules. Expanding it beyond that needs a fresh legal and DPIA review.

### Phase 0 checklist

- **DPIA (GDPR Art. 35)** before any processing. Owner: DPO with HR.
- **Legal basis and Art. 22 position** documented per country, with counsel.
- **Works council, Betriebsrat and Belgian bodies:** share the vendor documentation and the purpose, and agree the oversight design. This is a legal step and also the cheapest way to avoid a later block.
- **Vendor due diligence and contract:**
  - description of features used and training data
  - validation and adverse-impact test results
  - the ability to switch features off (for example photo, name, age, address)
  - audit rights, data processing agreement, sub-processors, data location, retention and deletion
  - explainability: a reason for every score that a recruiter can read and a candidate can be told
  - indemnity for discrimination or AI Act failures, as far as you can negotiate it
- **Feature minimisation:** strip name, photo, date of birth, gender, address and nationality from what the model sees. Check for proxies.
- **Candidate transparency:** privacy notice and application-page text that say AI assists screening, how, and how to ask for human review. Set up the process and an SLA for those requests.
- **Human oversight:** name the reviewers, train them on automation bias, and give them the authority and the time to overrule the score. If reviewers approve 99% of recommendations in 3 seconds each, that is rubber-stamping and won't count as oversight.
- **Retention:** define how long rejected candidates' data and scores are kept per country, and how deletion works.
- **Baseline metrics** captured before go-live, so you can show the tool helped.

### Metrics to track from Phase 1

| Metric | Target or trigger |
|---|---|
| Adverse-impact ratio per protected-group proxy and per country | Investigate below 0.8 (the four-fifths rule of thumb). Pause the feature if the cause isn't understood. |
| Recruiter override rate | Too low suggests rubber-stamping. Too high suggests a poor model. |
| False-negative audit (sample of low-scored CVs read by humans) | Set the tolerance in Phase 0, for example under 5% shortlistable. |
| Time to shortlist and time to fill | Better than baseline. The skill's reference target for IC roles is under 45 days. |
| Offer acceptance and 90-day turnover | No deterioration. Reference targets above 85% and below 5%. |
| Candidate experience (NPS or complaint count) and Art. 22 / human-review requests | Monitor for trends and answer within the SLA. |
| Time lost to rework or appeals | Should fall, not rise. |

### Governance

- **Accountable owner:** CHRO.
- **Required partners:** DPO, Legal in each country, works councils, CFO for the business case, and IT security for the ATS integration.
- **Kill switch:** a named person can switch the scoring off the same day if a gate metric fails.
- **Reporting:** a quarterly people-and-risk line to the executive team and board.

## What this costs you versus the original plan

- **Time:** the original plan sounds like weeks. This one is about 6 months to full scale, but Phase 2 already delivers most of the recruiter time saving, from around month 3-5.
- **Savings:** you won't save the full "no recruiter looks" amount. Bulk-rejecting a low-ranked band that a recruiter has glanced at and sampled still cuts the reading time sharply. I don't have your recruiter headcount or cost per screen, so I can't give a reliable euro figure. If you share them I can model it with the CFO view.
- **Risk:** you avoid the largest legal exposure and the likelihood of a works council stopping the project mid-flight.

## Things I'm assuming or can't see [assumed]

- The vendor, the product's actual feature set and its test evidence. I haven't seen any of it.
- Your current works council setup in each country, and whether a group-level body exists.
- Hiring volumes per job family, seasonal peaks (retail has big ones) and recruiter capacity.
- Whether the 70% figure was a vendor default or a deliberate target.

This is people-strategy advice, not legal advice. Have employment and data-protection counsel in each of the three countries confirm the points marked [medium], especially the AI Act dates and the works council rights, before you commit.

## Your decision

1. **Approve the phased design** (human decides every rejection, narrow knock-out auto-rejects only) and start Phase 0 now.
2. **Or tell me why full auto-reject is non-negotiable.** I'd then need Legal and the DPO to give a written position on Art. 22 per country before anything else. I'd expect them to say no.

Three things I need from you this week: the vendor's validation and adverse-impact documentation, the name of your DPO and legal contact in each country, and the current monthly hires and open vacancies by job family. With those I can turn Phase 0 into a dated project plan.
