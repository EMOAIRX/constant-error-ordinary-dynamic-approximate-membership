#!/usr/bin/env python3
"""Exhaustive check for small deterministic-DHI rejected-pair filters.

Model:
  * U = {0, ..., 5}; the current set has size 3.
  * A physical state is a rejected pair R.  Query returns NO exactly on R.
  * For each negative triple N = U \\ S, Build uses a distribution on
    available pairs R subset N.
  * Updates are deterministic functions F[x,y] on physical states, shared by
    every logical set for which replacement x -> y is legal.

For a 12- or 13-state family that can meet pointwise FPR <= 1/2, some
negative triple has exactly two available pairs.  Its distribution is forced
to be uniform on those pairs.  Deterministic forward and reverse updates
preserve the atom weights, so every negative triple must use a uniform
two-pair support.  The search therefore chooses two available pairs for each
negative triple and checks whether every shared F[x,y] can map source supports
bijectively to target supports.

The script first enumerates *all* 12- and 13-edge state families satisfying
the necessary static condition.  They form one relabeling orbit in each size:
the omitted edges are respectively a matching of size 3 or size 2.  Since the
dynamic feasibility problem is invariant under relabeling, one representative
of each orbit is exhaustively searched.
"""

from itertools import combinations, product


VERTICES = tuple(range(6))
ALL_EDGES = tuple(combinations(VERTICES, 2))
TRIPLES = tuple(combinations(VERTICES, 3))


def edges_in(triple, family):
    return tuple(edge for edge in combinations(triple, 2) if edge in family)


def is_matching(edges):
    endpoints = [vertex for edge in edges for vertex in edge]
    return len(endpoints) == len(set(endpoints))


def classify_families(state_count):
    """Return every family passing the necessary static FPR condition."""
    feasible = []
    for chosen in combinations(ALL_EDGES, state_count):
        family = frozenset(chosen)
        if all(len(edges_in(triple, family)) >= 2 for triple in TRIPLES):
            feasible.append(family)
    return feasible


def kernel_exists(family, supports, removed_member, inserted_member):
    """Check one deterministic update for ``removed_member -> inserted_member``.

    The old negative triple contains ``inserted_member`` and not
    ``removed_member``.  The new negative triple replaces ``inserted_member``
    by ``removed_member``.
    """
    domains = {}
    must_differ = []

    for negative in TRIPLES:
        if inserted_member not in negative or removed_member in negative:
            continue

        target_negative = tuple(
            sorted((set(negative) - {inserted_member}) | {removed_member})
        )
        source_support = tuple(supports[negative])
        target_support = set(supports[target_negative])

        # Uniform two-point distributions push forward correctly exactly when
        # the two source states map bijectively onto the two target states.
        for state in source_support:
            if state not in domains:
                domains[state] = set(family)
            domains[state].intersection_update(target_support)
        must_differ.append(source_support)

    if any(not domain for domain in domains.values()):
        return False

    variables = sorted(domains, key=lambda state: len(domains[state]))
    assignment = {}

    def backtrack(index):
        if index == len(variables):
            return True

        state = variables[index]
        for image in domains[state]:
            collision = False
            for left, right in must_differ:
                if state == left and right in assignment:
                    collision |= assignment[right] == image
                if state == right and left in assignment:
                    collision |= assignment[left] == image
                if collision:
                    break
            if collision:
                continue

            assignment[state] = image
            if backtrack(index + 1):
                return True
            del assignment[state]

        return False

    return backtrack(0)


def assignment_is_dynamic(family, supports):
    return all(
        kernel_exists(family, supports, removed_member, inserted_member)
        for removed_member in VERTICES
        for inserted_member in VERTICES
        if removed_member != inserted_member
    )


def search_representative(family):
    options = {}
    for negative in TRIPLES:
        available = edges_in(negative, family)
        options[negative] = tuple(
            frozenset(pair) for pair in combinations(available, 2)
        )

    candidate_count = 1
    for negative in TRIPLES:
        candidate_count *= len(options[negative])

    ordered_options = [options[negative] for negative in TRIPLES]
    tested = 0
    for choices in product(*ordered_options):
        tested += 1
        supports = dict(zip(TRIPLES, choices))
        if assignment_is_dynamic(family, supports):
            return candidate_count, tested, supports

    return candidate_count, tested, None


def main():
    representatives = {
        12: frozenset(ALL_EDGES)
        - frozenset({(0, 1), (2, 3), (4, 5)}),
        13: frozenset(ALL_EDGES) - frozenset({(0, 1), (2, 3)}),
    }

    for state_count in (12, 13):
        families = classify_families(state_count)
        omitted_size = len(ALL_EDGES) - state_count

        assert families
        assert all(
            is_matching(set(ALL_EDGES) - set(family)) for family in families
        )
        assert all(
            len(set(ALL_EDGES) - set(family)) == omitted_size
            for family in families
        )

        representative = representatives[state_count]
        assert representative in families

        candidate_count, tested, witness = search_representative(representative)

        print(f"states={state_count}")
        print(f"  all statically admissible families: {len(families)}")
        print(f"  omitted edges form a matching of size: {omitted_size}")
        print("  admissible relabeling classes: 1")
        print(f"  support assignments in representative: {candidate_count}")
        print(f"  support assignments tested: {tested}")
        print(f"  deterministic DHI witness found: {witness is not None}")
        print(f"  conclusion: {'feasible' if witness else 'infeasible'}")


if __name__ == "__main__":
    main()
