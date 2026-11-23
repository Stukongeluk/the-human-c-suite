# Accountability pack: the failed database migration

This pack has four working pieces: a note to send the board, a setup for the review, the rule for individual consequences, and talking points for your conversation with the platform lead. A short list of fixes you can expect closes it. Text in [brackets] is for you to fill in or adjust.

---

## 1. Draft note to the board

**Subject:** Last weekend's outage: accountability and next steps

Dear [Chair / board members],

Last weekend our database migration failed, and the platform was down for about 9 hours. Our first estimate of the cost is around €2 million. The CFO is confirming that figure, and what it includes, by [date].

I am accountable for this. The migration ran on plans, safeguards and processes that my organisation is responsible for, [and that I approved].

I understand that the board wants to see someone held accountable. I will not make a personnel decision about [name] or anyone else before we know what happened, and today we don't. Deciding now would cost us the person who knows the most about what went wrong. It would also make engineers less likely to raise problems early, and it would carry legal risk because we have no documented basis.

Here is what you will get from me:

- **By [date, two weeks out]:** a written review of what happened, why recovery took 9 hours, and which safeguards failed. [Facilitator], who was not involved in the migration, will lead it.
- **In the same report:** a fix plan with named owners, dates and costs.
- **This week, before the findings:** the criteria we will use to decide whether any individual consequences are warranted, so the outcome can't look improvised in either direction.

If the review shows that someone knowingly ignored agreed safeguards or hid information, I will act on that through HR. If it shows that our system set people up to fail, then the fix is the system, and delivering it is my job.

Kind regards,
[Name], CTO

---

## 2. The blameless review

**Setup**

- **Facilitator:** someone who was not involved in the migration and is not in the platform lead's reporting line. If the board wants more independence, use an outside facilitator.
- **In the room:** everyone who worked on the migration or the incident, plus whoever approved the plan. If you approved it, stay out of the first timeline session so people speak freely, and join for the findings.
- **Ground rule:** the review asks how this happened and why each decision made sense at the time. No individual is named as "the cause".
- **Output:** a timeline, the contributing factors, and fix actions with an owner and a date for each.

**Questions to answer**

*Before the migration*
- Was there a written plan with a way back (a rollback)? Had the rollback been tested?
- Was the migration rehearsed on production-sized data? How long did the rehearsal take compared with the planned window?
- Who approved the plan, the timing and the risk, and what information did they have?
- Did anyone raise concerns beforehand? If so, what happened to those concerns?
- Was there business or deadline pressure on the date or the scope?
- How many people were on it, how long had they been working, and was a second senior person available?

*During the incident*
- Was there an agreed abort time, as in "if this isn't done by X, we roll back"? Was it used, and if not, why not?
- When did it become clear that things were going wrong, and when was it escalated? What made escalation fast or slow?
- How do the 9 hours break down between restoring, deciding and waiting for people or vendors?
- Did monitoring catch the problem, or did customers?
- How did communication go, both internally and to customers?

*The system*
- Have there been earlier near-misses like this one?
- What would have turned 9 hours into 1?

---

## 3. When an individual is held to account

Agree on this rule before the findings come in. It applies to everyone involved, including whoever approved the plan, and that may be you. The first three rows come from the "just culture" model used in patient safety.

| What the review finds | Fair response |
|---|---|
| **Human error:** an unintended slip or mistake | Support the person and fix the system |
| **At-risk behaviour:** a shortcut whose risk was underestimated, often one that was normal in the team | Coach the person, and remove the pressures and gaps that made the shortcut normal |
| **Reckless behaviour:** knowingly ignoring a substantial, unjustifiable risk, such as skipping an agreed safeguard or overriding a no-go | An HR process with legal advice. The outcome can range from a formal warning to dismissal |
| **Dishonesty:** hiding or misrepresenting information during or after the incident | An HR process with legal advice |

---

## 4. Conversation with the platform lead

**Say**
- "I'm not going to make you the answer to this. I've told the board there will be no personnel decisions before the review."
- "I need you in the review as the main source. You won't lead it, and that protects both you and the review."
- "How are you doing?" Offer time off or support. A long incident followed by talk of blame is hard on anyone.
- "I can't promise an outcome. I can promise a fair process and the same standard for everyone, me included."

**Avoid**
- Taking them off their work while the review runs. That signals guilt before there are any facts.
- Keeping the board's suggestion from them if they ask or have already heard. If they haven't, you don't need to bring up a suggestion you're not acting on.

---

## 5. Fixes you can expect (to be confirmed by the review)

These are the usual candidates, listed so you can check the review's proposals against them. They are not conclusions.

- **A standard for high-risk migrations:** a written plan with a tested rollback, a rehearsal on production-sized data, a hard abort time, and go/no-go sign-off by two people.
- **Smaller steps:** move the data in steps while the system keeps running instead of in one big weekend cutover. One way is "expand and contract": add the new structure, move over gradually, then remove the old one.
- **Tested recovery:** a known, tested restore time for backups, plus a written runbook.
- **Staffing for change windows:** at least two senior people and set shift lengths.
- **Decision records:** write down any large, hard-to-reverse change as an architecture decision record (ADR), a short document covering context, options, decision and consequences, including the risk and the way back.
- **Time to recover as a team metric:** track how long the team takes to restore service after an incident (MTTR, mean time to recovery). The best-performing teams restore in under an hour. Measure this per team, not per person.

---

**Sources:** [Google SRE book: Postmortem culture](https://sre.google/sre-book/postmortem-culture/) · [DORA: Generative organizational culture](https://dora.dev/capabilities/generative-organizational-culture/) · [John Allspaw (Etsy): Blameless postmortems and a just culture](https://www.etsy.com/codeascraft/blameless-postmortems) · [GitLab: How is team-member-1 doing?](https://about.gitlab.com/blog/how-is-team-member-1-doing) · [ISMP/ECRI: Human error, at-risk and reckless behaviour](https://home.ecri.org/blogs/ismp-alerts-and-articles-library/the-differences-between-human-error-at-risk-behavior-and-reckless-behavior-are-key-to-a-just-culture) · [Deel: Performance dismissals in the UK, Germany, France and the Netherlands](https://www.deel.com/blog/performance-improvement-plans-international-dismissal-law/)
