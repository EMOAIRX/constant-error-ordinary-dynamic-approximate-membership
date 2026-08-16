#!/usr/bin/env python3
"""Exact small checks for the joint replacement rank-volume theorem."""

from __future__ import annotations

import itertools
import math


def popcount(value: int) -> int:
    return bin(value).count("1")


def masks_of_size(universe: int, size: int) -> tuple[int, ...]:
    return tuple(
        sum(1 << item for item in subset)
        for subset in itertools.combinations(range(universe), size)
    )


def submasks_of_size(mask: int, size: int) -> tuple[int, ...]:
    items = tuple(index for index in range(mask.bit_length()) if mask >> index & 1)
    return tuple(
        sum(1 << item for item in subset)
        for subset in itertools.combinations(items, size)
    )


def clique_completion_size(
    family: tuple[int, ...], ground: int, residual_size: int, shadow_size: int
) -> int:
    if not family:
        return 0
    shadow = {
        piece
        for member in family
        for piece in submasks_of_size(member, shadow_size)
    }
    return sum(
        all(piece in shadow for piece in submasks_of_size(candidate, shadow_size))
        for candidate in submasks_of_size(ground, residual_size)
    )


def phi(family: tuple[int, ...], universe: int, t: int, d: int) -> int:
    total = 0
    full = (1 << universe) - 1
    for a in range(universe):
        a_mask = 1 << a
        for b in range(universe):
            if a == b:
                continue
            b_mask = 1 << b
            residual = tuple(
                member ^ a_mask
                for member in family
                if member & a_mask and not member & b_mask
            )
            ground = full ^ a_mask ^ b_mask
            total += clique_completion_size(residual, ground, t - 1, d)
    return total


def entropy_bit(probability: float) -> float:
    if probability in (0.0, 1.0):
        return 0.0
    return -probability * math.log2(probability) - (
        1.0 - probability
    ) * math.log2(1.0 - probability)


def verify_joint_volume() -> None:
    universe, t = 5, 3
    layer = masks_of_size(universe, t)
    triple_count = math.comb(universe, t) * t * (universe - t)
    minimum_slack = float("inf")
    checked = 0

    envelope_checks = 0
    for family_bits in range(1, 1 << len(layer)):
        family = tuple(
            member for index, member in enumerate(layer) if family_bits >> index & 1
        )
        union = 0
        for member in family:
            union |= member
        envelope = math.comb(popcount(union), t) * t * (universe - t)
        phi_one = phi(family, universe, t, 1)
        phi_full = phi(family, universe, t, t - 1)
        assert phi_full == len(family) * t * (universe - t)
        assert phi_full <= phi_one <= envelope
        envelope_checks += 1

    # Binary source partitions provide a small sanity check for the
    # entropy/list direction; d=t-1 is exact, while d=1 is its union-rank
    # relaxation.  The general proof does not rely on this enumeration.
    first = layer[0]
    for choice in range(1 << (len(layer) - 1)):
        left = (first,) + tuple(
            layer[index + 1]
            for index in range(len(layer) - 1)
            if choice >> index & 1
        )
        if len(left) == len(layer):
            continue
        left_set = set(left)
        right = tuple(member for member in layer if member not in left_set)
        probability = len(left) / len(layer)
        information = entropy_bit(probability)
        for d in (1, t - 1):
            left_phi = phi(left, universe, t, d)
            right_phi = phi(right, universe, t, d)
            lower_bound = math.log2(triple_count) - (
                probability * math.log2(left_phi)
                + (1.0 - probability) * math.log2(right_phi)
            )
            slack = information - lower_bound
            assert slack >= -1e-12
            minimum_slack = min(minimum_slack, slack)
            checked += 1

    removed = {
        sum(1 << item for item in (0, 1, 4)),
        sum(1 << item for item in (2, 3, 4)),
    }
    sparse = tuple(member for member in layer if member not in removed)
    assert len(sparse) == 8
    assert phi(sparse, universe, t, 1) == triple_count == 60
    assert phi(sparse, universe, t, t - 1) == len(sparse) * t * (universe - t)

    if abs(minimum_slack) < 1e-12:
        minimum_slack = 0.0
    print(
        f"joint-volume families={envelope_checks} partitions={checked} "
        f"minimum_slack={minimum_slack:.12g} "
        f"sparse_phi1={phi(sparse, universe, t, 1)}"
    )


def apply_word(start: int, word: tuple[tuple[int, int], ...], capacity: int):
    state = start
    for operation, label in word:
        present = bool(state >> label & 1)
        if operation == 1:
            if present or popcount(state) == capacity:
                return None
            state |= 1 << label
        else:
            if not present:
                return None
            state ^= 1 << label
    return state


def verify_fixed_word_signature() -> None:
    universe = capacity = 3
    operations = tuple(itertools.product((0, 1), range(universe)))
    checked_pairs = 0
    for length in range(1, 5):
        for word in itertools.product(operations, repeat=length):
            touched = {label for _, label in word}
            first = {label: next(op for op, key in word if key == label) for label in touched}
            last = {label: next(op for op, key in reversed(word) if key == label) for label in touched}
            required_present = {label for label, op in first.items() if op == 0}
            final_present = {label for label, op in last.items() if op == 1}
            for load in range(capacity + 1):
                legal = []
                for start in range(1 << universe):
                    if popcount(start) != load:
                        continue
                    finish = apply_word(start, word, capacity)
                    if finish is not None:
                        legal.append((start, finish))
                        expected = start
                        for label in touched:
                            expected &= ~(1 << label)
                        for label in final_present:
                            expected |= 1 << label
                        assert finish == expected
                        assert all(start >> label & 1 for label in required_present)
                        assert all(
                            not (start >> label & 1)
                            for label in touched - required_present
                        )
                for (left, left_finish), (right, right_finish) in itertools.combinations(
                    legal, 2
                ):
                    assert left ^ right == left_finish ^ right_finish
                    assert not any((left ^ right) >> label & 1 for label in touched)
                    checked_pairs += 1
    print(f"fixed-word common-continuation pairs={checked_pairs}")


if __name__ == "__main__":
    verify_joint_volume()
    verify_fixed_word_signature()
