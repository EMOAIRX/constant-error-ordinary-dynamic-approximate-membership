#!/usr/bin/env python3
"""Exhaustive small-instance check of the fixed-slot histogram code."""

from fractions import Fraction as Q
from math import factorial


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, parts - 1, prefix + (value,))


def verify(b, s, extra_bits=4):
    denominator = b**s
    histograms = list(compositions(s, b))
    groups = [factorial(s) // product_factorials(c) for c in histograms]
    assert sum(groups) == denominator

    # Use a deliberately generous common slot so every histogram is codeable.
    minimum_width = min(Q(group, denominator) for group in groups)
    length = 0
    while Q(4, 2**length) > minimum_width:
        length += 1
    length += extra_bits

    codes = {}
    rank = 0
    for histogram, group in zip(histograms, groups):
        z = (2**length * rank) // denominator + 1
        point = Q(z, 2**length)
        left = Q(rank, denominator)
        right = Q(rank + group, denominator)
        assert left < point < right, (b, s, histogram, left, point, right)
        assert z not in codes, (b, s, histogram, codes[z])
        codes[z] = histogram
        rank += group

    # Decode by locating the unique interval containing the stored point.
    for z, expected in codes.items():
        point = Q(z, 2**length)
        rank = 0
        decoded = None
        for histogram, group in zip(histograms, groups):
            if Q(rank, denominator) < point < Q(rank + group, denominator):
                assert decoded is None
                decoded = histogram
            rank += group
        assert decoded == expected
    print(f"PASS b={b} s={s}: {len(histograms)} histograms, L={length}")


def product_factorials(histogram):
    result = 1
    for count in histogram:
        result *= factorial(count)
    return result


def main():
    for b in range(2, 7):
        for s in range(0, 8):
            verify(b, s)


if __name__ == "__main__":
    main()
