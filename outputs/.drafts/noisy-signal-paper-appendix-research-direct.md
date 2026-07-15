# Direct-research notes: appendix sources

## Search log
1. `web_search` "Wiener-Hopf scalar spectral factorization outer function H2 Hardy space statement" — confirmed canonical statement: nonneg integrable f with log f ∈ L¹(T) (Paley–Wiener / Szegő condition) admits a unique outer factor f_+ with f = |f_+|². Sources: arXiv:1603.01101 (Ephremidze).
2. `web_search` "Frullani integral generalisation Gamma(-alpha) kappa^alpha derivation" — Frullani identity is classical; the form ∫₀^∞ s^{-α-1}(e^{-κs} − 1) ds = Γ(−α) κ^α follows from the standard Frullani/Mellin extension (analytic continuation of Γ at negative argument). Refs: HAL hal-04611843; arXiv:2605.26153.
3. `web_search` "Hosking 1981 fractional differencing operator (1-L)^d binomial expansion ARFIMA" — direct PDF of Hosking 1981 confirms (1−B)^d = Σ_{k≥0} C(d,k)(−B)^k (generalised binomial expansion); Granger–Joyeux 1980 also introduces the same operator. Refs: Hosking 1981 PDF; Granger–Joyeux 1980 Wiley DOI.

## Sources accepted for appendix citations
- Hosking JRM (1981), "Fractional Differencing", Biometrika 68(1):165–176. — already in paper Sources [#17].
- Granger CWJ & Joyeux R (1980), J. Time Series Analysis 1(1):15–29. — already in paper Sources [#16].
- Samko–Kilbas–Marichev (1993) — already in paper Sources [#15], used for Marchaud form.
- Wiener (1949) — already in paper Sources [#14].
- Bochner's theorem and Paley–Wiener / Szegő condition — textbook (no new ref needed; will cite Wiener [#14] and refer to the standard statement).
- Frullani / Γ(−α)κ^α — derive in-line using analytic continuation of Γ; no new ref required beyond Samko–Kilbas–Marichev [#15].
- Gatheral (2010) for positive-definiteness ↔ no-dynamic-arbitrage — already in paper Sources [#2].

No new external references need to be added to the paper. All appendix claims map either to standard textbook results (proved in-place) or to existing entries in the bibliography.

## Mapping of appendix items to load-bearing claims in the main text

| Code | Main-text location | Appendix entry | Status of proof |
|------|--------------------|----------------|------------------|
| L1   | §2.4 PD ⇔ no dyn-arb       | B.1 | Short proof (Parseval); cite Gatheral [Gat10]. |
| L2   | §3.2 eq. (2)                | B.2 | Direct LF computation; closed form. |
| L3   | §4.1 eq. (4)–(6)            | B.3 | Variational derivation; orthogonality decomposition. |
| L4   | §4.2 spectral factorisation | B.4 | State Szegő condition; refer to Wiener (1949), prove uniqueness up to unimodular constant. |
| L5   | §5.5 eq. (12c)              | B.5 | Full proof (Gaussian projection = conditional expectation; Markov property). |
| L6   | §6.3 eq. (15b)              | B.6 | Frullani / Γ-analytic-continuation; derive Γ(1−α)=−αΓ(−α). |
| L7   | §6.3 eq. (15c)              | B.7 | Generalised binomial theorem evaluated at z=ρ; cite Hosking 1981. |
| L8   | §7.3 Proposition            | B.8 | Tower property + orthogonality of η⊥f, joint Gaussianity ⇒ E[f|F̃] is sufficient statistic. |

## Definitions to formalise in Appendix A

- A.1 Signal / trade-rate process (WSS in `ℓ²`)
- A.2 Symmetric admissible impact kernel (PD, real, even, Szegő)
- A.3 Cost norm / inner product `‖·‖_K`
- A.4 Hardy spaces `H²_±(T)`, causal/anticausal projection `[·]_±`
- A.5 Spectral factorisation `K̂ = K̂_+ K̂_-` and outer functions
- A.6 Wiener filter (causal Wiener–Hopf solution)
- A.7 Marchaud anticausal fractional derivative `D^α_-`
- A.8 Fractional difference operator `Δ^α` (Hosking)
- A.9 Kernel innovation `K_+^{-1} * f`

These are the formal objects used implicitly throughout the paper; the appendix simply collects them in one place.
