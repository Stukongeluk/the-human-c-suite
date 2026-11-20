# Advice: AI fraud-risk scoring of welfare recipients

**Short version:** do not advise "yes, in six months" and do not simply say "no". Advise the council that a system which scores every benefit recipient using debt-counselling and housing data is, as proposed, legally exposed, technically unproven and politically dangerous. Advise a gated route instead. The first gate is a legal and impact assessment, and the six-month go-live is only possible if every gate is passed, which is unlikely. The alderman should hear this now rather than in month five.

## 1. Why the proposal is risky

**The Dutch track record is the main argument.**
- *SyRI* (2020): the Hague court struck down the risk-profiling legislation as a violation of Article 8 ECHR.
- *Toeslagenaffaire*: risk models and nationality-based profiling contributed to a state scandal.
- *Rotterdam's welfare-fraud algorithm*: investigative journalists (Lighthouse Reports/Argos/Follow the Money, 2023) showed it scored people higher on factors such as gender, language and parenthood. Rotterdam stopped using it.
- *Amsterdam's "Smart Check" pilot*: as I understand it, it was halted in 2025 after bias testing, despite explicit fairness mitigation. Verify the details before quoting them to the council.

A council and a CIO who buy this system will be compared with these cases. Check the facts before citing them.

**"90% accurate" tells you almost nothing.** Fraud is rare among benefit recipients. Take a simple example with 10,000 recipients, 2% actual fraud, and a model that is 90% sensitive and 90% specific:
- 200 fraudsters, of whom 180 are caught.
- 9,800 non-fraudsters, of whom 980 are wrongly flagged.
- Only about 15% of flagged people are actual fraudsters, so about 85% of the people investigated are innocent.

Each of those is a person under investigation, possibly with a benefit suspended. The vendor must give you precision, recall and false-positive rates at the top-10% cutoff, on data from a comparable municipality, broken down by group. They must also say how "fraud" is defined. Intentional fraud, administrative error and late reporting are very different outcomes.

**Training labels are biased.** If the model learns from past investigations, it learns where investigators looked, not where fraud occurs. Targeting then produces more findings in the targeted group, which feeds the next model. This is a feedback loop, and "10% highest risk" will concentrate on already vulnerable groups.

**The data sources are the most sensitive part.**
- Debt-counselling (schuldhulpverlening) data was given in confidence so that people could get help. Reusing it for enforcement runs into purpose limitation (GDPR Art. 5(1)(b)), the confidentiality duties in the schuldhulpverlening framework, and the risk that people stop seeking help.
- Housing data adds more proxies for ethnicity, family situation and poverty.
- You need a specific statutory basis for each data flow. "The council wants it" is not one. Ask your legal department and the FG (data protection officer) directly.

## 2. Legal and regulatory position

- **EU AI Act:** AI systems used by public authorities to evaluate eligibility for essential public benefits and services are listed as high-risk (Annex III). Deployers that are public bodies need a fundamental rights impact assessment (Art. 27), human oversight, logging, transparency to those affected, and a conforming vendor. Pure profiling-based prediction of criminal offences is a prohibited practice (Art. 5(1)(d)). Whether a fraud score falls under that depends on design, so have it assessed. The application dates for the high-risk obligations have been the subject of postponement proposals (Digital Omnibus). Check the current timeline with legal, but plan as if the obligations will apply during the contract's lifetime.
- **GDPR:** a DPIA is mandatory and must be completed *before* processing. Art. 22 limits decisions based solely on automated processing. If the DPIA shows high residual risk, you must consult the Autoriteit Persoonsgegevens beforehand.
- **Dutch rules:** the Algoritmeregister obligation for government, the *Impact Assessment Mensenrechten en Algoritmes* (IAMA) and the national algorithm framework, plus non-discrimination law (Art. 1 Grondwet, College voor de Rechten van de Mens).
- **Participatiewet and enforcement:** the legal route from "high score" to investigation and sanction must have proper due process, reasoning and an objection route. A score is not evidence.

## 3. Why six months is not realistic

A responsible sequence is legal basis, DPIA, IAMA and FRIA, data-quality work and bias testing on your own data, a parallel-run pilot, procurement with proper contract terms, the algorithm register, training investigators, an objection procedure, and an audit. Rushing this is exactly how earlier failures happened. A go-live date set by politics, before the legal basis exists, shifts the risk onto you personally and onto the people affected. If the council still wants a date, make it a *decision* date (go/no-go on pilot), not a *live* date.

## 4. What I would advise the council

**Reframe the goal.** The goal is not "an AI model" but "less fraud and fewer errors in benefits, at proportionate cost and with trust intact". Ask what the current fraud and error rate is, what it costs, and what investigators cannot do today. Without a baseline you cannot show the system worked.

**Consider cheaper and safer options first:**
- Better checks at intake and at changes in circumstances (data already legally available, for example via the Inlichtingenbureau/SUWI-chain).
- Transparent, rule-based signals tied to a specific indicator, with a human reviewing the underlying facts.
- Peer-municipality cooperation and shared investigation expertise.
- Investment in error prevention (clear forms, proactive contact), which often recovers more than fraud investigation.

**If the council still wants an AI model, set gates:**
1. **Legal basis and DPIA/IAMA/FRIA** completed, with the FG and an external review. No debt-counselling data unless counsel confirms a lawful basis. Start with data you may legally use.
2. **Independent validation:** vendor performance on *your* data, with precision/recall, subgroup fairness metrics (age, gender, nationality, postcode, family type), and an explanation of every feature. Exclude proxies. Prefer an interpretable model.
3. **Silent pilot (shadow mode):** run it without acting on scores for several months and compare with caseworker findings. Stop if the false-positive rate or group disparities are too high.
4. **Human-led process:** the score may only prioritise a *review*, never trigger a sanction. Investigators need to see the reasons, be trained on automation bias, and be able to override. Record outcomes.
5. **Citizen safeguards:** register entry, plain-language notice, objection route, and a monitored complaint line.
6. **Contract terms:** use the PIANOo/government model contract clauses for AI procurement. Require audit and access rights, documentation, bias-testing duties, no vendor reuse of your data, exit and escalation terms, and a right to stop with no penalty.
7. **Ongoing monitoring:** quarterly fairness and drift reports to the council, and a sunset clause.

## 5. Questions to put to the vendor this week

- What exactly does "90% accurate" measure, on what data, and what are precision and recall at the top-10% cutoff?
- What is the label ("fraud")? Who produced it?
- Which features are used, and how do you exclude proxies for protected characteristics?
- Can you show bias results from a comparable Dutch municipality? Have any customers stopped using it, and why?
- Where is data stored and processed, and does anything leave the EU?
- Which AI Act and GDPR documentation do you provide?

## 6. How to put it to the alderman

"We can deliver a controlled pilot decision within six months. We cannot responsibly put a fraud score on every benefit recipient by then, because the legal basis, the DPIA and the bias test on our own data don't exist yet. Skipping them risks the outcome that SyRI and Rotterdam produced: a halted system, damage to residents, reputational harm, and wasted spending. I recommend we approve the assessments and a shadow pilot now, with a go/no-go at the end."

I would also put your advice in writing, with the legal and DPO opinions attached, so that the decision and the accountability sit where they belong.

*Caveat:* I am not a lawyer. The legal points above need confirmation from your own legal department, the FG and, where relevant, the AP. Check the case details and AI Act timeline before they go into a council paper.
