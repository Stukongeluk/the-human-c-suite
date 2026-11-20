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
