#!/usr/bin/env python3
"""Numerically optimize permanent-YES thinning of the mod-6 construction."""

import math

from explore_asymmetric_cross_block_lattices import exact_profile, rejection_profile


PROFILE = exact_profile(3, 3, 6)
RHO = rejection_profile(PROFILE, 3, 3, 6, 0.5)


def poisson_rejection(lam):
    term = math.exp(-lam)
    total = term * RHO[0]
    for load in range(1, len(RHO)):
        term *= lam / load
        total += term * RHO[load]
    return total


def calibrated_lambda(beta):
    target = 0.5 / beta
    left, right = 0.0, 10.0
    for _ in range(120):
        middle = (left + right) / 2
        if poisson_rejection(middle) > target:
            left = middle
        else:
            right = middle
    return (left + right) / 2


def generating_function(z):
    prefix = sum(PROFILE.states[c] * z**c for c in range(PROFILE.cutoff))
    return prefix + PROFILE.group_size * z**PROFILE.cutoff / (1 - z)


def mean_load(z):
    numerator = sum(c * PROFILE.states[c] * z**c for c in range(PROFILE.cutoff))
    numerator += PROFILE.group_size * (
        PROFILE.cutoff * z**PROFILE.cutoff / (1 - z)
        + z ** (PROFILE.cutoff + 1) / (1 - z) ** 2
    )
    return numerator / generating_function(z)


def rate(beta):
    lam = calibrated_lambda(beta)
    target_mean = lam / beta
    left, right = 1e-14, 1 - 1e-14
    for _ in range(120):
        middle = (left + right) / 2
        if mean_load(middle) < target_mean:
            left = middle
        else:
            right = middle
    z = (left + right) / 2
    # B/n=beta/lambda, while the fixed codebook must cover total load n.
    bits = beta * math.log2(generating_function(z)) / lam - math.log2(z)
    return bits, lam, z


def main():
    best = (float("inf"), None)
    for index in range(10001):
        beta = 0.5 + 0.5 * index / 10000
        result = rate(beta)
        if result[0] < best[0]:
            best = (result[0], (beta, *result[1:]))
    print("grid best", best)

    center = best[1][0]
    left, right = max(0.5, center - 0.001), min(1.0, center + 0.001)
    ratio = (math.sqrt(5) - 1) / 2
    c = right - ratio * (right - left)
    d = left + ratio * (right - left)
    fc, fd = rate(c)[0], rate(d)[0]
    for _ in range(100):
        if fc < fd:
            right, d, fd = d, c, fc
            c = right - ratio * (right - left)
            fc = rate(c)[0]
        else:
            left, c, fc = c, d, fd
            d = left + ratio * (right - left)
            fd = rate(d)[0]
    beta = (left + right) / 2
    print("refined", beta, rate(beta))
    print("endpoint", 1.0, rate(1.0))


if __name__ == "__main__":
    main()
