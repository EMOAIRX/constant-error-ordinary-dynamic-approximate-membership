# Reviewer-hostile priority audit: nonuniform constant-error fingerprint filters

Date of audit: 12 August 2026.

The purpose of this note is not to establish an exhaustive novelty guarantee.  It asks which existing papers a skeptical reviewer is most likely to cite in order to say that a nonuniform-fingerprint phase-transition result is already known, is a repackaging of weighted filters, or is too narrow.

## Verdict

No searched paper states the same theorem: an exact asymptotic linear coefficient for an exchangeable, pointwise-error fingerprint filter obtained by optimizing a hidden heterogeneous fingerprint alphabet, with a Poisson/multinomial occupancy converse and a constant-error phase transition.

However, each elementary ingredient has close precedent:

* nonuniform false-positive allocation: Weighted Bloom Filters and learned/partitioned filters;
* storing no information and always answering YES on a class: Daisy Bloom Filters;
* variable or elastic fingerprints: cuckoo/quotient-filter engineering literature;
* dynamic fingerprint multiplicities: Pagh--Pagh--Rao and Bercea--Even multiset dictionaries;
* source-distribution coding of a fingerprint multiset: explicitly anticipated by KLZ25 Section 6;
* convexification by mixing two designs: standard information theory.

Therefore a paper cannot be sold on “nonuniform fingerprints,” “always-positive regions,” or “convex envelopes.”  The defensible new package is the class-wide exact coefficient, rigorous converse for arbitrary heterogeneous and heavy cells, analytic phase diagram, and a fixed-memory dynamic structure attaining it with `o(n)` redundancy.

## Closest theoretical literature

### KLZ25: *Fingerprint Filters Are Optimal*

KLZ25 Section 6 explicitly says that constant-error fingerprints form a multiset and must be encoded optimally according to the distribution from which the multiset comes.  It leaves both a time-efficient upper bound and strong lower bounds open.  It does not specify a uniform Poisson formula, a nonuniform alphabet, a convex envelope, or a phase transition.

Safe distinction: the new work identifies and solves an optimization problem left implicit by KLZ, and must not attribute its candidate formula to KLZ.

### Weighted Bloom Filter, ISIT 2006, and successors

Weighted Bloom Filters choose key-dependent numbers of Bloom-filter hashes under nonuniform input/query weights.  Successors include data-popularity-conscious and improved weighted Bloom filters.

Overlap: heterogeneous protection, error-budget allocation, optimization over classes of keys.

Difference: the weights are externally attached to distinguishable universe keys or query frequencies.  In the proposed model all original keys are exchangeable; a hidden public-random permutation assigns them to heterogeneous fingerprint loads, and every fixed nonmember has the same marginal pointwise error probability.  The representation is an entropy-coded fingerprint multiplicity vector, not a Bloom bit array with key-dependent hash counts.

Reviewer risk: high at the level of intuition, low at the level of the proposed exact theorem if the exchangeability and pointwise quantifiers are explicit.

### Daisy Bloom Filters, arXiv:2205.14894v2 (2024)

Daisy Bloom Filters studies product input distribution `P` and query distribution `Q`, proves expected-space lower and upper bounds, and explicitly sets `k_x=0`--always answer YES--for high-inclusion or low-query-probability keys.

Overlap: permanent YES classes, distribution-aware space minimization, matching information-theoretic bounds, constant-time filter construction.

Difference: Daisy's heterogeneity is external and semantic (`p_x,q_x`), its FPR is averaged over `Q`, and its space objective is expected over sets drawn from `P^n`.  The proposed hidden-load construction preserves exchangeability and KLZ-style pointwise-over-randomness FPR for every fixed key; it optimizes collision multiplicity entropy under fully dynamic membership.

Unsafe claim: “we are the first to deliberately spend error probability by always answering YES on a region.”

### ChainedFilter, SIGMOD 2024 / arXiv:2308.13632

ChainedFilter develops a static membership chain rule and combines elementary filters.  It discusses distribution-aware and learned filters, but explicitly notes that its lossless chain rule does not extend to general dynamic membership.

Overlap: information-theoretic decomposition and combining multiple filter regimes.

Difference: no dynamic fingerprint-multiset exact coefficient or hidden-load occupancy optimization.

### Pagh--Pagh--Rao and Bercea--Even

Pagh--Pagh--Rao (SODA 2005) uses a dynamic multiset dictionary for fingerprints.  Bercea--Even, arXiv:2005.01098, gives a dense dynamic filter with fixed allocated memory, constant-time operations whp, and polynomial operation horizons.  Bercea--Even, arXiv:2005.02143, gives dynamic dictionaries for arbitrary multisets and counting filters.

Overlap: deletions require exact fingerprint multiplicities; random-multiset dictionaries; polynomial-horizon overflow model; constant-time dynamic operations.

Difference: their space is stated as a leading term plus an unspecified `O(n)`, exactly hiding the constant sought here.  Their Carter reduction uses a uniform fingerprint map and does not optimize unequal bucket loads or occupancy-source entropy.

Unsafe claims: “first dynamic multiplicity-aware fingerprint filter”; “first fixed-space polynomial-horizon filter”; “first constant-time dynamic random-multiset dictionary.”

### Adaptive/broom filters

Bender et al., arXiv:1711.01616, uses variable-length fingerprints/adaptivity bits and retains deleted fingerprints as “ghosts” to prevent repeated false-positive attacks.  It trades local and remote state for sustained FPR against adaptive queries.

Overlap: variable fingerprint information, ghosts, dynamic filters.

Difference: its ghosts encode deletion history and repair adaptive false positives.  They are not a randomly placed permanent YES component optimizing a single-query pointwise space/FPR curve.

Unsafe claim: “first use of ghosts in an AMQ.”

## Variable/flexible/elastic fingerprint papers

The following papers use language that could trigger a reviewer objection but appear technically different:

* Wu et al., *Elastic Bloom Filter: Deletable and Expandable Filter Using Elastic Fingerprints*, IEEE TC 2021: fingerprint flexibility for deletion/expansion.
* Lian--Wang--You, *Flexible Fingerprint Cuckoo Filter for Information Retrieval Optimization in Distributed Network*, Distributed and Parallel Databases 2024: flexible fingerprints in an engineering cuckoo-filter design.
* Zhang et al., *Bucket-Level Elastic Cuckoo Filter for Dynamic Set Membership Query and Encoded Set Operations*, IEEE/ACM ToN 2025: borrows fingerprint bits to create longer segment prefixes during bucket-level resizing.
* Ji et al., *PipeFilter*, IEEE TKDE 2025: pipeline-parallel cuckoo-filter architecture and high-load placement.
* Song--Yang, *Semantic Weight-Aware Cuckoo Filter*, 2026: appends quantized risk tags to fingerprints and uses weighted eviction.

These works optimize placement, expansion, throughput, deletion, or semantic prioritization.  None of the available metadata/abstracts gives an exact information-theoretic coefficient, Poisson occupancy converse, exchangeable biased fingerprint law, or constant-error convex-envelope phase transition.

Terminological warning: use “heterogeneous bucket probabilities/load distribution,” not the unqualified claim “variable fingerprints are new.”

## Retrieval literature

Value-dynamic retrieval cannot directly implement dynamic membership because its key set is fixed.  Fully dynamic retrieval can be reduced to a filter using independent random signatures, but for constant-size values it carries `Theta(n log log n)` redundancy in the large-polynomial-universe setting, far above the desired exact `Theta(n)` filter rate.  Cite Kuszmaul--Walzer STOC 2024 and Kuszmaul et al. arXiv:2410.10002.

## 2024--2026 search coverage

The audit searched Crossref, DBLP, Semantic Scholar paper search/citation metadata, arXiv PDFs/source archives where available, and references/citation graphs around Weighted Bloom Filters, Daisy, ChainedFilter, KLZ25, and Bercea--Even.  Search phrases included nonuniform/biased/weighted fingerprints, variable fingerprint length, constant-error optimal approximate membership, occupancy/multinomial entropy, dynamic multiset dictionaries, and always-positive regions.

The main 2024--2026 candidates located were ChainedFilter/SIGMOD 2024, Daisy v2/2024, flexible-fingerprint cuckoo filters/2024, PipeFilter/2025, bucket-level elastic cuckoo filters/2025, KLZ25, and semantic weight-aware cuckoo filters/2026.  No indexed result matched the proposed exact theorem.

Limitations:

* some IEEE/Springer full texts were closed, so model comparisons use abstracts and metadata;
* Semantic Scholar and OpenAlex rate limits intermittently prevented exhaustive citation expansion;
* absence from bibliographic search is not proof of novelty.

The closed 2024 flexible-fingerprint cuckoo paper should be obtained through library access before submission, although its venue/title/metadata indicate an implementation-oriented result rather than the same theory.

## Safe contribution statement

A conservative statement is:

> We characterize the optimal asymptotic space within a generalized class of exchangeable fingerprint filters that permits arbitrary hidden heterogeneous fingerprint loads.  The optimum exhibits a sharp constant-error phase transition and can strictly outperform uniform hashing.  Our converse covers arbitrary, possibly `n`-dependent, fingerprint alphabets and diverging heavy cells.  We further realize the optimal coefficient in a fixed-memory dynamic structure with `o(n)` redundancy over polynomial-length oblivious operation sequences.

This statement is safe only if all four components are proved.  Replace “optimal asymptotic space” by “source-coding optimum” if there is no dynamic fixed-memory implementation.  Add “within the generalized fingerprint class” everywhere unless an arbitrary-filter lower bound is proved.

## Claims that must not appear

* “We solve the KLZ25 constant-error problem” without a lower bound for arbitrary dynamic filters.
* “Fingerprint filters at constant error have rate `H(Poi(lambda))/lambda`” without optimizing nonuniform alphabets and specifying the space convention.
* “Uniform hashing is WLOG.”
* “First nonuniform/weighted/variable-fingerprint filter.”
* “First always-positive/ghost region.”
* “First entropy-coded fingerprint multiset.”
* “First dynamic multiset dictionary/counting filter.”
* “First oblivious polynomial-horizon fixed-memory dynamic filter.”
* “Convex-envelope phase transition alone resolves the dynamic upper bound.”

## Minimum package that avoids a “too narrow” rejection

1. A broad class definition covering arbitrary exchangeable, `n`-dependent fingerprint laws, rather than only a hand-designed two-tier construction.
2. A matching class-wide lower bound with uniform Poissonization/de-Poissonization and explicit treatment of heavy atoms.
3. An analytic phase theorem, not only numerical optimization.
4. A strict quantitative separation from uniform hashing on a nontrivial error interval.
5. A dynamic fixed-preallocated-memory implementation with `o(n)` redundancy and efficient operations, preferably constant or polylogarithmic time.
6. A precise comparison table against Weighted/Daisy, Bercea--Even/PPR, elastic/variable fingerprints, ChainedFilter, retrieval, and adaptive filters.

Items 1--4 alone are likely an information-theoretic short paper and remain vulnerable to “standard convexification” criticism.  Items 1--5 provide a credible ESA/ICALP submission and potentially SODA if the dynamic coding machinery is substantial.  A lower bound for arbitrary dynamic filters would address the full KLZ frontier.

