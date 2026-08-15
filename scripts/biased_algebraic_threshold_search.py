"""Optimize binary algebraic threshold quotients over the inner-bit bias."""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.special import gammaincc


def rejection_probability(modulus: int, load: float, bias: float) -> float:
    """Poisson-limit probability that a fresh nonmember is rejected."""
    rare_query = (
        bias
        * math.exp(-load * bias)
        * gammaincc(modulus, load * (1.0 - bias))
    )
    common_query = (
        (1.0 - bias)
        * math.exp(-load * (1.0 - bias))
        * gammaincc(modulus, load * bias)
    )
    return rare_query + common_query


def calibrated_load(modulus: int, epsilon: float, bias: float) -> float:
    target = 1.0 - epsilon
    upper = max(1.0, -2.0 * math.log(target) + modulus)
    while rejection_probability(modulus, upper, bias) > target:
        upper *= 2.0
    return brentq(
        lambda load: rejection_probability(modulus, load, bias) - target,
        0.0,
        upper,
    )


def saddle(modulus: int, load: float) -> float:
    def mean(z: float) -> float:
        return 2.0 * z / (1.0 - z) - (
            modulus * z**modulus / (1.0 - z**modulus)
        )

    return brentq(lambda z: mean(z) - load, 1e-14, 1.0 - 1e-14)


def rate(modulus: int, epsilon: float, bias: float) -> tuple[float, float, float]:
    load = calibrated_load(modulus, epsilon, bias)
    z = saddle(modulus, load)
    log_generating_function = math.log1p(-z**modulus) - 2.0 * math.log1p(-z)
    value = (log_generating_function / load - math.log(z)) / math.log(2.0)
    return value, load, z


def optimized_rate(modulus: int, epsilon: float) -> tuple[float, float, float, float]:
    result = minimize_scalar(
        lambda bias: rate(modulus, epsilon, bias)[0],
        bounds=(1e-10, 0.5),
        method="bounded",
        options={"xatol": 1e-13},
    )
    value, load, z = rate(modulus, epsilon, result.x)
    return value, result.x, load, z


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=40)
    args = parser.parse_args()
    for epsilon in (0.01, 0.1, 0.5, 0.7, 0.9, 0.99, 0.999, 0.9999):
        rows = [
            (optimized_rate(modulus, epsilon)[0], modulus, *optimized_rate(modulus, epsilon)[1:])
            for modulus in range(2, args.max_modulus + 1)
        ]
        value, modulus, bias, load, z = min(rows)
        uniform = min(
            (rate(candidate, epsilon, 0.5)[0], candidate)
            for candidate in range(2, args.max_modulus + 1)
        )
        print(
            f"epsilon={epsilon:g} q={modulus} p={bias:.12g} "
            f"lambda={load:.12g} z={z:.12g} R={value:.12g} "
            f"uniform_q={uniform[1]} uniform_R={uniform[0]:.12g} "
            f"gain={uniform[0] - value:.12g}"
        )


if __name__ == "__main__":
    main()
