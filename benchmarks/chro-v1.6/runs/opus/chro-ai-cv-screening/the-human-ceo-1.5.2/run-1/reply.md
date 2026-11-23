**My recommendation: switch the module on as a ranking assistant, not as an auto-rejecter.** Let it score every CV and say why, and have a recruiter confirm each of the roughly 2,800 rejections a month. That costs an estimated 0.4–0.75 FTE more than full automation, about €21–52k a year. It also keeps you within GDPR article 22, gets the works councils on board and avoids a pattern of discrimination claims in Germany. The full rollout plan is in `rollout-plan.md`.

**Why not auto-reject the bottom 70%**

- **It's the case the GDPR restricts.** Recital 71 names ["e-recruiting practices without any human intervention"](https://gdpr-info.eu/recitals/no-71/) as its example. Regulators allow automated shortlisting only when nothing less intrusive works. [Their own example](https://dataprotection.ro/servlet/ViewDocument?id=1463) is one vacancy with tens of thousands of applications. You get about 190 a working day across many vacancies, and a human check costs under one FTE. Showing recruiters only the top 30% doesn't help: in [SCHUFA (2023)](https://cms.law/en/deu/legal-updates/impact-of-the-cjeu-s-schufa-judgment-on-the-use-of-ai-in-hr) the EU Court held that a score which largely settles the outcome can be the decision itself.
- **"Bias-free" is a claim, not evidence, and the liability is yours.** In a [University of Washington test (2024)](https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/), three language models ranking 550+ real CVs preferred white-associated names 85% of the time and Black-associated names 9%. In Germany, indications of discrimination shift the burden of proof to you, and [compensation can reach three months' salary](https://www.gesetze-im-internet.de/agg/__15.html) per applicant (AGG §§15, 22). Across 33,600 automated rejections a year, one flaw becomes a pattern. "GDPR-compliant" isn't a product feature: as controller, the DPIA, transparency and safeguards are yours.
- **Works councils have a say first.** In the Netherlands they have a consent right on hiring-policy rules ([art. 27(1)(e) WOR](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/instemmingsrecht-van-de-or-bij-personeelsbeleid.html)). In Germany they must consent to selection guidelines, including AI-built ones ([§95(1), (2a) BetrVG](https://www.gesetze-im-internet.de/betrvg/__95.html)). In Belgium the works council must be informed and consulted ([CAO 9 and 39](https://www.osborneclarke.com/insights/what-should-employers-belgium-consider-when-using-ai-workplace)).
- **The AI Act classes CV filtering as high-risk.** The deployer duties (trained human oversight, logs, informing candidates and staff) apply from 2 December 2027, after the [Digital Omnibus delay](https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act). Build it that way now, not twice.
- **CVs are a weak signal for most retail roles.** In the [largest recent meta-analysis](https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance), years of experience predicted performance at 0.07. Structured interviews scored 0.42 and work samples 0.33.

The trap: once a vendor's score becomes the final decision, nobody ever sees the good people you rejected, and the legal and brand risk stays with you.

**Options**

| Option | Recruiter time saved (est.) | Main risk | Reversible? |
|---|---|---|---|
| Do nothing | none | Slow replies, overloaded recruiters | Yes |
| Auto-reject bottom 70% | 0.75–1.5 FTE | Art. 22, AGG claims, works council veto, bias nobody sees | You can switch it off, but 33,600 rejections a year can't be undone |
| **AI ranks, a recruiter confirms every rejection** | 0.4–0.75 FTE | Rubber-stamping, unless designed against | Yes |
| **Plus: short applications for store roles, objective knock-outs, AI for scheduling** | Likely the most, unmeasured | Configuration work | Yes |

**The rollout, each phase with a gate**

1. **Prepare (weeks 1–8):** ATS baseline, vendor checks, DPIA, works councils in all three countries while the plan can still change, candidate notices, training.
2. **Shadow test (weeks 9–16):** the AI scores in the background while recruiters work as usual. Count how many of your actual hires it would have rejected, and compare selection rates by gender, age band and CV language. Proceed only if no group falls below 80% of the best-treated group.
3. **Pilot (months 5–7):** one country, one job family. Recruiters confirm every rejection, overrides are tracked, and candidates can ask for a human review and an explanation.
4. **Expand in waves (months 8–12):** country by country, and in Germany only after a works agreement is signed.
5. **Run and audit:** monthly dashboard, quarterly bias review, yearly independent audit, AI Act readiness check in September 2027.

**Start this week:** AI for interview scheduling and status updates, plus clear knock-out questions in job ads (right to work, availability, required licences), with a recruiter confirming the declines. Both save time without scoring anyone.

**People:** tell the recruiters first that nobody loses their job over this module, and that the freed time goes into faster replies and structured interviews. One executive, for example the CHRO, owns the outcomes: if the system treats applicants unfairly, that's on leadership, not on the recruiter who clicked "confirm".

**Get in writing from the vendor:** an adverse-impact report on European data, which CV fields the model uses and masks, and whether your applicants' data trains their model. The full list is in section 8 of the plan.

**Assumptions** (estimates, to check against your ATS and payroll): screening takes 2–4 minutes per CV today, confirming a proposed rejection takes about half that, and an FTE costs €55–70k a year all-in. **What would change my mind:** a shadow test showing the bottom 70% holds almost nobody you'd hire and disadvantages no group, plus works council agreement. Then I'd automate narrow, objective knock-outs further, with a human route on request. A person would still decide every score-based rejection.

**Two questions that would change the plan:**
1. What are you solving: recruiter hours, time to first response or quality of hire? What's today's number?
2. What share of the 4,000 are store, warehouse and service roles? For those I'd drop CV scoring altogether.

What am I missing, and what would make this wrong? This isn't legal advice: have employment and privacy counsel in each country check the plan before the pilot.
