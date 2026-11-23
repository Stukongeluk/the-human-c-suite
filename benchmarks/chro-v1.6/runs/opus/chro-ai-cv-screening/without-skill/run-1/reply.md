I've written up the rollout plan (attached: **rollout-plan.md**), but not for the setup you described. Auto-rejecting the bottom 70% without a recruiter looking is the one part I'd advise against. In all three countries it is very likely unlawful as configured, and it would also cost you candidates you need. You can get most of the time saving with a recruiter still making every rejection.

## Why not auto-reject

- **GDPR Article 22.** Software rejecting an applicant on its own is the textbook case of a solely automated decision with significant effect. Recital 71 names "e-recruiting practices without any human intervention" as an example.
  - The exceptions are narrow. "Necessary for entering into a contract" is the only plausible one, and it's hard to argue when checking the rejected pile by hand costs about 0.3 FTE (see below).
  - Even if that exception held, every rejected applicant would still be entitled to human review, the right to contest, and meaningful information about the logic. That's 2,800 people a month.
  - The CJEU's SCHUFA ruling makes things stricter: a score that the decision draws heavily on can itself count as the automated decision. "A recruiter could look if they wanted to" doesn't get you out of it.
- **Works councils set the real timeline.**
  - In the Netherlands, the OR has a consent right over hiring policy (WOR art. 27(1)(d)). A decision made without that consent can be voided.
  - In Germany, the Betriebsrat co-determines technical systems that can monitor staff (§87(1) no. 6 BetrVG) and selection guidelines, explicitly including AI-assisted ones (§95(2a)).
  - In Belgium you have information and consultation duties (CAO/CCT 39), and the recruitment rules of CAO/CCT 38 apply.
  - Switching on first and consulting afterwards is the quickest way to have it switched off for you.
- **EU AI Act.** CV screening is explicitly high-risk (Annex III, point 4(a)).
  - Under the Digital Omnibus, in force since 27 July 2026, deployer duties for these systems apply from **2 December 2027**. They include human oversight by trained staff with authority to override, logs, informing candidates, and monitoring. Building to that now saves rebuilding in a year.
  - Emotion recognition is already banned, and the Commission says the ban covers hiring. Get written confirmation that the module does no video or voice "sentiment" analysis.
- **The vendor's claims don't move the risk off you.**
  - No model is bias-free. A vendor that claims it without test results broken down by group is giving you a warning sign, not reassurance.
  - "GDPR-compliant" describes their software, not how you use it. You are the controller, and whether an automated rejection is lawful depends on your deployment.
  - Discrimination liability stays with you. In Germany, under the AGG, a rejected applicant only has to show indications of discrimination for the burden of proof to shift to you.
- **It's bad for hiring.**
  - A fixed 70% cutoff rejects 70% whatever the pool looks like. For a warehouse or store vacancy with eight applicants, it throws out five or six people you probably need.
  - CV scoring also penalises thin-CV applicants: students, career-returners, people new to the country. They make up much of the frontline talent pool.
  - That adds up to around 33,000 applications a year turned away by a machine, and many of those applicants are your customers.

## What the plan does instead

**The AI sorts, summarises and fast-tracks. A person decides every rejection.**

- **Must-haves come first.** Right to work, any legally required minimum age, shift availability and licences are shown before people apply, so candidates can self-select. That's transparent, unlike a hidden score.
- **Scoring is criteria-based.** The model scores against criteria you define for each role family. Photo, name, age, gender, nationality and address are removed before scoring.
- **Three bands:**
  - Top: a recruiter fast-tracks the candidate within 48 hours.
  - Middle: normal review.
  - Bottom ("recommended reject"): a recruiter opens each application with the CV and reason codes side by side and confirms or overrides it. There is no bulk-reject button.
- **Thresholds per role family.** Low-volume and shortage roles get no bands at all.
- **Clear rejections.** Rejected candidates get a clear message, the main reason category, and a way to ask a person for a second look.

**What keeping humans in costs:** 2,800 bottom-band CVs at about a minute each is roughly 47 recruiter hours a month, about 0.3 FTE across the group. On the working assumptions in the plan (swap in your real numbers), assisted screening still cuts screening time by about half. Full auto-reject would save that last 0.3 FTE and take on all of the risk above.

## Timeline

| Phase | Weeks | What happens |
|---|---|---|
| 0. Hold | 0–1 | Auto-reject stays off; owners named; principles agreed |
| 1. Groundwork | 1–10 | Vendor due diligence and paired CV tests, DPIA, criteria per role family, works council processes opened in week 2 |
| 2. Shadow pilot | ~10–20 | Model scores 3 role families (one each in NL, BE and DE) with scores hidden from recruiters. Compared with what recruiters actually did, against agreed go/no-go criteria |
| 3. Assisted go-live | ~20–32 | Pilot roles first, then other high-volume role families in waves |
| 4. Run | ongoing | Monthly bias and override monitoring, stop conditions, AI Act readiness well before December 2027 |

Realistically, expect about 5 months to live assisted screening in the first roles. The German works council negotiation usually sets the pace. I'd propose a two-step agreement: pilot first, then the rollout based on the pilot data. Works councils tend to accept that faster than a full rollout up front.

## This week

1. Leave the module off. Don't enable auto-reject, and don't score live applicants until the DPIA covers it.
2. Send the vendor the 12 due-diligence questions in section 4 of the plan. Their answers will quickly show whether "bias-free" means anything.
3. Brief your DPO and employment counsel in each country, and put the topic on the agenda with the OR, the Betriebsrat and the Belgian works council.
4. Pick the three pilot role families. I'd suggest one e-commerce office role, one warehouse or logistics role and one store role.

This reflects the law as it stands now, but it isn't legal advice, so have counsel in each country confirm the specifics. Next I can draft the works council request, a sendable version of the vendor questionnaire, or the candidate notice and rejection templates in NL/FR/DE/EN.
