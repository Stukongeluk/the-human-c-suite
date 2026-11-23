I'm not going to build a performance-plus-Copilot scoring formula for the 60. This isn't a matter of preference. In a Dutch economic redundancy it's not a lawful way to select people, and using it would put the whole March timeline at risk.

**Why it fails, in brief:**
- **UWV and the unions see it on day one.** The collective-redundancy (WMCO) notification and the OR advice request both have to state your selection method. UWV checks every permit application against the legal order (the afspiegelingsbeginsel) and refuses applications that deviate from it. Its own implementation rules say the "indispensable employee" exception gives no basis for sparing someone because they perform better in the employer's view.
- **Termination agreements don't get around it.** Anyone you select by score can refuse to sign, and then you have no legal route to end their contract.
- **Last year's ratings can't be used retroactively.** The only performance rule that exists (art. 16 Ontslagregeling) can only spare above-average performers. It can't be used to select the lowest scorers. It also requires a CAO that provides for it, staff told in advance that performance could count in selection, regular assessments, and equal development opportunities for everyone.
- **Copilot data is the weakest part.**
  - It measures how much people use a tool, not what they deliver.
  - It hits part-timers, people on leave or sick leave, and roles where Copilot isn't relevant or allowed. That is a ready-made indirect discrimination claim.
  - Using it to judge staff needs the OR's consent under art. 27(1)(l) WOR, plus a lawful purpose under the GDPR. Staff were never told their usage data could be used this way.

## The selection criteria and formula that do hold up

For each function category where positions disappear (reduction *R*):

1. **External workers first.** Contractors, agency staff and secondees in that category go first: remove up to *R* of them. The rest, *R′*, comes from employees.
2. **Count per age band.** Count the employees in the category in each age band (15–25, 25–35, 35–45, 45–55, 55+). That gives *nᵇ* per band and *N* in total.
3. **Quota per band.** The quota is *qᵇ* = *R′* × *nᵇ* / *N*, without rounding. Each band first gets its whole number. Any dismissals still to place go to the bands with the highest decimal.
4. **Within each band:**
   1. First, employees at state pension (AOW) age, on-call workers, and fixed-term contracts ending within 26 weeks of UWV's decision.
   2. Then permanent staff, **shortest service first**.
5. **Protected or exempt cases.** If the selected person is protected (sick, pregnant, an OR member) or exempt (documented indispensable knowledge, work-limiting disability), the next person in the same band is selected instead.

**Example:** "Medior backend developer", 30 people, 5 positions go.
- 25–35: 15 people, quota 2.50, 2 go.
- 35–45: 10 people, quota 1.67, 2 go (after the remainder).
- 45–55: 5 people, quota 0.83, 1 goes (after the remainder).

In each band, the most recent hires are selected.

I've added the formula and this worked example to **plan-60-positions.md**, section 4.

## Where your judgment legitimately counts

- **In the organisation design, not the names.** You decide which work the company needs from here on, and therefore which function categories shrink, grow or disappear. If a capability isn't needed, that category can go. What doesn't hold is drawing category boundaries around particular individuals; UWV looks for that.
- **Real underperformance is a separate, individual track.** It needs a documented improvement plan and a genuine chance to improve. It takes months and isn't part of the 60.

Next, I can build the selection calculation as a spreadsheet for HR and your lawyer. They load the headcount data, and it produces the per-category lists, with a check for skew by gender, nationality and part-time status.
