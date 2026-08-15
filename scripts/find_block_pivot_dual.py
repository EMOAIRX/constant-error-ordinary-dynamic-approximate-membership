#!/usr/bin/env python3
"""Find a convex-dual witness for the equal-block pivot hierarchy."""

from __future__ import annotations

import argparse
import math

import numpy as np

from explore_block_pivot_hierarchy import constraints_for


def a_prime(x: float) -> float:
    return -1.0 / (x * math.log(2.0))


def b_prime(x: float) -> float:
    ratio = (2.0 - x) / (1.0 - x)
    return 0.5 * (ratio - math.log(ratio) - 1.0) / math.log(2.0)


def phi_da(a: float, c: float) -> float:
    ratio = (2.0 - a) / (c - a)
    return 0.5 * (ratio - math.log(ratio) - 1.0) / math.log(2.0)


def phi_dc(a: float, c: float) -> float:
    return -(1.0 - a / 2.0) / ((c - a) * math.log(2.0))


def jacobian(p: np.ndarray) -> np.ndarray:
    q = len(p)
    jac = np.zeros((q + 1, q))
    jac[0] = [a_prime(x) / q for x in p]
    for j in range(q - 1):
        row = j + 1
        for i in range(j):
            jac[row, i] = b_prime(p[i]) / q
        jac[row, j] = (
            b_prime(p[j]) + sum(phi_da(p[j], p[r]) for r in range(j + 1, q))
        ) / q
        for i in range(j + 1, q):
            jac[row, i] = phi_dc(p[j], p[i]) / q
    jac[q] = [b_prime(x) / q for x in p]
    return jac


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("values", nargs="+", type=float)
    args = parser.parse_args()
    p = np.asarray(args.values)
    jac = jacobian(p)
    system = np.r_[jac.T, np.ones((1, len(p) + 1))]
    rhs = np.r_[np.zeros(len(p)), 1.0]
    weights = np.linalg.solve(system, rhs)
    print("p=" + " ".join(f"{x:.15f}" for x in p))
    print("f=" + " ".join(f"{x:.15f}" for x in constraints_for(p)))
    print("lambda=" + " ".join(f"{x:.15f}" for x in weights))
    print("stationarity=" + " ".join(f"{x:.3e}" for x in weights @ jac))
    print(f"weighted_value={weights @ constraints_for(p):.15f}")


if __name__ == "__main__":
    main()
