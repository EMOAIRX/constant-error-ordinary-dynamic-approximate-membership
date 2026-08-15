# Intermediate theorem and priority audit around KLZ25 Section 6

## Bottom line

The standard typical-set/Poisson source-coding observation is not a paper contribution.  The standard oblivious, polynomial-horizon, preallocated-memory-with-overflow model is also already used by dynamic-filter constructions.  The most credible intermediate paper target is an **exact linear coefficient for generalized fingerprint filters**, including a nonuniform-load phase transition, together with a time-efficient dynamic implementation and a matching converse inside that class.

Even this target has significant priority adjacency: Weighted Bloom Filters and Daisy Bloom Filters already exploit nonuniform error allocation and “always YES” classes.  The new distinction would have to be stated narrowly and proved carefully: all original universe keys are exchangeable; a hidden random permutation assigns them to heterogeneous fingerprint loads; the guarantee remains pointwise for every fixed nonmember over the structure's randomness; and the objective is the exact linear coefficient of the dynamic fingerprint-multiset representation.

## 1. Models that are not new enough

### Typical-set coding

For uniform fingerprints, the occupancy vector has multinomial entropy

\[
H(C)=\frac n\lambda H(\operatorname{Poi}(\lambda))+O(\log n),
\qquad \lambda=-\ln(1-\varepsilon).
\]

Ranking a typical set and entering a failure/overflow state outside it is standard source coding.  By itself, this does not give a research contribution, and it also does not settle KLZ's fixed worst-case dynamic model.

### Oblivious polynomial horizons and overflow

Bercea--Even, *A Dynamic Space-Efficient Filter with Constant Time Operations* (SWAT 2020, arXiv:2005.01098), Theorem 1, preallocates a fixed memory block and guarantees no overflow with high probability for every polynomial-length sequence of insertions, deletions, and queries.  Definition 5 requires `Pr[FP_t] <= eps` for every operation sequence and time.  Their Carter reduction explicitly says that after applying a fully random uniform fingerprint map, the induced adversary is oblivious with respect to the random multiset (Claim 7 and Lemma 8).

Thus “oblivious sequence + polynomial horizon + whp overflow + fixed allocated memory” is an established dynamic-filter construction model, not a publishable modeling contribution.

Bercea--Even, *A Space-Efficient Dynamic Dictionary for Multisets with Constant Time Operations* (arXiv:2005.02143), Theorem 1 and Corollary 2, also give polynomial-horizon whp dynamic multiset dictionaries/counting filters with constant-time operations.  Their space bounds retain an unspecified `O(n)` term; they do not determine the exact constant-error linear coefficient.

## 2. Retrieval does not close the problem

A retrieval structure can be converted into a filter by independently sampling a signature `h:U -> {0,1}^v`, storing value `h(s)` for every member `s`, and testing whether `R(x)=h(x)`.  With the signature oracle independent of the retrieval structure, a fixed nonmember has false-positive probability `2^{-v}`.

But membership insertion and deletion require **incremental/dynamic retrieval**, not value-dynamic retrieval.  Value-dynamic retrieval has a fixed key set and supports only changes to values.

Kuszmaul et al., *Tight Bounds and Phase Transitions for Incremental and Dynamic Retrieval* (arXiv:2410.10002v2), pp. 1--3, define:

* value-dynamic = queries plus value updates;
* incremental = additionally insertions;
* dynamic = additionally deletions.

For constant value size, their incremental bound is `nv+Theta(n log log n)` and their fully dynamic lower bound (Theorem 1.3) is `nv+Omega(n log log n)` for large polynomial universes, matching the earlier `nv+Theta(n log log n)` dynamic upper bound at the asymptotic level.  This is much larger than the desired exact `Theta(n)` constant-error filter space.  Retrieval stores stronger per-key information and does not exploit fingerprint collisions as a multiset.  Hence it does not explain away KLZ Section 6.

## 3. Nonuniform fingerprints

Let fingerprint bucket `j` have probability `p_j=lambda_j/n`, with `sum_j lambda_j=n`.  Under Poissonization, bucket `j` has occupancy `Poi(lambda_j)`.  Under the key-mass distribution

\[
\Pr[\Lambda=\lambda_j]=\lambda_j/n,
\]

define

\[
r(\lambda)=\frac{H_2(\operatorname{Poi}(\lambda))}{\lambda},
\qquad g(\lambda)=1-e^{-\lambda}.
\]

Then source entropy per key and collision FPR are `E r(Lambda)` and `E g(Lambda)`.  The distributional fingerprint-source optimum is the lower convex envelope of `(g(lambda),r(lambda))`.

For the Shannon rate, the tangent to endpoint `(1,0)` occurs at

\[
\lambda_*=0.4399316\ldots,
\qquad \varepsilon_*=0.3559195\ldots.
\]

Above this point, mixing load `lambda_*` with a load tending to infinity beats uniform fingerprints.  At `eps=1/2`, it gives approximately `2.2006115` bits/key rather than the uniform `2.2879040`.

For fixed-length exact composition coding of every residual multiset, use

\[
w(\lambda)=\frac{1+\lambda}{\lambda}\log_2(1+\lambda)-\log_2\lambda.
\]

Its endpoint tangent is different:

\[
\lambda_{wc}=0.4022985\ldots,
\qquad \varepsilon_{wc}=0.3312189\ldots.
\]

The two thresholds must not be conflated.  The first is an average source-entropy calculation; the second is the all-compositions fixed-length calculation.

## 4. Priority adjacency

### Weighted Bloom Filters

Bruck--Gao--Jiang, *Weighted Bloom Filter* (ISIT 2006), optimizes key-dependent numbers of Bloom-filter hashes under nonuniform input/query information.  Later work includes data-popularity-conscious and improved weighted Bloom filters.  These works allocate different false-positive protection to externally distinguished keys.

### Daisy Bloom Filters

Bercea--Houen--Pagh, *Daisy Bloom Filters* (arXiv:2205.14894v2), is especially close conceptually.  It studies a product input distribution `P` and query distribution `Q`, gives expected-space lower and upper bounds, and explicitly assigns `k_x=0`--always answer YES--to keys with high inclusion probability or sufficiently low query probability (pp. 1--5).  Its false-positive constraint is averaged over `Q`.

The proposed nonuniform-fingerprint model differs because no universe key has external popularity information.  A hidden random partition makes every fixed key identically distributed, so the KLZ pointwise-over-randomness FPR remains valid.  The optimized heterogeneity is among fingerprint buckets, not among known key classes.  This is a defensible distinction, but “always YES saves space” and convex time-sharing cannot be claimed as new ideas.

### ChainedFilter and learned filters

ChainedFilter (arXiv:2308.13632) develops a static membership chain rule and discusses distribution-aware/learned cases, but explicitly says the lossless chain rule does not hold for general dynamic membership.  Learned and partitioned learned filters allocate false-positive budgets using classifiers/query classes.  Again, their heterogeneity is externally data-dependent rather than a hidden exchangeable fingerprint alphabet.

### Adaptive/broom filters

Bender et al., *Bloom Filters, Adaptivity, and the Dictionary Problem* (arXiv:1711.01616), studies sustained FPR against adaptive queries using feedback and remote state.  Its “ghosts” are deleted fingerprints retained to prevent repeat attacks, not a permanent randomized YES region used for a static pointwise error/space tradeoff.  This literature is relevant to adversarial operation sequences but does not contain the proposed occupancy-entropy phase theorem.

### Priority search result

Searches across Crossref, DBLP, Semantic Scholar citation graphs, arXiv sources, and the above adjacent papers found no work phrased as optimizing an exchangeable nonuniform fingerprint alphabet by the Poisson-occupancy entropy convex envelope, nor a theorem giving the exact dynamic linear coefficient and its phase transition.  This is evidence of a plausible open niche, not an exhaustive proof of novelty.  The greatest priority risk is Daisy/Weighted Bloom filter reviewers viewing the result as a repackaging of randomized false-positive allocation.

## 5. What theorem package is sufficient

### Too weak

Any of the following alone is unlikely to support a major TCS submission:

* the formula `rho(eps)=H(Poi(-ln(1-eps)))/(-ln(1-eps))`;
* typical-set ranking with unbounded update time;
* the one-dimensional convex-envelope calculation;
* an oblivious polynomial-horizon model without a new exact bound;
* a permanent YES region without a converse.

### Credible ESA/ICALP/SODA package

1. Define a broad generalized-fingerprint class allowing arbitrary, possibly `n`-dependent, exchangeable public-random fingerprint distributions and arbitrary encodings of their multiplicity vector.
2. Prove a matching converse reducing every such scheme--including heavy atoms whose loads diverge--to a load-distribution optimization.  Establish Poissonization/de-Poissonization uniformly.
3. Prove the analytic phase theorem: uniqueness of the tangent point, the exact two-component optimizer, and strict separation from uniform hashing.
4. Give a fixed-preallocated-space dynamic structure attaining the exact rate over every polynomial-length oblivious operation sequence, with constant-time operations whp and pointwise one-sided FPR.  This likely requires a distribution-sensitive refinement of the Bercea--Even random-multiset dictionary whose redundancy is `o(n)`, not an unspecified `O(n)`.
5. State and prove all overflow, metadata, hash-representation, deletion/multiplicity, and temporary-rebuild-space costs.

Items 1--3 plus an offline source code are probably a short-note result.  Items 1--4 form a plausible ESA/ICALP paper and could be competitive at SODA if the data-structural implementation is substantial.  A matching lower bound for arbitrary dynamic filters, rather than only fingerprint filters, would elevate the result to the full KLZ Section 6 problem.

## 6. Other intermediate directions

* **Expected versus fixed space:** a general separation theorem could be interesting, but merely observing Shannon versus enumerative coding is standard.  It needs a sharp impossibility or conversion theorem under dynamic updates.
* **Oblivious versus adaptive update sequences:** the distinction is important and connected to adaptive AMQs, but a restricted oblivious theorem is already standard.  A sharp space separation at constant error could be publishable.
* **Deletion requires multiplicities:** dynamic multiset dictionaries already solve multiplicity updates at the leading-term level.  The open contribution is their exact distribution-sensitive linear constant.
* **External exact set/rebuild advice:** retrieval and broom-filter literature already trades remote/external state for stronger guarantees.  A new theorem needs an explicit advice-space-versus-local-rate curve, not just a reduction.

