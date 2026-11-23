# Driver productivity: response to the leaderboard and bottom-10% proposal (detail)

For: CPTO. Date: 23 November 2026. Status: advisory. The legal points need checking by General Counsel and the DPO, and this is not legal advice.

Confidence tags: **[High]** means verified or an established pattern. **[Medium]** means one source or a reasonable inference. **[Low]** means based on assumptions.

---

## 1. Draft note to Operations (ready to adapt)

> **Subject:** Driver productivity: let's hit the target, but not with a ranking
>
> Hi [name],
>
> Thanks for the proposal. I share the goal of more delivered parcels per driver-hour, and I'd like to own that number with you rather than just review your plan.
>
> I don't want to ship the live leaderboard or the weekly bottom-10% list as specified, for three reasons:
>
> 1. **It mostly measures the route.** Stops per hour depends heavily on stop density, apartment blocks, parcel mix and depot load-out time. A weekly bottom 10% will mostly flag the hardest routes and bad weeks, not the weakest drivers. Whoever gets flagged will also "improve" the next week on their own, so the 8% will look real whether or not it is.
> 2. **It rewards stops, not deliveries.** A "not home" scan counts as a stop. A live ranking in the van also puts drivers under time pressure while they drive. In peak season that means more failed deliveries, complaints and incidents.
> 3. **It makes us look like the employer of our subcontractors' drivers.** Sending named subcontractor drivers to their employer for action is a real legal exposure in both Belgium and the Netherlands. On top of that we'd need works council consent and a DPIA for our own staff.
>
> What I propose instead:
>
> - **Next two weeks:** we look at the data together. Where do driver hours actually go? How much of the spread in stops per hour comes from the route and how much from the driver? What's behind the 8%? Can you send me the source?
> - **My team fixes what slows every driver down:** seconds per stop in the app, load sequencing, address data and failed first attempts.
> - **Mid-January, after peak:** a randomized pilot across depots. Drivers get private, route-adjusted feedback at the end of their shift. Drivers who stay below their route's expected range for several weeks get coaching. Subcontractors get scorecards for their whole fleet on quality and compliance. We measure successful deliveries per route-hour, with guardrails on failed deliveries, safety and driver attrition.
> - **If it works**, we roll it out once the works council and legal have signed off. If it doesn't, we've learned that cheaply.
>
> Until then, I'd like us to agree not to add anything during peak that pushes drivers to go faster.
>
> Can we take 45 minutes this week to agree the target and the diagnostic?
>
> [CPTO]

---

## 2. Why a weekly bottom-10% list misfires

I modelled a week's stops per hour for each driver as three parts added together: the route, the driver, and weekly noise. The model used 2,400 drivers over 13 weeks, a mean of 15 stops per hour and a standard deviation of 3. How the variation splits between the three parts is **[ASSUMED]**, so I ran three scenarios. This is an illustration, not a measurement.

| Split (route / driver / noise) | Share of each week's flagged drivers who are truly among the weakest 10% | Share of flagged drivers on the hardest quarter of routes | Drivers flagged at least once in 13 weeks | Next-week rise for the flagged group with no intervention | Accuracy of a route-adjusted 8-week average instead |
|---|---|---|---|---|---|
| 50 / 20 / 30 | 28% | 79% | 33% | +16% | 74% |
| 30 / 40 / 30 | 41% | 58% | 34% | +17% | 78% |
| 20 / 30 / 50 | 35% | 58% | 44% | +27% | 70% |

**What the table shows:**

- **A raw weekly ranking is right about 3 to 4 times in 10.** A flag that is wrong most of the time teaches drivers that it's arbitrary, and subcontractors end up acting on noise. [Medium]
- **Regression to the mean produces a built-in "gain".** If the 8% was measured as "flagged drivers before versus after", it would show double-digit gains even with no real effect. Any credible number needs a control group. [High on the mechanism]
- **A route-adjusted, multi-week view is much better, but still wrong about 1 time in 4.** That is good enough for offering coaching. It is not good enough for sanctions. [Medium]

**Replace the illustration with your real data (Action 3).**

- Fit a mixed model on 6 to 12 months of stop data. A mixed model is a regression that separates the share of variation caused by known factors from the share that belongs to each driver.
  - Known factors: route, depot, weekday, weather, parcel mix (size and weight), stop density, share of apartment stops, number of parcels per stop and driver tenure.
  - Driver effect: estimated separately for each driver.
- Report two numbers: the driver's share of the variation, and how well a driver's rank in one week predicts their rank the next.
- If the driver share is high and ranks are stable from week to week, a ranking carries more information than I've assumed. Update this advice if so.

**Check whether the metric can be gamed today.** Compare the rate of failed attempts with how long the GPS shows the van at the address. "Not home" scans with near-zero time at the door are the leading sign that stops per hour is already being gamed.

---

## 3. Evidence on rank feedback, time pressure and the sector

| Finding | Source | So what |
|---|---|---|
| Private rank information, with no pay or career consequences, raised productivity about 6.8% among ~65 workers in a German warehouse | [Blanes i Vidal & Nossol, Management Science 2011](https://personal.lse.ac.uk/blanesiv/tournaments.pdf) | Likely the best case for the 8%. It describes the opposite of a public ranking with sanctions. [High] |
| A randomized removal of rank displays in a US furniture firm increased sales. The decline under ranking came from workers ranked below their own expectations. | [Barankay, via Wharton](https://knowledge.wharton.upenn.edu/article/why-its-sometimes-better-not-to-tell-employees-where-they-stand/) | Ranking can demotivate exactly the bottom group you're trying to lift. [Medium] |
| "Time pressure and work-related stress decrease driver performance and vigilance and increase crash risk." EU-OSHA advises delivery riders' employers to avoid pay systems based on delivery performance and piecework. | [EU-OSHA, Driving for work](https://eguides.osha.europa.eu/vehicle-safety/themes/speeding) | A live ranking in the van is a time-pressure device. [High] |
| Couriers report speeding and running red lights to stay within time windows, and 40% of app users found the apps distracting. The study recommends that any drop rate allow safe travel within speed limits. | [UCL, Christie & Ward 2018](https://www.ucl.ac.uk/news/2018/aug/gig-economy-drivers-and-riders-heightened-risk-traffic-collisions) | Shows how pace pressure turns into risk. [Medium] |
| The Dutch Labour Inspectorate inspected 35 depots of the six largest parcel services, found a high work pace and physical overload, and gave the firms one year to act (October 2024) | [NOS](https://nos.nl/l/2540046) | The sector is under active inspection for work pace. [High] |
| 23% of parcel drivers cite high work pressure as a reason for work-related absence, against 11% in comparable occupations | [TNO, sickness absence among parcel drivers](https://monitorarbeid.tno.nl/wp-content/uploads/sites/16/2026/02/TNO-2025-M13169_Verzuim-bij-pakketbezorgers.pdf) | Pace pressure already shows up in absence. [Medium: cross-sectional data] |
| The former Inspectie SZW found misconduct at about 9 in 10 of 80 inspected couriers and subcontractors (2020) | [Radar / NRC](https://radar.avrotros.nl/artikelen/38277) | Inspectors and the press will read "flag drivers to subcontractors" in that light. [Medium: older data] |

---

## 4. Legal and compliance map (for General Counsel and the DPO to verify)

| Issue | Who it covers | What it means for this feature | Confidence |
|---|---|---|---|
| Works council consent, NL (WOR art. 27(1)(l)) | Your own Dutch staff. Whether subcontracted drivers count as "persons working in the enterprise" needs counsel's view. | Consent is needed before introducing a system aimed at, or merely suitable for, monitoring performance. If the works council invokes it, a decision taken without consent is void (art. 27(5)). | [Medium-High] |
| DPIA (data protection impact assessment) | Every driver whose data you process | NL: required for systematic employee monitoring. The Dutch DPA's 2026 draft list of DPIA exemptions explicitly leaves systematic employee monitoring out ([Salaris van Morgen](https://www.salarisvanmorgen.nl/2026/07/06/consultatie-lijst-dpia-uitzonderingen-verwerking-persoonsgevens-werknemers/)). BE: advised for electronic monitoring, and mandatory in some cases under the Belgian DPA's list ([Securex](https://www.securex.be/nl/lex4you/werkgever/themas/verplichtingen-werkgever/gdpr-en-privacy/verplichting-tot-gegevensbeschermingseffectbeoordeling-(dpia)-bij-het-invoeren-van-elektronisch-toez)). | [High] NL, [Medium] BE |
| GDPR art. 22 (automated decisions) | All drivers | A weekly automated flag that leads to fewer shifts or termination, with no meaningful human review, is a decision with significant effect based solely on automated processing. | [Medium] |
| GDPR lawful basis and necessity | All drivers | Legitimate interest must outweigh privacy. If a less intrusive option exists (private, route-adjusted feedback), a public live ranking is hard to justify as necessary. | [Medium] |
| Belgian Parcel Delivery Act | All last-mile drivers in Belgium, including subcontracted and self-employed ones | You are presumed liable for a direct subcontractor's breaches unless you show non-negligent monitoring. You must monitor without exercising employer authority over their people ([DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/belgium-parliament-approves-new-legislation-on-delivery-activities)). Delivery time is capped at 9 hours a day (10 hours twice a week), 56 hours a week and 90 hours over two weeks from 1 July 2026. Minimum remuneration and a prevention coordinator are also required ([PwC Legal](https://www.pwclegal.be/en/news/parcel-delivery-act-introduces-improved-working-conditions-for-p.html), [BelParcel](https://belparcel.fgov.be/en/which-obligations/overview.html)). | [Medium-High] |
| Authority over subcontracted drivers, NL | Subcontracted drivers in NL | Directing and supervising another firm's drivers points to labour provision. From 1 January 2027, under the Wtta, only licensed labour providers may lend workers and hirers may only use licensed ones. Registration runs in November and December 2026, and enforcement starts in 2028 ([Rendement](https://www.rendement.nl/uitzendkrachten-gedetacheerden/nieuws/toelatingsstelsel-voor-uitleners-gaat-1-januari-2027-in.html)). | [Medium] |
| Authority over subcontracted drivers, BE | Subcontracted drivers in BE | Exercising employer authority over another company's workers risks being treated as unlawfully placing workers at your disposal. [ASSUMED: rules on placing workers at a user's disposal; verify] | [Low-Medium] |
| EU Platform Work Directive (2024/2831) | Applies only if you qualify as a "digital labour platform" | Transposition is due 2 December 2026, and parcel delivery is among the sectors most likely affected. Using intermediaries doesn't avoid the obligations. A DPIA is always required, workers must get written information about the systems, a human must decide any restriction, suspension or termination, and representatives must be consulted before significant system changes ([Lewis Silkin](https://www.lewissilkin.com/insights/2026/11/13/the-eu-platform-work-directive-what-international-employers-need-to-know)). The Dutch draft Platform Work Act was published on 29 June 2026 ([Global Workplace Insider](https://www.globalworkplaceinsider.com/2026/09/the-platform-work-act-implementing-the-eu-platform-work-directive-in-the-netherlands/)). | [High] on the deadline, [Low-Medium] on whether you're in scope |
| Works council information and consultation, BE | Your own Belgian staff | Introducing new technology with collective effects normally triggers information and consultation duties. [ASSUMED: verify the applicable collective agreements] | [Low] |
| Psychosocial workload (NL Arbowet; BE welfare at work rules) | Your own staff, plus chain exposure for subcontracted staff | A ranking by work pace is a new source of work-pressure risk and belongs in the risk assessment. [ASSUMED] | [Medium] |

**What this means for the design:** manage subcontractors on fleet-level outcomes and let them manage their own people. Don't send them named individual rankings to act on.

---

## 5. What to measure instead

This follows the north star, leading indicators and lagging indicators hierarchy. A north star should measure value delivered to the customer, not activity.

- **North star (owned by you and Operations together):** successful first-attempt deliveries per route-hour.
- **Leading indicators that product and operations can move:**
  - Seconds spent at each stop (from scan to proof of delivery), broken down by app flow
  - Depot load-out time and sequencing errors
  - Address and geocode error rate
  - First-attempt success by reason code, checked against GPS time at the address
  - Planned versus actual route time
- **Guardrails (these must not get worse):**
  - False "not home" rate
  - Damage and misdelivery claims
  - Customer complaints
  - Safety events: speeding, harsh braking and incidents
  - Working-time compliance (the Belgian caps, the Dutch Working Hours Act)
  - 90-day driver attrition and absence
- **How feedback reaches drivers:**
  - Route-adjusted, using an 8-week rolling window.
  - Shown as a band: "within, above or below expected for your routes."
  - Private, at the end of the shift, never live while driving.
  - Only a person decides any follow-up, and the first step is always to check the route, vehicle and parcel mix.
- **How subcontractors are managed:** a fleet scorecard covering route-adjusted productivity, first-attempt success, quality, safety and working-time compliance.

---

## 6. Where an 8% could come from without anyone driving faster

All sizing below is **[ASSUMED]** and needs to be checked in the diagnostic before you commit to a number.

| Lever | Owner | Rough size |
|---|---|---|
| Friction in the app at each stop: taps, scan retries, photo proof of delivery, signature and age-check flows | Driver-app team | 10 s saved per stop × ~130 stops ≈ 22 min a day ≈ **4.5%** of an 8-hour shift |
| Failed first attempts: pre-delivery notifications, safe-place and neighbour preferences, redirecting to pickup points or lockers | Product + Customer | Each percentage point of failures removed saves roughly a point of repeat stops (assuming one redelivery per failure) |
| Load-out and in-van sequencing: shelf-by-stop loading, sort errors | Operations + Product | Unknown: measure the minutes per route at the depot and spent searching in the van |
| Address and geodata quality: access codes, apartment entrances, wrong pins | Product + Data | Unknown: measure the time between arriving near the address and the scan |
| Coaching for drivers who persistently fall below their route's expected range | Operations + subcontractors | Small overall, concentrated in a few drivers |

---

## 7. Pilot design (Q1 2027)

- **Unit:** randomize depots (or clusters of depots), not individual drivers, so that drivers at the same depot don't get different treatments. Stratify by NL and BE, and by urban and rural.
- **Baseline:** 4 weeks from December data, which captures peak and is labelled as such, plus early January.
- **Duration:** 8 to 10 weeks from mid-January.
- **Treatment:**
  1. Private, route-adjusted feedback at the end of each shift.
  2. A coaching offer through depot leads.
  3. Fleet scorecards for subcontractors.

  Ship the app speed fixes to everyone in stages, and measure them separately as each stage rolls out.
- **Primary metric:** successful deliveries per route-hour.
- **Guardrails and stop rules:** set the thresholds with Operations before the pilot starts. If safety events or the false "not home" rate in the treatment group rise beyond the agreed threshold compared with control, pause the pilot.
- **Decision rule:** agree it upfront, for example: "roll out if the primary metric rises by at least X% with guardrails flat; otherwise iterate."
- **Governance before launch:**
  - DPIA completed.
  - NL: works council consent. BE: information and consultation.
  - Drivers told in writing what is measured and why.
  - A data-sharing agreement with subcontractors that limits what they receive and how they may use it.
- **Driver input:** use ride-alongs during the diagnostic, and test mock-ups of the feedback screens with drivers before building them.

---

## 8. Critic pre-screen

This is a high-stakes decision because it touches all 2,400 drivers, so the advice gets a challenge before it is final.

- **Weakest point:** the case against ranking leans on an illustrative model. If your data shows a large, stable driver effect, a ranking carries more information than I've assumed. Action 3 settles this within two weeks.
- **Missing perspectives:** drivers and subcontractors haven't been asked yet. The CFO hasn't put a value on the 8% or on the cost of each week of delay.
- **If I'm wrong, the cost is:** roughly 8% of weekly driver cost for every week of delay [ASSUMED: the 8% would be real and net of failed deliveries]. The CFO should quantify it.
- **Verdict:** proceed, with the risks above noted.

---

## 9. Assumptions

- About 2,400 drivers, two thirds of them subcontracted (about 1,600), as you stated. The split between NL and BE is unknown.
- A mean of about 15 stops per hour, about 130 stops per day and an 8-hour shift [ASSUMED].
- The route, driver and noise split in Section 2 [ASSUMED].
- The source and method behind the 8% are unknown.
