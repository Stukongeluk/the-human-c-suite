Don’t fight this by arguing “metrics are bad”—redirect it to team delivery metrics and quietly flag the Dutch works council requirement, because individual activity rankings reliably break code review: Faros AI’s 2025 telemetry across 10,000+ developers found high-AI teams merged 98% more PRs while PRs grew 154% larger and review time jumped 91%, and Uplevel (2024, ~800 developers) saw no throughput gain with Copilot alongside 41% more bugs.

Your VP probably wants two reasonable things: to know whether delivery is healthy and whether the Copilot spend is paying off. Help them get that without ranking people.

### What to do next

1. **Start with your manager, not a public stand-off.** Keep it neutral and focused on the system, not the VP’s motives. Show what PR-count and acceptance-rate rankings do in practice: they penalise people who review code, mentor, fix incidents, or delete dead code, and invite engineers to split trivial PRs and accept noisy suggestions.
2. **Offer a concrete team-level alternative.** Propose measuring **teams** on a rolling baseline using DORA and flow metrics: change lead time, deployment frequency, change fail rate, deployment rework rate, review wait time, and PR size—plus aggregated developer-experience feedback. If there’s a real concern about an individual, managers should handle it through expectations, code-review evidence, and coaching, not a weekly leaderboard.
3. **Flag the works council (OR) and compliance risk—as protection, not rebellion.** In a 300-person Dutch company, an *ondernemingsraad* is mandatory. Under **Article 27(1)(l) of the Works Councils Act (WOR)**, systems suited to monitoring employee behaviour or performance—including per-person Copilot and Git analytics used for PIPs—generally require **prior OR consent** (*instemmingsrecht*). (The EU AI Act’s worker-notification duty for high-risk evaluation systems starts on 2 December 2027, but Dutch WOR consent applies now. This isn’t legal advice—suggest HR and counsel check before anything goes live.) If your manager won’t escalate, you can raise it quietly with HR, the OR, or your *vertrouwenspersoon*, using only records you’re allowed to keep.

### A line you can use
> “I want us to see whether Copilot is actually speeding up delivery, too. If we rank individuals on acceptance rate and PRs merged, people will split PRs and accept boilerplate, which clogs code review. Can we track team lead time, review wait time, and rework rate instead—and check with HR and the OR before turning on individual monitoring?”

I’ve saved a neutral, ready-to-share draft you can adapt for your manager or OR in [team-metrics-proposal.md](file:///G:/agy-bench/ws/607dac4c20b7/team-metrics-proposal.md).

What am I missing, and what would make this wrong?
