"""
Budget 2027 options model: 8% per cost centre vs a ranked plan.

ALL INPUTS ARE ILLUSTRATIVE ESTIMATES scaled to the facts given
(600 people, payroll 68% of opex, thin positive margin, B2B services, NL).
Replace every value in INPUTS and LEVERS with ledger, payroll, CRM and HR
figures, then rerun:  python3 budget_model.py
Amounts in EUR millions. "pts" = percentage points of 2026 opex.
Everything is measured against a 2027 "do nothing" baseline: flat headcount,
cao-level wage growth and CPI on non-payroll.

Levers common to both options (leaders first, headcount through flows,
pricing and leakage) are counted in both, so the comparison isolates what
actually differs: an 8% shave of non-payroll plus dismissals, versus a
zero-based review of non-payroll and no dismissals.
"""

INPUTS = {
    "opex_2026": 75.0,               # estimate: 600 FTE x ~EUR 85k loaded = EUR 51m = 68% of opex
    "payroll_share": 0.68,           # given
    "fte": 600,                      # given
    "op_margin_2026": 0.04,          # "thin but positive": assumed 4%
    "billable_share": 0.70,          # share of people in billable delivery roles (estimate)
    "wage_growth_2027": 0.038,       # CPB MEV 2027: cao wages, market sector
    "nonpay_inflation_2027": 0.027,  # CPB MEV 2027: CPI
}

# (cautious, mid, favourable)
LEVERS = {
    # Common: leaders first (exec 10% fixed-pay cut + no indexation, senior leaders no indexation)
    "leaders_inyear": (0.25, 0.35, 0.45),
    "leaders_runrate": (0.10, 0.15, 0.20),        # only the skipped indexation persists
    # Common: headcount through flows (freeze with exceptions, attrition, internal moves first)
    "attrition_rate": (0.10, 0.12, 0.14),         # voluntary leavers a year: 60 / 72 / 84 people (estimate)
    "not_replaced": (12, 20, 28),                 # of those leavers, not replaced by end-2027, mostly overhead
    "flow_role_cost_2026": 0.080,                 # loaded cost of an overhead role
    "flow_inyear_factor": (0.45, 0.50, 0.55),     # leavers spread through the year
    "recruit_cost_avoided": (0.004, 0.006, 0.008),
    # Common: pricing discipline and revenue leakage (profit, not opex)
    "pricing_pct": (0.005, 0.010, 0.015),         # of revenue, above current plan
    "leakage_pct": (0.003, 0.006, 0.010),
    "rev_inyear_real": (0.60, 0.70, 0.80),
    # Recommended only: zero-based review of non-payroll
    "zbb_pct": (0.08, 0.11, 0.14),
    "nonpay_inyear_real": (0.60, 0.65, 0.70),     # contracts and leases renew through the year
    "zbb_oneoff": (0.25, 0.18, 0.12),
    # Blanket only
    "blanket_pct": 0.08,
    "exit_months_2027": (4.5, 6.0, 7.0),          # months of saving in 2027 (exits mid-Aug / Jul / Jun)
    "oneoff_per_role": (0.030, 0.022, 0.015),     # transition payment, settlement premium, legal, outplacement
    "programme_oneoff": (0.30, 0.20, 0.15),       # counsel, works-council expert, HR time
    "share_with_demand": (0.50, 0.30, 0.10),      # billable people let go whose work others can't absorb
    "extra_attrition_pts": (0.03, 0.02, 0.01),    # extra voluntary turnover among those who stay
    "replacement_cost": (0.060, 0.045, 0.030),    # 0.5-1x base salary per extra leaver
    "attr_share_2027": 0.5,
}
NAMES = ["cautious", "mid", "favourable"]


def base():
    i = INPUTS
    p26 = i["opex_2026"] * i["payroll_share"]
    n26 = i["opex_2026"] - p26
    p27 = p26 * (1 + i["wage_growth_2027"])
    n27 = n26 * (1 + i["nonpay_inflation_2027"])
    rev = i["opex_2026"] / (1 - i["op_margin_2026"])
    return dict(p26=p26, n26=n26, p27=p27, n27=n27, dn27=p27 + n27, rev=rev,
                profit26=rev - i["opex_2026"], loaded27=p27 / i["fte"],
                rev_per_billable=rev / (i["fte"] * i["billable_share"]))


def common(k):
    b, L = base(), LEVERS
    fc = L["flow_role_cost_2026"] * (1 + INPUTS["wage_growth_2027"])
    n = L["not_replaced"][k]
    c = {}
    c["leaders_in"], c["leaders_rr"] = L["leaders_inyear"][k], L["leaders_runrate"][k]
    c["flows_pay_rr"] = n * fc
    c["flows_in"] = n * fc * L["flow_inyear_factor"][k] + n * L["recruit_cost_avoided"][k]
    c["flows_rr"] = n * fc + n * L["recruit_cost_avoided"][k]
    c["rev_rr"] = b["rev"] * (L["pricing_pct"][k] + L["leakage_pct"][k])
    c["rev_in"] = c["rev_rr"] * L["rev_inyear_real"][k]
    c["n"] = n
    return c


def recommended(k):
    b, L, c = base(), LEVERS, common(k)
    r = dict(c)
    r["nonpay_rr"] = b["n27"] * L["zbb_pct"][k]
    r["nonpay_in"] = r["nonpay_rr"] * L["nonpay_inyear_real"][k]
    r["oneoff"] = L["zbb_oneoff"][k]
    r["dismissals"] = 0
    r["dism_in"] = r["dism_rr"] = r["rev_lost_in"] = r["rev_lost_rr"] = r["attr_in"] = r["attr_y2"] = 0.0
    return finish(r)


def blanket(k):
    b, L, c = base(), LEVERS, common(k)
    r = dict(c)
    r["nonpay_rr"] = b["n27"] * L["blanket_pct"]
    r["nonpay_in"] = r["nonpay_rr"] * L["nonpay_inyear_real"][k]
    payroll_cut = b["p27"] * L["blanket_pct"]
    d = round((payroll_cut - c["flows_pay_rr"] - c["leaders_rr"]) / b["loaded27"])
    r["dismissals"] = d
    r["dism_rr"] = d * b["loaded27"]
    m = L["exit_months_2027"][k]
    r["dism_in"] = r["dism_rr"] * m / 12
    r["oneoff"] = d * L["oneoff_per_role"][k] + L["programme_oneoff"][k]
    r["billable_cut"] = d * INPUTS["billable_share"]
    r["utilised_cut"] = r["billable_cut"] * L["share_with_demand"][k]
    r["rev_lost_rr"] = r["utilised_cut"] * b["rev_per_billable"]
    r["rev_lost_in"] = r["rev_lost_rr"] * m / 12
    attr = INPUTS["fte"] * L["extra_attrition_pts"][k] * L["replacement_cost"][k]
    r["attr_in"] = attr * L["attr_share_2027"]
    r["attr_y2"] = attr - r["attr_in"]
    # The dismissals on their own: net of one-offs, extra attrition and lost revenue
    r["dism_net_in"] = r["dism_in"] - r["oneoff"] - r["attr_in"] - r["rev_lost_in"]
    r["dism_net_rr"] = r["dism_rr"] - r["attr_y2"] - r["rev_lost_rr"]
    # Break-even: billable people let go with real demand behind them that wipe out the dismissals' saving
    r["be_in"] = (r["dism_in"] - r["oneoff"] - r["attr_in"]) / (b["rev_per_billable"] * m / 12)
    r["be_rr"] = (r["dism_rr"] - r["attr_y2"]) / b["rev_per_billable"]
    return finish(r)


def finish(r):
    r["opex_in"] = r["leaders_in"] + r["nonpay_in"] + r["flows_in"] + r["dism_in"] - r["oneoff"]
    r["opex_rr"] = r["leaders_rr"] + r["nonpay_rr"] + r["flows_rr"] + r["dism_rr"]
    r["profit_in"] = r["opex_in"] + r["rev_in"] - r["rev_lost_in"] - r["attr_in"]
    r["profit_rr"] = r["opex_rr"] + r["rev_rr"] - r["rev_lost_rr"] - r["attr_y2"]
    r["two_year"] = r["profit_in"] + r["profit_rr"]
    return r


def quarters(k=1):
    """2027 by quarter. Ramps average to the in-year factors used above (mid case)."""
    L, c = LEVERS, common(k)
    fc = L["flow_role_cost_2026"] * (1 + INPUTS["wage_growth_2027"])
    nonpay_ramp = [0.25, 0.55, 0.80, 1.00]       # avg 0.65
    flow_ramp = [0.125, 0.375, 0.625, 0.875]     # avg 0.50
    rev_ramp = [0.40, 0.60, 0.80, 1.00]          # avg 0.70
    dism_ramp = [0.0, 0.0, 1.0, 1.0]             # exits 1 July
    rec, bl = recommended(k), blanket(k)
    out = {"rec": [], "bl": []}
    sev = bl["dismissals"] * L["oneoff_per_role"][k]
    prog = L["programme_oneoff"][k]
    bl_oneoff = [prog * 0.5, prog * 0.5 + sev * 0.4, sev * 0.6, 0.0]
    for q in range(4):
        common_q = {
            "Leaders first": c["leaders_in"] / 4,
            "Headcount through flows": c["n"] * fc / 4 * flow_ramp[q] + c["n"] * L["recruit_cost_avoided"][k] / 4,
        }
        rq = dict(common_q)
        rq["Non-payroll (zero-based review)"] = rec["nonpay_rr"] / 4 * nonpay_ramp[q]
        rq["Dismissals"] = 0.0
        rq["One-off costs"] = -(rec["oneoff"] if q == 0 else 0.0)
        rq["Opex effect"] = sum(rq.values())
        rq["Pricing and leakage"] = c["rev_rr"] / 4 * rev_ramp[q]
        rq["Revenue lost"] = 0.0
        rq["Extra attrition"] = 0.0
        rq["Profit effect"] = rq["Opex effect"] + rq["Pricing and leakage"]
        bq = dict(common_q)
        bq["Non-payroll (8% shave)"] = bl["nonpay_rr"] / 4 * nonpay_ramp[q]
        bq["Dismissals"] = bl["dism_rr"] / 4 * dism_ramp[q]
        bq["One-off costs"] = -bl_oneoff[q]
        bq["Opex effect"] = sum(bq.values())
        bq["Pricing and leakage"] = c["rev_rr"] / 4 * rev_ramp[q]
        bq["Revenue lost"] = -bl["rev_lost_rr"] / 4 * dism_ramp[q]
        bq["Extra attrition"] = -(bl["attr_in"] / 2 if q >= 2 else 0.0)
        bq["Profit effect"] = bq["Opex effect"] + bq["Pricing and leakage"] + bq["Revenue lost"] + bq["Extra attrition"]
        out["rec"].append(rq)
        out["bl"].append(bq)
    return out


def f(x):
    return f"{x:,.2f}".replace("-0.00", "0.00")


def pts(x):
    return f"{100 * x / INPUTS['opex_2026']:.1f}"


def check(a, b, label):
    assert abs(a - b) < 1e-9, f"{label}: {a} != {b}"


if __name__ == "__main__":
    b = base()
    tA = b["dn27"] * 0.08
    tB = b["dn27"] - INPUTS["opex_2026"] * 0.92
    print("BASE (illustrative)")
    print(f"opex 2026 {f(INPUTS['opex_2026'])} = payroll {f(b['p26'])} + non-payroll {f(b['n26'])}; "
          f"revenue {f(b['rev'])}; operating profit {f(b['profit26'])}")
    print(f"2027 do nothing: payroll {f(b['p27'])} + non-payroll {f(b['n27'])} = {f(b['dn27'])} "
          f"(+{f(b['dn27'] - INPUTS['opex_2026'])}, +{100 * (b['dn27'] / INPUTS['opex_2026'] - 1):.1f}%)")
    print(f"loaded cost/FTE 2027 {b['loaded27'] * 1000:.1f}k; revenue per billable FTE {b['rev_per_billable'] * 1000:.0f}k")
    print("Expected leavers: " + " | ".join(f"{INPUTS['fte'] * a:.0f}" for a in LEVERS["attrition_rate"])
          + "; not replaced: " + " | ".join(str(n) for n in LEVERS["not_replaced"]))
    print(f"Sensitivities: 1 pt wage growth = {f(b['p26'] * 0.01)}; 1% price = {f(b['rev'] * 0.01)}; "
          f"5 debtor days = {f(b['rev'] / 365 * 5)} one-time cash")
    print(f"Target A, 8% below 2027 do-nothing: {f(tA)} ({pts(tA)} pts)")
    print(f"Target B, 8% below 2026 actual: {f(tB)} ({pts(tB)} pts) below do-nothing")

    R = [recommended(k) for k in range(3)]
    B = [blanket(k) for k in range(3)]

    def row(label, key, opts, sign=1):
        return f"| {label} | " + " | ".join(f(sign * o[key]) for o in opts) + " |"

    for title, opts in [("RECOMMENDED", R), ("BLANKET 8%", B)]:
        print(f"\n{title} (cautious | mid | favourable)")
        print("| Line | cautious | mid | favourable |\n|---|---|---|---|")
        for lab, key, s in [("Leaders first, 2027", "leaders_in", 1), ("Non-payroll, 2027", "nonpay_in", 1),
                            ("Headcount through flows, 2027", "flows_in", 1), ("Dismissals, 2027", "dism_in", 1),
                            ("One-off costs", "oneoff", -1), ("**Opex effect 2027**", "opex_in", 1),
                            ("Pricing and leakage, 2027", "rev_in", 1), ("Revenue lost, 2027", "rev_lost_in", -1),
                            ("Extra attrition, 2027", "attr_in", -1), ("**Profit effect 2027**", "profit_in", 1),
                            ("**Opex effect, run-rate**", "opex_rr", 1), ("**Profit effect, run-rate**", "profit_rr", 1),
                            ("Two-year profit (2027 + run-rate)", "two_year", 1)]:
            print(row(lab, key, opts, s))
        print("| Opex 2027, pts | " + " | ".join(pts(o["opex_in"]) for o in opts) + " |")
        print("| Opex run-rate, pts | " + " | ".join(pts(o["opex_rr"]) for o in opts) + " |")
        print("| Dismissals | " + " | ".join(str(o["dismissals"]) for o in opts) + " |")
        for o in opts:
            check(o["opex_in"], o["leaders_in"] + o["nonpay_in"] + o["flows_in"] + o["dism_in"] - o["oneoff"], "opex_in")
            check(o["profit_in"], o["opex_in"] + o["rev_in"] - o["rev_lost_in"] - o["attr_in"], "profit_in")

    print("\nBLANKET: the dismissals on their own")
    for key in ["dismissals", "billable_cut", "utilised_cut", "dism_net_in", "dism_net_rr", "be_in", "be_rr"]:
        print(f"{key}: " + " | ".join(f(o[key]) for o in B))
    print(f"Residual opex gap of recommended vs Target A, run-rate: " + " | ".join(f(tA - o["opex_rr"]) for o in R))
    print(f"Residual profit gap of recommended vs Target A value, run-rate: " + " | ".join(f(tA - o["profit_rr"]) for o in R))

    print("\nSIDE BY SIDE, mid")
    r, bl = R[1], B[1]
    for name, o in [("Do nothing", None), ("Blanket", bl), ("Recommended", r)]:
        oi = 0 if o is None else o["opex_in"]
        val = b["dn27"] - oi
        print(f"{name}: 2027 opex {f(val)} ({100 * (val / INPUTS['opex_2026'] - 1):+.1f}% vs 2026)")
    print(f"Difference recommended - blanket: 2027 profit {f(r['profit_in'] - bl['profit_in'])}, "
          f"run-rate profit {f(r['profit_rr'] - bl['profit_rr'])}, two-year {f(r['two_year'] - bl['two_year'])}")

    print("\nQUARTERS 2027, mid")
    Q = quarters(1)
    for key, title in [("rec", "Recommended"), ("bl", "Blanket 8%")]:
        print(f"\n{title}\n| Line | Q1 | Q2 | Q3 | Q4 | 2027 |\n|---|---|---|---|---|---|")
        for line in Q[key][0].keys():
            vals = [q[line] for q in Q[key]]
            lab = f"**{line}**" if line in ("Opex effect", "Profit effect") else line
            print(f"| {lab} | " + " | ".join(f(v) for v in vals) + f" | {f(sum(vals))} |")
    check(sum(q["Profit effect"] for q in Q["rec"]), R[1]["profit_in"], "rec quarters")
    check(sum(q["Profit effect"] for q in Q["bl"]), B[1]["profit_in"], "bl quarters")
    check(sum(q["Opex effect"] for q in Q["bl"]), B[1]["opex_in"], "bl opex quarters")
    print("\nAll totals reconcile.")
