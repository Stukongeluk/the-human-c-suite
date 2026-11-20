# Driver productivity: how we get to the 8%

**To:** [Head of Operations]
**From:** [CPTO]
**Date:** [date]
**Status:** draft for discussion

Thanks for walking me through the proposal. Here is where I land, so we can decide together.

## Where we agree

- Stops per route-hour drives cost per parcel and peak capacity, and an 8% gain is worth chasing. [Add Operations' value estimate: € per year, or routes saved at peak.]
- Drivers want to know how their day went, and the app should help them do a good day's work.

## What I don't want to build, and why

I don't want to build the public stops-per-hour leaderboard or the weekly list of the bottom 10% sent to subcontractors, as specified:

1. **The list never shrinks.** A bottom 10% always exists: 240 named drivers every week, about 160 of them employed by subcontractors, however well the fleet performs.
2. **It mostly ranks routes.** Stop density, flats versus houses, parcels per stop, van loading order and familiarity with the route drive stops per hour more than effort does. If weekly rank is mostly noise, 99.6% of drivers would be flagged at least once a year; if it is mostly route, the same rural routes and new drivers are flagged every week.
3. **The number can rise while the business gets worse.** The fastest ways up a public ranking are "not home" scans, parcels left unattended and faster driving. Those show up as redeliveries, complaints, claims and road incidents, and as turnover among drivers we already struggle to replace. New drivers start at the bottom of the list.
4. **Legal and contractual risk.** To be confirmed by employment counsel and our DPO before we build any per-driver feature:
   - *Netherlands:* a system suited to monitoring performance needs works council consent (article 27(1)(l) WOR), and systematic monitoring of workers requires a data protection impact assessment.
   - *Belgium:* the works council must be informed and consulted on new technology with collective consequences (CAO/CCT no. 39), and the same GDPR questions apply.
   - *Subcontractors:* sending named drivers to their employer to act on can look like we exercise employer authority over their staff. In the Netherlands that can recast subcontracting as the supply of labour; in Belgium it can make us the deemed employer under the rules on making workers available (Law of 24 July 1987).

## What I propose instead

| Step | What | Who | When |
|---|---|---|---|
| 1. Find where the minutes go | From scan, GPS and app event data we already collect, aggregated per depot and route type, never per named driver: time at the stop, time searching the van, failed delivery attempts, taps per delivery, late depot departures. Ride along on 10–15 routes, own and subcontracted, to see what the data misses. | Product, Operations, two depots | January, weeks 1–3 |
| 2. Fix the top three causes | Likely candidates: loading sequence that doesn't match stop order, address and access data for flats, app friction at the door, route sequencing, not-home rates (customer notifications, safe places, pickup points). | Product and engineering with Operations | Weeks 4–10 |
| 3. Private feedback for drivers | Each driver sees their own day and trend on comparable routes; no ranking and no comparison with named colleagues. Visible only to the driver and not used for performance management. Designed with drivers, our works councils and subcontractor representatives, after the legal checks. | Product, HR, works councils | Design in Q1 |
| 4. Subcontractor performance on outcomes | Per subcontractor, route and depot: on-time delivery, first-time delivery rate, complaints, damage and incidents, managed through the contract. Subcontractors manage their own people. | Operations, Procurement | From Q1 |
| 5. A fair test | 4–6 pilot depots against matched comparison depots for 8–10 weeks. | Operations and Product | January to March |

Nothing new goes into the driver app during peak.

## How we'll know it worked

Agreed before the test starts, and reviewed together every two weeks:

- **Primary:** stops per route-hour, adjusted for route type, pilot depots against comparison depots.
- **Must not get worse:** first-time delivery rate, complaints and claims, road incidents and harsh-driving events (aggregated), injuries, and driver turnover and absence at our depots and subcontractors.
- **Decision rule:** if pilot depots beat comparison depots by [X]% with the guardrails flat, we roll out depot by depot. If they don't, we look again together, including at your proposal.

## What would change my mind

- A controlled test, ours or a credible external one, that shows a route-adjusted gain from ranking with first-time delivery, complaints and incidents flat.
- Drivers and their representatives asking for comparative feedback themselves.

## Questions for you

1. What is the 8% based on: a pilot, another carrier, a vendor's figure?
2. Which problem matters most right now: cost per parcel, peak capacity or late deliveries?

## Next steps

- **This week:** agree the problem and the target, and share the source of the 8%.
- **Before January:** legal check with counsel and the DPO; inform the works councils in the Netherlands and Belgium while the plan can still change; choose pilot and comparison depots.
- **January to March:** steps 1, 2 and 5, with a joint review every two weeks.

Tell me where this is wrong. If your version wins a fair test, I'll say so.
