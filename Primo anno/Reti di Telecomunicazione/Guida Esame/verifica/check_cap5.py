#!/usr/bin/env python3
from math import sqrt, log, exp, e
fails=[]
def check(n,g,w,tol=1e-9):
    ok=abs(g-w)<=tol*max(1,abs(w)); print(("OK   " if ok else "FAIL ")+f"{n}: {g:.10g} (atteso {w:.10g})")
    if not ok: fails.append(n)
# LCG esempio slide 37
x=7; seq=[x]
for _ in range(7): x=(7*x+7)%10; seq.append(x)
print("LCG:",seq); assert seq==[7,6,9,0,7,6,9,0]
# periodo
x=7;p=0
while True:
    x=(7*x+7)%10;p+=1
    if x==7:break
check("LCG periodo",p,4)
# forma chiusa
n=5; check("LCG forma chiusa",(7**n*7+(7**n-1)//6*7)%10,seq[5])
# CI t-Student: n=10, media 12.4, s=2.1
t=2.262; n=10; s=2.1
check("CI t half-width", t*s/sqrt(n), 1.5025, 1e-3)
check("CI z half-width", 1.96*s/sqrt(n), 1.3015, 1e-3)
# sorgente 2025
gA,gB=2,1
check("durata A",1/gA,0.5); check("durata B",1/gB,1.0)
check("P(A) stazionaria",(1/gA)/(1/gA+1/gB),1/3)
# Sim completo 1
check("F_A inversa",exp(log(0.5+1))-1,0.5); check("e^1-1",e-1,e-1)
cum=[0.4,0.5,0.6,0.7,1.0]; print("cumulate", cum)
# Sim completo 2: L_A
check("L_A c0",900*(1/3)+100,400); check("L_A c1a",1800*(1/3)-200,400); check("L_A c1b",1800*0.5-200,700)
check("masse L_A",900**-1*300+1800**-1*300+0.5,1)
check("I_A inversa",1/(1-0.5),2.0)
# media sorgente B: 4 ms, 1000 bit -> 250 kbit/s
check("rate B",1000/0.004,250000)
# Burke trasformata
lam,mu,s_=1.3,2.0,0.7; rho=lam/mu
lhs=rho*mu/(mu+s_)+(1-rho)*mu/(mu+s_)*lam/(lam+s_)
check("Burke",lhs,lam/(lam+s_))
# P-K M/M/1
W=lam*(2/mu**2)/(2*(1-rho)); check("PK MM1",W,rho/(mu-lam))
W=lam*(1/mu**2)/(2*(1-rho)); check("PK MD1",W,0.5*rho/(mu-lam))
# Stidham: nessun numero
# Dijkstra complessita: n+(n-1)+...+1 = n(n+1)/2
check("Dijkstra scansioni n=10",sum(range(1,11)),55)
print("FAIL" if fails else "Tutti i controlli superati.")
import sys; sys.exit(1 if fails else 0)
