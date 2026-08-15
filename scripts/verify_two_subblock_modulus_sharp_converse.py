#!/usr/bin/env python3
"""Rational interval certificate for q=3 two-subblock modulus sharpness.

Proves that Q=6 uniquely minimizes the half-error fixed-state rate over all
integer Q >= 1.  No third-party packages or floating-point comparisons are
used in the assertions.
"""

from fractions import Fraction
from math import factorial


def decimal(text):
    integer, fractional = text.split(".")
    return Fraction(int(integer + fractional), 10 ** len(fractional))


def exp_negative_bounds(x, terms=90):
    assert 0 <= x <= 3
    term = Fraction(1)
    partial = term
    for k in range(1, terms + 1):
        term *= x / k
        partial += term
    next_term = term * x / (terms + 1)
    ratio = x / (terms + 2)
    exp_upper = partial + next_term / (1 - ratio)
    return 1 / exp_upper, 1 / partial


def raw_log_bounds(x, terms=100):
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


LN2_LOW, LN2_HIGH = raw_log_bounds(Fraction(2))


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
    low, high = raw_log_bounds(normalized)
    if exponent >= 0:
        return low + exponent * LN2_LOW, high + exponent * LN2_HIGH
    return low + exponent * LN2_HIGH, high + exponent * LN2_LOW


def add(x, y, q):
    return ((x[0] + y[0]) % q, (x[1] + y[1]) % 3, (x[2] + y[2]) % 3)


def subtract(x, y, q):
    return ((x[0] - y[0]) % q, (x[1] - y[1]) % 3, (x[2] - y[2]) % 3)


def exact_profile(q):
    increments = ((1 % q, 0, 0), (1 % q, 1, 0), (0, 0, 0), (0, 0, 1))
    reachable = {(0, 0, 0)}
    walk = {(0, 0, 0): 1}
    states = []
    rejection = []
    for load in range(q + 10):
        states.append(len(reachable))
        if load == 0:
            rejected_pairs = 4
        else:
            rejected_pairs = sum(
                multiplicity
                * sum(subtract(s, v, q) not in previous for v in increments)
                for s, multiplicity in walk.items()
            )
        rejection.append(Fraction(rejected_pairs, 4 ** (load + 1)))
        if load and len(reachable) == len(previous):
            assert rejected_pairs == 0
            return states, rejection
        previous = reachable
        reachable = {add(s, v, q) for s in reachable for v in increments}
        next_walk = {}
        for s, multiplicity in walk.items():
            for v in increments:
                successor = add(s, v, q)
                next_walk[successor] = next_walk.get(successor, 0) + multiplicity
        walk = next_walk
    raise AssertionError("sumset did not stabilize")


def poisson_bounds(rejection, lam):
    polynomial = sum(
        rejection[c] * lam**c / factorial(c) for c in range(len(rejection))
    )
    exp_low, exp_high = exp_negative_bounds(lam)
    return exp_low * polynomial, exp_high * polynomial


def ogf(states, z):
    cutoff = len(states) - 1
    return sum(states[c] * z**c for c in range(cutoff)) + (
        states[-1] * z**cutoff / (1 - z)
    )


def ogf_mean(states, z):
    cutoff = len(states) - 1
    numerator = sum(c * states[c] * z**c for c in range(cutoff))
    numerator += states[-1] * (
        cutoff * z**cutoff / (1 - z) + z ** (cutoff + 1) / (1 - z) ** 2
    )
    return numerator / ogf(states, z)


def rate_lower_on_saddle_box(states, lam_high, z_low, z_high):
    # For every z in [z_low,z_high], A(z) >= A(z_low) and
    # -log(z) >= -log(z_high).  The objective decreases with lambda.
    log_a_low, _ = log_bounds(ogf(states, z_low))
    _, log_z_high = log_bounds(z_high)
    natural_low = log_a_low / lam_high - log_z_high
    return natural_low / LN2_HIGH


def rate_upper_at_point(states, lam_low, z):
    # Evaluating at any z upper-bounds the infimum.  The objective is largest
    # at the lower endpoint of the lambda bracket.
    _, log_a_high = log_bounds(ogf(states, z))
    log_z_low, _ = log_bounds(z)
    natural_high = log_a_high / lam_low - log_z_low
    return natural_high / LN2_LOW


BRACKETS = {
    1: ("1.77356358748", "1.77356358749", "0.43537443626", "0.43537443628"),
    2: ("2.28512267886", "2.28512267887", "0.47001993195", "0.47001993198"),
    3: ("2.47019762300", "2.47019762302", "0.46494335444", "0.46494335447"),
    4: ("2.58782787764", "2.58782787766", "0.46202855250", "0.46202855254"),
    5: ("2.63445009436", "2.63445009438", "0.45735082394", "0.45735082399"),
    6: ("2.64801769402", "2.64801769403", "0.45332084284", "0.45332084289"),
    7: ("2.65099377906", "2.65099377908", "0.45072433273", "0.45072433278"),
    8: ("2.65153628861", "2.65153628863", "0.44928206050", "0.44928206056"),
}


def independent_binary_count(load):
    return sum(min(a + 1, 3) * min(load - a + 1, 3) for a in range(load + 1))


def frozen_tail_states(q):
    prefix = [independent_binary_count(c) for c in range(q)]
    return prefix + [prefix[-1]]


def infinite_rejection_bounds(lam):
    # J_infinity(lam) = exp(-lam/2) * sum_{t=0}^2 (lam/4)^t/t!.
    polynomial = sum((lam / 4) ** t / factorial(t) for t in range(3))
    exp_low, exp_high = exp_negative_bounds(lam / 2)
    return exp_low * polynomial, exp_high * polynomial


def main():
    profiles = {}
    for q in range(1, 9):
        states, rejection = exact_profile(q)
        profiles[q] = (states, rejection)
        lam_low, lam_high, z_low, z_high = map(decimal, BRACKETS[q])
        assert poisson_bounds(rejection, lam_low)[0] > Fraction(1, 2)
        assert poisson_bounds(rejection, lam_high)[1] < Fraction(1, 2)
        assert ogf_mean(states, z_low) < lam_low
        assert ogf_mean(states, z_high) > lam_high

    q6_states, _ = profiles[6]
    q6_lam_low = decimal(BRACKETS[6][0])
    q6_z_test = decimal("0.45332084286")
    winner_upper = rate_upper_at_point(q6_states, q6_lam_low, q6_z_test)
    assert winner_upper < decimal("2.346150")

    for q in range(1, 9):
        if q == 6:
            continue
        states, _ = profiles[q]
        lam_high = decimal(BRACKETS[q][1])
        z_low = decimal(BRACKETS[q][2])
        z_high = decimal(BRACKETS[q][3])
        competitor_lower = rate_lower_on_saddle_box(
            states, lam_high, z_low, z_high
        )
        assert competitor_lower > winner_upper
        print(q, "certified lower", float(competitor_lower))

    # Analytic tail reduction.  The uncoupled half-error root is bracketed,
    # and every allocation-mod-Q quotient has lambda_Q <= lambda_infinity.
    inf_low = decimal("2.65163815056")
    inf_high = decimal("2.65163815058")
    assert infinite_rejection_bounds(inf_low)[0] > Fraction(1, 2)
    assert infinite_rejection_bounds(inf_high)[1] < Fraction(1, 2)

    tail_states = frozen_tail_states(9)
    tail_z_low = decimal("0.45004638026")
    tail_z_high = decimal("0.45004638032")
    assert ogf_mean(tail_states, tail_z_low) < inf_low
    assert ogf_mean(tail_states, tail_z_high) > inf_high
    tail_lower = rate_lower_on_saddle_box(
        tail_states, inf_high, tail_z_low, tail_z_high
    )
    assert tail_lower > winner_upper
    print("Q>=9 certified lower", float(tail_lower))
    print("Q=6 certified upper", float(winner_upper))
    print("PASS")


if __name__ == "__main__":
    main()
