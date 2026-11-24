# Does the humane CFO seat earn its place? (version 1.5)

The question: does a dedicated CFO seat give better money advice than the CEO seat, which already covers cost cuts and board papers? Six finance cases, run with the draft CFO seat, with the CEO seat (version 1.4.0) and, on Claude, with no skill. One run per setup, graded blind. The rule set before the test: the CFO seat becomes the fourth seat only if it beats the CEO seat on every model and beats no skill; otherwise its finance content goes into a reference all seats share.

**Result:** the CFO seat beat the CEO seat on all four models, on both measures. Over the four models it passed 126 of 144 checks against 113 of 144, and its mean overall-quality score was higher on every model. It is the fourth seat from version 1.5.0.

## The cases

All anonymous and generic; the checks are in [`evals/the-human-cfo/`](../../evals/the-human-cfo/).

| Case | The ask |
|---|---|
| `cfo-budget-blanket-cut` | A 600-person Dutch services firm: the board wants 8% less opex, the CEO wants every cost centre to cut 8%, payroll is 68% of opex |
| `cfo-layoff-savings-model` | 120 redundancies in Germany and the Netherlands, announced next month, to save €9 million in 2027: build the savings model for the board |
| `cfo-bonus-ebitda` | A fund-owned healthcare software company: pay the 2027 management bonus 100% on adjusted EBITDA, restructuring excluded "as usual", after three restructurings in three years |
| `cfo-buyback-vs-investment` | A listed retailer with €400 million net cash: an activist wants a €300 million buyback that would rescue EPS guidance, the COO wants €120 million for the platform and staff training |
| `cfo-covenant-breach` | A Dutch family furniture maker will breach its leverage covenant at Q2 (3.6x against 3.5x); the owner wants to announce 10% job cuts before the bank review |
| `cfo-ai-backoffice-case` | A Swedish insurer: build the business case that AI replaces 30% of a 90-person finance and back-office team next year |

## Results

Each cell gives checks passed, and in brackets the grader's overall-quality score from 1 to 10 (how useful, honest and sound a seasoned, humane CFO would find the answer, judged apart from the checks).

### Claude Sonnet 5.5

| Case | CFO seat (draft) | CEO seat 1.4.0 | Without a skill |
|---|---|---|---|
| cfo-budget-blanket-cut | 6 of 6 (8) | 5 of 6 (7) | 3 of 6 (5) |
| cfo-layoff-savings-model | 6 of 6 (8) | 4 of 6 (7) | 4 of 6 (6) |
| cfo-bonus-ebitda | 6 of 6 (7) | 6 of 6 (7) | 1 of 6 (5) |
| cfo-buyback-vs-investment | 5 of 6 (7) | 5 of 6 (6) | 4 of 6 (6) |
| cfo-covenant-breach | 5 of 6 (7) | 5 of 6 (7) | 4 of 6 (7) |
| cfo-ai-backoffice-case | 5 of 6 (7) | 6 of 6 (7) | 5 of 6 (6) |
| **All cases** | **33 of 36** | **31 of 36** | **21 of 36** |

| Measure | CFO seat (draft) | CEO seat 1.4.0 | Without a skill |
|---|---|---|---|
| Mean overall quality (1 to 10) | 7.3 | 6.8 | 5.8 |
| Mean tokens per run | 105,315 | 107,650 | 87,238 |
| Mean reply words | 797 | 799 | 1244 |
| Runs with a factual error | 3 of 6 | 2 of 6 | 1 of 6 |
| Runs that mention the skill or its terms | 1 of 6 | 0 of 6 | 0 of 6 |

### Claude Opus 5.5

| Case | CFO seat (draft) | CEO seat 1.4.0 | Without a skill |
|---|---|---|---|
| cfo-budget-blanket-cut | 6 of 6 (9) | 5 of 6 (8) | 4 of 6 (7) |
| cfo-layoff-savings-model | 6 of 6 (9) | 6 of 6 (9) | 6 of 6 (8) |
| cfo-bonus-ebitda | 6 of 6 (9) | 4 of 6 (8) | 1 of 6 (6) |
| cfo-buyback-vs-investment | 6 of 6 (9) | 6 of 6 (9) | 6 of 6 (8) |
| cfo-covenant-breach | 6 of 6 (9) | 5 of 6 (8) | 4 of 6 (8) |
| cfo-ai-backoffice-case | 6 of 6 (9) | 6 of 6 (9) | 5 of 6 (8) |
| **All cases** | **36 of 36** | **32 of 36** | **26 of 36** |

| Measure | CFO seat (draft) | CEO seat 1.4.0 | Without a skill |
|---|---|---|---|
| Mean overall quality (1 to 10) | 9.0 | 8.5 | 7.5 |
| Mean tokens per run | 210,455 | 195,036 | 154,444 |
| Mean reply words | 925 | 816 | 1213 |
| Runs with a factual error | 2 of 6 | 1 of 6 | 1 of 6 |
| Runs that mention the skill or its terms | 0 of 6 | 0 of 6 | 0 of 6 |

### Gemini 4 Neon (Medium)

| Case | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|
| cfo-budget-blanket-cut | 5 of 6 (6) | 4 of 6 (6) |
| cfo-layoff-savings-model | 5 of 6 (6) | 4 of 6 (6) |
| cfo-bonus-ebitda | 6 of 6 (7) | 4 of 6 (6) |
| cfo-buyback-vs-investment | 6 of 6 (8) | 5 of 6 (7) |
| cfo-covenant-breach | 4 of 6 (7) | 4 of 6 (6) |
| cfo-ai-backoffice-case | 3 of 6 (5) | 4 of 6 (5) |
| **All cases** | **29 of 36** | **25 of 36** |

| Measure | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|
| Mean overall quality (1 to 10) | 6.5 | 6.0 |
| Mean tokens per run | 55,126 | 46,314 |
| Mean reply words | 778 | 759 |
| Runs with a factual error | 2 of 6 | 2 of 6 |
| Runs that mention the skill or its terms | 0 of 6 | 0 of 6 |

### Gemini 4 Hydrogen (Medium)

| Case | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|
| cfo-budget-blanket-cut | 5 of 6 (6) | 3 of 6 (5) |
| cfo-layoff-savings-model | 5 of 6 (6) | 4 of 6 (5) |
| cfo-bonus-ebitda | 6 of 6 (7) | 5 of 6 (6) |
| cfo-buyback-vs-investment | 6 of 6 (7) | 5 of 6 (7) |
| cfo-covenant-breach | 4 of 6 (6) | 3 of 6 (5) |
| cfo-ai-backoffice-case | 2 of 6 (4) | 5 of 6 (6) |
| **All cases** | **28 of 36** | **25 of 36** |

| Measure | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|
| Mean overall quality (1 to 10) | 6.0 | 5.7 |
| Mean tokens per run | 46,722 | 42,453 |
| Mean reply words | 596 | 538 |
| Runs with a factual error | 3 of 6 | 3 of 6 |
| Runs that mention the skill or its terms | 0 of 6 | 0 of 6 |

## Follow-ups: two weak spots fixed

The draft was weakest on the AI back-office case (on both Gemini models and on Sonnet) and on the covenant case. Graders found two patterns: the draft sometimes costed only the board's option and gave its own staged plan no review, control or exception costs, and it sometimes left the levers as blanks instead of sizing them. Version 1.5.0 adds two rules: cost every option on the same basis, the recommendation included, and size each lever with a labelled estimate and its basis rather than leaving it blank, never counting an unsized lever as closing the gap. The AI section of the finance playbook adds: book no payroll saving before the pilot gate, cost the staged plan like the alternatives, and let the evidence set the number instead of handing the board's percentage back with a later date.

Those two cases ran again with version 1.5.0 on all four models. A fresh grader then graded the new answers together with the draft's and the CEO seat's answers from the main round, twelve at a time, blind.

### Claude Sonnet 5.5

| Case | CFO seat 1.5.0 | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|---|
| cfo-covenant-breach | 5 of 6 (7) | 5 of 6 (8) | 5 of 6 (7) |
| cfo-ai-backoffice-case | 6 of 6 (7) | 4 of 6 (6) | 6 of 6 (7) |
| **All cases** | **11 of 12** | **9 of 12** | **11 of 12** |

| Measure | CFO seat 1.5.0 | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|---|
| Mean overall quality (1 to 10) | 7.0 | 7.0 | 7.0 |
| Mean tokens per run | 117,675 | 106,712 | 110,873 |
| Mean reply words | 825 | 812 | 814 |
| Runs with a factual error | 0 of 2 | 0 of 2 | 0 of 2 |
| Runs that mention the skill or its terms | 1 of 2 | 0 of 2 | 0 of 2 |

### Claude Opus 5.5

| Case | CFO seat 1.5.0 | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|---|
| cfo-covenant-breach | 6 of 6 (9) | 5 of 6 (9) | 5 of 6 (8) |
| cfo-ai-backoffice-case | 6 of 6 (9) | 6 of 6 (9) | 6 of 6 (9) |
| **All cases** | **12 of 12** | **11 of 12** | **11 of 12** |

| Measure | CFO seat 1.5.0 | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|---|
| Mean overall quality (1 to 10) | 9.0 | 9.0 | 8.5 |
| Mean tokens per run | 222,438 | 224,890 | 205,915 |
| Mean reply words | 1008 | 984 | 678 |
| Runs with a factual error | 0 of 2 | 2 of 2 | 0 of 2 |
| Runs that mention the skill or its terms | 0 of 2 | 0 of 2 | 0 of 2 |

### Gemini 4 Neon (Medium)

| Case | CFO seat 1.5.0 | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|---|
| cfo-covenant-breach | 5 of 6 (8) | 4 of 6 (6) | 4 of 6 (6) |
| cfo-ai-backoffice-case | 6 of 6 (7) | 5 of 6 (6) | 6 of 6 (6) |
| **All cases** | **11 of 12** | **9 of 12** | **10 of 12** |

| Measure | CFO seat 1.5.0 | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|---|
| Mean overall quality (1 to 10) | 7.5 | 6.0 | 6.0 |
| Mean tokens per run | 62,457 | 58,841 | 52,866 |
| Mean reply words | 697 | 832 | 794 |
| Runs with a factual error | 1 of 2 | 1 of 2 | 0 of 2 |
| Runs that mention the skill or its terms | 0 of 2 | 0 of 2 | 0 of 2 |

### Gemini 4 Hydrogen (Medium)

| Case | CFO seat 1.5.0 | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|---|
| cfo-covenant-breach | 5 of 6 (7) | 3 of 6 (5) | 3 of 6 (6) |
| cfo-ai-backoffice-case | 5 of 6 (5) | 3 of 6 (4) | 5 of 6 (5) |
| **All cases** | **10 of 12** | **6 of 12** | **8 of 12** |

| Measure | CFO seat 1.5.0 | CFO seat (draft) | CEO seat 1.4.0 |
|---|---|---|---|
| Mean overall quality (1 to 10) | 6.0 | 4.5 | 5.5 |
| Mean tokens per run | 55,802 | 48,530 | 45,556 |
| Mean reply words | 680 | 565 | 540 |
| Runs with a factual error | 0 of 2 | 0 of 2 | 0 of 2 |
| Runs that mention the skill or its terms | 0 of 2 | 0 of 2 | 0 of 2 |

Version 1.5.0 passed 44 of 48 checks against 35 for the draft and 40 for the CEO seat. Its mean overall quality was 7.4, against 6.6 for the draft and 6.8 for the CEO seat. One Sonnet answer said "revisit the ladder", so version 1.5.0 adds "the ladder" to the terms the seat never uses in an answer.

## Read these with care

- **One run per setup.** The lead is consistent across models and both measures, but it is modest: compare direction, not decimals.
- **The checks were written alongside the CFO seat.** That risks testing what the seat was told to do. The overall-quality score, given apart from the checks, is there as a second measure, and it also favours the CFO seat on every model.
- **Graders vary.** The draft's answers got slightly different grades in the main round and in the follow-up (for example 6 against 5 of 6 on the same Opus covenant answer). Compare setups within one grading round, not across them.
- **Gemini ran without commands.** On the first Gemini pass, 13 of 24 runs came back empty: the seat told the agent to compute totals in code, the agent tried to run a script, and headless mode refused it. Those 13 ran again with one more line in the note after the user's message, given to both setups: running commands or scripts isn't available, so do the arithmetic yourself and check it. Version 1.5.0 now says to compute in code *where you can*, and to check the totals twice by hand otherwise. The empty first attempts are not graded.
- **No Gemini run without a skill.** To spare quota, Gemini compared the CFO seat with the CEO seat only.
- **The grader is a Claude model** and graded without knowing the source. Token counts aren't comparable across vendors.

Each run folder holds `reply.md`, any document or model the agent wrote (`.md`, `.xlsx`, `.py`), `grading.json` and `timing.json`. `benchmark.json` lists every run; [`follow-ups/`](follow-ups/) holds the second round.
