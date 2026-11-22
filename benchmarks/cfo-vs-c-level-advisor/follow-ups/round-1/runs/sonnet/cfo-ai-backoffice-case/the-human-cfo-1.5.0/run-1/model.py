# Illustrative model, SEK millions. All inputs are labelled ESTIMATES to be replaced with ledger/payroll/pilot data.
LOADED = 0.80      # fully loaded cost per FTE per year (salary ~0.58 + employer charges 31.42% + pension/benefits) EST
SAL = 0.58         # salary only EST
Q = LOADED/4
FTE = 90
Y = ["Q1-27","Q2-27","Q3-27","Q4-27","2028"]
# AI cost (same for both options that use AI) EST
oneoff_ai = [1.2,1.6,1.2,1.0,0.0]      # integration, data work, controls build = 5.0
run_ai    = [0.4,0.7,0.9,0.9,3.5]      # licences/usage, monitoring, model & control ops
# Capacity AI actually frees, FTE-equivalent average in period (low/base/high), gated by pilot
cap = {"low": [0,0,1.5,3,6],"base":[0,0,3,6,11],"high":[0,0,4,9,16]}
def sc(a,q4,y): return [x*(q if i<4 else 4*q) for i,(x,q) in enumerate(zip(a,[q4]*5))]
def A(c):
    # Board ask: 27 FTE out by redundancy. Decision Jan-27; MBL talks Q1; AF notification 4 months (26-100 people);
    # notice ~2 months -> exits ~1 Jul 27. Notice paid Q2 (no saving yet).
    n=27; out=[0,0,n*Q,n*Q,n*LOADED]
    sev=[0,7.6,0,0,0]                  # severance/TRR/outplacement/legal EST (4 mths salary + 60k + 0.8m legal): 27*.58/3 + 1.6 + .8
    gap=[max(0,(n if i>=2 else 0)-c[i]) for i in range(5)]
    cover=[g*0.6*LOADED*1.3*(0.25 if i<4 else 1) for i,g in enumerate(gap)]   # 60% of gap covered by contractors/overtime at 1.3x
    unmet=[g*0.4 for g in gap]
    rehire=[0,0,0,0,27*0.25*0.75*SAL]  # 25% of roles refilled, cost 0.75x salary
    attr=[0,0,0,0,5*SAL]               # ~5 extra regretted leavers replaced at 1x salary
    ai=[o+r for o,r in zip(oneoff_ai,run_ai)]
    net=[out[i]-sev[i]-cover[i]-rehire[i]-attr[i]-ai[i] for i in range(5)]
    return dict(gross=out,sev=sev,cover=cover,rehire=rehire,attr=attr,ai=ai,net=net,unmet=unmet)
def B(c):
    red=[0.5,1.5,3.5,5.5,10] if c is cap["base"] else None
    # reductions follow freed capacity via freeze + attrition (~9 leavers/yr natural) -> never ahead of the gate
    red=[min(r, c[i]+ (0.5 if i<2 else 0)) for i,r in enumerate([0.5,1.5,3.5,5.5,10])]
    gross=[red[i]*(Q if i<4 else LOADED) for i in range(5)]
    redeploy=[0.3,0.3,0.3,0.3,0.8]; mbl=[0.2,0.1,0.1,0.1,0.0]   # reskilling, rep/consultation, change EST
    ai=[o+r for o,r in zip(oneoff_ai,run_ai)]
    net=[gross[i]-redeploy[i]-mbl[i]-ai[i] for i in range(5)]
    return dict(gross=gross,redeploy=redeploy,mbl=mbl,ai=ai,net=net)
def row(n,v): return f"| {n} | "+" | ".join(f"{x:6.1f}" for x in v)+f" | {sum(v[:4]):6.1f} | {sum(v):6.1f} |"
H="| Line | "+" | ".join(Y)+" | 2027 total | 2027+2028 |\n|---|---|---|---|---|---|---|---|---|"
for k in ["base","low","high"]:
    a=A(cap[k]); b=B(cap[k])
    print(f"\n## Capacity case: {k} (FTE-equiv freed avg per period: {cap[k]})")
    print("\nOption A - board ask (27 exits, redundancy)\n"+H)
    for n,key in [("Gross saving","gross"),("Severance/TRR/legal","sev"),("Gap cover (contractors/overtime)","cover"),("Rehiring","rehire"),("Extra attrition","attr"),("AI cost (one-off+run)","ai"),("NET","net")]:
        sgn=1 if key in("gross","net") else -1
        print(row(n,[sgn*x for x in a[key]]))
    print("Unmet work (FTE-equiv, not costed):",[round(x,1) for x in a['unmet']])
    print("\nOption B - gated plan (freeze, attrition, redeploy)\n"+H)
    for n,key in [("Gross saving (FTE not backfilled)","gross"),("Redeployment/reskilling","redeploy"),("Consultation/change","mbl"),("AI cost (one-off+run)","ai"),("NET","net")]:
        sgn=1 if key in("gross","net") else -1
        print(row(n,[sgn*x for x in b[key]]))
# run-rate end-2028 and break-even
print("\nRun-rate end-2028 (annual, SEK m): AI run 3.5")
for k,e in [("low",8),("base",13),("high",18)]:
    print(k,"capacity FTE-eq",e,"% of 90:",round(e/90*100,1),"payroll value",round(e*LOADED,1),"net of AI run",round(e*LOADED-3.5,1))
print("Board ask run-rate gross:",round(27*LOADED,1),"; AI run 3.5 -> net",round(27*LOADED-3.5,1),"; needs 27 FTE-eq of real capacity = 30% of 90, plus ~",round(3.5/LOADED,1),"FTE-eq just to pay AI run")
print("Break-even capacity vs run cost only:",round(3.5/LOADED,1),"FTE-eq; incl. 5.0 one-off over 3 yrs:",round((3.5+5/3)/LOADED,1))
