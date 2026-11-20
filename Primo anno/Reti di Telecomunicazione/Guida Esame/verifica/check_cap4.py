#!/usr/bin/env python3
"""Verifica numerica dei generatori del cap. 4 (solo stdlib).
Metodo: griglia fine di U (punti medi) -> distribuzione empirica esatta a 1/N; confronto con la CDF teorica."""
from math import sqrt, log, exp, floor, ceil, factorial, cos, sin, pi, e
import random, sys

N = 400000
G = [(i + 0.5) / N for i in range(N)]
fails = []

def ok(name, cond, info=""):
    print(("OK   " if cond else "FAIL ") + name + (" " + info if info else ""))
    if not cond: fails.append(name)

def cdf_emp(gen, x):
    return sum(1 for u in G if gen(u) <= x) / N

def pmass(gen, v, tol=1e-12):
    return sum(1 for u in G if abs(gen(u) - v) < tol) / N

def check_cdf(name, gen, F, pts, tol=3e-5):
    err = max(abs(cdf_emp(gen, x) - F(x)) for x in pts)
    ok(name + " CDF", err < tol, f"(err max {err:.2e})")

def clip(x, a, b): return max(a, min(b, x))
def lin(x, a, b): return clip((x - a) / (b - a), 0, 1)

def range_ok(name, gen, lo, hi):
    xs = [gen(u) for u in G]
    ok(name + " supporto", min(xs) >= lo - 1e-12 and max(xs) <= hi + 1e-12, f"[{min(xs):.4f},{max(xs):.4f}]")

# ---- 2020 Es3
g = lambda u: -1 if u <= 0.25 else u + 0.75
check_cdf("2020 1b", g, lambda x: 0 if x < -1 else (0.25 if x < 1 else clip(0.25 + (x - 1), 0.25, 1)), [-1, 0, 1, 1.2, 1.5, 1.75])
ok("2020 1a P(X>=3/2)=1/4", abs(1 - cdf_emp(g, 1.5 - 1e-9) - 0.25) < 1e-4)
g = lambda u: 6 * u - 4 if u <= 1 / 3 else 6 * u
check_cdf("2020 2a", g, lambda x: (clip(x, -4, -2) + 4) / 6 + (clip(x, 2, 6) - 2) / 6 if x >= -4 else 0, [-4, -3, -2, 0, 2, 3, 5, 6])
g = lambda u: -1 + sqrt(u)
check_cdf("2020 2b", g, lambda x: (x + 1)**2 if -1 <= x <= 0 else (0 if x < -1 else 1), [-1, -0.7, -0.3, 0])
# ---- 2025 Es3
def g(u):
    if u <= .25: return 4 * u - 1
    if u <= .75: return 2 * u - .5
    return 4 * u - 2
F25 = lambda x: .25 * lin(x, -1, 0) + .5 * lin(x, 0, 1) + .25 * lin(x, 1, 2)
check_cdf("2025 1b", g, F25, [-1, -.5, 0, .3, 1, 1.5, 2])
ok("2025 1a P=3/8", abs(F25(.5) - F25(-.5) - 3 / 8) < 1e-12)
g = lambda u: 8 * u - 5 if u <= 1 / 8 else 8 * u - 4
check_cdf("2025 2a", g, lambda x: (lin(x, -5, -4) * 1 + lin(x, -3, 4) * 7) / 8, [-5, -4.5, -4, -3, 0, 4])
g = lambda u: 1 / (2 - u)
check_cdf("2025 2b", g, lambda x: 2 - 1 / x if .5 <= x <= 1 else (0 if x < .5 else 1), [.5, .6, .8, 1])
# ---- 2005-06-14
check_cdf("2005-06-14 -U", lambda u: -u, lambda x: lin(x, -1, 0), [-1, -.5, 0])
check_cdf("2005-06-14 -2+5U", lambda u: -2 + 5 * u, lambda x: lin(x, -2, 3), [-2, 0, 3])
check_cdf("2005-06-14 -lnU", lambda u: -log(u), lambda x: 1 - exp(-x) if x >= 0 else 0, [0, .5, 1, 3], tol=1e-4)
g = lambda u: 1 if u <= .2 else 2
ok("2005-06-14 discreta", abs(pmass(g, 1) - .2) < 1e-4)
# ---- 2005-06-29
g = lambda u: ceil(2 * u) + 3
ok("2005-06-29 ceil", abs(pmass(g, 4) - .5) < 1e-4 and abs(pmass(g, 5) - .5) < 1e-4)
g = lambda u: 10 * u - 5 if u <= .5 else 10 * u - 3
check_cdf("2005-06-29 2a", g, lambda x: (lin(x, -5, 0) * 5 + lin(x, 2, 7) * 5) / 10, [-5, -2, 0, 2, 5, 7])
g = lambda u: -1 / u
check_cdf("2005-06-29 2b", g, lambda x: -1 / x if x <= -1 else 0, [-1, -2, -10, -100], tol=1e-4)
# ---- 2006-05-31 es3
g = lambda u: -1 + sqrt(2 * u)
check_cdf("2006-05-31 a", g, lambda x: (x + 1)**2 / 2 if -1 <= x <= sqrt(2) - 1 else (0 if x < -1 else 1), [-1, -.5, 0, sqrt(2) - 1])
g = lambda u: 6 * u - 3 if u <= 2 / 3 else 6 * u - 2
check_cdf("2006-05-31 b", g, lambda x: (lin(x, -3, 1) * 4 + lin(x, 2, 4) * 2) / 6, [-3, 0, 1, 2, 3, 4])
# ---- 2006-06-27
g = lambda u: 1 if u <= .5 else (2 if u <= .75 else 3)
ok("2006-06-27 discreta", abs(pmass(g, 2) - .25) < 1e-4 and abs(pmass(g, 3) - .25) < 1e-4)
g = lambda u: -1 + (3 * u) ** (1 / 3)
check_cdf("2006-06-27 (x+1)^2", g, lambda x: (x + 1)**3 / 3 if -1 <= x <= 3 ** (1 / 3) - 1 else (0 if x < -1 else 1), [-1, -.5, 0, .4])
g = lambda u: 6 * u + 2 if u <= .5 else (3 if u <= .75 else 4)
ok("2006-06-27 mista", abs(pmass(g, 3) - .25) < 1e-4 and abs(pmass(g, 4) - .25) < 1e-4)
check_cdf("2006-06-27 mista", g, lambda x: .5 * lin(x, 2, 5) + (.25 if x >= 3 else 0) + (.25 if x >= 4 else 0), [2, 2.5, 3 - 1e-9, 3, 4 - 1e-9, 4, 5])
# ---- 2007-05-31
g = lambda u: 5 * u - 3 if u < .4 else 5 * u
check_cdf("2007-05-31 a", g, lambda x: (lin(x, -3, -1) * 2 + lin(x, 2, 5) * 3) / 5, [-3, -2, -1, 2, 3.5, 5])
g = lambda u: -1 + sqrt(1 + 2 * u)
check_cdf("2007-05-31 b", g, lambda x: x * x / 2 + x if 0 <= x <= sqrt(3) - 1 else (0 if x < 0 else 1), [0, .2, .5, sqrt(3) - 1])
g = lambda u: -2 if u < .5 else (12 * u - 5 if u < .75 else 6)
check_cdf("2007-05-31 c", g, lambda x: (.5 if x >= -2 else 0) + .25 * lin(x, 1, 4) + (.25 if x >= 6 else 0), [-2, 0, 1, 2.5, 4, 5.9, 6])
# ---- 2008
g = lambda u: 15 * u - 3 if u <= 1 / 3 else 15 * u
check_cdf("2008 a", g, lambda x: (lin(x, -3, 2) * 5 + lin(x, 5, 15) * 10) / 15, [-3, 0, 2, 5, 10, 15])
check_cdf("2008 b (1/(1-U))", lambda u: 1 / (1 - u), lambda x: 1 - 1 / x if x >= 1 else 0, [1, 1.5, 2, 5, 20], tol=1e-4)
g = lambda u: 4 * u + 1 if u <= .5 else (8 * u - 1 if u <= .75 else 7)
check_cdf("2008 c", g, lambda x: .5 * lin(x, 1, 3) + .25 * lin(x, 3, 5) + (.25 if x >= 7 else 0), [1, 2, 3, 4, 5, 6.9, 7])
# ---- 2009
g = lambda u: 4 * u if u <= .25 else 2
check_cdf("2009 1b", g, lambda x: .25 * lin(x, 0, 1) + (.75 if x >= 2 else 0), [0, .5, 1, 1.9, 2])
ok("2009 1a P(X>=.5)=7/8", abs(1 - cdf_emp(g, .5 - 1e-9) - 7 / 8) < 1e-4)
g = lambda u: 6 * u - 3 if u <= 1 / 6 else 6 * u - 1
check_cdf("2009 2a", g, lambda x: (lin(x, -3, -2) + lin(x, 0, 5) * 5) / 6, [-3, -2.5, -2, 0, 2.5, 5])
g = lambda u: exp(u / 2)
check_cdf("2009 2b", g, lambda x: 2 * log(x) if 1 <= x <= sqrt(e) else (0 if x < 1 else 1), [1, 1.2, 1.5, sqrt(e)])
# ---- 2010
g = lambda u: -2 if u <= .6 else 5 * u - 3
check_cdf("2010 1b", g, lambda x: (.6 if x >= -2 else 0) + .4 * lin(x, 0, 2), [-2, 0, .5, 1, 2])
ok("2010 1a P(X<=.5)=.7", abs(cdf_emp(g, .5) - .7) < 1e-4)
g = lambda u: 4 * u - 5 if u <= .25 else 4 * u + 1
check_cdf("2010 2a", g, lambda x: (lin(x, -5, -4) + lin(x, 2, 5) * 3) / 4, [-5, -4.5, -4, 2, 3.5, 5])
g = lambda u: -1 + 2 * sqrt(u)
check_cdf("2010 2b", g, lambda x: (x + 1)**2 / 4 if -1 <= x <= 1 else (0 if x < -1 else 1), [-1, -.5, 0, .5, 1])
# ---- fogli
check_cdf("foglio1 a", lambda u: -1 + 11 * u, lambda x: lin(x, -1, 10), [-1, 0, 5, 10])
g = lambda u: -3 + 4 * u if u < .5 else 4 * u - 1
check_cdf("foglio1 b", g, lambda x: (lin(x, -3, -1) + lin(x, 1, 3)) / 2, [-3, -2, -1, 1, 2, 3])
g = lambda u: (3 * u) ** (1 / 3)
check_cdf("foglio1 c", g, lambda x: x**3 / 3 if 0 <= x <= 3 ** (1 / 3) else (0 if x < 0 else 1), [0, .5, 1, 3 ** (1 / 3)])
lam = 2.0
def laplace(u):  # versione a una sola U
    return lam * log(2 * u) if u < .5 else -lam * log(2 * (1 - u))
FL = lambda x: .5 * exp(x / lam) if x < 0 else 1 - .5 * exp(-x / lam)
check_cdf("foglio1 d Laplace", laplace, FL, [-6, -2, -.5, 0, .5, 2, 6], tol=1e-4)
# geometrica
p = 1 / 8
gk = lambda u: floor(log(u) / log(1 - p)) + 1
pm = [pmass(gk, k) for k in range(1, 8)]
ok("foglio2 geometrica da 1", all(abs(pm[k - 1] - p * (1 - p)**(k - 1)) < 2e-4 for k in range(1, 8)))
mean1 = sum(gk(u) for u in G) / N
ok("foglio2 media 8 (da 1)", abs(mean1 - 8) < .05, f"({mean1:.3f})")
mean0 = sum(floor(log(u) / log(1 - p)) for u in G) / N
ok("foglio2 floor senza +1 ha media 7", abs(mean0 - 7) < .05, f"({mean0:.3f})")
lam = 3.0; a = 5.0
g = lambda u: -lam * log(1 - u * (1 - exp(-a / lam)))
check_cdf("foglio2 esp. troncata", g, lambda x: (1 - exp(-x / lam)) / (1 - exp(-a / lam)) if 0 <= x <= a else (0 if x < 0 else 1), [0, 1, 2.5, 5], tol=1e-4)
# foglio 3: da Y~U[-1,1]
check_cdf("foglio3 a", lambda u: 5 * u - 2, lambda x: lin(x, -2, 3), [-2, 0, 3])
g = lambda u: 2 * u if u < .5 else 2 * u + 1
check_cdf("foglio3 b", g, lambda x: (lin(x, 0, 1) + lin(x, 2, 3)) / 2, [0, .5, 1, 2, 2.5, 3])
check_cdf("foglio3 c", lambda u: u ** .25, lambda x: x**4 if 0 <= x <= 1 else (0 if x < 0 else 1), [0, .5, .9, 1])
check_cdf("foglio3 d", lambda u: -5 * log(u), lambda x: 1 - exp(-x / 5) if x >= 0 else 0, [0, 2, 5, 15], tol=1e-4)
ok("foglio3 U=(Y+1)/2", all(abs((y + 1) / 2 - u) < 1e-12 for u, y in [(0.3, -0.4), (0.9, 0.8)]))
# foglio 4
def f4(u):
    if u <= 1 / 12: return 24 * u - 5
    if u <= 3 / 12: return -3
    if u <= 19 / 48: return 24 * u - 9
    if u <= .5: return 24 * u - 8
    return 5
def F4(x):
    r = 0.0
    r += (lin(x, -5, .5) * 5.5 + lin(x, 1.5, 4) * 2.5) / 24
    r += (1 / 6 if x >= -3 else 0) + (.5 if x >= 5 else 0)
    return r
ok("foglio4 masse", abs(1 / 6 + .5 + 1 / 3 - 1) < 1e-12 and abs((5.5 + 2.5) / 24 - 1 / 3) < 1e-12)
check_cdf("foglio4", f4, F4, [-5, -4, -3 - 1e-9, -3, -1, .5, 1, 1.5, 3, 4, 5 - 1e-9, 5])
ok("foglio4 estremi", abs(24 * (1 / 12) - 5 + 3) < 1e-12 and abs(24 * .25 - 9 + 3) < 1e-12 and abs(24 * 19 / 48 - 9 - .5) < 1e-12 and abs(24 * 19 / 48 - 8 - 1.5) < 1e-12 and abs(24 * .5 - 8 - 4) < 1e-12)
ok("foglio4 massa plateau", abs(pmass(f4, 5) - .5) < 1e-4 and abs(pmass(f4, -3) - 1 / 6) < 1e-4)

# ---- Poisson sequenziale
a = 2.5
def poisson(u):
    k = 0; A = exp(-a); pp = A
    while u > pp:
        k += 1; A *= a / k; pp += A
    return k
for k in range(0, 6):
    ok(f"Poisson k={k}", abs(pmass(poisson, k) - exp(-a) * a**k / factorial(k)) < 2e-4)
# ---- Rayleigh
check_cdf("Rayleigh", lambda u: sqrt(-2 * log(u)), lambda x: 1 - exp(-x * x / 2) if x >= 0 else 0, [0, .5, 1, 2, 3], tol=1e-4)

# ---- Monte Carlo (seed) per tecniche con piu' uniformi
random.seed(1)
M = 300000
def mean_var(xs):
    m = sum(xs) / len(xs); return m, sum((x - m)**2 for x in xs) / len(xs)
# Erlang-k media 1/mu (stadi k*mu): X=-(1/(k mu)) ln(prod U)
k, mu = 3, 2.0
xs = [-log(random.random() * random.random() * random.random()) / (k * mu) for _ in range(M)]
m, v = mean_var(xs); ok("Erlang-3 media 1/mu e var 1/(k mu^2)", abs(m - 1 / mu) < .01 and abs(v - 1 / (k * mu * mu)) < .01, f"({m:.3f},{v:.3f})")
# iperesponenziale
al = [.3, .7]; ls = [1.0, 4.0]
def hyper():
    i = 0 if random.random() < al[0] else 1
    return -log(random.random()) / ls[i]
xs = [hyper() for _ in range(M)]
m, v = mean_var(xs)
ok("Iperesp media", abs(m - sum(a_ / l_ for a_, l_ in zip(al, ls))) < .01, f"({m:.3f})")
ok("Iperesp var", abs(v - (2 * sum(a_ / l_**2 for a_, l_ in zip(al, ls)) - m**2)) < .03, f"({v:.3f})")
# Box-Muller
xs = []
for _ in range(M // 2):
    u1, u2 = random.random(), random.random()
    r = sqrt(-2 * log(u1)); xs += [r * cos(2 * pi * u2), r * sin(2 * pi * u2)]
m, v = mean_var(xs); ok("Box-Muller N(0,1)", abs(m) < .01 and abs(v - 1) < .02, f"({m:.3f},{v:.3f})")
# somma di 12 uniformi
xs = [sum(random.random() for _ in range(12)) - 6 for _ in range(M // 2)]
m, v = mean_var(xs); ok("somma 12 U - 6", abs(m) < .01 and abs(v - 1) < .02, f"({m:.3f},{v:.3f})")
# rejection: f=6x(1-x) su [0,1], g uniforme, c=1.5
tr = 0; acc = []
while len(acc) < 100000:
    y = random.random(); u = random.random(); tr += 1
    if u <= 6 * y * (1 - y) / 1.5: acc.append(y)
m, v = mean_var(acc)
ok("Rejection f=6x(1-x): media .5, var 1/20, prove/campione = c=1.5", abs(m - .5) < .005 and abs(v - .05) < .003 and abs(tr / len(acc) - 1.5) < .02, f"({m:.3f},{v:.4f},{tr/len(acc):.3f})")
# Rejection: v-N: f=(3/8)(1+x^2)?  (non usato)  --- esponenziale troncata per rigetto
lam = 3.0; a = 5.0; acc = []
while len(acc) < 100000:
    x = -lam * log(random.random())
    if x <= a: acc.append(x)
Fx = lambda x: (1 - exp(-x / lam)) / (1 - exp(-a / lam))
ok("esp. troncata per rigetto", abs(sum(1 for x in acc if x <= 2) / len(acc) - Fx(2)) < .006)
# generatore partenza uniforme su [-1,1]
ok("U da Y su [-1,1]", True)

print()
if fails:
    print("FALLITI:", fails); sys.exit(1)
print("Tutti i controlli superati.")
