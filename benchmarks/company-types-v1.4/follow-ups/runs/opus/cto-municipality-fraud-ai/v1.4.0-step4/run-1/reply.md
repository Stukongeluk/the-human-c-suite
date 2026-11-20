My advice: don't buy this system as specified. Give the alderman a plan that serves the same goal, investigators spending their time on real cases, and shows results in six months. Whether to use a model then becomes a later council decision, made with your own numbers.

The number behind it: if the model flags the top 10% and is "90% accurate" in the usual sense (the share of correct yes/no calls), the arithmetic means it misses half the real cases, whatever the fraud rate. Take 2,500 households on benefits and a real fraud rate of 5% (both assumptions; you have the real figures). Then 250 households get a fraud investigation, often with a home visit. About 60 of them have a real case and about 190 don't. At a 2% rate, nine in ten of the people investigated have done nothing wrong. A model that flags nobody would be 95–98% "accurate".

**Why not this system**

- **"90% accurate" doesn't answer the questions that matter.** Ask the vendor in writing for:
  - the hit rate in its top 10%, and the share of all real cases it finds
  - its false-positive rates by gender, age, nationality, language and postcode
  - what counted as "fraud" in its training data, and whose data that was

  A model trained on past investigations learns who was investigated before, not who committed fraud.
- **The law applies now, not in 2027.**
  - The AI Act's ban on social scoring has applied since February 2025. Scoring people on data from unrelated contexts, such as debt counselling and housing, and then treating them worse comes close to the line Article 5(1)(c) draws. That needs a legal opinion before any procurement.
  - AI that public bodies use to grant, cut or reclaim benefits is high-risk under Annex III. The Digital Omnibus moved those obligations to December 2027 ([Orrick, July 2026](https://www.orrick.com/en/Insights/2026/05/EUs-Digital-Omnibus-on-AI-7-Key-Changes-You-Need-to-Know)), but that delay isn't a window. The GDPR already requires purpose limitation, a legal basis per data source and a DPIA. And in 2020 the Hague court stopped SyRI under Article 8 of the ECHR for this kind of opaque data linking.
  - Debt-counselling data is the worst part. People gave it to get help, and it can include health information. Using it for fraud selection teaches people in debt to avoid the help that prevents bigger problems.

  This isn't legal advice. Your data protection officer and legal team need to confirm it.
- **Dutch attempts like this have ended badly.**
  - The childcare benefits scandal: risk profiling helped wrongly accuse more than 20,000 families.
  - Rotterdam's welfare model, stopped in 2021, scored young mothers and people with weaker Dutch as higher risk.
  - DUO's student-grant checks led to a ministerial apology for indirect discrimination in 2024.
  - Amsterdam's "Slimme Check" tried harder on fairness than most and was halted after its pilot still showed bias.

  Citizens with the thinnest buffer paid first; the government paid later in trust and money.

Six months can't hold the required work either: a legal opinion on Article 5, a DPIA, a human-rights impact assessment (IAMA), an independent bias test, probably a European tender, and the works council's advice on a major new technology in the investigators' work.

**What the council has right:** public support for welfare depends on it being fair, and investigators are scarce. In the example, the model finds about 60 cases where 250 random checks would find about 13. So answer the goal, not just the purchase.

**The options**

- **A. Buy now, live in six months:** fastest, riskiest for people and legally, hardest to undo.
- **B. Fix and measure for six months, then decide on a model:** my recommendation.
- **C. No model, just better rules and process:** cheapest, and possibly enough. B will tell you.

**Option B in six months**

1. **Measure the real problem (months 1–3).** Review a random sample of about 200 files for the true overpayment rate and its causes, and measure your investigators' current hit rate per signal source. I expect, to be tested, mostly unreported income or household changes, not deliberate fraud.
2. **Use and fix what is lawful today (months 1–6).**
   - Work through the Inlichtingenbureau and Suwinet signals you already get. They are rule-based, lawful, equal for everyone and explainable.
   - Make changes easy to report, pre-fill income data, and write letters people understand.
   - Give investigators a proper case and workflow tool. That's IT you can deliver in six months.
3. **Set the bar for any future model (by month 6).** Fix the criteria before any vendor is scored:
   - benefits data only, each source with a legal basis
   - independent bias testing, including proxies such as postcode
   - publication in the algorithm register
   - a person decides, and the citizen can see why and challenge it
   - a shadow-mode test against random selection, with a stop criterion

   Involve the client council and the works council now, not after the purchase.

In month 6 the council decides with real numbers. A model, if chosen, is a 12–18 month route.

**A line for the alderman:** "I share the goal: investigators spending their time on real cases. This system, as specified, is the route Rotterdam and the tax authority took. Here's a plan that shows results in six months and lets the council decide on a model with our own numbers."

**What would change my advice:** independently validated error rates per group on Dutch municipal data, benefits data only, and a legal opinion clearing Article 5. Even then, not in six months.

I assumed "90% accurate" means overall accuracy. I couldn't run fresh web searches today, so have legal check the cases and dates before this goes to the college.

What am I missing, and what would make this wrong? I can draft the advice note for the alderman (in Dutch or English) and the vendor questions.
