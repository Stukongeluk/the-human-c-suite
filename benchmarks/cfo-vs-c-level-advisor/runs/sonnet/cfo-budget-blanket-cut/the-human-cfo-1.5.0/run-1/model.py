# All figures EUR thousands, ALL INPUTS ARE LABELLED ESTIMATES scaled from: 600 people, payroll 68% of opex.
HC=600; LOADED=85.0                      # est. fully loaded cost per FTE
PAY=HC*LOADED                            # 51,000
OPEX=PAY/0.68                            # 75,000
NONPAY=OPEX-PAY                          # 24,000
TARGET=0.08*OPEX                         # 6,000
REV=OPEX*1.04                            # est. thin margin ~4% -> 78,000
BILL=0.70*HC                             # est. 70% billable
REV_PER_BILL=REV/BILL                    # ~186
Q=[0,1,2,3]
def tot(l): return sum(l)
def qs(run, fr): return [run/4*f for f in fr]

# ---- Option A: blanket 8% ----
A_pay_run=0.08*PAY; A_np_run=0.08*NONPAY; A_fte=A_pay_run/LOADED
A_pay=qs(A_pay_run,[0,.15,.70,1.0]); A_np=qs(A_np_run,[.25,.75,1,1])
A_one=[0,-0.4*20*A_fte,-0.6*20*A_fte,0]           # est. EUR 20k/exit all-in (transition pay, legal, outplacement)
share_bill=0.60; trans=0.25                        # est.
A_lost_run=A_fte*share_bill*REV_PER_BILL*trans
A_rev=[-x for x in qs(A_lost_run,[0,.15,.70,1.0])]
A_att_total=18*0.5*LOADED                          # +3pt attrition = 18 leavers x 0.5 x loaded (Gallup low end)
A_att=[0,-.2*A_att_total,-.4*A_att_total,-.4*A_att_total]
A_net=[sum(x) for x in zip(A_pay,A_np,A_one,A_rev,A_att)]
A_y2_rehire=-0.20*A_fte*LOADED*(0.20+0.25)
A_y2=A_pay_run+A_np_run-A_lost_run+A_y2_rehire-0.0

# ---- Option B: targeted ----
B1_run=0.125*NONPAY
B1=qs(B1_run,[.15,.5,.85,1.0]); B1_one=[0,-0.05*B1_run,0,0]
leavers=0.12*HC; unfilled=35
B2_run=unfilled*LOADED
B2=[unfilled*LOADED/4*f for f in [.125,.375,.625,.875]]
B2_lost_run=unfilled*0.25*REV_PER_BILL*0.25
B2_rev=[-B2_lost_run/4*f for f in [.125,.375,.625,.875]]
B3_run=0.01*OPEX; B3=qs(B3_run,[0,.4,.8,1.0])
B4_var=660; B4_fix=264                              # 15 leaders x EUR 220k, 20% variable; 10% fixed cut from Q2 (needs consent)
B4=[B4_var/4+0, B4_var/4+B4_fix/4, B4_var/4+B4_fix/4, B4_var/4+B4_fix/4]
B_net=[sum(x) for x in zip(B1,B1_one,B2,B2_rev,B3,B4)]
B_y2=B1_run+B2_run-B2_lost_run+B3_run

def row(n,l,y2=None):
    return f"| {n} | "+" | ".join(f"{x:,.0f}" for x in l)+f" | {tot(l):,.0f} |"+(f" {y2:,.0f} |" if y2 is not None else "")
if __name__=="__main__":
    print("OPEX",OPEX,"PAY",PAY,"NONPAY",NONPAY,"TARGET",TARGET,"REV",REV,"RPB",REV_PER_BILL)
    print("A fte",A_fte,"A pay",A_pay_run,"np",A_np_run,"lost_run",A_lost_run)
    for n,l in [("A pay",A_pay),("A np",A_np),("A one",A_one),("A rev",A_rev),("A att",A_att),("A net",A_net)]: print(row(n,l))
    print("A y2 run-rate net approx",A_y2)
    for n,l in [("B1",B1),("B1one",B1_one),("B2",B2),("B2rev",B2_rev),("B3",B3),("B4",B4),("B net",B_net)]: print(row(n,l))
    print("B y2 run",B_y2, "B2lost",B2_lost_run)
    # break-even translation share for A in-year
    base_wo_rev=tot(A_pay)+tot(A_np)+tot(A_one)+tot(A_att)
    per_share=sum(A_rev)/trans
    print("A break-even translation share",base_wo_rev/(-per_share))
    # sensitivities
    for t in (0,0.5):
        print("A net yr1 at translation",t, base_wo_rev+per_share*t)
    print("A, if baseline includes 2.4m inflation: gap",TARGET+0.035*PAY+0.025*NONPAY)
    print("B yr1 low nonpay 10%:",tot(B_net)-tot(B1)+tot(B1)*0.10/0.125)
    print("B yr1 attrition 9%:",tot(B_net)-tot(B2)-tot(B2_rev)+(tot(B2)+tot(B2_rev))*0.75)
    print("pricing 1%",REV*0.01, "EBIT",REV-OPEX)
