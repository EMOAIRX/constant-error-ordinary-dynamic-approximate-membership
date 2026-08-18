# Canonical fixed-$\varepsilon$ replacement-cover lower bound

## The theorem

Fix $\varepsilon\in(0,1)$ and write

$$
\beta=1-\varepsilon,
\qquad
\ell=\log_2(1/\varepsilon),
\qquad
\sigma=\min\{\varepsilon,\beta\},
\qquad
B_0=4\ln2+1.
$$

For $0<t\le\sigma/4$, define

$$
\rho_\varepsilon(t)
=\varepsilon+t-(\varepsilon-t)2^{-2t^2},
\qquad
\alpha_\varepsilon(t)=\beta-t,
$$

and

$$
\Psi_\varepsilon(t)
=\frac{\alpha_\varepsilon(t)}2
\log_2\frac{\alpha_\varepsilon(t)}{e\rho_\varepsilon(t)}.
$$

There is a unique $t^*_\varepsilon\in(0,\sigma/4)$ satisfying

$$
\Psi_\varepsilon(t^*_\varepsilon)
=\ell+\frac{(t^*_\varepsilon)^2}{B_0}.
$$

Set

$$
\Gamma_\varepsilon
=\frac{(t^*_\varepsilon)^2}{B_0\ell}.
$$

Then every ordinary dynamic approximate-membership filter with capacity $n$,
zero false negatives, pointwise false-positive probability at most
$\varepsilon$, arbitrary history dependence, a free public random tape, and
fixed worst-case persistent space satisfies

$$
H^*_\varepsilon(n,u)
\ge
(1+\Gamma_\varepsilon)n\log_2(1/\varepsilon)-o(n)
$$

along every sequence with $n\to\infty$ and $u/n\to\infty$.

The theorem contains the half-error case by direct substitution. No numerical
witness and no separate half-error proof is used.

## Why the constant is canonical

The coefficient

$$
B_0=4\ln2+1
$$

is exactly the sum of the two accepted-size Chebyshev coefficients and the one
posterior-KL Markov coefficient. A positive constant fraction of good branches
is sufficient for exponential packing; there is no need to force that fraction
above $1/2$.

The reservoir function $\rho_\varepsilon(t)$ is the direct, unrelaxed limiting
upper bound furnished by support thickness. On a
branch with both accepted sizes in the $t$-window and conditional posterior KL
at most $t^2n$,

$$
\frac{|A'\setminus A|}{u}
\le
\varepsilon+t-(\varepsilon-t)2^{-2t^2}+o(1)
=\rho_\varepsilon(t)+o(1).
$$

Thus the theorem does not replace the reservoir by an arbitrarily selected
linear bound such as $c t$.

## Proof skeleton

Assume $H\le(1+\gamma)n\ell$ for a fixed
$0<\gamma<\Gamma_\varepsilon$, and put $t=t^*_\varepsilon$.

1. Carter stability gives

   $$
   \mathbb E(X-\varepsilon)^2,
   \mathbb E(X'-\varepsilon)^2
   \le2\ln2\,\gamma\ell+o(1),
   $$

   and expected parent and successor posterior deficits at most
   $\gamma n\ell+o(n)$.

2. The two size failures and one conditional-KL failure have total mass at most

   $$
   \frac{B_0\gamma\ell}{t^2}+o(1)
   =\frac{\gamma}{\Gamma_\varepsilon}+o(1)<1.
   $$

   Hence a positive constant fraction of replacement branches is good.

3. Joint conditioning on the deletion and insertion batches gives posterior
   support-union thickness

   $$
   v\ge(\varepsilon-t-o(1))2^{-2t^2}u.
   $$

   Common-word forcing then yields the exact reservoir bound above.

4. For every fixed $\eta>0$, a random fresh insertion batch has at least
   $(\beta-t-\eta)q$ keys outside the parent accepted set with probability
   $1-o(1)$. Those keys must all lie in the successor reservoir.

5. If $s_0=\lceil(\beta-t-\eta)q\rceil$, one successor state covers at most

   $$
   \binom uq
   \left(
   \frac{e(\rho_\varepsilon(t)+o(1))}{\beta-t-\eta}
   \right)^{s_0}
   $$

   insertion batches. Packing a positive fraction of all
   $\binom{u-n}{q}$ batches and using

   $$
   \log_2\frac{\binom uq}{\binom{u-n}q}=o(n)
   $$

   gives, after taking $\eta\downarrow0$,

   $$
   \frac Hn\ge\Psi_\varepsilon(t)-o(1)
   =(1+\Gamma_\varepsilon)\ell-o(1),
   $$

   contradicting $\gamma<\Gamma_\varepsilon$.

## Uniqueness of the balance point

As $t\downarrow0$, $\rho_\varepsilon(t)=2t+O_\varepsilon(t^2)$, so
$\Psi_\varepsilon(t)\to\infty$. Moreover, $\rho_\varepsilon$ is strictly
increasing and $\alpha_\varepsilon/\rho_\varepsilon$ is strictly decreasing.
Where $\Psi_\varepsilon\ge0$, differentiation gives

$$
\Psi_\varepsilon'(t)
=\frac{-\ln R(t)-1-
\alpha_\varepsilon(t)\rho_\varepsilon'(t)/\rho_\varepsilon(t)}{2\ln2}<0,
\qquad
R(t)=\frac{\alpha_\varepsilon(t)}{e\rho_\varepsilon(t)}.
$$

At $t=\sigma/4$, one has
$\Psi_\varepsilon(t)<\ell+t^2/B_0$. Therefore the two sides have exactly one
intersection in $(0,\sigma/4)$.

## Provenance

The simultaneous replacement-cover theorem and the joint posterior
conditioning mechanism were developed in this repository. The external
contribution by `yukuai26` identified the useful $\sqrt\gamma$ scale and a
general-$\varepsilon$ refinement direction. The theorem above is the unified
analytic closure for this one-parameter balance: it removes the selected
dyadic witness, the arbitrary
good-mass threshold, the linear reservoir relaxation, and the duplicated
tolerance loss.
