#!/usr/bin/env python3
"""Exhaustive small-instance check for operational support completion.

This is a finite sanity check, not a proof of the theorem.  It enumerates every
nonempty operational family of 2-subsets of a four-point universe, every
nonempty uniform source subfamily, and a uniformly random legal one-label
insert-delete suffix.
"""

from itertools import combinations
from math import comb, log2


UNIVERSE = frozenset(range(4))
LOAD = 2
ENDPOINTS = [frozenset(pair) for pair in combinations(UNIVERSE, LOAD)]
TOLERANCE = 1e-12


def entropy(probabilities):
    return -sum(p * log2(p) for p in probabilities if p > 0)


def main():
    checked = 0
    minimum_slack = float("inf")

    for operational_mask in range(1, 1 << len(ENDPOINTS)):
        operational = [
            endpoint
            for index, endpoint in enumerate(ENDPOINTS)
            if operational_mask & (1 << index)
        ]
        union = frozenset().union(*operational)
        ambient_rank = log2(comb(len(union), LOAD))

        for source_mask in range(1, 1 << len(operational)):
            source = [
                endpoint
                for index, endpoint in enumerate(operational)
                if source_mask & (1 << index)
            ]
            source_probability = 1 / len(source)
            label_probability = {label: 0.0 for label in UNIVERSE}
            transport = 0.0

            for endpoint in source:
                legal_labels = UNIVERSE - endpoint
                pair_probability = source_probability / len(legal_labels)
                for label in legal_labels:
                    label_probability[label] += pair_probability
                    section = [
                        witness for witness in operational if label not in witness
                    ]
                    section_union = frozenset().union(*section)
                    transport += pair_probability * LOAD * log2(
                        len(union) / len(section_union)
                    )

            source_entropy = log2(len(source))
            label_entropy = entropy(label_probability.values())
            conditional_label_entropy = log2(len(UNIVERSE) - LOAD)
            suffix_information = label_entropy - conditional_label_entropy
            bound = ambient_rank - source_entropy + suffix_information
            slack = bound - transport

            if slack < -TOLERANCE:
                raise AssertionError(
                    f"support-completion inequality failed with slack {slack}"
                )
            minimum_slack = min(minimum_slack, slack)
            checked += 1

    print(
        "PASS operational support completion: "
        f"{checked} source/fiber pairs, minimum slack {minimum_slack:.12g}"
    )


if __name__ == "__main__":
    main()
