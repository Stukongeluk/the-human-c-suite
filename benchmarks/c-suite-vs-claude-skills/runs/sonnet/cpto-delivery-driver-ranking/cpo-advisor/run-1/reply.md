# Response to Operations: live stops-per-hour leaderboard and weekly bottom-10% flag

## Bottom line

Do not ship it as specified. Say yes to the goal (productivity) and no to the mechanism (a raw, live, ranked stops-per-hour board plus an automatic weekly bottom-10% flag sent to subcontractors). Counter-propose a 6-8 week controlled pilot of a route-adjusted, private-to-the-driver feedback tool with quality guardrails, and let the pilot decide whether anything ranked ever goes live.

Confidence tags: [verified] = follows from the facts you gave or from how the metric is built; [medium] = well-supported but I have not seen your data; [assumed] = needs checking with Legal or your data.

## What I would tell Operations (and why)

**1. The 8% figure is a hope, not a forecast. [verified: no evidence was offered; medium: that it is optimistic]**
Ask where it comes from. If it comes from another carrier or from a general "leaderboards motivate people" claim, it does not transfer to a workforce that is two thirds subcontracted, where you do not set pay, scheduling or discipline. Ask what it is net of: more failed first attempts, damage, complaints, accidents and driver churn all cost money. A gross 8% in stops per hour can be a net loss.

**2. Stops per hour mostly measures the route, not the driver. [verified]**
It depends on stop density, parcels per stop, building type (apartment blocks vs rural addresses vs B2B), access and parking, time windows, parcel size and weight, vehicle, weather and traffic, and how the route was planned. Your own dispatch and routing decides most of those. Ranking drivers on the raw number will rank them largely on the routes they were given. If the bottom 10% each week turns out to be the same people on the hardest routes, you will be penalising your planning.

**3. A bottom 10% is a rank, not a standard. [verified]**
Ten percent of drivers (about 240 people) will be in the bottom decile every single week, however good the whole fleet is. It will flag people who are doing fine, and it creates pressure to keep ratcheting up. The proper question is "who is below a defined, route-adjusted standard, for how long, and why?", not "who is last?".

**4. You will get exactly what you measure. [verified for the mechanism; medium for the size of effect]**
Drivers optimise the number they are ranked on. Expect: skipping or rushing doorstep attempts, "delivered" scans that are not real deliveries, parcels left in unsafe places or with neighbours, parking illegally, cutting breaks, speed and phone use while driving, and cherry-picking easy stops where drivers can reorder. Each of those lands on your customer experience, claims cost, road safety and brand, not on the subcontractor's. A leaderboard that is live in the app, while the driver is driving, makes the safety point worse. I would not accept any live in-drive ranking.

**5. The subcontractor structure makes this riskier than it looks. [medium; confirm with Legal]**
- *Employment-law exposure.* You are not the employer of two thirds of these drivers. If your app ranks them, and you push weekly "bottom 10%" lists that trigger action by their employer, that looks like you directing and assessing the work. That is the kind of control that courts and authorities look at when deciding who the real employer is, or whether the subcontracting is genuine (chain liability, labour-hire and bogus-contracting rules in both NL and BE). Legal should confirm this before anything is built.
- *Privacy and works council.* Individual performance monitoring and sharing it with a third party needs a lawful basis, purpose limitation, a data protection impact assessment, and clarity on who is controller vs processor. Under GDPR, decisions with significant effects based solely on automated processing are restricted, so a flag must not automatically trigger dismissal or loss of work. In NL, systems that monitor employees generally need works council consent at the employer (the subcontractor), and Belgium has its own collective agreements on monitoring. Some subcontractors will have works councils; they may block it, and you will have shipped something you cannot switch on in half the network.
- *Rules on algorithmic management.* EU rules on algorithmic management in platform work are being transposed in 2026 and are a direction of travel even if you are not strictly in scope. [assumed: scope; ask Legal]
- *Subcontractor relationship.* A weekly list that names their drivers is a stick in a tight labour market. Good subcontractors will see it as interference or will lose drivers; weak ones will use it to churn drivers, which then hits your quality.

**6. There are better levers for the same goal. [medium]**
Route quality, stop sequencing, failed-attempt reduction, depot loading order and wait times, access problems and address data, and app friction (scan time per stop, navigation hand-offs) typically hold more productivity than pressuring individual drivers. A few of these can be measured directly from your data in days.

## What I would propose instead

**A. Fix the metric before anyone is compared. [verified as design]**
- Route-adjust it: compare actual vs expected time for the same route, based on stop count, parcels per stop, stop type, distance and time windows. Report "% vs expected", not raw stops per hour.
- Pair it with quality in the same view: first-attempt delivery rate, claims/damage, customer complaints, safety events. No productivity number is ever shown without them next to it.
- Use rolling 4-8 week windows, not single weeks, so one bad route or one sick day does not flag someone.

**B. Feedback, not ranking. [medium]**
- Each driver sees their own trend and their own route-adjusted figure, privately, outside driving time (end of shift or a weekly summary). No live board, no public ranking.
- Depot or subcontractor-level benchmarks (team vs team) for managers, with the drivers' individual data staying with the driver unless there is a clear, lawful, agreed purpose.
- If a driver is persistently far below the adjusted standard, the subcontractor gets a prompt to have a conversation and look at causes first (route, vehicle, training, access problems), not a "bottom 10%" list. A human decides, not the app.

**C. Test the 8% claim properly. [verified as method]**
- Pilot in a few depots across both countries, with matched comparison depots that do not get the tool, for 6-8 weeks. Pre-register what success means.
- Primary measure: route-adjusted productivity. Guardrails that must not get worse: first-attempt success, damage and claims, complaints, accident and near-miss rate, driver attrition and subcontractor attrition, scan-integrity checks (delivered scans without matching location or time).
- Decide up front: if the guardrails move the wrong way beyond a set threshold, we stop.
- Cost: a few weeks of one product trio plus analytics, and the Legal/DPIA work, which has to happen anyway.

**D. Do the legal and works-council groundwork in parallel. [verified as dependency]**
Legal reviews the employer/control question, GDPR basis and DPIA, and the works-council position in NL and BE before the pilot touches named drivers. Pick pilot subcontractors that are willing, so you learn how they would use the data.

## What I need from Operations before we commit

1. The source and the calculation behind "8%", and over what period.
2. Current baselines: stops per hour by route type, first-attempt rate, claims, complaints, accidents, driver turnover, by subcontractor.
3. How much of the variation in stops per hour is explained by route and stop mix. We can check this in days from existing data. If, say, most of the variation is route, the leaderboard is measuring planning.
4. What action they expect subcontractors to take on a flagged driver, and what the subcontractors' contracts allow.

## Your decision

Choose one:
1. **Recommended:** reply "yes to the goal, not to this design", propose the pilot above, and ask for the data in the list. Timeline: baseline analysis in about 2 weeks, pilot design in about 4, pilot running about 6-8 weeks after Legal sign-off.
2. Ship a reduced version now: private per-driver feedback only, no ranking, no flags to subcontractors. Lowest risk, but you learn less about impact.
3. Ship as asked. I would not, for the legal, safety and quality reasons above. If you are overruled, at minimum: no live in-drive display, route-adjusted metric, quality metrics shown alongside, a human review step before any action, Legal sign-off first, and a rollback trigger on the guardrail metrics.

## Draft message you can send to Operations

> Thanks. I want the productivity gain and I think there is real upside in this data. I do not think a live raw stops-per-hour leaderboard with an automatic weekly bottom-10% flag to subcontractors is the way to get it. Stops per hour mostly reflects the route we assign, so it would rank our planning as much as our drivers; a bottom 10% exists by definition every week; and a ranked, live number invites rushed and unsafe deliveries that cost us in claims, complaints and risk. Because two thirds of the drivers work for subcontractors, we also have employment-law, GDPR and works-council questions to clear first.
> Instead, let's run a 6-8 week pilot in a few depots: a route-adjusted productivity view shown privately to drivers, with quality and safety guardrails, compared against matched depots without it. If it delivers a net gain, we scale it, and we can then decide what is appropriate to share with subcontractors. Can you send me the basis for the 8% and the current baselines by route type and subcontractor so we can size it this week?

## Caveats

I have not seen your data, contracts or legal advice. The legal points are flags for Legal to confirm, not conclusions. The effect sizes are directional: the pilot exists to measure them.
