#!/usr/bin/env python3
"""Exact rational certificates used in POISSON_PHASE_TRANSITION_ANALYTIC.md.

This script deliberately contains no floating-point positivity test.  It
converts rational power-basis polynomials to Bernstein form on rational
intervals; nonnegative Bernstein coefficients certify nonnegativity.
"""

from fractions import Fraction as Q
from math import comb


def restrict_power(coeff, left, right):
    """Coefficients of p(left + (right-left)t), t in [0,1]."""
    degree = len(coeff) - 1
    out = [Q(0)] * (degree + 1)
    for i, value in enumerate(coeff):
        for j in range(i + 1):
            out[j] += value * comb(i, j) * left ** (i - j) * (right-left) ** j
    return out


def bernstein_coefficients(power):
    degree = len(power) - 1
    return [
        sum(
            power[i] * Q(comb(k, i), comb(degree, i))
            for i in range(k + 1)
        )
        for k in range(degree + 1)
    ]


def certify(coeff, intervals, name):
    for left, right in intervals:
        bernstein = bernstein_coefficients(restrict_power(coeff, left, right))
        assert min(bernstein) > 0, (name, left, right, bernstein)
    print(f"PASS {name}: {len(intervals)} exact Bernstein interval(s)")


def main():
    # With log 2 >= 69/100, exp(-x) bounded below by its degree-5
    # alternating Taylor polynomial, and log(1+x) bounded above by its
    # degree-5 alternating Taylor polynomial, q(x) is at least P(x).
    # q controls the global F'' proof on 0 < x <= 1.
    p_global = [
        Q(1), -Q(331, 100), Q(331, 100), -Q(793, 600),
        Q(631, 600), -Q(697, 800), Q(1577, 4000),
    ]
    dyadic_cover = [
        (Q(0), Q(1, 2)),
        (Q(1, 2), Q(5, 8)),
        (Q(5, 8), Q(21, 32)),
        (Q(21, 32), Q(11, 16)),
        (Q(11, 16), Q(3, 4)),
        (Q(3, 4), Q(1)),
    ]
    certify(p_global, dyadic_cover, "global small-load F'' lower bound")

    # On 0 < x <= 11/25, the curvature numerator is at least x*C(x).
    # Here we also use -log x >= 1-x, besides the same elementary bounds.
    p_curve = [Q(1), -Q(331, 100), Q(431, 100), -Q(8, 3), Q(2, 3)]
    certify(
        p_curve,
        [(Q(0), Q(11, 25))],
        "low-load curvature lower bound",
    )


if __name__ == "__main__":
    main()
