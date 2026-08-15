"""Numerical phase diagram for binary algebraic threshold quotients."""

from __future__ import annotations

import argparse
import math
import os
import sys

extra = "/private/tmp/dynamic-amq-scipy"
if os.path.isdir(extra):
    sys.path.insert(0, extra)
import numpy as np
from scipy.optimize import brentq


def poisson_no_probability(level: int, load: float) -> float:
    term = 1.0
    total = 1.0
    for t in range(1, level + 1):
        term *= load / (2.0 * t)
        total += term
    return math.exp(-load) * total


def calibrated_load(level: int, epsilon: float) -> float:
    target = 1.0 - epsilon
    hi = max(1.0, -2.0 * math.log(target) + level + 2.0)
    while poisson_no_probability(level, hi) > target:
        hi *= 2.0
    return brentq(
        lambda load: poisson_no_probability(level, load) - target,
        0.0,
        hi,
        xtol=1e-14,
    )


def local_gf(level: int, z: float) -> float:
    return sum((t + 1) * z**t for t in range(level + 1)) + (
        (level + 1) * z ** (level + 1) / (1.0 - z)
    )


def local_gf_derivative(level: int, z: float) -> float:
    polynomial = sum(t * (t + 1) * z ** (t - 1) for t in range(1, level + 1))
    tail = (level + 1) * (
        (level + 1) * z**level / (1.0 - z)
        + z ** (level + 1) / (1.0 - z) ** 2
    )
    return polynomial + tail


def rate(level: int, epsilon: float) -> tuple[float, float, float]:
    load = calibrated_load(level, epsilon)
    z = brentq(
        lambda value: value * local_gf_derivative(level, value) / local_gf(level, value) - load,
        1e-14,
        1.0 - 1e-14,
        xtol=1e-14,
    )
    value = math.log2(local_gf(level, z)) / load - math.log2(z)
    return value, load, z


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-level", type=int, default=30)
    parser.add_argument("--grid", type=int, default=3000)
    args = parser.parse_args()
    epsilons = np.geomspace(1e-5, 1.0 - 1e-5, args.grid)
    winners = []
    for epsilon in epsilons:
        values = [rate(level, float(epsilon))[0] for level in range(args.max_level + 1)]
        winners.append(int(np.argmin(values)))
    intervals = []
    start = 0
    for index in range(1, len(epsilons) + 1):
        if index == len(epsilons) or winners[index] != winners[start]:
            intervals.append((winners[start], epsilons[start], epsilons[index - 1]))
            start = index
    for level, left, right in intervals:
        print(f"grid winner L={level}: epsilon in [{left:.12g}, {right:.12g}]")
    print("refined adjacent boundaries")
    for first, second in zip(intervals, intervals[1:]):
        left_level, _, left_hi = first
        right_level, right_lo, _ = second
        root = brentq(
            lambda epsilon: rate(left_level, epsilon)[0] - rate(right_level, epsilon)[0],
            left_hi,
            right_lo,
            xtol=1e-13,
        )
        value = rate(left_level, root)[0]
        print(f"L={left_level} -> L={right_level}: epsilon={root:.12g}, R={value:.12g}")
    print("sample points")
    for epsilon in (1e-4, 1e-3, .01, .05, .1, .2, .3, .4, .5, .6, .7, .8, .9, .99):
        values = [rate(level, epsilon)[0] for level in range(args.max_level + 1)]
        level = int(np.argmin(values))
        value, load, z = rate(level, epsilon)
        baseline = rate(0, epsilon)[0]
        print(
            f"eps={epsilon:.6g} L={level} lambda={load:.9g} "
            f"R={value:.12g} R0={baseline:.12g} gain={baseline-value:.12g}"
        )


if __name__ == "__main__":
    main()
