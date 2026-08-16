#!/usr/bin/env python3
"""Exact and rational-interval verification for the mod-6 cross-block filter."""

from collections import defaultdict
from fractions import Fraction
from math import factorial


EXPECTED_D = [1, 4, 10, 18, 27, 36, 44, 50, 53, 54, 54]
EXPECTED_RHO = [
    Fraction(1),
    Fraction(3, 4),
    Fraction(9, 16),
    Fraction(13, 32),
    Fraction(9, 32),
    Fraction(3, 16),
    Fraction(237, 2048),
    Fraction(63, 1024),
    Fraction(189, 8192),
    Fraction(189, 32768),
    Fraction(0),
]
P_COEFF = [1, 3, 6, 8, 9, 9, 8, 6, 3, 1]


def profile(load):
    fibers = defaultdict(list)
    for a0 in range(load + 1):
        for a1 in range(load - a0 + 1):
            for b0 in range(load - a0 - a1 + 1):
                b1 = load - a0 - a1 - b0
                composition = (a0, a1, b0, b1)
                syndrome = ((a0 + a1) % 6, a1 % 3, b1 % 3)
                fibers[syndrome].append(composition)

    rejection = Fraction(0)
    union_histogram = [0] * 5
    for compositions in fibers.values():
        union_size = sum(
            any(composition[i] > 0 for composition in compositions)
            for i in range(4)
        )
        union_histogram[union_size] += 1
        for composition in compositions:
            probability = Fraction(
                factorial(load),
                4**load
                * factorial(composition[0])
                * factorial(composition[1])
                * factorial(composition[2])
                * factorial(composition[3]),
            )
            rejection += probability * Fraction(4 - union_size, 4)
    return len(fibers), rejection, union_histogram


def exp_negative_bounds(x, terms=80):
    """Rational lower/upper bounds for exp(-x), for 0 <= x <= 3."""
    assert 0 <= x <= 3
    term = Fraction(1)
    partial = term
    for k in range(1, terms + 1):
        term *= x / k
        partial += term
    next_term = term * x / (terms + 1)
    ratio = x / (terms + 2)
    exp_upper = partial + next_term / (1 - ratio)
    exp_lower = partial
    return 1 / exp_upper, 1 / exp_lower


def poisson_rejection_bounds(lam):
    polynomial = sum(
        EXPECTED_RHO[c] * lam**c / factorial(c) for c in range(10)
    )
    exp_low, exp_high = exp_negative_bounds(lam)
    return exp_low * polynomial, exp_high * polynomial


def polynomial(coefficients, x):
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def saddle_mean(z):
    p = polynomial(P_COEFF, z)
    derivative = sum(i * P_COEFF[i] * z ** (i - 1) for i in range(1, 10))
    return z * (derivative / p + 1 / (1 - z))


def raw_log_bounds_between_one_and_two(x, terms=80):
    assert 1 <= x <= 2
    t = (x - 1) / (x + 1)
    total = Fraction(0)
    power = t
    for j in range(terms):
        total += power / (2 * j + 1)
        power *= t * t
    lower = 2 * total
    tail = 2 * power / ((2 * terms + 1) * (1 - t * t))
    return lower, lower + tail


LN2_LOW, LN2_HIGH = raw_log_bounds_between_one_and_two(Fraction(2))


def log_bounds(x):
    assert x > 0
    exponent = 0
    normalized = x
    while normalized < 1:
        normalized *= 2
        exponent -= 1
    while normalized >= 2:
        normalized /= 2
        exponent += 1
    low, high = raw_log_bounds_between_one_and_two(normalized)
    if exponent >= 0:
        return low + exponent * LN2_LOW, high + exponent * LN2_HIGH
    return low + exponent * LN2_HIGH, high + exponent * LN2_LOW


def rate_bounds(lam_low, lam_high, z):
    a = polynomial(P_COEFF, z) / (1 - z)
    log_a_low, log_a_high = log_bounds(a)
    log_z_low, log_z_high = log_bounds(z)
    numerator_low = log_a_low / lam_high - log_z_high
    numerator_high = log_a_high / lam_low - log_z_low
    return numerator_low / LN2_HIGH, numerator_high / LN2_LOW


def decimal_fraction(text):
    integer, fractional = text.split(".")
    return Fraction(int(integer + fractional), 10 ** len(fractional))


def main():
    print("Exact profiles")
    for load in range(11):
        states, rejection, histogram = profile(load)
        assert states == EXPECTED_D[load]
        assert rejection == EXPECTED_RHO[load]
        print(load, states, rejection, histogram)

    # At load 9 all 54 group elements are reachable. Translation by any
    # increment keeps the reachable syndrome set full at every later load.
    assert EXPECTED_D[9] == 54
    # At load 10 every fiber has full four-symbol support union. Adding the
    # last inserted symbol to each load-c witness propagates this forever.
    assert profile(10)[2] == [0, 0, 0, 0, 54]

    differences = [EXPECTED_D[0]] + [
        EXPECTED_D[i] - EXPECTED_D[i - 1] for i in range(1, 10)
    ]
    assert differences == P_COEFF
    print("OGF numerator", P_COEFF)

    lam_low = decimal_fraction("2.64801769")
    lam_high = decimal_fraction("2.64801770")
    j_low = poisson_rejection_bounds(lam_low)
    j_high = poisson_rejection_bounds(lam_high)
    assert j_low[0] > Fraction(1, 2)
    assert j_high[1] < Fraction(1, 2)
    print("lambda bracket", float(lam_low), float(lam_high))
    print("J(lambda_low) lower", float(j_low[0]))
    print("J(lambda_high) upper", float(j_high[1]))

    z_low = decimal_fraction("0.45332084")
    z_high = decimal_fraction("0.45332085")
    assert saddle_mean(z_low) < lam_low
    assert saddle_mean(z_high) > lam_high
    print("saddle bracket", float(z_low), float(z_high))

    z_test = decimal_fraction("0.453320845")
    _, rate_high = rate_bounds(lam_low, lam_high, z_test)
    assert rate_high < decimal_fraction("2.34616")
    assert rate_high < decimal_fraction("2.34908")
    print("fixed-test certified rate upper", float(rate_high))
    print("PASS")


if __name__ == "__main__":
    main()
