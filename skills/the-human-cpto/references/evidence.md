# Evidence: product, engineering, AI and what works for people

Use these cases and studies to back up recommendations. State their limits honestly, and look for newer evidence when the decision depends on it: this file was last checked in November 2026. The detailed AI-in-engineering figures (DORA, METR, Faros, GitClear, Uplevel, Veracode, Stack Overflow) are in `ai-in-engineering.md`.

## Contents

- Building what customers use
  - Most features are rarely used
- Rewrites, outsourcing and core knowledge
  - Rewriting from scratch: Netscape
  - Outsourcing core work: the Boeing 787
  - The insourcing trend
- AI claims and juniors
  - AI makes confident mistakes, and the company is liable
  - Entry-level jobs and the talent pipeline
  - Protection for people who speak up (Netherlands and EU)
- Redeploying instead of cutting
  - IKEA (Ingka Group): AI took the routine work, people took new work
  - Klarna: from "AI does the work of 700 agents" to hiring humans again
  - Companies that cut jobs for AI often regret it
- The hidden costs of layoffs
- European and Nordic social practice
- Voice, fair process and leadership
- People and shareholder returns move together
- Shortcuts and decision quality
- How to use this file

Search for the topic you need (for example "Pendo", "Boeing" or "Klarna") instead of reading the whole file.

## Building what customers use

### Most features are rarely used

- Pendo's 2019 Feature Adoption Report analysed feature usage across 615 software products over three months. On average 12% of features generated 80% of daily usage, and 80% of features were rarely or never used. Pendo estimated publicly traded cloud companies spent up to $29.5 billion developing features that were rarely or never used.
- Limits: a vendor that sells adoption analytics, products that use Pendo, and an older dataset. Use it as a prompt to check your own adoption data, not as your number.
- Source: [Pendo, The 2019 Feature Adoption Report](https://www.pendo.io/resources/the-2019-feature-adoption-report/)

## Rewrites, outsourcing and core knowledge

### Rewriting from scratch: Netscape

- In April 2000 Joel Spolsky wrote that Netscape, by rewriting its browser from scratch, made "the single worst strategic mistake that any software company can make". The last major release had come almost three years before the next one went into beta, while competitors kept shipping.
- His argument: old code carries years of bug fixes and knowledge about edge cases, and throwing it away throws away that knowledge.
- Limits: an essay, not a study, and later writers describe rewrites that worked when scope was frozen and the old system kept running. Use it as a warning to prefer incremental replacement (the strangler-fig pattern).
- Source: [Joel Spolsky, "Things You Should Never Do, Part I" (2000)](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/)

### Outsourcing core work: the Boeing 787

- In 2001 Boeing senior technical fellow John Hart-Smith warned in an internal paper that excessive outsourcing would erode profits, concluding that "outsourcing all of the value-added work is tantamount to outsourcing all of the profits." Boeing defended its strategy. Source: [The Seattle Times (March 2003)](https://archive.seattletimes.com/archive/20030309/boeingcritique09/boeing-buzzes-about-source-of-work)
- Boeing went on to outsource large parts of the 787 Dreamliner's design and production. The programme ran years late. In 2011 Jim Albaugh, head of Boeing Commercial Airplanes, conceded that the outsourcing strategy had backfired and that recovering cost far more than keeping key technology closer to home would have. Source: [Aviation Week, reporting The Seattle Times (February 2011)](https://aviationweek.com/air-transport/aircraft-propulsion/boeing-commercial-airplanes-ceo-concedes-787-outsourcing)
- Lesson: outsourcing core, quality-critical work moves knowledge and control out of the company and adds coordination costs that rarely show up in the business case.

### The insourcing trend

- Deloitte's 2024 Global Outsourcing Survey of more than 500 executives reports that insourcing is on the rise and that organisations are rethinking talent strategies to gain more control and build strategic capabilities internally, while still using outsourcing where it fits. Source: [Deloitte (2024)](https://www.deloitte.com/us/en/services/consulting/articles/global-outsourcing-survey.html)
- Use it as a signal, not proof: it is a survey by a firm that also sells sourcing advice.

## AI claims and juniors

### AI makes confident mistakes, and the company is liable

- In Moffatt v. Air Canada (2024 BCCRT 149, 14 February 2024), the British Columbia Civil Resolution Tribunal held Air Canada liable for incorrect bereavement-fare information given by the chatbot on its website, and rejected the argument that the chatbot was responsible for its own actions. Source: [American Bar Association, Business Law Today (February 2024)](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- Use it to counter "AI is never wrong": errors happen, and responsibility stays with the company.

### Entry-level jobs and the talent pipeline

- Stanford Digital Economy Lab researchers (Brynjolfsson, Chandar, Chen) use ADP payroll data on millions of US workers. In the August 2026 revision, employment of workers aged 22–25 in AI-exposed occupations stood 19% below where it would have been had it kept pace with less-exposed peers, with no comparable gap for experienced workers. The authors call these descriptive indicators rather than causal estimates. Source: [Stanford Digital Economy Lab, "Canaries in the Coal Mine?"](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/)
- AWS CEO Matt Garman called replacing junior staff with AI "one of the dumbest things I've ever heard" (August 2025), arguing that juniors are among the least expensive employees, among the most engaged with AI tools, and the source of the future talent pipeline. Source: [The Register (August 2025)](https://www.theregister.com/2025/08/21/aws_ceo_entry_level_jobs_opinion/)
- Use the trend as the risk to manage, not as a justification: if everyone stops hiring juniors, nobody grows the seniors of 2030.

- SignalFire's 2025 talent report found Big Tech new-grad hiring down 25% in 2024 compared with 2023 and over 50% compared with 2019; new grads made up 7% of hires. Source: [SignalFire (May 2025)](https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025)

### Protection for people who speak up (Netherlands and EU)

- The Dutch Whistleblower Protection Act (Wet bescherming klokkenluiders) took effect on 18 February 2023, replacing the earlier Wet Huis voor klokkenluiders and implementing EU Directive 2019/1937. Organisations with 50 or more workers must have an internal reporting procedure, and the Huis voor Klokkenluiders advises people who report. Source: [Huis voor Klokkenluiders, FAQ for employers](https://www.huisvoorklokkenluiders.nl/binaries/huisvoorklokkenluiders/documenten/publicaties/2023/04/23/wet-bescherming-klokkenluiders/20231219+FAQ+Werkgevers+tav+Wet+bescherming+klokkenluiders.pdf)
- Not legal advice: check the current rules and the company's own procedure, and get counsel before any external report.

## Redeploying instead of cutting

### IKEA (Ingka Group): AI took the routine work, people took new work

- In 2021 Ingka Group, the largest IKEA franchisee, introduced an AI assistant called Billie. Over two years it handled 47% of customer queries to the call centres.
- Instead of cutting call centre jobs, Ingka retrained about 8,500 call centre workers as remote interior design advisers from 2021 onwards.
- Forrester reports that this advisory business brought in about €1.3 billion in 2022, roughly 3.3% of total revenue.
- Lesson: ask what higher-value work people can do once AI removes the repetitive tasks, and look for unmet customer demand. The automation saved money; the redeployment made money.
- Sources: [The Globe and Mail / Reuters (June 2023)](https://theglobeandmail.com/business/international-business/article-ikea-bets-on-remote-interior-design-as-ai-changes-sales-strategy/), [Forrester (July 2026)](https://www.forrester.com/blogs/ai-helped-ikea-create-e1-3-billion-in-new-revenue-but-not-how-you-think/)

### Klarna: from "AI does the work of 700 agents" to hiring humans again

- In February 2024 Klarna said its AI assistant did the work of 700 customer service agents. It paused hiring for over a year, and headcount fell about 22%, mostly through attrition.
- In May 2025 CEO Sebastian Siemiatkowski told Bloomberg that cost had been too dominant a factor and that service quality had suffered. Klarna started recruiting human customer service agents again, so customers can always reach a person.
- Lesson: measure quality, not only cost per contact, and keep a route to a human. Note that Klarna mainly shrank through attrition rather than mass layoffs; the cautionary point is about quality.
- Source: [Entrepreneur (May 2025), reporting Bloomberg](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)

<!-- shared:ai-layoff-regret -->
### Companies that cut jobs for AI often regret it

- In an Orgvue survey of more than 1,000 senior leaders (2025), 39% had made people redundant because of AI, and 55% of those said they had made the wrong decisions. Source: [HR Dive (2025)](https://www.hrdive.com/news/leaders-who-laid-off-workers-due-to-ai-regretted-it/746643/)
- Careerminds surveyed 600 HR leaders who made layoffs in the previous 12 months (February 2026):
  - Two in three companies that cut jobs because of AI were already rehiring, and 52% of those rehires came within six months.
  - Only 8.4% said their AI-driven restructure delivered and that they would repeat it unchanged.
  - For 30.9%, rehiring costs exceeded the savings.
  - Entry-level roles were hit hardest.
  - Sources: [Careerminds](https://careerminds.com/resources/cost-of-ai-layoffs), [CPA Practice Advisor (July 2026)](https://www.cpapracticeadvisor.com/2026/07/13/9-in-10-hr-leaders-regret-ai-driven-layoffs-new-survey-finds/186619/)
- Limits: both are vendor surveys (an org-design software firm and an outplacement firm). Use them as a strong signal, not as precise rates.
<!-- /shared:ai-layoff-regret -->

<!-- shared:hidden-costs-of-layoffs -->
## The hidden costs of layoffs

### Health and mortality

- Sullivan and von Wachter matched Pennsylvania earnings records from the 1970s and 1980s to death records. For high-seniority men who lost their job in a mass layoff, mortality in the following year was 50% to 100% higher than expected. Twenty years later, yearly death rates were still about 10% to 15% higher.
- Limits: US data from a specific period and group, with a weaker safety net than many European countries. Use it as evidence that job loss can do lasting harm, not as a precise forecast.
- Source: [Sullivan & von Wachter, "Job Displacement and Mortality", Quarterly Journal of Economics (2009)](https://ideas.repec.org/a/oup/qjecon/v124y2009i3p1265-1306..html)

### Survivors leave too

- Trevor and Nyberg found that downsizing a workforce by 1% was associated with a 31% increase in voluntary turnover the following year.
- Lesson: count the cost of losing people you wanted to keep, and invest in the people who stay.
- Sources: Trevor, C.O. & Nyberg, A.J. (2008), "Keeping your headcount when all about you are losing theirs", *Academy of Management Journal* 51(2), 259–276; summary by the [University of Wisconsin–Madison](https://clipsheet.strategiccommunication.wisc.edu/?p=218008)
<!-- /shared:hidden-costs-of-layoffs -->

<!-- shared:european-social-practice -->
## European and Nordic social practice

Details, country rules and limits: [european-and-nordic-practice.md](european-and-nordic-practice.md).

### Job security councils: Sweden re-employs displaced workers fastest

- Swedish employers fund job security councils through collective agreements. The councils step in as soon as notice is given, with counselling, training and money.
- The OECD found that over 85% of displaced Swedish workers found a new job within a year, the highest share in the OECD.
- Limits: Sweden's labour market was strong in that period, and earnings still fell by about 4–5% a year on average in the four years after displacement.
- Source: OECD (2015), [Back to Work: Sweden](https://www.oecd.org/employment/back-to-work-sweden_9789264246812-en)

### Short-time work kept jobs through the COVID crisis

- Germany's Kurzarbeit kept an estimated 2.2 million jobs at the peak of the crisis in 2020, against about 330,000 in the 2009 financial crisis (IMK).
- Limits: it suits a dip that will pass. In 2026 the IAB warned that extending it during a structural crisis can delay changes companies need to make.
- Sources: [Hans-Böckler-Stiftung (2021)](https://www.boeckler.de/de/pressemitteilungen-2675-kurzarbeit-sicherte-2020-mehr-als-sechs-mal-so-viele-stellen-32716.htm); [IAB statement (2026)](https://doku.iab.de/stellungnahme/2026/sn0326.pdf)

### Worker voice doesn't cost what critics expect

- German firms required to give a third of board seats to worker representatives paid no higher wages, built 40–50% larger capital stocks and outsourced less.
- The OECD finds that AI adoption tends to bring better outcomes for workers when their representatives are consulted.
- Sources: [Jäger, Schoefer & Heining, "Labor in the Boardroom", NBER w26519](https://www.nber.org/papers/w26519), published in the *Quarterly Journal of Economics* (2021); [OECD Employment Outlook 2023, executive summary](https://read.oecd.org/10.1787/08785bba-en)

### Shorter hours and an inclusive working life

- Iceland's 2015–2019 trials cut the week to 35–36 hours without cutting pay for about 2,500 workers. Productivity and service stayed the same or improved in most workplaces and wellbeing rose. Limits: mostly public sector, partly self-reported, and the work itself was redesigned.
- In Norway, people working in companies that signed the inclusive working life agreement were more likely to stay in work after long-term sick leave.
- Sources: [Autonomy and Alda, "Going Public" (2021)](https://autonomy.work/portfolio/icelandsww/); [Scand J Work Environ Health 2023](https://pubmed.ncbi.nlm.nih.gov/37548319/)
<!-- /shared:european-social-practice -->

<!-- shared:voice-and-fair-process -->
## Voice, fair process and leadership

Details and how to apply them: [good-leadership.md](good-leadership.md).

### Fair process makes hard decisions acceptable

- Kim and Mauborgne describe three elements: engage people in decisions that affect them, explain the thinking behind the final decision, and make expectations clear. Explanation lets people trust leaders' intentions even when their own ideas were rejected.
- Source: W. Chan Kim and Renée Mauborgne, "Fair Process: Managing in the Knowledge Economy", *Harvard Business Review*, July–August 1997

### Leaders decide whether people speak up

- Managerial openness predicted employees' improvement-oriented voice, through their sense of psychological safety, and leaders' behaviour mattered most for the best performers.
- A meta-analysis of 136 samples (over 22,000 people and nearly 5,000 groups) linked psychological safety to information sharing, learning, performance and satisfaction. Most studies were cross-sectional, so read it as association, not proof of cause.
- Managers rated employees who voiced challenge as weaker performers than those who voiced support. If challenge is punished, it stops.
- Sources: [Detert & Burris, *Academy of Management Journal* (2007)](https://doi.org/10.5465/amj.2007.26279183); [Frazier et al., *Personnel Psychology* (2017)](https://digitalcommons.odu.edu/management_fac_pubs/13/); [Burris, *Academy of Management Journal* (2012)](https://instituteforpr.org/risks-rewards-speaking-managerial-responses-employee-voice)

### Culture predicts delivery

- DORA's research finds that a high-trust, generative culture, in which information flows freely, predicts software delivery and organisational performance. In the 2023 report, teams with generative cultures had 30% higher organisational performance.
- Source: [DORA, generative organizational culture](https://dora.dev/capabilities/generative-organizational-culture/); [DORA 2023 report](https://dora.dev/dora-report-2023/)
<!-- /shared:voice-and-fair-process -->

## People and shareholder returns move together

Use this when someone argues that caring for people comes at the shareholders' expense.

- **Employee satisfaction and stock returns.** A portfolio of Fortune's "100 Best Companies to Work For in America" earned a risk-adjusted (four-factor) return of 3.5% a year from 1984 to 2009, and beat industry benchmarks by 2.1% a year. These companies also had more positive earnings surprises. Source: Edmans, "Does the stock market fully value intangibles? Employee satisfaction and equity prices", *Journal of Financial Economics* (2011), [abstract](https://repository.upenn.edu/fnce_papers/373).
- **Workplace wellbeing and firm performance.** Using over 15 million employee wellbeing ratings on Indeed for more than 1,600 US listed companies, Oxford researchers found higher wellbeing went with higher firm value, return on assets and profits. A simulated portfolio of the 100 companies with the highest wellbeing, bought on 1 January 2021, returned 20% more than the S&P 500 over two years. Source: De Neve, Kaats & Ward, Wellbeing Research Centre working paper 2304, [summary (June 2023)](https://wellbeing.hmc.ox.ac.uk/news/stock-market-performance/).
- **Engagement and business outcomes.** Gallup's 11th Q12 meta-analysis (2024) covers 183,806 business units with 3.35 million employees in 347 organisations. Units in the top quartile for engagement had 23% higher profitability than the bottom quartile, 18% higher sales productivity, 78% less absenteeism, 63% fewer safety incidents and 32% fewer quality defects. Source: [Gallup](https://www.gallup.com/workplace/321725/gallup-q12-meta-analysis.aspx).
- **Caveats to state when you cite these.** They are correlations; successful companies may also find it easier to keep people happy. The Oxford study used Indeed's data, and Gallup sells the survey it studies. Across 14 countries, the stock-return premium was larger where labour markets are flexible and smaller or absent where employment protection is strong, as in Germany, because regulation already guarantees a baseline. Source: Edmans, Li & Zhang, [VoxEU summary](https://cepr.org/voxeu/columns/employee-satisfaction-and-firm-value-global-perspective).
- **How to phrase the conclusion.** Not "treat people well and the share price rises by X%", but: across decades of data there is no sign that treating people well costs shareholders, and many signs that it pays.

<!-- shared:shortcuts-and-decision-quality -->
## Shortcuts and decision quality

Use this when a leader wants the quick, big win, or to show why a short pause to think pays off. `coaching-leaders.md` says how to use it in a conversation.

### The pressure is real

- In a survey of 401 senior US financial executives, 78% said they would give up economic value in exchange for smooth earnings. Many said they would cut discretionary spending, such as R&D, advertising and maintenance, or delay a valuable project to hit an earnings target. Source: Graham, Harvey & Rajgopal, "The economic implications of corporate financial reporting", *Journal of Accounting and Economics* (2005), [NBER working paper](https://www.nber.org/papers/w10550)
- In a 2016 McKinsey survey of over 1,000 executives and directors for FCLT Global, 87% felt the most pressure to demonstrate strong financial results within two years or less, up from 79% in 2013. Source: [FCLT Global, "Rising to the challenge of short-termism" (2016)](https://www.fcltglobal.org/resource/rising-to-the-challenge-of-short-termism/)

### How good decisions are made

- **Process beats extra analysis.** Lovallo and Sibony studied 1,048 major decisions over five years, including new products, M&A and large capital spending. The quality of the decision process mattered more than the quality of the analysis, by a factor of six. A good process meant real debate, explicit uncertainty and dissent. Source: [McKinsey Quarterly, "The case for behavioral strategy" (March 2010)](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-case-for-behavioral-strategy)
- **Rushing to the first remedy fails.** Paul Nutt's multi-decade research on real organisational decisions found that about half failed. Managers often latched onto the first remedy they came across. Source: [Ohio State University](https://news.osu.edu/half-of-business-decisions-fail-because-of-managements-blunders-new-study-finds/)
- **One option is not a choice.** In one study of 168 decisions, only 29% of teams considered more than one alternative. "Whether or not" decisions failed 52% of the time over the long term, against 32% for decisions with two or more alternatives. Source: Nutt, as reported in Chip and Dan Heath, *Decisive* (2013)
- **One-way and two-way doors.** In Amazon's 2015 letter to shareholders, Jeff Bezos split decisions into Type 1 (consequential and irreversible, to be made carefully) and Type 2 (reversible, to be made quickly by small groups). He warned that large organisations tend to use the heavy Type 1 process for everything. Source: [Business Insider summary of the letter (April 2016)](https://www.businessinsider.in/jeff-bezos-there-are-two-types-of-decisions-to-make-and-dont-confuse-them/articleshow/51706758.cms)
- **Think slow, act fast.** Flyvbjerg's database of more than 16,000 big projects shows 8.5% delivered on budget and on time, and only 0.5% did so and also delivered the promised benefits. Successful projects planned thoroughly, then delivered quickly. Source: Flyvbjerg & Gardner, *How Big Things Get Done* (2023), [review in The Independent Review](https://www.independent.org/tir/2023-fall/how-big-things-get-done/)
- **Pre-mortems surface risks.** Gary Klein's pre-mortem asks a team to assume the plan has failed and explain why. It builds on research showing that imagining an outcome has already happened increased the number of reasons people found by about 30%. Limits: the study counted reasons, not their accuracy. Source: Klein, "Performing a project premortem", *Harvard Business Review* (September 2007); [summary of the evidence](https://resources.rework.com/libraries/project-management/pre-mortem)
- **Bad news must be safe to bring.**
  - Amy Edmondson (1999) defined psychological safety as the belief that a team member won't be punished or humiliated for speaking up with ideas, questions, concerns or mistakes.
  - Google's Project Aristotle compared 180 teams and found it the most important of five dynamics of effective teams.
  - Source: [InfoQ on Google's findings (2016)](https://www.infoq.com/news/2016/10/google-perfect-team)

### Base rates for AI bets

- **Most AI pilots don't move the P&L yet.** MIT NANDA's "The GenAI Divide: State of AI in Business 2025" reported that about 95% of enterprise generative AI pilots showed no measurable P&L impact. It was based on 52 interviews, 153 survey responses and a review of 300+ public AI initiatives. Limits: the method has been criticised, so treat it as a direction, not a precise rate. Source: [The Register (August 2025)](https://www.theregister.com/2025/08/18/generative_ai_zero_return_95_percent)
- **Agentic AI projects get cancelled.** Gartner predicts that over 40% of agentic AI projects will be cancelled by the end of 2027 due to escalating costs, unclear business value or inadequate risk controls. Source: [Gartner (June 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- **Regretted AI layoffs:** see "Companies that cut jobs for AI often regret it" above.

### AI tends to agree with the person asking

- Anthropic researchers found that AI assistants consistently show sycophancy: they match the user's stated beliefs over truthful answers, partly because people rate agreeable answers more highly. A leader who asks an AI to confirm a shortcut is likely to get confirmation. Source: [Sharma et al., "Towards Understanding Sycophancy in Language Models" (Anthropic, 2023)](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)
<!-- /shared:shortcuts-and-decision-quality -->

## How to use this file

- Cite a case only where it fits the situation, and say how this company differs.
- Don't overstate. One company's success is an example, not a law.
- Add the company's own history: earlier launches and their adoption, migrations, rewrites, outsourcing deals and reorganisations, their real cost and what people remember about them. That is often the most persuasive evidence of all.
