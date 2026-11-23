# Q1 plan: ship the rebrand without leaving behind the customers it's for

**Bottom line**
Deliver the rebrand in Q1, but don't plan it as "everyone works on the rebrand." Split it into two parts. The launch core (name, look, domain, site) ships in Q1. The full design-system migration runs on into Q2 and Q3. Keep the teams that own invoicing, the accounting integration and reporting working on those three problems. Then put that trade-off to the CEO as one clear decision before Q1 starts. Overall confidence: **Medium**. I'm confident about the direction, but the exact split depends on sizing and revenue data you can gather in the next three weeks.

*How I've labelled each point: **High** = from your message or a well-established pattern · **Medium** = reasonable inference · **Assumed** = not checked yet, so verify it.*

---

## What I see

- **Customers are losing faith in the product.** NPS dropped 24 points (+28 to +4), and three complaints about core money workflows have been open for months *(High, from your message)*. That's the classic sign of slipping product-market fit among existing customers. A merger followed by a rename is exactly when customers reconsider their vendor *(Medium)*.
- **A new name on unchanged invoicing tells customers "they spent the quarter on a logo."** A rebrand needs proof that something got better. Three fixed complaints would be that proof *(Medium)*.
- **The rebrand and the complaints overlap technically.** A new domain affects the same areas customers already complain about *(High as a pattern, Assumed for your stack)*:
  - invoice emails: a new sending domain has no reputation yet, so invoices can land in spam
  - the accounting integration's OAuth login settings with each accounting provider
  - SSO (single sign-on) settings at every enterprise customer
  - payment links in invoices you've already sent

  The team fixing the integration should also own moving it to the new domain.
- **"The whole org" is probably more capacity than the rebrand needs.** The name, logo, theme and domain are weeks of work for a few teams. Marketing mostly owns the marketing site. The long pole is rebuilding every screen in a new component library, and that can be phased *(Medium, needs sizing from the teams)*.
- **A 100% rebrand quarter is never really 100%.** On-call, incidents and security fixes often take 10–20% of capacity *(Assumed range)*. Being honest about the real split is part of a credible plan.

## Why this matters
If Q1 is rebrand-only, the three complaints wait at least another quarter on top of the months they've already been open. Customers renewing in the first half of the year will judge you on that experience, not on the new name. A plan that does both lets the launch say: "new name, and we fixed what you told us about."

## How to act

1. **Build the customer evidence pack.** Tag detractor comments by theme. List the revenue and renewal dates of the accounts raising the three issues. Add ticket counts, the integration's failure rate and invoice time (p95, the time 95% of invoices finish within). Personally call 10 detractors this week. → *You, with Customer Success, RevOps and data* → **Fri 4 Dec**
2. **Size the work from the bottom up.** Split the rebrand into "launch core" and "full design-system migration," and size the three fixes. → *You, with the VP Eng/CTO, design lead and platform lead* → **Fri 11 Dec**
3. **Bring a one-page decision to the CEO** with options A, B and C and a recommended default (draft in the attached plan). → *You* → **decision in the week of 14 Dec**, so teams start Q1 on 4 Jan with a settled plan.
4. **Run Q1 as two tracks with one weekly review.**
   - Rebrand: theme first, then the in-app name and emails, then the domain. Keep the old domain working for years, not weeks. Launch in late March.
   - Customer recovery: fix the integration first, then invoicing speed, then reports (talk to customers before building).

   Hold a rebalancing checkpoint on **Fri 26 Feb**. → *You, with both track owners* → **weekly from 4 Jan**
5. **Build every screen you touch for the fixes in the new design system.** Invoicing and reports then become the showcase screens of the launch, and the two tracks help each other. → *Head of Design* → **from week 3**

## Risks
- **The three complaints might not be what drove NPS down.** For example, the cause could be pain from moving customers between the merged products. The evidence pack tests this first. If the data points elsewhere, follow the data.
- **The Q1 date might be fixed by something external** (trademark, merger agreement, contract). If so, the launch core can't slip. Option B protects it, but find out before the CEO meeting.
- **A botched domain cutover would hit the customers who are already unhappy.** It could break SSO, webhooks or invoice delivery. Run both domains in parallel, warm up the new email domain gradually, and give enterprise IT teams at least 6 weeks' notice.

## Your decision (to take to the CEO)

| | What happens | Trade-off |
|---|---|---|
| **A. Everyone on the rebrand, as decided** | Fastest full design-system rollout | Complaints wait until at least Q2, and the launch lands on an unchanged product. If chosen: ask for a small named team to treat the broken integration as a defect, tell affected customers when fixes will come, and write down the accepted risk. |
| **B. Rebrand core in Q1 plus protected customer recovery** *(recommended)* | New name, look, domain and site launch in Q1. Component migration runs through Q3. The teams that own invoicing, integrations and reports stay on the fixes (my rough guess before sizing: about a quarter of capacity). | Full visual consistency across every screen arrives one or two quarters later. |
| **C. Fix first, rebrand in Q2** | Best for customers in the short term | Reverses a leadership decision and drags out the two-brand confusion. I wouldn't lead with it. |

**Recommendation: B.** It delivers what leadership decided and gives the launch something real to announce.

**How to take it to the CEO:** take "any decision beats no decision" at face value. Bring a decision that can be made in one meeting, with a default and a February checkpoint so it's cheap to change. "Leadership decides" is fine too: your job is to make sure they decide with the cost in front of them. Then execute whatever they pick, fully and in the open. Don't run a quiet side roadmap.

**Not yet checked:** revenue at risk (CFO/Customer Success), sizing (VP Eng), launch dependencies (CMO). Treat anything above about your specific systems as an assumption until those come back.

**Detail:** I've attached `q1-plan.md` with the week-by-week plan for both tracks, a domain-migration checklist, the Q1 scorecard, a one-page CEO memo and the assumptions that would change the plan.
