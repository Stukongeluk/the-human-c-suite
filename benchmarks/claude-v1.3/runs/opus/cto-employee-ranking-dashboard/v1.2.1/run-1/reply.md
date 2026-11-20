You can push back without being "the difficult one". Don't argue against the VP. Offer him a better way to get what he's after, and let the formal process carry the part that would otherwise make you the bad guy. Two facts do most of the work:

- **At 300 people your company must have a works council, and a per-person performance ranking needs its consent.** Article 27(1)(l) WOR covers systems that can monitor employees' behaviour or performance. If the company rolls one out without consent, the works council can declare the decision void within a month ([Rendement](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/or-kan-besluit-van-bestuurder-nietig-verklaren.html)).
- **A bottom-10% rule puts people on plans every week, however good the team is.** It's a relative cut, so someone is always at the bottom. As an illustration (not your data): if weekly rank were mostly noise, about 3 in 4 engineers would land in the bottom 10% at least once in a quarter (1 − 0.9¹³ ≈ 75%).

## Why the metrics themselves fail

Keep this ready, but lead with the alternative, not the critique.

- **Copilot acceptance rate measures tool use, not value.** GitHub's own study found it predicts how productive developers *feel*, not what they deliver ([Ziegler et al., 2022](https://arxiv.org/abs/2205.06537)). Seniors who reject bad suggestions score low, and so does anyone working in a language or codebase where Copilot is weak. It's easy to game: accept everything, then delete it.
- **PRs merged rewards splitting work** and punishes the people who review, mentor, handle incidents, delete code or work part-time. In Faros AI's 2025 data, high-AI-adoption teams merged 98% more PRs while review time rose 91%. The count goes up and the queue gets worse. (Faros sells analytics, so treat that as a signal, not proof.)
- **Once a number decides who goes on a plan, people optimise the number.** Reviews get slower, nobody picks up the ugly legacy ticket, and helping a colleague costs you rank.

## What you can actually do, in order

1. **Ask what problem it solves, in private first.** Go through your manager or straight to the VP: "Is this about whether Copilot is paying off, delivery speed, or specific performance concerns?" Each has a better answer. Assume pressure before bad intent: a new VP has to show grip, and the Copilot bill may be what's behind this.
2. **Offer an alternative and offer to build it.** Suggest a 6–8 week pilot of a team-level dashboard. Track DORA metrics (lead time, deploy frequency, change failure rate, recovery time), review wait time and PR size, plus Copilot adoption per team, each team compared with its own baseline. That answers "is Copilot paying off?" far better than a leaderboard. Real individual concerns stay with managers: clear expectations, feedback, support, and evidence from the work and from peers. Offering to build it is the opposite of being difficult.
3. **Raise the process as a risk to his plan, not as a threat.**
   - The works council consent above.
   - A DPIA: the Dutch DPA lists systematic monitoring of employees' activities as processing that requires one ([list, entry 11](https://www.dirkzwager.nl/kennis/artikelen/definitieve-nederlandse-lijst-verwerkingen-waarbij-dpia-gegevensbeschermingseffectbeoordeling-verplicht-is-gepubliceerd)).
   - The plans themselves: in the Netherlands an improvement plan is the run-up to dismissal for unsuitability, and it has to rest on concrete shortcomings in the work. A ranking position is unlikely to hold up.
   - Suggest checking with HR and the privacy officer before launch. You're protecting him from a public rollback. (This is not legal advice; HR or counsel should confirm the details.)
4. **Don't stand alone.** One person objecting is "difficult"; five seniors and engineering managers proposing an alternative is feedback. HR and the privacy officer are natural allies. You can also ask a works council member a question in confidence. Checking monitoring tools is their job, and they'll see this anyway when consent is needed. The Dutch habit at its best: agree on monitoring tools with the people they measure before rollout, not after.
5. **Put it in writing, neutrally,** after you've talked (draft below). Keep your own short, factual notes of what was asked and answered.
6. **What not to do:** don't pull colleagues' individual data to prove your point, don't game the metrics in protest, and don't vent about it in Slack.

**The honest part:** there is some risk with a new VP. You keep it low by going private first, asking questions instead of giving verdicts, and showing up with a plan. If he goes ahead without works council consent, the works council deals with it, and you're no longer the person standing in the way. How far you push is your call; you don't owe anyone a career sacrifice.

## Draft message to the VP

> Hi [name], thanks for taking the time to talk about the engineering dashboard. I'd like it to work, so here are two risks and an offer.
>
> Risks: a per-person performance ranking needs works council consent and probably a DPIA before rollout, and I'd hate to see it stopped after launch. Acceptance rate and PR counts also reward volume over impact, which can push review times up.
>
> Offer: I'm happy to help set up a 6–8 week pilot with team-level delivery metrics (DORA, review wait time) and Copilot adoption per team against each team's baseline. That would show whether Copilot is paying off and where we're slow. Could we check it with HR and the privacy officer first?

What am I missing? For example, is this coming from the CEO, or does the company already have a works council agreement on engineering metrics?
