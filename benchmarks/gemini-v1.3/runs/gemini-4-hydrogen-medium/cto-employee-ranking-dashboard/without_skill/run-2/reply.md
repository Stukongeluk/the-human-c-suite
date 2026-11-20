You’re right to be concerned—this is a classic trap, and pushing back poorly can easily get you labeled as "anti-metrics" or "defensive." The trick is to avoid arguing about whether engineers *should* be accountable, and instead help the new VP avoid stepping on predictable operational and legal landmines.

Here is a practical playbook for how to handle this without painting a target on your back.

---

### 1. Reframe from "This is unfair" to "This will break delivery"
New VPs usually introduce metrics like this because they want visibility, want to prove ROI on AI tools, or want to look decisive early on. If you argue that it’s "demoralizing," you sound protective. If you argue that it **creates perverse incentives that hurt the business**, you sound like a senior leader thinking about outcomes.

Keep your critique focused on second-order effects:
* **PRs merged:** Rewards splitting trivial changes into multiple PRs and punishes the exact work a 300-person org actually needs—code reviews, incident response, architecture, mentoring, and debugging hard problems. Nobody will review someone else's PR if it takes time away from merging their own.
* **Copilot acceptance rate:** Measures how often someone hits `Tab`, not how good their code is. It penalizes engineers who reject subtle bugs, security issues, or hallucinated APIs, and it’s trivial to game (accept a suggestion, then delete/rewrite it).
* **Weekly cadence + bottom 10% PIP:** Normal week-to-week variance (on-call, design docs, a tricky production bug, PTO) will put strong engineers in the bottom 10%. Putting people on PIPs based on weekly noise will cause your best engineers—the ones with options—to leave first.

---

### 2. Use the Dutch context as a constructive "heads-up"
Because you’re in a 300-person company in Rotterdam, there is a very practical reality the new VP (especially if they’re from the US or UK) may not realize: **this likely isn't even legally straightforward to roll out.**

* **Ondernemingsraad (OR):** Under Dutch law (WOR, Article 27), introducing a system to monitor or evaluate individual employee performance (*personeelsvolgsysteem* / *personeelsbeoordeling*) generally requires formal consent (*instemmingsrecht*) from the Works Council. At 300 employees, your company should have one.
* **Dutch dismissal/PIP rules & AVG (GDPR):** Putting someone on an improvement plan (*verbetertraject*) in the Netherlands requires a well-founded, fair, individual dossier—not an arbitrary bottom-10% quota based on automated tool telemetry.

**How to bring this up without sounding threatening:** Don't say *"This is illegal."* Say:
> *"One thing worth flagging early before we invest time building this: in the Netherlands, tying individual tool metrics to PIPs usually triggers OR consent and HR/AVG requirements. Might be worth a quick check with People Ops so we don't build something that gets blocked later."*

Framing it as saving them from an embarrassing collision with HR/OR puts you on their side.

---

### 3. Don't fight it alone—and don't fight it in public
* **Avoid the public Slack/all-hands debate.** Calling it out in front of 300 people forces the VP to defend their authority.
* **Start with your Engineering Manager (EM) or Director.** EMs are the ones who would actually have to execute these weekly PIPs. Most good EMs will hate this just as much as you do, and they have a much cleaner channel to push back upward as a group.
* **Talk 1:1 with a few trusted Staff/Senior peers.** You want a calm, aligned message going up through multiple managers rather than one senior engineer complaining.

---

### 4. Offer a "Yes, and..." alternative
Executives hate hearing "no" without an alternative. If you understand what the VP actually wants (visibility into bottlenecks, AI ROI, and catching genuine underperformance), give them a better way to get it:

* **For delivery visibility:** Suggest **team-level** flow metrics (PR review turnaround time, cycle time, deployment frequency, change failure rate) rather than individual counts. That exposes real bottlenecks without pitting teammates against each other.
* **For Copilot ROI:** Suggest **aggregated, anonymous** adoption and sentiment (e.g., team-level usage trends + a quarterly survey on where Copilot helps or hurts) instead of individual acceptance rates.
* **For underperformance:** Suggest aligning on clear **role expectations per level** and reviewing them in regular manager calibration—not a weekly leaderboard.

---

### 5. Protect yourself and your team in the meantime
While this plays out:
* **Make "glue work" visible.** If you spend a week on an RFC, an incident, or unblocking three teammates, leave a short paper trail (e.g., brief weekly notes to your EM or in your team channel) so your impact isn't invisible if someone pulls a GitHub report.
* **Watch how the VP responds.** If they listen to well-reasoned feedback from EMs, seniors, and HR and pivot, great—you’ve built credibility. If they double down on weekly stack-ranking and PIP quotas anyway, treat that as clear data about what the next year will look like there, and update your CV accordingly.
