# Does a humane CHRO seat earn its place? (version 1.6)

The question: does a dedicated people seat give better advice on people decisions than the CEO seat, which already covers layoffs, reviews and change? Six HR cases, run with the draft CHRO seat, the CEO seat (version 1.5.2), the closest open-source CHRO skill we could find and no skill. One run per setup on Claude Sonnet 5.5 and Claude Opus 5.5, graded blind. The rule set before the test: the CHRO becomes the fifth seat only if it beats the CEO seat on both models.

The other skill is `chro-advisor` from the C-level advisor set in [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (MIT licence), tested at commit [`5909a72`](https://github.com/alirezarezvani/claude-skills/tree/5909a72e62b5fbb809935fb6a55b58bdbe175074/c-level-advisor/skills). Its files are not copied here.

**Result:** the CHRO seat beat the CEO seat on both models, on both measures. It passed 34 of 36 checks on Sonnet (CEO seat 27) and 36 of 36 on Opus (CEO seat 33). Its mean overall quality was 7.5 against 6.5 on Sonnet and 9.0 against 8.7 on Opus. On Opus the lead is small. It is the fifth seat from version 1.6.0. [Follow-ups](#follow-ups-what-the-draft-missed) on Sonnet then fixed what the draft missed.

## The cases

All anonymous and generic; the checks are in [`evals/the-human-chro/`](../../evals/the-human-chro/).

| Case | The ask |
|---|---|
| `chro-forced-ranking` | A 1,200-person software company in Amsterdam and Hamburg: the new CEO wants 10% of every team in the bottom category, a 60-day plan and exits by the end of Q3. Design the process and the manager briefing |
| `chro-ai-cv-screening` | A 2,500-person retailer hiring in the Netherlands, Belgium and Germany: switch on AI screening that auto-rejects the bottom 70% of 4,000 applications a month, unseen. The vendor says it is bias-free |
| `chro-rto-mandate` | An 800-person fintech in Utrecht and Berlin: five days in the office from 1 March "to fix our culture", with a third of staff hired remote or hybrid. Write the announcement |
| `chro-pay-gap` | A 650-person consultancy, 420 in the Netherlands and 230 in Belgium: a 14% gap overall and 6% in the same roles. The CFO wants to say nothing and close it over five years |
| `chro-burnout-survey` | A 450-person insurer in Rotterdam: burnout risk up in two departments, trust in leadership at 41%. The CEO wants "stable with some pockets" and resilience training. Keep it short |
| `chro-layoff-selection-list` | 40 of 300 roles in Rotterdam and Munich: managers named who stays, and HR ranked the rest on rating, sick days and part-time work. Finalise the list for the 15th |

## Results

Each cell gives checks passed, and in brackets the grader's overall-quality score from 1 to 10 (how useful, honest and sound a seasoned, humane CHRO would find the answer, judged apart from the checks).

### Claude Sonnet 5.5

| Case | CHRO seat (draft) | CEO seat 1.5.2 | `chro-advisor` | Without a skill |
|---|---|---|---|---|
| chro-forced-ranking | 6 of 6 (9) | 5 of 6 (7) | 4 of 6 (5) | 4 of 6 (5) |
| chro-ai-cv-screening | 6 of 6 (7) | 6 of 6 (7) | 4 of 6 (6) | 5 of 6 (6) |
| chro-rto-mandate | 5 of 6 (6) | 2 of 6 (5) | 3 of 6 (5) | 2 of 6 (4) |
| chro-pay-gap | 5 of 6 (7) | 4 of 6 (6) | 5 of 6 (6) | 3 of 6 (6) |
| chro-burnout-survey | 6 of 6 (8) | 5 of 6 (7) | 3 of 6 (6) | 5 of 6 (7) |
| chro-layoff-selection-list | 6 of 6 (8) | 5 of 6 (7) | 5 of 6 (5) | 4 of 6 (6) |
| **All cases** | **34 of 36** | **27 of 36** | **24 of 36** | **23 of 36** |

| Measure | CHRO seat (draft) | CEO seat 1.5.2 | `chro-advisor` | Without a skill |
|---|---|---|---|---|
| Mean overall quality (1 to 10) | 7.5 | 6.5 | 5.5 | 5.7 |
| Mean tokens per run | 98,683 | 100,242 | 90,528 | 80,494 |
| Mean minutes per run | 0.8 | 0.9 | 0.7 | 0.6 |
| Mean reply words | 756 | 584 | 1383 | 1225 |
| Runs with a factual error | 1 of 6 | 2 of 6 | 4 of 6 | 3 of 6 |
| Runs that mention a skill or its terms | 0 of 6 | 0 of 6 | 3 of 6 | 0 of 6 |
| Leadership owns the bad result (where there is one) | 1 of 4 | 3 of 4 | 0 of 4 | 0 of 4 |

### Claude Opus 5.5

| Case | CHRO seat (draft) | CEO seat 1.5.2 | `chro-advisor` | Without a skill |
|---|---|---|---|---|
| chro-forced-ranking | 6 of 6 (9) | 6 of 6 (9) | 6 of 6 (6) | 6 of 6 (8) |
| chro-ai-cv-screening | 6 of 6 (9) | 6 of 6 (9) | 6 of 6 (8) | 6 of 6 (8) |
| chro-rto-mandate | 6 of 6 (9) | 4 of 6 (8) | 5 of 6 (8) | 5 of 6 (7) |
| chro-pay-gap | 6 of 6 (9) | 6 of 6 (9) | 5 of 6 (8) | 5 of 6 (8) |
| chro-burnout-survey | 6 of 6 (9) | 5 of 6 (8) | 3 of 6 (7) | 6 of 6 (8) |
| chro-layoff-selection-list | 6 of 6 (9) | 6 of 6 (9) | 4 of 6 (8) | 4 of 6 (7) |
| **All cases** | **36 of 36** | **33 of 36** | **29 of 36** | **32 of 36** |

| Measure | CHRO seat (draft) | CEO seat 1.5.2 | `chro-advisor` | Without a skill |
|---|---|---|---|---|
| Mean overall quality (1 to 10) | 9.0 | 8.7 | 7.5 | 7.7 |
| Mean tokens per run | 150,068 | 167,066 | 149,136 | 115,121 |
| Mean minutes per run | 8.4 | 11.2 | 9.8 | 7.1 |
| Mean reply words | 599 | 650 | 1354 | 1183 |
| Runs with a factual error | 0 of 6 | 1 of 6 | 3 of 6 | 1 of 6 |
| Runs that mention a skill or its terms | 0 of 6 | 0 of 6 | 1 of 6 | 0 of 6 |
| Leadership owns the bad result (where there is one) | 1 of 4 | 4 of 4 | 0 of 4 | 1 of 4 |

### What the graders saw

- **Return to office** separated the setups most. The best answers advised against announcing five days as a decision. They cited the Dutch works council's consent right with the Caterpillar (2025) and Booking.com (2026) rulings and the German rule that ending agreed telework is a transfer. Then they wrote a proposal email with notice measured in months and a review date. The weakest wrote the mandate as decided ("this replaces the current arrangements").
- **Forced ranking.** The weaker answers brought the quota back as a soft "expected range", for example 10 to 17%, that tells managers roughly what share to rate low. Some also sent Dutch performance dismissals through the UWV instead of the court.
- **Pay gap.** The best answers costed every route as what the company pays plus what the underpaid women go without, which shows that the five-year "saving" is exactly the pay they could claim back. The weakest built the whole case on the new directive, never said equal pay is already law, and got the reporting dates or thresholds wrong.
- **Burnout.** The user asked for short; `chro-advisor` ran past the word limit on both models (697 and 624 words). Several answers asserted that resilience training doesn't help without citing the evidence (Fleming, 2024, 46,336 UK workers).
- **AI screening.** Almost every answer refused auto-reject and proposed a recruiter on every rejection. What separated them was current law: the 2026 Digital Omnibus moved the AI Act's high-risk duties to 2 December 2027, and some answers still called that a proposal.

## Follow-ups: what the draft missed

The draft missed one check on Sonnet in the pay gap: it proposed two to three pay rounds with no dates, and said a report was due in 2027 (the Dutch bill sets June 2028, on 2027). It missed one in the return to office: its email still announced five days as the decided default. On both models it almost never said that the bad news was leadership's to own, where the CEO seat did. Sonnet's replies also ran long (756 words on average; 976 on the pay gap).

The fixes, verified against current sources:

- the Dutch pay transparency dates (the minister said on 19 November 2026 that 1 January 2027 is no longer feasible), reporting per legal entity, Belgium's 2012 pay gap law and a plan measured in months, with the cost shown as pay withheld;
- the Dutch consent right on home-working policy (Caterpillar, Booking.com), the German transfer rule, and announcing a proposal, not a decision, where representatives must consent;
- leadership saying plainly that bad news (cuts, a pay gap, low trust) comes from its decisions;
- the 500-word limit for someone handling their own situation now also covers an HR leader taking a plan to their own CEO or CFO, as in the other seats, and what is cut goes into a document handed over with the reply;
- in the return to office, options that take nothing away from people come first: fix the named problem directly, and make home working good with funded team days, a home-working allowance (€2.45 a day tax-free in the Netherlands in 2026) and proper equipment.

The shared country notes gained Belgium, the Dutch home-working rulings and the German Federal Labour Court's April 2026 ruling that dismissals are void when the mass-dismissal notification is missing or early.

Each round was graded blind next to earlier answers to the same case. Rounds 1 to 3 ran on Sonnet only: the web search budget was spent by then, and the Opus runs depend on live research. Opus's draft had passed all 36 checks. Round 4 ran on both models.

| Round | Case | What ran | Checks (quality) | Reply words |
|---|---|---|---|---|
| 1 | chro-pay-gap | draft 2 / draft 1 / CEO seat | 6 (9) / 5 (7) / 4 (7) | 1002 / 976 / 509 |
| 1 | chro-rto-mandate | draft 2 / draft 1 / CEO seat | 5 (8) / 4 (7) / 2 (6) | 581 / 644 / 487 |
| 1 | chro-layoff-selection-list | draft 2 / draft 1 / CEO seat | 6 (9) / 6 (8) / 4 (7) | 906 / 836 / 860 |
| 2 | chro-pay-gap | draft 3 / draft 2 / draft 1 / CEO seat | 5 (7) / 6 (9) / 5 (7) / 4 (6) | 495 / 1002 / 976 / 509 |
| 2 | chro-forced-ranking | draft 3 / draft 1 / CEO seat | 6 (9) / 6 (9) / 5 (7) | 493 / 969 / 689 |
| 3 | chro-pay-gap | draft 4 / draft 3 / draft 2 | 6 (9) / 5 (7) / 6 (8) | 488 / 495 / 1002 |
| 3 | chro-forced-ranking | draft 4 / draft 3 / draft 1 | 6 (7) / 6 (9) / 6 (8) | 461 / 493 / 969 |

Draft 2 holds the fixes. Draft 3 adds the word limit: replies halved, but on the pay gap the shorter reply dropped how to test the 6% and lost a check. Draft 4 moves what is cut into a handed-over document: on the pay gap it got full marks in 488 words, with a 904-word CFO note and plan. The leadership line landed: in round 1, draft 2 said plainly that the gap and the cuts were leadership's, where draft 1 hadn't. Draft 4's forced-ranking answer scored lower on quality partly because it ended with a stray file path, an artefact of the test harness.

### Round 4: support for home working

A return to office can be softened without being humane: every answer so far protected remote contracts and wrote a proposal, but none put money or effort into making home working good. Draft 5 adds that option to the return-to-office guidance, with the Dutch and German figures. On Sonnet it still went straight to fewer office days, so version 1.6.0 adds one line to the seat itself: lead with the options that take nothing away from people. The grader got one extra check, whether an answer offers a concrete way to make home or hybrid work better (an allowance, equipment, funded team days), and graded six answers together, blind:

| Model | Answer | Checks (quality) | Supports home working | Reply words |
|---|---|---|---|---|
| Sonnet | **1.6.0** | **5 (8)** | **yes** | 466 |
| Sonnet | draft 1 | 3 (5) | no | 644 |
| Opus | draft 5 | 6 (9) | yes | 487 |
| Opus | draft 1 | 6 (8) | no | 455 |
| Opus | CEO seat 1.5.2 | 4 (7) | no | 527 |
| Opus | without a skill | 5 (7) | no | 1774 |

Only the new versions offered home-working support. Sonnet's 1.6.0 answer led with a buddy and funded team days, then the €2.45 allowance and equipment, and priced the allowance at about €91,000 a year for 270 people against the cost of replacing those who leave. Opus's draft 5 started those measures on 1 March, because they need nobody's consent, and put team-agreed anchor days to the works councils as a proposal. Sonnet's 1.6.0 answer missed one check by leaving out the Dutch Flexible Working Act. Opus wasn't rerun with the final one-line change.

## Read these with care

- **One run per setup.** The lead over the CEO seat is clear on Sonnet and small on Opus: compare direction, not decimals.
- **The checks were written alongside the CHRO seat.** That risks testing what the seat was told to do. The overall-quality score, given apart from the checks, is there as a second measure, and it also favours the CHRO seat on both models.
- **`chro-advisor` was built for another job.** It is written for startup people strategy (hiring plans, pay bands, org design) with a fixed output format; these cases are European, legal and adversarial. Its answers use emoji confidence tags; in the blind copies they were replaced by text tags (`[verified]`, `[medium]`, `[assumed]`) so the grader couldn't spot them. Its answers that mention "the skill" or its own steps count as a skill mention.
- **Claude only.** The Gemini quota was used up, so this round has no Gemini runs.
- **The web search budget ran out.** All agents in one turn share 200 searches. The graders of the main round ran out partway and checked the rest by opening the sources the answers cited; the follow-up graders could only fetch pages and use the vetted fact sheets. A few claims were left unverified rather than counted as errors; each `grading.json` says which.
- **Graders vary.** The same answer got different grades in different rounds: draft 1's return-to-office answer passed 5 checks in the main round and 4 in round 1, and draft 2's pay-gap answer had no factual error in round 1 and one in round 3. Compare setups within one grading round, not across them.
- **Version 1.6.0 was rerun on one case.** It is draft 4 plus the home-working guidance and the line on options that take nothing away; the pay-gap and length fixes were tested as draft 4, the layoff fixes as draft 2. Opus last ran as draft 5, one line short of 1.6.0. Its description was then shortened to fit the Agent Skills limit of 1,024 characters. The runs read `SKILL.md` directly, so that didn't affect them, but which prompts make an agent load the CHRO seat by itself hasn't been tested yet.
- **One rerun saved its reply one folder too high.** The file was moved into `outputs/` before grading; nothing else was changed.
- **One check was added for round 4.** "Supports home working" is an extra check, not one of the six, and it was written after the gap was found, so it measures the fix rather than discovering it.
- **The checks have known gaps.** The graders' notes in each `grading.json` list them, for example: no check on the Dutch consent right in the return-to-office case, a soft quota that still passes the forced-ranking checks, and bundled checks where one omission fails an otherwise strong answer. They are the starting point for the next round of test cases.

Each run folder holds `reply.md`, any document the agent wrote, `grading.json` and `timing.json`. `benchmark.json` lists every run of the main round; [`follow-ups/`](follow-ups/) holds the three rounds, with their own `benchmark.json`.
