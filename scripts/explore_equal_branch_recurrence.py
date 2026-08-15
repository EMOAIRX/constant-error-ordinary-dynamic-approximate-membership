#!/usr/bin/env python3
"""Explore the exact all-active branch recurrence using one-dimensional roots."""

from __future__ import annotations

import argparse
import math


def phi(a: float, c: float) -> float:
    return (1.0 - a / 2.0) * math.log2((2.0 - a) / (c - a))


def a_fn(x: float) -> float:
    return math.log2(2.0 / x)


def b_fn(x: float) -> float:
    return phi(x, 1.0)


def previous_point(tail: list[float]) -> float | None:
    current = tail[0]
    target = b_fn(current) + sum(phi(current, x) for x in tail[1:])

    def residual(previous: float) -> float:
        return sum(phi(previous, x) for x in tail) - target

    lo = 0.0
    hi = current * (1.0 - 1e-14)
    if residual(lo) > 0.0:
        return None
    for _ in range(70):
        mid = (lo + hi) / 2.0
        if residual(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def profile(blocks: int, last: float) -> list[float] | None:
    tail = [last]
    for _ in range(blocks - 1):
        previous = previous_point(tail)
        if previous is None:
            return None
        tail.insert(0, previous)
    return tail


def endpoint_residual(points: list[float]) -> float:
    return sum(a_fn(x) - b_fn(x) for x in points) / len(points)


def solve(blocks: int) -> tuple[list[float], float]:
    lo = 0.5
    hi = 1.0 - 1e-12
    # A failed backward recurrence means the last point is too small.
    for _ in range(80):
        mid = (lo + hi) / 2.0
        points = profile(blocks, mid)
        if points is None or endpoint_residual(points) > 0.0:
            lo = mid
        else:
            hi = mid
    points = profile(blocks, (lo + hi) / 2.0)
    assert points is not None
    rate = sum(a_fn(x) for x in points) / blocks
    return points, rate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blocks", type=int, default=32)
    parser.add_argument("--points", action="store_true")
    args = parser.parse_args()
    points, rate = solve(args.blocks)
    print(
        f"blocks={args.blocks} rate={rate:.15f} "
        f"endpoint_residual={endpoint_residual(points):.3e} "
        f"first={points[0]:.12g} last={points[-1]:.12g}"
    )
    if args.points:
        print(" ".join(f"{x:.12g}" for x in points))


if __name__ == "__main__":
    main()
