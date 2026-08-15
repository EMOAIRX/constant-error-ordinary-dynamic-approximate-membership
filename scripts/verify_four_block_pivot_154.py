#!/usr/bin/env python3
"""Directed-rounding certificate for the four-block pivot constant > 1.54."""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext


PRECISION = 90
LOG_PRECISION = 130
LOG_RADIUS = Decimal("1e-110")
ZERO = Decimal(0)
ONE = Decimal(1)
TWO = Decimal(2)
Q = 4
LOW_EDGE = Decimal("0.1")
HIGH_EDGE = Decimal("0.99")
TARGET = Decimal("1.54")


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


def add_lower(values: list[Decimal]) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        return sum(values, ZERO)


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


def average_lower(values: list[Decimal]) -> Decimal:
    return div_lower(add_lower(values), Decimal(len(values)))


def a_lower(x: Decimal) -> Decimal:
    return log2_lower(div_lower(TWO, x))


def b_lower(x: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        coefficient = ONE - x / TWO
        ratio = (TWO - x) / (ONE - x)
    return mul_lower(coefficient, log2_lower(ratio))


def phi_lower(p: Decimal, q: Decimal) -> Decimal:
    assert ZERO <= p < q <= ONE
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        coefficient = ONE - p / TWO
        ratio = (TWO - p) / (q - p)
    return mul_lower(coefficient, log2_lower(ratio))


Box = tuple[tuple[Decimal, Decimal], ...]


def normalize(box: Box) -> Box | None:
    lows = [interval[0] for interval in box]
    highs = [interval[1] for interval in box]
    for i in range(1, Q):
        lows[i] = max(lows[i], lows[i - 1])
    for i in range(Q - 2, -1, -1):
        highs[i] = min(highs[i], highs[i + 1])
    if any(lows[i] > highs[i] for i in range(Q)):
        return None
    return tuple(zip(lows, highs))


def rectangle_lower(box: Box) -> Decimal:
    lows = [interval[0] for interval in box]
    highs = [interval[1] for interval in box]
    branches = [average_lower([a_lower(x) for x in highs])]
    for j in range(Q - 1):
        terms = [b_lower(lows[r]) for r in range(j + 1)]
        if any(lows[j] >= highs[r] for r in range(j + 1, Q)):
            branches.append(Decimal("Infinity"))
        else:
            terms.extend(phi_lower(lows[j], highs[r]) for r in range(j + 1, Q))
            branches.append(average_lower(terms))
    branches.append(average_lower([b_lower(x) for x in lows]))
    return max(branches)


def midpoint_lower(x: Decimal, y: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = ROUND_FLOOR
        return (x + y) / TWO


def main() -> None:
    left_boundary = average_lower(
        [a_lower(LOW_EDGE)] + [a_lower(ONE)] * (Q - 1)
    )
    right_boundary = average_lower(
        [b_lower(ZERO)] * (Q - 1) + [b_lower(HIGH_EDGE)]
    )
    assert left_boundary > TARGET
    assert right_boundary > TARGET

    initial = tuple((LOW_EDGE, HIGH_EDGE) for _ in range(Q))
    stack = [initial]
    visited = 0
    max_stack = 1

    while stack:
        raw_box = stack.pop()
        box = normalize(raw_box)
        if box is None:
            continue
        visited += 1
        if rectangle_lower(box) > TARGET:
            continue

        widths = [hi - lo for lo, hi in box]
        split = max(range(Q), key=widths.__getitem__)
        assert widths[split] > Decimal("1e-30"), "unresolved leaf"
        lo, hi = box[split]
        mid = midpoint_lower(lo, hi)
        left = list(box)
        right = list(box)
        left[split] = (lo, mid)
        right[split] = (mid, hi)
        stack.append(tuple(left))
        stack.append(tuple(right))
        max_stack = max(max_stack, len(stack))
        assert visited < 5_000_000, "certificate did not terminate"

    print(f"target = {TARGET}")
    print(f"left boundary lower bound = {left_boundary}")
    print(f"right boundary lower bound = {right_boundary}")
    print(f"visited boxes = {visited}")
    print(f"maximum stack size = {max_stack}")
    print("unresolved boxes = 0")


if __name__ == "__main__":
    main()
