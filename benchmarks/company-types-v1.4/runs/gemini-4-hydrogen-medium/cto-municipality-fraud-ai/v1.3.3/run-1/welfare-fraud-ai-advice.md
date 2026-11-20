# Briefing Note: Proposed AI Fraud-Risk Scoring for Welfare Benefits

**To:** Alderman for Social Affairs & Digitalisation / College van B&W  
**From:** Chief Information Officer (CIO)  
**Date:** 20 November 2026  
**Subject:** Advice on proposed AI welfare fraud-risk scoring system (6-month target)

---

## 1. Executive Summary & Recommendation

**Recommendation:** Do not procure or deploy the proposed AI risk-scoring system within six months, and do not connect debt-counselling (*schuldhulpverlening*) data to fraud detection. Instead, commission an 8-week operational and legal review with our Fraud/Compliance investigators, Data Protection Officer (*Functionaris Gegevensbescherming*, FG), and legal counsel to address investigation bottlenecks through transparent, legally grounded triage.

The alderman’s and council’s goal—focusing scarce investigator capacity on genuine high-risk cases rather than random checks—is sound. However, the proposed vendor solution carries severe legal, mathematical, and reputational risks that would expose the municipality to court challenges, regulatory intervention, and public harm.

---

## 2. Four Reasons the Current Proposal Will Fail

### A. "90% accuracy" is a statistical trap (the base-rate problem)
Vendor headline accuracy figures are misleading when the event being predicted is rare:
* **Illustrative example:** Suppose 2% of 5,000 welfare recipients commit intentional fraud (100 cases). A trivial system that predicts "no fraud" for everyone is already **98% accurate** while catching zero fraud.
* Even if a model has 90% sensitivity and 90% specificity, flagging the **top 10%** (500 people) will still produce roughly **410 false positives**—meaning more than 4 out of 5 citizens investigated would be innocent residents who are disproportionately in financial distress.
* Before any vendor is evaluated, we would need precision, recall, false-positive rates across demographic subgroups, and validation on our own municipality’s legal definition of fraud—none of which exist today.

### B. Combining benefits, debt-counselling, and housing data violates core legal principles
*(Note: This is a governance and risk assessment, not formal legal advice; formal review by our FG and legal counsel is required.)*
* **Purpose limitation (GDPR / AVG):** Residents share sensitive financial and personal data with *schuldhulpverlening* in trust to resolve debt. Repurposing debt-counselling data for fraud scoring risks breaching GDPR purpose limitation and creates a chilling effect where vulnerable residents avoid seeking debt help.
* **SyRI precedent (Article 8 ECHR):** In 2020, the Hague District Court struck down the Dutch *Systeem Risico Indicatie* (SyRI) because opaque cross-domain risk profiling of welfare recipients failed the test of necessity, proportionality, and transparency.
* **EU AI Act (High-Risk classification):** AI systems used by public authorities to evaluate eligibility for, or reduce/revoke, essential public assistance benefits are classified as **High-Risk AI** under Annex III. This requires a Fundamental Rights Impact Assessment (FRIA), strict data governance, human oversight, and public transparency (such as registration in the Dutch *Algoritmeregister*).

### C. A six-month go-live is incompatible with lawful municipal delivery
Even if the legal basis existed, a compliant path—public procurement (*Aanbestedingswet*), a full Data Protection Impact Assessment (DPIA) and potential prior consultation with the *Autoriteit Persoonsgegevens* (AP), data-quality remediation across three legacy systems, bias testing, and works council (*Ondernemingsraad*, OR) consultation—takes **12 to 18+ months**, not six. Rushing this in six months turns a reversible policy idea into an irreversible legal and reputational liability.

### D. Operational blind spots
Targeting the "top 10%" without involving our investigators and caseworkers risks reinforcing historical bias in past investigation data (investigating the same neighbourhoods or household types repeatedly) while missing actual complex fraud.

---

## 3. Options for the College and Council

| Option | Timeline | Legal & Reputational Risk | What it delivers |
|---|---|---|---|
| **1. Process & Transparent Rules First (Recommended)** | 8–12 weeks for review; iterative improvements | **Low** | Go-and-see review with investigators to remove bottlenecks; clear, published, rule-based triage criteria using only lawful benefits data; zero black-box scoring. |
| **2. Narrow Legal & Data Feasibility Check** | 8–12 weeks | **Low–Medium** (paper exercise only) | FG, legal counsel, and investigators assess what data combinations are legally permissible and test whether simple rules outperform current selection. No vendor contract. |
| **3. Procure Vendor AI System as Proposed** | 12–18+ months realistically (cannot meet 6 months) | **Very High** | High likelihood of failing DPIA/AP review, SyRI-style litigation, and loss of citizen trust in debt counselling. |

---

## 4. Recommended Next Steps (Next 4 Weeks)

1. **Private alignment with the Alderman:** Agree on a realistic narrative for the council: we share the goal of smarter fraud prevention, but we will not expose the municipality to a SyRI-style legal defeat or compromise debt counselling.
2. **Commission an 8-week baseline review (Option 1):**
   * Sit with fraud investigators and benefits caseworkers to map where hours are actually lost today.
   * Task the FG and legal counsel with a formal memo on cross-domain data limits (specifically *schuldhulpverlening* and housing).
   * Establish upfront evaluation criteria—including false-positive limits and explainability—before speaking to any AI vendor.
3. **Involve the Works Council (OR) and Client Council (*Cliëntenraad*) early:** Bring them into the problem framing before any tooling or workflow changes are chosen.

---

## 5. Key Assumptions & Questions to Test

* **Assumptions:** We have not yet run a DPIA or audited the quality/bias of historical fraud labels; the vendor’s "90% accuracy" figure comes from marketing or another jurisdiction rather than our own population.
* **What would change this advice:** Only if our FG and external legal counsel confirmed a clear statutory basis for cross-domain scoring, the vendor proved low false-positive rates on our own historical data with zero demographic skew, and the council accepted a 12–18+ month timeline for full AI Act and DPIA compliance.
