#!/usr/bin/env python3
"""Optimistic frozen-tail lower bounds for the (q,Q) cross-block family."""

import math
from collections import defaultdict


TARGET = 2.346149054803345
LAMBDA_EXACT4 = 4 * math.log(2)


def layer_states(q, modulus, load):
    states = set()
    for a0 in range(load + 1):
        for a1 in range(load - a0 + 1):
            for b0 in range(load - a0 - a1 + 1):
                b1 = load - a0 - a1 - b0
                states.add(((a0 + a1) % modulus, a1 % q, b1 % q))
    return len(states)


def optimistic_rate(prefix):
    cutoff = len(prefix)
    tail = prefix[-1]

    def generating_function(z):
        return sum(prefix[c] * z**c for c in range(cutoff)) + tail * z**cutoff / (1 - z)

    def mean(z):
        numerator = sum(c * prefix[c] * z**c for c in range(cutoff))
        numerator += tail * (
            cutoff * z**cutoff / (1 - z) + z ** (cutoff + 1) / (1 - z) ** 2
        )
        return numerator / generating_function(z)

    left, right = 1e-14, 1 - 1e-14
    for _ in range(120):
        middle = (left + right) / 2
        if mean(middle) < LAMBDA_EXACT4:
            left = middle
        else:
            right = middle
    z = (left + right) / 2
    rate = math.log2(generating_function(z)) / LAMBDA_EXACT4 - math.log2(z)
    return rate, z


def main():
    for q in range(2, 31):
        best = (float("inf"), None)
        for modulus in range(1, 31):
            # Exact state counts through load 12, then freeze forever while
            # granting exact-composition rejection at all later loads.
            prefix = [layer_states(q, modulus, load) for load in range(13)]
            rate, z = optimistic_rate(prefix)
            if rate < best[0]:
                best = rate, modulus, z, prefix
        print(q, best[0], "Q", best[1], "excluded", best[0] > TARGET, "d", best[3])


if __name__ == "__main__":
    main()
