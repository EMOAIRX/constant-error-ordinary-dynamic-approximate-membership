#!/usr/bin/env python3
"""Heuristic search for a 15-state static mixed-mask filter at n=4.

For each negative four-set N, the available physical states are rejected
masks Z contained in N.  The best pointwise rejection probability is

    max_distribution min_{v in N} Pr[v in Z]
      = min_{q in simplex(N)} max_Z q(Z).

The right-hand side is a four-variable LP.  ``local_game_value`` enumerates
all vertices of its epigraph exactly up to floating-point linear algebra.
Local mask-pattern values are cached, so the outer simulated annealing can
search arbitrary mixtures of mask sizes 1 through 4.

A reported witness is exhaustively rechecked on all 70 negative sets.
Failure is heuristic, not a lower bound.
"""

from itertools import combinations
import math
import random

import numpy as np


VERTICES = tuple(range(8))
NEGATIVES = tuple(combinations(VERTICES, 4))
CANDIDATES = tuple(
    mask
    for mask in range(1, 1 << 8)
    if 1 <= mask.bit_count() <= 4
)
VALUE_CACHE = {}


def local_pattern(family, negative):
    global_negative = sum(1 << vertex for vertex in negative)
    key = 0
    for mask in family:
        if mask & ~global_negative:
            continue
        local = 0
        for index, vertex in enumerate(negative):
            if mask & (1 << vertex):
                local |= 1 << index
        key |= 1 << local
    return key


def local_game_value(pattern):
    """Return min_{q in Delta_4} max_{Z in pattern} q(Z)."""
    if pattern in VALUE_CACHE:
        return VALUE_CACHE[pattern]
    masks = [mask for mask in range(16) if pattern & (1 << mask)]
    if not masks:
        VALUE_CACHE[pattern] = 0.0
        return 0.0

    # Variables are q_0,...,q_3,t.  Besides sum q=1, a vertex has four
    # active inequalities chosen from q_i=0 and q(Z)-t=0.
    active_rows = []
    for coordinate in range(4):
        row = np.zeros(5)
        row[coordinate] = 1
        active_rows.append((row, 0.0))
    for mask in masks:
        row = np.zeros(5)
        for coordinate in range(4):
            if mask & (1 << coordinate):
                row[coordinate] = 1
        row[4] = -1
        active_rows.append((row, 0.0))

    best = float("inf")
    sum_row = np.array([1.0, 1.0, 1.0, 1.0, 0.0])
    for chosen in combinations(active_rows, 4):
        matrix = np.vstack([sum_row] + [item[0] for item in chosen])
        rhs = np.array([1.0] + [item[1] for item in chosen])
        try:
            solution = np.linalg.solve(matrix, rhs)
        except np.linalg.LinAlgError:
            continue
        q = solution[:4]
        t = solution[4]
        if np.min(q) < -1e-9:
            continue
        if any(
            sum(q[i] for i in range(4) if mask & (1 << i)) > t + 1e-9
            for mask in masks
        ):
            continue
        best = min(best, t)

    assert best < float("inf")
    VALUE_CACHE[pattern] = best
    return best


def family_score(family):
    values = [
        local_game_value(local_pattern(family, negative))
        for negative in NEGATIVES
    ]
    deficits = [max(0.0, 0.5 - value) for value in values]
    return sum(value > 1e-9 for value in deficits), sum(deficits), min(values)


def search(size=15, restarts=2, steps=200, seed=0):
    rng = random.Random(seed)
    best = None
    candidate_set = set(CANDIDATES)
    for _ in range(restarts):
        family = set(rng.sample(CANDIDATES, size))
        score = family_score(family)
        temperature = 0.2
        for step in range(steps):
            if score[0] == 0:
                assert family_score(family)[2] >= 0.5 - 1e-9
                return tuple(sorted(family)), score
            removed = rng.choice(tuple(family))
            added = rng.choice(CANDIDATES)
            while added in family:
                added = rng.choice(CANDIDATES)
            candidate = (family - {removed}) | {added}
            candidate_score = family_score(candidate)
            old_energy = score[0] + score[1]
            new_energy = candidate_score[0] + candidate_score[1]
            delta = new_energy - old_energy
            if delta <= 0 or rng.random() < math.exp(-delta / temperature):
                family = candidate
                score = candidate_score
            temperature = max(0.005, 0.2 * (1.0 - step / steps))
            if best is None or score < best[0]:
                best = score, tuple(sorted(family))
    return None, best


def decode(mask):
    return tuple(vertex for vertex in VERTICES if mask & (1 << vertex))


def main():
    witness, result = search()
    if witness is not None:
        print("15-state static witness found")
        print("score:", result)
        print([decode(mask) for mask in witness])
    else:
        score, family = result
        print("no witness found (heuristic only)")
        print("best score (bad sets, total deficit, min margin):", score)
        print([decode(mask) for mask in family])
    print("cached local games:", len(VALUE_CACHE))


if __name__ == "__main__":
    main()
