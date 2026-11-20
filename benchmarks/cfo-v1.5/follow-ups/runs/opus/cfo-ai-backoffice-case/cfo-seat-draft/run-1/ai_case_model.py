#!/usr/bin/env python3
"""
AI in finance operations: business case model (DRAFT)

What it does
  Compares four options for the 90-person finance and back-office team, net of
  every cost, by quarter for 2027 and by year for 2028-2029:
    0  Do nothing (no programme)
    1  The board's ask: AI plus 27 compulsory redundancies, exits effective 1 July 2027
    2  Redundancies timed to proven capacity: AI first, one round of 24 exits
       effective 1 January 2028
    3  Capacity-led (recommended): AI first; headcount falls only as fast as
       measured capacity, through attrition, a hiring freeze with exceptions and
       redeployment into funded vacancies; no compulsory redundancies planned.
       If, at the 2028 Q2 gate, attrition would leave more than 3 FTE of
       measured capacity unused by end-2029, voluntary terms are offered for
       that surplus (effective 2028 Q3)

Conventions
  * SEK million, constant 2027 prices (no wage inflation), savings positive,
    costs negative, all versus "do nothing".
  * EVERY input below is an ESTIMATE unless marked "given". Replace them with
    ledger, payroll (aggregated, never individual) and HRIS data, and with
    vendor quotes, before anyone relies on the output.
  * P&L and cash differ only for exit packages (provision when the plan is
    announced, cash when people leave). SaaS configuration costs are expensed,
    not capitalised.

Run
  python3 ai_case_model.py            prints all tables as markdown
"""
from copy import deepcopy

QUARTERS = [f"{y} Q{q}" for y in (2027, 2028, 2029) for q in (1, 2, 3, 4)]
N = len(QUARTERS)

PROCESSES = [
    "Accounts payable and expenses",
    "Reconciliations and accounting operations",
    "Reporting (statutory, Solvency II, management, tax)",
    "Leadership, systems and controls",
]

BASE = {
    # --- Team ---------------------------------------------------------------
    "headcount": 90,  # given
    "fte_by_process": dict(zip(PROCESSES, [24, 30, 24, 12])),  # estimate
    # Share of each process's hours that AI can do at the required quality at
    # full run-rate (estimate; the pilot measures this against a baseline)
    "ai_share": dict(zip(PROCESSES, [0.45, 0.30, 0.15, 0.00])),
    "ai_multiplier": 1.0,  # sensitivity lever on the line above
    "simplification_fte": 4.0,  # non-AI: stop unused reports, fewer suppliers, more e-invoices (estimate)
    "oversight_fte": 3.0,  # new work: exceptions, monitoring, control testing, vendor management (estimate)
    # Ramp to full run-rate, per quarter 2027 Q1 .. 2029 Q4 (estimate)
    "ai_ramp": [0.00, 0.10, 0.35, 0.60, 0.75, 0.82, 0.88, 0.95, 1.0, 1.0, 1.0, 1.0],
    "simp_ramp": [0.10, 0.30, 0.60, 0.80] + [1.0] * 8,
    "oversight_ramp": [0.0, 1.0, 1.0, 1.0] + [1.0] * 8,
    # --- Pay (estimates; replace with payroll aggregate) --------------------
    "monthly_salary_sek": 47_000,
    # employer contributions 31.42% (Skatteverket, 2026), occupational pension
    # incl. special payroll tax, holiday pay, other benefits
    "load_factor": 1.47,
    # --- Flows (estimates; replace with HRIS) -------------------------------
    "attrition_annual": 0.10,  # voluntary ~8% + retirements ~2%
    "backfill_cost_per_fte_year": 1.10,  # SEK m, contractors and overtime, blended
    "project_backfill_fte": [2, 2, 2, 2] + [0] * 8,  # cover for staff working on the programme
    "redeploy": [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],  # moves into funded vacancies elsewhere (option 3)
    # --- Programme costs, SEK m per quarter (estimates; get quotes) ---------
    "licences": [0.3, 1.0, 1.0, 1.0] + [1.0] * 8,
    "implementation": [1.5, 3.0, 3.0, 1.5] + [0.25] * 4 + [0.0] * 4,
    "controls_audit": [0.5, 0.5, 0.3, 0.2] + [0.125] * 8,
    "reskilling": [0.3, 0.6, 0.5, 0.4] + [0.15] * 4 + [0.075] * 4,
    # --- Exit costs (estimates; check with counsel and the collective agreement)
    "package_months": 6,  # negotiated packages / agreed lists; no statutory severance in Sweden
    "legal_per_round": 1.0,
    "outplacement_per_person": 0.03,  # top-up beyond the job security council
    "retention_pool": 1.0,  # key people through the transition
    "retraining_stayers": 0.5,  # selection order means leavers are not the people whose tasks went
    "survivor_attrition_uplift": 0.04,  # extra annual voluntary attrition among stayers, 4 quarters
    "replacement_cost_factor": 0.75,  # x annual salary (Gallup range: 0.5x to 2x)
    "recruit_fee": 0.15,  # per permanent rehire
    # Option 3 voluntary window (only if a lasting surplus is measured)
    "voluntary_threshold_fte": 3.0,
    "voluntary_package_months": 9,  # voluntary terms must be attractive enough to choose
}

LINES = [
    ("gross", "Gross people saving (from actual exit or non-replacement dates)"),
    ("packages", "Exit packages"),
    ("legal", "Legal and advisory"),
    ("outplacement", "Outplacement top-up"),
    ("retention", "Retention pool and retraining of stayers"),
    ("extra_attrition", "Extra voluntary attrition (replacement cost)"),
    ("work_backfill", "Work still to be done (contractors, overtime)"),
    ("rehire", "Permanent rehires: recruitment fees"),
    ("licences", "AI licences and usage"),
    ("implementation", "Implementation, integration, data work"),
    ("controls_audit", "Controls, DORA and outsourcing review, audit"),
    ("reskilling", "Reskilling and AI literacy"),
    ("project_backfill", "Backfill for staff working on the programme"),
]
RECURRING = {"gross", "licences", "controls_audit", "reskilling", "work_backfill"}


def derived(a):
    d = {}
    d["annual_loaded"] = a["monthly_salary_sek"] * 12 * a["load_factor"] / 1e6
    d["q_cost"] = d["annual_loaded"] / 4
    d["monthly_loaded"] = a["monthly_salary_sek"] * a["load_factor"] / 1e6
    d["replacement_cost"] = a["replacement_cost_factor"] * a["monthly_salary_sek"] * 12 / 1e6
    runrate_ai = sum(a["fte_by_process"][p] * a["ai_share"][p] for p in PROCESSES) * a["ai_multiplier"]
    d["runrate_ai"] = runrate_ai
    d["cap"] = [
        runrate_ai * a["ai_ramp"][t]
        + a["simplification_fte"] * a["simp_ramp"][t]
        - a["oversight_fte"] * a["oversight_ramp"][t]
        for t in range(N)
    ]
    d["runrate_cap"] = runrate_ai + a["simplification_fte"] - a["oversight_fte"]
    return d


def empty():
    return {k: [0.0] * N for k, _ in LINES}


def programme(a, lines):
    for k in ("licences", "implementation", "controls_audit", "reskilling"):
        lines[k] = [-v for v in a[k]]


def project_backfill(a, d, red, lines):
    bf = a["backfill_cost_per_fte_year"] / 4
    for t in range(N):
        need = a["project_backfill_fte"][t]
        spare = max(0.0, d["cap"][t] - red[t])
        lines["project_backfill"][t] = -(need - min(need, spare)) * bf


def redundancy_option(a, d, size, exit_q, plan_q, rounds_q):
    """Compulsory redundancies of `size`, effective from quarter index exit_q.
    plan_q: quarter the plan is announced (provision); rounds_q: quarters with legal work."""
    lines = empty()
    bf = a["backfill_cost_per_fte_year"] / 4
    red = [0.0] * N
    rehired_prev = 0.0
    for t in range(N):
        if t < exit_q:
            continue
        r = float(size)
        if t >= 8:  # from 2029, a lasting shortfall is filled with permanent rehires
            rehired = max(0.0, size - d["cap"][t])
            lines["rehire"][t] = -max(0.0, rehired - rehired_prev) * a["recruit_fee"]
            rehired_prev = max(rehired_prev, rehired)
            r = size - rehired
        red[t] = r
        lines["work_backfill"][t] = -max(0.0, r - d["cap"][t]) * bf
    for t in range(N):
        lines["gross"][t] = red[t] * d["q_cost"]
    pkg = -size * d["monthly_loaded"] * a["package_months"]
    lines["packages"][plan_q] = pkg
    cash_shift = {"packages": (plan_q, exit_q, pkg)}  # P&L in plan_q, cash in exit_q
    for q in rounds_q:
        lines["legal"][q] = -a["legal_per_round"] / len(rounds_q)
    lines["outplacement"][exit_q] = -size * a["outplacement_per_person"]
    lines["retention"][exit_q] += -a["retraining_stayers"]
    lines["retention"][exit_q + 1] += -a["retention_pool"] / 2
    lines["retention"][exit_q + 3] += -a["retention_pool"] / 2
    survivors = a["headcount"] - size
    for t in range(exit_q, min(N, exit_q + 4)):
        lines["extra_attrition"][t] = -survivors * a["survivor_attrition_uplift"] / 4 * d["replacement_cost"]
    programme(a, lines)
    project_backfill(a, d, red, lines)
    return lines, red, cash_shift, size


def option_0(a, d):
    return empty(), [0.0] * N, {}, 0


def option_1(a, d):
    # MBL negotiation and notification to Arbetsförmedlingen in Q1, notices in
    # Q2, exits effective 1 July 2027 (2027 Q3)
    return redundancy_option(a, d, size=27, exit_q=2, plan_q=1, rounds_q=[0, 1])


def option_2(a, d):
    # Gate after the Q3 2027 pilot results, MBL in Q3, notices in Q4, exits
    # effective 1 January 2028; sized to measured run-rate capacity
    size = int(round(d["runrate_cap"]))
    return redundancy_option(a, d, size=size, exit_q=4, plan_q=3, rounds_q=[2, 3])


def option_3_core(a, d, voluntary=0, vol_q=6):
    """Headcount falls only as fast as measured capacity. `voluntary` people may
    leave on voluntary terms effective quarter vol_q (2028 Q3), agreed the quarter before."""
    lines = empty()
    red = [0.0] * N
    red_prev = 0.0
    for t in range(N):
        need = a["project_backfill_fte"][t]
        ceiling = max(0.0, d["cap"][t] - need)  # capacity first covers the project, then absorbs leavers
        leavers = a["attrition_annual"] / 4 * (a["headcount"] - red_prev)
        outflow = leavers + a["redeploy"][t] + (voluntary if t == vol_q else 0)
        r = min(red_prev + outflow, ceiling)
        red[t] = r
        red_prev = r
    for t in range(N):
        lines["gross"][t] = red[t] * d["q_cost"]
        lines["work_backfill"][t] = -max(0.0, red[t] - d["cap"][t]) * a["backfill_cost_per_fte_year"] / 4
    cash_shift = {}
    if voluntary:
        pkg = -voluntary * d["monthly_loaded"] * a["voluntary_package_months"]
        lines["packages"][vol_q - 1] = pkg
        cash_shift["packages"] = (vol_q - 1, vol_q, pkg)
        lines["legal"][vol_q - 1] = -a["legal_per_round"] / 2
        lines["outplacement"][vol_q] = -voluntary * a["outplacement_per_person"]
        survivors = a["headcount"] - red[vol_q]
        for t in range(vol_q, min(N, vol_q + 4)):
            lines["extra_attrition"][t] = (-survivors * a["survivor_attrition_uplift"] / 2 / 4
                                           * d["replacement_cost"])
    programme(a, lines)
    project_backfill(a, d, red, lines)
    return lines, red, cash_shift


def option_3(a, d):
    # Gate in 2028 Q2: if, on measured capacity, attrition would leave more than
    # `voluntary_threshold_fte` of capacity unused at end-2029, offer voluntary
    # terms (reduced hours, partial retirement, voluntary packages) for that surplus.
    lines, red, cash_shift = option_3_core(a, d)
    surplus = d["cap"][N - 1] - red[N - 1]
    voluntary = int(round(surplus)) if surplus > a["voluntary_threshold_fte"] else 0
    if voluntary:
        lines, red, cash_shift = option_3_core(a, d, voluntary=voluntary)
    return lines, red, cash_shift, 0, voluntary


OPTIONS = [
    ("0. Do nothing", option_0),
    ("1. Board's ask: 27 redundancies, mid-2027", option_1),
    ("2. Redundancies timed to proven capacity, Jan 2028", option_2),
    ("3. Capacity-led, no compulsory redundancies (recommended)", option_3),
]


def run(a):
    d = derived(a)
    out = {}
    for name, fn in OPTIONS:
        res = fn(a, d)
        lines, red, cash_shift, dismissed = res[:4]
        voluntary = res[4] if len(res) > 4 else 0
        pl = [sum(lines[k][t] for k, _ in LINES) for t in range(N)]
        cash = pl[:]
        for _, (pq, cq, amt) in cash_shift.items():
            cash[pq] -= amt
            cash[cq] += amt
        cum, payback = 0.0, None
        for t in range(N):
            cum += cash[t]
            if payback is None and cum >= 0 and any(c != 0 for c in cash[: t + 1]) and t > 0:
                payback = QUARTERS[t]
        runrate = sum(lines[k][N - 1] for k in RECURRING) * 4
        out[name] = dict(lines=lines, red=red, pl=pl, cash=cash, cum_cash=cum,
                         payback=payback, runrate=runrate, dismissed=dismissed, voluntary=voluntary)
    return d, out


# ----------------------------------------------------------------- output ---
PERIODS = [("2027 Q1", [0]), ("2027 Q2", [1]), ("2027 Q3", [2]), ("2027 Q4", [3]),
           ("FY 2027", [0, 1, 2, 3]), ("FY 2028", [4, 5, 6, 7]), ("FY 2029", [8, 9, 10, 11]),
           ("3 years", list(range(N)))]


def f(x):
    if abs(x) < 0.05:
        return "0.0"
    return f"{x:,.1f}"


def option_table(name, r):
    hdr = "| SEK m | " + " | ".join(p for p, _ in PERIODS) + " | Run-rate from 2030 |"
    sep = "|---|" + "---:|" * (len(PERIODS) + 1)
    rows = [hdr, sep]
    for k, label in LINES:
        vals = r["lines"][k]
        if all(abs(v) < 1e-9 for v in vals):
            continue
        cells = [f(sum(vals[i] for i in idx)) for _, idx in PERIODS]
        rr = f(vals[N - 1] * 4) if k in RECURRING else "0.0"
        rows.append(f"| {label} | " + " | ".join(cells) + f" | {rr} |")
    pl_cells = [f(sum(r["pl"][i] for i in idx)) for _, idx in PERIODS]
    cash_cells = [f(sum(r["cash"][i] for i in idx)) for _, idx in PERIODS]
    rows.append("| **Net P&L effect** | " + " | ".join(f"**{c}**" for c in pl_cells) + f" | **{f(r['runrate'])}** |")
    rows.append("| **Net cash effect** | " + " | ".join(f"**{c}**" for c in cash_cells) + f" | **{f(r['runrate'])}** |")
    fte = [f(r["red"][idx[-1]]) for _, idx in PERIODS]
    rows.append("| FTE fewer than today, end of period | " + " | ".join(fte) + f" | {f(r['red'][N-1])} |")
    return f"#### {name}\n\n" + "\n".join(rows) + "\n"


def check_totals(out):
    # every table adds up: lines sum to net, periods sum to 3-year total
    for name, r in out.items():
        for t in range(N):
            assert abs(sum(r["lines"][k][t] for k, _ in LINES) - r["pl"][t]) < 1e-9, name
        assert abs(sum(r["cash"]) - sum(r["pl"])) < 1e-9, name  # timing only
        assert abs(sum(r["pl"][:4]) + sum(r["pl"][4:8]) + sum(r["pl"][8:]) - sum(r["pl"])) < 1e-9


def summary_table(d, out):
    hdr = ("| Option | Net P&L 2027 | Net cash 2027 | Net P&L 2028 | Net P&L 2029 | 3-year net | "
           "Run-rate a year from 2030 | FTE fewer end-2027 | end-2028 | end-2029 | Compulsory dismissals | "
           "Voluntary exits | Cash payback |")
    rows = [hdr, "|---|" + "---:|" * 12]
    for name, r in out.items():
        rows.append(
            f"| {name} | {f(sum(r['pl'][:4]))} | {f(sum(r['cash'][:4]))} | {f(sum(r['pl'][4:8]))} | "
            f"{f(sum(r['pl'][8:]))} | {f(sum(r['pl']))} | {f(r['runrate'])} | {f(r['red'][3])} | "
            f"{f(r['red'][7])} | {f(r['red'][11])} | {r['dismissed']} | {r['voluntary']} | "
            f"{r['payback'] or 'after 2029'} |")
    return "\n".join(rows) + "\n"


def capacity_table(a, d):
    rows = ["| Process | FTE today | AI share of hours at run-rate | FTE of capacity at run-rate |",
            "|---|---:|---:|---:|"]
    tot = 0.0
    for p in PROCESSES:
        c = a["fte_by_process"][p] * a["ai_share"][p] * a["ai_multiplier"]
        tot += c
        rows.append(f"| {p} | {a['fte_by_process'][p]} | {a['ai_share'][p]*a['ai_multiplier']:.0%} | {c:.1f} |")
    rows.append(f"| AI capacity, gross | {a['headcount']} | {tot/a['headcount']:.0%} | {tot:.1f} |")
    rows.append(f"| Plus process simplification (no AI) | | | {a['simplification_fte']:.1f} |")
    rows.append(f"| Less new oversight work | | | -{a['oversight_fte']:.1f} |")
    rows.append(f"| **Net capacity at run-rate** | | **{d['runrate_cap']/a['headcount']:.0%}** | **{d['runrate_cap']:.1f}** |")
    q = ["| | " + " | ".join(QUARTERS) + " |", "|---|" + "---:|" * N,
         "| Net capacity, FTE | " + " | ".join(f"{c:.1f}" for c in d["cap"]) + " |"]
    return "\n".join(rows) + "\n\n" + "\n".join(q) + "\n"


SCENARIOS = [
    ("Base case", {}),
    ("AI does 60% of what we assume", {"ai_multiplier": 0.6}),
    ("AI does 130% of what we assume", {"ai_multiplier": 1.3}),
    ("Attrition 6% a year, not 10%", {"attrition_annual": 0.06}),
    ("No funded vacancies to redeploy into", {"redeploy": [0] * N}),
    ("Exit packages 9 months, not 6", {"package_months": 9}),
    ("Stayers' attrition +8 points, not +4", {"survivor_attrition_uplift": 0.08}),
    ("Backfill SEK 1.3m per FTE-year, not 1.1m", {"backfill_cost_per_fte_year": 1.3}),
    ("Attrition 6% and no funded vacancies", {"attrition_annual": 0.06, "redeploy": [0] * N}),
]


def scenario(overrides):
    a = deepcopy(BASE)
    a.update(overrides)
    return run(a)


def sensitivity_table():
    names = [n for n, _ in OPTIONS[1:]]
    hdr = ("| Scenario | " + " | ".join(f"Opt {n.split('.')[0]}: 3-yr net / FTE end-2029" for n in names)
           + " | Opt 3: voluntary exits offered in 2028 | Opt 3: unused capacity end-2029, FTE |")
    rows = [hdr, "|---|" + "---:|" * (len(names) + 2)]
    for label, ov in SCENARIOS:
        d, out = scenario(ov)
        cells = [f"{f(sum(out[n]['pl']))} / {f(out[n]['red'][11])}" for n in names]
        spare = d["cap"][N - 1] - out[names[-1]]["red"][N - 1]
        rows.append(f"| {label} | " + " | ".join(cells)
                    + f" | {out[names[-1]]['voluntary']} | {f(spare)} |")
    return "\n".join(rows) + "\n"


def breakeven():
    """Where would the board's route (option 1) catch up with the recommended one?"""
    n1, n3 = OPTIONS[1][0], OPTIONS[3][0]

    def net(m, name, extra=None):
        ov = {"ai_multiplier": m}
        ov.update(extra or {})
        _, out = scenario(ov)
        return sum(out[name]["pl"])

    no_window = {"voluntary_threshold_fte": 1e9}

    def solve(g, lo=0.3, hi=3.0):
        if g(lo) > 0 or g(hi) < 0:
            return None
        for _ in range(60):
            mid = (lo + hi) / 2
            if g(mid) < 0:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    vs_attrition_only = solve(lambda m: net(m, n1) - net(m, n3, no_window))
    own_positive = solve(lambda m: net(m, n1))
    grid = [0.5 + 0.05 * i for i in range(31)]  # 50% .. 200%
    best_gap = max(net(m, n1) - net(m, n3) for m in grid)
    return vs_attrition_only, own_positive, best_gap


def main():
    d, out = run(BASE)
    check_totals(out)
    print(f"Loaded cost per FTE: SEK {d['annual_loaded']:.3f}m a year (estimate)")
    print(f"Team cost today: SEK {d['annual_loaded']*BASE['headcount']:.1f}m a year (estimate)")
    print(f"Headline the board may expect: 27 x loaded cost = SEK {27*d['annual_loaded']:.1f}m a year\n")
    print("Totals are computed from unrounded figures, so a row or column can differ by 0.1 from the sum of the rounded cells shown.\n")
    print("### Capacity\n")
    print(capacity_table(BASE, d))
    print("### Summary\n")
    print(summary_table(d, out))
    print("### Options, net and by quarter\n")
    for name, r in out.items():
        if name.startswith("0."):
            continue
        print(option_table(name, r))
    print("### Sensitivities (3-year net P&L, SEK m / FTE fewer at end-2029)\n")
    print(sensitivity_table())
    be_attr, be_pos, best_gap = breakeven()
    print("### Break-even\n")
    print(f"- Option 1's own three-year net turns positive only if AI delivers "
          f"{'more than 3x' if be_pos is None else f'{be_pos:.0%}'} of the capacity assumed.")
    print(f"- Option 1 beats option 3 without its voluntary window (attrition and redeployment only) "
          f"from {'more than 3x' if be_attr is None else f'{be_attr:.0%}'} of the capacity assumed.")
    print(f"- With the voluntary window, option 1 never beats option 3 between 50% and 200% of the "
          f"capacity assumed (closest gap: SEK {best_gap:.1f}m over three years)." if best_gap < 0 else
          f"- With the voluntary window, option 1 beats option 3 by up to SEK {best_gap:.1f}m somewhere "
          f"between 50% and 200% of the capacity assumed.")


if __name__ == "__main__":
    main()
