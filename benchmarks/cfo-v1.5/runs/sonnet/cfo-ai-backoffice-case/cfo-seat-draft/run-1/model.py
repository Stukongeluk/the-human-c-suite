# Illustrative model, SEK millions. Every input is an ESTIMATE to be replaced by payroll, vendor quotes and pilot data.
import json
FTE=90; COST=0.80            # loaded cost per FTE per year (salary + 31.42% social fees + pension + overhead), est.
Q=COST/4
cols=["Q1","Q2","Q3","Q4","Year 2"]
def row(v): return [round(x,1) for x in v]
# AI programme (same in B and C)
oneoff=[1.5,2.0,1.0,0.5,0.0]; run=[0.2,0.5,0.8,1.0,3.5]; ctrl=[0.0,0.4,0.4,0.4,1.6]
ai=[a+b+c for a,b,c in zip(oneoff,run,ctrl)]
# AI capacity released in FTE-equivalents (average in period), base case
cap=[0.5,2,4,7,17]
# Option B: 27 exits, all effective start of Q4 (MBL talks + 4-month AF notice + notice periods)
B_fte=[0,0,0,27,27]; B_mult=[0,0,0,1,4]   # Q4 counted as 1 quarter, Year 2 as 4 quarters
B_gross=[0,0,0,27*Q,27*COST]
sev=[0,0,3.0,2.1,0]           # package ~150k + outplacement ~40k per head, legal/advisory 1.0m, phased
shortfall=[max(0,27-c) if i>=3 else 0 for i,c in enumerate(cap)]
B_backfill=[0,0,0,-shortfall[3]*Q*1.5, -shortfall[4]*COST*1.25*0.5]  # Q4 contractors at 1.5x; Y2 mix contractor/rehire, half of the gap
B_attr=[0,0,0,0,-6*0.6]       # 6 extra regretted leavers x 0.75x salary replacement
B=[B_gross[i]-sev[i]+B_backfill[i]+B_attr[i]-ai[i] for i in range(5)]
# Option C: freeze + attrition + redeploy + voluntary exits
C_fte=[0.5,2,4,6,11.5]
C_gross=[C_fte[i]*Q for i in range(4)]+[11.5*COST]
C_cost=[0,0,0.2,0.4,1.4]      # redeployment training ~0.2m/10 people, voluntary packages 5 x 0.2m + support
C=[C_gross[i]-C_cost[i]-ai[i] for i in range(5)]
def tot(v): return round(sum(v[:4]),1), round(v[4],1), round(sum(v),1)
out={"AI programme cost":row(ai),"B net":row(B),"C net":row(C),"B":tot(B),"C":tot(C),"AI":tot(ai),
"B_gross":row(B_gross),"B_sev":row(sev),"B_backfill":row(B_backfill),"B_attr":row(B_attr),
"C_gross":row(C_gross),"C_cost":row(C_cost),"baseline_cost":FTE*COST,"27fte_cost":27*COST,
"run_rate_Y3_C":round(22*COST-5.1,1),"run_rate_27_after_AI":round(27*COST-5.1,1)}
# sensitivity: AI capacity at 50%/150% of base for Year 2 net of B (shortfall effect)
for k in (0.5,1.0,1.5):
    c=min(27,17*k); sf=27-c
    y2=27*COST-sf*COST*1.25*0.5-6*0.6-ai[4]
    out[f"B_Y2_cap{k}"]=round(y2,1)
    out[f"C_Y2_cap{k}"]=round(11.5*COST-1.4-ai[4],1)
print(json.dumps(out,indent=1))
