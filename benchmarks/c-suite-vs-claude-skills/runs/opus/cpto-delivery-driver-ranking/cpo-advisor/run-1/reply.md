━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CPTO ADVISOR: Driver leaderboard and weekly bottom-10% flag

**BOTTOM LINE**
Agree with Operations on the productivity goal and decline the design. Don't ship a live stops-per-hour leaderboard, and don't send a weekly bottom-10% list to subcontractors. Instead, share the target with Operations, run a two-week diagnostic, and after peak season run a randomized pilot of route-adjusted feedback plus fixes to the app and routing. Confidence: High that this design should not ship. Medium that the alternative gets close to 8%.

**WHAT**
- **Stops per hour mostly ranks routes, not drivers.** I ran a simple model that splits variation in stops per hour into 50% route, 20% driver and 30% weekly noise. Under that split, only about 3 in 10 drivers in a weekly bottom 10% are really among your weakest. About 8 in 10 are on the hardest quarter of routes, and a third of all drivers get flagged at least once a quarter. [ASSUMED: the variance split. Your own data will give the real numbers.] Confidence: Medium.
- **The 8% is unproven, and the flag would make it look true anyway.** In the same model, the flagged group "improves" by about 16% the next week with no intervention at all. That is regression to the mean: people picked out on a bad week usually have a more normal one next. The best study in favour of rank feedback found +6.8%, but there the feedback was private and had no consequences ([Blanes i Vidal & Nossol](https://personal.lse.ac.uk/blanesiv/tournaments.pdf)). When a US firm took rank displays away, sales went up, and the gain came mostly from low-ranked staff who had been giving up ([Barankay, Wharton](https://knowledge.wharton.upenn.edu/article/why-its-sometimes-better-not-to-tell-employees-where-they-stand/)). Confidence: Medium-High.
- **It rewards the wrong thing and puts pressure on drivers while they drive.** A "not home" scan counts as a stop, so stops per hour can rise while successful deliveries fall. A live ranking in the van is time pressure while driving, and EU-OSHA says time pressure raises crash risk ([EU-OSHA](https://eguides.osha.europa.eu/vehicle-safety/themes/speeding)). Couriers working to time windows say they speed to keep up ([UCL](https://www.ucl.ac.uk/news/2018/aug/gig-economy-drivers-and-riders-heightened-risk-traffic-collisions)). Confidence: High that this happens. Low on how big it is until you measure it.
- **The legal exposure is concrete, and the subcontractor part is the largest.**
  - Your own Dutch employees: the works council must consent to a system that monitors performance (WOR art. 27(1)(l)).
  - All drivers: systematic monitoring of employees needs a DPIA (data protection impact assessment, a formal privacy risk review). An automated weekly flag that costs drivers work also touches GDPR art. 22.
  - Subcontracted drivers: naming them to their own employer for action looks like you are exercising employer authority over people you don't employ. Belgium's Parcel Delivery Act expects you to monitor subcontractors without doing that ([DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/belgium-parliament-approves-new-legislation-on-delivery-activities)). In the Netherlands it pushes those contracts toward labour provision just as the Wtta licensing regime for labour providers starts on 1 January 2027 ([Rendement](https://www.rendement.nl/uitzendkrachten-gedetacheerden/nieuws/toelatingsstelsel-voor-uitleners-gaat-1-januari-2027-in.html)).
  - EU Platform Work Directive: transposition is due 2 December 2026, and parcel delivery is named as a likely affected sector. Whether you are in scope is a question for counsel ([Lewis Silkin](https://www.lewissilkin.com/insights/2026/11/13/the-eu-platform-work-directive-what-international-employers-need-to-know)).

  Confidence: Medium. General Counsel has not checked any of this yet.
- **Your biggest levers are in the product, not in a ranking.** They are seconds per stop in the app, load sequencing, address data and first-attempt success. Rough arithmetic: saving 10 seconds per stop at about 130 stops a day frees about 22 minutes, or around 4.5% of an 8-hour shift, and nobody has to drive faster. [ASSUMED: stops per day and shift length] Confidence: Low-Medium.

**WHY THIS MATTERS**
If the flag mostly measures routes and bad luck, subcontractors will drop drivers who aren't the problem, in a tight driver market, and replace them with slower new hires. The 8% will then show up on the dashboard but not in cost per delivered parcel. Meanwhile you build evidence that you are the real employer of about 1,600 subcontracted drivers.

**HOW TO ACT**
1. Reply to Operations. Back the goal, decline the spec, and propose a joint diagnostic and a Q1 pilot. Also agree that no new features that push driving pace go live during peak, from now to 4 January. A draft note is in the detail doc. → You → Wed 25 Nov
2. Ask where the 8% comes from: the source, the setting, whether there was a control group, which metric it measured, and whether it is net of failed deliveries. → Head of Operations → Fri 4 Dec
3. Run the diagnostic.
   - Split stops-per-hour variation across route, depot, parcel mix, stop density, driver tenure and the driver, using 6 to 12 months of data.
   - Check "not home" scans against GPS time at the address.
   - Do 15 to 20 ride-alongs across Dutch and Belgian depots.

   → Head of Data + driver-app product lead → Fri 11 Dec
4. Get a legal scope memo covering WOR art. 27, the DPIA, GDPR art. 22, the Platform Work Directive, and the subcontractor authority risk in the Netherlands and Belgium. Brief the works council early. → General Counsel + DPO → Fri 18 Dec
5. Run the pilot.
   - Design: randomize by depot, 8 to 10 weeks.
   - Primary metric: successful deliveries per route-hour.
   - Guardrails: first-attempt success, false "not home" scans, claims, complaints, safety events, working-time compliance and 90-day attrition.

   → Driver-app product lead + Operations lead → design by 8 Jan, start mid-January, readout end of March

**RISKS**
- The weakest point of this advice: if Operations has a controlled result behind the 8%, each week of delay costs real money. Action 2 checks that first.
- A plain "no" makes you the blocker. Operations may then get subcontractors to rank drivers from exported data anyway. Share the target, and control what driver data leaves your systems.
- Adding pace pressure during peak (now to New Year) raises incident risk exactly when volumes and fatigue are highest.
- The alternative may land below 8%. Knowing that is better than a number that only exists on a dashboard.

**YOUR DECISION**
- Option A: ship as specified. Fastest. Highest legal, safety and attrition risk, and the measured gain will be inflated.
- Option B: ship a softer version now, with a private ranking and no flag. Lower risk, but it still uses raw stops per hour during peak, and it still needs works council consent and a DPIA.
- Option C: decline the spec, share the target, diagnose in December, then pilot route-adjusted feedback plus app and routing fixes in Q1. About 8 weeks slower to start, and the only option that shows what actually works.
- Recommendation: C. It chases the same goal without paying for it in safety, driver trust and legal exposure.

**PEER CHECK:** Not done yet. General Counsel and the DPO need to check the legal points, Operations the 8% claim and the baseline, and the CFO the value of the gain and the cost of waiting.

**DETAIL:** `driver-productivity-response-detail.md` has the draft note to Operations, the model's numbers, the legal map, the metric design, the pilot design and sources.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
