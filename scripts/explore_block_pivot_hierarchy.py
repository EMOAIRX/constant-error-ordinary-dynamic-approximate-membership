#!/usr/bin/env python3
"""Numerically explore the equal-block all-pivot convex hierarchy."""

from __future__ import annotations

import argparse
import math
import os
import sys

import numpy as np

EXTRA = "/private/tmp/dynamic-amq-scipy"
if os.path.isdir(EXTRA):
    sys.path.insert(0, EXTRA)
from scipy.optimize import minimize


def phi(a: float, c: float) -> float:
    if c <= a:
        return 1e8
    return (1.0 - a / 2.0) * math.log2((2.0 - a) / (c - a))


def a_fn(x: float) -> float:
    return math.log2(2.0 / x)


def b_fn(x: float) -> float:
    return (1.0 - x / 2.0) * math.log2((2.0 - x) / (1.0 - x))


def constraints_for(p: np.ndarray) -> np.ndarray:
    q = len(p)
    out = [sum(a_fn(x) for x in p) / q]
    for j in range(q - 1):
        value = sum(b_fn(p[r]) for r in range(j + 1))
        value += sum(phi(p[j], p[r]) for r in range(j + 1, q))
        out.append(value / q)
    out.append(sum(b_fn(x) for x in p) / q)
    return np.asarray(out)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blocks", type=int, default=4)
    parser.add_argument("--restarts", type=int, default=20)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    q = args.blocks
    rng = np.random.default_rng(20260813)
    best = None

    for rep in range(args.restarts):
        p0 = np.linspace(0.2, 0.9, q)
        if rep:
            p0 = np.sort(rng.uniform(0.05, 0.95, q))
        t0 = constraints_for(p0).max() + 0.1

        def objective(z: np.ndarray) -> float:
            return z[-1]

        def feasible(z: np.ndarray) -> np.ndarray:
            p = z[:-1]
            ordering = np.diff(p)
            epigraph = z[-1] - constraints_for(p)
            return np.r_[ordering, epigraph]

        result = minimize(
            objective,
            np.r_[p0, t0],
            method="SLSQP",
            bounds=[(1e-8, 1.0 - 1e-8)] * q + [(0.0, 10.0)],
            constraints={"type": "ineq", "fun": feasible},
            options={"maxiter": 10000, "ftol": 1e-13},
        )
        p = result.x[:-1]
        values = constraints_for(p)
        record = (values.max(), p, values, result.success)
        if best is None or record[0] < best[0]:
            best = record

    assert best is not None
    value, p, values, success = best
    print(f"blocks={q} success={success} max={value:.15f}")
    if args.summary:
        print(f"spread={values.max() - values.min():.3e}")
        return
    print("p=" + " ".join(f"{x:.12f}" for x in p))
    print("F=" + " ".join(f"{x:.12f}" for x in values))


if __name__ == "__main__":
    main()
