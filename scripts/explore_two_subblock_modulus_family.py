#!/usr/bin/env python3
"""Exact profiles and numerical rates for the two-subblock modulus family."""

from __future__ import annotations

import argparse
import math
from collections import defaultdict
from fractions import Fraction


def compositions4(load: int):
    for a0 in range(load + 1):
        for a1 in range(load - a0 + 1):
            for b0 in range(load - a0 - a1 + 1):
                yield (a0, a1, b0, load - a0 - a1 - b0)


def profile(modulus: int):
    group_order = 9 * modulus
    states = []
    rejections = []
    full_support = []
    for load in range(group_order + 2):
        fibers = defaultdict(list)
        for composition in compositions4(load):
            a0, a1, _, b1 = composition
            syndrome = ((a0 + a1) % modulus, a1 % 3, b1 % 3)
            fibers[syndrome].append(composition)

        rejection = Fraction(0)
        all_full = True
        for fiber in fibers.values():
            support = [any(x[i] for x in fiber) for i in range(4)]
            union_size = sum(support)
            all_full &= union_size == 4
            for x in fiber:
                multiplicity = math.factorial(load)
                for coordinate in x:
                    multiplicity //= math.factorial(coordinate)
                rejection += Fraction(multiplicity * (4 - union_size), 4 ** (load + 1))
        states.append(len(fibers))
        rejections.append(rejection)
        full_support.append(all_full)

        if len(fibers) == group_order and all_full:
            break
    else:
        raise AssertionError("profile did not stabilize")
    return states, rejections, full_support


def poisson_rejection(load: float, rejections: list[Fraction]) -> float:
    term = math.exp(-load)
    total = term * float(rejections[0])
    for c in range(1, len(rejections)):
        term *= load / c
        total += term * float(rejections[c])
    return total


def ogf(z: float, states: list[int]) -> float:
    cutoff = len(states) - 1
    return sum(states[c] * z**c for c in range(cutoff)) + (
        states[-1] * z**cutoff / (1.0 - z)
    )


def ogf_mean(z: float, states: list[int]) -> float:
    cutoff = len(states) - 1
    numerator = sum(c * states[c] * z**c for c in range(cutoff))
    numerator += states[-1] * (
        cutoff * z**cutoff / (1.0 - z)
        + z ** (cutoff + 1) / (1.0 - z) ** 2
    )
    return numerator / ogf(z, states)


def evaluate(modulus: int):
    states, rejections, full_support = profile(modulus)
    lower, upper = 0.0, 20.0
    for _ in range(120):
        middle = (lower + upper) / 2.0
        if poisson_rejection(middle, rejections) > 0.5:
            lower = middle
        else:
            upper = middle
    load = (lower + upper) / 2.0

    lower, upper = 1e-14, 1.0 - 1e-14
    for _ in range(120):
        middle = (lower + upper) / 2.0
        if ogf_mean(middle, states) < load:
            lower = middle
        else:
            upper = middle
    saddle = (lower + upper) / 2.0
    rate = math.log2(ogf(saddle, states)) / load - math.log2(saddle)
    return rate, load, saddle, states, rejections, full_support


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=30)
    args = parser.parse_args()
    for modulus in range(1, args.max_modulus + 1):
        rate, load, saddle, states, rejections, _ = evaluate(modulus)
        cutoff = len(states) - 1
        print(
            f"Q={modulus:2d} R={rate:.12f} lambda={load:.12f} "
            f"z={saddle:.12f} cutoff={cutoff:2d} "
            f"d={states} rho={[str(x) for x in rejections]}"
        )


if __name__ == "__main__":
    main()
