# Correctness Review — *Optimal Trading Filters: a Wiener–Hopf Approach* (v3)

**File reviewed:** `v3/optimal-trading-filters-v3.tex` (503 lines).
**Companion code exercised:** `experiments/rate_response_2ema.py`, `experiments/risk_response_check.py`, `experiments/review_factorization_check.py`, `experiments/closed_form_vs_operator.py`, `experiments/nv_vs_stationary.py`, `experiments/make_figures.py`, plus independent numerical/analytic checks written for this review.
**Scope:** mathematical correctness of the recently added/changed results — the trading-filter theorem and OU formulas, the value-of-information scalings and $\Phi$-asymptotics, the causality gap $\sin(\pi\beta/2)$, the pure power-law fractional-integral policy and its stationarity condition, and impact surfing $R(\theta)$. I did **not** edit any files.

---

## Part 1: Structured Review

## Summary

The paper solves the adapted (causal) linear–quadratic trading problem of Eq. (1) — linear gain against a return signal, net of temporary impact, transient/propagator impact, and mean–variance inventory risk — by Wiener–Hopf (Szegő) factorization of the friction operator $N=N_-N_+$ (position-referred), or $Q=Q_-Q_+$ (rate-referred). The central identity, Lemma 1, gives the adapted projected inverse $(P_+AP_+)^{-1}=A_+^{-1}P_+A_-^{-1}$; Theorem 2/3 turn this into a closed-form transfer function for stationary Gaussian signals, from which the OU value $v=\sigma^2\theta/4\Phi(\theta)^2$, the value-of-information scalings, the causality gap, the fractional-integral policy, and the impact-surfing rate response all follow.

The core derivations are, with the exceptions below, **correct and internally consistent**, and are supported by the companion numerics. I verified analytically: the $\Phi(\theta)$ asymptotics ($\sqrt\lambda$; $\sqrt{2\kappa\gamma+\lambda}$; $\sqrt\eta\,\theta$; $\sqrt{\gamma c_\beta}\,\theta^{(1+\beta)/2}$), the value scalings ($\theta^2$, $\theta^{1-\beta}$, saturation at $\mathrm{Var}(\alpha)/2\eta$), the fractional order $\nu=(1-\beta)/2$ and the position exponent $(1+\beta)/2$, the stationarity condition, the aim-portfolio and two-EMA recoveries, and the surfing consistency limits. Two issues need attention: a **directional (sign) error in the statement of Proposition 1** (surfing threshold), and an **ill-posed benchmark definition** ($v_{\rm ant}$, Eq. 20) in exactly the scale-free case where the headline $\sin(\pi\beta/2)$ is claimed.

## Strengths

- **[S1]** Lemma 1's factorization order is empirically pinned. `review_factorization_check.py` (Check B) shows the *upper–lower* order $A_+^{-1}P_+A_-^{-1}$ reproduces the direct adapted optimum to `2.6e-16`, while the reversed order is off by `0.085`. This confirms the non-commutativity argument is not cosmetic.
- **[S2]** The OU value and $\Phi$-asymptotics are exactly reproducible. I independently confirmed $\|\hat\psi\|^2=\pi\sigma^2\theta$, $[h]_+=\hat\psi/\Phi$, hence $v=\sigma^2\theta/4\Phi^2$; and all four $\Phi(\theta)$ limits by direct evaluation of Eq. (30) (e.g. pure risk gives $\Phi=\sqrt\lambda$ from the Poisson integral, power law gives $\sqrt{\gamma c_\beta}\,\theta^{(1+\beta)/2}$ using $\int\log|t|/(\theta^2+t^2)\,dt=(\pi/\theta)\log\theta$).
- **[S3]** The terminal-anchored power-law Volterra factor Eq. (47) is verified to machine ratio `1.000000` by kernel integration $C_-C_+=G_T$ across $\beta\in\{0.3,0.5,0.7\}$ and several $(t,v)$ (`review_factorization_check.py`, Check C).
- **[S4]** The surfing consistency checks in Appendix C are exact: I reproduced $R\to(\kappa^2-\theta^2)/2\kappa\gamma$ as $\lambda\to0$ and $R\to-\theta^2/\lambda$ as $\gamma\to0$ by hand from Eq. (42); the two-EMA recovery rates $b_1,b_2$ match `nv_vs_stationary.py` (`match: True`).
- **[S5]** The value-of-information story is quantitatively self-consistent: `make_figures.py` uses $v=\theta^2 V/(2\Phi^2)$ with $V=\mathrm{Var}(\alpha)$, which equals the body's $\sigma^2\theta/4\Phi^2$ under $\mathrm{Var}(\alpha)=\sigma^2/2\theta$, and reproduces the $\theta^2$/$\theta^{1-\beta}$/saturation trichotomy.

## Weaknesses

- **[W1] BLOCKER (directional/sign error).** Proposition 1 (`prop:response`, Eq. 41 region, lines ~301–307) states the exponential-kernel rate "**reverses below the threshold** $\theta^\ast=\kappa-2m$." This is **backwards**. The proposition's own criterion "the rate reverses exactly when $2c_1\Phi(\theta)>1$" gives, with $\Phi=\sqrt A(m+\theta)/(\kappa+\theta)$ and $c_1=1/\sqrt A$, $2c_1\Phi=2(m+\theta)/(\kappa+\theta)>1\iff\theta>\kappa-2m$. Reversal therefore occurs **above** $\theta^\ast$, not below. This is confirmed by (i) the main text (§4.2: "$\theta>\kappa$ at $\lambda=0$ … runs against the signal"), (ii) the Figure 3 caption ("follows the signal ($R>0$) below the boundary … trades against it ($R<0$) above"), and (iii) the code: `risk_response_check.py` prints `lambda=0.5: theta* = +0.6667`, then `R(theta=0.3)=+0.0167` (below, follows) and `R(theta=1.5)=-0.3052` (above, reverses); `rate_response_2ema.py`'s docstring says "REVERSES for theta>theta*." The formal statement is thus contradicted by its own hypothesis, the body, the figure, and the numerics. One-clause fix ("below" → "above"), but it is a mathematically incorrect Proposition as written.

- **[W2] MAJOR (ill-posed benchmark for a headline result).** The causality gap is *defined* as $v/v_{\rm ant}$ with $v_{\rm ant}=\frac1{4\pi}\int S_\mu/\hat n\,d\omega$ (Eq. 20). For the pure power-law kernel — precisely the case where the headline law $v/v_{\rm ant}=\sin(\pi\beta/2)$ (Eq. 21) is claimed — this integral **diverges**: with $S_\mu(0)\ne0$ (OU) and $\hat n=\gamma c_\beta|\omega|^{1+\beta}$, the integrand behaves as $|\omega|^{-(1+\beta)}$ at the origin. I confirmed numerically that the position-form $v_{\rm ant}$ blows up as the low-frequency cutoff shrinks (`3.2e4 → 1.0e6 → 3.2e7 → 1.0e9` for cutoff `1e-2 … 1e-5`, i.e. $\sim\epsilon^{-\beta}$). The finite, correct $\sin(\pi\beta/2)$ requires the **rate-referred** benchmark $v_{\rm ant}=\frac1{4\pi}\int S_\alpha/\hat q\,d\omega$, which I verified analytically equals $\sigma^2\theta^{-\beta}/(4\gamma c_\beta\sin(\pi\beta/2))$, giving exactly $v/v_{\rm ant}=\sin(\pi\beta/2)$. Appendix B does compute it this way ("via (vant)" but with $\hat q_-,\hat\varphi$), yet the body never states that $v_{\rm ant}$ must be re-referred to the rate for $\lambda=0$, and Eq. (20) as printed cannot support Eq. (21). Compounding this: the position-form ($\int S_\mu/\hat n$) and rate-form ($\int S_\alpha/\hat q$) anticipative values are **not the same number** off the adapted optimum (they differ by the integration-by-parts martingale term $\E\int x\,dM$, which vanishes only for adapted $x$), so "$v_{\rm ant}$" needs a single, stated definition. No script cross-checks Eq. (21) from raw $v,v_{\rm ant}$ integrals — the figure plots the closed form directly — so this gap is not caught by the numerics.

- **[W3] MINOR (verification claim slightly outruns the discrete evidence).** The abstract/§2.3 assert "all closed forms are checked against discretized adapted optima." For the surfing/rate response the discrete match is only *qualitative* at high $\theta$: `rate_response_2ema.py` shows, at $\eta=0.05$, `theta=6.0: R_analytic=+3.73 vs R_discrete=+1.70` (gap `2.0`), and even the $\eta=0$ reference degrades (`theta=6: -7.01 vs -5.59`). The `dt`-refinement in `risk_response_check.py` shows convergence toward the analytic value as `dt→0`, so the analytic formula is the ground truth and the gap is discretization, not a formula error — but the sweeping "all closed forms checked" should be qualified (sign and saturation are robust; magnitudes at high $\theta$ are grid-limited).

## Questions for Authors

- **[Q1]** In Proposition 1, please confirm the intended direction and correct "below" → "above" (see W1). Is there any regime you intended "below" to describe (e.g. a differently-signed convention for $R$)? None is visible.
- **[Q2]** Which single definition of $v_{\rm ant}$ do you intend (W2)? If it is the rate-referred $\frac1{4\pi}\int S_\alpha/\hat q$ for $\lambda=0$, please state it at Eq. (20)/(21) and note that Eq. (20) as written is the $\lambda>0$ position-referred form (finite there) and diverges in the scale-free limit.
- **[Q3]** Can you add a direct numerical check of $\sin(\pi\beta/2)$ from computed $v$ and (rate-referred) $v_{\rm ant}$? Currently the figure plots the closed form only.

## Verdict

The mathematical core — Lemma 1, Theorems 2–3, the OU value, the $\Phi$-asymptotics, the fractional-integral policy with exponent $(1+\beta)/2$ and $\nu=(1-\beta)/2$, the stationarity condition, and the rational-friction recoveries — is **sound and reproducible**, confirmed both analytically and against the code. Two items require revision before the results can be stated as written: **W1 is a genuine correctness error** in a formal Proposition (trivial to fix but must be fixed), and **W2 is a definitional gap** that makes the headline causality-gap benchmark ill-posed in the exact case it is applied to (the $\sin(\pi\beta/2)$ result is *correct* under the rate-referred benchmark, but the paper's stated $v_{\rm ant}$ does not deliver it). Revision risk is **low-to-moderate**: both are localized and do not threaten the main construction. Confidence in this assessment: **high** for W1 (multiply corroborated), **high** for W2 (analytic + numerical), moderate for the completeness of my scan of the finite-horizon appendix (Prop. 2/Appendix D I checked only at the level of scalings, not constants). Confidence score: **4/5**.

## Revision Plan

1. **W1 (BLOCKER):** In Proposition 1, change "the rate reverses below the threshold $\theta^\ast=\kappa-2m$" to "**above** the threshold." Verify the surrounding sentence ("reverses exactly when $2c_1\Phi>1$") and Figure 3 caption are then mutually consistent (they already state the correct direction).
2. **W2 (MAJOR):** At Eq. (20), state that $v_{\rm ant}$ is position-referred and finite for $\lambda>0$; add the rate-referred form $v_{\rm ant}=\frac1{4\pi}\int S_\alpha/\hat q\,d\omega$ used for the scale-free kernel, and note Eq. (20) diverges there. Make explicit (one line) that the two forms are the *same* anticipative value only on the adapted optimum / when $\lambda>0$; the $\lambda=0$ gap uses the rate form. Optionally cite the Appendix B residue computation at Eq. (21).
3. **W3 (MINOR):** Qualify "all closed forms are checked against discretized adapted optima" to reflect that high-$\theta$ rate responses are confirmed in sign/saturation and converge under `dt`-refinement, rather than matching tightly on a fixed grid. Consider adding the `dt`-refinement table to the verification notes.

---

## Part 2: Inline Annotations

> "and the rate reverses below the threshold $\theta^\ast = \kappa-2m = \kappa\Bigl[1-2\sqrt{\lambda/(2\kappa\gamma+\lambda)}\Bigr]$."
**[W1] BLOCKER:** Direction is inverted. The same proposition's criterion $2c_1\Phi>1$ evaluates to $2(m+\theta)/(\kappa+\theta)>1\iff\theta>\kappa-2m$, so reversal occurs **above** $\theta^\ast$. Confirmed by §4.2 ("$\theta>\kappa$ … runs against the signal"), the Figure 3 caption ("$R>0$ below … $R<0$ above"), and `risk_response_check.py` (`theta*=+0.6667`; `R(0.3)=+0.017`, `R(1.5)=-0.305`). Replace "below" with "above."

> "the rate reverses exactly when $2c_1\Phi(\theta)>1$."
**[W1] (supporting):** This clause is *correct* and is exactly what contradicts the "below" claim immediately following it — the two are inconsistent as printed.

> "The \emph{causality gap} is the ratio $v/v_{\rm ant}\le1$ … $v_{\rm ant} = \frac{1}{4\pi}\int \frac{S_\mu}{\hat n}\,d\omega$"
**[W2] MAJOR:** This position-referred integral diverges for the pure power-law kernel ($\int|\omega|^{-(1+\beta)}$ at the origin), the very case where Eq. (21) is stated. Numerically it grows as $\epsilon^{-\beta}$ under low-frequency cutoff $\epsilon$ (`3.2e4→1.0e9` for `1e-2→1e-5`). Define the rate-referred $v_{\rm ant}=\frac1{4\pi}\int S_\alpha/\hat q$ for $\lambda=0$, which yields the finite $\sin(\pi\beta/2)$.

> "Under pure power-law impact the causality gap is scale-free … $\frac{v}{v_{\rm ant}} = \sin\!\frac{\pi\beta}{2}.$"
**[W2] (result is correct under the right benchmark):** I confirmed analytically $v=\sigma^2\theta^{-\beta}/4\gamma c_\beta$ and (rate-form) $v_{\rm ant}=\sigma^2\theta^{-\beta}/(4\gamma c_\beta\sin(\pi\beta/2))$, giving exactly $\sin(\pi\beta/2)$; the empirical range $\beta\in(0.2,0.6)\Rightarrow(0.309,0.809)$ ("a third and four-fifths") also checks out. The law is right; only the benchmark *definition* in the body (Eq. 20) is inconsistent with it.

> "the sine arising from the argument of $(-i\omega)^{\beta-1}$ on the two half-lines." (Appendix B)
**[Q2]:** This is where the *rate-referred* $v_{\rm ant}$ is implicitly used ($\hat q_-,\hat\varphi$). Please surface this switch in the body so Eq. (20) and Eq. (21) are consistent.

> "the position is stationary if and only if $\int|\omega|^{-(1+\beta)}S_\mu(\omega)\,d\omega<\infty$, that is, if $S_\mu(\omega)$ vanishes at $\omega=0$ faster than $|\omega|^\beta$."
**[S-verify] Correct.** If $S_\mu\sim|\omega|^p$ near 0 the integrand is $|\omega|^{p-1-\beta}$, integrable at 0 iff $p>\beta$. Exponent and low-frequency argument confirmed. (And $S_\mu(0)\ne0$ for OU fails it, as stated.)

> "$x^\star \propto I^{(1+\beta)/2}_+\mu$"
**[S-verify] Correct.** $\hat n_+=\sqrt{\gamma c_\beta}(-i\omega)^{(1+\beta)/2}$, so $\hat x^\star=\hat\mu/(\Phi\hat n_+)\propto(-i\omega)^{-(1+\beta)/2}\hat\mu$, whose symbol is that of $I^{(1+\beta)/2}_+$. Exponent $(1+\beta)/2$ verified; likewise $Q_\pm=(\gamma c_\beta)^{1/2}I^\nu_\pm$, $\nu=(1-\beta)/2$.

> "with value $v=\sigma^2\theta/4\Phi(\theta)^2$"
**[S-verify] Correct.** From $v=\frac1{4\pi}\|[h]_+\|^2=\frac1{4\pi}\|\hat\psi/\Phi\|^2$ and $\|\hat\psi\|^2=\pi\sigma^2\theta$. Consistent with `make_figures.py` ($v=\theta^2V/2\Phi^2$, $V=\mathrm{Var}(\alpha)=\sigma^2/2\theta$).

> "$\Phi\to\sqrt\lambda$ and $\Phi\to\sqrt{2\kappa\gamma+\lambda}$ … $\Phi\propto\theta^{(1+\beta)/2}$ … $\Phi\propto\sqrt\eta\,\theta$"
**[S-verify] All four correct** by direct evaluation of Eq. (30)/the outer factors; and they map to $v\propto\theta^2$, $v\propto\theta^{1-\beta}$, and saturation $v\to\mathrm{Var}(\alpha)/2\eta$ for $\theta\gtrsim\sqrt{\lambda/\eta}$ as claimed.

> "$c_1 = \lim_{|\omega|\to\infty}\frac{1}{\hat n_+(\omega)} = \frac{1}{\sqrt{2\gamma\kappa+\lambda}}$ (exponential), $c_1=0$ (power-law, or any $\eta>0$)"
**[S-verify] Correct.** $\hat n_+\to\sqrt A$ for exponential/$\eta=0$; $\hat n_+$ grows without bound when $\eta>0$ or for the power law. Matches `rate_response_2ema.py`.

> "All closed forms are checked against discretized adapted optima." (Abstract)
**[W3] MINOR:** Qualify. The filter/factorization/value checks are tight (`≤1e-15` to ~1%), but the high-$\theta$ rate responses match only in sign/saturation on a fixed grid (`R_analytic=+3.73 vs +1.70` at $\theta=6,\eta=0.05$), converging under `dt`-refinement.

---

## Items by severity

**BLOCKERS**
- **W1** — Prop. 1 (`prop:response`), the $\theta^\ast=\kappa-2m$ sentence: "reverses below" should be "reverses above." Contradicted by its own criterion, §4.2, Fig. 3 caption, and `risk_response_check.py`/`rate_response_2ema.py`.

**FIXES-WORTH-DOING-NOW**
- **W2** — Eq. (20) $v_{\rm ant}=\frac1{4\pi}\int S_\mu/\hat n$ diverges for the pure power law where Eq. (21) $\sin(\pi\beta/2)$ is asserted; state and use the rate-referred $\frac1{4\pi}\int S_\alpha/\hat q$. Result is correct under that benchmark (verified analytically); definition in the body is not. No script checks Eq. (21) from raw integrals.

**OPTIONAL**
- **W3** — Soften "all closed forms are checked against discretized adapted optima"; add the `dt`-refinement evidence for the surfing response; the fixed-grid discrete $R$ is only a sign/saturation check at high $\theta$.
- Add a direct numerical verification of $\sin(\pi\beta/2)$ (Q3).

**IGNORE / DEFER**
- The task's named companion `experiments/test_all_results.py` does not exist under `experiments/` (only `v2/experiments/test_all_results.py`); this is a stale reference, not a paper defect. All other named scripts run clean.
- Finite-horizon Appendix D constants (Prop. 2) checked only at the level of scalings ($d(t)^{-\nu}$, $e^{-b_1 d(t)}$), which are consistent with `nv_vs_stationary.py`'s interior relaxation; sharp constants are out of scope and the paper already flags them as not yet sharp.

## Sources

Local artifacts only (no external sources inspected):
- `v3/optimal-trading-filters-v3.tex`
- `experiments/rate_response_2ema.py`, `experiments/risk_response_check.py`, `experiments/review_factorization_check.py`, `experiments/closed_form_vs_operator.py`, `experiments/nv_vs_stationary.py`, `experiments/make_figures.py`, `experiments/filtering_fracdiff_powerlaw.py`
