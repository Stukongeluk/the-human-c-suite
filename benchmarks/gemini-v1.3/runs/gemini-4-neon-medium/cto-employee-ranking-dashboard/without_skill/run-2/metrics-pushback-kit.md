# Practical Pushback Kit: Weekly Copilot & PR Stack Ranking

A set of low-friction scripts and a lightweight alternative proposal tailored for a 300-person company in the Netherlands.

---

## 1. Talking Points for Your Engineering Manager (First Move)

Use this in a 1:1 before saying anything publicly. The goal is to test whether your EM already sees the risk and give them clean ammunition.

> "Hey [Name], I've been thinking about the weekly Copilot acceptance + PR count ranking and bottom-10% PIP idea. I want [VP's name] to get real visibility into delivery and AI adoption, so I'm not pushing back on measuring engineering health.
>
> Two things worry me as a senior engineer:
> 1. **Dutch compliance risk:** At 300 people, individual performance tracking tied to PIPs almost certainly triggers *Ondernemingsraad* consent (*instemmingsrecht* under WOR Art. 27(1)(g) and (l)), an AVG DPIA, and won't hold up as a *verbetertraject* dossier under Dutch labor law. If HR/Legal/OR haven't signed off yet, rolling this out could blow up in [VP's name]'s first quarter.
> 2. **Delivery side effects:** Weekly PR counts and Copilot acceptance rates heavily penalize code reviews, debugging, architecture, on-call, and mentoring—and actively reward splitting tiny PRs and blindly accepting boilerplate.
>
> Are you already raising this with leadership, or would it be helpful if I wrote up a short, constructive alternative we could share?"

---

## 2. Direct "Helpful Risk-Flagger" Note to the VP (If You Have Direct Access)

Keep it calm, business-focused, and protective of *their* credibility. Avoid moralizing.

> **Subject:** Quick thoughts on the engineering metrics rollout (NL compliance + signal quality)
>
> Hi [VP Name],
>
> Welcome again—I'm fully behind getting clearer visibility into delivery speed and whether we're getting real value out of Copilot.
>
> Before the weekly PR + Copilot ranking rolls out, I wanted to flag two practical risks from the ground level:
>
> 1. **Dutch labor & Works Council (OR) exposure:** Because we're a 300-person Dutch entity, individual-level monitoring systems and assessment rules require prior consent (*instemmingsrecht*) from the Ondernemingsraad under WOR Art. 27(1)(g) & (l), plus an AVG/GDPR DPIA. In addition, a weekly forced-curve PIP doesn't meet the Dutch *verbetertraject* standard if ever challenged. Looping in HR/Legal/OR early avoids an unnecessary stall or legal pushback.
> 2. **Perverse incentives on senior work:** On a weekly cadence, PR count and Copilot acceptance rate skew heavily toward small, boilerplate changes and away from high-leverage work like thorough code reviews, incident response, architecture, and complex debugging. GitHub's own guidance advises against using acceptance rate for individual evaluation for this reason.
>
> If it's useful, I'd be happy to help put together a lightweight dashboard that gives you real visibility—team-level delivery metrics (cycle time, deployment frequency, change failure rate) alongside aggregate Copilot adoption and friction points—without creating gaming or OR friction.
>
> Happy to chat for 15 minutes if that's helpful.
>
> Best,  
> [Your Name]

---

## 3. Confidential Note to the Ondernemingsraad (OR)

OR members are bound by confidentiality (Art. 20 WOR) and have statutory dismissal protection. You can ask a neutral, factual question without sounding adversarial.

> Hi [OR Member Name],
>
> I wanted to check something with the OR in confidence.
>
> Our new VP of Engineering recently announced a plan to rank engineers weekly based on GitHub Copilot acceptance rates and number of PRs merged, with the bottom 10% placed on improvement plans (PIPs).
>
> Could you let me know whether this proposal has been submitted to the OR for consent (*instemmingsrecht*) under **Art. 27(1)(g)** (*personeelsbeoordeling*) and **Art. 27(1)(l)** (*personeelsvolgsystemen*) of the WOR, and whether an AVG DPIA has been conducted?
>
> I'd prefer to keep my name out of it for now, as I'm hoping this can be resolved constructively through the normal process. Thanks for looking into it.

---

## 4. One-Page Alternative Proposal (Give the VP an Off-Ramp)

When executives ask for bad metrics, it's usually because they feel blind. Offer a better lens that answers their actual questions.

### What Leadership Actually Needs to Know
1. **Are we shipping reliably and fast enough?**
2. **Is our Copilot spend paying off?**
3. **Who is struggling and needs coaching or support?**

### Proposed Measurement Framework

| Goal | Avoid (High Noise / Legal Risk) | Use Instead (High Signal / NL-Compliant) |
| :--- | :--- | :--- |
| **Delivery speed & quality** | Individual weekly PR count | **Team-level DORA metrics** (PR cycle time, deployment frequency, change failure rate, MTTR) reviewed monthly |
| **AI / Copilot ROI** | Individual Copilot acceptance rate | **Aggregate adoption & enablement** (active seats, team-level usage trends, developer surveys on where Copilot helps vs. hurts, prompt/workflow sharing) |
| **Individual performance** | Weekly bottom-10% forced curve | **Manager-led quarterly calibration** tied to the engineering career ladder (code quality, delivery impact, unblocking others, reliability) — creating a defensible dossier if a real *verbetertraject* is ever needed |

### Why This Works Better
- **Zero gaming:** Teams optimize for shipping working software together rather than splitting 1-line PRs or accepting bloated AI completions.
- **Protects senior leverage:** Code reviews, architecture, mentoring, and incident response stay valued.
- **Legally clean in the Netherlands:** Aggregate team metrics avoid individual surveillance issues under the AVG and WOR, while structured manager-led reviews hold up under Dutch employment law.
