Plan Q1 around the three customer problems first, and shrink the rebrand to the part the merger genuinely needs: the name in the app, legal entities, redirects and a basic marketing page. The design system, the full marketing site and the polish move to Q2. NPS dropping from +28 to +4 while invoicing, the accounting integration and reports sit open for months is the signal that matters most, and a new name doesn't fix an unhappy customer. Customers who leave over a slow invoice don't come back because the logo changed.

This isn't "decision vs. no decision". Your CEO is right that a decision beats drift on things that are cheap to undo. The rebrand's scope is cheap to adjust (phasing it costs a quarter, not a company). A badly rushed Q1 for every team is the expensive-to-undo part, because churn and regretted leavers are hard to reverse. So the decision to take to leadership is not "rebrand or not", but "how much of the rebrand is must-have in Q1".

**A Q1 shape I'd propose (to be sized by the teams, not by me)**

1. **Customer fixes get named owners and dedicated capacity.** One team or squad each for invoicing speed, the accounting integration and the missing reports. Each has an outcome, a measure and a date, for example: invoice generation time at p95, integration failure rate and support tickets about it, and the number of customers who asked for each report. Pull these from your analytics, support and CRM data.
2. **The rebrand gets a must-have list, with an owner.** Name in the app, legal and billing entities, domain redirects and email, and a minimal marketing page. Everything else (the new design system, the full site, deep UI restyling) is phased later, with a decision date.
3. **Health work is in the plan.** Reliability, tech debt and the on-call load stay visible, not "if there's time". Leave slack: teams planned at 100% have no room for incidents.
4. **Overlap is sequenced, not stacked.** Avoid the same team being the bottleneck for both the rebrand and a customer fix. Check which team is most loaded and whether it is also the least healthy.

**Before you commit anything, ask the teams for three numbers**

- What capacity is really left for roadmap work, from their own past throughput, minus unplanned work, on-call and incidents?
- What is the smallest version of each customer fix that moves the metric?
- What does the must-have rebrand actually cost? Teams often find this is far smaller than the full programme, and also find hidden work: a domain change can break OAuth callbacks, webhooks and partner listings for your accounting integration, and affects email deliverability and search ranking. That is a reason to put the integration owners in the rebrand planning from day one.

If the sum exceeds capacity, cut scope first, then sequence to Q2, then remove in-flight low-value work. Don't close the gap with overtime or skipped testing and security review.

**How to take this to the CEO**

Don't open with "the rebrand is wrong". Bring a one-page decision record: the problem (NPS +28 to +4, three open complaints, revenue at risk), two or three options (full rebrand in Q1; must-have rebrand plus customer fixes; customer fixes only), the cost and risk of each, and what would change your mind. Ask for a short window, a week or so, for the teams' input before the final call. That fits "leadership decides" while still using what the teams know. Ask in a private conversation first, then in writing. Find the real reason for the Q1 deadline too: a contractual date, a trade show, a legal requirement or the integration of two customer bases? If a date is real, the must-have list protects it. If it is only momentum, say so gently.

Two questions that would change my answer:

- What is the revenue at risk behind those three complaints (churned or at-risk accounts, renewals in the next two quarters)?
- Is any part of the rebrand fixed by a hard date or contract?

If your company has a works council (mandatory in the Netherlands from 50 employees), a change this size to how teams spend a quarter may also need its advice early; worth checking with HR. This is not legal advice.

My assumptions: the three complaints are the main driver of the NPS fall (I haven't seen your NPS comments or churn reasons), and the merger really needs one name soon. What am I missing, and what would make this wrong?
