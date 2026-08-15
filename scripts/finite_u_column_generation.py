"""Column generation for finite-horizon ordinary dynamic AMQ automata.

The master LP mixes deterministic public-tape transducers.  The pricing MILP
finds a deterministic q-state transducer minimizing a dual-weighted sum of
false positives, while enforcing zero false negatives on every history node.
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from fractions import Fraction

import numpy as np

extra = "/private/tmp/dynamic-amq-scipy"
if os.path.isdir(extra):
    sys.path.insert(0, extra)
from scipy.optimize import Bounds, LinearConstraint, linprog, milp
from scipy.sparse import coo_matrix, csr_matrix, hstack


@dataclass(frozen=True)
class Node:
    parent: int
    operation: int
    set_mask: int


def build_histories(universe: int, capacity: int, depth: int) -> list[Node]:
    nodes = [Node(-1, -1, 0)]
    frontier = [0]
    for _ in range(depth):
        new_frontier = []
        for parent in frontier:
            mask = nodes[parent].set_mask
            if mask.bit_count() < capacity:
                for key in range(universe):
                    if not (mask >> key) & 1:
                        nodes.append(Node(parent, key, mask | (1 << key)))
                        new_frontier.append(len(nodes) - 1)
            for key in range(universe):
                if (mask >> key) & 1:
                    nodes.append(Node(parent, universe + key, mask ^ (1 << key)))
                    new_frontier.append(len(nodes) - 1)
        frontier = new_frontier
    return nodes


class PricingMILP:
    def __init__(self, universe: int, states: int, nodes: list[Node]):
        self.u, self.q, self.nodes = universe, states, nodes
        self.fp = [
            (node, key)
            for node, record in enumerate(nodes)
            for key in range(universe)
            if not (record.set_mask >> key) & 1
        ]
        n_nodes, operations = len(nodes), 2 * universe
        offset = 0
        self.s = np.arange(offset, offset + n_nodes * states).reshape(n_nodes, states)
        offset += n_nodes * states
        self.f = np.arange(offset, offset + operations * states * states).reshape(
            operations, states, states
        )
        offset += operations * states * states
        self.a = np.arange(offset, offset + states * universe).reshape(states, universe)
        offset += states * universe
        self.e = np.arange(offset, offset + len(self.fp))
        offset += len(self.fp)
        self.variables = offset

        rows, cols, data, lower, upper = [], [], [], [], []
        row = 0

        def add(entries, lo=-np.inf, hi=np.inf):
            nonlocal row
            for col, value in entries:
                rows.append(row); cols.append(int(col)); data.append(value)
            lower.append(lo); upper.append(hi); row += 1

        for node in range(n_nodes):
            add([(self.s[node, state], 1) for state in range(states)], 1, 1)
        add([(self.s[0, 0], 1)], 1, 1)
        for operation in range(operations):
            for source in range(states):
                add([(self.f[operation, source, target], 1) for target in range(states)], 1, 1)
        for child, record in enumerate(nodes[1:], start=1):
            for source in range(states):
                for target in range(states):
                    add([
                        (self.s[record.parent, source], 1),
                        (self.f[record.operation, source, target], 1),
                        (self.s[child, target], -1),
                    ], hi=1)
        for node, record in enumerate(nodes):
            for key in range(universe):
                if (record.set_mask >> key) & 1:
                    for state in range(states):
                        add([(self.s[node, state], 1), (self.a[state, key], -1)], hi=0)
        for index, (node, key) in enumerate(self.fp):
            for state in range(states):
                add([
                    (self.s[node, state], 1),
                    (self.a[state, key], 1),
                    (self.e[index], -1),
                ], hi=1)
        matrix = coo_matrix((data, (rows, cols)), shape=(row, self.variables)).tocsr()
        self.constraint = LinearConstraint(matrix, np.asarray(lower), np.asarray(upper))
        self.bounds = Bounds(np.zeros(self.variables), np.ones(self.variables))
        self.integrality = np.ones(self.variables)

    def price(self, weights: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
        objective = np.zeros(self.variables)
        objective[self.e] = weights
        result = milp(
            objective,
            integrality=self.integrality,
            bounds=self.bounds,
            constraints=self.constraint,
            options={"time_limit": 120, "mip_rel_gap": 0},
        )
        if not result.success:
            raise RuntimeError(result.message)
        assignment = np.argmax(result.x[self.s], axis=1)
        accepted = np.zeros(self.q, dtype=np.uint64)
        for node, state in enumerate(assignment):
            accepted[state] |= np.uint64(self.nodes[node].set_mask)
        pattern = np.asarray(
            [int((accepted[assignment[node]] >> np.uint64(key)) & np.uint64(1))
             for node, key in self.fp], dtype=np.uint8
        )
        transition = np.argmax(result.x[self.f], axis=2).astype(np.uint8)
        return float(weights @ pattern), pattern, transition


def master(columns: list[np.ndarray]):
    matrix = np.column_stack(columns).astype(float)
    count = matrix.shape[1]
    objective = np.r_[np.zeros(count), 1.0]
    result = linprog(
        objective,
        A_ub=hstack([csr_matrix(matrix), -np.ones((matrix.shape[0], 1))]),
        b_ub=np.zeros(matrix.shape[0]),
        A_eq=np.r_[np.ones(count), 0.0][None, :],
        b_eq=[1.0],
        bounds=[(0, None)] * count + [(0, 1)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return result, -result.ineqlin.marginals


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--universe", type=int, default=6)
    parser.add_argument("--capacity", type=int, default=3)
    parser.add_argument("--states", type=int, default=4)
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--seed-columns", type=int, default=0)
    parser.add_argument("--seed-random", type=int, default=0)
    parser.add_argument("--checkpoint")
    parser.add_argument("--certificate")
    args = parser.parse_args()
    nodes = build_histories(args.universe, args.capacity, args.depth)
    pricing = PricingMILP(args.universe, args.states, nodes)
    transitions = []
    if args.checkpoint and os.path.exists(args.checkpoint):
        saved = np.load(args.checkpoint)
        columns = [column.copy() for column in saved["columns"]]
        if "transitions" in saved:
            transitions = [item.copy() for item in saved["transitions"]]
        while len(transitions) < len(columns):
            transitions.insert(0, np.zeros((2 * args.universe, args.states), dtype=np.uint8))
    else:
        columns = [np.ones(len(pricing.fp), dtype=np.uint8)]
        transitions = [np.zeros((2 * args.universe, args.states), dtype=np.uint8)]
    seen = {column.tobytes() for column in columns}
    print(f"nodes={len(nodes)} fp={len(pricing.fp)} vars={pricing.variables}")
    # A one-column all-YES master has extremely degenerate dual optima.  Seed
    # it by pricing individual constraints and reproducible positive weights.
    # These are ordinary valid columns; they do not change the master LP.
    for index in range(min(args.seed_columns, len(pricing.fp))):
        weights = np.zeros(len(pricing.fp))
        weights[index] = 1.0
        _, pattern, transition = pricing.price(weights)
        key = pattern.tobytes()
        if key not in seen:
            seen.add(key); columns.append(pattern); transitions.append(transition)
    rng = np.random.default_rng(20260813)
    for _ in range(args.seed_random):
        weights = rng.exponential(size=len(pricing.fp))
        weights /= weights.sum()
        _, pattern, transition = pricing.price(weights)
        key = pattern.tobytes()
        if key not in seen:
            seen.add(key); columns.append(pattern); transitions.append(transition)
    print(f"seeded_columns={len(columns)}")
    for iteration in range(args.iterations):
        result, dual = master(columns)
        value, pattern, transition = pricing.price(dual)
        print(f"iteration={iteration} master={result.fun:.12g} pricing={value:.12g} columns={len(columns)}")
        if value >= result.fun - 1e-8:
            print("certified finite-horizon optimum", result.fun)
            support = np.flatnonzero(result.x[:-1] > 1e-9)
            dual_support = np.flatnonzero(dual > 1e-9)
            print(f"primal_support={len(support)} dual_support={len(dual_support)} dual_sum={dual.sum():.12g}")
            for index in dual_support:
                node, key = pricing.fp[index]
                path = []
                cursor = node
                while cursor:
                    path.append(nodes[cursor].operation)
                    cursor = nodes[cursor].parent
                path.reverse()
                rational = Fraction(float(dual[index])).limit_denominator(1000000)
                print(
                    f"  y={dual[index]:.12g} rational={rational} "
                    f"path={path} query={key}"
                )
            if args.certificate:
                np.savez_compressed(
                    args.certificate,
                    optimum=np.asarray(result.fun),
                    columns=np.asarray(columns, dtype=np.uint8),
                    transitions=np.asarray(transitions, dtype=np.uint8),
                    primal_weights=result.x[:-1],
                    dual_weights=dual,
                    fp=np.asarray(pricing.fp, dtype=np.int64),
                    node_parent=np.asarray([node.parent for node in nodes], dtype=np.int64),
                    node_operation=np.asarray([node.operation for node in nodes], dtype=np.int64),
                    node_set_mask=np.asarray([node.set_mask for node in nodes], dtype=np.uint64),
                )
            break
        key = pattern.tobytes()
        if key in seen:
            raise RuntimeError("pricing returned a duplicate improving column")
        seen.add(key); columns.append(pattern); transitions.append(transition)
        if args.checkpoint:
            np.savez_compressed(
                args.checkpoint,
                columns=np.asarray(columns, dtype=np.uint8),
                transitions=np.asarray(transitions, dtype=np.uint8),
            )


if __name__ == "__main__":
    main()
