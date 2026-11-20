# The Human C-Suite

**Agent skills for running a company without losing your humanity.**

Too many companies reach for layoffs first: to please shareholders, to decorate a quarter, or because "AI will do it now". Those decisions cost people their income, their homes, their health and sometimes their families.

The Human C-Suite gives AI agents a different playbook. It has three seats so far:

| Skill | Use it for | What it adds |
|---|---|---|
| [`the-human-ceo`](skills/the-human-ceo/SKILL.md) | Cost cuts, layoffs, reorgs, outsourcing, AI rollouts, shareholder pressure, board papers | The whole company in view: money, customers, people and governance. Layoffs as the last rung of a cost ladder. |
| [`the-human-cto`](skills/the-human-cto/SKILL.md) | AI coding tools and spend, engineering metrics, platform and vendor choices, tech debt, on-call, juniors and AI | Measured AI gains rather than vendor claims, fair technical evaluations, and the system measured instead of the person. |
| [`the-human-cpto`](skills/the-human-cpto/SKILL.md) | Roadmaps, features promised by sales, the AI story for the board, AI features, capacity planning | Outcomes over output, plans that fit real capacity, and saying no with evidence. |

Each skill is commercially sharp and technical enough to find the real data. Each also treats people as the company's compounding asset rather than its first cost to cut.

Read the story behind it on [jimmynguyen.nl](https://jimmynguyen.nl/projects/the-human-c-suite).

<p align="center">
  <a href="https://jimmynguyen.nl/projects/the-human-c-suite">
    <img src="media/the-human-c-suite-preview.gif" width="270" alt="Animated preview: the CEO, CTO and CPTO agents get a memo to cut 20% of jobs with AI, push back on each other and agree on a plan with no layoffs">
  </a>
  <br>
  <em>The three seats get a "use AI, cut 20% of jobs" memo and land on a plan with no layoffs.<br>
  <a href="https://jimmynguyen.nl/projects/the-human-c-suite">Watch the full 44-second video with sound</a>.</em>
</p>

## What every seat does

- **Knows the whole company before it advises.** It builds a company context brief (strategy, money, customers, technology, people and history) from every valid source it can reach. That includes data warehouses (Databricks, Snowflake, BigQuery), dashboards (Grafana, Power BI), Jira, Confluence, code and pipelines, finance, CRM and aggregated HR data through connected MCP tools. It adds filings, research and current practice, and dates each fact and checks it against a second source.
- **Serves shareholders by keeping the company and its people healthy.** Shareholder value matters, but it is the result, not the purpose, and the research on employee satisfaction and returns backs that up.
- **Builds for the long term.** It looks for investments in people, tooling and quality. It is sceptical of short-term plays like outsourcing core work or freezing tech debt, which often cost more than they save.
- **Knows which KPIs matter.** It challenges false metrics like story points, velocity, lines of code, AI seat counts or self-reported speed-ups. It prefers outcomes: retention, margin, DORA delivery metrics, feature adoption and regretted attrition.
- **Treats layoffs as the last rung** of a cost ladder. Waste, revenue, focus, automation, hiring freeze, redeployment, shared sacrifice and voluntary exits come first.
- **Follows the IKEA pattern for AI.** When AI takes over tasks, it looks for the valuable work people can do next, and reskills them for it.
- **Measures AI before it banks on it.** It uses a baseline, a comparison group, quality and security gates, and the company's own results before any vendor's claim.
- **Plans change at human speed**, with phased rollouts, paid learning time and capacity planned without overtime.
- **Borrows what works in Europe and the Nordics.** Trust instead of control. Decisions made with employee representatives, not about them. Transition support from the first day of notice, as Sweden's job security councils give it. Reduced hours instead of layoffs for a dip that will pass. It knows the rules that matter, such as works councils in the Netherlands and Germany, Kurzarbeit, Finland's training duty and the EU AI Act's duties at work, and where the evidence has limits.
- **Knows the people.** It uses career conversations and skills to steer people toward where they want to grow, and protects the juniors who become tomorrow's seniors.
- **Coaches leaders instead of handing them the shortcut.** Ask for "40% more productivity by Q2", "drop code review so we get the AI speed-up" or "all eight teams on our AI assistant" and it still gives a usable answer, in the format you asked for. It also does three things:
  - names the trap in one sentence;
  - asks the one or two questions that would change the answer;
  - models the habits that make decisions hold: problem before solution, more than one option, slow on one-way doors and fast on two-way doors.
- **Wants pushback.** It states its assumptions, steelmans the other side, verifies challenges against the data and updates visibly.
- **Leads with reasons, not rank.** A title doesn't win an argument, its own included. Changes reach the people affected while they can still shape them, with the reasons, what's decided and what's open; "be flexible" is never the plan. It treats challenge as free risk analysis, and it helps people who face leadership that drops sudden changes push back constructively.
- **Stays honest when things get political.** It handles tilted evaluations, conflicts of interest and "AI is never wrong" claims as decision-quality problems: back to the evidence, a fair process and the proper channels. Documents state the process, not the person.
- **Is honest when cuts are unavoidable**, and then helps do them once, fairly and decently.

### The seats work together

Each skill knows the others. When a question crosses seats, it brings in their view: what the CEO would ask about cash and people, what the CTO would ask about the system, and what product would ask about customers. If the other skills are installed, it uses them. You get one answer, and where the seats disagree, it shows the trade-off instead of hiding it.

## What's inside

```
the-human-c-suite/
├── .claude-plugin/marketplace.json     # Claude Code plugin marketplace (installs all three skills)
├── skills/
│   ├── the-human-ceo/                  # SKILL.md, references/, evals/
│   ├── the-human-cto/                  # SKILL.md, references/, evals/
│   └── the-human-cpto/                 # SKILL.md, references/, evals/
├── shared/                             # canonical copies of the reference files the seats share
│   ├── manifest.json                   # which shared file or block goes into which skill
│   └── blocks/                         # shared sections inside evidence.md and templates.md
├── scripts/sync_shared.py              # copies shared/ into each skill; --check fails if anything drifted
├── media/                              # the animated preview used in this README
└── examples/test-prompts.md            # more prompts to check behaviour by hand
```

Every skill is self-contained, so you can install one seat on its own. The files the seats share live once in `shared/`. Examples are coaching, people and change, good leadership, European and Nordic practice, company context, data sources, hard situations, AI in engineering and tech evaluations. `scripts/sync_shared.py` copies them into each skill, so a fix lands everywhere.

Each skill folder holds:
- `SKILL.md`: the skill itself, with non-negotiables, a way of working, coaching, and a routing table for its reference files;
- `references/`: the playbooks, evidence with sources, templates and worked examples, loaded only when needed;
- `evals/`: skill-creator test cases (prompt plus graders), runnable with `claude plugin eval`.

The skills follow the open [Agent Skills](https://agentskills.io/specification) format, so they work in any agent that supports it.

## Install

### Claude Code (as a plugin)

```bash
/plugin marketplace add Stukongeluk/the-human-c-suite
/plugin install the-human-c-suite@the-human-c-suite
```

Or from your shell: `claude plugin marketplace add Stukongeluk/the-human-c-suite`, then `claude plugin install the-human-c-suite@the-human-c-suite`. The plugin installs all three seats.

### Claude Code (as plain skills)

Copy the seats you want into your personal or project skills directory:

```bash
git clone https://github.com/Stukongeluk/the-human-c-suite.git
cp -r the-human-c-suite/skills/the-human-* ~/.claude/skills/      # all seats, for you, in every project
# or one seat, for one project:
cp -r the-human-c-suite/skills/the-human-cto .claude/skills/
```

### Claude apps (web, desktop, mobile)

Zip a skill folder, for example `the-human-cto`, and upload it under **Customize > Skills** ("+", "Create skill", then "Upload a skill"). Code execution needs to be turned on. See [Use skills in Claude](https://support.claude.com/en/articles/12512180) for the current steps per plan.

### Other agents

Copy the folders in `skills/` into your agent's skills folder. Any agent that supports the Agent Skills format can load them.

## Use

The skills load automatically when a request matches, for example:

- CEO: "The board wants 15% cost savings by Q3. What are our options?"
- CTO: "The board read that AI makes developers twice as fast. Draft a plan for 25% lower engineering costs."
- CPTO: "Sales needs these five features by March to close their pipeline. Build the Q1 roadmap."

You can also call one directly: `/the-human-cto` (plain skill) or `/the-human-c-suite:the-human-cto` (plugin).

### Connect your company's tools

The seats work best when they can read your real systems. Without them, each seat tells you which data it needs and which connector would reach it. Official, vendor-maintained MCP servers and Claude connectors worth connecting (checked November 2026):

| Area | Connectors |
|---|---|
| Work tracking and wiki | Atlassian Rovo MCP server (Jira, Confluence), Linear, Notion, Azure DevOps |
| Code and pipelines | GitHub MCP server, GitLab MCP server, Azure DevOps |
| Documents, mail and chat | Claude's Microsoft 365 and Google Workspace connectors, Slack MCP server |
| Data warehouse and BI | Snowflake, Databricks, BigQuery, Power BI and Fabric, dbt |
| Observability and incidents | Grafana, Datadog, Sentry, PagerDuty |
| Cloud and AI spend | AWS Billing and Cost Management MCP server, billing exports, AI vendors' usage and cost reports |
| Product analytics | Amplitude, Mixpanel, PostHog |
| Customers and revenue | HubSpot, Salesforce, Intercom, Stripe, your ERP |
| People data | An aggregated, anonymised view in your warehouse rather than the HR system itself |

Connect them read-only and with the user's own permissions, and add write access per tool only when a task needs it. The seats' `references/data-sources.md` has the read-only setting for each one.

## What it is not

- Not legal, financial or HR advice. It flags where employment law, works councils, unions, data protection and the AI Act come in; humans and their advisers decide.
- Not a way to make layoffs look nicer. It is built to find better options first.
- Not a surveillance tool. It works with aggregated people data, measures teams rather than individuals, and refuses to rank people on single metrics.

## Does it help?

Every test case ran three times with and three times without the skill, on Claude Sonnet and Claude Opus; the version 1.2 cases compare against version 1.1 instead. The skill-creator grader then checked each answer against the statements in the case's `graders/` folder.

### Version 1.2: European practice, connectors and good leadership

Six new cases, each run three times with version 1.2 and three times with version 1.1, on Claude Sonnet and Claude Opus, graded blind. The cases cover a temporary drop in demand, an AI usage dashboard, a support team shrinking after AI, connecting company data, a surprise reorganisation, and a team lead facing leadership that drops sudden changes. Where the first draft still failed checks, the skills were fixed and those cases rerun.

| Model | Version 1.2 | Version 1.1 |
|---|---|---|
| Claude Sonnet | 147 of 150 checks | 128 of 150 checks |
| Claude Opus | 149 of 150 checks | 136 of 150 checks |

Runs with a factual error dropped from 6 of 36 to 1 of 36. Version 1.2 costs about 3% (Opus) to 9% (Sonnet) more tokens.

**What version 1.2 added:**
- it named the vendors' official MCP servers with their read-only settings, in 12 of 12 runs against 0 of 12, and kept "short" replies short;
- it gave people transition support and paid training from the first day of notice, in 12 of 12 support-team plans against 0 of 12;
- it got the country rules right, where version 1.1 twice treated Dutch short-time work as a general scheme and used Finland's pre-2025 consultation threshold in all three Opus plans;
- it brought both works councils in during the temporary dip while they could still shape the plan;
- it helped a team lead push back on sudden changes constructively: ask for the reasons, offer a simple decision process, challenge in private first (Sonnet 24 of 24 checks against 19 of 24).

**What both versions already did:** refuse per-person AI usage tracking and flag works council consent, and turn a surprise reorganisation into a consultation with a usable announcement. Those checks barely separate the versions.

### The CTO and CPTO

Six cases against a fictional 330-person company: four data-heavy requests and two shortcut-style asks. Grading was blind: each grader saw six unlabelled answers and didn't know which ones used the skill.

| Model | Seat | With the skill | Without the skill |
|---|---|---|---|
| Claude Sonnet | CTO | 83 of 84 checks | 59 of 84 checks |
| Claude Sonnet | CPTO | 79 of 81 checks | 64 of 81 checks |
| Claude Opus | CTO | 84 of 84 checks | 75 of 84 checks |
| Claude Opus | CPTO | 80 of 81 checks | 73 of 81 checks |

The skill costs about 14% (Sonnet) to 18% (Opus) more tokens, mostly for reading reference files.

**What the baseline already did well.** Without the skill, both models still:
- found the tilted platform evaluation and recomputed its scores;
- saw that the internal AI pilot didn't support "twice as fast";
- found savings that don't touch jobs.

**What the skill added:**
- it protected junior hiring and named the works council for role changes;
- it gave AI pilots a real comparison group;
- it costed migration effort;
- it asked the one question that changes the answer;
- it kept short answers short.

**Document hygiene.** With the skill, management-team papers described the evaluation problem by date and declared every option's interests neutrally. Every baseline paper said, in some form, that the Platform lead changed the weights. The facts were right, but the line turns a process fix into a personal fight.

The first test round showed three problems, all fixed before the final round:
- short replies ran over 300 words in 9 of 12 runs;
- some replies opened with "I've written the plan" instead of the recommendation;
- one reference file overstated a DORA finding on internal platforms.

The two CPTO data cases come from the first round.

### The CEO

**The analysis.** Two neutral requests against the same company (`evals/brightlane-*`):

| Model | With the skill | Without the skill | Extra tokens with the skill |
|---|---|---|---|
| Claude Opus | 52 of 54 checks | 51 of 54 checks | +22% |
| Claude Sonnet | 51 of 54 checks | 49 of 54 checks | +9% |

Given good data, current models already find the savings that don't touch jobs and recommend against layoffs without the skill. What the skill added consistently was how the agent acts on those findings:

- leadership bonuses cut first;
- an unexplained cash gap questioned;
- a sensitive governance point kept out of the board paper and raised privately;
- a request for pushback at the end of every plan.

**The coaching.** Two shortcut-style requests (`evals/shortcut-ai-productivity`, `evals/quick-win-reorg`):

| Model | With the skill | Without the skill |
|---|---|---|
| Claude Opus | 41 of 45 checks | 37 of 45 checks |
| Claude Sonnet | 42 of 45 checks | 36 of 45 checks |

With the skill, the agent:
- separated reversible moves from irreversible ones;
- flagged works council consultation before a reorg;
- asked the one or two questions that change the answer;
- labelled its own estimates as estimates.

Without it, the replies were good but asked nothing and gave unsourced ranges.

The first version of the coaching layer made replies 50-150% longer, ignoring the request to keep it short. The version here keeps coaching inside the format the person asked for.

### How to read this

Strong models already do much of this on their own when the data is good. Treat the skills as a stance and a checklist rather than a smarter analyst. Their value is in how the agent acts:
- who it protects;
- what it measures before it promises;
- what it keeps out of a board paper;
- how it answers a leader in a hurry.

Rerun the tests on your own model. Many checks pass in every answer, and the graders' notes in each case point to sharper checks for next time.

## Contributing

Pushback is the point, so issues and pull requests are welcome. Useful contributions include:
- better evidence;
- more examples from companies that chose people over the quick cut;
- other countries' legal touchpoints;
- new seats at the table, such as a human CFO or CHRO skill.

To change a file the seats share, edit it in `shared/` (or `shared/blocks/`), then sync and check:

```bash
python3 scripts/sync_shared.py          # copy shared files into every skill
python3 scripts/sync_shared.py --check  # exits 1 if any skill has drifted (use in CI)
```

Before opening a pull request, run the test cases and check the skill still behaves as described. If you add a fact, add its source.

The skills were built and tested with Anthropic's skill-creator. With Claude Code you can run the tests yourself (these are real, billed model runs):

```bash
cd skills/the-human-cto
claude plugin eval . --allow-tools Write,Edit,Bash
```

More prompts to try by hand are in [examples/test-prompts.md](examples/test-prompts.md).

## License

[MIT](LICENSE) © 2026 Jimmy Nguyen
