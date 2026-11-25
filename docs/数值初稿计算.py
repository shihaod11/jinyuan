def mlife(L): L=min(L,85); return 18*1.08**(L-1)*(1+0.05*(L-1))
def mdmg(L): L=min(L,85); return 6*1.05**(L-1)*(1+0.025*(L-1))
def xpneed(L): return round((40*L**2.6+120*L)*(1+max(0,L-60)*0.12)*(1+max(0,L-85)*0.25),-1)
def mxp(L): L=min(L,85); return 25*1.055**(L-1)*(1+0.02*(L-1))
def plife(L):
    base=40+10*L+(20+1.6*L)/2; flat=min(400,5*L); inc=min(1.6,0.02*L)
    return (base+flat)*(1+inc)
def pdps(L):
    base=8*(1+0.11*min(L,85)); gem=1.12**(min(20,1+L/4.2)-1); inc=1+min(3.5,0.045*L)
    sup=1.25**min(5,1+L//15); crit=1+min(0.8,0.01*L); spd=1.4+min(0.6,0.008*L)
    return base*gem*inc*sup*crit*spd
cum=0; kph=4000; out=[]
for L in range(1,100):
    kills=xpneed(L)/mxp(L); cum+=kills/kph
    if L in [1,5,10,15,20,25,30,40,50,60,70,80,85,90,95,99]:
        out.append((L,round(mlife(L)),round(mdmg(L)),int(xpneed(L)),round(mxp(L)),round(kills),round(cum,1),round(plife(L)),round(pdps(L)),round(mlife(L)/pdps(L),2)))
for o in out: print(o)
