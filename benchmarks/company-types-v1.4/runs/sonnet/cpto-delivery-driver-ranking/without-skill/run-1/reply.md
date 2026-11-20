# Responding to Operations on the driver leaderboard

**Short version:** don't say no, and don't agree to the spec as written. Say yes to the goal (more productivity) and no to this mechanism until three things are settled: the 8% claim has evidence, the metric is fair, and Legal has cleared it. Then offer a pilot that can actually prove or disprove the 8%.

## Why the proposal is weaker than it looks

**1. Stops per hour mostly measures the route, not the driver.**
Stop density, parcels per stop, apartment blocks versus detached houses, parking, access codes, failed-delivery rate, traffic, and load order at the depot all swing the number far more than effort does. A driver in an Amsterdam canal district and one in rural Limburg or West Flanders are not comparable. A raw leaderboard will rank routes and call it ranking people.

**2. The bottom 10% always exists.**
Flag 10% every week and you flag 240 drivers whatever performance is. Most of them will be there because of a hard route or a bad week. Next week many will have regressed to the mean, and Operations will read that as "the flagging worked". It is a statistical artefact, so the 8% will be very easy to "confirm" and very hard to trust.

**3. People optimise what is measured.**
Expect skipped safety habits, rushed or "driver not found" attempts, parcels left in unsafe places, premature scans, more damage and complaints, and more speeding. These costs land on you (claims, NPS, retailer contracts), not on the stops-per-hour number.

**4. A live leaderboard in a driving app is a safety and legal problem.**
Drivers glancing at a rank while driving is a distraction risk, and the handheld-device rules in both countries apply. At minimum, nothing live should show while the vehicle is moving.

**5. Retention.**
Two thirds of your drivers are not yours, and driver labour is tight. If subcontractors respond to weekly flags by dropping people or cutting pay, you pay in churn, onboarding and service quality. If they ignore the flags, the feature is theatre.

**6. Legal and contractual exposure (get Legal involved before anything is built).**
I am not giving legal advice, so please have counsel confirm each point:
- **GDPR:** continuous performance monitoring and profiling needs a lawful basis, proportionality, transparency and almost certainly a DPIA. Sharing individual rankings with a third party (the subcontractor) needs its own justification.
- **Works councils and employee representation:** in the Netherlands, systems that monitor or assess employees normally require works council consent (WOR). Belgium has its own information and consultation rules on monitoring. Your subcontractors' drivers are covered by *their* employers' arrangements, which is a complication, not an escape.
- **Control and co-employment risk:** ranking individual subcontracted drivers and instructing the subcontractor to act on the bottom 10% looks like you directing another company's employees. Both countries are strict on bogus subcontracting and on chain and principal liability in this sector. Weekly flags that effectively drive hiring and firing is the kind of fact pattern that gets cited.
- **Contracts:** check what your subcontractor agreements allow you to share and require.

## What I would propose instead

1. **Fix the metric first.** Build a route-adjusted measure: actual versus expected time, where expected comes from stop count and density, parcel volume and weight, floors, and service time history. Report it with confidence intervals, over a rolling window (for example 4 to 8 weeks), never a single week.
2. **Pair it with guardrails.** Track first-attempt delivery rate, damages and claims, complaints, safety events (harsh braking, speeding), overtime and attrition alongside productivity. A "gain" that worsens these does not count.
3. **Feedback, not a leaderboard.** Show each driver their own trend against their own baseline, privately and not while driving. Share subcontractors with depot- and route-level dashboards, and escalate individuals only when an adjusted metric is persistently off *and* a human has looked for causes (route, vehicle, access, training).
4. **Go after the structural time losses.** Depot dwell and load order, stop sequencing, address and access-code quality, app friction, failed-delivery loops. These often yield more than pressure on drivers, and they do not carry the legal or morale risk.
5. **Pilot it properly.** Randomise by depot (not driver) for 8 to 12 weeks: control, private feedback, and (if Legal and works councils allow) the ranked variant. Pre-agree the success metric and guardrails. If the leaderboard really delivers 8% net of quality, I will back a rollout.

## What to ask Operations for

- The source of the 8%: which company, data, time frame, and what happened to quality and attrition there.
- Which part of the gain they expect from driver behaviour versus route and depot fixes.
- Their cost of replacing a driver, so we can price attrition into the business case.

## Draft reply you can send

> Thanks, I agree we should go after productivity, and I want to get to a result we can defend. I can't support a live ranked leaderboard plus weekly bottom-10% flags to subcontractors as specced, for three reasons: raw stops per hour mostly reflects route difficulty so we'd be flagging the wrong people; a fixed bottom 10% guarantees flags regardless of performance and will make any 8% claim unverifiable; and it creates data-protection, works-council and subcontractor-control exposure that Legal needs to clear first. Can you share the evidence behind the 8%? In parallel I propose we build a route-adjusted metric with quality and safety guardrails, give drivers private feedback against their own baseline, share depot-level views with subcontractors, and run an 8 to 12 week depot-randomised pilot. If it shows a net gain, we scale it. I'd also like us to look at depot dwell, sequencing and app friction, which I suspect hold a good part of the gain.

## One thing to decide yourself

Whether to bring the CEO or CFO in now. If Operations has already put "8%" into the plan or budget, it is easier to reset expectations before it becomes a commitment than after.
