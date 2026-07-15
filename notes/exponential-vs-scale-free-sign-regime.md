# Exponential vs. Scale-Free Kernels: A Sign-Flip Regime That Disappears

**Date:** 2026-07-11
**Companion to:** `papers/markowitz-of-cost-pnas.md`, `notes/sign-agreement-conditions.md`
**Question:** For an exponential impact kernel, the optimal execution rule against a mean-reverting signal admits a regime in which the trader trades against the current signal on average. The scale-free (power-law) kernel of the paper has no such regime. Why?

---

## 1. Exponential kernel: the derivation

Take the impact operator $G$ to be convolution against $G(t) = e^{-\kappa|t|}$, with resilience parameter $\kappa > 0$. Its Fourier symbol is $\hat G(\xi) = 2\kappa/(\kappa^2 + \xi^2)$, positive-definite as required, and factorizes as $\hat G = \hat G_-\hat G_+$ with

$$\hat G_\pm(\xi) = \frac{\sqrt{2\kappa}}{\kappa \mp i\xi}.$$

$\hat G_+$ is analytic in the upper half-plane (pole at $\xi = -i\kappa$ in the lower half-plane), so its time-domain factor $G_+(t) = \sqrt{2\kappa}\,e^{-\kappa t}\mathbf{1}_{t\geq 0}$ is causal. The two inverses are first-order differential operators:

$$G_+^{-1} = \frac{1}{\sqrt{2\kappa}}\bigl(\kappa + \partial_t\bigr), \qquad G_-^{-1} = \frac{1}{\sqrt{2\kappa}}\bigl(\kappa - \partial_t\bigr).$$

**Markov signal (OU).** Let $d\alpha_t = -\theta\alpha_t\,dt + \sigma\,dW_t$ with $\theta > 0$. Forecast curve $\bar\alpha(s,v) = e^{-\theta(v-s)}\alpha_s$ for $v\geq s$. Step 1 of the adapted optimum requires $\zeta_s = (G_-^{-1}\bar\alpha(s,\cdot))(s)$. Since $\partial_v\bar\alpha(s,v)|_{v=s} = -\theta\alpha_s$:

$$\zeta_s = \frac{\kappa + \theta}{\sqrt{2\kappa}}\,\alpha_s.$$

Step 2 applies $G_+^{-1}$ pathwise. Using $\dot\alpha_t = -\theta\alpha_t + \sigma\dot W_t$ (formally, as a distribution):

$$u^\star_t = \gamma^{-1}\,\frac{\kappa+\theta}{2\kappa}\bigl(\kappa\alpha_t + \dot\alpha_t\bigr) = \gamma^{-1}\,\frac{\kappa+\theta}{2\kappa}\bigl[(\kappa-\theta)\alpha_t + \sigma\dot W_t\bigr]. \tag{1}$$

Taking conditional expectation on $\alpha_t$:

$$\boxed{\ \mathbb{E}[u^\star_t \mid \alpha_t] = \frac{\kappa^2 - \theta^2}{2\kappa\gamma}\,\alpha_t.\ } \tag{2}$$

**Three regimes.**

- **Fast impact, slow signal ($\kappa > \theta$).** Coefficient positive. On average, trade in the direction of the signal.
- **Slow impact, fast signal ($\kappa < \theta$).** Coefficient negative. On average, trade *against* the current signal.
- **Matched decay ($\kappa = \theta$).** Coefficient zero. On average, do nothing — all trading responds to the innovation $\sigma\dot W_t$, none to the level.

The white-noise term in (1) is a technical artifact of the OU signal not being differentiable in the usual sense; it does not affect the conditional-expectation regime.

## 2. Why the sign flips

Physically: an executed trade at time $t$ leaves an impact tail decaying with half-life $1/\kappa$. A signal at time $t$ has predictive half-life $1/\theta$. If $\theta > \kappa$, the impact from a signal-following trade outlives the signal itself; the trader pays impact cost after the alpha is gone. The cost-optimal response is to under-trade the level, and beyond the phase boundary $\theta = \kappa$, to trade in the opposite direction — anticipating the signal's mean reversion and starting the unwind before the signal decays.

Mechanically: the exponential kernel forces the inverse operator to be a *first-order* differential operator $\kappa + \partial_t$. Applied to a mean-reverting signal, the two pieces of this operator pull opposite ways: $\kappa\alpha_t$ is signal-following, and $\partial_t\alpha_t$ is signal-anti-following in conditional expectation (since $\mathbb{E}[\dot\alpha_t \mid \alpha_t] = -\theta\alpha_t$). Whichever term dominates determines the sign of the trade.

Symbol-level: the WH inverse $\hat G_+^{-1}(\xi) = (\kappa - i\xi)/\sqrt{2\kappa}$ has a *zero* at $\xi = -i\kappa$. The OU signal has a spectral pole at $\xi = \pm i\theta$ (spectrum $\sigma^2/(\theta^2+\xi^2)$). When the operator zero passes the signal pole in the complex plane — at $\theta = \kappa$ — the sign of the response flips. Zero-pole crossings on the imaginary axis are a standard mechanism for sign flips in linear filtering.

## 3. Scale-free kernel: no sign flip

For the power-law kernel of the paper, $\hat G_+^{-1}(\xi) = c_\beta^{-1/2}(-i\xi)^\nu$ with $\nu = (1-\beta)/2 \in (0, 1/2)$. This symbol has a *branch point* at $\xi = 0$; it has no zero anywhere in the complex plane away from the branch point, and in particular no zero on the imaginary axis. There is no signal-decay rate $\theta$ at which the operator zero could coincide with the signal pole. The zero-pole crossing mechanism of §2 is unavailable.

The direct calculation confirms this. From §2.7 of the paper, $\zeta_s = \theta^\nu\alpha_s$ for OU. From the sign-agreement note,

$$\mathbb{E}[u^\star_t \mid \alpha_t] = \gamma^{-1}\kappa_{1-\beta}\theta^{2\nu}\,\alpha_t = \gamma^{-1}\kappa_{1-\beta}\theta^{1-\beta}\,\alpha_t.$$

The coefficient is $\theta^{1-\beta} > 0$ for all $\theta > 0$ and all $\beta \in (0,1)$. **No regime of the parameter space produces on-average against-signal trading under the scale-free kernel.**

Mechanically: the fractional operator $D_+^\nu$ is not first-order. In Marchaud form,

$$(D_+^\nu\alpha)(t) = \frac{\nu}{\Gamma(1-\nu)}\int_0^\infty \frac{\alpha_t - \alpha_{t-r}}{r^{1+\nu}}\,dr,$$

it integrates the trajectory over all past scales. For stationary mean-reverting $\alpha$, $\mathbb{E}[\alpha_{t-r} \mid \alpha_t] = \alpha_t e^{-\theta r}$ under time-reversibility, so each increment $\alpha_t - \mathbb{E}[\alpha_{t-r}\mid\alpha_t] = \alpha_t(1-e^{-\theta r})$ has the same sign as $\alpha_t$. The integral of same-signed increments is same-signed. The operator averages away the local anti-correlation that drives the sign flip in the first-order case.

## 4. What the two cases share and where they differ

Both cases share the value formula: OU on either kernel gives value $\propto \theta^{1-\beta}$ (paper §2.7) or its exponential counterpart $\propto \frac{(\kappa+\theta)^2}{2\kappa}$, both strictly increasing in the signal-decay rate $\theta$. Both share $\mathbb{E}\!\int u^\star_t\alpha_t\,dt > 0$: the integrated identity of the sign-agreement note is a general consequence of the gain–cost value being positive, and it holds under both kernels.

Both differ in the conditional-expectation identity. Under the scale-free kernel, $\mathbb{E}[u^\star_t \mid \alpha_t]$ is always a positive multiple of $\alpha_t$ (on-average signal-following). Under the exponential kernel, the sign of this multiple depends on the ratio $\theta/\kappa$, and passes through zero at $\theta = \kappa$.

## 5. Where the exponential regime shows up in the literature

The Neuman–Voß (2022) treatment of signal-adaptive execution under exponential kernel gives a Riccati closed form for the optimal position. Their optimal trading rate is a linear combination of the current signal, the current inventory, and the impact state; sign structure depends on the eigenvalues of the state-space matrix, and regime transitions of the type derived above should be visible in the Riccati coefficients as the signal timescale crosses the impact timescale. Whether the sign-flip phase boundary $\theta = \kappa$ derived here matches a transition in the Neuman–Voß feedback gains is a check I have not performed; the WH derivation makes the boundary explicit and provides a candidate location.

## 6. General principle

The distinction is not particular to OU. For any Markov signal with generator $\mathcal{L}$, exponential kernel gives

$$\mathbb{E}[u^\star_t \mid \alpha_t] \propto (\kappa + \mathcal{L})\alpha_t,$$

and sign depends on whether $\kappa I + \mathcal{L}$ acts positively or negatively on $\alpha_t$. For monotone-mean-reverting signals (spectrum of $\mathcal{L}$ negative on $\alpha$-modes), this operator has a sign-flip regime whenever $\kappa$ is smaller than the modulus of a signal eigenvalue.

For the scale-free kernel, the corresponding operator is $D_+^\nu$, whose action on a stationary process cannot be written as $\text{const} + \mathcal{L}$-scale operator; it is inherently multiscale. The absence of a resilience timescale $\kappa$ in the kernel removes the phase boundary.

**One-line summary.** Exponential kernels give first-order inverse operators with a zero on the imaginary axis; the zero can cross a signal pole and flip the sign of the conditional-expectation response. Power-law kernels give fractional-order inverse operators with no such zero, so the response sign is fixed by the impact-decay exponent alone and is always co-directional with the signal on average.

## 7. Implications

- The signal-vs-antisignal phase boundary of the exponential kernel is a modeling artifact of a single resilience timescale coinciding with the signal timescale. Reporting execution results under exponential kernels without stating the ratio $\theta/\kappa$ leaves ambiguous which regime is being reported.
- The scale-free result is a strengthened form of on-average signal-following: for any mean-reverting signal, the conditional expectation of the optimal trade is co-directional with the current signal, at all impact exponents and all signal timescales.
- For the paper: this contrast is one clean argument for the empirical relevance of the power-law kernel form beyond the microstructural evidence — the optimal policy under the scale-free kernel has structurally simpler sign behavior, avoiding regime-dependent interpretation.

## 8. Two natural follow-ups

- **Two-exponential kernel.** $G(t) = a_1 e^{-\kappa_1|t|} + a_2 e^{-\kappa_2|t|}$ has two resilience timescales. Does the against-signal regime persist for OU signal with $\theta$ between $\kappa_1$ and $\kappa_2$, or does averaging over two timescales already begin to erase the phase boundary? The prediction from the general principle is that with $n$ exponential modes, there are $n$ candidate sign-flip boundaries, and the boundaries begin to overlap as $n$ grows, approaching the smooth-signed behavior of the fractional-integral limit.
- **Regularized power-law.** Adding a temporary-impact term $\tfrac12\eta u_t^2$ (paper §4.2) introduces a crossover frequency $\xi_\ast = (\gamma c_\beta/\eta)^{1/(1-\beta)}$. Below $\xi_\ast$ the fractional structure dominates; above it, myopic signal-following takes over. Neither regime displays a sign flip against the signal, but the coefficient of the on-average response is $\eta$-dependent.
