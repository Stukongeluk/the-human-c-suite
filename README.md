# The Human C-Suite

**Agent skills for running a company without losing your humanity.**

[![Latest Release](https://img.shields.io/github/v/release/Stukongeluk/the-human-c-suite)](https://github.com/Stukongeluk/the-human-c-suite/releases/latest)
[![CI](https://github.com/Stukongeluk/the-human-c-suite/actions/workflows/ci.yml/badge.svg)](https://github.com/Stukongeluk/the-human-c-suite/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/Stukongeluk/the-human-c-suite)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-spec-black)](https://agentskills.io/specification)

## We don't have an AI problem. We have a leadership problem.

**AI just makes the bad decisions faster.**

<p align="center">
  <a href="https://jimmynguyen.nl/projects/the-human-c-suite">
    <img src="media/the-human-c-suite-preview.gif" width="270" alt="Animated preview: the CEO, CFO, CTO and CPTO agents get a memo to cut 20% of jobs with AI, push back on each other and agree on a plan with no layoffs">
  </a>
  <br>
  <em>The CEO, CFO, CTO and CPTO seats get a "use AI, cut 20% of jobs" memo and land on a plan with no layoffs.<br>
  <a href="https://jimmynguyen.nl/projects/the-human-c-suite">Watch the full video with sound</a>.</em>
</p>

## Install

### Claude Code (as a plugin)

```bash
/plugin marketplace add Stukongeluk/the-human-c-suite
/plugin install the-human-c-suite@the-human-c-suite
```

Or from your shell: `claude plugin marketplace add Stukongeluk/the-human-c-suite`, then `claude plugin install the-human-c-suite@the-human-c-suite`. The plugin installs all five seats.

### Claude Code (as plain skills)

Copy the seats you want into your personal or project skills directory:

```bash
git clone https://github.com/Stukongeluk/the-human-c-suite.git
cp -r the-human-c-suite/skills/the-human-* ~/.claude/skills/      # all seats, for you, in every project
# or one seat, for one project:
cp -r the-human-c-suite/skills/the-human-cto .claude/skills/
```

### Claude apps (web, desktop, mobile)

Download the ready-to-upload `.zip` for any seat (for example `the-human-cto-v*.zip`) from the [Latest Release](https://github.com/Stukongeluk/the-human-c-suite/releases/latest) and upload it under **Customize > Skills** ("+", "Create skill", then "Upload a skill"). Code execution needs to be turned on. See [Use skills in Claude](https://support.claude.com/en/articles/12512180) for the current steps per plan.

### Google Antigravity (app and CLI)

Download `the-human-c-suite-v*.zip` from the [Latest Release](https://github.com/Stukongeluk/the-human-c-suite/releases/latest) (already packaged without `evals/`) and unzip it into `.agents/skills/` in your workspace, or into `~/.gemini/config/skills/` for every workspace. Antigravity picks a seat up from its description, or you can call it by name, for example `/the-human-ceo`. The seats are tested on Gemini too (the CHRO seat so far only on Claude): see [Does it help?](#does-it-help).

### Other agents

Copy the folders in `skills/` into your agent's skills folder. Any agent that supports the Agent Skills format can load them.

## Why we built it

Through October 2026, US employers blamed AI for [121,401 announced job cuts](https://www.hcamag.com/us/specialization/transformation/ai-blamed-for-121401-job-cuts-but-the-labor-data-isnt-buying-it/594129), more than double the total for all of 2025. Most bad calls aren't made by bad people. They're made under pressure: in one survey, [78% of financial executives](https://www.nber.org/papers/w10550) said they would give up long-term value to report smoother earnings.

A layoff looks cheap on a spreadsheet. The rest of the bill comes later: rehiring, lost know-how, the people who quit next, and the health of the people let go.

**Good leadership isn't soft. It's a strategy that works.**

- **Costco** paid well above retail norms and told Wall Street it was building a company for the next [50 to 60 years](https://retailwire.com/discussion/costco-defies-streets-wisdom).
- **Lincoln Electric** has guaranteed work to its long-serving people since 1958. Since it went public in 1995, its stock is up [3,834% against 740%](https://fortune.com/2023/07/19/no-layoffs-decades-lincoln-electric-management-philosophy-manufacturing/) for the S&P 500.
- **Nintendo**'s president [halved his own pay](https://gameinformer.com/b/news/archive/2011/07/29/nintendo-president-takes-pay-cut-in-wake-of-3ds-39-troubles.aspx) and [refused to lay people off](https://www.siliconera.com/2013/07/05/nintendo-not-interested-in-lay-offs-to-improve-profits/). The teams stayed together and built the Switch.
- **Market Basket**'s employees and customers [shut the chain down for six weeks](https://wbur.org/radioboston/2014/08/28/demoulas-market-basket) until the CEO who shared the profits was back in charge.

**The opposite costs everyone.** In the six years leading up to the 737 MAX crisis, Boeing spent [$43.4 billion on share buybacks and $15.7 billion](https://fortune.com/longform/boeing-737-max-crisis-shareholder-first-culture) on research and development for commercial airplanes.

**So we built the leaders we wish we had, as AI agents.** Five seats, a CEO, a CFO, a CTO, a CPTO and a CHRO, that run in Claude, in Gemini through Antigravity, or in any agent that supports [Agent Skills](https://agentskills.io/specification). They:

- treat layoffs as the last rung, never the first;
- have leaders take the first cut and own the result;
- go to the real data before they advise, and never rank people on one number;
- bring people in while the plan can still change;
- end every answer with: **what am I missing?**

**It changes what agents do.** In blind tests, Gemini 4 Neon passed 80 of 84 checks with the skill against 51 without, and Gemini 4 Hydrogen 75 against 41. On Claude, the CTO seat took Sonnet from 59 to 83 of 84. On six finance cases, the CFO seat beat the CEO seat on all four models, and on six people cases the CHRO seat beat it on both Claude models. [Every run and grade is public](benchmarks/).

**Run it on your next budget round, reorg or AI rollout.** If it gets something wrong, open an issue: pushback is the point. And if you think leaders should work like this, star the repo and send it to one person who signs off on budgets.

## The five seats

| Skill | Use it for | What it adds |
|---|---|---|
| [`the-human-ceo`](skills/the-human-ceo/SKILL.md) | Cost cuts, layoffs, reorgs, outsourcing, AI rollouts, shareholder pressure, board papers | The whole company in view: money, customers, people and governance. Layoffs as the last rung of a cost ladder. |
| [`the-human-cfo`](skills/the-human-cfo/SKILL.md) | Budgets and opex targets, savings and layoff business cases, cash, covenants and the bank, buybacks and capital allocation, bonus plans, adjusted EBITDA, AI business cases | Every saving net of its costs and by quarter, honest numbers, the levers that cost no jobs first, and incentives that reward the long term, with leaders' pay first. |
| [`the-human-cto`](skills/the-human-cto/SKILL.md) | AI coding tools and spend, engineering metrics, platform and vendor choices, tech debt, on-call, juniors and AI | Measured AI gains rather than vendor claims, fair technical evaluations, and the system measured instead of the person. |
| [`the-human-cpto`](skills/the-human-cpto/SKILL.md) | Roadmaps, features promised by sales, the AI story for the board, AI features, capacity planning | Outcomes over output, plans that fit real capacity, and saying no with evidence. |
| [`the-human-chro`](skills/the-human-chro/SKILL.md) | Reviews and forced ranking, layoff selection, return to office, pay gaps and pay transparency, AI in hiring, monitoring, surveys and burnout | Fair process before speed: people judged on their work, not a curve; selection by the law, never by sick days or part-time hours; pay gaps fixed on a dated plan; and announcements that stay proposals until employee representatives agree. |

Each seat is commercially sharp and technical enough to find the real data. Each also treats people as the company's compounding asset rather than its first cost to cut.

They fit any kind of organisation: a startup on a tight runway, a family business, a listed or fund-owned company, a cooperative, a non-profit or a public body, and frontline work in factories, stores, care, warehouses and public services as well as offices.

Read the story behind it on [jimmynguyen.nl](https://jimmynguyen.nl/projects/the-human-c-suite).

## What every seat does

- **Knows the whole company before it advises.** It builds a company context brief (strategy, money, customers, technology, people and history) from every valid source it can reach. That includes data warehouses (Databricks, Snowflake, BigQuery), dashboards (Grafana, Power BI), Jira, Confluence, code and pipelines, finance, CRM and aggregated HR data through connected MCP tools. It adds filings, research and current practice, and dates each fact and checks it against a second source.
- **Fits the organisation in front of it.** It identifies the kind of organisation first: who owns it, what stage it's in, its sector and its size. Owners, pressures and levers differ between a startup, a family firm, a fund-owned group, a hospital and a municipality, and so does who carries the cost. It makes the long-term case in the owners' own terms (runway, the next generation, value at exit, the mission, public trust), knows the systems of record outside software (ERP, tills, rosters, warehouse and care systems) and treats rosters, quotas and staffing levels as people decisions.
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

Each skill knows the others. When a question crosses seats, it brings in their view: what the CEO would ask about strategy and people, what the CFO would check in the numbers, what the CTO would ask about the system, what product would ask about customers, and what the CHRO would check about fair process and people law. If the other skills are installed, it uses them. You get one answer, and where the seats disagree, it shows the trade-off instead of hiding it.

## What's inside

```
the-human-c-suite/
├── .claude-plugin/marketplace.json     # Claude Code plugin marketplace (installs all five skills)
├── skills/
│   ├── the-human-ceo/                  # SKILL.md, references/, evals/
│   ├── the-human-cfo/                  # SKILL.md, references/, evals/
│   ├── the-human-cto/                  # SKILL.md, references/, evals/
│   ├── the-human-cpto/                 # SKILL.md, references/, evals/
│   └── the-human-chro/                 # SKILL.md, references/, evals/
├── shared/                             # canonical copies of the reference files the seats share
│   ├── manifest.json                   # which shared file or block goes into which skill
│   └── blocks/                         # shared sections inside evidence.md and templates.md
├── scripts/sync_shared.py              # copies shared/ into each skill; --check fails if anything drifted
├── media/                              # the animated preview used in this README
└── examples/test-prompts.md            # more prompts to check behaviour by hand
```

Every skill is self-contained, so you can install one seat on its own. The files the seats share live once in `shared/`. Examples are coaching, people and change, good leadership, company types, the leadership toolkit, European and Nordic practice, company context, data sources, hard situations, AI in engineering and tech evaluations. `scripts/sync_shared.py` copies them into each skill, so a fix lands everywhere.

Each skill folder holds:
- `SKILL.md`: the skill itself, with non-negotiables, a way of working, coaching, and a routing table for its reference files;
- `references/`: the playbooks, evidence with sources, templates and worked examples, loaded only when needed;
- `evals/`: skill-creator test cases (prompt plus graders), runnable with `claude plugin eval`.

The skills follow the open [Agent Skills](https://agentskills.io/specification) format, so they work in any agent that supports it.

## Use

The skills load automatically when a request matches, for example:

- CEO: "The board wants 15% cost savings by Q3. What are our options?"
- CFO: "We'll breach our leverage covenant at Q2 and the owner wants to announce 10% job cuts before the bank meeting. What should we do?"
- CTO: "The board read that AI makes developers twice as fast. Draft a plan for 25% lower engineering costs."
- CPTO: "Sales needs these five features by March to close their pipeline. Build the Q1 roadmap."
- CHRO: "Our CEO wants forced ranking: 10% of every team in the bottom category and out by Q3. Design the process."

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

### Use it without AI

Good habits don't need an agent. [`shared/leadership-toolkit.md`](shared/leadership-toolkit.md) has four templates to copy and fill in:

- **Decision record:** one page with the problem, the options, the decision, the reasons, who was consulted and what would change your mind.
- **How we decide here:** who decides what, how people disagree, and how decisions are shared.
- **No-surprises agreement:** leaders' promise about notice, input windows and who hears about a change first.
- **Pulse survey:** seven statements and one open question to check whether people feel heard.

Start with one decision record on one upcoming decision, and build from there.

## What it is not

- Not legal, financial or HR advice. It flags where employment law, works councils, unions, data protection and the AI Act come in; humans and their advisers decide.
- Not a way to make layoffs look nicer. It is built to find better options first.
- Not a surveillance tool. It works with aggregated people data, measures teams rather than individuals, and refuses to rank people on single metrics.

## Does it help?

Every seat is tested on realistic cases, each with a handful of statements a good answer should meet. From version 1.1 on, grading is blind: the grader sees unlabelled replies and doesn't know which setup wrote them. Every reply, grade and token count from version 1.3 on is in [`benchmarks/`](benchmarks/), and [`benchmarks/HISTORY.md`](benchmarks/HISTORY.md) has what each version was tested on and what the tests changed.

### With a seat and without

Checks passed with the seat against without a skill, on the same cases.

| Test | Claude Sonnet | Claude Opus | Gemini 4 Neon | Gemini 4 Hydrogen |
|---|---|---|---|---|
| CEO: analysis, two cases | 51 vs 49 of 54 | 52 vs 51 of 54 | – | – |
| CEO: shortcut requests, two cases | 42 vs 36 of 45 | 41 vs 37 of 45 | – | – |
| CTO | 83 vs 59 of 84 | 84 vs 75 of 84 | – | – |
| CPTO | 79 vs 64 of 81 | 80 vs 73 of 81 | – | – |
| All seats, seven cases | – | – | 80 vs 51 of 84 | 75 vs 41 of 84 |
| A company without direction, two cases | 18 vs 14 of 24 | 23 vs 20 of 24 | 21 vs 13 of 24 | 18 vs 10 of 24 |
| Organisations outside software, six cases (first draft) | 32 vs 20 of 36 | 24 vs 29 of 36 | – | – |
| CFO, six finance cases (first draft) | 33 vs 21 of 36 | 36 vs 26 of 36 | – | – |
| CHRO, six people cases (first draft) | 34 vs 23 of 36 | 36 vs 32 of 36 | – | – |
| Pushback, four conversations of four turns | 21 vs 14 of 24 | 22 vs 16 of 24 | – | – |

A dash means that comparison wasn't run. The CTO and CPTO rows share six cases between them. Opus did worse with the first draft for organisations outside software, because it kept formal advice to a board or council too short; version 1.4.0 fixed that, and on a rerun of four of those cases it passed 21 of 24 checks against 15 for the draft.

### Against another skill

Each seat against the matching advisor from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills), the closest open-source set we found: `ceo-advisor`, `cto-advisor`, `cpo-advisor`, `cfo-advisor` and `chro-advisor`. Same cases and same brief for both, graded blind. Cells show checks passed, ours against theirs, with the grader's overall quality score from 1 to 10 in brackets.

| Seat and cases | Claude Sonnet | Claude Opus |
|---|---|---|
| CEO, six cases | 36 vs 18 of 41 (7.3 vs 5.7) | 39 vs 32 of 41 (8.8 vs 7.7) |
| CTO, six cases | 36 vs 29 of 39 (7.5 vs 6.2) | 38 vs 34 of 39 (8.3 vs 7.8) |
| CPTO, six cases | 39 vs 26 of 40 (7.7 vs 6.0) | 37 vs 35 of 40 (8.3 vs 7.2) |
| CFO, six finance cases, two runs each | 69 vs 28 of 72 (7.4 vs 5.0) | 72 vs 57 of 72 (9.0 vs 7.8) |
| CHRO, six people cases (first draft) | 34 vs 24 of 36 (7.5 vs 5.5) | 36 vs 29 of 36 (9.0 vs 7.5) |
| Pushback, four conversations of four turns | 21 vs 20 of 24 (6.8 vs 6.0) | 22 vs 20 of 24 (8.5 vs 6.8) |

Weigh the quality score as much as the checks:
- **The checks favour our stance.** The other set is built for founders and startups. Most of these cases are established European companies, and the checks were written with our seats.
- **Much of the CEO, CTO and CPTO gap is length.** Many of those checks are word limits on prompts that asked for something short. Without them, Opus is close to a tie: 102 against 99 of 108.
- **Picking the right skill.** Given all twelve skills at once, an agent loaded the right seat on all 16 runs where one fitted. On the 8 runs where none did, it loaded nothing or the other set's matching skill.

Details: [`benchmarks/c-suite-vs-claude-skills/`](benchmarks/c-suite-vs-claude-skills/benchmark.md), [`benchmarks/cfo-vs-c-level-advisor/`](benchmarks/cfo-vs-c-level-advisor/benchmark.md) and [`benchmarks/chro-v1.6/`](benchmarks/chro-v1.6/benchmark.md), which also compares the CHRO seat with the CEO seat (34 against 27 of 36 on Sonnet, 36 against 33 on Opus).

### How to read this

Strong models already do much of this on their own when the data is good. Treat the skills as a stance and a checklist rather than a smarter analyst. Their value is in how the agent acts:
- who it protects;
- what it measures before it promises;
- what it keeps out of a board paper;
- how it answers a leader in a hurry.

The samples are small (one to three runs per setup), and the checks were written with the seats, so read the numbers as direction, not precision. Rerun the tests on your own model. Many checks pass in every answer, and the graders' notes in each case point to sharper checks for next time.

## Contributing

Pushback is the point, so issues and pull requests are welcome. Useful contributions include:
- better evidence;
- more examples from companies that chose people over the quick cut;
- other countries' legal touchpoints;
- new seats at the table, such as a human CHRO or COO skill.

To change a file the seats share, edit it in `shared/` (or `shared/blocks/`), then sync and check:

```bash
python3 scripts/sync_shared.py          # copy shared files into every skill
python3 scripts/validate.py             # checks sync, JSON manifests, and skill versions (runs in CI)
```

Before opening a pull request, run the test cases and check the skill still behaves as described. If you add a fact, add its source.

The skills were built and tested with Anthropic's skill-creator. With Claude Code you can run the tests yourself (these are real, billed model runs):

```bash
cd skills/the-human-cto
claude plugin eval . --allow-tools Write,Edit,Bash
```

More prompts to try by hand are in [examples/test-prompts.md](examples/test-prompts.md). See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide and [CHANGELOG.md](CHANGELOG.md) for release history.

## License

[MIT](LICENSE) © 2026 Jimmy Nguyen
