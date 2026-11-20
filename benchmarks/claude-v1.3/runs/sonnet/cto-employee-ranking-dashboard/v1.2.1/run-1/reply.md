You can disagree without being difficult: don't say "this is wrong", ask for the reasons in private, bring a better alternative, and make sure the works council knows. You are probably right on the substance, and at a 300-person Dutch company you also have a formal route that doesn't depend on you personally standing up to the VP.

**Why the ranking doesn't work (the facts you can use)**

- **Copilot acceptance rate measures tool usage, not value.** It can rise while quality falls. It also varies with language, codebase and task type, so it mostly shows what someone works on, not how well.
- **PRs merged punishes the people you most want to keep.** It undercounts reviewing, mentoring, incident work, and deleting or simplifying code. AI also makes PR volume cheap. In Faros AI telemetry from 10,000+ developers (2025), high-AI-adoption teams merged 98% more PRs, but review time rose 91% and PRs grew 154% larger. (Faros sells engineering analytics, so treat it as one data point.) If PR count drives rankings, people will split PRs and skip reviews.
- **"Bottom 10%" is a quota, not a finding.** Somebody is always in the bottom decile, even on a strong team. A weekly cadence makes it worse, because weekly numbers are mostly noise (holidays, on-call, a big refactor).
- **Once a number decides who gets a plan, people optimise the number.** You get gaming, less collaboration, and your best reviewers quietly leaving.

**The Dutch angle, which may be your strongest card**

With 300 employees you should have a works council (ondernemingsraad; mandatory from 50). Under article 27(1)(l) WOR, it has a consent right over systems suited to monitoring employees' behaviour or performance. A weekly per-person ranking built on Copilot and Git data plausibly falls under that, and it also raises GDPR questions (purpose, proportionality, transparency). I'm not a lawyer, and I don't know whether your company has a council or what the VP has already agreed with it. But "has this been through the OR?" is a neutral, process question, not an attack on the VP. Improvement plans based on these numbers could also be hard to defend as fair process in an employment dispute. Ask HR to check.

**What I'd do, in this order**

1. **Ask before you argue, in private.** Something like: "What problem are you trying to solve: delivery speed, quality, or specific people you're worried about? What would make you change the approach? What's already agreed with HR and the works council?" Often the VP has a real concern (slow delivery, an AI-spend question, pressure from above) and picked the first metric to hand. Understanding it lets you answer it.
2. **Offer an alternative that serves the same goal.** A VP who wants visibility needs something better than "no". For example:
   - team-level delivery and health metrics: DORA (lead time, deploy frequency, change fail rate, recovery time), review wait time, work in progress, unplanned work share
   - a short developer experience survey
   - Copilot measured as a pilot, team against comparable team, on delivery and quality, not per person
   - for a real performance concern about one person: the manager handles it with clear expectations, feedback and peer input, with HR, using evidence from the work
3. **Put it in writing, briefly.** A short note: the goal as you understand it, two or three risks of the current plan with sources, your proposal, and an offer to pilot it for six weeks. Pitch it as "here's how we get what you want without the risks", not "you're wrong".
4. **Find allies with a stake.** A couple of other senior engineers and engineering managers, HR, and the works council members. You don't need to lead a revolt; if several people ask the same neutral questions, it reads as due diligence, not as you being difficult.
5. **Raise the works council question** if nobody else does, ideally by asking the VP or HR first ("have we taken this to the OR?") before going to the council directly.

**Realistic expectations**

- Don't refuse to participate and don't sabotage the data. Disagreeing openly through proper channels is normal in Dutch workplaces; doing it with evidence and an alternative is what keeps you from being seen as difficult.
- If the VP dismisses all of it and plans start going to people on these numbers, escalate in proportion: your own manager or skip-level, HR, then the works council or a union. Keep a factual record of what you asked and what was said. Get independent legal advice (a union or an employment lawyer) before anything external. If real attempts change nothing, it is legitimate to decide whether you want to work there. That's your call, and your personal risk is real.

**Assumptions:** I haven't seen your data or know your VP, and I'm assuming the ranking is per person and tied to plans, as you describe. If it turns out to be team-level or only advisory, most of this softens.

What am I missing, and what would make this wrong? In particular: what does your VP say is the underlying problem, and is there a works council in place?
