#!/usr/bin/env python3
"""Exact n=4 obstruction for static pair-state filters below 1 bit/key.

A state is an edge {u,v} and rejects exactly u and v.  For a negative
4-set N, a distribution over edges inside N has rejection probability at
least 1/2 at every vertex iff the induced graph admits a fractional perfect
matching.  On four vertices this is equivalent to containing an ordinary
perfect matching.  Thus the static design problem is: find the fewest edges
in an 8-vertex graph such that every induced 4-set contains a perfect
matching.

Writing H for the complement graph, a four-set has no perfect matching in G
exactly when H contains an edge from each of the three perfect matchings of
K4.  A minimal such transversal is either a triangle or a 3-edge star.
Therefore the condition is equivalent to H being triangle-free with maximum
degree at most two.  Such an 8-vertex H has at most eight edges, and C8 attains
the bound.  Hence G needs exactly 28 - 8 = 20 states, already more than 2^4.
"""

from itertools import combinations


VERTICES = tuple(range(8))
EDGES = tuple(combinations(VERTICES, 2))
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}
FOUR_SETS = tuple(combinations(VERTICES, 4))


def matching_masks(four_set):
    a, b, c, d = four_set
    matchings = (
        ((a, b), (c, d)),
        ((a, c), (b, d)),
        ((a, d), (b, c)),
    )
    return tuple(
        (1 << EDGE_INDEX[tuple(sorted(left))])
        | (1 << EDGE_INDEX[tuple(sorted(right))])
        for left, right in matchings
    )


CONSTRAINTS = tuple(matching_masks(four_set) for four_set in FOUR_SETS)


def violations(graph_mask):
    return sum(
        not any(graph_mask & matching == matching for matching in matchings)
        for matchings in CONSTRAINTS
    )


def is_witness(graph_mask):
    return violations(graph_mask) == 0


def decode(mask):
    return [edge for index, edge in enumerate(EDGES) if mask & (1 << index)]


def main():
    cycle = {(vertex, (vertex + 1) % 8) for vertex in VERTICES}
    cycle = {tuple(sorted(edge)) for edge in cycle}
    witness_edges = set(EDGES) - cycle
    witness_mask = sum(1 << EDGE_INDEX[edge] for edge in witness_edges)
    assert len(cycle) == 8
    assert len(witness_edges) == 20
    assert is_witness(witness_mask)
    print("complement H: C8")
    print("states in G: 20")
    print("all 70 negative four-sets contain a perfect matching: yes")
    print("exact storage log2(20) / 4: {:.12g}".format(np_log2(20) / 4))


def np_log2(value):
    # Keep this script dependency-free.
    from math import log2

    return log2(value)


if __name__ == "__main__":
    main()
