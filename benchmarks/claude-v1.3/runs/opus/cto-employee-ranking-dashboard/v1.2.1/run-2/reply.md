You can push back on this without being the difficult one. Don't argue against measuring. Offer your VP a better way to get what they want, and ask the process questions a 300-person Dutch company has to answer before a system like this goes live anyway. The core problem fits in one number: a forced bottom 10% always has people in it, however well everyone works. If weekly ranks are mostly noise, about 72% of engineers land in the bottom 10% at least once in 12 weeks (1 − 0.9¹²).

**The arguments, if you need them**

- Both numbers measure activity, not value. Acceptance rate goes up if you accept everything and fix it later, and down for people who read suggestions carefully. PR counts punish whoever spent the week reviewing, mentoring, on call or on one hard migration, and reward splitting work into small pieces.
- Together they reward the pattern that costs teams most with AI tools. On high-adoption teams, Faros AI saw 98% more merged PRs, but PRs were 154% larger and review time rose 91% ([2025](https://www.faros.ai/blog/ai-productivity-paradox-report-2025); Faros sells analytics). Uplevel found no faster cycle time with Copilot and 41% more bugs ([2024](https://cio.com/article/3540579/devs-gaining-little-if-anything-from-ai-coding-assistants.html)).
- Weekly is noise. A holiday, an on-call week or onboarding a new colleague puts someone at the bottom.
- The fair steelman: acceptance rate isn't a random choice. GitHub's own research found it the best predictor of how productive developers *feel* ([Ziegler et al., 2022](https://arxiv.org/abs/2205.06537)). But feeling faster isn't being faster: in [METR's 2025 trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), experienced developers took 19% longer with AI tools while believing they'd been faster.

**What you can do, lowest risk first**

1. **Ask about the goal, in private.** "What should this solve: delivery speed, showing the board what Copilot is worth, or concerns about specific people?" New VPs are often under pressure to show AI results fast, so assume pressure before anything else. Each of those goals has a better tool than a ranking.
2. **Offer the alternative, and the work.** A team-level view: lead time, deployment frequency, change fail rate and recovery time (the DORA metrics), plus review wait time and PR size. For Copilot: team metrics before and after rollout, active seats against seats paid, and a short developer survey. Offer to pilot it with two or three teams for six weeks. Volunteering to build the better version is the opposite of being difficult. I've drafted a one-page proposal you can adapt: `team-metrics-proposal.md`.
3. **Ask the process questions, framed as protecting the launch.**
   - Works council: a company your size must have one (it's mandatory from 50 employees). A system suited to monitoring performance needs its consent under article 27(1)(l) WOR. Without consent, the works council can have the decision declared void, and employees then don't have to follow it ([Rendement](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/or-kan-besluit-van-bestuurder-nietig-verklaren.html)).
   - Privacy: the Autoriteit Persoonsgegevens lists systematic monitoring of employees' activities as processing that needs a DPIA ([Staatscourant 2019, 64418](https://zoek.officielebekendmakingen.nl/stcrt-2019-64418.pdf)). Has the privacy officer seen this?
   - HR: in Dutch law, a dismissal for poor performance needs concrete, job-related shortcomings and a real chance to improve, which is what an improvement plan is for. A relative weekly rank shows neither, and HR will probably say so.

   "Have we checked this with...?" is what careful people ask. It isn't opposition.
4. **Bring in the people with a stake.** Engineering managers would have to run these improvement plans, and staff engineers and HR will have views. A proposal from several people reads as input rather than one person resisting. Keep it a proposal, not a campaign against the VP.
5. **Talk first, then put it in writing, briefly.** There's a draft below.
6. **If it goes ahead anyway,** the works council is the formal route, and you can talk to a member confidentially; that's what it's there for. The vertrouwenspersoon handles intimidation and integrity issues, not disagreements about metrics. Keep a short factual record of what you asked and when. Be honest with yourself about the risk, too: you don't owe anyone a fight that damages your career. Raising it once, well, with an alternative, is already a lot.

Meanwhile, keep reviewing and helping others. That work matters even when a dashboard can't see it.

**Draft message to your VP**

> Hi [name], thanks for sharing the plan for the weekly engineering dashboard. I'd like better visibility on delivery and on what Copilot gives us too, and I'm happy to help build it. Before it goes live, I have three questions. What's the main problem we're solving: delivery speed, Copilot's value, or specific performance concerns? Has it been past the works council and our privacy officer, since individual performance monitoring needs works council consent and probably a DPIA? And would you be open to a six-week pilot with team-level metrics first? I've put a one-page proposal together. Could we take 30 minutes this week?

This isn't legal advice. Check the legal points with HR or an employment lawyer before you lean on them.

One question for you: do you know what's driving this? A board question about Copilot spend, or worries about particular people? The answer decides which alternative to lead with.
