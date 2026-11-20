# Q1 Roadmap Trade-off Brief: Customer Commitments vs. Team Capacity

Use this 1-page structure to prepare with your engineering lead and run a private 1:1 with your CEO.

## 1. The Goal of the Conversation
Align with the CEO on protecting your biggest customer **without** burning out the team or breaking existing Q1 commitments. You are not saying "no"—you are asking the CEO to choose which trade-off the business wants to take.

---

## 2. Prepare the Numbers First (30 mins with your Engineering Lead)
Before meeting the CEO, fill in the blanks using your team's real Q1 capacity (excluding planned leave, on-call, support, and committed reliability/debt work):

| Item | Estimated Effort (Weeks / Sprints) | Customer / Revenue Impact |
|---|---|---|
| **Available Q1 Team Capacity** | `[X]` weeks | — |
| **Already Committed Q1 Roadmap** | `[Y]` weeks | `[e.g., Retention / ARR at stake]` |
| **Remaining Uncommitted Buffer** | `[X - Y]` weeks | — |
| **New Feature 1** | `[A]` weeks | `[Biggest customer problem it solves]` |
| **New Feature 2** | `[B]` weeks | `[Biggest customer problem it solves]` |
| **New Feature 3** | `[C]` weeks | `[Biggest customer problem it solves]` |

> **Note:** Also check what the customer *actually needs to achieve* with each feature. Sometimes a configuration change, integration, or smaller v1 solves 80% of the problem in 20% of the time.

---

## 3. Three Options to Put on the Table

| Option | What Ships in Q1 | What Moves or Changes | Risk / Trade-off |
|---|---|---|---|
| **Option A: Swap (Recommended if all 3 are hard Q1 commitments)** | The 3 customer features (scoped to smallest viable version) | Defer `[Feature/Project X]` and `[Feature/Project Y]` from Q1 to Q2 | Protects the biggest customer and team health; delays other Q1 goals visibly. |
| **Option B: Phase (Recommended if the customer is flexible on timing)** | 1 critical feature (or workaround) in Q1 + firm discovery/delivery dates for the other 2 in Q2 | Minimal displacement of current Q1 roadmap | Reduces Q1 churn risk on existing commitments; requires the CEO/account lead to align expectations with the customer now. |
| **Option C: Add Capacity (Only if demand is lasting)** | Existing Q1 + part of the new work | Temporarily shift engineers from `[Team Z]` (with their lead's agreement) | Slows `[Team Z]`'s roadmap; onboarding still takes time, so it rarely saves Q1 alone. |

*What is off the table:* Absorbing all three on top of Q1 via overtime or skipping testing/security reviews. That creates production incidents and slows Q2 delivery for everyone.

---

## 4. Script for the Private 1:1 with the CEO

**Opening (acknowledge the business goal):**
> "I want to make sure we deliver for [Customer Name]—they're our biggest account and keeping them happy matters. I sat down with [Engineering Lead] to map the three new features against our Q1 capacity."

**Show the math (neutral, no blame):**
> "Right now, our team has `[X]` weeks of capacity in Q1, and `[Y]` weeks are already committed to `[Existing Q1 Priority 1 & 2]`. The three new features are roughly `[A+B+C]` weeks. We can't fit both in Q1 without breaking quality or burning out the team."

**Hand over the choice:**
> "Here are two ways we can hit this: Option A is we prioritize the three features for Q1 and move `[Existing Q1 Priority]` to Q2. Option B is we ship `[Feature 1]` in Q1, give [Customer Name] a firm Q2 date for the other two, and keep the rest of Q1 intact. Which trade-off makes the most sense for the business?"

**Preventing a repeat (end of meeting, keep it light):**
> "Going forward, if a big deal needs a custom commitment, can we do a quick 24-hour sizing check with engineering before we lock a date with the customer? That way you can promise a firm answer date on the call without getting surprised later."
