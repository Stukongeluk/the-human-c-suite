# Response Brief: Driver App Leaderboard & Weekly Bottom-10% Flagging

**To:** Head of Operations (cc: CEO, Legal/HR)  
**From:** CPTO  
**Date:** November 2026  
**Decision:** Do not build the live driver leaderboard or automated bottom-10% subcontractor flagging. Instead, run a 2-week diagnostic on aggregated route and depot data to capture the 8% productivity gain without legal exposure, safety incidents, or driver churn.

---

## 1. The Goal We Share

Lifting network productivity by 8% across ~2,400 drivers (~800 own staff, ~1,600 subcontractor drivers) is a meaningful margin and capacity target. The disagreement is not on the 8% goal—it is on whether individual surveillance and public ranking will deliver it or backfire.

---

## 2. Why the Proposed Feature Will Backfire

1. **Legal & Co-Determination Blockers (Netherlands & Belgium — *verify with employment counsel*):**
   - **Works Council Consent (NL):** Under Article 27(1)(l) of the Dutch Works Councils Act (*WOR*), any system suited to monitoring employee attendance, behaviour, or performance requires **prior Works Council (*Ondernemingsraad*) consent** for our ~800 directly employed drivers. Deploying without consent makes the rollout legally voidable. Belgian works council / union consultation rules similarly apply to workplace monitoring systems.
   - **Subcontractor Misclassification Risk:** Weekly flagging of individual subcontractor drivers ("bottom 10%", ~160 subcontractor drivers/week) looks like direct employer supervision and disciplinary control. In both the Netherlands and Belgium, exercising authority over a subcontractor's staff creates serious **disguised employment (*schijnzelfstandigheid*)** liability.
   - **GDPR & AI Act:** A live leaderboard visible to peers exposes personal performance data without a clear lawful basis and fails data-minimisation tests. Automated or semi-automated flagging for weekly sanctioning also triggers Data Protection Impact Assessment (DPIA) and GDPR Art. 22 obligations. (Under the EU AI Act, worker monitoring and task-allocation systems are classified as high-risk; mandatory worker-representative notice under Art. 26(7) applies from 2 December 2027, while national co-determination and GDPR apply today.)

2. **Metric Distortion & Safety Risk:**
   - **Stops/hour measures the route, not the driver:** Dense city centres, apartment buildings, rural distances, traffic, parcel size, and late depot waves distort raw stops/hour far more than individual effort.
   - **Gaming hurts customers and safety:** Putting a live rank in the cab pushes drivers to rush—skipping doorstep handovers (raising "not at home" disputes and redelivery costs), mishandling parcels, and driving unsafely. Those costs hit claims, insurance, and retention.

---

## 3. Three Options

| Option | Expected Impact | Risks & Costs | Reversible? |
|---|---|---|---|
| **A. Do nothing** | 0% lift | Misses margin/capacity target | Yes |
| **B. Live leaderboard + bottom-10% flagging** | Unproven (+8% assumed); likely short-term spike followed by gaming & churn | High: WOR Art. 27 breach, subcontractor misclassification, GDPR/DPIA, road safety & damage claims | Hard (trust & legal damage persist) |
| **C. Recommended: 2-week diagnostic + route/app fixes** | Targets 5–10% real capacity gain via fewer failed drops and less depot wait time | Low: uses existing aggregated telemetry; builds driver & Works Council trust | Yes |

---

## 4. Recommended Path Forward

1. **Diagnose before building (Weeks 1–2):** Pull aggregated, anonymised telemetry by depot and route type to see where hours are actually lost—late morning wave departures, poor stop clustering, address/geofence errors, or failed first-time deliveries.
2. **Co-design with drivers and Ops (Week 3):** Shadow a handful of routes across NL and BE depots to validate what slows drivers down in the app and at the kerb.
3. **Ship helpful, system-level fixes (Weeks 4–8):**
   - Route clustering and dynamic stop-sequence improvements.
   - Pre-arrival customer notifications to cut failed first-time deliveries.
   - Faster scan/proof-of-delivery UX in the app.
   - *Private* in-app route progress for the driver only (vs. plan, never vs. peers).
4. **Manage subcontractors at the contract level:** Hold subcontractors to **route-level and depot-level SLAs** (on-time delivery, first-time success, damage rate), leaving individual coaching to the subcontractor.

---

## 5. Success & Guardrail Metrics (Measured at Depot/Cohort Level)

- **Productivity:** Delivered stops per paid route-hour; first-time delivery success rate.
- **Quality & Safety:** Damage/missing-parcel claims per 1,000 stops; road/near-miss incident rate.
- **People:** Driver attrition (own and subcontractor); app usability score.
