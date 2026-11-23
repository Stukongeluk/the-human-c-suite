# AI CV screening: rollout plan

*Draft for discussion with HR leadership, Talent Acquisition, the DPO, employment counsel and the works councils in the Netherlands, Belgium and Germany. 23 November 2026. This is not legal advice. Laws are dated as checked in November 2026; counsel in each country should confirm them before anything goes live.*

## Recommendation

We introduce the ATS screening module to help recruiters, not to decide for them. It sorts the queue and summarises each application against the published criteria for the role. A recruiter decides every rejection. We test the module on our own applicants before any live use, and we roll it out country by country once our employee representatives have agreed to it. The first assisted pilot can start in about three months. If the pilot meets its criteria, the group-wide rollout starts from about month seven.

**What this plan changes from the original request.** The request was to auto-reject the lowest-scoring 70% of applications without a recruiter looking. This plan keeps a recruiter on every rejection and replaces the fixed 70% with published, job-related criteria. There are three reasons. A solely automated rejection is generally not allowed under Article 22 of the GDPR. It would need works council agreement that we don't yet have. And it would hide any bias from us.

## 1. The problem we are solving

We fill this in during weeks 1–2 from ATS data, by country and job family. Without a baseline we can't show that the module helped.

| Measure | Today | Target (to agree) |
|---|---|---|
| Applications per month (group total about 4,000) | | |
| Share of applications for store, warehouse and customer-service roles | | |
| Time from application to first response | | e.g. within 5 working days |
| Time to hire | | |
| Recruiter hours spent on first screening per month | | e.g. halved |
| Candidates who drop out before an interview | | |
| Hires still employed at 90 days, or passing probation | | no worse than today |
| Share progressing at each stage, by group, where lawful to measure | | no unexplained gaps |

The question we want answered: is the pressure recruiter workload, slow replies that lose good candidates, or the quality of hires? Each answer points to a different fix. For high-volume frontline roles, a short structured application and automatic interview booking may save more time than any CV scoring.

## 2. How the module will be used

1. **No automatic rejections.** Auto-reject stays switched off in every country. A trained recruiter makes each rejection. That recruiter sees the application and can overrule the module.
2. **Criteria first.** For each job family, the must-have and nice-to-have criteria are written down, job-related and published in the ad. They are agreed, with the works councils where the law requires it, before the module scores anyone. Rejections follow these criteria, not a share of the pool. In a strong month more people go forward; in a weak month fewer do.
3. **Reasons, not just a number.** For each criterion, recruiters see what the module found in the CV and where. Nobody acts on a single overall score. The CJEU has held that a score a decision-maker relies on can count as the decision itself ([SCHUFA, C-634/21](https://curia.europa.eu/juris/liste.jsf?num=C-634/21)), so the recruiter's own judgement has to be real.
4. **Sorting, not filtering.** The module orders the queue and drafts summaries. A person opens every application before it is rejected.
5. **Inputs we switch off or exclude:**
   - video or voice analysis, and any emotion or personality inference (emotion recognition in recruitment has been prohibited under the AI Act since 2 February 2025; [Bundesnetzagentur](https://bundesnetzagentur.de/EN/Areas/Digitalisation/AI/08_ProhibitedPractices/start.html))
   - photo, name, date of birth or graduation year as a stand-in for age, address or postcode, nationality, marital status
   - penalties for gaps in a CV (these often mark care, parental leave or illness) and for part-time history
   - pay history (the EU Pay Transparency Directive bans asking about it)
   - social media scraping
6. **Candidates are told and can reach a person.** See section 10 for the draft texts.
7. **The logs judge the tool, not recruiters.** Override and decision logs are used at team and job-family level to monitor the module. They are never used to rank or assess individual recruiters. We agree this in writing with the works councils.
8. **One named owner** is accountable for the module after go-live (section 3).

## 3. Who owns what

| Role | Responsibility |
|---|---|
| Executive sponsor: CHRO | Decision to proceed at each go/no-go, and the relationship with the works councils |
| Programme owner: Head of Talent Acquisition | Baseline, pilot, monitoring after go-live, and the stop decision if a stop rule is triggered |
| Data protection officer | DPIA, lawful basis, candidate notices, access and explanation requests, retention |
| Employment counsel in NL, BE and DE | Representative rights, equality law, AI Act duties, review of this plan |
| Works council liaison per country | Consultation and consent process, and the pilot agreements |
| ATS administrator / IT | Module settings, excluded inputs, logs, exports for testing |
| Recruiter design group (4–6 recruiters from all three countries, including high-volume frontline hiring) | Criteria per job family, the summary format, the override workflow, training |
| Finance partner | Cost of the pilot, value of the time saved, cost of legal exposure |

## 4. Phases and timeline

| Phase | Weeks | What happens | Ready to move on when |
|---|---|---|---|
| 0. Frame and prepare | 1–4 | Baseline from the ATS. Vendor questions sent (section 7). DPIA started. Each works council told about the problem and the options, not a finished plan. Recruiter design group set up. Criteria drafted for 2–3 high-volume job families. | Problem and targets written down. Vendor answers received. Works councils engaged. |
| 1. Offline test | 4–10 | The module runs on past applications that our retention rules still let us hold. We compare its sorting with what recruiters actually decided and who was hired. | No unexplained gaps between groups. Few strong candidates sorted to the bottom. DPIA covers the test. |
| 2. Live shadow | 8–14 | The module scores live applications in the background in one country and 1–2 job families. Recruiters don't see the scores, and we compare afterwards. This runs under a time-limited pilot agreement with the works council concerned. | Same tests as phase 1 on live data. Pilot agreement in place. |
| 3. Assisted pilot | 14–26 | Recruiters see the summaries and sorting and decide every application. Candidates are told. A second recruiter reviews a random 5% of rejections blind. Stop rules are active. | Go/no-go criteria met (section 8). Recruiters and the works council have reviewed the results. |
| 4. Country-by-country rollout | from about month 7 | Each country goes live only after its works council has agreed. Monthly monitoring. Re-test after every model update. | Ongoing |

Timing depends most on the works councils. In Germany, if no agreement is reached, an arbitration board (Einigungsstelle) decides, which can take months. Plan for that rather than around it. Because the group operates in three countries, the simplest and fairest approach is to apply the strictest rule everywhere: a person on every rejection, and agreement with representatives before use.

## 5. Employee representatives, per country

Bring each one in at the problem stage, with the baseline numbers, while the design can still change. Treat their objections as free risk analysis.

**Netherlands**
- **Recruitment policy:** a rule on recruitment and selection needs works council consent ([article 27(1)(e) WOR](https://wetten.overheid.nl/BWBR0002747)).
- **Monitoring recruiters:** because the module logs what recruiters do, consent is also likely needed under 27(1)(l) (systems suited to monitoring behaviour or performance) and 27(1)(k) (processing of employees' personal data).
- **Which council:** for a system used across the group, this is usually the central works council.
- **Without consent:** a decision taken without consent is void if the works council invokes that in writing within one month.

**Germany**
- **Selection guidelines:** guidelines for selecting new hires need the works council's consent, and the law says so explicitly when AI is used to draw them up ([§95(1) and (2a) BetrVG](https://www.gesetze-im-internet.de/betrvg/__95.html)).
- **Questionnaires:** application questionnaires, including any knockout questions, need consent ([§94 BetrVG](https://www.gesetze-im-internet.de/betrvg/__94.html)).
- **Monitoring recruiters:** technical systems suited to monitoring employees, such as logs of recruiters' actions, are subject to co-determination ([§87(1) no. 6 BetrVG](https://www.gesetze-im-internet.de/betrvg/__87.html)).
- **Planning and expert:** the works council must be informed about planned work processes that use AI ([§90 BetrVG](https://www.gesetze-im-internet.de/betrvg/__90.html)). It may bring in an expert to assess the AI, at the employer's cost ([§80(3) BetrVG](https://www.gesetze-im-internet.de/betrvg/__80.html)).
- **Which council:** check whether there is a works council in each entity. For a uniform system across the company, the central works council (Gesamtbetriebsrat) is often the one responsible.

**Belgium**
- **Personnel policy:** the works council must be informed about rules on personnel policy, including recruitment and selection, and about projects that would change them, and it gives advice (CBA No. 9). A recruitment AI tool is a typical example ([Osborne Clarke](https://www.osborneclarke.com/node/23410); [ACV on the works council's role](https://www.hetacv.be/militant/themas/or-personeelsbeleid)).
- **New technology:** where a new technology has significant collective consequences for employment or working conditions, such as recruiters' work, CBA No. 39 requires information and consultation in advance. Counsel should confirm whether it applies and the lead time.
- **Recruitment code:** CBA No. 38 sets a code of conduct for recruitment. It asks employers to tell unsuccessful qualified candidates in writing within a reasonable time, to keep candidate data confidential and to finish the procedure within a reasonable time. Most of it is morally rather than legally binding ([Securex](https://www.securex.be/nl/lex4you/werkgever/themas/aanwerven-arbeidsovereenkomst/selectie-en-werving/wat-is-de-gedragscode-die-volgens-cao-nr-38-nageleefd-moet-worden)).

**Internal applicants.** If the module also scores employees who apply internally, it assesses employees directly. Include that in every consent and consultation request.

**Recruiters.** Their work changes most. The time the module saves is planned for faster replies and more interview time. Any change to recruiter roles goes through the normal consultation process.

## 6. Data protection, equality law and the AI Act

**GDPR (all three countries)**
- **Responsibility:** we are the controller. A vendor's statement that its product is "GDPR-compliant" doesn't cover how we use it, and the decision design is ours.
- **No solely automated rejection:** a decision based solely on automated processing that significantly affects a person is generally not allowed without a legal exception and safeguards ([Article 22](https://eur-lex.europa.eu/eli/reg/2016/679/oj)). Recital 71 names "e-recruiting practices without any human intervention" as an example. The contract-necessity exception requires us to show that no less intrusive method would work. About 190 applications a working day, spread across three countries and many recruiters, is hard to fit into that. Even then, candidates keep the right to a human review and to contest the decision. EU regulators' guidance also requires human involvement to be meaningful, not a token gesture ([Article 29 Working Party, WP251rev.01](https://ec.europa.eu/newsroom/article29/items/612053)).
- **DPIA:** scoring applicants at scale with a new technology meets several of the criteria for a mandatory data protection impact assessment (Article 35). It must be finished before the live shadow phase.
- **Transparency:** privacy notices must explain that software is used, what it looks at and how a person decides (Articles 13–14).
- **Explanations:** when asked, we must explain the procedure and principles actually applied to the person's data ([CJEU, Dun & Bradstreet Austria, C-203/22, 27 February 2025](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-02/cp250022en.pdf)).
- **Processor agreement (Article 28):** covers EU hosting, sub-processors and any transfers. It also says whether the vendor may use our candidates' data to train its general model. Our default is no.
- **Retention:** follow each country's practice. Dutch DPA guidance is generally four weeks after the procedure ends, or up to a year with consent. In Germany, data is usually kept a few months, to cover the deadline for discrimination claims. Short retention may leave little history for the offline test; if so, rely on the live shadow phase.
- **Bias testing with sensitive data:** measuring outcomes by group may need sensitive data. The 2026 AI Act amendments allow processing personal data where strictly necessary to detect and correct bias, under safeguards ([Loyens & Loeff](https://www.loyensloeff.com/fr/insights/news--events/news/eu-ai-act-key-amendments-adopted-under-digital-omnibus-package/)). The DPO confirms the scope. Use voluntary, separately stored equality monitoring, reported only in aggregate.

**Equality law: the exposure if the module skews against a group**
- **Germany:** a rejected applicant can claim compensation of up to three months' pay even if they wouldn't have been hired, and must claim within two months ([§15 AGG](https://www.gesetze-im-internet.de/agg/__15.html)). Once there is evidence pointing to discrimination, the burden of proof shifts to us ([§22 AGG](https://www.gesetze-im-internet.de/agg/__22.html)).
- **Belgium:** discrimination at work carries a lump-sum compensation of six months' gross pay ([CMS](https://cms.law/en/int/expert-guides/cms-expert-guide-on-discrimination-in-the-workplace/belgium)).
- **Netherlands:** equal treatment law applies to recruitment, and candidates can take complaints to the Netherlands Institute for Human Rights.

**AI Act**
- **Status:** CV screening is a high-risk use (Annex III, point 4) ([Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)). After the 2026 Digital Omnibus, the obligations for these systems apply from **2 December 2027** ([Lewis Silkin](https://lewissilkin.com/insights/2026/07/09/council-of-the-eu-gives-ai-omnibus-final-green-light-102nbb1)). They don't apply yet, but we build to them now so we don't have to rebuild later.
- **What they ask of us as the user of the system:**
  - use it according to the vendor's instructions
  - give human oversight to people with the competence, training and authority to overrule it
  - make sure the data we feed it is relevant
  - monitor it and report risks to the vendor
  - keep its logs for at least six months
  - inform workers' representatives and the workers affected before using it at work
  - inform candidates that it is used in decisions about them
  - explain individual decisions on request
- **Training:** providers and users must take measures to support AI literacy among the staff who use the system (Article 4, as amended in 2026). The recruiter training in section 9 covers this.

## 7. Questions for the vendor (send in week 1)

1. What does the model use as input, and what is it trained to predict? On whose data was it trained, and how recent is that data?
2. Which inputs can we switch off (section 2, point 5)? Can the module show evidence for each criterion instead of one score?
3. Your bias audit: who did it, on what data, for which groups, with which fairness measure, and with what results? Do the results hold for Dutch, French and German CVs and for CVs from frontline workers?
4. How was it validated against job performance or retention, and not just against past recruiter choices?
5. What are its error rates, in particular how often it sorts strong candidates to the bottom?
6. Please send your instructions for use and technical documentation as required for high-risk systems, and your plan for the AI Act conformity assessment and EU database registration by December 2027.
7. How can a recruiter overrule the module, and is the override logged with a reason?
8. Which logs do we get, for how long, and can we export scores and decisions for our own audits?
9. How are we notified of model updates, and can we test an update before it goes live?
10. Where is the data hosted, which sub-processors are used, and are there transfers outside the EEA?
11. Is our candidates' data used to train models for other customers?
12. Which other European retail clients use the module with auto-reject switched off, and what did they measure?

## 8. Testing and the pilot

**What we compare.** In phases 1 and 2, we put the module's sorting next to recruiters' actual decisions on the same applications. We look at three things:
- **Agreement:** how often the module and recruiters agree, compared with how often two recruiters agree with each other on a blind sample.
- **Missed candidates:** applicants the module would have put at the bottom but who were interviewed, hired or passed probation.
- **Gaps between groups:** progression rates by gender, age band, part-time history, CV gaps, CV language and country of education, plus disability and nationality where this is lawful and data is available. We look at each stage and each job family.

Human screening isn't neutral either. Field experiments in all three of our countries found that minority applicants needed to send more applications to get the same responses ([Quillian et al., 2019](https://www.ipr.northwestern.edu/news/2019/quillian_racial_discrimination.html)). We therefore test recruiters and the module side by side and trust neither by default.

**Measures, reported monthly at job-family and country level (never per recruiter)**

| Measure | Why |
|---|---|
| Time to first response, time to hire | The problem we are solving |
| Recruiter screening hours per month | The saving |
| Progression rate by group at each stage | Fairness |
| Disagreement rate in the 5% blind second review of rejections | Catching rubber-stamping and errors |
| Share of module suggestions that recruiters overrule | A very low share can mean people have stopped checking |
| 90-day retention and probation pass rate of hires | Quality of hire |
| Candidate requests for an explanation or a second look, and how many changed the outcome | Whether people can actually contest a decision |
| Candidate complaints and satisfaction | Our employer brand, and our customers |

**Go/no-go for rollout, all of which must hold**
- Time to first response and screening hours improved against the baseline by the agreed targets.
- No group's progression rate in any job family falls below 80% of the highest group's rate, unless there is a written, job-related explanation. This four-fifths test is a US rule of thumb ([29 CFR 1607.4(D)](https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607/section-1607.4)). We use it as a tripwire, not as a legal standard.
- In the blind review, disagreement on rejections is no higher than disagreement between two recruiters.
- Quality of hire is no worse than the baseline.
- The works council in the country concerned has agreed.

**Stop rules, agreed before the pilot starts.** The programme owner pauses the module in a job family or country if any of these happen:
- a group-gap tripwire is breached and not explained within two weeks
- blind-review disagreement rises above the agreed threshold
- the vendor changes the model without notice
- an excluded input turns out to be in use
- a data protection authority or equality body opens an inquiry
- a works council withdraws its agreement

During a pause, recruiters screen as they do today.

## 9. Recruiters

- **Design:** the recruiter design group shapes the criteria, the summary format and the override workflow, and reviews every phase's results before the next phase starts.
- **Training before the pilot:** what the module does and doesn't do, how it can be wrong, and automation bias (the pull to agree with the machine). Recruiters learn how to overrule it and record why, and how to handle a candidate's request for an explanation. Training is documented to meet the AI literacy duty.
- **Workload:** checking the module's suggestions takes time, and that time is planned, not squeezed. Override logs are not used to judge individual recruiters (section 2, point 7).

## 10. Candidate communication (drafts, to translate into Dutch, French and German)

**In the job ad and on the application page**
> We use software to help our recruiters sort applications and summarise them against the requirements in this ad. The software doesn't reject anyone: a recruiter reads every application and decides. You can ask how it was used for your application, and ask another recruiter to take a second look, at [contact].

**Privacy notice paragraph**
> When you apply, our applicant tracking system compares the information in your application with the requirements listed in the ad and gives our recruiters a summary and a suggested order. It does not use your photo, age, nationality, address or any analysis of video or voice. A recruiter makes every decision about your application. You have the right to an explanation of how the software was used, to give your view, and to ask for your application to be reviewed by another person. [Retention period per country.] [DPO contact.]

**Rejection message**
> Thank you for applying for [role]. A recruiter has read your application against the requirements in the ad ([the two or three must-haves]) and we won't be taking it further this time, because [reason in one line]. If you think we've missed something, reply within 14 days and another recruiter will look at it again. You can also ask us what information we used and how [link].

**Reply to a request for an explanation**
> You asked how your application for [role] was assessed. Our software compared your application with these requirements: [list]. For each one it found: [summary]. Recruiter [first name] read your application and decided [outcome] because [reason]. [Second recruiter] has now looked at it again and [confirms / has changed the outcome]. If you disagree, you can contact our data protection officer at [contact].

## 11. Cost and timing (for finance)

- **Keeping a person on every rejection.** At 4,000 applications a month, the bottom 70% would be about 2,800 applications. If the module summarises each against the criteria, a recruiter needs roughly one to two minutes to confirm or overturn it. That is about 47–93 hours a month, or 0.3–0.6 FTE across the group. This is an estimate; the phase 0 baseline will firm it up, and the pilot measures the real time.
- **One-off costs to price:**
  - employment and data protection counsel in three countries
  - the DPIA
  - an independent bias audit (get quotes)
  - Talent Acquisition time for the pilot (around a fifth of one lead's time for six months)
  - the recruiter design group's time
  - works council time, plus any expert a German works council brings in
- **Exposure avoided by not auto-rejecting:**
  - GDPR fines of up to €20 million or 4% of worldwide turnover for breaches of data subject rights, including Article 22 (Article 83(5))
  - AGG compensation in Germany and lump sums in Belgium, per affected applicant
  - works council challenges that can stop or void the rollout
- **Brand.** About 33,600 people a year would be rejected without anyone looking, and in retail many of them are customers. Virgin Media reported that 18% of its unsuccessful candidates were customers, and it put the cost of poor candidate experience at £4.4 million a year ([Starred](https://www.starred.com/blog/how-virgin-media-revolutionized-their-candidate-experience); a vendor's account, so read it as direction only).
- **When the benefit lands.** The benefit (faster replies and recruiter time) shows up from the assisted pilot, around month four. The costs come first.

## 12. Monitoring after go-live

- **Monthly:** the measures in section 8, by country and job family, reviewed by the programme owner and the DPO.
- **Quarterly:** the same report goes to the works councils and the recruiter design group, including what we changed.
- **After every model update:** the offline comparison is re-run before the update goes live.
- **Yearly:** an independent bias audit, a DPIA review and a review of this plan.
- **Candidates:** every request for an explanation or a second look is tracked to its outcome.

## 13. Pre-mortem: if this has failed a year from now, why?

| Likely reason | Early warning | What we do |
|---|---|---|
| Recruiters rubber-stamp the module, so in law and in practice it decides | Override share near zero; blind-review disagreement rising | Retrain recruiters, show criterion evidence instead of a score, rebalance workload |
| A hidden proxy (name, gaps, language) skews outcomes in one country | A group-gap tripwire in one job family | Pause that job family, find the input, remove it, re-test |
| The vendor updates the model silently | Sudden change in score patterns | Contract clause requiring notice; re-test before acceptance |
| Works council talks stall in one country | No pilot agreement by week 12 | Pilot where agreement exists; share results; don't go live without agreement |
| The time saving is smaller than hoped | Screening hours flat in the pilot | Put the effort into structured applications and automatic interview booking for frontline roles instead |

## 14. Assumptions, and what would change this plan

- **Volume:** most of the 4,000 monthly applications are for store, warehouse and customer-service roles. If most are office or technology roles, the criteria and the time estimate change.
- **The module:** it can switch off auto-reject, exclude inputs, show evidence per criterion and export logs. If it can't, we should look at a different module before piloting.
- **Works councils:** there is a works council in at least the Dutch and German entities. If not, we still consult staff and recruiters, because the GDPR, equality law and the AI Act apply either way.
- **The pilot results:** if the module sorts no better than a structured application form, the cheaper and more transparent option wins.

*What are we missing, and what would make this plan wrong?* Send comments to the programme owner before the phase 0 review.

## Sources

- Regulation (EU) 2016/679 (GDPR), Articles 13–15, 22, 28, 35, 83 and Recital 71: [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- Article 29 Working Party, Guidelines on automated individual decision-making and profiling (WP251rev.01), endorsed by the EDPB: [European Commission](https://ec.europa.eu/newsroom/article29/items/612053)
- CJEU, SCHUFA Holding (Scoring), C-634/21, 7 December 2023: [Curia](https://curia.europa.eu/juris/liste.jsf?num=C-634/21)
- CJEU, Dun & Bradstreet Austria, C-203/22, 27 February 2025: [Curia press release](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-02/cp250022en.pdf)
- Regulation (EU) 2024/1689 (AI Act), Articles 4, 5, 26, 86 and Annex III: [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj); Digital Omnibus on AI, final adoption and dates: [Lewis Silkin (July 2026)](https://lewissilkin.com/insights/2026/07/09/council-of-the-eu-gives-ai-omnibus-final-green-light-102nbb1), [Loyens & Loeff (June 2026)](https://www.loyensloeff.com/fr/insights/news--events/news/eu-ai-act-key-amendments-adopted-under-digital-omnibus-package/); emotion recognition: [Bundesnetzagentur](https://bundesnetzagentur.de/EN/Areas/Digitalisation/AI/08_ProhibitedPractices/start.html)
- Netherlands, Wet op de ondernemingsraden, article 27: [wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002747)
- Germany, BetrVG [§80](https://www.gesetze-im-internet.de/betrvg/__80.html), [§87](https://www.gesetze-im-internet.de/betrvg/__87.html), [§90](https://www.gesetze-im-internet.de/betrvg/__90.html), [§94](https://www.gesetze-im-internet.de/betrvg/__94.html), [§95](https://www.gesetze-im-internet.de/betrvg/__95.html); AGG [§15](https://www.gesetze-im-internet.de/agg/__15.html), [§22](https://www.gesetze-im-internet.de/agg/__22.html)
- Belgium: [Osborne Clarke on AI in the workplace (April 2024)](https://www.osborneclarke.com/node/23410); [ACV on the works council and personnel policy](https://www.hetacv.be/militant/themas/or-personeelsbeleid); [Securex on CBA No. 38](https://www.securex.be/nl/lex4you/werkgever/themas/aanwerven-arbeidsovereenkomst/selectie-en-werving/wat-is-de-gedragscode-die-volgens-cao-nr-38-nageleefd-moet-worden); [CMS on discrimination at work](https://cms.law/en/int/expert-guides/cms-expert-guide-on-discrimination-in-the-workplace/belgium); [Institute for the Equality of Women and Men, AI and recruitment (July 2026)](https://igvm-iefh.belgium.be/en/news/insights-ai-and-recruitment-how-mitigate-gender-bias-responsible-ai-practices)
- Selection methods: [Sackett, Zhang, Berry & Lievens (2022), *Journal of Applied Psychology*](https://doi.org/10.1037/apl0000994)
- AI screening cases: [Reuters on Amazon (2018)](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G); [Holland & Knight on Mobley v. Workday (2025)](https://www.hklaw.com/en/insights/publications/2025/05/federal-court-allows-collective-action-lawsuit-over-alleged)
- Human hiring discrimination: [Quillian et al. (2019), *Sociological Science*](https://sociologicalscience.com/download/vol-6/june/SocSci_v6_467to496.pdf), [Northwestern summary](https://www.ipr.northwestern.edu/news/2019/quillian_racial_discrimination.html)
- Four-fifths rule: [29 CFR 1607.4(D)](https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607/section-1607.4)
- Candidate experience: [Starred on Virgin Media](https://www.starred.com/blog/how-virgin-media-revolutionized-their-candidate-experience)
