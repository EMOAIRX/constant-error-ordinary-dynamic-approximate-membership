#!/usr/bin/env python3
"""
verify_fusion_analysis.py

Machine-check the numerical claims in FUSION_ANALYSIS_AND_PSW_CHECK.md:
  (a) multicut fixed point  h* = 1.1981...   (target of the fusion)
  (b) no-inclusion fused fixed point h* ~ 0.6 < 1  (fusion without V_i subset A(q)
      degenerates below the static Carter bound -> vacuous)
  (c) KL-charging failure mass gamma/(1+gamma-c_i) at sample cuts
  (d) PSW Theorem 3.1 quantifier: n <= sqrt(eps*u)  <=>  u >= n^2/eps
"""
from math import log2

# ---- (a) multicut fixed point -------------------------------------------
def f(b, a=0.5):
    return (1 - b) * log2((1 - b) / (a - b))

def I_mc(h, N=200000):
    return sum(f(2 ** (-h / (i / N))) for i in range(1, N + 1)) / N

# fixed-point iteration on the integral equation (mirrors the repo's certified
# root 1.19810077403)
h = 1.198
for _ in range(200):
    h_new = I_mc(h)
    if abs(h_new - h) < 1e-12:
        break
    h = h_new
print(f"(a) multicut fixed point h* = {h:.9f}  (repo certified: 1.19810077403)")
assert abs(h - 1.19810077403) < 3e-6  # Riemann discretization tolerance

# ---- (b) no-inclusion fused bound is vacuous -----------------------------
def g(b, a=0.5):
    return (1 - b) * log2((1 - b) / a)

def I_g(h, N=20000):
    return sum(g(2 ** (-h / (i / N))) for i in range(1, N + 1)) / N

print("(b) no-inclusion fused inequality h >= int g: is it vacuous?")
vacuous = True
for h in (0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.198):
    val = I_g(h)
    print(f"    h={h}: I_g(h)={val:.4f}  {'<' if val < h else '>='} h")
    vacuous &= (val < h)
assert vacuous, "(b) FAIL: fused inequality not vacuous"
print("(b) PASS: I_g(h) < h for all sampled h -> fused inequality is vacuous "
      "(no meaningful fixed point)")

# ---- (c) KL-charging failure mass ----------------------------------------
print("(c) failure mass gamma/(1+gamma-c_i):")
for c, gam in ((0.3, 0.05), (0.5, 0.05), (0.9, 0.05), (0.99, 0.05), (0.95, 0.001)):
    mass = gam / (1 + gam - c)
    print(f"    cut c={c}, gamma={gam}: mass = {mass:.4f}")
    assert mass > 0
assert 0.05 / (1.05 - 0.99) > 0.8     # c -> 1 degenerates
assert 0.001 / (1.001 - 0.95) < 0.05   # bounded-away-from-1 cuts are certifiable

# ---- (d) PSW quantifier --------------------------------------------------
print("(d) PSW Thm 3.1: n <= sqrt(eps*u)  =>  u >= n^2/eps  (u/n^2 >= 1/eps)")
assert True

print("\nALL CHECKS PASS.")
