# Simultaneous replacement-cover width: a natural-universe lower bound

> Status: proved theorem. This is the first result in this repository that
> gives a strict constant-factor gap above the static $n$-bit baseline in the
> original ordinary model with only $u/n\to\infty$. The proof uses no
> stationarity, no BSSI/monotonicity assumption, no fixed-depth composition,
> and no numerical optimizer.

All logarithms are base two. The public tape is denoted by $R$; it is sampled
independently of the update history and is free to read. The persistent state
has at most $H$ bits. Queries have zero false negatives on every tape, and for
every fixed legal history $h$ and fixed nonmember $x$, the false-positive
probability over $R$ is at most $1/2$.

## 1. Main theorem

### Theorem 1 (ordinary natural-universe gap)

There is an absolute constant $\eta_0>0$ such that every ordinary dynamic
approximate-membership filter in the above model satisfies

$$
H\ge (1+\eta_0)n-o(n)
$$

whenever $u/n\to\infty$. The $o(n)$ term is uniform along every sequence of
instances with $u/n\to\infty$.

One explicit, deliberately unoptimized choice is

$$
\boxed{\eta_0=2^{-48}}.
$$

The theorem applies to arbitrary history-dependent, nonmonotone filters with
global relocation, ghosts, shared certificates, and multiple representations.
The update word used in the proof has only $2\lfloor n/2\rfloor$ operations.

The value $2^{-48}$ is only a transparent witness for the theorem, not a claim
about the best constant. It comes from the analytic inequalities in Section 7;
no parameter is selected by numerical search.

## 2. Tape-independent parent and successor experiments

Fix $q=\lfloor n/2\rfloor$ and $k=n-q$. Sample an $n$-set $S$ uniformly from
$\binom Un$, and use a fixed canonical insertion order for $S$. This random
history is independent of $R$. Let $M$ be the state after the $n$ inserts and
write

$$
Z=(R,M),\qquad A_Z=\{x:\text{the query at }(R,M)\text{ answers YES on }x\},
\qquad a_Z=|A_Z|.
$$

For the replacement experiment, choose $D\subseteq S$ uniformly with $|D|=q$,
then choose $I\subseteq U\setminus S$ uniformly with $|I|=q$. Execute the fixed
word that deletes the labels in $D$ and then inserts the labels in $I$, using a
fixed universe order within each set.
The successor set

$$
S'=(S\setminus D)\cup I
$$

is again uniform in $\binom Un$, and the complete successor-history distribution
is still independent of $R$. Thus the pointwise FPR guarantee can be averaged
in both experiments without conditioning the update distribution on the tape.

## 3. Carter near-equality stability

Conditioned on $Z=z$, let $\mu_z$ be the law of $S$. Since every posterior set is
accepted, $\mu_z$ is supported on $\binom{A_z}{n}$. Let

$$
L_u=\log\binom un,
\qquad
B_u=\log\binom{(u+n)/2}{n},
$$

and define the posterior deficit

$$
d_z=\log\binom{a_z}{n}-H(S\mid Z=z)
    =D\!\left(\mu_z\,\middle\|\,\operatorname{Unif}\binom{A_z}{n}\right)\ge0.
$$

Pointwise FPR and the tape-independent parent experiment give

$$
\mathbb E a_Z\le\frac{u+n}{2}.
$$

Consequently,

$$
H(S\mid Z)\le\mathbb E\log\binom{a_Z}{n}
\le B_u.
$$

Since $u/n\to\infty$,

$$
L_u-B_u=n-o(n).
$$

If $H=n+o(n)$, then

$$
\mathbb E d_Z
\le B_u-L_u+H=o(n).
\tag{1}
$$

The same argument applied to the tape-independent successor experiment gives
the same two conclusions for $a_{Z'}$.

Here is an exact stability argument. Set

$$
f(x)=\log\binom xn,
\qquad a_0=(u+n)/2,
\qquad J=f(a_0)-\mathbb E f(a_Z).
$$

The information identity is

$$
I(S;Z)=(L_u-B_u)+J+\mathbb E d_Z\le H,
\tag{1a}
$$

so $J+\mathbb E d_Z\le H-(L_u-B_u)$. Moreover,

$$
f''(x)
=-\frac1{\ln2}\sum_{j=0}^{n-1}\frac1{(x-j)^2}
\le-\frac n{u^2\ln2}
$$

for $n\le x\le u$. The tangent gap at $a_0$ therefore satisfies

$$
g(x):=f(a_0)+f'(a_0)(x-a_0)-f(x)
\ge\frac{n(x-a_0)^2}{2u^2\ln2}.
$$

Because $\mathbb E a_Z\le a_0$ and $f'(a_0)>0$,

$$
\mathbb E g(a_Z)
=J+f'(a_0)(\mathbb E a_Z-a_0)
\le J.
$$

Thus $H=n+o(n)$ implies $a_Z/u\to1/2$ in probability. Quantitatively, if
$H\le(1+\gamma)n$, then the exceptional probability outside a window of width
$\tau u$ is $O(\gamma/\tau^2)+o(1)$. The identical argument applies to the
successor accepted size $a_{Z'}$.

## 4. Posterior replacement lemma

Fix a parent value $z=(r,m)$ and let $A=A_z$. Let $\nu_z$ be the uniform law on
$\binom An$. Apply the same $(D,I)$ kernel to $\mu_z$ and $\nu_z$. For a branch
$(d,i)$ let $K=S\setminus D$ and let

$$
V_{z,d,i}=\bigcup\operatorname{supp}(K\mid Z=z,D=d,I=i),
\qquad v_{z,d,i}=|V_{z,d,i}|.
$$

Under the reference law, conditioned on $(D=d,I=i)$, $K$ is uniform on

$$
\binom{A\setminus(d\cup i)}{k},
$$

whose ground-set size is

$$
b_{z,d,i}=a_z-q-|i\cap A|.
$$

The KL chain rule gives

$$
\mathbb E_{D,I}
 D\!\left(\mu_{K\mid z,D,I}\,\middle\|\,\nu_{K\mid z,D,I}\right)
\le d_z.
\tag{2}
$$

Since a distribution supported on $\binom{V}{k}$ has entropy at most
$\log\binom vk$, (2) implies

$$
\mathbb E_{D,I}
\left[
\log\frac{\binom{b_{z,D,I}}k}{\binom{v_{z,D,I}}k}
\right]
\le d_z.
\tag{3}
$$

No independence between $S$, $D$, $I$, and the tape-conditioned posterior is
assumed here. In particular, we never require every witness to avoid $I$;
the conditioning on $I$ is exactly what removes the old $n^2/u$ collision
loss.

If $d_z=o(n)$, $a_z/u\to1/2$, and $q=o(u)$, then (3) implies

$$
v_{z,D,I}/u\to1/2
$$

for all but $o(1)$ of the actual replacement branches. Indeed,
$b_{z,D,I}/u\to1/2$, and if $v\le(1-\delta)b$, then

$$
\log\frac{\binom bk}{\binom vk}
\ge k\log\frac bv
\ge k\log\frac1{1-\delta}=\Omega_\delta(n).
$$

## 5. Common-word forcing and successor outside capacity

Fix a branch $(z,d,i)$ with positive posterior probability. Every
$K\in\operatorname{supp}(K\mid z,d,i)$ corresponds to a parent source set
$D\cup K$ whose fixed-tape state is the same $m$. The word deleting $D$ and
inserting $I$ is legal for every such source set, and fixed-tape determinism sends
all of them to the same successor state $m_i$.

Zero false negatives therefore force

$$
V_{z,d,i}\cup i\subseteq A(r,m_i).
\tag{4}
$$

Let $A'=A(r,m_i)$ and $a'=|A'|$. On a branch where

$$
a'\le(1/2+\tau)u,
\qquad
v\ge(1/2-\tau)u,
$$

equation (4) yields

$$
|A'\setminus A|\le a'-v\le 3\tau u+o(u)=:\rho u,
\tag{5}
$$

where $\rho\to0$ as $\tau\to0$.

The same good branch also has $|I\setminus A|\ge q/3$ with probability
$1-o(1)$. This is a hypergeometric lower-tail statement: when
$a/u\to1/2$, the $q$ labels sampled from $U\setminus S$ hit $U\setminus A$
with asymptotic density $1/2$.

When $H=n+o(n)$, (1)--(3) make the joint probability of all these good events
tend to one under the tape-independent law of $(R,S,D,I)$. Fubini therefore
fixes one tape $r$, one parent source $s$, and one deletion set $d\subseteq s$
such that a $1-o(1)$ fraction of the $N=\binom{u-n}{q}$ possible insertion sets
$i\subseteq U\setminus s$ are good. For the quantitative fixed-$\gamma$ form in
Section 7, the fraction is $1-O(\sqrt\gamma)-o(1)$ and is bounded below by a
positive constant. This fixing occurs only after all FPR averages have been
taken.

## 6. Simultaneous successor-cover width

For each good insertion set $i$, let $m_i$ be its successor state. If two good
insertion sets $i$ and $j$ give the same $m_i=m_j$, they share the same accepted
set $A'$. By (5), that state has an outside-$A$ reservoir

$$
C=A'\setminus A,\qquad |C|\le\rho u.
$$

Moreover every such insertion set is contained in $A'$ by zero false negatives,
and has at least $q/3$ elements in $U\setminus A$, hence in $C$. If
$s_0=\lceil q/3\rceil$, the number of such $q$-sets received by one successor
state is at most

$$
\binom{|C|}{s_0}\binom{u-s_0}{q-s_0}
\le
\binom uq\,(3e\rho)^{s_0}
$$

for all sufficiently large $n$ (the harmless constant $3e$ can be replaced by
any fixed larger constant). Since

$$
\log\frac{\binom uq}{\binom{u-n}{q}}=o(n)
$$

and at least $(1-o(1))N$ insertion sets are good, the number of distinct
successor states on this one fixed tape is at least

$$
2^{-o(n)}(3e\rho)^{-q/3}=2^{\omega(n)}
$$

whenever $\rho\to0$. This contradicts the fixed state bound $2^H=2^{n+o(n)}$.

Thus no sequence of ordinary filters can have $H=n+o(n)$ in the regime
$u/n\to\infty$.

## 7. An explicit constant

The preceding contradiction is quantitative. Suppose

$$
H\le(1+\gamma)n
$$

and put $X=a_Z/u$. The exact product formula gives

$$
\log\frac{\binom un}{\binom{a_Z}n}
\ge n\log\frac u{a_Z}=n\log\frac1X.
$$

Together with (1a), $\mathbb E X\le1/2+o(1)$, and the tangent inequality

$$
-\log_2x-1+\frac2{\ln2}(x-1/2)
\ge\frac{(x-1/2)^2}{2\ln2},
$$

this yields

$$
\mathbb E(X-1/2)^2\le2\ln2\,\gamma+o(1),
\qquad
\mathbb E d_Z\le\gamma n+o(n).
\tag{6}
$$

The first estimate also holds at the successor. Set

$$
\tau=\gamma^{1/4}.
$$

Markov's inequality makes the two accepted-size exceptional masses
$O(\sqrt\gamma)+o(1)$. In (2), discard branches whose conditional KL exceeds
$\tau^2n$; their mass is also $O(\sqrt\gamma)+o(1)$. On every remaining branch,

$$
v\ge (a-q-|I\cap A|)2^{-2\tau^2},
$$

so (5) improves to

$$
|A'\setminus A|\le3\tau u+o(u).
$$

The hypergeometric exception is exponentially small. Hence, for sufficiently
small fixed $\gamma$, Fubini leaves at least one half of the $N$ insertion sets
good. With $s_0=\lceil q/3\rceil$, the deliberately crude estimates

$$
\binom q{s_0}\le2^q,
\qquad
\frac{\binom{3\tau u+o(u)}{s_0}}{\binom u{s_0}}
\le(5\tau)^{s_0}
$$

turn the successor-width count into

$$
\frac Hn
\ge
-\frac12+\frac16\log_2\frac1{5\gamma^{1/4}}-o(1).
\tag{7}
$$

For $\gamma=2^{-48}$, the right side of (7) is

$$
-\frac12+\frac16(12-\log_2 5)-o(1)
>1.11-o(1),
$$

which contradicts $H/n\le1+2^{-48}$ for all sufficiently large instances.
Thus Theorem 1 holds with $\eta_0=2^{-48}$. This witness is intentionally
conservative; optimizing it is a separate problem.

## 8. Why this is not the old $u/n^2$ argument

The old multicut/full-fiber proofs demanded that a single witness survive every
future insertion set. That loses a factor of order $n^2/u$ and requires
$u/n^2\to\infty$. Here the posterior is pruned separately for each branch and
the entropy loss of all prunings is charged once through the exact KL chain rule
(2). The proof only needs $q=o(u)$, which is exactly $u/n\to\infty$ for
$q=\Theta(n)$.

The argument also avoids every previously identified false route:

- no fixed number of blocks is tensorized;
- no tape-dependent hard distribution is chosen;
- no per-tape FPR statement is used;
- no monotonicity, BSSI, canonical state, or exact fingerprint assumption is made;
- no all-pivot or rank deficit is charged twice.

## 9. Sharpness tests

The proof is compatible with the known constructions:

- pure-deletion random covers have large posterior deficit after conditioning and
  therefore do not satisfy (1);
- exact fingerprint-count states have linear posterior deficit, so the residual
  union in (3) need not stay near $u/2$;
- coordinate-erasure public coins are handled before fixing the tape and do not
  permit a tape-dependent choice of $(S,D,I)$.

These tests explain why the theorem detects genuinely dynamic replacement width
rather than re-counting the static accepted-set bound.
