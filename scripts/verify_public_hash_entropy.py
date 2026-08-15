#!/usr/bin/env python3
"""Exhaustively verify the public-hash mutual-information identities.

The instances are intentionally tiny: enumerate every hash tape h:U->[q]
and every n-subset S.  This checks the exact finite identity, independently
of asymptotics or sampling error.
"""

from __future__ import annotations

import itertools
import math
from collections import defaultdict
from fractions import Fraction


def entropy(distribution: dict[object, Fraction]) -> float:
    return -sum(float(x) * math.log(float(x)) for x in distribution.values() if x)


def multinomial_distribution(k: int, probabilities: tuple[Fraction, ...]):
    out: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    q = len(probabilities)
    for labels in itertools.product(range(q), repeat=k):
        mass = Fraction(1)
        counts = [0] * q
        for label in labels:
            mass *= probabilities[label]
            counts[label] += 1
        out[tuple(counts)] += mass
    return dict(out)


def verify(m: int, n: int, probabilities: tuple[Fraction, ...]) -> None:
    q = len(probabilities)
    subsets = tuple(itertools.combinations(range(m), n))
    subset_mass = Fraction(1, len(subsets))

    p_h: dict[tuple[int, ...], Fraction] = {}
    p_n: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    p_c: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    p_nc: dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction] = defaultdict(Fraction)
    p_nh: dict[tuple[tuple[int, ...], tuple[int, ...]], Fraction] = defaultdict(Fraction)

    for tape in itertools.product(range(q), repeat=m):
        tape_mass = Fraction(1)
        population = [0] * q
        for label in tape:
            tape_mass *= probabilities[label]
            population[label] += 1
        population_tuple = tuple(population)
        p_h[tape] = tape_mass
        p_c[population_tuple] += tape_mass

        for subset in subsets:
            occupancy = [0] * q
            for key in subset:
                occupancy[tape[key]] += 1
            occupancy_tuple = tuple(occupancy)
            joint_mass = tape_mass * subset_mass
            p_n[occupancy_tuple] += joint_mass
            p_nc[(occupancy_tuple, population_tuple)] += joint_mass
            p_nh[(occupancy_tuple, tape)] += joint_mass

    def mutual_information(
        joint: dict[tuple[object, object], Fraction],
        left: dict[object, Fraction],
        right: dict[object, Fraction],
    ) -> float:
        return sum(
            float(mass)
            * math.log(float(mass / (left[x] * right[y])))
            for (x, y), mass in joint.items()
            if mass
        )

    i_n_h = mutual_information(p_nh, p_n, p_h)
    i_n_c = mutual_information(p_nc, p_n, p_c)
    rhs = entropy(multinomial_distribution(m, probabilities)) - entropy(
        multinomial_distribution(m - n, probabilities)
    )

    tolerance = 2e-12
    assert abs(i_n_h - i_n_c) < tolerance, (i_n_h, i_n_c)
    assert abs(i_n_h - rhs) < tolerance, (i_n_h, rhs)
    assert p_n == multinomial_distribution(n, probabilities)
    print(
        f"PASS m={m} n={n} p={tuple(map(str, probabilities))}: "
        f"I(N;h)=I(N;C)={i_n_h:.12f}, entropy difference={rhs:.12f}"
    )


def main() -> None:
    cases = (
        (3, 1, (Fraction(1, 2), Fraction(1, 2))),
        (4, 2, (Fraction(1, 3), Fraction(2, 3))),
        (5, 2, (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))),
        (6, 3, (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4))),
    )
    for case in cases:
        verify(*case)


if __name__ == "__main__":
    main()
