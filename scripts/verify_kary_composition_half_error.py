#!/usr/bin/env python3
"""Numerically audit the optimistic K-ary composition threshold relaxation."""

import math
import argparse


def rejection(k, q, lam):
    term = 1.0
    total = 0.0
    absence = 1.0 - 1.0 / k
    for c in range(q):
        if c:
            term *= lam / c
        total += term * absence**c
    return math.exp(-lam) * total


def half_error_root(k, q):
    hi = 1.0
    while rejection(k, q, hi) > 0.5:
        hi *= 2.0
    lo = 0.0
    for _ in range(120):
        mid = (lo + hi) / 2.0
        if rejection(k, q, mid) > 0.5:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def relaxed_rate(k, q):
    lam = half_error_root(k, q)
    tail_states = math.comb(q + k - 2, k - 1)

    def objective(log_z):
        z = math.exp(log_z)
        generating_function = sum(
            math.comb(c + k - 1, k - 1) * z**c for c in range(q)
        )
        generating_function += tail_states * z**q / (1.0 - z)
        return (
            math.log(generating_function, 2) / lam - log_z / math.log(2.0)
        )

    lo = -30.0
    hi = -1e-12
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    left = hi - ratio * (hi - lo)
    right = lo + ratio * (hi - lo)
    left_value = objective(left)
    right_value = objective(right)
    for _ in range(150):
        if left_value < right_value:
            hi, right, right_value = right, left, left_value
            left = hi - ratio * (hi - lo)
            left_value = objective(left)
        else:
            lo, left, left_value = left, right, right_value
            right = lo + ratio * (hi - lo)
            right_value = objective(right)
    return lam, objective((lo + hi) / 2.0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=100)
    parser.add_argument("--max-q", type=int, default=100)
    args = parser.parse_args()
    results = []
    for k in range(2, args.max_k + 1):
        for q in range(2, args.max_q + 1):
            lam, rate = relaxed_rate(k, q)
            results.append((rate, k, q, lam))
    for rate, k, q, lam in sorted(results)[:10]:
        print(f"K={k:2d} q={q:2d} lambda={lam:.12f} rate={rate:.12f}")


if __name__ == "__main__":
    main()
