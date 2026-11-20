# Action Plan & Templates: Responding to Weekly Individual Metric Rankings

This document contains ready-to-use scripts and a lightweight counter-proposal you can adapt to push back on individual Copilot/PR stack-ranking **without making yourself the target**.

---

## 1. Confidential Note to the Ondernemingsraad (OR / Works Council)

*Send this to an OR member you trust (in person, over a coffee, or via a brief message). Ask them to treat the source confidentially and raise it with HR/Leadership as a standard compliance check.*

> **Subject:** Heads-up: proposed weekly engineer ranking (Copilot + PR metrics)
>
> Hi [Name],
>
> I wanted to flag something confidentially for the OR before it gets rolled out formally.
>
> Our new VP of Engineering recently mentioned wanting to introduce a weekly individual ranking of engineers based on GitHub Copilot acceptance rate and number of PRs merged, with the bottom 10% placed on performance improvement plans (PIPs).
>
> Leaving aside the engineering concerns, this looks like it directly touches **WOR Article 27(1)**—specifically:
> - **(g)** performance appraisal systems (*personeelsbeoordeling*),
> - **(k)** processing of employee personal data (*personeelsgegevens*), and
> - **(l)** systems used to monitor employee behavior or performance (*personeelsvolgsysteem*).
>
> It also raises obvious **AVG/GDPR** questions (including whether a DPIA has been completed, given the Autoriteit Persoonsgegevens' rules on employee monitoring).
>
> I'm guessing the new VP simply isn't familiar with Dutch labor law and the OR's *instemmingsrecht* yet. Could the OR check in with HR/Leadership to ensure nothing like this is piloted or rolled out without formal OR review and consent? I'd appreciate it if my name stays out of it.
>
> Thanks,
> [Your Name]

---

## 2. "Protective & Pragmatic" Message to Your Engineering Manager (or HR)

*Use this framing so you come across as aligned with the company's success—not defensive or resistant to accountability.*

> Hi [Manager's Name],
>
> I've been thinking about [VP's Name]'s idea to track Copilot acceptance and PR counts weekly with a bottom-10% PIP threshold. I completely get why they want visibility into delivery and AI ROI, especially coming in new.
>
> I wanted to flag two practical risks early so we don't accidentally step on a rake:
>
> 1. **Dutch compliance risk:** At our size in the Netherlands, using individual IDE/GitHub telemetry to rank people and trigger PIPs almost certainly requires **OR consent (WOR Art. 27)** and a **GDPR DPIA**, and a forced weekly ranking won't hold up under Dutch dismissal law if HR ever relies on it. It might save [VP's Name] a lot of friction if HR/Legal flags this early.
> 2. **Perverse incentives:** Weekly PR counts and Copilot acceptance rates heavily penalize senior work—architecture, code reviews, incident response, mentoring, and hard bugs—and encourage splitting trivial PRs or accepting mediocre AI code just to stay off the bottom of the list.
>
> If it's helpful, I'd be happy to help put together a short counter-proposal for measuring team delivery and Copilot adoption in a way that actually gives [VP's Name] real signal. What do you think?

---

## 3. One-Page Counter-Proposal: Measuring Delivery & AI ROI Without Gaming

*Offer this through your EM or alongside a couple of respected senior/staff peers so leadership has an easy "off-ramp" that still looks like a win.*

### Goal
Give Engineering Leadership clear visibility into:
1. **Delivery speed & reliability**
2. **Return on investment (ROI) from GitHub Copilot**
3. **Genuine underperformance** that needs coaching or a formal PIP

### Why Individual Weekly PRs + Copilot Acceptance Backfire
- **Goodhart's Law:** Optimizing for PR count produces smaller, noisier PRs and rubber-stamped reviews. Optimizing for Copilot acceptance rate incentivizes accepting verbose or subtly buggy code rather than writing minimal, maintainable code.
- **Penalizes high-leverage work:** Engineers on call, unblocking teammates, reviewing complex PRs, or tackling ambiguous architecture problems look "unproductive" on a weekly PR/Copilot leaderboard.
- **Weekly noise:** One week of vacation, sick leave, on-call duty, or a complex incident will push strong engineers into the "bottom 10%."
- **Compliance & retention:** Individual telemetry-driven forced ranking triggers Dutch Works Council (*OR*) consent requirements (WOR Art. 27), GDPR DPIA obligations, and severe attrition among top performers.

### Recommended Alternative (3-Layer Approach)

| What Leadership Wants to Know | Recommended Signal | Cadence & Level |
|---|---|---|
| **Is engineering shipping faster and safely?** | **DORA metrics** (Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR) + sprint/roadmap predictability | Monthly, **Team level** |
| **Is Copilot worth the license cost?** | **Aggregated adoption metrics** (active seats, team-level usage trends) + short quarterly developer survey on time saved & friction points | Quarterly, **Org / Team level** |
| **Who is struggling and needs support or a PIP?** | **Manager-led performance calibration** based on role expectations (delivery impact, code quality, reliability, collaboration) | Ongoing 1:1s + bi-annual calibration, **Individual level** |

### Quick Wins in the Next 30 Days
1. Publish a **team-level** delivery dashboard (lead time, deployment frequency, incident rate).
2. Run a **2-minute anonymous Copilot pulse survey** to identify teams that need enablement/training rather than policing acceptance rates.
3. Align Engineering Managers on clear **career-ladder expectations** so genuine underperformance is addressed fairly, early, and legally.
