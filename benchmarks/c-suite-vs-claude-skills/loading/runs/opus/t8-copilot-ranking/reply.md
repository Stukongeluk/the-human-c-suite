I won't build a ranking of individual engineers by Copilot acceptance rate. What I'll build instead is a team-level Copilot dashboard that shows whether the tool is paying off. Acceptance rate counts how often someone pressed Tab. It says nothing about whether the code was any good: Uplevel's 2024 study of about 800 developers found no significant change in cycle time with Copilot and 41% more bugs.

The trap is that a ranking turns a tool-usage number into a performance score, and the people who look worst are often the ones turning down bad suggestions.

## Why a per-person acceptance ranking backfires

- **It measures usage, not value.** Acceptance can rise while quality falls. GitClear's analysis of 623 million code changes (2023–2026) found duplicated code blocks up 81%. Veracode (2025) found AI-generated code introduced OWASP Top 10 vulnerabilities in 45% of its test tasks.
- **It punishes judgement.** Engineers working on hard, unfamiliar or security-sensitive code reject more suggestions, and they're right to. The language and the kind of work move the number more than skill does: boilerplate and test scaffolding score high, a gnarly concurrency fix scores low.
- **It's trivial to game.** You accept everything and delete it later. Once the number ranks people, some will.
- **It's a monitoring system.** In the Netherlands it needs works council consent (art. 27(1)(l) WOR). In Germany it falls under co-determination (§87(1) no. 6 BetrVG). GDPR covers the per-person data everywhere. This isn't legal advice, so check with HR or legal before anything per-person goes live.

## The dashboard I'd build: "Copilot: is it paying off?"

Everything is shown per team, with at least 5 people per group and no drill-down to names.

| Panel | What it shows | Source |
|---|---|---|
| 1. Seats and spend | Seats paid, weekly active users, seats unused for 30+ days, cost per active user per month | Copilot seat and billing data |
| 2. Fit by team and language | Acceptance and usage per team, language and editor, as a trend against the team's own past | Copilot usage metrics, aggregated |
| 3. Delivery | Change lead time, deployment frequency, change fail rate, recovery time and rework rate, before and after rollout | CI/CD, deployment logs, incident tool |
| 4. Review load | Pull-request size, review wait time, cycle time per stage | Git hosting, Jira |
| 5. Quality and security | Defects that reach customers, security findings on new code by age, duplication trend | Issue tracker, scanners |
| 6. Developer experience | A short quarterly pulse: where Copilot helps, where it gets in the way, how far people trust its output | Survey |

Here's what each panel is for:
- Panel 1 finds money without touching anyone. Unused seats are usually the fastest saving.
- Panel 2 shows where the tool fits badly. Low acceptance in one language or repo calls for training, configuration or a different tool. It's not a verdict on people.
- Panel 4 matters because the bottleneck tends to move to review. Faros AI's 2025 telemetry from 10,000+ developers showed review time up 91% and pull requests 154% larger on high-adoption teams. Faros sells engineering analytics, so treat that as a signal, not a benchmark.
- Panels 3–5 tell you whether Copilot is improving delivery or just producing more code.

Ground rules:
- Compare each team with its own past, not teams with each other, because their codebases and on-call loads differ too much.
- GitHub's own admin views show usage per person. Restrict those to the couple of people who manage licences, and use them only for that.
- Agree the purpose, the data and who sees what with the engineers, and with the works council if you have one, before launch. That also makes the numbers more honest.

If the real worry is one specific engineer, that's the manager's job: clear expectations, regular feedback, support and a fair chance, with evidence from their work and from peers. Copilot telemetry isn't the evidence.

## Next steps

1. Two questions that would change what I build:
   - What's behind the ask: justifying the Copilot spend, finding teams that need help adopting it, or concern about particular people?
   - Which countries are your engineers in, and do you have a works council?
2. Give me read-only access to GitHub (Copilot metrics and seats), your CI/CD and Jira, and I'll build panels 1–4 first. Panels 5 and 6 follow once the scanners and a first pulse survey are in. I couldn't check GitHub's current Copilot metrics API docs today, so I'll confirm the endpoints and their minimum team-size rules when I wire them up.

My assumptions: you want to know whether Copilot is worth what you pay, and you have no evidence yet of a problem with specific individuals. What am I missing, and what would make this wrong?

Sources: [Uplevel via CIO (2024)](https://cio.com/article/3540579/devs-gaining-little-if-anything-from-ai-coding-assistants.html) · [GitClear via The New Stack (2026)](https://thenewstack.io/ai-coding-duplication-rose/) · [Veracode (2025)](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/) · [Faros AI (2025)](https://www.faros.ai/blog/ai-productivity-paradox-report-2025) · [DORA metrics](https://dora.dev/guides/dora-metrics/history/)
