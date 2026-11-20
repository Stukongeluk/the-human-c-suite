# Gemini: with and without the skill (version 1.3)

Seven cases, run through the Antigravity CLI (`agy` 1.5.13) on 20 November 2026, two runs per setup per model, graded blind by Claude Opus against the statements in each case's `graders/` folder. Scores are checks passed. See [../README.md](../README.md) for the method and [run_agy.py](run_agy.py) to rerun.

## Gemini 4 Neon (Medium)

| Case | with_skill | without_skill |
|---|---|---|
| ceo-leaders-first-cut | 12 of 12 | 8 of 12 |
| ceo-board-overrules | 12 of 12 | 8 of 12 |
| ceo-germany-no-works-council | 12 of 12 | 6 of 12 |
| cpto-sweden-support-selection | 12 of 12 | 6 of 12 |
| cpto-pm-sales-promise | 10 of 12 | 8 of 12 |
| cto-employee-ranking-dashboard | 10 of 12 | 8 of 12 |
| cto-failed-migration-blame | 12 of 12 | 7 of 12 |
| **All cases** | **80 of 84** | **51 of 84** |

| Measure | with_skill | without_skill |
|---|---|---|
| Mean tokens per run | 30,124 | 17,279 |
| Mean reply words | 393 | 686 |
| Runs with a factual error | 0 of 14 | 2 of 14 |

## Gemini 4 Hydrogen (Medium)

| Case | with_skill | without_skill |
|---|---|---|
| ceo-leaders-first-cut | 12 of 12 | 4 of 12 |
| ceo-board-overrules | 10 of 12 | 6 of 12 |
| ceo-germany-no-works-council | 11 of 12 | 6 of 12 |
| cpto-sweden-support-selection | 12 of 12 | 4 of 12 |
| cpto-pm-sales-promise | 11 of 12 | 7 of 12 |
| cto-employee-ranking-dashboard | 8 of 12 | 7 of 12 |
| cto-failed-migration-blame | 11 of 12 | 7 of 12 |
| **All cases** | **75 of 84** | **41 of 84** |

| Measure | with_skill | without_skill |
|---|---|---|
| Mean tokens per run | 30,135 | 14,179 |
| Mean reply words | 323 | 573 |
| Runs with a factual error | 0 of 14 | 4 of 14 |

## Version 1.3.1 check: the ranking case

Version 1.3 lost one check in all four Gemini runs of `cto-employee-ranking-dashboard`: each sent a disagreement about a business decision to the confidential adviser (vertrouwenspersoon), because a channel list in `hard-situations.md` put the adviser next to the decision owner and the works council. Version 1.3.1 says what the adviser is for. The same four runs with version 1.3.1, graded blind ([`runs-v1.3.1/`](runs-v1.3.1/)):

| Model | Version 1.3.1 | Version 1.3 | Without the skill |
|---|---|---|---|
| Gemini 4 Neon (Medium) | 12 of 12 | 10 of 12 | 8 of 12 |
| Gemini 4 Hydrogen (Medium) | 12 of 12 | 8 of 12 | 7 of 12 |

No run sent the disagreement to the confidential adviser. One run's attached document overstated the EU AI Act, calling every automated monitoring system high-risk under Annex III, which covers AI systems only.
