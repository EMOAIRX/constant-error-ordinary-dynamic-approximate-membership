#!/usr/bin/env python3
"""Exhaust support patterns for stochastic 12-state rejected-pair WHI.

This searches a necessary condition that is independent of transition
probabilities.  If an input state m occurs for several logical source sets
under the same replacement label, every output in the support of K(m, .)
must be valid for every corresponding target set.  Hence their target-state
supports must have nonempty intersection.

For the K6-minus-perfect-matching family, triples containing an omitted edge
have exactly two available states and FPR <= 1/2 forces both into the Build
support.  Each transversal triple has three available states and may use any
two or all three.  There are only 4^8 = 65,536 patterns.
"""

from itertools import combinations, product


VERTICES = tuple(range(6))
TRIPLES = tuple(combinations(VERTICES, 3))
OMITTED = frozenset({(0, 1), (2, 3), (4, 5)})
STATES = tuple(edge for edge in combinations(VERTICES, 2) if edge not in OMITTED)


def available_states(negative):
    return tuple(state for state in STATES if set(state) <= set(negative))


def support_options(negative):
    available = available_states(negative)
    if len(available) == 2:
        return (frozenset(available),)
    assert len(available) == 3
    return tuple(
        frozenset(option)
        for size in (2, 3)
        for option in combinations(available, size)
    )


def first_obstruction(supports):
    for removed in VERTICES:
        for inserted in VERTICES:
            if removed == inserted:
                continue
            legal_sources = [
                negative
                for negative in TRIPLES
                if inserted in negative and removed not in negative
            ]
            for state in STATES:
                relevant_sources = [
                    negative
                    for negative in legal_sources
                    if state in supports[negative]
                ]
                if not relevant_sources:
                    continue
                common_targets = set(STATES)
                for negative in relevant_sources:
                    target = tuple(
                        sorted((set(negative) - {inserted}) | {removed})
                    )
                    common_targets.intersection_update(supports[target])
                if not common_targets:
                    return removed, inserted, state, tuple(relevant_sources)
    return None


def main():
    options = {negative: support_options(negative) for negative in TRIPLES}
    varying = [negative for negative in TRIPLES if len(options[negative]) > 1]
    fixed = {
        negative: choices[0]
        for negative, choices in options.items()
        if len(choices) == 1
    }

    tested = 0
    witnesses = []
    for choices in product(*(options[negative] for negative in varying)):
        tested += 1
        supports = dict(fixed)
        supports.update(zip(varying, choices))
        if first_obstruction(supports) is None:
            witnesses.append(supports)
            if len(witnesses) == 3:
                break

    print(f"varying transversal triples: {len(varying)}")
    print(f"patterns available: {4 ** len(varying)}")
    print(f"patterns tested: {tested}")
    print(f"support-feasible witnesses found: {len(witnesses)}")
    if witnesses:
        for negative in varying:
            print(negative, sorted(witnesses[0][negative]))


if __name__ == "__main__":
    main()
