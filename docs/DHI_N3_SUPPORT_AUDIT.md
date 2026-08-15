# Support audit for `n=3`, `|U|=6`, `epsilon=1/2`

This note isolates a finite support-level calculation. It does not prove a
general lower bound for randomized DHI filters.

## Complete rejected-pair fibers

For a pair `D subset U`, define the complete fiber

\[
\mathcal F_D=\{S\in\tbinom U3:S\cap D=\varnothing\}.
\]

It contains the four triples inside `U \ D`. Suppose every representation
state is of this form. Let `R` be the collection of rejected pairs present as
states.

### Johnson-graph closure lemma

If `R` is nonempty and satisfies the DHI support-trace condition, then

\[
R=\binom U2.
\]

Consequently at least 15 states are required in this subclass.

**Proof.** Take `D in R`, `y in D`, and `x notin D`. The label `(x,y)` is legal
on a nonempty part of `F_D`. After replacing `x` by `y`, its restricted target
trace is the restriction of the complete fiber whose rejected pair is

\[
D'=(D-\{y\})\cup\{x\}.
\]

For a complete rejected-pair target fiber, equality of restricted traces
forces exactly this `D'`: outside `{x,y}` the rejected coordinates must agree,
the target cannot reject `y`, and its second rejected coordinate must be `x`.
Thus `D' in R`.

The graph on two-subsets in which pairs are adjacent when one element is
exchanged is the connected Johnson graph `J(6,2)`. Hence a nonempty collection
closed under every such exchange contains all `binom(6,2)=15` pairs. QED.

## The 24 obstructions for the twelve-state candidate

The symmetric candidate removes the perfect matching

\[
\{01,23,45\}
\]

from the 15 pair masks. Every edge of `J(6,2)` from a retained pair to a
missing pair is a support obstruction. A vertex of `J(6,2)` has degree eight,
and the three missing matching edges are pairwise nonadjacent. The number of
obstructions is therefore

\[
3\cdot 8=24.
\]

For example, from rejected pair `12` under label `0 -> 2`, the three source
sets

\[
034,\quad035,\quad045
\]

are sent to

\[
234,\quad235,\quad245.
\]

Their complete pair-fiber target would reject `01`, one of the removed masks.

More generally, if a set `M` of pair masks is missing, the complete-fiber cut
contains

\[
8|M|-2E_{J(6,2)}(M)
\]

edges, where `E_{J(6,2)}(M)` is the number of Johnson edges internal to `M`.

## Selective pair fibers

The script [scripts/dhi_n3_pair_fiber_search.py](../scripts/dhi_n3_pair_fiber_search.py) checks a
strictly larger but still limited class:

1. There are exactly `q` states and their rejected pairs are distinct.
2. A state with rejected pair `D` may use any two, three, or four of the four
   triples disjoint from `D`. Any two distinct such triples already have union
   `U \ D`, so its actual rejected set remains exactly `D`.
3. For every state and every replacement label with a nonempty source trace,
   at least one state must have exactly the required restricted target trace.

For a fixed inventory, each state has 11 possible fibers. The program uses
sound domain propagation followed by exhaustive branching. At a fully assigned
leaf it has checked every required trace equality, so the search is complete
for the class above.

On the current machine, a representative run prints:

```text
q=12: feasible inventories 0/455; 5.790s
q=13: feasible inventories 0/105; 2.076s
q=14: feasible inventories 0/15; 0.838s
q=15: feasible inventories 1/1; 0.903s
```

The full run takes roughly ten seconds. Exact timings are printed by the
script and depend on the machine.

This computation does **not** cover:

- two states with the same rejected pair but different fibers;
- states rejecting zero, one, or three elements;
- representation probabilities or the `epsilon=1/2` inequalities;
- proportional likelihood-column constraints;
- common stochastic-kernel weights.

It therefore cannot be extrapolated to a general 12-, 13-, or 14-state DHI
lower bound.

## A necessary condition beyond complete fibers

Let a state have actual rejected pair `D`, take `y in D`, `x notin D`, and put

\[
P=(D-\{y\})\cup\{x\}.
\]

If its source slice for `(x,y)` contains at least two triples, the corresponding
two target triples have union `U \ P`. Any matching output state must therefore
accept all of `U \ P`, so its rejected set is a subset of `P`.

Thus a selective construction has only three possibilities:

1. provide a state that rejects the swapped pair `P`;
2. route through a weak state rejecting at most one element of `P`;
3. thin the source fiber until this source slice contains at most one triple.

For every logical set `S`, the pointwise false-positive constraints imply the
aggregate rejection inequality

\[
\sum_m \mu_S(m)|D_m|\ge \frac32.
\]

Consequently weak routing states cannot carry arbitrary probability mass. This
is the first constraint that must be combined with support trace closure in a
general 13/14-state search.

## SAT/MILP formulation

For a general finite search, use binary variables

\[
Y_{m,S}=1 \iff \mu_S(m)>0.
\]

The rejected-coordinate variables are determined by

\[
R_{m,z}=1 \iff Y_{m,S}=0\text{ for every }S\ni z.
\]

For each label `e=(x,y)`, source state `m`, and possible target state `m'`, a
binary trace-matching variable can enforce

\[
Y_{m',T}=Y_{m,\tau_e^{-1}T}
\qquad(T\in\Omega_{y,x}).
\]

Every nonempty source slice needs at least one matching target. This is a SAT
support layer.

After fixing supports, introduce probabilities `p[S,m]`. Static feasibility is
an LP:

\[
\sum_m p_{S,m}=1,
\qquad
\sum_{m:R_{m,z}=1}p_{S,m}\ge\frac12
\quad(z\notin S).
\]

To make `Y` denote exact rather than possible support, one may maximize a
common positive lower bound `delta` subject to `p[S,m] >= delta Y[m,S]`, or
prune zero entries and rerun the support search.

For deterministic update functions, binary transition variables can be
combined with `p[S,m]` using standard product linearization, giving an MILP.
For genuinely stochastic common kernels, the constraints

\[
p_{\tau S,m'}=\sum_m p_{S,m}K_e(m,m')
\]

are bilinear. Flow variables additionally require rank-one/common-conditional
constraints, so this case is not an LP or MILP without discretization or a
nonlinear exact solver.

## Evidentiary value

The 24-obstruction calculation rules out one natural symmetric candidate. The
exhaustive selective-pair calculation rules out a meaningful larger subclass.
Neither is strong evidence by itself for an asymptotic `1 bit/key` theorem,
because mixed rejected-set sizes and duplicate masks are precisely the devices
that a smaller stochastic construction might exploit. A genuine small-instance
theorem requires exhausting those cases and the probability/kernel equations.
