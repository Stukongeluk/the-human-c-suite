**CTO: AI coding agents and code review**

**Bottom line:** Yes to AI coding agents for every engineer in January. No to dropping review for small changes. Review is where AI-written bugs get caught, and skipping it won't give you the speed-up anyway. Make review faster instead. Confidence: high.

**What**
- **AI code needs more checking, not less.** AI co-authored PRs had about 1.7x more issues than human-only ones ([CodeRabbit, 470 PRs](https://www.coderabbit.ai/blog/state-of-AI-vs-human-code-generation-report)). In security-relevant tasks, models picked the insecure option 45% of the time ([Veracode, 100+ models](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)). [medium: both are vendor studies]
- **Review is the bottleneck, so your instinct is half right.** Teams with high AI adoption merged 98% more PRs, but review time went up 91% and delivery at company level didn't improve ([Faros AI, 10,000+ devs](https://www.faros.ai/blog/ai-productivity-paradox-report-2025)). [medium: vendor telemetry]
- **AI speeds delivery but breaks things without safety nets.** DORA's 2025 research (DORA is Google's long-running software delivery study) finds AI now raises throughput but still hurts stability "without robust control systems" ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)). Review is one of those systems. [verified]
- **"Small" is the wrong filter.** Agents can split any change into small PRs, so the exemption soon covers most of your code. A one-line change to auth or config can still take production down. Risk depends on what a change touches, not how big it is. [assumed: my reasoning, not measured]
- **Feeling faster isn't the same as being faster.** In METR's 2025 trial, developers thought AI made them about 20% faster while it measured them 19% slower ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). Their 2026 follow-up is inconclusive. Measure it. [verified]

**Why it matters:** Skipping review saves a few hours per PR. The price is more rollbacks, more security holes and code nobody on the team understands. Review is also how juniors learn: in [Anthropic's trial](https://www.anthropic.com/research/AI-assistance-coding-skills), developers using AI scored 17% lower on understanding the code they had just written, and lowest on debugging. If you fall under PCI DSS, requirement 6.2.3 requires review before release ([text](https://ce.prod.cloudaware.com/frameworks/pci-dss-v4.0.1/06/02/03/)). SOC 2 and ISO 27001 auditors usually check for reviewed changes too. [ASSUMPTION: I don't know your compliance scope]

**How to act**
1. Record a baseline per team, not per person: deploy frequency, lead time, change failure rate (the share of releases that cause an incident) and PR review time → eng leads → Fri 18 Dec.
2. Publish a one-page AI policy covering approved tools, what data may go into them, and "you own what you merge, whoever typed it" → CTO → Fri 18 Dec.
3. Make review faster: an AI reviewer does a first pass, PRs stay small, and a human gives first review within 4 working hours → tech leads → live Mon 4 Jan.
4. Add a fast lane based on risk, not size. Docs and copy-only changes merge once CI (the automated build and tests) passes. Anything touching auth, payments, data, infra, dependencies, config or tests always gets a human → CTO + security lead → Mon 4 Jan.
5. Review at 30, 60 and 90 days. If change failure rate or review time rises, slow down. If they hold, widen the fast lane → CTO → Feb/Mar/Apr.

**Your decision**
- **A: Skip review for small changes.** Saves review time, but expect more incidents, security debt and audit findings.
- **B: Agents for everyone, keep review and make it faster.** Most of the speed-up, without losing safety.

Recommendation: B.

Want me to draft the one-page AI policy from step 2?
