You’re right that this is a terrible policy—and the good news is that at a **300-person company in the Netherlands**, you have unusually strong leverage to stop it *without* looking like the difficult engineer.

The trick is **not** to argue from personal outrage or ethics. Frame yourself as the pragmatic senior engineer helping a new VP avoid a legal, operational, and retention landmine.

---

### 1. Your Biggest Lever: Dutch Law (WOR, AVG, and Dismissal Law)

A new VP—especially one coming from US/UK tech or trying to make a fast impact—often doesn’t realize how hard this collides with Dutch law:

* **Ondernemingsraad (OR / Works Council):** At 300 employees in the Netherlands, you are legally required to have an OR (50+ threshold). Under the *Wet op de ondernemingsraden* (**WOR Art. 27(1)(g)** and **27(1)(l)**), the OR has **instemmingsrecht (right of consent)** over both employee appraisal systems (*personeelsbeoordeling*) and systems capable of monitoring employee performance/behavior (*personeelsvolgsystemen*). Implementing this without OR consent makes the policy **null and void** (*nietig*) if the OR invokes nullity within a month.
* **GDPR / AVG:** Tracking individual Copilot acceptance rates and PR counts for disciplinary action requires a lawful basis, proportionality/subsidiarity (hard to defend when team-level metrics exist), almost certainly a **DPIA** (Art. 35 AVG), and runs straight into **Art. 22 AVG** if "bottom 10% = automatic PIP" has no real human assessment.
* **Dutch labor law (*verbetertraject*):** In the Netherlands, you cannot fire someone off a weekly forced curve. A *kantonrechter* requires a substantiated individual dossier tied to actual job requirements and a genuine, tailored improvement plan (*disfunctioneren*, Art. 7:669(3)(d) BW). HR and Legal will quietly know this is unenforceable.

**Why this helps you socially:** Flagging *"Hey, before this rolls out, has HR/Legal/OR cleared WOR Art. 27 and an AVG DPIA?"* doesn’t sound rebellious. It sounds like you’re saving the VP from an embarrassing first-quarter faceplant.

---

### 2. The Engineering Argument (Keep It About Business Risk)

If you discuss the metrics themselves, stick to **second-order effects on delivery**, not feelings:

* **Goodhart’s Law in week one:** People will split trivial changes into 10 micro-PRs and blindly accept verbose/mediocre Copilot completions to stay out of the bottom 10%. (Even GitHub’s own guidance explicitly advises *against* using Copilot acceptance rate as an individual performance metric.)
* **It punishes senior leverage:** Code reviews, architecture, debugging hard production issues, on-call, and mentoring produce *fewer* PRs and *lower* Copilot acceptance—and they are the exact things that keep a 300-person engineering org from collapsing.
* **Weekly cadence is pure noise:** One vacation day, one incident, or one complex refactor puts a strong engineer in the bottom 10%.
* **Regrettable attrition:** Your best senior engineers will immediately see the perverse incentives and start interviewing, while people who game vanity metrics look like top performers.

---

### 3. Your Step-by-Step Playbook (Lowest Friction First)

1. **Don’t fight it in a public Slack channel or All-Hands.** Public pushback forces a new VP to get defensive to save face.
2. **Sound out your Engineering Manager (EM) privately first.** Ask in your 1:1 whether leadership/HR/OR have reviewed it and share the compliance + delivery risks. Many EMs hate this too and are looking for senior-engineer backing to push upward.
3. **Give the VP a face-saving off-ramp.** Executives ask for bad metrics because they feel blind. Pair your pushback with a concrete alternative that answers what they *actually* want to know:
   * *Are we shipping well?* → **Team-level DORA metrics** (cycle time, deployment frequency, change failure rate, MTTR).
   * *Is Copilot worth the money?* → **Aggregate adoption + developer friction surveys** and enablement workshops.
   * *Who needs help?* → **Manager-led quarterly calibration** against the engineering ladder (which actually holds up under Dutch law).
4. **If it’s still moving forward, tip off the OR confidentially.** OR members have a statutory duty of confidentiality (Art. 20 WOR) and dismissal protection. A simple, neutral question—*"Has the OR been asked for instemming under Art. 27 WOR for the weekly Copilot/PR ranking?"*—is usually enough to put the entire rollout on ice while keeping your name out of it.
5. **Loop in HR/Privacy (DPO) if you don’t have an active OR.** Asking your Privacy Officer/DPO whether a DPIA has been completed for individual Copilot telemetry is another completely neutral, non-confrontational circuit breaker.

---

### 4. Protect Yourself in the Meantime

* **Keep receipts of high-leverage work** (design docs, major reviews, incident leads, mentoring) in a simple weekly brag doc.
* **Keep everything written:** If anything resembling a PIP ever lands in your inbox, get the criteria in writing—and remember that under Dutch law you never have to sign a PIP agreement or *vaststellingsovereenkomst* (VSO) on the spot. (If you don't have *rechtsbijstandverzekering* for work disputes yet, it's worth checking your policy, though most have a waiting period.)

---

I also put together a ready-to-use companion document in [metrics-pushback-kit.md](file:///G:/agy-bench/ws/5090a4a60105/metrics-pushback-kit.md) with:
- A 1:1 script for your Engineering Manager
- A "helpful heads-up" email template if you talk to the VP directly
- A confidential message template for your Ondernemingsraad (OR)
- A 1-page alternative metrics proposal you can hand them as an off-ramp
