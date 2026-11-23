**Advise the council not to buy and go live in six months. Advise a staged route instead: a six-month decision and design phase (legal basis, impact assessment, independent test, residents and staff involved), with any live scoring only after those gates pass, and only if the numbers justify it.** The vendor's "90% accurate" tells you almost nothing, and the plan as described has a real chance of repeating Dutch history.

**Why "90% accurate" is not enough**

Accuracy depends on how rare fraud is. Illustration only, with my assumptions: 4,000 recipients, 2% with real fraud (80 people), and a model that is right 90% of the time on both fraudsters and non-fraudsters.
- It flags 72 of the 80 fraudsters, and also 392 of the 3,920 honest people.
- Of 464 flagged, about 15% are fraudsters. Roughly 85% of the people your investigators would be pointed at did nothing wrong.

Ask the vendor for precision at the top 10%, false-positive rates per group (nationality, age, gender, postcode, single parents, people with debts), and results on a municipality like yours, tested by someone other than the vendor. Fraud labels also come from past investigations, so the model may mostly learn where you looked before. That is a bias loop, not a prediction.

**Why this is the high-risk kind of system**

- Dutch precedent: the court stopped SyRI in 2020 as disproportionate, the childcare benefits scandal wrongly branded over 20,000 families as fraudsters and brought down the cabinet in 2021, and Rotterdam's welfare-risk model was suspended after criticism. Please verify the exact details before citing them to the council.
- Debt-counselling data is the sharpest problem. People share it to get help. Reusing it to flag them as fraud risks is a purpose-limitation question under the GDPR, and it will make vulnerable residents avoid help. I doubt you have a lawful basis; your privacy officer and a lawyer must say.
- Under the AI Act, AI that decides on access to public benefits is high-risk, with obligations from December 2027 (check current dates). You would be buying a system that has to be compliant within roughly a year of going live. You also need a DPIA, an impact assessment on human rights and algorithms (IAMA), registration in the algorithm register, human review of every flag, and bias testing that includes proxies. A flag must never itself be grounds to cut or suspend a benefit. This is not legal advice.
- Residents: tell them, let them see their own data and object. Involve the client council, your investigators and, where the system touches their work, the works council (consent rights on monitoring systems).
- A vendor's flag does not pass on your responsibility. If a subcontractor or the vendor's model is wrong, the municipality answers.

**What I would put to the council instead**

1. **Fix the cause first.** Most benefit overpayments come from complexity and mistakes, not intent. Analyse closed cases: how many were errors, late reporting, or our own processing mistakes? Simpler forms, fewer re-claims and earlier contact cost less and harm no one.
2. **Focus investigators without scoring people.** Use tip-offs, specific rule-based data matches that already have a legal basis, and case-level triage by experienced staff. Measure outcomes per team, not per person.
3. **If the council still wants a model:** use benefits data only, start with a shadow run in which nobody acts on the scores, and have an independent party check false positives and group differences. Set stop criteria up front: for example, halt if the precision at the top 10% is below an agreed level or if any group is flagged disproportionately. Keep the ability to switch it off.
4. **Procurement:** require the model documentation, the right to audit, your ownership of the data and the exit terms. Do not sign a multi-year contract before the gates pass. Declare the interests of everyone who scores the vendors and fix the criteria first.

**Timeline for the alderman:** within six months you can deliver the case analysis, the legal assessment, the DPIA, the vendor test and the involvement of residents, and the first process improvements. That is a decision he can defend. A live system that is later struck down, or that wrongly accuses residents, is a political liability he will own.

**The seats beyond IT:** the CFO question is the full cost (licences, review staff, objections, legal claims, and the savings that fraud recovery actually yields). The CEO or town clerk question is public trust. The product question is whether this helps residents or only investigators.

**Two questions that would change my advice:** what share of your closed cases were errors versus intent, and does the vendor have a lawful basis for combining debt-counselling data?

**Assumptions and limits:** I have not seen your data or the vendor's documentation, and the numbers above are illustrations. What am I missing, and what would make this wrong?
