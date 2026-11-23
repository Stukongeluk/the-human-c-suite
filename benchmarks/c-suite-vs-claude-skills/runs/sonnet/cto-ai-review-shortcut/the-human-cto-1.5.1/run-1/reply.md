Half of it: yes to AI coding agents for everyone from January, no to dropping review for small changes. Review is the one place where the speed-up turns into incidents.

**Why not drop review**
- Faros AI (10,000+ developers, 2025): on high-adoption teams, merged pull requests rose 98% but review time rose 91%. Review is already the bottleneck, so cutting it for "small" changes hides the problem instead of fixing it.
- Veracode (2025): AI-generated code introduced OWASP Top 10 vulnerabilities in 45% of test tasks. GitClear found code duplication up 81%.
- DORA 2025: AI amplifies what you already have. Without strong review and tests, it amplifies the weaknesses.
- "Small" is where agents hurt most: small diffs get waved through, and many small diffs add up.

**What I'd do instead**
1. Roll out agents in January, with training and paid learning time. Reversible and cheap.
2. Keep review, but make it faster: small PRs, a review SLA (for example, first response within 4 working hours), automated tests, linting and security scans as the first gate, and a lighter review for low-risk areas such as docs, config and tests.
3. Baseline now: lead time, review wait, change fail rate, escaped defects. Compare after 8-12 weeks. If small changes prove safe, relax the rules for those paths using your own data.
4. Don't promise a speed-up number to anyone yet. Measure it first.

**Two questions that would change my answer**
- What is the actual bottleneck today: writing code, review wait, or releases?
- Do you have automated tests and a change fail rate you trust?

What am I missing, and what would make this wrong?
