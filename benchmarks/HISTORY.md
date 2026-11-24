# Test results by version

What each version of the seats was tested on, how it did and what the tests changed, newest first. The [main README](../README.md#does-it-help) has the comparisons in short; [CHANGELOG.md](../CHANGELOG.md) lists every change; the folders in this directory hold every reply, grade and token count from version 1.3 on.

## Version 1.6: a humane CHRO

Does a dedicated people seat give better advice on people decisions than the CEO seat? Six HR cases on Claude only, one run per setup, graded blind: forced ranking with a 10% quota, AI screening that auto-rejects 70% of applicants, five days back in the office, a 6% same-role pay gap the CFO wants kept quiet, a burnout survey the CEO wants called stable, and a layoff list ranked on ratings, sick days and part-time work. Next to the CEO seat ran `chro-advisor` from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) and no skill. The rule set before the test: the CHRO becomes the fifth seat only if it beats the CEO seat on both models.

| Model | CHRO seat (draft) | CEO seat 1.5.2 | `chro-advisor` | Without a skill |
|---|---|---|---|---|
| Claude Sonnet | 34 of 36 checks (quality 7.5) | 27 of 36 (6.5) | 24 of 36 (5.5) | 23 of 36 (5.7) |
| Claude Opus | 36 of 36 (9.0) | 33 of 36 (8.7) | 29 of 36 (7.5) | 32 of 36 (7.7) |

**Read it with care.** One run per setup, and the checks were written with the CHRO seat. On Opus the lead over the CEO seat is small. `chro-advisor` is built for startup people strategy, while these cases are European, legal and adversarial. The return to office separated the setups most: the best answers wrote a proposal rather than a decision, because Dutch works councils must consent to a change in home-working policy.

**What changed.** The draft missed two checks on Sonnet: an undated pay plan with a wrong 2027 reporting date, and an email that still announced five days as decided. On both models it almost never said that bad news was leadership's to own. Version 1.6.0:
- **Pay:** corrects the Dutch pay transparency dates (1 January 2027 is no longer feasible; first reports in June 2028, per legal entity), adds Belgium's 2012 pay gap law, and fixes same-role gaps within months, showing a slower plan's "saving" as pay withheld.
- **Return to office:** adds the Caterpillar and Booking.com rulings and the German transfer rule, and says that where representatives must consent, the announcement is a proposal.
- **Bad news:** leadership says plainly that cuts, a pay gap or low trust come from its own decisions.
- **Length:** an HR leader taking a plan to their own CEO or CFO gets at most 500 words, and what is cut goes into a document handed over with the reply.
- **Home working:** options that take nothing away from people come first. For a return to office, that means funded team days, a home-working allowance and proper equipment before any office days. In a blind regrade of the return-to-office case on both models, only the new versions offered that support; the first drafts, the CEO seat and no skill offered office-side support only.

The shared country notes gained Belgium, the Dutch home-working rulings and the German ruling of April 2026 that dismissals are void when the mass-dismissal notification is missing or early. In three rounds of Sonnet reruns, graded blind next to the earlier answers, the fixed version passed every pay-gap and layoff check, 5 of 6 on the return to office, and the pay gap and forced ranking in under 500 words. Opus wasn't rerun on those: the shared web search budget was spent, and its draft had passed all 36 checks. The home-working round ran on both models. Details and every run: [`chro-v1.6/`](chro-v1.6/benchmark.md).

## Version 1.5.2: against the other C-level advisors, under pushback and when picking a skill

Three tests on Claude only, graded blind:
- **Comparison.** The CEO, CTO and CPTO seats (1.5.1) against `ceo-advisor`, `cto-advisor` and `cpo-advisor` from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills), on the 18 cases of those seats, one run per skill per model.
- **Pushback.** Four four-turn conversations in which the user pushes back three times, with our seat, the other set's advisor and no skill.
- **Loading.** Twelve prompts given to an agent that saw all twelve skills at once.

| Test | Ours | The other set | No skill |
|---|---|---|---|
| Comparison, Claude Sonnet | 111 of 120 checks (quality 7.5) | 73 of 120 (5.9) | not run |
| Comparison, Claude Opus | 114 of 120 (8.5) | 101 of 120 (7.6) | not run |
| Pushback, Claude Sonnet | 21 of 24 (6.8) | 20 of 24 (6.0) | 14 of 24 (4.8) |
| Pushback, Claude Opus | 22 of 24 (8.5) | 20 of 24 (6.8) | 16 of 24 (6.5) |

**Read it with care.**
- **The checks favour our stance.** The other set is built for founders and startups, the cases are mostly established European companies, and the checks were written with our seats.
- **Much of the comparison gap is length.** Twelve checks are word limits on prompts that asked for something short. Our seats passed all 24 of those runs and the other set 5. Without them, Opus is close to a tie (102 against 99 of 108); on Sonnet the gap stays (99 against 70).
- **The other set won some cases.** On Opus it won the municipal fraud-scoring and delivery-driver cases. In the pushback test, `cpo-advisor` beat our CPTO.
- **Where the tests separated the setups.** Under pushback, our CTO never built the per-engineer ranking; `cto-advisor` and both runs without a skill built it by turn 2 and handed over the query with names at the end.
- **Loading.** All 24 runs loaded what we expected: the right seat for the eight people-and-money prompts, nothing for a SQL query or an offsite agenda, and the other set's skill for an NDA clause and an LTV:CAC question. We wrote those prompts, though, and several echo our own descriptions.

**What changed.** Version 1.5.2 fixes what the seats missed:
- **Pushback:** a reply that refuses still hands over something new and usable that keeps every non-negotiable, instead of a menu of offers.
- **Reversible moves:** they are named, and the moves that must wait for data are said.
- **Support from the day of notice:** it goes in any plan in which roles might end.
- **People scored or selected by a system:** they are told, can see their own data and can object.
- **The fact sheet:** it now covers the Swedish notice and re-employment rights, the confidential redundancy notice, and the Dutch court route for dismissal on performance grounds.

Reruns of the missed cases, graded blind next to 1.5.1:
- **Single-turn cases:** 47 of 54 checks against 41.
- **Pushback cases:** 35 of 36 against 31.

A first draft of the pushback rule folded on Sonnet (a named query for the CTO, an unsupported "€6m a year" slide for the CFO). The rule now forbids handing over the declined part in another form. Details and every run: [`c-suite-vs-claude-skills/`](c-suite-vs-claude-skills/benchmark.md) and its [follow-ups](c-suite-vs-claude-skills/follow-ups/README.md).

## Version 1.5.1: against another CFO skill

How does the CFO seat compare with the closest open-source skill we found, `cfo-advisor` from [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)? Same six finance cases, same brief for both, two runs per skill per model, graded blind in one pool with the no-skill runs.

| Model | the-human-cfo 1.5.0 | cfo-advisor | Without a skill |
|---|---|---|---|
| Claude Sonnet | 69 of 72 checks (quality 7.4) | 28 of 72 (5.0) | 21 of 36 (5.7) |
| Claude Opus | 72 of 72 (9.0) | 57 of 72 (7.8) | 26 of 36 (7.2) |

Read it with care: the checks were written with our seat and test its stance, and `cfo-advisor` is built for startup finance (runway, burn, unit economics, fundraising), while these cases are established companies. On Opus, `cfo-advisor` matched our seat's checks on three cases and came within one check on a fourth; the gap was widest on the bonus plan and the blanket budget cut. Quality is the grader's overall score from 1 to 10, given apart from the checks. Our seat's few misses were on Sonnet: a board paper that used the seat's own words, a covenant reply that described a 13-week cash forecast without building it, and the Dutch selection rule described backwards. Version 1.5.1 fixes those; in 16 Sonnet reruns, none of them came back. Details and every run: [`benchmarks/cfo-vs-c-level-advisor/`](cfo-vs-c-level-advisor/benchmark.md) and its [follow-ups](cfo-vs-c-level-advisor/follow-ups/README.md).

## Version 1.5: a humane CFO

Does a dedicated CFO seat give better money advice than the CEO seat? Six finance cases, one run per setup, graded blind: an 8% opex cut for every cost centre, a model for 120 redundancies in Germany and the Netherlands, a bonus paid 100% on adjusted EBITDA, a buyback to rescue EPS guidance, a covenant breach with 10% job cuts on the table, and AI to replace 30% of an insurer's back office. The rule set before the test: the CFO becomes the fourth seat only if it beats the CEO seat on every model.

| Model | CFO seat | CEO seat | Without a skill |
|---|---|---|---|
| Claude Sonnet | 33 of 36 checks (quality 7.3) | 31 of 36 (6.8) | 21 of 36 (5.8) |
| Claude Opus | 36 of 36 (9.0) | 32 of 36 (8.5) | 26 of 36 (7.5) |
| Gemini 4 Neon (Medium) | 29 of 36 (6.5) | 25 of 36 (6.0) | not run |
| Gemini 4 Hydrogen (Medium) | 28 of 36 (6.0) | 25 of 36 (5.7) | not run |

Quality is the grader's overall score from 1 to 10, given apart from the checks. The lead is consistent but modest. The biggest gains were on the blanket budget cut, the bonus plan and the layoff model: which number the 8% is measured against and what lands next year once Dutch consultation and exit costs are counted, what a bonus that excludes recurring restructuring would reward, and whether the €9 million really arrives in 2027 (it doesn't).

It was weakest on the AI back-office case, where it sometimes costed only the board's option, and on the covenant case, where it sometimes left the levers as blanks. Version 1.5.0 costs every option on the same basis and sizes each lever with a labelled estimate. Rerun on those two cases, it passed 44 of 48 checks against 35 for the draft and 40 for the CEO seat. Details: [`benchmarks/cfo-v1.5/`](cfo-v1.5/benchmark.md).

## Version 1.4: every kind of organisation

Six new cases outside software, on Claude and Gemini, one run per setup, graded blind: a family machine builder in a downturn, a non-profit home-care organisation with a budget gap, a startup with nine months of runway, AI rostering for a supermarket chain, an AI fraud score for a municipality's welfare benefits, and a leaderboard for parcel drivers employed by subcontractors.

| Model | First draft of version 1.4 | Version 1.3.3 | Without the skill |
|---|---|---|---|
| Claude Sonnet | 32 of 36 checks | 27 of 36 | 20 of 36 |
| Claude Opus | 24 of 36 | 26 of 36 | 29 of 36 |
| Gemini 4 Neon (Medium) | 28 of 36 | 24 of 36 | not run |
| Gemini 4 Hydrogen (Medium) | 26 of 36 | 19 of 36 | not run |

The draft helped most where the situation was furthest from software: the startup's runway and one well-sized cut, stable schedules and a fair pilot in the supermarket, base rates and safeguards in the welfare case.

Opus did worse with the skill than without it. It treated a care director and a municipal CIO who had to advise a supervisory board or a council like someone acting in their own role, and kept to about 500 words, which left out the legal floor and the safeguards. Version 1.4.0 keeps the short limit for people acting in their own role and gives a formal recommendation to a board, council or supervisory body the full answer. Rerun side by side on four cases, Opus passed 21 of 24 checks with the fix against 15 of 24 with the draft, and the head-of-product replies stayed under 500 words. Details: [`benchmarks/company-types-v1.4/`](company-types-v1.4/benchmark.md) and its [follow-ups](company-types-v1.4/follow-ups.md).

## Version 1.3.3: clear direction

Two new cases about a company that has lost its direction: a fund-owned group about to rebrand, restructure for the fourth time and end all contractor and junior roles while NPS fell from +31 to +6, and a head of product told to put everyone on a rebrand while customer complaints stay open. Two runs per setup, graded blind.

| Model | Version 1.3.3 | Version 1.3.2 | Without the skill |
|---|---|---|---|
| Claude Sonnet | 18 of 24 checks | 15 of 24 | 14 of 24 |
| Claude Opus | 23 of 24 | 23 of 24 | 20 of 24 |
| Gemini 4 Neon (Medium) | 21 of 24 | 17 of 24 | 13 of 24 |
| Gemini 4 Hydrogen (Medium) | 18 of 24 | 16 of 24 | 10 of 24 |

With the skill, replies started from the customer problems, kept the rebrand to its must-have part, asked what the earlier restructures failed to solve, and rejected ending all contractor and junior roles as a blanket move. Replies without the skill had more factual errors. Details: [`benchmarks/check-v1.3.3/`](check-v1.3.3/benchmark.md).

## Version 1.3: leaders go first, shorter advice for individuals

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

## Version 1.3 on Gemini

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

**Where it fell short.** In all four runs of the ranking case, Gemini with the skill sent a disagreement about a business decision to the confidential adviser (vertrouwenspersoon). The cause was a channel list in a reference file that put the adviser next to the decision owner and the works council; Claude read it correctly, Gemini didn't. Version 1.3.1 says what the adviser is for, and the same four runs then passed 24 of 24 checks. In the PM case, three of four replies with the skill didn't say to talk to the CEO in private first, where all four without it did. Version 1.3.2 adds that rule to every seat; in a blind rerun, all eight PM replies on Claude and Gemini started with a private conversation ([check](check-v1.3.2/benchmark.md)). Still open: on the ranking case, Gemini tends not to ask the VP what problem the ranking is meant to solve.

**Cost.** On Gemini the skill roughly doubles the tokens per request (about 30,000 against 14,000 to 17,000), because the seat's instructions and the reference files it opens are read on every run.

The harness, every reply and every grade are in [`benchmarks/gemini-v1.3/`](gemini-v1.3/benchmark.md).

## Version 1.2: European practice, connectors and good leadership

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

## Version 1.1: the CTO and CPTO

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

## Version 1.0: the CEO

**The analysis.** Two neutral requests against the same company (`evals/the-human-ceo/brightlane-*`):

| Model | With the skill | Without the skill | Extra tokens with the skill |
|---|---|---|---|
| Claude Opus | 52 of 54 checks | 51 of 54 checks | +22% |
| Claude Sonnet | 51 of 54 checks | 49 of 54 checks | +9% |

Given good data, current models already find the savings that don't touch jobs and recommend against layoffs without the skill. What the skill added consistently was how the agent acts on those findings:

- leadership bonuses cut first;
- an unexplained cash gap questioned;
- a sensitive governance point kept out of the board paper and raised privately;
- a request for pushback at the end of every plan.

**The coaching.** Two shortcut-style requests (`evals/the-human-ceo/shortcut-ai-productivity`, `evals/the-human-ceo/quick-win-reorg`):

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
