# When Do the Optimal Trade and the Signal Share Signs?

**Date:** 2026-07-11
**Companion to:** `papers/markowitz-of-cost-pnas.md`
**Question:** Under what conditions is $\text{sign}(u^\star_t) = \text{sign}(\alpha_t)$ for the closed-form optimal execution rate?

---

## 1. Why the question is not trivial

The gain–cost problem
$$V(\alpha) = \sup_{u\in L^2_{\rm adap}}\ \mathbb{E}\!\int u_t\alpha_t\,dt - \frac{\gamma}{2}\mathbb{E}\!\iint |t-v|^{-\beta}u_t u_v\,dt\,dv$$
has a solution $u^\star = \gamma^{-1}(P_+CP_+)^{-1}\alpha$ that delivers strictly positive expected gain whenever $\alpha$ is nontrivial. Positive *expected* gain does not imply *pointwise* sign match. Three distinct claims must be separated:

- **(S1) integrated:** $\int u^\star_t\alpha_t\,dt \geq 0$ in expectation. **Always true**; equals $2V(\alpha)/\gamma\cdot\gamma = 2V(\alpha)$.
- **(S2) conditional expectation:** $\mathbb{E}[u^\star_t\alpha_t \mid \alpha_t] \geq 0$ pointwise in $\alpha_t$. Holds under stationarity plus a monotone-forecast property.
- **(S3) almost sure pointwise:** $u^\star_t\alpha_t \geq 0$ a.s. for all $t$. **Not generic**, even for benign signals.

The interesting question is when (S3) holds, or how badly it fails. The answer is analogous to a familiar feature of Markowitz portfolios.

---

## 2. Markowitz precedent

For $w^\star = \lambda^{-1}\Sigma^{-1}\mu$, the components of $w^\star$ can carry opposite signs from the corresponding components of $\mu$. Standard example: two positively correlated assets with $\mu_1 > \mu_2 > 0$ and $\rho$ close to 1 gives $w^\star_2 < 0$ — a short leg funds a levered long on the higher-return asset. Sign preservation $\mu\geq 0 \Rightarrow w^\star\geq 0$ requires structural conditions on $\Sigma$: sufficient is that $\Sigma$ is a *Stieltjes matrix* (positive diagonal, non-positive off-diagonal, positive definite), or that $\Sigma^{-1}$ has non-negative entries (inverse M-matrix). Neither is generic for real return covariances.

The temporal analog is not obvious because our cost kernel $|t-s|^{-\beta}$ has non-negative entries. But sign preservation of $\Sigma^{-1}\mu$ depends on the entries of $\Sigma^{-1}$, not $\Sigma$. And $\Sigma^{-1}$ non-negative is a strong condition that neither the temporal cost operator nor its adapted restriction satisfies.

---

## 3. Unconstrained (non-adapted) case

The naive Markowitz analog on the whole line is $u = \gamma^{-1}C^{-1}\alpha$. In Fourier, $\widehat{C^{-1}}(\xi) = c_\beta^{-1}|\xi|^{1-\beta}$, so $C^{-1}$ is (up to constant) the fractional Laplacian $(-\Delta)^{(1-\beta)/2}$. For $\beta\in(0,1)$ this is a purely non-local operator whose real-space kernel

$$k(t) = c_\beta'\cdot\text{p.v.}\,|t|^{-(2-\beta)}$$

has a **positive singular core and a negative bulk when integrated against smooth positive test functions**. Concretely, for a Gaussian bump $\alpha_t = e^{-t^2}$, $((-\Delta)^{(1-\beta)/2}\alpha)(t)$ is positive at $t=0$ but negative for $|t|$ larger than a $\beta$-dependent crossover. Sign preservation fails on any signal with sufficient decay.

**Takeaway.** Even ignoring adaptedness, $C^{-1}$ is not sign-preserving. This is the temporal counterpart of $\Sigma^{-1}$ being non-M in Markowitz.

---

## 4. Adapted power-law case

Theorem 1 of the paper gives

$$u^\star_t = \gamma^{-1}\kappa_{1-\beta}(D_+^\nu\zeta)(t),\qquad \zeta_s = (D_-^\nu\bar\alpha(s,\cdot))(s),\qquad \nu = \tfrac{1-\beta}{2}.$$

Sign preservation for the composite operator requires two steps:

**Step A — forecast collapse.** $\zeta_s$ is the anticausal Marchaud fractional derivative of the forecast curve $v\mapsto\bar\alpha(s,v)$ evaluated at its left endpoint:

$$\zeta_s = \frac{\nu}{\Gamma(1-\nu)}\int_0^\infty\frac{\bar\alpha(s,s)-\bar\alpha(s,s+r)}{r^{1+\nu}}\,dr. \tag{$\star$}$$

$\zeta_s$ has the same sign as $\alpha_s$ *if the forecast curve does not overshoot its current value in the future*: i.e., if $\alpha_s > 0$ and $r\mapsto\bar\alpha(s,s+r)/\alpha_s$ is non-increasing on $r\geq 0$ (with the ratio in $[0,1]$), then every increment in $(\star)$ is non-negative.

A clean sufficient condition on the signal dynamics: **the forecast decay is completely monotone**, i.e., $r\mapsto\mathbb{E}_s[\alpha_{s+r}]/\alpha_s$ is completely monotone in $r$. Mean-reverting signals with exponential or mixture-of-exponentials decay satisfy this; OU is the reference case.

**Step B — causal fractional derivative.** Given $\zeta$, $u^\star_t\propto(D_+^\nu\zeta)(t) = \tfrac{\nu}{\Gamma(1-\nu)}\int_0^\infty\tfrac{\zeta_t-\zeta_{t-r}}{r^{1+\nu}}dr$. This has $u^\star_t\geq 0$ whenever $\zeta$ is non-decreasing on $(-\infty,t]$ (each increment non-negative).

**The trap.** For a random stationary signal, $\zeta$ inherits the fluctuations of $\alpha$ and is not monotone. Even if $\zeta_t>0$, the past values $\zeta_{t-r}$ can be larger than $\zeta_t$, making $D_+^\nu\zeta$ negative. This is where sign-match fails almost surely.

---

## 5. The OU worked example

Let $\alpha$ be a stationary Ornstein–Uhlenbeck process: $d\alpha_t = -\theta\alpha_t\,dt + \sigma\,dW_t$, stationary variance $\sigma^2/(2\theta)$. The forecast curve is $\bar\alpha(s,s+r) = \alpha_s e^{-\theta r}$, exponentially decaying and completely monotone.

Substituting into $(\star)$ and using $\int_0^\infty(1-e^{-\theta r})r^{-1-\nu}dr = \theta^\nu\Gamma(1-\nu)/\nu$:

$$\boxed{\ \zeta_s = \theta^\nu\alpha_s.\ }$$

**Step A succeeds exactly:** $\zeta$ is proportional to $\alpha$ with positive coefficient $\theta^\nu$.

Step B: $u^\star_t = \gamma^{-1}\kappa_{1-\beta}\theta^\nu(D_+^\nu\alpha)(t)$. Now $D_+^\nu\alpha$ is a stationary Gaussian process (linear functional of a Gaussian process). By stationarity of OU and time-reversibility, the conditional mean is

$$\mathbb{E}[(D_+^\nu\alpha)(t)\mid\alpha_t] = \theta^\nu\alpha_t,$$

so $\mathbb{E}[u^\star_t\mid\alpha_t] = \gamma^{-1}\kappa_{1-\beta}\theta^{1-\beta}\alpha_t$. **(S2) holds exactly** with positive coefficient $\propto\theta^{1-\beta}$; this matches the OU value scaling in §4 of the paper.

**(S3) does not hold.** The joint Gaussian correlation between $u^\star_t$ and $\alpha_t$ can be computed by spectral integration. With $S_\alpha(\xi) = \sigma^2/(\theta^2+\xi^2)$ and the Fourier multiplier of $D_+^\nu$ being $(-i\xi)^\nu$:

- $\mathrm{Var}(\alpha_t) = \sigma^2/(2\theta)$.
- $\mathrm{Cov}(u^\star_t,\alpha_t) = \gamma^{-1}\kappa_{1-\beta}\sigma^2\theta^{2\nu-1}/2$.
- $\mathrm{Var}(u^\star_t) = \gamma^{-2}\kappa_{1-\beta}^2\sigma^2\theta^{4\nu-1}/(2\cos\pi\nu)$, using $\int_{-\infty}^\infty |u|^{2\nu}/(1+u^2)\,du = \pi/\cos\pi\nu$ for $\nu\in(-\tfrac12,\tfrac12)$.

Combining,

$$\boxed{\ \rho(u^\star_t,\alpha_t) = \sqrt{\cos\pi\nu} = \sqrt{\cos\bigl(\tfrac{\pi(1-\beta)}{2}\bigr)} = \sqrt{\sin(\tfrac{\pi\beta}{2})}.\ }$$

For a bivariate mean-zero Gaussian pair with correlation $\rho$, the probability of a sign match is $\tfrac{1}{2}+\tfrac{1}{\pi}\arcsin\rho$. Numerical values across the empirical range $\beta\in[0.2,0.6]$:

| $\beta$ | $\nu$ | $\rho$ | $\Pr(\text{sign match})$ |
|---|---|---|---|
| 0.20 | 0.400 | 0.556 | 0.688 |
| 0.30 | 0.350 | 0.674 | 0.735 |
| 0.40 | 0.300 | 0.767 | 0.778 |
| 0.50 | 0.250 | 0.841 | 0.818 |
| 0.60 | 0.200 | 0.899 | 0.856 |
| 0.80 | 0.100 | 0.975 | 0.929 |
| 0.90 | 0.050 | 0.994 | 0.965 |

**Reading.** Even in the cleanest possible signal case (OU, completely monotone forecast, all "Step A" obstructions absent), the optimal trade rate and the signal disagree in sign 15–30% of the time across the empirical impact range. Sign disagreement is a structural feature of transient-impact optimal execution, not a pathology.

**Two limits are informative.**

- $\beta\to 1^-$ (temporary impact, $\nu\to 0$): $\rho\to 1$, sign-match probability $\to 1$. The optimizer collapses to $u^\star\propto\alpha$ (Markowitz limit; no history-weighting).
- $\beta\to 0^+$ (extreme long memory, $\nu\to 1/2$): $\rho\to 0$, sign-match probability $\to 1/2$. The optimizer becomes asymptotically uncorrelated with the current signal — trades on integrated forecast history rather than the instantaneous value.

---

## 6. Sufficient conditions for guaranteed (S3) sign preservation

(S3) requires a restrictive setup. The following each imply almost-sure pointwise sign match:

**(C1) Deterministic monotone signal.** If $\alpha$ is deterministic, non-negative, and non-decreasing on $\mathbb{R}$ with completely monotone forecast in the trivial sense (past values known), and if additionally the projection $P_+C_-^{-1}\alpha$ produces a non-decreasing $\zeta$, then $u^\star\geq 0$. The double requirement — non-negativity of $\zeta$ from Step A and monotonicity of $\zeta$ for Step B — makes this class narrow.

**(C2) Constant-in-time signal on a half-line.** If $\alpha_t = c\cdot\mathbb{1}_{[0,\infty)}(t)$ with $c>0$, then $\zeta$ is proportional to a half-power of $t$ on $t\geq 0$, non-negative and non-decreasing; $u^\star\geq 0$ for $t\geq 0$. This is the finite-horizon Almgren–Chriss / GSS boundary-layer regime with an additional sign symmetry.

**(C3) Small-$\nu$ limit.** For $\nu\to 0$ (i.e., $\beta\to 1$), both Marchaud derivatives approach the identity, $u^\star\to\gamma^{-1}\alpha$, and (S3) holds trivially. For any fixed $\nu>0$, expand: $D_\pm^\nu = I + \nu\log(\pm iD) + O(\nu^2)$. To leading order in $\nu$, sign is preserved; violations are $O(\nu)$ and driven by the logarithmic correction. Cross-reference: this matches the small-$\nu$ regime where the fractional-Sobolev value scales linearly with $\nu$ (paper §3).

**(C4) Signals with a signed spectral factorization.** If $\alpha$ admits a *positive-coefficient* representation $\alpha_t = \int_0^\infty g(r)\,dM_{t-r}$ with a non-negative kernel $g$ against a positive random measure $dM$, then the causal application of $C_+^{-1}P_+C_-^{-1}$ commutes with the positivity of $g$ under further conditions on $g$'s complete monotonicity. This is a specialization; the general form requires signed measures.

None of (C1)–(C4) is generic. In practice, (S3) should not be assumed and must be checked empirically per signal.

---

## 7. Necessary condition candidates

**Complete monotonicity of the forecast decay is necessary for $\text{sign}(\zeta_s) = \text{sign}(\alpha_s)$ under any adapted signal.** If the forecast curve overshoots current value in the future (e.g., forecasted mean-reversion to a level above $\alpha_s$ when $\alpha_s>0$), the integrand in $(\star)$ has mixed sign and $\zeta_s$ can flip. Signals with mean-reverting-to-nonzero targets, or signals whose forecast anticipates a regime change, fail this necessary condition at Step A alone.

**Non-anticipation of over-mean-reversion is necessary at Step B.** If $\zeta$ recently spiked and has since decayed, the past excess $\zeta_{t-r} > \zeta_t$ makes $D_+^\nu\zeta$ negative even when $\zeta_t > 0$. In particular, right after any local maximum of $\zeta$, the optimizer trades against the current sign of $\zeta$. The rationale is straightforward: the trader unwinds part of the position they built during the spike, because holding it costs more than the current forecast justifies.

---

## 8. Interpretation and practical implications

- **Sign flips are cost-optimal, not diagnostic errors.** The optimizer reduces cost by trading *ahead of* forecast changes (Step B, causal Marchaud derivative). "Ahead of" a signal decline means selling before the signal has fully turned; if the decline turns out to be a transient blip, this looks like a wrong-way trade in hindsight.

- **Positive expected gain does not require positive pointwise gain.** The tradeability functional $\|P_+C_-^{-1}\alpha\|^2$ is unconditionally positive, but the pointwise decomposition into signal-following and signal-anticipating components leaves the trader with negative-gain moments in exchange for lower cost overall.

- **Operational check.** For a candidate signal, run Monte Carlo on $\Pr(\text{sign}(u^\star_t)\neq\text{sign}(\alpha_t))$ under the calibrated $\beta$. The OU table above gives an approximate lower bound on this quantity for stationary Gaussian mean-reverting signals; empirical signals often show worse rates.

- **Comparison with Markowitz.** In Markowitz, one *reports* $w^\star$ and often observes short legs against high-return assets. Interpretation is standard: correlations force hedging. The temporal analog is: transient impact forces the optimizer to unwind against the signal after spikes. This is the same mathematical phenomenon (inverse of a correlated positive operator applied to a positive input).

---

## 9. Open questions

1. **Sharp probability bound.** Is $\Pr(\text{sign}(u^\star_t)\neq\text{sign}(\alpha_t)) \leq \Phi(-\sqrt{\cos\pi\nu})\cdot 2$ for all stationary Gaussian signals with completely monotone forecast, with the OU case saturating the bound? The bound $\tfrac12 - \tfrac{1}{\pi}\arcsin\sqrt{\cos\pi\nu}$ from §5 for OU is a candidate universal lower bound for the mismatch probability across mean-reverting Gaussian signals; more general signals may violate it.

2. **Non-Gaussian signals.** For heavy-tailed or skewed signals, the joint distribution of $(u^\star_t,\alpha_t)$ is non-Gaussian; the arcsine formula for sign match no longer applies. Do heavy-tailed signals sign-match less often?

3. **Constrained problems.** Adding a long-only constraint $u_t\geq 0$ forces sign-match with the constraint $\alpha_t\geq 0$ (else $u^\star_t = 0$). The KKT structure introduces a signal-dependent stopping set; describing its shape is a follow-up to §4.4 of the paper.

4. **Nonlinear cost extensions.** With cost $\langle u, Gf(u)\rangle$ for a monotone $f$, the first-order condition is nonlinear and sign match may improve (concavity in cost penalizes large trades disproportionately, reducing overshoot). Preliminary intuition; needs verification.

---

## 10. One-line takeaway

For transient-impact optimal execution with a mean-reverting signal, the optimal trade and the current signal share sign about $\tfrac12+\tfrac{1}{\pi}\arcsin\sqrt{\sin(\pi\beta/2)}$ of the time under OU. Almost-sure pointwise sign preservation requires deterministic monotone signals or the temporary-impact limit $\beta\to 1$; it is not a property of generic profitable execution schedules.
