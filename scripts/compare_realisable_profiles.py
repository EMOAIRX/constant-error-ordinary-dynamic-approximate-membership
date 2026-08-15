#!/usr/bin/env python3
"""Compare all-pivot optimizer averages with realizable fingerprint profiles."""

from __future__ import annotations

import math

from explore_block_pivot_hierarchy import constraints_for


LAMBDA_THRESHOLD = 1.325819075285
LAMBDA_EXACT = math.log(2.0)


def threshold_x(t: float) -> float:
    y = LAMBDA_THRESHOLD * t
    return 2.0 * (1.0 - math.exp(-y) * (1.0 + y / 2.0 + y * y / 8.0))


def exact_x(t: float) -> float:
    return 2.0 * (1.0 - math.exp(-LAMBDA_EXACT * t))


def block_averages(fn, q: int, samples: int = 100000) -> list[float]:
    out = []
    per = samples // q
    for block in range(q):
        total = 0.0
        for j in range(per):
            t = (block + (j + 0.5) / per) / q
            total += fn(t)
        out.append(total / per)
    return out


def report(name: str, fn, q: int) -> None:
    p = block_averages(fn, q)
    values = constraints_for(p)
    print(name)
    print("p=" + " ".join(f"{x:.12f}" for x in p))
    print("F=" + " ".join(f"{x:.12f}" for x in values))
    print(f"max={values.max():.12f} min={values.min():.12f}")


def main() -> None:
    report("threshold-L2", threshold_x, 10)
    report("exact-fingerprint", exact_x, 10)


if __name__ == "__main__":
    main()
