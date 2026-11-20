**Short answer:** say yes to the tool and no to the plan as pitched.

Demand forecasting is worth having and will probably save real hours. But three parts of the pitch (schedules three days ahead, changing shifts on the day, all 140 stores by March) run into Dutch law, your cao, your works council and your peak calendar. And the 12% is the vendor's number; nobody has checked it against your stores. I'd propose a version that still gets the savings and holds up: run the forecast in shadow mode in every store now, pilot properly through Easter, decide in June, and roll out in waves so every store is live before the end of 2027.

I've put a one-page version you can send to the COO in `memo-to-coo.md`.

---

## Why the plan as pitched won't work

**1. Publishing three days ahead breaks your cao and the law**

- **The cao.** Both sector supermarket cao's (VGL/Supermarkten and Levensmiddelenbedrijf) say the full roster must be published **at least one full week** before it starts. If it isn't, staff only have to work their *structural* hours. They also say at least 50% of contracted hours are fixed structural time, fixed free time includes two evenings a week, and working in that free time is voluntary.
- **The Arbeidstijdenwet.** Changes to a work schedule need 28 days' notice unless the cao or an agreement says otherwise.
- **On-call staff (WAB).** You have to call them at least 4 days ahead. A cao can shorten that to as little as 1 day, and the supermarket cao's use 24 hours for unforeseen factors. If you cancel or change a call inside that window, you still owe the hours.

In practice: with three-day publishing, every hour beyond someone's structural hours becomes voluntary. If you trim a shift on the day, you pay for it anyway. If you add one, people can say no. So legally, "adjusting shifts on the day" is an app that offers open shifts to volunteers. That's useful, but it's not where 12% comes from.

**2. 15-minute matching runs into the youth rules and minimum-pay rules**

- Forecasting in 15-minute slots is fine. Building *shifts* out of 15-minute slots isn't. For small contracts, or contracts with no fixed hours, the law requires at least 3 hours' pay per call, so very short shifts don't save money.
- For 16 and 17-year-olds: no more than 9 hours a shift and 45 a week, **school time counts as working time**, and no night work or overtime. A pupil who has had a 7-hour school day can work 2 more hours that day. The vendor's engine won't know school hours unless you give it data about minors, and then you have to protect that data.
- Under the cao, nobody has to work more than two evenings a week, and shifts should be as continuous as possible.

**3. March isn't a responsible date**

- It's 20 November. Sinterklaas, Christmas and New Year come before March, and that peak is when you'd normally freeze changes. That leaves about 12–13 usable weeks to bring 140 stores live: 10–12 stores a week. Each needs manager training, staff app onboarding, integration with HR, payroll and time-and-attendance, and checked cao rules.
- **You need works council (OR) consent before you start.** Article 27(1)(b) WOR covers rules on working and rest times, and (k) and (l) likely apply too: processing personal data and monitoring staff. If you go ahead without consent and the OR invokes it, the decision is void. A consent request this big realistically takes 6–12 weeks, often with an outside expert paid by you.
- You need a **DPIA** before processing starts: 9,000 employees, many of them minors, processed systematically.
- **Easter is 28 March 2027.** The last March wave would go live right on the Easter peak.
- **Timing with the unions.** The sector cao expired on 1 April 2026. In early November the unions said the 16 November round would be the last if the offer didn't improve. I don't know how that round went. But announcing "AI cuts 12% of hours" in that climate hands the unions a campaign, and the headline writes itself: students losing hours to an algorithm.

**4. The 12% is a sales claim, not a forecast**

- Ask the vendor: 12% against what baseline? Measured how? In which country, under which labour rules? Reference customers in the US or UK can schedule in ways you can't.
- **Ask where the hours come from.** Rough illustration: if your 9,000 staff average 15 paid hours a week, that's about 7 million hours a year. 12% is about 840,000 hours. That's roughly the whole jobs of 1,000 students, or about 1.8 hours a week less for everyone. You can't cut contracted hours on your own. On-call staff with 12 months' service are entitled to an offer at their average hours. Under the cao, extra hours worked structurally lead to a bigger contract. So in practice the hours would come out of students' flexible hours. They would absorb the cuts.
- **Unstable schedules cost money.** In Gap's randomised trial, stable schedules raised median sales by 7% and labour productivity by 5%. Shift Project data finds that schedule instability is a strong predictor of staff leaving. Student turnover is probably already your largest hidden labour cost: recruiting, training and early mistakes. If schedule churn pushes attrition up by even a few points, it eats a large part of the saving.
- **A Dutch example.** Picnic built its own rostering app that combines partly fixed shifts, annual-hours contracts, staff availability, shift swaps and picking up last-minute shifts. It reports 5–15% less over-planning. The saving came from better matching *and* from giving staff control, not from cutting shifts on the day.

My guess, and it's only a guess, is that the figure you can reach within your rules is well below 12%, maybe around half. The pilot is how you find out.

---

## What I'd recommend instead

Present it to the COO as the same goal (labour productivity) with a version that actually delivers the savings.

### Phase 0: now to end of January

- **Don't sign a 140-store, March commitment.** Sign a pilot plus an option on the remaining stores at a locked price (terms below).
- **Run the forecast in shadow mode in all 140 stores.** Feed it POS, delivery, promotion and weather data. Compare its forecasts with actual sales and with the schedules managers actually made. Nobody's schedule changes and almost no personal data is involved, so there's little friction with the OR or GDPR (still tell the OR). Store by store, you learn where over- and under-staffing really is. That gives you your own evidence of how big the saving can be.
- **Get the rules engine right.** Load the working-time act, youth rules, WAB notice periods, minimum pay per call, cao terms and contract types, then test it against real rosters. Include the bandwidth contract that the *Wet meer zekerheid flexwerkers* brings in on 1 January 2028, so you only configure once.
- **Start with the OR now.** Share the plan, the pilot design and the guardrails, and ask for consent for the pilot. Treat them as co-designers. They'll know which features would make staff's lives easier, and a tool staff want is far easier to get consent for.
- Do the DPIA, the processor agreement and the AI Act classification (see vendor terms).

### Phase 1: February to May, a controlled pilot

- **8–12 stores** (urban and rural, large and small, some with many students), each matched to a **control store**. Run it through Easter and the May holidays so you see peak trading.
- **Guardrails:**
  - Publish schedules at least one full week ahead, as the cao requires; aim for two.
  - Forecast in 15-minute slots but build shifts in sensible blocks: at least 3 hours, no split shifts.
  - Protect structural hours; don't cut anyone's contracted hours.
  - On the day, offer open shifts to volunteers through the app. Don't cancel inside the notice window, and if you do, pay for it.
  - The store manager approves each schedule before it's published. Log and review overrides; they're useful signal, not failure.
  - Don't let shift allocation use behaviour or "reliability" scores for individuals.
  - Don't let the cost function quietly push hours to the youngest, cheapest staff. Get legal's view under the age-discrimination act (WGBL) and make that a deliberate decision.
  - Let staff enter their availability, swap shifts and see their hours balance.
- **What to measure against the control stores** (agree the thresholds with the COO up front):
  - Labour hours per euro of sales, or per scanned item
  - Sales, on-shelf availability, checkout queue times, complaints
  - Voluntary attrition (especially in the first 90 days) and sick leave
  - Schedule stability: share of hours changed after publication, changes made inside 24 hours, and how much each person's weekly hours swing
  - Compliance violations (target: zero) and payroll error rate
  - Time store managers spend on scheduling (often a real, overlooked gain)

### Phase 2: June, go/no-go

Go ahead if the productivity gain is meaningful and the customer and staff measures haven't worsened beyond the thresholds you agreed. Share the results with the executive team and the OR.

### Phase 3: rollout in waves

Roll out 20–35 stores per wave: one in June, a pause for the summer holidays, then September to mid-November. That gets every store live before the peak freeze, before the AI Act high-risk rules apply (2 December 2027) and before the flex-work law (1 January 2028). If the pilot is clearly working by week 8, start the first wave in May.

**The honest trade-off:** compared with a March big bang that goes perfectly, this gives up roughly half of the theoretical 2027 saving. That's about 600 store-months live in 2027 against about 1,260. But a perfect big bang isn't the realistic alternative. The realistic alternatives are a rollout the OR stops, one you roll back over Easter, or one that saves 12% on paper while attrition and empty shelves quietly eat the saving.

---

## Terms to get from the vendor

- **A pilot plus an option** on the remaining stores at a locked price, with the option open until about the end of September. The March deadline is the vendor's quarter, not yours, so use it as leverage.
- **Part of the fee tied to measured savings** against the control stores, using your data and your method.
- **Proof it handles Dutch rules:** Dutch supermarket references under these cao's; youth rules including school time; WAB notice periods; minimum pay per call; 2028 bandwidth contracts.
- **The AI Act.** Get a written position on the classification. Annex III point 4 covers AI used for decisions that affect the terms of work relationships, to allocate tasks based on individual behaviour or traits, or to monitor performance. After the Digital Omnibus, the high-risk obligations apply from 2 December 2027. As the employer deploying it, you'd need human oversight by trained people, logs kept for at least six months, and you'd have to inform the OR and affected workers before putting it into service. Your contract will run past that date, so build it in now.
- **GDPR:** EU hosting, a list of sub-processors, help with the DPIA, safeguards for minors' data, and only the data it needs.
- **Your data and forecasts stay yours:** full export, API access and help with exit.
- **An SLA and an offline fallback** for the store app, so a scheduler outage can't stop a store from running.
- **Explanations:** managers and staff can see why a schedule looks the way it does.

## Technical points to check yourself

- **Forecast inputs.** How clean is your 15-minute POS history per store? Do you have a reliable promotions calendar? Do you have delivery times? Shelf-filling follows the trucks, not the customers, and a large share of supermarket hours isn't checkout work.
- **Labour standards.** The forecast is turned into hours using labour standards: minutes per case, per customer, per online order. If those are wrong, the schedule is precisely wrong.
- **Integration.** HR master data (contracts, dates of birth, availability), time and attendance, and payroll, including evening and Sunday allowances. Payroll errors are the fastest way to lose staff trust.
- **Identity and access** for about 9,000 staff on a mobile app, many of them minors.

## How I'd put it to the COO

"I want this to work, and I think the plan as pitched is the most likely way to make it fail. Here's a version that gets us the saving on evidence, without a fight with the works council or a meltdown at Easter. The March deadline is the vendor's quarter, not ours."

**Caveats.** This isn't legal advice. Which cao applies to you (VGL/Supermarkten, Levensmiddelenbedrijf or a company cao) and how the current negotiations end both matter. Have HR and your employment lawyer confirm the rules before anything is configured. I also don't know how mature your scheduling is today. If stores roster from spreadsheets, the gain may be bigger; if you already run a decent workforce-management system, smaller.

---

**Sources**

- Supermarket cao rostering rules: [cao Levensmiddelenbedrijf 2025/2026 (Stcrt. 2025, 14579)](https://zoek.officielebekendmakingen.nl/stcrt-2025-14579.pdf); [cao Supermarkten VGL (FNV)](https://www.fnv.nl/getmedia/18c9c6e7-339c-46d3-963e-af97eb245d25/608-Supermarkten-VGL-cao-Grootwinkelbedrijven-Levensmiddelen-2020-2023-v291221.pdf)
- State of the cao talks: [FNV, 2 November 2026](https://www.fnv.nl/nieuwsbericht/sectornieuws/handel/2026/11/cao-bod-werkgevers-supermarkten-blijft-onvoldoende); [CNV, December 2025](https://www.cnv.nl/handel/detailhandel-food/nieuws/update-caos-supermarkten-2025-12-22/)
- On-call rules (WAB, 3-hour minimum, 12-month offer): [Ondernemersplein: regels voor oproepkrachten](https://ondernemersplein.overheid.nl/wetten-en-regels/regels-voor-oproepkrachten/)
- 28-day schedule notice: [Ondernemersplein: werktijden](https://ondernemersplein.overheid.nl/werktijden/)
- Rules for 16 and 17-year-olds: [Rijksoverheid](https://www.rijksoverheid.nl/vraag-en-antwoord/bijbaan-vakantiewerk-en-stage-door-jongeren/hoeveel-uur-werken-16-17-jaar)
- OR consent for rosters: [Rendement, art. 27 WOR](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/geen-uitbreiding-rooster-zonder-instemming.html)
- Flex-work law, 1 January 2028: [CMS](https://cms.law/nl/nld/legal-updates/de-eerste-kamer-akkoord-de-wet-meer-zekerheid-flexwerkers-is-een-feit); [Ondernemersplein](https://ondernemersplein.overheid.nl/nulurencontracten-niet-meer-toegestaan/)
- AI Act: [Article 26, deployer obligations (EC AI Act Service Desk)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26); [Annex III employment uses (Eversheds Sutherland)](https://www.eversheds-sutherland.com/en/global/insights/eu-ai-act-high-risk-ai-systems-in-employment); [Digital Omnibus in force, high-risk date moved to 2 December 2027 (Lewis Silkin)](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo)
- Evidence on schedule stability: [Gap stable-scheduling RCT (UChicago)](https://news.uchicago.edu/story/stable-scheduling-increases-sales-and-employee-productivity-study-finds); [Choper, Schneider & Harknett, schedule instability and turnover (Harvard Kennedy School)](https://www.hks.harvard.edu/publications/uncertain-time-precarious-schedules-and-job-turnover-us-service-sector); [Picnic's rostering app (AWVN)](https://www.awvn.nl/roosters-en-werktijden/publicaties/roosterapp-picnic-inkomenszekerheid-en-flexibiliteit/)
