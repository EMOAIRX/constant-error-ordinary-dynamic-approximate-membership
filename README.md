# Constant-error ordinary dynamic approximate membership

Research workspace for the fixed-constant-error ordinary dynamic approximate
membership problem left open by Kuszmaul--Liang--Zhou (FOCS 2025).

## Latest result

The newest structural result is an **operational support-completion and
avalanche-or-information theorem**.  It applies to the full ordinary model at a
single replacement cut: arbitrary history dependence, multiple
representations, nonmonotone queries, ghosts, holonomy, and public-coin
reliability allocation are all allowed.

For a uniform `t`-set source, a self-contained random suffix, parent full-fiber
union size `w`, successor transport loss `L`, static support information `A`, and
suffix-source information `J`, it proves

\[
t\,\mathbb E\log_2\frac{w}{w-L}
\le H-A+J.
\]

Consequently, if

\[
\Pr[L\ge\theta w]\ge\tau,
\]

then, in the natural-universe regime with `J=o(t)`,

\[
H\ge t\left[
\log_2\frac1\varepsilon
+\tau\log_2\frac1{1-\theta}
\right]-o(t).
\]

Thus a constant operational avalanche gives a genuine lower-bound premium
over the Carter rate without BSSI or source-cover completeness.  The proof's
infinitesimal support completion accounts for source-invisible operational
ghosts at vanishing entropy cost while retaining their full-union deficit.

- [Full theorem](./docs/OPERATIONAL_SUPPORT_COMPLETION_AVALANCHE_LOWER_BOUND_2026_08_16.md)
- [Hostile proof audit](./docs/OPERATIONAL_SUPPORT_COMPLETION_HOSTILE_AUDIT_2026_08_16.md)

## Strongest numerical theorem

The strongest numerical result remains the natural-universe lower bound for
filters with **bounded source-section influence (BSSI)**.

For an ordinary one-sided dynamic filter with fixed `H`-bit persistent memory,
free public randomness, pointwise false-positive probability at most
`epsilon`, superlinear operation horizon, and

\[
u/n\longrightarrow\infty,
\]

BSSI implies

\[
H\ge C_{\rm end}(\varepsilon)n-o(n),
\]

where

\[
C_{\rm end}(\varepsilon)
=\min_{0<x<1}\max\left\{
\log_2\frac1{\varepsilon x},
(1-\varepsilon x)
\log_2\frac{1-\varepsilon x}{\varepsilon(1-x)}
\right\}.
\]

At half error,

\[
\boxed{H\ge1.434406361243753\ldots n-o(n).}
\]

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

The new support-completion theorem removes source-invisible ghosts as a
single-cut obstruction: a large avalanche is already paid by excess state
information.  What remains is the opposite regime.  An unrestricted
counterexample must maintain small operational avalanches across many
recurrent replacement cuts without paying equivalent joint response width or
false-positive cost.

The matching arbitrary-filter lower bound remains open. The main target is a
replacement-response width theorem, equivalently a stationary causal
one-sided Poisson rate-distortion theorem with labeled successor closure.

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
