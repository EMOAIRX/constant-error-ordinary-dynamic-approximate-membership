# Constant-error ordinary dynamic approximate membership

Research workspace for the fixed-constant-error ordinary dynamic approximate
membership problem left open by Kuszmaul--Liang--Zhou (FOCS 2025).

## Latest result

The newest result is an **unconditional ordinary-model lower-bound
improvement**. For fixed $0<\varepsilon<1$, one-sided pointwise error, free
public randomness, and

$$
\frac{u}{n^2}\longrightarrow\infty,
$$

every fully dynamic filter with $H$ bits of worst-case persistent memory
satisfies

$$
\liminf_{n\to\infty}\frac Hn\ge h_\varepsilon,
$$

where $h_\varepsilon$ is the unique fixed point

$$
h_\varepsilon
=
\int_0^1
(1-2^{-h_\varepsilon/c})
\log_2
\frac{1-2^{-h_\varepsilon/c}}
{\varepsilon-2^{-h_\varepsilon/c}}
\,dc.
$$

At half error,

$$
\boxed{h_{1/2}=1.19810077403325\ldots}
$$

for the integral fixed point. A monotone left-Riemann certificate gives the
rigorous rounded statement

$$
\boxed{H\ge1.198n-o(n).}
$$

This strictly improves the formally proved Lovett--Porat bound
$1.1n-o(n)$ and exceeds their reported recursive value near $1.13$. The proof
does not use their invalid black-box substitution
$H\mapsto M_D(k,\varepsilon)$. It keeps the same unknown global $H$ at every
cut, partitions the suffix into disjoint segments, and counts only

$$
(\text{initial prefix},\text{ final physical state}).
$$

Each segment is charged by the prefix union available before that segment;
the final factor $2^H$ is used exactly once. Fresh-distinct legality is repaired
by a canonical-witness transport bound, which is where the present
$u/n^2\to\infty$ assumption enters.

This is not a twenty-block numerical certificate. With only two suffix
segments and the rational cuts

$$
c_0=\frac7{12},
\qquad
c_1=\frac56,
$$

the same theorem already gives the reviewer-safe explicit bound

$$
\boxed{H\ge1.134n-o(n).}
$$

- [Multicut theorem](./docs/MULTICUT_PREFIX_UNION_LOWER_BOUND_2026_08_16.md)
- [Hostile proof audit](./docs/MULTICUT_PREFIX_UNION_HOSTILE_AUDIT_2026_08_16.md)
- [Half-error verifier](./scripts/verify_multicut_half_error.py)

The previous joint rank-volume theorem remains useful as a replacement-route
structural identity, but it is no longer the latest result:

- [Joint rank-volume theorem](./docs/JOINT_REPLACEMENT_RANK_VOLUME_LOWER_BOUND_2026_08_16.md)
- [Joint rank-volume hostile audit](./docs/JOINT_REPLACEMENT_RANK_VOLUME_HOSTILE_AUDIT_2026_08_16.md)
- [Previous operational avalanche theorem](./docs/OPERATIONAL_SUPPORT_COMPLETION_AVALANCHE_LOWER_BOUND_2026_08_16.md)

## Strongest conditional numerical theorem

The strongest numerical result remains the natural-universe lower bound for
filters with **bounded source-section influence (BSSI)**.

For an ordinary one-sided dynamic filter with fixed $H$-bit persistent memory,
free public randomness, pointwise false-positive probability at most
$\varepsilon$, superlinear operation horizon, and

$$
u/n\longrightarrow\infty,
$$

BSSI implies

$$
H\ge C_{\rm end}(\varepsilon)n-o(n),
$$

where

$$
C_{\rm end}(\varepsilon)
=\min_{0<x<1}\max\left\{
\log_2\frac1{\varepsilon x},
(1-\varepsilon x)
\log_2\frac{1-\varepsilon x}{\varepsilon(1-x)}
\right\}.
$$

At half error,

$$
\boxed{H\ge1.434406361243753\ldots n-o(n).}
$$

This is a structural universe-range improvement, not a deeper finite-block
numerical certificate. The proof uses only the two endpoint pivots.

- [BSSI theorem](./docs/BOUNDED_SOURCE_SECTION_INFLUENCE_NATURAL_UNIVERSE_LOWER_BOUND_2026_08_15.md)
- [BSSI hostile audit](./docs/BOUNDED_SOURCE_SECTION_INFLUENCE_HOSTILE_AUDIT_2026_08_15.md)

## Is this the general ordinary-model solution?

**It is a genuine unconditional ordinary-model improvement, but it is not the
final sharp solution.**

The new fixed-point theorem, whose half-error coefficient is numerically
$1.198100774\ldots$, permits arbitrary history dependence, multiple
representations, nonmonotone query sets, ghosts, holonomy, and public-coin
reliability allocation. It uses no BSSI or history-independence assumption.
Its current universe hypothesis is

$$
u/n^2\to\infty.
$$

What remains open is to weaken this to the full natural-universe regime
$u/n\to\infty$, determine the sharp constant, and understand whether the
optimal half-error coefficient reaches the fingerprint upper endpoint.

The BSSI theorem below remains a stronger conditional result in the wider
$u/n\to\infty$ regime.

BSSI permits:

- arbitrary history dependence and multiple representations;
- nonmonotone query sets, holonomy, ghosts, and global certificates;
- arbitrary public-coin reliability allocation, including highly correlated
  tapes.

It additionally requires that, at every relevant KLZ cut, source-prefix
witnesses cover the full operational union and that revealing one fresh suffix
insertion destroys only bounded expected union mass. We have not proved that
every low-space ordinary filter satisfies this condition.

The support-completion and joint rank-volume theorems remain possible tools for
reducing the universe requirement or improving the coefficient, but they are
not needed for the new unconditional multicut bound.

## Repository layout

- `docs/`: theorems, audits, counterexamples, literature notes, and research
  handoffs.
- `scripts/`: exact verifiers and exploratory programs.
- `README.md`: current result, theorem boundary, and entry points.

## Start here

- [Current research handoff](./docs/NEW_THREAD_HANDOFF_2026_08_14.md)
- [Community-level status](./docs/COMMUNITY_CLOSE_RESEARCH_VERDICT_2026_08_14.md)
- [General lower-bound target and barriers](./docs/SUBEXP_HORIZON_WIDTH_TARGET_AND_LINEAR_SYNDROME_BARRIER_2026_08_14.md)
- [Sharp subexponential-horizon upper bound](./docs/SUBEXPONENTIAL_HORIZON_FINGERPRINT_UPPER_BOUND_AUDIT_2026_08_14.md)
- [Exact right-congruence formulation](./docs/RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md)

## Verification

Run the main theorem verifiers from the repository root:

```bash
bash scripts/run_theorem_verifiers.sh
python3 scripts/verify_endpoint_batch_constant.py
python3 scripts/verify_multicut_half_error.py
```

Exploratory scripts are not proofs. Numerical observations are promoted to
theorems only after a separate exact certificate and hostile model audit.
