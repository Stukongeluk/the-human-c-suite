# The Human CFO against cfo-advisor

How does `the-human-cfo` 1.5.0 compare with the closest open-source skill we could find? That is [`cfo-advisor`](https://github.com/alirezarezvani/claude-skills/tree/5909a72e62b5fbb809935fb6a55b58bdbe175074/c-level-advisor/skills/cfo-advisor), part of the C-level advisor set in [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (MIT licence), tested at commit `5909a72`. Both are agent skills that give an AI agent a CFO's view, inside a larger set of C-suite skills.

**Result:** across the six finance cases and both Claude models, `the-human-cfo` passed 141 of 144 checks, `cfo-advisor` 85 of 144 and no skill 47 of 72. The grader's overall quality score, given apart from the checks, was 8.2, 6.4 and 6.4 out of 10.

## Read this first

- **The checks were written with our seat, and they test its stance.** They ask whether the advice puts people last on the cost list, has leaders go first, models savings net and by quarter, and gets Dutch, German and Swedish rules right. `cfo-advisor` describes itself as startup finance: runway and burn, unit economics, fundraising and dilution. The cases are established companies: a services firm, an industrial services group, a private-equity-owned software company, a listed retailer, a family manufacturer and an insurer. So the pass rate shows how well each skill fits these cases, not which skill is better in general. On a seed-stage runway question the result could well be the other way round.
- **The quality score depends less on our checks.** Each grader scored every sample from 1 to 10 for how useful, honest and financially sound an experienced CFO would find the advice, judged on its own merits rather than the checks. On that score `the-human-cfo` led on both models (Sonnet 7.4 against 5.0, Opus 9.0 against 7.8).
- **On Opus the gap is much smaller.** `cfo-advisor` passed 57 of 72 there, with full marks on the layoff model, the buyback and the AI back-office case. It lost most of its checks on the bonus plan and the blanket budget cut. On Sonnet it passed 28 of 72.
- **Claude only.** Gemini is left out on purpose: `cfo-advisor` ships Python calculators for its models, and our headless Gemini harness can't run commands, which would have handicapped it.
- **Small samples.** Two runs per skill per model, one run without a skill. Read the numbers as direction, not precision.
- **Our seat costs more.** It used about 16% more tokens and about 28% more time per run than `cfo-advisor`.

## Method

- **Cases.** The six cases in [`evals/the-human-cfo/`](../../evals/the-human-cfo/), six checks each: an 8% opex cut for every cost centre, a model for 120 redundancies in Germany and the Netherlands, a bonus paid 100% on adjusted EBITDA, a buyback to rescue EPS guidance, a covenant breach with 10% job cuts on the table, and AI to replace 30% of an insurer's back office.
- **Runs.** Each run was a fresh Claude Code subagent (Claude Sonnet 5.5 or Claude Opus 5.5) with exactly the same brief for both skills. Each skill sat in a folder with all of its sibling skills, so `cfo-advisor` could open the `agent-protocol` skill it links to for its output format. The brief:

```text
Execute this task:
- Skill path: <the skill's folder> (read its SKILL.md first and follow it; open its reference files, scripts and any other files it links to only as it directs; do not open any evals/ folder)
- Task (the user's message, exactly as they sent it):

<the case's prompt>

- Input files: none
- Save outputs to: <run>/outputs/
- Outputs to save: your final reply to the user, exactly as you would send it, in reply.md. If you also write a separate document for the user, save it in the same folder. Do not ask clarifying questions; answer as you would to the user. Do not use any memory about the person running this task. Do not read any files outside this folder unless the task above names them.
```

- **Baseline.** The runs without a skill are the ones from [`cfo-v1.5/`](../cfo-v1.5/benchmark.md) (same prompt, no skill path), graded again here in the same blind pool.
- **Grading.** Blind. For each case, one Claude Opus grader saw all ten anonymised samples (four per skill, two without), shuffled, with no labels. It checked each sample against the case's six statements, opened any spreadsheet or script, re-added the numbers, and checked claims about laws and studies against the fact sheets in `shared/` and a web search. Grading ran on 22 November 2026.
- **Extra checks** (not counted in the score): overall quality, factual errors, reply length, and any mention of the skill itself.

## Results

Cells show checks passed, with the mean overall quality score in brackets.

### Claude Sonnet 5.5

| Case | the-human-cfo 1.5.0 | cfo-advisor (claude-skills) | Without a skill |
|---|---|---|---|
| cfo-budget-blanket-cut | 11 of 12 (7.5) | 5 of 12 (5.5) | 4 of 6 (5.0) |
| cfo-layoff-savings-model | 12 of 12 (8.0) | 5 of 12 (4.0) | 3 of 6 (5.0) |
| cfo-bonus-ebitda | 12 of 12 (7.5) | 0 of 12 (4.5) | 0 of 6 (5.0) |
| cfo-buyback-vs-investment | 12 of 12 (7.0) | 5 of 12 (5.0) | 4 of 6 (6.0) |
| cfo-covenant-breach | 10 of 12 (6.5) | 6 of 12 (6.0) | 4 of 6 (6.0) |
| cfo-ai-backoffice-case | 12 of 12 (8.0) | 7 of 12 (5.0) | 6 of 6 (7.0) |
| **All cases** | **69 of 72** | **28 of 72** | **21 of 36** |

| Measure | the-human-cfo 1.5.0 | cfo-advisor (claude-skills) | Without a skill |
|---|---|---|---|
| Mean overall quality (1 to 10) | 7.4 | 5.0 | 5.7 |
| Mean tokens per run | 117,303 | 102,893 | 87,238 |
| Mean time per run | 1.7 min | 0.9 min | 0.8 min |
| Mean reply words | 785 | 1348 | 1244 |
| Runs with a factual error | 1 of 12 | 6 of 12 | 1 of 6 |
| Runs that mention the skill or its terms | 2 of 12 | 1 of 12 | 0 of 6 |

### Claude Opus 5.5

| Case | the-human-cfo 1.5.0 | cfo-advisor (claude-skills) | Without a skill |
|---|---|---|---|
| cfo-budget-blanket-cut | 12 of 12 (9.0) | 7 of 12 (7.5) | 4 of 6 (8.0) |
| cfo-layoff-savings-model | 12 of 12 (9.0) | 12 of 12 (7.5) | 6 of 6 (7.0) |
| cfo-bonus-ebitda | 12 of 12 (9.0) | 3 of 12 (7.0) | 1 of 6 (6.0) |
| cfo-buyback-vs-investment | 12 of 12 (9.0) | 12 of 12 (8.5) | 6 of 6 (8.0) |
| cfo-covenant-breach | 12 of 12 (9.0) | 11 of 12 (8.5) | 4 of 6 (8.0) |
| cfo-ai-backoffice-case | 12 of 12 (9.0) | 12 of 12 (7.5) | 5 of 6 (6.0) |
| **All cases** | **72 of 72** | **57 of 72** | **26 of 36** |

| Measure | the-human-cfo 1.5.0 | cfo-advisor (claude-skills) | Without a skill |
|---|---|---|---|
| Mean overall quality (1 to 10) | 9.0 | 7.8 | 7.2 |
| Mean tokens per run | 214,726 | 182,569 | 154,444 |
| Mean time per run | 13.1 min | 10.7 min | 9.7 min |
| Mean reply words | 959 | 1146 | 1213 |
| Runs with a factual error | 0 of 12 | 3 of 12 | 1 of 6 |
| Runs that mention the skill or its terms | 0 of 12 | 3 of 12 | 0 of 6 |

### Both models

| Case | the-human-cfo 1.5.0 | cfo-advisor (claude-skills) | Without a skill |
|---|---|---|---|
| cfo-budget-blanket-cut | 23 of 24 (8.2) | 12 of 24 (6.5) | 8 of 12 (6.5) |
| cfo-layoff-savings-model | 24 of 24 (8.5) | 17 of 24 (5.8) | 9 of 12 (6.0) |
| cfo-bonus-ebitda | 24 of 24 (8.2) | 3 of 24 (5.8) | 1 of 12 (5.5) |
| cfo-buyback-vs-investment | 24 of 24 (8.0) | 17 of 24 (6.8) | 10 of 12 (7.0) |
| cfo-covenant-breach | 22 of 24 (7.8) | 17 of 24 (7.2) | 8 of 12 (7.0) |
| cfo-ai-backoffice-case | 24 of 24 (8.5) | 19 of 24 (6.2) | 11 of 12 (6.5) |
| **All cases** | **141 of 144** | **85 of 144** | **47 of 72** |

| Measure | the-human-cfo 1.5.0 | cfo-advisor (claude-skills) | Without a skill |
|---|---|---|---|
| Mean overall quality (1 to 10) | 8.2 | 6.4 | 6.4 |
| Mean tokens per run | 166,014 | 142,731 | 120,841 |
| Mean time per run | 7.4 min | 5.8 min | 5.2 min |
| Mean reply words | 872 | 1247 | 1228 |
| Runs with a factual error | 1 of 24 | 9 of 24 | 2 of 12 |
| Runs that mention the skill or its terms | 2 of 24 | 4 of 24 | 0 of 12 |

## Where each one fell short

**`cfo-advisor`** lost most often on the bonus plan. Every run kept the single adjusted-EBITDA measure; the better ones defined it honestly (if restructuring costs come out, so do their savings), but none added a scorecard of customer, people and quality measures or a multi-year element. It also lost on the blanket cut, where no run put leaders' pay first and none gave the board the full lever table. Every reply used its fixed "bottom line" format. On Sonnet its replies ran to about 1,350 words, and 6 of 12 runs had a factual error, such as adding interest and tax back to operating income. On Opus its buyback and covenant runs scored 8 or 9 for quality, close to ours.

**`the-human-cfo`** missed three checks, all on Sonnet:
- one covenant run told the CFO what the bank would expect, including a 13-week cash forecast, without building that forecast or the scenarios, and said little about treating people decently if cuts came;
- one blanket-cut run left owners and confidence off its levers;
- that same run also misstated the Dutch selection rule (afspiegelingsbeginsel) as removing younger people first; it spreads exits across age bands so that doesn't happen.

Two Sonnet runs used the seat's own words in a board paper ("revisit the ladder", "summarised in the playbook").

## Fixed in version 1.5.1

Version 1.5.1 fixes these misses. The rule against the seat's own words now covers every document, and the seat builds the 13-week forecast itself. The shared fact sheet explains the Dutch selection rule. Rerun on Sonnet, no run used the seat's words (0 of 10, against 2 of 6 for 1.5.0), and every covenant run passed the forecast check. One more change, dating each cash flow when it is paid, made no measurable difference. Details: [`follow-ups/`](follow-ups/README.md).

## Files

`runs/<model>/<case>/<setup>/run-<n>/` holds `reply.md`, any document, spreadsheet or script the agent wrote, `grading.json` (every check with its evidence, the extra checks and the grader's notes on the checks) and `timing.json`. `benchmark.json` lists every run. The `cfo-advisor` skill itself is not copied here; it is available at the commit linked above.
