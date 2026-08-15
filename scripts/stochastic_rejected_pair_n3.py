#!/usr/bin/env python3
r"""Convex-feasibility checks for stochastic WHI on 12 states at n=3.

The universe is split into the omitted perfect matching 01, 23, 45.  A
physical state is any other pair and rejects exactly its two endpoints.
For a negative triple N = U \ S, Build is initially taken to be uniform on
the available state-pairs contained in N.  For each ordered replacement
label x -> y, an independent row-stochastic kernel K[x,y] must simultaneously
push every legal source distribution to its target distribution.

This is a genuine linear feasibility problem once the Build distributions
are fixed.  Fresh randomness used by K is not stored after the update; the
resulting physical state is the complete persistent state.
"""

from itertools import combinations

from fractions import Fraction

import numpy as np


VERTICES = tuple(range(6))
TRIPLES = tuple(combinations(VERTICES, 3))
OMITTED = frozenset({(0, 1), (2, 3), (4, 5)})
STATES = tuple(edge for edge in combinations(VERTICES, 2) if edge not in OMITTED)
STATE_INDEX = {state: index for index, state in enumerate(STATES)}


def build_distribution(negative):
    available = [state for state in STATES if set(state) <= set(negative)]
    result = np.zeros(len(STATES))
    for state in available:
        result[STATE_INDEX[state]] = 1.0 / len(available)
    return result


BUILD = {negative: build_distribution(negative) for negative in TRIPLES}


def pointwise_rejection_probabilities(negative):
    distribution = BUILD[negative]
    return {
        vertex: sum(
            distribution[index]
            for index, state in enumerate(STATES)
            if vertex in state
        )
        for vertex in negative
    }


def stochastic_kernel(removed_member, inserted_member):
    """Numerically minimize ||P K - Q|| over row-stochastic K.

    This is projected gradient descent on a convex quadratic.  A returned
    near-zero residual is a candidate witness, not by itself an exact proof;
    ``exact_residual`` below rationalizes and checks the candidate.
    """
    state_count = len(STATES)
    source_rows = []
    target_rows = []
    for negative in TRIPLES:
        if inserted_member not in negative or removed_member in negative:
            continue
        target = tuple(
            sorted((set(negative) - {inserted_member}) | {removed_member})
        )
        source_rows.append(BUILD[negative])
        target_rows.append(BUILD[target])

    source_matrix = np.asarray(source_rows)
    target_matrix = np.asarray(target_rows)
    kernel = np.full((state_count, state_count), 1.0 / state_count)
    step = 1.0 / (np.linalg.norm(source_matrix, 2) ** 2)

    for iteration in range(20_000):
        gradient = source_matrix.T @ (source_matrix @ kernel - target_matrix)
        candidate = kernel - step * gradient
        kernel = project_rows_to_simplex(candidate)
        if iteration % 100 == 0:
            residual = np.max(np.abs(source_matrix @ kernel - target_matrix))
            if residual < 1e-12:
                break

    residual = np.max(np.abs(source_matrix @ kernel - target_matrix))
    return kernel, residual


def project_rows_to_simplex(matrix):
    """Euclidean projection of every matrix row onto the simplex."""
    ordered = np.sort(matrix, axis=1)[:, ::-1]
    cumulative = np.cumsum(ordered, axis=1) - 1
    indices = np.arange(1, matrix.shape[1] + 1)
    positive = ordered - cumulative / indices > 0
    rho = positive.sum(axis=1) - 1
    threshold = cumulative[np.arange(matrix.shape[0]), rho] / (rho + 1)
    return np.maximum(matrix - threshold[:, None], 0)


def rationalize(kernel, max_denominator=120):
    return [
        [Fraction(float(value)).limit_denominator(max_denominator) for value in row]
        for row in kernel
    ]


def exact_residual(kernel, removed_member, inserted_member):
    for row in kernel:
        if any(value < 0 for value in row) or sum(row) != 1:
            return False
    for negative in TRIPLES:
        if inserted_member not in negative or removed_member in negative:
            continue
        target = tuple(
            sorted((set(negative) - {inserted_member}) | {removed_member})
        )
        source_support = [
            STATE_INDEX[state]
            for state in STATES
            if set(state) <= set(negative)
        ]
        target_support = [
            STATE_INDEX[state]
            for state in STATES
            if set(state) <= set(target)
        ]
        for output_state in range(len(STATES)):
            actual = sum(kernel[index][output_state] for index in source_support)
            actual /= len(source_support)
            expected = Fraction(int(output_state in target_support), len(target_support))
            if actual != expected:
                return False
    return True


def main():
    minimum_rejection = min(
        probability
        for negative in TRIPLES
        for probability in pointwise_rejection_probabilities(negative).values()
    )
    print(f"states: {len(STATES)}")
    print(f"minimum pointwise rejection probability: {minimum_rejection:.12g}")

    feasible = []
    infeasible = []
    for removed_member in VERTICES:
        for inserted_member in VERTICES:
            if removed_member == inserted_member:
                continue
            kernel, residual = stochastic_kernel(removed_member, inserted_member)
            exact_kernel = rationalize(kernel)
            is_exact = residual < 1e-10 and exact_residual(
                exact_kernel, removed_member, inserted_member
            )
            (feasible if is_exact else infeasible).append(
                (removed_member, inserted_member)
            )

    print(f"feasible ordered labels: {len(feasible)} / 30")
    print(f"infeasible ordered labels: {infeasible}")


if __name__ == "__main__":
    main()
