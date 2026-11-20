#!/usr/bin/env python3
"""Verifica i numeri del cap. 6 (ARQ, lunghezza ottima del pacchetto)."""
from math import sqrt, ceil
import sys
bad = []
def chk(name, got, want, tol=1e-6):
    ok = abs(got - want) <= tol * max(1.0, abs(want))
    print(("OK   " if ok else "FAIL ") + f"{name}: {got:.8g} (atteso {want:.8g})")
    if not ok: bad.append(name)

# ARQ: serie geometrica e rho_max
p = 0.1; a = 5.0
tv_sw = sum((i + 1) * (1 - p) * p**i for i in range(2000)) / 1  # E[#tentativi]
chk("S&W E[tent]=1/(1-p)", tv_sw, 1 / (1 - p), 1e-9)
chk("S&W rho", (1 - p) / a, 0.18)
chk("GBN rho", (1 - p) / (1 + (a - 1) * p), 0.642857, 1e-5)
chk("GBN a=1 -> S&W", (1 - p) / (1 + 0 * p), 1 - p)
chk("SR rho", 1 - p, 0.9)
# GBN: tv = tI + tT p/(1-p) con tT = a tI
chk("GBN tv/tI", 1 + a * p / (1 - p), (1 + (a - 1) * p) / (1 - p), 1e-12)

# pipelining
def Tapp(X, L, H, C, h): return ((h - 1) * (X + H) + L + (L / X + .5) * H) / C
def Tex(X, L, H, C, h): return ((h - 1) * (X + H) + L + ceil(L / X) * H) / C
def Xopt(L, H, h): return sqrt(L * H / (h - 1))
def Tmin_closed(L, H, C, h): return ((h - 1) * H + L + H / 2 + 2 * sqrt((h - 1) * L * H)) / C

L, H, C, h = 10000, 100, 100e3, 3   # 2006-06-13
X = Xopt(L, H, h)
chk("2006 X*", X, 707.1068, 1e-6); chk("2006 T approx", Tapp(X, L, H, C, h), 0.130783, 1e-5)
chk("2006 T closed", Tmin_closed(L, H, C, h), Tapp(X, L, H, C, h), 1e-9)
chk("2006 T ceil @707", Tex(707, L, H, C, h), 0.13114, 1e-4)
best = min(range(50, L + 1), key=lambda x: Tex(x, L, H, C, h))
print("   2006 minimo esatto: X=%d T=%.6f" % (best, Tex(best, L, H, C, h)))
L, H, C, h = 20000, 400, 2e6, 2     # 2007-05-31
X = Xopt(L, H, h)
chk("2007 X*", X, 2828.4271, 1e-6); chk("2007 T approx", Tapp(X, L, H, C, h), 0.0131285, 1e-4)
chk("2007 T closed", Tmin_closed(L, H, C, h), Tapp(X, L, H, C, h), 1e-9)
chk("2007 T ceil@2828 (=valore prof)", Tex(2828, L, H, C, h), 0.013214, 1e-4)
chk("2007 ceil(L/X)", ceil(L / 2828), 8)
best = min(range(50, L + 1), key=lambda x: Tex(x, L, H, C, h))
chk("2007 minimo esatto T", Tex(best, L, H, C, h), 0.01303, 5e-3)
print("   2007 minimo esatto: X=%d" % best)
# punti per il grafico (h=3, 2006)
for x in (300, 707, 2000, 5000):
    print("   graf x=%d T=%.4f" % (x, Tapp(x, 10000, 100, 100e3, 3)))
print("FALLITI:" if bad else "Tutti i controlli cap6 superati.", bad or "")
sys.exit(1 if bad else 0)
