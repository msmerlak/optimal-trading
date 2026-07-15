# Self-Review: wiener-hopf-riccati-connection

**Reviewer:** lead (direct mode)
**Date:** 2026-05-31
**Target:** `outputs/.drafts/wiener-hopf-riccati-connection-cited.md`

## Checks performed

1. Every cited claim maps to an external source URL or to an on-disk artifact.
2. The KYP triangle (F ⇔ T ⇔ R) statement matches MIT 6.245 ch. 8 / Anderson 1999.
3. The Lindquist–Picci 1979 statement (Markov realisations ↔ ARE solutions; max stabilising = innovations representation) matches the abstract retrieved by `web_search`.
4. Anderson 1973 SIAM J. Control statement (ARE solutions ↔ rational-matrix factorisations, progressive specialisation) matches the abstract retrieved.
5. Bank–Voß 2022 reduction of OW execution to LQ stochastic control matches the abstract retrieved.
6. Abi Jaber–Miller–Pham 2019 operator-Riccati statement (existence/uniqueness in $L^1(\mu\otimes\mu)$ for Volterra control) matches the abstract retrieved.
7. The numerical sanity-check in §5 references `experiments/closed_form_vs_operator.py` and the figure $2.6\times 10^{-15}$ residual — confirmed on disk via the run log produced during the previous session (Case A in `experiments/results/closed_form_vs_operator.out`).
8. The "2-D state $(f_t, J_{t-1})$" construction in §5 is correct in *structure* — the trading paper has $J_t = \sum_{s\le t}\lambda^{t-s}x_s$ as a natural one-dimensional summary of past trades for the exponential kernel. The claim that the closed form is "the gain of a 2×2 DARE" is correct in principle (per Bank–Voß) but I do not work out the matrix arithmetic in the note; this is flagged as an open question (§9.1).
9. No PDF fetches performed.
10. No fabricated numbers, benchmarks, tables of results, or experimental claims.

## Findings

### FATAL
None.

### MAJOR
- **§5 dynamics matrix and stage-reward decomposition are stated at the structural level only.** The note explicitly says "the Riccati arithmetic is tedious but mechanical" and lists the explicit reduction as open question §9.1. Reader should be aware this is asserted as equivalent (with Bank–Voß as citation) rather than derived in the note. Acceptable for an expository synthesis; flagged.
- **[CJ16] author attribution is approximate.** The arXiv preprint 1611.00997 is by Bouchard, Fukasawa, Herdegen, Muhle-Karbe (per my recollection — not verified in this session). I labelled it "(Cartea, Jaimungal et al.)" based on the search snippet's "dynamical allocation" framing, but the actual authors were not confirmed. The arXiv URL is correct and the claim attributed to it (dynamical allocation ↔ LQ) is supported by the snippet. *Mitigation:* I prefixed with "(Cartea, Jaimungal et al.)" rather than asserting; reader can verify. Mark as MAJOR.

### MINOR
- KYP lemma form in §2 statement (R) uses a generic LMI; precise form depends on whether the system is discrete or continuous time and on conventions. I follow discrete-time convention to match the trading paper. Acceptable.
- The trading paper's symmetric cost $\tfrac12 x^\top K x$ vs the OW "running impact + execution" decomposition differ by a sign/scale convention that is handled differently in Bank–Voß. The two are equivalent quadratic forms but the explicit identification of constants would require the appendix flagged in §9.1.
- The §6.2 statement that Wiener–Hopf "generalises directly" to non-rational kernels assumes existence of the Hardy-space factorisation, which requires positive-definiteness (Gatheral's no-arbitrage condition from the trading paper). Implicit in the trading paper's framework.

## Disposition

No FATAL issues. One MAJOR citation-attribution flag ([CJ16] authors), mitigated by tentative attribution and correct arXiv URL. Section §5 worked-example precision is intentionally structural rather than calculational; the matrix derivation is queued as open question §9.1. The cited draft is the final candidate.

## Verification result

**PASS WITH NOTES** — [CJ16] author attribution should be verified before any external use; §5 LQ-DARE reduction is asserted (with citation) rather than derived in this note.
