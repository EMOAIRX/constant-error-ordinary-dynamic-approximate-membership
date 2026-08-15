#!/usr/bin/env python3
"""Numerical verifier for the Poisson-entropy phase transition.

This is deliberately dependency-free.  It evaluates the exact derivative
identities by summing Poisson probabilities and uses bisection for the two
reported roots.  It is evidence/a regression test, not directed-rounding
interval arithmetic and therefore is not by itself a formal proof.
"""

import math


def poisson_entropy_derivatives(lam):
    """Return H, H', H'' in nats for X ~ Poisson(lam)."""
    cutoff = max(120, math.ceil(lam + 22 * math.sqrt(lam + 1)))
    probability = math.exp(-lam)
    entropy = 0.0
    expected_log_next = 0.0
    expected_log_ratio = 0.0

    for k in range(cutoff):
        if k:
            probability *= lam / k
        if probability:
            entropy -= probability * math.log(probability)
        expected_log_next += probability * math.log(k + 1)
        expected_log_ratio += probability * math.log((k + 2) / (k + 1))

    first = expected_log_next - math.log(lam)
    second = expected_log_ratio - 1 / lam
    return entropy, first, second


def quantities(lam):
    entropy, first, second = poisson_entropy_derivatives(lam)
    r = entropy / lam
    r1 = first / lam - entropy / lam**2
    r2 = second / lam - 2 * first / lam**2 + 2 * entropy / lam**3
    return {
        "r": r,
        "f1": math.exp(lam) * (r + r1),
        "f2": math.exp(lam) * (r + 2 * r1 + r2),
        "curve_curvature_sign": r2 + r1,
    }


def bisect(function, left, right, iterations=90):
    left_value = function(left)
    right_value = function(right)
    assert left_value * right_value <= 0
    for _ in range(iterations):
        middle = (left + right) / 2
        middle_value = function(middle)
        if left_value * middle_value <= 0:
            right, right_value = middle, middle_value
        else:
            left, left_value = middle, middle_value
    return (left + right) / 2


def main():
    minimizer = bisect(lambda x: quantities(x)["f1"], 0.3, 0.6)
    inflection = bisect(
        lambda x: quantities(x)["curve_curvature_sign"], 1.0, 2.0
    )
    q = quantities(minimizer)

    print(f"lambda_* = {minimizer:.15f}")
    print(f"epsilon_* = {1 - math.exp(-minimizer):.15f}")
    print(f"C_* (nats) = {math.exp(minimizer) * q['r']:.15f}")
    print(f"C_* (bits) = {math.exp(minimizer) * q['r'] / math.log(2):.15f}")
    print(f"curve inflection lambda = {inflection:.15f}")

    # Dense logarithmic regression grid.  Convexity of f=e^lambda r implies
    # the supporting-line claim and uniqueness of its stationary point.
    minimum_f2 = float("inf")
    minimum_curvature_before_star = float("inf")
    previous_f1 = None
    monotone_f1 = True
    for i in range(20001):
        exponent = -6 + i * 8 / 20000
        lam = 10**exponent
        values = quantities(lam)
        minimum_f2 = min(minimum_f2, values["f2"])
        if lam <= minimizer:
            minimum_curvature_before_star = min(
                minimum_curvature_before_star,
                values["curve_curvature_sign"],
            )
        if previous_f1 is not None and values["f1"] < previous_f1 - 1e-9:
            monotone_f1 = False
        previous_f1 = values["f1"]

    print(f"minimum sampled (e^lambda r)'' = {minimum_f2:.12g}")
    print(
        "minimum sampled curve-curvature sign before lambda_* = "
        f"{minimum_curvature_before_star:.12g}"
    )
    print(f"sampled (e^lambda r)' monotone = {monotone_f1}")


if __name__ == "__main__":
    main()
