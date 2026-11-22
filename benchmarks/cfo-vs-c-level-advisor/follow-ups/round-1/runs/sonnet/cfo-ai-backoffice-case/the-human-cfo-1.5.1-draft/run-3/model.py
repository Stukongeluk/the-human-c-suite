# Business case model: 30% of a 90-person finance/back-office team. ALL inputs are labelled estimates (SEK m) to be replaced with payroll aggregates.
import json
HC=90; TARGET=27
LOADED=0.85   # SEK m per FTE per year, fully loaded (salary ~0.60 + employer charges 31.42% + pension/benefits) -- ESTIMATE
LAS_FACTOR=0.90  # LAS seniority order: leavers are the shortest-serving, ~10% cheaper than average -- ESTIMATE
q=lambda x:x/4
Q=['Y1Q1','Y1Q2','Y1Q3','Y1Q4','Y2Q1','Y2Q2','Y2Q3','Y2Q4']
def z(): return [0.0]*8

# ---- Task sizing (FTE-equivalents of work, estimate; scope split of the 90) ----
scope={'Accounts payable':24,'Reconciliations':22,'Reporting/FP&A':18,'Other (claims acctg, reinsurance, tax, treasury, controls)':26}
share={'Accounts payable':(0.35,0.50,0.65),'Reconciliations':(0.30,0.45,0.60),'Reporting/FP&A':(0.15,0.27,0.40),'Other (claims acctg, reinsurance, tax, treasury, controls)':(0.05,0.12,0.20)}
sizing={}
for i,n in enumerate(['low','base','high']):
    sizing[n]=round(sum(scope[k]*share[k][i] for k in scope),1)

# ---- Option A: board ask, 27 involuntary exits in year 1 ----
A={}
frac=[0,0,0.6,1.0,1,1,1,1]            # share of 27 FTE-quarters saved (MBL talks + 4-month AF notice + LAS notice => first exits ~end Q2)
A['Gross saving']=[27*LOADED*LAS_FACTOR/4*f for f in frac]
sev=z(); sev[1]=27*0.4*LOADED*LAS_FACTOR*0.5; sev[2]=27*0.4*LOADED*LAS_FACTOR*0.5   # ~4 months' pay package, paid at exit
A['Severance/packages (est. 4 months pay)']=[-x for x in sev]
tr=z(); tr[1]=-27*0.04*0.5; tr[2]=-27*0.04*0.5
A['Transition support, legal, union process']=[a+b for a,b in zip(tr,[-0.5,-0.5,0,0,0,0,0,0])]
cover=[0,0,0.30,0.45,0.60,0.70,0.80,0.85]  # share of the removed work the AI really covers when the people are gone (no pilot gate)
uncov=[(1-c)*27*LOADED/4*(1 if f>0 else 0)*f for c,f in zip(cover,frac)]
A['Work still to be done: 60% bought back at 1.4x (contractors/overtime)']=[-0.6*1.4*u for u in uncov]
A['Extra attrition: +5 pts regretted leavers, replaced at 0.9x salary']=[0,0,-0.5*3*LOADED*0.9/2,-0.5*3*LOADED*0.9/2,-0.5*3*LOADED*0.9/2 ,-0.5*3*LOADED*0.9/2,0,0]
A['Rehiring 4 of the 27 roles in year 2 (fees + ramp, 0.5x)']=[0,0,0,0,-4*0.5*LOADED/2,-4*0.5*LOADED/2,0,0]
Aai=[-3.0,-3.5,-4.8,-5.7,-3.0,-3.0,-3.0,-3.0]  # rushed rollout; includes 20% premium
A['AI programme: licences, integration, data, controls, review']=Aai

# ---- Option B: gated plan, freeze + attrition + voluntary exits + redeploy, AI staged by evidence ----
B={}
ATTR=HC*0.09/4; NOBACKFILL=0.8       # 9% attrition ESTIMATE; 80% of leavers not backfilled (20% exceptions in control roles)
cum=[]; c=0
for i in range(8):
    c+=ATTR*NOBACKFILL; cum.append(c)
avg=[(cum[i]+(cum[i-1] if i else 0))/2 for i in range(8)]  # mid-quarter
B['Gross saving: freeze + attrition (not backfilled)']=[a*LOADED/4 for a in avg]
volfte=[0,0,0,5,5,5,5,5]; volprev=[0,0,0,0,5,5,5,5]
B['Gross saving: 5 voluntary exits (end Q4 Y1, after gate 2)']=[v*LOADED/4 for v in volprev]
vp=z(); vp[3]=-5*0.5*LOADED
B['Voluntary exit packages (est. 6 months pay) + job-security-council support']=vp
B['Backfill exceptions and temporary cover during pilots']=[-0.3,-0.4,-0.4,-0.4,-0.3,-0.3,-0.2,-0.2]
B['Redeployed staff: reskilling time (paid)']=[0,-0.4,-0.6,-0.6,-0.4,-0.3,-0.2,-0.2]
B['Extra attrition from change (est. +1 pt)']=[0,0,-0.2,-0.2,-0.2,-0.2,-0.1,-0.1]
Bai=[-2.5,-3.0,-3.5,-3.5,-3.0,-3.0,-3.0,-3.0]
B['AI programme: licences, integration, data, controls, review']=Bai

def tot(d): 
    t=[sum(v[i] for v in d.values()) for i in range(8)]
    return t
def yr(t): return round(sum(t[:4]),1),round(sum(t[4:]),1)
out={}
for name,d in (('A',A),('B',B)):
    t=tot(d); cumul=[]; s=0
    for x in t: s+=x; cumul.append(round(s,1))
    out[name]={'lines':{k:[round(x,2) for x in v] for k,v in d.items()},'net':[round(x,2) for x in t],'Y1':yr(t)[0],'Y2':yr(t)[1],'cum':cumul}
out['sizing_fte']=sizing
out['team_end_Y1_B']=round(HC-cum[3]-5,1); out['team_end_Y2_B']=round(HC-cum[7]-5,1)
out['A_headcount_end']=HC-27
# Run-rate year 3 steady state (annualised)
b_y3_gross=(cum[7]+ATTR*NOBACKFILL*4/2+5)*LOADED  # roughly mid-Y3 average
out['B_Y3_leavers_cum_end']=round(cum[7]+ATTR*NOBACKFILL*4+5,1)
# break-even: steady-state coverage at which A's Y2 net saving is zero
for cov in [0.5,0.6,0.7,0.8,0.9,1.0]:
    gross=27*LOADED*LAS_FACTOR; buy=0.6*1.4*(1-cov)*27*LOADED; ai=12.0; 
    out.setdefault('A_steady',{})[cov]=round(gross-buy-ai,1)
print(json.dumps(out,indent=1))

# ---- Year 3 (annual, simplified) ----
b_avg_fte=(cum[7]+5)+ATTR*NOBACKFILL*4/2
B_y3=b_avg_fte*LOADED-8.0-1.0-0.3
cov_y3=0.90
A_y3=27*LOADED*LAS_FACTOR-0.6*1.4*(1-cov_y3)*27*LOADED-8.0
print('Y3 B',round(B_y3,1),'cum3',round(out['B']['cum'][-1]+B_y3,1),'| Y3 A',round(A_y3,1),'cum3',round(out['A']['cum'][-1]+A_y3,1))
print('B avg FTE out Y3',round(b_avg_fte,1),'end',out['B_Y3_leavers_cum_end'])
# sensitivity: B cumulative 3-yr if AI run cost +/-30% and attrition 6% vs 12%
for ai_mult in (0.7,1.0,1.3):
  for attr in (0.06,0.09,0.12):
    ATT=HC*attr/4; c=0; cm=[]
    for i in range(12):
        c+=ATT*NOBACKFILL; cm.append(c)
    tot3=0
    for i in range(12):
        prev=cm[i-1] if i else 0
        avgf=(cm[i]+prev)/2
        vol=5 if i>=4 else 0
        gross=(avgf+vol)*LOADED/4
        ai=(Bai[i] if i<8 else -2.0)*ai_mult
        other=(-0.7-0.0) if i<8 else -0.325
        pk=-2.12 if i==3 else 0
        tot3+=gross+ai+other+pk
    print('AIx',ai_mult,'attr',attr,'3yr cum B',round(tot3,1))
