# Advisory Memo: Proposed AI Fraud-Risk Scoring System for Welfare Benefits

**To:** Alderman for Social Affairs & Municipal Executive (*College van B&W*)  
**From:** Chief Information Officer (CIO)  
**Date:** November 2026  
**Subject:** Technical, Legal, and Operational Assessment of Proposed Welfare Fraud-Scoring AI (6-Month Target)

---

## Executive Recommendation

**Do not buy or deploy the proposed mass risk-scoring AI system, and do not commit to a six-month go-live.**

Combining welfare, debt-counselling, and housing data to score every benefit recipient creates acute legal exposure under Dutch and EU law, risks repeating the SyRI and Rotterdam welfare-algorithm failures, and will likely send investigators after **3 to 5 innocent residents for every actual case of fraud**.

Instead, within the same six-month window, we can deliver a lawful, lower-cost, higher-impact alternative: **targeted, transparent checks strictly within statutory *Participatiewet* data, paired with investigator-led workflow improvements and early error prevention**—while keeping debt-counselling data strictly firewalled.

---

## 1. The Legitimate Goal

The council's underlying objective is sound: public funds must be protected, deliberate fraud undermines public support for the social safety net, and our investigators have limited capacity that should be focused where it makes the greatest difference. The question is not whether to tackle fraud, but which method achieves that goal legally, accurately, and without harming honest residents.

---

## 2. Why "90% Accurate" Does Not Mean What It Sounds Like

The vendor's headline claim of "90% accuracy" is not a usable measure for fraud detection, because deliberate welfare fraud is a low-prevalence event.

- **A trivial benchmark:** If 2% of recipients commit deliberate fraud, a system that simply predicts *"no one commits fraud"* is **98% accurate** while catching nothing.
- **The false-positive problem:** Even under a generous interpretation of the vendor's claim—assuming **90% sensitivity** (catches 90% of actual fraud) and **90% specificity** (correctly clears 90% of honest residents)—the math per 1,000 recipients looks like this (illustrative prevalence estimates; actual local rates must be verified from our own case records):

| Illustrative true fraud rate | Fraudsters caught (True Positives) | Honest residents flagged (False Positives) | Total flagged for investigation | Share of flagged residents who are innocent |
|---|---:|---:|---:|---:|
| **2%** (20 fraudsters, 980 honest) | 18 | 98 | **116** | **84.5%** |
| **5%** (50 fraudsters, 950 honest) | 45 | 95 | **140** | **67.9%** |

*Arithmetic check: at 2%, 18 + 98 = 116 (98 / 116 = 84.5%). At 5%, 45 + 95 = 140 (95 / 140 = 67.9%).*

**Operational and human impact:**
- Investigators would spend **two-thirds to four-fifths of their capacity** investigating innocent residents—reducing, rather than increasing, effective enforcement capacity.
- Historical training data only reflects *who was previously investigated*, not true fraud across the whole population. Models trained on past investigation records routinely amplify historical bias against specific neighbourhoods, household types, or language backgrounds.

---

## 3. Legal and Governance Exposure

*Note: This section flags legal and regulatory risks for executive awareness and is not formal legal advice. Our Data Protection Officer (Functionaris Gegevensbescherming, FG) and Legal Affairs (*Juridische Zaken*) must issue a formal opinion before any procurement step.*

1. **Purpose limitation (*doelbinding*) and debt-counselling data (GDPR / AVG Art. 5 & 6):**  
   Residents enter municipal debt-counselling (*schuldhulpverlening*) voluntarily in a moment of vulnerability. Repurposing debt-counselling records for fraud surveillance conflicts with purpose limitation and lacks a clear statutory basis under the *Wet gemeentelijke schuldhulpverlening* (Wgs). It also creates a severe practical backfire: residents avoid debt help out of fear of triggering a fraud investigation, escalating arrears into evictions and higher municipal costs.
2. **ECHR Article 8 and the SyRI precedent:**  
   In February 2020, the District Court of The Hague struck down the national SyRI risk-scoring system for violating Article 8 of the European Convention on Human Rights, citing opaque mass data-linking across welfare, housing, and debt domains that treated citizens as *a priori* suspects without proportionality or transparency. Cross-linking our benefits, debt-counselling, and housing systems for blanket risk-scoring follows the same legal pattern.
3. **Mandatory DPIA and *Autoriteit Persoonsgegevens* (AP) scrutiny:**  
   Automated fraud profiling by social services requires a full Data Protection Impact Assessment (GDPR Art. 35) and, where high residual risk remains, mandatory prior consultation with the AP (GDPR Art. 36).
4. **EU AI Act (status as of November 2026):**
   - **Prohibited practices (Art. 5, in force since February 2025):** Public-authority "social scoring" that evaluates citizens' trustworthiness from unrelated behavioural or socio-economic data is banned. Combining debt-counselling and housing data into a general risk score risks crossing this boundary.
   - **High-Risk AI (Annex III, point 5(a)):** AI used by public authorities to assess eligibility for, or reclaim, public assistance benefits is classified as High-Risk. Under the 2026 Digital Omnibus on AI (Regulation (EU) 2026/1744), full compliance for Annex III systems becomes enforceable on **2 December 2027**—barely six months after the proposed go-live. Compliance requires a **Fundamental Rights Impact Assessment (FRIA, Art. 27)**, documented data governance and bias testing, audit logging, transparency, and meaningful human oversight.
   - **Public transparency:** The system will require publication in the Dutch **Algoritmeregister**, placing its data sources and error rates under full council and public scrutiny.
5. **Works Council (*Ondernemingsraad*, OR):**  
   Under the Dutch Works Councils Act (*WOR*), major organisational/IT changes require OR advice (Art. 25), and any system capable of tracking investigators' case handling or performance requires OR consent (Art. 27(1)(l)).

---

## 4. Why Six Months Is Not Achievable

Even if the legal barriers were resolvable, a responsible rollout cannot fit into six months:
- Legal basis review, DPIA, and potential AP prior consultation: **3–6 months**
- Public procurement (*aanbesteding*), independent bias audit, and FRIA: **4–6 months**
- OR consultation, investigator training, and secure integration across legacy systems: **3–4 months**

Total realistic timeline for a compliant high-risk AI deployment: **12–18 months minimum**, with a high probability that the DPIA or legal review halts the project before launch.

---

## 5. Options Compared

| Dimension | Option A: Targeted Statutory Checks & Workflow Redesign *(Recommended)* | Option B: Narrow Scoping & Independent Vendor Audit | Option C: Buy & Deploy Vendor AI in 6 Months *(Not Recommended)* |
|---|---|---|---|
| **Timeline** | **4–6 months** to first measurable results | **12–18 months** (with strict go/no-go gate) | 6 months (unrealistic; high likelihood of halt) |
| **Data used** | Statutory *Participatiewet* & authorised cross-checks only; **no debt-counselling data** | Statutory data only; debt-counselling excluded | Benefits + debt-counselling + housing |
| **Legal risk** | Low (clear statutory basis, transparent rules) | Medium (requires DPIA, FRIA, AP check) | **Critical** (GDPR, ECHR Art. 8 / SyRI, AI Act) |
| **False-positive impact** | Low; every flag has a concrete, explainable legal trigger | Tested in shadow mode before live use | **High** (est. 68–85% of flagged cases innocent) |
| **Reversibility** | High (incremental, modular changes) | High until procurement decision | Low (vendor lock-in, reputational damage) |

---

## 6. Recommended Next Steps (Next 30 Days)

1. **Week 1 — Joint review:** Convene CIO, FG (DPO), Legal Affairs, and the leads of *Handhaving* (Investigations) and *Schuldhulpverlening* to confirm the legal boundary on debt-counselling data and establish our actual baseline fraud vs. administrative-error rates.
2. **Week 2 — Investigator bottleneck diagnosis:** Spend two days with investigators to map where their time actually goes and which concrete, legally verifiable signals produce the highest share of real fraud cases.
3. **Week 3 — Vendor evidence check (if council still requires evaluation):** Send the vendor a mandatory five-question technical request: (a) precision, recall, and false-positive rate at 2% and 5% prevalence; (b) full list of input variables; (c) subgroup disparity test results; (d) independent audit report; (e) AI Act Annex III compliance dossier. Do not proceed without written answers.
4. **Week 4 — Council briefing:** Present Option A to the council as a faster, lawful, transparent way to improve enforcement within six months—protecting both public funds and residents' rights.

---

## Key Assumptions & Open Questions

- **Assumptions:** True deliberate fraud prevalence is in the low single digits (2–5%); no special local statutory override exists for repurposing debt-counselling data; investigators currently face a triage/data-quality bottleneck rather than a lack of leads.
- **What would change this recommendation:** Verified local case data showing a much higher prevalence of deliberate fraud that deterministic checks miss, combined with a formal written legal opinion from the FG and Legal Affairs confirming a valid statutory basis and AP clearance—and even then, debt-counselling data should remain excluded and the timeline extended to 12–18 months.
