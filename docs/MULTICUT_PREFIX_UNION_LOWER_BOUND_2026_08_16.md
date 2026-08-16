# Multicut prefix-union lower bound for ordinary dynamic AMQ

> Status: proved for the standard public-tape, one-sided, pointwise-error
> model. No history independence, monotone-query, BSSI, locality, or bounded
> horizon assumption is used. The current fresh-distinct transport step
> requires $u/n^2\to\infty$.

## 1. Main theorem

Fix $0<\varepsilon<1$. Let a randomized ordinary dynamic approximate
membership filter have capacity $n$, universe size $u=u_n$, worst-case
persistent memory $H_n$ bits, no false negatives, and pointwise false-positive
probability at most $\varepsilon$. Assume

$$
\frac{u}{n^2}\longrightarrow\infty.
$$

The filter may be history dependent, may have multiple representations, and
may use a free public random tape. Because a fully dynamic filter must support
the legal history consisting of $n$ fresh distinct insertions, it is enough to
lower-bound that experiment.

Define

$$
f_\varepsilon(b)
=
(1-b)\log_2\frac{1-b}{\varepsilon-b},
\qquad 0\le b<\varepsilon.
$$

Then

$$
\liminf_{n\to\infty}\frac{H_n}{n}
\ge h_\varepsilon,
$$

where $h_\varepsilon$ is the unique solution larger than
$\log_2(1/\varepsilon)$ of

$$
h_\varepsilon
=
\int_0^1
f_\varepsilon\!\left(2^{-h_\varepsilon/c}\right)\,dc.
$$

Equivalently,

$$
\int_{h_\varepsilon}^{\infty}
\frac{f_\varepsilon(2^{-t})}{t^2}\,dt
=1.
$$

At half error,

$$
\boxed{
h_{1/2}=1.19810077403325\ldots
}
$$

Numerically this is the fixed point above. A monotone left-Riemann certificate
at $h=1.198$ gives the fully explicit rigorous corollary

$$
\boxed{H_n\ge1.198n-o(n).}
$$

This strictly improves the formally proved Lovett--Porat coefficient $1.1$.
It also exceeds their reported, but not formally certified, recursive value
near $1.13$.

## 2. A finite two-segment certificate

The improvement does not depend on a deep numerical block composition. Take
only the two suffix segments determined by

$$
c_0=\frac7{12},
\qquad
c_1=\frac56,
\qquad
c_2=1.
$$

The finite-partition theorem below implies that every limiting rate $h$ must
satisfy, at $\varepsilon=1/2$,

$$
h-c_0
\ge
(c_1-c_0)f_{1/2}(2^{-h/c_0})
+(1-c_1)f_{1/2}(2^{-h/c_1}).
$$

At $h=1.134$, the two sides are

$$
0.550666666666666\ldots
$$

and

$$
0.551313982923797\ldots,
$$

respectively. The necessary inequality fails by more than
$6.47\cdot10^{-4}$. Monotonicity then gives the explicit reviewer-safe
corollary

$$
\boxed{H_n\ge1.134n-o(n).}
$$

The integral coefficient is the closed-form limit of the same theorem, not a
separate twenty-block claim.

## 3. Deterministic layered graph after fixing the tape

Let $W=(W_1,\ldots,W_n)$ be uniform over ordered distinct $n$-tuples from the
universe. For a public tape $R$, let $A_R(W)$ be the set of keys accepted by
the final state.

Pointwise false-positive control and zero false negatives give

$$
\mathbb E_R|A_R(W)|
\le
\varepsilon u+(1-\varepsilon)n.
$$

Averaging also over $W$ fixes one tape $r$ such that

$$
\mathbb E_W|A_r(W)|
\le
\varepsilon u+(1-\varepsilon)n.
$$

After this fixing, every update transition and query answer is deterministic.
At every insertion layer there are at most $2^{H_n}$ physical states, and a
final physical state determines one accepted set $A$.

Fix a finite partition

$$
0<c_0<c_1<\cdots<c_d=1,
$$

and write $k_i=\lfloor c_i n\rfloor$ and
$m_i=k_{i+1}-k_i$.

For a distinct prefix $p$ of length $k_i$, let $v(p)$ be its physical state
and define the prefix union

$$
L(p)
=
\{y:\text{some distinct length-}k_i\text{ prefix reaching }v(p)
\text{ contains }y\}.
$$

## 4. Large prefix unions at all cuts

At layer $k_i$, the number of distinct prefixes whose union has size at most
$\beta u$ is at most

$$
2^{H_n}(\beta u)^{k_i}.
$$

Since the total number of distinct prefixes is $(u)_{\underline{k_i}}$, for
any $\delta>0$ the choice

$$
\beta_{i,n}
=
\left(
\delta 2^{-H_n}
\frac{(u)_{\underline{k_i}}}{u^{k_i}}
\right)^{1/k_i}
$$

gives

$$
\Pr[|L(P_i)|<\beta_{i,n}u]\le\delta.
$$

If $H_n/n\to h$, $u/n^2\to\infty$, and
$\log(1/\delta)=o(n)$, then

$$
\beta_{i,n}=2^{-h/c_i}-o(1).
$$

The same global $H_n$ appears at every cut. It is never replaced by a lower
bound for a smaller subproblem.

## 5. Fresh-distinct transport repair

For every $y\in L(p)$, choose one canonical distinct witness prefix $p_y$
that reaches $v(p)$ and contains $y$. Let $Z$ be the future distinct suffix
after $p$.

If $y$ already occurs in the actual full history $pZ$, it is accepted directly.
Otherwise, whenever

$$
(p_y\setminus\{y\})\cap Z=\varnothing,
$$

$p_yZ$ is a legal insertion history and, because $p_y$ and $p$ reach the same
state at the same layer, both histories reach the same final state. Zero false
negatives then imply

$$
y\in A(pZ).
$$

Consequently, $L(p)\setminus A(pZ)$ is contained in the set of labels whose
chosen witness has some other label intersecting $Z$. Conditional on any fixed
prefix $p$,

$$
\mathbb E\bigl[|L(p)\setminus A(pZ)|\mid p\bigr]
\le
|L(p)|
\frac{(n-k_i)(k_i-1)}{u-n+1}.
$$

Set

$$
a_n=\frac{n^2}{u},
\qquad
\xi_n=a_n^{1/3},
\qquad
\delta_n=\max\{a_n^{1/3},1/n\}.
$$

Markov's inequality gives, at every fixed cut,

$$
\Pr[|L(P_i)\setminus A(W)|>\xi_nu]
=O(a_n^{2/3})
=o(\delta_n).
$$

This is the only place where the present proof needs
$u/n^2\to\infty$.

## 6. Simultaneously good histories

Choose

$$
\alpha_n
=
\frac{\varepsilon+(1-\varepsilon)n/u}
{1-(2d+2)\delta_n}.
$$

Markov gives

$$
\Pr[|A(W)|\le\alpha_nu]
\ge(2d+2)\delta_n.
$$

At every cut, the large-union failure probability is at most $\delta_n$.
Conditional on a prefix, the next segment is a hypergeometric sample from the
remaining universe. Hence, for

$$
\gamma_{i,n}
=
\sqrt{\frac{\log(2/\delta_n)}{2m_i}},
$$

the fraction of the next segment lying in $L(P_i)$ differs from
$|L(P_i)|/u$ by $o(1)$ except on probability at most $\delta_n$.

A union bound over the fixed number of cuts, together with the transport
bound, leaves at least

$$
\delta_n-o(\delta_n)=2^{-o(n)}
$$

of all full distinct histories satisfying simultaneously:

- $|A(W)|\le\alpha_nu$;
- $|L(P_i)|\ge\beta_{i,n}u$ at every cut;
- $|L(P_i)\setminus A(W)|\le\xi_nu$ at every cut;
- the next segment has the typical intersection size with $L(P_i)$.

Call these histories good.

## 7. The multisegment tree bound

Fix an initial prefix $p_0$ and one final physical state $q$, and write
$A=A(q)$ for its accepted set. Consider the tree of good suffixes that start
at $p_0$ and end at $q$.

At a node entering segment $i$, write

$$
|L(P_i)|=bu,
\qquad
b\ge\beta_{i,n}.
$$

Because the leaf is good,

$$
|A\setminus L(P_i)|
\le
(\alpha_n+\xi_n-b)u.
$$

Every label in the segment is also in $A=A(q)$, by zero false negatives for
the actual history ending at $q$.

If the next segment has $j$ hits in $L(P_i)$, its number of possible ordered
labels is at most

$$
\binom{m_i}{j}
(bu)^j
\bigl((\alpha_n+\xi_n-b)u\bigr)^{m_i-j}.
$$

For a typical segment, $j\le(b+o(1))m_i$. Comparing the last display with the
corresponding binomial mass with outside probability $1-b$ gives the uniform
branching bound

$$
u^{m_i}
2^{-m_i f_{\alpha_n+\xi_n}(\beta_{i,n})+o(n)}.
$$

The function $f_a(b)$ is increasing in $b$, because with
$r=(1-b)/(a-b)>1$,

$$
f_a'(b)
=
\frac{r-1-\ln r}{\ln2}>0.
$$

Crucially, $L(P_i)$ is fixed before segment $i$ is counted. The bound is
node-wise and uniform, so it multiplies down the tree even though later unions
depend on earlier segment labels. No intermediate state is transmitted or
enumerated.

Therefore the number of good suffixes for a fixed pair $(p_0,q)$ is at most

$$
u^{n-k_0}
2^{-\sum_{i=0}^{d-1}m_i
f_{\alpha_n+\xi_n}(\beta_{i,n})+o(n)}.
$$

## 8. Counting the endpoint pairs

There are at least

$$
2^{-o(n)}(u)_{\underline n}
$$

good full histories. Dividing by the fixed-pair tree bound gives at least

$$
u^{k_0}
2^{\sum_i m_i f_{\alpha_n+\xi_n}(\beta_{i,n})-o(n)}
$$

distinct pairs $(p_0,q)$.

On the other hand, there are at most $2^{H_n}$ final physical states, and
every key in $p_0$ must lie in $A(q)$. Thus

$$
|\{(p_0,q)\}|
\le
2^{H_n}(\alpha_nu)^{k_0}.
$$

The factor $2^{H_n}$ is used exactly once. Comparing the bounds, dividing by
$n$, and taking $n\to\infty$ proves the finite-partition inequality

$$
\boxed{
h+c_0\log_2\varepsilon
\ge
\sum_{i=0}^{d-1}
(c_{i+1}-c_i)
f_\varepsilon\!\left(2^{-h/c_i}\right).
}
$$

## 9. From finite cuts to the integral fixed point

For fixed $s=c_0>0$, refine the partition after taking the asymptotic limit.
The left-endpoint sums converge to

$$
h+s\log_2\varepsilon
\ge
\int_s^1
f_\varepsilon\!\left(2^{-h/c}\right)\,dc.
$$

The derivative with respect to $s$ of the right side after moving the prefix
term across is

$$
\log_2\frac1\varepsilon
-f_\varepsilon(2^{-h/s})<0.
$$

Hence the strongest endpoint is $s\downarrow0$, giving

$$
h
\ge
I_\varepsilon(h)
:=
\int_0^1
f_\varepsilon\!\left(2^{-h/c}\right)\,dc.
$$

Since $f_\varepsilon$ is increasing and $2^{-h/c}$ decreases with $h$,
$I_\varepsilon(h)$ is strictly decreasing. The necessary lower coefficient is
therefore the unique fixed point $h_\varepsilon=I_\varepsilon(h_\varepsilon)$:
at $h=\log_2(1/\varepsilon)$ the integral is strictly larger than $h$, while
for sufficiently large $h$ it is strictly smaller than $h$.

## 10. Scope and remaining boundary

The theorem covers:

- ordinary history-dependent filters;
- multiple representations and nonmonotone accepted sets;
- free public randomness and arbitrary reliability allocation across tapes;
- unrestricted operation time;
- the fully dynamic model, by restriction to legal fresh insertions.

It does not yet cover every superlinear universe. The canonical-witness
transport bound loses $\Theta(n^2/u)$, so the current proof requires
$u/n^2\to\infty$. Weakening this to only $u/n\to\infty$, and determining the
sharp constant, remain open.
