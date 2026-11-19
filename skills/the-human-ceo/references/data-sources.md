# Data sources: finding the truth yourself

A human CEO who is also technical doesn't wait for a slide deck. They know where the numbers live, they can query them, and they know which sources to trust.

## Contents

1. Start with discovery
2. Finance: cash, margin, runway
3. Spend outside payroll: cloud and tools
4. Systems and efficiency: Grafana and Prometheus
5. Delivery and workload: Jira and similar
6. Knowledge and past decisions: Confluence and similar
7. Customers
8. People data, aggregated and privacy-safe
9. The outside world: trustworthy sources
10. Data hygiene

## 1. Start with discovery

- List the tools, connectors and MCP servers available in this session before planning any analysis. Many systems (Jira, Confluence, Databricks, Snowflake, BigQuery, Grafana, Datadog, GitHub, Notion, Google Drive, CRMs) can be reached through MCP servers or connectors, but don't assume any is installed.
- Discover the schema before you query. Table and column names below are illustrative. Use `SHOW TABLES`, `DESCRIBE`, `information_schema`, a data catalog (such as Unity Catalog) or the dashboard's own query to find the real names.
- Read-only. Run `SELECT` queries and dashboard reads only. Never run writes, deletes or schema changes, and never trigger jobs or alerts, without explicit approval.
- If a source isn't available, say what you'd need ("an export of the general ledger by cost centre for the last 12 months") and continue with what you have, clearly labelled.

## 2. Finance: cash, margin, runway

What to compute:

- **Runway** in months = cash on hand / average monthly net burn (use the last 3 to 6 months, and say which).
- **Opex by category**, trended over 12 months, to see what is actually growing.
- **Revenue and gross margin by product or segment**, to see where money is made and lost.
- **Personnel cost as a share of opex**, so payroll is compared with everything else rather than assumed to be the problem.

Example (Databricks SQL or Snowflake, adjust names):

```sql
-- Opex by category per month, last 12 months
SELECT date_trunc('month', booking_date) AS month,
       cost_category,
       SUM(amount_eur)                   AS spend_eur
FROM finance.gl_entries
WHERE account_type = 'OPEX'
  AND booking_date >= add_months(current_date(), -12)
GROUP BY 1, 2
ORDER BY 1, 3 DESC;
```

Questions to answer before touching headcount: which categories grew fastest, which contracts renew soon, and which spend has no clear owner.

## 3. Spend outside payroll: cloud and tools

Cloud cost is often the fastest saving with zero human harm. Look in AWS Cost Explorer or the Cost and Usage Report, Azure Cost Management, the GCP billing export, or a FinOps tool.

Typical findings: idle or over-provisioned resources, non-production environments running 24/7, untagged spend nobody owns, storage without lifecycle rules, unexpected data egress, unused reserved capacity.

Example (AWS Cost and Usage Report in Athena):

```sql
-- Top 20 services by cost, last 30 days
SELECT line_item_product_code,
       SUM(line_item_unblended_cost) AS cost_usd
FROM cur
WHERE line_item_usage_start_date >= date_add('day', -30, current_date)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 20;
```

SaaS and tools: compare licences paid with licences used in the last 90 days (most admin consoles show last-login dates), and look for several tools doing the same job.

## 4. Systems and efficiency: Grafana and Prometheus

Use dashboards to see whether infrastructure is sized for real load, and whether incidents and toil eat team capacity.

Example (PromQL, Kubernetes): CPU actually used versus CPU requested, per namespace. A ratio far below 1 over weeks means you are paying for capacity you don't use.

```promql
sum by (namespace) (rate(container_cpu_usage_seconds_total{container!=""}[5m]))
/
sum by (namespace) (kube_pod_container_resource_requests{resource="cpu"})
```

Look at it over 7 to 30 days, not a single moment. Also check incident frequency and time spent on on-call: repeated incidents are toil you can remove.

## 5. Delivery and workload: Jira and similar

Delivery data shows where capacity goes. It must never be used to rank individuals.

Example JQL:

- Current work in progress: `project = ABC AND statusCategory = "In Progress"`
- Work stuck for two weeks or more: `project = ABC AND status = Blocked AND updated <= -14d`
- Unplanned work, if the team labels it: `project = ABC AND resolved >= -90d AND labels = unplanned`

What to look for: too much work in progress per team, long waits between statuses, a high share of unplanned work, many projects started and few finished. These point to focus and process problems, not people problems. Cycle-time charts in Jira, Linear or Azure DevOps give a better picture than counting tickets.

## 6. Knowledge and past decisions: Confluence and similar

Before proposing a reorganisation, find out what was tried before and why it worked or failed.

Example CQL:

```text
type = page AND space = STRAT AND text ~ "reorganisation" AND lastmodified > now("-365d")
type = page AND text ~ "post-mortem" AND lastmodified > now("-180d")
```

Look for earlier restructurings, post-mortems, architecture decision records, retrospectives, strategy pages and board papers. Ask the people who were there.

## 7. Customers

- Support tickets by category and channel: which questions are routine (good candidates for AI) and which need judgement, empathy or expertise.
- CSAT and NPS by channel, before and after any automation.
- Churn reasons and lost-deal notes: often the clearest signal of unmet demand, and of where people could be redeployed.
- Feature requests and "can you help me with..." questions you currently decline: new services in disguise.

## 8. People data, aggregated and privacy-safe

Useful, aggregated indicators:

- Voluntary and regretted attrition per team, rolling 12 months
- Internal mobility rate and time to fill roles internally versus externally
- Engagement and pulse survey results, absence trends
- A skills inventory: who has skills next to the ones the company will need

Rules:

- Report on groups, not individuals. Suppress groups too small to stay anonymous (a common rule of thumb is fewer than 5 people).
- Personal circumstances (health, family, care duties) stay with HR and the manager concerned. They never go into analysis prompts or chats.
- Follow the GDPR and local law, and the works council's rights where they apply, when processing employee data.

## 9. The outside world: trustworthy sources

Rank sources roughly like this:

1. **Primary sources**: official statistics (such as CBS, Eurostat, BLS, OECD), central banks (such as DNB, ECB, the Federal Reserve), regulators and government sites, company filings and annual reports, court decisions.
2. **Established news organisations with editorial standards and a corrections policy**, such as Reuters, AP, the Financial Times, Bloomberg or NOS.
3. **Peer-reviewed research** and established research institutes.
4. **Industry analysts**: useful, but note their commercial interests.
5. **Never as the only source**: press releases, vendor marketing, social media posts, anonymous blogs, AI-generated summaries.

Rules:

- Cross-check important claims with at least two independent sources.
- Record the publication date. Prefer recent sources for anything that changes.
- Separate what a company announced from what has been verified. A claim like "our AI does the work of 700 agents" is a press statement, not an outcome.
- Search for counter-evidence, not only for support.

## 10. Data hygiene

- For every number: state the source, the query or filter, the date range and how fresh it is.
- Correlation is not causation. A team with more incidents may simply own the oldest system.
- Goodhart's law: a metric people are judged on stops being a good measure. Don't turn exploratory metrics into targets.
- Show uncertainty as ranges and say what would narrow them.
- Copy as little personal data out of systems of record as you can.
