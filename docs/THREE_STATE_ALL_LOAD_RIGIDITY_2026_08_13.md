# Three-state all-load rigidity for relational binary transducers

> Status: finite, tape-wise structural theorem. The argument allows multiple
> representations, nontransitive fibers, ghosts, irreversible updates, and
> arbitrary history dependence. It requires exact load, binary
> label-oblivious local updates, at most three reachable states at every
> positive load, and maximal rejection for every fixed load-two history.

## 1. Model

Fix one deterministic component of the public mixture. The mixture coin is
independent of the IID uniform binary labels assigned to keys. A current local
multiset has load `c` and one-count `k in {0,...,c}`. The persistent state also
records the exact load. Let `Q_c` be the reachable physical states at load
`c`, with

\[
|Q_c|\le 3\qquad(c\ge 1).
\]

Updates use only the inserted/deleted binary label. The maps at adjacent
loads need not be inverses. A one-sided query at a state must accept every
binary symbol appearing in any logical composition represented by that state.

For `q in Q_c`, define its relational composition fiber

\[
K_c(q)=\{k:\text{some legal history of load }c
\text{ and one-count }k\text{ reaches }q\}.
\]

The fibers may overlap and need not define a partition.

Assume every fixed history ending at load two attains the universal binary
one-sided rejection ceiling

\[
\operatorname{Rej}(H)=\frac14.
\tag{1}
\]

The probability in (1) is over the independent uniform binary labels of the
fixed update keys and the fresh query key.

## 2. Load two is forced to be canonical

For any fixed two-key history, the only rejection events allowed by
one-sidedness are

\[
(00,\text{ query }1),\qquad(11,\text{ query }0),
\]

each of probability `1/8`. Equality in (1) therefore forces, for every such
history:

- a state reached with composition `0` accepts only symbol `0`;
- a state reached with composition `1` accepts both symbols;
- a state reached with composition `2` accepts only symbol `1`.

These three query semantics are distinct. Since `|Q_2| <= 3`, there are
exactly three reachable states, denoted

\[
q_{2,0},q_{2,1},q_{2,2},
\]

and every history of one-count `k` reaches the unique state `q_{2,k}`. Thus
history dependence and multiple representations disappear at this layer.

## 3. Load three

Suppose a state `q in Q_3` represents two one-counts `k<l`.

- If `k,l <= 2`, deleting a zero from both logical worlds is legal. The same
  deterministic transition from `q` must reach both `q_{2,k}` and
  `q_{2,l}`, impossible unless `k=l`.
- If `k,l >= 1`, deleting a one similarly forces
  `q_{2,k-1}=q_{2,l-1}`, again impossible unless `k=l`.

Consequently the only distinct compositions that can share a load-three
state are the boundary pair `{0,3}`. Four compositions must be covered by at
most three states, so necessarily

\[
K_3(q_{3,0})=\{0,3\},\qquad
K_3(q_{3,1})=\{1\},\qquad
K_3(q_{3,2})=\{2\}.
\tag{2}
\]

There cannot be additional overlap: it would be one of the forbidden pairs
above. Every state in (2) accepts both symbols. In particular, even the pure
compositions `0` and `3` have zero rejection.

## 4. Induction at every higher load

We prove that for every `c >= 3`:

1. `|Q_c|=3`;
2. every composition `k` reaches a unique state determined by `k mod 3`;
3. every state accepts both binary symbols.

The claim holds at `c=3` by (2). Assume it holds at load `c` and consider
load `d=c+1`.

If one state at load `d` represents distinct compositions `k,l`:

- when `k,l<d`, common deletion of a zero gives the same load-`c` state, so
  the induction hypothesis implies
  \[
  k\equiv l\pmod 3;
  \]
- when `k,l>0`, common deletion of a one gives
  \[
  k-1\equiv l-1\pmod3,
  \]
  hence again `k congruent l mod 3`.

The only pair not tested by either common deletion is the boundary pair
`{0,d}`.

Because `d>=4`, the interior compositions

\[
1,2,\ldots,d-1
\]

contain all three residue classes modulo three. No state can contain interior
compositions from two different residues. Hence these interior compositions
already require three distinct states. Since `|Q_d|<=3`, they exhaust the
entire layer, and each residue has exactly one state. This also rules out
multiple representations of an interior composition: placing one residue in
two states would leave fewer than three states for the three required residue
classes.

The pure endpoint `0` cannot occupy a new singleton state. If it joins a state
containing an interior composition `l`, zero deletion forces `l congruent 0
mod 3`. Thus it joins the residue-zero state, unless it shares only with the
opposite endpoint `d`. But there is no fourth state available. A state
containing both endpoints and an interior composition is possible only when
that interior residue agrees with both `0` and `d`; in all cases this still
places the endpoints in an already occupied residue state. The symmetric
argument places `d` in its residue-`d` state. Therefore every composition has
the unique state indexed by its residue modulo three.

Each residue state contains an interior composition, and every interior
composition contains both symbols. One-sidedness therefore forces every
load-`d` state to accept both symbols. This completes the induction.

The transitions are also forced on reachable states. If `q_{c,r}` denotes the
unique residue-`r` state, one-sided logical correctness gives

\[
I_b(q_{c,r})=q_{c+1,r+b},
\qquad
D_b(q_{c,r})=q_{c-1,r-b},
\tag{3}
\]

whenever the corresponding operation is legal for at least one composition in
the source fiber. Residues are modulo three. Thus there is no residual
history information inside the three physical states: the reachable machine
itself, not only its query rule, is the order-three quotient.

## 5. Theorem and public mixtures

### Theorem

Under the assumptions above,

\[
\boxed{
\operatorname{Rej}(H)=0
\quad\text{for every fixed history }H
\text{ ending at load }c\ge3.
}
\tag{4}
\]

Moreover the composition fibers and all reachable update maps at every
`c>=2` are exactly the one-count modulo-three quotient.

For a public mixture of deterministic label-oblivious transducers whose
mixture coin is independent of the IID binary labels, assume
(1) holds after averaging over the mixture for every fixed load-two history.
The value `1/4` is a tape-wise upper bound. Equality of the average with this
upper bound implies that almost every mixture component attains equality for
that history. Fixed finite-key histories are countable, so intersecting the
corresponding probability-one events shows that almost every component
satisfies the tape-wise hypothesis simultaneously. Applying the theorem to
each component gives (4) for the mixture as well.

The independence qualification is necessary for this reduction. If the
chosen transition table can be correlated with the entire binary label
function through free public randomness, conditioning on the table need not
leave the fixed keys' labels IID uniform; average equality then does not imply
component-wise equality by the argument above. Such a model requires a
same-tape formulation and is outside this theorem.

## 6. Scope

The conclusion fails to follow from `|Q_3|<=3` alone. The load-two equality
is what creates three unique, deletion-distinguishable predecessor states.
It also does not cover a local machine that can read key identities, a global
public tape, or neighboring block states in addition to the binary label. In
that larger model, equal stored local state does not imply equal transition
behavior.

Within the stated relational label-oblivious class, however, a proposed
profile with

\[
d_c=3\ (c\ge2),\qquad \rho_3>0
\]

is impossible. The only all-load continuation is query-equivalent to the
canonical order-three quotient, with

\[
(\rho_1,\rho_2,\rho_3,\ldots)
=\left(\frac12,\frac14,0,0,\ldots\right).
\]
