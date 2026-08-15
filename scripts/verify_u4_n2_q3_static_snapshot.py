"""Verify the static U=4,n=2,three-state snapshot optimum 5/12."""

from __future__ import annotations

import itertools
import os
import sys

import numpy as np

EXTRA = "/private/tmp/dynamic-amq-scipy"
if os.path.isdir(EXTRA):
    sys.path.insert(0, EXTRA)

from scipy.optimize import linprog
from scipy.sparse import csr_matrix, hstack


def main() -> None:
    pairs = list(itertools.combinations(range(4), 2))
    constraints = [(pair, key) for pair in pairs for key in range(4) if key not in pair]
    columns = []
    for coloring in itertools.product(range(3), repeat=len(pairs)):
        accepted = [0, 0, 0]
        for pair, color in zip(pairs, coloring):
            accepted[color] |= sum(1 << key for key in pair)
        pair_color = dict(zip(pairs, coloring))
        columns.append(
            tuple((accepted[pair_color[pair]] >> key) & 1
                  for pair, key in constraints)
        )
    matrix = np.unique(np.asarray(columns, dtype=np.uint8), axis=0).T.astype(float)
    count = matrix.shape[1]
    result = linprog(
        np.r_[np.zeros(count), 1.0],
        A_ub=hstack([csr_matrix(matrix), -np.ones((len(constraints), 1))]),
        b_ub=np.zeros(len(constraints)),
        A_eq=np.r_[np.ones(count), 0.0][None, :],
        b_eq=[1.0],
        bounds=[(0, None)] * count + [(0, 1)],
        method="highs",
    )
    print(f"colorings={3 ** len(pairs)} unique_columns={count}")
    print(f"optimum={result.fun:.12g}")
    if not result.success or abs(result.fun - 5 / 12) > 1e-9:
        raise SystemExit("FAIL: expected 5/12")
    print("PASS")


if __name__ == "__main__":
    main()
