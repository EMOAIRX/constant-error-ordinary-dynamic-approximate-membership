# Continuous all-pivot variational limit

> Status: proved as the exact limit of the finite all-pivot Jensen hierarchy.
> The theorem gives a strict, non-numerical improvement over every fixed
> finite partition, including the certified ten-block constant. It retains
> the existing full-fiber lifting assumptions $u/n^2\to\infty$ and
> $f(n)/n\to\infty$.

All logarithms are base two.

## 1. The result

For $0\le a<c\le1$, set

$$
\Phi(a,c)
=
\left(1-\frac a2\right)
\log_2\frac{2-a}{c-a},
$$

and

$$
A(c)=\Phi(0,c)=\log_2\frac2c,
\qquad
B(c)=\Phi(c,1)
=
\left(1-\frac c2\right)
\log_2\frac{2-c}{1-c}.
$$

Let $\mathcal X$ be the monotone profiles $x:[0,1]\to[0,1]$, using the
left-continuous representative in the interior and setting $x(0)=0$ and
$x(1)=1$. Define

$$
\mathcal F_0[x]
=
\int_0^1 A(x(r))\,dr,
$$

$$
\mathcal F_t[x]
=
\int_0^t B(x(r))\,dr
+
\int_t^1\Phi(x(t),x(r))\,dr,
\qquad 0<t<1,
$$

and

$$
\mathcal F_1[x]
=
\int_0^1 B(x(r))\,dr.
$$

The continuous all-pivot constant is

$$
\boxed{
C_{\mathrm{AP}}
=
\inf_{x\in\mathcal X}
\sup_{0\le t\le1}\mathcal F_t[x].
}
$$

The infimum is attained. If $C_q$ denotes the equal-mass $q$-block Jensen
constant from the finite all-pivot theorem, then

$$
\boxed{
C_q<C_{\mathrm{AP}}
\quad\text{for every finite }q,
\qquad
\lim_{q\to\infty}C_q=C_{\mathrm{AP}}.
}
$$

Consequently, the ordinary half-error full-fiber theorem strengthens to

$$
\boxed{
H\ge C_{\mathrm{AP}}n-o(n)
}
$$

whenever

$$
\frac{u}{n^2}\to\infty,
\qquad
\frac{f(n)}n\to\infty.
$$

In particular, without selecting any new numerical parameters,

$$
\boxed{
C_{\mathrm{AP}}>C_{10}
\ge1.607987002861718\ldots .
}
$$

The numerical solution of the associated all-active integral equation is
near $1.7156$. That decimal is only a numerical location; the theorem above
does not use it.

## 2. Equivalent value-space game

Let $\mu=x_\#\operatorname{Leb}$ be the value distribution of a profile.
For $a,c\in[0,1]$, define the extended kernel

$$
K(a,c)
=
\begin{cases}
B(c),&c\le a,\\
\Phi(a,c),&c>a.
\end{cases}
$$

The kernel is nonnegative and lower semicontinuous. If $\mu$ has an atom of
mass $\eta$ at $c>0$, then pivots $a\uparrow c$ from below contribute
$\eta\Phi(a,c)\to\infty$. An atom at $c=0$ is instead excluded by the
endpoint functional $\mathcal F_0=\int A(c)\,d\mu(c)$, since $A(0)=+\infty$.
Hence every finite-value profile has an atomless value distribution.

For atomless $\mu$, write

$$
P_\mu(a)=\int K(a,c)\,d\mu(c).
$$

At values attained by the profile, $P_\mu(a)$ is exactly the corresponding
rank-pivot functional. On a gap of $\operatorname{supp}\mu$, no mass crosses
the pivot and $P_\mu(a)$ is nondecreasing because $\Phi(a,c)$ is
nondecreasing in its first argument. Therefore the largest value on a gap is
already obtained at its right support boundary. It follows that

$$
\boxed{
C_{\mathrm{AP}}
=
\inf_{\substack{\mu\in\mathcal P([0,1])\\\mu\text{ atomless}}}
\sup_{a\in[0,1]}P_\mu(a).
}
$$

This is a one-dimensional zero-sum kernel game. It is the exact continuous
closure of the all-pivot method, not a new finite list of selected pivots.

## 3. Finite games are exactly the old $C_q$

For a nondecreasing vector

$$
0<p_0\le\cdots\le p_{q-1}<1,
$$

let

$$
L_{q,0}(p)
=
\frac1q\sum_{i=0}^{q-1}A(p_i),
$$

$$
L_{q,j}(p)
=
\frac1q\left[
\sum_{i<j}B(p_i)
+
\sum_{i\ge j}\Phi(p_{j-1},p_i)
\right],
\qquad1\le j<q,
$$

and

$$
L_{q,q}(p)
=
\frac1q\sum_{i=0}^{q-1}B(p_i).
$$

Then

$$
C_q
=
\inf_p\max_{0\le j\le q}L_{q,j}(p).
$$

If

$$
\mu_q=\frac1q\sum_{i=0}^{q-1}\delta_{p_i},
$$

then $L_{q,j}$ is exactly the payoff of $\mu_q$ at action
$a=p_{j-1}$, with the two endpoint actions $a=0,1$. Equivalently, if
$x$ is constant with value $p_i$ on the open rank cell
$(i/q,(i+1)/q)$ and takes the left value at a grid point, then

$$
\mathcal F_{j/q}[x]=L_{q,j}(p).
$$

Conversely, for an arbitrary monotone $x$, let $p_i$ be its average on the
$i$th rank cell. Convexity of $A$, $B$, and $c\mapsto\Phi(a,c)$, together
with monotonicity in the first argument, gives

$$
\mathcal F_{j/q}[x]\ge L_{q,j}(p).
$$

Thus $C_q$ is exactly the minimax value when the adversary is restricted to
the grid pivots $0,1/q,\ldots,1$.

## 4. Compactness and absence of atoms

Take near-minimizers $p^{(q)}$ with

$$
\max_jL_{q,j}(p^{(q)})\le M
$$

for a common finite $M$; the linear profile supplies such a common bound.
Let an interval $I$ of length $\delta<1$ contain $m$ coordinates of
$p^{(q)}$. Use its leftmost coordinate as a pivot. Every one of the other
$m-1$ coordinates in $I$ contributes at least

$$
\Phi(a,c)
\ge
\frac12\log_2\frac1\delta.
$$

Hence

$$
\mu_q(I)
\le
\frac1q
+
\frac{2M}{\log_2(1/\delta)}.
$$

Any weak limit of the $\mu_q$ is therefore atomless. This is the
equicoercive fact behind the continuum limit: a positive mass of nearly
equal profile values would be detected by a pivot immediately before that
mass and would pay the logarithmic diagonal singularity.

The same estimate applies to a minimizing sequence for
$C_{\mathrm{AP}}$. More explicitly, if $V(\mu)\le M$ and
$I=[\ell,\ell+\delta]$ with $\ell>0$, choose a pivot immediately to the left
of $\ell$. All mass in $I$ is then on the $\Phi$ side of the kernel, so
letting the pivot approach $\ell$ gives

$$
\mu(I)
\le
\frac{2M}{\log_2(1/\delta)}.
$$

Intervals meeting zero are controlled separately by

$$
\mu([0,\delta])\log_2\frac2\delta
\le
\int A(c)\,d\mu(c)
\le M.
$$

Thus, by applying these uniform bounds to continuity intervals, a weak limit
of a minimizing sequence is atomless. For every fixed $a$, lower
semicontinuity of $K(a,\cdot)$ and Portmanteau give

$$
P_\mu(a)
\le
\liminf_m P_{\mu_m}(a)
\le
\liminf_m V(\mu_m).
$$

Taking the supremum over $a$ proves lower semicontinuity of $V$ along the
minimizing sequence. Weak compactness of probability measures therefore
shows that the infimum defining $C_{\mathrm{AP}}$ is attained by an
atomless measure.

## 5. Convergence of the complete finite hierarchy

The Jensen lifting in Section 3 gives

$$
C_q\le C_{\mathrm{AP}}
$$

for every $q$.

For the reverse asymptotic inequality, take a subsequence realizing
$\liminf_q C_q$ and near-minimizing empirical measures
$\mu_q\Rightarrow\mu$ along it, with optimization error $o(1)$. Section 4
shows that $\mu$ is atomless. For every $a\in\operatorname{supp}\mu$, choose
coordinates $a_q$ of $p^{(q)}$ with $a_q\to a$. The corresponding branch
payoff is

$$
\int K(a_q,c)\,d\mu_q(c).
$$

Since

$$
\delta_{a_q}\otimes\mu_q
\Rightarrow
\delta_a\otimes\mu
$$

and $K$ is lower semicontinuous, Portmanteau gives

$$
P_\mu(a)
\le
\liminf_{q\to\infty}
\int K(a_q,c)\,d\mu_q(c)
\le
\liminf_{q\to\infty}(C_q+o(1)).
$$

The gap monotonicity from Section 2 extends this bound from the support to
every $a\in[0,1]$. Therefore

$$
C_{\mathrm{AP}}
\le
\sup_aP_\mu(a)
\le
\liminf_{q\to\infty}C_q.
$$

Together with $C_q\le C_{\mathrm{AP}}$, this proves

$$
\lim_{q\to\infty}C_q=C_{\mathrm{AP}}.
$$

This order of limits is important. For the AMQ theorem, $q$ is fixed while
$n\to\infty$; only after obtaining the asymptotic inequality for every fixed
$q$ do we take the supremum over $q$. No growing-depth operation tree or
universe-exposure estimate is introduced.

## 6. Why every finite partition is strictly weaker

Let $\mu_*$ attain $C_{\mathrm{AP}}$, and let $x_*$ be its quantile profile.
Because $\mu_*$ is atomless, $x_*$ is not constant on any rank interval of
positive length.

Assume for contradiction that $C_q=C_{\mathrm{AP}}$ for some finite $q$.
Let $p_i$ be the average of $x_*$ on the $i$th rank cell. For all grid cuts,

$$
\mathcal F_{j/q}[x_*]\ge L_{q,j}(p).
$$

Also

$$
\mathcal F_{j/q}[x_*]
\le
\sup_t\mathcal F_t[x_*]
=C_{\mathrm{AP}},
$$

while the definition of $C_q$ gives

$$
\max_jL_{q,j}(p)\ge C_q=C_{\mathrm{AP}}.
$$

Thus some branch must attain equality throughout the Jensen chain. If it is
an endpoint branch, strict convexity of $A$ or $B$ forces $x_*$ to be
constant on every rank cell. If it is an interior branch, strict convexity
of $B$ on the left cells and of $c\mapsto\Phi(a,c)$ on the right cells gives
the same conclusion. In either case $\mu_*$ has atoms of mass $1/q$, which
contradicts the finite value of the optimizer.

Hence

$$
\boxed{C_q<C_{\mathrm{AP}}}
$$

for every finite $q$. This is the strict improvement: the logarithmic
diagonal singularity rules out equality with any finite Jensen partition.

## 7. Lifting back to dynamic approximate membership

The already-audited full-fiber theorem proves, for every fixed $q$,

$$
H\ge C_qn-o(n)
$$

under $u/n^2\to\infty$ and a supported operation horizon
$f(n)/n\to\infty$. Therefore

$$
\liminf_{n\to\infty}\frac Hn
\ge C_q
$$

for every fixed $q$. Taking the supremum over $q$ after the $n\to\infty$
limit and applying Section 5 yields

$$
\liminf_{n\to\infty}\frac Hn
\ge
\sup_qC_q
=C_{\mathrm{AP}}.
$$

No state budget is added across pivots. Each finite $q$ is an alternative
decoder using the same $H$-bit state, exactly as in the existing all-pivot
proof.

## 8. All-active equation and uniqueness

The main theorem above does not assume that every pivot is active or that the
optimizer has a density. If an attained optimizer has a positive density
$\rho$, all pivots are active, and the corresponding endpoint density is Dini
with a finite positive limit, then comparison with the endpoint pivot gives
the tail equation

$$
\int_a^1
[\Phi(a,c)-B(c)]\rho(c)\,dc
=0,
\qquad0<a<1.
$$

With

$$
u=1-a,
\qquad
v=1-c,
\qquad
r(v)=\rho(1-v),
$$

the equation becomes

$$
\int_0^u
\mathcal K(u,v)r(v)\,dv
=0,
$$

where

$$
\mathcal K(u,v)
=
\left[
(1+u)\ln\frac{1+u}{u-v}
-(1+v)\ln\frac{1+v}{v}
\right].
$$

There is at most one normalized positive Dini solution among solutions for
which $r_1(u)/r_2(u)$ has a finite positive limit as $u\downarrow0$. In
particular, this applies when both solutions satisfy the endpoint
regular-variation law in the companion note. Indeed, differentiating with the
same cutoff at $v=u$ gives the finite-part identity

$$
0
=
(1+u)\int_0^u\frac{r(u)-r(v)}{u-v}\,dv
+\int_0^u
\left[\ln\frac{1+u}{u-v}+1\right]r(v)\,dv.
$$

The Dini assumption makes the first integral finite. To see the cancellation,
use

$$
\partial_u\mathcal K(u,v)
=
\ln\frac{1+u}{u-v}-\frac{1+v}{u-v}
$$

before taking the common cutoff to zero; the boundary logarithm cancels the
constant part of $(1+u)\int r(v)/(u-v)\,dv$.

Now set $q=r_1/r_2$ and subtract $q(u)$ times the identity for $r_2$ from
the identity for $r_1$. This gives

$$
\int_0^u
W(u,v)r_2(v)[q(u)-q(v)]\,dv
=0,
$$

where

$$
W(u,v)
=
\frac{1+u}{u-v}
-\ln\frac{1+u}{u-v}
-1
>0.
$$

The endpoint ratio limit lets the running maximum/minimum argument start at
$u=0$. If $q$ were nonconstant, its first running extremum away from that
limit would make the integrand have one sign and be strict on a set of
positive measure, a contradiction. Hence $q$ is constant, and normalization
makes the solution unique. Without an endpoint ratio limit, interior Dini
regularity alone does not justify this maximum-principle step.

The endpoint expansion already proved in the companion note,

$$
r(v)
=
r_0\left[
1+v\ln v
-\left(1+\frac{\pi^2}{6}\right)v
+o(v)
\right],
$$

is consistent with this uniqueness statement. Existence of a positive
all-active density and attainment of a countably additive exact dual remain
separate regularity questions; they are not needed for the variational-limit
lower bound or its strict improvement over $C_{10}$.

## 9. Scope and non-claims

- The theorem closes the all-pivot Jensen hierarchy itself and proves a
  strict improvement over every finite partition.
- It does not lower the universe assumption from $u/n^2\to\infty$ to
  $u/n\to\infty$.
- It does not prove that $C_{\mathrm{AP}}$ matches the best ordinary AMQ
  upper bound.
- The numerical location near $1.7156$ is not used as a theorem.
- No regularized-kernel parameter, numerical tangent, or increasing block
  count is used to create the strict gap.
