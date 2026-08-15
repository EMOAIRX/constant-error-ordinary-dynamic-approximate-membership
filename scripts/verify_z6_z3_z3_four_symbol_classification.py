#!/usr/bin/env python3
"""Exact classification certificate for four symbols in Z6 x Z3 x Z3.

The proof-facing coordinates use the CRT isomorphism

    Z6 x Z3 x Z3 ~= Z2 x F3^3.

After translating one increment to zero, every generating four-set projects
to an affine frame in F3^3.  Up to affine automorphism and complementing the
Z2 coordinate, only the 2+2 and 1+3 parity splits remain.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product


Element = tuple[int, int, int, int]
ZERO: Element = (0, 0, 0, 0)


BALANCED_D = (1, 4, 10, 18, 27, 36, 44, 50, 53, 54, 54)
BALANCED_RHO = (
    Fraction(1), Fraction(3, 4), Fraction(9, 16), Fraction(13, 32),
    Fraction(9, 32), Fraction(3, 16), Fraction(237, 2048),
    Fraction(63, 1024), Fraction(189, 8192), Fraction(189, 32768),
    Fraction(0),
)
UNBALANCED_D = BALANCED_D
UNBALANCED_RHO = (
    Fraction(1), Fraction(3, 4), Fraction(9, 16), Fraction(51, 128),
    Fraction(135, 512), Fraction(333, 2048), Fraction(189, 2048),
    Fraction(189, 4096), Fraction(567, 32768), Fraction(567, 131072),
    Fraction(0),
)


def add(x: Element, y: Element) -> Element:
    return ((x[0] + y[0]) % 2,) + tuple(
        (x[i] + y[i]) % 3 for i in range(1, 4)
    )


def det3_mod3(columns: tuple[Element, Element, Element]) -> int:
    matrix = [[columns[j][i] for j in range(3)] for i in range(1, 4)]
    value = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    return value % 3


def exact_profile(increments: tuple[Element, ...]):
    walk_counts = {ZERO: 1}
    support_unions = {ZERO: 0}
    states = []
    rejections = []
    for load in range(109):
        states.append(len(walk_counts))
        rejected = sum(
            multiplicity * (4 - support_unions[state].bit_count())
            for state, multiplicity in walk_counts.items()
        )
        rejections.append(Fraction(rejected, 4 ** (load + 1)))
        if len(walk_counts) == 54 and all(mask == 15 for mask in support_unions.values()):
            return tuple(states), tuple(rejections)

        next_counts = defaultdict(int)
        next_unions = defaultdict(int)
        for state, multiplicity in walk_counts.items():
            for symbol, increment in enumerate(increments):
                target = add(state, increment)
                next_counts[target] += multiplicity
                next_unions[target] |= support_unions[state] | (1 << symbol)
        walk_counts = dict(next_counts)
        support_unions = dict(next_unions)
    raise AssertionError("profile did not stabilize")


def main():
    # Canonical affine-frame representatives.  The first coordinate is Z2;
    # the last three coordinates are F3^3.
    balanced = (ZERO, (0, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1))
    unbalanced = (ZERO, (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1))
    assert exact_profile(balanced) == (BALANCED_D, BALANCED_RHO)
    assert exact_profile(unbalanced) == (UNBALANCED_D, UNBALANCED_RHO)

    # Exhaust the normalized four-sets only to certify the orbit counts and
    # that no third affine-frame parity type exists.  The structural reason
    # is determinant != 0 plus Z2 complement/symbol permutation.
    group = list(product(range(2), range(3), range(3), range(3)))
    nonzero = [value for value in group if value != ZERO]
    balanced_count = 0
    unbalanced_count = 0
    nongenerating_count = 0
    for tail in combinations(nonzero, 3):
        if det3_mod3(tail) == 0:
            nongenerating_count += 1
            continue
        number_of_ones = sum(value[0] for value in tail)
        if number_of_ones == 0:
            # The F3 projection is a basis, but the increments miss the Z2
            # factor, so the four-set does not generate the full group.
            nongenerating_count += 1
            continue
        assert number_of_ones in (1, 2, 3)
        if number_of_ones == 2:
            balanced_count += 1
        else:
            unbalanced_count += 1

    assert balanced_count == 5616
    assert unbalanced_count == 7488
    assert balanced_count + unbalanced_count == 13104
    assert balanced_count + unbalanced_count + nongenerating_count == 23426

    # Same state OGF, strictly larger rejection for the balanced type from
    # load 3 through the last nonzero layer.
    assert BALANCED_D == UNBALANCED_D
    assert BALANCED_RHO[:3] == UNBALANCED_RHO[:3]
    assert all(
        BALANCED_RHO[c] > UNBALANCED_RHO[c]
        for c in range(3, 10)
    )
    print("normalized four-sets", 23426)
    print("generating balanced", balanced_count)
    print("generating unbalanced", unbalanced_count)
    print("PASS: exactly two generating profile types; balanced strictly dominates")


if __name__ == "__main__":
    main()
