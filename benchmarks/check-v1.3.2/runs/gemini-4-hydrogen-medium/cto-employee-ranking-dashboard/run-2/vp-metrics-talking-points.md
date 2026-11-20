# Responding to Individual Copilot & PR Rankings

A practical guide and ready-to-use alternative for a 1-on-1 with your VP of Engineering.

---

## 1. The 1-on-1 Script (Private, Constructive, Protective)

**Goal:** Position yourself as an ally helping a new VP avoid a predictable engineering and legal trap—not as someone resisting accountability.

> "Welcome to the team—I want this to go well for you, which is why I'm bringing this to you privately first.
>
> Two things on the weekly Copilot acceptance + PRs-merged ranking:
>
> First, on the engineering side, those numbers will give you the wrong signal. Engineers who review a lot of PRs, handle incidents, mentor juniors, or simplify and delete code will drop to the bottom, while anyone who splits one change into five tiny PRs or accepts boilerplate suggestions will rise to the top. Even in controlled studies (like METR's 2025 trial), experienced developers using AI tools took 19% longer on tasks while feeling faster—so acceptance rate doesn't reliably track value.
>
> Second, in the Netherlands at our size (300 people), rolling out individual activity rankings tied to PIPs usually triggers the Works Council's (OR) consent right under Article 27(1)(l) of the Works Councils Act (WOR) for performance-monitoring systems. *(Not legal advice—worth checking with HR before anything is published.)*
>
> If your real goal is to see where delivery is slow or where AI is actually helping, I'd love to help you put together a team-level dashboard—lead time, review wait time, change fail rate, and rework—in the next two weeks. And for genuine individual performance issues, managers can handle those through regular feedback and work quality."

---

## 2. What to Offer Instead: Team-Level Delivery & Health Metrics

Pair every speed metric with a quality or health metric so nobody can hit one target by breaking something else. Compare each team against its own past, not against other teams.

| Question | Team-Level Metrics | Source |
|---|---|---|
| **How fast and safely do we deliver?** | Change lead time, deployment frequency, change fail rate, failed deployment recovery time, deployment rework rate (DORA) | CI/CD, deployment logs, incident tool |
| **Where does work get stuck?** | Review wait time, cycle time per stage, work in progress (WIP) per team, PR size | Git hosting, Jira / Linear |
| **How much capacity goes to unplanned work?** | Share of unplanned work, incidents per service, time spent on toil/maintenance | Incident tool, issue labels |
| **Is the system & team healthy?** | SLO availability, on-call pages outside working hours, developer experience pulse | Observability, incident tool, surveys |

**How to measure Copilot honestly:** Track team delivery and quality metrics (lead time, rework rate, change fail rate) before and after adoption, or with a voluntary comparison group—never via per-person acceptance leaderboards.

---

## 3. If the Private Conversation Doesn't Work

1. **Stay factual and calm.** Don't debate it in public channels or speculate about the VP's motives. Keep notes on what was proposed, when, and what you raised.
2. **Use the right internal channels in order:**
   - **Your manager or skip-level:** Share the delivery-risk and WOR-consent concern briefly.
   - **HR / People:** Ask neutrally whether the proposed individual tracking has been checked against Works Council (OR) requirements.
   - **Works Council (OR):** At 300 employees in the Netherlands, individual performance-monitoring dashboards fall squarely under the OR's remit (Article 27(1)(l) WOR). Let the formal governance channel carry the weight so you don't have to fight it alone.
3. **Protect yourself:** Only keep records you are entitled to keep, and never breach confidentiality or data-protection rules.

---

## Sources

- DORA metrics (including deployment rework rate): [dora.dev](https://dora.dev/guides/dora-metrics/history/)
- SPACE developer productivity framework: Forsgren et al., *ACM Queue* (2021)
- Measuring developer productivity & gaming risks: Gergely Orosz & Kent Beck, *The Pragmatic Engineer* (2023)
- AI coding tools randomised trial: METR (2025)
- Dutch Works Councils Act (Wet op de ondernemingsraden, Article 27(1)(l)): check with your HR / legal counsel (this document is not legal advice)
