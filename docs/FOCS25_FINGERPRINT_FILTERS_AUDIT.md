# Audit of Kuszmaul--Liang--Zhou, *Fingerprint Filters Are Optimal*

Source audited: arXiv:2510.18129v1, dated 20 October 2025, PDF pp. 1--21. The source archive and PDF are stored under `/tmp` for this audit; the public identifier is [arXiv:2510.18129](https://arxiv.org/abs/2510.18129).

## Exact model and Theorem 1.1

Definition 2.1 (PDF pp. 2--3) fixes capacity `n`, error parameter `eps`, and a finite universe `U`. A randomized dynamic filter maintains an arbitrary current set `S subseteq U` of size at most `n` and supports `Initialize`, `Query`, `Insert`, and `Delete`.

The guarantee is pointwise: for every queried `x in S`, `Query(x)` is true deterministically; for every `x notin S`, `Query(x)` is false with probability at least `1-eps`, where probability is over the algorithm's randomness and `x` is not random. Updates receive only the current memory, the update key, and the random tape; the algorithm is not given `S` explicitly.

The computational model is deliberately permissive for time: a fixed-length `H`-bit memory can be accessed arbitrarily. Randomized algorithms additionally get an infinite read-only tape of independent random bits, which is not charged to `H` (Preliminaries, PDF p. 2; footnote 5 explains simulation by a random-bit pointer).

Theorem 1.1 (Introduction, PDF p. 2; restated at start of Section 3) says:

> If `eps=o(1)`, `|U|=omega(n eps^{-1})`, and the algorithm can support a sequence of `omega(n)` insertions and deletions, then every such dynamic filter uses at least
> `n log(eps^{-1}) + n log e - o(n)` bits.

The lower bound is a fixed-memory (therefore worst-case space) statement. It is not an expected-space or high-probability-space bound. There is no additional failure event in the theorem: the only error is the pointwise false-positive probability in Definition 2.1. The random tape is public to Alice and Bob in the communication proof and free in the data-structure space measure.

The phrase “support a sequence of `omega(n)` insertions and deletions” is weaker than a bound for all infinite operation sequences: it is enough that the implementation can execute some sequence whose length grows superlinearly in `n`; the proof chooses its own sequence. Since the theorem is information-theoretic, no operation-time restriction appears.

## Proof architecture and where `eps=o(1)` enters

* Section 3, Proposition 3.1 (PDF p. 3): history-independent and monotone filters. A one-way protocol sends a random ordered `n`-tuple of distinct keys. The filter state is sent first; each key is then encoded from a shrinking accepted-set difference. Claim 3.2 (PDF p. 4) gives the communication entropy lower bound `log |U|^{underbar n}`. Claim 3.3 (PDF p. 6) bounds the single-key coding cost. Lemma 3.4 (PDF p. 8) gives the factorial saving `log(n!/n^n)=-n log e+o(n)`, using Karamata's inequality (Theorem 3.5, PDF p. 9).
* Section 4, Proposition 4.3 (PDF p. 10): removes history independence using a public-random obfuscating tree and batching parameter `b`. Claim 4.4 is the entropy lower bound (p. 12); Lemma 4.5 and Claims 4.6--4.7 control one batch and the obfuscation coupling (pp. 15--16); Lemma 4.8 removes the small additive term inside the logarithms (p. 18). The tree depth is `b=omega(1)` but chosen sufficiently slowly; its operation count is `n M^{b+1}/b`, so the proof can fit any prescribed `f(n)=omega(n)` operations.
* Section 5, Lemma 5.3 (PDF p. 20): removes monotonicity by replacing the accepted set by a reconstructible set (Definition 5.2, p. 20), defined over histories conforming to a random universe partition (Definition 5.1, p. 19). The reconstructible set is contained in the actual accepted set, contains the true set, and is monotone along the required prefixes.

The key estimate in the warmup (Claim `clm:entropy_single_key_independent`, source `warmup.tex`) bounds a key's expected coding cost by
`log |U| + (1-eps) log a_(ell,r] + log eps + o(1)`.
The final `o(1)` uses both `eps=o(1)` and `|U|=omega(n eps^{-1})`: specifically `h(eps)=o(1)`, `log(1-eps)=o(1)`, `eps log eps=o(1)`, and `log(((1-eps)n+eps|U|)/(eps|U|))=o(1)`. The proof then multiplies `(1-eps)` by the factorial inequality and replaces it by `1` at an `o(n)` loss. For constant `eps`, these simplifications are not negligible. Section 4 also selects `b` using `9^{b^2}=o(eps|U|/n)`; this remains possible when `eps` is fixed and `|U|/n -> infinity`, but it does not repair the constant-error entropy terms.

## What Section 6 actually leaves open

Section 6 (PDF p. 21) has a paragraph titled “Tight upper and lower bounds for `eps^{-1}=Theta(1)`.” It states:

1. The paper proves optimality only for `eps=o(1)`.
2. The authors conjecture fingerprint filters remain optimal for constant error.
3. For constant error, fingerprints form a **multiset**, not a set; a space-optimal implementation must encode that multiset information-theoretically optimally according to the distribution from which it is generated.
4. Even constructing such a fingerprint filter with time-efficient operations is open.
5. Strong constant-error lower bounds are also open; the current proof does not become tight by merely doing more careful bookkeeping.

No constant-error target constant or matching formula is stated in the paper.

## Natural occupancy interpretation of the multiset sentence

Take a fingerprint range of size `q=n/lambda` and hash `n` keys independently and uniformly. To obtain asymptotic false-positive rate `eps`, choose
`lambda=-ln(1-eps)`, because an absent key collides with at least one stored fingerprint with probability
`1-(1-1/q)^n -> 1-exp(-lambda)=eps`.

Let `C_j` be the number of keys mapped to bucket `j`. The vector `(C_1,...,C_q)` is multinomial. In the sparse occupancy limit, bucket counts are asymptotically independent `Poi(lambda)` variables, conditioned on their sum being `n`; conditioning costs only `O(log n)` bits. Consequently the Shannon entropy of the count vector is
`q H(Poi(lambda)) + o(n)`, giving the natural entropy rate
`rho(eps) = H(Poi(lambda))/lambda` bits per stored key.

This is exactly the most literal mathematical realization of the Section 6 phrase “encode this multiset ... based on the distribution that the multiset comes from.” It is **not** a theorem or notation in KLZ25. As `eps -> 0`,
`rho(eps)=log(eps^{-1})+log e+o(1)`, matching Theorem 1.1. Numerically, `rho(1/2)=2.287904...` bits/key and `rho(1/4)=3.378498...` bits/key.

The rate must not be confused with the number of all possible multisets. Enumerative fixed-length coding of every weak composition of `n` into `q` bins costs
`log binom(n+q-1,n)`, whose per-key limit is `(1+1/lambda) H_2(lambda/(1+lambda))`; for `eps=1/2` this is about `2.384500` bits/key, strictly above `rho`. Shannon/arithmetic coding reaches `rho` only in expected (or suitably high-probability plus a tail code) length under the multinomial source.

## Why the upper bound is genuinely open

The KLZ model charges a single fixed worst-case memory length and requires updates for arbitrary valid insertion/deletion sequences. An entropy coder for the final random fingerprint multiset does not by itself provide:

* a fixed-length bound for every multiset and every operation history;
* local, time-efficient increment/decrement updates to a succinct codeword;
* decodability of membership queries while counts are modified;
* a way to handle codeword length fluctuations without paying a linear worst-case slack;
* preservation of pointwise one-sided FPR with the random hash function on the free tape.

Thus `rho(eps)` is a rigorous candidate for the optimal **average source-coding rate** of the canonical fingerprint multiset, but turning it into a dynamic filter with worst-case `n rho(eps)+o(n)` bits is precisely the missing upper-bound problem identified in Section 6. A claimed solution must state its space convention explicitly (worst-case fixed length vs expected/whp) and account for update time and all metadata.

## Prior-work boundary

The introduction records the relevant pre-2025 bounds: Carter et al. static lower bound `n log eps^{-1}`; Lovett--Porat's `n log eps^{-1}+n f(eps)` lower bound even for incremental filters; Kuszmaul--Walzer's `n log eps^{-1}+0.35n-o(n)` lower bound for `eps=o(1)`; and Bender et al.'s dynamic fingerprint construction at `n log eps^{-1}+n log e+o(n)` bits in their stated range of `eps`. KLZ25 closes the dynamic lower-bound gap only in the regime `eps=o(1)`.

The audited source is v1 (20 Oct 2025). I found no evidence in the supplied source archive of a later revision or a theorem resolving the Section 6 constant-error question. Any 2026 literature search should therefore be reported separately and should not silently upgrade the conjecture into a known result.
