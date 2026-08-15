#!/usr/bin/env python3
"""Explore masked binary threshold branches versus the coordinate branch.

This is a floating-point explorer, not an interval certificate.  It uses only
the Python standard library so that the phase comparisons are reproducible in
the current workspace.
"""

from __future__ import annotations

import argparse
import math


def psi(block_ratio: float) -> float:
    if block_ratio == 0.0:
        return 0.0
    return (1.0 + block_ratio) * math.log2(1.0 + block_ratio) - block_ratio * math.log2(block_ratio)


def coordinate_branch(delta: float) -> tuple[float, float, float]:
    """Return rate, effective tracked mass, and Poisson load."""
    if delta <= math.exp(-1.0):
        load = 1.0
        tracked_mass = math.e * delta
    else:
        load = math.log(1.0 / delta)
        tracked_mass = 1.0
    block_ratio = tracked_mass / load
    return psi(block_ratio), tracked_mass, load


def rejection(modulus: int, load: float, bias: float) -> float:
    total = 0.0
    factorial = 1.0
    load_power = 1.0
    for count in range(modulus):
        if count:
            factorial *= count
            load_power *= load
        absence = bias * (1.0 - bias) ** count + (1.0 - bias) * bias**count
        total += load_power * absence / factorial
    return math.exp(-load) * total


def state_rate(modulus: int, block_ratio: float) -> float:
    def mean(z: float) -> float:
        return 2.0 * z / (1.0 - z) - modulus * z**modulus / (1.0 - z**modulus)

    target = 1.0 / block_ratio
    low, high = 0.0, 1.0
    for _ in range(100):
        middle = (low + high) / 2.0
        if mean(middle) < target:
            low = middle
        else:
            high = middle
    z = (low + high) / 2.0
    log_a = math.log1p(-(z**modulus)) - 2.0 * math.log1p(-z)
    return (block_ratio * log_a - math.log(z)) / math.log(2.0)


def feasible_load_limit(modulus: int, bias: float, delta: float) -> float:
    low, high = 0.0, 1.0
    while rejection(modulus, high, bias) > delta:
        high *= 2.0
    for _ in range(100):
        middle = (low + high) / 2.0
        if rejection(modulus, middle, bias) > delta:
            low = middle
        else:
            high = middle
    return (low + high) / 2.0


def golden_maximum(function, low: float, high: float) -> tuple[float, float]:
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    left = high - ratio * (high - low)
    right = low + ratio * (high - low)
    f_left, f_right = function(left), function(right)
    for _ in range(100):
        if f_left < f_right:
            low, left, f_left = left, right, f_right
            right = low + ratio * (high - low)
            f_right = function(right)
        else:
            high, right, f_right = right, left, f_left
            left = high - ratio * (high - low)
            f_left = function(left)
    point = (low + high) / 2.0
    return point, function(point)


def threshold_branch(modulus: int, bias: float, delta: float) -> tuple[float, float, float, float]:
    limit = feasible_load_limit(modulus, bias, delta)
    load, efficiency = golden_maximum(
        lambda value: value * rejection(modulus, value, bias), 1e-15, limit
    )
    conditional_rejection = rejection(modulus, load, bias)
    tracked_mass = delta / conditional_rejection
    block_ratio = delta / efficiency
    return state_rate(modulus, block_ratio), tracked_mass, load, block_ratio


def optimize_bias(modulus: int, delta: float, bias_steps: int) -> tuple[float, float, float, float, float]:
    best = (math.inf, math.nan, math.nan, math.nan, math.nan)
    # Endpoints have a smaller reachable-state OGF and belong to the unary
    # branch.  Scan strictly positive fixed biases here.
    for step in range(1, bias_steps + 1):
        bias = 0.5 * step / bias_steps
        rate, tracked_mass, load, block_ratio = threshold_branch(modulus, bias, delta)
        candidate = rate, bias, tracked_mass, load, block_ratio
        if candidate < best:
            best = candidate
    return best


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon", type=float, nargs="*", default=[0.01, 0.1, 0.25, 0.5, 0.6, 0.75, 0.9, 0.99])
    parser.add_argument("--max-modulus", type=int, default=16)
    parser.add_argument("--bias-steps", type=int, default=160)
    args = parser.parse_args()

    for epsilon in args.epsilon:
        delta = 1.0 - epsilon
        coordinate_rate, coordinate_mass, coordinate_load = coordinate_branch(delta)
        best = (math.inf, 0, math.nan, math.nan, math.nan, math.nan)
        for modulus in range(2, args.max_modulus + 1):
            rate, bias, tracked_mass, load, block_ratio = optimize_bias(
                modulus, delta, args.bias_steps
            )
            candidate = rate, modulus, bias, tracked_mass, load, block_ratio
            if candidate < best:
                best = candidate
        rate, modulus, bias, tracked_mass, load, block_ratio = best
        print(
            f"eps={epsilon:.9g} delta={delta:.9g} "
            f"coordinate={coordinate_rate:.12f} theta={coordinate_mass:.9g} mu={coordinate_load:.9g} "
            f"threshold={rate:.12f} q={modulus} p={bias:.9g} "
            f"beta={tracked_mass:.9g} lambda={load:.9g} b={block_ratio:.9g} "
            f"gap={coordinate_rate-rate:.12f}"
        )


if __name__ == "__main__":
    main()
