# Review: "Optimal Trading Against a Signal: a Wiener-Hopf Approach"

**Artifact:** `tex/factorization-optimal-trading.tex` (local LaTeX draft, compiled PDF present)
**Review focus:** mathematical correctness and relevance
**Date:** 2026-07-14
**Method:** full read of the .tex and .bib; hand verification of every displayed formula; targeted numerical experiments (`experiments/review_factorization_check.py`); direct inspection of the Forde–Sánchez-Betancourt–Smith (FSS) 2022 paper.

---

## Summary Assessment

The whole-line theory is sound. Every whole-line computation I checked is correct: the Fourier constant c_β, the symbol split |ξ|^{β−1} = (iξ)^{−ν}(−iξ)^{−ν}, the causality assignment of the factors under the stated convention, the projected-inverse identity (Lemma 1) in the order stated, the appendix FOC verification for Corollary 1, both OU closed forms (θ^ν whitening for the power law; the (κ²−θ²)/2κγ sign-flip formula for the exponential), the OU spectral-hypothesis threshold β > 1/2, and the temporary-impact crossover frequency.

The finite-interval theory contains a factorization-order error that invalidates Corollary 2 as written and weakens Theorem 1's finite-interval clause and Proposition 3. The projected-inverse identity (P₊CP₊)⁻¹ = C₊⁻¹P₊C₋⁻¹ holds for factorizations C = C₋C₊ with the **causal factor on the right** (verified analytically on a 2-period model and numerically to machine precision; the opposite order fails by ~10⁻¹ in the same test). Proposition 2 and the explicit kernel (eq. \eqref{eq:volterra-kernel}) instead deliver G_T = TT* with T causal — the opposite order. I verified numerically that the draft's kernel does satisfy TT* = G_T exactly (constant included), and that T*T is horizon-dependent, so no reinterpretation rescues the order. The correct causal-right factor is the time reflection of T, with endpoint weights anchored at T rather than 0. Corollary 2's boundary weights B(t) = t^{−ν} are therefore anchored at the wrong endpoint.

Two further quantitative claims are wrong as stated (the stationary spectrum of ζ in §4.2 and the value functional in §5.5 both drop the adapted projection — the draft's own OU formula is a counterexample), and the uniform KKT-multiplier bound is attributed to a proposition that does not exist in FSS 2022.

The literature positioning (§1.3) is accurate and well-targeted; the contribution claim (bulk closed form, fractional-calculus structure) is genuine relative to the cited prior work, conditional on repairing the finite-interval results.

---

## Strengths

- **Whole-line results verified correct.** All symbol computations, factor causality assignments, and the two OU worked examples check out by hand (evidence notes items 1–14). The sign-flip contrast between exponential (transition at θ = κ) and power-law (no transition) kernels is correct and is a genuinely informative result.
- **The projected-inverse identity is true** (in the correct order) and its whole-line application is clean. My discrete Gaussian test reproduces the directly computed adapted optimum to 2.6×10⁻¹⁶.
- **The explicit finite-interval kernel is a correct factorization of G_T** — numerically exact for β ∈ {0.3, 0.5, 0.7}, including the constant c_β. The raw material for a fixed Corollary 2 is present.
- **Accurate literature review.** The characterizations of Lehalle–Neuman, Neuman–Voß, Abi Jaber–Neuman, GSS, and FSS match the sources I inspected. The novelty claim (no prior bulk closed form for adapted rate under power-law kernel with stochastic signal) is consistent with FSS's Fredholm/Volterra representation, which is horizon-tied as the draft says.
- Honest handling of the unboundedness of the pure power-law operator (§4.1 boundedness caveat) and of limitations (§6).

## Critical Issues

**C1. Finite-interval factorization order is wrong (Prop 2 → Thm 1 → Cor 2 → Prop 3).**
Lemma 1 assumes C = C₋C₊ with C₊ causal and proves (P₊CP₊)⁻¹ = C₊⁻¹P₊C₋⁻¹. This order requirement is real: on a 2-period model with sequentially revealed signal, the identity with C = C₋C₊ (reverse-order/"UL" factorization) reproduces the adapted optimum exactly, while the Cholesky order C = C₊C₋ does not (numerical check: errors 2.6e−16 vs 8.5e−2). Proposition 2 asserts G_T = **TT*** with T causal — the LU order — and Theorem 1's finite-interval clause and Corollary 2 substitute exactly this into the lemma. The draft's kernel genuinely satisfies TT* = G_T (verified numerically, constant included) and cannot satisfy T*T = G_T (T*T is horizon-dependent while G_T's kernel is not), so the mismatch is not notational.
*Fix direction:* since RG_TR = G_T under time reflection R, G_T = (RTR)(RT*R) = C₋C₊ with causal factor C₊ = RT*R, whose kernel is c_β^{1/2}((T−s)/(T−t))^ν (t−s)^{ν−1}/Γ(ν). The corrected Corollary 2 has endpoint weights B̃(t) = (T−t)^{−ν} anchored at the **terminal** boundary (which is also the natural anchor: the informational asymmetry of adaptedness points forward). All of §4.3, Proposition 3, and the finite-interval statements in the abstract, §1.4, and §7 need rewriting accordingly. Note the draft is internally inconsistent here: §1.3 correctly quotes Gohberg–Krein as I+K = (I+L*)(I+L) (causal factor on the right), contradicting Prop 2's TT*.

## Major Issues

**M1. Spectrum of ζ (§4.2) drops the adapted projection.**
The claim "ζ has stationary power spectrum c_β^{−1}|ξ|^{1−β}S_α(ξ)" is the spectrum of the *unprojected* whitening C₋⁻¹α. The draft's own OU result is a counterexample: ζ_s = θ^ν α_s has spectrum θ^{2ν}S_α(ξ) ≠ c_β^{−1}|ξ|^{1−β}S_α(ξ). The correct statement involves the forecast-curve (projected) whitening; the flat-spectrum property holds only in the perfect-foresight limit.

**M2. Value functional (§5.5) is the anticipative value, not the value "attained at u\*".**
At the adapted optimum, V = ½E⟨u*,α⟩ = (2γ)⁻¹E‖P₊C₋⁻¹α‖². The stated V(α) = (2γc_β)⁻¹∫|ξ|^{1−β}S_α(ξ)dξ equals (2γ)⁻¹E‖C₋⁻¹α‖² — an upper bound attained only for perfectly predictable signals. OU cross-check: the adapted value is smaller by exactly the factor sin(πβ/2). The qualitative point of §5.5 (spectral weighting ≠ R², timescale matters) survives, but the formula and the words "attained at u*" must change. This error is correlated with M1.

**M3. Phantom citation: FSS "Prop. 3.2" does not exist.**
FSS 2022 contains Theorem 2.2, Remarks 2.3–2.5 and 3.1, and Lemma A.1; its §3.2 is "Temporary price impact". There is no Proposition 3.2 and no uniform-in-T KKT-multiplier bound of the form cited. The draft cites [Prop.~3.2]{FordeSanchezSmith2022} twice (Proposition 3 and its appendix proof) as the load-bearing reference for the second term of the interior error bound. Either prove the bound or remove it.

**M4. Proposition 2's hypothesis does not cover the paper's application.**
For the power-law kernel, G_T is a compact operator with unbounded inverse — not a "strictly positive compact perturbation of the identity". The parenthetical "(equivalently, its symbol satisfies the whole-line Wiener–Hopf hypothesis)" is not an equivalence. As stated, the proposition excludes the paper's main use case; the factorization does exist (numerically exact here; FSS pp. 590–591 via Porter–Stirling Ex. 9.2), but under different hypotheses (weakly singular positive-definite kernel, factors between weighted spaces) that should be stated.

**M5. Proposition 3's proof is incomplete beyond M3.**
The proof bounds the Marchaud tail truncation and the KKT term, but omits the error from the endpoint-weight conjugation ((t/s)^ν ≠ 1), which is a third contribution of a priori comparable size. The d(t)^{−ν} scaling is plausible; it is not established. (After the C1 fix, this proof must be redone against the corrected formula anyway.)

**M6. "The multipliers μ_k solve a finite linear system" (Thm 1, Cor 2) is wrong for a.s. constraints.**
For the pathwise terminal-inventory constraint X_T = 0 in the adapted problem, the multiplier is process-valued (FSS's λ(u), one value per Wiener coordinate), not a finite vector. The finite-linear-system claim holds only for finitely many expectation constraints. State which constraint class is meant.

## Minor Issues

1. **Prop 1 uniqueness:** with the normalization conj(Ĉ₊) = Ĉ₋, the residual freedom is a *unimodular* constant, not a positive one (a positive c ≠ 1 breaks the product or the adjointness).
2. **Prop 2 uniqueness:** for G = TT*, the freedom is a *right* unitary (T → TU), not left.
3. **Terminology:** "Marchaud fractional integrals" (Contribution, §4, Conclusion) — the integrals I±^ν are Liouville/Weyl (Riemann–Liouville on the half-line); Marchaud names the derivative representation. The draft itself defines them as Riemann–Liouville in eq. \eqref{eq:marchaud-wh}.
4. **§5.4:** triangular-Toeplitz application/solve is O(N log N) for the whole grid, not "per time step".
5. **Exponential OU (eq. \eqref{eq:exp-ou}):** u* contains σẆ_t, so it is not an L² process pathwise; a remark on admissibility (mollification or interpretation as a distribution-valued optimum) is needed.
6. **§5.3 matrix Wiener–Hopf remark** ("available only when the eigenvalue crossings on the imaginary axis are absent") is vague; existence of matrix WH factorization is governed by partial indices — either cite (e.g. Gohberg–Krein 1958 matrix factorization) or cut.
7. The §5.5 value integral should state the spectral normalization (2π convention) to make the constant checkable.

## Reproducibility and Verification

| Item | Status |
|---|---|
| c_β constant, symbol split, factor causality (whole line) | Verified (hand computation) |
| Lemma 1, order C = C₋C₊ | Verified (2-period analytic + numerical, error 2.6e−16) |
| Lemma 1 with order C = C₊C₋ | Refuted (numerical error 8.5e−2) — confirms C1 |
| Eq. \eqref{eq:volterra-kernel}: TT* = G_T incl. constant | Verified numerically (β = 0.3, 0.5, 0.7; ratio ≡ 1.000000) |
| T*T = G_T | Refuted (horizon-dependent) |
| Power-law OU: ζ = θ^ν α, conditional mean θ^{1−β}α/γc_β | Verified (hand computation) |
| Exponential OU: sign flip at θ = κ | Verified (hand computation) |
| §4.2 spectrum of ζ | Refuted (OU counterexample) — M1 |
| §5.5 value formula | Refuted (projection dropped; OU factor sin(πβ/2)) — M2 |
| FSS Thm 2.2, TT* decomposition, pp. 590–591 | Verified against FSS PDF |
| FSS "Prop. 3.2" | Refuted (does not exist in FSS) — M3 |
| Arveson 1975 Thm 4.4.2, Hytönen et al. Prop 2.6.13, Klenke Thm 14.16 numbering | Verification: NOT RUN (sources not inspected; flag for author check) |
| Neuman–Voß 2022 bibliographic data | Not re-verified this session (verified per project CHANGELOG 2026-07-11) |

Experiment script and outputs: `experiments/review_factorization_check.py`. Evidence notes: `outputs/.drafts/factorization-optimal-trading-review-evidence.md`.

## Inline Annotations

- **Abstract, sentence 4** ("On a finite horizon the same recipe produces an optimal policy…"): contingent on C1 fix; the recipe as instantiated in §4 uses the wrong factor.
- **§1.3, Gohberg–Krein sentence** (I+K = (I+L*)(I+L)): correct, and inconsistent with Prop 2's G_T = TT*. Keep this order; fix Prop 2.
- **Prop 1**: "unique up to a positive multiplicative constant" → unimodular (Minor 1).
- **Prop 2**: hypothesis excludes power-law G_T (M4); "left unitary" → right (Minor 2); ordering (C1).
- **Lemma 1**: statement and both appendix proofs are correct for C = C₋C₊; the finite-interval appendix paragraph ("Replace C_± by the Gohberg–Krein factors T, T*… applies verbatim") is where C1 enters — with C₊ = T, C₋ = T* one needs G_T = T*T, which is false for the paper's T.
- **Theorem 1, finite-interval clause**: needs the reflected factor (C1) and a corrected multiplier statement (M6).
- **Eq. \eqref{eq:bdry} (Cor 2)**: weights B(t) = t^{−ν} should be (T−t)^{−ν}-anchored after the C1 fix; the claimed equivalence to FSS Thm 2.2 should then be re-derived, not asserted.
- **§4.2, sentence "The intermediate process ζ has stationary power spectrum…"**: false as stated (M1).
- **§4.3 and Prop 3**: rewrite after C1; remove FSS Prop 3.2 citations (M3); add weight-deviation term (M5).
- **§5.5, "the whole-line value attained at u* takes the form V(α)…"**: replace by projected-whitening value or relabel as anticipative upper bound (M2).
- **§7 Conclusion, final paragraph**: "boundary-deformed fractional derivative… converges… at rate O(d(t)^{−ν})" — soften until Prop 3 is proved.

## Recommendation

**Major revision.** The whole-line core (Lemma 1, Theorem 1 on ℝ, Corollary 1, both OU examples, §5.1–5.2) is correct and publishable in substance. The finite-interval strand (Prop 2 as applied, Theorem 1 on [0,T], Corollary 2, Prop 3) must be repaired: use the time-reflected, terminal-anchored causal factor; restate Prop 2 with hypotheses covering compact G_T; re-derive the boundary-deformed formula and interior error bound; remove the phantom FSS Prop 3.2 citations. Fix the two projection-dropping claims (§4.2 spectrum, §5.5 value), which currently overstate results the paper does not need to overstate. The fixes look mechanical rather than fatal — the reflection argument gives the corrected factor in closed form — but they change displayed formulas, so the revision is major.

## Sources

- Artifact: `tex/factorization-optimal-trading.tex`; bibliography: `tex/factorization-optimal-trading.bib` (local)
- Verification script: `experiments/review_factorization_check.py` (this session; outputs quoted in evidence notes)
- Evidence notes: `outputs/.drafts/factorization-optimal-trading-review-evidence.md`
- Forde, M., Sánchez-Betancourt, L., Smith, B. (2022). "Optimal trade execution for Gaussian signals with power-law resilience." *Quantitative Finance* 22(3), 585–596. https://doi.org/10.1080/14697688.2021.1950919 — open-access PDF: https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26/files/srf55z9197
- Gohberg, I., Krein, M.G. *Theory and Applications of Volterra Operators in Hilbert Space*, AMS: https://bookstore.ams.org/MMONO/24
- Triangular factorization of positive operators (convention S = S₋S₊): https://doi.org/10.1007/978-3-7643-8539-2_17
