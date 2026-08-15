#!/usr/bin/env python3
"""Numerical explorer for the KLZ all-pivot profile minimax."""

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


def phi(a: float, b: float, delta: float = 0.5) -> float:
    if b <= a:
        return 1e6
    y = 1.0 - delta * a
    return y * math.log2(y / (delta * (b - a)))


def pivots(x: np.ndarray, delta: float = 0.5) -> np.ndarray:
    b = len(x) - 1
    out = np.empty(b + 1)
    for s in range(b + 1):
        total = sum(phi(x[k - 1], x[b], delta) for k in range(1, s + 1))
        total += sum(phi(x[s], x[k], delta) for k in range(s + 1, b + 1))
        out[s] = total / b
    return out


def unpack(v: np.ndarray) -> np.ndarray:
    weights = np.exp(np.r_[v, 0.0] - np.max(np.r_[v, 0.0]))
    increments = weights / weights.sum()
    return np.r_[0.0, np.cumsum(increments)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, default=32)
    parser.add_argument("--restarts", type=int, default=8)
    args = parser.parse_args()
    rng = np.random.default_rng(20260813)
    best = None
    for rep in range(args.restarts):
        v0 = np.zeros(args.b - 1) if rep == 0 else rng.normal(scale=0.5, size=args.b - 1)
        x0 = unpack(v0)[1:-1]
        t0 = pivots(np.r_[0.0, x0, 1.0]).max() + 0.01

        def objective(z: np.ndarray) -> float:
            return z[-1]

        def constraints(z: np.ndarray) -> np.ndarray:
            x = np.r_[0.0, z[:-1], 1.0]
            return z[-1] - pivots(x)

        result = minimize(
            objective,
            np.r_[x0, t0],
            method="SLSQP",
            bounds=[(1e-8, 1.0 - 1e-8)] * (args.b - 1) + [(0.0, 10.0)],
            constraints={"type": "ineq", "fun": constraints},
            options={"maxiter": 5000, "ftol": 1e-12},
        )
        x = np.r_[0.0, np.sort(result.x[:-1]), 1.0]
        values = pivots(x)
        record = (values.max(), x, values, result)
        if best is None or record[0] < best[0]:
            best = record
    assert best is not None
    value, x, values, result = best
    print(f"b={args.b} success={result.success} max={value:.15f}")
    print("x=" + " ".join(f"{z:.10f}" for z in x))
    print("F=" + " ".join(f"{z:.10f}" for z in values))


if __name__ == "__main__":
    main()
