#!/usr/bin/env python3
"""Search heterogeneous masked binary-canonical mixtures at epsilon=1/2.

For fixed coefficient saddle z, each block type contributes

    b log A(z),       tracked mass b*lambda,
    rejection b*lambda*J(lambda).

The global constraints are rejection >= 1/2 and tracked mass <= 1.  Thus the
inner optimization is a two-constraint linear program over type atoms.  An
extreme solution has at most two positive atoms.  This script scans threshold
and coordinate atoms, then exactly checks all one- and two-atom LP vertices on
the finite grid.  It is numerical evidence, not an interval certificate.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse
import math


DELTA = 0.5


@dataclass(frozen=True)
class Atom:
    kind: str
    q: int
    p: float
    lam: float
    log_a: float
    mass_per_block: float
    rejection_per_block: float


def log_a_threshold(q: int, z: float) -> float:
    return math.log1p(-(z**q)) - 2.0 * math.log1p(-z)


def rejection_threshold(q: int, p: float, lam: float) -> float:
    total = 0.0
    term = 1.0
    for count in range(q):
        absence = p * (1.0 - p) ** count + (1.0 - p) * p**count
        total += term * absence
        term *= lam / (count + 1.0)
    return math.exp(-lam) * total


def rejection_coordinate(p: float, lam: float) -> float:
    return p * math.exp(-lam * p)


def make_atoms(z: float, max_q: int, p_steps: int, lambda_steps: int, lambda_max: float) -> list[Atom]:
    atoms: list[Atom] = []
    # Log-spaced load grid.  Include loads near zero without using zero itself.
    low = math.log(1e-3)
    high = math.log(lambda_max)
    loads = [math.exp(low + (high - low) * index / (lambda_steps - 1)) for index in range(lambda_steps)]
    for p_index in range(1, p_steps + 1):
        p = 0.5 * p_index / p_steps
        for lam in loads:
            coordinate_rejection = rejection_coordinate(p, lam)
            atoms.append(
                Atom(
                    "coordinate", 0, p, lam,
                    -math.log1p(-z),
                    lam,
                    lam * coordinate_rejection,
                )
            )
            for q in range(2, max_q + 1):
                conditional_rejection = rejection_threshold(q, p, lam)
                atoms.append(
                    Atom(
                        "threshold", q, p, lam,
                        log_a_threshold(q, z),
                        lam,
                        lam * conditional_rejection,
                    )
                )
    return atoms


def dominated_prune(atoms: list[Atom], cost_bins: int = 2000) -> list[Atom]:
    """Keep atoms relevant to low cost / high rejection tradeoffs.

    This is only a performance heuristic.  The final pair check is exact on
    the retained finite set, not on the original continuum.
    """
    by_bin: dict[tuple[int, int], Atom] = {}
    max_cost = max(atom.log_a for atom in atoms)
    for atom in atoms:
        # Normalize by block cost.  One-dimensional mixture geometry is in
        # (mass/cost, rejection/cost); retain the largest rejection per bins.
        mass_ratio = atom.mass_per_block / atom.log_a
        rejection_ratio = atom.rejection_per_block / atom.log_a
        mass_bin = min(cost_bins - 1, int(cost_bins * mass_ratio / (1.0 + mass_ratio)))
        cost_bin = min(cost_bins - 1, int(cost_bins * atom.log_a / max_cost))
        key = mass_bin, cost_bin
        old = by_bin.get(key)
        if old is None or rejection_ratio > old.rejection_per_block / old.log_a:
            by_bin[key] = atom
    return list(by_bin.values())


def solve_one(atom: Atom) -> tuple[float, tuple[tuple[Atom, float], ...]] | None:
    if atom.rejection_per_block <= 0.0:
        return None
    blocks = DELTA / atom.rejection_per_block
    if blocks * atom.mass_per_block > 1.0 + 1e-12:
        return None
    return blocks * atom.log_a, ((atom, blocks),)


def solve_pair(first: Atom, second: Atom) -> tuple[float, tuple[tuple[Atom, float], ...]] | None:
    # Both rejection and mass constraints active.  Other LP vertices are the
    # one-atom solutions checked separately.
    determinant = (
        first.rejection_per_block * second.mass_per_block
        - second.rejection_per_block * first.mass_per_block
    )
    if abs(determinant) < 1e-14:
        return None
    first_blocks = (DELTA * second.mass_per_block - second.rejection_per_block) / determinant
    second_blocks = (first.rejection_per_block - DELTA * first.mass_per_block) / determinant
    if first_blocks < -1e-12 or second_blocks < -1e-12:
        return None
    first_blocks = max(0.0, first_blocks)
    second_blocks = max(0.0, second_blocks)
    cost = first_blocks * first.log_a + second_blocks * second.log_a
    return cost, ((first, first_blocks), (second, second_blocks))


def describe(solution: tuple[float, tuple[tuple[Atom, float], ...]], z: float) -> str:
    cost, support = solution
    rate = (cost - math.log(z)) / math.log(2.0)
    pieces = []
    for atom, blocks in support:
        pieces.append(
            f"{atom.kind}(q={atom.q},p={atom.p:.6g},lambda={atom.lam:.6g},"
            f"b={blocks:.6g},beta={blocks*atom.lam:.6g})"
        )
    return f"z={z:.12g} rate={rate:.12f} " + " + ".join(pieces)


def optimize_at_z(args: argparse.Namespace, z: float):
    atoms = make_atoms(z, args.max_q, args.p_steps, args.lambda_steps, args.lambda_max)
    retained = dominated_prune(atoms, args.prune_bins)
    best = None
    for atom in retained:
        candidate = solve_one(atom)
        if candidate is not None and (best is None or candidate[0] < best[0]):
            best = candidate
    for first_index, first in enumerate(retained):
        for second in retained[first_index + 1 :]:
            candidate = solve_pair(first, second)
            if candidate is not None and (best is None or candidate[0] < best[0]):
                best = candidate
    return best, len(atoms), len(retained)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=12)
    parser.add_argument("--p-steps", type=int, default=40)
    parser.add_argument("--lambda-steps", type=int, default=240)
    parser.add_argument("--lambda-max", type=float, default=12.0)
    parser.add_argument("--z-low", type=float, default=0.35)
    parser.add_argument("--z-high", type=float, default=0.55)
    parser.add_argument("--z-steps", type=int, default=81)
    parser.add_argument("--prune-bins", type=int, default=120)
    args = parser.parse_args()

    best = None
    for index in range(args.z_steps):
        z = args.z_low + (args.z_high - args.z_low) * index / (args.z_steps - 1)
        candidate, total, retained = optimize_at_z(args, z)
        if candidate is not None:
            rate = (candidate[0] - math.log(z)) / math.log(2.0)
            if best is None or rate < best[0]:
                best = rate, z, candidate
    assert best is not None
    rate, z, solution = best
    print(f"grid_atoms={total} retained={retained}")
    print(describe(solution, z))


if __name__ == "__main__":
    main()
