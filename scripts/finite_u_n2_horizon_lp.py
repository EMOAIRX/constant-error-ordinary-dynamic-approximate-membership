"""Finite-horizon LP audit for one-bit ordinary dynamic AMQs at n=2.

This is a falsification tool, not an asymptotic lower-bound proof.  It
enumerates every deterministic two-state key-only transducer on U=[4].  For
each transducer, zero false negatives force a minimal query mask at each
state.  A public-random-tape filter is a convex combination of these columns.
"""

from __future__ import annotations

import argparse
import itertools
import os
import sys

import numpy as np


def histories(max_depth: int) -> tuple[list[tuple[int, int, int]], list[int]]:
    """Return (parent, operation, set-mask) records for all legal histories."""
    records = [(-1, -1, 0)]
    frontier = [0]
    for _ in range(max_depth):
        new_frontier = []
        for parent in frontier:
            set_mask = records[parent][2]
            size = set_mask.bit_count()
            if size < 2:
                for key in range(4):
                    if not (set_mask >> key) & 1:
                        records.append((parent, key, set_mask | (1 << key)))
                        new_frontier.append(len(records) - 1)
            for key in range(4):
                if (set_mask >> key) & 1:
                    records.append((parent, 4 + key, set_mask ^ (1 << key)))
                    new_frontier.append(len(records) - 1)
        frontier = new_frontier
    return records, frontier


def enumerate_columns(max_depth: int) -> tuple[np.ndarray, list[tuple[int, int]]]:
    records, _ = histories(max_depth)
    strategy_count = 2 * 4**8
    codes = np.arange(strategy_count, dtype=np.uint32) // 2
    initial = (np.arange(strategy_count, dtype=np.uint32) & 1).astype(np.uint8)
    transitions = np.empty((8, strategy_count, 2), dtype=np.uint8)
    for operation in range(8):
        function = ((codes >> (2 * operation)) & 3).astype(np.uint8)
        transitions[operation, :, 0] = function & 1
        transitions[operation, :, 1] = function >> 1

    state = np.empty((len(records), strategy_count), dtype=np.uint8)
    state[0] = initial
    for index, (parent, operation, _) in enumerate(records[1:], start=1):
        previous = state[parent]
        state[index] = transitions[operation, np.arange(strategy_count), previous]

    accepted = np.zeros((2, strategy_count), dtype=np.uint8)
    for index, (_, _, set_mask) in enumerate(records):
        at_one = state[index].astype(bool)
        accepted[1, at_one] |= set_mask
        accepted[0, ~at_one] |= set_mask

    constraints: list[tuple[int, int]] = []
    rows = []
    for index, (_, _, set_mask) in enumerate(records):
        for key in range(4):
            if not (set_mask >> key) & 1:
                constraints.append((index, key))
                rows.append(
                    ((accepted[state[index], np.arange(strategy_count)] >> key) & 1)
                )
    matrix = np.asarray(rows, dtype=np.uint8)
    return matrix, constraints


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=3)
    args = parser.parse_args()

    extra = "/private/tmp/dynamic-amq-scipy"
    if os.path.isdir(extra):
        sys.path.insert(0, extra)
    from scipy.optimize import linprog
    from scipy.sparse import csr_matrix

    matrix, constraints = enumerate_columns(args.depth)
    # Duplicate columns are interchangeable and make the LP unnecessarily big.
    patterns, first = np.unique(matrix, axis=1, return_index=True)
    del first
    column_count = patterns.shape[1]
    print(
        f"depth={args.depth} constraints={len(constraints)} "
        f"strategies={matrix.shape[1]} unique_columns={column_count}"
    )
    # Minimize the worst pointwise FPR.  The last variable is that maximum.
    objective = np.zeros(column_count + 1)
    objective[-1] = 1
    inequalities = np.hstack(
        [patterns.astype(float), -np.ones((len(constraints), 1))]
    )
    result = linprog(
        objective,
        A_ub=csr_matrix(inequalities),
        b_ub=np.zeros(len(constraints)),
        A_eq=np.hstack([np.ones((1, column_count)), np.zeros((1, 1))]),
        b_eq=np.ones(1),
        bounds=[(0, None)] * column_count + [(0, 1)],
        method="highs",
    )
    print(result.message)
    if result.success:
        weights = result.x[:-1]
        support = np.flatnonzero(weights > 1e-9)
        worst = np.max(patterns @ weights)
        print(f"support={len(support)} optimum={result.fun:.12g} worst_fpr={worst:.12g}")
        for column in support:
            print(f"  p={weights[column]:.12g} pattern={patterns[:, column].tolist()}")
        dual = -result.ineqlin.marginals
        dual_support = np.flatnonzero(dual > 1e-9)
        print(f"dual_support={len(dual_support)} dual_sum={dual.sum():.12g}")
        for row in dual_support:
            print(f"  y={dual[row]:.12g} constraint={constraints[row]}")


if __name__ == "__main__":
    main()
