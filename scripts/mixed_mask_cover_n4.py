#!/usr/bin/env python3
"""Heuristic search for sub-1-bit mixed rejected-mask filters at n=4.

A sufficient static construction is a family F of rejected masks such that
every negative four-set N is the union of two (not necessarily distinct)
masks Z1,Z2 in F.  Build can then choose Z1 or Z2 with probability 1/2;
every negative item is rejected with probability at least 1/2.

This script searches for |F| <= 15.  A found family is an exact, exhaustively
verified static witness.  Failure is only heuristic and is not a lower bound.
"""

from itertools import combinations
import math
import random


VERTICES = tuple(range(8))
FOUR_MASKS = tuple(sum(1 << v for v in values) for values in combinations(VERTICES, 4))
FOUR_INDEX = {mask: index for index, mask in enumerate(FOUR_MASKS)}
CANDIDATES = tuple(
    mask
    for mask in range(1, 1 << len(VERTICES))
    if 1 <= mask.bit_count() <= 4
)


def union_index(left, right):
    return FOUR_INDEX.get(left | right, -1)


def coverage_counts(family):
    counts = [0] * len(FOUR_MASKS)
    for i, left in enumerate(family):
        for right in family[i:]:
            index = union_index(left, right)
            if index >= 0:
                counts[index] += 1
    return counts


def uncovered_count(family):
    return sum(count == 0 for count in coverage_counts(family))


def adjust_pair(counts, left, right, delta):
    index = union_index(left, right)
    if index < 0:
        return 0
    was_uncovered = counts[index] == 0
    counts[index] += delta
    is_uncovered = counts[index] == 0
    return int(is_uncovered) - int(was_uncovered)


def random_search(size, restarts=80, steps=20_000, seed=0):
    rng = random.Random(seed + size)
    universe = set(CANDIDATES)
    best_score = len(FOUR_MASKS) + 1
    best_family = None

    for _ in range(restarts):
        family = set(rng.sample(CANDIDATES, size))
        counts = coverage_counts(tuple(family))
        score = sum(count == 0 for count in counts)
        temperature = 2.0
        for step in range(steps):
            if score == 0:
                assert uncovered_count(tuple(family)) == 0
                return tuple(sorted(family))
            removed = rng.choice(tuple(family))
            added = rng.choice(CANDIDATES)
            while added in family:
                added = rng.choice(CANDIDATES)
            candidate_counts = counts.copy()
            candidate_score = score
            for other in family:
                candidate_score += adjust_pair(
                    candidate_counts, removed, other, -1
                )
            remaining = family - {removed}
            for other in remaining | {added}:
                candidate_score += adjust_pair(
                    candidate_counts, added, other, 1
                )
            delta = candidate_score - score
            if delta <= 0 or rng.random() < math.exp(-delta / temperature):
                family = remaining | {added}
                counts = candidate_counts
                score = candidate_score
            temperature = max(0.03, 2.0 * (1.0 - step / steps))
            if score < best_score:
                best_score = score
                best_family = tuple(sorted(family))

    return None, best_score, best_family


def decode(mask):
    return tuple(vertex for vertex in VERTICES if mask & (1 << vertex))


def main():
    for size in range(15, 11, -1):
        result = random_search(size)
        if isinstance(result, tuple) and len(result) == size:
            print(f"size={size}: exact union-cover witness")
            print([decode(mask) for mask in result])
            return
        _, best_score, best_family = result
        print(f"size={size}: no witness; best uncovered={best_score}")
        print([decode(mask) for mask in best_family])


if __name__ == "__main__":
    main()
