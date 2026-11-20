This is one of the toughest spots to be in as a PM, and how you handle the next 48 hours matters more than the capacity math itself.

The goal isn't to prove the CEO wrong—it's to **make yourself their partner in keeping the promise without blowing up the company's other commitments**. If you lead with "You didn't ask us" or "We don't have capacity," it turns into a tug-of-war. If you lead with trade-offs and solutions, you stay on the same side of the table.

Here is a step-by-step way to handle it.

---

### 1. Do 24 hours of quiet homework before reacting
Before you book time with the CEO, get the facts so you aren't negotiating in the dark:

- **Find out what was *actually* promised.** Was it written in an email or SOW, or mentioned verbally on a call? Customers often care about a specific outcome by Q1, not necessarily the full, gold-plated version of three features.
- **Size the work with your Tech Lead / EM.** Don't do a two-week discovery—just get rough T-shirt sizes and answers to three questions:
  1. What is the **minimum viable version (MVP)** of these three features that would genuinely satisfy the customer in Q1?
  2. What **currently on the Q1 roadmap** has equivalent effort if we had to swap?
  3. Are there any **temporary workarounds** (manual ops, config, existing functionality) that buy time on one of the three?

---

### 2. Bring options, not a "no"
CEOs hate hearing "we can't." They respond much better to *"Here is how we can do it, and here is what each path costs."* Put together a simple 1-page summary (or 3-slide deck) with three concrete choices:

* **Option A: Hit the Q1 customer promise via a roadmap swap (Recommended if the customer deal/renewal depends on it)**
  * *What happens:* We ship the 3 features (or their Q1-viable MVPs) by end of Q1.
  * *The trade-off:* We pause `[Roadmap Item X]` and `[Roadmap Item Y]` and push them to Q2.
  * *Business impact:* Clearly state what breaks or slips if X and Y move (e.g., *"Delays self-serve onboarding by 6 weeks, which affects ~15 mid-market prospects"*).

* **Option B: Phase the promise with the customer**
  * *What happens:* We ship Feature 1 (or the core workflow of all 3) by end of Q1, and deliver the rest in early Q2.
  * *The trade-off:* Keeps `[Roadmap Item X]` on track, but requires going back to the customer to align on a phased rollout (which you can offer to help frame as a joint win/beta).

* **Option C: Keep both (Capacity / Quality reality check)**
  * *What happens:* Trying to do all of it with the current team.
  * *The trade-off:* Be direct and unemotional here—*"At current capacity, committing to both means one of two things: we miss the Q1 date for the customer, or we ship unstable code that creates support fire drills in Q2."* (If contractors or borrowing engineers from another squad is genuinely viable for Q1, list it; if ramp-up time means they won't help by end of Q1, say so plainly.)

---

### 3. How to run the 1:1 conversation
Frame the meeting around **helping the CEO succeed**, not defending your backlog. A script you can adapt:

> *"I want to make sure we deliver for [Customer]—I know how important that relationship is. I sat down with [Tech Lead] to map out what it takes to get those three features live by the end of Q1.*
>
> *Since the team is already 100% allocated to [Existing Q1 Goal], we can't absorb all three on top of the current plan without missing dates or breaking quality. So I put together three ways we can make this work, depending on what's highest priority for the business right now.*
>
> *Option A gets all three to [Customer] by Q1 if we move [X and Y] to Q2. Option B keeps [X] on track if we can phase the customer delivery. Which trade-off makes the most sense to you?"*

Why this works:
- **Zero blame.** You didn't scold them for bypassing the process.
- **You protected their credibility.** You're actively trying to help them honor their word.
- **The trade-off belongs to the CEO.** Instead of *you* saying "no" to the customer, the *CEO* decides whether delaying `[Roadmap Item X]` is worth it.

---

### 4. Follow up in writing immediately
Right after the meeting, send a short recap in Slack or email:
- What was decided (e.g., *"Confirmed: we're prioritizing the 3 [Customer] features for Q1 and moving [X, Y] to Q2"*).
- Who is communicating any downstream impact (e.g., Sales, CS, or other stakeholders expecting X and Y).

This prevents revisionist history later in the quarter when someone asks why `[Roadmap Item X]` isn't done.

---

### 5. Fix the root cause *after* the fire is out
Don't bring up process in the middle of the crunch—it will sound defensive. Wait until Q1 is settled (or during a calmer retro), and frame a lightweight fix around **protecting the CEO from getting burned**:

> *"I want to make sure you never get put in a spot where a date you give a key customer is at risk. Next time a big customer asks for something custom on a tight timeline, can we do a quick 15-minute check with me and [Tech Lead] before locking a date? Even a rough sanity check lets you promise with confidence—or give them a date we know we can beat."*

Keep it to a 15-minute sanity check, not a committee or a ticket intake form. A CEO will usually agree to something that protects their own credibility with top customers.
