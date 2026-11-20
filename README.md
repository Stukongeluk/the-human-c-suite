# The Human C-Suite

**Agent skills for running a company without losing your humanity.**

## We don't have an AI problem. We have a leadership problem.

**AI just makes the bad decisions faster.**

<p align="center">
  <a href="https://jimmynguyen.nl/projects/the-human-c-suite">
    <img src="media/the-human-c-suite-preview.gif" width="270" alt="Animated preview: the CEO, CTO and CPTO agents get a memo to cut 20% of jobs with AI, push back on each other and agree on a plan with no layoffs">
  </a>
  <br>
  <em>The three seats get a "use AI, cut 20% of jobs" memo and land on a plan with no layoffs.<br>
  <a href="https://jimmynguyen.nl/projects/the-human-c-suite">Watch the full 44-second video with sound</a>.</em>
</p>

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

### Google Antigravity (app and CLI)

Copy the seat folders from `skills/` into `.agents/skills/` in your workspace, or into `~/.gemini/config/skills/` for every workspace. Leave out the `evals/` folders. Antigravity picks a seat up from its description, or you can call it by name, for example `/the-human-ceo`. The seats are tested on Gemini too: see [On Gemini](#on-gemini).

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

**So we built the leaders we wish we had, as AI agents.** Three seats, a CEO, a CTO and a CPTO, that run in Claude, in Gemini through Antigravity, or in any agent that supports [Agent Skills](https://agentskills.io/specification). They:

- treat layoffs as the last rung, never the first;
- have leaders take the first cut and own the result;
- go to the real data before they advise, and never rank people on one number;
- bring people in while the plan can still change;
- end every answer with: **what am I missing?**

**It changes what agents do.** In blind tests, Gemini 4 Neon passed 80 of 84 checks with the skill against 51 without, and Gemini 4 Hydrogen 75 against 41. On Claude, the CTO seat took Sonnet from 59 to 83 of 84. [Every run and grade is public](benchmarks/).

**Run it on your next budget round, reorg or AI rollout.** If it gets something wrong, open an issue: pushback is the point. And if you think leaders should work like this, star the repo and send it to one person who signs off on budgets.

## The three seats

| Skill | Use it for | What it adds |
|---|---|---|
| [`the-human-ceo`](skills/the-human-ceo/SKILL.md) | Cost cuts, layoffs, reorgs, outsourcing, AI rollouts, shareholder pressure, board papers | The whole company in view: money, customers, people and governance. Layoffs as the last rung of a cost ladder. |
| [`the-human-cto`](skills/the-human-cto/SKILL.md) | AI coding tools and spend, engineering metrics, platform and vendor choices, tech debt, on-call, juniors and AI | Measured AI gains rather than vendor claims, fair technical evaluations, and the system measured instead of the person. |
| [`the-human-cpto`](skills/the-human-cpto/SKILL.md) | Roadmaps, features promised by sales, the AI story for the board, AI features, capacity planning | Outcomes over output, plans that fit real capacity, and saying no with evidence. |

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

Every skill is self-contained, so you can install one seat on its own. The files the seats share live once in `shared/`. Examples are coaching, people and change, good leadership, company types, the leadership toolkit, European and Nordic practice, company context, data sources, hard situations, AI in engineering and tech evaluations. `scripts/sync_shared.py` copies them into each skill, so a fix lands everywhere.

Each skill folder holds:
- `SKILL.md`: the skill itself, with non-negotiables, a way of working, coaching, and a routing table for its reference files;
- `references/`: the playbooks, evidence with sources, templates and worked examples, loaded only when needed;
- `evals/`: skill-creator test cases (prompt plus graders), runnable with `claude plugin eval`.

The skills follow the open [Agent Skills](https://agentskills.io/specification) format, so they work in any agent that supports it.

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

Every test case ran with and without the skill, on Claude Sonnet and Claude Opus; the version 1.2 and later cases compare against the previous version instead. The skill-creator grader then checked each answer against the statements in the case's `graders/` folder. Every reply, grade and token count from the version 1.3 and later tests, and from the Gemini tests, is in [`benchmarks/`](benchmarks/).

### Version 1.4: every kind of organisation

Six new cases outside software, on Claude and Gemini, one run per setup, graded blind: a family machine builder in a downturn, a non-profit home-care organisation with a budget gap, a startup with nine months of runway, AI rostering for a supermarket chain, an AI fraud score for a municipality's welfare benefits, and a leaderboard for parcel drivers employed by subcontractors.

| Model | First draft of version 1.4 | Version 1.3.3 | Without the skill |
|---|---|---|---|
| Claude Sonnet | 32 of 36 checks | 27 of 36 | 20 of 36 |
| Claude Opus | 24 of 36 | 26 of 36 | 29 of 36 |
| Gemini 4 Neon (Medium) | 28 of 36 | 24 of 36 | not run |
| Gemini 4 Hydrogen (Medium) | 26 of 36 | 19 of 36 | not run |

The draft helped most where the situation was furthest from software: the startup's runway and one well-sized cut, stable schedules and a fair pilot in the supermarket, base rates and safeguards in the welfare case.

Opus did worse with the skill than without it. It treated a care director and a municipal CIO who had to advise a supervisory board or a council like someone acting in their own role, and kept to about 500 words, which left out the legal floor and the safeguards. Version 1.4.0 keeps the short limit for people acting in their own role and gives a formal recommendation to a board, council or supervisory body the full answer. Rerun side by side on four cases, Opus passed 21 of 24 checks with the fix against 15 of 24 with the draft, and the head-of-product replies stayed under 500 words. Details: [`benchmarks/company-types-v1.4/`](benchmarks/company-types-v1.4/benchmark.md) and its [follow-ups](benchmarks/company-types-v1.4/follow-ups.md).

### Version 1.3.3: clear direction

Two new cases about a company that has lost its direction: a fund-owned group about to rebrand, restructure for the fourth time and end all contractor and junior roles while NPS fell from +31 to +6, and a head of product told to put everyone on a rebrand while customer complaints stay open. Two runs per setup, graded blind.

| Model | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| Claude Sonnet | 18 of 24 checks | 15 of 24 | 14 of 24 |
| Claude Opus | 23 of 24 | 23 of 24 | 20 of 24 |
| Gemini 4 Neon (Medium) | 21 of 24 | 17 of 24 | 13 of 24 |
| Gemini 4 Hydrogen (Medium) | 18 of 24 | 16 of 24 | 10 of 24 |

With the skill, replies started from the customer problems, kept the rebrand to its must-have part, asked what the earlier restructures failed to solve, and rejected ending all contractor and junior roles as a blanket move. Replies without the skill had more factual errors. Details: [`benchmarks/check-v1.3.3/`](benchmarks/check-v1.3.3/benchmark.md).

### Version 1.3: leaders go first, shorter advice for individuals

Seven new cases, each run twice with version 1.3 and twice with version 1.2.1, on Claude Sonnet and Claude Opus, graded blind. Two runs per setup is a small sample, so read the numbers as direction, not precision.

| Case | Model | Version 1.3 | Version 1.2.1 |
|---|---|---|---|
| A flop and a board that wants 15% cuts | Claude Sonnet | 12 of 12 checks | 8 of 12 checks |
| | Claude Opus | 12 of 12 checks | 10 of 12 checks |
| Advice to one person: a PM with a promised feature, an engineer facing a ranking, a CTO after an outage | Claude Sonnet | 34 of 36 checks | 26 of 36 checks |
| | Claude Opus | 36 of 36 checks | 29 of 36 checks |

**What version 1.3 added:**
- where something had gone wrong, a leader in the advice said plainly that the result was theirs in 8 of 8 Sonnet runs (against 3 of 8) and 8 of 8 Opus runs (against 4 of 8);
- after the flop, leadership owned the result and took the first and largest cut in 4 of 4 runs, against 0 of 4 with version 1.2.1, presented as a signal of trust rather than the savings plan;
- advice to one person came in at 430 to 600 words with the first steps and a line they can use; version 1.2.1 wrote 770 to 1,060 words, and most of its missed checks were length;
- runs with a factual error: Opus 0 of 14 (against 2). Sonnet did worse here, 4 of 14 against 2, all minor slips such as saying Germany's notification duty starts above 10% of staff instead of at 10%.

**What didn't separate:** the board that overrules the alternatives, cuts in Germany without a works council, and choosing who stays in a Swedish support team. Both versions wrote the plan when asked, used the right selection rules and flagged the notifications, so those checks barely moved. Token use stayed within about 4% of version 1.2.1.

The first draft of the shorter-replies rule ("the first 300 to 500 words") still let Sonnet run to 600 to 800 words; the final wording ("about 400 words and never more than 500") fixed that, and those three cases were rerun.

### On Gemini

The skills follow the open Agent Skills format, so the seven version 1.3 cases also ran on Gemini through the Antigravity CLI, with and without the skill, two runs per setup, graded blind. Gemini loaded the seat by name (`/the-human-ceo`), so this tests what the skill's content does, not whether Gemini picks it up by itself.

| Model | With the skill | Without the skill |
|---|---|---|
| Gemini 4 Neon (Medium) | 80 of 84 checks | 51 of 84 checks |
| Gemini 4 Hydrogen (Medium) | 75 of 84 checks | 41 of 84 checks |

The skill made a bigger difference on Gemini than on Claude. With the skill, Gemini:
- had a leader own the bad result in 14 of 16 runs where something had gone wrong (against 4 of 16), and after the flop, had leadership take the first and largest cut in 4 of 4 runs (against 0 of 4);
- got the country rules right: Germany's social selection (Sozialauswahl) instead of performance rankings in 4 of 4 runs (against 0 of 4), and Sweden's re-employment priority and transition support in 4 of 4 (against 0 of 4);
- questioned the cut before planning it, in Germany and Sweden alike (8 of 8 against 0 of 8), and ruled out closing a capacity gap with overtime (4 of 4 against 0 of 4);
- made no factual errors in 28 runs, against 6 in 28 without, and wrote replies about 40% shorter (360 words against 630 on average).

**Where it fell short.** In all four runs of the ranking case, Gemini with the skill sent a disagreement about a business decision to the confidential adviser (vertrouwenspersoon). The cause was a channel list in a reference file that put the adviser next to the decision owner and the works council; Claude read it correctly, Gemini didn't. Version 1.3.1 says what the adviser is for, and the same four runs then passed 24 of 24 checks. In the PM case, three of four replies with the skill didn't say to talk to the CEO in private first, where all four without it did. Version 1.3.2 adds that rule to every seat; in a blind rerun, all eight PM replies on Claude and Gemini started with a private conversation ([check](benchmarks/check-v1.3.2/benchmark.md)). Still open: on the ranking case, Gemini tends not to ask the VP what problem the ranking is meant to solve.

**Cost.** On Gemini the skill roughly doubles the tokens per request (about 30,000 against 14,000 to 17,000), because the seat's instructions and the reference files it opens are read on every run.

The harness, every reply and every grade are in [`benchmarks/gemini-v1.3/`](benchmarks/gemini-v1.3/benchmark.md).

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
