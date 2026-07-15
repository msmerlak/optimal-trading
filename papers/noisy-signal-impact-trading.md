# Optimal Trading with Noisy Signals and Persistent Impact: Wiener–Hopf Duality and the Innovation Principle

---

> **Draft status:** First complete draft.  
> All derivations are original unless cited. Claims marked *tentative* have not been cross-checked against the full literature and should be treated as conjectures.

---

## Abstract

We study stationary optimal trading policies for an agent who observes a noisy predictor of per-trade returns and faces persistent (transient) price impact described by a general positive-definite convolution kernel $K$.  Posing the expected-gain-minus-cost objective as a quadratic program in the space of trade rates, we identify the cost functional as the squared norm induced by $K$ on trades, and its Legendre–Fenchel conjugate as the dual norm induced by $K^{-1}$ on signals.  The unconstrained optimal policy solves the Fredholm equation $K*x = f$.  Imposing causality—so that trades depend only on the past signal—requires the Wiener–Hopf factorisation $K = K_+ K_-$.  We show that for an AR(1) signal and an exponential impact kernel, the anticausal factor acts on the signal by simple scalar multiplication, leaving a constant that depends on the product of signal autocorrelation and kernel decay rate; the causal factor then reduces the optimal policy to a first-order causal difference of the signal—its *kernel innovation*.  For power-law kernels the same structure holds with the causal factor becoming a causal fractional derivative.  Finally, when the predictor is observed with additive noise, we show that the optimal policy admits a clean two-stage decomposition: first denoise via the Wiener filter, then apply the impact-adjusted causal rule.  Throughout, we interpret the construction as a separation of the estimation problem (predicting the true signal) from the control problem (trading optimally given the signal), a separation that holds exactly under Gaussian linearity.

---

## 1. Introduction

A recurrent theme in quantitative trading is the tension between *acting on a signal* and *absorbing the market impact of doing so*.  When a trader acts aggressively on a predictor, the predictive edge is consumed by the price disturbance the very execution creates.  When the trader acts too timidly, the signal decays before it is monetised.  The optimal balance depends, in a precise mathematical sense, on the spectral geometry of the impact kernel and the signal.

The seminal framework of Gârleanu and Pedersen [GP13] resolves an analogous tension in closed form for **quadratic instantaneous transaction costs** (no transient impact) with OU return-predicting factors: the optimal portfolio is a weighted average of a current Markowitz target and the existing position, with a constant trading-speed parameter (the 'aim-and-trade' rule). Their cost structure is *not* a transient propagator kernel, but their analysis provides the conceptual blueprint for combining a quadratic trading penalty with a mean-reverting alpha signal.  The line of work [LN19, AJN24, AN22, GSS12] extends to Volterra-type transient propagator kernels and vector signals, typically at the cost of characterising the solution through an operator-valued Riccati or Fredholm equation rather than giving a closed-form recipe.

The present note takes a different—and deliberately elementary—path.  Rather than deriving the optimal policy from a dynamic programming equation, we:

1. Pose the infinite-horizon stationary problem directly in frequency domain.
2. Read off the solution structure from the Legendre–Fenchel transform of the quadratic cost.
3. Use the Wiener–Hopf factorisation of $K$ to impose causality.
4. Carry out the calculation explicitly for AR(1) signals, obtaining a closed-form result that reveals the *innovation* interpretation.
5. Layer on an additive observation noise model and derive the Wiener prefilter.

The derivations are self-contained and may serve as a pedagogical entry point to the more technically demanding literature cited above.

### 1.1 Paper outline

Section 2 sets up the propagator model and defines the stationary objective.  Section 3 develops the Legendre–Fenchel duality, defining the two norms.  Section 4 derives the causal optimal policy via Wiener–Hopf factorisation.  Section 5 specialises to the AR(1) signal and proves that the anticausal factor acts as a scalar, with the scalar depending on the signal–kernel correlation $\lambda\rho$.  Section 6 provides the innovation interpretation and generalises to power-law kernels.  Section 7 treats the noisy predictor.  Section 8 works through illustrative examples.  Sections 9–11 discuss related work, limitations, and conclusions.

---

## 2. Problem Formulation

### 2.1 Propagator model of price impact

We work in discrete time with period normalised to one.  Let $x_t \in \mathbb{R}$ denote the *trade rate* at time $t$ (signed, positive = buy), and define the *position* $q_t = \sum_{s \leq t} x_s$.  Following the propagator framework of Bouchaud, Gefen, Potters & Wyart [BGPW04] and Gatheral [Gat10], the mid-price is

$$S_t = S_0^{\rm unaffected} + \sum_{s \leq t} G(t-s)\, x_s,$$

where $G : \mathbb{Z}_{\geq 0} \to \mathbb{R}$ is the (causal, one-sided) **impact kernel**, characterising how much a unit trade at time $s$ has shifted the price at time $t > s$.  Common choices include the **exponential** $G(n) = \lambda^n$ and the **power-law** $G(n) = n^{-\beta}$ with $\beta \in (0,1)$.

### 2.2 Return on trade versus return on position

The PnL of the trading strategy has two components.  The *signal PnL* arises because the agent holds a view $f_t$ on the immediate expected return generated by a unit trade (return on trade, not on position).  Formally, if we write the unaffected-price increment as $\delta S_t^0 \approx f_t$ in expectation, then the expected revenue from trade $x_t$ is $f_t x_t$.

The *impact cost* is the execution shortfall: executing $x_t$ at a price that has been moved up by its own past trades.  The expected cost (to second order in $x$) is

$$C_t = \sum_{s \leq t} G(t-s)\, x_s \cdot x_t.$$

Summing over time and symmetrising:

$$\mathcal{C}(x) = \frac{1}{2}\sum_{s,t} x_t\, K(t-s)\, x_s, \quad K(n) = G(|n|),$$

where $K$ is the **symmetrised kernel**, $K(n) = G(|n|)$.  We adopt the standard *execution-at-mid* convention in which the trader pays only half of the contemporaneous self-impact $G(0)$; this convention is what allows the cost to be written cleanly as the symmetric quadratic form with $K(0) = G(0)$.

### 2.3 Stationary objective

We seek a *stationary causal policy*: a filter $H$ with $x_t = \sum_{k \geq 0} H(k)\, f_{t-k}$, so that trades depend causally on the signal history.  In the infinite-horizon ergodic limit, the per-period expected gain-minus-cost is

$$\mathcal{J}(H) = \mathbb{E}[f_t x_t] - \frac{1}{2}\mathbb{E}[x_t (K * x)_t],$$

where $(K*x)_t = \sum_s K(t-s) x_s$.  Using stationarity and the Parseval–Plancherel identity, this becomes

$$\mathcal{J}(H) = \int_{-\pi}^{\pi} \hat{H}(\omega)\, S_f(\omega)\frac{d\omega}{2\pi} - \frac{1}{2}\int_{-\pi}^{\pi} |\hat{H}(\omega)|^2 \hat{K}(\omega)\, S_f(\omega)\frac{d\omega}{2\pi}, \tag{1}$$

where $\hat{H}(\omega) = \sum_{k\geq 0} H(k) e^{-i\omega k}$ is the causal transfer function and $S_f(\omega)$ is the power spectral density of the signal $f$.

### 2.4 Positive-definiteness and no-dynamic-arbitrage

We assume $\hat{K}(\omega) > 0$ for all $\omega$.  This is equivalent to requiring that the cost functional $\mathcal{C}$ is strictly convex (positive definite as a quadratic form), which in turn is the condition for absence of dynamic arbitrage in the sense of Gatheral [Gat10]: no round-trip strategy can yield positive expected PnL.

---

## 3. Legendre–Fenchel Duality: Two Norms

### 3.1 The cost norm on trades

The quadratic cost defines an inner product on trade sequences:

$$\langle x, x' \rangle_K = \sum_{s,t} x_t K(t-s) x'_s = \int_{-\pi}^{\pi} \hat{x}(\omega)^* \hat{K}(\omega) \hat{x}'(\omega) \frac{d\omega}{2\pi},$$

and an associated norm $\|x\|_K^2 = \langle x, x\rangle_K$.  The stationary cost per period is $\frac{1}{2}\|x\|_K^2$.

### 3.2 The Legendre–Fenchel transform

The **Legendre–Fenchel conjugate** of $\phi(x) = \frac{1}{2}\|x\|_K^2$ is

$$\phi^*(f) = \sup_x \left[\langle f, x\rangle - \frac{1}{2}\|x\|_K^2\right] = \frac{1}{2}\|f\|_{K^{-1}}^2, \tag{2}$$

where $\|f\|_{K^{-1}}^2 = \langle f, K^{-1}*f\rangle$ is the **dual norm** induced by $K^{-1}$.  The supremum is attained at the unconstrained optimal trade

$$x^* = K^{-1} * f, \tag{3}$$

i.e., the trade that inverts the kernel on the signal.  The value $\phi^*(f)$ measures how much signal is *extractable* given the cost geometry: it is the maximum expected gain per period, and defines a natural inner product on the signal space.

**Interpretation:** Equation (2) says that the cost kernel $K$ simultaneously defines two objects:
- A *norm on trades* $\|\cdot\|_K$, quantifying how expensive it is to move through the market.
- A *dual norm on signals* $\|\cdot\|_{K^{-1}}$, quantifying how much predictive edge a signal carries after impact is accounted for.

The Legendre–Fenchel transform is the passage between these two dual spaces.

---

## 4. Causal Optimal Policy: Wiener–Hopf Factorisation

The unconstrained optimum (3) requires inverting $K$ without any causality constraint.  In practice, we demand that $x_t$ depend only on $f_s$, $s \leq t$.  This is the classical **causal Wiener filter** problem applied to the quadratic cost.

### 4.1 First-order condition

Restricting to causal $x$ (transfer function analytic outside the unit disk in the $z$-variable, i.e. expanded in non-negative powers of $z^{-1}$), the FOC for maximising $\langle f, x\rangle - \tfrac{1}{2}\langle x, K*x\rangle$ is the **projection FOC**: the residual $K*x - f$ has zero causal part,

$$[K*x - f]_+ = 0, \qquad x \text{ causal.} \tag{4}$$

Factor $\hat K(z) = \hat K_+(z)\hat K_-(z)$ with $\hat K_+$ causal (analytic and minimum-phase outside the unit disk) and $\hat K_-$ anticausal.  Setting $y = K_+ * x$ (causal, since $K_+$ is causal), condition (4) becomes

$$[\hat K_-(z)\, \hat y(z) - \hat f(z)]_+ = 0 \quad \Longleftrightarrow \quad \hat y(z) = \left[\frac{\hat f(z)}{\hat K_-(z)}\right]_+, \tag{5}$$

where we used that multiplication by the anticausal $\hat K_-$ followed by causal projection $[\cdot]_+$ is invertible on the causal subspace.  Inverting $K_+$ recovers $x$:

$$\boxed{\hat{x}(z) = \hat{K}_+^{-1}(z)\,\left[\frac{\hat{f}(z)}{\hat{K}_-(z)}\right]_+} \tag{6}$$

This is the *standard causal Wiener–Hopf solution* to $K * x = f$ under causality. It is not new — versions of it appear in [GSS12], [AN22], and (in the power-law case) [FSB+] — and serves here as the entry point to the explicit AR(1) reduction of §5 and the noisy-signal composition of §7, which are the contributions of this note.

### 4.2 The factorisation

For the symmetric kernel $K(n) = G(|n|)$ with $\hat{K}(\omega) > 0$, Bochner's theorem guarantees that $\hat{K}$ has a unique spectral factorisation

$$\hat{K}(\omega) = |\hat{K}_+(\omega)|^2, \quad \hat{K}_+(\omega) = \exp\!\left(\frac{1}{2}\int_{-\pi}^{\pi} \log \hat{K}(\theta)\,\frac{e^{i\theta}+e^{i\omega}}{e^{i\theta}-e^{i\omega}}\,\frac{d\theta}{2\pi}\right),$$

where $\hat{K}_+$ is the outer (causal) spectral factor and $\hat{K}_- = \hat{K}_+(-\omega)$ is the anticausal factor.

The causal solution (6) separates into two stages:
1. **Anticausal whitening** of the signal: apply $\hat{K}_-^{-1}$ to $\hat{f}$ (a non-causal, anticausal operation on $f$).
2. **Causal projection**: keep only the causal part $[\,\cdot\,]_+$.
3. **Causal shaping**: apply $\hat{K}_+^{-1}$ to the result.

---

## 5. AR(1) Signal: The Anticausal Factor Reduces to a Scalar

We now specialise to the most tractable and empirically relevant case: an **AR(1) signal** and an **exponential impact kernel**.

### 5.1 Setup

*Signal:* $f_t = \rho f_{t-1} + \epsilon_t$, with $|\rho| < 1$ and $\epsilon_t \sim \text{i.i.d.}(0,\sigma^2)$.  The spectral density is
$$S_f(\omega) = \frac{\sigma^2}{|1 - \rho e^{-i\omega}|^2}, \quad \hat{f}(z) = \frac{\sigma}{1 - \rho z^{-1}} \quad (|z| > |\rho|).$$

*Kernel:* $K(n) = \lambda^{|n|}$ for $\lambda \in (0,1)$.  The $z$-transform is
$$\hat{K}(z) = \frac{1-\lambda^2}{(1-\lambda z^{-1})(1-\lambda z)},$$
which gives the Wiener–Hopf factors
$$\hat{K}_+(z) = \frac{\sqrt{1-\lambda^2}}{1-\lambda z^{-1}}, \qquad \hat{K}_-(z) = \frac{\sqrt{1-\lambda^2}}{1-\lambda z}.$$

Here $\hat{K}_+$ has its pole at $|z| = \lambda < 1$ (inside the unit disk), so it is causal and stable.  The anticausal factor $\hat{K}_-$ has its pole at $|z| = 1/\lambda > 1$ (outside).

### 5.2 Applying the anticausal inverse

The anticausal factor inverse is $\hat{K}_-^{-1}(z) = (1-\lambda z)/\sqrt{1-\lambda^2}$.  Computing the product:

$$\frac{\hat{f}(z)}{\hat{K}_-(z)} = \hat{K}_-^{-1}(z)\,\hat{f}(z) = \frac{1-\lambda z}{\sqrt{1-\lambda^2}}\cdot\frac{\sigma}{1-\rho z^{-1}} = \frac{\sigma}{\sqrt{1-\lambda^2}}\cdot\frac{z(1-\lambda z)}{z-\rho}. \tag{7}$$

We perform a partial fraction decomposition of the rational factor:

$$\frac{z(1-\lambda z)}{z-\rho} = \frac{-\lambda z^2 + z}{z-\rho}.$$

Polynomial long division gives:

$$-\lambda z^2 + z = (-\lambda z + 1 - \lambda\rho)(z-\rho) + \rho(1-\lambda\rho),$$

so

$$\frac{z(1-\lambda z)}{z-\rho} = -\lambda z + (1-\lambda\rho) + \frac{\rho(1-\lambda\rho)}{z-\rho}. \tag{8}$$

### 5.3 Causal projection

In $z$-transform terms:
- The term $-\lambda z$ corresponds to $-\lambda\,\delta_{t+1}$: a **future** shift, hence **anticausal** — excluded by $[\,\cdot\,]_+$.
- The term $(1-\lambda\rho)$ is instantaneous: **present**, included.
- The term $\frac{\rho(1-\lambda\rho)}{z-\rho} = \frac{\rho(1-\lambda\rho) z^{-1}}{1-\rho z^{-1}}$: has a stable pole at $z=\rho$ inside the unit disk — **causal**, included.

Combining the last two terms:

$$\left[\frac{z(1-\lambda z)}{z-\rho}\right]_+ = (1-\lambda\rho) + \frac{\rho(1-\lambda\rho)}{z-\rho} = (1-\lambda\rho)\left(1 + \frac{\rho}{z-\rho}\right) = (1-\lambda\rho)\cdot\frac{z}{z-\rho}. \tag{9}$$

Therefore

$$\left[\frac{\hat{f}(z)}{\hat{K}_-(z)}\right]_+ = \frac{\sigma(1-\lambda\rho)}{\sqrt{1-\lambda^2}}\cdot\frac{1}{1-\rho z^{-1}} = \frac{(1-\lambda\rho)}{\sqrt{1-\lambda^2}}\,\hat{f}(z). \tag{10}$$

**Key result:** the causal projection of $\hat{K}_-^{-1}\hat{f}$ is *proportional to $\hat{f}$ itself*, with scalar coefficient $(1-\lambda\rho)/\sqrt{1-\lambda^2}$.  The anticausal factor does not distort the shape of the signal; it merely rescales it by a constant that encodes the *alignment* between the signal's autocorrelation $\rho$ and the kernel's decay rate $\lambda$.

### 5.4 The full optimal causal policy

Applying the causal factor $\hat{K}_+^{-1}(z) = (1-\lambda z^{-1})/\sqrt{1-\lambda^2}$:

$$\hat{x}(z) = \frac{1-\lambda z^{-1}}{\sqrt{1-\lambda^2}}\cdot\frac{(1-\lambda\rho)}{\sqrt{1-\lambda^2}}\,\hat{f}(z) = \frac{(1-\lambda\rho)}{1-\lambda^2}\,(1-\lambda z^{-1})\,\hat{f}(z). \tag{11}$$

In the time domain:

$$\boxed{x_t = \frac{1-\lambda\rho}{1-\lambda^2}\,(f_t - \lambda f_{t-1}).} \tag{12}$$

*Interpretation:* The optimal trade at time $t$ is proportional to the **first-order backward difference** of the signal weighted by the kernel decay $\lambda$.  The prefactor $(1-\lambda\rho)/(1-\lambda^2)$ is a constant that depends only on the correlation between consecutive terms of the signal ($\rho$) and the persistence of price impact ($\lambda$).

An intuitive re-derivation of the scalar collapse via Markov conditional expectations is given in §5.5.

Limit cases (direct substitution into (12) with $c(\rho,\lambda) := (1-\lambda\rho)/(1-\lambda^2)$):
- $\lambda \to 0$ (temporary impact): $c \to 1$, so $x_t \to f_t$ — trade proportional to the signal itself.
- $\rho \to 0$ (white-noise signal): $c \to 1/(1-\lambda^2)$, so $x_t \to \frac{1}{1-\lambda^2}(f_t - \lambda f_{t-1})$ — the kernel-innovation of an i.i.d. signal, scaled by the kernel's spectral mass.
- $\rho \to \lambda$ (signal autocorrelation matches kernel decay): $c \to 1$, so $x_t \to f_t - \lambda f_{t-1}$ — unscaled kernel innovation; the signal and kernel "resonate" so no additional rescaling is needed.
- $\rho \to 1$ (near-unit-root signal): $c \to (1-\lambda)/(1-\lambda^2) = 1/(1+\lambda)$, so $x_t \to \frac{1}{1+\lambda}(f_t - \lambda f_{t-1})$ — the signal becomes near-constant and the prefactor reflects only the kernel structure.

### 5.5 Markov closure of the future integral

The partial-fraction calculation in §5.3 is correct but somewhat opaque about *why* the answer comes out as a single scalar times $\hat f$. The following alternative derivation makes the mechanism transparent and shows that the scalar collapse is a consequence of the **Markov property of the signal**, not of the exponential form of the kernel.

**The anticausal filter as a future integral.** The anticausal Wiener–Hopf factor inverse $\hat K_-^{-1}(z) = (1-\lambda z)/\sqrt{1-\lambda^2}$ has $z$-transform expansion $\hat K_-^{-1}(z) = \sum_{m \ge 0} a_m\, z^m$ with $a_0 = 1/\sqrt{1-\lambda^2}$ and $a_1 = -\lambda/\sqrt{1-\lambda^2}$ (and $a_m = 0$ for $m \ge 2$). Multiplication by $z^m$ on the $z$-transform corresponds to a *forward* time shift $L^{-1}$, so $K_-^{-1}$ acts on a sequence $f$ as the anticausal sum

$$
(K_-^{-1} * f)_t \;=\; \sum_{m \ge 0} a_m\, f_{t+m}.
\tag{12a}
$$

For the exponential kernel this is the two-term combination $(f_t - \lambda f_{t+1})/\sqrt{1-\lambda^2}$. In general it is a linear combination of *future* signal values, which the trader cannot observe.

**Causal projection = conditional expectation.** Under joint Gaussianity of $f$, the deterministic $[\,\cdot\,]_+$ projection of $K_-^{-1} f$ onto the causal subspace coincides with the $\mathcal{F}_t$-conditional expectation:

$$
[K_-^{-1} f]_+(t) \;=\; \mathbb{E}\!\left[(K_-^{-1} * f)_t \,\Big|\, \mathcal{F}_t\right] \;=\; \sum_{m \ge 0} a_m\, \mathbb{E}[f_{t+m} \mid \mathcal{F}_t].
\tag{12b}
$$

(For non-Gaussian $f$, the right-hand side is the optimal *linear* projection onto $\mathcal{F}_t^f$, which coincides with the $[\,\cdot\,]_+$ operator on z-transforms; the equality holds in the wide-sense-stationary sense.)

**Markov closure.** If $f$ is AR(1) with $f_t = \rho f_{t-1} + \epsilon_t$, the Markov property gives

$$
\mathbb{E}[f_{t+m} \mid \mathcal{F}_t] \;=\; \rho^m f_t, \qquad m \ge 0.
$$

Substituting into (12b),

$$
[K_-^{-1} f]_+(t) \;=\; \Big(\sum_{m \ge 0} a_m\, \rho^m\Big) f_t \;=\; \hat K_-^{-1}(\rho)\,f_t.
\tag{12c}
$$

The anticausal filter's $z$-transform, evaluated at the AR(1) pole $\rho$, *is* the scalar. For the exponential kernel

$$
\hat K_-^{-1}(\rho) \;=\; \frac{1 - \lambda \rho}{\sqrt{1-\lambda^2}},
$$

reproducing (10).

**Why this is the right way to think about (10).** The constant $\lambda\rho$ in (12) has a direct probabilistic meaning: $\lambda$ is the impulse-response coefficient of the anticausal Wiener–Hopf factor inverse at one-step-ahead, and $\rho$ is the one-step-ahead conditional expectation coefficient of the signal. Their product is the only term in (12a) that survives the conditional expectation; $a_0 = 1$ contributes the leading $1$. The signal–kernel "alignment" interpretation given after (10) is therefore literal: the constant measures how much of the anticausal filter's reach falls within the predictable horizon of the signal.

**Generalisation to AR($p$) and finite-state Markov signals.** Markov closure extends with no essential change to richer signals.

- *AR($p$).* If $f$ has rational spectrum with autoregressive roots $z_1,\dots,z_p$ (inside the unit disk), then $\mathbb{E}[f_{t+m} \mid \mathcal{F}_t] = \sum_{j=1}^p c_j(\mathcal{F}_t)\,z_j^m$ for $\mathcal{F}_t$-measurable coefficients $c_j$. Equation (12b) collapses to a sum of $p$ scalars,
  $$
  [K_-^{-1} f]_+(t) \;=\; \sum_{j=1}^p \hat K_-^{-1}(z_j)\, c_j(\mathcal{F}_t),
  $$
  so the causal projection remains a *finite-dimensional* linear functional of the signal history, rather than a scalar multiple of $f_t$.

- *Finite-state Markov.* If $f_t = h(X_t)$ for a Markov chain $X$ with transition operator $\mathbf{P}$, then $\mathbb{E}[f_{t+m} \mid X_t] = (\mathbf{P}^m h)(X_t)$, and the closure becomes the matrix expression
  $$
  [K_-^{-1} f]_+(t) \;=\; \Big(\hat K_-^{-1}(\mathbf{P})\,h\Big)(X_t),
  $$
  where $\hat K_-^{-1}(\mathbf{P}) = \sum_{m \ge 0} a_m \mathbf{P}^m$ is the filter's transfer function evaluated at the transition operator. Convergence requires the spectral radius of $\mathbf{P}$ times the radius of convergence of $\hat K_-^{-1}$ to be less than one.

**Where the closure fails.** The argument breaks exactly where the Markov hypothesis fails:

- *Long-memory / fractional Brownian signals.* For $f$ driven by fBm with Hurst $H \neq 1/2$, $\mathbb{E}[f_{t+m} \mid \mathcal{F}_t]$ is not a finite linear combination of finitely many statistics of $\mathcal{F}_t$ but a path functional of the entire history (cf. the prediction formula for fBm of Nuzman & Poor 2000). Equation (12b) does not collapse, and the optimal policy must be expressed in terms of operator resolvents — the regime of Abi Jaber–Neuman [AJN22; AJN24].
- *Switching regimes.* If the AR coefficient $\rho$ itself follows a hidden Markov chain, $\mathbb{E}[f_{t+m}\mid\mathcal F_t]$ depends on the posterior over regimes and the closure is at best matrix-valued under the filter's belief state.

This perspective also clarifies the role of the exponential kernel: it gives a $\hat K_-^{-1}$ with only *two* non-zero impulse-response coefficients ($a_0, a_1$), so the future integral reduces to a single one-step-ahead forecast $\rho f_t$. Any kernel with infinitely many anticausal impulse-response coefficients still produces a scalar via (12c), provided the series $\sum_m a_m \rho^m = \hat K_-^{-1}(\rho)$ converges — a condition we exploit in §6.3 to handle power-law kernels.

---

## 6. The Innovation Interpretation

### 6.1 Kernel innovations

Define the **kernel innovation** of the signal $f$ with respect to the impact kernel $K$ as the output of the causal spectral factor inverse applied to $f$:

$$\hat{K}_+^{-1}(z)\,\hat{f}(z).$$

For the exponential kernel this is $(1-\lambda z^{-1})\hat{f}(z)/\sqrt{1-\lambda^2}$, the first-order causal difference operator.  In the time domain this is $f_t - \lambda f_{t-1}$, which is precisely the **one-step-ahead innovation of $f$ in the AR(1) model with parameter $\lambda$**.

The result (12) says:

> *The optimal trade is proportional to the kernel innovation of the signal, up to a scalar that encodes signal autocorrelation.*

This is a natural generalisation of the idea that in a white-noise world, optimal trades equal the signal.  With persistent impact, the correct "whitening" uses the impact kernel rather than the signal's own autocorrelation structure.

### 6.2 Power-law kernels and causal fractional derivatives

For the power-law kernel $K(n) \sim |n|^{-\beta}$, $0 < \beta < 1$, the Fourier transform satisfies $\hat{K}(\omega) \sim C|\omega|^{\beta-1}$ for $|\omega| \ll 1$.  The Wiener–Hopf causal factor has transfer function

$$\hat{K}_+(\omega) \sim C_+\,(-i\omega)^{(\beta-1)/2}, \tag{13}$$

so the causal factor inverse is

$$\hat{K}_+^{-1}(\omega) \sim C_+^{-1}\,(-i\omega)^{(1-\beta)/2}. \tag{14}$$

In the time domain, multiplication by $(-i\omega)^{\alpha}$ (with $\alpha = (1-\beta)/2 \in (0,\tfrac{1}{2})$) corresponds to a **causal fractional derivative of order $\alpha$**:

$$(\mathcal{D}^\alpha_+ f)_t = \frac{1}{\Gamma(1-\alpha)}\int_0^\infty \frac{f_t - f_{t-s}}{s^{1+\alpha}}\,ds. \tag{15}$$

Note that for $\beta \in (0,1)$ the symmetric kernel $K(n) = |n|^{-\beta}$ is *not* absolutely summable; it must be interpreted as a positive-definite tempered distribution whose Fourier transform $\hat K(\omega) \sim |\omega|^{\beta-1}$ is locally integrable at the origin (cf. [Gat10] for the no-arbitrage admissibility of such kernels).

The optimal trade is therefore $x_t \propto \mathcal{D}^{(1-\beta)/2}_+ f_t$: a **causal fractional derivative of the signal**.

This operator is smoother than first-differencing ($\alpha = 1$) but rougher than the signal itself ($\alpha = 0$), reflecting the intermediate persistence of power-law impact.  The exponent $(1-\beta)/2$ is exactly one-half the scaling exponent of the inverse kernel, which in turn determines the depth of the impact's memory.

The AR(1) anticausal projection analysis from §5 extends analogously: for Markov signals (AR or OU), the anticausal projection again reduces to a scalar times the signal, with the constant given explicitly by the Markov-closure construction of §5.5. We work this out for power-law kernels in §6.3.

### 6.3 Closed-form constants for AR/OU × power-law kernels

The Markov closure formula (12c) makes the AR(1) × power-law constant just as computable as the exponential case, provided we identify the anticausal Wiener–Hopf factor of the power-law kernel.

**Continuous-time: OU signal × power-law kernel.** Let $f$ be an Ornstein–Uhlenbeck signal with mean-reversion rate $\kappa > 0$, so $\mathbb{E}[f(t+s)\mid \mathcal{F}_t] = e^{-\kappa s} f(t)$ for $s \ge 0$. Let the symmetric impact kernel be $K(\tau) = c_\beta |\tau|^{-\beta}$ with $\beta \in (0,1)$, whose Fourier transform satisfies $\hat K(\omega) \propto |\omega|^{\beta-1}$. Spectral factorisation gives $\hat K_+(\omega) \propto (i\omega)^{(\beta-1)/2}$, equivalently a causal fractional integral of order $\alpha := (1-\beta)/2 \in (0, \tfrac{1}{2})$ — see (13). The anticausal factor inverse $K_-^{-1}$ therefore acts as the **anticausal Marchaud fractional derivative of order $\alpha$**,

$$
(\mathcal{D}^\alpha_- f)(t) \;=\; \frac{1}{\Gamma(-\alpha)}\int_0^\infty s^{-\alpha-1}\,[f(t+s) - f(t)]\, ds,
\tag{15a}
$$

where the subtraction of $f(t)$ regularises the $s \to 0^+$ singularity (the kernel $s^{-\alpha-1}$ is non-integrable near $0$ for $\alpha > 0$).

Taking $\mathcal{F}_t$-conditional expectation under the OU dynamics and using $\mathbb{E}[f(t+s) - f(t) \mid \mathcal{F}_t] = (e^{-\kappa s} - 1)f(t)$,

$$
\mathbb{E}[(\mathcal{D}^\alpha_- f)(t) \mid \mathcal{F}_t] \;=\; \frac{f(t)}{\Gamma(-\alpha)} \int_0^\infty s^{-\alpha-1}\,(e^{-\kappa s} - 1)\, ds.
$$

The Frullani-type integral is standard: with the substitution $u = \kappa s$,

$$
\int_0^\infty s^{-\alpha-1}\,(e^{-\kappa s} - 1)\, ds \;=\; \kappa^\alpha \int_0^\infty u^{-\alpha-1}\,(e^{-u} - 1)\,du \;=\; \Gamma(-\alpha)\,\kappa^\alpha,
$$

where the last equality is the analytic continuation of $\Gamma$ at negative argument (or, equivalently, integration by parts followed by $\int_0^\infty u^{-\alpha} e^{-u}\,du = \Gamma(1-\alpha)$ and the identity $\Gamma(1-\alpha) = -\alpha\,\Gamma(-\alpha)$). Hence

$$
\boxed{\;\mathbb{E}[(\mathcal{D}^\alpha_- f)(t) \mid \mathcal{F}_t] \;=\; \kappa^\alpha\, f(t),\quad \alpha = \tfrac{1-\beta}{2}.\;}
\tag{15b}
$$

The full optimal trade is then $x_t \propto \kappa^\alpha \cdot \mathcal{D}^\alpha_+ f(t)$, with the proportionality absorbing the spectral-factorisation normalisation. The constant $\kappa^\alpha$ is the *direct power-law analogue* of $(1-\lambda\rho)/\sqrt{1-\lambda^2}$ in (10): it measures the alignment between the mean-reversion rate of the signal and the memory depth $\alpha$ of the impact. Numerically, $\int_0^\infty u^{-\alpha-1}(e^{-u}-1)\,du = \Gamma(-\alpha)$ on $\alpha \in (0,1)$ is verified in `experiments/markov_closure_check.py`.

Limit cases:
- $\kappa \to 0$ (random walk signal): $\kappa^\alpha \to 0$, the optimal scalar vanishes; intuitively, a non-decaying signal offers no predictable horizon over which to monetise the fractional anticipation.
- $\beta \to 1$ (kernel approaches temporary/$\delta$-like): $\alpha \to 0$, and $\kappa^\alpha \to 1$, recovering the white-kernel limit $x_t \propto f_t$.
- $\beta \to 0$ (kernel approaches permanent): $\alpha \to \tfrac12$, and the optimal scalar is $\sqrt{\kappa}$ — the half-derivative regime, ill-posed without regularisation as noted in §8.2.

**Discrete-time fractional differencing.** If we model the discrete anticausal Wiener–Hopf factor inverse as the anticausal fractional difference operator

$$
\hat K_-^{-1}(z) \;=\; (1 - z)^\alpha \;=\; \sum_{m \ge 0} \binom{\alpha}{m} (-z)^m
$$

(the discrete counterpart of an anticausal fractional derivative, in the ARFIMA / Granger–Joyeux–Hosking sense), then for an AR(1) signal Markov closure (12c) gives

$$
[K_-^{-1} f]_+(t) \;=\; \hat K_-^{-1}(\rho)\,f_t \;=\; (1 - \rho)^\alpha\, f_t,
\tag{15c}
$$

by the generalised binomial theorem. The full optimal policy is then $x_t \propto (1-\rho)^\alpha\,(\Delta^\alpha_+ f)_t$, where $\Delta^\alpha_+$ is the causal fractional difference. Equation (15c) is verified to seven decimal places across $\alpha \in \{0.25, 0.5, 0.75\}$ and $\rho \in \{0.3, 0.7, 0.95\}$ in `experiments/markov_closure_check.py`.

**Discrete-time literal power-law kernel.** If instead one insists on a *literal* discrete kernel $K(n) = (1+|n|)^{-\beta}$, the anticausal Wiener–Hopf factor inverse is no longer a clean fractional difference. Its impulse-response coefficients $\{a_m\}_{m \ge 0}$ have a power-law tail $a_m \sim c\, m^{-1-\alpha}$ but with non-elementary lead coefficients. Markov closure (12c) then gives

$$
[K_-^{-1} f]_+(t) \;=\; \Big(\sum_{m \ge 0} a_m\, \rho^m\Big)\, f_t,
\tag{15d}
$$

which in the leading-order tail approximation evaluates to a Lerch transcendent / polylogarithm $\Phi(\rho, 1+\alpha, m_0)$ rather than an elementary scalar. Full closed form requires the spectral factorisation of the specific discrete power-law spectrum, which we do not pursue here; (15b) and (15c) are the elementary continuous-time and ARFIMA versions that capture the essential structure.

**Summary.** Whenever the signal is Markov and the kernel admits a Wiener–Hopf factorisation, the anticausal projection collapses to a *single scalar* given by $\hat K_-^{-1}$ evaluated at the signal's persistence parameter (a number for AR(1)/OU, a finite list for AR($p$), an operator for finite-state Markov). The exponential / AR(1), OU / power-law, and ARFIMA / fractional-differencing closures (10), (15b), (15c) are three explicit instances of the same identity (12c).

---

## 7. Noisy Predictor and Wiener Filtering

### 7.1 Observation model

Suppose the agent cannot observe $f_t$ directly but instead observes

$$\tilde{f}_t = f_t + \eta_t, \tag{16}$$

where $\eta_t \sim \text{i.i.d.}(0, \sigma_\eta^2)$ is independent observation noise.  The noise might represent model error, data delays, or the inherent uncertainty of an estimated predictor.

The signal spectral density is $S_f(\omega) = \sigma^2/|1-\rho e^{-i\omega}|^2$ and the noisy observation spectrum is

$$S_{\tilde{f}}(\omega) = S_f(\omega) + \sigma_\eta^2. \tag{17}$$

### 7.2 The Wiener filter

The optimal causal linear estimate of $f_t$ from the infinite past of $\{\tilde{f}_s : s \leq t\}$ is the classical **causal Wiener filter**:

$$\hat{f}_t^W = \sum_{k=0}^\infty W(k)\,\tilde{f}_{t-k}, \quad W(z) = \frac{1}{\hat{\phi}_{\tilde{f}}^+(z)}\left[\frac{S_f(z)}{\hat{\phi}_{\tilde{f}}^-(z)}\right]_+, \tag{18}$$

where $S_{\tilde{f}} = \hat{\phi}_{\tilde{f}}^+ \hat{\phi}_{\tilde{f}}^-$ is the spectral factorisation of the observed spectrum.  In the non-causal (two-sided, smoothing) case this simplifies to the familiar Wiener ratio:

$$W^{\rm nc}(\omega) = \frac{S_f(\omega)}{S_f(\omega) + \sigma_\eta^2} = \frac{\text{SNR}(\omega)}{1+\text{SNR}(\omega)}, \tag{19}$$

where $\text{SNR}(\omega) = S_f(\omega)/\sigma_\eta^2$ is the signal-to-noise ratio at frequency $\omega$.

### 7.3 Separation: denoise first, then trade

**Proposition (Separation Principle).**  *In the linear-Gaussian stationary model, the optimal causal policy given noisy observations $\tilde{f}$ factors as*

$$x_t^* = (\text{kernel-causal rule}) \circ (\text{causal Wiener filter}) \circ \tilde{f}_t.$$

*Formally:*

$$\hat{x}^*(z) = \hat{K}_+^{-1}(z)\left[\frac{\hat{f}^W(z)}{\hat{K}_-(z)}\right]_+. \tag{20}$$

*Proof sketch.*  The joint optimal policy maximises $\mathbb{E}[f_t x_t - \frac{1}{2}x_t(K*x)_t]$ over causal functions of $\tilde{f}$.  Since $\eta$ and $f$ are independent and the cost is quadratic, the optimal policy depends on $\tilde{f}$ only through the minimum-mean-squared-error estimate of $f$, which is the causal Wiener filter $\hat{f}^W$.  The remaining optimisation over causal functions of $\hat{f}^W$ is identical to the clean-signal problem, so the kernel-based causal rule applies.  $\square$

This separation holds exactly under Gaussian linearity and approximately (by the certainty-equivalence principle) for more general signal distributions.

### 7.4 Practical implication

Equation (20) provides an actionable two-stage recipe:

**Stage 1 (Signal estimation):** Apply the causal Wiener filter to the raw predictor to get $\hat{f}_t^W$.  This shrinks the signal toward zero at frequencies where noise dominates (low SNR) and passes it through at frequencies where the signal is strong (high SNR).

**Stage 2 (Trade execution):** Apply the kernel-innovation operator $\hat{K}_+^{-1}$ to the filtered signal to get the trade rate.

The two stages are computed in series.  If one uses the *non-causal* Wiener filter (equation 19) as an approximation, the recipe becomes:

$$x_t^* \approx \hat{K}_+^{-1} * \left(\frac{S_f}{S_f + \sigma_\eta^2} * \tilde{f}\right)_t. \tag{21}$$

The SNR weighting in Stage 1 is the key correction: without it, the agent trades too aggressively at noise-dominated frequencies, paying unnecessary impact costs.

---

## 8. Examples

### 8.1 Exponential kernel + AR(1) signal (full solution)

From equation (12), the optimal trade under a *clean* signal is

$$x_t = \frac{1-\lambda\rho}{1-\lambda^2}(f_t - \lambda f_{t-1}).$$

With observation noise $\tilde f_t = f_t + \eta_t$, the two-stage decomposition (20) applies:

**Stage 1.** The causal Wiener filter applied to $\tilde f$ produces $\hat f^W_t$. Spectral factorisation of $S_{\tilde f}(\omega) = \sigma^2/|1-\rho e^{-i\omega}|^2 + \sigma_\eta^2$ yields a rational transfer function with a pole at $z = \rho$ and a zero $\lambda_W \in (0,1)$ determined by the (standard) quadratic spectral-factorisation equation. The filtered signal $\hat f^W$ is therefore **ARMA(1,1)** with pole $\rho$ and zero $\lambda_W$, not AR(1).

**Stage 2.** Applying the causal Wiener–Hopf operator to $\hat f^W$,

$$\hat x(z) = \hat K_+^{-1}(z)\,\bigl[\hat f^W(z)/\hat K_-(z)\bigr]_+.$$

*Important caveat.* Because $\hat f^W$ is ARMA(1,1) rather than AR(1), the scalar collapse of the anticausal projection used in §5.3 does **not** apply: the causal projection $[\hat f^W/\hat K_-]_+$ produces additional causal terms beyond a single proportionality, and the final policy is not simply (12) with $\rho$ replaced by some "$\rho_W$". Carrying out the partial-fraction expansion of $(1-\lambda_W z^{-1})(1-\lambda z)/(1-\rho z^{-1})$ yields a closed form, but it is a sum of two terms rather than a rescaled AR(1) policy. We record this as future work; the operator-level statement (20) is the rigorous result.

A convenient *heuristic* leading-order approximation, valid when $\lambda_W \ll 1$ (low noise), is

$$x_t \approx \frac{1 - \lambda\rho}{1-\lambda^2}\bigl(\hat f^W_t - \lambda\, \hat f^W_{t-1}\bigr), \qquad \text{(heuristic; low-noise limit)} \tag{22}$$

which coincides with (12) applied to the filtered signal as if it were AR(1). This is *not* an exact identity for general noise levels.

### 8.2 Power-law kernel + OU signal

For $K(\tau) \propto |\tau|^{-\beta}$ and an OU signal $df = -\kappa f\,dt + \sigma\,dW$, the continuous-time optimal trade is

$$x_t \;\propto\; \kappa^{(1-\beta)/2}\,\mathcal{D}^{(1-\beta)/2}_+ f_t,$$

with the scalar $\kappa^\alpha$ ($\alpha = (1-\beta)/2$) derived in §6.3 by Markov closure of the anticausal Marchaud fractional derivative against the OU forecast $\mathbb{E}[f(t+s)\mid\mathcal F_t] = e^{-\kappa s}f(t)$. For $\beta \to 1$ (near-temporary impact) the exponent $\alpha \to 0$ and the policy approaches the signal itself; for $\beta \to 0$ (near-permanent impact) $\alpha \to \tfrac12$, giving a half-derivative scaled by $\sqrt{\kappa}$ and reflecting the extreme cost of reversing impact in a nearly permanent model.

*Note:* For the pure permanent-impact limit ($\beta = 0$), the problem is ill-posed without additional regularisation (risk aversion or spread cost), consistent with the observation that permanent-impact models require explicit position risk to generate finite optimal trades [AC01].

### 8.3 Comparison table

| Kernel $K$ | $\hat{K}_+^{-1}$ (causal factor) | Optimal trade (clean signal) |
|---|---|---|
| Exponential $\lambda^{\vert n\vert}$ | $(1-\lambda z^{-1})/\sqrt{1-\lambda^2}$ | $c(\rho,\lambda)\,(f_t - \lambda f_{t-1})$ |
| White (temporary) $\delta_0$ | $1$ | $f_t$ |
| Power-law $\vert\tau\vert^{-\beta}$ (cont., OU signal) | $\mathcal{D}^{(1-\beta)/2}_+$ | $\kappa^{(1-\beta)/2}\,\mathcal{D}^{(1-\beta)/2}_+\,f_t$ |
| Fractional differencing $(1-L)^\alpha$ (disc., AR(1)) | $\Delta^\alpha_+$ | $(1-\rho)^\alpha\,\Delta^\alpha_+\,f_t$ |
| Flat (permanent) $1$ | $(-\partial_t)^{1/2}$ | ill-posed (regularisation needed) |

*Table 1: Causal factor $\hat{K}_+^{-1}$ and resulting optimal policy for common impact kernels. The constant $c$ in each case depends on the signal autocorrelation and kernel parameters. Permanent impact row is marked as requiring regularisation.*

---

## 9. Related Work

**Gârleanu & Pedersen [GP13]** derive a closed-form optimal policy for a setting with **quadratic instantaneous transaction costs** (not a transient impact propagator) and OU return-predicting factors with possibly different mean-reversion speeds.  Their "aim-and-trade" rule — hold a portfolio that trades partially toward a current Markowitz-style target — is conceptually parallel to our (12) but is *not nested* in our framework: our cost is quadratic in a convolution of trades (transient impact), and our (12) has no explicit position-risk term.  A precise correspondence would require adding a position-risk penalty and taking a temporary-cost limit ($\lambda \to 0$ with the impact rescaled), which we do not pursue here.  We view GP13 as the conceptual antecedent for combining a quadratic trading penalty with a mean-reverting alpha signal, but the two problems live in different cost geometries.

**Gatheral [Gat10]** establishes the connection between positive-definiteness of $K$ (as a quadratic form on trade sequences) and absence of dynamic arbitrage, and characterises the admissible class of power-law kernels via Bochner's theorem.  Our cost norm $\|\cdot\|_K$ is precisely his "trading cost" functional.

**Bouchaud, Gefen, Potters & Wyart [BGPW04]** introduce the propagator model and show empirically that $G(t) \sim t^{-\beta}$ fits Paris Bourse data well.  Their model is the empirical foundation of our general kernel assumption.

**Lehalle & Neuman [LN19]** incorporate a Markovian signal into a finite-horizon liquidation problem with **linear transient impact with exponential resilience** (Obizhaeva–Wang style), plus linear temporary impact.  They derive existence and uniqueness of an optimal strategy and obtain an explicit form for OU signal + exponential resilience via an ODE/Riccati system.  Our §5 result (12) is the stationary, infinite-horizon analogue, derived via a frequency-domain projection rather than dynamic programming.  The *singular control* extension (with block trades at the boundary) is developed in **Neuman & Voß (2022)** and is closer to what was earlier described as a "singular strategy" in this literature.

**Abi Jaber, Neuman & Tuschmann [AJN24]** treat the **finite-horizon matrix-valued cross-impact** extension of the propagator problem and solve via operator resolvents.  Our stationary scalar setting is conceptually parallel but not literally nested in their framework — they work with terminal-liquidation constraints, we work in an infinite-horizon ergodic regime — though the scalar single-asset Volterra subcase of their machinery overlaps the operator content of our §4.

**Forde, Sánchez-Betancourt et al. [FSB+]** characterise the optimal signal-adaptive liquidation strategy for a Gaussian (OU or fractional Brownian motion) signal under **power-law resilience and zero temporary impact**, with the optimal selling speed expressed as a Gaussian Volterra process. This is the closest direct precedent to our §6 (power-law kernel → causal fractional derivative); their derivation is technically sharper than ours and handles the finite-horizon case, while our stationary frequency-domain argument is comparatively elementary.

**The noisy-signal observation model (§7)** is standard in control theory (certainty equivalence, Wiener 1949, Kalman 1960) but does not appear to have been explicitly connected to the Wiener–Hopf trading framework in the form of equation (20).  The Wiener filter in financial contexts is mentioned in passing in [GP13, §IV.C] and in some practitioner literature, but typically as a heuristic rather than as a derivation from first principles.

---

## 10. Limitations and Open Questions

1. **Scalar, single-asset model.** The derivation is one-dimensional.  Cross-impact (matrix-valued $K$) complicates the Wiener–Hopf factorisation substantially, requiring operator-valued spectral factorisation [AJN24].

2. **Linearity and Gaussianity.** The separation principle (§7.3) holds exactly only under Gaussian linearity.  Non-linear signals, heavy-tailed noise, or model uncertainty would require robust or non-linear extensions.

3. **Stationarity.** The infinite-horizon stationary formulation sidesteps terminal conditions.  For finite-horizon or inventory-constrained problems, the Wiener–Hopf argument must be replaced by a time-varying Riccati or Fredholm equation.

4. **Risk aversion.** The objective maximises expected gain minus expected impact cost with no explicit risk (variance) penalty on P&L.  Including a risk term modifies the signal target but preserves the factored structure [GP13].

5. **Scalar collapse for general Markov signals.** The Markov-closure argument of §5.5 shows that the anticausal projection reduces to a scalar (equation 12c) whenever the signal is AR(1) or, more generally, Ornstein–Uhlenbeck, and admits a finite-dimensional extension for AR($p$) or finite-state Markov signals. For *non*-Markov signals — fractional Brownian, long-memory ARFIMA with the signal driven by fBm rather than the kernel, hidden-Markov-switching regimes — the closure fails and the optimal policy requires the operator-resolvent machinery of Abi Jaber–Neuman [AJN22; AJN24].

6. **Empirical validation.** All results in this note are theoretical.  Empirical tests—comparing the theoretically optimal policy against benchmarks using real signal and impact data—are a natural next step. *(Proposed experiment: simulate AR(1) signal + exponential-kernel impact, measure Sharpe improvement of policy (12) over naive $x_t = f_t$ as a function of $\lambda$ and $\rho$.)*

7. **Connection to Gârleanu–Pedersen limit.** The conceptual parallel to GP "aim-and-trade" is discussed in §9, but a formal nesting would require introducing a position-risk term and a temporary-cost limit, which we do not pursue.  We make no claim of an exact correspondence.

---

## 11. Conclusion

We have shown that the problem of stationary optimal trading with persistent impact and a predictive signal reduces cleanly to a pair of dual norms—one on trades, one on signals—connected by the Legendre–Fenchel transform of the quadratic cost functional.  The causal optimal policy is computed by Wiener–Hopf factorisation of the impact kernel.

For the empirically relevant AR(1) signal and exponential kernel case, the anticausal Wiener–Hopf factor acts on the signal by a simple scalar multiplication—a constant that depends on the product $\lambda\rho$ of kernel decay and signal autocorrelation.  The remaining causal factor implements a first-order backward difference of the signal: the optimal trade is the *kernel innovation* of the predictor.  For power-law kernels the causal factor becomes a causal fractional derivative of order $(1-\beta)/2$, directly encoding the memory depth of the impact.

When the predictor is observed with noise, the optimal policy separates cleanly: a causal Wiener filter first extracts the best estimate of the true signal, and the kernel-innovation operator is then applied to the filtered output.  Intuitively, the Wiener filter removes the noise before the trade calculation, preventing the agent from paying impact costs to chase predictors that are dominated by noise.

The unifying theme is a *separation of timescales*: the signal geometry (predictability, autocorrelation) and the impact geometry (kernel, memory) jointly determine the optimal trade through a product structure that separates estimation (Wiener filter) from execution (kernel innovation).

---


## Appendix A. Definitions

This appendix collects the formal objects used implicitly throughout the paper. Conventions: time index $t \in \mathbb{Z}$ in discrete sections, $t \in \mathbb{R}$ in continuous sections (§6.2, §6.3, §8.2); the unit circle is $\mathbb{T} = \{z \in \mathbb{C} : |z|=1\}$; for a real-valued time series $x$, we write $\hat x(z) = \sum_t x_t z^{-t}$ for the bilateral $z$-transform when it converges, and $\hat x(\omega) = \hat x(e^{i\omega})$ on $\mathbb{T}$.

**Definition A.1 (Signal and trade-rate processes).** A *signal* $f = (f_t)_{t\in\mathbb{Z}}$ is a real, zero-mean, wide-sense-stationary (WSS) process with absolutely summable autocovariance $\gamma_f(k) = \mathbb{E}[f_t f_{t+k}]$, equivalently a continuous positive spectral density $S_f$ on $\mathbb{T}$. A *trade-rate process* $x = (x_t)_{t\in\mathbb{Z}}$ is any real process adapted to a given filtration $\{\mathcal F_t\}$; the *position* is $q_t = \sum_{s \le t} x_s$. The *causal admissible class* $\mathcal A^c$ consists of WSS $x$ of the form $x_t = (H * f)_t$ with $H : \mathbb{Z}_{\ge 0} \to \mathbb{R}$ satisfying $\sum_k H(k)^2 S_f$-essentially bounded, so that $\mathbb{E}[x_t^2] < \infty$.

**Definition A.2 (Admissible impact kernel).** An *admissible symmetric impact kernel* is a real function $K : \mathbb{Z} \to \mathbb{R}$ with $K(n) = K(-n)$, $\sum_n |K(n)| < \infty$ or — for the power-law case — $K$ a positive-definite tempered distribution, and Fourier transform $\hat K(\omega) > 0$ for all $\omega \in \mathbb{T}$ (resp. for all $\omega \in \mathbb{R}$). The continuous-time analogue $K : \mathbb{R} \to \mathbb{R}$ has the same definition with $\mathbb{R}$ replacing $\mathbb{Z}$ and Fourier transform on $\mathbb{R}$. The *one-sided* kernel is $G(n) := K(n)$ for $n \ge 0$ (§2.1).

**Definition A.3 (Cost inner product and cost norm).** For $x, x' \in \ell^2(\mathbb{Z})$,
$$
\langle x, x'\rangle_K \;:=\; \sum_{s,t} x_t\, K(t-s)\, x'_s \;=\; \int_{-\pi}^{\pi} \hat x(\omega)^* \hat K(\omega)\, \hat x'(\omega)\,\frac{d\omega}{2\pi},
$$
with associated norm $\|x\|_K^2 := \langle x,x\rangle_K$. Positivity of $\hat K$ (Definition A.2) makes $\langle\cdot,\cdot\rangle_K$ an inner product on $\ell^2$ (cf. Theorem B.1).

**Definition A.4 (Hardy spaces and causal/anticausal projections).** Let $L^2(\mathbb{T})$ be square-integrable functions on the unit circle with the Plancherel inner product $\langle f, g\rangle = \int f^* g\, d\omega/(2\pi)$. The *causal Hardy space* $H^2_+(\mathbb{T})$ is the closed subspace of $L^2(\mathbb{T})$ spanned by $\{e^{-ik\omega} : k \ge 0\}$ — equivalently, the boundary values of functions analytic on $\{|z| > 1\}$ and decaying at infinity. The *anticausal* Hardy space $H^2_-(\mathbb{T})$ is the orthogonal complement, spanned by $\{e^{ik\omega} : k \ge 1\}$. The *causal projection* $[\cdot]_+ : L^2(\mathbb{T}) \to H^2_+$ and *anticausal projection* $[\cdot]_-$ are the orthogonal projections; in $z$-transform terms, $[\sum_k c_k z^{-k}]_+ = \sum_{k \ge 0} c_k z^{-k}$ and $[\cdot]_- = I - [\cdot]_+$.

**Definition A.5 (Outer spectral factor).** An admissible spectral density $\hat K$ (Definition A.2) satisfies the *Szegő / Paley–Wiener condition*
$$
\int_{-\pi}^{\pi} \log \hat K(\omega)\,\frac{d\omega}{2\pi} \;>\; -\infty. \tag{A.1}
$$
Under (A.1) there exists a unique (up to a unimodular constant) *outer function* $\hat K_+ \in H^2_+$ with $\hat K(\omega) = |\hat K_+(\omega)|^2 = \hat K_+(\omega)\,\hat K_-(\omega)$, where $\hat K_-(\omega) := \overline{\hat K_+(\omega)} = \hat K_+(\omega^{-1})$ is the anticausal factor (see Theorem B.4). Both $\hat K_+$ and $\hat K_+^{-1}$ lie in $H^2_+$ in the bounded case; in the power-law case the same factorisation is defined via the upper-half-plane analogue with $\hat K_+(\omega) \propto (i\omega)^{(\beta-1)/2}$.

**Definition A.6 (Causal Wiener filter).** Given an observation $\tilde f_t = f_t + \eta_t$ with $\eta \perp f$ both WSS, the *causal Wiener filter* is the unique $W \in H^2_+$ minimising $\mathbb{E}[(f_t - (W*\tilde f)_t)^2]$. Its closed form is
$$
\hat W(z) \;=\; \frac{1}{\hat\phi^+(z)}\Bigg[\frac{S_f(z)}{\hat\phi^-(z)}\Bigg]_+,
$$
where $S_{\tilde f} = \hat\phi^+\hat\phi^-$ is the spectral factorisation of the observed spectrum (Wiener 1949).

**Definition A.7 (Marchaud anticausal fractional derivative).** For $\alpha \in (0, 1)$ and $f$ a function on $\mathbb{R}$ with sufficient regularity (Hölder $\beta > \alpha$ suffices), the *anticausal Marchaud fractional derivative* of order $\alpha$ is
$$
(\mathcal D^\alpha_- f)(t) \;:=\; \frac{1}{\Gamma(-\alpha)}\int_0^\infty s^{-\alpha-1}\,[f(t+s) - f(t)]\,ds, \tag{A.2}
$$
and the *causal* Marchaud derivative $\mathcal D^\alpha_+ f$ is given by $s \mapsto -s$ in (A.2). The regularising subtraction $-f(t)$ makes the integral converge despite the non-integrability of $s^{-\alpha-1}$ at $s=0$ (Samko–Kilbas–Marichev 1993, §5).

**Definition A.8 (Discrete fractional difference operator).** With $L$ the backward shift $(Lf)_t = f_{t-1}$, the *causal fractional difference of order $\alpha \in \mathbb{R}$* is
$$
\Delta^\alpha_+ \;:=\; (1 - L)^\alpha \;=\; \sum_{m \ge 0} \binom{\alpha}{m}(-L)^m,
\qquad \binom{\alpha}{m} \;=\; \frac{\alpha(\alpha-1)\cdots(\alpha-m+1)}{m!}, \tag{A.3}
$$
with the generalised binomial coefficients. The *anticausal* version $\Delta^\alpha_- = (1 - L^{-1})^\alpha$ replaces $L$ by $L^{-1}$. Convergence in $\ell^2$ on stationary inputs holds for $\alpha > -1/2$ ([GJ80, #16]; [Hosking81, #17]).

**Definition A.9 (Kernel innovation).** For an admissible kernel $K$ with outer factor $K_+$ (Definition A.5) and signal $f$, the *kernel innovation of $f$ with respect to $K$* is
$$
\iota^K_t \;:=\; (K_+^{-1} * f)_t.
$$
For $K(n) = \lambda^{|n|}$ this is $(f_t - \lambda f_{t-1})/\sqrt{1-\lambda^2}$ (eq. (12)); for the continuous-time power-law kernel it is the causal Marchaud derivative $\mathcal D^{(1-\beta)/2}_+ f$ (eq. (14)); for the discrete fractional-differencing kernel it is $\Delta^\alpha_+ f$ (Table 1).

---

## Appendix B. Proofs

Each theorem corresponds to a load-bearing claim in the main text; the cross-reference is given in the statement.

### B.1 Positive-definiteness ⇔ No dynamic arbitrage (§2.4)

**Theorem B.1.** *Let $K$ be a real, symmetric kernel on $\mathbb{Z}$ with absolutely summable autocovariance, and let $\hat K$ denote its Fourier transform on $\mathbb{T}$. The following are equivalent:*

1. *The cost form $\mathcal C(x) = \tfrac{1}{2}\sum_{s,t} x_s K(t-s) x_t$ is strictly positive on every finite-support sequence $x \ne 0$.*
2. $\hat K(\omega) > 0$ for almost every $\omega \in \mathbb{T}$.
3. *No finite-support round-trip $x$ (i.e. $\sum_t x_t = 0$, $x_t = 0$ outside a finite window) has $\mathcal C(x) \le 0$; equivalently, no manipulation strategy generates a positive expected price increment with negative cost (Gatheral [Gat10]).*

*Proof.* (1) $\Leftrightarrow$ (2) is Bochner's theorem. By the Parseval–Plancherel identity, for any finite-support $x$ with $z$-transform $\hat x \in L^2(\mathbb{T})$,
$$
2\,\mathcal C(x) \;=\; \langle x, K*x\rangle \;=\; \int_{-\pi}^{\pi} |\hat x(\omega)|^2\, \hat K(\omega)\,\frac{d\omega}{2\pi}. \tag{B.1}
$$
If $\hat K > 0$ a.e., (B.1) shows $\mathcal C(x) > 0$ for $x \ne 0$ (since $\hat x \not\equiv 0$). Conversely, if $\hat K(\omega_0) < 0$ on a positive-measure set, choose a band-limited $x$ with $|\hat x|$ supported there; then (B.1) gives $\mathcal C(x) < 0$, contradicting positivity.

(2) $\Leftrightarrow$ (3) is Theorem 1 of Gatheral [Gat10]: a round-trip strategy has expected revenue $-\mathcal C(x)$ (the negative of the impact cost), so a profitable round-trip exists iff $\mathcal C(x) < 0$ for some $x$ with $\sum_t x_t = 0$, which by (B.1) is iff $\hat K$ takes negative values. $\square$

### B.2 Legendre–Fenchel duality (§3.2, eq. (2))

**Theorem B.2.** *Let $\phi(x) = \tfrac{1}{2}\|x\|_K^2$ with $K$ admissible (Def. A.2). Then the convex conjugate $\phi^*(f) = \sup_x[\langle f,x\rangle - \phi(x)]$ equals $\tfrac{1}{2}\|f\|_{K^{-1}}^2$, with the supremum attained at $x^\star = K^{-1} * f$.*

*Proof.* Differentiate the concave functional $x \mapsto \langle f, x\rangle - \tfrac{1}{2}\langle x, K*x\rangle$: the FOC reads $f - K*x = 0$, so $x^\star = K^{-1}*f$ (well-defined since $\hat K > 0$ a.e., so $\hat K^{-1} \in L^\infty_{\text{loc}}$). Substituting,
$$
\phi^*(f) \;=\; \langle f, x^\star\rangle - \tfrac{1}{2}\langle x^\star, K*x^\star\rangle \;=\; \langle f, K^{-1}*f\rangle - \tfrac{1}{2}\langle K^{-1}*f, f\rangle \;=\; \tfrac{1}{2}\|f\|_{K^{-1}}^2. \quad\square
$$

### B.3 Wiener–Hopf first-order condition (§4.1, eqs. (4)–(6))

**Theorem B.3.** *Let $K$ be admissible. The functional $\mathcal J(x) = \langle f, x\rangle - \tfrac{1}{2}\langle x, K*x\rangle$ has a unique maximiser on the causal subspace $\mathcal A^c$. The maximiser $x^*$ is characterised by*
$$
\big[K*x^* - f\big]_+ \;=\; 0, \tag{B.2}
$$
*and is given in $z$-transform form by*
$$
\hat x^*(z) \;=\; \hat K_+^{-1}(z)\,\bigl[\hat f(z) / \hat K_-(z)\bigr]_+. \tag{B.3}
$$

*Proof.* Causal admissible $x$ form a closed convex subspace of $L^2(\mathbb{T})$ in $z$-transform (Def. A.4). Strict concavity of $\mathcal J$ follows from Theorem B.1, giving uniqueness. The FOC requires the Gâteaux derivative $D\mathcal J(x)[h] = \langle f - K*x, h\rangle$ to vanish for all causal $h$, i.e. $f - K*x \perp H^2_+$, equivalently $[K*x - f]_+ = 0$.

Factor $\hat K = \hat K_+ \hat K_-$ (Theorem B.4). Set $\hat y(z) := \hat K_+(z)\hat x(z)$, which lies in $H^2_+$ iff $\hat x$ does (since $\hat K_+$ is outer). Then $\hat K(z)\hat x(z) = \hat K_-(z)\hat y(z)$, and (B.2) becomes
$$
[\hat K_-(z)\hat y(z) - \hat f(z)]_+ = 0
\;\Longleftrightarrow\; \hat y(z) - [\hat f(z)/\hat K_-(z)]_+ \in H^2_-,
$$
using that multiplication by anticausal $\hat K_-$ preserves $H^2_-$. Since $\hat y \in H^2_+$, the difference must vanish: $\hat y(z) = [\hat f(z)/\hat K_-(z)]_+$, giving (B.3). $\square$

### B.4 Spectral factorisation (§4.2)

**Theorem B.4 (Szegő factorisation).** *Let $\hat K \in L^1(\mathbb{T})$ with $\hat K \ge 0$ and the Paley–Wiener / Szegő condition $\int \log \hat K\,d\omega/(2\pi) > -\infty$ (eq. (A.1)). Then there exists a unique outer function $\hat K_+ \in H^2_+$ with $\hat K_+(\infty) > 0$ and $|\hat K_+(\omega)|^2 = \hat K(\omega)$ a.e. Setting $\hat K_-(\omega) := \overline{\hat K_+(\omega)}$ gives $\hat K = \hat K_+\hat K_-$.*

*Proof.* Standard; we record the construction. Define
$$
\hat K_+(z) \;:=\; \exp\!\Bigg(\tfrac{1}{2}\int_{-\pi}^{\pi}\log\hat K(\theta)\,\frac{e^{i\theta}+z^{-1}}{e^{i\theta}-z^{-1}}\,\frac{d\theta}{2\pi}\Bigg), \qquad |z| > 1, \tag{B.4}
$$
which is the exponential of the *Schwarz integral* of $\tfrac{1}{2}\log\hat K$. By construction $\hat K_+$ is analytic and zero-free on $\{|z|>1\}$; its non-tangential boundary values exist a.e. and satisfy $|\hat K_+(\omega)|^2 = \exp(\log\hat K(\omega)) = \hat K(\omega)$. Outer functions are characterised by maximising $|\hat K_+(\infty)| = \exp(\int \tfrac{1}{2}\log\hat K\,d\omega/(2\pi))$ among $H^2_+$ functions with the same modulus on $\mathbb{T}$ (Hoffman, *Banach Spaces of Analytic Functions*, Ch. 5); uniqueness up to a unimodular constant follows. The normalisation $\hat K_+(\infty) > 0$ fixes that constant.

For the power-law continuous-time case $\hat K(\omega) = c|\omega|^{\beta-1}$, the analogous outer function on the upper half-plane is $\hat K_+(\omega) = c^{1/2}(i\omega)^{(\beta-1)/2}$ with the principal branch; this is the standard fractional-integration symbol (Samko–Kilbas–Marichev 1993, §7), and recovers (13). $\square$

*Remark.* The Szegő condition (A.1) is satisfied by every kernel considered in the paper: the exponential kernel $\hat K(\omega) = (1-\lambda^2)/|1-\lambda e^{-i\omega}|^2$ is bounded away from $0$, hence $\log \hat K \in L^\infty(\mathbb{T})$; the power-law kernel has only a logarithmic singularity in $\log \hat K$ at $\omega = 0$, which is integrable.

### B.5 AR(1) Markov-closure identity (§5.5, eq. (12c))

**Theorem B.5.** *Let $f$ be a WSS AR(1) process with $f_t = \rho f_{t-1} + \epsilon_t$, $|\rho| < 1$, $\epsilon_t$ i.i.d. with $\mathbb{E}\epsilon_t^2 = \sigma^2 < \infty$. Let $\hat K_-^{-1}(z) = \sum_{m \ge 0} a_m z^m$ converge for $|z| \le |\rho|^{-1}$. Then the causal projection of the anticausal filter satisfies*
$$
[K_-^{-1} * f]_+(t) \;=\; \hat K_-^{-1}(\rho)\, f_t, \quad\text{a.s.} \tag{B.5}
$$
*If $f$ is in addition Gaussian, the equality holds in $L^2(\mathbb{P})$ with $[\cdot]_+$ the orthogonal projection onto the $\sigma$-algebra $\mathcal F_t^f$; for general WSS $f$ it holds with $[\cdot]_+$ the linear projection onto $\overline{\mathrm{span}}\{f_s : s \le t\}$.*

*Proof.* The action of $K_-^{-1}$ as an anticausal sum (eq. (12a)) is $(K_-^{-1}*f)_t = \sum_{m \ge 0} a_m f_{t+m}$, which converges in $L^2$ when $\sum_m a_m^2 \rho^{2m} < \infty$ — guaranteed by the convergence assumption.

For Gaussian $f$, the deterministic causal projection $[\cdot]_+$ on $z$-transforms coincides with conditional expectation onto $\mathcal F_t^f$ (Doob, *Stochastic Processes*, Ch. XII §5; this is the standard equivalence of orthogonal projection in $L^2$ to conditional expectation for jointly Gaussian families). For general WSS $f$, it equals the wide-sense linear projection (Hannan, *Multiple Time Series*, Ch. III). In either case, by linearity and dominated convergence,
$$
[K_-^{-1}*f]_+(t) \;=\; \sum_{m \ge 0} a_m\, \mathbb{E}[f_{t+m}\mid \mathcal F_t^f]. \tag{B.6}
$$
The AR(1) Markov property gives $\mathbb{E}[f_{t+m}\mid \mathcal F_t^f] = \rho^m f_t$ (iterate the recursion: $f_{t+1} = \rho f_t + \epsilon_{t+1}$ with $\epsilon_{t+1} \perp \mathcal F_t^f$). Substituting into (B.6),
$$
[K_-^{-1}*f]_+(t) \;=\; \Big(\sum_{m \ge 0} a_m \rho^m\Big)\,f_t \;=\; \hat K_-^{-1}(\rho)\,f_t. \quad\square
$$

*Verification of (10).* For the exponential kernel, $\hat K_-^{-1}(z) = (1-\lambda z)/\sqrt{1-\lambda^2}$, so $\hat K_-^{-1}(\rho) = (1-\lambda\rho)/\sqrt{1-\lambda^2}$, reproducing the §5.3 partial-fraction result.

### B.6 Frullani / Γ-identity for OU × power-law (§6.3, eq. (15b))

**Theorem B.6.** *For $\alpha \in (0,1)$ and $\kappa > 0$,*
$$
\int_0^\infty s^{-\alpha-1}\,(e^{-\kappa s} - 1)\,ds \;=\; \Gamma(-\alpha)\,\kappa^\alpha. \tag{B.7}
$$
*Consequently, if $f$ is an OU process with mean-reversion rate $\kappa$ ($\mathbb{E}[f(t+s)|\mathcal F_t] = e^{-\kappa s}f(t)$), the Marchaud anticausal derivative $\mathcal D^\alpha_-$ (Def. A.7) satisfies $\mathbb{E}[(\mathcal D^\alpha_- f)(t)\mid \mathcal F_t] = \kappa^\alpha f(t)$.*

*Proof.* Substitute $u = \kappa s$:
$$
\int_0^\infty s^{-\alpha-1}(e^{-\kappa s}-1)\,ds \;=\; \kappa^\alpha \int_0^\infty u^{-\alpha-1}(e^{-u}-1)\,du.
$$
For the right-hand integral, integrate by parts with $dv = (e^{-u}-1)\,du$ and $w = u^{-\alpha-1}$; both boundary terms vanish for $\alpha \in (0,1)$ (the integrand $u^{-\alpha}(e^{-u}-1)$ is $O(u^{1-\alpha}) \to 0$ at $0$ and $O(u^{-\alpha}e^{-u}) \to 0$ at $\infty$), giving
$$
\int_0^\infty u^{-\alpha-1}(e^{-u}-1)\,du \;=\; -\frac{1}{\alpha}\int_0^\infty u^{-\alpha}\,e^{-u}\,du \;\cdot\;(-1) \cdot (-1) \;=\; -\frac{1}{\alpha}\,\Gamma(1-\alpha),
$$
where $\int_0^\infty u^{-\alpha}e^{-u}\,du = \Gamma(1-\alpha)$ by the definition of the Gamma function. The functional equation $\Gamma(1-\alpha) = -\alpha\,\Gamma(-\alpha)$ then yields
$$
\int_0^\infty u^{-\alpha-1}(e^{-u}-1)\,du \;=\; -\frac{1}{\alpha}\cdot(-\alpha\Gamma(-\alpha)) \;=\; \Gamma(-\alpha),
$$
which proves (B.7). The OU consequence follows by linearity of conditional expectation applied to (A.2) using $\mathbb{E}[f(t+s)-f(t)\mid\mathcal F_t] = (e^{-\kappa s}-1)f(t)$. $\square$

*Numerical sanity.* The identity (B.7) is verified by `experiments/markov_closure_check.py`. The script's output `experiments/results/markov_closure_check.out` records the ratio of a crude trapezoidal estimate of the LHS to $\Gamma(-\alpha)$; mid-range $\alpha \in [0.25, 0.75]$ agrees to within 0.5%, while the endpoints lose precision as expected for a non-adaptive quadrature applied to a singular integrand. The identity itself is exact.

### B.7 ARFIMA / generalised binomial closure (§6.3, eq. (15c))

**Theorem B.7.** *Let $\Delta^\alpha_- = (1 - L^{-1})^\alpha$ (Def. A.8, anticausal version) and $f$ AR(1) with parameter $\rho$, $|\rho|<1$. Then*
$$
[\Delta^\alpha_- f]_+(t) \;=\; (1-\rho)^\alpha\, f_t. \tag{B.8}
$$

*Proof.* The anticausal fractional difference has $z$-transform $\hat{\Delta}^\alpha_-(z) = (1-z)^\alpha$, expanding to $\sum_{m\ge 0}\binom{\alpha}{m}(-z)^m$ (the generalised binomial series; [Hosking81, #17] Theorem 1; [GJ80, #16]). Setting $a_m = \binom{\alpha}{m}(-1)^m$ and applying Theorem B.5,
$$
[\Delta^\alpha_- f]_+(t) \;=\; \Big(\sum_{m\ge 0}\binom{\alpha}{m}(-\rho)^m\Big) f_t \;=\; (1-\rho)^\alpha\, f_t,
$$
where the final equality is the generalised binomial theorem evaluated at $-\rho$ for $|\rho| < 1$. The series converges absolutely for $|\rho| < 1$ and all $\alpha \in \mathbb{R}$; for $\alpha \in (-1/2, 1/2)$ the operator preserves WSS $\ell^2$ inputs ([Hosking81, #17] §2). $\square$

*Numerical sanity.* The series identity $\sum_{m\ge 0}\binom{\alpha}{m}(-\rho)^m = (1-\rho)^\alpha$ is verified to $\sim 7$ decimal places for $\alpha \in \{0.25, 0.5, 0.75\}$ and $\rho \in \{0.3, 0.7, 0.95\}$ in `experiments/markov_closure_check.py` (output file `experiments/results/markov_closure_check.out`).

### B.8 Separation principle (§7.3)

**Theorem B.8 (Denoise-then-trade).** *Let $f, \eta$ be independent, jointly Gaussian, zero-mean, WSS processes; let $\tilde f_t = f_t + \eta_t$, and let the agent observe the filtration $\tilde{\mathcal F}_t = \sigma(\tilde f_s : s \le t)$. Assume $K$ is admissible (Def. A.2). Then the maximiser of $\mathcal J(x) = \mathbb{E}[f_t x_t - \tfrac{1}{2}x_t(K*x)_t]$ over $\tilde{\mathcal F}$-causal WSS $x$ is*
$$
\hat x^*(z) \;=\; \hat K_+^{-1}(z)\,\bigl[\hat f^W(z)/\hat K_-(z)\bigr]_+, \tag{B.9}
$$
*where $f^W_t := \mathbb{E}[f_t \mid \tilde{\mathcal F}_t]$ is the causal Wiener filter output (Def. A.6).*

*Proof.* Decompose $\mathcal J$ by tower property: for any $\tilde{\mathcal F}$-causal $x$,
$$
\mathbb{E}[f_t x_t] = \mathbb{E}\big[\mathbb{E}[f_t\mid \tilde{\mathcal F}_t]\,x_t\big] = \mathbb{E}[f^W_t\, x_t],
$$
using $x_t \in \tilde{\mathcal F}_t$. The cost term $\mathbb{E}[x_t(K*x)_t]$ depends only on $x$. Therefore
$$
\mathcal J(x) \;=\; \mathbb{E}[f^W_t x_t] - \tfrac{1}{2}\mathbb{E}[x_t(K*x)_t], \tag{B.10}
$$
which is **the clean-signal problem with $f$ replaced by $f^W$**, optimised over $\tilde{\mathcal F}$-causal $x$. Since $f^W$ is itself $\tilde{\mathcal F}$-causal (causal Wiener filter, Def. A.6), the causal-functions-of-$f^W$ class is identical to causal-functions-of-$\tilde f$ that respect $\tilde{\mathcal F}_t$-measurability. Applying Theorem B.3 with $f \leftarrow f^W$ gives (B.9). Joint Gaussianity ensures $\mathbb{E}[f_t\mid\tilde{\mathcal F}_t]$ is the linear Wiener filter, justifying the use of (B.9) inside the linear Wiener–Hopf machinery. $\square$

*Remark (certainty equivalence).* Outside the Gaussian regime, $f^W_t = \mathbb{E}[f_t\mid\tilde{\mathcal F}_t]$ need not be a linear functional of $\tilde f$; the wide-sense linear best estimate still satisfies (B.10) with $f^W$ replaced by the linear projection, yielding the linear-optimal policy (21) of §7.4. This is the *certainty-equivalence* version of the separation principle (Wiener 1949; Kalman 1960; cf. §9).

---

### Cross-reference index

| Theorem | Statement in main text | Page/section |
|---|---|---|
| B.1 | PD ⇔ no dyn-arb | §2.4 |
| B.2 | $\phi^*(f) = \tfrac12 \|f\|_{K^{-1}}^2$ | §3.2, eq. (2)–(3) |
| B.3 | Wiener–Hopf optimum | §4.1, eqs. (4)–(6) |
| B.4 | Szegő factorisation | §4.2 |
| B.5 | Markov-closure scalar identity | §5.5, eq. (12c) |
| B.6 | $\Gamma(-\alpha)\kappa^\alpha$ identity | §6.3, eq. (15b) |
| B.7 | $(1-\rho)^\alpha$ identity | §6.3, eq. (15c) |
| B.8 | Denoise-then-trade | §7.3 |

---


## Sources

1. **Gârleanu & Pedersen (2013)** – "Dynamic Trading with Predictable Returns and Transaction Costs." *Journal of Finance*, 68(6):2309–2340.  
   https://doi.org/10.1111/jofi.12080  
   Preprint: http://docs.lhpedersen.com/DynamicTrading.pdf

2. **Gatheral (2010)** – "No-Dynamic-Arbitrage and Market Impact." *Quantitative Finance*, 10(7):749–759.  
   https://doi.org/10.1080/14697680903373692  
   SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1292353

3. **Bouchaud, Gefen, Potters & Wyart (2004)** – "Fluctuations and Response in Financial Markets: The Subtle Nature of 'Random' Price Changes." *Quantitative Finance*, 4(2):176–190.  
   https://iopscience.iop.org/article/10.1088/1469-7688/4/2/007  
   arXiv: https://arxiv.org/abs/cond-mat/0307332

4. **Lehalle & Neuman (2019)** – "Incorporating Signals into Optimal Trading." *Finance and Stochastics*, 23(2):275–311.  
   https://doi.org/10.1007/s00780-019-00382-7  
   arXiv: https://arxiv.org/abs/1704.00847

5. **Abi Jaber, Neuman & Tuschmann (2024)** – "Optimal Portfolio Choice with Cross-Impact Propagators."  
   arXiv: https://arxiv.org/abs/2403.10273

6. **Abi Jaber & Neuman (2022)** [AN22] – "Optimal Liquidation with Signals: The General Propagator Case."  
   arXiv: https://arxiv.org/abs/2211.00447

7. **Almgren & Chriss (2001)** – "Optimal Execution of Portfolio Transactions." *Journal of Risk*, 3:5–39. [AC01]  
   http://www.risk.net/journal-of-risk/1506832/optimal-execution-portfolio-transactions

8. **Gatheral, Schied & Slynko (2012)** [GSS12] – "Transient Linear Price Impact and Fredholm Integral Equations." *Mathematical Finance* 22(3):445–474.  
   DOI: https://doi.org/10.1111/j.1467-9965.2011.00478.x  
   SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1531466

9. **Alfonsi, Schied & Slynko (2012)** – "Order Book Resilience, Price Manipulation, and the Positive Portfolio Problem." *SIAM Journal on Financial Mathematics* 3(1):511–533.

10. **Obizhaeva & Wang (2013)** – "Optimal Trading Strategy and Supply/Demand Dynamics." *Journal of Financial Markets* 16(1):1–32.

11. **Neuman & Voß (2022)** – "Optimal Signal-Adaptive Trading with Temporary and Transient Price Impact."  
    arXiv: https://arxiv.org/abs/2002.09549

12. **Forde, Sánchez-Betancourt et al.** [FSB+] – "Optimal Trade Execution for Gaussian Signals with Power-Law Resilience."  
    Oxford ORA: https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26

13. **Bouchaud, Bonart, Donier & Gould (2018)** – *Trades, Quotes and Prices: Financial Markets Under the Microscope.* Cambridge University Press.

14. **Wiener (1949)** – *Extrapolation, Interpolation and Smoothing of Stationary Time Series.* MIT Press. [Wiener filter / Wiener–Hopf theory]

15. **Samko, Kilbas & Marichev (1993)** – *Fractional Integrals and Derivatives: Theory and Applications.* Gordon and Breach. [Fractional derivatives and causal operators; Marchaud form used in §6.3]

16. **Granger & Joyeux (1980)** – "An Introduction to Long-Memory Time Series Models and Fractional Differencing." *J. Time Series Analysis* 1(1):15–29. [Discrete fractional differencing $(1-L)^\alpha$ used in §6.3]

17. **Hosking (1981)** – "Fractional Differencing." *Biometrika* 68(1):165–176. [ARFIMA / discrete fractional difference]

18. **Nuzman & Poor (2000)** – "Linear Estimation of Self-Similar Processes via Lamperti's Transformation." *J. Applied Probability* 37(2):429–452. [Prediction formula for fBm; cited in §5.5 as the regime where Markov closure fails]

---

*End of draft. File: `papers/noisy-signal-impact-trading.md`.*
