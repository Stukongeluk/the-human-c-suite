"""Savings model: 80 redundancies, NL + BE, FY2027 by quarter. All inputs are labelled estimates."""
import json
N_NL, N_BE = 56, 24                      # ESTIMATE split
COST_NL, COST_BE = 63_000, 70_000        # ESTIMATE fully loaded EUR/yr
N = N_NL + N_BE
BLEND = (N_NL*COST_NL + N_BE*COST_BE)/N
REV, CM = 120_000_000, 0.22              # ESTIMATE revenue, contribution margin
SC = {  # exit month = last month paid (1=Jan). Saving starts the month after.
 "fast": dict(nl_exit=4, be_exit=8,  leak=.06, rehire=.05, extra_attr=6,  rev_loss=.001, sev_nl=14_000, sev_be=9_000, outpl=4_000, fixed=250_000, premium=1.5),
 "base": dict(nl_exit=6, be_exit=10, leak=.12, rehire=.08, extra_attr=12, rev_loss=.003, sev_nl=10_000, sev_be=6_000, outpl=5_000, fixed=350_000, premium=1.0),
 "slow": dict(nl_exit=9, be_exit=12, leak=.20, rehire=.12, extra_attr=20, rev_loss=.006, sev_nl=10_000, sev_be=6_000, outpl=5_000, fixed=450_000, premium=1.0),
}
REPL = 18_000   # ESTIMATE replacement cost per extra leaver (recruit + ramp), frontline-heavy workforce
REHIRE_FEE = 12_000
def q(months):  # months list -> quarter totals
    return [sum(months[i*3:(i+1)*3]) for i in range(4)]
def run(s):
    p = SC[s]
    gross=[0]*12
    for m in range(12):
        gross[m] = (N_NL*COST_NL/12 if m+1>p["nl_exit"] else 0) + (N_BE*COST_BE/12 if m+1>p["be_exit"] else 0)
    leak=[-g*p["leak"] for g in gross]
    # rehired roles refilled ~9 months after exit on avg for base; modelled as starting month 10 (fast: 8, slow: 12 -> none in 2027)
    start = {"fast":8,"base":10,"slow":13}[s]
    rehire=[-(N*p["rehire"]*BLEND/12) if m+1>=start else 0 for m in range(12)]
    # one-offs
    sev=[0]*12; out=[0]*12; adv=[0]*12; rec=[0]*12; attr=[0]*12; rev=[0]*12
    sev[p["nl_exit"]-1] -= N_NL*p["sev_nl"]*p["premium"]
    sev[p["be_exit"]-1] -= N_BE*p["sev_be"]
    out[2] -= (N_NL+N_BE)*p["outpl"]*0.5; out[4] -= (N_NL+N_BE)*p["outpl"]*0.5   # support starts at notice
    adv[0] -= p["fixed"]*0.4; adv[2] -= p["fixed"]*0.3; adv[5] -= p["fixed"]*0.3
    if start<=12: rec[start-1] -= N*p["rehire"]*REHIRE_FEE
    for m in range(12): attr[m] -= p["extra_attr"]*REPL/12 if m>=3 else 0
    for m in range(12): rev[m] -= REV*p["rev_loss"]*CM/12 if m+1>p["nl_exit"] else 0
    lines={"Gross saving (from actual exit dates)":gross,"Work still to be done (overtime, agency)":leak,
      "Rehired roles (salary cost returns)":rehire,"Severance, transition and social-plan payments":sev,
      "Outplacement and transition support":out,"Legal, adviser, works-council costs":adv,
      "Rehiring fees":rec,"Extra voluntary attrition (replacement cost)":attr,"Revenue at risk (margin lost)":rev}
    net=[sum(l[m] for l in lines.values()) for m in range(12)]
    res={k:q(v) for k,v in lines.items()}; res["NET (cash approx.)"]=q(net)
    return res, sum(net)
def yr2(s):
    p=SC[s]; g=N*BLEND; 
    return g*(1-p["leak"]-p["rehire"]) - p["extra_attr"]/2*REPL - REV*p["rev_loss"]*CM
out={}
for s in SC:
    r,t=run(s); out[s]={"quarters":r,"FY2027_net":t,"FY2027_gross":sum(r["Gross saving (from actual exit dates)"]),"Y2028_net_runrate":yr2(s)}
print("BLEND loaded cost", round(BLEND), "full-year gross if all 80 left 1 Jan:", round(N*BLEND))
print("Cost per head needed for EUR6M:", 6_000_000/N)
for s,o in out.items():
    print("\n==",s, "FY27 gross", round(o["FY2027_gross"]), "FY27 net", round(o["FY2027_net"]), "2028 net", round(o["Y2028_net_runrate"]))
    for k,v in o["quarters"].items(): print(f"{k:50s}", [round(x/1000) for x in v], round(sum(v)/1000))
# break-even for base: revenue loss (as % of revenue) that wipes FY27 net
b=out["base"]; ex_rev=b["FY2027_net"]-sum(b["quarters"]["Revenue at risk (margin lost)"])
print("\nbase FY27 net excluding revenue risk", round(ex_rev), "-> break-even revenue loss", round(ex_rev/CM), "=", round(ex_rev/CM/REV*100,2),"% of revenue (annualised from exits is bigger)")
# sensitivities on base
import copy
def net_with(**kw):
    old={k:SC["base"][k] for k in kw}; SC["base"].update(kw); r,t=run("base"); SC["base"].update(old); return t
print("sens NL exit month 4/6/9:", [round(net_with(nl_exit=m)) for m in (4,6,9)])
print("sens leakage 6/12/20%:", [round(net_with(leak=x)) for x in (.06,.12,.20)])
# alternative levers: (low, high) full-year EUR, in-year share, temporary?
LEV={"Purchasing, subcontractor and agency rates (2-4% of ~EUR45M third-party spend)":(900_000,1_800_000,.5,False),
"Pricing and revenue leakage (0.5-1.0% of ~EUR120M revenue)":(600_000,1_200_000,.6,False),
"Freeze on indirect/office backfill + non-renewal of flex contracts (15-25 roles, from attrition)":(700_000,1_300_000,.5,False),
"Voluntary exit scheme, net of payments (15-25 people, 12-18 month payback)":(400_000,900_000,.35,False),
"Leadership bonus waiver and perks (est. pool EUR0.6-1.0M; one year only, not run-rate)":(600_000,1_000_000,1.0,True)}
lo=hi=0; rr_lo=rr_hi=0
for k,(a,b_,sh,t) in LEV.items():
    lo+=a*sh; hi+=b_*sh
    if not t: rr_lo+=a; rr_hi+=b_
    print(f"{k[:70]:70s} FY27 {a*sh/1e3:.0f}-{b_*sh/1e3:.0f}k  full-year {a/1e3:.0f}-{b_/1e3:.0f}k")
print("alt FY27 total", round(lo), round(hi), " run-rate (excl temporary)", rr_lo, rr_hi)
json.dump(out, open("model_output.json","w"), indent=1)
