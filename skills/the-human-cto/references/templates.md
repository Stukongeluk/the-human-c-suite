# Templates

## Contents

- Architecture decision record (ADR)
- Evaluation scorecard
- Migration plan
- AI tool pilot plan
- Decision memo
- Career conversation guide
- Pre-mortem
- Communication checklist

<!-- shared:tech-templates -->
## Architecture decision record (ADR)

```markdown
# ADR-<n>: <decision title>

**Status:** proposed / accepted / superseded by ADR-<n> · **Date:** <date> · **Decision owner:** <role>

## Context
<The problem, constraints and forces. Link the data: incidents, costs, delivery metrics, with dates.>

## Options
<Each option, including "keep what we have", with its trade-offs.>

## Decision
<What we chose and why, in a few sentences.>

## Consequences
<What gets better, what gets harder, who is affected, what it costs to reverse.>

## Revisit when
<The specific signal that would make us reconsider.>

## Interests declared
<Anyone involved who built, sells or has a stake in an option, and how that was handled.>
```

## Evaluation scorecard

Agree and record the criteria and weights before anyone scores. Changing them later needs a written reason and a re-run under both versions.

| Criterion | Weight (fixed on <date>, agreed by <who>) | Evidence used | Option A | Option B | Keep current |
|---|---|---|---|---|---|
| Reliability in production (incidents, change fail rate, recovery time) | | | | | |
| Delivery for the teams using it (lead time, deploy frequency) | | | | | |
| Total cost over 3–5 years, including migration and exit | | | | | |
| Operability and on-call load | | | | | |
| Security and compliance | | | | | |
| Skills: who can run it today, who must learn it | | | | | |
| Fit with strategy and architecture | | | | | |

Below the table: who scored, interests declared, dissenting views, and the result under any alternative weighting that was proposed.
<!-- /shared:tech-templates -->

## Migration plan

| Wave | Teams or services | Why this order | Dates | Support (pairing, training, platform help) | Exit criteria | Owner |
|---|---|---|---|---|---|---|
| Pilot | <one willing team, low-risk service> | | | | | |
| Wave 1 | | | | | | |
| Wave 2 | | | | | | |
| Retire old platform | | | | | | |

Also state: capacity reserved for the migration (not "on top of the roadmap"), how long the old platform stays supported, the rollback plan, and the people indicators watched (on-call load, unplanned work, engagement of the teams doing the work).

## AI tool pilot plan

```markdown
# Pilot: <tool> for <use case>

**Question:** <What would make us scale, change or stop?>
**Teams:** pilot <team(s)> · comparison <team(s)> · **Duration:** 8–12 weeks

## Baseline (before)
Change lead time, cycle time per stage, review wait time, change fail rate, rework,
escaped defects, security findings, developer experience score.

## Ways of working
Small pull requests, tests required, review rules for AI-written code, security scanning, training time.

## Measure (after)
The same metrics for pilot and comparison groups. Self-reported speed-ups noted separately.

## Cost
Seats and API spend, including review and correction time.

## Decision rule (agreed up front)
Scale if <metric> improves by <x> without <quality metric> getting worse; otherwise change or stop.

## Where freed capacity goes
<Debt, reliability, roadmap, mentoring, growth: decided before results are known.>
```

## Decision memo

```markdown
# Decision: <title>

**Decision needed by:** <date> · **Decision owner:** <role> · **Prepared:** <date>

## The problem in one sentence
## What the data says (fact · value · source and date · confidence)
## Options considered (including "do nothing")
## Recommendation
## Human impact (who is affected, how, what we do for them)
## Transition plan
## Communication plan (see the communication checklist)
## Assumptions, and what would change my mind
## Questions for you (pushback welcome)
```

<!-- shared:people-templates -->
## Career conversation guide

Use in 1:1s, especially before and during change. Listen more than you talk, and write down what you agree.

- What part of your work gives you the most energy? What drains you?
- What are you proud of from the last year?
- Where do you want to be in two or three years? Does that include managing people, going deeper, or something else?
- Which skills would you like to learn? Which do you have that we don't use?
- What makes your work harder than it needs to be?
- If your current tasks were automated tomorrow, what would you most like to do instead?
- Is there anything in your situation we should take into account? (Only what they choose to share.)
- What do you need from me?

## Pre-mortem

Before a big decision, ask the group: "It is twelve months from now and this decision clearly failed. Write down why." Collect the reasons, group them, and add a mitigation or an early warning signal for the top five.

## Communication checklist

- [ ] Employee representatives (works council, unions) involved before the decision is final, where required or sensible
- [ ] Managers briefed first, with a script, answers to likely questions and support for themselves
- [ ] Affected people told personally by their own manager or leader, in person or live, before any wider announcement
- [ ] The why explained with real numbers, plus what is decided, what is still open, and next steps with dates
- [ ] Practical information ready the same day: what changes, support available, who to ask
- [ ] Everyone else told the same day, honestly, including what it means for them
- [ ] No mass emails, no surprise lockouts, no announcement on a Friday afternoon or just before holidays
- [ ] Follow-up moments scheduled: Q&A, 1:1s, a check-in after two and six weeks
<!-- /shared:people-templates -->
