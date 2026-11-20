#!/usr/bin/env python3
"""Verifica numeri del cap.3 (affidabilita' e protezione). Solo stdlib."""
from math import comb
import sys
fails = []
def check(name, got, want, tol=1e-9):
    ok = abs(got - want) <= tol * max(1.0, abs(want))
    print(("OK   " if ok else "FAIL ") + f"{name}: {got:.8g} (atteso {want:.8g})")
    if not ok: fails.append(name)

def base(Lkm, MTTR, rate):
    g = rate * Lkm / 1000; MTTF = 8760 / g; return g, MTTF, MTTF / (MTTF + MTTR), MTTR / MTTF
def U_MN(rho, N, M, NG=None):
    NN = N if NG is None else NG
    p = lambda n: comb(NN + M, n) * rho**n / (1 + rho)**(NN + M)
    return sum((n - M) / NN * p(n) for n in range(M + 1, NN + M + 1))

# tema: (L, MTTR, rate)  -> tabella
temi = {"2005-06-01": (500, 12, 5), "2005-06-29": (800, 12, 5), "2006-05-31": (750, 18, 5),
        "2006-06-27": (1600, 12, 5), "2007-06-12": (1500, 18, 4), "2008-05-28": (800, 6, 5),
        "2010-06-15": (500, 24, 5), "2020-05-27": (750, 18, 4)}
print("tema g/anno MTTF A U U11 A11")
for k, (L, R, r) in temi.items():
    g, MTTF, A, rho = base(L, R, r); U11 = U_MN(rho, 1, 1)
    check(k + " U11 = (1-A)^2", U11, (1 - A)**2, 1e-9)
    check(k + " U11 = rho^2/(1+rho)^2", U11, (rho / (1 + rho))**2, 1e-9)
    print(f"  {k} g={g:.4g} MTTF={MTTF:.6g} A={A:.7f} U={1-A:.4e} U11={U11:.4e} A11={1-U11:.8f} rho={rho:.6g}")
# valori attesi dalle soluzioni
atteso = {"2005-06-01": (3504, 0.9966, 1.1648e-5), "2005-06-29": (2190, 0.99455, 2.9698e-5),
          "2006-05-31": (2336, 0.99235, 5.847e-5), "2006-06-27": (1095, 0.98916, 1.175e-4),
          "2007-06-12": (1460, 0.98782, 1.48e-4), "2008-05-28": (2190, 0.99727, 7.465e-6),
          "2010-06-15": (3504, 0.9932, 4.628e-5), "2020-05-27": (2920, 0.99387, 3.75354e-5)}
for k, (mttf, A_, U_) in atteso.items():
    L, R, r = temi[k]; g, MTTF, A, rho = base(L, R, r)
    check(k + " MTTF", MTTF, mttf, 1e-3); check(k + " A", A, A_, 2e-4); check(k + " U11", U_MN(rho, 1, 1), U_, 2e-3)
# 1:2 (N=2,M=1)
for k, U12 in {"2005-06-29": 4.4466e-5, "2006-05-31": 8.748e-5}.items():
    L, R, r = temi[k]; g, MTTF, A, rho = base(L, R, r)
    p2 = 3 * rho**2 / (1 + rho)**3; p3 = rho**3 / (1 + rho)**3
    check(k + " U12 formula", 0.5 * p2 + p3, U_MN(rho, 2, 1), 1e-12); check(k + " U12", U_MN(rho, 2, 1), U12, 2e-3)
# priorita' 2006-05-31
L, R, r = temi["2006-05-31"]; g, MTTF, A, rho = base(L, R, r)
Ug = U_MN(rho, 1, 1); U = U_MN(rho, 2, 1); Us = (U * 2 - Ug * 1) / 1
check("2006-05-31 Ug", Ug, 5.847e-5, 2e-3); check("2006-05-31 Us", Us, 1.1649e-4, 2e-3)
check("2006-05-31 As", 1 - Us, 0.99988, 1e-5)
check("2006-05-31 N U = NG UG + NS US", 2 * U, Ug + Us, 1e-12)
# 2:1 = N=1,M=2 e (1-A)^3
for k, Uw in {"2006-06-27": 1.27e-6, "2007-06-12": 1.81e-6}.items():
    L, R, r = temi[k]; g, MTTF, A, rho = base(L, R, r)
    check(k + " U21 = (1-A)^3", U_MN(rho, 1, 2), (1 - A)**3, 1e-9); check(k + " U21 val", (1 - A)**3, Uw, 5e-2)
L, R, r = temi["2006-06-27"]; g, MTTF, A, rho = base(L, R, r)
check("2006-06-27 A21", 1 - (1 - A)**3, 0.9999987, 1e-6); check("2006-06-27 1:1 >1e-4", float(U_MN(rho, 1, 1) > 1e-4), 1.0)
L, R, r = temi["2007-06-12"]; g, MTTF, A, rho = base(L, R, r)
check("2007-06-12 1:1 >1e-4", float(U_MN(rho, 1, 1) > 1e-4), 1.0); check("2007-06-12 2:1 <1e-4", float(U_MN(rho, 1, 2) < 1e-4), 1.0)
# 2020
L, R, r = temi["2020-05-27"]; g, MTTF, A, rho = base(L, R, r)
check("2020 g", g, 3.0); check("2020 rho", rho, 0.006164383, 1e-6); check("2020 A11", 1 - U_MN(rho, 1, 1), 0.99996246, 1e-7)
# classi SLA
def classe(U): return "Premium" if U < 1e-5 else "Gold" if U < 1e-4 else "Silver" if U < 1e-3 else "Bronze" if U < 1e-2 else "-"
L, R, r = temi["2005-06-01"]; g, MTTF, A, rho = base(L, R, r)
print("  2005-06-01:", classe(1 - A), "->", classe(U_MN(rho, 1, 1)))
assert classe(1 - A) == "Bronze" and classe(U_MN(rho, 1, 1)) == "Gold"
L, R, r = temi["2008-05-28"]; g, MTTF, A, rho = base(L, R, r)
print("  2008:", classe(1 - A), "->", classe(U_MN(rho, 1, 1)))
assert classe(1 - A) == "Bronze" and classe(U_MN(rho, 1, 1)) == "Premium"
# 1:3 binomiale: normalizzazione
rho = 0.01
check("binomiale somma=1", sum(comb(4, n) * rho**n / (1 + rho)**4 for n in range(5)), 1.0, 1e-12)
print(); print("FALLITI:", fails) if fails else print("cap3: tutti i controlli superati.")
sys.exit(1 if fails else 0)
