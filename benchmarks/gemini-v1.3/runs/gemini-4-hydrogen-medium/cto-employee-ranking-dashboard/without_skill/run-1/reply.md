You’re right to push back, and you don’t have to play the "angry senior engineer" to do it effectively. In a 300-person Dutch company, you actually have both **engineering arguments** and **Dutch institutional guardrails** on your side.

The key to not being seen as difficult is to frame your pushback around **protecting the VP from predictable failure** (bad data, gaming, legal/OR blowback, and losing senior talent), rather than debating whether accountability is good.

Here is what you can actually do, roughly in order of leverage and safety.

---

### 1. Quietly check the Dutch governance guardrails (lowest personal risk)
At 300 employees in the Netherlands, your company is legally required to have an **Ondernemingsraad (OR)** and an HR/Legal function. A new VP—especially if they’re from outside NL/EU—often doesn't realize they can't unilaterally run weekly stack-ranking into PIPs here:

* **WOR Article 27 (*Instemmingsrecht*):** Under the *Wet op de ondernemingsraden*, the OR has the **right of consent** over both employee monitoring systems (*personeelsvolgsystemen*, Art. 27(1)(l)) and performance appraisal systems (*beoordelingssystemen*, Art. 27(1)(g)). Rolling out individual Copilot/PR tracking tied to PIPs without OR consent is generally unlawful.
* **AVG / GDPR:** Individual-level telemetry used for automated or systematic ranking and disciplinary action requires a strict legal basis, proportionality, transparency, and usually a Data Protection Impact Assessment (DPIA).
* **Dutch dismissal / PIP law (*verbetertraject*):** A formal PIP in NL requires documented, role-relevant underperformance and fair coaching—not "you landed in the bottom 10% of PR counts this week."

**What to do:** You don’t need to play lawyer in a public meeting. Either:
* Ask your manager or HRBP a neutral, "helpful" question: *"Has Legal/OR signed off on using individual Copilot and PR metrics for PIPs under WOR Art. 27 and AVG? I’d hate for us to get blindsided halfway through."*
* Or speak privately with an OR member you trust so the OR asks that question formally. That takes the target completely off your back.

---

### 2. Align with your Engineering Manager and Staff+ peers first
Don't be a lone voice. Before talking up the chain, talk to your EM and a couple of respected senior/staff engineers:
* Ask your EM privately: *"How are we supposed to handle weeks where someone is on-call, doing heavy code reviews, mentoring, or tackling a multi-week architecture spike—all of which give you zero PRs merged and low Copilot acceptance?"*
* Good EMs usually hate these mandates too because **they** are the ones forced to put good engineers on fake PIPs. Give your EM concrete examples they can take upward.

---

### 3. Use "Yes, and" framing if you speak to the VP
If you’re in a position to give direct feedback (e.g., skip-level 1:1 or an engineering leadership channel), don't argue that metrics are bad. Agree with the underlying goal (visibility into delivery and AI ROI) and show how **these specific metrics** will break it:

* **Show the gaming mechanics calmly:**
  * *PRs merged* rewards splitting one change into 10 tiny PRs and punishes reviewing others' PRs, helping teammates, on-call, and hard cross-cutting work.
  * *Copilot acceptance rate* rewards hitting Tab on boilerplate or mediocre suggestions and punishes engineers working on novel/complex logic or carefully rejecting bad completions.
  * *Weekly cadence + bottom 10% PIP* guarantees false positives from normal variance (vacations, big refactors, incident response) and kills collaboration—nobody helps a teammate if it drops their own weekly PR count.
* **Propose what to measure instead:**
  * **Team-level delivery metrics** (DORA metrics, PR review turnaround time, cycle time, deployment frequency) rather than individual stack rankings.
  * **Aggregate AI enablement** (% of engineers actively using Copilot, qualitative friction surveys, where AI actually saves time) rather than individual acceptance rates.
  * **Calibration-based performance** led by EMs who actually see the whole picture (impact, unblocking others, reliability, mentoring).

Framing it as *"I want you to get real signal on engineering velocity, and this will give you noisy, gamed data within two weeks"* positions you as a pragmatic ally, not a blocker.

---

### 4. Protect your team's visibility while this plays out
Even if the policy gets walked back or softened, while it's in the air:
* **Make "invisible" work visible:** Encourage your team to log spikes, design docs, major code reviews, and incident/support work in sprint updates or weekly summaries so EMs have a paper trail if anyone looks at raw PR counts.
* **Don't let juniors panic-game:** Quietly tell junior/mid engineers not to start chopping PRs into 3-line fragments or blindly accepting Copilot code unless told otherwise, and that you and your EM are raising the concerns upward.

---

### 5. Watch how leadership reacts
How the VP responds tells you a lot about your future there:
* **Good sign:** They listen to the OR/EM/senior pushback, realize Dutch context + Goodhart's Law makes this a bad idea, and pivot to team-level metrics or enablement.
* **Red flag:** They double down, try to route around the OR/EMs, or treat valid concerns about metric gaming as "resistance to accountability." If that happens, quietly update your CV—because a 300-person company in Rotterdam where a VP insists on weekly stack-ranked PIPs will lose its best engineers fast.
