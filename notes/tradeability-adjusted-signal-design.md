# Tradeability-Adjusted Signal Design

*Research note. Follow-up direction from the fractional-derivative optimal-execution paper.*

## 1. The objective mismatch

Standard signal-development pipelines optimize predictive quality:

- **Regression loss**: $\mathbb E[(r_{t+h} - \hat\alpha_t)^2]$.
- **Information coefficient**: $\text{IC} = \text{corr}(\hat\alpha_t, r_{t+h})$.
- **Paper Sharpe**: $\text{Sharpe}(\hat\alpha \cdot r)$ with no cost model.

None of these see the impact operator $C$. Two signals with identical IC can have vastly different *realized* value because the mapping from signal to trading rate goes through the fractional-derivative operator $u^\star = \gamma^{-1}\kappa_{1-\beta}D_+^\nu\zeta$, and the cost of using the signal is $\gamma^{-1}\|P_+ C_-^{-1}\alpha\|_{L^2}^2$ per unit time, not $\gamma^{-1}\|\alpha\|_{L^2}^2$.

The framework of the paper suggests a different objective. Given a stationary adapted signal $\alpha$, its **tradeability** is
$$T(\alpha) \;:=\; \|P_+ C_-^{-1}\alpha\|_{L^2(\mathbb P\otimes dt)}^2,$$
and the achievable value per unit cost aversion is $V^\star = T(\alpha)/(2\gamma)$. All practical questions about signal design under transient impact reduce to controlling $T(\alpha)$.

## 2. Decomposition of $T(\alpha)$

Three axes control the tradeability functional. Each corresponds to a distinct signal-design decision.

### 2.1 Spectral axis (unconstrained ceiling)

Under Parseval,
$$\|\alpha\|_{C^{-1}}^2 \;=\; c_\beta^{-1}\int_{-\infty}^\infty |\xi|^{1-\beta}\,|\hat\alpha(\xi)|^2\,d\xi \;=\; c_\beta^{-1}\|\alpha\|_{\dot H^\nu}^2,\qquad \nu = \tfrac{1-\beta}{2}.$$
This is a $\dot H^\nu$-norm: tradeability rewards **high-frequency content** at rate $|\xi|^{1-\beta}$. Per unit $L^2$-energy, faster signals dominate slower ones. For stationary OU with mean-reversion $\theta$ and variance $\sigma^2/(2\theta)$, direct calculation from eq. (14) gives
$$\frac{V^\star_{\rm OU}}{\text{Var}(\alpha)} \;=\; \frac{1}{2\gamma c_\beta}\,\theta^{1-\beta}.$$
Per unit variance the tradeability grows as $\theta^{1-\beta}$: doubling the mean-reversion rate multiplies value by $2^{1-\beta}$ (≈ 1.5× for $\beta = 0.4$).

**Design implication.** Smoothing operations (EMAs, low-pass filters, Kalman smoothers) that make a signal "look better" in a backtest by reducing paper-turnover simultaneously reduce $\|\alpha\|_{\dot H^\nu}$. They trade axis-1 tradeability for cosmetic paper-Sharpe.

### 2.2 Adaptedness axis (projection loss)

The gap between unconstrained and adapted value is
$$\|\alpha\|_{C^{-1}}^2 \;-\; T(\alpha) \;=\; \|(I-P_+)\,C_-^{-1}\alpha\|_{L^2}^2 \;\ge\; 0,$$
the $L^2$-norm of the un-forecastable part of the anticausally whitened signal. This gap vanishes iff $C_-^{-1}\alpha$ is already adapted — iff $D_-^\nu\bar\alpha(t,\cdot)$ evaluated at $t$ is a functional of $\mathcal F_t$ alone.

**Markov signals achieve this exactly.** The OU calculation collapses the whole anticausal integral to $\theta^\nu\alpha_t$, a pointwise function of the current state. More generally, any finite-dimensional Markov signal with linear-Gaussian forecast dynamics has zero adaptedness loss.

**Non-Markov signals pay a Bregman-type gap.** Long-memory alphas — fractionally integrated processes, Volterra Gaussian models, signals aggregating a slowly decaying kernel of past features — have forecast curves whose anticausal half-derivative at $t$ depends on structure the trader cannot pin down from $\mathcal F_t$. The gap $\|(I-P_+)C_-^{-1}\alpha\|^2$ is the strictly-positive cost of this un-summarizable dependence.

**Design implication.** Predictor architectures with unbounded state (deep sequence models, non-Markov RNNs, transformer stacks aggregating long histories) can bake long-memory structure into the output. Some of that structure will not survive the $P_+$ projection. State-space models with a finite hidden dimension avoid this by construction.

### 2.3 Response axis (causal fractional derivative)

The trading rate is $u^\star_t = \gamma^{-1}\kappa_{1-\beta}(D_+^\nu\zeta)(t)$, where $D_+^\nu$ acts as a bandpass with gain $\propto |\xi|^\nu$ on the whitened forecast $\zeta$. Sharp features in $\zeta$ (jumps, level shifts, event responses) generate large short-duration trades; smooth features produce muted responses.

**Design implication.** Signals derived from event indicators (macro releases, earnings, order-book imbalance thresholds) produce high-tradeability responses. Signals produced by heavy regularization or ensembling that smooths out sharp features suppress their own tradeable content.

## 3. The tradeability-adjusted training objective

For a parametric predictor $\alpha_\theta = f_\theta(x)$ evaluated on adapted feature process $x_t$, replace the standard loss with
$$\mathcal L_{\rm trad}(\theta) \;=\; -\,\mathbb E\,\|P_+ C_-^{-1}\alpha_\theta\|_{L^2}^2 \;+\; \lambda_{\rm reg}\, R(\theta),$$
with $R(\theta)$ a normalization or complexity penalty. Without normalization, the objective is trivially maximized by scaling $\alpha_\theta$; the natural constraint is a **realized-return orthogonality**:
$$\mathbb E\!\int u^\star(\alpha_\theta)_t \, r_{t+dt}\,dt \;=\; \text{const},$$
i.e., fix the actually realized expected trading PnL and maximize the fraction of it that survives cost. This gives the right dimensional invariant: **PnL efficiency**, not raw signal magnitude.

Computationally, $C_-^{-1} = c_\beta^{-1/2}D_-^\nu$ is an upper-triangular Toeplitz operator on discretized time. $P_+$ conditional expectation is approximated by regressing on $\mathcal F_t$-measurable features (or by the trained model's own filtration proxy). The loss and its gradient are $O(N\log N)$ per training example via FFT — cheap enough for deep-learning workflows.

## 4. Tradeability-weighted signal combination

Given $K$ candidate signals $\alpha^{(1)}, \ldots, \alpha^{(K)}$, the linear combination $\alpha = \sum_k w_k \alpha^{(k)}$ has tradeability
$$T(\alpha) \;=\; w^\top T_{\rm mat}\, w,\qquad (T_{\rm mat})_{jk} := \langle P_+ C_-^{-1}\alpha^{(j)},\, P_+ C_-^{-1}\alpha^{(k)}\rangle.$$
Under signal-Gram normalization $w^\top \Sigma w = 1$ with $\Sigma_{jk} = \langle \alpha^{(j)}, \alpha^{(k)}\rangle$, the tradeability-maximal combination is the leading generalized eigenvector of $(T_{\rm mat}, \Sigma)$:
$$w^\star \;=\; \arg\max_{w^\top\Sigma w = 1} w^\top T_{\rm mat}\, w \;=\; \text{leading eigvec of } \Sigma^{-1/2}T_{\rm mat}\Sigma^{-1/2}.$$

Contrast with **IC-weighted combination**, which solves
$$w^{\rm IC} \;=\; \arg\max_{w^\top\Sigma w = 1} w^\top \iota,\qquad \iota_k = \mathbb E[\alpha^{(k)}_t \cdot r_{t+h}],$$
giving $w^{\rm IC} \propto \Sigma^{-1}\iota$ (a Markowitz-shape formula on signals).

The two agree only when $T_{\rm mat} \propto \iota\iota^\top$, which happens iff all signals share the same shape after anticausal whitening — a degenerate case. Generically the tradeability-weighted combination differs from the IC-weighted one, and the difference measures how much value the IC weighting is leaving on the table.

**A cleaner form.** Under $\text{const}$-PnL normalization, the tradeability-optimal combination is
$$w^\star \;\propto\; T_{\rm mat}^{-1}\,\iota,$$
the tradeability-Mahalanobis analog of IC-weighting. This is the exact recipe: **replace the signal covariance $\Sigma$ with the tradeability form $T_{\rm mat}$ in the Markowitz-shape combination formula**.

## 5. Empirical predictions

1. **Smoothed signals underperform raw features cost-adjusted, even when they win on IC.** For a paired comparison (raw vs. EMA of a feature), tradeability-adjusted PnL should favor raw; paper-Sharpe should favor EMA.
2. **Regime signals with jumps score above their IC.** Event dummies (Fed announcements, earnings, macro releases) inject high-frequency content that the fractional-derivative response amplifies.
3. **Deep-sequence-model predictors trained on MSE loss lose tradeability to shallow state-space predictors with equal predictive $R^2$.** Because unbounded-state models bake long-memory structure into the forecast that $P_+$ subsequently discards.
4. **Tradeability-Mahalanobis ($T_{\rm mat}^{-1}\iota$) beats IC-Markowitz ($\Sigma^{-1}\iota$) out of sample** on signal-combination tasks, with an edge that grows in the number of signals combined (more room for cross-signal cost interference).
5. **The edge over IC-Markowitz scales with $\beta$**: shallow impact-decay ($\beta$ close to 1, kernel close to integrable) leaves less room for spectral shape to matter; steep decay ($\beta$ close to 0, long-memory impact) makes spectral shape decisive.

## 6. Connections and prior work

- **Grinold & Kahn (*Active Portfolio Management*)** discuss horizon-matching between alpha and trading. This framework is the continuous-time, cost-operator-aware version of horizon-matching, replacing the intuition "match your alpha horizon to your trading horizon" with the formula "match the spectrum of your alpha to $|\xi|^{\beta-1}$".
- **Kolm–Ritter** and other cost-aware portfolio-optimization work adds turnover penalties $\sum(\Delta w)^2$ to Markowitz. This is the finite-dimensional projection of the continuous-time cost norm and misses the temporal-covariance structure that $C$ encodes.
- **Almgren–Chriss** treats deterministic trajectories with linear temporary impact only; no signal, no fractional derivative. Their optimal trajectory is the $\eta \to \infty$ limit of §4.2.
- **Neuman–Voß (2022)** solves signal-adaptive execution against exponential kernel via Riccati. The fractional case is not covered by that machinery — the exponential kernel has finite-dimensional Markovian state, the power-law kernel does not.
- **Abi Jaber–Neuman (2025)**'s resolvent framework covers the general propagator case but does not produce a closed-form signal-design objective. The tradeability functional $T(\alpha)$ is a byproduct of the closed form (12) and is not directly available from their formulation.
- **Rough-path alpha models** (rough Bergomi, rough Heston as return-generators, not the same as rough signals) are orthogonal — they concern the return process, not the signal.

## 7. Where the framework does not extend

- **Nonlinear signal response.** The gain–cost problem is linear-quadratic; real trader responses to signals often saturate (position limits, capital allocation, drawdown gates). Adding a bounded feasible set makes (11) unavailable and the framework degrades to a variational inequality.
- **Multi-signal cross-tradeability.** §4.3 gestures at diagonal cross-impact. Genuine cross-impact ($A$ not simultaneously diagonalizable with the signal covariance) needs the matrix-symbol Wiener–Hopf machinery, which is well-defined but the design implications are open.
- **Non-stationary kernels.** Intraday impact varies with volume profile; overnight adds discontinuities. The framework assumes a fixed power-law $|t|^{-\beta}$.
- **Signal cost / attention cost.** The framework prices trading cost but not signal acquisition cost. A more complete objective would trade tradeability against signal-computation expense.
- **Adverse selection.** If the signal correlates with counterparty information, the effective kernel becomes state-dependent and the fixed-$C$ Wiener–Hopf is inadequate.

## 8. Concrete follow-up program

A publishable follow-up paper could proceed as follows.

1. **Theoretical.** Derive the tradeability-Mahalanobis combination formula $w^\star \propto T_{\rm mat}^{-1}\iota$ rigorously; state conditions under which it dominates IC-Markowitz.
2. **Simulation.** Generate synthetic paths from a factor model, apply competing signal-combination rules, measure realized tradeability-adjusted PnL under the fractional-cost model. Sweep $\beta$ and signal-count.
3. **Empirical.** Fit $\beta$ from mid-price impact on a real intraday dataset (US large-cap equities, $\beta \approx 0.4$ is a common empirical value). Compare tradeability-weighted vs. IC-weighted signal combinations on out-of-sample intraday alpha portfolios.
4. **Tooling.** Release a Python package implementing $C_-^{-1}$, $P_+$-adaptedness projection (as conditional expectation regressed on features), and the tradeability loss as a differentiable layer for ML pipelines.
5. **Ablations.** Show that smoothing operations, ensembling with soft aggregation, and long-horizon MSE training each reduce tradeability at fixed IC; quantify the loss.

The one-line pitch: **for signal-designers under transient impact, the loss function should be $-\|P_+ C_-^{-1}\alpha\|_{L^2}^2$ rather than MSE, and the combination rule should replace $\Sigma$ with $T_{\rm mat}$ in the Markowitz-shape formula.** Everything else in transient-impact signal design is a special case of this.

## 9. Open theoretical questions

- Is there a **variational characterization** of the tradeability-maximal signal under a raw predictive-$R^2$ constraint? (Rayleigh quotient on a Sobolev space intersected with the adapted subspace.)
- Under what conditions on the signal generator does $T(\alpha) / \|\alpha\|^2$ have a **closed-form ratio** in terms of the signal's spectral density and Markov dimension?
- What is the **finite-sample estimator** of $T_{\rm mat}$ from a discretely sampled signal panel, and its bias/variance properties?
- Does the framework extend to **jump-diffusion signals**? Fractional derivatives of jump processes are well-defined but the $L^2$-Sobolev hypothesis of §2.1 fails.
- Is there a **duality principle** between signal design (max $T$) and impact-kernel identification (fit $\beta$)? Both are inverse problems on the operator $C$.
