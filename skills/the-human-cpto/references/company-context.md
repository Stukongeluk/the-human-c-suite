# Company context brief

Good advice for one company can be terrible advice for another. Before recommending anything, know the company you are advising: what kind of organisation it is, its strategy, money, people, history and constraints. This file is the template for a **company context brief** and says where to find each part.

## Contents

1. How to build and keep the brief
2. The brief (template)
3. Where to look, and what to search for
4. Keeping it current: dates, staleness and up-to-date practice

## 1. How to build and keep the brief

1. **Look for an existing brief first.** Check the project or working folder (for example `company-context.md`), your memory or notes from earlier sessions, and the knowledge base (search for "company context", "strategy", "about us"). Read it, then refresh what is stale instead of starting over.
2. **Discover every source you can reach.** List the connected tools and MCP servers, then use each relevant one read-only. More independent sources make a better picture, as long as each one is trustworthy.
3. **Prefer systems of record over hearsay.** The general ledger beats a slide; the HRIS beats a guess; Git and Jira history beat someone's memory of who built what.
4. **Triangulate.** Check important claims against a second, independent source. When sources disagree, say so and show both.
5. **Date everything.** Every fact in the brief gets its source and an "as of" date.
6. **Name the gaps.** List what you could not find and ask for it. Never fill gaps silently with assumptions; label any assumption as one.
7. **Keep it.** Offer to save the brief (for example as `company-context.md`, or a page in the knowledge base) so the next decision starts from it, and update it whenever you learn something material. Only write it somewhere with the user's approval.
8. **Respect privacy.** The brief describes the company, teams and aggregated people data, never personal circumstances of individuals.

## 2. The brief (template)

```markdown
# Company context brief: <company>
As of <date> · Sources: <list> · Gaps: <list>

## Identity and strategy
- Kind of organisation: ownership (founder and investors, family, listed, fund-owned with an exit horizon, employee-owned or cooperative, non-profit, public), sector, size and stage ([company-types.md](company-types.md))
- What we sell or provide, to whom, and why customers, patients or citizens choose us (or can't choose anyone else)
- Strategy and current priorities (OKRs, strategy pages, board papers)
- Business model and how the company makes money; key markets
- Ownership and governance: shareholders, investors, board/supervisory board, works council

## Money
- Revenue, growth, gross margin, EBITDA (last 3 years + current year to date)
- Cash, burn, runway; debt and covenants
- Opex by category and its trend; biggest contracts and renewal dates
- Budget cycle and who approves what

## Customers and market
- Main segments, retention/churn, NPS/CSAT trends, top complaints
- Competitors and how we compare; market trends that matter now
- Regulation and compliance obligations that shape decisions

## Operations, products and technology
- How the work gets done: plants, stores, wards, depots, sites or offices; capacity, service levels, quality and safety record
- Products, platforms and their owners (CODEOWNERS, service catalogue)
- Architecture and key systems; technical debt hot spots
- Delivery and reliability: DORA metrics, incidents, SLOs
- Tools and vendors, including AI tools and their cost and usage

## People and organisation
- Org structure, team sizes, spans of control (aggregated)
- Skills inventory, seniority mix, critical knowledge holders (by role, not by name where possible)
- Attrition, regretted attrition, engagement trends, absence
- Culture and ways of working; employee representation and its relationship with management
- History: earlier reorganisations, layoffs, outsourcing or big changes, and how they went

## Current situation
- The decision on the table, who asked, by when, and why now
- Initiatives already running that this decision touches
- Known risks, open conflicts and stakeholder positions

## Gaps and assumptions
- What is missing, who could provide it, and what is assumed meanwhile
```

## 3. Where to look, and what to search for

| Part of the brief | Internal sources (read-only) | External sources |
|---|---|---|
| Strategy and governance | Knowledge base (Confluence, Notion, SharePoint, Drive): strategy, OKRs, board papers, all-hands decks | Annual report, company filings (for example the Chamber of Commerce/KvK in the Netherlands), press releases, interviews |
| Money | Finance/ERP, data warehouse, BI dashboards, budget files | Filed accounts, investor updates, credit reports |
| Customers and market | CRM, support tooling, NPS/CSAT, churn analysis, sales notes | Analyst reports, competitor sites and filings, review sites, trade press, regulators |
| Operations | ERP, MES and maintenance systems, POS, rostering and workforce management, WMS/TMS, field service, quality, safety and incident logs; patient or case records only in aggregate | Regulators' and inspectorates' reports, sector benchmarks, trade associations |
| Product and technology | Git (history, CODEOWNERS), service catalogue, Jira/Linear, Grafana/Datadog, incident tooling, cloud billing, AI vendor admin consoles | Vendor documentation and pricing pages, security advisories |
| People and organisation | HRIS (aggregated), org chart, engagement surveys, works council minutes, earlier reorganisation documents | Employer review sites (treat as signals, not facts), labour market statistics |
| History and decisions | Decision records (ADRs), post-mortems, retrospectives, old project pages, announcement channels | Press coverage of earlier changes |

Useful search terms in a knowledge base or chat archive: "strategy", "OKR", "roadmap", "board", "all-hands", "budget", "reorganisation", "restructuring", "post-mortem", "lessons learned", "decision", "RFC", "ADR", "vendor selection", "evaluation", "outsourcing", "AI". Search public channels and pages only, and never read private messages or personal folders.

## 4. Keeping it current: dates, staleness and up-to-date practice

- **Staleness rule of thumb:** financials older than a quarter, org data older than a month, and strategy pages older than a year need checking before you rely on them. Say how old each key fact is.
- **Check current practice for anything that moves.** Employment law, AI capabilities and pricing, benchmarks (the latest DORA report, Gallup, labour-market data), and what comparable companies do now all change. When a decision depends on them, look up the current version with a web search or the official source, prefer the most recent edition, and cite its date.
- **This skill's own reference files were last checked in November 2026.** If a decision leans on a fact from them and time has passed, verify it again.
- **Look for counter-evidence and newer findings,** not just support for what you already think. Practices that were standard a few years ago, such as story points as a performance measure or large offshoring of core work, have been widely re-examined.
