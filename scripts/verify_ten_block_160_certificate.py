#!/usr/bin/env python3
"""Fraction-only convex-dual certificate for the ten-block constant > 1.6079."""

from __future__ import annotations

from fractions import Fraction as F


Interval = tuple[F, F]
BLOCKS = 10
TARGET = F(16079, 10000)
LOG_TERMS = 120


def add(x: Interval, y: Interval) -> Interval:
    return x[0] + y[0], x[1] + y[1]


def mul(x: Interval, y: Interval) -> Interval:
    values = [x[i] * y[j] for i in (0, 1) for j in (0, 1)]
    return min(values), max(values)


def scale(c: F, x: Interval) -> Interval:
    return (c * x[0], c * x[1]) if c >= 0 else (c * x[1], c * x[0])


def inv(x: Interval) -> Interval:
    assert x[0] > 0
    return F(1) / x[1], F(1) / x[0]


def div(x: Interval, y: Interval) -> Interval:
    return mul(x, inv(y))


def sum_intervals(values: list[Interval]) -> Interval:
    total = (F(0), F(0))
    for value in values:
        total = add(total, value)
    return total


def log_interval(x: F) -> Interval:
    """Enclose ln(x) using an exact atanh series and rational tail bound."""
    assert x > 0
    if x < 1:
        lower, upper = log_interval(1 / x)
        return -upper, -lower

    z = (x - 1) / (x + 1)
    partial = F(0)
    power = z
    for k in range(LOG_TERMS):
        partial += power / (2 * k + 1)
        power *= z * z
    lower = 2 * partial
    remainder = 2 * power / ((2 * LOG_TERMS + 1) * (1 - z * z))
    return lower, lower + remainder


LN2 = log_interval(F(2))
INV_LN2 = inv(LN2)


def log2_interval(x: F) -> Interval:
    return div(log_interval(x), LN2)


def a_value(x: F) -> Interval:
    return log2_interval(F(2) / x)


def b_value(x: F) -> Interval:
    return scale(F(1) - x / 2, log2_interval((F(2) - x) / (F(1) - x)))


def phi_value(a: F, c: F) -> Interval:
    assert a < c
    return scale(F(1) - a / 2, log2_interval((F(2) - a) / (c - a)))


def a_prime(x: F) -> Interval:
    return scale(-F(1) / x, INV_LN2)


def b_prime(x: F) -> Interval:
    ratio = (F(2) - x) / (F(1) - x)
    natural = add(
        scale(-F(1, 2), add(log_interval(ratio), (F(1), F(1)))),
        (ratio / 2, ratio / 2),
    )
    return mul(natural, INV_LN2)


def phi_a_prime(a: F, c: F) -> Interval:
    assert a < c
    ratio = (F(2) - a) / (c - a)
    natural = add(
        scale(-F(1, 2), add(log_interval(ratio), (F(1), F(1)))),
        (ratio / 2, ratio / 2),
    )
    return mul(natural, INV_LN2)


def phi_c_prime(a: F, c: F) -> Interval:
    assert a < c
    return scale(-(F(2) - a) / (2 * (c - a)), INV_LN2)


def branch_values(z: list[F]) -> list[Interval]:
    values = [scale(F(1, BLOCKS), sum_intervals([a_value(x) for x in z]))]
    for r in range(BLOCKS - 1):
        left = [b_value(z[i]) for i in range(r + 1)]
        right = [phi_value(z[r], z[j]) for j in range(r + 1, BLOCKS)]
        values.append(scale(F(1, BLOCKS), sum_intervals(left + right)))
    values.append(scale(F(1, BLOCKS), sum_intervals([b_value(x) for x in z])))
    return values


def mixture_gradient(z: list[F], weights: list[F]) -> list[Interval]:
    gradient: list[Interval] = []
    for i in range(BLOCKS):
        terms = [scale(weights[0] / BLOCKS, a_prime(z[i]))]
        for r in range(BLOCKS - 1):
            if i < r:
                derivative = b_prime(z[i])
            elif i == r:
                derivative = add(
                    b_prime(z[i]),
                    sum_intervals(
                        [phi_a_prime(z[r], z[j]) for j in range(r + 1, BLOCKS)]
                    ),
                )
            else:
                derivative = phi_c_prime(z[r], z[i])
            terms.append(scale(weights[r + 1] / BLOCKS, derivative))
        terms.append(scale(weights[BLOCKS] / BLOCKS, b_prime(z[i])))
        gradient.append(sum_intervals(terms))
    return gradient


def decimal_fraction(text: str) -> F:
    whole, fractional = text.split(".")
    return F(int(whole + fractional), 10 ** len(fractional))


def main() -> None:
    z = [
        decimal_fraction(value)
        for value in (
            "0.24607073074127461",
            "0.41943582092445958",
            "0.54874422327959660",
            "0.64917775981383674",
            "0.72956444610870852",
            "0.79540135190501848",
            "0.85029461667573258",
            "0.89670648012901277",
            "0.93636784338373746",
            "0.97051323016209312",
        )
    ]
    weights = [
        decimal_fraction(value)
        for value in (
            "0.236811761162405",
            "0.092787322757503",
            "0.074942840662885",
            "0.066524701834436",
            "0.061560128205742",
            "0.058483982270063",
            "0.056758934426834",
            "0.056276433051068",
            "0.057287271113586",
            "0.060711040113579",
            "0.177855584401899",
        )
    ]

    assert F(0) < z[0] < z[-1] < F(1)
    assert all(z[i] < z[i + 1] for i in range(BLOCKS - 1))
    assert all(weight > 0 for weight in weights)
    assert sum(weights, F(0)) == 1

    branches = branch_values(z)
    mixture = sum_intervals(
        [scale(weight, branch) for weight, branch in zip(weights, branches)]
    )
    gradient = mixture_gradient(z, weights)

    loss = F(0)
    for x, derivative in zip(z, gradient):
        derivative_abs = max(abs(derivative[0]), abs(derivative[1]))
        loss += derivative_abs * max(x, 1 - x)
    certified = mixture[0] - loss

    coarse_denominator = 10**15
    coarse_lower = F(
        certified.numerator * coarse_denominator // certified.denominator,
        coarse_denominator,
    )
    assert coarse_lower <= certified
    assert coarse_lower > TARGET

    print(f"mixture_value_lower={float(mixture[0]):.15f}")
    print(f"gradient_loss_upper={float(loss):.15e}")
    print(f"global_lower={float(certified):.15f}")
    print(f"readable_exact_lower={coarse_lower}")
    print(f"exact_margin_over_1.6079={coarse_lower - TARGET}")
    print("PASS: ten-block constant > 1.6079")


if __name__ == "__main__":
    main()
