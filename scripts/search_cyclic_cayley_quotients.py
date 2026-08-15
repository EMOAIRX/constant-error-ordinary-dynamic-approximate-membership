"""Search cyclic Cayley accumulators for half-error dynamic membership.

This is a candidate finder, not a proof certificate.  It exactly enumerates
reachable sumsets and random-walk rejection profiles, then numerically solves
the Poisson calibration and fixed-state saddle point.
"""

from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass

@dataclass(frozen=True)
class Candidate:
    rate: float
    modulus: int
    subset: tuple[int, ...]
    load: float
    saddle: float
    state_counts: tuple[int, ...]
    rejection: tuple[float, ...]


def profile(modulus: int, subset: tuple[int, ...]) -> tuple[list[int], list[float]]:
    """Return layers through the first saturated reachable sumset."""
    probability = [0.0] * modulus
    probability[0] = 1.0
    reachable = {0}
    counts = [1]
    rejection = [1.0]

    for load in range(1, modulus + 1):
        previous = reachable
        reachable = {(x + a) % modulus for x in previous for a in subset}
        next_probability = [0.0] * modulus
        for syndrome, mass in enumerate(probability):
            for a in subset:
                next_probability[(syndrome + a) % modulus] += mass / len(subset)
        probability = next_probability

        accepted_mass = 0.0
        for syndrome, mass in enumerate(probability):
            if mass == 0.0:
                continue
            accepted = sum(
                ((syndrome - a) % modulus) in previous for a in subset
            )
            accepted_mass += mass * accepted / len(subset)
        counts.append(len(reachable))
        rejection.append(max(0.0, 1.0 - accepted_mass))

        # Once the sumset stops growing, it is a coset of the generated
        # subgroup.  Every later symbol is accepted and the state count is
        # constant.
        if len(reachable) == len(previous):
            rejection[-1] = 0.0
            return counts, rejection

    raise AssertionError("a finite cyclic sumset must stabilize")


def poisson_rejection(load: float, rejection: list[float]) -> float:
    term = math.exp(-load)
    total = term * rejection[0]
    for c in range(1, len(rejection)):
        term *= load / c
        total += term * rejection[c]
    return total


def calibrated_load(rejection: list[float]) -> float:
    return bisect_root(lambda x: poisson_rejection(x, rejection) - 0.5, 0.0, 20.0)


def bisect_root(function, lower: float, upper: float) -> float:
    lower_value = function(lower)
    upper_value = function(upper)
    if lower_value == 0.0:
        return lower
    if lower_value * upper_value >= 0.0:
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
    prefix = sum(value * z**c for c, value in enumerate(counts[:-1]))
    return prefix + counts[-1] * z ** (len(counts) - 1) / (1.0 - z)


def ogf_mean(z: float, counts: list[int]) -> float:
    cutoff = len(counts) - 1
    value = ogf(z, counts)
    numerator = sum(c * counts[c] * z**c for c in range(cutoff))
    numerator += counts[-1] * (
        cutoff * z**cutoff / (1.0 - z)
        + z ** (cutoff + 1) / (1.0 - z) ** 2
    )
    return numerator / value


def evaluate(modulus: int, subset: tuple[int, ...]) -> Candidate:
    counts, rejection = profile(modulus, subset)
    load = calibrated_load(rejection)
    saddle = bisect_root(
        lambda z: ogf_mean(z, counts) - load,
        1e-12,
        1.0 - 1e-12,
    )
    rate = (math.log(ogf(saddle, counts)) / load - math.log(saddle)) / math.log(2.0)
    return Candidate(
        rate,
        modulus,
        subset,
        load,
        saddle,
        tuple(counts),
        tuple(rejection),
    )


def primitive(subset: tuple[int, ...], modulus: int) -> bool:
    divisor = modulus
    for value in subset:
        divisor = math.gcd(divisor, value)
    return divisor == 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=30)
    parser.add_argument("--max-alphabet", type=int, default=5)
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()

    best: list[Candidate] = []
    for modulus in range(3, args.max_modulus + 1):
        for size in range(2, min(args.max_alphabet, modulus) + 1):
            for tail in itertools.combinations(range(1, modulus), size - 1):
                subset = (0, *tail)
                if not primitive(subset, modulus):
                    continue
                candidate = evaluate(modulus, subset)
                best.append(candidate)
    best.sort(key=lambda item: item.rate)
    for item in best[: args.top]:
        rejection = ",".join(f"{x:.6g}" for x in item.rejection)
        print(
            f"R={item.rate:.12f} m={item.modulus} V={item.subset} "
            f"lambda={item.load:.9f} z={item.saddle:.9f} "
            f"d={item.state_counts} rho=({rejection})"
        )


if __name__ == "__main__":
    main()
