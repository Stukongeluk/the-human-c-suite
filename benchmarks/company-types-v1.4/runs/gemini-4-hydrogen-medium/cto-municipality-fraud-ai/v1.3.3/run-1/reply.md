**Advise against buying or deploying this system, and do not commit to a six-month go-live.** Even if the vendor’s "90% accuracy" claim were true, flagging the top 10% of welfare recipients when true fraud is rare (say 2%, as an illustrative baseline) means roughly **4 out of 5 people investigated would be false positives**—innocent residents in financial distress—while combining benefits, debt-counselling, and housing data exposes the municipality to severe GDPR, *SyRI*-style human-rights, and EU AI Act risks.

I’ve written a briefing note you can adapt for the alderman and *College van B&W* in [welfare-fraud-ai-advice.md](file:///G:/agy-bench/ws/b8262d347e62/welfare-fraud-ai-advice.md).

### What’s really going on
The alderman and council have a legitimate goal: spending scarce investigator hours on real fraud instead of random checks. The trap is letting a vendor demo and a six-month deadline dictate the solution before you’ve checked the legal basis, the base-rate math, or where investigator time is actually lost.

Four facts to put on the table:
1. **"90% accurate" means very little without precision and false-positive rates.** A model that predicts "no fraud" for everyone is already 98% accurate if 2% of recipients commit fraud. Ask for precision, recall, and false-positive rates across demographic groups on *your* municipality’s data—not a headline number.
2. **Cross-domain data is a legal minefield** *(not legal advice—have your FG and legal counsel confirm)*: Residents enter *schuldhulpverlening* in trust. Repurposing debt-counselling and housing data for fraud scoring risks breaching GDPR purpose limitation (*doelbinding*), deters people from seeking debt help, and echoes the opaque cross-domain profiling struck down in the 2020 *SyRI* ruling (Article 8 ECHR).
3. **Welfare-benefit AI is High-Risk under the EU AI Act.** Systems used by public authorities to evaluate or revoke essential public assistance fall under Annex III, bringing strict obligations on data governance, human oversight, Fundamental Rights Impact Assessments, and transparency (*Algoritmeregister*).
4. **Six months is not enough time.** Between public procurement (*Aanbestedingswet*), a full DPIA (and possible *Autoriteit Persoonsgegevens* consultation), data-quality work across three systems, and Works Council (*OR*) consultation on investigator workflows, a lawful rollout takes 12–18+ months—not six.

### What to do next
1. **Meet the alderman privately first**, before the next council or *college* meeting, so they aren’t cornered in public. Give them a protective way to reframe the ask:
   > *"We share the council's goal of focusing investigator hours on real fraud, and we can start improving triage within eight weeks. Buying an off-the-shelf AI that pulls in debt-counselling data in six months would expose the municipality to a SyRI-style legal defeat and damage trust in debt support. Let's run an 8-week operational and legal review first, and bring back lawful options."*
2. **Offer two reversible options instead of a binary yes/no:**
   - **Option 1 (Recommended): Process & transparent rules first.** Spend 8 weeks with your fraud investigators and caseworkers to find where hours are actually lost, and—if triage is needed—build clear, published, rule-based criteria using only lawful benefits data.
   - **Option 2: Narrow 8–12 week legal & data feasibility check.** Have your FG, legal counsel, and investigators establish what data may legally be combined and whether simple rules already outperform current selection, with zero vendor commitment.
3. **Bring the Works Council (*OR*) and Client Council (*Cliëntenraad*) in early** on the problem framing, before any tooling or workflow changes are selected.

**Key assumptions:** Your municipality hasn’t yet completed a DPIA or audited historical fraud labels for bias, and the vendor’s 90% figure comes from marketing or another jurisdiction rather than your own population.

**What am I missing, and what would make this wrong?**
