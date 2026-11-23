I wouldn't take the cut to the board as proposed. The business case I've written is for a different decision:

- freeze hiring in QA and second-line support today
- measure the agents' real error rate on that work for eight weeks
- decide team size in early February against thresholds you agree now

On illustrative costs, cutting 6 QA and 10 second-line roles saves €1.18M a year on paper. In year one it saves about €0.26M, and that is before the cost of any errors that reach customers. Nobody has measured that cost yet.

The trap: a case built on "basically never wrong" falls at the board's first question: what's the error rate, and on which tasks? And cutting the people who catch the errors also takes away the means to find out.

**Why the claim can't carry the decision yet**
- **Second line is where the hard cases land.** Accuracy on routine tickets doesn't automatically carry over to escalations.
- **Your teams may be part of why the agents look so good.** The agents may look nearly flawless partly because QA and second line catch their mistakes before customers do. Remove the reviewers and the errors go straight to customers, unseen.
- **"Rarely wrong" needs a number.** Say the agents handle 1,200 second-line tickets a month unreviewed. At 2% wrong, that's 24 wrong answers a month reaching customers, and the company is liable for them. In 2024 a tribunal held Air Canada responsible for its chatbot's wrong refund advice.
- **Others have tried this.** Klarna leaned on AI for customer service, then said quality had suffered and started hiring humans again in 2025. In a 2026 survey of HR leaders, two in three companies that had cut jobs for AI were already rehiring.

**The numbers** (illustrative, € thousands; swap in your payroll figures)

| | Year 1 | Year 2 |
|---|---|---|
| Payroll saving, 16 roles | 885 | 1,180 |
| Exit costs | −400 | 0 |
| Oversight the agents still need (2 FTE) | −120 | −160 |
| Extra AI usage | −36 | −48 |
| Extra leavers among those who stay | −70 | 0 |
| **Net, before the cost of errors** | **259** | **972** |

- **Year one** ranges from about €19k to €419k, depending on exit costs.
- **Year two** falls to about €552k if you rehire four support roles, as most companies that cut for AI report doing.
- **Freed capacity is smaller than the resolution rate suggests.** Even a strong agent usually takes the shorter tickets. In my worked example it frees about 5 FTE of second-line capacity, not 10.

To be fair to your CTO, they may be right. If so, eight weeks of measurement will prove it, and waiting costs about €0.25M of deferred saving. You then reshape the teams category by category, with data behind you. If the agents aren't that good, cutting first could cost more than it saves, and it can't be undone.

**What's in the draft** (business-case.md)
- the options side by side, including doing nothing and redeploying people (IKEA's operator Ingka retrained 8,500 call-centre staff into a business Forrester puts at €1.3 billion in 2022 revenue)
- the economics
- an eight-week measurement plan with example thresholds
- human impact
- legal and consultation steps
- communication
- a pre-mortem

**This week**
1. **Freeze hiring in both teams.** It's reversible, and every leaver you don't replace saves €70–80k a year.
2. **Make the measurement a joint project with your CTO, not a challenge.** Something like: "Which error rate are we assuming, and on which tasks? Let's measure it for eight weeks with human review before we change any roles." Agree the thresholds before any data comes in.
3. **Have the two teams' managers tell their people in person.** It's a measurement, the teams help design it, and nobody loses their job while it runs. Promise nothing beyond that yet.
4. **Talk to employment counsel early.** Depending on your country and size, 16 exits may count as a collective redundancy with consultation duties. A works council would also have a say in both the reorganisation and any tool that measures staff performance.

**Two questions that would change the answer**
- **What's behind the proposal: capturing capacity from the agents, or a cost target?** If it's a target, tell me how much, by when, and why. The options then get wider (AI and cloud spend, vendors, pricing, leadership pay), and I'd rework the case around it.
- **What data supports "basically never wrong"?** Which tasks, which error rate, measured how, and over what volume?

What am I missing, and what would make this wrong?
