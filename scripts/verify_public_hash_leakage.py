#!/usr/bin/env python3
"""Exhaustively verify the public-hash leakage lemma on small instances.

This is a regression check, not a proof.  It enumerates every categorical
hash map and every ordered sample without replacement, computes I(L; h), and
checks the analytic upper bound from PUBLIC_HASH_CONDITIONAL_CONVERSE.md.
"""

import itertools
import math


def entropy(probabilities):
    return -sum(x * math.log2(x) for x in probabilities if x)


def verify(u, n, probabilities):
    alphabet = range(len(probabilities))
    maps = list(itertools.product(alphabet, repeat=u))
    map_weights = []
    for mapping in maps:
        weight = 1.0
        for label in mapping:
            weight *= probabilities[label]
        map_weights.append(weight)

    samples = list(itertools.permutations(range(u), n))
    sample_probability = 1 / len(samples)
    unconditional = {
        labels: math.prod(probabilities[x] for x in labels)
        for labels in itertools.product(alphabet, repeat=n)
    }

    mutual_information = 0.0
    for mapping, map_weight in zip(maps, map_weights):
        if not map_weight:
            continue
        conditional = {labels: 0.0 for labels in unconditional}
        for sample in samples:
            labels = tuple(mapping[x] for x in sample)
            conditional[labels] += sample_probability
        for labels, value in conditional.items():
            if value:
                mutual_information += (
                    map_weight
                    * value
                    * math.log2(value / unconditional[labels])
                )

    falling = math.prod(range(u - n + 1, u + 1))
    q = len(probabilities) - 1
    bound = math.log2(u**n / falling) + n * q / (u * math.log(2))
    assert mutual_information <= bound + 1e-10
    return mutual_information, bound


def main():
    cases = [
        (4, 2, (0.5, 0.5)),
        (5, 2, (0.2, 0.3, 0.5)),
        (5, 3, (0.1, 0.4, 0.5)),
        (6, 2, (0.1, 0.2, 0.3, 0.4)),
    ]
    for u, n, probabilities in cases:
        information, bound = verify(u, n, probabilities)
        print(
            f"u={u} n={n} alphabet={len(probabilities)} "
            f"I(L;h)={information:.9f} bound={bound:.9f}"
        )


if __name__ == "__main__":
    main()
