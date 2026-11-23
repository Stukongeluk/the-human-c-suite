**Don't switch on auto-reject.** Roll the module out as recruiter-assisted triage instead: it sorts and summarises CVs, a recruiter decides every rejection, and it goes live country by country after a test on your own applicants and agreement with your works councils. The full rollout plan is in `ai-cv-screening-rollout-plan.md`. What I changed from your brief: a person looks at every rejection, and published criteria replace the fixed 70% cut, because the version you asked for isn't lawful as designed in any of your three countries.

**Why auto-rejecting 70% unread fails here**

- **It's a solely automated decision under the GDPR.** Rejecting 2,800 people a month with no human involved is what [Article 22](https://eur-lex.europa.eu/eli/reg/2016/679/oj) restricts; Recital 71 names "e-recruiting practices without any human intervention". Even a score a recruiter just follows can count as the decision ([CJEU, SCHUFA, C-634/21](https://curia.europa.eu/juris/liste.jsf?num=C-634/21)). The vendor can't be "GDPR-compliant" for you: you're the controller, and the design is yours.
- **Your works councils have to agree first.** A system switched on without this can be blocked or voided.
  - Netherlands: recruitment policy needs consent ([art. 27(1)(e) WOR](https://wetten.overheid.nl/BWBR0002747)).
  - Germany: selection guidelines need consent, explicitly also when AI is involved ([§95 BetrVG](https://www.gesetze-im-internet.de/betrvg/__95.html)), as do questionnaires (§94) and systems that log recruiters' work (§87(1) no. 6).
  - Belgium: the works council is informed and consulted on recruitment rules and new technology ([Osborne Clarke](https://www.osborneclarke.com/node/23410)).
- **The AI Act classes CV screening as high-risk.** From 2 December 2027 it needs trained people who can overrule it, monitoring, logs and notice to representatives and candidates ([Lewis Silkin on the final dates](https://lewissilkin.com/insights/2026/07/09/council-of-the-eu-gives-ai-omnibus-final-green-light-102nbb1)). Auto-reject would need rebuilding within a year.
- **"Bias-free" is a claim nobody has tested on your applicants.** Amazon dropped a CV scorer that learned to downgrade "women's" ([Reuters](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G)); Workday faces a US collective action over age ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2025/05/federal-court-allows-collective-action-lawsuit-over-alleged)). The risk is proxies: names, care or illness gaps, part-time history, graduation year, CV language. Reject 70% unread and you'll never see whose CVs they were.

The trap in one line: a fixed 70% is a curve. It rejects the same share whether this month's pool is strong or weak, and nobody sees who it got wrong.

**What keeping a person costs: roughly half a recruiter**

If the module summarises each low-sorted CV against your published must-haves, a recruiter can confirm or overturn it in one to two minutes. That's 2,800 × 1–2 minutes, or about 47–93 hours a month: 0.3–0.6 FTE across the group (my estimate; your baseline will firm it up). Against it:

- GDPR fines of up to €20 million or 4% of worldwide turnover
- in Germany, discrimination compensation per rejected applicant, up to three months' pay even if they wouldn't have been hired ([§15 AGG](https://www.gesetze-im-internet.de/agg/__15.html))
- in Belgium, a lump sum of six months' gross pay for discrimination at work ([CMS](https://cms.law/en/int/expert-guides/cms-expert-guide-on-discrimination-in-the-workplace/belgium))
- about 33,600 people a year rejected unread, and in retail many of them are your customers

**Options**

| Option | Gain | Risk | Reversible? |
|---|---|---|---|
| Auto-reject the bottom 70% (as asked) | 0.3–0.6 FTE of reading | Unlawful as designed; bias stays invisible | No. A wrongly rejected candidate is gone |
| **Assisted triage, a person decides every rejection (recommended)** | Most of the time saving; faster first replies | Rubber-stamping, caught with blind spot checks | Yes |
| Restructure frontline hiring: short structured application, automatic interview booking, structured interviews | Likely the biggest speed gain for store and warehouse roles | New forms need works council agreement | Yes |
| Do nothing | Nothing | Recruiter overload, slow replies, lost candidates | Not applicable |

I'd combine the second and third: in high-volume hiring, speed comes from structure, and structured, job-related assessment best predicts performance ([Sackett et al., 2022](https://doi.org/10.1037/apl0000994)).

**The plan in brief** (the full version adds vendor questions, stop rules and candidate texts)

1. **Weeks 1–4:** baseline from the ATS (time to first reply, time to hire, recruiter hours, 90-day retention); vendor due-diligence questions; data protection impact assessment started; the problem, not a finished plan, taken to the works councils; a recruiter design group set up.
2. **Weeks 4–14:** test on past applications your retention rules still allow, then live in shadow mode, with scores hidden from recruiters. Compare with recruiter decisions, and outcomes by group.
3. **Weeks 14–26:** assisted pilot in one country and job family, under a pilot agreement with its works council. Candidates are told, a person makes every rejection, a second recruiter re-checks 5% blind, and stop rules are agreed up front.
4. **From about month 7:** country by country, once each works council agrees and go/no-go criteria are met. Monthly monitoring by group, never per recruiter; re-test after every model update.

**Can start this week, with nothing switched on:** everything in step 1. Keep auto-reject off and scores hidden until the shadow test.

**Two questions that would change the plan**

1. What is the 70% meant to fix: recruiter workload, time to hire, or quality of hire? And what share of the 4,000 applications is for store, warehouse and service roles?
2. Which works councils do you have: a Dutch central works council, a German Gesamtbetriebsrat, Belgian works councils?

**Key assumptions:** most volume is frontline retail hiring; the module can show reasons per criterion and log decisions; you have works councils in at least the Netherlands and Germany.

In fairness to the vendor: human screeners are biased too, as field experiments in all three of your countries show ([Quillian et al., 2019](https://www.ipr.northwestern.edu/news/2019/quillian_racial_discrimination.html)). So the plan tests the module and your recruiters side by side and trusts neither by default.

What am I missing, and what would make this wrong?

*This isn't legal advice. Have employment and data protection counsel in each country check the plan before anything goes live.*
