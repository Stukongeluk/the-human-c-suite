# The Human C-Suite

**Agent skills for running a company without losing your humanity.**

Five skills that act as a humane, technically fluent leadership team: a CEO, a CFO, a CTO, a CPTO and a CHRO. Bring them the decisions that affect people's jobs or a company's long-term health: cost cuts and layoffs, AI rollouts and AI spend, roadmaps and capacity, budgets and covenants, reviews and forced ranking, pay gaps and return to office. You get a usable answer in the format you asked for, and a seat that coaches you through the decision instead of handing you the shortcut.

## The seats

- **`the-human-ceo`**: cost cuts, layoffs, reorgs, outsourcing, AI rollouts, shareholder pressure and board papers, with the whole company in view and layoffs as the last rung of a cost ladder.
- **`the-human-cfo`**: budgets, savings and layoff business cases, cash, covenants, buybacks, bonus plans and AI business cases, with every saving shown net of its costs and by quarter.
- **`the-human-cto`**: AI coding tools and spend, engineering metrics, platform and vendor choices, tech debt and on-call, with AI gains measured rather than taken from vendor claims.
- **`the-human-cpto`**: roadmaps, features promised by sales, the AI story for the board and AI features, with plans that fit real capacity and a no backed by evidence.
- **`the-human-chro`**: reviews and calibration, layoff selection, return to office, pay gaps and pay transparency, AI in hiring, monitoring and burnout, with fair process before speed.

The seats know each other. When a question crosses seats, the one you asked brings in the others' view and shows where they disagree.

## What every seat does

- Builds a picture of the company before it advises, from the sources your session can reach, and dates and checks each fact.
- Treats layoffs as a last resort, after waste, revenue, focus, redeployment, shared sacrifice and voluntary exits.
- Measures AI against a baseline before banking on it, and moves people to valuable work when AI takes over tasks.
- Judges teams and systems rather than individuals, and uses aggregated people data only.
- Knows European and Nordic practice, such as works councils, short-time work and consultation duties.
- States its assumptions, says what would change its mind, and invites pushback.

## Try it

- "The board wants 15% cost savings by Q3. What are our options?"
- "We'll breach our leverage covenant at Q2 and the owner wants to announce 10% job cuts before the bank meeting. What should we do?"
- "The board read that AI makes developers twice as fast. Draft a plan for 25% lower engineering costs."
- "Sales needs these five features by March to close their pipeline. Build the Q1 roadmap."
- "Our CEO wants forced ranking: 10% of every team in the bottom category and out by Q3. Design the process."

A seat loads on its own when a request matches. You can also call one by name, for example `/the-human-c-suite:the-human-cto`.

## Install in Claude Code

```bash
/plugin install the-human-c-suite --marketplace Stukongeluk/the-human-c-suite
```

On Claude Code before 2.1.275, add the marketplace first with `/plugin marketplace add Stukongeluk/the-human-c-suite`, then run `/plugin install the-human-c-suite@the-human-c-suite`.

## What this plugin contains and runs

Only skills: Markdown instructions and reference files. There are no hooks, MCP servers, commands, agents or scripts, and the plugin sends nothing anywhere by itself. When a seat needs facts, it uses the tools your session already has, such as the connectors you have connected (Jira, a data warehouse, finance or HR systems) and web search. Every seat is read-only by default: it changes nothing in your systems and sends no messages to staff without your explicit approval.

## More

Benchmarks, the full documentation and the source are on [GitHub](https://github.com/Stukongeluk/the-human-c-suite). The story behind it is on [jimmynguyen.nl](https://jimmynguyen.nl/projects/the-human-c-suite).

MIT licence, © 2026 Jimmy Nguyen.
