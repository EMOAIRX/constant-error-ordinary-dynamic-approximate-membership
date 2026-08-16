# Hostile audit of the multicut prefix-union lower bound

## Verdict

The finite-partition inequality and its integral limit survive the current
hostile audit. The proof gives an unconditional ordinary-model improvement
under $u/n^2\to\infty$.

At $\varepsilon=1/2$ it yields

$$
h_{1/2}=1.19810077403325\ldots
$$

for the integral fixed point, with the rigorously certified rounded corollary
$H\ge1.198n-o(n)$.

A two-segment rational certificate already gives

$$
H\ge1.134n-o(n),
$$

so the breakthrough is not dependent on a twenty-block numerical climb.

## 1. The state budget is not counted repeatedly

The counted object is

$$
(\text{initial prefix},\text{ final physical state}).
$$

For a fixed pair, each suffix segment is bounded by a node-wise branching
factor. These factors multiply because they refer to disjoint input segments.
Intermediate states are neither encoded nor summed over. For the fixed final
state $q$, its accepted set $A(q)$ is also fixed. The only state-count factor
is the final bound

$$
|\{q\}|\le2^H.
$$

Thus there is no hidden $2^{dH}$ or induced-width assumption.

## 2. The segment must use its left endpoint

The union controlling segment $i$ must be $L(P_i)$ from the prefix before that
segment. Using the union after the segment to charge the same segment would be
circular: the child state depends on the labels currently being counted and
would require an intermediate-state factor.

The proved finite sum is therefore the left-endpoint sum

$$
h+c_0\log_2\varepsilon
\ge
\sum_i(c_{i+1}-c_i)
f_\varepsilon(2^{-h/c_i}).
$$

Left and right Riemann sums have the same continuous limit, but only the left
version has the direct tree proof.

## 3. Lovett--Porat recursion is not used

At every cut, the large-union threshold is

$$
\beta_i=2^{-H/k_i+o(1)}.
$$

The same unknown total space $H$ remains in all thresholds. The proof never
replaces $H$ by a lower bound $M_D(k_i,\varepsilon)$. That invalid substitution
would enlarge $\beta_i$ and strengthen the covering bound without
justification.

## 4. Fresh-distinct legality is repaired explicitly

For a prefix union label $y$, choose a canonical distinct witness prefix. The
witness can be transported through the actual suffix unless it intersects
that suffix. Conditional on any prefix,

$$
\mathbb E[|L_i\setminus A|]
\le
|L_i|
\frac{(n-k_i)(k_i-1)}{u-n+1}.
$$

With $u/n^2\to\infty$, Markov makes the lost fraction $o(1)$ simultaneously at
every fixed cut. No repeated-label insertion or illegal concatenation is
silently used.

This audit does not justify replacing $u/n^2\to\infty$ by
$u/n\to\infty$.

## 5. Pointwise FPR is used before fixing the tape

For every fixed full history, pointwise FPR is summed over nonmembers, and
only then are expectations over the public tape and the uniform history
exchanged. A tape with small average final accepted-set size is fixed after
this step.

The proof never conditions the FPR guarantee on a physical state. Claim-8
failures, hypergeometric failures, witness conflicts, and the small-accepted-
set event are all measured on the unconditioned uniform full-history
distribution after the tape has been fixed.

## 6. Path-dependent unions do not break multiplication

Later prefix unions may depend arbitrarily on earlier segment labels. For each
current tree node, however, its union is already fixed. The next-segment count
has one uniform upper bound depending only on the guaranteed lower union size.
Induction on tree depth therefore multiplies the maximum node branching
factors. No independence between different levels is claimed or needed.

## 7. Good-history mass is subexponential

For fixed partition depth $d$, set

$$
a_n=n^2/u,
\qquad
\xi_n=a_n^{1/3},
\qquad
\delta_n=\max\{a_n^{1/3},1/n\}.
$$

The losses are:

- $d\delta_n$ from the large-union bounds;
- $d\delta_n$ from hypergeometric concentration;
- $O(d a_n^{2/3})=o(\delta_n)$ from witness conflicts.

Choosing the Markov threshold so that the small-accepted-set event has mass
at least $(2d+2)\delta_n$ leaves at least
$\delta_n-o(\delta_n)=2^{-o(n)}$ good mass. Its logarithm disappears after
division by $n$.

The continuum statement is obtained by first proving every fixed finite
partition, then refining the partition after the $n\to\infty$ limit. No
uncontrolled depth $d(n)$ is needed.

## 8. Remaining limitations

The result assumes:

- one-sided error;
- worst-case fixed persistent memory;
- the standard public-tape state-machine interface;
- $u/n^2\to\infty$ for fresh-distinct transport.

It does not prove the sharp constant, does not cover two-sided error, and does
not yet establish the same coefficient for the full natural-universe regime
$u/n\to\infty$.
