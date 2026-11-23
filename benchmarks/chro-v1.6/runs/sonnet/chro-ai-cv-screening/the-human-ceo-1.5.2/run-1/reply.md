I'd roll this out in stages with the AI scoring and sorting CVs but a recruiter making every rejection, and not auto-reject the bottom 70% (2,800 of 4,000 applicants a month, 33,600 a year). I've drafted the full plan for you, your DPO and the works councils in `rollout-plan.md`.

**Why not as proposed**
- **It is a fully automated decision about people.** GDPR Article 22 restricts decisions made solely by automated processing that significantly affect someone. The regulation's own recital uses e-recruiting without human intervention as its example. This sits in the higher fine tier (up to EUR 20m or 4% of worldwide turnover). Counsel needs to confirm how it applies to us.
- **The vendor's promises don't transfer the risk.** "GDPR-compliant" and "bias-free" are sales claims. We are the controller, and we are the ones who answer to candidates, regulators and courts. No CV model is bias-free: they learn from past hiring and can penalise gaps, part-time work, foreign education or language. Amazon scrapped its own recruiting tool in 2018 for this reason. We need to test on our own applicants, in four languages.
- **Works councils get a say first.** The Dutch works council has a consent right on systems that assess people (art. 27(1)(l) WOR). German works councils have co-determination on such systems (§87(1) no. 6 BetrVG), and the AGG protects applicants. Belgium needs a check, including the recruitment collective agreement (CAO 38). The EU AI Act classes recruitment AI as high-risk; the employer's duty to inform representatives currently applies from December 2027, but national rules apply now.
- **The 70% is a quota, not a quality bar.** In a strong month it rejects good candidates anyway.
- **The saving looks small.** At 2 to 5 minutes per CV (my estimate, please replace it with yours), screening is about 133 to 333 recruiter hours a month, or 0.9 to 2.1 FTE. We would be taking legal and hiring-quality risk on 48,000 applications a year for that.

**The staged plan (indicative, from December 2026)**
1. **Foundations, about 6 weeks.** Name an owner and DPO, start the DPIA, bring the works councils in now with the real numbers, and put vendor due diligence in writing: training data, validation on European candidates, audit rights, model-change notice. Write the candidate notice and a route to human review.
2. **Shadow mode, about 3 months.** The tool scores, but nobody is rejected on it. We measure who it would have rejected that recruiters advanced, and test selection rates by gender, age, language, gaps and country.
3. **Assist mode, one country and one job family, about 3 months.** Recruiters see the ranking and reasons, and decide. Each month they blind-review a sample of the lowest-scored applicants to check whether the score deserves trust.
4. **Extend country by country**, only after each gate is met. Automatic rejection is limited to objective, disclosed knock-outs (no right to work, missing mandatory licence), with human audits.

Each gate has stop rules. Score-based auto-rejection comes back only with a completed DPIA, counsel's sign-off, works council agreement and at least 12 months of clean audit data.

**People:** the business case assumes no recruiter cuts. Freed time goes to candidate contact, hiring-manager coaching and store hiring support. Recruiters join the design group, since they know the edge cases. If something goes wrong, accountability sits with us as leadership, not with the vendor or the recruiter.

**If speed is the real pain,** a short structured application with job-related knock-out questions and instant acknowledgements can start in weeks, without scoring anyone.

**Two questions that would change this plan:**
1. What is the actual problem: time to respond, time to hire, recruiter workload, quality of hires? What are today's numbers per country and job family?
2. Which entities have works councils or union representation in NL, BE and DE, and have they been told yet?

This is not legal advice, and the plan needs employment and data protection counsel in each country. What am I missing, and what would make this wrong?
