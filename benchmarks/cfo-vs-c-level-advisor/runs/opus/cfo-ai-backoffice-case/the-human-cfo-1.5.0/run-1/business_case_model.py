"""
AI in finance and back office: business case model (2027-2029, by quarter).

Every input below is an ESTIMATE unless marked GIVEN or SOURCE. Replace the
estimates with payroll aggregates, activity data, vendor quotes and HR data
before the paper goes to the board. Run: python3 business_case_model.py
All amounts in SEK million; capacity and headcount in FTE.
"""

import math

# ---------------------------------------------------------------- inputs
HC0 = 90                      # GIVEN: finance and back-office team, FTE
SAL_M = 48_000                # ESTIMATE: average monthly salary, SEK
ONCOST = 98_842 / 66_159      # SOURCE: SCB labour cost, finance & insurance white-collar,
                              # Aug 2025: total labour cost / wages = 1.49
COST_FTE = SAL_M * 12 * ONCOST / 1e6   # fully loaded payroll cost per FTE-year, SEK m
ANNUAL_SAL = SAL_M * 12 / 1e6          # salary only, SEK m
CONTRACTOR_FTE = 850 * 1_650 / 1e6     # ESTIMATE: SEK 850/hour x 1,650 hours = cover per FTE-year
EMPLOYER_CONTRIB = 0.3142              # SOURCE: Skatteverket, full rate 2026

# Work areas: FTE (ESTIMATE split of the 90), share of hours automatable at the
# required quality at maturity (low, base, high) (ESTIMATE, to be measured in pilots)
AREAS = [
    # name,                                   fte, low,  base, high, wave
    ("Accounts payable and supplier data",    16, 0.35, 0.50, 0.65, 1),
    ("Reconciliations and close",             22, 0.30, 0.45, 0.60, 1),
    ("External and regulatory reporting",     18, 0.10, 0.20, 0.30, 2),
    ("Management reporting and analysis",     12, 0.20, 0.30, 0.40, 2),
    ("Payments, collections, other back office", 22, 0.10, 0.20, 0.30, 2),
]
assert sum(a[1] for a in AREAS) == HC0

# Share of automated hours that come back as review and exception handling (ESTIMATE)
REVIEW = {"low": 0.35, "base": 0.25, "high": 0.20}

# Share of mature potential reached, quarter average, Q1 2027 .. Q4 2031 (ESTIMATE)
RAMP = {
    1: [0.00, 0.10, 0.35, 0.60, 0.70, 0.80, 0.85, 0.90, 0.95, 1.00, 1.00, 1.00] + [1.00] * 8,
    2: [0.00, 0.00, 0.10, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.90, 0.95] + [1.00] * 8,
}
NQ = 20
YEARS = [2027, 2028, 2029, 2030, 2031]
DISCOUNT = 0.08               # ESTIMATE: hurdle rate for the NPV line
QLABELS_ALL = [f"Q{q % 4 + 1} {2027 + q // 4}" for q in range(NQ)]

# Finance automation and AI controls team, drawn from the existing team (ESTIMATE)
AUTO_TEAM = [1] + [3] * 19

# AI programme cost, common to every option that uses AI (ESTIMATE; vendor quotes needed)
LICENCES = [0.20, 0.30, 0.75, 0.75] + [0.75] * 4 + [0.80] * 12   # ~SEK 3m/yr run-rate
IMPLEMENT = [1.00, 1.50, 3.00, 2.00] + [0.50] * 4 + [0.0] * 12
CONTROLS = [0.50, 0.50, 0.25, 0.25] + [0.125] * 16
TOOL_TRAINING = [0.25, 0.25, 0.25, 0.25] + [0.0] * 16

# People
ATTRITION = 0.09              # ESTIMATE: voluntary leavers + retirements per year
CRITICAL_REPLACE = 0.30       # ESTIMATE: share of leavers replaced anyway (critical skills)
REINVEST = 0.15               # CHOICE: share of freed capacity kept for quality, faster close, backlog
REDEPLOY_PLAN = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1] + [0] * 10   # ESTIMATE: moves into open roles elsewhere
REDEPLOY_TRAINING = 0.05      # ESTIMATE: SEK m per person moved
RESKILL = [0.30] * 8 + [0.15] * 12          # ESTIMATE: learning budget, paid time

# Redundancy mechanics (ESTIMATE; Swedish law and agreements to be confirmed by counsel)
SEVERANCE_MONTHS = 6          # negotiated package on top of notice pay
OUTPLACEMENT = 0.04           # SEK m per person, top-up beyond the job security council
LEGAL_HR = 1.5                # SEK m, counsel, HR project, negotiations
GARDEN_LEAVE = 0.5            # share of people on notice released from work
LIFO_PAY = 0.9                # selection order by service: leavers paid below average
EXTRA_ATTRITION_B = 0.045     # survivors' extra yearly attrition for 4 quarters after notice
EXTRA_ATTRITION_D = 0.02
REPLACE_COST = 0.5 * ANNUAL_SAL   # Gallup: one-half to two times salary; low end used
REHIRE_ONEOFF = 0.5 * ANNUAL_SAL  # recruitment and ramp-up per rehire


SCALE = {"capacity": 1.0, "programme": 1.0, "cover": 1.0}   # sensitivity multipliers


def capacity(case):
    """Freed capacity, FTE-equivalent, per quarter."""
    out = []
    for q in range(NQ):
        c = 0.0
        for name, fte, lo, ba, hi, wave in AREAS:
            share = min(1.0, {"low": lo, "base": ba, "high": hi}[case] * SCALE["capacity"])
            c += fte * share * (1 - REVIEW[case]) * RAMP[wave][q]
        out.append(c)
    return out


def mature(case):
    return sum(fte * min(1.0, {"low": lo, "base": ba, "high": hi}[case] * SCALE["capacity"])
               * (1 - REVIEW[case]) for _, fte, lo, ba, hi, _ in AREAS)


def programme_cost():
    return [SCALE["programme"] * (LICENCES[q] + IMPLEMENT[q] + CONTROLS[q] + TOOL_TRAINING[q])
            for q in range(NQ)]


def blank():
    keys = ["gross", "severance", "outplacement", "legal", "cover", "rehire",
            "attrition_cost", "ai", "reskill", "net"]
    return {k: [0.0] * NQ for k in keys}


def option_c(case, reinvest=REINVEST, attrition=ATTRITION):
    """Capacity first: hiring freeze with exceptions, natural attrition, redeployment."""
    cap = capacity(case)
    r = blank()
    hc, red, moved, kept_open = HC0, 0.0, 0.0, 0.0
    hc_path, red_path = [], []
    for q in range(NQ):
        usable = cap[q] * (1 - reinvest) - AUTO_TEAM[q]
        leavers = hc * attrition / 4
        avail = max(0.0, usable - red)
        n = min(leavers * (1 - CRITICAL_REPLACE), avail)
        rd = min(REDEPLOY_PLAN[q], max(0.0, avail - n))
        r["gross"][q] = (red + 0.5 * (n + rd)) * COST_FTE / 4
        red += n + rd
        moved += rd
        kept_open += n
        hc -= n + rd
        gap = max(0.0, AUTO_TEAM[q] + red - cap[q] * (1 - reinvest))
        r["cover"][q] = -gap * CONTRACTOR_FTE * SCALE["cover"] / 4
        r["ai"][q] = -programme_cost()[q]
        r["reskill"][q] = -(RESKILL[q] + rd * REDEPLOY_TRAINING)
        hc_path.append(hc)
        red_path.append(red)
    finish(r)
    return r, hc_path, {"involuntary": 0, "redeployed": round(moved, 1),
                        "leavers_not_replaced": round(kept_open, 1)}


def option_b(case):
    """Board's ask as stated: 27 redundancies decided in 2027 alongside the AI rollout."""
    cap = capacity(case)
    r = blank()
    n_exit = round(0.30 * HC0)                    # 27
    exits = [0, 4, 12, 11] + [0] * (NQ - 4)       # notices April 2027; 1-6 months by service
    assert sum(exits) == n_exit
    garden = n_exit * GARDEN_LEAVE                # stop working at notice (start Q2)
    rehires = 0
    cum = 0.0
    hc_path = []
    for q in range(NQ):
        prev = cum
        cum += exits[q]
        # pay stops at exit (mid-quarter)
        r["gross"][q] = (prev + 0.5 * exits[q]) * COST_FTE * LIFO_PAY / 4
        # people not doing the work: garden leave from Q2, the rest as they exit
        working_exited = (n_exit - garden) * ((prev + 0.5 * exits[q]) / n_exit)
        not_working = (garden if q >= 1 else 0.0) + working_exited
        if q >= 1:
            sev = exits[q] * SEVERANCE_MONTHS * SAL_M * (1 + EMPLOYER_CONTRIB) / 1e6
            r["severance"][q] = -sev
            r["outplacement"][q] = -exits[q] * OUTPLACEMENT
        r["legal"][q] = -LEGAL_HR / 2 if q in (0, 1) else 0.0
        # from Q1 2028 rehire permanent staff for the part of the gap that persists
        if q == 4:
            persist = AUTO_TEAM[11] + n_exit - cap[11]    # gap still open at end of 2029
            rehires = max(0, math.floor(persist))
            r["rehire"][q] = -rehires * REHIRE_ONEOFF
        if q >= 4:
            r["rehire"][q] += -rehires * COST_FTE / 4      # their payroll
        gap = max(0.0, AUTO_TEAM[q] + not_working - rehires - cap[q])
        r["cover"][q] = -gap * CONTRACTOR_FTE * SCALE["cover"] / 4
        if 2 <= q <= 5:                                    # Q3 2027 .. Q2 2028
            r["attrition_cost"][q] = -(HC0 - n_exit) * EXTRA_ATTRITION_B / 4 * REPLACE_COST
        r["ai"][q] = -programme_cost()[q]
        hc_path.append(HC0 - cum + rehires)
    finish(r)
    return r, hc_path, {"involuntary": n_exit, "rehires": rehires}


def option_d(case):
    """Staged: option C through 2027, then one redundancy round in 2028 sized at the
    autumn 2027 gate, bringing forward reductions that attrition would deliver later."""
    cap = capacity(case)
    r = blank()
    hc, red, exited = HC0, 0.0, 0
    usable_mature = mature(case) * (1 - REINVEST) - AUTO_TEAM[-1]
    x = 0
    hc_path = []
    for q in range(NQ):
        usable = cap[q] * (1 - REINVEST) - AUTO_TEAM[q]
        leavers = hc * ATTRITION / 4
        avail = max(0.0, usable - red)
        n = min(leavers * (1 - CRITICAL_REPLACE), avail)
        rd = min(REDEPLOY_PLAN[q], max(0.0, avail - n))
        if q == 3:   # autumn 2027 gate: reach mature usable capacity by mid-2028
            after_q4 = red + n + rd
            expected_2028 = 4 * (hc * ATTRITION / 4) * (1 - CRITICAL_REPLACE) + sum(REDEPLOY_PLAN[4:8])
            x = max(0, math.floor(usable_mature - after_q4 - expected_2028))
        exits = x if q == 5 else 0          # notices January 2028, exits mid-2028
        nonexit_red = red - exited
        r["gross"][q] = (nonexit_red + 0.5 * (n + rd)) * COST_FTE / 4 + \
            (exited + 0.5 * exits) * COST_FTE * LIFO_PAY / 4
        red += n + rd + exits
        exited += exits
        hc -= n + rd + exits
        if exits:
            r["severance"][q] = -exits * SEVERANCE_MONTHS * SAL_M * (1 + EMPLOYER_CONTRIB) / 1e6
            r["outplacement"][q] = -exits * OUTPLACEMENT
        if q in (3, 4) and x:
            r["legal"][q] = -(LEGAL_HR * 0.6) / 2
        gap = max(0.0, AUTO_TEAM[q] + red - cap[q] * (1 - REINVEST))
        if q in (4, 5) and x:               # garden leave for part of the notice period
            gap += x * GARDEN_LEAVE * 0.5
        r["cover"][q] = -gap * CONTRACTOR_FTE * SCALE["cover"] / 4
        if 5 <= q <= 8 and x:
            r["attrition_cost"][q] = -hc * EXTRA_ATTRITION_D / 4 * REPLACE_COST
        r["ai"][q] = -programme_cost()[q]
        r["reskill"][q] = -(RESKILL[q] + rd * REDEPLOY_TRAINING)
        hc_path.append(hc)
    finish(r)
    return r, hc_path, {"involuntary": x}


def finish(r):
    for q in range(NQ):
        r["net"][q] = sum(r[k][q] for k in r if k != "net")


def yearly(series):
    return [sum(series[4 * i:4 * i + 4]) for i in range(len(YEARS))]


def npv(series):
    return sum(v / (1 + DISCOUNT) ** ((q + 0.5) / 4) for q, v in enumerate(series))


LINE_NAMES = {
    "gross": "Gross payroll saving (from each actual exit or non-replacement)",
    "severance": "Severance packages incl. employer contributions",
    "outplacement": "Outplacement top-up",
    "legal": "Counsel, HR project, negotiations",
    "cover": "Work still to be done: contractors and temporary cover",
    "rehire": "Rehiring: recruitment, ramp-up and rehired payroll",
    "attrition_cost": "Extra voluntary attrition (replacement cost)",
    "ai": "AI programme: licences, integration, data, controls, tool training",
    "reskill": "Learning budget, reskilling and redeployment",
    "net": "**Net cash and P&L effect vs. baseline**",
}


def table(r, title):
    rows = [f"**{title}** (SEK m; + = better than baseline)", "",
            "| Line | Q1 27 | Q2 27 | Q3 27 | Q4 27 | 2027 | 2028 | 2029 | 2030 | 2031 | 5 years |",
            "|---|---|---|---|---|---|---|---|---|---|---|"]
    for k, label in LINE_NAMES.items():
        s = r[k]
        if all(abs(v) < 1e-9 for v in s):
            continue
        y = yearly(s)
        cells = [f"{v:.1f}" for v in s[:4]] + [f"{v:.1f}" for v in y] + [f"{sum(y):.1f}"]
        if k == "net":
            cells = [f"**{c}**" for c in cells]
        rows.append(f"| {label} | " + " | ".join(cells) + " |")
    return "\n".join(rows)


def check(r):
    for q in range(NQ):
        assert abs(sum(r[k][q] for k in r if k != "net") - r["net"][q]) < 1e-9


def summary_row(opt, case):
    fn = {"B": option_b, "C": option_c, "D": option_d}[opt]
    r, hc, meta = fn(case)
    check(r)
    y = yearly(r["net"])
    return y, hc, meta, r


if __name__ == "__main__":
    print(f"Cost per FTE-year: SEK {COST_FTE:.2f} m; team payroll SEK {HC0 * COST_FTE:.1f} m; "
          f"30% = {round(0.3 * HC0)} FTE = SEK {round(0.3 * HC0) * COST_FTE:.1f} m/yr")
    print(f"Contractor cover per FTE-year: SEK {CONTRACTOR_FTE:.2f} m")
    print()
    print("Capacity freed (FTE-equivalent, quarter average, 2027-2029)")
    for case in ("low", "base", "high"):
        c = capacity(case)
        print(f"  {case:5s} " + " ".join(f"{v:5.1f}" for v in c[:12])
              + f" | mature {mature(case):.1f} ({mature(case) / HC0:.0%})"
              + f" | Q4 2027 {c[3]:.1f} ({c[3] / HC0:.0%}) | Q4 2028 {c[7]:.1f} ({c[7] / HC0:.0%})")
    print()
    print("Task sizing (FTE-equivalent at maturity, net of review)")
    for name, fte, lo, ba, hi, wave in AREAS:
        print(f"  {name:45s} {fte:3d}  auto {lo:.0%}-{hi:.0%} (base {ba:.0%})  "
              f"low {fte * lo * (1 - REVIEW['low']):.1f}  base {fte * ba * (1 - REVIEW['base']):.1f}"
              f"  high {fte * hi * (1 - REVIEW['high']):.1f}  wave {wave}")
    print()
    for opt, title in (("B", "Option B: 27 redundancies in 2027"),
                       ("C", "Option C: capacity first, attrition and redeployment (recommended)"),
                       ("D", "Option D: option C, plus one redundancy round in 2028 sized at the gate")):
        y, hc, meta, r = summary_row(opt, "base")
        print(table(r, title + ", base case"))
        print(f"\nHeadcount end 2027 / 2028 / 2029 / 2031: {hc[3]:.0f} / {hc[7]:.0f} / {hc[11]:.0f} / {hc[19]:.0f}; {meta}\n")
    print("Summary (SEK m): 2027 | 2028 | 2029 | 2030 | 2031 | 5-yr | NPV 8% || HC end-27/28/29/31 | involuntary")
    for case in ("low", "base", "high"):
        for opt in ("B", "C", "D"):
            y, hc, meta, r = summary_row(opt, case)
            print(f"  {opt} {case:5s} " + " ".join(f"{v:6.1f}" for v in y) + f" {sum(y):6.1f} {npv(r['net']):6.1f}"
                  f" || {hc[3]:.0f}/{hc[7]:.0f}/{hc[11]:.0f}/{hc[19]:.0f} | {meta.get('involuntary', 0)}")
    print()
    print("Sensitivity, option C base: attrition 6% / 12%, reinvestment 0%")
    for att in (0.06, 0.12):
        r, hc, _ = option_c("base", attrition=att)
        y = yearly(r["net"])
        print(f"  attrition {att:.0%}: 2027 {y[0]:.1f}  5-yr {sum(y):.1f}  NPV {npv(r['net']):.1f}  HC end-2029 {hc[11]:.0f}")
    r, hc, _ = option_c("base", reinvest=0.0)
    y = yearly(r["net"])
    print(f"  reinvest 0%:   2027 {y[0]:.1f}  5-yr {sum(y):.1f}  NPV {npv(r['net']):.1f}  HC end-2029 {hc[11]:.0f}")
    print("Sensitivity: AI programme cost -30% / +30% (5-yr net, base case)")
    for f in (0.7, 1.3):
        SCALE["programme"] = f
        print(f"  x{f}: B {sum(option_b('base')[0]['net']):.1f}  C {sum(option_c('base')[0]['net']):.1f}"
              f"  D {sum(option_d('base')[0]['net']):.1f}   (2027: B {sum(option_b('base')[0]['net'][:4]):.1f}"
              f"  C {sum(option_c('base')[0]['net'][:4]):.1f})")
    SCALE["programme"] = 1.0
    print("Sensitivity: option B if a third of the work gap is absorbed by overtime or dropped work")
    SCALE["cover"] = 2 / 3
    for case in ("low", "base", "high"):
        y = yearly(option_b(case)[0]["net"])
        print(f"  B {case}: 2027 {y[0]:.1f}  5-yr {sum(y):.1f}")
    SCALE["cover"] = 1.0
    print("Break-even: capacity multiplier on the high case at which B's 5-yr net matches C's")
    for m in [1.0 + 0.05 * i for i in range(0, 21)]:
        SCALE["capacity"] = m
        b, c = sum(option_b("high")[0]["net"]), sum(option_c("high")[0]["net"])
        if b >= c:
            print(f"  x{m:.2f}: B {b:.1f} >= C {c:.1f}; mature capacity {mature('high'):.1f} FTE-eq "
                  f"({mature('high') / HC0:.0%}), Q4 2027 {capacity('high')[3]:.1f}")
            break
    else:
        print("  B never catches C within x2.0 of the high case")
    SCALE["capacity"] = 1.0
    print("Option C: cost of finding out (net, H1 2027, base):", f"{sum(option_c('base')[0]['net'][:2]):.1f}")
    for case in ("low", "base", "high"):
        r, hc, _ = option_c(case)
        print(f"  C {case}: net 2031 {sum(r['net'][16:20]):.1f}/yr; gross run-rate {4 * r['gross'][19]:.1f}; "
              f"cumulative turns positive in " +
              next((QLABELS_ALL[q] for q in range(NQ) if sum(r['net'][:q + 1]) > 0), "after 2031"))
