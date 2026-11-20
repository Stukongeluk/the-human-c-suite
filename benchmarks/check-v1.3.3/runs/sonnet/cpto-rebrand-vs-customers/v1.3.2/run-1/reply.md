Plan Q1 as a split, not a choice: ship the rebrand in its smallest workable form, and ring-fence a named team for invoicing, the accounting integration and reports. Don't take "all of product and engineering on the rebrand" to the teams as it stands. NPS dropped 24 points (+28 to +4) while those three complaints stayed open, and a whole quarter spent on a new name does nothing for the customers who are unhappy.

**How I'd shape it**

1. **Agree with the CEO that a decision is needed, then make it a better one.** Leadership has decided the rebrand, fine. What is still open is how much of the organisation it takes and in what order. That is yours to propose.
2. **Split the rebrand by deadline.** Name in the app, new domain and marketing site probably have real dates (merger, contracts, legal). The design system is the biggest piece and the easiest to phase: new components for new work, old screens migrated over time. Ask which parts have a hard date and why.
3. **Protect the customer fixes with named owners.** Dedicate one or two teams to invoicing speed, the integration and the missing reports, each with a measurable outcome (invoice generation time, integration failure rate, report requests closed). Let the teams size the work first, then decide the split. Don't set the percentage before they have estimated.
4. **Sequence the domain move carefully.** Changing domains can break SSO, webhooks, OAuth redirects and email deliverability. Your accounting integration is probably one of the things at risk, so fix it before the migration, not after.
5. **Plan to real capacity.** Take unplanned work, on-call and leave out first, leave slack, and no overtime. If the two streams don't fit, cut rebrand scope or move the design system to Q2. Don't squeeze the teams.

**Before you go to the CEO, get three facts**
- How much churn and at-risk revenue ties to those three complaints (CRM, support tickets by cause)?
- What do the teams estimate for each stream?
- Which rebrand dates are fixed, and by what?

**The conversation.** Have it privately with the CEO first, before any wider meeting. Something like: *"I agree with the decision and I'll deliver it. These three issues account for X of churn and our NPS is down 24 points. I'd like to ship the rebrand on its dates and keep one team on customer fixes, with a checkpoint at week six. If the numbers show I'm wrong, I'll change course."* That keeps "leadership decides" intact, and it makes the trade-off visible instead of absorbing it quietly.

**Review rhythm.** Check NPS and complaint volume, churn, rebrand milestones, and team load and attrition every two weeks.

**Assumptions:** the complaints drive the NPS drop (not yet verified), and the rebrand has some flexible scope. What am I missing, and what would make this wrong?

I can turn this into a one-page Q1 plan or a draft note to the CEO if useful.
