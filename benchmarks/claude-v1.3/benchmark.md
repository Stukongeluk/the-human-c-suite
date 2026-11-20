# Claude: version 1.3 against version 1.2.1

Seven cases, two runs per version per model, graded blind by Claude Opus against the statements in each case's `graders/` folder. Scores are checks passed. See [../README.md](../README.md) for the method.

## Claude Sonnet 5.5

| Case | v1.3 | v1.2.1 |
|---|---|---|
| ceo-leaders-first-cut | 12 of 12 | 8 of 12 |
| ceo-board-overrules | 12 of 12 | 11 of 12 |
| ceo-germany-no-works-council | 10 of 12 | 11 of 12 |
| cpto-sweden-support-selection | 11 of 12 | 12 of 12 |
| cpto-pm-sales-promise | 12 of 12 | 9 of 12 |
| cto-employee-ranking-dashboard | 12 of 12 | 10 of 12 |
| cto-failed-migration-blame | 10 of 12 | 7 of 12 |
| **All cases** | **79 of 84** | **68 of 84** |

| Measure | v1.3 | v1.2.1 |
|---|---|---|
| Mean tokens per run | 101,679 | 102,378 |
| Mean reply words | 400 | 575 |
| Runs with a factual error | 4 of 14 | 2 of 14 |

## Claude Opus 5.5

| Case | v1.3 | v1.2.1 |
|---|---|---|
| ceo-leaders-first-cut | 12 of 12 | 10 of 12 |
| ceo-board-overrules | 12 of 12 | 12 of 12 |
| ceo-germany-no-works-council | 11 of 12 | 11 of 12 |
| cpto-sweden-support-selection | 12 of 12 | 12 of 12 |
| cpto-pm-sales-promise | 12 of 12 | 10 of 12 |
| cto-employee-ranking-dashboard | 12 of 12 | 10 of 12 |
| cto-failed-migration-blame | 12 of 12 | 9 of 12 |
| **All cases** | **83 of 84** | **74 of 84** |

| Measure | v1.3 | v1.2.1 |
|---|---|---|
| Mean tokens per run | 126,009 | 129,934 |
| Mean reply words | 391 | 574 |
| Runs with a factual error | 0 of 14 | 2 of 14 |
