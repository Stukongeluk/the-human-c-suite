**Advise the council not to buy a scoring system for go-live in six months. Advise a six-month "prove it first" programme instead: a legal and impact assessment, a measured baseline, and a shadow-mode test with no consequences for residents. Decide on purchase only after that. "90% accurate" tells you almost nothing, and the data mix you describe is where Dutch government has been hurt before.**

**Why "90% accurate" can't carry this decision**

Fraud is rare. Suppose you have 5,000 benefit recipients and 3% commit fraud (150 people; my assumption, so replace it with your own number). A model that flags nobody is 97% accurate and catches nothing. Now suppose the model finds 60% of real fraud in the top 10%. That is 500 people flagged, 90 genuine cases and 410 residents investigated for nothing, so 18% precision. In this example, four of five investigations land on someone who did nothing wrong. Ask the vendor for precision and recall in the top 10%, per group (age, origin, household type, neighbourhood), measured on a municipality like yours and not on its own test data. Also ask how "fraud" was labelled in training. If the labels are past investigation outcomes, the model learns where you looked before, not where fraud is. Much registered "fraud" is also unintentional error, which is a different problem needing a different response.

**What the Dutch record says**

- The toeslagenaffaire showed what happens when risk signals turn into suspicion of whole groups, with no human who can say "this is wrong".
- The Hague district court stopped SyRI in 2020 for lack of transparency and proportionality in combining government data for risk profiling.
- Rotterdam's welfare risk model was dropped after outside analysis found bias. Amsterdam's pilot got similar scrutiny. Check current details before you cite them.

I'd tell the council that the reputational risk is theirs and yours, not the vendor's.

**Three things that block "live in six months"**

1. **Law.** I'm not a lawyer, so get your municipal legal team and the Autoriteit Persoonsgegevens guidance involved early. Questions to settle: is there a legal basis in the Participatiewet and GDPR to combine benefits, debt-counselling (schuldhulpverlening) and housing data for profiling everyone? Purpose limitation and data minimisation are the hard parts. Debt-counselling data is sensitive; if residents learn it feeds fraud scores, some will stop asking for help, which raises debt and costs elsewhere. Scoring everyone looks close to the AI Act's ban on social scoring by public authorities where it leads to unjustified or disproportionate treatment, and AI that assesses benefit eligibility is high-risk, with duties such as risk management, human oversight, logging, and a fundamental rights impact assessment for public bodies. As I understand the 2026 Digital Omnibus, many high-risk duties moved to December 2027, but that date and the scope should be confirmed. Don't use the delay as a reason to skip the work: Dutch law (GDPR Art. 22 and the DPIA duty, the algorithm register) applies already.
2. **Process.** Participatiewet client participation means the cliëntenraad should be consulted at the problem stage, with real numbers. So should the data protection officer and, where investigators' work changes, the works council (ondernemingsraad).
3. **Time.** A DPIA, legal basis, procurement, integration of three source systems with different data quality, and a measured pilot don't fit in six months at a sustainable pace. A rushed launch means overtime and shortcuts.

**Options**

| | What | Upside | Risk |
|---|---|---|---|
| A | Buy and go live in 6 months | Meets the political date | Highest legal, reputational and harm risk. Hard to reverse once investigators trust the list |
| B (recommended) | Six months of foundations plus shadow pilot, then a go/no-go | A date the alderman can announce, and an honest decision | Slower. The council may be disappointed |
| C | No scoring: improve what investigators already do (concrete-signal rules, quality of existing checks, tips, random audits) | Cheapest, lawful on today's basis, fast | Less "AI" story, and smaller gains |

Before anything else, run random sample checks. They give you the real fraud rate and error rate, which no vendor can supply, and every option needs that number.

**What B delivers in six months**
- Month 1-2: legal basis memo, DPIA and fundamental rights assessment started, cliëntenraad and DPO briefed, vendor questions sent (error rates per group, labels, explainability, audit rights, the right to switch it off, and who owns the data and the model).
- Month 2-4: baseline from random sampling; compare it with how investigators select cases now.
- Month 4-6: shadow mode on one data source at first (benefits only), scores shown to nobody who can act on them. Compare precision against the baseline, by group.
- Go/no-go criteria agreed now, before results exist: minimum precision, maximum disparity between groups, and a requirement that no resident is treated worse on the score alone. An investigator must have a concrete reason, and the resident must be able to see why and object.
- Publish it in the algorithm register. Name a person who owns the outcome, not "the system".

If the answer is eventually yes, go live in waves, with a kill switch and a monthly review of outcomes by group.

**A fair evaluation**: if you score vendors, fix criteria and weights before anyone scores, and keep anyone with a vendor relationship out of the panel. The alderman's deadline is a political fact, so make it work for you: "Live in six months" can become "responsible decision in six months".

**What would change my mind:** a legal basis confirmed for this exact data combination, shadow results showing high precision with no group disparity, and a clear way for residents to contest a flag.

Two questions would sharpen this. What is your measured fraud rate today (if any), and which of the three data sources has a legal basis for this purpose right now? What am I missing, and what would make this wrong?
