**Bottom Line:** Don't buy a separate tool for this. Use the usage and acceptance dashboards that come with the assistant you choose, and show them per team, not per engineer. A named list of low adopters is the wrong thing to build.

**What**
- 🟢 Every major assistant (GitHub Copilot, Cursor, Claude Code and others) already ships an admin dashboard with active users, usage and suggestion acceptance. A third-party tool adds cost and one more vendor dependency for no gain. My default is buy, but only when nothing you already have covers the need, and here something does.
- 🟡 If you later want delivery context next to adoption (cycle time, PR merge time, change failure rate), Swarmia or LinkedB are the kind of tool to look at. Run a short trial, and ask them to confirm team-level views and German and Dutch data-protection terms.

**Why not per-engineer follow-up**
- 🟢 Individual output metrics create competition and get gamed. Once usage is a target, people accept suggestions they don't want so their numbers look good (Goodhart's law).
- 🟢 A low acceptance rate is not low performance. It often means the engineer is careful or works on code the tool handles badly.
- 🟡 Legal exposure is real in both countries. In Germany, a system that can monitor employee behaviour or performance normally needs works council agreement (BetrVG §87(1) no. 6). In the Netherlands the works council has a consent right over personnel monitoring systems (WOR art. 27). GDPR purpose limitation and transparency also apply. 🔴 I'm not a lawyer and haven't seen your works council agreements, so have legal confirm before rollout.

**How to act**
1. Choose the assistant on code quality, security and your stack, with a 4-week pilot across both offices.
2. Report by team and office: weekly active users, and how usage relates to PR cycle time and review load.
3. For low adoption, ask why. Run a short survey and hold manager conversations about blockers such as licences, training, repo coverage or trust. Offer pairing sessions and champions in each team.
4. Agree the metrics with the works councils before launch. Say in writing that individual data is not used for performance reviews.

**Your decision:** Are you willing to drop the per-engineer view in exchange for faster works council sign-off and higher trust? I recommend yes. If you want to push back, tell me what the managers need to decide that team-level data can't tell them.
