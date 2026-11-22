# Illustrative model, all inputs are labelled estimates (mSEK = million SEK). Replace with ledger/payroll data.
L=0.90            # fully loaded cost per FTE per year, mSEK (estimate)
Q=L/4
N=90
areas={'AP':25,'Recon':20,'Reporting':25,'Other':20}   # assumed split of 90 FTE
share={'low':{'AP':.15,'Recon':.10,'Reporting':.04,'Other':0},
       'base':{'AP':.30,'Recon':.22,'Reporting':.10,'Other':0},
       'high':{'AP':.50,'Recon':.40,'Reporting':.20,'Other':0}}
stop={'low':1,'base':3,'high':5}   # FTE-equivalent from stopping/simplifying work
REVIEW=0.25                        # share of freed hours spent on review/exceptions
ramp=[0,.15,.40,.70,.85,.95,1,1]   # share of steady-state capacity by quarter (8 quarters)
def cap(c):
    gross=sum(areas[a]*share[c][a] for a in areas)
    net=gross*(1-REVIEW)+stop[c]
    return gross,net
for c in share:
    g,n=cap(c); print(c,'gross AI FTE-eq %.1f, net steady-state capacity %.1f (%.0f%% of 90)'%(g,n,100*n/N))
def capq(c): return [cap(c)[1]*r for r in ramp]

def yr(x): return sum(x[:4]),sum(x[4:8])
def show(name,rows):
    print('\n'+name)
    tot=[0]*8
    for k,v in rows.items():
        print('%-34s'%k,' '.join('%6.1f'%x for x in v),'| Y1 %6.1f Y2 %6.1f'%yr(v))
        tot=[a+b for a,b in zip(tot,v)]
    print('%-34s'%'NET (cash, +=benefit)',' '.join('%6.1f'%x for x in tot),'| Y1 %6.1f Y2 %6.1f'%yr(tot), ' cum %.1f'%sum(tot))
    return tot

# ---- Option B: board ask, 27 FTE out (4 natural attrition + 23 redundancies)
def optB(c):
    out=[0,3,20,27,27,27,27,27]        # average FTE out per quarter (consultation + notice delay)
    rows={}
    rows['Gross payroll saving']=[o*Q for o in out]
    rows['AI build/run (rushed)']=[-2.5,-3,-3.5,-1.0,-1.25,-1.25,-1.25,-1.25]
    rows['Transition packages (23 x 0.3)']=[0,-1.7,-3.5,-1.7,0,0,0,0]
    rows['Counsel, union talks, outplacement']=[-0.5,-0.4,-0.2,-0.1,0,0,0,0]
    cq=capq(c)
    short=[max(0,o-k) for o,k in zip(out,cq)]
    rows['Work still to do: contractors @1.3x']=[-s*Q*1.3 for s in short]
    rows['Extra attrition (+4) backfill 0.5 ea']=[0,0,-0.5,-1.0,-0.5,0,0,0]
    rows['Rehire ~25% of 23 roles @0.5 ea']=[0,0,0,0,-1.0,-1.0,-0.5,-0.5]
    return rows
# ---- Option C: staged
def optC(c):
    # headcount out: attrition unfilled (~8%/yr = 7) + voluntary exits after gate; capped by AI+stop capacity
    cq=capq(c)
    att=[0.5,2,4,6,8,10,12,14]
    vol=[0,0,0,0,0,1,3,3]
    cap_limit=cq   # never take out more than capacity actually released
    out=[min(a+v,k+1.0) for a,v,k in zip(att,vol,cap_limit)]
    out=[max(0,o) for o in out]
    rows={}
    rows['Gross payroll saving']=[o*Q for o in out]
    rows['AI build/run (phased)']=[-1.0,-1.0,-2.5,-2.5,-1.0,-1.0,-1.0,-1.0]
    rows['Controls, audit, vendor risk']=[-0.2]*8
    rows['Reskilling/redeployment budget']=[-0.1,-0.2,-0.2,-0.2,-0.1,-0.1,-0.1,-0.1]
    rows['Voluntary packages (up to 3 x 0.3)']=[0,0,0,0,0,-0.3,-0.3,-0.3]
    rows['Counsel and consultation']=[-0.1,-0.1,0,0,0,0,0,0]
    return rows,out
if __name__=='__main__':
    for c in ['low','base','high']:
        print('\n================',c.upper())
        t=show('B board ask',optB(c))
        rows,out=optC(c); print('C FTE out/quarter',[round(x,1) for x in out])
        show('C staged',rows)
    print('\nGross run-rate of 27 FTE: %.1f mSEK/yr; total base 90 FTE: %.1f'%(27*L,90*L))
    # break-even for B: base case, contractor share
