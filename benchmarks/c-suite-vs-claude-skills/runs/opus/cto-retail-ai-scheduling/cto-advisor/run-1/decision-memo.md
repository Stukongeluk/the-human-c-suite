# ADR-001: AI workforce-management tool for 140 stores

**Date:** 2026-11-23
**Status:** Proposed
**Deciders:** CEO (final), COO (business owner), CTO, CFO, HR director; the works council (OR) has consent rights
**Confidence tags:** [Verified] = checked against a primary or authoritative source · [Medium] = sourced but applying it to you needs judgement · [Assumed] = my assumption; replace it with your data

---

## 1. Decision in one paragraph

Buy a workforce-management (WFM) tool, but do not run the vendor's plan as pitched. Go live in March 2027 in 8–10 pilot stores with matched control stores. Set the tool up within the CAO (collective labour agreement) and Dutch law: rosters published at least a week ahead, same-day changes only by voluntary offer, cancelled hours paid, youth working-time limits enforced, and no scoring of individual staff. Make a go/no-go decision in June 2027 on a scorecard that weighs sales, service and people outcomes alongside labour hours. If it passes, roll out in waves from September 2027 to Q1 2028. Set the savings target from the pilot evidence, not from the vendor's 12%.

## 2. Context and problem statement

- 140 stores, about 9,000 staff, many of them students on flexible contracts.
- The COO proposes an AI WFM tool. The vendor promises 12% fewer labour hours by forecasting demand in 15-minute slots, publishing schedules 3 days ahead and adjusting shifts on the day. The vendor wants all stores live by March 2027.
- Today is 23 Nov 2026. Between now and March sit the December peak and, in most retailers, a store-change freeze.
- The sector CAO expired on 1 April 2026. Negotiations were suspended on 17 Nov 2026, with wage start dates still open. The old terms keep applying until a new CAO is agreed. [Verified: [FNV, 18 Nov 2026](https://www.fnv.nl/nieuwsbericht/sectornieuws/handel/2026/11/voortgang-onderhandelingen-cao-supermarkten), [FNV, 2 Nov 2026](https://www.fnv.nl/nieuwsbericht/sectornieuws/handel/2026/11/cao-bod-werkgevers-supermarkten-blijft-onvoldoende), [CNV](https://www.cnv.nl/handel/detailhandel-food/cao-supermarkten-vgl/28-06-2024_08-12-2025_cao-supermarkten-vgl-oud/)]

## 3. Decision drivers

1. **Legal compliance:** the CAO, the WAB (Dutch flex-work law, including on-call rules), the Working Hours Act (Arbeidstijdenwet, including youth rules), the Works Councils Act (WOR), the GDPR (EU data protection law) and the EU AI Act.
2. **Real net margin**, meaning labour savings minus lost sales, extra turnover and implementation cost. Labour hours alone are not the measure.
3. **Staff stability.** Students are the flexible capacity of the business, and predictable rosters keep them.
4. **Delivery risk:** integrations, payroll accuracy, and 140 managers adopting the tool.
5. **Reversibility and vendor lock-in.**

## 4. What the vendor proposes vs what the rules allow

| Vendor feature | Rule | Implication | Required configuration |
|---|---|---|---|
| Publish schedules 3 days ahead | Both supermarket CAOs: the full roster must be known "minimaal één volle week voor aanvang". If it isn't, staff can only be required to work their structural hours. Days off and the fixed free day must be known 2 weeks ahead. The Working Hours Act default is 28 days unless the CAO sets otherwise. [Verified: [CAO Levensmiddelenbedrijf 2025/26 art. 4.3f](https://zoek.officielebekendmakingen.nl/stcrt-2025-14579.pdf), [VGL CAO 2020–23 art. 4.3f](https://www.fnv.nl/getmedia/18c9c6e7-339c-46d3-963e-af97eb245d25/608-Supermarkten-VGL-cao-Grootwinkelbedrijven-Levensmiddelen-2020-2023-v291221.pdf), [Ondernemersplein](https://ondernemersplein.overheid.nl/wetten-en-regels/werktijden-en-rusttijden/)] | Not compliant as pitched | Publish **at least 7 full days** ahead as a hard floor; aim for 14 |
| Adjust shifts on the day | The 24-hour call-in and cancellation window covers only *erbijbaners* (staff on at most 12 h/week) and, in the VGL CAO, *hulpkrachten*, and only for unforeseen factors. Other on-call staff need **4 days' notice**. If the employer cancels or changes hours inside that window, the employee is paid for the original call. [Verified: CAOs above, [WAB on-call rules](https://ondernemersplein.overheid.nl/wetten-en-regels/regels-voor-oproepkrachten/), [AWVN](https://www.awvn.nl/hr-van-a-tot-z/onvoorspelbaar-werkpatroon/)] | Same-day cuts mostly save **nothing**, because the hours are still paid | Same-day changes become **voluntary** offers (open shifts, swaps, "go home early" offers). No forced cancellations inside the notice window |
| Match staff to demand in 15-minute slots | At least **50% of contracted hours** must be fixed structural time. At least 50% of opening hours minus contract hours is fixed free time, including two evenings a week, and work in that time is voluntary only. Shop staff can't be required to work more than two evenings a week. [Verified: VGL CAO art. 4.3c, 4.3e, 4.5] | Limits how far hours can be shaped to demand | Rule constraints in the engine; a **minimum shift length** to agree with the OR (e.g. 3 h) [Assumed: the number is a proposal] |
| On-the-day extensions and late shifts | Ages 16–17: max 9 h per shift and 45 h per week, school time counts as working time, no night work, no on-call duty or overtime. Age 15 in school weeks: 2 h per school day, 12 h per week, normally between 07:00 and 19:00. [Verified: [Rijksoverheid 16–17](https://www.rijksoverheid.nl/themas/werk/werktijden/vraag-en-antwoord/bijbaan-vakantiewerk-en-stage-door-jongeren/hoeveel-uur-werken-16-17-jaar), [Rijksoverheid 15](https://www.rijksoverheid.nl/documenten/vraag-en-antwoord/bijbaan-vakantiewerk-en-stage-door-jongeren/hoeveel-uur-werken-15-jaar)] | Labour Inspectorate exposure on every automated change | Age and school calendars as **hard constraints**, tested before go-live |
| Rollout without works-council consent | Consent is needed for the working-time regulation (WOR 27(1)(b), which explicitly covers *dienstroosters*), for the personal-data regulation (27(1)(k)) and for systems "geschikt voor" monitoring attendance, behaviour or performance (27(1)(l)). Advice is needed on a major technology change (25(1)(k)). Without consent, the OR can claim nullity in writing within one month. [Verified: [Rendement](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/instemmingsrecht-or-werktijd-en-vakantie.html), [Praxikon](https://www.praxikon.com/nl/posts/or-instemmingsrecht-ai-op-de-werkvloer)] | Hard gate before go-live | File the consent request with the draft regulation text by 18 Dec 2026 |
| Uses staff data, possibly scoring individuals | A DPIA is mandatory for systematic employee monitoring and for profiling that includes assessing work performance. [Verified: [AP list via Dirkzwager](https://www.dirkzwager.nl/kennis/artikelen/definitieve-nederlandse-lijst-verwerkingen-waarbij-dpia-gegevensbeschermingseffectbeoordeling-verplicht-is-gepubliceerd)] GDPR art. 22 limits decisions with significant effects made solely by automated means, and assigned hours determine flex workers' income. [Medium] | DPIA before the live pilot | A manager approves every roster; staff can see why they got their hours and contest them |
| AI-driven allocation | EU AI Act Annex III (employment: allocating tasks based on individual behaviour or traits, monitoring or evaluating performance) applies from **2 Dec 2027**, after the Digital Omnibus delay. [Verified: [Cuatrecasas](https://www.cuatrecasas.com/en/portugal/intellectual-property/art/digital-omnibus-ai-has-been-published), [Orrick](https://www.orrick.com/zh-CN/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes)] Whether this tool falls in scope depends on its features. [Medium: General Counsel to classify] | Falls inside the contract term | Individual scoring off. Vendor contractually committed to provider obligations (documentation, logs, instructions, human-oversight features) |
| Contracts it depends on | From **1 Jan 2028**, zero-hours contracts largely disappear and become "bandwidth" contracts (maximum at most 130% of the minimum). Pupils and students working on average at most 16 h/week remain exempt. [Verified: [Dirkzwager](https://www.dirkzwager.nl/kennis/artikelen/wet-meer-zekerheid-flexwerkers-dit-verandert-er-voor-werkgevers), [Ondernemersplein](https://ondernemersplein.overheid.nl/wetswijzigingen/nulurencontracten-niet-meer-toegestaan/)] | Less flexibility for non-student staff from 2028 | The vendor's rules engine must handle this at no extra licence cost |

**Caveat:** I checked the CAO Levensmiddelenbedrijf 2025/26 (generally binding text) and the VGL CAO 2020–23 text. If you apply your own company CAO, or a later VGL version, General Counsel must confirm these clauses.

## 5. Options considered

| | A. Vendor plan as-is | B. Pilot, then waves (recommended) | C. Don't buy; improve current scheduling |
|---|---|---|---|
| What | 140 stores by March, 3-day publication, same-day changes | 8–10 pilot stores live in March, go/no-go in June, waves Sept 2027–Q1 2028 | Better forecasting spreadsheets and manager training on existing tools |
| Labour savings | Claimed 12%. Much of it is unlawful or still paid (cancelled hours) | Measured. Likely 2–6% [Medium] | Small |
| Sales and service risk | High: thin staffing at peaks | Measured against control stores | Unchanged |
| Legal risk | High: breaches the CAO, no OR consent, DPIA not done | Low, if the gates are respected | Low |
| Industrial-relations risk | High: lands mid-CAO talks | Moderate: needs an honest story to the OR | Low |
| Delivery risk | High: big-bang integrations and payroll in about 8–10 working weeks | Moderate | Low |
| Reversibility | Poor: 140 stores and all staff onboarded at once | Good: stop after the pilot | n/a |
| Main downside | Can be voided, invites conflict, may lose sales | Chain-wide savings start ~6–9 months later | Forgoes forecasting gains |

**Build vs buy:** buy. Scheduling isn't your core IP, and mature WFM products exist. If this vendor wasn't chosen through a competitive evaluation, ask two alternatives with Dutch retail references for a quote now. It costs about 4 weeks, runs in parallel with the OR process, and gives you leverage on terms.

## 6. Decision outcome

**Chosen option: B.** It keeps the COO's goal (efficiency) and a March go-live, removes the legal blockers and replaces a vendor claim with measured evidence.

- **Easier:** defending the outcome to the OR, the unions, the board and the Labour Inspectorate. Setting a savings target you can actually book. Negotiating the contract.
- **Harder:** chain-wide savings arrive later, and you have to manage the COO's and the vendor's expectations now.
- **Reversibility:** high until the wave rollout starts. Contract the expansion as an option, not a commitment.
- **Review date:** June 2027 (go/no-go), and again before 2 Dec 2027 (AI Act) and 1 Jan 2028 (flex law).

## 7. Savings vs sales model (replace the assumptions with your data)

| Input | Value | Tag |
|---|---|---|
| Store staff | 9,000 | Given |
| Average paid hours per person per week | 17 | [Assumed] |
| Annual paid hours | 9,000 × 17 × 52 ≈ 8.0M | Derived |
| Average fully loaded cost per hour | €18 | [Assumed] |
| Annual store labour cost | ≈ €143M | Derived |
| Annual sales | €1.4bn (≈ €10M per store) | [Assumed] |
| Gross margin | 25% | [Assumed] |

Each 1% of labour hours is worth about €1.43M a year. Each 1% of sales is worth about €3.5M of gross margin.

| Realised reduction in labour hours | Annual saving | Sales drop that cancels it out |
|---|---|---|
| 12% (vendor claim) | €17.2M | 4.9% |
| 6% (vendor-funded Forrester case for a comparable tool: 6–7% fewer scheduled hours) | €8.6M | 2.5% |
| 3% (my planning case) | €4.3M | 1.2% |
| 1.5% (middle of Deloitte's 0.5–2.5% range) | €2.1M | 0.6% |

Sources: [Forrester TEI, commissioned by Legion](https://tei.forrester.com/go/legion/workforcemanagement/) (its composite assumes forecast accuracy rising from 87% to 96%, and overtime at 20% of pay beforehand), [Deloitte](https://www.deloitte.com/us/en/industries/consumer/articles/retail-labor-optimization-workforce-management.html).

How to read this:
- The sales effect isn't hypothetical. In the [Gap randomised trial](https://news.uchicago.edu/story/stable-scheduling-increases-sales-and-employee-productivity-study-finds) (28 stores, 2015–16), stable scheduling raised median sales by 7% and labour productivity by 5%. [Mani, Kesavan & Swaminathan (2015)](https://pure.psu.edu/en/publications/estimating-the-impact-of-understaffing-on-sales-and-profitability/) found all 41 stores they studied systematically understaffed at a 3-hour peak, and that removing understaffing raises sales and profit. These are US apparel stores, not Dutch grocery, so the applicability is [Medium].
- Hours cut inside the notice window are still paid, so that part of the claimed saving is zero.
- A 12% cut works out to about 2 hours per person per week on average. For students that is a real share of their income, and losing them in a tight labour market costs recruitment and training. [Assumed: put your turnover cost per leaver into the model]
- The best use of forecasting is usually to **move** hours from troughs to peaks (better queues and shelf availability), not to cut a fixed percentage. Let the pilot show how much can actually be removed.

## 8. Three-year TCO template (to get from the vendor and your teams)

| Component | Year 1 | Year 2 | Year 3 | Notes |
|---|---|---|---|---|
| Licence | | | | Per employee per month × 9,000 staff. Each €1 per employee per month ≈ €108k a year |
| Implementation and integrations | | | | POS, promotions, DC deliveries, HR system, time and attendance, payroll, single sign-on |
| Internal team | | | | Product owner, integration engineers, payroll and HR specialists, store change leads [Assumed: 4–6 FTE for 9–12 months] |
| Training | | | | 140 managers plus deputies, and app onboarding for 9,000 staff (paid time: 1 h each ≈ 9,000 h) |
| CAO and legal rule maintenance | | | | New CAO in 2027 (employers propose a new wage structure and premium changes), flex law in 2028 |
| Compliance | | | | DPIA, AI Act deployer duties, audits |
| Hypercare and support | | | | Saturday-peak SLA |
| Exit | | | | Data export and parallel run |

## 9. Pilot design

**Stores:** 8–10 pilot stores covering large, small and city stores, student-heavy stores and suburban stores, plus 8–10 control stores matched on sales, size and trend. Exclude stores with a new manager or a planned renovation.

**Phases**
1. **Gate 0 (by end of Feb 2027):** OR consent, DPIA signed off, General Counsel's opinion on the CAO and AI Act, pilot-only contract, payroll parallel run passed.
2. **Shadow mode (Feb, about 4 weeks):** forecast-only, using sales, promotion and delivery data. Compare the tool's 15-minute, hourly and daily forecasts with actual demand and with managers' current plans. Set the accuracy target from this baseline. Check with General Counsel and the OR whether forecast-only use needs consent. It processes no staff data, but involve the OR anyway.
3. **Live pilot (Mar–May, 12 weeks):** the tool proposes rosters within the guardrails below, and managers approve them.
4. **Evaluation (June):** compare against the control stores (difference-in-differences against 52 weeks of history), with metrics and thresholds registered with the CFO before go-live. Ten stores will only reveal large effects (several percent), so watch the leading indicators (queues, shelf availability) closely.

**Guardrails (to put in the OR regulation and the vendor configuration)**
- Rosters published at least 7 full days ahead (CAO floor), aiming for 14.
- No forced changes after publication beyond the CAO's 24-hour rule for unforeseen events, which covers small-hours staff only. Cancelled hours are paid.
- Same-day flexibility only through voluntary offers.
- A minimum shift length agreed with the OR.
- At least 50% structural hours, plus the CAO's free-evening rules.
- Youth limits and school calendars as hard constraints.
- A minimum staffing floor per store for safety. The unions also propose minimum staffing with a sensible junior/senior mix.
- No individual performance scoring. Results are measured at team and store level only.
- A manager approves every roster, staff can see why they got their hours, and there is a contest route.

**Scorecard: pilot vs control** (the thresholds are proposals to agree with the COO and CFO)

| Area | Metric | Go threshold |
|---|---|---|
| Efficiency | Labour hours per €1,000 sales | Better than control (target ≥ 3%) |
| Sales | Like-for-like sales and transactions | No meaningful drop vs control |
| Customer | Peak checkout queue time, on-shelf availability, complaints | Not worse |
| People | Voluntary turnover, sick leave, % of shifts changed after publication, swing in each person's weekly hours, staff survey ("I can plan my life around my roster") | Not worse; changes after publication ≤ 5% |
| Compliance | CAO, Working Hours Act and youth-rule breaches; payroll accuracy | Zero breaches; ≥ 99.9% of payslips correct |
| Managers | Time spent scheduling | Lower |

## 10. Contract terms to negotiate

- Pilot fee plus a **priced option** to expand, with no committed go-live date for all stores.
- **Part of the fee at risk** on savings measured by you against control stores, with Dutch rules switched on.
- A rules engine that covers the CAO, the WAB, youth rules and the 2028 flex law, with **updates for the new CAO and law changes at no extra licence cost**.
- EU hosting, a data processing agreement (*verwerkersovereenkomst*), a list of sub-processors, no use of your data to train models for other customers without consent, full export in open formats, and exit assistance with a 90-day data return.
- AI Act: the vendor commits to provider obligations by 2 Dec 2027 if the tool is high-risk, and supplies documentation and logs for your deployer duties.
- Availability SLA covering store opening hours, especially Saturdays, and an **offline fallback** so stores can still see the last published roster.
- Security: SSO, ISO 27001 or SOC 2 reports, pen-test results, audit rights.

## 11. Technical integration checklist

- **Inputs:** POS transactions per 15 minutes per store; promotion calendar; DC delivery windows and volumes (for shelf-stacking workload); opening hours, holidays and local events.
- **Master data:** contract type and hours, structural hours, age, school calendars, skills (e.g. till, fresh counter), availability from the staff app.
- **Outputs:** approved rosters to time and attendance, then to payroll with CAO premiums (Sunday 50%, 22:00–06:00 50%, holidays 100%) [Verified: [CNV summary](https://www.cnv.nl/handel/detailhandel-food/cao-supermarkten-vgl/28-06-2024_08-12-2025_cao-supermarkten-vgl-oud/)].
- **Payroll parallel run** for at least two pay periods before any live store.
- **Monitoring:** forecast accuracy, roster-rule violations caught by the engine, payroll differences, app adoption.
- **Fallback** if the tool is down: the last published roster plus a manual process.

## 12. Timeline

| When | What | Owner |
|---|---|---|
| By 4 Dec 2026 | Joint CTO–COO position; vendor asked to restate the 12% under Dutch rules | CTO, COO |
| By 11 Dec 2026 | CEO decision; contract rescoped to pilot plus option; alternative quotes requested | CEO, Procurement |
| By 18 Dec 2026 | OR consent request filed; DPIA started; General Counsel opinion on CAO fit and AI Act scope | HR director, DPO, General Counsel |
| Dec 2026 – early Jan 2027 | Peak freeze: design only, no store changes | CTO |
| Jan 2027 | POS, promotion, delivery and HR integrations; rules configured; payroll parallel run | CTO |
| Feb 2027 | Shadow mode in pilot stores; manager training; target date for OR decision | CTO, COO |
| Mar–May 2027 | 12-week live pilot (only after Gate 0) | COO |
| Jun 2027 | Go/no-go; savings target re-based on evidence | COO, CFO, CTO |
| Sep–Nov 2027 | Waves of about 25 stores | COO, CTO |
| 2 Dec 2027 | AI Act Annex III applies: compliance evidence in place | CTO, General Counsel |
| Dec 2027 | Peak freeze | |
| 1 Jan 2028 | Flex law in force: contract rules updated | HR director, CTO |
| Jan–Mar 2028 | Remaining stores | COO, CTO |

## 13. Critic pre-screen

- **Weakest point:** it delays chain-wide savings by about 6–9 months. On the vendor's numbers that defers roughly €9–13M. On my 3% planning case it is about €2–3M. [Assumed, per section 7] A 10-store pilot also can't detect small sales effects.
- **Missing perspective:** store managers and students haven't been asked. Many may welcome replacing spreadsheet and WhatsApp rosters with an app that offers swaps and predictable shifts, so involve them in the pilot design. The COO's underlying pressure is real: employers say minimum-wage rises are straining the wage structure. That needs an answer, not just a "no".
- **If this recommendation is wrong, the cost is** delayed savings. **If the vendor plan is wrong, the cost is** a decision the OR can void, conflict during the CAO talks, payroll errors for 9,000 people and sales losses that could exceed the savings.
- **Verdict:** proceed, with the risks noted above.

## 14. Peer verification still needed

- **General Counsel:** which CAO applies and its current text; whether forecast-only shadow mode needs OR consent; AI Act classification; GDPR art. 22.
- **CFO:** the inputs in section 7; scorecard thresholds; the TCO.
- **HR director:** OR timeline (the OR can take weeks, so plan for it); student turnover cost.
- **COO:** pilot store selection; the minimum staffing floor; what has already been promised to the board.

## 15. Sources

- Ondernemersplein: [regels voor oproepkrachten](https://ondernemersplein.overheid.nl/wetten-en-regels/regels-voor-oproepkrachten/) · [werktijden en rusttijden](https://ondernemersplein.overheid.nl/wetten-en-regels/werktijden-en-rusttijden/) · [nulurencontracten niet meer toegestaan](https://ondernemersplein.overheid.nl/wetswijzigingen/nulurencontracten-niet-meer-toegestaan/)
- AWVN: [onvoorspelbaar werkpatroon](https://www.awvn.nl/hr-van-a-tot-z/onvoorspelbaar-werkpatroon/)
- CAO texts: [Levensmiddelenbedrijf 2025/26, Stcrt. 2025, 14579](https://zoek.officielebekendmakingen.nl/stcrt-2025-14579.pdf) · [VGL Grootwinkelbedrijven 2020–23](https://www.fnv.nl/getmedia/18c9c6e7-339c-46d3-963e-af97eb245d25/608-Supermarkten-VGL-cao-Grootwinkelbedrijven-Levensmiddelen-2020-2023-v291221.pdf) · [CNV: VGL CAO status](https://www.cnv.nl/handel/detailhandel-food/cao-supermarkten-vgl/28-06-2024_08-12-2025_cao-supermarkten-vgl-oud/)
- CAO talks: [FNV 18 Nov 2026](https://www.fnv.nl/nieuwsbericht/sectornieuws/handel/2026/11/voortgang-onderhandelingen-cao-supermarkten) · [FNV 2 Nov 2026](https://www.fnv.nl/nieuwsbericht/sectornieuws/handel/2026/11/cao-bod-werkgevers-supermarkten-blijft-onvoldoende) · [FNV proposals 2026–27](https://www.fnv.nl/getmedia/0a042a4d-7803-4450-839a-5504b9088fdf/Voorstellenbrief-CAO-LMB-VGL-2026-2027.pdf) · [FNV 19 Jun 2026](https://www.fnv.nl/nieuwsbericht/sectornieuws/handel/2026/06/wie-betaalt-de-prijs-voor-een-goede-cao-supermarkt)
- Flex law: [Dirkzwager](https://www.dirkzwager.nl/kennis/artikelen/wet-meer-zekerheid-flexwerkers-dit-verandert-er-voor-werkgevers)
- Works council: [Rendement on art. 27(1)(b)](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/instemmingsrecht-or-werktijd-en-vakantie.html) · [Praxikon on OR rights over AI](https://www.praxikon.com/nl/posts/or-instemmingsrecht-ai-op-de-werkvloer)
- Privacy: [Dirkzwager on the AP DPIA list](https://www.dirkzwager.nl/kennis/artikelen/definitieve-nederlandse-lijst-verwerkingen-waarbij-dpia-gegevensbeschermingseffectbeoordeling-verplicht-is-gepubliceerd)
- AI Act: [Cuatrecasas on Regulation (EU) 2026/1744](https://www.cuatrecasas.com/en/portugal/intellectual-property/art/digital-omnibus-ai-has-been-published) · [Orrick](https://www.orrick.com/zh-CN/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes)
- Youth rules: [Rijksoverheid 16–17](https://www.rijksoverheid.nl/themas/werk/werktijden/vraag-en-antwoord/bijbaan-vakantiewerk-en-stage-door-jongeren/hoeveel-uur-werken-16-17-jaar) · [Rijksoverheid 15](https://www.rijksoverheid.nl/documenten/vraag-en-antwoord/bijbaan-vakantiewerk-en-stage-door-jongeren/hoeveel-uur-werken-15-jaar)
- Evidence on scheduling: [Gap stable scheduling trial (UChicago)](https://news.uchicago.edu/story/stable-scheduling-increases-sales-and-employee-productivity-study-finds) · [Mani, Kesavan & Swaminathan 2015](https://pure.psu.edu/en/publications/estimating-the-impact-of-understaffing-on-sales-and-profitability/) · [Forrester TEI for Legion (vendor-commissioned)](https://tei.forrester.com/go/legion/workforcemanagement/) · [Deloitte](https://www.deloitte.com/us/en/industries/consumer/articles/retail-labor-optimization-workforce-management.html)
