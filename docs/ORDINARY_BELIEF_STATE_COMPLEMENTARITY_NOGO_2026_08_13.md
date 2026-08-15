# Ordinary belief-state complementarity no-go

> Date: 2026-08-13. Status: finite-parameter barrier theorem. The constructions
> below are ordinary, key-only, fixed-memory dynamic AMQs and support arbitrarily
> long legal histories. Their state spaces are deliberately enormous. They are
> counterexamples to universal proof interfaces, not space-efficient upper bounds.

All logarithms are base two.

## 1. Ordinary model and the proposed complementarity

Let `U` be a finite universe and let the capacity be `n`. A legal history starts
from the empty set, uses `Insert(x)` only when `x` is absent and the resulting
load is at most `n`, and uses `Delete(x)` only when `x` is present. A randomized
ordinary AMQ has a fixed persistent state space, a free read-only public tape,
zero false negatives on every tape, and pointwise false-positive probability at
most `epsilon`: for every fixed legal history `h` and every fixed
`x notin S(h)`,

\[
\Pr_R[\operatorname{Query}_{M_R(h)}(x)=\mathsf{YES}]
\le \varepsilon.
\tag{1}
\]

The interface under audit attempts to charge two quantities to the same state
information:

- a posterior thickness deficit `D`, measuring how thin a source posterior is
  inside an ambient hard list;
- a transport or rank saving `T`, obtained after a legal suffix removes
  incompatible witnesses.

A universal inequality of the schematic form

\[
D+T\le \text{available state information}+o(n)
\tag{2}
\]

would yield a rank--transport complementarity. The results below show that
ordinary AMQ semantics alone cannot imply (2), even with arbitrary-long
replacement closure, multiple representations, and global certificates.

## 2. Belief-state realization theorem

Write

\[
\mathscr S_n=\{S\subseteq U:|S|\le n\},
\qquad
\mathscr B_n=2^{\mathscr S_n}\setminus\{\varnothing\}.
\tag{3}
\]

For a nonempty family `B in mathscr B_n`, define

\[
A(B)=\bigcup_{S\in B}S.
\tag{4}
\]

For a key `x`, define the partial belief transitions

\[
I_x(B)=\{S\cup\{x\}:S\in B,\ x\notin S,\ |S|<n\},
\tag{5}
\]

\[
D_x(B)=\{S\setminus\{x\}:S\in B,\ x\in S\}.
\tag{6}
\]

The transition is needed only when the resulting family is nonempty.

### Theorem 2.1 (belief-state realization)

Fix any nonempty family `C subseteq mathscr S_n`. There is a deterministic
ordinary key-only transducer with the following properties.

1. It has a distinguished state `b_C` whose represented logical worlds are
   exactly `C`.
2. From any reached belief state `b_B`, `Insert(x)` and `Delete(x)` apply (5)
   and (6), respectively.
3. Its query rule is

   \[
   \operatorname{Query}_{b_B}(x)=\mathsf{YES}
   \quad\Longleftrightarrow\quad x\in A(B).
   \tag{7}
   \]

4. Starting from any actual `S in C`, every arbitrarily long legal continuation
   remains defined, the actual current set belongs to the current belief family,
   and there are no false negatives.

Moreover, this belief component can be embedded in a transducer starting from
the empty set: before a prescribed source profile is reached, store the current
set exactly; on first reaching the profile, enter `b_C` if the actual set lies
in `C`, and otherwise remain exact.

**Proof.** Suppose the actual current set `S` belongs to `B`. If a legal
`Insert(x)` is performed, then `x notin S` and `|S|<n`, hence
`S union {x} in I_x(B)`. If a legal `Delete(x)` is performed, then `x in S`,
hence `S setminus {x} in D_x(B)`. Thus the actual world survives every legal
transition, so the reached family is nonempty. Induction over the continuation
proves that the actual current set always belongs to the current belief family.
Equation (7) then gives zero false negatives. The transition depends only on
the current physical state and the update key, so the construction is a
labeled right congruence and supports continuations of arbitrary length.

For the embedding, the exact pre-profile state determines whether the source
profile has been reached and whether its set belongs to `C`. Thereafter use the
belief transitions above. Since `U` and `n` are finite, the union of the exact
and belief state spaces is finite and can be encoded in one fixed-size block.
This proves existence, not a useful space bound. \(\square\)

### Remark 2.2 (sections are operationally realizable)

If `y` is absent from the actual set, the self-contained suffix

\[
\tau_y=(\operatorname{Insert}(y),\operatorname{Delete}(y))
\tag{8}
\]

maps `b_B` to

\[
b_{B^{\neg y}},
\qquad
B^{\neg y}=\{S\in B:y\notin S\}.
\tag{9}
\]

Consequently, arbitrary family sections are not merely posterior thought
experiments: they occur as successor states of a genuine ordinary transducer.

## 3. Pointwise-FPR public-coin mixture

### Theorem 3.1 (exact/lossy mixture)

Let `L` be any deterministic one-sided transducer, including the belief-state
transducer of Theorem 2.1. For every `epsilon in [0,1]`, there is a randomized
ordinary AMQ which supports every legal history supported by `L`, has zero
false negatives, and satisfies (1).

**Construction.** The public tape chooses `Z in {0,1}` with
`Pr[Z=1]=epsilon`. If `Z=0`, maintain the current set exactly. If `Z=1`, run
`L`. Pad the two branches to one fixed persistent block.

**Proof.** Both branches have zero false negatives. For any fixed legal history
and fixed current nonmember, the exact branch rejects. The lossy branch may
answer either way, so

\[
\Pr[\mathsf{FP}]
\le \Pr[Z=1]=\varepsilon.
\tag{10}
\]

The history and query are fixed before averaging over the public tape; no FPR
claim is made after conditioning on `Z` or on a physical state. The state block
is fixed because both finite branch state spaces are preallocated. \(\square\)

### Contribution boundary

Theorem 3.1 can require

\[
\log|\mathscr B_n|
\le |\mathscr S_n|
\tag{11}
\]

bits, which is generally exponential in `n log u`. Neither Theorem 2.1 nor
Theorem 3.1 is a competitive AMQ upper bound. Their role is to show that a
property claimed for every ordinary AMQ must survive arbitrary belief-state
geometry and globally correlated public tapes.

## 4. Uniform `m`-subset tensor counterexample

Fix `m>=2`. Let a block universe `V` have size `2m`, fix a distinguished key
`a in V`, and draw

\[
X\sim\binom Vm
\tag{12}
\]

uniformly. Define the one-bit source state

\[
M=\mathbf 1[a\in X].
\tag{13}
\]

For a realized state `M=z`, let `C_z` be the posterior support and `W_z` its
coordinate union. Thus

\[
C_1=\{S\in\tbinom Vm:a\in S\},
\qquad W_1=V,
\tag{14}
\]

whereas

\[
C_0=\{S\in\tbinom Vm:a\notin S\},
\qquad W_0=V\setminus\{a\}.
\tag{15}

Define the within-union posterior deficit

\[
D_z=\log\binom{|W_z|}{m}-H(X\mid M=z).
\tag{16}

Direct counting gives

\[
D_1
=\log\binom{2m}{m}-\log\binom{2m-1}{m-1}
=1,
\qquad
D_0=0.
\tag{17}

The complementary ambient-support term is

\[
A_z=H(X)-\log\binom{|W_z|}{m},
\tag{18}

so `A_1=0`, `A_0=1`, and pointwise

\[
A_z+D_z=I(X;M)=1.
\tag{19}

Here (19) means that either branch supplies one bit of source information, but
the split between ambient support and within-union thickness is branch
dependent.

### A legal suffix and two exact transport quantities

Condition on `M=1`. Given the actual `X`, draw

\[
Y\mid X
\sim\operatorname{Unif}(V\setminus X).
\tag{20}

Then `Y != a`, and the suffix `tau_Y` from (8) is legal. By Remark 2.2 it maps
the belief family `C_1` to

\[
C_{1,Y}=\{S\in C_1:Y\notin S\}.
\tag{21}

There are two distinct, useful rank losses.

First, the posterior-list shrinkage is

\[
\begin{aligned}
T_{\rm list}
&=\log\frac{|C_1|}{|C_{1,Y}|}\\
&=\log\frac{\binom{2m-1}{m-1}}{\binom{2m-2}{m-1}}\\
&=\log\frac{2m-1}{m}.
\end{aligned}
\tag{22}

Second, the coordinate union changes from `V` to `V setminus {Y}`. Its hard
ambient-rank shrinkage is

\[
\begin{aligned}
T_{\rm union}
&=\log\frac{\binom{2m}{m}}{\binom{2m-1}{m}}\\
&=1\\
&=D_1.
\end{aligned}
\tag{23}

The two quantities must not be conflated: (22) counts surviving posterior
worlds, while (23) ranks all `m`-sets in the surviving coordinate union.

### Exact suffix-information identity

Given `X`, the suffix label `Y` is uniform on `m` nonmembers, hence

\[
H(Y\mid X,M=1)=\log m.
\tag{24}

By symmetry, given `M=1`, `Y` is uniform on the `2m-1` keys other than `a`, so

\[
H(Y\mid M=1)=\log(2m-1).
\tag{25}

Therefore

\[
\boxed{
I(X;Y\mid M=1)
=T_{\rm list}
=\log\frac{2m-1}{m},
\qquad
T_{\rm union}=D_1=1.
}
\tag{26}

In particular `T_list -> 1` as `m -> infinity`. The same one bit which makes
the posterior thin also supports an asymptotically one-bit suffix section.
There is no universal strict complementarity between these quantities.

### Tensorization

Take `b` disjoint copies of the experiment, with independent `X_i`, states
`M_i`, and, on coordinates with `M_i=1`, suffix labels `Y_i`. Embed the product
belief family by Theorem 2.1 and execute the suffixes sequentially; capacity
`bm+1` suffices because each insert-delete pair temporarily raises the load by
only one. The transducer continues to support arbitrary legal updates after
all suffixes.

Let `J={i:M_i=1}`. Conditional on `M=(M_1,...,M_b)`,

\[
\sum_{i\in J}D_i
=\sum_{i\in J}T_{{\rm union},i}
=|J|,
\tag{27}

and

\[
\sum_{i\in J}T_{{\rm list},i}
=\sum_{i\in J}I(X_i;Y_i\mid M_i=1)
=|J|\log\frac{2m-1}{m}.
\tag{28}

Since `E|J|=b/2`, all three totals are linear in `b`. This is an
arbitrary-history ordinary-model counterexample, not a finite-depth artifact.
It shows exactly why a valid inequality must retain suffix-source information:
in this example that term pays the entire list-transport cost.

## 5. Growing parents and the DTC identity

Let `Z` collect public context, including the filter tape when information
quantities are evaluated. Assume

\[
X_1,\ldots,X_b\mid Z
\quad\text{are conditionally independent},
\tag{29}

and let `M` be a common final state. A leave-one-out parent observable has the
form

\[
F_i=f_i(M,Z,X_{-i}).
\tag{30}

For any posterior ambient list `Omega_i`, define

\[
A_i
=H(X_i\mid Z)-\mathbb E\log|\Omega_i|,
\tag{31}

\[
D_i
=\mathbb E\log|\Omega_i|
-H(X_i\mid Z,X_{-i},F_i).
\tag{32}

Then

\[
A_i+D_i
=I(X_i;F_i\mid Z,X_{-i}).
\tag{33}

Data processing and (29) give

\[
\sum_i(A_i+D_i)
\le\sum_iI(X_i;M\mid Z,X_{-i}).
\tag{34}

Define conditional dual total correlation by

\[
\operatorname{DTC}(X\mid M,Z)
=H(X\mid M,Z)
-\sum_iH(X_i\mid X_{-i},M,Z).
\tag{35}

Expanding the mutual informations yields the exact identity

\[
\boxed{
\sum_iI(X_i;M\mid Z,X_{-i})
=I(X;M\mid Z)+\operatorname{DTC}(X\mid M,Z).
}
\tag{36}

Thus the sharp universal leave-one-out bound is

\[
\boxed{
\sum_i(A_i+D_i)
\le I(X;M\mid Z)+\operatorname{DTC}(X\mid M,Z).
}
\tag{37}

Taking `F_i=M` makes the data-processing step an equality, so no smaller
purely information-theoretic right-hand side is possible in general.

Ordinary conditional total correlation cannot replace DTC. For independent
fair bits `B_1,...,B_b` and

\[
M=B_1\oplus\cdots\oplus B_b,
\tag{38}

one has

\[
I(B;M)=1,
\qquad
\operatorname{TC}(B\mid M)=1,
\qquad
\operatorname{DTC}(B\mid M)=b-1,
\tag{39}

while every leave-one-out term equals one. Hence the left side of (36) is
`b`. This parity mechanism admits an ordinary arbitrary-history embedding by
Theorems 2.1 and 3.1; a global certificate may be reused by linearly many
leave-one-out parents.

For any single decode permutation `pi`, no DTC penalty appears:

\[
\sum_{k=1}^b
I(X_{\pi(k)};M\mid Z,X_{\pi(<k)})
=I(X;M\mid Z).
\tag{40}

Therefore the failure occurs when favorable leave-one-out contexts are selected
across different decode permutations and then added without normalized pivot
weights. A convex combination of complete chain rules remains valid.

## 6. Formal no-go theorem

### Theorem 6.1 (ordinary complementarity no-go)

No rank--transport complementarity with a positive universal gap can be
derived solely from the following properties:

1. ordinary key-only updates and queries;
2. zero false negatives and pointwise FPR at most a fixed positive `epsilon`;
3. one fixed persistent state block and a public random tape;
4. arbitrary history dependence, multiple representations, and global
   certificates;
5. support for arbitrarily long legal insert/delete/replacement histories;
6. a common final state from which growingly many parent observables are
   measurable;
7. largeness, overlap, or even uniformity of each individual source posterior
   inside its operational belief fiber.

More precisely:

- Theorems 2.1 and 3.1 realize arbitrary belief-family sections in the full
  ordinary model while preserving (1).
- Equations (17)--(28) give tensor families in which thickness deficit and hard
  union transport use the same linear budget, while list transport is paid
  exactly by suffix-source mutual information.
- Equations (36)--(39) show that growing leave-one-out parents can reuse a
  global certificate through a linear DTC term.

Hence neither

\[
\sum_i(D_i+T_i)
\le I(X;M\mid Z)-\sum_iA_i+o(n)
\tag{41}

nor the same inequality with ordinary conditional TC in place of DTC is a
universal ordinary-AMQ theorem.

**Proof.** The first assertion follows from the realization and mixture
theorems. The uniform-subset tensor violates any strict complementarity which
omits suffix-source information, because (26)--(28) simultaneously approach
equality on a linear number of coordinates. The parity source violates every
leave-one-out bound which omits DTC by (36)--(39). All constructions have
finite preallocated state spaces and support arbitrary legal continuations.
No statement about small state-space size is used. \(\square\)

## 7. Minimal surviving KLZ-specific conjecture

The no-go theorem does not rule out a result which uses the specific random
suffixes and decode order of the KLZ obfuscating tree. The narrow remaining
target is the following.

### Conjecture 7.1 (KLZ operational-section inequality)

For one fixed KLZ decode permutation, or for a normalized convex combination
of complete pivot chains, there exist parent posteriors `mu_j`, a single family
of operational reference measures `nu_j`, and corresponding legal random
suffixes `Y_j` such that

\[
\sum_j\lambda_j
\bigl(D_j+T^{\rm op}_j\bigr)
\le
I(X;M_{\rm final}\mid R,\Theta)
-\sum_j\lambda_jA_j
+\sum_j\lambda_j I(X_j;Y_j\mid\mathcal C_j)
+o(n),
\tag{42}

where:

1. the weights are nonnegative and sum to one across complete pivot chains;
2. `T_j^op` is measured on full operational fibers, not only on source
   posterior supports;
3. the total suffix-source term in (42) is `o(n)` for the KLZ sampling regime;
4. each source posterior is dominated by its operational reference measure
   before and after every relevant suffix section, with total logarithmic
   domination loss `o(n)`;
5. the reference measures satisfy a section anti-concentration or influence
   tensorization strong enough to exclude belief families such as Section 4;
6. the statement averages over the original public tape and permits arbitrary
   per-tape reliability allocation, including ALL-YES tapes.

Conditions 1 and 6 prevent cross-pivot double charging and illegal
tape-conditioned FPR arguments. Conditions 2, 4, and 5 exclude the arbitrary
belief-section realization. Condition 3 excludes the exact equality mechanism
in (26). Removing any of these protections exposes one of the preceding
counterexamples.

Conjecture 7.1 is deliberately KLZ-specific. Ordinary transition compatibility,
growing depth, or source-to-operational thickness without a common
section-stable reference measure is not enough.

## 8. Research verdict

The publishable unconditional result is a barrier theorem:

- arbitrary operational belief geometry is realizable in the ordinary model;
- pointwise FPR permits global exact/lossy tape mixtures;
- uniform posterior thickness does not create rank--transport complementarity;
- leave-one-out parent sums require DTC, not ordinary TC;
- none of these constructions is a low-space upper bound.

The only remaining positive route is to prove a low-information,
section-stable operational inequality for the particular KLZ random suffixes.
Such a result would be a new property of the KLZ experiment, not a consequence
of ordinary AMQ semantics alone.
