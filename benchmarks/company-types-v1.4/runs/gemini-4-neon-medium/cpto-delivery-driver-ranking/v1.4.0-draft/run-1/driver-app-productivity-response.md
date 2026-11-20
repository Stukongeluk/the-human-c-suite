# Proposal: Improving Delivery Productivity Without Individual Driver Ranking

**To:** Head of Operations, CEO, Legal & DPO  
**From:** CPTO  
**Date:** November 2026  

## Executive Summary

Operations' target of an **8% lift in stops per hour** across our 2,400 drivers (~190 driver-equivalents of capacity) is a major commercial prize, and Product & Tech wants to help deliver it. However, we should **not** build a live in-cab leaderboard or a weekly bottom-10% flag sent to subcontractors. That design creates severe legal exposure in the Netherlands and Belgium, introduces a road-safety hazard, and will likely lose the 8% gain to damage claims, failed deliveries, and driver churn.

Instead, we propose a **two-week operational and app diagnostic** to locate where minutes are actually lost per route, followed by a **pilot at two depots** targeting routing, depot dispatch delays, and app friction—measured at the route and depot level across productivity, quality, and safety.

---

## Why the Leaderboard and Bottom-10% Flag Will Backfire

### 1. Legal and Regulatory Exposure (NL & BE)
*Note: This is an operational risk flag, not legal advice; Legal and DPO should review before any work is scoped.*

- **Subcontractor authority & disguised employment (~1,600 drivers):** Two thirds of our fleet is employed by subcontractors. Live-ranking individual subcontractor drivers and flagging a weekly bottom 10% looks like exercising direct employer authority (*gezagsverhouding* in NL; *werkgeversgezag* / unlawful personnel lending in BE), creating significant reclassification and joint-liability risk in a heavily scrutinised parcel sector.
- **Works Council consent (~800 employed drivers):** In the Netherlands, any system suited to monitoring employee behaviour or performance requires prior Works Council (*OR*) consent under **Article 27(1)(l) WOR**. Belgian social consultation rules and workplace privacy protections similarly apply. Shipping without consent risks invalidation and industrial friction.
- **GDPR & automated profiling:** Sharing weekly individual performance rankings with third-party subcontractors triggers strict data-minimisation, legal-basis, and DPIA requirements—and **Article 22** scrutiny if subcontractors act on the flag to drop drivers.
- **Upcoming EU rules:** The EU Platform Work Directive (2024/2831) transposition deadline is December 2026, and the EU AI Act's high-risk worker-monitoring obligations (Annex III / Article 26(7)) take effect in December 2027 (moved from August 2026 by the 2026 Digital Omnibus). Building individual surveillance now builds technical and compliance debt we will have to unwind.

### 2. Safety and Quality Risk
- **In-cab distraction:** A live stops-per-hour leaderboard encourages checking the screen while driving, speeding, and skipping breaks. One serious road incident carries unacceptable human, legal, and reputational cost.
- **Predictable gaming:** Raw stops per hour measures the *route* (urban high-rises, rural sprawl, bulky parcels, traffic, late depot waves) as much as the driver. Ranking individuals on it drives doorstepping, skipped signature checks, and false "not at home" scans—eroding the 8% gain through re-deliveries, claims, and shipper churn.

---

## Where the 8% Actually Lives: Proposed Alternative

Rather than pressuring drivers to rush, we should remove the friction that slows every route down.

| Phase | Action | Owner | Timing |
|---|---|---|---|
| **1. Diagnose** | Pull 90 days of **aggregated** TMS, depot scan, app telemetry, and failed-delivery data (no individual rankings). Ride along with 10–15 employed and subcontractor drivers across urban and rural routes to identify top time-sinks (late wave dispatch, bad address pins, slow app scans, offline dropouts, unbalanced routes). | Product, Ops, Data | Weeks 1–2 |
| **2. Consult** | Share the productivity problem and diagnostic findings with the NL/BE Works Councils and Legal/DPO *before* designing any new app feature or telemetry. | CPTO, Ops, HR, Legal | Week 3 |
| **3. Pilot** | Ship the top 2–3 driver-helping fixes (e.g., faster scan flow, offline reliability, better drop-off instructions, route rebalancing, recipient delivery-window confirmation) at two pilot depots. Share **aggregated** route-type and depot-level performance with subcontractors against contractual SLAs. | Product & Tech, Ops | Weeks 4–9 |
| **4. Decide** | Evaluate pilot results against all four balanced metrics before scaling across the network. | CPTO, Ops, CEO | Week 10 |

---

## Balanced Success Metrics (Route & Depot Level Only)

We will only count a productivity gain as real if all four indicators hold together:
1. **Stops per hour** (normalised by route density and parcel mix, aggregated by depot/route cluster)
2. **First-time delivery rate** (catches fake "not at home" scans)
3. **Damage, loss, and customer complaint rate** (catches rushing and doorstepping)
4. **Road safety incidents, near-misses, and driver turnover** (catches unsafe pace)

---

## Open Questions for Alignment

1. What evidence supports the 8% estimate, and how much of the current variance in stops per hour disappears once we control for route density and depot dispatch time?
2. Which two depots (one NL, one BE) give us the cleanest test for a 6-week friction-removal pilot?
3. What am I missing, and what would make this plan wrong?
