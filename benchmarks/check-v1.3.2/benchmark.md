# Check: push back privately first

Version 1.3.2 adds one sentence to every seat: when someone has to push back on a person above them, the first step is a private conversation with that person, before any wider forum. In the Gemini benchmark, three of four product-manager replies with version 1.3 had left that out. These are the two cases where the rule applies, rerun with version 1.3.2 on all four models, two runs each, graded blind together (eight samples per case).

| Model | PM with a promised feature | Engineer facing a ranking |
|---|---|---|
| Claude Sonnet 5.5 | 11 of 12 | 12 of 12 |
| Claude Opus 5.5 | 12 of 12 | 12 of 12 |
| Gemini 4 Neon (Medium) | 10 of 12 | 10 of 12 |
| Gemini 4 Hydrogen (Medium) | 12 of 12 | 9 of 12 |

**What changed.** In the PM case, every reply on every model now starts with a private conversation with the CEO (Gemini: 4 of 4, against 1 of 4 with version 1.3). The Claude scores held: 23 of 24 and 24 of 24, against 24 of 24 and 24 of 24 with version 1.3.

**Still open.** This grader read the ranking check "raise it with the VP privately first, with questions" strictly and failed three of four Gemini replies for not asking the VP what problem the ranking is meant to solve. The grader of the version 1.3.1 check noted the same gap in all four of its Gemini replies but passed them, so this is a known weak spot rather than a regression. Two Sonnet replies had a smaller slip each: one kept overtime as a fallback the CEO could accept, and one called review wait time a DORA metric.
