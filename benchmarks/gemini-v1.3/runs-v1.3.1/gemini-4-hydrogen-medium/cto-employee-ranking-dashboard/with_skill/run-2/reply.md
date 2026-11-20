Don't fight the VP head-on—redirect the goal to **team-level delivery metrics** and let **Dutch works council (*ondernemingsraad*, OR) governance** do the heavy lifting. At a 300-person company in the Netherlands (where an OR is mandatory from 50 employees), using per-person Copilot and PR data to put the bottom 10% on improvement plans likely requires OR consent under Article 27(1)(l) of the Works Councils Act (*WOR*)—this isn't legal advice, so check with HR or an OR member, but it gives you a neutral, process-based way to pause it without looking "difficult."

### Why this approach works
Leaders usually ask for individual rankings because they want faster delivery or proof that AI spend is paying off. Weekly rankings on PRs merged and Copilot acceptance rate backfire on both:
* **They punish glue work:** Engineers who review PRs, mentor, fix incidents, or delete dead code merge fewer PRs.
* **They measure usage, not speed:** Accepting AI suggestions blindly raises rework. In a 2025 METR randomised trial, experienced open-source developers took **19% longer** with AI tools even though they felt faster.

### What to do next
1. **Start 1-on-1 with your manager or skip-level, not in a group channel.** Frame yourself as helping the VP get real visibility, not blocking accountability.
2. **Offer a concrete alternative.** Propose a team-level view: **DORA metrics** (change lead time, deployment frequency, change fail rate, recovery time) plus **PR review wait time** and **unplanned work**. That shows where delivery is actually stuck.
3. **Ask the governance question neutrally.** Mention that per-person monitoring tied to PIPs usually triggers OR consent under WOR Article 27(1)(l), and ask if HR and the OR have signed off. (If leadership pushes ahead anyway, quietly flag it to an OR representative—sticking strictly to facts, with no speculation about motives.)
4. **Don't carry it alone.** Align with one or two other senior engineers or engineering managers before raising it, and keep any notes factual and within data-protection rules.

### A line you can use
> "I want the VP to get clear visibility into delivery speed and whether Copilot is helping. My worry is that individual PR and acceptance-rate rankings penalise people doing code reviews and incident work, and in the Netherlands per-person monitoring for PIPs usually needs OR consent under Article 27 WOR. Could we show them a team-level DORA and review-bottleneck view instead?"

I've saved a one-page breakdown and talking points you can adapt in [engineering-metrics-alternative.md](file:///G:/agy-bench/ws/a924302dd3b8/engineering-metrics-alternative.md).

What am I missing, and what would make this wrong?
