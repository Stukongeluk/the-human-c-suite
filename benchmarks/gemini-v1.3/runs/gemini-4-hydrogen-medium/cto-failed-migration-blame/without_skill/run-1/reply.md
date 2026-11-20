**Do not fire the platform team lead—at least not as a reaction to the outage, and not before a full post-mortem.**

Unless the investigation uncovers willful negligence, dishonesty, or a deliberate bypass of established safeguards, firing the lead is the wrong move both operationally and culturally. A €2M, 9-hour outage is a **systemic failure**, not a single-person failure. No individual should be in a position where one mistake or one bad migration plan can take down the business for nine hours.

At the same time, you cannot simply tell the board "we don't do blame." A €2M hit is a serious business failure, and the board is right to demand accountability. Your job is to **redirect their demand for a scapegoat into real executive accountability and measurable risk reduction.**

Here is what you should do, in order:

---

### 1. Align with the CEO Immediately
Before you go back to the board, get on the same page with your CEO. Explain two things:
* **Operational risk:** The platform lead holds critical institutional knowledge of the database and the incident. Removing them right now destabilizes the team while you are still hardening the system.
* **Chilling effect:** Firing the person who ran a high-risk migration signals to every senior engineer that owning hard infrastructure work is career-ending. Your best people will either leave or become risk-averse and hide problems.

### 2. Separate "Accountability" from "Firing" for the Board
Tell the board directly: **"As CTO, the engineering guardrails and readiness standards are my responsibility. I am accountable for this."**

Then draw a clear line:
* **If there was misconduct or reckless disregard** (e.g., ignoring an explicit block, faking test results, hiding risks), you will take disciplinary action, up to termination.
* **If it was an engineering and process failure**, firing the lead doesn't fix the system—it just guarantees the next person can make the exact same mistake.

Commit to delivering a **Root Cause & Remediation Brief** within 5–7 business days with hard dates and owners.

### 3. Focus the Post-Mortem on Two Questions
A 9-hour outage usually has two distinct failures:
1. **Why did the migration fail?** (e.g., lock contention, data skew, staging not matching production scale/volume, missing dry run).
2. **Why did it take 9 hours to recover?** (e.g., untested rollback, slow backup restore, destructive forward-only schema changes, unclear incident command).

Boards care deeply about the second question. Cutting recovery time from 9 hours to 30 minutes is concrete risk mitigation they can understand.

### 4. Put Concrete Guardrails in Place (and Report Them)
Give the board specific, verifiable changes rather than vague promises to "be more careful":
* **Mandatory dry runs & rollback verification:** No database migration runs in production without a tested, timed rollback/failback plan validated against production-scale data.
* **Two-key sign-off for high-blast-radius changes:** Require independent peer/architecture review and explicit go/no-go criteria (including abort thresholds) before execution.
* **Zero-downtime migration standards:** Enforce backward-compatible, phased schema changes (e.g., expand-and-contract) so a bad deploy doesn't require a multi-hour restore.
* **RTO/RPO drills:** Schedule regular, timed database restore drills to prove recovery times meet business tolerances.

### 5. Evaluate the Platform Lead Fairly—and Privately
Have a candid 1:1 with the lead today:
* Shield them from board politics right now so they can focus on stabilizing the platform and contributing honestly to the post-mortem.
* Still hold them to a high bar. Once the facts are in, assess their **judgment and preparation**: Did they flag risks beforehand? Did they push back on an unrealistic timeline, or rush? Did they skip known steps?
* If there are genuine capability or leadership gaps (e.g., poor planning, inability to manage risk under pressure), address them through coaching, scope adjustment, or a formal performance plan—not a public execution to appease the board.

### 6. Communicate Clearly to the Engineering Org
Rumors spread fast after a major outage, especially if leadership is rattled. Tell the team:
* What happened at a high level and the business impact.
* That the post-mortem will be rigorous and blameless—focused on systems, tooling, and recovery time.
* That you are owning the conversation with leadership and the board.

---

**The bottom line to take to your board:**  
*"Firing the lead gives us the illusion of accountability while leaving the exact same failure modes in place. Keeping them while fixing our migration gates, rollback testing, and recovery time actually protects the company from another €2M weekend—and I will personally report back on those milestones until they are closed."*
