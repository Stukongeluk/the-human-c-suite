# Connectors

The seats work best when they can read the company's real systems. The plugin's `.mcp.json` lists official, vendor-hosted MCP servers, the same ones Anthropic's own plugins use. Nothing connects until you sign in to a server yourself, and you only need the ones your company uses. The skills name the kind of system ("the work tracker", "the data warehouse"), so any server of that kind works, including ones you add yourself.

| Kind of system | Included servers | Other options |
|---|---|---|
| Work tracking and wiki | Atlassian (Jira, Confluence), Linear, Asana, monday.com, ClickUp, Notion | Azure DevOps |
| Code and pipelines | GitHub (read-only URL) | GitLab |
| Incidents and observability | PagerDuty, Datadog | Grafana, Sentry |
| Data warehouse | BigQuery, Snowflake\*, Databricks\* | Power BI and Fabric, dbt |
| Product analytics and customers | Amplitude (US and EU), Pendo, Intercom, HubSpot | Mixpanel, PostHog, Salesforce, Stripe |
| Documents and mail | Google Drive | Claude's Microsoft 365 and Google Workspace connectors |
| Chat | none included | Slack, through Claude's Slack connector |

\* Snowflake and Databricks servers live at an address of your own account, so the entry has no URL. Add yours with `claude mcp add --transport http <name> <url>`, using the URL from the vendor's documentation.


## Keep it read-only

- **GitHub** uses the `/readonly` URL, so it can read code, pull requests and pipelines but not change them.
- **HubSpot** acts with your own HubSpot permissions and has no read-only switch: sign in with an account that can only view the CRM.
- **Amplitude, Pendo, Datadog and PagerDuty** can change dashboards, alerts or incidents: grant read permission only. A seat never acknowledges, resolves or silences an alert on its own.
- **Google Drive** acts with your own permissions: the seats change and send nothing without your explicit approval.
- **Data warehouses:** use a role that can only read curated, documented schemas (finance marts, delivery facts, aggregated people views), never raw HR or customer tables.

## People data

No HR system is included on purpose. For leadership questions, the seats work from an aggregated, anonymised view in the warehouse with small groups suppressed. In Germany and the Netherlands, connecting tools to employee data can need the works council's agreement.

What the plugin does with your data: see [PRIVACY.md](PRIVACY.md).
