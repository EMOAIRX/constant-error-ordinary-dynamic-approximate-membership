# Finite-universe replacement AMQ: research audit

Status: working research memo, 2026-08-11.  Statements are separated into
proved facts, computational evidence, and conjectures.  The note studies a
community-facing problem, not an exposition or a connection to information
thermodynamics.

## 1. The real scenario

A service maintains exactly `n` live identifiers from a known dense namespace
`U`.  A typical event evicts one live identifier `x` and activates one absent
identifier `y`.  The service publishes or replicates a compact one-sided
membership filter:

- a live identifier must never be reported absent;
- an absent identifier may be reported present with probability at most
  `epsilon`, causing an unnecessary backing-store lookup;
- a memory snapshot should reveal the current live set, but not the sequence
  of replacements that produced it.

Fixed capacity is natural for caches, shard-local object directories, slot
allocators, and replicated admission sets.  The dense-universe regime is not
the usual Bloom-filter asymptotic regime; it is useful precisely because exact
storage, static approximate storage, and dynamically maintainable storage all
have different constant rates.

The history-independence requirement is a separate axis from update time.  It
does not say that dynamicity is "just hashing": Cuckoo hashing is one possible
implementation mechanism, whereas the model below asks an information-theoretic
state-count question even when computation is free.

## 2. Model

Let

\[
|U|=(1+\lambda)n,\qquad
\Omega=\binom Un.
\]

For every current set `S in Omega`, the stored state has distribution `mu_S`
on a common finite state space `M`.  Query randomness can be removed without
loss.  For a physical state `m`, put

\[
\mathcal F_m=\{S:\mu_S(m)>0\},\qquad
A_m=\bigcup_{S\in\mathcal F_m}S,
\qquad D_m=U\setminus A_m.
\]

The optimal query for `m` answers YES exactly on `A_m`.  Thus there are no
false negatives, and the pointwise false-positive condition is

\[
\Pr_{M\sim\mu_S}[z\in D_M]\ge 1-\varepsilon
\quad\text{for every }S\in\Omega, z\notin S.
\]

In particular,

\[
\mathbb E_{M\sim\mu_S}|D_M|
\ge (1-\varepsilon)(|U|-n)
=(1-\varepsilon)\lambda n.
\]

For a legal replacement define

\[
\tau_{x,y}(S)=S-\{x\}+\{y\},
\qquad x\in S, y\notin S.
\]

For each ordered label `(x,y)`, one common update kernel `K_{x,y}` must satisfy

\[
\mu_S K_{x,y}=\mu_{\tau_{x,y}(S)}
\]

for every source set on which the replacement is legal.  All persistent
random seeds, PRNG state, and metadata count as part of `M`.  Fresh update
randomness is represented by a stochastic kernel.

This is single-snapshot, endpoint or weak history independence.  It is not
strong history independence and is not the unrestricted insert/delete AMQ
model.

Define the worst-case state-count rate

\[
g_{\rm rep}(\lambda,\varepsilon)
=\limsup_{n\to\infty}\frac1n\log_2|\mathcal M_n|,
\]

with superscripts such as `det-WHI` when updates are deterministic.

## 3. The anchor point

The cleanest test case is

\[
|U|=2n,\qquad |S|=n,\qquad \varepsilon=\frac12.
\]

The static finite-universe benchmark is

\[
f_{\rm static}
=2H_2(1/4)-1
=0.622556\ldots\quad\text{bits/key}.
\]

The lower bound is the standard dense one-sided counting/entropy bound.  A
matching upper bound under the present **pointwise** quantifiers needs a
balanced randomized codebook, not merely an unweighted set cover.  One may
sample

\[
\Theta(n)\frac{\binom{2n}{n/2}}{\binom n{n/2}}
\]

rejected `n/2`-subsets as physical states.  For every negative `n`-set, the
compatible sampled incidence vectors must have the all-`1/2` vector in their
convex hull; a halfspace/VC union bound with a sufficiently large constant is
the required existence lemma.  Choosing the corresponding convex weights as
`mu_S` gives pointwise rejection probability `1/2`.  This proof obligation
must be written explicitly; ChainedFilter's average-FPR formulation cannot be
silently substituted for it.

There is a deterministic-update WHI construction with

\[
g_{\rm det-WHI}\le 1.
\]

Fix a partition `U=C_0 disjoint-union C_1` with `|C_0|=|C_1|=n`.  Build
chooses a uniform bit `b` and stores `(b,S cap C_b)`.  Elements outside `C_b`
are answered YES; elements inside it are answered from the stored
intersection.  A nonmember is rejected with probability exactly `1/2`.
Replacement changes only the stored intersection and preserves `b`, so the
endpoint distribution is history independent.  There are `2^(n+1)` states.

The central conjecture is therefore

\[
\boxed{g_{\rm det-WHI}(1,1/2)=1.}
\]

If true, replacement compatibility destroys the last
`0.377444... bits/key` of static chain-rule compression.

For fully stochastic update kernels the corresponding equality is less
certain.  Fresh randomness can sometimes discard and recreate endpoint
randomness, and it cannot be removed without proof.

## 4. What the literature does and does not settle

### Static membership and ChainedFilter

Carter--Floyd--Gill--Markowsky--Wegman initiated exact and approximate
membership testing.  ChainedFilter gives a chain-rule framework spanning
approximate and exact membership and supplies the dense static benchmark used
above.  Its general chain rule is not a theorem about common dynamic update
kernels.  The paper explicitly treats dynamic membership as a separate issue
and falls back to replaceable elementary filters in applications.

### Ordinary dynamic filters

The FOCS 2025 paper *Fingerprint Filters Are Optimal* proves sharp optimality
in its stated small-error, sufficiently large-universe regime.  It does not
cover constant `epsilon` in a dense universe.  The paper identifies the
constant-error regime as an open frontier.  This makes the anchor point above
non-vacuous, but also means that a result must be positioned against the
broader dynamic-filter question rather than advertised as the first dynamic
AMQ lower bound.

### History independence

Naor--Teague, Blelloch--Golovin, and subsequent history-independent hashing
work already provide the abstract idea that the state distribution depends
only on the current logical set.  That abstraction is not new here.  The
unsettled intersection is the exact finite-universe, one-sided state-count rate
under labeled replacements.

### Retrieval/Bloomier filters, local codes, and sketches

Bloomier/retrieval structures return values on members and arbitrary values on
nonmembers.  They are adjacent to AMQs, not simply newer versions of the same
problem.  Value-dynamic retrieval lower bounds are relevant to proof methods.
Malleable, locally updatable, and rewriting codes similarly study nearby
transition constraints, but they do not directly impose the hidden-set common
kernel used here.  Linear turnstile sketches give history-independent local
updates in a restricted algebraic model; their query guarantees are different.

## 5. Structural lemmas that are already rigorous

### 5.1 Label-local Blackwell proportionality

Fix a label `(x,y)` and write a legal source set as `R union {x}`, where

\[
R\in\binom{U\setminus\{x,y\}}{n-1}.
\]

Forward and reverse replacement kernels make the two statistical experiments
`{mu_(R+x)}` and `{mu_(R+y)}` Blackwell-equivalent.  Equality in data
processing implies that whenever

\[
K_{x,y}(m,m')>0,
\]

there is a constant `c_(m,m')>0` such that

\[
\mu_S(m)
=c_{m,m'}\mu_{\tau_{x,y}S}(m')
\quad\text{for every legal source }S.
\]

Consequently,

\[
\tau_{x,y}(\mathcal F_m\cap\Omega_{x,y})
=\mathcal F_{m'}\cap\Omega_{y,x}.
\]

This is stronger than support inclusion.  It is only label-local: it does not
automatically glue the different labels into a global deterministic statistic
or a global permutation action.

### 5.2 Complete-certificate orbit closure

Suppose every state with rejected certificate `D` has the complete fiber

\[
\mathcal F_D=\{S:S\cap D=\varnothing\}.
\]

For `y in D` and `x notin D`, trace equality forces the swapped certificate

\[
D'=(D-\{y\})\cup\{x\}.
\]

The Johnson graph on certificates of fixed size is connected, so a nonempty
system must contain every certificate of that size.  At the anchor certificate
size `n/2`, this costs

\[
\log_2\binom{2n}{n/2}
=1.622556n+o(n),
\]

showing why complete accepted-superset fibers are dynamically expensive.

### 5.3 Frozen-mask lower bound

In the restricted construction where a persistent mask `C` is chosen
independently of `S` and the state records exactly `S cap C`, the FPR condition
forces `E|C| >= n`.  Some positive-weight component therefore has `|C|>=n`
and must realize at least `2^(n-o(n))` feasible intersection patterns.  The
balanced-cut construction is optimal in this frozen/no-drop subclass.

This does not prove the cylinder-fiber or general WHI conjecture: a stochastic
update may drop endpoint information and add it back under the reverse label.

## 6. Computational evidence and its limits

All scripts use exact finite enumeration rather than floating-point
optimization.

### `n=3`, twelve and thirteen deterministic rejected-pair states

[`scripts/rejected_pair_dhi_n3.py`](../scripts/rejected_pair_dhi_n3.py) exhausts the relevant
state families and support assignments:

```text
states=12: infeasible
states=13: infeasible
```

The conclusion is complete only when every physical state rejects a distinct
pair and updates are deterministic.

### `n=3`, selective distinct pair fibers

[`scripts/dhi_n3_pair_fiber_search.py`](../scripts/dhi_n3_pair_fiber_search.py) allows each pair
state to serve any two, three, or four compatible triples and checks exact
support-trace closure:

```text
q=12: 0/455 inventories feasible
q=13: 0/105 inventories feasible
q=14: 0/15 inventories feasible
q=15: 1/1 inventory feasible
```

The formal scope and Johnson-graph proof are in
[`DHI_N3_SUPPORT_AUDIT.md`](DHI_N3_SUPPORT_AUDIT.md).

### A natural twelve-state family also fails for stochastic kernels

[`scripts/stochastic_support_search_n3.py`](../scripts/stochastic_support_search_n3.py) checks all
`4^8=65536` Build support patterns for the `K_6`-minus-perfect-matching family.
Every pattern violates a necessary common-output-support condition for some
state and label.  Thus fresh update randomness does not rescue this natural
twelve-state family.

### Why this is not asymptotic evidence by itself

At the anchor point, a general state must reject `n/2` elements on average.
Pair states are therefore special to tiny `n`; they cannot represent the
asymptotic geometry.  Duplicate masks, mixed rejected-set sizes, likelihood
weights, and stochastic kernel equations remain possible escape routes.

## 7. The missing theorem

For a state `m`, define its selectivity deficit relative to its visible
rejected set:

\[
a_m=log_2\binom{2n-|D_m|}{n}-\log_2|\mathcal F_m|.
\]

Complete fibers have `a_m=0`; cut/intersection states are highly selective.
Let `R(m)` be the state orbit reachable while following legal replacements and
a compatible hidden logical set.  The desired new combinatorial statement has
the form

\[
\log_2|\mathcal R(m)|
\ge \log_2\binom{2n}{|D_m|}
-\kappa a_m-o(n).
\]

Together with the static covering count and
`E|D_M|>=n/2`, an inequality of the right strength would yield the `1` bit/key
lower bound.  Standard Kruskal--Katona shadows count neighboring sets but do
not count distinct posterior rays or enforce compatibility across all labeled
links.  That local-to-global step is the actual technical problem.

The most plausible intermediate class is the cylinder family

\[
\mathcal F_m
=\{S:I_m\subseteq S,\ Z_m\cap S=\varnothing\}.
\]

It contains complete rejected certificates and balanced-cut intersection
states.  A useful theorem must allow endpoint constraints to be dropped and
reintroduced; forbidding that behavior reduces the result to the frozen-mask
lemma.

## 8. Research program and success criteria

### Phase A: falsification before asymptotics

1. Exhaust general deterministic-update `n=3` states with mixed rejected-set
   sizes and duplicate query masks, separating support SAT from probability LP.
2. Solve the first unresolved general-mask instance
   `n=4, |U|=8, |M|<=15`: first the 70 local static LPs, then support
   intersection pruning, then deterministic or stochastic replacement
   equations.  Pair-only states are already known to require 20 states.
3. Search explicitly for cylinder endpoint drop/re-add constructions below the
   balanced-cut state count.
4. For stochastic kernels, solve fixed-support feasibility and look for a
   concrete sub-one-bit family before investing in a general lower bound.

Success means either a genuine counterexample family or a model-complete small
instance theorem.  More pair-state examples are not sufficient.

### Phase B: restricted but meaningful theorem

Prove the `1` bit/key lower bound for all cylinder fibers with arbitrary
endpoint drop/re-add and deterministic updates.  The proof should be stated as
an orbit-versus-selectivity theorem, not as an implementation-specific hashing
argument.

This could be a substantial component of a theory paper if accompanied by the
static/dynamic separation and general-model evidence.  A frozen-mask-only
theorem is too weak as a main result.

### Phase C: main theorem

Prove or refute

\[
g_{\rm det-WHI}(1,1/2)=1,
\]

then determine whether stochastic kernels have the same rate.  A stronger
paper would derive a rate function over `(lambda,epsilon)` and identify when
dense finite-universe behavior joins the large-universe dynamic-filter regime.

## 9. Current verdict

The problem is mathematically coherent and not obviously subsumed by
ChainedFilter, Bloomier filters, Cuckoo hashing, or the FOCS 2025 fingerprint
optimality theorem.  Its best feature is a sharp proposed separation at an
explicit constant-rate anchor:

\[
0.622556\ldots\quad\text{static}
\qquad\text{versus conjecturally}\qquad
1\quad\text{deterministic-update WHI}.
\]

Its main risk is not priority but relevance and tractability: finite-universe
fixed-capacity WHI is narrower than the community's open constant-error
dynamic-filter problem, while fully stochastic common kernels create a real
local-to-global obstruction.  The recommended positioning is therefore:

> use finite-universe replacement as the clean constant-error laboratory for
> the price of transition compatibility, and connect any theorem explicitly
> to the broader dynamic-filter frontier.

Do not call it a direct sequel to ChainedFilter, and do not claim a general
dynamic AMQ optimum until mixed fibers and stochastic kernels are handled.

### Portfolio decision

Among nearby community problems, the recommended order is:

1. **Dense replacement AMQ + deterministic-update WHI** as the current
   tractable main line, with the sharp anchor theorem as a kill criterion.
2. **Constant-error ordinary dynamic filters**, explicitly open after FOCS
   2025, as the highest-impact long-term generalization but a much riskier
   immediate target.
3. **Value-dynamic retrieval and the `n log e` redundancy question** as the
   cleanest backup connecting Bloomier/Xor/ribbon/MPHF work.
4. **Mergeable AMQs and the exact cost of composability** as a promising but
   not yet priority-audited new model.
5. **Adaptive-adversary robust dynamic filters** only later; its many security
   and repair-model branches would currently obscure the information-theoretic
   core.

If no argument survives arbitrary cylinder endpoint drop/re-add after a
bounded proof effort, the right response is to change problems, not to add
resize, adversarial-query, or thermodynamic machinery to rescue the model.

## 10. Core references

- Carter, Floyd, Gill, Markowsky, Wegman, *Exact and Approximate Membership
  Testers*, STOC 1978, DOI: <https://doi.org/10.1145/800133.804332>.
- Li et al., *ChainedFilter: Combining Membership Filters by Chain Rule*,
  PACMMOD/SIGMOD 2024, DOI: <https://doi.org/10.1145/3626721>.
- Lovett, Porat, *A Space Lower Bound for Dynamic Approximate Membership Data
  Structures*, FOCS 2010 / SICOMP 2013, DOI:
  <https://doi.org/10.1137/100806763>.
- Pagh, Segev, Wieder, *How to Approximate a Set Without Knowing Its Size in
  Advance*, FOCS 2013, <https://arxiv.org/abs/1304.1188>.
- Kuszmaul, Walzer, *Space Lower Bounds for Dynamic Filters and Value-Dynamic
  Retrieval*, STOC 2024,
  <https://dblp.org/rec/conf/stoc/KuszmaulW24.html>.
- Kuszmaul, Liang, Zhou, *Fingerprint Filters Are Optimal*, FOCS 2025,
  DOI: <https://doi.org/10.1109/FOCS63196.2025.00055>, arXiv:
  <https://arxiv.org/abs/2510.18129>.
- Naor, Teague, *Anti-Persistence: History Independent Data Structures*,
  STOC 2001.
- Blelloch, Golovin, *Strongly History-Independent Hashing with Applications*,
  FOCS 2007.
- Varshney, Kusuma, Goyal, *Malleable Coding: Compressed Palimpsests*, IEEE
  Transactions on Information Theory 2012.
