# Research map

This index separates results that apply to the original ordinary model from
results that require stronger universe or structural assumptions.

## Original ordinary model: current endpoints

These are the two directly comparable half-error bounds under $u/n\to\infty$,
arbitrary history dependence, fixed worst-case memory, zero false negatives,
and pointwise false-positive probability.

- Lower endpoint: $H\ge n-o(n)$, the static accepted-set bound.
- Upper endpoint: $H\le2.349083440193\ldots n+o(n)$.
  - [Verified algebraic threshold quotient](./VERIFIED_ALGEBRAIC_THRESHOLD_QUOTIENT_2026_08_13.md)
  - [Hostile audit](./ALGEBRAIC_THRESHOLD_QUOTIENT_HOSTILE_AUDIT_2026_08_13.md)

The finite-parameter optimum is exactly characterized by the randomized
right-congruence variational problem, although this does not yet yield a sharp
asymptotic constant:

- [Right-congruence global variational characterization](./RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md)

## Stronger universe assumption

Under $u/n^2\to\infty$, the unconditional multicut prefix-union theorem gives

$$
H\ge1.198n-o(n)
$$

at half error.

- [Theorem](./MULTICUT_PREFIX_UNION_LOWER_BOUND_2026_08_16.md)
- [Hostile audit](./MULTICUT_PREFIX_UNION_HOSTILE_AUDIT_2026_08_16.md)

This result is not used as the headline lower endpoint for $u/n\to\infty$.

## Additional structural assumption

Under bounded source-section influence (BSSI), the natural-universe theorem
gives

$$
H\ge1.434406361243753\ldots n-o(n).
$$

- [BSSI theorem](./BOUNDED_SOURCE_SECTION_INFLUENCE_NATURAL_UNIVERSE_LOWER_BOUND_2026_08_15.md)
- [BSSI hostile audit](./BOUNDED_SOURCE_SECTION_INFLUENCE_HOSTILE_AUDIT_2026_08_15.md)

This is a useful stability theorem, but BSSI has not been proved for every
ordinary filter.

## General structural tools

The following are unconditional finite-parameter statements, but they do not
by themselves improve the standard-model numerical lower endpoint:

- [Operational avalanche-or-information theorem](./OPERATIONAL_SUPPORT_COMPLETION_AVALANCHE_LOWER_BOUND_2026_08_16.md)
- [Joint transportable-section rank-volume theorem](./JOINT_REPLACEMENT_RANK_VOLUME_LOWER_BOUND_2026_08_16.md)
- [Full-fiber transport-information dichotomy](./FULL_FIBER_TRANSPORT_INFORMATION_DICHOTOMY_2026_08_13.md)

## Main barriers and no-go results

- [Multi-parent excess-information counterexample](./MULTIPARENT_EXCESS_INFORMATION_COUNTEREXAMPLE_2026_08_13.md)
- [Reverse-entropy telescoping audit](./REVERSE_ENTROPY_TELESCOPING_AUDIT_2026_08_13.md)
- [Ordinary belief-state complementarity no-go](./ORDINARY_BELIEF_STATE_COMPLEMENTARITY_NOGO_2026_08_13.md)
- [Rank-$1$ residual-shadow barrier](./JOINT_REPLACEMENT_RANK_VOLUME_LOWER_BOUND_2026_08_16.md#6-rank-1-premium-%E7%9A%84%E4%B8%A5%E6%A0%BC-barrier)

These results explain why raw per-cut entropy deficits, marginal union sizes,
or repeated posterior charging cannot be summed under one $H$-bit budget.

## Verification policy

Scripts in `../scripts/` either verify theorem constants/certificates or explore
candidate directions. Exploratory output is not a theorem without a separate
finite proof and hostile audit.
