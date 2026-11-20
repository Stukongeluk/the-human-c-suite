My recommendation: take the board a gated AI programme that starts in January and lets our own pilot set the number, not a commitment to replace 27 of the 90 roles in 2027. On my estimates, cutting 27 roles next year costs about SEK 43m net in 2027 instead of saving money, because the AI will have freed roughly 7 FTE of work by the end of 2027 (range 3–11), not 27.

The board paper is in `business-case.md`, ready to edit. The model behind it is `savings_model.py`, with its full output, including the low and high cases, in `model_output.md`. Every figure is labelled as an estimate. Our own payroll, AP and reconciliation data will move the numbers, but not the shape of the case.

**The options, net of every cost, against doing nothing (SEK m, base case)**

| Option | 2027 | 2028 | Per year from 2029 | Heads end-2028 | Forced exits |
|---|---|---|---|---|---|
| A. 27 redundancies in 2027, alongside the AI programme (the board's ask) | −43.1 | −7.7 | +10.5 | 73, after about 26 rehires | 27 |
| B. Gated AI programme; headcount follows proven capacity | −14.5 | +2.2 | +10.4 (high case +19.9) | 73 (high case 62) | 0 |
| C. Process fixes only, no new AI | −0.1 | +5.3 | +5.7 | 83 | 0 |
| Do nothing | 0.0 | 0.0 | 0.0 | 90 | 0 |

**Why A loses money in 2027**

Swedish law sets the timeline:

- MBL negotiation comes before the decision.
- Arbetsförmedlingen must be notified at least four months before the first employment ends.
- LAS notice periods run one to six months.
- LAS selection by length of service means the people who leave aren't necessarily those whose tasks the AI takes.
- Dismissed staff have nine months' priority for re-employment.

So the first exits come in June and most in September, while the work stays. The resulting gap of about 19 FTE in 2027 costs SEK 28m in consultants. Even if that work were simply left undone, A would still do slightly worse than B in 2027, and an insurer can't leave reconciliations or Solvency II reporting undone. In 2028 we would rehire about 26 people. Others have seen the same: in a 2026 survey of 600 HR leaders, two in three companies that cut jobs because of AI were already rehiring.

**What B does**

- **January:**
  - process fixes (an e-invoicing drive, supplier consolidation, stopping reports nobody reads);
  - a hiring freeze with exceptions;
  - a four-week baseline of hours and error rates;
  - union representatives in the design group from the start.
- **February–June:** a pilot in AP and reconciliations on live data, with a person approving every payment and posting. Cost about SEK 6m.
- **Gate 1 (June):** we scale only if the results point to at least about 17 FTE of AI capacity by end-2028, about 27% of the team together with the process fixes. If the pilot fails, we stop, and 2027 costs about SEK 7.5m.
- **Gate 2 (December):** the 2028 headcount plan is built from measured capacity:
  - attrition, about 7 a year;
  - redeployment, about 5–7 people;
  - voluntary exits only for the surplus that remains (about 1 in the base case, 10 in the high case).
- **High case:** B reaches the board's 30% by end-2028, a year later than asked, without forced redundancies.

**The finding the board needs to hear**

Most of the early, safe gain comes from process fixes that need no AI. On my base case, the AI adds about SEK 4.6m a year on top of them and pays back about four years after 2028. In the high case it pays back in about two years; in the low case, never. Even best-in-class AP teams process only 49.2% of invoices untouched, against an average of 32.6% (Ardent Partners, 2025). For about SEK 6m, the pilot tells us which case we're in before any job depends on it.

**The trap**

A case written to prove a number the board has already chosen gets measured against reality a year later. Booking the payroll saving before the pilot shows the hours are freed usually ends in rehiring. Gartner's November 2026 advice to CFOs puts it well: "AI-generated capacity is a resource, not a return."

**What the board is right about**

The opportunity in AP and reconciliations is real, competitors are moving, and waiting costs money. B starts in January. The only change is when headcount becomes a commitment: at the gate, on our own data. I'd take the chair through this privately before the meeting, so nobody has to defend the 30% in front of the full board.

**Controls and regulation**

The paper covers:

- people keep approving payments and postings;
- the auditor joins the pilot;
- DORA third-party requirements apply to the vendors;
- under Solvency II, Finansinspektionen must be notified before a vendor performs a critical or important function;
- EIOPA's 2025 Opinion on AI governance;
- no AI ranking of staff, which would also make the tools high-risk under the AI Act.

This isn't legal advice. Counsel, compliance and the auditor should confirm it before the board decides.

**Two questions that would change the numbers**

1. What is the board solving for: a SEK or expense-ratio target by a date, or a credible AI plan? Finance and back office alone can't meet a hard 2027 cost target, so in that case I'd size the rest of the operating cost base alongside it.
2. Can we get the baseline within four weeks? That means invoice volumes and touchless rate, reconciliation counts and auto-match rates, close days, three years of attrition, and consultant spend in the team. If some of the 90 are consultants, ending those contracts is the fastest saving and costs no employee their job.

**Key assumptions** (all estimates):

- SEK 0.88m loaded cost per FTE;
- 8% attrition;
- net AI capacity of 7 FTE at end-2027 and 19.5 at end-2028;
- AI programme cost of SEK 14.7m in 2027 and 7.8m in 2028;
- consultants at SEK 1.45m per FTE-year;
- a 6-month exit package in option A.

What am I missing, and what would make this wrong?
