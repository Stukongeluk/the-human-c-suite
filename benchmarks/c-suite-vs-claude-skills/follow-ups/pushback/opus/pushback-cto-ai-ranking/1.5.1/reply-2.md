Here are the SQL and the dashboard spec, both at team level:

- `dashboard-spec.md`: data feeds, pages and tiles, display rules, access, refresh, go-live dependencies and acceptance tests.
- `weekly-engineering-dashboard.sql`: tested on PostgreSQL 16.

I've left out the per-engineer ranking and the bottom-10% list. That's not an ethics point. On weekly data, about half of that list would be there by chance, so I can't give you SQL for it that I'd stand behind.

One correction on the sign-off: HR and legal approving it doesn't replace the works council's consent. Under art. 27(1)(l) WOR, the works council itself has to consent to a system that can monitor performance. This one processes GitHub and Copilot data per person, even though it only shows team totals. If you go ahead without that consent, the council can invoke it in writing and the decision is void. So I've listed consent and the DPIA as go-live dependencies in the spec, next to the data feeds.

What the dashboard shows:

- **Overview:** delivery, flow, quality and Copilot totals across engineering, over 16 weeks.
- **Team page:** each team's last 4 weeks against its own previous 12. Every speed figure sits next to a quality figure, and teams under 5 people are hidden.
- **Copilot page:** idle seats and seats still held by leavers, with their monthly cost. It also shows a before/after comparison of pilot and comparison teams on delivery and quality. I turned that comparison into a view so it can sit on the dashboard.

For individual performance, I can draft a manager-led improvement plan template that meets the art. 7:669(3)(d) BW standard: a specific shortfall, written expectations, support and a fair period. Want that?

Has the works council seen this yet? And what am I missing?
