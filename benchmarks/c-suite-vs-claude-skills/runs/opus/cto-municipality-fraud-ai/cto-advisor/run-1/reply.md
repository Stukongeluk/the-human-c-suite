# CTO advisor: AI fraud-risk scoring for welfare recipients

## BOTTOM LINE

Advise the alderman not to buy this system as specified and not to promise go-live in six months. Scoring every recipient on benefits, debt-counselling and housing data is the design that Dutch courts, the Dutch Data Protection Authority (Autoriteit Persoonsgegevens, AP) and the EU AI Act have already turned against. "90% accurate" tells you almost nothing, and the likely result is that most of the people your investigators visit have done nothing wrong. Offer him a six-month plan that improves targeting now and ends in a well-founded go/no-go decision.

Confidence: high on the direction. Medium on the legal details, which your data protection officer (FG) and legal team need to confirm.

## WHAT

1. **You would be rebuilding Rotterdam's system.** Rotterdam gave each of its roughly 30,000 recipients a risk score and sent the top 10% to investigators (2017–2021). Lighthouse Reports audited the code and found the system discriminated by ethnicity, age, gender and parenthood. Experts judged it little better than random. A court struck down the national SyRI system in 2020 under Article 8 ECHR. Amsterdam followed responsible-AI practice closely: no gender, nationality or age inputs, bias tests, reweighting and an external review. It also screened only new applications. It still stopped its pilot in November 2023 when bias came back in live use, after spending an estimated €500k or more. DUO selected students using only age, distance and education level, and that still discriminated indirectly. €61m has been set aside for refunds. [VERIFIED] Confidence: high.
2. **The EU AI Act treats this as high-risk, and the debt data may make it prohibited.** AI that public authorities use to grant, reduce, revoke or reclaim benefits is high-risk under Annex III 5(a). The Commission's 2026 draft guidelines name fraud-flagging of benefit claims as high-risk even when a caseworker takes over after the flag. Separately, the social-scoring ban in Article 5(1)(c) has applied since February 2025. It covers scores that lead to unfavourable treatment based on data from an unrelated context, or to treatment out of proportion to the behaviour. The Commission's guidance gives welfare agencies scoring fraud risk on unrelated data as an example of a prohibited use. Debt-counselling data comes from exactly that kind of unrelated context. [Sources VERIFIED; how they apply to this case ASSUMED] Confidence: medium-high.
3. **"90% accurate" is the wrong number to judge this by.** Say you investigate the top 10% and 5% of recipients really have an unlawful overpayment. Picking people at random already scores 86% "accuracy", because accuracy also counts everyone you correctly left alone. Take 3,000 recipients, so 300 investigations a year. A model with an AUC of 0.85 scores 90% accuracy, and 222 of the 300 people it flags are innocent. (AUC is the chance that the model ranks a real case above a non-case; 0.5 is a coin flip.) Even a model with 90% sensitivity and 90% specificity, far better than Rotterdam's, would leave about 170 of the 300 innocent. [Calculation; recipient count and prevalence ASSUMED] Confidence: high on the logic, medium on the exact figures.
4. **Debt-counselling data is the worst input you could add.** It is collected to help people. The VNG guide ties its processing to that purpose and advises restraint even for fraud checks inside debt help itself. Once residents learn that asking for debt help raises their fraud score, the people who most need help will stop asking, and problem debt costs the municipality far more than the fraud you would catch. Limit housing data to what already has a legal basis, such as address and household checks against the BRP (the municipal population register). [Partly VERIFIED; the effect on behaviour ASSUMED] Confidence: medium.
5. **Six months is not enough for a lawful go-live.** You would first need:
   - a DPIA (data protection impact assessment). If high risk remains, prior consultation with the AP can take 8 + 6 weeks.
   - a fundamental rights impact assessment (FRIA, Art. 27)
   - a legal basis for each data source
   - integration of three source systems
   - an independent bias test on your own data
   - possibly a European tender

   Plan for 12–18 months, and only if every gate passes. [ASSUMED from typical municipal timelines] Confidence: medium.

## WHY THIS MATTERS

If this goes wrong, you repeat what the Netherlands has already paid for in court rulings, AP fines, refunds and lost trust among the residents who depend on you most. Meanwhile your investigators spend most of their time on people who did nothing wrong. Also watch for a vendor argument that going live before 2 December 2027, when the AI Act's high-risk rules start to apply, keeps you outside the Act until 2030. It doesn't protect you: the GDPR, Article 8 ECHR, equal-treatment law and the social-scoring ban all apply today.

## HOW TO ACT

1. **Written advice to the alderman.** Send him written advice: "not this design, not this deadline; here is what we can deliver in six months". Ask for it to go to the college. **Owner:** you. **Deadline:** within 2 weeks.
2. **FG and legal opinions, no resident data.** Ask the FG for a formal opinion and legal for an AI Act classification (high-risk or prohibited). Give the vendor no resident data, not even for a demo, until the DPIA is done. **Owner:** you, with the FG and legal. **Deadline:** 4 weeks.
3. **Vendor questions.** Send the vendor the 12 questions in the memo: precision in the top 10%, error rates per group, how "fraud" was labelled in the training data, the full variable list, conformity documentation, audit access and exit terms. No answers means no further talks. **Owner:** you and procurement. **Deadline:** send within 2 weeks.
4. **Six-month track with Work & Income.** Run three things:
   - Check a random sample of about 200 files. That gives you real prevalence, honest mistakes versus fraud, and any bias in how people are selected today.
   - Clear the backlogs of signals you already receive lawfully: Inlichtingenbureau data matches and BRP changes.
   - Make it easier for residents to report income changes.

   **Owner:** head of Work & Income, with the enforcement team leader. **Deadline:** start in month 1, report in month 6.
5. **Go/no-go in month 6.** Bring a go/no-go decision to the council. Base it on the baseline, the legal opinions and, if the vendor cooperates, an independent sandbox test. **Owner:** the alderman, on your advice. **Deadline:** month 6.

## RISKS

- **The alderman goes ahead anyway.** Your written advice and the FG opinion put the risk on record. The DPIA is a mandatory gate, so there is no lawful go-live without it.
- **Saying no is not neutral.** The way investigators choose cases today may be biased too; Amsterdam found its caseworkers were. That is why the random sample measures the current process as well.
- **My legal reading may be stricter than your lawyers' in places.** Even if the Article 5 question goes your way, the high-risk duties and the Rotterdam and SyRI precedents remain.

## YOUR DECISION

- **Option A: buy as specified and go live in six months.** Fast and visible, but very likely unlawful in part (the debt data), unsupported on accuracy and exposed to the Rotterdam/SyRI outcome.
- **Option B: rule out algorithmic targeting entirely.** Legally safest, but it leaves the real problem, scarce investigator time, unsolved, and today's process unmeasured.
- **Option C (recommended): evidence first, then decide.** Run the six-month evidence track and improve targeting by lawful means. Then decide go/no-go on a narrow, explainable tool without debt-counselling data. It goes ahead only if the baseline, the DPIA/FRIA and an independent bias test support it. The alderman gets results in six months, just not this system.

**Detail:** see `advice-memo.md`. It has the decision record with a 3-year cost view, the base-rate table, the 12 vendor questions, a legal checklist, the six-month plan, go/no-go criteria and a critic's review of this advice.

**Not yet checked by:** your FG and legal counsel (the legal reading) or finance (the cost ranges in the memo).

**Sources**
- Rotterdam: [Lighthouse Reports, Suspicion Machines](https://www.lighthousereports.com/?p=1399)
- Amsterdam: [MIT Technology Review, June 2025](https://www.technologyreview.com/2025/06/11/1118233/amsterdam-fair-welfare-ai-discriminatory-algorithms-failure/amp/)
- SyRI: [Rechtbank Den Haag](https://www.rechtspraak.nl/organisatie-en-contact/organisatie/rechtbanken/rechtbank-den-haag/nieuws/2020/02/syri-legislation-in-breach-of-european-convention-on-human-rights)
- DUO: [Rijksoverheid, Nov 2024](https://www.rijksoverheid.nl/actueel/nieuws/2024/11/11/gecontroleerde-oud-studenten-met-uitwonendenbeurs-krijgen-geld-terug)
- Belastingdienst fine: [NOS, Dec 2021](https://nos.nl/artikel/2408587-boete-voor-belastingdienst-van-2-7-miljoen-voor-discriminatie-toeslagenouders)
- AI Act Annex III: [EU AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3)
- Draft high-risk guidelines: [Commission draft, 2026](https://www.dirittobancario.it/wp-content/uploads/2026/05/Draft-Guidelines-on-the-classification-of-high-risk-AI-Annex-III.pdf)
- Social-scoring guidance: [FPF summary](https://fpf.org/blog/red-lines-under-the-eu-ai-act-unpacking-social-scoring-as-a-prohibited-ai-practice)
- Omnibus dates: [Cuatrecasas](https://www.cuatrecasas.com/en/portugal/intellectual-property/art/digital-omnibus-ai-has-been-published)
- Debt-counselling data: [VNG handreiking schuldhulpverlening](https://vng.nl/sites/default/files/2025-10/handreiking-schuldhulpverlening.pdf)
