#!/usr/bin/env python3
"""Ricalcola tutti i risultati numerici citati nella guida (solo stdlib)."""
from fractions import Fraction as F
from math import comb, sqrt, ceil, log, exp
import sys

fails = []
def check(name, got, want, tol=1e-9):
    g = float(got); w = float(want)
    ok = abs(g - w) <= tol * max(1.0, abs(w))
    print(("OK   " if ok else "FAIL ") + f"{name}: {g:.10g} (atteso {w:.10g})")
    if not ok: fails.append(name)

def ctmc(states, rates):
    """rates: {(i,j): r}. Distribuzione stazionaria esatta (Fraction)."""
    n = len(states); idx = {s: k for k, s in enumerate(states)}
    A = [[F(0)] * n for _ in range(n)]
    for (i, j), r in rates.items():
        A[idx[j]][idx[i]] += F(r); A[idx[i]][idx[i]] -= F(r)
    A[-1] = [F(1)] * n
    b = [F(0)] * (n - 1) + [F(1)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]; b[c], b[p] = b[p], b[c]
        d = A[c][c]; A[c] = [x / d for x in A[c]]; b[c] /= d
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]; b[r] -= f * b[c]
    return {s: b[idx[s]] for s in states}

def bd(lams, mus):
    st = list(range(len(lams) + 1))
    r = {}
    for k, l in enumerate(lams): r[(k, k + 1)] = l
    for k, m in enumerate(mus): r[(k + 1, k)] = m
    return ctmc(st, r)

print("== Code e catene ==")
# 2020 Es1: M/M/1/3 rho=1 (lam=mu=1)
p = bd([1, 1, 1], [1, 1, 1]); N = sum(k * v for k, v in p.items()); la = 1 - p[3]
check("2020 p3", p[3], F(1, 4)); check("2020 N", N, F(3, 2)); check("2020 T*lam", N / la, 2)
check("2020 Nq", p[2] + 2 * p[3], F(3, 4)); check("2020 W*mu", (p[2] + 2 * p[3]) / la, 1)
check("2020 util", 1 - p[0], la)
# 2025 token bucket lam=1, mu=1/2
p = bd([1, 1, 1], [F(1, 2)] * 3)
check("2025 p0", p[0], F(1, 15)); check("2025 p3", p[3], F(8, 15))
thr = 1 * p[0] + F(1, 2) * p[2] + F(1, 2) * p[3]
check("2025 throughput", thr, F(7, 15)); N = p[2] + 2 * p[3]
check("2025 N", N, F(4, 3)); check("2025 T", N / thr, F(20, 7)); check("2025 thr=lam(1-p3)", thr, 1 - p[3])
# 2005-11-07 token bucket lam=mu
p = bd([1, 1, 1], [1, 1, 1]); thr = p[0] + p[2] + p[3]
check("TB2005 thr", thr, F(3, 4)); check("TB2005 T", (p[2] + 2 * p[3]) / thr, 1)
# 2005-06-01 vacation, lam=mu=1. stati 0,1V,1L,2,3
S = ['0', '1V', '1L', '2', '3']
r = {('0', '1V'): 1, ('1V', '2'): 1, ('1L', '0'): 1, ('1L', '2'): 1, ('2', '1L'): 1, ('2', '3'): 1, ('3', '2'): 1}
p = ctmc(S, r)
check("vac p0", p['0'], F(1, 7)); check("vac p3", p['3'], F(2, 7))
N = p['1V'] + p['1L'] + 2 * p['2'] + 3 * p['3']; check("vac N", N, F(12, 7))
la = 1 - p['3']; check("vac util", 1 - p['0'] - p['1V'], la)
# 2005-06-29 scarto q_n=n/3  rho=1 numerico (forma letterale)
rho = F(1)
p0 = 1 / (1 + rho + F(2, 3) * rho**2 + F(2, 9) * rho**3)
p = bd([1, F(2, 3), F(1, 3)], [1, 1, 1])
check("scarto p0", p[0], p0); check("scarto p3", p[3], F(2, 9) * p0)
# 2006-05-31 M/M/2/2 rho=1/2 (lam=1, mu=2)
p = bd([1, 1], [2, 4]); check("MM22 p0", p[0], F(8, 13)); check("MM22 p2", p[2], F(1, 13))
check("MM22 N", p[1] + 2 * p[2], F(6, 13)); la = 1 - p[2]
check("MM22 T*mu", (p[1] + 2 * p[2]) / la * 2, 1)
# 2006-06-13 E2/1/1 lam=mu=1 : stati 0,11,12
p = ctmc(['0', '11', '12'], {('0', '11'): 1, ('11', '12'): 2, ('12', '0'): 2})
check("E2 p0", p['0'], F(1, 2)); check("E2 p11", p['11'], F(1, 4))
check("E2 PB=rho/(1+rho)", 1 - p['0'], F(1, 2))
# 2006-06-27 M/M/1/2 rho_max per Pb<=0.2 e rho=1/3
rm = (0.2 + sqrt(0.04 + 4 * 0.8 * 0.2)) / (2 * 0.8); check("MM12 rho_max", rm, 0.6404, 1e-3)
p = bd([1, 1], [3, 3]); check("MM12 Pb(1/3)", p[2], F(1, 13)); check("MM12 N", p[1] + 2 * p[2], F(5, 13))
# 2007-05-31 scoraggiati M/M/2/2 rho=1/2 (lam=1,mu=2)
p = bd([1, F(1, 2)], [2, 4]); check("disc p0", p[0], F(16, 25)); check("disc p2", p[2], F(1, 25))
check("disc N", p[1] + 2 * p[2], F(2, 5))
rm = (0.3 + sqrt(0.09 + 4 * 0.175 * 0.3)) / (2 * 0.175); check("disc rho_max", rm, 2.4221, 1e-3)
# 2007-06-12 E3/1/1 lam = mu/2 (mu=1)
p = ctmc(['0', 'a', 'b', 'c'], {('0', 'a'): F(1, 2), ('a', 'b'): 3, ('b', 'c'): 3, ('c', '0'): 3})
check("E3 p0", p['0'], F(2, 3)); check("E3 N", 1 - p['0'], F(1, 3))
# 2008 eterogenei mu1=2, mu2=1, lam=1: stati 0,A(S1),B(S2),2
p = ctmc(['0', 'A', 'B', '2'], {('0', 'A'): 1, ('A', '0'): 2, ('B', '0'): 1, ('A', '2'): 1, ('B', '2'): 1, ('2', 'A'): 1, ('2', 'B'): 2})
check("het p0", p['0'], F(5, 9)); check("het pA", p['A'], F(2, 9)); check("het pB", p['B'], F(1, 9)); check("het p2", p['2'], F(1, 9))
N = p['A'] + p['B'] + 2 * p['2']; check("het N", N, F(5, 9)); check("het T", N / (1 - p['2']), F(5, 8))
# 2009 M/M/3/3 rho=1
p = bd([1, 1, 1], [1, 2, 3]); check("MM33 p0", p[0], F(3, 8)); check("MM33 p3", p[3], F(1, 16))
check("MM33 N", sum(k * v for k, v in p.items()), F(15, 16))
# 2010 M/M/2/3 rho=1
p = bd([1, 1, 1], [1, 2, 2]); check("MM23 p0", p[0], F(4, 11)); check("MM23 p3", p[3], F(1, 11))
N = sum(k * v for k, v in p.items()); la = 1 - p[3]
check("MM23 N", N, 1); check("MM23 T", N / la, F(11, 10)); check("MM23 W", N / la - 1, F(1, 10))
check("MM23 W via Nq", p[3] / la, F(1, 10))
# E2|M|1|0 (arrivi Erlang-2, servizio exp mu), lam=mu=1 ; a=2*lam
st = ['01', '02', '11', '12']
a = 2
p = ctmc(st, {('01', '02'): a, ('02', '11'): a, ('11', '12'): a, ('12', '11'): a, ('11', '01'): 1, ('12', '02'): 1})
check("E2M10 p01", p['01'], F(1, 6)); check("E2M10 p02", p['02'], F(5, 18)); check("E2M10 p11", p['11'], F(1, 3)); check("E2M10 p12", p['12'], F(2, 9))
PB = p['12'] / (p['02'] + p['12']); check("E2M10 PB", PB, F(4, 9))
check("E2M10 PB formula", (F(a) / (a + 1))**2, F(4, 9))
check("E2M10 thr", 1 * (1 - PB), 1 * (p['11'] + p['12']))
# M/G/1/1 insensibilita: Pb = rho/(1+rho)
check("E3 insens", F(1, 2) / (1 + F(1, 2)), F(1, 3))

print("== Reti / grado di servizio ==")
def Tstar(links, gamma):
    return sum(l / (m - l) for l, m in links) / gamma
# 2005-06-01 (kbit/s, 'pacchetti da 1 kbit')
L = [(32, 64), (32, 48), (32, 64), (36, 48), (36, 64)]
L = [(32, 64), (32, 48), (32, 64), (36, 48), (36, 64)]  # AB AC BC BD CD
check("2005-06-01 T", Tstar([(32, 64), (32, 48), (32, 64), (36, 48), (36, 64)], 168), 0.0493, 2e-3)
check("2005-06-01 T'", Tstar([(32, 64), (32, 48), (36, 64), (32, 48), (40, 64)], 168), 0.04734, 2e-3)
# 2006-06-13  pkt/s: AB60/160 AC20/30 BC60/80 BD40/60 CD60/90, gamma=200
check("2006-06-13 T", Tstar([(60, 160), (20, 30), (60, 80), (40, 60), (60, 90)], 200), 0.048, 1e-6)
check("2006-06-13 eta_max", min(160/60, 30/20, 80/60, 60/40, 90/60), 4/3)
# 2007-06-12
check("2007-06-12 T", Tstar([(30, 100), (40, 50), (50, 60), (60, 80), (20, 30)], 150), 0.0962, 2e-3)
check("2007-06-12 diretto", Tstar([(30, 100), (40, 50), (50, 60), (60, 80), (25, 30)], 155), 0.1124, 2e-3)
check("2007-06-12 via CBD", Tstar([(30, 100), (40, 50), (55, 60), (65, 80), (20, 30)], 155), 0.1404, 2e-3)
# 2009
check("2009 T", Tstar([(30, 40), (40, 60), (30, 50), (60, 80)], 110), 0.0864, 1e-3)
check("2009 eta_max", min(40/30, 60/40, 50/30, 80/60), 4/3)
check("2009 T(eta->0)", sum(l / m for l, m in [(30, 40), (40, 60), (30, 50), (60, 80)]) / 110, 0.0251515151, 1e-6)
# 2 link paralleli
def split(V1, V2, G):
    k = sqrt(V1 / V2); X = (V1 - k * (V2 - G)) / (1 + k)
    T = (X / (V1 - X) + (G - X) / (V2 - G + X)) / G
    return X, T
X, T = split(60, 80, 40); check("2005-06-14 X*", X, 13.5898, 1e-4); check("2005-06-14 T", T, 0.01964, 1e-3)
X, T = split(80, 100, 100); check("2025 X*", X, 42.229, 1e-4); check("2025 T", T, 0.024861, 1e-4)
check("2025 non split", (40 / 40 + 60 / 40) / 100, 0.025)
# potenza
check("potenza max", max(l * (1 - l) for l in [i / 1000 for i in range(1000)]), 0.25)

print("== Affidabilita ==")
def prot(Lkm, MTTR, rate=5.0, N=1, M=1):
    g = rate * Lkm / 1000; MTTF = 8760 / g; A = MTTF / (MTTF + MTTR); rho = MTTR / MTTF
    pn = lambda n: comb(N + M, n) * rho**n / (1 + rho)**(N + M)
    U = sum((n - M) / N * pn(n) for n in range(M + 1, N + M + 1))
    return MTTF, A, U
for nm, (Lk, R, rate, N, M, Aw, Uw) in {
    "2005-06-01 1:1": (500, 12, 5, 1, 1, 3504, 1.1648e-5),
    "2005-06-29 1:1": (800, 12, 5, 1, 1, 2190, 2.9698e-5),
    "2005-06-29 1:2": (800, 12, 5, 2, 1, 2190, 4.4466e-5),
    "2006-05-31 1:1": (750, 18, 5, 1, 1, 2336, 5.847e-5),
    "2006-05-31 1:2": (750, 18, 5, 2, 1, 2336, 8.748e-5),
    "2008 1:1": (800, 6, 5, 1, 1, 2190, 7.465e-6),
    "2010 1:1": (500, 24, 5, 1, 1, 3504, 4.628e-5),
    "2020 1:1": (750, 18, 4, 1, 1, 2920, 3.75354e-5),
}.items():
    MTTF, A, U = prot(Lk, R, rate, N, M)
    check(nm + " MTTF", MTTF, Aw, 1e-3); check(nm + " U", U, Uw, 2e-3)
MTTF, A, U = prot(750, 18, 4); check("2020 A", A, 0.99387, 1e-5)
MTTF, A, U1 = prot(750, 18, 4); check("2020 U=(1-A)^2", (1 - A)**2, U1, 1e-3)
MTTF, A, _ = prot(750, 18, 5); N, Ng, Ns = 2, 1, 1
_, _, Ug = prot(750, 18, 5, 1, 1); _, _, U12 = prot(750, 18, 5, 2, 1)
check("2006-05-31 Us", (U12 * N - Ug * Ng) / Ns, 1.1649e-4, 2e-3)
_, A, _ = prot(1600, 12, 5); check("2006-06-27 A", A, 0.98916, 1e-4); check("2006-06-27 U 1:1", (1 - A)**2, 1.175e-4, 2e-3); check("2006-06-27 2:1", 1 - (1 - A)**3, 0.9999987, 1e-6)
_, A, _ = prot(1500, 18, 4); check("2007-06-12 A", A, 0.98782, 1e-4); check("2007-06-12 1:1 U", (1 - A)**2, 1.48e-4, 1e-2); check("2007-06-12 2:1 U", (1 - A)**3, 1.81e-6, 1e-2)

print("== Pacchetto ottimo ==")
def Topt(Lb, H, C, h):
    X = sqrt(Lb * H / (h - 1)); T = ((h - 1) * (X + H) + Lb + (Lb / X + .5) * H) / C
    return X, T
X, T = Topt(10000, 100, 100e3, 3); check("2006-06-13 X*", X, 707.1, 1e-3); check("2006-06-13 T", T, 0.1308, 1e-3)
X, T = Topt(20000, 400, 2e6, 2); check("2007-05-31 X*", X, 2828.4, 1e-3); check("2007-05-31 T (approx)", T, 0.01313, 1e-3)
exact = min(((X + 400) + 20000 + ceil(20000 / X) * 400) / 2e6 for X in range(100, 20001))
check("2007-05-31 T esatto", exact, 0.01303, 2e-3)

print("== Generazione ==")
check("2025 2b F inversa", 1 / (2 - 0.5), 1 / 1.5)
check("2020 Y", -1 + sqrt(.25), -0.5)
check("sheet4 fine primo tratto", 24 * (19/48) - 9, 0.5)
check("sheet4 inizio secondo tratto", 24 * (19/48) - 8, 1.5)

print()
if fails:
    print("FALLITI:", fails); sys.exit(1)
print("Tutti i controlli superati.")
