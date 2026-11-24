# When does Claude load a seat?

A skill only helps if Claude loads it, and Claude decides that from the skill's description alone. This test checks two things for each of the five seats: does Claude pick the seat for the requests it was built for, and does it leave the seat alone for routine work in the same area?

## Method

- **Messages.** 90 in all ([`judgments.csv`](judgments.csv) has every one). For each seat, 10 requests it should handle, written the way people ask, often without mentioning people at all ("Should we rewrite our monolith in Go?", "We have 9 months of runway left. What's the plan?"). And for each seat's area, 8 near-misses that no seat should take: routine work such as fixing a stack trace, a VAT question, release notes, a job description or a depreciation sheet.
- **Competition.** The skills list held the five seats and 22 skills that compete for the same requests, from Anthropic's public employment-legal, product-management, engineering and marketing plugins, the document skills and a career plugin ([`setup.json`](setup.json) lists them). That is a harder field than most people have installed.
- **Judging.** Claude Sonnet 5.5 and Claude Opus 5.5 each saw the full list and the messages, and said which skill they would load first, or none, treating each message as a fresh session. Three shuffles of the list and the message order per model: 540 judgments, November 2026.
- **Limits.** This is a simulation: the model was asked which skill it would load. It was not a live session with the plugin installed, because the Claude Code CLI could not sign in in the test workspace. Asked directly, a model is probably quicker to pick a skill than in a live session, where it can also just answer, so read the rates as a comparison between seats and descriptions rather than as live loading rates. The live check is below.

## Results with the 1.6.0 descriptions

| Seat | Right seat | Any seat | Near-misses that loaded a seat |
|---|---|---|---|
| `the-human-ceo` | 58 of 60 | 60 of 60 | 0 of 48 |
| `the-human-cfo` | 60 of 60 | 60 of 60 | 0 of 48 |
| `the-human-cto` | 55 of 60 | 60 of 60 | 0 of 48 |
| `the-human-cpto` | 45 of 60 | 51 of 60 | 0 of 48 |
| `the-human-chro` | 60 of 60 | 60 of 60 | 0 of 48 |

No near-miss loaded a seat on either model: routine work went to the specialist skill or to no skill at all. The misses were all on product and technology:

- "Our NPS dropped 15 points after the redesign. What do we do?" went to a metrics-review skill on 5 of 6 runs. The CPTO description named roadmaps and features but not customers leaving or satisfaction falling.
- "Should we build our own LLM features or buy them from a vendor?" went to the CTO on 6 of 6, and "Tech debt is slowing us down but the CEO wants features" went to the CPTO on 5 of 6 instead of the CTO. Both descriptions claim build-or-buy and tech debt against features, and the seats bring each other in, so this costs little.
- "Prioritise this backlog of 40 items" went to a roadmap skill on 2 of 6 runs.

## What changed

The CPTO description now names "falling NPS, churn or adoption". To stay within the 1,024 characters the Agent Skills format allows, it no longer lists "AI tooling and spend" (the CTO's ground, and the CTO still takes those requests) or "or executives" after "features promised by sales".

The retest ran the old and new description side by side on the same shuffles: the CPTO's and CTO's 20 messages, the 8 CPTO near-misses, and 5 new messages (three about falling churn, adoption or active users, and two near-misses: a chart of active users and an NPS benchmark question).

| CPTO description | Right seat | Any seat | Near-misses that loaded a seat | CTO messages, right seat |
|---|---|---|---|---|
| 1.6.0 | 30 of 52 | 34 of 52 | 0 of 40 | 38 of 40 |
| New | 40 of 52 | 45 of 52 | 0 of 40 | 38 of 40 |

The NPS and active-user questions now go to the CPTO, the near-misses still load nothing, and the CTO is unchanged. Backlog prioritisation still goes to the roadmap skill and LLM build-or-buy to the CTO.

## Check it live

With the plugin installed in Claude Code, send a message and check whether the seat loaded. The command prints `true` and exits 0 when Claude called the Skill tool for the CPTO; run it a few times, because loading varies from run to run:

```bash
claude -p "Our NPS dropped 15 points after the redesign. What do we do?" --output-format stream-json --verbose \
  | jq -e -s 'any(.[]; .type == "assistant" and any(.message.content[]?; .type == "tool_use" and .name == "Skill" and (.input.skill | test("the-human-cpto"))))'
```
