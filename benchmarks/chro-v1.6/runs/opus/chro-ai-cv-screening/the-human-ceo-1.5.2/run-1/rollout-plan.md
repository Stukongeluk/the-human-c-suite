# Rollout plan: AI-assisted CV screening in the Netherlands, Belgium and Germany

**Prepared:** 23 November 2026 · **Decision owner:** [CHRO, on behalf of the executive team] · **Decision needed by:** [date] · **For:** executive team, talent acquisition, legal and privacy, works councils in NL, BE and DE

*Draft for discussion. Legal points were checked against public sources in November 2026. This is not legal advice: employment and privacy counsel in each country must confirm them before the pilot.*

## 1. The decision in brief

We will introduce the AI screening module in our applicant tracking system (ATS) as a ranking and explanation aid. It will not reject anyone on its own. It scores each CV and gives its reasons, and a trained recruiter makes every rejection decision. We go live in phases: a shadow test on our own applicants first, then a pilot, then waves by country. We start only after works council involvement in each country. We will **not** switch on automatic rejection of the lowest-scoring 70%.

The numbers behind this:

- At 4,000 applications a month, automatic rejection of the bottom 70% would mean **2,800 rejections a month, 33,600 a year,** with no person involved.
- Having a recruiter confirm each proposed rejection costs an estimated **0.4–0.75 FTE, about €21–52k a year,** more than full automation (section 12).
- What a CV mostly shows is a weak predictor of job performance. In the most recent large meta-analysis, years of job experience scored a validity of 0.07, against 0.42 for structured interviews and 0.33 for work samples [11].

**Accountability:** the CHRO owns the outcomes of this system for the executive team. If it treats applicants unfairly, leadership answers for it, not the recruiter who confirmed a suggestion.

## 2. The problem we are solving

We receive about 4,000 applications a month, about 190 per working day. The working assumption, to be confirmed by the executive team in phase 0, is that we want to:

1. reply to candidates faster
2. spend less recruiter time on screening
3. keep or improve the quality of our hires
4. treat every applicant fairly and lawfully in three countries.

Facts to collect in phase 0 (team-level and aggregated, never per recruiter):

| Fact | Source | Why it matters |
|---|---|---|
| Applications per month by country, job family and CV language | ATS reports | Where the volume is; which languages the model must handle (NL, FR, DE, EN) |
| Time from application to first response, and to hire | ATS reports | Whether speed is the real problem |
| Recruiter hours on screening vs scheduling, chasing hiring managers and admin | Two-week team time study | Where AI saves the most time |
| Conversion from applied to screened, interviewed and hired | ATS reports | Baseline for the shadow test |
| 90-day retention and probation outcomes of hires | HRIS | Quality of hire |
| Recruiter FTE and loaded cost | HRIS, payroll | Replaces the estimates in section 12 |
| Works councils per country and site; existing agreements on the ATS and HR systems | Legal, HR | Consultation route |
| Vendor documentation, data processing agreement, sub-processors | Vendor | Due diligence (section 8) |

## 3. Options considered

| Option | Recruiter time saved (est.) | Time to effect | Who is affected, and how | Hidden costs | Reversible? | Main risks |
|---|---|---|---|---|---|---|
| A. Do nothing | none | none | Recruiters stay overloaded; candidates wait | Slow hiring, lost candidates, store understaffing | Yes | Status quo keeps getting worse as volume grows |
| B. Auto-reject the bottom 70% (as proposed) | 0.75–1.5 FTE | Weeks technically, but needs works council consent in NL and DE first | 33,600 applicants a year rejected without a person; older applicants, people with career gaps and non-native speakers are most at risk | DPIA and legal work anyway; claims handling; rebuild for the AI Act by Dec 2027 | You can switch it off, but you can't undo the rejections | GDPR art. 22, AGG claims in Germany, works council veto, bias nobody sees, brand damage with applicants who are also customers |
| **C. AI ranks and explains, a recruiter confirms every rejection** | 0.4–0.75 FTE | 4–7 months, phased | Applicants get a human decision and a review route; recruiters move from reading every CV to checking and overriding suggestions | Recruiter training; monitoring; vendor audit | Yes | Rubber-stamping if the design and workload invite it (section 4) |
| **D. Redesign the funnel for store, warehouse and service roles:** short application without a CV, objective knock-out questions, a fast structured phone screen | Probably the largest; measure in phase 0 | 1–3 months | Applicants with thin or non-standard CVs get a fairer chance; store managers get structured interview guides | ATS configuration; interview guides | Yes | Knock-outs that aren't truly job-required |
| **E. AI for admin first:** interview scheduling, reminders, status updates, candidate FAQs | Measure in phase 0 | Weeks | Candidates get faster replies; nobody is scored | Configuration; telling candidates they're talking to an AI assistant | Yes | Low |

**The view from each seat**

- **Customers and brand:** many applicants for store roles are customers too, and a rejection that is fast, explained and fair protects the brand.
- **Finance:** the difference between B and C is tens of thousands of euros a year. B carries GDPR fines of up to €20m or 4% of worldwide turnover [1] and claims per rejected applicant in Germany [9]. These are maximum figures, not expected ones.
- **Operations:** store managers care about good candidates arriving quickly. C, D and E address that directly.
- **Technology:** C needs version control, logging, data export and masking from the vendor (section 8).
- **People:** recruiters keep the judgement and lose the drudgery. Applicants keep a human decision.

**Recommendation: C, combined with D and E.** Start E and the knock-out part of D now. Run C through the phases in section 6.

## 4. How the module will be used: design rules

1. **The score suggests; a recruiter decides.** Recruiters can't bulk-reject candidates below a score threshold. Each proposed rejection is opened together with the CV and the AI's reasons.
2. **Overriding is as easy as confirming.** Recruiters have the time, training and authority to disagree with the score. If overriding takes more effort than agreeing, people will defer to the machine. Regulators say human oversight must be meaningful, "rather than just a token gesture" [2].
3. **No individual speed targets.** Recruiters are not measured individually on how fast or how many suggestions they confirm. Performance indicators are team-level only.
4. **Masked inputs.** Before scoring, the model is not shown names, photos, dates of birth or age, gender, nationality, address or postcode, marital status or graduation years. It must not infer protected characteristics. German CVs often still include a photo and a date of birth, so masking must work for them too.
5. **No video, voice or emotion analysis** of candidates in this rollout.
6. **Knock-out questions only for objective, job-required criteria stated in the job ad,** such as the right to work, availability, a required licence or a legal minimum age. Candidates answer them themselves. A recruiter checks the resulting declines every day, and the candidate is told which requirement was not met.
7. **Candidates are told up front,** in Dutch, French, German and English, in the job ad and on the application form: AI helps rank applications, a person decides, which data is used, and how to ask for a human review and an explanation.
8. **Human review on request,** by a recruiter who did not make the original decision, within [5] working days. The explanation sets out the procedure and the principles actually applied [4].
9. **Logs and audit.** Scores, reasons, decisions and overrides are logged and exportable for our own audits, within the national retention limits. Keep them long enough to defend a claim: in Germany, AGG claims must be made within two months of the rejection [9].
10. **Change control.** No change to the model version, job-family criteria or configuration goes live without a repeat bias test.
11. **Purpose limit.** The score is used only for this recruitment step. It is not used for internal mobility, performance or anything else without a new assessment and new consultation.

## 5. The legal floor (checked November 2026)

| Rule | What it means for us | Applies |
|---|---|---|
| GDPR art. 22 and recital 71 [1] | People have the right not to be subject to a decision based solely on automated processing with significant effects. Recital 71 names "e-recruiting practices without any human intervention" as an example. The exceptions (necessity for a contract, authorisation by law, explicit consent) are narrow. For necessity, regulators require that no less intrusive means would work; their own example is one vacancy with tens of thousands of applications [2]. Even then, safeguards are required: human intervention, the right to give one's view and the right to contest | Now, all three countries |
| CJEU C-634/21 *SCHUFA* (7 Dec 2023) [3] | A score that significantly shapes a decision can itself be an automated decision. Letting recruiters see only the top 30% doesn't make the rejection of the other 70% a human one | Now |
| GDPR arts. 13–15; CJEU C-203/22 *Dun & Bradstreet Austria* (27 Feb 2025) [4] | Tell applicants about automated processing and its logic. On request, explain the procedure and principles actually applied; handing over the algorithm is not enough | Now |
| GDPR art. 35 | Data protection impact assessment before processing starts, including the shadow test | Before phase 1 |
| AI Act, Annex III point 4 (recruitment and filtering of applications), arts. 26 and 86 [5][6] | High-risk system. As deployer we must: use it according to the instructions; assign trained human oversight with authority; keep input data relevant; monitor it; keep logs for at least six months; inform workers' representatives and staff before use; inform candidates; give individual explanations | From 2 Dec 2027, after the Digital Omnibus (Regulation (EU) 2026/1744, in force 27 July 2026) [5] |
| AI Act art. 4 | Measures to support the AI literacy of staff who use AI (softened by the Omnibus) [5] | Now |
| NL: WOR art. 27(1)(e) [7] | Works council consent for rules on hiring policy, including recruitment and selection | Now |
| NL: Equal Treatment Act (AWGB) | Covers recruitment and selection | Now |
| DE: BetrVG §95(1) and (2a) [8] | Works council consent for selection guidelines, explicitly also when AI is used to draw them up. Without agreement, the conciliation board decides | Now |
| DE: BetrVG §87(1) no. 6 | Co-determination on technical systems suited to monitoring employees, here the recruiters who use the ATS | Now |
| DE: BetrVG §90 and §80(3) | Early information on planned AI use; the works council may bring in an expert | Now |
| DE: AGG §§15 and 22 [9] | A rejected applicant who would not have been hired anyway can get compensation of up to three months' salary. Claims must be made within two months. Indications of discrimination shift the burden of proof to the employer | Now |
| BE: CAO/CCT 9 and 39 [10] | Inform the works council about changes to personnel policy, such as AI in recruitment; inform and consult on new technology with significant collective consequences | Now |
| BE: CAO/CCT 38 [12] | Recruitment code: questions must relate to the job, applicant data stays confidential, applicants who met the requirements but were not selected are told in writing within a reasonable time, practical tests are time-limited. Largely guidance rather than enforceable rules | Now |

Open legal questions for counsel: which German body is competent for a group-wide system (local works councils or the central works council); whether Belgian sector agreements add requirements; and national retention periods for applicant data.

## 6. Rollout phases and gates

| Phase | When | What happens | Who is involved | Gate to the next phase |
|---|---|---|---|---|
| 0. Prepare | Weeks 1–8 (allow for the holiday period) | Confirm the goal and collect the baseline (section 2); vendor due diligence (section 8); DPIA; candidate texts in four languages; recruiter training; start E and the knock-out questions from D; works councils informed at the problem stage, with the real numbers, while the design can still change | CHRO (owner), TA lead, DPO, legal, works councils, 2–3 recruiters per country in a design group | DPIA signed off; vendor answers acceptable; NL consent request and BE information done; DE negotiation started; privacy notice updated |
| 1. Shadow test | Weeks 9–16, in the countries where phase 0 is complete | The AI scores applications in the background. Recruiters work as usual and don't see the scores. We compare the AI's proposed rejections with what recruiters actually did (section 7) | TA analytics, DPO, vendor, a works council observer | Selection-rate ratio of 0.8 or higher for every monitored group. False rejections below the threshold agreed in phase 0 (suggested starting point: fewer than 1 in 20 of the candidates recruiters advanced, and fewer than 1 in 50 of those hired). Reasons are job-relevant in a sample of 100. Results shared with the works councils |
| 2. Pilot | Months 5–7 | One country and one job family, such as customer service in NL, in assist mode under the design rules (section 4). Human review on request is live | Pilot recruiters, hiring managers, DPO | Time to first response better than baseline; override rate between 2% and 20%, or explained; selection-rate ratios hold; review requests handled on time; team pulse among recruiters not worse; no unresolved works council objection |
| 3. Expand in waves | Months 8–12 | Country by country and job family by job family. Germany only after a works agreement (Betriebsvereinbarung) is signed. Each wave is stable before the next one starts | TA, country HR, works councils | The same gates as the pilot, per wave |
| 4. Run and audit | From month 12 | Monthly dashboard; quarterly bias review shared with the works councils; yearly independent audit; AI Act readiness check in September 2027 (during phase 3), ahead of 2 December 2027 | CHRO, DPO, internal audit | Ongoing, under the stop rules in section 11 |

## 7. Testing for bias and quality on our own applicants

1. **Run it live rather than on old CVs.** We probably no longer lawfully hold most rejected applicants' CVs, so the shadow test uses current applications under the updated privacy notice and DPIA.
2. **Measure false rejections.** What share of the candidates recruiters advanced, and of the people we hired, would the AI have put in its bottom 70%?
3. **Compare selection rates by group** at the AI step: gender, age band, CV language (NL, FR, DE, EN, other), country, career gaps of more than 12 months, and student or part-time applicants. Compute each group's pass rate divided by the pass rate of the best-treated group. A ratio below 0.8, the "four-fifths" rule of thumb from the US Uniform Guidelines, is a tripwire for investigation, not a legal safe harbour.
4. **Handle ethnicity with care.** We don't hold data on ethnic origin, and inferring it from names is processing special-category data. Test it only through the vendor or an independent auditor, on a legal basis counsel has confirmed. The Omnibus extended the legal basis for bias detection, but its scope for deployers needs checking [13].
5. **Review the disagreements.** A small panel (a recruiter, a hiring manager and an observer from the works council) blind-reviews a sample of cases where the AI and the recruiter disagree, to learn which of them was right.
6. **Publish the method and results** to the works councils before the pilot decision.

Why this matters: in a 2024 University of Washington study, three language models ranked over 550 real CVs against 500+ job listings. They preferred white-associated names 85% of the time and Black-associated names 9%, and male-associated names 52% against 11% for female-associated names [14]. Amazon dropped its own CV-scoring tool in 2018 after it learned to penalise CVs containing the word "women's" [15]. In the US, the EEOC settled a case in 2023 against a company whose software automatically rejected women aged 55 and over and men aged 60 and over, more than 200 qualified applicants [16]. And in May 2025 a US court let a nationwide age-discrimination collective action over Workday's screening tools proceed [17].

## 8. Vendor due diligence: get answers in writing before activation

1. **Bias evidence:** adverse-impact results on European, multilingual data. Ask for the method, the groups tested, the selection-rate ratios, the date, and whether the test was independent.
2. **What the model predicts:** similarity to the job description, or resemblance to past hires? A model trained on past hiring decisions reproduces past bias.
3. **Inputs:** which CV fields it uses, whether names, photos, dates of birth and postcodes are masked before scoring, and whether it infers any protected characteristic.
4. **Explanations:** per-candidate reasons in plain language that we can give to a candidate on request [4].
5. **Data:** the data processing agreement (GDPR art. 28), sub-processors, where the data is processed and any transfers outside the EU, retention and deletion. No use of our applicants' data to train the vendor's general models.
6. **AI Act:** the vendor's plan for conformity assessment, CE marking, registration and instructions for use by 2 December 2027, and what happens to our contract if they miss it.
7. **Logs and export:** scores, reasons and decisions can be exported for our own audits.
8. **Model changes:** announced in advance with new test results, and an option to pin a version.
9. **Contract:** audit rights, cooperation with regulators and works councils, the right to suspend, and liability for discriminatory outcomes.
10. **References:** EU customers with works councils, especially in Germany, and any complaints, regulator inquiries or litigation involving the product.

## 9. People

- **Recruiters:** they hear first, from their own manager, before anyone else: nobody in recruitment loses their job because of this module. Their role shifts from reading every CV to judging suggestions, running structured interviews, supporting hiring managers and looking after candidates. They get paid training time on AI literacy, automation bias, overriding and handling review requests. Two or three recruiters per country sit in the design group.
- **Hiring and store managers:** structured interview guides for frontline roles, and a briefing before the pilot reaches their job family.
- **Applicants:** a human decision, a reason, a review route and faster replies. Store roles get an application route that doesn't depend on a polished CV.
- **Works councils:** involved at the problem stage with the real numbers, shown the shadow-test results before the pilot decision, and given a quarterly report after that. Their objections are treated as free risk analysis.

## 10. Human impact assessment

| Question | Answer |
|---|---|
| Who is affected? | About 4,000 applicants a month across NL, BE and DE; recruiters [number to confirm]; hiring and store managers |
| What changes for them? | Applicants: how they are assessed and informed. Recruiters: checking and overriding suggestions instead of reading every CV. Managers: how candidate shortlists are built |
| Who is affected disproportionately? | Older applicants; women and carers with career gaps; people with disabilities and non-standard CVs; non-native speakers and CVs in French, German or other languages; people with non-Western names; students and first-time job seekers with thin CVs; career changers |
| What do they lose that is hard to replace? | A fair chance at a job. Trust in a brand many of them also buy from |
| What do we offer? | A human decision, an explanation, review on request, a no-CV route for store roles |
| What do the recruiters experience? | A change in workload, and pressure to rubber-stamp if capacity isn't planned. Mitigated by capacity planning (section 12), training and no individual speed targets |
| What happens to service quality? | Better if hiring speeds up and good candidates aren't lost; worse if false rejections leave stores short-staffed. Measured through 90-day retention and time to hire |
| Which legal and consultation steps apply? | Section 5 |
| How will we know it is going badly? | The stop rules in section 11 |

## 11. Measures, review rhythm and stop rules

| Indicator | Baseline | Target or tripwire | Rhythm |
|---|---|---|---|
| Time from application to first response | Phase 0 | Target set in phase 0 | Monthly |
| Time to hire | Phase 0 | Target set in phase 0 | Monthly |
| Team recruiter hours on screening | Phase 0 | Down by about 0.4–0.75 FTE (estimate) | Quarterly |
| Selection-rate ratio by group, at the AI step and at each later stage | Shadow test | 0.8 or higher | Monthly in the pilot, then quarterly |
| Override rate on proposed rejections | Pilot | Investigate below 2% or above 20% | Monthly |
| Human review requests, and how many were overturned | Pilot | Handled within [5] working days | Monthly |
| Candidate experience score | Phase 0 | Not worse than baseline | Quarterly |
| Hiring managers' satisfaction with shortlists | Phase 0 | Not worse than baseline | Quarterly |
| 90-day retention of hires | Phase 0 | Not worse than baseline | Quarterly |
| Recruiter workload and pulse (team level) | Phase 0 | Not worse than baseline | Quarterly |

**Stop rules:**
- A group's selection-rate ratio falls below 0.8 in a job family with enough volume: pause the score for that job family and investigate with the vendor.
- A works council, data protection authority or equality body raises a formal concern: pause in that country until it is resolved.
- A model change went live without notice or re-testing: revert to the previous version or pause.
- The override rate stays below 2% for two months: audit a sample for rubber-stamping.
- Time to first response is no better than baseline after the pilot: revisit the business case before expanding.

## 12. Time and cost estimate

Assumptions (estimates, to replace with phase-0 data):
- screening takes 2–4 minutes per CV today
- confirming a proposed rejection, with the AI's reasons shown, takes about half that: 1–2 minutes
- one FTE gives 125 productive hours a month and costs €55–70k a year all-in.

The low end of each range combines the lower time with €55k, and the high end the higher time with €70k.

| For the ~2,800 lower-ranked CVs a month | Today (manual) | B. Auto-reject | C. Assist (recommended) |
|---|---|---|---|
| Recruiter hours per month | 93–187 | 0 | 47–93 |
| FTE equivalent | 0.75–1.5 | 0 | 0.37–0.75 |
| Saving against today, per year | n/a | €41–105k | €21–52k |

The price of keeping a person on every rejection, compared with option B, is therefore 0.37–0.75 FTE, or €21–52k a year. The top 30% of applications (about 1,200 a month) are screened by recruiters under every option, so they are left out of this table.

One-off costs to quote in phase 0: the DPIA and legal review per country, an independent bias audit, ATS configuration, recruiter training time, and translation of candidate texts.

## 13. Assumptions, and what would change this plan

- **Assumption:** most volume is in store, warehouse and service roles. **Would change the plan:** if most volume is in specialist roles, option D matters less and C matters more.
- **Assumption:** the vendor can mask inputs and export scores and reasons. **Would change the plan:** if it can't, we don't activate scoring and stay with D and E.
- **Assumption:** confirming a proposed rejection takes about half the time of a full screen. **Would change the plan:** if the pilot shows it takes almost as long, the module adds little, and the time savings should come from D and E.
- **Would change the plan towards more automation:** a shadow test and pilot showing that the AI's bottom group contains almost nobody we would hire and disadvantages no group, plus works council agreement. Then we could automate narrow, objective knock-outs further, with a human route on request. Rejections based on the model's score would still be decided by a person.

## 14. Open questions

1. What exactly are we solving: recruiter hours, time to first response or quality of hire? What are today's numbers?
2. What share of the 4,000 applications a month is for store, warehouse and service roles?
3. Which works councils exist in each country and at each German site, and which existing agreements cover the ATS?
4. Where does the vendor process our data, and has any other EU customer with a works council already negotiated this module?

What are we missing, and what would make this plan wrong?

## Sources

1. GDPR, [article 22](https://gdpr-text.com/en/read/article-22/) and [recital 71](https://gdpr-info.eu/recitals/no-71/); fines in article 83(5).
2. Article 29 Working Party, Guidelines on automated individual decision-making and profiling (WP251 rev.01, endorsed by the EDPB), chapters IV.A and IV.C.1: [copy hosted by the Romanian data protection authority](https://dataprotection.ro/servlet/ViewDocument?id=1463).
3. CJEU, C-634/21 *SCHUFA Holding* (7 December 2023): [EUR-Lex](https://eur-lex.europa.eu/eli/C/2024/913/oj/eng); on its meaning for HR AI, [CMS (22 February 2024)](https://cms.law/en/deu/legal-updates/impact-of-the-cjeu-s-schufa-judgment-on-the-use-of-ai-in-hr).
4. CJEU, C-203/22 *Dun & Bradstreet Austria* (27 February 2025): [Court press release](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-02/cp250022en.pdf).
5. Digital Omnibus on AI, Regulation (EU) 2026/1744: [White & Case (July 2026)](https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act); [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/); [Lewis Silkin (9 July 2026)](https://lewissilkin.com/insights/2026/07/09/council-of-the-eu-gives-ai-omnibus-final-green-light-102nbb1).
6. AI Act, [article 26 (AI Act Service Desk)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26).
7. WOR art. 27(1)(e): [Rendement (2 December 2024)](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/instemmingsrecht-van-de-or-bij-personeelsbeleid.html).
8. [§95 BetrVG](https://www.gesetze-im-internet.de/betrvg/__95.html).
9. [§15 AGG](https://www.gesetze-im-internet.de/agg/__15.html); §22 AGG (burden of proof).
10. Belgium, CBA no. 9 and no. 39 and AI: [Osborne Clarke (19 April 2024)](https://www.osborneclarke.com/insights/what-should-employers-belgium-consider-when-using-ai-workplace).
11. Sackett, Zhang, Berry and Lievens, "Revisiting meta-analytic estimates of validity in personnel selection", *Journal of Applied Psychology* (2022); summary in [SIOP TIP](https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance).
12. Belgium, CAO no. 38 recruitment code: [Securex](https://www.securex.be/nl/lex4you/werkgever/themas/aanwerven-arbeidsovereenkomst/selectie-en-werving/wat-is-de-gedragscode-die-volgens-cao-nr-38-nageleefd-moet-worden); recommendations on AI in recruitment from the Belgian Institute for the Equality of Women and Men with ULiège and UHasselt: [policy brief](https://orbi.uliege.be/bitstream/2268/340904/1/IEFH%20ULiege%20UHasselt%20-%20AI%20%26%20Recruitment%20-%20Policy%20Brief%20EN.pdf).
13. Bias-detection legal basis after the Omnibus: [Orrick (29 July 2026)](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes).
14. [University of Washington News (31 October 2024)](https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/), on Wilson and Caliskan, AAAI/ACM Conference on AI, Ethics, and Society.
15. Reuters report on Amazon's recruiting tool, via [Euronews (10 October 2018)](https://www.euronews.com/2018/10/10/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women).
16. [EEOC, iTutorGroup settlement (11 September 2023)](https://eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit).
17. *Mobley v. Workday*, preliminary certification of a collective action under the Age Discrimination in Employment Act (16 May 2025): [Holland & Knight](https://www.hklaw.com/en/insights/publications/2025/05/federal-court-allows-collective-action-lawsuit-over-alleged).
