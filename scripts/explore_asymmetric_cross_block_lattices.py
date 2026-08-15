#!/usr/bin/env python3
"""Explore asymmetric two-subblock additive filters.

The local state is

    (c, (a0 + a1) mod Q, a1 mod q_a, b1 mod q_b).

Symbols A0,A1 have probability alpha/2 each and B0,B1 have probability
(1-alpha)/2 each.  State and support profiles are exact; rates are numerical.
"""

from __future__ import annotations

import argparse
import math
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class Profile:
    states: tuple[int, ...]
    support_masks: tuple[dict[tuple[int, int, int], int], ...]
    cutoff: int
    group_size: int


def add(state, increment, q_a, q_b, modulus):
    return (
        (state[0] + increment[0]) % modulus,
        (state[1] + increment[1]) % q_a,
        (state[2] + increment[2]) % q_b,
    )


@lru_cache(maxsize=None)
def exact_profile(q_a: int, q_b: int, modulus: int) -> Profile:
    increments = ((1, 0, 0), (1, 1, 0), (0, 0, 0), (0, 0, 1))
    zero = (0, 0, 0)
    masks = {zero: 0}
    layers = []
    states = []
    full_mask = 15
    group_size = q_a * q_b * modulus

    # A finite Cayley graph reaches its eventual support within group_size
    # steps; another group_size steps suffice for full symbol witnesses.
    for load in range(2 * group_size + 1):
        layers.append(masks)
        states.append(len(masks))
        if len(masks) == group_size and all(mask == full_mask for mask in masks.values()):
            return Profile(tuple(states), tuple(layers), load, group_size)

        next_masks = defaultdict(int)
        for state, mask in masks.items():
            for symbol, increment in enumerate(increments):
                target = add(state, increment, q_a, q_b, modulus)
                next_masks[target] |= mask | (1 << symbol)
        masks = dict(next_masks)
    raise AssertionError("profile did not stabilize")


def rejection_profile(profile: Profile, q_a: int, q_b: int, modulus: int, alpha: float):
    increments = ((1, 0, 0), (1, 1, 0), (0, 0, 0), (0, 0, 1))
    symbol_probabilities = (alpha / 2, alpha / 2, (1 - alpha) / 2, (1 - alpha) / 2)
    mass = {(0, 0, 0): 1.0}
    result = []
    for load in range(profile.cutoff + 1):
        rejected = 0.0
        masks = profile.support_masks[load]
        for state, probability in mass.items():
            mask = masks[state]
            rejected += probability * sum(
                symbol_probabilities[symbol]
                for symbol in range(4)
                if not mask & (1 << symbol)
            )
        result.append(rejected)
        if load == profile.cutoff:
            break
        next_mass = defaultdict(float)
        for state, probability in mass.items():
            for symbol, increment in enumerate(increments):
                target = add(state, increment, q_a, q_b, modulus)
                next_mass[target] += probability * symbol_probabilities[symbol]
        mass = dict(next_mass)
    return result


def poisson_rejection(lam, rejections):
    term = math.exp(-lam)
    total = term * rejections[0]
    for load in range(1, len(rejections)):
        term *= lam / load
        total += term * rejections[load]
    return total


def calibrate_lambda(rejections):
    left, right = 0.0, 1.0
    while poisson_rejection(right, rejections) > 0.5:
        right *= 2
    for _ in range(100):
        middle = (left + right) / 2
        if poisson_rejection(middle, rejections) > 0.5:
            left = middle
        else:
            right = middle
    return (left + right) / 2


def generating_function(z, profile):
    prefix = sum(profile.states[c] * z**c for c in range(profile.cutoff))
    return prefix + profile.group_size * z**profile.cutoff / (1 - z)


def mean_load(z, profile):
    numerator = sum(c * profile.states[c] * z**c for c in range(profile.cutoff))
    numerator += profile.group_size * (
        profile.cutoff * z**profile.cutoff / (1 - z)
        + z ** (profile.cutoff + 1) / (1 - z) ** 2
    )
    return numerator / generating_function(z, profile)


def rate_for(profile, lam):
    left, right = 1e-14, 1 - 1e-14
    for _ in range(100):
        middle = (left + right) / 2
        if mean_load(middle, profile) < lam:
            left = middle
        else:
            right = middle
    saddle = (left + right) / 2
    rate = math.log2(generating_function(saddle, profile)) / lam - math.log2(saddle)
    return rate, saddle


def evaluate(q_a, q_b, modulus, alpha):
    profile = exact_profile(q_a, q_b, modulus)
    rejections = rejection_profile(profile, q_a, q_b, modulus, alpha)
    lam = calibrate_lambda(rejections)
    rate, saddle = rate_for(profile, lam)
    return rate, lam, saddle, profile


def optimize_alpha(q_a, q_b, modulus):
    # The objective need not be convex globally, so locate a basin on a grid
    # before applying golden-section search.
    grid = [0.02 + 0.96 * index / 96 for index in range(97)]
    values = [(evaluate(q_a, q_b, modulus, alpha)[0], alpha) for alpha in grid]
    _, center = min(values)
    left = max(0.001, center - 0.02)
    right = min(0.999, center + 0.02)
    ratio = (math.sqrt(5) - 1) / 2
    c = right - ratio * (right - left)
    d = left + ratio * (right - left)
    fc = evaluate(q_a, q_b, modulus, c)[0]
    fd = evaluate(q_a, q_b, modulus, d)[0]
    for _ in range(60):
        if fc < fd:
            right, d, fd = d, c, fc
            c = right - ratio * (right - left)
            fc = evaluate(q_a, q_b, modulus, c)[0]
        else:
            left, c, fc = c, d, fd
            d = left + ratio * (right - left)
            fd = evaluate(q_a, q_b, modulus, d)[0]
    alpha = (left + right) / 2
    return alpha, evaluate(q_a, q_b, modulus, alpha)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=7)
    parser.add_argument("--max-modulus", type=int, default=16)
    parser.add_argument("--top", type=int, default=30)
    args = parser.parse_args()

    candidates = []
    for q_a in range(1, args.max_q + 1):
        for q_b in range(q_a, args.max_q + 1):
            for modulus in range(1, args.max_modulus + 1):
                alpha, result = optimize_alpha(q_a, q_b, modulus)
                rate, lam, saddle, profile = result
                candidates.append((rate, q_a, q_b, modulus, alpha, lam, saddle, profile.cutoff))
    for candidate in sorted(candidates)[: args.top]:
        rate, q_a, q_b, modulus, alpha, lam, saddle, cutoff = candidate
        print(
            f"R={rate:.12f} qA={q_a} qB={q_b} Q={modulus} "
            f"alpha={alpha:.9f} lambda={lam:.9f} z={saddle:.9f} cutoff={cutoff}"
        )


if __name__ == "__main__":
    main()
