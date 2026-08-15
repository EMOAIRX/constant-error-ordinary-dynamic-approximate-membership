r"""Exact support search for a restricted n=3, |U|=6 DHI model.

The search is complete only for the following class:

* every state has a distinct rejected pair D;
* its logical fiber is any subset of {S: |S|=3, S cap D = empty}
  whose union is U \ D (equivalently, any 2, 3, or 4 of the four
  compatible triples);
* for every state and replacement label with a nonempty source trace,
  some state has exactly the required restricted target trace.

It does not model duplicate rejected pairs, states rejecting 0, 1, or 3
elements, representation probabilities, false-positive inequalities, or
the common-kernel weight equations.
"""

from __future__ import annotations

import itertools
import time


UNIVERSE = frozenset(range(6))
TRIPLES = tuple(frozenset(items) for items in itertools.combinations(UNIVERSE, 3))
TRIPLE_INDEX = {triple: index for index, triple in enumerate(TRIPLES)}
PAIR_MASKS = tuple(frozenset(items) for items in itertools.combinations(UNIVERSE, 2))
LABELS = tuple(itertools.permutations(UNIVERSE, 2))


def fiber_domain(mask: frozenset[int]) -> tuple[frozenset[int], ...]:
    """Return all selective fibers whose actual rejected set is exactly mask."""
    compatible = tuple(
        TRIPLE_INDEX[triple]
        for triple in TRIPLES
        if triple.isdisjoint(mask)
    )
    return tuple(
        frozenset(choice)
        for size in range(2, 5)
        for choice in itertools.combinations(compatible, size)
    )


def source_trace(
    fiber: frozenset[int], label: tuple[int, int]
) -> frozenset[int]:
    x, y = label
    return frozenset(
        TRIPLE_INDEX[frozenset((TRIPLES[index] - {x}) | {y})]
        for index in fiber
        if x in TRIPLES[index] and y not in TRIPLES[index]
    )


def target_slice(
    fiber: frozenset[int], label: tuple[int, int]
) -> frozenset[int]:
    x, y = label
    return frozenset(
        index
        for index in fiber
        if y in TRIPLES[index] and x not in TRIPLES[index]
    )


def inventory_is_feasible(
    masks: tuple[frozenset[int], ...]
) -> tuple[bool, tuple[frozenset[int], ...] | None]:
    """Solve the finite fiber CSP for one inventory of distinct pair masks."""
    domains = tuple(fiber_domain(mask) for mask in masks)
    state_count = len(masks)

    traces = {
        (state, value, label): source_trace(domains[state][value], LABELS[label])
        for state in range(state_count)
        for value in range(len(domains[state]))
        for label in range(len(LABELS))
    }
    slices = {
        (state, value, label): target_slice(domains[state][value], LABELS[label])
        for state in range(state_count)
        for value in range(len(domains[state]))
        for label in range(len(LABELS))
    }

    def propagate(candidate_domains: list[set[int]]) -> bool:
        changed = True
        while changed:
            changed = False
            for source_state in range(state_count):
                impossible = []
                for source_value in candidate_domains[source_state]:
                    value_is_possible = True
                    for label in range(len(LABELS)):
                        trace = traces[source_state, source_value, label]
                        if not trace:
                            continue
                        has_target = any(
                            any(
                                slices[target_state, target_value, label] == trace
                                for target_value in candidate_domains[target_state]
                            )
                            for target_state in range(state_count)
                        )
                        if not has_target:
                            value_is_possible = False
                            break
                    if not value_is_possible:
                        impossible.append(source_value)

                if impossible:
                    candidate_domains[source_state].difference_update(impossible)
                    changed = True
                    if not candidate_domains[source_state]:
                        return False
        return True

    def search(candidate_domains: list[set[int]]) -> list[set[int]] | None:
        if not propagate(candidate_domains):
            return None
        if all(len(domain) == 1 for domain in candidate_domains):
            return candidate_domains

        state = min(
            (
                index
                for index, domain in enumerate(candidate_domains)
                if len(domain) > 1
            ),
            key=lambda index: len(candidate_domains[index]),
        )
        for value in tuple(candidate_domains[state]):
            branch = [set(domain) for domain in candidate_domains]
            branch[state] = {value}
            result = search(branch)
            if result is not None:
                return result
        return None

    solution = search([set(range(len(domain))) for domain in domains])
    if solution is None:
        return False, None
    fibers = tuple(
        domains[state][next(iter(solution[state]))]
        for state in range(state_count)
    )
    return True, fibers


def main() -> None:
    for state_count in (12, 13, 14, 15):
        started = time.perf_counter()
        feasible_inventories = 0
        inventory_count = 0
        for masks in itertools.combinations(PAIR_MASKS, state_count):
            inventory_count += 1
            feasible, _ = inventory_is_feasible(masks)
            feasible_inventories += int(feasible)
        elapsed = time.perf_counter() - started
        print(
            f"q={state_count}: feasible inventories "
            f"{feasible_inventories}/{inventory_count}; {elapsed:.3f}s"
        )


if __name__ == "__main__":
    main()
