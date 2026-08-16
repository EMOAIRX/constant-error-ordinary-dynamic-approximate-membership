# Constant-error ordinary dynamic approximate membership

Research workspace for the fixed-constant-error ordinary dynamic approximate
membership problem left open by Kuszmaul--Liang--Zhou (FOCS 2025).

## Latest result

The newest structural result is a **joint transportable-section rank-volume
lower bound**. It applies to arbitrary history-dependent ordinary filters with
multiple representations, ghosts, holonomy, nonmonotone queries, and
public-coin reliability allocation. It does not require BSSI.

For a uniform $t$-set source, let $w$ be the full operational-fiber union size.
Choose source members to delete and nonmembers to insert, and let
$\Delta^{(d)}$ be the resulting residual $d$-shadow rank deficit. For every
$1\le d\le t-a$, the theorem proves

$$
H\ge
\log_2\binom ut
-\mathbb E\log_2\binom wt
+\mathbb E\Delta^{(d)}.
$$

After the pointwise-FPR bound, in the natural-universe regime this becomes

$$
H\ge
t\log_2\frac1\varepsilon
+\mathbb E\Delta^{(d)}
-o(t).
$$

The replacement labels and untouched survivors are encoded jointly, so the
previous suffix-source mutual-information penalty disappears exactly rather
than being assumed small. The hierarchy interpolates from query-visible union
rank at $d=1$ to full operational-support count at $d=t-a$. The entropy proof
uses parent operational sections; fixed-word transport makes those sections
available at candidate-specific successors, but successor FPR has not yet
been used to force the premium positive.

There is also a sharp boundary: an operational family with only $O(\log u)$
sets can have $\Delta^{(1)}=0$ for every one-for-one replacement section.
Therefore rank-1 union geometry alone cannot yield a universal premium. The
next target is to prove that extensive recurrent replacements expose some
higher residual shadow as future rank-1 query behavior, or to construct a
right-congruent counterexample.

- [Joint rank-volume theorem](./docs/JOINT_REPLACEMENT_RANK_VOLUME_LOWER_BOUND_2026_08_16.md)
- [Hostile proof audit](./docs/JOINT_REPLACEMENT_RANK_VOLUME_HOSTILE_AUDIT_2026_08_16.md)
- [Previous operational avalanche theorem](./docs/OPERATIONAL_SUPPORT_COMPLETION_AVALANCHE_LOWER_BOUND_2026_08_16.md)

## Strongest numerical theorem

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

**No.** The BSSI numerical theorem is effective and fairly broad, but it is
still conditional.

BSSI permits:

- arbitrary history dependence and multiple representations;
- nonmonotone query sets, holonomy, ghosts, and global certificates;
- arbitrary public-coin reliability allocation, including highly correlated
  tapes.

It additionally requires that, at every relevant KLZ cut, source-prefix
witnesses cover the full operational union and that revealing one fresh suffix
insertion destroys only bounded expected union mass. We have not proved that
every low-space ordinary filter satisfies this condition.

The support-completion theorem removes source-invisible ghosts as a single-cut
obstruction. The newer joint rank-volume theorem also removes the
suffix-source-information penalty and exposes a hierarchy of higher-order
residual deficits. What remains is to force one of those deficits to become
linear under extensive recurrent replacement, using only point-query
semantics and one persistent-state budget.

The matching arbitrary-filter lower bound remains open. The main target is a
recurrent residual-shadow exposure or cylinder-recursion width theorem for the
full labeled right-congruence action.

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
python3 scripts/verify_ten_block_160_certificate.py
```

Exploratory scripts are not proofs. Numerical observations are promoted to
theorems only after a separate exact certificate and hostile model audit.
