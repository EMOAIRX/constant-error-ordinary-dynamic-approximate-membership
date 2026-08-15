#!/usr/bin/env python3
"""Numerical explorer for the occupancy source-coding reliability curve.

The model has q = c n identical tracked cells of load lambda and one
permanent-positive category of mass beta = 1-c*lambda.  For a candidate
empirical occupancy law mu on the tracked cells,

    A(mu) = c H(mu)
    I(mu) = c D(mu || Pois(lambda))
            + D_Pois(1-c E_mu[K] || beta).

The inverse fixed-length reliability function is

    R_b(c, lambda) = sup { A(mu) : I(mu) <= b }.

Pareto-optimal mu are Conway--Maxwell--Poisson laws
proportional to x^k/(k!)^a, 0 <= a <= 1.  This script scans that two-parameter
family using only the Python standard library.  It is an explorer, not a
computer-assisted proof.
"""

from __future__ import annotations

import argparse
import math


LN2 = math.log(2.0)


def logsumexp(values: list[float]) -> float:
    top = max(values)
    return top + math.log(sum(math.exp(v - top) for v in values))


def cmp_law(a: float, mean: float, cutoff: int) -> list[float]:
    if mean == 0.0:
        return [1.0] + [0.0] * cutoff
    if a == 0.0:
        x = mean / (1.0 + mean)
        probabilities = [(1.0 - x) * x**k for k in range(cutoff + 1)]
        probabilities[-1] += 1.0 - sum(probabilities)
        return probabilities

    def law(log_x: float) -> tuple[list[float], float]:
        logs = [k * log_x - a * math.lgamma(k + 1.0) for k in range(cutoff + 1)]
        normalizer = logsumexp(logs)
        probabilities = [math.exp(v - normalizer) for v in logs]
        return probabilities, sum(k * p for k, p in enumerate(probabilities))

    low, high = -40.0, 40.0
    for _ in range(100):
        middle = (low + high) / 2.0
        _, current_mean = law(middle)
        if current_mean < mean:
            low = middle
        else:
            high = middle
    return law((low + high) / 2.0)[0]


def entropy_bits(probabilities: list[float]) -> float:
    return -sum(p * math.log2(p) for p in probabilities if p > 0.0)


def poisson_divergence_bits(probabilities: list[float], lam: float) -> float:
    answer = 0.0
    for k, p in enumerate(probabilities):
        if p == 0.0:
            continue
        log_poisson = -lam + k * math.log(lam) - math.lgamma(k + 1.0)
        answer += p * (math.log(p) - log_poisson) / LN2
    return answer


def scalar_poisson_divergence_bits(value: float, mean: float) -> float:
    if mean == 0.0:
        return 0.0 if abs(value) < 1e-12 else math.inf
    if value == 0.0:
        return mean / LN2
    return (value * math.log(value / mean) - value + mean) / LN2


def design_rate(
    eps: float,
    lam: float,
    exponent: float,
    a_steps: int,
    mean_steps: int,
    cutoff: int,
) -> tuple[float, float, float]:
    survival = 1.0 - eps
    c = survival * math.exp(lam) / lam
    beta = 1.0 - c * lam
    if beta < -1e-10:
        return math.inf, c, beta
    beta = max(0.0, beta)

    best = -math.inf
    best_i = math.nan
    max_mean = 1.0 / c
    if beta == 0.0:
        means = [max_mean]
    else:
        means = [max_mean * j / mean_steps for j in range(mean_steps + 1)]

    for ai in range(a_steps + 1):
        a = ai / a_steps
        for mean in means:
            probabilities = cmp_law(a, mean, cutoff)
            tracked_divergence = c * poisson_divergence_bits(probabilities, lam)
            top_value = max(0.0, 1.0 - c * mean)
            information = tracked_divergence + scalar_poisson_divergence_bits(
                top_value, beta
            )
            if information <= exponent + 1e-9:
                rate = c * entropy_bits(probabilities)
                if rate > best:
                    best = rate
                    best_i = information
    return best, c, best_i


def optimize(
    eps: float,
    exponent: float,
    lambda_steps: int,
    a_steps: int,
    mean_steps: int,
    cutoff: int,
) -> None:
    lambda_limit = -math.log(1.0 - eps)
    candidates = [lambda_limit * (j + 1) / lambda_steps for j in range(lambda_steps)]
    best = (math.inf, math.nan, math.nan, math.nan)
    for lam in candidates:
        rate, c, used_exponent = design_rate(
            eps, lam, exponent, a_steps, mean_steps, cutoff
        )
        if rate < best[0]:
            best = rate, lam, c, used_exponent
    rate, lam, c, used_exponent = best
    print(
        f"epsilon={eps:.8g} b={exponent:.8g} "
        f"rate={rate:.9f} lambda={lam:.9f} c={c:.9f} "
        f"I={used_exponent:.9f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon", type=float, default=0.5)
    parser.add_argument("--exponent", type=float, default=0.1)
    parser.add_argument("--lambda-steps", type=int, default=100)
    parser.add_argument("--a-steps", type=int, default=80)
    parser.add_argument("--mean-steps", type=int, default=100)
    parser.add_argument("--cutoff", type=int, default=160)
    args = parser.parse_args()
    optimize(
        args.epsilon,
        args.exponent,
        args.lambda_steps,
        args.a_steps,
        args.mean_steps,
        args.cutoff,
    )


if __name__ == "__main__":
    main()
