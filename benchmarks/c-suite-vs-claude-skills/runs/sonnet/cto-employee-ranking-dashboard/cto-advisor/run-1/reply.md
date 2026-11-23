## Bottom Line

You can push back without being difficult, and you probably should. Don't argue "this is wrong". Argue "this won't get you what you want, and it creates risks for you". Then bring a better proposal. In the Netherlands you also have a procedural lever that makes the pushback routine rather than personal: the works council.

Confidence: high that the metrics are unfit for ranking people. Medium on the Dutch legal points, because I'm not your lawyer and the details depend on your company's setup. Check them before you quote them.

## What is wrong with the plan

**1. Neither metric measures what the VP cares about (confidence: high).**
- *Copilot acceptance rate* measures how someone interacts with a suggestion tool. It says nothing about the quality or value of the work. A careful engineer who rejects bad suggestions scores low. Someone who accepts everything and fixes it later scores high. Engineers who work on legacy code, unusual stacks or hard design problems get fewer useful suggestions. The number also drifts with the language and the type of task.
- *PRs merged* rewards small, frequent PRs and punishes the people we most want: the engineer who spends a week on a design that removes a whole class of bugs, the reviewer who unblocks five colleagues, the mentor, the person on incident duty. These are exactly the things that go untracked.
- Neither metric appears in the standard engineering metrics frameworks (DORA, SPACE). Both explicitly warn against individual output metrics. The frameworks I work from list individual velocity and commit counts as things not to measure, because they create competition and get gamed.

**2. Goodhart's law will hit within weeks (confidence: high).** Once a number decides who lands on a plan, it stops measuring work and starts measuring gaming. Expect PRs split into trivial pieces, suggestions accepted without thought, and AI-generated code that nobody understands. Review quality and shared ownership go down, and incident rates go up, while the dashboard looks great.

**3. A "bottom 10%" is a quota, not a performance finding (confidence: high).** Someone is always at the bottom, even in a team where everyone performs well. Forced ranking also pushes people to avoid helping colleagues, since helping lowers their own numbers. It makes your best engineers update their CVs, because they see the system and know it doesn't describe them. At 300 people you can't afford to lose the senior engineers who hold the system knowledge.

**4. Weekly cadence is noise (confidence: medium).** One week of PR counts is mostly vacation, on-call, sprint timing and PR size. Ranking on it means you are mostly ranking luck.

**5. Dutch context (confidence: medium, verify with HR/legal or your works council).**
- A company with 50 or more employees is required to have a works council (ondernemingsraad). Under the Works Councils Act (WOR, art. 27), employee assessment systems and systems that record or monitor employee performance generally need the works council's consent *before* introduction. A weekly individual ranking built from tool telemetry looks like a textbook case. If your VP is rolling this out without the OR, that is the strongest point you have.
- The data is personal data under the AVG/GDPR. Using it to rank people and trigger HR consequences needs a legal basis, proportionality, and transparency to the employees. "We had the dashboard anyway" is weak.
- A verbeterplan matters in Dutch employment law because it's the first step toward a dismissal for poor performance. Dismissal on those grounds requires a fair assessment, a clear and reasonable improvement opportunity, and a record. A plan triggered by a bottom-10% ranking on two proxy metrics is a poor record, and could hurt the company if it ever got that far. That is a risk the VP will care about even if they don't care about the engineers.

## What you can actually do

Be honest with yourself about your position: you're a senior engineer, not the decision-maker. The goal is to get the decision made on better information, not to win. Roughly in order:

1. **Ask questions first, in a 1:1 (this week).** Don't open with "I think it's wrong". Open with: "What problem are we trying to solve? Is it throughput, quality, AI adoption, or people we're worried about?" A new VP usually wants visibility and a way to show results. Once you know the actual goal, you can offer a better way to meet it. If the real goal is "make sure Copilot spend pays off", that's a different and easier problem.

2. **Offer a replacement, not just an objection.** Something like: "Here's how I'd get you that visibility without the risks."
   - Measure the *team*, not individuals: DORA metrics (deploy frequency, lead time, change failure rate, time to restore), plus PR cycle time and review turnaround.
   - Track Copilot adoption and impact at team level (usage, and whether lead time and defect rates change), not per-person acceptance rates.
   - Add a short developer survey and an on-call load metric, so you see friction and burnout early.
   - Handle individual performance the normal way: managers with context, 1:1s, peer feedback, concrete examples. Metrics can start a conversation but never end one.

3. **Offer to run a small pilot.** "Let's look at team-level data for 6 weeks and see what it tells us before we attach consequences." That is easy to say yes to, and it gives the data a chance to show its own limits.

4. **Run a quick sanity test with real data, if you can get it.** Ask for the numbers for the last 4 weeks and check: do the same people stay at the bottom? Do known-strong engineers (the ones who do reviews, incidents, mentoring) rank low? If the bottom 10% turns out to be your tech leads and your on-call heroes, that's a convincing, non-personal argument. If you can't get the data, a dry-run on your own team is enough.

5. **Raise the process point with the right people.** Ask HR and the works council, neutrally, whether this has gone through the OR (art. 27 WOR) and whether a privacy assessment has been done. Framed as "I want to make sure we do this properly", this reads as diligence. If you are an OR member, or know one, the OR may do the pushing for you.

6. **Line up allies.** Talk to a few other seniors and tech leads before the meeting. One engineer objecting looks like resistance. Several people raising the same practical concerns look like a signal about the organization. Tech leads and their managers also lose the most from the quota, and they have more standing than you.

7. **Protect yourself and your team in the meantime.** Keep a short written record of what you raised and when. Don't game the numbers, and don't tell your team to. If the ranking goes live anyway, help colleagues understand it and keep your reviewing and mentoring visible in other ways, such as in 1:1s and written feedback.

## How to say it without being "difficult"

A few phrasings that stay on the VP's side:
- "I want this to work, so I'd like to check it against what we know about our own team first."
- "I'm worried the numbers will get gamed, which would give you worse visibility than you have now."
- "Can we start with team-level numbers and add individual data if the pilot shows it's reliable?"
- "Do we need to take this through the OR first? I'd hate for it to be stopped later."

Avoid "this is unfair", "this is demoralizing", or anything about the VP's judgment. Talk about outcomes and risk instead.

## Your Decision

- **Do now:** book a 1:1 with the VP and ask what problem the ranking is meant to solve. Bring a one-page team-level alternative.
- **If they won't move:** raise the works council and privacy questions through HR, and gather allies. Escalating through legitimate channels is not being difficult.
- **If it goes live regardless:** keep your own conduct clean, document your concerns, and support colleagues who end up on plans, including pointing them to the OR and, if needed, a legal adviser or union.

One check on me: I don't know your VP, your company culture, or whether an OR already exists and has been consulted, so tailor the order of these steps to what you know. If the VP is open to evidence, steps 1 to 3 may be all you need. If they've made up their mind, step 5 is where the leverage is.
