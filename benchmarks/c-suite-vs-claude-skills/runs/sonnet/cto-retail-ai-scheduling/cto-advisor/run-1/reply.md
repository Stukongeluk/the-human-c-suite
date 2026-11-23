# Recommendation: AI workforce scheduling, 140 stores

## Bottom Line

Do not commit to "all stores live by March". Recommend a **staged rollout with hard go/no-go gates**: a proven pilot in roughly 8-12 stores from February, then waves across the remaining stores if the gates are met. Tell the COO this is a plan to capture the savings safely, not a "no".

Three things drive this:

1. **Three-day publication probably breaks Dutch law for your on-call staff.** It is the vendor's default, not a legal design. 🟡
2. **The tool changes working conditions and processes personal data on 9,000 people, so you almost certainly need Works Council consent first.** 🟢 That cannot realistically be finished and bedded in before March.
3. **The 12% is a vendor claim, not a measured number for your chain.** 🔴 It has to be proven in your stores, against service levels, before you bet 140 stores on it.

## What (with confidence)

| Finding | Confidence |
|---|---|
| WOR art. 27 gives the Works Council a consent right over working-time/rota regulations and over systems that process or monitor employee data. A tool that sets schedules and re-plans shifts on the day squarely triggers it. Check the exact sub-sections with your labour lawyer. | 🟢 |
| The Dutch Flexible Work/WAB rules require that on-call staff get at least 4 days' notice of a shift. A CAO can shorten that, but not necessarily to 3 days. Cancelling inside the notice period generally means the wages are still owed. Your CAO decides the real number. | 🟡 |
| "Adjust shifts on the day" for students on flexible contracts will hit the same notice and refusal rights, plus ATW rest and break rules (stricter for under-18s). The tool must encode these as hard constraints, not preferences. | 🟡 |
| Scheduling and managing workers is a **high-risk AI use case** under the EU AI Act (employment/worker management). Obligations are scheduled to apply from August 2026, but a proposed delay is in play. Verify the current date, and assume your chain is the "deployer" with duties on human oversight, worker information and logging. | 🟡 |
| GDPR: a DPIA is required. Fully automated decisions with significant effects (art. 22) need a human in the loop. The Dutch DPA (AP) is active on employee monitoring. | 🟢 |
| March is about 14 weeks away, and that window includes the December peak, when you will not want store managers learning a new tool or schedules changing. Realistically you have 6-8 working weeks of usable build time. 140 stores in that window is high risk. | 🟢 (timeline arithmetic), 🟡 (the peak-season constraint is my assumption about your trading calendar) |
| The 12% is the vendor's figure. Typical savings in retail workforce management come mostly from cutting overstaffing at quiet times and from better forecasting. The real result depends on how much slack you have today and on how much work is **not** demand-driven (deliveries, shelf replenishment, bakery, cleaning). | 🔴 |

## Why

**1. The savings claim and the risk sit in the same place.** Cutting 12% of hours means running leaner exactly when forecasts are wrong. In a supermarket the failure modes are queues, empty shelves, missed freshness and compliance issues (age checks, food safety), which cost sales and customer trust. A 15-minute resolution looks precise, but the work is not 15-minute work. Restocking a pallet or a delivery does not split into quarter-hour pieces. Ask the vendor how the model handles non-checkout tasks.

**2. Your workforce makes this a people-risk, not just an IT project.** Many of your staff are students on flexible contracts. Short-notice changes hit them hardest: exams, second jobs, childcare, travel. Predictable schedules are a retention lever. If the tool optimises hours at the cost of predictability, you will pay for it in attrition, recruitment and training. Those costs do not appear in the vendor's 12%. Your own turnover data will show what a 1-2 point rise costs you.

**3. Consent, not just a go-live date, is the critical path.** The Works Council (and the unions behind the CAO) will want to know what the algorithm optimises for, which data it uses, who can override it, and how fairness is assured. If they find out after the contract is signed you will lose months, and the relationship. Involve them now as a design partner.

**4. Forecast quality is unproven on your data.** The tool is only as good as the demand forecast and the data feeding it (POS, footfall, promotions, weather, local events, HR availability and contract rules). A vendor demo on someone else's data tells you little. Back-test on 12-24 months of your own store data before committing.

**5. Lock-in and contract terms.** A "by March, all stores" deadline is a sales lever for the vendor. The leverage goes the other way if you ask for staged payment, a pilot exit clause and data portability.

## How to Act

**Next 2 weeks**
- Brief the COO and CFO: the aim is to capture the savings with a defensible plan, with the gates below. Agree the **net** benefit definition (labour hours saved minus lost sales, availability and attrition effects), not just hours saved.
- Open the process with the Works Council (OR) and brief HR and the unions as your CAO requires. Ask your legal counsel to confirm the notice rules in your CAO and for on-call staff.
- Start the DPIA with your DPO. Ask the vendor for its AI Act conformity documentation, model description and data-processing agreement (including where data is hosted).
- Request a **back-test** on your data: vendor forecast vs actual for 10-15 stores across store types (urban, rural, large, small) for at least a year.

**Weeks 3-6**
- Contract: pilot-first structure with payment tied to gates, an exit right, data export, a price cap for the rollout, and configurable legal constraints (notice periods, rest times, youth rules) that your team controls.
- Integration readiness: POS, HR/payroll, time and attendance, availability app. Name the owner. Integration is the usual cause of retail WFM delay. 🟡
- Design guardrails: no automatic shift changes without staff acceptance; minimum notice that satisfies the stricter of law and CAO (probably 4+ days for on-call, not 3); fairness rules; a manager override at every step; no silent cuts of contracted hours.

**Pilot (indicatively Feb-Apr)**
- 8-12 stores, mixed types, with matched **control stores** so you can separate the tool's effect from seasonality.
- Start with **recommendations the store manager approves** ("assisted mode"), then move to auto-publish only if the gates are met. Delay "adjust on the day" until later; it carries the most legal and staff risk.

**Gates to roll out beyond the pilot** (set the thresholds with the COO and the OR before starting)
1. Forecast accuracy better than the current manual process by an agreed margin.
2. Labour-hour reduction meaningfully above zero **with** service KPIs flat: queue times, on-shelf availability, sales per labour hour, customer satisfaction.
3. Staff metrics: no rise in no-shows, shift-swap complaints or voluntary attrition among students beyond an agreed band; a staff survey.
4. Legal and privacy sign-off done (OR consent, DPIA, AI Act position).
5. Support load acceptable: tickets per store, store-manager time spent on the tool.

**Waves**: if the gates pass, roll out in waves of ~20-30 stores, avoiding peak periods, with a rollback path (revert to the previous scheduling process) for each wave. Full rollout could realistically complete in the second half of 2027, not March. Tell the COO that the savings are delayed by months, not lost.

**Document it**: write this as an ADR (options: do nothing, vendor X as proposed, staged vendor X, alternative vendor/build). Include a 3-year TCO and a reversibility section. "Build" is almost certainly wrong here; this is commodity capability. Run at least one competing vendor quote for leverage. 🟡

## What the numbers could look like (illustrative, 🔴 assumptions)

I do not have your cost base, so treat this as a method, not a forecast. If labour is, say, 10-12% of revenue and the tool delivers half the claimed saving (6%) in the first year, the benefit is roughly half what the COO's slide shows. If the tool pushes student attrition up a few points, or loses a fraction of a percent of sales to availability, much of the remainder can disappear. Ask finance to model three cases (vendor claim, half the claim, and a downside with attrition and sales loss) before the Works Council meeting.

## Your Decision

1. **Recommended:** staged rollout with gates, pilot from February, full rollout when gates pass. Lowest regret.
2. **Acceptable if the COO insists on speed:** all-store contract signed now, but with a pilot-first schedule, gate-linked payments and an exit clause, and no auto-adjustment on the day until legal clearance.
3. **Not recommended:** all stores live by March on the vendor's terms. This is the option with the highest legal, operational and people risk, and a weak negotiating position.

Questions that would change my advice: What does your CAO say on roster notice? What share of staff are on-call/min-max versus fixed-hours contracts? Is there a Works Council at group level, and how has it handled prior tooling? How much of store labour is demand-driven versus fixed tasks? Who is the vendor, and who are its reference customers in Dutch grocery?

I am glad to draft the ADR, the Works Council briefing, or the vendor back-test and contract requirements next. Verify all legal points above with your counsel before relying on them; I have flagged where I am less certain.
