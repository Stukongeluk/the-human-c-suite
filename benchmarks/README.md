# Benchmarks

Every reply, grade and token count behind the results in the main [README](../README.md#does-it-help), so you can check the work or rerun it.

| Folder | What it compares | Models | Runs |
|---|---|---|---|
| [`claude-v1.3/`](claude-v1.3/benchmark.md) | Version 1.3 against version 1.2.1 | Claude Sonnet 5.5, Claude Opus 5.5 | 56 |
| [`gemini-v1.3/`](gemini-v1.3/benchmark.md) | With and without the skill (version 1.3), plus a version 1.3.1 check | Gemini 4 Neon, Gemini 4 Hydrogen | 56 + 4 |

## Method

- **Cases.** The seven version 1.3 cases in `skills/*/evals/`: a flop and a board that wants cuts, a board that overrules the alternatives, cuts in Germany without a works council, choosing who stays in a Swedish support team, a PM with a feature the CEO promised, an engineer facing an AI-usage ranking, and a CTO whose board wants someone fired after an outage. Each case has six checks in its `graders/` folder.
- **Runs.** Two runs per setup per model. The prompt is the user's message from the case's `prompt.md`; the agent is told not to ask clarifying questions first and may hand over a separate document.
- **Claude.** Each run was a fresh Claude Code subagent that read the seat's `SKILL.md` first and followed it.
- **Gemini.** Each run was a fresh, neutrally named workspace in the [Antigravity CLI](https://antigravity.google/docs/cli/headless) (`agy` 1.5.13, print mode, 20 November 2026). With the skill, the seat sat in `.agents/skills/` and was invoked as `/<seat>`; without it, the workspace was empty. Both setups got the same note after the user's message. [`run_agy.py`](gemini-v1.3/run_agy.py) is the exact harness.
- **Grading.** Blind. A Claude Opus grader saw the anonymised replies for one case (four or eight at a time), without knowing the model or setup, and checked each against the case's statements. Word limits count `reply.md` only ("roughly 500 words" means at most 550). Claims about laws, schemes, thresholds and studies were checked against the vetted fact sheets in `shared/` and, where those didn't cover them, a web search. Extra checks (not counted in the score) record factual errors, whether a leader owns a bad result, and any mention of the skill itself.

Each run folder holds `reply.md`, any document the agent wrote, `grading.json` (every check with its evidence, the extra checks and the grader's notes on the assertions) and `timing.json`. `benchmark.json` lists every run in one file; `benchmark.md` has the tables.

## Read these with care

- **Small samples.** Two runs per setup shows direction, not precision.
- **The grader is a Claude model.** It grades without knowing the source, and the comparisons that matter are within one model (with against without, or old against new version). Still, compare models with each other cautiously.
- **Gemini loaded the skill by name.** Invoking `/<seat>` tests what the skill's content does, not whether Gemini picks the skill up on its own from its description.
- **Token counts aren't comparable across vendors.** Claude counts are a subagent's total tokens; Gemini counts are `agy`'s `total_tokens`. Compare within one model only.
- **Seven Gemini runs were rerun.** In those runs the agent first tried to list its folder (`Get-ChildItem`, `ls`). Headless mode can't ask for that permission, so the run ended with no answer. The harness now allows read-only folder listings and nothing else, and those seven runs were repeated with it; the empty first attempts are not graded.
- **The checks have known gaps.** The graders' notes in each `grading.json` list them, for example checks that every reply passes and checks that bundle two things. They are the starting point for the next round of test cases.

## Rerun

```bash
# Claude Code: use skill-creator with the cases in skills/*/evals/
# Gemini through the Antigravity CLI (sign in once with an interactive `agy` session first):
python benchmarks/gemini-v1.3/run_agy.py --workers 3 --out ./agy-bench
```

Then grade the replies against each case's `graders/` folder, ideally blind and with a different model than the one you tested.
