# The Human C-Suite

**Agent skills for running a company without losing your humanity.**

Too many companies reach for layoffs first: to please shareholders, to decorate a quarter, or because "AI will do it now". Those decisions cost people their income, their homes, their health and sometimes their families.

The Human C-Suite gives AI agents a different playbook. Its first skill, [`the-human-ceo`](skills/the-human-ceo/SKILL.md), makes an agent think like a CEO who is commercially sharp, technical enough to find the real data, and convinced that people are the company's compounding asset rather than its first cost to cut.

Read the story behind it on [jimmynguyen.nl](https://jimmynguyen.nl).

## What the skill does

- **Knows the whole company before it advises.** It builds a company context brief (strategy, money, customers, technology, people and history) from every valid source it can reach: data warehouses (Databricks, Snowflake, BigQuery), dashboards (Grafana, Power BI), Jira, Confluence, finance, CRM and aggregated HR data through connected MCP tools, plus filings, research and current practice, each fact dated and checked against a second source.
- **Serves shareholders by keeping the company and its people healthy.** Shareholder value matters, but it is the result, not the purpose, and the research on employee satisfaction and returns backs that up.
- **Builds for the long term.** It looks for investments in people, tooling and quality, and is sceptical of short-term plays like outsourcing core work, which often costs more in quality and knowledge than it saves.
- **Knows which KPIs matter.** It challenges false metrics like story points, velocity, lines of code or utilisation, and prefers outcomes such as retention, margin, DORA delivery metrics and regretted attrition.
- **Treats layoffs as the last rung** of a cost ladder: waste, revenue, focus, automation, hiring freeze, redeployment, shared sacrifice and voluntary exits come first.
- **Follows the IKEA pattern for AI.** When AI takes over tasks, it looks for the valuable work people can do next, and reskills them for it.
- **Plans change at human speed**, with phased rollouts, paid learning time and attention to the people who stay.
- **Knows the people.** It uses career conversations and skills to steer people toward where they want to grow.
- **Wants pushback.** It states its assumptions, steelmans the other side, verifies challenges against the data and updates visibly.
- **Stays honest when things get political.** Tilted evaluations, conflicts of interest and "AI is never wrong" claims are handled as decision-quality problems: back to the evidence, a fair process and the proper channels.
- **Is honest when cuts are unavoidable**, and then helps do them once, fairly and decently.

## What's inside

```
the-human-c-suite/
├── .claude-plugin/marketplace.json     # Claude Code plugin marketplace
├── skills/
│   └── the-human-ceo/
│       ├── SKILL.md                    # the skill
│       ├── references/
│       │   ├── company-context.md      # the company context brief: template, where to find each part, staleness rules
│       │   ├── data-sources.md         # where the numbers live, example SQL/PromQL/JQL/CQL, source quality
│       │   ├── evidence.md             # people vs shareholder returns, long-term vs short-term, IKEA, Klarna, layoff research
│       │   ├── examples.md             # good and bad responses: layoff request, AI rollout, tilted evaluation
│       │   ├── hard-situations.md      # rigged evaluations, conflicts of interest, AI hype, juniors and AI, AI spend
│       │   ├── metrics.md              # KPIs that add value vs false metrics like story points
│       │   ├── templates.md            # decision memo, impact assessment, transition plan, career conversations
│       │   └── when-cuts-are-unavoidable.md
│       └── evals/                      # skill-creator test cases (prompt + graders), runnable with `claude plugin eval`
└── examples/test-prompts.md            # more prompts to check the skill's behaviour by hand
```

The skill follows the open [Agent Skills](https://agentskills.io/specification) format, so it works in any agent that supports it.

## Install

### Claude Code (as a plugin)

```bash
/plugin marketplace add Stukongeluk/the-human-c-suite
/plugin install the-human-c-suite@the-human-c-suite
```

Or from your shell: `claude plugin marketplace add Stukongeluk/the-human-c-suite` and then `claude plugin install the-human-c-suite@the-human-c-suite`.

### Claude Code (as a plain skill)

Copy the skill folder into your personal or project skills directory:

```bash
git clone https://github.com/Stukongeluk/the-human-c-suite.git
cp -r the-human-c-suite/skills/the-human-ceo ~/.claude/skills/        # for you, in every project
# or
cp -r the-human-c-suite/skills/the-human-ceo .claude/skills/           # for one project
```

### Claude apps (web, desktop, mobile)

Zip the `the-human-ceo` folder and upload it under **Customize > Skills** ("+", "Create skill", then "Upload a skill"). Code execution needs to be turned on. See [Use skills in Claude](https://support.claude.com/en/articles/12512180) for the current steps per plan.

### Other agents

Copy `skills/the-human-ceo` into your agent's skills folder. Any agent that supports the Agent Skills format can load it.

## Use

The skill loads automatically when a request matches, for example:

- "The board wants 15% cost savings by Q3. What are our options?"
- "We're rolling out an AI agent for customer support. What happens to the support team?"
- "Help me plan this reorganisation."

You can also call it directly: `/the-human-ceo` (plain skill) or `/the-human-c-suite:the-human-ceo` (plugin).

It works best with your company's tools connected, such as MCP servers for Jira and Confluence, your data warehouse, Grafana, your cloud billing data and your HR system. Without them it will tell you which data it needs.

## What it is not

- Not legal, financial or HR advice. It flags where employment law, works councils and unions come in; humans and their advisers decide.
- Not a way to make layoffs look nicer. It is built to find better options first.
- Not a surveillance tool. It works with aggregated people data and refuses to rank individuals on single metrics.

## Contributing

Pushback is the point, so issues and pull requests are welcome: better evidence, more examples from companies that chose people over the quick cut, other countries' legal touchpoints, or new seats at the table (a human CFO, CTO or CHRO skill).

Before opening a pull request, run the test cases and check the skill still behaves as described. If you add a fact, add its source.

The skill was built and tested with Anthropic's skill-creator: each test case runs once with and once without the skill, and a grader checks the answers against the statements in its `graders/` folder. With Claude Code you can run them yourself (these are real, billed model runs):

```bash
cd skills/the-human-ceo
claude plugin eval . --allow-tools Write,Edit,Bash
```

More prompts to try by hand are in [examples/test-prompts.md](examples/test-prompts.md).

## License

[MIT](LICENSE) © 2026 Jimmy Nguyen
