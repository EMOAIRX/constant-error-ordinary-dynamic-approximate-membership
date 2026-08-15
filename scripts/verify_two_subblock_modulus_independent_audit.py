#!/usr/bin/env python3
"""Independent Fraction-only audit of the q=3 allocation-mod-Q theorem.

All logical comparisons use integers or fractions.Fraction.  Decimal output is
only a human-readable rendering of already-certified rational intervals.
"""

from fractions import Fraction as F
from math import factorial


def dec(text):
    whole, fractional = text.split(".")
    return F(int(whole + fractional), 10 ** len(fractional))


def add(x, y, q):
    return ((x[0] + y[0]) % q, (x[1] + y[1]) % 3, (x[2] + y[2]) % 3)


def sub(x, y, q):
    return ((x[0] - y[0]) % q, (x[1] - y[1]) % 3, (x[2] - y[2]) % 3)


def exact_profile(q):
    """Return d_c and rho_c until the first permanent zero-rejection layer."""
    # The four entries remain separate because query support distinguishes
    # A0,A1,B0,B1, even when two group increments coincide.
    steps = ((1 % q, 0, 0), (1 % q, 1, 0), (0, 0, 0), (0, 0, 1))
    reachable = {(0, 0, 0)}
    walk = {(0, 0, 0): 1}
    states, rejection = [], []

    for c in range(q + 10):
        states.append(len(reachable))
        if c == 0:
            rejected = 4
        else:
            # At syndrome s, coordinate i occurs in some composition in the
            # fiber iff s-steps[i] was reachable at load c-1.
            rejected = sum(
                multiplicity * sum(sub(s, v, q) not in previous for v in steps)
                for s, multiplicity in walk.items()
            )
        rejection.append(F(rejected, 4 ** (c + 1)))

        if c and reachable == previous:
            # Since the zero step makes the reachable sets nested, equality
            # plus closure under every step propagates forever.
            assert rejected == 0
            return states, rejection

        previous = reachable
        reachable = {add(s, v, q) for s in reachable for v in steps}
        next_walk = {}
        for s, multiplicity in walk.items():
            for v in steps:
                t = add(s, v, q)
                next_walk[t] = next_walk.get(t, 0) + multiplicity
        walk = next_walk
    raise AssertionError("stabilization bound was insufficient")


EXPECTED = {
    1: ([1, 3, 6, 8, 9, 9], ["1", "5/8", "13/32", "3/16", "15/256", "0"]),
    2: ([1, 4, 9, 14, 17, 18, 18], ["1", "3/4", "17/32", "41/128", "71/512", "71/2048", "0"]),
    3: ([1, 4, 10, 17, 23, 26, 27, 27], ["1", "3/4", "9/16", "3/8", "27/128", "45/512", "45/2048", "0"]),
    4: ([1, 4, 10, 18, 26, 32, 35, 36, 36], ["1", "3/4", "9/16", "13/32", "67/256", "73/512", "231/4096", "231/16384", "0"]),
    5: ([1, 4, 10, 18, 27, 35, 41, 44, 45, 45], ["1", "3/4", "9/16", "13/32", "9/32", "181/1024", "387/4096", "147/4096", "147/16384", "0"]),
    6: ([1, 4, 10, 18, 27, 36, 44, 50, 53, 54, 54], ["1", "3/4", "9/16", "13/32", "9/32", "3/16", "237/2048", "63/1024", "189/8192", "189/32768", "0"]),
    7: ([1, 4, 10, 18, 27, 36, 45, 53, 59, 62, 63, 63], ["1", "3/4", "9/16", "13/32", "9/32", "3/16", "31/256", "1205/16384", "2557/65536", "3825/262144", "3825/1048576", "0"]),
    8: ([1, 4, 10, 18, 27, 36, 45, 54, 62, 68, 71, 72, 72], ["1", "3/4", "9/16", "13/32", "9/32", "3/16", "31/256", "39/512", "2987/65536", "3159/131072", "9405/1048576", "9405/4194304", "0"]),
}


ROOT_BOXES = {
    1: ("1.77356358748", "1.77356358749", "0.43537443626", "0.43537443628"),
    2: ("2.28512267886", "2.28512267887", "0.47001993195", "0.47001993198"),
    3: ("2.47019762300", "2.47019762302", "0.46494335444", "0.46494335447"),
    4: ("2.58782787764", "2.58782787766", "0.46202855250", "0.46202855254"),
    5: ("2.63445009436", "2.63445009438", "0.45735082394", "0.45735082399"),
    6: ("2.64801769402", "2.64801769403", "0.45332084284", "0.45332084289"),
    7: ("2.65099377906", "2.65099377908", "0.45072433273", "0.45072433278"),
    8: ("2.65153628861", "2.65153628863", "0.44928206050", "0.44928206056"),
}


def exp_minus_bounds(x, terms=100):
    """Rational enclosure of exp(-x), valid here for 0 <= x <= 3."""
    assert 0 <= x <= 3
    term = F(1)
    partial = term
    for k in range(1, terms + 1):
        term *= x / k
        partial += term
    next_term = term * x / (terms + 1)
    ratio = x / (terms + 2)
    exp_x_upper = partial + next_term / (1 - ratio)
    return 1 / exp_x_upper, 1 / partial


def poisson_bounds(rho, lam):
    p = sum(rho[c] * lam**c / factorial(c) for c in range(len(rho)))
    lo, hi = exp_minus_bounds(lam)
    return lo * p, hi * p


def log_unit_bounds(x, terms=110):
    """Enclose log(x) for 1 <= x <= 2 by the atanh series."""
    assert 1 <= x <= 2
    t = (x - 1) / (x + 1)
    power, partial = t, F(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= t * t
    lo = 2 * partial
    tail = 2 * power / ((2 * terms + 1) * (1 - t * t))
    return lo, lo + tail


LN2_LO, LN2_HI = log_unit_bounds(F(2))


def log_bounds(x):
    assert x > 0
    exponent = 0
    while x < 1:
        x *= 2
        exponent -= 1
    while x >= 2:
        x /= 2
        exponent += 1
    lo, hi = log_unit_bounds(x)
    if exponent >= 0:
        return lo + exponent * LN2_LO, hi + exponent * LN2_HI
    return lo + exponent * LN2_HI, hi + exponent * LN2_LO


def ogf(states, z):
    k = len(states) - 1
    return sum(states[c] * z**c for c in range(k)) + states[k] * z**k / (1 - z)


def mean(states, z):
    k = len(states) - 1
    numerator = sum(c * states[c] * z**c for c in range(k))
    numerator += states[k] * (k * z**k / (1 - z) + z ** (k + 1) / (1 - z) ** 2)
    return numerator / ogf(states, z)


def rate_lower(states, lam_hi, z_lo, z_hi):
    log_a_lo, _ = log_bounds(ogf(states, z_lo))
    _, log_z_hi = log_bounds(z_hi)
    return (log_a_lo / lam_hi - log_z_hi) / LN2_HI


def rate_upper(states, lam_lo, z):
    _, log_a_hi = log_bounds(ogf(states, z))
    log_z_lo, _ = log_bounds(z)
    return (log_a_hi / lam_lo - log_z_lo) / LN2_LO


def D(c):
    return sum(min(a + 1, 3) * min(c - a + 1, 3) for a in range(c + 1))


def frozen_tail(q):
    return [D(c) for c in range(q)] + [D(q - 1)]


def uncoupled_rejection_bounds(lam):
    # For a queried coordinate, rejection is {its count=0 and the other
    # count in the same binary subblock is at most 2}.  Poisson splitting
    # therefore gives exp(-lam/2) sum_{t=0}^2 (lam/4)^t/t!.
    p = sum((lam / 4) ** t / factorial(t) for t in range(3))
    lo, hi = exp_minus_bounds(lam / 2)
    return lo * p, hi * p


def main():
    profiles, intervals = {}, {}
    for q in range(1, 9):
        states, rho = exact_profile(q)
        expected_states, expected_rho = EXPECTED[q]
        assert states == expected_states
        assert rho == [F(x) for x in expected_rho]

        lam_lo, lam_hi, z_lo, z_hi = map(dec, ROOT_BOXES[q])
        assert poisson_bounds(rho, lam_lo)[0] > F(1, 2)
        assert poisson_bounds(rho, lam_hi)[1] < F(1, 2)
        assert mean(states, z_lo) < lam_lo
        assert mean(states, z_hi) > lam_hi

        lo = rate_lower(states, lam_hi, z_lo, z_hi)
        hi = rate_upper(states, lam_lo, (z_lo + z_hi) / 2)
        assert lo < hi
        profiles[q], intervals[q] = (states, rho), (lo, hi)
        print(f"Q={q}: {float(lo):.12f} < R_Q < {float(hi):.12f}")

    # The closest certified competitor is Q=5.
    gap_lo = intervals[5][0] - intervals[6][1]
    gap_hi = intervals[5][1] - intervals[6][0]
    assert gap_lo > dec("0.0003159365")
    assert gap_hi < dec("0.0003159370")
    for q in (1, 2, 3, 4, 7, 8):
        assert intervals[q][0] > intervals[5][0]
    print(f"certified R5-R6: ({float(gap_lo):.13f}, {float(gap_hi):.13f})")

    # Exact uncoupled half-error bracket.
    inf_lo, inf_hi = dec("2.65163815056"), dec("2.65163815058")
    assert uncoupled_rejection_bounds(inf_lo)[0] > F(1, 2)
    assert uncoupled_rejection_bounds(inf_hi)[1] < F(1, 2)

    # Q=9 frozen-tail relaxation.  Analytically, these OGF coefficients are
    # no larger than the true coefficients for every Q>=9.
    tail = frozen_tail(9)
    z_lo, z_hi = dec("0.45004638026"), dec("0.45004638032")
    assert mean(tail, z_lo) < inf_lo
    assert mean(tail, z_hi) > inf_hi
    tail_lo = rate_lower(tail, inf_hi, z_lo, z_hi)
    assert tail_lo > intervals[6][1]
    assert tail_lo > dec("2.3477511223")
    print(f"Q>=9 certified lower bound: {float(tail_lo):.12f}")
    print("PASS: unique minimizer Q=6 within the allocation-load-mod-Q family")


if __name__ == "__main__":
    main()
