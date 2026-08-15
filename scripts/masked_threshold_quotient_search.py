"""Optimize permanent-YES mass combined with algebraic threshold blocks."""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import differential_evolution, minimize
from scipy.special import gammaincc


def conditional_rejection(modulus: int, load: float, bias: float) -> float:
    return (
        bias
        * math.exp(-load * bias)
        * gammaincc(modulus, load * (1.0 - bias))
        + (1.0 - bias)
        * math.exp(-load * (1.0 - bias))
        * gammaincc(modulus, load * bias)
    )


def state_rate(modulus: int, block_ratio: float) -> float:
    """Worst-case fixed-state rate for B/n=block_ratio."""
    state_load = 1.0 / block_ratio

    def mean(z: float) -> float:
        return 2.0 * z / (1.0 - z) - (
            modulus * z**modulus / (1.0 - z**modulus)
        )

    from scipy.optimize import brentq

    z = brentq(lambda value: mean(value) - state_load, 1e-14, 1.0 - 1e-14)
    log_a = math.log1p(-z**modulus) - 2.0 * math.log1p(-z)
    return (block_ratio * log_a - math.log(z)) / math.log(2.0)


def parameters_from_coordinates(
    coordinates: np.ndarray, target_rejection: float
) -> tuple[float, float]:
    tracked_mass = target_rejection + (1.0 - target_rejection) / (
        1.0 + math.exp(-coordinates[0])
    )
    bias = 0.5 / (1.0 + math.exp(-coordinates[1]))
    return tracked_mass, bias


def objective(
    coordinates: np.ndarray, modulus: int, target_rejection: float
) -> float:
    tracked_mass, bias = parameters_from_coordinates(coordinates, target_rejection)
    required = target_rejection / tracked_mass

    from scipy.optimize import brentq

    upper = max(1.0, -math.log(required) / max(bias, 1e-12))
    while conditional_rejection(modulus, upper, bias) > required:
        upper *= 2.0
    try:
        load = brentq(
            lambda value: conditional_rejection(modulus, value, bias) - required,
            0.0,
            upper,
        )
    except ValueError:
        return 1e6
    block_ratio = tracked_mass / load
    return state_rate(modulus, block_ratio)


def optimized_rate(modulus: int, epsilon: float) -> tuple[float, float, float, float]:
    target = 1.0 - epsilon
    result = differential_evolution(
        lambda coordinates: objective(coordinates, modulus, target),
        bounds=((-14.0, 14.0), (-14.0, 14.0)),
        seed=modulus,
        tol=1e-10,
        polish=False,
    )
    result = minimize(
        lambda coordinates: objective(coordinates, modulus, target),
        result.x,
        method="Nelder-Mead",
        options={"xatol": 1e-11, "fatol": 1e-12},
    )
    tracked_mass, bias = parameters_from_coordinates(result.x, target)
    required = target / tracked_mass
    from scipy.optimize import brentq

    upper = max(1.0, -math.log(required) / bias)
    while conditional_rejection(modulus, upper, bias) > required:
        upper *= 2.0
    load = brentq(
        lambda value: conditional_rejection(modulus, value, bias) - required,
        0.0,
        upper,
    )
    return result.fun, tracked_mass, bias, tracked_mass / load


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=20)
    args = parser.parse_args()
    for epsilon in (0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.95, 0.99):
        rows = [
            (optimized_rate(modulus, epsilon)[0], modulus, *optimized_rate(modulus, epsilon)[1:])
            for modulus in range(2, args.max_modulus + 1)
        ]
        rate, modulus, tracked_mass, bias, block_ratio = min(rows)
        print(
            f"epsilon={epsilon:g} R={rate:.12g} q={modulus} "
            f"tracked={tracked_mass:.12g} p={bias:.12g} B/n={block_ratio:.12g}"
        )


if __name__ == "__main__":
    main()
