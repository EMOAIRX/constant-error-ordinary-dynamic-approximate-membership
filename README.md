# Constant-error ordinary dynamic approximate membership

This repository studies the fixed-constant-error ordinary dynamic approximate
membership problem left open by Kuszmaul--Liang--Zhou (FOCS 2025).

## Standard-model frontier

The comparison below uses the same model and the natural universe regime:

- capacity $n$ and $u/n\to\infty$;
- arbitrary-length legal insert/delete histories;
- fixed worst-case persistent memory;
- free public randomness;
- zero false negatives;
- pointwise false-positive probability at most $1/2$.

Let $H^*_{1/2}(n,u)$ be the optimal worst-case memory in this model. The current
proved bounds recorded in this repository are

$$
\boxed{
n-o(n)
\le
H^*_{1/2}(n,u)
\le
2.349083440193\ldots\,n+o(n).
}
$$

| Direction | Bound | Status |
|---|---:|---|
| Lower bound | $H\ge n-o(n)$ | Unconditional Carter/static accepted-set bound |
| Upper bound | $H\le2.349083440193\ldots n+o(n)$ | Unconditional audited order-$3$ algebraic threshold quotient |

The upper construction is an ordinary key-only right congruence. It supports
arbitrary history length, has no overflow state, and satisfies pointwise error.

- [Audited upper-bound theorem](./docs/VERIFIED_ALGEBRAIC_THRESHOLD_QUOTIENT_2026_08_13.md)
- [Hostile upper-bound audit](./docs/ALGEBRAIC_THRESHOLD_QUOTIENT_HOSTILE_AUDIT_2026_08_13.md)
- [Exact right-congruence formulation](./docs/RIGHT_CONGRUENCE_GLOBAL_VARIATIONAL_2026_08_13.md)

## Honest status of the lower bound

There is currently **no proved unconditional coefficient larger than $1$ in
this repository under only $u/n\to\infty$**.

The strongest unconditional improvement proved here is

$$
H\ge1.198n-o(n),
$$

but it requires the stronger universe hypothesis

$$
u/n^2\to\infty.
$$

It therefore does not replace the standard-model lower endpoint above.

- [Large-universe multicut theorem](./docs/MULTICUT_PREFIX_UNION_LOWER_BOUND_2026_08_16.md)
- [Hostile proof audit](./docs/MULTICUT_PREFIX_UNION_HOSTILE_AUDIT_2026_08_16.md)

The $1.434406\ldots$ BSSI theorem and other structural results use additional
hypotheses or prove intermediate inequalities. They are kept in the research
map, not in the standard-model headline interval.

## Repository map

- [Research map and result classification](./docs/README.md)
- `docs/`: theorems, audits, barriers, counterexamples, and research notes.
- `scripts/`: exact verifiers and exploratory programs.

## Verification

Run the theorem verifiers from the repository root:

```bash
bash scripts/run_theorem_verifiers.sh
python3 scripts/verify_multicut_half_error.py
```

Exploratory computations are not treated as proofs. A numerical observation is
promoted only after a finite statement and a hostile model audit are available.
