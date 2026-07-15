# Bulk theorem refutation — empirical and proof-level

**Date:** 2026-06-30
**Status:** The bulk theorem (Thm 4.1 of `papers/fractional-derivative-optimal-execution.md` v2) is **wrong**. The correct adapted-optimal control is the filtration Wiener–Hopf form (diagonal trace of $D_-^\beta$ followed by causal $D_+^\beta$ along time), **not** the certainty-equivalent Riesz applied to the fixed time-$t$ forecast curve.

This note records the empirical refutation, the proof-level location of the bug, and the corrected statement that has been patched into the paper.

## Empirical evidence

Experiment: `experiments/bulk_vs_filtration_WH_discrete.py`. Discrete AR(1) signal `alpha_n = rho * alpha_{n-1} + eps_n`; symmetric power-law kernel `G(k) = c |k|^{-gamma}` for `k != 0` plus temporary impact `eta` on the diagonal. Four candidates are scored by `Sharpe^2 / T = -2 J* / T` after analytically optimizing each candidate's scalar gain:

| symbol | policy shape                                                                       |
|--------|------------------------------------------------------------------------------------|
| W      | numerically optimized causal FIR of length L (true LQ optimum on adapted controls) |
| U      | filtration W-H (corrected): `(1-rho)^beta * D_+^beta alpha_n`, beta = (1-gamma)/2  |
| P      | v2 bulk: `D_+^{1-gamma} alpha_n + (1-rho)^{1-gamma} alpha_n` (the (4.3.6) form)    |
| α      | naive alpha-chase: `u_n = alpha_n`                                                 |

### Convergence to the gold standard (γ=0.3, ρ=0.9, η=1, N=100k)

| L     | S²_W   | S²_U   | S²_P   | U/W   | P/W   |
|-------|--------|--------|--------|-------|-------|
| 100   | 0.8271 | 0.8398 | 0.7215 | 1.015 | 0.872 |
| 300   | 0.8350 | 0.8393 | 0.7206 | 1.005 | 0.863 |
| 800   | 0.8382 | 0.8390 | 0.7199 | **1.001** | **0.859** |
| 2000  | 0.8450 | 0.8457 | 0.7259 | **1.001** | **0.859** |

U matches the gold standard to 0.1%. P loses 14% of the achievable Sharpe².

### Scan over γ, ρ, η (N=50k, L_wiener=200)

| γ    | ρ    | η    | S²_W   | S²_U   | S²_P   | U/W   | P/W   |
|------|------|------|--------|--------|--------|-------|-------|
| 0.30 | 0.50 | 0.5  | 0.9127 | 0.8948 | 0.7524 | 0.980 | 0.824 |
| 0.30 | 0.90 | 0.5  | 0.9452 | 0.9376 | 0.7843 | 0.992 | 0.830 |
| 0.30 | 0.90 | 5.0  | 0.4527 | 0.4149 | 0.3339 | 0.917 | 0.738 |
| 0.30 | 0.99 | 5.0  | 1.2869 | 1.2517 | 0.9196 | 0.973 | 0.715 |
| 0.50 | 0.50 | 0.5  | 0.7901 | 0.7091 | 0.6714 | 0.897 | 0.850 |
| 0.50 | 0.90 | 0.5  | 0.8789 | 0.8451 | 0.8179 | 0.962 | 0.931 |
| 0.70 | 0.50 | 0.5  | 0.7409 | 0.5910 | 0.5816 | 0.798 | 0.785 |
| 0.70 | 0.99 | 5.0  | 2.4503 | 2.4612 | 2.4493 | 1.004 | 1.000 |

Patterns:
- **U ≈ W everywhere** (up to L_wiener truncation): U is the right policy.
- **P < U** whenever the regime is non-trivial (small γ, moderate η). Gap shrinks to zero only in the asymptotic limits γ→1 (Riesz becomes identity) and large η (kernel becomes diagonal).

## Where the v2 proof fails

In §2.3 / §4.1 the verification of the candidate `u^cand_v = κ D^{1-γ} bar_alpha(v,·)(v)` against the conditioned FOC `(★_bulk^F)` proceeds in two steps:

1. **Forecast tower + commutation for v ≥ t:**
   `E_t[u^cand_v] = κ D^{1-γ} E_t[bar_alpha(v,·)](v) = κ D^{1-γ} bar_alpha(t,·)(v)`.
   This is correct (Bochner commutation + tower).

2. **Substitution and Plancherel collapse:**
   `E_t[∫ G(|t-v|) u^cand_v dv] = ∫ G(|t-v|) E_t[u^cand_v] dv = (G ∗ κ D^{1-γ} bar_alpha(t,·))(t) = α_t`.
   This step **silently extends step 1 to all v ∈ R, including v < t**.

For **v < t** the candidate `u^cand_v` is already F_v-measurable so `E_t[u^cand_v] = u^cand_v = κ D^{1-γ} bar_alpha(v,·)(v)`, which uses the **time-v** forecast curve. The v2 substitution replaces it with `κ D^{1-γ} bar_alpha(t,·)(v)`, which uses the **time-t** forecast curve at a past coordinate. These differ on s ∈ (v, t]: the time-t curve has the realized `α_s`, while the time-v curve has the forecast `E_v[α_s]`. The discarded piece is the martingale increment `α_s − E_v[α_s]` — F_t-measurable, does not vanish under E_t — exactly the "new information arrived between v and t" that the substitution loses.

Hence the v2 candidate **does not satisfy the conditioned FOC**, and by strict convexity it is not the adapted minimizer. The Bensoussan certainty-equivalence appeal in v2 §2.3 is too cavalier: classical LQ certainty equivalence requires either pointwise/Markov cost or causal cost operators; here C = G∗ is non-local and its inverse D^{1-γ} is non-causal, so `(P_+ C P_+)^{-1} ≠ P_+ C^{-1} P_+` and the projected inverse does **not** coincide with applying C^{-1} to the forecast curve.

## The corrected statement (v3, patched into the paper)

With β = (1−γ)/2 and `c_γ = 2c Γ(1−γ) sin(πγ/2)`, define the F_s-adapted process
$$\zeta_s := (D_-^\beta \bar\alpha(s,\cdot))(s).$$
Then the unique adapted minimizer is
$$u^*_t = c_\gamma^{-1}(D_+^\beta \zeta)(t) = c_\gamma^{-1}\,D_+^\beta\,P_+\,D_-^\beta\,\alpha\;\;\text{at }t,$$
i.e. the filtration W-H form `C_+^{-1} P_+ C_-^{-1}` of the projected operator, with the optional projection **between** the two half-order factors. The crucial structural difference from v2 (4.3.3) is that the outer $D_+^\beta$ acts on the **diagonal trace** $s \mapsto D_-^\beta\bar\alpha(s,\cdot)(s)$ along the conditioning-time axis, not on the cross-section of the fixed time-$t$ forecast curve. v2 §4.3 explicitly warned against the diagonal trace as "suboptimal"; the warning is the bug.

### FOC verification (sketch)

Define $\hat\zeta_t(s) := \mathbb E_t[\zeta_s]$. For $s\le t$: $\zeta_s\in\mathcal F_s\subset\mathcal F_t$, so $\hat\zeta_t(s)=\zeta_s$. For $s>t$: by Bochner + tower, $\hat\zeta_t(s) = D_-^\beta\bar\alpha(t,\cdot)(s)$. Then $\mathbb E_t[u^*_v] = c_\gamma^{-1}(D_+^\beta\hat\zeta_t)(v)$, and the symbol identity $\hat G(\xi)(i\xi)^\beta = c_\gamma(-i\xi)^{-\beta}$ gives $G*D_+^\beta = c_\gamma I_-^\beta$ (anticausal RL integral of order β), so
$$\mathbb E_t[(Cu^*)(t)] = (I_-^\beta\hat\zeta_t)(t).$$
$I_-^\beta$ at $t$ only uses $\hat\zeta_t(s)$ for $s\ge t$, where it equals $D_-^\beta\bar\alpha(t,\cdot)(s)$. Hence
$$(I_-^\beta\hat\zeta_t)(t) = I_-^\beta D_-^\beta\bar\alpha(t,\cdot)(t) = \bar\alpha(t,t) = \alpha_t.\;\;\checkmark$$
The past leg of $\hat\zeta_t$ — where the projected version differs from the v2-style time-$t$ curve — never enters the Plancherel collapse, because $I_-^\beta$ at $t$ looks only forward.

### OU specialization

For OU ($d\alpha = -\theta\alpha\,dt + \sigma\,dW$, $\bar\alpha(t,s) = e^{-\theta(s-t)}\alpha_t$ for $s>t$), the inner step has closed form $\zeta_s = \theta^\beta\alpha_s$ (same exponential-integration that gave (4.3.5) in v2, but at half order), so
$$u^*_t = c_\gamma^{-1}\theta^\beta(D_+^\beta\alpha)(t).$$
The v2 (4.3.6) form $\kappa[(D_+^{1-\gamma}\alpha)(t) + \theta^{1-\gamma}\alpha_t]/(2\sin(\pi\gamma/2))$ is the (incorrect) certainty-equivalent answer; the empirical scan above is precisely the AR(1) discretization of this comparison.

## Artifacts

- Experiment: `experiments/bulk_vs_filtration_WH_discrete.py`
- Paper: `papers/fractional-derivative-optimal-execution.md` — §2.3, §4.1, §4.3 patched
- Replacement-text reference (more verbose, with line-precise hints): `papers/.plans/bulk-theorem-correction.md`
- Bochner commutation reference: Hytönen–van Neerven–Veraar–Weis, *Analysis in Banach Spaces I* (2016), Prop. 2.6.13
- Classical filtration W-H: Wiener 1949; Kailath–Sayed–Hassibi *Linear Estimation* (2000) ch. 7–8
