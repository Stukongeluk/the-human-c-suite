**Advise the council not to buy this system as proposed, and not to promise go-live in six months.** Offer instead a six-month programme that ends with a decision the council can defend: a baseline, a legal assessment, and a small shadow-mode pilot on benefits data only. Two reasons carry the advice: "90% accurate" says almost nothing about how many innocent people would be flagged, and pooling debt-counselling and housing data for fraud scoring is the part most likely to fail legally and politically. I haven't seen the vendor's documents, so what follows is a framework to test them against, not a verdict on this product.

**1. What "90% accurate" hides**

Fraud is rare, so accuracy is the wrong measure. An illustrative case (your real numbers will differ): 10,000 recipients, 2% committing fraud, so 200 cases. A model that is 90% right on both fraudsters and non-fraudsters finds 180 of them but also wrongly flags 980 of the 9,800 honest people. Of about 1,160 flagged, roughly 85% are innocent. The vendor must give you, on your own data: the precision in the top 10%, the false-positive rate, and the error rates by group (age, nationality, neighbourhood, single parents). It must also say what "fraud" meant in the training data. If it means "past investigations that found something", the model learns where we looked before, and it will keep looking there.

**2. Why the three data sources are the problem**

- Debt-counselling data was given so people could get help. Reusing it to flag them for investigation is a purpose-limitation problem under the GDPR, and it teaches vulnerable residents to stay away from help.
- Dutch history is blunt here: the court halted SyRI in 2020 on privacy grounds, and the childcare benefits scandal wrongly branded more than 20,000 families as fraudsters, partly through risk profiling, and brought down the cabinet in 2021. Residents and journalists will ask first about this system, and the council will own the answers.
- Under the AI Act, systems that evaluate people's eligibility for public benefits are generally high-risk, with a mandatory fundamental-rights and data-protection impact assessment, human oversight and bias testing. Most of those obligations apply from December 2027 after the Digital Omnibus delay, but a contract signed now has to meet them. Whole-population scoring built on unrelated personal data also sits close to the Act's ban on social scoring, already in force. Your DPO and legal counsel need to rule on this before procurement, not after. This is not legal advice.

**3. The honest comparison**

The investigators' capacity is the real constraint, so the question is whether a model beats the alternatives:

- Tips, existing signals and simple rules on benefits data alone.
- Fixing the process: much "fraud" is errors in a complicated system, and prevention at intake is cheaper than recovery.
- A pilot of the model on benefits data only, in shadow mode, compared with what investigators find anyway.

I would put these side by side by cost per euro correctly recovered and harm per wrongly flagged household, with criteria fixed before anyone scores them, and with the vendor's claims tested by someone who doesn't sell it.

**4. A plan that fits the six months**

- *Months 1-2:* baseline (current caseload, hit rate, recoveries, how errors are separated from intent), DPIA and impact assessment, early talks with the investigators and the works council on how they would use scores.
- *Months 2-4:* procurement with fixed criteria and weights, declared interests, and contract terms for audit access, bias testing, no data reuse by the vendor, and a clean exit.
- *Months 4-6:* shadow-mode pilot, benefits data only. No score triggers action alone, and every flag gets human review by someone who can overrule it. Citizens can see why they were selected and can contest it. Register the system in the algorithm register.
- *Decision gate:* go live only if precision, group-level error rates and recoveries beat the baseline on pre-agreed numbers. Stopping is an acceptable result.

The alderman still gets visible progress in six months: a live pilot, a published method, and a legal footing. Going live fast with the wrong data is the risk that ends careers, his and yours.

**5. Safeguards for the investigators**

A "top 10%" list will turn into a quota unless you say otherwise. Measure outcomes at team level, don't rank investigators by hit rate, and keep room for judgement. They are the human check, and they carry the blame if the model is wrong.

**6. What I'd ask you before you advise**

- What is the evidence of fraud here today, and how much is intent rather than error? That decides whether scoring is even the right tool.
- Who selected the vendor, and has anyone with a stake in it declared it?

**What I'm assuming:** a roughly 2% fraud rate (illustrative), no connection yet between the three systems, and that the vendor hasn't shown precision figures. I'm also assuming the council wants control over where the model is allowed to be used, not only a go-live date. What am I missing, and what would make this wrong?

If useful, I can draft the one-page council memo or the questions to put to the vendor.
