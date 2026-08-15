#!/usr/bin/env python3
"""Rational certificates for the q<=5 two-subblock infinite strips."""

from __future__ import annotations

from fractions import Fraction
from math import factorial

from verify_cross_block_mod6_construction import (
    LN2_HIGH,
    exp_negative_bounds,
    log_bounds,
)


R36_UPPER = Fraction(234616, 100000)  # 2.34616, certified by the Q=6 verifier.

CASES = {
    2: (6, Fraction(2293, 1000)),
    3: (9, Fraction(663, 250)),
    4: (7, Fraction(2751, 1000)),
    5: (7, Fraction(277, 100)),
}


def exact_allocation_states(q: int, load: int) -> int:
    return sum(
        min(a + 1, q) * min(load - a + 1, q)
        for a in range(load + 1)
    )


def frozen_ogf(q: int, cutoff: int, z: Fraction) -> Fraction:
    tail = exact_allocation_states(q, cutoff - 1)
    return sum(
        exact_allocation_states(q, c) * z**c for c in range(cutoff)
    ) + tail * z**cutoff / (1 - z)


def frozen_mean(q: int, cutoff: int, z: Fraction) -> Fraction:
    tail = exact_allocation_states(q, cutoff - 1)
    numerator = sum(
        c * exact_allocation_states(q, c) * z**c
        for c in range(1, cutoff)
    )
    numerator += tail * (
        cutoff * z**cutoff / (1 - z)
        + z ** (cutoff + 1) / (1 - z) ** 2
    )
    return numerator / frozen_ogf(q, cutoff, z)


def uncoupled_rejection_upper(q: int, load: Fraction) -> Fraction:
    polynomial = sum(
        (load / 4) ** t / factorial(t) for t in range(q)
    )
    _, exp_upper = exp_negative_bounds(load / 2)
    return exp_upper * polynomial


def objective_lower(
    q: int, cutoff: int, load_upper: Fraction, left: Fraction, right: Fraction
) -> Fraction:
    log_a_left, _ = log_bounds(frozen_ogf(q, cutoff, left))
    _, log_right = log_bounds(right)
    return log_a_left / (load_upper * LN2_HIGH) - log_right / LN2_HIGH


def certify_case(q: int, cutoff: int, load_upper: Fraction) -> Fraction:
    assert uncoupled_rejection_upper(q, load_upper) < Fraction(1, 2)

    # Coarse exterior bounds. A(z)>=1 makes -log_2(z) sufficient on the left.
    left_edge = Fraction(3, 10)
    right_edge = Fraction(11, 20)
    _, log_left = log_bounds(left_edge)
    left_lower = -log_left / LN2_HIGH

    # log A(e^y) is convex in y. Once its tilted mean is above load_upper,
    # the objective is increasing for every larger z.
    assert frozen_mean(q, cutoff, right_edge) > load_upper
    right_lower = objective_lower(
        q, cutoff, load_upper, right_edge, right_edge
    )

    # The left exterior objective is decreasing up to the unique saddle;
    # the saddle lies to the right because the tilted mean is below load.
    assert frozen_mean(q, cutoff, left_edge) < load_upper
    left_lower = objective_lower(q, cutoff, load_upper, left_edge, left_edge)
    minimum = min(left_lower, right_lower)
    pieces = 800
    width = right_edge - left_edge
    for index in range(pieces):
        left = left_edge + width * index / pieces
        right = left_edge + width * (index + 1) / pieces
        minimum = min(
            minimum,
            objective_lower(q, cutoff, load_upper, left, right),
        )
    return minimum


def main() -> None:
    for q, (cutoff, load_upper) in CASES.items():
        lower = certify_case(q, cutoff, load_upper)
        assert lower > R36_UPPER
        print(
            f"q={q} Q0={cutoff} lambda_upper={float(load_upper):.6f} "
            f"certified_rate_lower={float(lower):.9f}"
        )
    print("PASS")


if __name__ == "__main__":
    main()
