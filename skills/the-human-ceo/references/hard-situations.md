# Hard situations: when a decision is rigged, political or driven by hype

Most damaging decisions aren't made in a clean spreadsheet. A leader with a stake tilts an evaluation. Someone lobbies for a product that benefits them. A slogan like "AI is never wrong" replaces evidence. This file covers how a human CEO, or anyone advising one, handles that without becoming part of the problem.

## Contents

1. The general protocol
2. Cooked numbers in an evaluation
3. Letting juniors go "because of AI"
4. AI spend that nobody tracks
5. "AI is never wrong, so we need fewer people"
6. Lobbying and hidden conflicts of interest
7. When you are not the one in charge

## 1. The general protocol

1. **Judge the decision, not the person.** You can usually prove that a decision is badly founded. You can rarely prove someone's motives. Lead with the first.
2. **Go back to the raw data.** Re-run the numbers yourself from the source systems. Ask for the method, the raw scores and the version history: who changed what, and when. Confluence page history, spreadsheet version history, Jira changelogs and Git history are often the clearest record there is.
3. **Write it down.** Facts, dates, sources, in neutral language. No adjectives, no speculation about motives. Keep unverified claims about people, such as relationships or intentions, out of written messages; describe only what you can show. Offer a ready-to-send, neutral draft of the message to the decision owner.
4. **Make the process fair again.** Criteria and weights fixed before scoring, independent or blind reviewers, people with a stake stepping out of the decision, the method and raw data published.
5. **Use the right channel, in proportion.** Start with the decision owner if that is safe. Then the CEO, the works council, the internal reporting channel or confidential adviser, and the supervisory board or audit committee. External reporting is the last step. In the EU, the Whistleblower Directive (2019/1937) protects people who report breaches. In the Netherlands, the Whistleblower Protection Act (Wet bescherming klokkenluiders) has applied since 18 February 2023, employers with 50 or more workers must have an internal reporting procedure, and the Huis voor Klokkenluiders gives advice. This is not legal advice; check the current rules and get counsel for anything serious.
6. **Protect the people affected,** including whoever raised the concern. Retaliation against someone who reported in good faith is a serious problem in itself.
7. **Don't become what you're fighting.** No snooping, no leaking, no gossip, no "the end justifies the means". Never dig into someone's private life to win an argument about a business decision.
8. **Reopen bad decisions.** Sunk cost is not a reason to continue. If a rigged decision already hurt people, for example jobs lost on a platform that should never have won, say so and look at what can still be repaired: re-evaluation, rehiring or redeployment, and an honest account to the people affected.

## 2. Cooked numbers in an evaluation

Typical case: several options are compared, such as platforms, vendors or tools, and a leader who owns or sponsors one of them influences the scoring.

**Signals**
- Criteria or weights changed after the first results were known
- The person scoring, or setting the weights, owns or sponsors one of the options
- Raw scores, test data or the method are not available
- The result contradicts operational data, user feedback or earlier rounds
- People who disagree are sidelined, or are told the decision is final before it is made
- Unusual urgency to decide

**What to check**
- Version history of the scorecard and the decision page: the first published scores and weights against the final ones
- Whether the scores can be reproduced from the raw data
- Operational evidence for each option: incidents and recovery time, DORA metrics, cost per unit, developer satisfaction, adoption
- What users and the teams running each option actually say

**What to do**
- Re-run the evaluation with criteria and weights fixed before scoring, an independent panel without a stake, and the sponsor of any option stepping out of the scoring
- Publish the method and raw data so anyone can check them
- If the decision is already taken and harm followed, raise it as a decision-quality issue with the CEO or board, with the evidence. Propose a re-evaluation and look at what can still be repaired for the people affected
- If the evidence shows deliberate manipulation, take it through the governance channel (step 5 of the protocol), not into a meeting or a group chat

**How to say it:** "In version 1 option B led on four of six criteria. In version 3 the weights changed after the scores were in, and option C came first. Before we build on this, let's re-run it with fixed criteria and a panel that doesn't own any of the options."

## 3. Letting juniors go "because of AI"

**Why it backfires**
- Juniors are tomorrow's seniors. Without them the talent pipeline empties, and in a few years you pay a premium for the seniors you didn't grow.
- Judging AI output well takes experience, and experience comes from doing the work. Cutting the people who are learning removes the future reviewers of AI output.
- Juniors are usually among the cheapest people in the company, so the saving is small and the long-term cost is large.
- They are often the most fluent users of new tools, and they bring fresh questions to old assumptions.

**What to check**
- Does AI actually do their tasks at the required quality, measured in a pilot rather than in a demo?
- Where do the juniors' hours really go, and who would absorb the work?
- Seniority mix and succession: who will maintain each critical system in three years, and how many people can maintain it today?

**What to do**
- Redesign junior roles around AI instead of removing them: pairing, reviewing and testing AI output, owning small systems end to end, structured apprenticeships
- Keep a deliberate share of entry-level roles in workforce planning, and track time to productivity
- Evidence for the conversation is in [evidence.md](evidence.md): the entry-level employment trend and why industry leaders call this a mistake

## 4. AI spend that nobody tracks

**Signals**
- Large monthly AI bills that nobody can explain line by line
- Licences for everyone, regular use by a few
- The most expensive model used for simple tasks, or agents left running on schedules nobody reviews
- AI-generated dashboards and reports that nobody opens
- No budget owner, and leaders surprised by what enterprise plans cost

**What to check**
- Invoices and usage reports per seat, team and project: the vendor's admin console, API usage dashboards, cloud billing
- Active users over the last 30 days against licences paid
- Cost per useful output, for example per dashboard actually viewed (most BI tools show view statistics)
- Cheaper ways to get the same result: the BI tool the company already pays for, smaller models, scheduled or cached reports

**What to do**
- Give AI spend an owner, a budget and alerts, and review it monthly like any other cloud cost
- Right-size licences and pick the right model for each task
- Judge AI spend on value (decisions changed, hours saved, quality gained), not on usage
- Keep a time-boxed budget for experiments; learning is worth paying for, as long as it is visible

**How to say it, without blame:** "We spend X a month on AI. Y% of seats were active in the last 30 days, and Z of the generated dashboards were opened. Here is how we keep the value and cut the waste."

## 5. "AI is never wrong, so we need fewer people"

**The facts**
- Current AI systems make confident mistakes, and the company stays responsible for what its AI says. In Moffatt v. Air Canada (February 2024), a Canadian tribunal held Air Canada liable for wrong refund information given by its website chatbot.
- Productivity gains are real in some tasks but not automatic. In a 2025 randomised trial by METR, experienced open-source developers took 19% longer on tasks when they could use AI tools, while believing the tools had made them faster.
- Fewer people checking the work means more errors reach customers.

**What to do**
- Ask for the evidence behind the claim: which error rate, on which tasks, measured how
- Run a controlled pilot with quality metrics and human review before changing headcount
- Define where a person must stay accountable: legal commitments, safety, customer promises, decisions about people
- Size freed capacity honestly, with the method in SKILL.md
- Keep the people who catch errors, and keep a route to a human

**How to say it:** "Which error rate are we assuming, and on which tasks? Let's measure it for six weeks with human review before we change any roles."

## 6. Lobbying and hidden conflicts of interest

Typical case: a product, vendor or plan is pushed by someone with a personal stake. That can be a shareholding, a side deal, a former employer, a friend, or a personal relationship with a decision-maker or a vendor. Pressure can also come from a shareholder or board member tied to a vendor, or from executives trading favours.

**Focus on the conflict, not on private lives.** The problem is an undisclosed interest influencing a business decision, not who is friends with or dating whom. Don't investigate people's private lives and don't spread rumours. It hurts people, it can breach privacy law, and it destroys your credibility.

**Signals**
- A decision taken outside the normal process, or "it has already been decided"
- The evaluation skipped or shortened for one option
- A sponsor who is unusually insistent and won't share the business case
- Pressure from a board member or investor linked to the vendor

**What to do**
- Check the company's conflict-of-interest, gifts and procurement policies, and follow them
- Insist that the decision goes through the normal process with documented criteria and an independent evaluation
- Ask, as standard practice, that anyone with a personal or financial interest declares it and steps out of the decision. Make this routine, not an accusation
- Record the rationale for the decision so it can be reviewed later
- Shareholders and board members may ask and advise, but management decides on evidence. In many jurisdictions, including the Netherlands, directors must act in the interest of the company as a whole, not of one shareholder
- If there is credible evidence that an undisclosed conflict shaped a material decision, take it to compliance, the chair of the supervisory board or audit committee, or the internal reporting channel. Not to the hallway.

## 7. When you are not the one in charge

Most people who spot these problems are not the CEO. When the user is an employee, manager or advisor:

- Help them build a short, factual case: what happened, the evidence, the impact, what they propose
- Suggest allies with a stake in good outcomes: finance, security, the works council, the teams affected
- Use the safest effective channel first: their manager or a skip-level, then the confidential adviser (vertrouwenspersoon in the Netherlands) or the internal reporting channel
- Keep only records they are allowed to keep, and never break confidentiality or data protection rules to "prove" a point
- Recommend independent legal advice before any external report
- Be honest about the personal risk, and respect their choice. Speaking up is brave; it is not an obligation to sacrifice their career

Sources for the facts in this file are listed in [evidence.md](evidence.md).
