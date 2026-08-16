#!/usr/bin/env python3
"""Numerical checks for the half-error multicut lower bound.

The finite two-segment check is the reviewer-safe certificate.  The midpoint
integral computation is a high-resolution check of the continuous fixed point;
the theorem itself defines that coefficient by its integral equation.
"""

from decimal import Decimal, getcontext
import math


getcontext().prec = 80


def decimal_log2(x: Decimal) -> Decimal:
    return x.ln() / Decimal(2).ln()


def decimal_power_two(x: Decimal) -> Decimal:
    return (x * Decimal(2).ln()).exp()


def decimal_f_half(b: Decimal) -> Decimal:
    one = Decimal(1)
    half = Decimal(1) / 2
    return (one - b) * decimal_log2((one - b) / (half - b))


def verify_two_segment_certificate() -> None:
    h = Decimal("1.134")
    c0 = Decimal(7) / Decimal(12)
    c1 = Decimal(5) / Decimal(6)
    b0 = decimal_power_two(-h / c0)
    b1 = decimal_power_two(-h / c1)
    lhs = h - c0
    rhs = (c1 - c0) * decimal_f_half(b0) + (Decimal(1) - c1) * decimal_f_half(b1)
    gap = rhs - lhs

    assert gap > Decimal("0.00064"), gap

    print("two-segment rational certificate")
    print(f"  beta_0 = {b0}")
    print(f"  beta_1 = {b1}")
    print(f"  lhs    = {lhs}")
    print(f"  rhs    = {rhs}")
    print(f"  gap    = {gap}")


def f_half_float(b: float) -> float:
    return (1.0 - b) * math.log2((1.0 - b) / (0.5 - b))


def midpoint_integral(h: float, intervals: int) -> float:
    total = 0.0
    inverse = 1.0 / intervals
    for index in range(intervals):
        c = (index + 0.5) * inverse
        total += f_half_float(2.0 ** (-h / c))
    return total * inverse


def decimal_integrand_half(h: Decimal, c: Decimal) -> Decimal:
    if not c:
        return Decimal(1)
    return decimal_f_half(decimal_power_two(-h / c))


def verify_rounded_integral_certificate() -> None:
    h = Decimal("1.198")
    intervals = 5_000
    width = Decimal(1) / intervals
    lower_sum = sum(
        decimal_integrand_half(h, Decimal(index) * width)
        for index in range(intervals)
    ) * width
    gap = lower_sum - h

    # The integrand is increasing in c, so this left Riemann sum is a lower
    # bound for the integral.  Its positive margin certifies h_{1/2} > 1.198.
    assert lower_sum > Decimal("1.19807"), lower_sum
    assert gap > Decimal("0.00007"), gap

    print("rounded integral certificate")
    print(f"  left sum = {lower_sum}")
    print(f"  gap      = {gap}")


def continuous_fixed_point() -> None:
    intervals = 400_000
    low = 1.19
    high = 1.21
    for _ in range(55):
        middle = (low + high) / 2.0
        if midpoint_integral(middle, intervals) > middle:
            low = middle
        else:
            high = middle
    root = (low + high) / 2.0
    residual = midpoint_integral(root, 800_000) - root

    assert 1.19809 < root < 1.19811, root
    assert abs(residual) < 2e-10, residual

    print("continuous fixed-point check")
    print(f"  root     = {root:.15f}")
    print(f"  residual = {residual:.3e}")


if __name__ == "__main__":
    verify_two_segment_certificate()
    verify_rounded_integral_certificate()
    continuous_fixed_point()
