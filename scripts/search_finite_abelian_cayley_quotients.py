"""Search small finite-Abelian Cayley quotients for half-error filters.

Candidate finder only: profiles are enumerated exactly with integer walk
counts, while Poisson calibration and the OGF saddle use floating point.
"""

from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass


Element = tuple[int, ...]


@dataclass(frozen=True)
class Candidate:
    rate: float
    factors: tuple[int, ...]
    subset: tuple[Element, ...]
    load: float
    saddle: float
    state_counts: tuple[int, ...]
    rejection_numerators: tuple[int, ...]
    rejection_denominators: tuple[int, ...]


def add(x: Element, y: Element, factors: tuple[int, ...]) -> Element:
    return tuple((a + b) % modulus for a, b, modulus in zip(x, y, factors))


def neg(x: Element, factors: tuple[int, ...]) -> Element:
    return tuple((-a) % modulus for a, modulus in zip(x, factors))


def profile(
    factors: tuple[int, ...], subset: tuple[Element, ...]
) -> tuple[list[int], list[int], list[int]]:
    zero = tuple(0 for _ in factors)
    reachable = {zero}
    walk_counts = {zero: 1}
    counts = [1]
    rejection_numerators = [1]
    rejection_denominators = [1]
    alphabet = len(subset)
    group_order = math.prod(factors)

    for load in range(1, group_order + 1):
        previous = reachable
        reachable = {
            add(syndrome, symbol, factors)
            for syndrome in previous
            for symbol in subset
        }
        next_counts: dict[Element, int] = {}
        for syndrome, multiplicity in walk_counts.items():
            for symbol in subset:
                successor = add(syndrome, symbol, factors)
                next_counts[successor] = next_counts.get(successor, 0) + multiplicity
        walk_counts = next_counts

        rejected_pairs = 0
        for syndrome, multiplicity in walk_counts.items():
            rejected_symbols = sum(
                add(syndrome, neg(symbol, factors), factors) not in previous
                for symbol in subset
            )
            rejected_pairs += multiplicity * rejected_symbols
        counts.append(len(reachable))
        rejection_numerators.append(rejected_pairs)
        rejection_denominators.append(alphabet ** (load + 1))

        if len(reachable) == len(previous):
            assert rejected_pairs == 0
            return counts, rejection_numerators, rejection_denominators

    raise AssertionError("finite sumset did not stabilize")


def rejection_values(numerators: list[int], denominators: list[int]) -> list[float]:
    return [a / b for a, b in zip(numerators, denominators)]


def poisson_rejection(load: float, rejection: list[float]) -> float:
    term = math.exp(-load)
    total = term * rejection[0]
    for c in range(1, len(rejection)):
        term *= load / c
        total += term * rejection[c]
    return total


def bisect_root(function, lower: float, upper: float) -> float:
    lower_value = function(lower)
    if lower_value == 0.0:
        return lower
    if lower_value * function(upper) >= 0.0:
        raise ValueError("root is not bracketed")
    for _ in range(100):
        middle = (lower + upper) / 2.0
        middle_value = function(middle)
        if lower_value * middle_value <= 0.0:
            upper = middle
        else:
            lower = middle
            lower_value = middle_value
    return (lower + upper) / 2.0


def ogf(z: float, counts: list[int]) -> float:
    cutoff = len(counts) - 1
    return sum(counts[c] * z**c for c in range(cutoff)) + (
        counts[-1] * z**cutoff / (1.0 - z)
    )


def ogf_mean(z: float, counts: list[int]) -> float:
    cutoff = len(counts) - 1
    numerator = sum(c * counts[c] * z**c for c in range(cutoff))
    numerator += counts[-1] * (
        cutoff * z**cutoff / (1.0 - z)
        + z ** (cutoff + 1) / (1.0 - z) ** 2
    )
    return numerator / ogf(z, counts)


def evaluate(factors: tuple[int, ...], subset: tuple[Element, ...]) -> Candidate:
    counts, numerators, denominators = profile(factors, subset)
    rejection = rejection_values(numerators, denominators)
    load = bisect_root(
        lambda value: poisson_rejection(value, rejection) - 0.5, 0.0, 20.0
    )
    saddle = bisect_root(
        lambda value: ogf_mean(value, counts) - load,
        1e-12,
        1.0 - 1e-12,
    )
    rate = (
        math.log(ogf(saddle, counts)) / load - math.log(saddle)
    ) / math.log(2.0)
    return Candidate(
        rate,
        factors,
        subset,
        load,
        saddle,
        tuple(counts),
        tuple(numerators),
        tuple(denominators),
    )


def generated_group(
    factors: tuple[int, ...], subset: tuple[Element, ...]
) -> bool:
    zero = tuple(0 for _ in factors)
    reached = {zero}
    while True:
        expanded = reached | {
            add(x, symbol, factors) for x in reached for symbol in subset
        }
        if expanded == reached:
            return len(reached) == math.prod(factors)
        reached = expanded


def factor_tuples(max_order: int, max_rank: int, include_cyclic: bool):
    if include_cyclic:
        for order in range(2, max_order + 1):
            yield (order,)
    for rank in range(2, max_rank + 1):
        for factors in itertools.combinations_with_replacement(
            range(2, max_order + 1), rank
        ):
            if math.prod(factors) > max_order:
                break
            # Invariant-factor form avoids most isomorphic duplicates.
            if all(b % a == 0 for a, b in zip(factors, factors[1:])):
                yield factors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=36)
    parser.add_argument("--max-rank", type=int, default=3)
    parser.add_argument("--alphabet", type=int, choices=(3, 4), default=3)
    parser.add_argument("--top", type=int, default=30)
    parser.add_argument("--include-cyclic", action="store_true")
    args = parser.parse_args()

    candidates: list[Candidate] = []
    for factors in factor_tuples(args.max_order, args.max_rank, args.include_cyclic):
        elements = list(itertools.product(*(range(value) for value in factors)))
        zero = tuple(0 for _ in factors)
        nonzero = [element for element in elements if element != zero]
        for tail in itertools.combinations(nonzero, args.alphabet - 1):
            subset = (zero, *tail)
            if not generated_group(factors, subset):
                continue
            candidates.append(evaluate(factors, subset))

    candidates.sort(key=lambda candidate: candidate.rate)
    for candidate in candidates[: args.top]:
        rho = tuple(
            a / b
            for a, b in zip(
                candidate.rejection_numerators, candidate.rejection_denominators
            )
        )
        print(
            f"R={candidate.rate:.12f} G={candidate.factors} "
            f"V={candidate.subset} lambda={candidate.load:.9f} "
            f"z={candidate.saddle:.9f} d={candidate.state_counts} "
            f"rho={tuple(round(value, 9) for value in rho)}"
        )


if __name__ == "__main__":
    main()
