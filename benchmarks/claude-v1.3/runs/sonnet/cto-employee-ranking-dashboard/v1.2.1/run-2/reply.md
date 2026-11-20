You can push back without being difficult, because your strongest argument is also the VP's own interest: a weekly ranking on Copilot acceptance rate and PRs merged will damage the thing he wants to improve, and in the Netherlands he probably can't switch it on without your works council. Don't open with "this is wrong". Open with a question and a better proposal. Here is how.

**Why the metrics fail (facts you can hand him)**

- **Both numbers measure activity, not value.** Acceptance rate measures how much of a suggestion someone keeps, not whether the code was good. It can rise while quality falls. PRs merged rewards small, frequent changes and punishes the people who review, mentor, fix incidents and delete code. AI also makes PR volume cheap.
- **The cost moves to review.** Faros AI telemetry from 10,000+ developers (2025) found that on high-AI-adoption teams, PRs merged rose 98% but review time rose 91% and PRs grew 154% larger. (Faros sells engineering analytics, so treat it as one data point, not gospel.) Rank on PRs and you reward exactly that pattern.
- **Weekly is mostly noise.** Weekly counts swing with sprint phase, on-call, holidays, and whether you work on a legacy service or a greenfield one. If the bottom 10% is picked weekly and it is largely random, about 65% of engineers land in it at least once in 10 weeks (1 - 0.9^10). That is my arithmetic on a simplifying assumption, but the point holds: a rolling ranking will hit people who did nothing wrong.
- **People will optimise the number.** Once a number decides who gets an improvement plan, engineers accept every suggestion and split every PR in two. You lose the signal and the quality.
- **Seniors take the hit first.** Review, design help and incident work do not show up in either metric. The people holding the system together will look weakest.

**Two Dutch-specific points (not legal advice; check with HR or counsel)**

- At 300 people you must have a works council (ondernemingsraad; mandatory from 50 employees). It has a consent right (instemmingsrecht, art. 27(1)(l) WOR) on systems suited to monitoring or evaluating employees' behaviour or performance. A per-person weekly dashboard of Copilot and PR data is a clear candidate. If it was rolled out without their agreement, that is a procedural problem independent of whether you like the metric.
- Personal data used for performance management also falls under the GDPR (purpose, proportionality, transparency). And Copilot's admin consoles often show per-person usage by default, so it is worth asking who can see what.

This gives you a way to object that is not "I disagree with you". It is "has the OR been involved? I'd hate for this to be challenged later."

**What you can actually do, in order**

1. **Ask questions privately first, not in a meeting.** A precise question lands better than a confident objection. Ask the VP: What problem is this solving (delivery speed, quality, cost, a specific team)? What would you expect to see change in three months? What happens to someone flagged who is doing review and incident work? Assume he is under pressure from above, not acting in bad faith, and let him save face.
2. **Come with an alternative, not only a no.** Offer something that answers his real need, which is probably "how do I know engineering is delivering and where is it stuck?":
   - Team-level DORA metrics (lead time, deployment frequency, change failure rate, recovery time), each paired with a quality measure
   - Where work gets stuck: review wait time, work in progress, unplanned work
   - A short developer-experience survey
   - For Copilot specifically: delivery and quality before and after, with a comparison group, not per-person acceptance rates
   Offer to set up a baseline from data you already have, as a small pilot. That makes you the person solving his problem, not blocking it.
3. **If he does have concerns about specific people, route them properly.** Individual performance is a manager conversation: clear expectations, feedback, support, a fair chance, with HR involved. Evidence comes from the work and from peers, not from a dashboard. You can say this without defending weak performers.
4. **Find allies with a stake.** Other engineering managers, HR (an automated bottom-10% rule creates real legal and attrition risk for them), and the works council. Ask the OR whether they have been consulted; you don't need to lead any fight yourself.
5. **Put your points in writing, short and factual.** One page: the problem as you understand it, the evidence above, your alternative, and what would change your mind. Neutral language, no motives, no adjectives. Keep it to what you can show.
6. **Know your limits.** You are not obliged to risk your career. If the VP hears you out and goes ahead anyway, the works council route and HR are the legitimate next channels, in proportion. Keep a factual record of what you asked and what the answers were. If it comes to anything serious, get independent advice (a union, or an employment lawyer) before escalating.

**A message you could send**

> Hi [name], I'd like to make the weekly engineering view as useful as possible for you. Before it goes live, could we talk about what decision it should drive? I have two concerns: acceptance rate and PRs merged tend to reward volume over quality (review load goes up sharply on teams that chase PR counts), and I'd want to check that the works council has been involved, as per-person performance data usually needs their agreement. I can pull together a team-level view of lead time, review wait and change failure rate from data we already have, and we could compare it to what the ranking would show. Would 30 minutes this week work?

**My assumptions, and what would change my mind:** I'm assuming the real aim is delivery and quality, not cost-cutting disguised as performance management, and that you have no existing agreement with the OR on this. If the VP has data showing a few engineers are clear outliers on several measures including quality, a manager-led, fair process for those individuals is a different conversation from a ranking. What am I missing, and what would make this wrong? In particular: is there an OR here, and what is the VP actually trying to fix?
