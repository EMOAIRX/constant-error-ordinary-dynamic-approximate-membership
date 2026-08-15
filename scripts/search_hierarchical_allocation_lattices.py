#!/usr/bin/env python3
"""Exact profile search for hierarchical allocation lattices.

Leaves are binary order-3 quotients. Each internal tree node stores the load
of its left subtree modulo the node's modulus; the root load is also exact.
"""

from collections import defaultdict
from fractions import Fraction
from math import exp, factorial, log, log2, sqrt
from itertools import product


def tree_intervals(leaves):
    """Preorder intervals for all internal nodes of a balanced binary tree."""
    result = []

    def visit(left, right):
        if right - left == 1:
            return
        middle = (left + right) // 2
        result.append((left, middle, right))
        visit(left, middle)
        visit(middle, right)

    visit(0, leaves)
    return result


def increments(leaves, moduli):
    nodes = tree_intervals(leaves)
    assert len(nodes) == len(moduli)
    result = []
    for leaf in range(leaves):
        allocation = tuple(
            1 if left <= leaf < middle else 0
            for left, middle, _ in nodes
        )
        for bit in range(2):
            result.append(
                tuple(value % modulus for value, modulus in zip(allocation, moduli))
                + tuple(bit if index == leaf else 0 for index in range(leaves))
            )
    return result


def add_syndrome(state, increment, moduli, leaves):
    split = len(moduli)
    return tuple(
        (state[i] + increment[i]) % moduli[i] for i in range(split)
    ) + tuple(
        (state[split + i] + increment[split + i]) % 3
        for i in range(leaves)
    )


def exact_profiles(leaves, moduli, max_load=80):
    alphabet = 2 * leaves
    incs = increments(leaves, moduli)
    zero = (0,) * (len(moduli) + leaves)
    counts = {zero: 1}
    unions = {zero: 0}
    states = []
    rejections = []
    full_mask = (1 << alphabet) - 1
    group_size = 3**leaves
    for modulus in moduli:
        group_size *= modulus

    for load in range(max_load + 1):
        states.append(len(counts))
        rejected_paths = sum(
            path_count * (alphabet - unions[syndrome].bit_count())
            for syndrome, path_count in counts.items()
        )
        rejections.append(Fraction(rejected_paths, alphabet ** (load + 1)))
        if len(counts) == group_size and all(mask == full_mask for mask in unions.values()):
            return states, rejections, load, group_size

        new_counts = defaultdict(int)
        new_unions = defaultdict(int)
        for syndrome, path_count in counts.items():
            for symbol, increment in enumerate(incs):
                target = add_syndrome(syndrome, increment, moduli, leaves)
                new_counts[target] += path_count
                new_unions[target] |= unions[syndrome] | (1 << symbol)
        counts, unions = dict(new_counts), dict(new_unions)
    return states, rejections, None, group_size


def bisect(function, left, right, iterations=100):
    left_value = function(left)
    for _ in range(iterations):
        middle = (left + right) / 2
        middle_value = function(middle)
        if left_value * middle_value <= 0:
            right = middle
        else:
            left, left_value = middle, middle_value
    return (left + right) / 2


def golden(function, left, right, iterations=100):
    ratio = (sqrt(5) - 1) / 2
    c = right - ratio * (right - left)
    d = left + ratio * (right - left)
    fc, fd = function(c), function(d)
    for _ in range(iterations):
        if fc < fd:
            right, d, fd = d, c, fc
            c = right - ratio * (right - left)
            fc = function(c)
        else:
            left, c, fc = c, d, fd
            d = left + ratio * (right - left)
            fd = function(d)
    x = (left + right) / 2
    return x, function(x)


def rate(states, rejections, saturation_load, group_size):
    def rejection(load):
        return exp(-load) * sum(
            float(value) * load**c / factorial(c)
            for c, value in enumerate(rejections)
        )

    right = 1.0
    while rejection(right) > 0.5:
        right *= 2
    mean = bisect(lambda value: rejection(value) - 0.5, 1e-12, right)

    def generating_function(z):
        prefix = sum(states[c] * z**c for c in range(saturation_load))
        return prefix + group_size * z**saturation_load / (1 - z)

    saddle_log, result = golden(
        lambda y: log2(generating_function(exp(y))) / mean - y / log(2),
        -15,
        -1e-12,
    )
    return mean, exp(saddle_log), result


def evaluate(leaves, moduli):
    states, rejections, saturation, group_size = exact_profiles(leaves, moduli)
    if saturation is None:
        return None
    mean, saddle, bits = rate(states, rejections, saturation, group_size)
    return bits, mean, saddle, saturation, states, rejections


def main():
    candidates = []
    for moduli in product(range(3, 10), repeat=3):
        result = evaluate(4, moduli)
        if result is not None:
            candidates.append((result[0], moduli, result))
            print(moduli, result[0], result[1], result[3])
    print("BEST")
    for bits, moduli, result in sorted(candidates)[:20]:
        print(moduli, bits, result[1], result[2], result[3])
        print("d", result[4])
        print("rho", result[5])


if __name__ == "__main__":
    main()
