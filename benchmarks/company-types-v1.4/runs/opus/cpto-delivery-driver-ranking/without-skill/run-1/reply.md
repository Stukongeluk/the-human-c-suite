**Short answer:** Back the goal and turn down the mechanism. Don't build the live stops-per-hour leaderboard or the weekly bottom-10% list for subcontractors as specified. Don't just say no either. Offer Operations a route to the same 8% that has a better chance of actually showing up in your P&L, and offer to test it against their idea with numbers you both agree on in advance.

8% is worth chasing. On 2,400 drivers it's roughly 180 drivers' worth of hours. So take the target seriously. The problem is that this design measures the wrong thing, rewards the wrong behaviour, and pulls you into managing other companies' employees.

## Why the proposal as written is a bad bet

**1. Stops per hour mostly measures the route, not the driver.** The number is driven by:
- stop density, high-rise vs. rural, and parcels per stop
- business vs. residential addresses
- how well the van was loaded at the depot and what time it left
- vehicle type and how well the driver knows the route

A forced ranking also flags 240 drivers every week by design, even if everyone improves. I ran a quick simulation with illustrative assumptions: route explains half the weekly variation, driver skill a quarter, week-to-week noise a quarter. Under those assumptions:
- Only about **1 in 3 weekly flags** lands on a driver who is genuinely in the bottom 10% for skill.
- About **1 in 6 flags** goes to a driver who is *above* median.
- More than **40% of all drivers** would be flagged at least once a year.

Even if routes explained *nothing*, fewer than half the flags would be accurate. Your data team can replace my assumptions with real ones in a week.

There's a trap too. Next week the flagged group will "improve" by about a quarter of its gap with no intervention at all, purely through regression to the mean. Ops will read that as proof it works.

**2. It will be gamed, and the gaming costs more than 8%.**
- *Denominator gaming:* logging on late, logging off early, taking breaks off-app. That means unrecorded, unpaid working time in your chain. In the Netherlands that's a chain-liability exposure for wages. In Belgium the Parcel Act sets a minimum hourly fee and working-time caps, and makes you presumed liable for your direct subcontractors' breaches unless you can show proper oversight.
- *Numerator gaming:* "not home" scans without really trying, parcels left at doors, rushed neighbour drop-offs. Your first-attempt success rate falls and redeliveries, claims and complaints go up.
- *Safety:* speeding, skipped breaks, and a constantly updating ranking on a phone in the cab, which invites drivers to look at the screen while driving. If there's a serious crash, the first question will be what your app was rewarding.

**3. Flagging individual subcontractor drivers is acting like their employer.** Your subcontracting model depends on the line between "we contract a service" and "we direct their people". Ranking named drivers of another company and sending that company a weekly list of who's underperforming is performance management of their staff.
- *Netherlands:* the more you direct and supervise subcontractor staff, the more the arrangement looks like labour hire rather than contracting, with the equal-pay and liability consequences that follow.
- *Belgium:* the Parcel Act *requires* you to monitor your chain. But advisers explicitly warn that this monitoring must not turn into exercising employer authority over subcontractors' staff, and Belgium has a long-standing ban on illegally putting workers at someone's disposal.

Get counsel in both countries to look at this specifically. My expectation is they'll be uncomfortable.

**4. Privacy law and works councils won't allow it in this form, and won't allow it quickly.** To be fair to Ops: proportionate productivity monitoring tied to a real operational purpose is lawful. In December 2025 France's Conseil d'État cut Amazon's CNIL fine from €32m to €15m and accepted several of its scanner indicators. It also upheld that keeping detailed data for performance evaluation wasn't justified. The parts of this proposal that break are:
- **A weekly named flag that a third party uses to decide about someone's work.** After the CJEU's *SCHUFA* ruling, a score that someone else "draws strongly" on can itself count as an automated decision under Art. 22 GDPR. That brings rights to human review and to contest it. Italy fined Glovo's Foodinho €2.6m over a rider ranking that cut low scorers off from work without those safeguards.
- **A public leaderboard** shows every driver's performance to colleagues, including employees of competing subcontractors. It also hands each subcontractor a list of its rivals' best drivers.
- **Process:** this needs a DPIA. For your own Dutch drivers it needs works council consent: monitoring systems suited to checking performance fall under the works council's consent right in art. 27 of the Dutch Works Councils Act (WOR). In Belgium the works council has to be informed and consulted on new technology. The "ship it next sprint" timeline isn't real anyway.
- **Later:** if the ranking ever becomes "smart" (an ML model adjusting for route difficulty, feeding decisions about drivers), it moves into AI Act high-risk territory for worker evaluation. Those obligations were pushed to December 2027 in the AI Omnibus deal.

**5. Reputation.** The NL/BE parcel sector is already under scrutiny:
- Belgium passed its Parcel Act after the subcontractor scandals.
- The Dutch Labour Inspectorate took enforcement action at all six big parcel companies in 2023–24 over depot work that was physically too heavy.

"Delivery app names and shames the bottom 10% of drivers every week" is a headline waiting to happen, and your large shippers will ask about it in supplier audits.

**And to be honest about the evidence:** the 8% isn't absurd as a short-term bump in the *measured* number. In one German warehouse, simply telling pickers their own relative position raised output by about 6.8% with no lasting quality damage. But that was private feedback on a fairly uniform task, not a public ranking on very different routes. A randomized study the other way found that *removing* rank feedback from furniture salespeople raised sales by about 11%. Rank feedback can help or hurt, and the details decide which. What matters is net, lasting gain in **successful deliveries per paid hour**, not stops per logged hour.

## What I'd propose instead

1. **Diagnose (2–3 weeks).** Split stops-per-hour variation into depot, route, day and driver. Find where the time actually goes: depot departure delays, van load sequence, time spent finding entrances and access, failed attempts, taps per scan, parking. My bet is that most of the recoverable 8% is in the system, not in the bottom 240 drivers.
2. **Fix system levers. This is your product team's home turf.**
   - Load vans in drop order.
   - Let drivers capture access and entrance notes that the next driver gets.
   - Fewer taps per stop.
   - Better delivery-moment predictions and customer notifications to cut failed first attempts.
   - Lockers or pickup points for addresses that fail repeatedly.
   - Same driver, same route wherever possible.
3. **Private, fair feedback for drivers.** Each driver sees their own trend against what's *expected for their route*, alongside quality measures (first-attempt success, damage, complaints). Nobody else sees it, and it's never shown while the vehicle is moving. If Ops wants a competitive element, make it team or depot goals, not an individual ranking.
4. **Manage subcontractors on outcomes, not on their people.**
   - Scorecards per subcontractor: route-adjusted productivity, quality and compliance (hours, minimum fee, rest).
   - You manage the contract; they manage their staff.
   - For a driver who is a persistent outlier on comparable routes over 6–8 weeks, use a human-reviewed process. Check route, vehicle and equipment first, then offer a ride-along or coaching. The driver can see the data and contest it. No automatic weekly list.
5. **Test it properly.** Randomize by depot.
   - Arms: system fixes alone vs. system fixes plus private feedback vs. control. If Ops still wants a visible leaderboard, I'd agree to test a route-adjusted, team-level version in a few depots with your own employed drivers, *after* the DPIA and works council consent. I'd decline the bottom-10% flag to subcontractors outright.
   - Primary metric: successful deliveries per paid hour.
   - Guardrails: first-attempt success, claims and damage, complaints, safety events, break compliance, the gap between logged and paid hours, sick leave, and turnover, including at subcontractors.
   - Run at least 10–12 weeks so novelty wears off. Agree the success threshold with Ops *before* you start, and commit to rolling out whatever wins.

## Questions to put back to Ops about the 8%

- Where does it come from: a vendor case study, another carrier, our own pilot?
- Measured as stops per *logged* hour, or successful deliveries per *paid* hour?
- Was there a control group, and over how long was it measured?
- Is it net of extra failed deliveries, redeliveries, claims and driver churn? A new driver on an unfamiliar route is slower for weeks, so churn eats productivity directly.
- What do they expect subcontractors to *do* with the list?

## A message you could send

> I want the 8% too. It's worth roughly 180 drivers' worth of capacity, so let's go after it seriously. I'm not going to build the version on the table, though. Stops per hour mostly reflects route difficulty, so a weekly bottom-10% list would mostly flag hard routes and bad luck. It also invites under-logged hours and "not home" scans, and it puts us in the position of performance-managing our subcontractors' employees. That's a legal problem for us in both NL and BE, and a GDPR and works council problem on top.
>
> Here's my counter-proposal. Give us three weeks to find where the lost time actually sits. Then run a randomized depot test of system fixes plus private, route-adjusted feedback for drivers, measured on successful deliveries per paid hour with quality and safety guardrails. We agree the success bar together up front, and if it clears, we roll it out. Can you also share where the 8% estimate comes from, so we can use it as the benchmark?

Before anything goes live, check the Dutch and Belgian legal specifics with counsel and your DPO. The points above are what I'd expect them to raise, but they aren't a substitute for their review.

## Sources

- Blanes i Vidal & Nossol, [Tournaments without prizes: evidence from personnel records](https://personal.lse.ac.uk/blanesiv/tournaments.pdf) (Management Science, 2011): +6.8% from relative-position information for warehouse pickers
- Barankay, [Rank Incentives: Evidence from a Randomized Workplace Experiment](https://repository.upenn.edu/bepp_papers/75): removing rank feedback raised sales about 11%
- [Conseil d'État cuts Amazon France Logistique fine from €32m to €15m](https://ppc.land/france-slashes-amazons-gdpr-fine-from-eu32m-to-eu15m-over-warehouse-monitoring/) (23 Dec 2025); original CNIL findings summarized by [Lewis Silkin](https://www.lewissilkin.com/passle/102j1g2)
- [Italian Garante fines Foodinho €2.6m over rider performance algorithms](https://www.insideprivacy.com/gdpr/italian-supervisory-authority-fines-foodinho-over-its-use-of-performance-management-algorithms/)
- [CJEU SCHUFA (C-634/21): a score a third party draws strongly on is an automated decision](https://www.aoshearman.com/en/insights/ao-shearman-in-the-netherlands/102k8l4/cjeu-rules-that-a-credit-score-constitutes-automated-decision-making-under-the-gd)
- Belgian Parcel Act: [DLA Piper summary](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/belgium-parliament-approves-new-legislation-on-delivery-activities) (chain liability; monitoring must not become employer authority) and [PwC Legal summary](https://www.pwclegal.be/en/news/parcel-delivery-act-introduces-improved-working-conditions-for-p.html)
- [Works council consent right for monitoring systems (WOR art. 27), per the Dutch DPA's guidance](https://www.dirkzwager.nl/kennis/artikelen/instemmingsrecht-van-de-or-volgens-het-or-privacyboekje-van-de-ap)
- [Dutch Labour Inspectorate: healthy and safe work in parcel depots (2024)](https://nlarbeidsinspectie.nl/binaries/nlarbeidsinspectie/documenten/rapporten/2024/10/08/gezond-en-veilig-werken-in-depots-van-pakketbezorgdiensten/gezond-en-veilig-werken-in-depots-van-pakketbezorgdiensten-samenvatting.pdf)
- [AI Act Omnibus agreement: Annex III high-risk obligations moved to 2 Dec 2027](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
