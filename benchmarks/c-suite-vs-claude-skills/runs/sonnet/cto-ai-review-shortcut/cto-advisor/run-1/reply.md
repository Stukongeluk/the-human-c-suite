**Bottom Line:** Half of it is good. Roll out AI coding agents to everyone, but don't drop code review for small changes. Make review faster and tier it by risk instead.

**What**

- **AI agents for all engineers from January: yes, with a short pilot first.** (Confidence: medium) Give each team a few weeks to set conventions: which tasks suit agents, how to prompt, and what context to supply. Track the results from day one.
- **No review for "small" changes: no.** (Confidence: medium) Agents raise the number of changes and make it easy to produce plausible-looking code nobody fully understands. Review is the main check on that, so removing it hits exactly where the risk grows.

**Why**

- "Small" is a poor test. Small diffs cause outages (a config flag, an auth check, a query change). Diff size says little about blast radius. (Confidence: high)
- The real bottleneck is usually review wait time, not review itself. Fix the queue and you get the speed-up without removing the safety check. (Confidence: medium, check against your own PR cycle-time data)
- Review is also how juniors learn and how the team keeps shared ownership of the code. Dropping it while adopting agents weakens both. (Confidence: medium)
- I have no data from your systems here, so the speed gain and the failure risk are both assumed, not measured. (Confidence: low)

**How to Act**

1. **Tier review by risk, not size.** Auto-merge with green CI only for low-risk classes: docs, tests, formatting, dependency bumps. Everything touching auth, payments, data, infra or config needs a human reviewer.
2. **Speed up the rest.** Use an AI first-pass review, small PRs, and a review SLA (for example, first response within 4 working hours).
3. **Keep the agent's author accountable.** The engineer who merges agent code owns it and must be able to explain it.
4. **Audit.** Sample the no-review merges weekly for the first quarter.
5. **Measure before and after.** Track lead time for changes, deployment frequency, change failure rate and time to recovery. Set a stop rule up front: if change failure rate rises meaningfully for two consecutive weeks, tighten review again.

**Your Decision**

Approve the January rollout with the pilot and metrics. Replace "drop review for small changes" with risk-tiered review plus an SLA. If you still want to skip review for some classes, name them and set the rollback trigger first. Tell me your current PR review wait time and change failure rate and I can size the gain.
