# Response to Operations: Driver App Leaderboard & Weekly Bottom-10% Flag

**Prepared for:** Executive Team / Operations / HR & Legal  
**Scope:** ~2,400 drivers across the Netherlands and Belgium (~800 directly employed, ~1,600 via subcontractors)  
**Date:** 20 November 2026  

---

## 1. Recommendation

**Do not build the live stops-per-hour leaderboard in the driver app or the automated weekly bottom-10% flag.** Instead, target the **8% productivity opportunity** by measuring and fixing **route, depot, and address-data bottlenecks**—paired with quality and safety metrics—and managing subcontractors on **service-level outcomes**, not individual driver rankings.

---

## 2. Why the Proposed Feature Will Backfire

### A. It measures route luck, not driver effort—and invites gaming
Stops per hour depends heavily on factors outside a driver's control: route density, apartment blocks vs. detached houses, traffic, weather, parcel weight, and signature requirements.
- **Forced ranking creates permanent churn:** Flagging the bottom 10% every week means **~240 drivers are flagged every single week**, even if overall performance improves.
- **What gets rewarded:** A live leaderboard pushes drivers to optimise the number at the expense of service and safety—skipping safe parking, rushing stairs, leaving parcels in unsafe spots, or marking recipients "not at home" without ringing to clear stops faster. That drives up redelivery costs, damage claims, customer churn, and road incidents.

### B. Legal, Works Council, and Subcontractor Risks (NL & BE)
Before building any monitoring feature, Product & Tech cannot ship a system that creates unapproved legal exposure. (Note: the points below are operational governance flags to verify with Dutch and Belgian employment counsel, not legal advice.)
- **Netherlands — Works Council consent (*Instemmingsrecht*):** Under Article 27(1)(l) of the Dutch Works Councils Act (*Wet op de ondernemingsraden*, WOR), introducing or changing a system suited to monitoring employee attendance, behaviour, or performance requires **prior consent** from the Works Council (*Ondernemingsraad*). With ~800 directly employed drivers, this applies directly.
- **Belgium — Works Council & Safety Committee:** Performance-monitoring systems and evaluation criteria trigger information and consultation duties with the Works Council (*Ondernemingsraad* / *Conseil d'entreprise*) and, given the road-safety and psychosocial stress impact of live pace pressure, the Committee for Prevention and Protection at Work (CPBW/PPT).
- **GDPR & Automated Profiling:** Weekly automated flagging of ~240 named individuals to third parties (subcontractors) requires a clear lawful basis, proportionality, and transparency—and risks failing a Data Protection Impact Assessment (DPIA).
- **Subcontractor Authority & Co-Employment Risk:** Issuing weekly individual performance flags on ~1,600 subcontractor drivers blurs the line between managing a B2B service contract and exercising direct employer authority over subcontractor staff (a key risk under Dutch and Belgian labour/false-self-employment rules).
- **EU AI Act (upcoming):** Under the EU AI Act (Annex III), systems used to evaluate or monitor workers are classified as high-risk; from **2 December 2027** (following the 2026 Digital Omnibus), employers must formally inform workers' representatives and affected workers before deploying high-risk systems (Article 26(7)). National co-determination rules already apply today.

### C. Unverified Assumption Behind the "8% Lift"
No evidence has been shared yet showing that driver pace—rather than depot wave delays, poor route clustering, or bad address data—is the primary cause of the gap between high- and low-performing routes.

---

## 3. What to Do Instead: Fix the System, Keep the 8% Goal

Instead of putting a scoreboard in the cab, use our existing telemetry at **depot and route level** to find where minutes are actually lost, and run a **6-week controlled pilot** in 2–3 depots.

### 1. Pair Every Speed Metric with Quality, Safety, and Health
Never track stops per hour in isolation. Review route/depot performance on a balanced scorecard:

| Dimension | Metric | Purpose |
|---|---|---|
| **Efficiency** | Stops per hour (by route type/density) | Identify route-design and depot bottlenecks |
| **Quality** | First-time delivery success rate; "not at home" scan rate | Catch rushed or skipped deliveries early |
| **Customer** | Damage claims & missing-parcel complaints per 1,000 stops | Prevent speed from eroding customer trust |
| **Safety & People** | Road/van incidents, harsh-braking telemetry (aggregated), sick leave & driver turnover | Ensure pace targets remain safe and sustainable |

### 2. Attack the Real Bottlenecks (Weeks 1–6 Pilot)
- **Audit the 8% gap:** Compare the top and bottom 20% of *routes* (not drivers) by route type. Check how much variance comes from late depot departures, mis-sequenced stops, missing gate/apartment codes, and bad geocodes.
- **Fix the app friction drivers actually feel:** Ask a sample of own and subcontractor drivers where they lose 15–30 minutes a day (e.g., slow scanner flows, wrong pin drops, unclear delivery instructions) and fix those in the driver app.
- **Manage subcontractors by contract SLA:** Hold subcontractor partners accountable to depot-level SLAs (on-time delivery, first-time-right rate, complaints, and route completion), leaving individual driver coaching and management to their own employer.

---

## 4. Immediate Next Steps (This Week)

1. **Product & Tech + Ops:** Pull the last 90 days of route-level data to separate route/depot variance from driver variance, and check the basis for the 8% estimate.
2. **HR & Legal:** Confirm Works Council (NL/BE) and DPIA requirements before any driver-level performance data is surfaced or shared with subcontractors.
3. **Ops + Product:** Select 2–3 depots for a 6-week pilot focused on route clustering, depot dispatch timing, and app friction—and invite drivers to help identify the biggest time-wasters.
