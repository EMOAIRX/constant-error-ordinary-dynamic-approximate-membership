#!/usr/bin/env python3
"""Exact uniform-query failure audit for Pair_(6,8,4,1)."""

from collections import defaultdict
from fractions import Fraction as F
from math import comb, factorial


MODULI = (6, 8, 4, 1)
MAX_LOAD = 55
LAMBDA = F(209, 10)


def base_type(max_load):
    generic = []
    query = []
    for load in range(max_load + 1):
        e_counts = defaultdict(int)
        q_counts = defaultdict(int)
        for ones in range(load + 1):
            count = comb(load, ones)
            residue = ones % 3
            slack = load - residue
            one_gap = 3 if residue == 0 else 0
            e_counts[slack] += count
            # Query symbol 1 has gap 3 only at residue 0.  Query symbol 0 has
            # gap 1 at every residue.  Their fixed-load rejection marginals
            # agree, but their joint (gap, slack) laws do not.
            q_counts[(one_gap, slack)] += count
            q_counts[(1, slack)] += count
        assert sum(e_counts.values()) == 2**load
        assert sum(q_counts.values()) == 2 ** (load + 1)
        generic.append(dict(e_counts))
        query.append(dict(q_counts))
    return 2, generic, query


def pair_type(child, modulus, max_load):
    child_alphabet, child_generic, child_query = child
    alphabet = 2 * child_alphabet
    generic = []
    query = []

    for load in range(max_load + 1):
        e_counts = defaultdict(int)
        q_counts = defaultdict(int)
        for left_load in range(load + 1):
            right_load = load - left_load
            interleavings = comb(load, left_load)

            for left_slack, left_count in child_generic[left_load].items():
                carried_left_slack = modulus * (left_slack // modulus)
                for right_slack, right_count in child_generic[right_load].items():
                    slack = carried_left_slack + right_slack
                    e_counts[slack] += interleavings * left_count * right_count

            # Queries whose label lies in the left child.
            for (left_gap, left_slack), left_count in child_query[left_load].items():
                residue_slack = left_slack % modulus
                missing = max(left_gap - residue_slack, 0)
                gap = modulus * ((missing + modulus - 1) // modulus)
                carried_left_slack = modulus * (left_slack // modulus)
                for right_slack, right_count in child_generic[right_load].items():
                    slack = carried_left_slack + right_slack
                    q_counts[(gap, slack)] += (
                        interleavings * left_count * right_count
                    )

            # Queries whose label lies in the right child.  Allocation residue
            # constrains only the left load, so the right-child query gap is
            # not rounded modulo Q.
            for left_slack, left_count in child_generic[left_load].items():
                carried_left_slack = modulus * (left_slack // modulus)
                for (right_gap, right_slack), right_count in child_query[
                    right_load
                ].items():
                    slack = carried_left_slack + right_slack
                    q_counts[(right_gap, slack)] += (
                        interleavings * left_count * right_count
                    )

        assert sum(e_counts.values()) == alphabet**load
        assert sum(q_counts.values()) == alphabet ** (load + 1)
        generic.append(dict(e_counts))
        query.append(dict(q_counts))

    return alphabet, generic, query


def rejection_profile(filter_type):
    alphabet, _, query = filter_type
    result = []
    for load, counts in enumerate(query):
        rejected = sum(count for (gap, slack), count in counts.items() if slack < gap)
        result.append(F(rejected, alphabet ** (load + 1)))
    return result


def polynomial_multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def ogf_numerator():
    numerator = [1, 1, 1]
    for modulus in MODULI:
        numerator = polynomial_multiply(numerator, numerator)
        numerator = polynomial_multiply(numerator, [1] * modulus)
    return numerator


def exp_negative_small_bounds(x, terms=100):
    """Bounds exp(-x) for 0 <= x <= 3 by inverting exp(x)."""
    assert 0 <= x <= 3
    term = F(1)
    partial = term
    for k in range(1, terms + 1):
        term *= x / k
        partial += term
    next_term = term * x / (terms + 1)
    ratio = x / (terms + 2)
    exp_upper = partial + next_term / (1 - ratio)
    exp_lower = partial
    return 1 / exp_upper, 1 / exp_lower


def exp_negative_bounds(x):
    pieces = max(1, (x.numerator + 3 * x.denominator - 1) // (3 * x.denominator))
    low, high = exp_negative_small_bounds(x / pieces)
    return low**pieces, high**pieces


def main():
    filter_type = base_type(MAX_LOAD)
    first_pair_profile = None
    for modulus in MODULI:
        filter_type = pair_type(filter_type, modulus, MAX_LOAD)
        if modulus == 6:
            first_pair_profile = rejection_profile(filter_type)

    expected_first_pair = [
        F(1), F(3, 4), F(9, 16), F(13, 32), F(9, 32), F(3, 16),
        F(237, 2048), F(63, 1024), F(189, 8192), F(189, 32768), F(0),
    ]
    assert first_pair_profile[:11] == expected_first_pair

    rho = rejection_profile(filter_type)
    assert rho[1] == F(495, 512)
    poisson_polynomial = sum(
        rho[c] * LAMBDA**c / factorial(c) for c in range(MAX_LOAD + 1)
    )
    _, exp_high = exp_negative_bounds(LAMBDA)
    first_tail_term = LAMBDA ** (MAX_LOAD + 1) / factorial(MAX_LOAD + 1)
    tail_ratio = LAMBDA / (MAX_LOAD + 2)
    poisson_tail_upper = exp_high * first_tail_term / (1 - tail_ratio)
    rejection_upper = exp_high * poisson_polynomial + poisson_tail_upper
    assert rejection_upper < F(1, 2)

    numerator = ogf_numerator()
    assert len(numerator) == 107

    print("moduli", MODULI)
    print("alphabet", filter_type[0])
    print("OGF numerator degree", len(numerator) - 1)
    print("uniform-query rho_1", rho[1])
    print("Poisson rejection upper at lambda=20.9", float(rejection_upper))
    print("PASS: the proposed lambda=20.9 half-error certificate fails")


if __name__ == "__main__":
    main()
