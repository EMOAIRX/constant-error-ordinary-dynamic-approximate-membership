#!/usr/bin/env python3
"""Directed-rounding branch certificate for the three-pivot constant > 1.48."""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext


PRECISION = 90
LOG_PRECISION = 130
# Decimal.ln is correctly rounded to nearest. At LOG_PRECISION, every ln used
# below has magnitude below 100, so this radius is far larger than one ulp.
LOG_RADIUS = Decimal("1e-110")
ZERO = Decimal(0)
ONE = Decimal(1)
TWO = Decimal(2)
HALF = Decimal("0.5")
EDGE = Decimal("0.05")
TARGET = Decimal("1.48")


def ln_bounds(x: Decimal) -> tuple[Decimal, Decimal]:
    assert x > 0
    with localcontext() as ctx:
        ctx.prec = LOG_PRECISION
        nearest = x.ln()
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        lower = nearest - LOG_RADIUS
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_CEILING
        upper = nearest + LOG_RADIUS
    return lower, upper


def log2_lower(x: Decimal) -> Decimal:
    numerator_lower, _ = ln_bounds(x)
    _, denominator_upper = ln_bounds(TWO)
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        return numerator_lower / denominator_upper


def add_lower(x: Decimal, y: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        return x + y


def mul_lower(x: Decimal, y: Decimal) -> Decimal:
    assert x >= 0 and y >= 0
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        return x * y


def div_lower(x: Decimal, y: Decimal) -> Decimal:
    assert x >= 0 and y > 0
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        return x / y


def a_lower(x: Decimal) -> Decimal:
    return log2_lower(div_lower(TWO, x))


def b_lower(x: Decimal) -> Decimal:
    # B(x) = (1-x/2) log_2((2-x)/(1-x)).
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        coefficient = ONE - x / TWO
        ratio = (TWO - x) / (ONE - x)
    return mul_lower(coefficient, log2_lower(ratio))


def phi_lower(p: Decimal, q: Decimal) -> Decimal:
    # Phi(p,q) = (1-p/2) log_2((2-p)/(q-p)).
    assert ZERO <= p < q <= ONE
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        coefficient = ONE - p / TWO
        ratio = (TWO - p) / (q - p)
    return mul_lower(coefficient, log2_lower(ratio))


def average_lower(x: Decimal, y: Decimal) -> Decimal:
    return mul_lower(HALF, add_lower(x, y))


def rectangle_lower(box: tuple[Decimal, Decimal, Decimal, Decimal]) -> Decimal:
    p_lo, p_hi, q_lo, q_hi = box
    first = average_lower(a_lower(p_hi), a_lower(q_hi))
    second = average_lower(b_lower(p_lo), b_lower(q_lo))
    if p_lo >= q_hi:
        third = Decimal("Infinity")
    else:
        third = average_lower(b_lower(p_lo), phi_lower(p_lo, q_hi))
    return max(first, second, third)


def midpoint_lower(x: Decimal, y: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        return (x + y) / TWO


def main() -> None:
    # Boundary p <= EDGE: F1 >= (A(EDGE)+A(1))/2.
    left_boundary = average_lower(a_lower(EDGE), a_lower(ONE))
    # Boundary q >= 1-EDGE: F2 >= (B(0)+B(1-EDGE))/2.
    right_boundary = average_lower(b_lower(ZERO), b_lower(ONE - EDGE))
    assert left_boundary > TARGET
    assert right_boundary > TARGET

    stack = [(EDGE, ONE - EDGE, EDGE, ONE - EDGE)]
    visited = 0
    max_depth = 0

    while stack:
        p_lo, p_hi, q_lo, q_hi = stack.pop()
        visited += 1
        if p_lo >= q_hi:
            continue
        if rectangle_lower((p_lo, p_hi, q_lo, q_hi)) > TARGET:
            continue

        p_width = p_hi - p_lo
        q_width = q_hi - q_lo
        assert max(p_width, q_width) > Decimal("1e-30"), "unresolved leaf"

        if p_width >= q_width:
            mid = midpoint_lower(p_lo, p_hi)
            stack.append((p_lo, mid, q_lo, q_hi))
            stack.append((mid, p_hi, q_lo, q_hi))
        else:
            mid = midpoint_lower(q_lo, q_hi)
            stack.append((p_lo, p_hi, q_lo, mid))
            stack.append((p_lo, p_hi, mid, q_hi))
        max_depth += 1
        assert visited < 1_000_000, "certificate did not terminate"

    print(f"target = {TARGET}")
    print(f"left boundary lower bound = {left_boundary}")
    print(f"right boundary lower bound = {right_boundary}")
    print(f"visited rectangles = {visited}")
    print("unresolved rectangles = 0")


if __name__ == "__main__":
    main()
