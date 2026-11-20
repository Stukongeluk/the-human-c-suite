# Advice Note: Proposed AI Fraud-Risk Scoring System for Welfare Benefits

**To:** Alderman for Social Affairs & Municipal Executive (College van B&W)  
**From:** Chief Information Officer (CIO)  
**Date:** November 2026  
**Subject:** Technical, legal and operational assessment of the proposed welfare fraud-risk AI system, and safer alternatives  

---

## Recommendation

**Do not purchase or deploy a predictive AI risk-scoring system for welfare benefits, and do not link debt-counselling or housing data to fraud detection.**

Instead, over the next six months, we should:
1. **Reduce improper payments at the source** by fixing the most common administrative errors and unclear reporting rules in the benefits process.
2. **Focus investigator capacity using transparent, rule-based checks** on legally permitted benefits data only, designed together with our investigators and caseworkers.
3. **Require formal legal, privacy and bias gates** before any future analytics pilot is considered.

This protects public money and investigator time without exposing residents to wrongful accusations or exposing the municipality to court injunctions, regulatory fines and lasting damage to public trust.

---

## 1. Why the vendor's "90% accuracy" claim does not work in practice

The council's goal is sound: public funds should go to people who are entitled to them, and our investigators have limited capacity. However, "90% accuracy" is a misleading metric when true fraud is rare.

To illustrate the arithmetic on a representative caseload of **2,000 welfare recipients** (illustrative numbers; we should verify our actual caseload and confirmed fraud rate before any decision):

| Metric | Scenario A: 2% true fraud (40 cases) | Scenario B: 5% true fraud (100 cases) |
|---|---|---|
| Honest recipients in caseload | 1,960 | 1,900 |
| Fraud cases correctly flagged (90% sensitivity) | 36 | 90 |
| Fraud cases missed (10%) | 4 | 10 |
| Honest recipients falsely flagged (10% error rate) | 196 | 190 |
| Honest recipients correctly cleared (90% specificity) | 1,764 | 1,710 |
| **Total residents flagged for investigation** | **232** | **280** |
| **Share of investigated residents who are innocent** | **84.5%** | **67.9%** |

Two consequences follow directly from this math:
- **Even a "90% accurate" model sends investigators mostly after honest residents** — roughly 4 in 5 at a 2% fraud rate, or 2 in 3 at a 5% fraud rate.
- **Investigating a fixed "top 10%" (200 residents) guarantees high false positives.** If actual fraud is 2% (40 cases), even a mathematically perfect model means at least **160 of the 200 residents investigated (80%) are innocent**.

A system that floods investigators with false positives does not save capacity; it consumes it, while subjecting innocent, vulnerable residents to intrusive investigations.

---

## 2. Legal, privacy and public-trust risks

*Note: This is a CIO risk assessment, not formal legal advice. Our Data Protection Officer (Functionaris Gegevensbescherming) and municipal legal counsel must review any proposal before procurement.*

1. **Linking debt-counselling and housing data breaches purpose limitation and undermines care.**  
   Under the GDPR (AVG), personal data collected for one purpose cannot simply be repurposed for fraud investigation without a specific, proportionate legal basis. Residents enter debt counselling (*schuldhulpverlening*) voluntarily for help. If seeking debt help raises a resident's fraud-risk score, people will delay or avoid counselling — worsening municipal debt and homelessness costs.
2. **Dutch judicial and political precedent is clear.**  
   In February 2020, The Hague District Court struck down the Dutch government's SyRI risk-profiling system for violating Article 8 of the European Convention on Human Rights (right to privacy), citing lack of transparency and proportionality when linking government datasets to score citizens for welfare fraud. In the Dutch childcare benefits scandal (*toeslagenaffaire*), risk profiling contributed to wrongly accusing more than 20,000 families of fraud and led to the cabinet's resignation in January 2021.
3. **Proxy discrimination is hard to eliminate and easy to trigger.**  
   Even when protected characteristics are removed, models trained on benefits, debt and housing data routinely pick up proxies such as postcode, household composition, language or housing type — creating indirect discrimination risks and reputational exposure.
4. **EU AI Act and governance obligations.**  
   Under the EU AI Act (Annex III), AI systems used by public authorities to assess eligibility for, or revoke or reclaim, public assistance benefits are classified as **high-risk**. While the Act's main high-risk obligations apply from **2 December 2027** (following the 2026 Digital Omnibus), building a system today that cannot pass a Fundamental Rights Impact Assessment, bias audit, transparency requirement and human-oversight standard creates immediate stranded-asset risk. Today, GDPR (including DPIA and Article 22 safeguards on automated decision-making) and Dutch *Algoritmeregister* transparency standards already apply.
5. **Co-determination (Ondernemingsraad).**  
   Because a risk-scoring system changes how investigators work and can be used to track their case outcomes, the Works Council (*OR*) should be consulted early under the Works Councils Act (*WOR*), alongside frontline investigators.

---

## 3. Why a six-month go-live is not viable

Delivering a lawful, audited system in six months is not realistic. A defensible process requires:
- Legal basis verification and a full DPIA (plus potential prior consultation with the *Autoriteit Persoonsgegevens* if residual risk remains high);
- Public procurement compliance;
- Independent bias and accuracy testing on local data;
- Works Council consultation and investigator workflow design;
- Publication in the municipal *Algoritmeregister* and clear appeal paths for residents.

Compressing this into six months means skipping the exact safeguards that prevent a public-sector scandal.

---

## 4. Recommended options for the next six months

| Option | What it does | Timeline | Risk profile | Expected impact |
|---|---|---|---|---|
| **Option 1 (Recommended): Process fixes + transparent rule-based checks** | Analyse last 12 months of improper payments to separate honest mistakes from deliberate fraud; simplify unclear reporting rules; give investigators transparent, legally grounded rule-based signals on benefits data only, with human review. | 3–6 months | Low legal and reputational risk; fully explainable to residents and the council. | Reduces improper payments at the source and focuses investigator time on verifiable anomalies. |
| **Option 2: Gated feasibility study (no procurement yet)** | Commission a 12-week joint review by Legal, DPO, IT, investigators and the OR to test whether any lawful, non-discriminatory statistical signal exists within benefits data alone (excluding debt-counselling and housing data). | 3 months for study; 12–18+ months if ever built | Controlled; no vendor lock-in or unlawful deployment. | Gives the council an evidence-based answer before committing budget. |
| **Option 3 (Not recommended): Buy vendor AI model in 6 months** | Procure and deploy the vendor's risk-scoring model across benefits, debt-counselling and housing data. | 6 months (high risk of delay or injunction) | Very high legal, financial and political risk. | High false-positive rate (68–85%+); erodes trust in debt counselling and municipal services. |

---

## 5. Proposed next steps (first 30 days)

1. **Pull our own baseline data (Week 1–2):** Measure our actual welfare caseload, the share of improper payments caused by administrative error vs. intentional fraud, and where investigators currently spend their time.
2. **Convene a joint review (Week 2–3):** Bring together the DPO, legal counsel, social-affairs management, frontline investigators and the Works Council to review the baseline data and design Option 1.
3. **Brief the council transparently (Week 4):** Present the baseline numbers, the false-positive math, and a concrete six-month plan under Option 1 that delivers measurable reductions in improper payments without legal or reputational exposure.

---

## Sources

- District Court of The Hague, *NJCM et al. v. State of the Netherlands (SyRI)*, ECLI:NL:RBDHA:2020:1878 (5 February 2020).
- Dutch childcare benefits scandal (*Toeslagenaffaire*): Parliamentary Interrogation Committee report *Ongekend Onrecht* (December 2020); resignation of Rutte III cabinet (15 January 2021).
- EU Artificial Intelligence Act (Regulation (EU) 2024/1689), Annex III (high-risk AI systems in public assistance benefits) and Article 26; 2026 Digital Omnibus timeline (high-risk obligations applying from 2 December 2027).
- General Data Protection Regulation (GDPR / AVG), Articles 5 (purpose limitation), 22 (automated decision-making) and 35 (DPIA).
- Dutch Works Councils Act (*Wet op de ondernemingsraden*, WOR), Articles 25 and 27.
