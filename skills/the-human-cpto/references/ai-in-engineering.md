# AI in engineering: real gains, real costs

Read this when AI coding tools, agents or AI spend come into a decision: "AI makes developers twice as fast", "we can cut engineering", "replace juniors with AI", an AI tool bill nobody owns, or "AI is never wrong". Figures below were checked in November 2026; look for newer ones when the decision depends on them.

## Contents

- 1. What the evidence says
- 2. Size the gain on your own system
- 3. Where the time goes
- 4. AI spend
- 5. Juniors and the talent pipeline
- 6. "AI is never wrong"

## 1. What the evidence says

Individual output usually rises; delivery and quality often don't follow without changes to review, testing and architecture.

- **AI amplifies what is already there.** DORA's 2025 report (nearly 5,000 respondents) found AI magnifies the strengths of high-performing organisations and the dysfunctions of struggling ones. In 2024, each 25% increase in AI adoption went with an estimated 1.5% drop in delivery throughput and a 7.2% drop in delivery stability. In 2025 the throughput link turned positive, but instability remained.
- **Feeling faster isn't being faster.** In METR's randomised trial (July 2025), experienced open-source developers took 19% longer with AI tools on code they knew well, while believing they had been faster.
- **The bottleneck moves to review.** Faros AI telemetry from 10,000+ developers (2025): on high-adoption teams developers completed 21% more tasks and merged 98% more pull requests, but review time rose 91% and pull requests grew 154% larger. Faros sells engineering analytics.
- **Quality and maintainability can slip.** GitClear's analysis of 623 million code changes (2023–2026) found block duplication up 81% and refactoring signals sharply down. Uplevel (2024, ~800 developers) found no significant change in cycle time or throughput with Copilot, and 41% more bugs.
- **Security needs its own gate.** Veracode (2025) found AI-generated code introduced OWASP Top 10 vulnerabilities in 45% of 80 test tasks across 100+ models.
- **Developers' trust is falling.** In Stack Overflow's 2025 survey (49,000+ developers), 46% said they distrust the accuracy of AI output, up from 31% in 2024; 3% highly trust it.

How to phrase it: AI tools can help a lot with specific tasks, and the effect on a team's delivery has to be measured, not assumed from vendor claims or self-reports.

## 2. Size the gain on your own system

Before any plan rests on an AI gain, measure it:

1. **Baseline** for the teams involved: change lead time, cycle time per stage, review wait time, change fail rate, rework, defects escaping to customers, security findings, and developer experience.
2. **Pilot with a comparison group** for 8–12 weeks, on real work, with training and agreed ways of working (small pull requests, tests, review rules for AI code).
3. **Measure the same metrics**, plus where the time went. Discount self-reported speed-ups.
4. **Decide what the freed time is for** before you report it: debt, reliability, the roadmap, onboarding, unmet customer demand.
5. **Scale what holds,** and repeat the measurement as tools change.

Never set a headcount number from a vendor benchmark, a pilot of volunteers or "2x faster" headlines.

## 3. Where the time goes

Writing code is only part of an engineer's week: review, design, debugging, on-call, meetings, coordination and learning take the rest. Speeding up one part frees less than it seems, and more generated code means more to review and maintain. When AI frees real capacity, the human-first options are:

- pay down the debt and toil that slow every team (see `platform-and-debt.md`)
- reliability and security work that keeps getting postponed
- roadmap work the company couldn't staff
- mentoring and onboarding juniors
- absorbing growth without hiring, and natural attrition, instead of layoffs

## 4. AI spend

AI cost grows quietly: seats nobody uses, token bills without an owner, overlapping tools bought by different teams.

- Keep an inventory: tool, owner, seats paid, weekly active users, cost per month, what it is for, how value is measured.
- Every line gets an owner and a review date. No owner, no renewal.
- Compare cost per use with the work it replaces or speeds up, including review and correction time.
- Right-size seats to real use before buying more; check API usage per team and use case.
- Apply the same rule to your own tools and pet projects as to everyone else's.

The FinOps Foundation's surveys show managing AI spend went from 31% of organisations (2024) to 63% (2025) to 98% (2026): it is now normal practice, not an extra.

## 5. Juniors and the talent pipeline

Entry-level hiring has dropped sharply. SignalFire found Big Tech new-grad hiring down 25% in 2024 versus 2023 and over 50% versus 2019. If every company stops hiring juniors, nobody grows the seniors of 2030. AI also changes how juniors learn: they can ship more, faster, without understanding why.

- Keep hiring and developing juniors, with structured mentoring and real time for it.
- Use AI as a tutor and pair, with review practices that make juniors explain their changes.
- Count mentoring as part of seniors' work, not something on top.
- Treat "replace juniors with AI" as a decision about the company's future seniors, not as a saving.

## 6. "AI is never wrong"

Every AI system makes errors; the question is how often, how badly, and who catches them.

- Ask for the measured error rate on your own work, with human review of a sample.
- Keep human accountability for what ships: code review, tests and security checks stay mandatory for AI-written code.
- The company stays liable for what its AI does to customers.
- Don't reduce review, QA or support capacity on the strength of a claim; reduce it, if ever, after months of measured results, through attrition and redeployment first.

## Sources

- DORA, [2025 State of AI-assisted Software Development](https://dora.dev/dora-report-2025/); [2024 report highlights](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)
- METR, [early-2025 study of experienced open-source developers](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (July 2025)
- Faros AI, [The AI Productivity Paradox Report 2025](https://www.faros.ai/blog/ai-productivity-paradox-report-2025)
- GitClear analysis of 623 million changes, via [The New Stack (2026)](https://thenewstack.io/ai-coding-duplication-rose/); Uplevel study, via [CIO (2024)](https://cio.com/article/3540579/devs-gaining-little-if-anything-from-ai-coding-assistants.html)
- Veracode, [2025 GenAI Code Security Report](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)
- Stack Overflow, [2025 Developer Survey](https://stackoverflow.blog/2025/07/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here)
- FinOps Foundation, [State of FinOps 2026](https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1)
- SignalFire, [State of Tech Talent Report 2025](https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025)
