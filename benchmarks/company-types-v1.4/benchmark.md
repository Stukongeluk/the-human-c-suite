# Version 1.4: every kind of organisation

Version 1.4 makes the seats fit any organisation, not just software companies, while keeping the human side and the long term at the centre. It adds a company-types reference (ownership and stage, sectors and frontline work, small organisations, technology outside software companies), routes all three seats to it, makes the company context brief sector-neutral and adds the Dutch on-call and flexible-work rules.

Six new, anonymous cases test it, each outside the software world:

| Case | Seat | The situation |
|---|---|---|
| ceo-family-manufacturer-downturn | CEO | A third-generation family machine builder near Stuttgart; two automotive customers cut orders 35%, partly for good; the bank wants a plan; the adviser says let 45 of 210 go |
| ceo-homecare-budget-cut | CEO | A Dutch non-profit home-care organisation 7% short; the supervisory board wants fewer district nurses, minute-by-minute visit registration and central planning |
| ceo-startup-runway | CEO | A 48-person climate-tech startup in Stockholm with nine months of runway; investors want 30% cut this month |
| cto-retail-ai-scheduling | CTO | A Dutch supermarket chain; the COO wants an AI rostering tool in all 140 stores by March, 12% fewer hours, schedules three days ahead |
| cto-municipality-fraud-ai | CTO | A Dutch municipality wants an AI that scores everyone on welfare for fraud risk, "90% accurate", live in six months |
| cpto-delivery-driver-ranking | CPTO | A parcel company wants a live leaderboard of drivers and the bottom 10% flagged to their subcontractors every week |

## Main round

One run per setup per model: the first draft of version 1.4, version 1.3.3 and (on Claude) no skill. Graded blind, ten samples per case. One run per setup is a small sample, so read the numbers per model as direction.

### Claude Sonnet 5.5

| Case | Version 1.4 (first draft) | Version 1.3.3 | Without the skill |
|---|---|---|---|
| ceo-family-manufacturer-downturn | 5 of 6 | 5 of 6 | 3 of 6 |
| ceo-homecare-budget-cut | 4 of 6 | 4 of 6 | 4 of 6 |
| ceo-startup-runway | 6 of 6 | 3 of 6 | 2 of 6 |
| cto-retail-ai-scheduling | 5 of 6 | 4 of 6 | 3 of 6 |
| cto-municipality-fraud-ai | 6 of 6 | 5 of 6 | 4 of 6 |
| cpto-delivery-driver-ranking | 6 of 6 | 6 of 6 | 4 of 6 |
| **All cases** | **32 of 36** | **27 of 36** | **20 of 36** |

| Measure | Version 1.4 (first draft) | Version 1.3.3 | Without the skill |
|---|---|---|---|
| Mean tokens per run | 119,895 | 113,246 | 97,744 |
| Mean reply words | 902 | 948 | 1253 |
| Runs with a factual error | 1 of 6 | 0 of 6 | 4 of 6 |
| A leader owns the bad result (where one is in the prompt) | 3 of 3 | 3 of 3 | 0 of 3 |

### Claude Opus 5.5

| Case | Version 1.4 (first draft) | Version 1.3.3 | Without the skill |
|---|---|---|---|
| ceo-family-manufacturer-downturn | 3 of 6 | 4 of 6 | 5 of 6 |
| ceo-homecare-budget-cut | 3 of 6 | 4 of 6 | 4 of 6 |
| ceo-startup-runway | 6 of 6 | 6 of 6 | 5 of 6 |
| cto-retail-ai-scheduling | 5 of 6 | 5 of 6 | 5 of 6 |
| cto-municipality-fraud-ai | 3 of 6 | 3 of 6 | 5 of 6 |
| cpto-delivery-driver-ranking | 4 of 6 | 4 of 6 | 5 of 6 |
| **All cases** | **24 of 36** | **26 of 36** | **29 of 36** |

| Measure | Version 1.4 (first draft) | Version 1.3.3 | Without the skill |
|---|---|---|---|
| Mean tokens per run | 172,081 | 161,008 | 142,483 |
| Mean reply words | 739 | 718 | 1983 |
| Runs with a factual error | 0 of 6 | 0 of 6 | 2 of 6 |
| A leader owns the bad result (where one is in the prompt) | 3 of 3 | 2 of 3 | 0 of 3 |

### Gemini 4 Neon (Medium)

| Case | Version 1.4 (first draft) | Version 1.3.3 |
|---|---|---|
| ceo-family-manufacturer-downturn | 6 of 6 | 6 of 6 |
| ceo-homecare-budget-cut | 5 of 6 | 3 of 6 |
| ceo-startup-runway | 2 of 6 | 2 of 6 |
| cto-retail-ai-scheduling | 5 of 6 | 3 of 6 |
| cto-municipality-fraud-ai | 6 of 6 | 5 of 6 |
| cpto-delivery-driver-ranking | 4 of 6 | 5 of 6 |
| **All cases** | **28 of 36** | **24 of 36** |

| Measure | Version 1.4 (first draft) | Version 1.3.3 |
|---|---|---|
| Mean tokens per run | 43,335 | 38,994 |
| Mean reply words | 734 | 816 |
| Runs with a factual error | 1 of 6 | 3 of 6 |
| A leader owns the bad result (where one is in the prompt) | 2 of 3 | 3 of 3 |

### Gemini 4 Hydrogen (Medium)

| Case | Version 1.4 (first draft) | Version 1.3.3 |
|---|---|---|
| ceo-family-manufacturer-downturn | 5 of 6 | 5 of 6 |
| ceo-homecare-budget-cut | 4 of 6 | 3 of 6 |
| ceo-startup-runway | 5 of 6 | 2 of 6 |
| cto-retail-ai-scheduling | 5 of 6 | 3 of 6 |
| cto-municipality-fraud-ai | 3 of 6 | 2 of 6 |
| cpto-delivery-driver-ranking | 4 of 6 | 4 of 6 |
| **All cases** | **26 of 36** | **19 of 36** |

| Measure | Version 1.4 (first draft) | Version 1.3.3 |
|---|---|---|
| Mean tokens per run | 42,374 | 34,922 |
| Mean reply words | 558 | 629 |
| Runs with a factual error | 4 of 6 | 2 of 6 |
| A leader owns the bad result (where one is in the prompt) | 1 of 3 | 1 of 3 |

**Overall:** 110 of 144 checks with the first draft of version 1.4, against 96 with version 1.3.3; on Claude, 49 of 72 without the skill.

**What the draft did well.** Sonnet and both Gemini models gained the most: the startup case (runway arithmetic, one cut sized to the plan, Swedish rules), the supermarket case (stable schedules, a pilot measured on more than labour hours, scheduling guardrails) and the welfare-fraud case (base rates, precedents, safeguards).

**What it got wrong: Opus.** Opus did worse with either version of the skill than without it (24 and 26 of 36, against 29). In the home-care, welfare-fraud and driver cases it applied the skill's limit for people acting in their own role (about 400 words, never more than 500) to a director and a CIO who had to bring a recommendation to a supervisory board or a council. The short replies left out the legal floor, the safeguards and the people to involve. Without the skill, Opus wrote 1,000 to 2,300 words and covered them.

## Follow-ups

The fixes, each checked before the next ([`follow-ups.md`](follow-ups.md)):
1. From the version 1.3.3 check: rank the customer problems, name owners and dates before the data is in, and count the words before sending.
2. The limit of about 500 words holds for people acting in their own role, including a manager taking a plan to their own manager or CEO. A formal recommendation to a board, council or supervisory body gets the normal chat budget.
3. Small additions to the company-types reference where replies fell short: what a bank needs (13-week cash forecast, covenant headroom, scenarios and the actions each triggers), scheduling guardrails, and what to monitor before changing staffing in care.
4. Two wording fixes where Gemini misread the reference: the Gap result came on top of two weeks' notice, and the nurse-staffing study is about patients per nurse, not skill mix.

## Harness note

The skill tells the agent to search its evidence file rather than read it whole. In headless mode Gemini Hydrogen used `rg` for that, the CLI couldn't ask permission, and six runs ended with no answer. The harness now also allows read-only search and read commands (`rg`, `grep`, `findstr`, `Select-String`, `Get-Content`, `cat`, `type`); those six runs were repeated and the empty attempts are not graded.
