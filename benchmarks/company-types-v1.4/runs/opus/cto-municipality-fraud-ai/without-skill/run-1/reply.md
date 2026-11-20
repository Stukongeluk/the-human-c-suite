**Short version:** Advise the college not to buy this system as described. Advise them not to accept a six-month go-live for anything like it either. Put that advice in writing. Then give the alderman something he can deliver in six months: a sharper, defensible approach to enforcement, plus the facts needed to decide whether any algorithm is warranted at all.

This isn't an "AI is bad" position. The problem is this specific design: score every benefit recipient, using debt-counselling and housing data, to decide who gets investigated. The Netherlands has tried that design several times. It has ended in a court ruling, fines, public apologies and, once, a cabinet resignation.

## Why I'd advise against it

**1. It may be unlawful, not just risky.**

- **Possible prohibited practice.** Since February 2025 the EU AI Act has banned social scoring by public authorities (Art. 5(1)(c)). That means scoring people on personal characteristics where the score leads to unfavourable treatment in a context unrelated to where the data was collected, or to treatment out of proportion to what they did. Fraud scoring as such isn't banned. What pushes this proposal towards the ban is the data it pulls in: residents gave information to the debt-counselling service to get help, and it would now be used to pick them for fraud investigation. The Commission's guidelines on prohibited practices use welfare-fraud scoring built on unrelated data as an example of where the ban applies. Whether this crosses the line is a legal judgement, and you need it in writing before anyone signs anything.
- **At minimum, high-risk.** AI that public authorities use to assess eligibility for public assistance, or to reduce, revoke or reclaim it, is high-risk under Annex III. As the deployer you would need:
  - a fundamental rights impact assessment
  - competent human oversight and logging
  - registration in the EU database
  - to tell the people being scored
  - to be able to explain individual outcomes (Art. 26, 27, 49 and 86).

  The vendor needs a conformity assessment and technical documentation, and you should see both before you buy.
- **GDPR.** Debt-counselling data was collected to help people get out of debt. Reusing it for fraud scoring is a textbook purpose-limitation problem (Art. 5(1)(b) and 6(4)), and I doubt you have a legal basis for it. A DPIA is mandatory; fraud prevention and profiling are both on the AP's list of processing that always requires one. With residual risk this high, expect a prior consultation with the AP, which alone can take up to 14 weeks. Under the CJEU's SCHUFA ruling (C-634/21), a score that in practice decides who gets investigated can also count as an automated decision under Art. 22.
- **SyRI.** In 2020 the District Court of The Hague struck down SyRI under Article 8 ECHR: too opaque, not verifiable, not proportionate. SyRI linked benefits, housing, debt and other government data to flag fraud risk. Your proposal is a municipal version of the same idea.

**2. "90% accurate" tells you nothing, and the real numbers are uncomfortable.**

Fraud is rare, so accuracy is the wrong measure. If 3% of recipients have a real issue, a "model" that flags nobody is 97% accurate. What matters is how many of the people you flag actually did something wrong.

Here is a worked example; put your own figures in. Say 2,500 people are on benefits, 3% of them have a real issue (75 people), and investigators take the top 10% (250 people):

| Scenario | Real cases found | Flagged people who did nothing wrong | Real cases missed |
|---|---|---|---|
| Vendor's "90% accurate", taken at face value at a 10% cut-off | ~37 | ~212 (85% of the list) | ~38 |
| A perfect model | 75 | 175 (70% of the list) | 0 |
| 250 picked at random | ~7 | ~243 | ~68 |

Two things follow:

- **Most of your top 10% will be innocent, even with a perfect model**, as long as fewer than 10% of recipients commit fraud. That is arithmetic, not a flaw in the model.
- **The model may well beat random selection, but at a price.** Each run sends about 200 households through an investigation. You can't give them a reason for it, and you can't fully explain it to the council.

The 90% figure is itself suspect. Models like this are trained on the outcomes of past investigations, and past investigations weren't random. So the model learns who you used to look at and sends you back to them, which is a feedback loop. That is what happened in Rotterdam: its model rated women, young parents and people with limited Dutch as higher risk. Debt and housing data make this worse, because they act as proxies for poverty, household make-up and often migration background.

**3. The Dutch track record is clear.**

- **Toeslagenaffaire:** a risk model that used nationality, an AP fine and a cabinet resignation.
- **SyRI:** struck down in court.
- **Rotterdam:** model suspended in 2021 after criticism from its own audit office (Rekenkamer), then picked apart in public in 2023.
- **DUO:** risk profiling of students stopped after it was found to select students with a migration background far more often; the government apologised.
- **Amsterdam's "Slimme Check":** built on purpose as the responsible version, with an explainable model and bias correction, and shelved after the pilot still showed bias.

If Amsterdam couldn't make the careful version work, a six-month vendor rollout won't.

**4. Six months can't be done responsibly.** For a good system, all of this takes 12–18 months:

- a European tender
- the DPIA and the fundamental rights impact assessment
- a legal opinion on Article 5
- a possible AP prior consultation
- bias testing on your own data
- a pilot

If something is live in six months, it's live because some of these steps were skipped. When it goes wrong, the cost falls first on your poorest residents, then on the alderman, then on you.

There's also a quieter cost. Debt counselling only works if people come early. Once residents learn that asking for help raises their fraud score, the people you most want to reach will stay away. They will find out, because you'll be required to tell them.

## What I'd advise instead

The council's underlying goal is legitimate: use limited investigator capacity well and protect public money. Give the alderman a plan that meets that goal within six months.

**Months 0–3: get the facts.**

- Find out what fraud actually costs you now. Split intentional fraud from honest mistakes with the duty to report changes, and look at current hit rates and amounts recovered.
- Run a random-sample check of a few hundred files. It's defensible, it doesn't discriminate, and it gives you the true error and fraud rate. Any vendor claim has to be measured against that number.
- Get a formal legal opinion on three questions: Article 5 of the AI Act, the GDPR basis for each data source, and SyRI. It should come from your data protection officer (FG) and legal team, with outside counsel if needed.

**Months 3–6: improve enforcement without profiling people.**

- **Signal-based checks.** Check concrete, verifiable discrepancies, such as Inlichtingenbureau/Suwinet matches on undeclared income or BRP registrations at an address, instead of scoring people on who they are.
- **Prevention.** Send clearer letters, make it easy to report changes, and do regular check-ins. Many "fraud" cases are people who didn't understand a rule, and the national revision of the Participatiewet is moving the same way.
- **Report to the council at month 6** with results and the baseline. That's the alderman's deliverable.

**After that, only if the data justifies it.** If there's a real gap that better selection would close, scope a narrow, explainable tool with these conditions:

- no debt-counselling data
- no protected characteristics or obvious proxies
- a DPIA and a fundamental rights impact assessment (IAMA), with the client council involved
- an independent bias audit on your own data
- a pilot with a random control group
- humans make the decisions and record their reasons
- registration in the algorithm register
- an evaluation and sunset clause

The council then decides go or no-go on the evidence.

## Questions to put to the vendor now

These cost little to ask and will tell you a lot:

1. What exactly does "90% accurate" measure? Give precision and recall at a 10% cut-off, the population tested and its fraud rate.
2. What labels was the model trained on, and how were those cases originally picked for investigation?
3. Which variables does it use? Does it use nationality, country of birth, language, gender, age, postcode or household composition, or proxies for them?
4. What are the bias results per group? Will you let an independent party test the model on our data before we sign?
5. On the AI Act: are you the provider, where is your conformity assessment, and can we see the technical documentation and instructions for use?
6. Can it explain an individual score in terms an investigator and a resident can both understand?
7. Which Dutch municipalities use it, and did their DPIA (and any AP consultation) clear?

If the answers are vague, that's your answer.

## How to bring this to the alderman

Don't frame it as "IT says no." Frame it as: "Here's how we deliver better enforcement in six months, and here's how we keep you out of the next SyRI headline."

- **Put it in a written advice to the college**, so the decision is taken with eyes open. The college is the data controller, not the vendor.
- **Bring in the FG now.** That's required for the DPIA anyway.
- **Talk to your investigators and your debt-counselling team.** They know where the real problems are, and they're the ones who would live with the list.

I've drafted that advice note, with the phased plan and the vendor questions, in `advice-memo.md`. It's in English; I can do a Dutch version for the college.

**Check before this goes into a council document.** I wrote this from my own knowledge and didn't check current sources. Have legal confirm when the high-risk obligations apply: the original date was 2 August 2026, and the EU's Digital Omnibus package proposed pushing it back. They should also check the case and guidance references above. Neither changes the advice, because the AI Act prohibitions and the GDPR apply today, and a system bought now has to comply for as long as you use it. If the vendor does come back with strong, locally validated, unbiased results using only directly relevant data, I'd revisit the third phase, just not on a six-month clock.
