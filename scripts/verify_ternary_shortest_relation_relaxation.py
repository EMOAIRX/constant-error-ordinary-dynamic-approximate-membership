#!/usr/bin/env python3
"""Audit the ternary shortest-relation frozen-tail relaxations.

This is a high-precision floating-point verifier, not interval arithmetic.
"""

from __future__ import annotations

import math


def states(c: int) -> int:
    return (c + 1) * (c + 2) // 2


def ogf(r: int, z: float) -> float:
    return sum(states(c) * z**c for c in range(r)) + (
        states(r - 1) * z**r / (1.0 - z)
    )


def ogf_mean(r: int, z: float) -> float:
    numerator = sum(c * states(c) * z**c for c in range(1, r))
    numerator += states(r - 1) * (
        r * z**r / (1.0 - z) + z ** (r + 1) / (1.0 - z) ** 2
    )
    return numerator / ogf(r, z)


def saddle_rate(r: int, load: float) -> tuple[float, float]:
    lower = 1e-15
    upper = 1.0 - 1e-15
    for _ in range(180):
        middle = (lower + upper) / 2.0
        if ogf_mean(r, middle) < load:
            lower = middle
        else:
            upper = middle
    z = (lower + upper) / 2.0
    rate = math.log2(ogf(r, z)) / load - math.log2(z)
    return rate, z


def zero_tail_rejection(r: int, load: float) -> float:
    term = math.exp(-load)
    total = term
    for c in range(1, r):
        term *= load / c
        total += term * (2.0 / 3.0) ** c
    return total


def zero_tail_root(r: int) -> float:
    lower = 0.0
    upper = 10.0
    for _ in range(180):
        middle = (lower + upper) / 2.0
        if zero_tail_rejection(r, middle) > 0.5:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2.0


def main() -> None:
    benchmark = 2.349083440193
    exact_tail_load = 3.0 * math.log(2.0)
    print(" r   optimistic_exact_tail   threshold_zero_tail   zero_tail_load")
    for r in range(4, 16):
        optimistic, _ = saddle_rate(r, exact_tail_load)
        threshold_load = zero_tail_root(r)
        threshold, _ = saddle_rate(r, threshold_load)
        marker = "> benchmark" if optimistic > benchmark else "<= benchmark"
        print(
            f"{r:2d}   {optimistic:.12f} {marker:12s}   "
            f"{threshold:.12f}   {threshold_load:.12f}"
        )


if __name__ == "__main__":
    main()
