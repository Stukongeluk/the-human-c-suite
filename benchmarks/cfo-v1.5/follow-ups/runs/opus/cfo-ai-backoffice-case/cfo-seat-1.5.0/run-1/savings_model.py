"""
AI in finance & back office: net savings model, by quarter (2027) and year (2028).

Every input below is an ESTIMATE unless marked otherwise. Replace them with
figures from payroll (aggregated), the ERP/AP subledger, the reconciliation
tool, the close calendar, HR attrition data and vendor quotes, then re-run.

Run:  python3 savings_model.py            (prints all tables as markdown)

Options, all costed on the same basis against "do nothing" (Option 0):
  A  Board's ask: 27 redundancies (30% of 90) in 2027, alongside the AI programme
  B  Recommended: gated AI programme; headcount follows *proven* capacity via
     hiring freeze, natural attrition, redeployment; voluntary exits only after
     the end-2027 gate, and only for surplus that remains
  C  Process fixes only (e-invoicing, supplier consolidation, report clean-up),
     no new AI; headcount via freeze and attrition
Constant 2027 prices; wage growth and volume growth are left out on purpose
(they affect all options alike).
"""

from dataclasses import dataclass

# ---------------------------------------------------------------- inputs
MONTHS = [(y, m) for y in (2027, 2028) for m in range(1, 13)]
N = len(MONTHS)

TEAM = {  # FTE by team (assumption: replace with the real org chart)
    "Accounts payable & supplier data": 20,
    "Reconciliations (bank, premium, claims, reinsurance, IC)": 22,
    "Accounting & close": 16,
    "Reporting (IFRS/statutory, Solvency II, management)": 22,
    "Management, finance systems & controls": 10,
}
FTE0 = sum(TEAM.values())  # 90

# Share of each team's hours freed by end-2028 (estimate), split into
# process fixes that need no AI, and the AI increment on top.
PROCESS_SHARE = {  # low, base, high
    "Accounts payable & supplier data": (0.10, 0.15, 0.20),
    "Reconciliations (bank, premium, claims, reinsurance, IC)": (0.05, 0.10, 0.12),
    "Accounting & close": (0.03, 0.05, 0.08),
    "Reporting (IFRS/statutory, Solvency II, management)": (0.03, 0.05, 0.08),
    "Management, finance systems & controls": (0.0, 0.0, 0.0),
}
TOTAL_SHARE = {  # process + AI, low, base, high
    "Accounts payable & supplier data": (0.25, 0.45, 0.65),
    "Reconciliations (bank, premium, claims, reinsurance, IC)": (0.20, 0.35, 0.50),
    "Accounting & close": (0.10, 0.20, 0.30),
    "Reporting (IFRS/statutory, Solvency II, management)": (0.05, 0.12, 0.25),
    "Management, finance systems & controls": (0.0, 0.0, 0.05),
}
NEW_AI_WORK = (2.0, 3.0, 4.0)  # FTE of new work: review, exceptions, monitoring, controls
SCEN = {"low": 0, "base": 1, "high": 2}

# Realisation of the end-2028 level at each quarter end (estimate):
# pilot H1 2027, scale H2 2027, full by end 2028.
RAMP_Q_END = {(2027, 3): 0.0, (2027, 6): 0.05, (2027, 9): 0.20, (2027, 12): 0.35,
              (2028, 3): 0.50, (2028, 6): 0.65, (2028, 9): 0.80, (2028, 12): 1.00}

# Cost per FTE (estimate). SCB 2024 averages: ekonomiassistenter SEK 38,100,
# redovisningsekonomer 45,700, controllers 58,900 per month; blended to 2027.
SALARY_M = 50_000
PAID_MONTHS = 12.2            # 12 + holiday supplement
EMPLOYER_CONTRIB = 0.3142     # Skatteverket, 2026 full rate (fact)
PENSION = 0.07                # occupational pension as share of salary (estimate)
SLP = 0.2426                  # special payroll tax on pension costs (fact)
OTHER_PER_HEAD = 25_000       # IT, equipment, benefits that go with the person (estimate)
ANNUAL_SALARY = SALARY_M * PAID_MONTHS
COST_FTE_Y = (ANNUAL_SALARY * (1 + EMPLOYER_CONTRIB)
              + SALARY_M * 12 * PENSION * (1 + SLP) + OTHER_PER_HEAD)
COST_FTE_M = COST_FTE_Y / 12

CONSULTANT_FTE_Y = 1_450_000  # ~SEK 850/h x 1,700 h (estimate)
HIRE_COST = 0.5 * ANNUAL_SALARY  # all-in replacement cost, Gallup lower bound (estimate)
ATTRITION = 0.08              # voluntary attrition per year (estimate; get real data)
ATTRITION_POST_CUT = 0.13     # +5 pp for 12 months after a 30% cut (estimate)

SEVERANCE_A = 6 * SALARY_M * (1 + EMPLOYER_CONTRIB)    # negotiated package (estimate)
SEVERANCE_VOL = 9 * SALARY_M * (1 + EMPLOYER_CONTRIB)  # voluntary package (estimate)
OUTPLACEMENT = 40_000         # top-up beyond the job security council (estimate)
LEGAL_A = 800_000             # counsel for MBL/LAS process (estimate)
REDEPLOY_COST = 60_000 + 2 * COST_FTE_M * 0.5  # reskilling + 2 months at half output

# Programme costs per quarter, SEK (estimates; replace with quotes)
def q_costs(spec):
    """spec: dict label -> list of 8 quarterly amounts (2027Q1..2028Q4)."""
    return spec

AI_PROGRAMME = q_costs({
    "AI licences and usage": [100e3, 400e3, 800e3, 1_200e3, 875e3, 875e3, 875e3, 875e3],
    "Integration and data work (ERP, bank feeds, supplier master)": [1_000e3, 2_000e3, 2_000e3, 1_000e3, 500e3, 500e3, 0, 0],
    "Controls, audit, DORA and model risk": [0, 500e3, 500e3, 700e3, 200e3, 200e3, 200e3, 200e3],
    "Programme team": [750e3, 750e3, 750e3, 750e3, 375e3, 375e3, 375e3, 375e3],
    "Training and change (paid work time)": [250e3, 500e3, 500e3, 250e3, 250e3, 250e3, 250e3, 250e3],
})
PROCESS_PROGRAMME = q_costs({
    "Process fixes (e-invoicing drive, supplier clean-up, report inventory)": [300e3, 500e3, 500e3, 200e3, 75e3, 75e3, 75e3, 75e3],
})

DIP_FTE = 1.5           # parallel running + training, Apr 2027 - Mar 2028 (estimate)
SURVIVOR_DIP = 0.05     # A: output loss of whole team Feb-Sep 2027 (estimate)
NOTICE_OUTPUT = 0.60    # A: output of people working their notice (estimate)

# ---------------------------------------------------------------- helpers
def idx(y, m):
    return MONTHS.index((y, m))

def ramp(i):
    """Linear interpolation of RAMP_Q_END, value at end of month i."""
    pts = sorted((idx(y, m), v) for (y, m), v in RAMP_Q_END.items())
    if i <= pts[0][0]:
        return pts[0][1]
    for (i0, v0), (i1, v1) in zip(pts, pts[1:]):
        if i0 <= i <= i1:
            return v0 + (v1 - v0) * (i - i0) / (i1 - i0)
    return pts[-1][1]

AI_K = None  # optional override: AI increment as a multiple of the base case

def capacity(scen, include_ai=True):
    """Net FTE of work removed at end-2028, and monthly path."""
    s = SCEN[scen]
    proc = sum(TEAM[t] * PROCESS_SHARE[t][s] for t in TEAM)
    if not include_ai:
        full = proc
    elif AI_K is not None:
        b = SCEN["base"]
        inc = (sum(TEAM[t] * (TOTAL_SHARE[t][b] - PROCESS_SHARE[t][b]) for t in TEAM)
               - NEW_AI_WORK[b])
        full = sum(TEAM[t] * PROCESS_SHARE[t][b] for t in TEAM) + AI_K * inc
    else:
        full = sum(TEAM[t] * TOTAL_SHARE[t][s] for t in TEAM) - NEW_AI_WORK[s]
    # average capacity during month i = mean of start and end of month
    path = [full * (ramp(i - 1) + ramp(i)) / 2 if i > 0 else full * ramp(0) / 2
            for i in range(N)]
    return full, path

def dip_path(with_ai=True):
    lo, hi = idx(2027, 4), idx(2028, 3)
    return [DIP_FTE if (with_ai and lo <= i <= hi) else 0.0 for i in range(N)]

@dataclass
class Result:
    lines: dict          # label -> monthly SEK (positive = saving, negative = cost)
    hc: list             # headcount at month end
    gap: list            # FTE gap covered by consultants
    pnl_shift: dict      # label -> monthly P&L-only timing adjustments
    exits: float = 0.0
    redeployed: float = 0.0
    voluntary: float = 0.0
    hires: float = 0.0

def programme_lines(spec):
    out = {}
    for label, qs in spec.items():
        monthly = []
        for q in qs:
            monthly += [-q / 3] * 3
        out[label] = monthly
    return out

def baseline_hires():
    hc, hires = FTE0, []
    for i in range(N):
        leavers = hc * ATTRITION / 12
        hires.append(leavers)  # baseline replaces every leaver
    return hires

BASE_HIRES = baseline_hires()

# ---------------------------------------------------------------- options
def option_A(scen, rehire_from=(2028, 4)):
    _, cap = capacity(scen, True)
    dip = dip_path(True)
    cut = round(0.30 * FTE0)  # 27
    exit1, exit2 = idx(2027, 6), idx(2027, 9)  # employments end 30 Jun / 30 Sep
    share1 = 0.40
    notice_start = idx(2027, 3)                # notice given 1 Mar after MBL
    lines = {k: [0.0] * N for k in [
        "Gross payroll saving", "Severance and exit packages",
        "Outplacement and transition support", "Legal and advisory",
        "Work still to be done (consultants for the gap)",
        "Recruitment vs baseline (rehiring, extra attrition)",
        "Redeployment (reskilling, ramp-up)"]}
    pnl = {"Severance provision timing (P&L only)": [0.0] * N}
    hc = FTE0
    hcs, gaps = [], []
    hires_total = redeployed = 0.0
    for i in range(N):
        # exits
        if i == exit1 + 1:
            hc -= cut * share1
        if i == exit2 + 1:
            hc -= cut * (1 - share1)
        # under notice
        under_notice = 0.0
        if notice_start <= i <= exit1:
            under_notice = cut
        elif exit1 < i <= exit2:
            under_notice = cut * (1 - share1)
        # attrition among the rest
        rate = ATTRITION_POST_CUT if idx(2027, 7) <= i <= idx(2028, 6) else ATTRITION
        leavers = max(hc - under_notice, 0) * rate / 12
        hc -= leavers
        need = FTE0 - cap[i] + dip[i]
        survivor = SURVIVOR_DIP if idx(2027, 2) <= i <= idx(2027, 9) else 0.0
        output = (hc - under_notice) * (1 - survivor) + under_notice * NOTICE_OUTPUT
        gap = max(need - output, 0.0)
        hires = 0.0
        if i >= idx(*rehire_from) and gap > 0:  # rehire permanently from this month
            hires = gap / (1 - survivor)
            hc += hires
            gap = 0.0
        moved = 0.0
        surplus = output - need if gap == 0 else 0.0
        if hires == 0 and i >= idx(2027, 10) and surplus > 1.0:  # same rule as B
            moved = min(surplus - 1.0, 0.5)
            hc -= moved
            redeployed += moved
        lines["Redeployment (reskilling, ramp-up)"][i] = -moved * REDEPLOY_COST
        hires_total += hires
        lines["Gross payroll saving"][i] = (FTE0 - hc) * COST_FTE_M
        lines["Work still to be done (consultants for the gap)"][i] = -gap * CONSULTANT_FTE_Y / 12
        lines["Recruitment vs baseline (rehiring, extra attrition)"][i] = -(hires - BASE_HIRES[i]) * HIRE_COST
        hcs.append(hc)
        gaps.append(gap)
    # before Q2 2028 nobody is hired, so baseline recruitment is avoided; that
    # avoided cost is already in the formula above (hires=0 -> +BASE_HIRES*cost).
    pay1, pay2 = exit1, exit2
    lines["Severance and exit packages"][pay1] -= cut * share1 * SEVERANCE_A
    lines["Severance and exit packages"][pay2] -= cut * (1 - share1) * SEVERANCE_A
    lines["Outplacement and transition support"][notice_start] -= cut * OUTPLACEMENT
    lines["Legal and advisory"][idx(2027, 1)] -= LEGAL_A / 2
    lines["Legal and advisory"][idx(2027, 2)] -= LEGAL_A / 2
    # P&L: whole severance provided when plan announced (Mar 2027), cash at exit
    total_sev = cut * SEVERANCE_A
    pnl["Severance provision timing (P&L only)"][idx(2027, 3)] -= total_sev
    pnl["Severance provision timing (P&L only)"][pay1] += cut * share1 * SEVERANCE_A
    pnl["Severance provision timing (P&L only)"][pay2] += cut * (1 - share1) * SEVERANCE_A
    lines.update(programme_lines(AI_PROGRAMME))
    lines.update(programme_lines(PROCESS_PROGRAMME))
    return Result(lines, hcs, gaps, pnl, exits=cut, hires=hires_total, redeployed=redeployed)

def option_freeze(scen, include_ai=True, allow_voluntary=True, voluntary=None):
    """Options B (include_ai) and C (process only)."""
    _, cap = capacity(scen, include_ai)
    dip = dip_path(include_ai)
    lines = {k: [0.0] * N for k in [
        "Gross payroll saving", "Redeployment (reskilling, ramp-up)",
        "Voluntary exit packages", "Outplacement and transition support",
        "Work still to be done (consultants for the gap)",
        "Recruitment vs baseline (fewer replacements)"]}
    hc = FTE0
    hcs, gaps = [], []
    redeployed = hires_total = 0.0
    redeploy_from = idx(2027, 10)     # after gate 1 and MBL talks
    vol_exit = idx(2028, 9)           # employment ends 30 Sep 2028
    vol = voluntary or 0.0
    for i in range(N):
        leavers = hc * ATTRITION / 12
        hc -= leavers
        need_perm = FTE0 - cap[i]      # permanent need
        hires = 0.0
        if hc < need_perm:             # replace only what is still needed
            hires = need_perm - hc
            hc = need_perm
        temp_gap = max(need_perm + dip[i] - hc, 0.0)   # parallel running: temporary cover
        lines["Work still to be done (consultants for the gap)"][i] = -temp_gap * CONSULTANT_FTE_Y / 12
        need = need_perm + dip[i]
        surplus = hc - need
        moved = 0.0
        if i >= redeploy_from and surplus > 1.0:
            moved = min(surplus - 1.0, 0.5)
            hc -= moved
            redeployed += moved
        if i == vol_exit + 1 and vol > 0:
            hc -= vol
        hires_total += hires
        lines["Gross payroll saving"][i] = (FTE0 - hc) * COST_FTE_M
        lines["Recruitment vs baseline (fewer replacements)"][i] = -(hires - BASE_HIRES[i]) * HIRE_COST
        lines["Redeployment (reskilling, ramp-up)"][i] = -moved * REDEPLOY_COST
        hcs.append(hc)
        gaps.append(temp_gap)
    if vol > 0:
        lines["Voluntary exit packages"][vol_exit] -= vol * SEVERANCE_VOL
        lines["Outplacement and transition support"][vol_exit - 2] -= vol * OUTPLACEMENT
    if include_ai:
        lines.update(programme_lines(AI_PROGRAMME))
    lines.update(programme_lines(PROCESS_PROGRAMME))
    res = Result(lines, hcs, gaps, {}, redeployed=redeployed, voluntary=vol, hires=hires_total)
    if include_ai and allow_voluntary and voluntary is None:
        # gate 2: offer voluntary exits for the surplus projected for Dec 2028
        surplus_dec = hcs[-1] - (FTE0 - cap[-1] + dip[-1])
        # people who leave voluntarily in Sep are also not there for attrition;
        # size the offer at the surplus beyond a 1-FTE buffer, whole people
        offer = max(0, int(surplus_dec - 1.0))
        if offer > 0:
            return option_freeze(scen, include_ai, allow_voluntary, voluntary=offer)
    return res

# ---------------------------------------------------------------- reporting
def quarters(monthly):
    q = [sum(monthly[i:i + 3]) for i in range(0, 12, 3)]
    return q + [sum(monthly[12:24])]

def fmt(x):
    v = x / 1e6
    return f"{v:+.1f}" if abs(v) >= 0.05 else "0.0"

def r1(x):
    """Round SEK to SEK m with one decimal (half away from zero)."""
    v = x / 1e6
    return float(f"{v:.1f}") + 0.0

import math

def lr_round(values_sek):
    """Largest-remainder rounding to SEK 0.1m so the rounded parts add to the rounded total."""
    tenths = [v / 1e5 for v in values_sek]           # in units of SEK 0.1m
    target = round(sum(tenths))
    base = [math.floor(t) for t in tenths]
    rem = sorted(range(len(tenths)), key=lambda i: tenths[i] - base[i], reverse=True)
    for i in rem[: target - sum(base)]:
        base[i] += 1
    return [b / 10 for b in base]

def row_cells(m):
    q = quarters(m)
    qs = lr_round(q[:4])
    return qs + [round(sum(qs), 1), r1(q[4])]

def displayed(res):
    """Rounded cells; quarters add to the 2027 cell; nets are the sum of displayed lines."""
    rows = {}
    for label, m in res.lines.items():
        if all(abs(v) < 1 for v in m):
            continue
        rows[label] = row_cells(m)
    net_row = [round(sum(r[c] for r in rows.values()), 1) for c in range(6)]
    shift = [0.0] * 6
    for m in res.pnl_shift.values():
        shift = [a + b for a, b in zip(shift, row_cells(m))]
    pnl_row = [round(a + b, 1) for a, b in zip(net_row, shift)]
    return rows, net_row, pnl_row

def dfmt(v):
    return "0.0" if abs(v) < 0.05 else f"{v:+.1f}"

def dnet(res):
    _, n, _ = displayed(res)
    return n[4], n[5]

def table(res, title):
    cols = ["2027 Q1", "2027 Q2", "2027 Q3", "2027 Q4", "2027", "2028"]
    print(f"\n#### {title}\n")
    print("| Line (SEK m; + saving, - cost) | " + " | ".join(cols) + " |")
    print("|---|" + "---|" * len(cols))
    rows, net_row, pnl_row = displayed(res)
    for label, cells in rows.items():
        print(f"| {label} | " + " | ".join(dfmt(v) for v in cells) + " |")
    print("| **Net cash effect** | " + " | ".join(f"**{dfmt(v)}**" for v in net_row) + " |")
    print("| **Net P&L effect** | " + " | ".join(f"**{dfmt(v)}**" for v in pnl_row) + " |")
    tot = [0.0] * N
    hq = [res.hc[i] for i in (2, 5, 8, 11)] + [res.hc[11], res.hc[23]]
    print("| Headcount at period end | " + " | ".join(f"{h:.0f}" for h in hq) + " |")
    gq = [sum(res.gap[i:i + 3]) / 3 for i in (0, 3, 6, 9)]
    gq += [sum(res.gap[:12]) / 12, sum(res.gap[12:]) / 12]
    if any(g > 0.05 for g in gq):
        print("| Work gap covered by consultants (avg FTE) | " + " | ".join(f"{g:.1f}" for g in gq) + " |")
    return tot

def net(res):
    tot = [0.0] * N
    for m in res.lines.values():
        tot = [a + b for a, b in zip(tot, m)]
    return sum(tot[:12]), sum(tot[12:]), tot

def run_rate(res):
    """Dec 2028 annualised payroll saving net of recurring programme costs and gap."""
    pay = res.lines["Gross payroll saving"][-1] * 12
    gap = res.lines.get("Work still to be done (consultants for the gap)", [0] * N)[-1] * 12
    rec = 0.0
    for k in ("AI licences and usage", "Controls, audit, DORA and model risk"):
        if k in res.lines:
            rec += res.lines[k][-1] * 12
    for k in PROCESS_PROGRAMME:
        if k in res.lines:
            rec += res.lines[k][-1] * 12
    return pay + gap + rec

def main():
    global CONSULTANT_FTE_Y, SEVERANCE_A
    print(f"Loaded cost per FTE (est.): SEK {COST_FTE_Y/1e6:.2f}m/yr; team of {FTE0}: SEK {FTE0*COST_FTE_Y/1e6:.1f}m/yr")
    print(f"30% = {round(0.3*FTE0)} FTE = SEK {round(0.3*FTE0)*COST_FTE_Y/1e6:.1f}m/yr gross run-rate")
    print(f"Severance A per person SEK {SEVERANCE_A/1e3:.0f}k; voluntary package SEK {SEVERANCE_VOL/1e3:.0f}k; hire cost SEK {HIRE_COST/1e3:.0f}k; redeploy SEK {REDEPLOY_COST/1e3:.0f}k")

    print("\n### Capacity freed by end-2028 (net FTE)\n")
    print("| Team | FTE | Process fixes (low/base/high) | Process + AI (low/base/high) |")
    print("|---|---|---|---|")
    for t, f in TEAM.items():
        p = "/".join(f"{f*s:.1f}" for s in PROCESS_SHARE[t])
        a = "/".join(f"{f*s:.1f}" for s in TOTAL_SHARE[t])
        print(f"| {t} | {f} | {p} | {a} |")
    pt = [sum(TEAM[t] * PROCESS_SHARE[t][s] for t in TEAM) for s in range(3)]
    at = [sum(TEAM[t] * TOTAL_SHARE[t][s] for t in TEAM) for s in range(3)]
    print(f"| Gross total | {FTE0} | " + "/".join(f"{x:.1f}" for x in pt) + " | " + "/".join(f"{x:.1f}" for x in at) + " |")
    print("| New work: review, exceptions, monitoring | | 0 | " + "/".join(f"-{x:.1f}" for x in NEW_AI_WORK) + " |")
    nt = [at[s] - NEW_AI_WORK[s] for s in range(3)]
    print(f"| **Net capacity** | | " + "/".join(f"**{x:.1f}**" for x in pt) + " | " + "/".join(f"**{x:.1f}**" for x in nt) + " |")
    print(f"| Share of 90 | | " + "/".join(f"{x/FTE0:.0%}" for x in pt) + " | " + "/".join(f"{x/FTE0:.0%}" for x in nt) + " |")
    for scen in SCEN:
        full, path = capacity(scen)
        print(f"- {scen}: net capacity end-2027 {full*ramp(idx(2027,12)):.1f} FTE, end-2028 {full:.1f} FTE")

    results = {}
    for scen in SCEN:
        results[("A", scen)] = option_A(scen)
        results[("B", scen)] = option_freeze(scen, True)
        results[("C", scen)] = option_freeze(scen, False, False)

    print("\n### Quarterly model, base case")
    table(results[("A", "base")], "Option A - 27 redundancies in 2027 (board's ask), base case")
    table(results[("B", "base")], "Option B - gated programme, headcount follows proven capacity (recommended), base case")
    table(results[("C", "base")], "Option C - process fixes only, no new AI, base case")

    print("\n### Options side by side (SEK m, net vs do nothing)\n")
    print("| Option | Scenario | 2027 net cash | 2028 net cash | 2027+2028 | Dec-2028 run-rate (net of recurring costs) | Headcount Dec 2028 | Exits (forced / voluntary) | Redeployed | Hires |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    print("| 0 Do nothing | all | 0.0 | 0.0 | 0.0 | 0.0 | 90 | 0 / 0 | 0 | baseline |")
    for opt in "ABC":
        for scen in SCEN:
            r = results[(opt, scen)]
            y1, y2 = dnet(r)
            forced = r.exits
            print(f"| {opt} | {scen} | {dfmt(y1)} | {dfmt(y2)} | {dfmt(round(y1+y2,1))} | {fmt(run_rate(r))} | {r.hc[-1]:.0f} | {forced:.0f} / {r.voluntary:.0f} | {r.redeployed:.1f} | {r.hires:.1f} |")

    # incremental value of AI over process-only (B vs C)
    print("\n### What the AI adds over process fixes alone (B minus C, SEK m)\n")
    print("| Scenario | 2027 | 2028 | Run-rate Dec 2028 |")
    print("|---|---|---|---|")
    for scen in SCEN:
        b1, b2 = dnet(results[("B", scen)])
        c1, c2 = dnet(results[("C", scen)])
        print(f"| {scen} | {dfmt(round(b1-c1,1))} | {dfmt(round(b2-c2,1))} | {fmt(run_rate(results[('B',scen)])-run_rate(results[('C',scen)]))} |")

    # sensitivities on Option A 2027
    print("\n### Sensitivities, base case (2027 net cash, SEK m)\n")
    base_A = dnet(option_A("base"))[0] * 1e6
    base_B = dnet(option_freeze("base", True))[0] * 1e6
    rows = []
    keep = CONSULTANT_FTE_Y
    for val in (1_100_000, 1_800_000):
        CONSULTANT_FTE_Y = val
        rows.append((f"Consultant cost SEK {val/1e6:.1f}m/FTE-yr (base 1.45)", dnet(option_A('base'))[0]*1e6, dnet(option_freeze('base', True))[0]*1e6))
    CONSULTANT_FTE_Y = keep
    keep = SEVERANCE_A
    for months in (3, 12):
        SEVERANCE_A = months * SALARY_M * (1 + EMPLOYER_CONTRIB)
        rows.append((f"Exit package {months} months (base 6)", dnet(option_A('base'))[0]*1e6, dnet(option_freeze('base', True))[0]*1e6))
    SEVERANCE_A = keep
    print("| Sensitivity | Option A 2027 | Option B 2027 |")
    print("|---|---|---|")
    print(f"| Base assumptions | {fmt(base_A)} | {fmt(base_B)} |")
    for lbl, a, b in rows:
        print(f"| {lbl} | {fmt(a)} | {fmt(b)} |")
    print(f"| AI high case | {dfmt(dnet(results[('A','high')])[0])} | {dfmt(dnet(results[('B','high')])[0])} |")
    print(f"| AI low case | {dfmt(dnet(results[('A','low')])[0])} | {dfmt(dnet(results[('B','low')])[0])} |")

    # break-even: what would make A's 2027 net zero?
    print("\n### Break-even for Option A in 2027\n")
    # (1) if all hidden costs were zero (no consultants, no dips)
    rA = results[("A", "base")]
    gap_cost_27 = -sum(rA.lines["Work still to be done (consultants for the gap)"][:12])
    print(f"- Consultant cost for the work gap in 2027: SEK {gap_cost_27/1e6:.1f}m (avg gap {sum(rA.gap[:12])/12:.1f} FTE)")
    print(f"- A's 2027 net with zero consultant cost (work simply not done): SEK {dfmt(dnet(rA)[0] - row_cells(rA.lines['Work still to be done (consultants for the gap)'])[4])}m")
    # (2) AI capacity needed by Sep 2027 to avoid any gap
    print(f"- To have no work gap after the September exits, the AI would need to free about {27 - 0:.0f} FTE plus attrition by Q3 2027; the high case frees {capacity('high')[0]*ramp(idx(2027,9)):.1f}.")

def stopped_at_gate1(scen):
    """B in a case where the pilot fails: AI spend stops after Q2 2027, process fixes continue."""
    c = option_freeze(scen, False, False)
    lines = dict(c.lines)
    for label, qs in AI_PROGRAMME.items():
        monthly = []
        for qi, q in enumerate(qs):
            monthly += [-(q if qi < 2 else 0) / 3] * 3
        lines[label] = monthly
    lines["Contract exit and wind-down (estimate)"] = [0.0] * N
    lines["Contract exit and wind-down (estimate)"][idx(2027, 7)] = -500e3
    return Result(lines, c.hc, c.gap, {}, hires=c.hires)

def extras():
    global AI_K
    print("\n### Downside capped by the gate\n")
    r = stopped_at_gate1("low")
    y1, y2 = dnet(r)
    print(f"- B, pilot fails at gate 1 (low case, AI stopped after Q2 2027): 2027 {dfmt(y1)}, 2028 {dfmt(y2)}, run-rate {fmt(run_rate(r))}")
    rb = option_freeze("low", True)
    b1, b2 = dnet(rb)
    print(f"- compare: B low case carried on regardless: 2027 {dfmt(b1)}, 2028 {dfmt(b2)}, run-rate {fmt(run_rate(rb))}")

    print("\n### Option A if it rehires from Q4 2027 instead of using consultants until Q2 2028\n")
    for scen in SCEN:
        ra = option_A(scen, rehire_from=(2027, 10))
        y1, y2 = dnet(ra)
        print(f"- A ({scen}), rehire from Oct 2027: 2027 {dfmt(y1)}, 2028 {dfmt(y2)}, run-rate {fmt(run_rate(ra))}, hires {ra.hires:.1f}, headcount Dec 2028 {ra.hc[-1]:.0f}")

    print("\n### Payback (cumulative 2027-28 net, then Dec-2028 run-rate per year)\n")
    print("| Option | Scenario | Cumulative to Dec 2028 | Run-rate/yr | Years after 2028 to recover |")
    print("|---|---|---|---|---|")
    for opt, fn in (("A", lambda s_: option_A(s_)), ("B", lambda s_: option_freeze(s_, True)), ("C", lambda s_: option_freeze(s_, False, False))):
        for scen in SCEN:
            r = fn(scen)
            y1, y2 = dnet(r)
            cum, rr = round(y1 + y2, 1), run_rate(r) / 1e6
            yrs = "already positive" if cum >= 0 else (f"{-cum/rr:.1f}" if rr > 0 else "never")
            print(f"| {opt} | {scen} | {dfmt(cum)} | {dfmt(round(rr,1))} | {yrs} |")

    print("\n### Gate hurdle: AI increment needed for B to beat C within two years after 2028 (by end 2030)\n")
    c1, c2, _ = net(option_freeze("base", False, False))
    crr = run_rate(option_freeze("base", False, False))
    lo, hi = 0.0, 3.0
    for _ in range(40):
        mid = (lo + hi) / 2
        AI_K = mid
        rb = option_freeze("base", True)
        b1, b2, _ = net(rb)
        val = (b1 + b2 + 2 * run_rate(rb)) - (c1 + c2 + 2 * crr)
        if val > 0:
            hi = mid
        else:
            lo = mid
    AI_K = hi
    full, _ = capacity("base", True)
    b = SCEN["base"]
    inc = sum(TEAM[t] * (TOTAL_SHARE[t][b] - PROCESS_SHARE[t][b]) for t in TEAM) - NEW_AI_WORK[b]
    print(f"- AI increment must be >= {hi:.2f} x base ({hi*inc:.1f} net FTE by end 2028; total with process fixes {full:.1f} FTE = {full/FTE0:.0%} of 90)")
    AI_K = None

    print("\n### AI programme cost sensitivity (base case, B minus C)\n")
    print("| AI programme cost | B-C 2027+2028 | B-C run-rate/yr | B-C cumulative by end 2030 |")
    print("|---|---|---|---|")
    global AI_PROGRAMME
    keep = AI_PROGRAMME
    for f in (0.7, 1.0, 1.3):
        AI_PROGRAMME = {k: [v * f for v in qs] for k, qs in keep.items()}
        rb, rc = option_freeze("base", True), option_freeze("base", False, False)
        b1, b2, _ = net(rb)
        c1, c2, _ = net(rc)
        d2, drr = (b1 + b2) - (c1 + c2), run_rate(rb) - run_rate(rc)
        print(f"| x{f:.1f} | {fmt(d2)} | {fmt(drr)} | {fmt(d2 + 2*drr)} |")
    AI_PROGRAMME = keep
    tot27 = sum(sum(q[:4]) for q in keep.values()); tot28 = sum(sum(q[4:]) for q in keep.values())
    print(f"\n- AI programme cost (same in A and B): 2027 SEK {tot27/1e6:.1f}m, 2028 SEK {tot28/1e6:.1f}m; H1 2027 (pilot to gate 1) SEK {sum(sum(q[:2]) for q in keep.values())/1e6:.1f}m")

if __name__ == "__main__":
    main()
    extras()
