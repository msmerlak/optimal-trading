# Evidence notes — review of tex/factorization-optimal-trading.tex

Artifact: `tex/factorization-optimal-trading.tex` (read in full, 2026-07-14).
Companion: `tex/factorization-optimal-trading.bib` (read in full).
Experiment: `experiments/review_factorization_check.py` (written and run this session).

## Analytic checks (done by hand, this session)

### Verified correct
1. **Fourier constant.** FT of |t|^{-β} with e^{iξt} convention = 2Γ(1−β)sin(πβ/2)|ξ|^{β−1}. Matches draft's c_β. ✔
2. **Symbol split.** |ξ|^{β−1} = (iξ)^{−ν}(−iξ)^{−ν}, ν=(1−β)/2, principal branches: for ξ>0 phases e^{∓iπν/2} cancel. ✔ (−iξ)^{−ν} analytic/nonvanishing in UHP ⇔ causal under the stated convention; symbol of I_+^ν is (−iξ)^{−ν}, of I_−^ν is (iξ)^{−ν}. ✔ Assignment C_+ = c^{1/2}I_+^ν, C_− = c^{1/2}I_−^ν consistent. ✔
3. **Exponential kernel.** Ĉ = 2κ/(κ²+ξ²); factors √(2κ)/(κ∓iξ); C_+^{−1} = (2κ)^{−1/2}(κ+∂_t) has symbol (κ−iξ)/√(2κ) = 1/Ĉ_+, Ĉ_+ = √(2κ)/(κ−iξ) = FT of √(2κ)e^{−κt}1_{t≥0}, causal. ✔
4. **Lemma 1 (whole line / correct order).** Verified analytically on a 2-period toy model (C 2×2, signal revealed sequentially): the adapted optimum u_1 = [α_1 − (b/d)ᾱ_2]d/(ad−b²) is reproduced exactly by C_+^{−1}P_+C_−^{−1} **iff C = C_−C_+ (anticausal × causal, "UL")**. The Cholesky order C = C_+C_− ("LU") gives u_1 = α_1/a − ... ≠ correct. On the whole line convolutions commute, so whole-line results unaffected.
5. **Eq (proj-cma).** (P_+C_−^{−1}α)_s = (C_−^{−1}ᾱ(s,·))(s) by conditional Fubini. ✔
6. **Step (c) symbol identity.** c|ξ|^{β−1}(−iξ)^ν = c(iξ)^{−ν} ⇒ C D_+^ν = c I_−^ν. ✔
7. **Power-law OU whitening.** ᾱ(t,s)=e^{−θ(s−t)}α_t; Marchaud integral ∫_0^∞(1−e^{−θr})r^{−1−ν}dr = θ^νΓ(1−ν)/ν ⇒ ζ_t = θ^να_t. ✔ Conditional mean of D_+^να given α_t uses OU time-reversibility ⇒ θ^να_t; total coefficient θ^{2ν}=θ^{1−β}. ✔ Positive for all θ,β. ✔
8. **Exponential OU.** ζ_s=(κ+θ)α_s; u* = (κ+θ)/(2κγ)[(κ−θ)α_t+σẆ_t]; conditional mean (κ²−θ²)/(2κγ)α_t; sign flip at θ=κ. ✔ (Note u* contains white noise ⇒ not in L² pathwise; admissibility unremarked in draft.)
9. **OU spectral-hypothesis threshold.** ∫|ξ|^{2(1−β)+ε}/(θ²+ξ²)dξ<∞ ⇔ β>1/2+ε/2. Draft's "β>1/2" ✔.
10. **Marchaud tail bound.** ν∫_{T−s}^∞ 2‖f‖_∞ r^{−1−ν}dr = 2‖f‖_∞(T−s)^{−ν}/... matches draft constant. ✔
11. **φ₁ bound.** φ₁=[t(T−t)]^{−ν} = [d(T−d)]^{−ν} ≤ d^{−ν}(T/2)^{−ν}. ✔
12. **Crossover.** c|ξ|^{β−1}=η/γ ⇒ ξ*=(γc/η)^{1/(1−β)}. ✔ High-freq limit u≈α/η. ✔
13. **Weight-conjugation algebra.** T = c^{1/2}B^{−1}I_+^νB with B=t^{−ν} has kernel c^{1/2}(t/s)^ν(t−s)^{ν−1}/Γ(ν) = draft's k(s,t). ✔ Cor 2 substitution algebra (collecting c^{−1/2} factors) ✔ internally consistent.
14. **GSS endpoint weights** (t(T−t))^{(β−1)/2} = U-shaped, consistent with GSS/FSS §2.3. ✔

### Found incorrect / problematic
A. **Finite-interval factorization order (critical).** Lemma 1 requires C = C_−C_+ with C_+ causal (verified: 2-period analytic + numerical, below). Prop 2 asserts G_T = **TT*** with T causal (= C_+C_−). Numerics: TT* with the draft's kernel equals |t−v|^{−β} exactly (constant included), and T*T is horizon-dependent ⇒ with this kernel only TT* holds. Hence Theorem 1's finite-interval clause "C_± = T, T*" and Cor 2's formula plug the LU factorization into a UL identity. Exact reflection argument: RG_TR = G_T ⇒ G_T = (RTR)(RT*R) = U U* with U anticausal, i.e. the correct causal-right factor is C_+ = RT*R with kernel c^{1/2}((T−s)/(T−t))^ν(t−s)^{ν−1}/Γ(ν): **weights anchored at the right endpoint (T−t)^{−ν}, not t^{−ν}**. Also note draft §1.3 itself quotes Gohberg–Krein as I+K = (I+L*)(I+L) (UL) — internally inconsistent with Prop 2's TT*.
B. **Spectrum of ζ (§4.2).** Claim: ζ has spectrum c^{−1}|ξ|^{1−β}S_α. OU counterexample from the draft's own eq (ou): ζ_s = θ^να_s ⇒ spectrum θ^{2ν}S_α(ξ) ≠ c^{−1}|ξ|^{1−β}S_α(ξ). The stated spectrum is that of the *unprojected* C_−^{−1}α (perfect-foresight whitening).
C. **Value functional (§5.5).** V = ½E⟨u*,α⟩ = (2γ)^{−1}E‖P_+C_−^{−1}α‖². Draft's V(α) = (2γc)^{−1}∫|ξ|^{1−β}S_αdξ = (2γ)^{−1}E‖C_−^{−1}α‖² — the anticipative value, an upper bound. OU cross-check: adapted value σ²θ^{−β}/2·(γc)^{-1}-scale vs anticipative σ²θ^{−β}/(2sin(πβ/2)) — strictly larger for β<1. "Attained at u*" is wrong.
D. **Phantom citation.** FSS 2022 has NO Proposition 3.2 (their §3.2 = temporary price impact; only Theorem 2.2, Remarks 2.3–2.5, 3.1, Lemma A.1). Draft cites [Prop.~3.2]{FSS} twice (Prop 3 statement + appendix proof) for the uniform KKT-multiplier bound. Unsupported.
E. **Prop 2 hypothesis mismatch.** "strictly positive compact perturbation of the identity" — power-law G_T is itself compact (weakly singular kernel), not I+compact, and has unbounded inverse; the parenthetical "(equivalently, its symbol satisfies the whole-line WH hypothesis)" is not an equivalence. The proposition as stated does not cover the paper's main application.
F. **Prop 3 proof gap.** Even modulo issue A, the proof bounds only the Marchaud tail truncation and the KKT term; it omits the deviation of the weights (t/s)^ν from 1 (the B-conjugation error term). Rate d^{−ν} plausible but not established.
G. **KKT multipliers "finite linear system" (Thm 1, Cor 2).** For the a.s. terminal constraint X_T=0 in the adapted problem, FSS's multiplier is a function λ(u) (one per Wiener coordinate), not a finite vector. Draft's claim valid only for finitely many expectation constraints.
H. **Prop 1 uniqueness** "up to a positive multiplicative constant": with normalization conj(Ĉ_+)=Ĉ_−, the residual freedom is a unimodular constant (positive c≠1 violates adjointness/product).
I. **Prop 2 uniqueness** "up to a left unitary": for G=TT*, freedom is T→TU (right unitary).
J. Terminology: "Marchaud fractional integrals" — the integrals are Liouville/Weyl (RL on half-line); Marchaud names the derivative form. Used in Contribution, §4, Conclusion.
K. §5.4 "O(N log N) per time step" — triangular-Toeplitz apply/solve is O(N log N) for the whole grid, not per step.
L. Exponential-OU u* contains σẆ (white noise): not admissible in L² as stated; needs remark.

## Numerical results (experiments/review_factorization_check.py, run 2026-07-14)
- Check A: TT* kernel vs |t−v|^{−β}, β∈{0.3,0.5,0.7}, 3 point pairs each: ratio = 1.000000 (all). Confirms eq (volterra-kernel) as a TT* factorization *including the constant c_β*.
- Check A2: T*T kernel at (t,v)=(0.5,0.3): 2.10 (T=1), 2.46 (T=2), 2.73 (T=4) vs G=2.236 — horizon-dependent, so T*T ≠ G_T.
- Check B (n=5, random SPD signal covariance, power-law+ridge cost, sequential filtration): ‖W_direct − W_UL‖ = 2.6e−16; ‖W_direct − W_LU‖ = 8.5e−2. UL = reverse-order Cholesky (C = C_−C_+, causal right factor) matches the directly computed adapted optimum; LU (Cholesky) fails.

## Sources inspected
- `tex/factorization-optimal-trading.tex`, `tex/factorization-optimal-trading.bib` (local)
- Forde, Sánchez-Betancourt, Smith, "Optimal trade execution for Gaussian signals with power-law resilience", Quant. Finance 22(3), 585–596, 2022. Open-access PDF: https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26/files/srf55z9197 (parsed to /Users/orwell/Downloads/1469768820211950919.md). DOI: https://doi.org/10.1080/14697688.2021.1950919
  - Confirms: Thm 2.2 exists (Fredholm-equation characterization); G_1 = TT* from Porter–Stirling Ex 9.2/6.2; T = B^{−1}I_νB, pp. 590–591; used only for full inversion g = (T*)^{−1}T^{−1}h (order-insensitive); no Prop 3.2 anywhere; no uniform-in-T KKT bound stated.
- Gohberg–Krein, Theory and Applications of Volterra Operators in Hilbert Space (AMS bookstore listing): https://bookstore.ams.org/MMONO/24
- Web search results on triangular factorization conventions (S = S_−S_+ "left factorization"): https://doi.org/10.1007/978-3-7643-8539-2_17

## Unverified (not checked, flagged in review)
- Arveson 1975 Thm 4.4.2 numbering; Hytönen et al. Prop 2.6.13 numbering; Klenke Thm 14.16 numbering.
- Neuman–Voß 2022 volume/pages (previously verified per CHANGELOG 2026-07-11).
