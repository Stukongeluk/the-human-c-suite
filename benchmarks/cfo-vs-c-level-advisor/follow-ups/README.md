# Follow-ups: version 1.5.1

The comparison with `cfo-advisor` showed four weak spots in `the-human-cfo` 1.5.0, all on Claude Sonnet:

- two board papers used the seat's own words ("revisit the ladder", "summarised in the playbook");
- one covenant reply said the bank would expect a 13-week cash forecast instead of building one, and said little about treating people decently if cuts came;
- one budget reply said the Dutch selection rule (afspiegelingsbeginsel) removes younger people first, which is the opposite of what it does.

Version 1.5.1 makes four changes:

1. **Plain words in every document.** The rule against the seat's own terms now stands on its own line. It covers the reply and every document, names "the playbook" and "the templates", and asks for a check before handing a document over.
2. **Build the cash forecast.** For a cash, runway or covenant problem, the seat builds the 13-week forecast and the base and downside cases with their headroom itself, with labelled estimates.
3. **The Dutch selection rule explained.** The shared fact sheet now says how afspiegeling works, so all four seats have it. It applies per group of interchangeable jobs at each business location: five age bands, the same age mix before and after, the shortest-serving first within each band. Sources: [Rijksoverheid](https://www.rijksoverheid.nl/onderwerpen/ontslag/afspiegelingsbeginsel) and [UWV](https://www.uwv.nl/werkgevers/werkgever-en-ontslag/ik-wil-ontslag-aanvragen/detail/ontslag-via-uwv/ontslagaanvraag-wegens-bedrijfseconomische-redenen/rekening-houden-met-de-ontslagvolgorde-afspiegelingsbeginsel).
4. **Cash in the right quarter.** Each cash flow is dated when it is paid, temporary measures stay out of run-rates, and the reply quotes the figures the code gives. The draft had changes 1 to 3, plus a line that any involuntary reductions come with a fair package and support from the day of notice; change 4 came after round 1.

## Round 1: the draft against 1.5.0

Claude Sonnet 5.5 reran the draft on the three cases with misses: four runs each on the AI back-office and covenant cases, two on the blanket cut. These were graded blind in one pool per case with the two 1.5.0 Sonnet runs from the comparison.

| Case | 1.5.1 draft | 1.5.0 |
|---|---|---|
| cfo-ai-backoffice-case | 24 of 24 checks (quality 8.0) | 12 of 12 (7.5) |
| cfo-covenant-breach | 22 of 24 (7.5) | 10 of 12 (7.5) |
| cfo-budget-blanket-cut | 11 of 12 (7.5) | 11 of 12 (8.0) |
| Runs that used the seat's own words | 0 of 10 | 2 of 6 |

- **Jargon:** fixed. No draft run used the seat's terms; both 1.5.0 back-office runs did.
- **Forecast:** every draft covenant run passed the forecast check. The 1.5.0 run that had missed it missed it again.
- **Selection rule:** the error did not come back.
- **Cash timing:** the graders still flagged slips on both versions. They found one-off cash counted before it is paid and a one-year pay cut inside a run-rate, plus a few ratios that didn't follow from the reply's own inputs. That led to change 4.

## Round 2: 1.5.1 against the draft

Three Sonnet runs each on the covenant and blanket-cut cases with change 4, graded blind in one pool with the draft runs from round 1.

| Case | 1.5.1 | 1.5.1 draft |
|---|---|---|
| cfo-covenant-breach | 18 of 18 checks (quality 7.7) | 22 of 24 (7.8) |
| cfo-budget-blanket-cut | 17 of 18 (7.3) | 11 of 12 (8.0) |
| Runs with a factual error | 4 of 6 | 2 of 6 |

Change 4 made no measurable difference. The checks were about the same and so were the quality scores, and arithmetic or timing slips still turned up in some runs on both versions. The same draft runs drew different factual-error verdicts from different graders (round 1 found errors in five of six, round 2 in two), so this measure is noisy at this sample size. We kept the change because it describes correct practice and did no harm on the checks. Making every illustrative number consistent remains the main open point for Sonnet.

Opus wasn't rerun; it passed 72 of 72 with 1.5.0.

## Files

`round-1/` and `round-2/` each hold `benchmark.json` and `runs/sonnet/<case>/<setup>/run-<n>/` with the reply, any documents, `grading.json` and `timing.json`. A run that appears in both rounds was graded again in the second pool, so its two `grading.json` files can differ.
