# CEO Advisor: selection criteria for the 60

## Bottom line

I won't build a performance-plus-Copilot ranking for the 60. In the Netherlands it can't legally select people for an economic redundancy, so it would stall the plan and put the 31 March date at risk. Below are the criteria and formula that will hold up, and the places where performance can legitimately count. Confidence: high.

## Why that formula fails in practice

- **UWV doesn't accept it.** For a business-economic dismissal, UWV (the state employment agency that grants dismissal permits) uses three criteria: group, age band and length of service. Performance isn't one of them. Anyone selected on scores who doesn't sign an exit agreement can't get a UWV permit. [Verified: UWV]
- **You'd have to write the method down for the unions and the works council.** The collective dismissal notice to UWV and the unions must state the selection method. So must the request for advice to the works council (OR). Writing "last year's ratings plus Copilot usage" there hands both of them the case against you. [Verified for the UWV notice: CMS. Medium for the OR request]
- **Using the method only for exit-agreement offers doesn't fix it.** People offered an agreement can refuse it. Those who refuse can't be dismissed through UWV. Ratings and Copilot use also tend to track part-time work, leave, age and disability, which opens you to discrimination claims. [Medium]
- **Copilot data brings separate problems.** It was collected to run a tool, not to judge people, so using it this way breaks GDPR's purpose-limitation principle. Using it to monitor individual performance also needs the OR's consent (art. 27 WOR). And it measures how much someone uses the tool, not what they deliver. [Medium]

## The selection criteria and formula that hold up

Run this for each role category *c*, where a category groups interchangeable roles (similar work, skills, level and pay) at one location:

1. **P_c** = the number of positions removed in *c*, taken from the stop list.
2. **External contractors go first.** Remove the E_c contractors in *c*. The places left for employees are **R_c = P_c − E_c**. If R_c ≤ 0, no employee in *c* is affected. [Verified: UWV]
3. **Split R_c across the five age bands** (15–25, 25–35, 35–45, 45–55, 55+) in proportion to each band's share of the employees in *c*: **r_b = R_c × (n_b ÷ n_c)**. Round so the totals add up to R_c; your lawyer applies UWV's rounding. [Verified: UWV for the method; Medium for the rounding]
4. **Within each band, rank people in this order:**
   1. employees past state pension (AOW) age
   2. zero-hours staff
   3. fixed-term contracts ending within 26 weeks of the UWV decision
   4. permanent staff, by start date, latest first

   The first r_b people on that list are selected. [Verified: UWV for the groups and for latest-hired-first. Medium for the group order inside each band; your lawyer confirms]
5. **Remove exceptions.** Take out anyone with dismissal protection, or with documented indispensable knowledge. The next person in the same band takes their place. [Verified: UWV]
6. **Allow swaps.** A volunteer in the same category and band may take a selected colleague's place (*plaatsmaker*). [Medium]

**The individual "score" is the start date within the age band.** The legal order needs no other score.

## Where performance can count

- **Which work stops.** You choose the positions by what work is going, not who does it. Categories can't be drawn around named people.
- **The indispensability exception.** Use it person by person, with documents showing critical knowledge. It is narrow, and it can't become a ranking of the whole company.
- **Volunteers.** The voluntary scheme lets you refuse volunteers whose skills you need.
- **A separate performance track, outside the 60.** For real underperformers, use an improvement plan, or have an honest exit conversation that names performance as the reason. Never present it as a redundancy.
- **Copilot data.** Use it for team-level adoption insights only, never in individual decisions.

## How to act

1. Run the formula on the HR census and send the draft selection to the lawyer → HR → Fri 4 Dec
2. List candidates for the indispensability exception, with the reason and evidence for each → exec team → Thu 3 Dec
3. List genuine underperformers for a separate improvement process starting in January, outside the 60 → managers and HR → Fri 11 Dec
4. Exclude the Copilot usage data from every people decision in this process → you → now

This extends section 3 of `reduction-plan-60-v0.2.md`. Everything else in the plan stays as it is.
