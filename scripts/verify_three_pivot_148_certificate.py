#!/usr/bin/env python3
"""Pure-rational certificate that the three-pivot constant exceeds 1.48.

The analytic input is that the three branches f0, f1, fm are convex on
0 < p < q < 1.  For positive weights summing to one, their mixture L is
therefore convex and max(f0, f1, fm) >= L.  At the rational point x0 below,

    L(x) >= L(x0) + grad L(x0) . (x - x0).

Every quantity on the right is enclosed using Fraction arithmetic.  The
gradient residual is bounded over the larger rectangle [0, 1]^2, producing
a global lower bound on L and hence on C_3.  Decimal output is display only;
all assertions are comparisons of exact rational numbers.
"""

from __future__ import annotations

from fractions import Fraction as F


Interval = tuple[F, F]
TARGET = F(148, 100)


def add(x: Interval, y: Interval) -> Interval:
    return x[0] + y[0], x[1] + y[1]


def mul(x: Interval, y: Interval) -> Interval:
    values = [x[i] * y[j] for i in (0, 1) for j in (0, 1)]
    return min(values), max(values)


def scale(c: F, x: Interval) -> Interval:
    return (c * x[0], c * x[1]) if c >= 0 else (c * x[1], c * x[0])


def inv(x: Interval) -> Interval:
    assert x[0] > 0
    return F(1, 1) / x[1], F(1, 1) / x[0]


def div(x: Interval, y: Interval) -> Interval:
    return mul(x, inv(y))


def log_interval(x: F, terms: int = 120) -> Interval:
    """Bound ln(x) via the atanh series, entirely over rationals."""
    assert x > 0
    if x < 1:
        lo, hi = log_interval(1 / x, terms)
        return -hi, -lo
    z = (x - 1) / (x + 1)
    partial = F(0)
    power = z
    for k in range(terms):
        partial += power / (2 * k + 1)
        power *= z * z
    lower = 2 * partial
    remainder = 2 * power / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + remainder


LN2 = log_interval(F(2))


def log2_interval(x: F) -> Interval:
    return div(log_interval(x), LN2)


def a_value(x: F) -> Interval:
    return log2_interval(F(2) / x)


def b_value(x: F) -> Interval:
    y = F(1) - x / 2
    return scale(y, log2_interval((F(2) - x) / (F(1) - x)))


def phi_value(p: F, q: F) -> Interval:
    y = F(1) - p / 2
    return scale(y, log2_interval((F(2) - p) / (q - p)))


def inv_ln2() -> Interval:
    return inv(LN2)


def a_prime(x: F) -> Interval:
    return scale(-F(1) / x, inv_ln2())


def b_prime(x: F) -> Interval:
    natural = add(
        scale(-F(1, 2), add(log_interval((F(2) - x) / (F(1) - x)), (F(1), F(1)))),
        ((F(2) - x) / (2 * (F(1) - x)),) * 2,
    )
    return mul(natural, inv_ln2())


def phi_a_prime(p: F, q: F) -> Interval:
    natural = add(
        scale(-F(1, 2), add(log_interval((F(2) - p) / (q - p)), (F(1), F(1)))),
        ((F(2) - p) / (2 * (q - p)),) * 2,
    )
    return mul(natural, inv_ln2())


def phi_b_prime(p: F, q: F) -> Interval:
    return scale(-(F(2) - p) / (2 * (q - p)), inv_ln2())


def main() -> None:
    p, q = F(149, 250), F(107, 125)
    weights = [F(388, 1000), F(411, 1000), F(201, 1000)]
    assert 0 < p < q < 1
    assert all(weight > 0 for weight in weights)
    assert sum(weights, F(0)) == 1

    f0 = scale(F(1, 2), add(a_value(p), a_value(q)))
    f1 = scale(F(1, 2), add(b_value(p), b_value(q)))
    fm = scale(F(1, 2), add(b_value(p), phi_value(p, q)))
    value = add(add(scale(weights[0], f0), scale(weights[1], f1)), scale(weights[2], fm))

    gp = add(
        add(scale(weights[0] / 2, a_prime(p)), scale(weights[1] / 2, b_prime(p))),
        scale(weights[2] / 2, add(b_prime(p), phi_a_prime(p, q))),
    )
    gq = add(
        add(scale(weights[0] / 2, a_prime(q)), scale(weights[1] / 2, b_prime(q))),
        scale(weights[2] / 2, phi_b_prime(p, q)),
    )

    # On the containing rectangle [0,1]^2, the two residual affine terms
    # lose at most max(|r|p0, |r|(1-p0)) in each coordinate.
    gp_abs = max(abs(gp[0]), abs(gp[1]))
    gq_abs = max(abs(gq[0]), abs(gq[1]))
    loss = gp_abs * max(p, 1 - p) + gq_abs * max(q, 1 - q)
    certified = value[0] - loss

    # Publish a short exact rational below the (very large) Fraction obtained
    # from the 120-term logarithm enclosures.  This makes the final comparison
    # readable while the assertion still checks the full-precision bound.
    coarse_denominator = 10**12
    coarse_numerator = (
        certified.numerator * coarse_denominator // certified.denominator
    )
    coarse_lower = F(coarse_numerator, coarse_denominator)
    assert coarse_lower <= certified

    print(f"weighted_value_lower={float(value[0]):.15f}")
    print(f"gradient_p_interval=({float(gp[0]):.15f},{float(gp[1]):.15f})")
    print(f"gradient_q_interval=({float(gq[0]):.15f},{float(gq[1]):.15f})")
    print(f"global_lower={float(certified):.15f}")
    print(
        "readable_exact_lower="
        f"{coarse_lower.numerator}/{coarse_lower.denominator}"
    )
    print(
        "exact_margin_over_1.48="
        f"{(coarse_lower - TARGET).numerator}/"
        f"{(coarse_lower - TARGET).denominator}"
    )
    assert coarse_lower > TARGET
    assert certified > TARGET
    print("PASS: C_3 > 1.48")


if __name__ == "__main__":
    main()
