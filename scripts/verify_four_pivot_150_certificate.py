#!/usr/bin/env python3
"""Pure-rational convex-dual certificate for the four-pivot constant > 1.50."""

from __future__ import annotations

from fractions import Fraction as F


Interval = tuple[F, F]
TARGET = F(3, 2)


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


def log_interval(x: F, terms: int = 150) -> Interval:
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


def log2_interval(x: F) -> Interval:
    return div(log_interval(x), LN2)


def a_value(x: F) -> Interval:
    return log2_interval(F(2) / x)


def b_value(x: F) -> Interval:
    return scale(F(1) - x / 2, log2_interval((F(2) - x) / (F(1) - x)))


def phi_value(p: F, q: F) -> Interval:
    return scale(F(1) - p / 2, log2_interval((F(2) - p) / (q - p)))


def inv_ln2() -> Interval:
    return inv(LN2)


def a_prime(x: F) -> Interval:
    return scale(-F(1) / x, inv_ln2())


def b_prime(x: F) -> Interval:
    natural = add(
        scale(-F(1, 2), add(log_interval((F(2) - x) / (F(1) - x)), (F(1), F(1)))),
        ((F(2) - x) / (2 * (F(1) - x)),) * 2,
    )
    return mul(natural, inv_ln2())


def phi_a_prime(p: F, q: F) -> Interval:
    natural = add(
        scale(-F(1, 2), add(log_interval((F(2) - p) / (q - p)), (F(1), F(1)))),
        ((F(2) - p) / (2 * (q - p)),) * 2,
    )
    return mul(natural, inv_ln2())


def phi_b_prime(p: F, q: F) -> Interval:
    return scale(-(F(2) - p) / (2 * (q - p)), inv_ln2())


def sum_intervals(values: list[Interval]) -> Interval:
    total = (F(0), F(0))
    for value in values:
        total = add(total, value)
    return total


def main() -> None:
    # Rational approximations to the numerical KKT point and positive weights.
    z = [F(502232, 10**6), F(751825, 10**6), F(901385, 10**6)]
    weights = [F(345897, 10**6), F(168988, 10**6), F(146079, 10**6)]
    weights.append(F(1) - sum(weights, F(0)))
    assert ZERO < z[0] < z[1] < z[2] < F(1)
    assert all(w > 0 for w in weights) and sum(weights, F(0)) == 1

    branches = [
        scale(F(1, 3), sum_intervals([a_value(x) for x in z])),
        scale(F(1, 3), sum_intervals([b_value(z[0]), phi_value(z[0], z[1]), phi_value(z[0], z[2])])),
        scale(F(1, 3), sum_intervals([b_value(z[0]), b_value(z[1]), phi_value(z[1], z[2])])),
        scale(F(1, 3), sum_intervals([b_value(x) for x in z])),
    ]
    value = sum_intervals([scale(w, branch) for w, branch in zip(weights, branches)])

    gradients: list[Interval] = []
    # Coordinate z0.
    gradients.append(sum_intervals([
        scale(weights[0] / 3, a_prime(z[0])),
        scale(weights[1] / 3, sum_intervals([b_prime(z[0]), phi_a_prime(z[0], z[1]), phi_a_prime(z[0], z[2])])),
        scale(weights[2] / 3, b_prime(z[0])),
        scale(weights[3] / 3, b_prime(z[0])),
    ]))
    # Coordinate z1.
    gradients.append(sum_intervals([
        scale(weights[0] / 3, a_prime(z[1])),
        scale(weights[1] / 3, phi_b_prime(z[0], z[1])),
        scale(weights[2] / 3, sum_intervals([b_prime(z[1]), phi_a_prime(z[1], z[2])])),
        scale(weights[3] / 3, b_prime(z[1])),
    ]))
    # Coordinate z2.
    gradients.append(sum_intervals([
        scale(weights[0] / 3, a_prime(z[2])),
        scale(weights[1] / 3, phi_b_prime(z[0], z[2])),
        scale(weights[2] / 3, phi_b_prime(z[1], z[2])),
        scale(weights[3] / 3, b_prime(z[2])),
    ]))

    loss = F(0)
    for point, gradient in zip(z, gradients):
        residual = max(abs(gradient[0]), abs(gradient[1]))
        loss += residual * max(point, F(1) - point)
    certified = value[0] - loss
    denominator = 10**12
    coarse = F(certified.numerator * denominator // certified.denominator, denominator)

    print(f"weighted_value_lower={float(value[0]):.15f}")
    for i, gradient in enumerate(gradients):
        print(f"gradient_{i}_interval=({float(gradient[0]):.15f},{float(gradient[1]):.15f})")
    print(f"global_lower={float(certified):.15f}")
    print(f"readable_exact_lower={coarse.numerator}/{coarse.denominator}")
    assert coarse > TARGET
    assert certified > TARGET
    print("PASS: four-pivot constant > 1.50")


ZERO = F(0)


if __name__ == "__main__":
    main()
