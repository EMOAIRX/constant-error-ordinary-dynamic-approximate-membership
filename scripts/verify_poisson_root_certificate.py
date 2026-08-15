#!/usr/bin/env python3
"""Pure-rational certificate for the Poisson phase-transition root.

For rational 0 < x < 1, bound

    S(x) = x H'(x) + (x-1) H(x)

using rational Taylor bounds for exp and log and a geometric Poisson-tail
bound.  Since the analytic companion proves S is strictly increasing after
multiplication by the positive factor relating it to F', opposite signs at
two rational endpoints rigorously enclose the unique stationary point.
"""

from fractions import Fraction as Q
from math import factorial


def log_bounds(x: Q, terms: int = 240) -> tuple[Q, Q]:
    """Rigorous bounds for log(x), using the atanh expansion."""
    assert x > 0
    z = (x - 1) / (x + 1)
    zz = z * z
    power = z
    total = Q(0)
    for j in range(terms):
        total += Q(2) * power / (2 * j + 1)
        power *= zz
    # Absolute tail: denominators are at least the first omitted one.
    error = Q(2) * abs(power) / ((2 * terms + 1) * (1 - zz))
    return total - error, total + error


def exp_minus_bounds(x: Q, terms: int = 120) -> tuple[Q, Q]:
    """Alternating-series bounds for exp(-x), valid for 0 < x < 1."""
    assert 0 < x < 1
    total = Q(0)
    term = Q(1)
    partials = []
    for k in range(terms + 1):
        if k:
            term *= -x / k
        total += term
        partials.append(total)
    # Even partial sums are upper bounds; odd partial sums are lower bounds.
    if terms % 2 == 0:
        upper = partials[terms]
        lower = partials[terms - 1]
    else:
        lower = partials[terms]
        upper = partials[terms - 1]
    return lower, upper


def add_interval(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul_nonnegative(a, b):
    assert a[0] >= 0 and b[0] >= 0
    return a[0] * b[0], a[1] * b[1]


def poisson_a_bounds(x: Q, cutoff: int = 30):
    """Bounds A=E log(X!) and A'=E log(X+1), X~Pois(x)."""
    exp_lo, exp_hi = exp_minus_bounds(x)
    a_lo = Q(0)
    a_hi = Q(0)
    ap_lo = Q(0)
    ap_hi = Q(0)
    log_factorial_lo = Q(0)
    log_factorial_hi = Q(0)

    for k in range(cutoff + 1):
        mass_factor = x**k / factorial(k)
        p_interval = (exp_lo * mass_factor, exp_hi * mass_factor)

        if k >= 2:
            lk_lo, lk_hi = log_bounds(Q(k))
            log_factorial_lo += lk_lo
            log_factorial_hi += lk_hi
        if k >= 1:
            a_term = mul_nonnegative(
                p_interval, (log_factorial_lo, log_factorial_hi)
            )
            a_lo += a_term[0]
            a_hi += a_term[1]

        lnext = log_bounds(Q(k + 1))
        ap_term = mul_nonnegative(p_interval, lnext)
        ap_lo += ap_term[0]
        ap_hi += ap_term[1]

    # For k >= cutoff+1, log(k!) <= k^2 and log(k+1) <= k+1.
    # Bound each positive tail by its first term times a geometric series.
    k = cutoff + 1
    p_first_hi = exp_hi * x**k / factorial(k)

    # Ratio of k^2 p_k terms at and beyond k.
    rho_a = x * Q(k + 1, k * k)
    assert rho_a < 1
    a_hi += p_first_hi * k * k / (1 - rho_a)

    # Ratio of (k+1) p_k terms at and beyond k.
    rho_ap = x * Q(k + 2, (k + 1) * (k + 1))
    assert rho_ap < 1
    ap_hi += p_first_hi * (k + 1) / (1 - rho_ap)
    return (a_lo, a_hi), (ap_lo, ap_hi)


def stationary_bounds(x: Q):
    """Bounds S=x(x-1)-x^2 log x+x A'+(x-1)A."""
    log_lo, log_hi = log_bounds(x)
    (a_lo, a_hi), (ap_lo, ap_hi) = poisson_a_bounds(x)
    base_lo = x * (x - 1) - x * x * log_hi
    base_hi = x * (x - 1) - x * x * log_lo
    # x > 0 and x-1 < 0.
    lower = base_lo + x * ap_lo + (x - 1) * a_hi
    upper = base_hi + x * ap_hi + (x - 1) * a_lo
    return lower, upper


def entropy_bounds(x: Q):
    log_lo, log_hi = log_bounds(x)
    (a_lo, a_hi), _ = poisson_a_bounds(x)
    return x * (1 - log_hi) + a_lo, x * (1 - log_lo) + a_hi


def decimal(q: Q, digits: int = 18) -> str:
    return f"{q.numerator / q.denominator:.{digits}g}"


def main():
    endpoints = (
        Q(4399316012447, 10_000_000_000_000),
        Q(4399316012449, 10_000_000_000_000),
        Q(11, 25),
    )
    intervals = []
    for x in endpoints:
        bounds = stationary_bounds(x)
        intervals.append(bounds)
        print(
            f"x={decimal(x, 16)} "
            f"S in [{decimal(bounds[0])}, {decimal(bounds[1])}]"
        )

    assert intervals[0][1] < 0
    assert intervals[1][0] > 0
    assert intervals[2][0] > 0
    print("PASS unique root lies in the first two rational endpoints")
    print("PASS lambda_* < 11/25 = 0.44")

    left, right = endpoints[:2]
    expm_left = exp_minus_bounds(left)
    expm_right = exp_minus_bounds(right)
    # exp(-x) decreases with x.
    epsilon_lower = 1 - expm_left[1]
    epsilon_upper = 1 - expm_right[0]

    h_left = entropy_bounds(left)
    h_right = entropy_bounds(right)
    # H(Pois(x)) is increasing for x>0.  Bound every positive factor of
    # exp(x) H(x)/x independently across [left,right].
    c_nats_lower = Q(1, 1) / expm_left[1] * h_left[0] / right
    c_nats_upper = Q(1, 1) / expm_right[0] * h_right[1] / left
    ln2 = log_bounds(Q(2))
    c_bits_lower = c_nats_lower / ln2[1]
    c_bits_upper = c_nats_upper / ln2[0]
    print(
        "epsilon_* in "
        f"[{decimal(epsilon_lower, 17)}, {decimal(epsilon_upper, 17)}]"
    )
    print(
        "C_* bits in "
        f"[{decimal(c_bits_lower, 17)}, {decimal(c_bits_upper, 17)}]"
    )


if __name__ == "__main__":
    main()
