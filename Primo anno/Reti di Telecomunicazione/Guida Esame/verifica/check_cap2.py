#!/usr/bin/env python3
"""Verifica i numeri del cap. 2 (reti, grado di servizio, potenza)."""
from math import sqrt
import sys
bad = []
def chk(name, got, want, tol=1e-6):
    ok = abs(got - want) <= tol * max(1.0, abs(want))
    print(("OK   " if ok else "FAIL ") + f"{name}: {got:.8g} (atteso {want:.8g})")
    if not ok: bad.append(name)

def n_sum(links): return sum(l / (m - l) for l, m in links)
def Tstar(links, g): return n_sum(links) / g

# 2005-06-01: unita' kbit/s (pacchetti da 1 kbit)
base = [(32, 64), (32, 48), (32, 64), (36, 48), (36, 64)]  # AB AC BC BD CD
chk("2005-06-01 sum n", n_sum(base), 8.285714286)
chk("2005-06-01 T", Tstar(base, 168), 0.049320, 1e-4)
re = [(32, 64), (32, 48), (36, 64), (32, 48), (40, 64)]
chk("2005-06-01 sum n'", n_sum(re), 7.952381, 1e-6)
chk("2005-06-01 T'", Tstar(re, 168), 0.047336, 1e-4)
chk("2005-06-01 riduzione %", 100 * (1 - Tstar(re, 168) / Tstar(base, 168)), 4.02, 5e-3)
chk("scala L=800 bit", Tstar(base, 168) * 0.8, 0.039456, 1e-4)

# 2005-06-14 potenza e 2 link
chk("potenza lambda*", max(range(1, 1000), key=lambda i: (i/1000) * (1 - i/1000)) / 1000, 0.5, 1e-3)
def split(V1, V2, G):
    k = sqrt(V1 / V2); X = (V1 - k * (V2 - G)) / (1 + k)
    T = (X / (V1 - X) + (G - X) / (V2 - G + X)) / G
    return X, T
X, T = split(60, 80, 40)
chk("2005-06-14 X*", X, 13.5898, 1e-5); chk("2005-06-14 T", T, 0.019642, 1e-4)
chk("2005-06-14 quadratica", X**2 - 720 * X + 9600, 0.0, 1e-6)
chk("2005-06-14 non split L2", 1 / (80 - 40), 0.025)
chk("2005-06-14 non split L1", 1 / (60 - 40), 0.05)
# derivata nulla
d = lambda x: 60 / (60 - x)**2 - 80 / (40 + x)**2
chk("2005-06-14 dT/dX=0", d(X), 0.0, 1e-9)

# 2006-06-13 (pkt/s, 800 bit)
L = [(60, 160), (20, 30), (60, 80), (40, 60), (60, 90)]  # AB AC BC BD CD
chk("2006-06-13 sum n", n_sum(L), 9.6); chk("2006-06-13 T", Tstar(L, 200), 0.048)
chk("2006-06-13 eta_max", min(m / l for l, m in L), 4 / 3)
# stesso risultato lavorando in kbit/s (L=0.8 kbit)
Lk = [(48, 128), (16, 24), (48, 64), (32, 48), (48, 72)]
chk("2006-06-13 in kbit/s", Tstar(Lk, 160) * 0.8, 0.048)

# 2007-06-12 (1200 bit)
L = [(30, 100), (40, 50), (50, 60), (60, 80), (20, 30)]  # AB AC CB BD CD
chk("2007-06-12 sum n", n_sum(L), 14.428571); chk("2007-06-12 T", Tstar(L, 150), 0.096190, 1e-4)
d1 = [(30, 100), (40, 50), (50, 60), (60, 80), (25, 30)]
chk("2007-06-12 diretto", Tstar(d1, 155), 0.112438, 1e-4)
d2 = [(30, 100), (40, 50), (55, 60), (65, 80), (20, 30)]
chk("2007-06-12 CBD", Tstar(d2, 155), 0.140415, 1e-4)

# 2009 (1200 bit)
L = [(30, 40), (40, 60), (30, 50), (60, 80)]  # AB AC CB BD (CD non usato)
chk("2009 sum n", n_sum(L), 9.5); chk("2009 T", Tstar(L, 110), 0.086364, 1e-5)
chk("2009 eta_max", min(m / l for l, m in L), 4 / 3)
chk("2009 T(eta->0)", sum(l / m for l, m in L) / 110, 0.025152, 1e-4)

# 2025
X, T = split(80, 100, 100)
chk("2025 X*", X, 42.2292, 1e-5); chk("2025 T", T, 0.0248613, 1e-4)
chk("2025 non split", (40 / 40 + 60 / 40) / 100, 0.025)
chk("2025 scambio f1/f2", (60 / 20 + 40 / 60) / 100, 0.036667, 1e-5)
chk("2025 stazionarieta'", 80 / (80 - X)**2 - 100 / X**2, 0.0, 1e-9)

# slide 16-18 (6 nodi): tabella a UNA direzione
tab = [(14, 25), (12, 25), (6, 12.5), (11, 25), (13, 62.5), (8, 12.5), (10, 25), (8, 25)]
chk("slide sum lambda (1 dir)", sum(l for l, _ in tab), 82); chk("slide sum lambda (2 dir)", 2 * sum(l for l, _ in tab), 164)
chk("slide hop medi 164/124", 164 / 124, 1.3226, 1e-3)
chk("slide T* (2 dir)", 2 * n_sum(tab) / 124, 0.1143, 5e-3)
chk("slide T* (1 sola dir, SBAGLIATO)", n_sum(tab) / 124, 0.0571, 5e-3)
chk("slide T0", 2 * sum(l / m for l, m in tab) / 124, 0.0569, 5e-3)
chk("slide eta_sat", min(m / l for l, m in tab), 1.5625)
chk("conversione hop", 164 / 124, 1.3226, 1e-3)

print("FALLITI:" if bad else "Tutti i controlli cap2 superati.", bad or "")
sys.exit(1 if bad else 0)
