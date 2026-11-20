You're right to be alarmed—and the good news is that **being at a 300-person company in Rotterdam gives you far more leverage than you probably realize**, without having to become the "difficult" engineer who fights the new VP head-on.

In the Netherlands, this policy is very likely **illegal to roll out unilaterally** and will almost certainly stall the moment the right internal guardrails are alerted.

Here is what you can actually do, in order of lowest personal risk to highest leverage.

---

### 1. Don't fight it publicly in Slack or an all-hands
Pushing back emotionally in a public channel makes it easy for a new VP (especially one importing US-style stack-ranking habits) to dismiss you as "resistant to accountability" or "anti-AI." Keep your tone **calm, curious, and protective of the company**.

### 2. Quietly alert your *Ondernemingsraad* (OR / Works Council)
At 300 employees in the Netherlands, your company is legally required to have an **OR** (*Wet op de ondernemingsraden*, WOR). Under **WOR Article 27(1)**, management **cannot** introduce this without the OR's prior consent (*instemmingsrecht*). This proposal hits three separate triggers at once:
- **Art. 27(1)(g):** Performance appraisal systems (*personeelsbeoordeling*)
- **Art. 27(1)(k):** Processing and protection of employee personal data
- **Art. 27(1)(l):** Systems intended or suitable for monitoring employee behavior or performance (*personeelsvolgsysteem*)

If leadership rolls it out anyway without OR consent, the OR can invoke nullity (*nietigheid*) within a month (Art. 27(5) WOR).

**What to do:** Have a quiet 1-on-1 coffee or send a confidential note to an OR member you trust. Frame it as *"I think the new VP may not know Dutch OR rules yet—wanted to flag this before it turns into a mess."* Let the OR be the "bad guy" doing its legal job. That keeps the target completely off your back.

### 3. Flag the GDPR / Dutch labor law risk to your EM or HR as a "helpful heads-up"
Framing your objection around **protecting the company and the VP from an unforced legal error** makes you look like a mature senior engineer, not a complainer:
- **GDPR / AVG & DPIA:** Monitoring individual IDE/GitHub telemetry to rank employees and trigger PIPs requires a mandatory **DPIA** (*Art. 35 AVG*, explicitly required by the *Autoriteit Persoonsgegevens* for employee monitoring), a valid legal basis (employee "consent" doesn't hold up due to power imbalance), and proportionality—which Copilot acceptance rate fails because it's a noisy, gameable proxy.
- **Dutch dismissal law (*disfunctioneren*, BW Art. 7:669(3)(d)):** Putting people on PIPs (*verbetertrajecten*) based on a mechanical weekly "bottom 10%" leaderboard will be torn apart by a *kantonrechter* if it ever leads to a dismissal attempt. HR and Legal will recognize this immediately once it's on their radar.

### 4. Give the VP an "off-ramp" (a better way to get what they actually want)
New VPs usually pitch metrics like this because they feel blind—they want to show the board that engineering is shipping and that the Copilot licenses are paying off. If you only say "no," you look obstructive. If you say *"Here's why those two metrics backfire, and here's a cleaner way to get real visibility,"* you look like a partner.

The strongest engineering arguments to share privately with your EM (and align on with a couple of respected Senior/Staff peers):
- **Goodhart's Law:** PR counts incentivize splitting 1-line changes into 10 tiny PRs and rubber-stamping reviews. Copilot acceptance rate incentivizes accepting verbose, buggy, or insecure suggestions instead of rejecting bad AI output.
- **It punishes senior engineering work:** Architecture, code reviews, mentoring, on-call/incidents, and hard debugging produce fewer PRs and lower Copilot acceptance. You'd literally be putting your highest-leverage people on PIPs.
- **Weekly cadence is pure noise:** A week of vacation, sick leave, on-call, or a single complex ticket guarantees someone lands in the bottom 10%.
- **Better alternatives:** Team-level **DORA metrics** (deployment frequency, lead time, change failure rate, MTTR), **aggregated/anonymized** Copilot adoption + developer surveys for AI ROI, and **manager-led calibration** for real underperformance.

### 5. Protect yourself quietly in the meantime
- Keep a lightweight weekly brag/impact doc of your actual contributions (design docs, reviews, incidents resolved, mentoring, shipped work).
- Save copies of any written announcements about the ranking policy.
- Don't panic-game the metrics, and if you are ever handed an unfair PIP based on this, **don't sign it on the spot**—ask for time to review and consult your OR, union (e.g., FNV/CNV), or *rechtsbijstandverzekering* (legal aid insurance) if you have one.

---

### Ready-to-use templates
I've saved a companion document with copy-pasteable templates in [action-plan-and-templates.md](file:///G:/agy-bench/ws/757cbfcc6f6d/action-plan-and-templates.md), including:
1. A **confidential message to the OR** citing WOR Art. 27 & AVG/GDPR
2. A **diplomatic, "protective" note to your EM or HR**
3. A **1-page counter-proposal** you can hand to leadership as an easy off-ramp
