# Review plan — factorization-optimal-trading

## Artifact
- `tex/factorization-optimal-trading.tex` (local LaTeX draft, ~46 KB, compiled PDF present)
- Title: "Optimal Trading Against a Signal: a Wiener-Hopf Approach" (M. Smerlak)
- Focus requested by user: **mathematical correctness and relevance**

## Review criteria
- Correctness of symbol computations (Fourier constants, factorizations, fractional-operator symbols)
- Correctness of the projected-inverse identity (Lemma 1) and the factorization *ordering* it requires
- Consistency of the whole-line (Wiener–Hopf) and finite-interval (Gohberg–Krein) results
- Correctness of OU closed forms (power-law and exponential kernels), sign-flip claim
- Correctness of spectral/value claims (§4.2 spectrum of ζ, §5.5 value functional)
- Interior error bound (Prop 3) — proof completeness
- Hypotheses vs. applications (Prop 2 "compact perturbation of identity" vs. compact G_T)
- Relevance/accuracy of citations: FSS 2022, Gohberg–Krein, Arveson, Abi Jaber–Neuman, Neuman–Voß
- Novelty positioning vs. prior treatments

## Verification checks
1. Analytic: FT of |t|^{-β}, c_β constant; (iξ)^{-ν}(-iξ)^{-ν} split; exponential-kernel factors; OU whitening θ^ν; exponential OU sign flip; spectral hypothesis for OU; KKT weight bound.
2. Decisive 2-period (and numerical n-period) check of which factorization order (C = C_-C_+ vs C_+C_-) makes (P_+CP_+)^{-1} = C_+^{-1}P_+C_-^{-1} true.
3. Numerical: does the explicit finite-interval kernel give TT* = G_T (with constant c_β)? Does T*T depend on T (ruling out that order)?
4. Numerical: adapted optimum via direct linear solve vs. UL-formula vs. LU-formula on a discrete Gaussian toy problem.
5. Literature: fetch/verify Forde–Sánchez-Betancourt–Smith factorization convention and Thm 2.2 / Prop 3.2; Gohberg–Krein I+K ordering convention.
6. Spectrum-of-ζ claim vs. OU counterexample; value formula V(α) vs. attained adapted value.

## Deliverables
- Evidence: `outputs/.drafts/factorization-optimal-trading-review-evidence.md`
- Final: `outputs/factorization-optimal-trading-review.md`
- Experiment script: `experiments/review_factorization_check.py`
