#!/usr/bin/env python3
"""Recompute the half-error endpoint-batch min--max constant."""

from __future__ import annotations

import math


DELTA = 0.5


def a_value(x: float) -> float:
    return math.log2(1.0 / (DELTA * x))


def b_value(x: float) -> float:
    y = 1.0 - DELTA * x
    return y * math.log2(y / (DELTA * (1.0 - x)))


def main() -> None:
    lo, hi = 0.5, 0.9
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if a_value(mid) > b_value(mid):
            lo = mid
        else:
            hi = mid

    root = (lo + hi) / 2.0
    a = a_value(root)
    b = b_value(root)

    assert abs(a - b) < 1e-12
    assert abs(root - 0.739998185722401) < 1e-12
    assert abs(a - 1.434406361243753) < 1e-12

    print(f"x_star = {root:.15f}")
    print(f"A(x_star) = {a:.15f}")
    print(f"B(x_star) = {b:.15f}")


if __name__ == "__main__":
    main()
