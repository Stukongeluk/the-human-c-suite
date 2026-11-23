# Advice on the AI fraud-risk scoring system

## Bottom line

Advise the council **not to buy this system as specified and not to go live in six months.** Offer the alderman something he can still announce: a six-month "prepare and prove" phase that ends in a go/no-go decision backed by evidence. The system as described (a risk score for every welfare recipient, fed by benefits, debt-counselling and housing data) is close to the profile of the Dutch cases that were stopped by courts, auditors or the municipalities themselves. The main exposure is legal and political, not technical. Confidence: high (verified pattern, see below).

## What I'm confident about (and what I'm not)

| Claim | Confidence |
|---|---|
| "90% accurate" tells you almost nothing about whether investigators will be pointed at the right people | Verified (arithmetic below) |
| Scoring welfare recipients for fraud risk is a **high-risk AI use** under the EU AI Act, and a score that works like a general profile of citizens risks running into the social-scoring ban | Medium: classification and timelines need confirmation by your legal counsel, and the Digital Omnibus may shift application dates |
| Pooling debt-counselling (schuldhulpverlening) data into a fraud model needs a lawful basis you probably don't have | Medium: depends on your verordening and data-sharing arrangements, which I haven't seen |
| Six months is not enough to do this properly | Verified for the legal and procurement steps; medium for the technical ones |
| The vendor's model will be biased against particular groups | Assumed: unknown until tested on your data. It is the risk to test for, not a finding |

## Why

**1. "90% accurate" is the wrong number.**
Take 10,000 recipients and assume 2% commit fraud (200 people; your real base rate is unknown, so ask for it). Even if the model is 90% right on both fraudsters and non-fraudsters:
- It finds 180 of the 200 fraudsters.
- It also flags 980 innocent people.
- Of the ~1,160 flagged, only about 1 in 7 is actually committing fraud.

And you want investigators to work the top 10%, which is about 1,000 files. Ask for precision at the top 10%, recall, false-positive rate, and the figures broken down by group. Also ask what "fraud" means in the training labels: intentional fraud, or any recovery or administrative error? Labels built from past investigations only reflect where people looked before, so the model learns your historical attention, not fraud. That creates a feedback loop.

**2. Dutch history makes this the highest-scrutiny use case there is.**
- Toeslagenaffaire: risk profiling and a fraud-first culture ruined thousands of families.
- SyRI was ruled unlawful by the Hague court in 2020: pooling data across systems for fraud risk scoring.
- Rotterdam's welfare fraud algorithm was suspended and later found to disadvantage groups through its variables (reported 2023).
- Amsterdam's Smart Check pilot was stopped in 2025 after it failed bias testing.

These are your peers, and the Algemene Rekenkamer and the Autoriteit Persoonsgegevens (AP) have both been explicit about algorithms in government. Treat that as the reference class for your project, not the vendor's brochure. A "top 10% of everyone" score is the same pattern again. 🟢 (history: verified, though check the latest status of each case before you cite it in a council paper).

**3. The data mix is the real problem.**
- Debt-counselling data was given by people in trouble to get help. Using it to flag them for investigation is a purpose change (AVG purpose limitation) and is hard to defend. It also has a chilling effect: people will stop seeking debt help, which makes the social problem worse and costs you more later.
- Housing data and benefits data together is exactly the kind of linkage SyRI was struck down for.
- Features like postcode, household composition, or debt can act as proxies for ethnicity, migration background or poverty.
- A DPIA is mandatory here. If the residual risk is high you must consult the AP before starting. An automated decision with legal effect (stopping a benefit) on the score alone falls under AVG art. 22, so a human decision-maker with real authority is required.

**4. Six months is not realistic.**
Before go-live you need, at minimum: a legal basis check, a DPIA, a human-rights and algorithm impact assessment (IAMA), a bias and quality audit on your own data, registration in the algorithm register, a procurement route (Aanbestedingswet, likely above the European threshold, with a proper ADR-style decision record), and the AI Act obligations for high-risk systems (risk management, data governance, human oversight, logging, transparency). Add integration across three source systems and training for investigators. Doing all of this in six months, with a vendor "live in 6 months" promise, means skipping something, and the skipped item is usually the audit.

**5. Vendor and exit risk.**
You would be handing your most sensitive citizen data to a vendor and a model you cannot fully explain. Under the evaluation framework I use, you need explainability (can you tell a citizen and a judge why they were flagged?), a contractual right to audit the model and its training data, data residency in the EU, no vendor training on your data, and an exit clause. If the vendor won't commit to these, that is your answer.

## How to act

**Next 2 weeks**
1. Ask the vendor for written answers: base rate assumed, precision and recall at the top 10%, performance split by group (age, gender, nationality or migration background, household type), how "fraud" was labelled, which features are used, what the model explains per case, where it runs, and who else uses it and with what outcome.
2. Brief your Data Protection Officer (FG), legal counsel, and the CISO. Start the DPIA and the IAMA now; do not wait for the contract.
3. Write down the problem you are solving. How much fraud is estimated, what does it cost, and how does investigation capacity limit you today? Without a baseline you cannot show the system worked.

**Months 1 to 6: "prepare and prove" in place of "go live"**
- **Fix the data basis first.** Define the lawful basis, and exclude debt-counselling data entirely unless counsel confirms a lawful basis. Strip out proxy variables.
- **Consider a simpler first step.** Transparent, rule-based risk indicators built with investigators (specific, explainable signals such as inconsistencies between declared and registered data) plus random sampling. These are explainable to a citizen and a judge, cheaper, and give you the unbiased labels any later model needs.
- **If you still want a model, run a limited pilot** with: a retrospective back-test on your own historical data, bias metrics agreed in advance with go/no-go thresholds, a control group (random selection) to measure whether the model beats chance, a human investigator who must verify before any action, no automatic benefit stops, and an objection route for citizens.
- **Governance:** an independent review (e.g. the Rekenkamer-style audit questions, an external algorithm auditor), council oversight, publication in the algorithm register, and a client-council (cliëntenraad) consulted early. Record the decision as an ADR with 3-year TCO including audit, monitoring and legal costs, and a do-nothing and a rules-based alternative.
- **Procurement:** only issue a contract with audit rights, explainability, EU hosting, exit and a termination right if the bias tests fail.

**Kill criteria (agree them now, with the alderman)**
Stop or do not proceed if: no lawful basis for any of the three data sources, the DPIA shows high residual risk, error rates differ materially across groups, precision at the top 10% is not clearly better than the simple-rules baseline, or the vendor refuses audit.

**Month 6 outcome:** a decision paper to the council with evidence, not a go-live.

## Your decision

- **Recommended:** reframe the deliverable from "live in six months" to "a tested, lawful, accountable approach in six months", and tell the alderman plainly that the failure cases in the Netherlands all involved moving fast on this exact kind of project.
- **Alternative if the council insists on speed:** go live only with a rules-based, explainable, benefits-data-only approach under human review. I would not accept the full three-system model at that speed.
- **Don't:** sign the vendor contract on the strength of the 90% figure, or let the debt-counselling data into the model.

What I would want from you to firm this up: the vendor's written answers (point 1 above), your estimated fraud rate, and the legal basis your verordening gives you for sharing data across these systems. I would also verify the current AI Act dates, since the Digital Omnibus may change them, and the status of the Rotterdam and Amsterdam cases before you quote them to the council.
