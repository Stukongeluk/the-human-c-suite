Advise **no** to buying this system as scoped, and **no** to the six-month deadline: at a typical 3% fraud base rate, a "90% accurate" model still produces roughly **78% false positives** among everyone it flags, meaning your investigators would spend most of their time chasing innocent residents.

I have also drafted a ready-to-use advisory memo for your Alderman and *College van B&W* in [welfare-fraud-ai-advice-memo.md](file:///G:/agy-bench/ws/2dde7c1c4c27/welfare-fraud-ai-advice-memo.md).

### The trap
The council is buying a tool before diagnosing the bottleneck, and treating a high-risk, irreversible public-law decision like a standard six-month SaaS rollout.

### Why this fails in a Dutch municipality
- **"90% accuracy" hides false positives:** Without precision, recall, and subgroup bias metrics on your own data, overall accuracy is meaningless on rare events.
- **Debt-counselling data breaks trust and law:** Pulling *schuldhulpverlening* and housing data into fraud scoring raises serious GDPR (*AVG*) purpose-limitation issues (not legal advice—confirm with your *Functionaris Gegevensbescherming*, FG) and punishes residents for seeking debt help.
- **EU AI Act & *Toeslagenaffaire* exposure:** AI used to evaluate access to public benefits is **high-risk** under the EU AI Act (full obligations apply from December 2027), requiring bias testing, human oversight, and a DPIA. After the *Toeslagenaffaire*, an opaque risk-scoring model is a political and legal minefield.
- **Co-determination:** Your Works Council (*Ondernemingsraad*, OR) has advisory/consent rights under Articles 25 and 27 WOR on systems that shape or monitor staff work, and the *Cliëntenraad* should be involved early.

### What to do next
1. **Speak privately with the Alderman first**—before the next council meeting—so they aren't cornered in public.
2. **Offer two safer alternatives alongside "do not buy":**
   - *Option A (Recommended, 2–4 months):* Sit with benefits caseworkers and investigators to fix the rules, forms, and life-change reporting gaps that cause most avoidable errors.
   - *Option B (6–9 months, conditional):* If triage is still needed after a DPIA and FG/OR sign-off, test simple, explainable rule-based checks **on benefits data only** (no debt-counselling data) with mandatory human review.
3. **Require raw metrics from the vendor**—precision at 10%, false-positive rate, and proxy-bias tests—before any further talks.

**A line you can use with the Alderman:**
> "I want our investigators focused on real fraud too, but '90% accuracy' on welfare data still flags mostly innocent residents—and using debt-counselling data puts us straight into *Toeslagenaffaire* territory. Give me two weeks with the FG and our investigators to show you a safer option that actually helps them."

**Key assumptions:** Actual fraud prevalence in your caseload is low (single-digit %), and your municipality has an FG, OR, and *Cliëntenraad* to involve. What am I missing about the council's real pressure here, and what would make this wrong?
