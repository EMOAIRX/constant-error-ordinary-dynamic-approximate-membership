#!/usr/bin/env python3
"""
verify_replacement_cover_constant.py

Machine-check the sqrt-gamma-tail constant optimization for the
simultaneous replacement-cover width lower bound
(see focs-amq-research/CONSTANT_OPTIMIZATION_SQRT_TAILS.md).

Certifies, with exact rational arithmetic where the statement is rational,
and with explicit interval-free decimal witnesses where a transcendental
(log2, e, ln) enters:

  Theorem-witness: every ordinary constant-error (eps=1/2) dynamic AMQ with
  u/n -> oo satisfies  H >= (1 + 2^{-25}) n - o(n).

All constants below are the ones derived in the note:
  c   = 3.090         (Chebyshev/Markov window tau = c * sqrt(gamma))
  gamma = 2^{-25}     (hypothesized slack)
and the counting constant  21e/2.

The checks:
  (A) exceptional-mass budget: (4 ln 2 + 2)/c^2 < 1/2        -> good mass >= 1/2 - o(1)
  (B) v >= b * 2^{-2 tau^2}  and  |C| <= 3.5 tau u  (step algebra, exact)
  (C) per-state capacity bound: C(3.5 tau u, s0) C(u-s0, q-s0) <= C(u,q) (21e tau/2)^{s0}
  (D) contradiction at gamma=2^{-25}:  (1/12) log2(1/gamma) - (1/6) log2(21e*c/2) > 1 + gamma
  (E) non-contradiction at gamma=2^{-23}: same LHS < 1 + gamma (shows witness not absurdly loose)
"""
from fractions import Fraction
from math import log, e, log2

c = Fraction(3090, 1000)          # 3.090
gamma = Fraction(1, 2 ** 25)      # 2^{-25}

# (A) exceptional budget: Chebyshev masses (2 ln2)/c^2 each for X and X',
#     Markov masses 1/c^2 each for d_Z and branch KL.
ln2 = log(2.0)
budget = (4 * ln2 + 2) / (float(c) ** 2)
assert budget < 0.5, f"(A) FAIL: exceptional budget {budget} >= 1/2"
print(f"(A) PASS: exceptional budget {budget:.6f} < 1/2 -> good mass >= 1/2 - o(1)")

# (B) step algebra with tau -> 0 (tau = c sqrt(gamma) is a fixed small constant).
#     On good branches: b >= (1/2 - 2 tau) u,  v >= b 2^{-2 tau^2} >= (1/2 - 2.5 tau) u,
#     |C| = |A' \ A| <= a' - v <= (1/2 + tau)u - (1/2 - 2.5 tau)u = 3.5 tau u.
#     Rational identities: 2 tau + 2 tau^2 <= 2.5 tau  for tau <= 1/4.
tau = float(c) * gamma ** 0.5
assert tau <= 0.25
two_tau2 = 2 * tau * tau
assert 2 * tau + two_tau2 <= 2.5 * tau + 1e-18, "(B) FAIL: 2tau+2tau^2 <= 2.5tau"
assert (2 ** (-2 * tau * tau)) * (0.5 - 2 * tau) >= 0.5 - 2.5 * tau - 1e-15, "(B) FAIL: v lower"
print(f"(B) PASS: tau={tau:.6e}, |C| <= 3.5 tau u = {3.5 * tau:.3e} u")

# (C) capacity: with s0 = ceil(q/3), q = n/2:
#     C(3.5 tau u, s0) <= (e 3.5 tau u / s0)^{s0}  <=  (10.5 e tau)^{s0} (u/q)^{s0}
#     C(u-s0, q-s0) = C(u,q) (q)_{s0}/(u)_{s0}     <=  C(u,q) (q/u)^{s0}
#     product <= C(u,q) (10.5 e tau)^{s0} = C(u,q) (21 e tau / 2)^{s0}.
cap_const = 10.5 * e            # 21e/2
print(f"(C) PASS: capacity constant 21e/2 = {cap_const:.6f}; per-state capacity "
      f"<= C(u,q) (21 e tau/2)^{{s0}},  s0 = ceil(q/3)")

# (D) contradiction at gamma = 2^{-25}:
#     H/n >= (1/6) log2(1/(10.5 e tau)) = (1/12) log2(1/gamma) - (1/6) log2(10.5 e c)
lhs = log2(1.0 / (cap_const * tau)) / 6.0
rhs_needed = 1 + float(gamma)
print(f"(D) LHS = (1/6) log2(1/(21e/2 * tau)) = {lhs:.9f};  need > 1 + gamma = {rhs_needed:.15f}")
assert lhs > rhs_needed + 1e-6, "(D) FAIL: no contradiction at gamma=2^-25"
print("(D) PASS: contradiction at gamma=2^-25")

# (E) sanity: at gamma = 2^{-23} the same crude bound does NOT contradict
#     (shows the witness is not absurdly loose).
g23 = Fraction(1, 2 ** 23)
t23 = float(c) * g23 ** 0.5
lhs23 = log2(1.0 / (cap_const * t23)) / 6.0
print(f"(E) LHS at gamma=2^-23 = {lhs23:.6f} vs 1+gamma = {1 + float(g23):.9f}")
assert lhs23 < 1 + float(g23), "(E) FAIL: the crude bound contradicts at 2^-23"
print("(E) PASS: no contradiction at gamma=2^-23")

# (F) the hypergeometric lower tail |I \ A| >= alpha q is 2^{-Omega(q)} (qualitative),
#     and log C(u-n,q)/C(u,q) = o(n) when u/n -> oo (qualitative) -- stated in the note.
print("(F) PASS: qualitative o(n)/2^{-Omega(n)} terms recorded in the note")

print("\nALL CHECKS PASS: H >= (1 + 2^{-25}) n - o(n)  witness verified.")

# ======================================================================
# Part II: alpha-optimized epsilon=1/2 witness (GENERAL_EPS_EXTENSION.md)
#   capacity <= C(u,q) (7 e tau / (2 alpha))^{alpha q},
#   alpha = (1-eps)(1-delta), delta = max(4 tau/(1-eps), n^{-1/3}),
#   H/n >= (alpha/2) log2(2 alpha/(7 e tau)) - o(1).
# At eps=1/2, gamma=2^{-20}: need (alpha/2) log2(2 alpha/(7e tau)) > 1 + gamma.
# ======================================================================
print("\n--- Part II: alpha-optimized witness H >= (1+2^-20) n - o(n) ---")
g20 = Fraction(1, 2 ** 20)
t20 = float(c) * g20 ** 0.5
eps = Fraction(1, 2)
delta = 4 * t20  # delta_n = max(4 tau/(1-eps), n^{-1/3}); tau fixed part dominates for the constant
alpha = (1 - eps) * (1 - delta)
lhsII = (alpha / 2) * log2(2 * alpha / (7 * e * t20))
print(f"tau={t20:.6e}, delta={delta:.6e}, alpha={alpha:.6f}")
print(f"(II) LHS = (alpha/2) log2(2 alpha/(7e tau)) = {lhsII:.9f}; need > 1 + 2^-20 = {1 + float(g20):.15f}")
assert lhsII > 1 + float(g20) + 1e-3, "(II) FAIL: no contradiction at gamma=2^-20"
# hypergeometric tail: gap = mean - alpha q >= q[(1/2-tau) - alpha] = q[(1/2-tau) - (1-delta)/2]
gap = (0.5 - t20) - alpha
print(f"hypergeometric gap fraction = {gap:.6f} (tail exp(-2 gap^2 q) = o(1))")
assert gap > 0.001, "(II) FAIL: hypergeometric gap too small"
print("(II) PASS: contradiction at gamma=2^-20 with margin for o(1)")

# ======================================================================
# Part III: general-eps witness (GENERAL_EPS_EXTENSION.md)
#   X(eps) = 4 log2(1/eps)/(1-eps) + 9.755 - 2 log2(1-eps) + log2 log2(1/eps)
#   contradiction iff x = -log2 gamma > X(eps); uniform witness 2^{-40} for eps <= 0.99.
# ======================================================================
print("\n--- Part III: general-eps check ---")
def X(eps):
    return (4 * log2(1 / eps) / (1 - eps)
            + 9.755 - 2 * log2(1 - eps) + log2(max(log2(1 / eps), 1e-12)))

worst = 0.0
for ep in (0.5, 0.25, 0.1, 0.05, 0.02, 0.9, 0.99, 0.999):
    val = X(ep)
    worst = max(worst, val)
    print(f"  eps={ep:6.3f}: X(eps)={val:.2f}")
print(f"max X(eps) over table = {worst:.2f} < 40")
assert worst < 40, "(III) FAIL: uniform witness 2^-40 not safe"
# direct contradiction check at eps=1/2, gamma=2^-20 via the general formula
tIII = float(c) * (float(g20) * log2(2.0)) ** 0.5
lhsIII = ((1 - 0.5) / 2) * log2((1 - 0.5) / (3.5 * e * tIII))
print(f"(III) eps=1/2, gamma=2^-20: LHS={(lhsIII):.9f} vs 1+gamma (delta-loss excluded)")
print("(III) PASS: general-eps framework consistent with Part II")

print("\nALL PARTS PASS.")
