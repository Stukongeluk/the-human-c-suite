# Advisory Memo: Proposed AI Fraud-Risk Scoring System for Welfare Benefits

**To:** Alderman for Social Affairs & Municipal Executive (*College van B&W*)  
**From:** Chief Information Officer (CIO)  
**Date:** 20 November 2026  
**Subject:** Assessment of proposed AI fraud-risk scoring system and six-month timeline

---

## 1. Recommendation

Do **not** procure or deploy the proposed AI fraud-risk scoring system as currently scoped, and do **not** commit to a six-month go-live.

Instead, take a two-track approach:
1. **Immediate (0–3 months):** Work with benefits caseworkers and investigators to identify where errors and unreported changes actually originate, and test simpler process fixes before buying predictive software.
2. **Scoped evaluation (3–6 months, if data-driven triage is still needed):** Run a legal and technical feasibility check with our Data Protection Officer (*Functionaris Gegevensbescherming*, FG) and caseworkers on a narrow, transparent, rule-based administrative-check pilot—**excluding** debt-counselling (*schuldhulpverlening*) data—with no automated scoring of residents.

---

## 2. Why the Vendor's "90% Accuracy" Claim Does Not Hold Up

A vendor quoting "90% accuracy" without showing precision, recall, and false-positive rates on municipal data is not giving us a number we can act on. In welfare administration, actual fraud is a small minority of cases. When the base rate is low, high overall accuracy hides a very high false-positive rate.

**Worked example (1,000 benefit recipients, assuming a 3% fraud rate):**

| Metric | Count | Share |
|---|---:|---|
| Actual fraud cases (3% base rate) | 30 | 3.0% |
| Non-fraud cases | 970 | 97.0% |
| True positives (90% sensitivity) | 27 | 2.7% |
| False negatives (missed fraud) | 3 | 0.3% |
| True negatives (90% specificity) | 873 | 87.3% |
| False positives (innocent residents flagged) | 97 | 9.7% |
| **Total flagged** | **124** | **12.4%** |

- **Overall accuracy:** (27 + 873) / 1,000 = **90.0%**.
- **Share of flagged residents who are innocent:** 97 / 124 = **78.2%**.

Even if investigators only review the top 10% (100 cases), a "90% accurate" model can still send investigators after mostly innocent residents—consuming investigation capacity while damaging trust with people who are following the rules.

---

## 3. Legal, Privacy, and Public-Trust Risks

*(Note: This section flags governance and statutory risks for review by our FG and legal counsel; it is not formal legal advice.)*

1. **Purpose limitation and debt-counselling data (GDPR / AVG):** Residents share sensitive financial information with *schuldhulpverlening* in confidence to get out of debt. Re-purposing debt-counselling data to calculate a fraud-risk score undermines purpose limitation under the GDPR and creates a perverse incentive: residents in trouble will avoid debt counselling if seeking help triggers a fraud investigation.
2. **Mandatory Data Protection Impact Assessment (DPIA) and bias testing:** Systematic risk profiling of citizens requires a DPIA before procurement or deployment. Any model trained on historical investigation data risks reproducing past biases or using proxies such as postcode or nationality.
3. **EU AI Act (High-Risk classification):** Under the EU AI Act, AI systems used by public authorities to evaluate eligibility for, or access to, essential public assistance benefits are classified as **high-risk** (Annex III). Full high-risk obligations—including a Fundamental Rights Impact Assessment, strict data governance, logging, and human oversight—apply from **December 2027**. Building a system now that cannot meet those standards creates stranded cost and compliance exposure.
4. **Public-trust precedent:** Following the Dutch childcare benefits scandal (*Toeslagenaffaire*), where risk profiling contributed to wrongly accusing more than 20,000 families of fraud, any opaque municipal risk-scoring system carries severe political, legal, and reputational risk.
5. **Co-determination (*Wet op de ondernemingsraden*, WOR):** Introducing a system that shapes or monitors how investigators and caseworkers allocate and perform their work triggers advisory and/or consent rights with the Works Council (*Ondernemingsraad*, OR) under Articles 25 and 27 WOR. The Client Council (*Cliëntenraad*) should also be consulted early.

---

## 4. Why Six Months Is Not Realistic

A six-month go-live is incompatible with safe delivery for a mid-sized municipality:
- **Procurement:** Public procurement (*aanbesteding*) rules and vendor due diligence alone typically consume several months depending on contract value.
- **Data integration & quality:** Connecting three separate source systems (benefits, debt-counselling, housing) with differing data definitions, consent bases, and retention rules cannot be done safely in a rush.
- **Governance:** Completing a DPIA, FG review, OR consultation, and bias audit before go-live requires sequencing that does not fit inside six months.

---

## 5. Options Compared

| Option | What it does | Operational & human impact | Legal & trust risk | Timeline |
|---|---|---|---|---|
| **Option A: Fix process & clarity first (Recommended)** | Audit why errors/overpayments happen with caseworkers and investigators; simplify reporting forms and proactive outreach; improve case-management tooling. | Reduces avoidable citizen errors and investigator noise; keeps investigators in control. | Low. No cross-domain profiling; strengthens public trust. | 2–4 months for first improvements. |
| **Option B: Narrow, transparent data-quality checks (Conditional)** | After DPIA and OR/FG sign-off, test simple, explainable rule-based checks *within* benefits data only (no debt-counselling or housing data), with mandatory human review and no risk scores. | Gives investigators clear, explainable signals they can verify and challenge. | Moderate; manageable with DPIA, transparency, and human review. | 6–9 months to safe pilot. |
| **Option C: Buy & deploy vendor AI risk scorer in 6 months (Not recommended)** | Integrates benefits, debt-counselling, and housing data to rank all recipients and target the top 10%. | High false-positive load on investigators; vulnerable residents wrongly investigated; chills uptake of debt counselling. | Severe (GDPR purpose limitation, bias/proxy risk, EU AI Act high-risk readiness, political/reputational exposure). | Unrealistic in 6 months. |

---

## 6. Next Steps

1. **This week:** Align privately with the Alderman on the false-positive math, the debt-counselling data boundary, and a realistic timeline before the next council briefing.
2. **Weeks 2–4:** Convene benefits investigators, caseworkers, the FG, and legal counsel to review where current investigation capacity is actually spent.
3. **Month 2:** Present Options A and B to the Works Council (*OR*) and Client Council (*Cliëntenraad*) with clear criteria, before any vendor commitment is made.
