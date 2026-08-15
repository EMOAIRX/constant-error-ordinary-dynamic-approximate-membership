# Counterexample audit for finite-universe replacement membership

## Model audited

The universe is (U=[2n]), the logical set is an (n)-subset (S), and a
replacement (x\to y) is legal when (x\in S,y\notin S).  A physical state
(m) has a fixed rejected mask (Z_m\subseteq U); equivalently the query says
NO on (Z_m) and YES elsewhere.  One-sidedness requires

\[
\mu_S(m)>0\quad\Longrightarrow\quad Z_m\subseteq U\setminus S.
\]

Pointwise FPR (1/2) is

\[
\Pr_{m\sim\mu_S}[y\in Z_m]\ge \tfrac12
\qquad(S\subseteq U,\ |S|=n,\ y\notin S).
\]

Endpoint/weak history independence with a stochastic update kernel is

\[
\mu_S K_{x,y}=\mu_{S-\{x\}+\{y\}}.
\]

Fresh randomness used while applying (K_{x,y}) is free transient
randomness, but its sampled output and every piece of persistent seed or
metadata are part of the physical state.  Deterministic-update WHI is the
special case in which every row of every (K_{x,y}) is a point mass.

## Exact 12-state stochastic obstruction at (n=3)

Fix the 12 physical states to be the edges of (K_6) after omitting the
perfect matching (01,23,45).  State (e) rejects exactly the two endpoints
of (e).  Write (N=U\setminus S) for a negative triple.

If (N) contains an omitted matching edge, exactly two physical-state edges
lie inside (N).  Pointwise rejection at least (1/2) forces Build to put
probability (1/2) on each, so both are in its support.  If (N) is a
transversal of the three omitted matching edges, all three triangle edges are
available.  Every feasible positive support has size two or three: support
one is impossible, every two-edge support uses weights (1/2,1/2), and a
three-edge support has each edge weight at most (1/2).

For a fixed label (x\to y), use negative-set notation, so a legal source
(N) contains (y) and not (x), and its target is

\[
N' = N-\{y\}+\{x\}.
\]

If an input state (m) occurs in the Build support of several such source
triples, every state (m') with (K_{x,y}(m,m')>0) must occur in the Build
support of every corresponding target triple.  Therefore

\[
\operatorname{supp}K_{x,y}(m,\cdot)
\subseteq
\bigcap_{N:\,m\in\operatorname{supp}\mu_N}
\operatorname{supp}\mu_{N'}.
\]

The intersection must be nonempty because the row of (K) sums to one.  This
is a necessary condition for an arbitrary stochastic kernel; it does not
assume deterministic updates or particular nonzero weights.

There are eight transversal negative triples.  Exhausting their four support
choices (three two-edge supports and the full three-edge support) gives
(4^8=65,536) patterns.  None satisfies the necessary intersection condition
for all labels and input states.  Thus this fixed 12-state query family is
impossible even with fresh update randomness.

Reproduction:

```text
python3 scripts/stochastic_support_search_n3.py
varying transversal triples: 8
patterns available: 65536
patterns tested: 65536
support-feasible witnesses found: 0
```

The result does **not** rule out:

- a different 12-state family of rejected masks;
- masks of sizes other than two;
- duplicate physical states with the same rejected mask but different
  transition roles;
- 13 or 14 states;
- a general construction whose state is not represented by a rejected pair.

The separate script `scripts/stochastic_rejected_pair_n3.py` checks the especially
natural uniform Build distribution.  Exactly the six labels along the
omitted matching are feasible; the other 24 labels are infeasible.  This
numerical convex check is illustrative only; the support enumeration above is
the exact weight-independent result.

## Exact static theorem for pair states at (n=4)

Suppose every physical state rejects exactly a pair.  Let (G) be the graph
whose edges are the available physical states.  For a negative four-set
(N), a Build distribution on (E(G[N])) has four rejection marginals.  Their
sum is exactly two because every sampled state rejects two vertices.  Hence
all four marginals are at least (1/2) iff all four equal (1/2).  Scaling
the edge weights by two gives a fractional perfect matching of (G[N]).

On four vertices a graph has a fractional perfect matching iff it has an
ordinary perfect matching.  One way to see this is that the half-integral
components of a fractional 1-factor are single edges and odd cycles; four
vertices cannot be covered by odd cycles without leaving an isolated vertex.

Let (H=\overline G).  The three perfect matchings of a (K_4) partition its
six edges into three pairs.  A four-set has no perfect matching in (G) iff
(H) hits all three of those matchings.  Choosing one hit from each class
always gives either a triangle or a three-edge star, and each triangle or
three-edge star hits all three classes.  Consequently every four-set has a
perfect matching in (G) iff

\[
H\text{ is triangle-free and }\Delta(H)\le2.
\]

Such an eight-vertex (H) has at most eight edges by the degree bound.  The
cycle (C_8) is triangle-free, has maximum degree two, and has eight edges.
Therefore the exact optimum in the pair-state subclass is

\[
|E(G)|=\binom82-8=20.
\]

It uses

\[
\frac{\log_2 20}{4}=1.080482\ldots
\]

bits per key, so pair states cannot give the desired (n=4,k\le15)
counterexample even before dynamic constraints are imposed.

Reproduction: `python3 scripts/pair_state_graph_n4.py`.

This theorem says nothing about mixed rejected-mask sizes.

## Mixed masks and duplicate masks

For arbitrary rejected masks, static feasibility of a fixed family
(Z_1,\ldots,Z_k\) is a separate four-dimensional LP for every negative set
(N):

\[
\begin{aligned}
&p_{N,m}\ge0,\qquad \sum_m p_{N,m}=1,\\
&p_{N,m}>0\Longrightarrow Z_m\subseteq N,\\
&\sum_{m:v\in Z_m}p_{N,m}\ge\tfrac12
\quad(v\in N).
\end{aligned}
\]

The dual local value is

\[
\max_p\min_{v\in N}\Pr[v\in Z]
=
\min_{q\in\Delta(N)}\max_{m:Z_m\subseteq N}q(Z_m).
\]

`scripts/mixed_mask_static_n4.py` implements this local dual exactly up to numerical
linear algebra and provides a bounded heuristic outer search over 15 masks of
sizes one through four.  It found no witness, but this is not an exhaustive
lower bound.  `scripts/mixed_mask_cover_n4.py` tests the stronger sufficient condition
that every negative four-set is the union of two chosen masks; it also found
no 12--15 mask witness heuristically.

Duplicate query masks do not improve static feasibility: their probability
masses can be aggregated without changing any query marginal.  They can help
dynamics by separating transition contexts, so they must be allowed in a
dynamic search; their cost is one physical state per copy.

## Cylinder drop/re-add audit

A cylinder state is a pair of disjoint certificates

\[
(I,Z),\qquad I\subseteq S,\quad Z\subseteq U\setminus S,
\]

and rejects (Z).  Under (x\to y), the information guaranteed for every
hidden source set in the cylinder is

\[
(I\setminus\{x\})\cup\{y\}
\quad\text{positive},\qquad
(Z\setminus\{y\})\cup\{x\}
\quad\text{negative}.
\]

A kernel may forget parts of these certificates and use fresh randomness,
but it cannot safely add any other element without learning more about the
hidden set.  Repeated drop/re-add therefore needs a stationary replenishment
mechanism; the label supplies only the newly positive (y) and newly negative
(x).  No such mechanism yielding a sub-1-bit state family was found.

There is a clean negative result for the fully permutation-equivariant
cylinder approach.  A complete orbit of states with certificate sizes
((i,z)) has

\[
\binom{2n}{z}\binom{2n-z}{i}
\]

physical states.  Pointwise FPR implies

\[
\mathbb E|Z|\ge n/2,
\]

so a mixture of complete orbits must contain a positive-mass orbit with
(z\ge n/2).  Since (z\le n), the smallest such orbit already has

\[
\binom{2n}{n/2}=2^{1.622556\ldots n-o(n)}
\]

states; adding (I) only increases the count.  This rules out sub-1-bit
constructions only under full permutation-orbit closure, which is much
stronger than WHI.

## Smallest unresolved computational target

No stochastic or deterministic sub-1-bit construction was found.  The first
finite instance not dismissed by the present arguments is

\[
n=4,\quad |U|=8,\quad k\le15,
\]

with arbitrary rejected masks, including duplicate masks when dynamics is
added.

The recommended exact workflow is:

1. Solve the static family problem first.  Choose 15 masks (Z_m\subseteq[8])
   up to permutation and duplicate ordering, and test the 70 local LPs above.
2. If no static family exists, (n=4,k\le15) is closed before WHI.
3. For every surviving family, enumerate feasible Build support patterns and
   apply the stochastic support-intersection obstruction label by label.
4. For deterministic updates, introduce maps (F_{x,y}:[k]\to[k]); after
   fixing these discrete maps, the equations
   \(\mu_NF_{x,y}=\mu_{N'}\) are linear in the Build probabilities.
5. For fully stochastic kernels the joint equations are bilinear in
   \((\mu,K)); support CSP and label-local Blackwell equivalence should be
   used before nonlinear solving.

A finite (n=4) witness would refute a universal exact (k\ge2^n) claim, but
would not by itself refute the asymptotic (g\ge1) conjecture without a valid
tensoring construction that handles arbitrary occupancies across blocks.

## Bottom line

The counterexample search found no viable sub-1-bit route.  Fresh stochastic
update randomness does not rescue the most natural 12-state (n=3)
rejected-pair candidate.  Pair-only states are already statically too
expensive at (n=4).  Fully symmetric cylinder mixtures are asymptotically
far above one bit.  The sharp remaining falsification target is the exact
general-mask (n=4,k\le15) problem, followed by its deterministic and
stochastic transition refinements.
