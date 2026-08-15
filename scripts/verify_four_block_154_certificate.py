#!/usr/bin/env python3
"""Fraction-only convex-dual certificate for the four-block constant > 1.54.

For z_0 < ... < z_3, the five branches are

    f_0       = (1/4) sum_i A(z_i),
    f_{r+1}   = (1/4) [sum_{i <= r} B(z_i)
                              + sum_{j > r} Phi(z_r, z_j)],  r = 0, 1, 2,
    f_4       = (1/4) sum_i B(z_i).

All branches are convex.  A positive rational mixture L of them satisfies
max_i f_i >= L.  The script evaluates L and its gradient at a rational point,
then uses the convex first-order inequality and a global [0,1]^4 rectangle
bound for the small gradient residual.  All certified comparisons use exact
Fraction arithmetic; floats are printed only for readability.
"""

from __future__ import annotations

from fractions import Fraction as F


Interval = tuple[F, F]
BLOCKS = 4
TARGET = F(154, 100)


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


def sum_intervals(xs: list[Interval]) -> Interval:
    total = (F(0), F(0))
    for x in xs:
        total = add(total, x)
    return total


def log_interval(x: F, terms: int = 120) -> Interval:
    """Enclose ln(x) by the atanh series and a rational tail bound."""
    assert x > 0
    if x < 1:
        lo, hi = log_interval(1 / x, terms)
        return -hi, -lo

    z = (x - 1) / (x + 1)
    partial = F(0)
    power = z
    for k in range(terms):
        partial += power / (2 * k + 1)
        power *= z * z
    lower = 2 * partial
    remainder = 2 * power / ((2 * terms + 1) * (1 - z * z))
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
    natural = add(
        scale(
            -F(1, 2),
            add(log_interval((F(2) - x) / (F(1) - x)), (F(1), F(1))),
        ),
        ((F(2) - x) / (2 * (F(1) - x)),) * 2,
    )
    return mul(natural, INV_LN2)


def phi_a_prime(a: F, c: F) -> Interval:
    assert a < c
    natural = add(
        scale(
            -F(1, 2),
            add(log_interval((F(2) - a) / (c - a)), (F(1), F(1))),
        ),
        ((F(2) - a) / (2 * (c - a)),) * 2,
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
    assert len(values) == BLOCKS + 1
    return values


def mixture_gradient(z: list[F], weights: list[F]) -> list[Interval]:
    gradient: list[Interval] = []
    for i in range(BLOCKS):
        terms = [scale(weights[0] / BLOCKS, a_prime(z[i]))]

        # In interior branch r+1, coordinate i is respectively an earlier
        # B argument, the shared Phi left argument, or a Phi right argument.
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
        decimal_fraction("0.435286582899"),
        decimal_fraction("0.672473997153"),
        decimal_fraction("0.822405230844"),
        decimal_fraction("0.925522048947"),
    ]
    weights = [
        decimal_fraction("0.316977180108"),
        decimal_fraction("0.147649270359"),
        decimal_fraction("0.124838459830"),
        decimal_fraction("0.117472213103"),
        decimal_fraction("0.293062876600"),
    ]

    assert F(0) < z[0] < z[1] < z[2] < z[3] < F(1)
    assert len(weights) == BLOCKS + 1
    assert all(weight > 0 for weight in weights)
    assert sum(weights, F(0)) == 1

    branches = branch_values(z)
    mixture_value = sum_intervals(
        [scale(weight, branch) for weight, branch in zip(weights, branches)]
    )
    gradient = mixture_gradient(z, weights)

    # Convexity gives L(x) >= L(z) + grad L(z).(x-z).  Bound the affine
    # residual on the containing rectangle [0,1]^4.
    loss = F(0)
    for x, derivative in zip(z, gradient):
        derivative_abs = max(abs(derivative[0]), abs(derivative[1]))
        loss += derivative_abs * max(x, 1 - x)
    certified = mixture_value[0] - loss

    coarse_denominator = 10**12
    coarse_lower = F(
        certified.numerator * coarse_denominator // certified.denominator,
        coarse_denominator,
    )
    assert coarse_lower <= certified

    for i, branch in enumerate(branches):
        print(f"branch_{i}_lower={float(branch[0]):.15f}")
    print(f"mixture_value_lower={float(mixture_value[0]):.15f}")
    for i, derivative in enumerate(gradient):
        print(
            f"gradient_{i}_interval="
            f"({float(derivative[0]):.15e},{float(derivative[1]):.15e})"
        )
    print(f"global_lower={float(certified):.15f}")
    print(
        "readable_exact_lower="
        f"{coarse_lower.numerator}/{coarse_lower.denominator}"
    )
    margin = coarse_lower - TARGET
    print(f"exact_margin_over_1.54={margin.numerator}/{margin.denominator}")

    assert coarse_lower > TARGET
    assert certified > TARGET
    print("PASS: four-block constant > 1.54")


if __name__ == "__main__":
    main()
