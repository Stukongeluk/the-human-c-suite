## CTO view: a weekly engineer ranking by Copilot acceptance rate and PRs merged

### Bottom line

You're right that this is the wrong design. You can say so without becoming "the difficult one". Raise it with the VP privately, before the first ranking goes out. Frame it as protecting their goal, bring an alternative that's ready to use, and let the company's own checks (works council, privacy officer, HR) do the blocking, so you don't have to.
**Confidence:** high on the metrics problem. Medium on exactly how Dutch law applies to this particular dashboard.

*Tags: [verified] = checked against a source listed below; [medium] = a reasonable inference; [assumed] = not checked.*

### What

- **Copilot acceptance rate measures the tool, not the engineer.** [verified] GitHub defines it as how often developers accept Copilot's suggestions, a sign that the suggestions are "relevant and useful". GitHub also says to look for patterns "rather than focusing on any single number". In GitHub's own research, junior developers accepted more suggestions, and acceptance rate predicted *self-reported* productivity, not measured output. Rank people on it and a senior who rejects a bad suggestion scores lower than someone who accepts it.
- **PRs merged per person counts activity, and it's easy to game.** [verified] The authors of SPACE, a productivity framework from GitHub and Microsoft Research co-written by DORA's Nicole Forsgren, write that activity metrics like PR counts "should never be used in isolation either to reward or to penalize developers". [medium] Once there's a weekly ranking, expect more, smaller PRs and fewer code reviews. The people who review, mentor, do on-call or take the hard problems will sink in the ranking.
- **A fixed bottom 10% puts people on plans whether or not anyone is underperforming.** [verified, but the evidence is a simulation] The best-known study of forced ranking simulated firing the lowest-rated staff. Gains were about 16% a year for the first two years, fell to about 1% by year ten, and stopped after about year 20. The study did not measure the effects on morale and retention.
- **In the Netherlands, this probably can't just be switched on.** [verified rules; medium on how they apply here] A company of 300 people must have a works council (OR, *ondernemingsraad*). Under article 27 of the Works Councils Act (WOR), the OR has a consent right over staff-assessment systems, over how employees' personal data is processed, and over systems that can monitor performance. A decision taken without that consent is void if the OR invokes this within a month. The Dutch privacy regulator (AP) lists systematic monitoring of employees as needing a DPIA, a formal privacy risk assessment. If the ranking in effect decides who goes on a plan, GDPR article 22 may also apply. That article covers decisions made solely by automated processing, and the EU Court of Justice ruled in the SCHUFA case that a score can count as such a decision when it largely determines the outcome.
- **Plans based on rank are weak exactly where plans matter most.** [verified rules; medium on outcome] To dismiss someone in the Netherlands for underperforming, the employer must have told them in time and given them a real chance to improve, and the problem must not come from the employer failing to provide training. Judges also want a clearly backed-up need for improvement and concrete, achievable goals. "Bottom 10% on Copilot acceptance" meets neither test.

### Why this matters

The ranking will change behaviour faster than it measures anything. People will accept more suggestions and split their PRs, quality and reviewing will suffer, and the engineers who hold teams together will look worst and leave first. The VP also faces a likely clash with the OR and improvement plans that won't stand up legally. So raising this helps them; it doesn't block them.

### How to act

1. **Ask before you argue.** → You → this week, before the first ranking is published. Ask the VP for a 30-minute 1:1. Start with the goal, not the objection (see the script below).
2. **Bring the alternative and offer to build it.** → You → within a week of the 1:1. Measure at team level, not person level: Copilot adoption alongside the four DORA delivery metrics (deployment frequency, lead time for changes, change failure rate, time to restore service) and PR cycle time, tracked as trends from before the rollout to after. Individual performance stays with line managers, where a number can start a conversation but never decide one. `proposal-team-level-metrics.md` in this folder is written so you can send it as is or adapt it.
3. **Propose a test instead of a debate.** → The VP or engineering managers → before anyone is put on a plan. Take last quarter's data, list who would have landed in the bottom 10%, and ask each manager privately whether that matches who is actually struggling. If the list is full of reviewers, on-call people and seniors on hard problems, the metric fails by the VP's own standard. Let them run this. Don't pull your colleagues' individual data yourself.
4. **Raise the governance points as questions.** → You → in the same 1:1, then a short follow-up email. For example: "Has this been through HR, the privacy officer and the OR? I think it needs OR consent and a DPIA." That isn't being difficult. It saves the VP from a decision that could be void.
5. **Have a backstop with a date.** → You → if nothing has changed after about two weeks. Find two or three other seniors or engineering managers who share the concern, so it isn't only "your" issue. If the ranking still goes live with automatic plans, talk to an OR member. You can do that confidentially, and assessing schemes like this is exactly their job.

**What to say in the 1:1** (adapt to your own words):
> "I want the Copilot rollout to succeed, and I agree we need to see where delivery is getting stuck. What decision do you want this ranking to support: whether Copilot is paying off, or who needs help? I'm worried these two numbers will answer neither. People will learn to move them within a few weeks, and the reviewers and on-call people will end up at the bottom. Could we test it first against last quarter? And I've drafted a team-level version I'd be happy to build."

### Risks

- **Raising it in public.** Doing this in a group meeting or on Slack reads as challenging a new leader in public. Keep the first conversation private.
- **Your own number.** If you review and mentor a lot, you may rank low on PRs merged yourself. Raise it before the first ranking, and argue about the method rather than your own score, so it can't look self-serving.
- **Going to the OR.** It's a legitimate channel, but the VP may feel you went around them. Do it after the 1:1, not instead of it, unless plans are already being handed out.

### Your decision

- **Option A: a private 1:1 with the VP, with the alternative in hand.** Lowest risk and the best chance of changing the design. It costs you a few hours of preparation.
- **Option B: a joint note from several seniors or managers.** A stronger signal, but more confrontational for a new VP.
- **Option C: go straight to the OR.** The strongest lever, with the highest cost to your relationship with the VP. It's the right move if rankings and plans are already live.
- **Option D: go along with it.** No friction now. You pay later in gaming, people leaving, and possibly your own place in the bottom 10%.
- **Recommendation:** A this week, with C as the backstop if nothing changes.

**Assumptions:**
- [assumed] The ranking hasn't gone live yet and nobody has been put on a plan.
- [assumed] Your company has an OR. It's required from 50 employees, but not every company has actually set one up. The privacy and dismissal-law points apply either way.
- This isn't legal advice. How the WOR and GDPR apply to this exact dashboard is for your privacy officer, HR or an employment lawyer to judge. That's one more reason to raise it as a question rather than a claim.

**Detail:** `proposal-team-level-metrics.md`, a one-page proposal for the VP.

### Sources

- GitHub Docs, [About Copilot usage metrics](https://docs.github.com/en/copilot/concepts/copilot-usage-metrics/copilot-metrics) (definition of acceptance rate, "look for patterns")
- Ziegler et al. (GitHub), [Measuring GitHub Copilot's Impact on Productivity](https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity), CACM (acceptance rate vs self-reported productivity; juniors accept more)
- Forsgren et al., [The SPACE of Developer Productivity](https://queue.acm.org/detail.cfm?id=3454124), ACM Queue (activity metrics "should never be used in isolation")
- Scullen et al. forced-ranking simulation, summarised by [Newswise](https://www.newswise.com/articles/view/510197/?sc=bwtn)
- Rijksoverheid, [When is a works council mandatory?](https://www.rijksoverheid.nl/onderwerpen/ondernemingsraad/vraag-en-antwoord/wanneer-is-een-ondernemingsraad-or-verplicht) (50+ employees)
- Dirkzwager, [OR consent rights per the AP's privacy booklet for works councils](https://www.dirkzwager.nl/kennis/artikelen/instemmingsrecht-van-de-or-volgens-het-or-privacyboekje-van-de-ap) (personal data, monitoring systems, void within one month); Rendement, [OR consent on staff assessment](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/instemmingsrecht-or-beoordeling-en-beloning.html)
- Dirkzwager, [AP list of processing that requires a DPIA](https://www.dirkzwager.nl/kennis/artikelen/definitieve-nederlandse-lijst-verwerkingen-waarbij-dpia-gegevensbeschermingseffectbeoordeling-verplicht-is-gepubliceerd) (item 11, employee monitoring)
- CMS, [SCHUFA judgment and AI in HR](https://cms.law/en/deu/legal-updates/impact-of-the-cjeu-s-schufa-judgment-on-the-use-of-ai-in-hr)
- UWV, [Factsheet: dismissal for underperformance](https://www.uwv.nl/werkgevers/Images/factsheet-ontslag-bij-disfunctioneren.pdf); HR Praktijk, [What judges require of improvement plans](https://www.hrpraktijk.nl/juridisch/ontslag/rechters-maken-duidelijk-waaraan-verbetertrajecten-moeten-voldoen/)
