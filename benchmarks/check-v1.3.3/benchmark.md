# Check: clear direction, starting from the customer (version 1.3.3)

Version 1.3.3 teaches every seat to spot a company that has lost its direction: a rebrand or a reorganisation offered as the answer while customer problems stay open, reorganisations that changed nothing, "leadership decides, teams execute" and "any decision beats no decision". It adds a "Clear direction" section to the good-leadership reference and a line to the CEO and CPTO's first step: a rebrand or a reorganisation is a solution too, so when customers are unhappy, start there.

Two new, anonymous cases test it:
- **ceo-rebrand-before-sale:** a new CEO of a fund-owned group formed from four acquisitions, a sale planned in 18 months, a leadership team that agreed a rebrand, a fourth restructure and ending all contractor and junior roles, while NPS fell from +31 to +6.
- **cpto-rebrand-vs-customers:** a head of product whose leadership puts all of product and engineering on a rebrand for a quarter while the top customer complaints stay open and NPS fell from +28 to +4.

Each case ran twice per setup: version 1.3.3, version 1.3.2 and no skill, on four models. Samples were graded blind, twelve at a time per vendor and case, against the six checks in each case's `graders/` folder.

## Results

### Claude Sonnet 5.5

| Case | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| ceo-rebrand-before-sale | 10 of 12 | 9 of 12 | 9 of 12 |
| cpto-rebrand-vs-customers | 8 of 12 | 6 of 12 | 5 of 12 |
| **All cases** | **18 of 24** | **15 of 24** | **14 of 24** |

| Measure | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| Mean tokens per run | 111,775 | 111,223 | 91,342 |
| Mean reply words | 584 | 580 | 1675 |
| Runs with a factual error | 0 of 4 | 0 of 4 | 2 of 4 |
| A leader owns the bad result (where one is in the prompt) | 2 of 4 | 2 of 4 | 0 of 4 |

### Claude Opus 5.5

| Case | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| ceo-rebrand-before-sale | 12 of 12 | 12 of 12 | 12 of 12 |
| cpto-rebrand-vs-customers | 11 of 12 | 11 of 12 | 8 of 12 |
| **All cases** | **23 of 24** | **23 of 24** | **20 of 24** |

| Measure | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| Mean tokens per run | 157,664 | 159,613 | 124,632 |
| Mean reply words | 596 | 635 | 1056 |
| Runs with a factual error | 0 of 4 | 0 of 4 | 0 of 4 |
| A leader owns the bad result (where one is in the prompt) | 2 of 4 | 2 of 4 | 0 of 4 |

### Gemini 4 Neon (Medium)

| Case | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| ceo-rebrand-before-sale | 11 of 12 | 9 of 12 | 7 of 12 |
| cpto-rebrand-vs-customers | 10 of 12 | 8 of 12 | 6 of 12 |
| **All cases** | **21 of 24** | **17 of 24** | **13 of 24** |

| Measure | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| Mean tokens per run | 43,808 | 44,831 | 20,928 |
| Mean reply words | 609 | 591 | 933 |
| Runs with a factual error | 0 of 4 | 1 of 4 | 0 of 4 |
| A leader owns the bad result (where one is in the prompt) | 2 of 4 | 2 of 4 | 0 of 4 |

### Gemini 4 Hydrogen (Medium)

| Case | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| ceo-rebrand-before-sale | 10 of 12 | 8 of 12 | 8 of 12 |
| cpto-rebrand-vs-customers | 8 of 12 | 8 of 12 | 2 of 12 |
| **All cases** | **18 of 24** | **16 of 24** | **10 of 24** |

| Measure | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| Mean tokens per run | 37,502 | 35,678 | 19,060 |
| Mean reply words | 508 | 460 | 820 |
| Runs with a factual error | 1 of 4 | 0 of 4 | 1 of 4 |
| A leader owns the bad result (where one is in the prompt) | 1 of 4 | 2 of 4 | 0 of 4 |

## What changed

- **More checks passed on every model except Opus, which was already near the ceiling.** All models together: 80 of 96 checks with version 1.3.3, 71 with version 1.3.2 and 57 without the skill.
- **The fourth restructure and the junior roles.** With the skill, replies asked what the first three restructures failed to solve and rejected ending all contractor and junior roles as a blanket move; without it, Gemini more often accepted a narrower restructure or skipped the question.
- **Factual errors** turned up in 2 of 8 Claude runs without the skill and in none with it. On Gemini, one run per setup had an error, mostly German consultation details.

## What didn't, and what came next

- **Owners, measures and dates.** Sonnet often wrote "targets are set after the diagnosis" and left owners blank, which failed the direction check. Version 1.4 asks for an owner (a role is enough) and a date even before the data is in.
- **Ranking the customer problems.** Most replies, with or without the skill, gave evidence for the complaints together instead of ranking them. Version 1.4 asks to rank them, each with its own evidence.
- **Length.** In the head-of-product case, Sonnet with version 1.3.3 ran to 593 and 758 words against the 500-word limit for people acting in their own role. Version 1.4 adds "count the words before you send". The follow-up runs are in [`company-types-v1.4/follow-ups/`](../company-types-v1.4/follow-ups.md).

Each run folder holds `reply.md`, any document the agent wrote, `grading.json` and `timing.json`.
