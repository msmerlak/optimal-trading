# Review Plan: factorization-optimal-trading-math

## Artifact
- `tex/factorization-optimal-trading.tex` (385 lines, 14 pp PDF)
- Bibliography: `tex/factorization-optimal-trading.bib`

## Scope
Mathematical correctness only. Not clarity, style, novelty, or reproducibility (previously covered).

## Objects to verify

### Section 2
- Adapted FOC derivation: $\gamma\,\E_t[(Cu^\star)(t)] = \alpha_t$ from Gâteaux derivative + adaptedness.
- Operator-form FOC: $\gamma P_+ C P_+ u^\star = \alpha$.
- Existence/uniqueness of $(P_+ CP_+)^{-1}$ under standing hypotheses.

### Section 3
- **Lemma 1** (projected-inverse identity): $(P_+ CP_+)^{-1} = C_+^{-1}P_+ C_-^{-1}$ on $L^2_{\adap}$.
  - Sub-claim: $C_+$ preserves adapted; $C_-$ preserves anticausal.
  - Sub-claim: $P_+ C_-\cdot P_+^\perp = 0$ (adjoint direction).
  - Sub-claim: $P_+ C_-^{-1} P_+ C_- = P_+$ on adapted vectors.
- **Theorem 1** (closed form): $u^\star = \gamma^{-1}C_+^{-1}P_+ C_-^{-1}\alpha$.
- **eq (proj-cma)**: $(P_+ C_-^{-1}\alpha)_s = (C_-^{-1}\bar\alpha(s,\cdot))(s)$.
- **eq (value)**: $V(\alpha) = \frac{1}{2\gamma}\|P_+ C_-^{-1}\alpha\|^2$.
- **Prop 1** (Wiener–Hopf): factorization existence under $\log\hat C/(1+\xi^2)\in L^1$.
- **Prop 2** (Gohberg–Krein): existence of $G_T = TT^*$ Volterra factorization.

### Section 4
- Whole-line power-law factors: $C_\pm = c_\beta^{1/2}I_\pm^\nu$, $\hat C_\pm(\xi) = c_\beta^{1/2}(\mp i\xi)^{-\nu}$.
- Log-integrability of pure power-law symbol.
- Finite-interval Volterra kernel eq (17): $k(s,t) = c_\beta^{1/2}(t/s)^{(1-\beta)/2}(t-s)^{\nu-1}/\Gamma(\nu)$.
- Weight-conjugated form eq (18): $T = c_\beta^{1/2}B^{-1}I_+^\nu B$.
- Consistency: $G_T = TT^* = c_\beta B^{-1}I_+^\nu B^2 I_-^\nu B^{-1}$.
- **Cor 1** (bulk formula): $u^\star_t = \gamma^{-1}c_\beta^{-1}(D_+^\nu\zeta)(t)$, $\zeta_s = (D_-^\nu\bar\alpha(s,\cdot))(s)$.
  - Total prefactor consistency $(c_\beta^{-1/2})^2 = c_\beta^{-1}$.
- **eq (ou)**: for OU signal, $(D_-^\nu\bar\alpha(t,\cdot))(t) = \theta^\nu\alpha_t$ and $\E[u^{OU}_t|\alpha_t] = \gamma^{-1}c_\beta^{-1}\theta^{1-\beta}\alpha_t$.
- Standing-hypothesis constraint for OU: $\beta > 1/2$.
- **Cor 2** (finite interval): $u^{\star,T}_t = \gamma^{-1}c_\beta^{-1}B^{-1}(D_+^\nu B P_+ B D_-^\nu B^{-1}\alpha^{eff})(t)$.
- **Prop 3** (interior error): $|u^{\star,T}_t - u^{\star,\R}_t| \le C_1\|\alpha\|_\infty d(t)^{-\nu} + C_2\|\alpha^{eff}\|_{trad}T^{-\nu}d(t)^{-\nu}$.
  - Marchaud tail-bound constant.
  - KKT eigenfunction $\phi_1(t) = [t(T-t)]^{(\beta-1)/2}$ and its bound.

### Section 5
- Exponential factors: $C_\pm^{-1} = (2\kappa)^{-1/2}(\kappa\pm\partial_t)$.
- **eq (exp-bulk)**: $u^{exp}_t = \frac{1}{2\kappa\gamma}(\kappa+\partial_t)\zeta_t$, $\zeta_s = (\kappa-\partial_r)\bar\alpha(s,r)|_{r=s^+}$.
  - Internal-consistency: prefactor vs $\zeta$-definition.
- **eq (exp-ou)**: OU-signal reduction and sign flip at $\theta = \kappa$.
- Temporary-impact crossover frequency $\xi_* = (\gamma c_\beta/\eta)^{1/(1-\beta)}$.
- Multi-asset diagonalization with eigenvalue prefactor $\Lambda_{ii}^{-1}$.

### Section 6
- Joint gain–risk–cost operator symbol $\gamma\hat C + \lambda\Sigma/\xi^2$.
- Position-in-rate-coordinates Fourier symbol $1/(-i\xi) \Rightarrow$ quadratic $1/\xi^2$.

### Appendix
- Symbol identity $\hat C(\xi)(-i\xi)^\nu = c_\beta(i\xi)^{-\nu}$ ⇒ operator $CD_+^\nu = c_\beta I_-^\nu$.
- Corollary 1 proof: Steps (a)/(b)/(c) using conditional Fubini and $I_-^\nu D_-^\nu = \mathrm{id}$.
- Corollary 2 proof: inversion of weight-conjugated factors.
- Proposition 3 proof: Marchaud tail bound derivation.

## Method
Read each derivation. Recompute from first principles where a step is non-trivial. Grep-check notation consistency. No external code or datasets to run.

## Deliverables
- Plan: this file
- Evidence: `outputs/.drafts/factorization-optimal-trading-math-review-evidence.md`
- Final review: `outputs/factorization-optimal-trading-math-review.md`
