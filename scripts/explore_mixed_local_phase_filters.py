#!/usr/bin/env python3
"""Numerically optimize mixtures of canonical local filter types.

Each type t has state OGF A_t(z) and Poisson rejection J_t(lambda).  A key is
routed to type t with probability alpha_t and then uniformly to B_t blocks.
Writing x_t=B_t/n, the local mean is lambda_t=alpha_t/x_t.  The global
fixed-state OGF is prod_t A_t(z)^(B_t), so the per-key rate is

    sum_t x_t log2 A_t(z) - log2 z,

where z enforces the global capacity saddle.  Rejection is
sum_t alpha_t J_t(lambda_t).
"""

from __future__ import annotations

import math
import random

from explore_asymmetric_cross_block_lattices import exact_profile, rejection_profile


def profile_mod6():
    profile = exact_profile(3, 3, 6)
    rejection = rejection_profile(profile, 3, 3, 6, 0.5)
    return profile.states, profile.cutoff, profile.group_size, rejection


def profile_binary(q):
    states = tuple(range(1, q + 1)) + (q,)
    rejection = tuple(2.0 ** (-c) for c in range(q)) + (0.0,)
    return states, q, q, rejection


def ogf(z, kind):
    states, cutoff, tail, _ = kind
    return sum(states[c] * z**c for c in range(cutoff)) + tail * z**cutoff / (1 - z)


def mean(z, kind):
    states, cutoff, tail, _ = kind
    numerator = sum(c * states[c] * z**c for c in range(cutoff))
    numerator += tail * (
        cutoff * z**cutoff / (1 - z) + z ** (cutoff + 1) / (1 - z) ** 2
    )
    return numerator / ogf(z, kind)


def rejection(lam, kind):
    values = kind[3]
    term = math.exp(-lam)
    result = term * values[0]
    for c in range(1, len(values)):
        term *= lam / c
        result += term * values[c]
    return result


def evaluate(alpha, lambda_a, lambda_b, kind_a, kind_b):
    if not 0 < alpha < 1 or lambda_a <= 0 or lambda_b <= 0:
        return float("inf"), None
    x_a = alpha / lambda_a
    x_b = (1 - alpha) / lambda_b
    total_rejection = alpha * rejection(lambda_a, kind_a) + (1 - alpha) * rejection(lambda_b, kind_b)
    if total_rejection < 0.5:
        return float("inf"), None

    left, right = 1e-12, 1 - 1e-12
    for _ in range(100):
        z = (left + right) / 2
        if x_a * mean(z, kind_a) + x_b * mean(z, kind_b) < 1:
            left = z
        else:
            right = z
    z = (left + right) / 2
    rate = x_a * math.log2(ogf(z, kind_a)) + x_b * math.log2(ogf(z, kind_b)) - math.log2(z)
    return rate, (alpha, lambda_a, lambda_b, total_rejection, z, x_a, x_b)


def search(kind_a, kind_b, restarts=100, steps=5000, seed=0):
    rng = random.Random(seed)
    best = (float("inf"), None)
    for _ in range(restarts):
        point = [rng.uniform(0.02, 0.98), rng.uniform(0.1, 8), rng.uniform(0.1, 8)]
        score, data = evaluate(*point, kind_a, kind_b)
        temperature = 0.1
        scale = [0.1, 0.5, 0.5]
        for step in range(steps):
            candidate = [
                point[i] + rng.gauss(0, scale[i] * max(0.02, temperature))
                for i in range(3)
            ]
            candidate[0] = min(0.999999, max(0.000001, candidate[0]))
            candidate[1] = min(20, max(0.001, candidate[1]))
            candidate[2] = min(20, max(0.001, candidate[2]))
            candidate_score, candidate_data = evaluate(*candidate, kind_a, kind_b)
            delta = candidate_score - score
            if delta <= 0 or rng.random() < math.exp(-min(delta, 100) / max(temperature, 1e-6)):
                point, score, data = candidate, candidate_score, candidate_data
            temperature *= 0.999
            if score < best[0]:
                best = score, data
                print("BEST", best, flush=True)
    return best


def main():
    kinds = {"mod6": profile_mod6()}
    for q in range(2, 9):
        kinds[f"bin{q}"] = profile_binary(q)
    for name in ["bin2", "bin3", "bin4", "bin5", "bin6", "bin7", "bin8"]:
        print("PAIR mod6", name)
        print(search(kinds["mod6"], kinds[name], restarts=15, steps=1500, seed=17))


if __name__ == "__main__":
    main()
