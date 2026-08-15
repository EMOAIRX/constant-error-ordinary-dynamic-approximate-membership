#!/usr/bin/env python3
"""Heuristic search for four-symbol Cayley quotients in a fixed Abelian group.

Profiles use exact integer walk counts and support unions.  The final rate is
floating point, so this is a candidate finder rather than a certificate.
"""

from __future__ import annotations

import argparse
import math
import random
from collections import defaultdict
from functools import lru_cache


def add(x, y, factors):
    return tuple((a + b) % modulus for a, b, modulus in zip(x, y, factors))


def generated_group(subset, factors):
    zero = (0,) * len(factors)
    reached = {zero}
    while True:
        expanded = reached | {add(x, symbol, factors) for x in reached for symbol in subset}
        if expanded == reached:
            return len(reached) == math.prod(factors)
        reached = expanded


def profile(subset, factors):
    zero = (0,) * len(factors)
    walk_counts = {zero: 1}
    support_unions = {zero: 0}
    states = []
    rejection = []
    order = math.prod(factors)

    for load in range(2 * order + 1):
        states.append(len(walk_counts))
        rejected_pairs = sum(
            multiplicity * (4 - support_unions[state].bit_count())
            for state, multiplicity in walk_counts.items()
        )
        rejection.append(rejected_pairs / 4 ** (load + 1))
        if len(walk_counts) == order and all(mask == 15 for mask in support_unions.values()):
            return tuple(states), tuple(rejection), load

        next_counts = defaultdict(int)
        next_unions = defaultdict(int)
        for state, multiplicity in walk_counts.items():
            for symbol, increment in enumerate(subset):
                target = add(state, increment, factors)
                next_counts[target] += multiplicity
                next_unions[target] |= support_unions[state] | (1 << symbol)
        walk_counts = dict(next_counts)
        support_unions = dict(next_unions)
    raise AssertionError("profile did not stabilize")


def poisson_rejection(lam, rejection):
    term = math.exp(-lam)
    total = term * rejection[0]
    for load in range(1, len(rejection)):
        term *= lam / load
        total += term * rejection[load]
    return total


def ogf(z, states, cutoff, order):
    return sum(states[c] * z**c for c in range(cutoff)) + order * z**cutoff / (1 - z)


def ogf_mean(z, states, cutoff, order):
    numerator = sum(c * states[c] * z**c for c in range(cutoff))
    numerator += order * (
        cutoff * z**cutoff / (1 - z) + z ** (cutoff + 1) / (1 - z) ** 2
    )
    return numerator / ogf(z, states, cutoff, order)


def make_evaluator(factors):
    order = math.prod(factors)

    @lru_cache(maxsize=None)
    def evaluate(tail):
        zero = (0,) * len(factors)
        subset = (zero, *tail)
        if not generated_group(subset, factors):
            return (float("inf"), None)
        states, rejection, cutoff = profile(subset, factors)
        left, right = 0.0, 10.0
        for _ in range(80):
            middle = (left + right) / 2
            if poisson_rejection(middle, rejection) > 0.5:
                left = middle
            else:
                right = middle
        lam = (left + right) / 2

        left, right = 1e-14, 1 - 1e-14
        for _ in range(80):
            middle = (left + right) / 2
            if ogf_mean(middle, states, cutoff, order) < lam:
                left = middle
            else:
                right = middle
        z = (left + right) / 2
        rate = math.log2(ogf(z, states, cutoff, order)) / lam - math.log2(z)
        return rate, (subset, lam, z, states, rejection, cutoff)

    return evaluate


def normalized_tail(elements):
    return tuple(sorted(elements))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--factors", default="6,3,3")
    parser.add_argument("--restarts", type=int, default=60)
    parser.add_argument("--steps", type=int, default=500)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    factors = tuple(int(value) for value in args.factors.split(","))
    zero = (0,) * len(factors)
    group = [
        tuple(coordinates)
        for coordinates in __import__("itertools").product(*(range(m) for m in factors))
    ]
    nonzero = [element for element in group if element != zero]
    rng = random.Random(args.seed)
    evaluate = make_evaluator(factors)

    seeds = []
    if factors == (6, 3, 3):
        seeds.append(normalized_tail(((1, 0, 0), (1, 1, 0), (0, 0, 1))))
    best = (float("inf"), None)
    for restart in range(args.restarts):
        current = seeds[restart] if restart < len(seeds) else normalized_tail(rng.sample(nonzero, 3))
        score, data = evaluate(current)
        temperature = 0.01
        for step in range(args.steps):
            mutated = list(current)
            mutated[rng.randrange(3)] = rng.choice(nonzero)
            if len(set(mutated)) < 3:
                continue
            candidate = normalized_tail(mutated)
            candidate_score, candidate_data = evaluate(candidate)
            delta = candidate_score - score
            if delta <= 0 or rng.random() < math.exp(-delta / max(temperature, 1e-8)):
                current, score, data = candidate, candidate_score, candidate_data
            temperature *= 0.99
            if score < best[0]:
                best = (score, data)
                subset, lam, z, states, rejection, cutoff = data
                print(
                    f"BEST R={score:.12f} V={subset} lambda={lam:.9f} "
                    f"z={z:.9f} cutoff={cutoff} d={states} rho={rejection}",
                    flush=True,
                )
    print("FINAL", best)


if __name__ == "__main__":
    main()
