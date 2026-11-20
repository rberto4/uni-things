#!/usr/bin/env python3
"""Verifica numeri del cap.7 (controllo di flusso). Solo stdlib."""
from math import exp, factorial, sqrt
import sys
fails = []
def check(name, got, want, tol=1e-9):
    ok = abs(got - want) <= tol * max(1.0, abs(want))
    print(("OK   " if ok else "FAIL ") + f"{name}: {got:.8g} (atteso {want:.8g})")
    if not ok: fails.append(name)

def embedded(lam, r, K=120):
    """Catena embedded agli istanti di token: i' = max(0, i+k-1), k~Poisson(lam/r)."""
    x = lam / r; a = [exp(-x) * x**k / factorial(k) for k in range(K + 3)]
    P = [[0.0] * K for _ in range(K)]
    for i in range(K):
        for k in range(len(a)):
            j = max(0, i + k - 1); j = min(j, K - 1); P[i][j] += a[k]
    p = [1.0 / K] * K
    for _ in range(4000):
        q = [0.0] * K
        for i in range(K):
            pi = p[i]
            if pi:
                row = P[i]
                for j in range(max(0, i - 1), min(K, i + 25)): q[j] += pi * row[j]
        s = sum(q); p = [v / s for v in q]
    return a, p

lam, r = 0.5, 1.0   # esempio: lambda/r = 1/2
a, p = embedded(lam, r)
check("a0", a[0], exp(-0.5)); check("a1", a[1], 0.5 * exp(-0.5))
check("p0 = (r-lam)/(r a0)", p[0], (r - lam) / (r * a[0]), 1e-8)
check("p1 = (1-a0-a1)/a0 p0", p[1], (1 - a[0] - a[1]) / a[0] * p[0], 1e-8)
check("p2 = p0/a0 (...) [sulle slide appare 1/a2: refuso]", p[2], p[0] / a[0] * ((1 - a[0] - a[1]) * (1 - a[1]) / a[0] - a[2]), 1e-8)
# ricorsione generale: p_{i+1} = [p_i (1-a1) - sum_{j<i} a_{i-j+1} p_j] / a0
q = [p[0]]
for i in range(0, 8):
    s_ = sum(a[i - j + 1] * q[j] for j in range(0, i))
    q.append(((1 - a[1]) * q[i] - s_) / a[0] if i > 0 else (1 - a[0] - a[1]) / a[0] * q[0])
check("ricorsione p5", q[5], p[5], 1e-6)
check("equil. p0=(a0+a1)p0+a0 p1", p[0], (a[0] + a[1]) * p[0] + a[0] * p[1], 1e-8)
print("  p0..p5 =", [round(v, 5) for v in p[:6]])
for W in (1, 2):
    T = sum((j - W) * p[j] for j in range(W + 1, len(p))) / r
    print(f"  W={W}: T(slide)={T:.5f} s;  P(nessun token disponibile)={sum(p[j] for j in range(W, len(p))):.5f}")
W = 2; T2 = sum((j - W) * p[j] for j in range(W + 1, len(p))) / r
# token perso solo in stato 0 senza arrivi
check("lam = r(1 - p0 a0)", lam, r * (1 - p[0] * a[0]), 1e-8)

# finestra
c = 64e3; L = 1000.0
ceff = lambda W, RTT: min(c, W * L / RTT)
check("ceff W=1 RTT=0.1", ceff(1, 0.1), 10e3); check("ceff W=5 RTT=0.2", ceff(5, 0.2), 25e3)
check("BDP c*RTT (RTT=0.2) in pkt", c * 0.2 / L, 12.8); check("ceff W=13 RTT=0.2 = c", ceff(13, 0.2), c)
check("ceff W=20 RTT=0.1", ceff(20, 0.1), c)

# CQL: coerenza di b_M
B, N = 100, 4
check("b_M slide sqrt(B/N)=5 < B/N=25", float(sqrt(B / N) < B / N), 1.0)
check("b_M = B/sqrt(N)=50 > B/N", float(B / sqrt(N) > B / N), 1.0)
check("partizione completa C=B/N", B / N, 25.0)
print(); print("FALLITI:", fails) if fails else print("cap7: tutti i controlli superati.")
sys.exit(1 if fails else 0)
