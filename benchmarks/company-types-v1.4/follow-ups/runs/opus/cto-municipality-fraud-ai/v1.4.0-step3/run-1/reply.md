**My advice: don't buy this system as specified, and don't commit to going live in six months. Instead, offer the alderman a six-month plan that makes fraud enforcement measurably better now. Any risk model becomes a separate, later decision, once you've tested whether it adds anything.** Two numbers explain why:

- Suppose 5% of recipients commit fraud. Then a "model" that clears everyone is 95% accurate, so "90% accurate" tells you nothing until you know what was measured.
- Suppose "90%" means it catches 9 in 10 fraud cases and clears 9 in 10 honest people. With 3,000 recipients it would flag 135 real cases and 285 honest people: two in three of the people flagged did nothing wrong. Even a perfect model would put at least 150 innocent people among the top 10% (300 people). These are illustrative figures, so swap in your own.

I've drafted an advice note for the alderman and the college, `advice-note.md`, with the numbers, the legal table, pilot conditions and questions for the vendor.

**Why this design is the risky one**

- **What it learns.** It would learn from past investigations, which reflect whom investigators chose to check, and from "fraud" as the Participatiewet records it: any unreported change, deliberate or not. That points to people with irregular income, complicated households or weak Dutch: vulnerability, not dishonesty. Rotterdam's risk score (2017–2021) used language, gender and age, and the city stopped it after its court of audit criticised it.
- **The data.** Debt-counselling data was collected to help people. Using it for fraud scoring needs its own legal basis, and it teaches people in debt to avoid the early help you want them to seek. Use housing data only where it ties directly to a benefit condition, such as who lives at the address.
- **The legal floor** (as of November 2026; not legal advice, so have your data protection officer and lawyers confirm):
  - In the SyRI case (February 2020), the court in The Hague struck down risk scoring of benefit recipients for lack of transparency and safeguards.
  - The AI Act's ban on social scoring has applied since February 2025. Scoring people on data from an unrelated context, such as debt help, comes close to it.
  - AI used to grant, reduce, revoke or reclaim public benefits is high-risk under the AI Act. The duties for organisations using it (a fundamental rights impact assessment, human oversight, registration, telling the people affected) apply from December 2027. Anything you buy now has to meet them.
  - The GDPR requires a data protection impact assessment (DPIA) before you start. Under the EU Court of Justice's SCHUFA ruling (2023), a score that largely decides who gets investigated can count as an automated decision.
- **Six months** isn't enough for a tender, a DPIA, a human-rights impact assessment (IAMA), a legal basis for the data, testing on your own data and an independent bias test. Something has to give, and it will be the safeguards. The childcare benefits scandal shows where that ends.

**Three options**

1. **Recommended, months 0–6: improve current enforcement and measure it.**
   - Set a baseline: investigations per year, the hit rate for each selection route (tips, Inlichtingenbureau signals, random checks), amounts recovered, and how much was intent and how much was mistakes.
   - Add a small random sample to learn the real rate of violations. Any future model has to beat that.
   - Use the clear, lawful signals you already receive, and fix the main causes of mistakes at the source: income reporting and changes in the household.
   - Involve the investigators, the client council and the works council from the start. The works council has an advisory right on major new technology.
2. **Conditional, decided around months 9–12: a narrow pilot of a model, only if the baseline shows a gap a model could close.** Benefits data only, with no nationality, language, postcode or stand-ins for them. Explained scores, an independent bias test, investigators deciding, comparison with random selection, and stop criteria agreed in advance.
3. **As asked: buy and go live in six months.** I'd advise against it. The risks fall on the residents least able to absorb them, and politically on the alderman.

**The other side, fairly.** The council's goal is legitimate: enforcement is a legal duty, it protects public money and support for the scheme, and investigators' time is scarce. Option 1 serves that goal, and in six months the alderman has results to report, not a procurement still under way.

**How to raise it.** Talk to the alderman in private first, before any council paper. You could say: "I share the goal of focusing our investigators. I can show you better results within six months without putting everyone on benefits under suspicion. What I can't do is make this system lawful and fair by then." Ask the vendor in writing what the 90% measures, on whose data, and what counted as "fraud". The full list of questions is in the note.

**Two questions that would change my answer**

- Did the council ask for this specific system, or for better enforcement? Option 1 delivers the second; for the first, the college reports back with reasons.
- How much is lost to fraud now, and how well does your current selection perform?

**Assumptions:** about 3,000 recipients and a violation rate of 2–5% (at 2%, 84% of those flagged would be innocent); the vendor's figure hasn't been tested on your data; and there's no legal basis yet for using debt-counselling data in fraud checks. I couldn't re-check the sources today, so confirm the dates before the paper goes out.

What am I missing, and what would make this wrong?
