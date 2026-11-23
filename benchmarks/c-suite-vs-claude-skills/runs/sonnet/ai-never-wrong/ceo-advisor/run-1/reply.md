# Cutting QA (6) and half of second-line support (10 of 20): the business case

## Bottom line

I can't write the business case on the premise you were given, because the premise is not evidence yet. "Basically never wrong" is a sentence, not a number. A case for removing 16 people that rests on it would fail the first board question ("wrong how often, measured how, on what?"), and if the claim is off, you would carry the cost: customer harm, rework, and rehiring in a worse market.

What I can give you is the version that holds up: a gated case where the savings are real if the CTO's claim survives a two-to-four week test, and where you decide on the numbers instead of on the claim. Below is the structure, the arithmetic you need, and what to ask the CTO for this week.

Confidence in this recommendation: medium-high. Confidence that the cut is right or wrong: unknown, and that is the point. Nobody has shown the data yet.

## What we know and don't (tagged)

- [Verified] The proposal: remove 6 QA and 10 of 20 second-line support engineers, 16 people, because AI agents are "basically never wrong". Source: your message.
- [Assumed] That the claim is measured. I have seen no error rate, sample size, evaluation method or time window.
- [Assumed] That the agents have been measured on the work these two teams do. Second-line support gets the cases first line and the agents could not solve. QA exists to catch defects, including defects from AI-generated code and from the agents themselves. An agent's accuracy on easy tickets says little about hard tickets or about its own errors.
- [Assumed] Savings. I do not have your salary data. See the model below; replace my placeholders.

## Why the claim is not enough

1. **"Rarely wrong" is not "never wrong", and at volume the gap is large.** At 10,000 agent actions a month, a 99% accuracy rate is 100 wrong outcomes a month. Whether that is fine depends on what each one costs (a wrong refund, a wrong answer to a regulated customer, a bad release). A number you can price is what the case needs.
2. **Selection bias.** If "never wrong" comes from tickets the agent closed, the cases it got wrong may never have been flagged, because the customer gave up, or a human quietly fixed it. Reopen rate, repeat contacts, escalation rate and churn after contact are the honest measures.
3. **Who checks the checker?** QA is the independent control. Removing it and relying on the CTO's assurance means the function that built the system also grades it. Auditors and boards treat that as a control gap.
4. **Second-line is your fallback.** Halving it removes capacity exactly where the agents are weakest, and the incidents that need it arrive in bursts, not evenly.
5. **Cuts are hard to reverse.** Rehiring QA and senior support engineers costs months and institutional knowledge. Piloting costs weeks. This asymmetry favors testing first.

## Illustrative savings model (placeholders, replace with your finance data)

| Item | Placeholder | Note |
|---|---|---|
| Heads removed | 16 | 6 QA + 10 support |
| Fully loaded cost per head | 70,000 per year | Assumed; use your actual figure |
| Gross annual saving | about 1.12M | 16 x 70,000 |
| One-off costs | Severance/transition, plus knowledge capture | Varies by jurisdiction and contracts; get HR/legal numbers |
| Offsets | AI usage/inference cost growth, tooling, remaining staff overtime | Often missing from first drafts |
| Downside per 1 point of accuracy lost | Volume x cost per error | The line the CTO's claim must be tested against |

Break-even rule: the cut pays back only while (cost of extra errors, rework and churn) is below the gross saving minus one-off and offset costs. With the placeholders above, if the extra errors cost more than roughly 1M a year, you lose money. Compute that with real volumes before anyone presents a headline saving.

## Options (three paths, per the decision framework I use)

| Path | Upside | Downside | Reversible? |
|---|---|---|---|
| A. Cut now as proposed | Full saving starts immediately | Unverified claim carries all the risk; weak control environment; hard to undo | No |
| B. Gated, staged reduction (recommended) | Saves most of the money if the claim holds; stops the cut if it doesn't | Savings start 1-2 quarters later | Mostly |
| C. Keep teams, redeploy | Lowest risk; moves people to higher-value work (agent evaluation, QA of AI output, harder escalations) | Little or no cost saving | Yes |

Recommended: B. In practice, QA is not removed but changes jobs (evaluating the agents is real work), and second-line shrinks through attrition and redeployment first, with a hard trigger for any further reduction.

## How to act (next 4 weeks)

1. **Ask the CTO for evidence, in writing, within a week:** the error rate with its definition; sample size and period; how errors were found and by whom (not the agents themselves); results split by ticket difficulty and by tier; reopen/repeat-contact rate; the worst 20 failures and what they cost. If the data lives in dashboards, have someone outside the CTO's org pull it.
2. **Run a blind audit.** QA (the team you may cut) samples a few hundred agent outcomes, stratified by difficulty, without knowing which the agents consider easy. This is also the cheapest way to get a defensible number.
3. **Pilot the reduction.** Take one queue or product area, reduce human cover there only, and track customer outcomes against a control area for 4-8 weeks.
4. **Set the trigger in advance.** Agree with the CTO and CFO, before the pilot, what accuracy, reopen rate, and CSAT make the next step proceed, pause or reverse. Writing the threshold down protects you from arguing about it after the fact.
5. **Finish the model** with real salaries, one-off costs, AI run costs and error costs; then the board paper writes itself, with an honest range instead of one number.
6. **Treat people as the last lever, not the first.** If the pilot supports it, use attrition, redeployment into AI evaluation and escalation roles, and contractor reductions before layoffs. Check legal and consultation obligations for your jurisdiction early, because they affect the timeline and cost.

## Your decision

- Do you want the gated plan (B) taken to the board, or do you need a full case for the cut (A)? If A, I would still want the evidence in step 1 first; I will not put a number in front of a board that I cannot trace.
- Who owns the independent measurement? I suggest the CFO or COO, not the CTO.
- What is the maximum acceptable cost of AI errors per year that you are willing to underwrite? That figure sets the trigger.

One more thing to push back on, kindly: the CTO may well be right that the agents are very good, and this plan gets you that saving faster with evidence than a cut now would. But it is worth knowing why the CTO is confident. If the answer is "the demos look great", that is a different level of evidence than "we audited 500 outcomes with an independent reviewer".

If you send me the actual error data, headcount costs and ticket volumes, I will turn this into the full model and a board-ready paper.
