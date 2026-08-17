# Implications, Generalizations, and Connections of Wiener–Hopf Optimal Trading

**Companion note to** `papers/noisy-signal-impact-trading.md` and `outputs/optimal-trading-fractional-derivatives.md`.
**Date:** 2026-05-30.
**Status:** Synthesis / reflective note. No new theorems; conjectures are flagged.

---

## Executive Summary

The accompanying paper draft establishes a deliberately simple result: the stationary optimal causal trading policy under transient impact $K$ and signal $f$ is

$$
\hat x(\omega) \;=\; \big[K_+^{-1} \,[K_-^{-1} \hat f]_+ \big](\omega),
$$

i.e. *factor the kernel, project onto the causal subspace, divide by the causal factor*. For AR(1) signals and exponential impact this collapses to a scalar; for power-law impact the causal factor becomes a *causal fractional derivative*; under additive observation noise the rule decomposes cleanly into a Wiener prefilter followed by the same impact-adjusted causal operator.

This note steps back and asks what that result is *really* an instance of. Six themes emerge.

1. **It is the LQG separation principle in disguise.** Estimation (Wiener prefilter) commutes with control (Wiener–Hopf factor). The novelty is not separation itself, but the fact that the "control" half is a spectral factorisation of the impact kernel rather than the usual Riccati gain.
2. **The power-law / fractional-derivative case is not a curiosity — it is forced by no-arbitrage.** Jusselin–Rosenbaum (2018) show that no-arbitrage at the Hawkes/order-flow level *uniquely* selects a power-law macroscopic impact kernel. The fractional derivative in the optimal policy is therefore the canonical, not the exotic, case.
3. **The matrix / multi-asset generalisation is the operator-resolvent problem solved by Abi Jaber–Neuman–Tuschmann (2024).** Our scalar result is the rank-1 special case of their matrix Volterra propagator setup.
4. **The information-theoretic shadow is Gaussian rate–distortion with reverse water-filling.** The same Kolmogorov–Szegő innovation filter that appears in the trading rule also realises the Gaussian R(D) function predictively (Zamir–Kochman–Erez 2008). Predictive information $I(\text{past};\text{future})$ is the natural upper bound on long-horizon monetisable alpha.
5. **Crowding turns $K$ into an equilibrium-dependent $K_{\text{eff}}$ via mean-field games.** The Wiener–Hopf logic survives but the factor depends on the population strategy.
6. **The closed-form rule is the linear-Gaussian sanity check for signature methods, RL, and structured state-space models.** Any nonlinear/model-free method (Kalsi–Lyons signatures, deep RL for execution, S4-style learnable causal filters) should reduce to the Wiener–Hopf solution in its linear-Gaussian limit.

The rest of this note develops each thread and flags conjectures and open puzzles.

---

## 1. The LQG Separation Principle as the True Parent

The paper draft proves a *two-stage* decomposition for the noisy-signal problem: Wiener filter the observation to estimate the true predictor, then apply the impact-adjusted causal rule to the estimate. The author treats this as a clean by-product. It is in fact a special case of the *separation principle* of linear-quadratic-Gaussian (LQG) stochastic control, whose modern statement is given by Bensoussan–Van Schuppen–Willems (2011) and whose textbook form goes back to Kalman, Bucy, Wonham, Åström, and Willems.

**The LQG statement.** For a linear system with Gaussian state and observation noise and a quadratic cost, the optimal control law $u^\star_t$ depends on the observation history only through the Kalman estimate $\hat x_t$, and the control gain is identical to the gain one would use if the state were observed perfectly. Estimation and control decouple.

**The trading specialisation.** Our problem is LQG-equivalent in the following sense:

- *State* = the AR(1) (or Volterra) signal $f_t$ driving expected returns.
- *Observation* = the noisy predictor $y_t = f_t + n_t$.
- *Control* = the trade rate $x_t$.
- *Quadratic cost* = the propagator-induced norm $\langle x, K x \rangle$.
- *Linear running reward* = $f_t x_t$.

The control half of LQG is usually a finite-dimensional Riccati equation. Here it is replaced by *Wiener–Hopf factorisation in frequency domain* — equivalent in the infinite-horizon stationary limit but more transparent, because $K$ is naturally a convolution operator rather than a state-space matrix.

**Why this matters.** Three immediate consequences follow.

- The separation extends, *unchanged*, to vector signals, observation channels with correlated noise, and time-varying gains — wherever LQG itself extends.
- The separation *breaks* exactly where LQG breaks: non-Gaussian noise, non-quadratic costs, or hidden-mode dynamics (Markov-jump linear systems, Markov-switching impact regimes). In all these cases the optimal policy is no longer linear in $\hat f$, and the Wiener–Hopf rule is only the certainty-equivalent approximation.
- For markov-switching impact regimes (different liquidity regimes), the separation can be salvaged only under restrictive observability assumptions — a recent literature studies precisely this (e.g. recent work on separation for hidden-mode MJLS).

**Conjecture (separation under partial observation of impact).** *If the trader has noisy observations of both the signal $f_t$ and the impact-state itself (e.g. order-book imbalance summarising the impact kernel state), then the optimal causal policy decomposes into (i) a joint Kalman–Bucy filter over $(f, \text{impact state})$ and (ii) the impact-adjusted causal Wiener–Hopf rule applied to the filtered $f$, with the same causal factor $K_+$.* This would be a strict generalization of the paper's noisy-predictor result and worth checking against the operator framework of Abi Jaber–Neuman (2022).

---

## 2. Power-Law Impact Is Forced by No-Arbitrage

The paper introduces the power-law kernel $G(n) = n^{-\beta}$ as a tractable alternative to the exponential, and notes that its Wiener–Hopf causal factor is a fractional derivative. This invites the reader to view power laws as one option among many. The microstructure literature is sharper: under mild no-arbitrage and order-flow assumptions, *the power law is essentially unique.*

The relevant chain is:

1. **Hawkes microstructure.** Order arrivals are well-fit by self-exciting Hawkes processes. Jaisson–Rosenbaum (2015) show that *nearly unstable* Hawkes processes — those with branching ratio close to 1, the empirically observed regime — have a scaling limit that is a *rough* (fractional) process.
2. **No-arbitrage on metaorders.** Jaisson (2015) and then Jusselin–Rosenbaum (2018, arXiv:1805.07134) impose linear permanent impact and the martingale property on the macroscopic price. They prove that *no-arbitrage forces the market impact function of a metaorder to be of power-law type*, with the exponent in one-to-one correspondence with the rough-volatility Hurst exponent $H$.
3. **Unified theory.** Ouazzani Chahdi, Rosenbaum, Szymanski (2026, arXiv:2601.23172) pin down a *single statistic* $H_0$ — the persistence of "core" order flow — that simultaneously determines signed-flow autocorrelation, rough volatility, and power-law impact.

**Implication for the paper.** The fractional-derivative formulation of the optimal causal policy is *not* a mathematical convenience. It is the unique no-arbitrage-consistent specialisation of the general Wiener–Hopf result. The constant $\lambda \rho$ that drops out of the AR(1) × exponential calculation — the product of signal persistence and kernel decay rate — has a natural counterpart in the power-law case: a product of *signal Hurst* and *kernel Hurst*, both of which feed back into the same $H_0$ of the unified theory.

**Open puzzle.** Is the AR(1) × exponential closed form a *strict* approximation to the AR-fractional × power-law case in the limit of small mismatch, in some controlled sense (e.g. matched first two cumulants of the kernel spectrum)? If so, the "exponential" calculation in the paper inherits real-world relevance beyond pedagogy.

---

## 3. The Multi-Asset Generalisation Is a Matrix Wiener–Hopf Problem

A vector signal $\mathbf f_t \in \mathbb R^d$ trading a basket with matrix-valued impact $\mathbf K(n) \in \mathbb R^{d \times d}$ leads to a *matrix* Wiener–Hopf problem: find a causal matrix-valued $\mathbf K_+$ and anticausal $\mathbf K_-$ with $\mathbf K = \mathbf K_+ \mathbf K_-$ on the unit circle (spectral factorisation of a matrix-valued positive-definite function).

This is exactly the problem solved, in continuous time and for general Volterra propagators, by Abi Jaber, Neuman & Tuschmann (2024, arXiv:2403.10273): operator-resolvent characterisation of the optimal multi-asset policy under matrix-valued cross-impact and a measurable signal. Earlier work — Alfonsi–Schied (arXiv:1310.4471), Mastromatteo et al. (arXiv:1702.03838), Frei et al. (arXiv:2503.05594) — establishes when matrix decay kernels admit well-posed optimal strategies in the first place.

**Three takeaways.**

- Existence of matrix Wiener–Hopf factorisation is *not* automatic: it requires matrix-valued positive definiteness, and even that is insufficient for arbitrage-freeness in the strict sense (Alfonsi–Schied 1310.4471 give a counterexample).
- When the matrix kernel is diagonal (no cross-impact) or rank-1 (one liquidity factor), the matrix problem reduces to the scalar Wiener–Hopf problem of the paper applied componentwise or to projected coordinates.
- In the rough-volatility / multivariate-Volterra-Heston regime, the matrix factor itself contains fractional-derivative components, producing genuinely coupled fractional execution rules.

**Conjecture (commuting-kernel reduction).** *If $\mathbf K$ admits a constant orthogonal eigenbasis (i.e. the spectral measure of $\mathbf K(\omega)$ has the same eigenvectors for all $\omega$), then matrix Wiener–Hopf factorisation reduces to scalar Wiener–Hopf in each eigen-coordinate.* This is the right structural assumption that would make the paper's scalar result lift cleanly to multi-asset, and it is a strictly weaker condition than diagonal $\mathbf K$.

---

## 4. The Information-Theoretic Shadow: Rate–Distortion and Predictive Information

The Wiener–Hopf factor $K_+$ that appears in the optimal trading rule is the same object as the *Kolmogorov–Szegő innovation filter* of the signal's spectrum. This makes the trading problem dual, in a precise sense, to a Gaussian source-coding problem.

**Gaussian rate–distortion.** Cover & Thomas (ch. 13) give the Gaussian R(D) function for a stationary source as a reverse water-filling on its power spectrum. Zamir, Kochman & Erez (2008, arXiv:0711.1766) provide a *predictive* time-domain realisation: the optimal lossy code is generated by an innovation filter — the same Kolmogorov–Szegő factor — followed by a memoryless test channel.

**Trading-side analogue.** In the trading problem, the dual norm $\|\hat f\|_{K^{-1}}^2$ measures the *gain capacity* of the signal under the impact metric. The frequency-domain optimal value of the gain-minus-cost objective is

$$
\mathcal{J}^\star \;=\; \frac{1}{2} \int_{-\pi}^{\pi} \frac{|[K_-^{-1}\hat f]_+(\omega)|^2}{\hat K(\omega)} \frac{d\omega}{2\pi}.
$$

This is structurally identical to a *reverse water-filling integral over the signal–kernel ratio*: where $S_f(\omega)/\hat K(\omega)$ is large, alpha is monetisable cheaply; where it is small, the kernel "drowns" the signal.

**Predictive information as the natural alpha bound.** Bialek, Nemenman & Tishby (2001) define the *predictive information*

$$
I_{\text{pred}}(T) = I(\text{past}_T;\text{future}_T)
$$

of a stationary process and identify three regimes — finite, logarithmic, and fractional power-law — distinguishing classes of processes by the long-time scaling of how much the past tells you about the future. Abdallah–Plumbley (2012, arXiv:1206.0304) give the predictive-information *rate* in closed form for AR(N) processes and observe a duality: PIR is invariant under spectral inversion (poles ↔ zeros of the transfer function).

**Two conjectures.**

- *(Information bound on alpha)* The infinite-horizon revenue $\mathcal{J}^\star$ is upper-bounded by a constant times the predictive information rate of the signal, with the constant determined by the spectrum of $K$. Intuitively, you cannot monetise more alpha than the signal contains about future returns.
- *(Fractional regime of revenue)* When the signal is a long-memory process (Bialek's fractional-power-law regime), the cumulative revenue under a power-law impact kernel scales as $T^{H_f + H_K - 1}$ rather than linearly in $T$, where $H_f$ and $H_K$ are the signal and kernel Hurst exponents. This would explain, on information-theoretic grounds, why rough-vol-style trading strategies have anomalous long-horizon Sharpe scaling.

---

## 5. Crowding, Mean-Field Games, and the Effective Kernel

The single-agent picture assumes the impact kernel $K$ is *exogenous*. In reality, $K$ is the aggregate response of *all* traders to one trader's orders. When many agents share signals or estimators, their collective impact dominates.

Cardaliaguet & Lehalle (arXiv:1610.09904) formulate optimal liquidation as a mean-field game (MFG) of controls and show that *trade crowding* — many similar agents trading similar signals — modifies the equilibrium trading speed in a measurable way. Neuman & Voß (arXiv:2106.09267) prove $O(N^{-2})$ convergence of $N$-player Nash equilibria to the MFG limit.

**Implication for the Wiener–Hopf picture.** In the symmetric MFG, the *effective* impact kernel experienced by a representative agent is $K_{\text{eff}} = K + \Phi[\bar x]$, where $\bar x$ is the population-average trading rate and $\Phi$ is a linear operator capturing the crowding feedback. The Wiener–Hopf factorisation must then be performed on $K_{\text{eff}}$, which depends on the equilibrium — leading to a fixed-point problem.

**Practical reading.** A trader who measures $K$ from order-book data and applies the single-agent Wiener–Hopf rule is implicitly running a *Stackelberg* assumption: that others do not adapt. Under crowding this systematically *under-discounts* alpha at horizons longer than the equilibration time of the population strategy. The result is real-world alpha decay that the single-agent model attributes to "kernel misspecification" but which is in fact endogenous crowding.

---

## 6. Sanity-Check Baseline for ML Methods

Three machine-learning approaches to execution converge on the same problem the paper solves analytically. The closed-form Wiener–Hopf rule is the right baseline for each.

### 6.1 Signature methods (Kalsi–Lyons–Perez Arribas 2020)

Signatures of rough paths provide a nonparametric basis for path-dependent functionals. Kalsi, Lyons & Perez Arribas (arXiv:1905.00728, SIAM J. Fin. Math.) develop a signature-based optimal execution method that requires only that price is a geometric rough path and impact is a continuous function of trading speed.

The Wiener–Hopf rule is the *linear projection* of the signature-based optimal control onto degree-1 elements (the linear-Gaussian case). Any signature-method implementation should be cross-checked against the linear formula in the AR(1) × exponential regime where the latter is exact.

### 6.2 Deep RL for execution (Micheli–Monod 2024, etc.)

The literature reviewed in `outputs/optimal-trading-fractional-derivatives.md` (§9) increasingly uses RL with general decay kernels. The Wiener–Hopf rule is the *expected outcome* of an RL agent trained in the linear-Gaussian setting with the right inductive bias. Failure to recover it is a diagnostic of training pathology or insufficient exploration of long-memory effects.

### 6.3 Structured state-space sequence models (S4)

Gu, Goel & Ré (arXiv:2111.00396) parameterise long causal convolutions through structured (diagonal-plus-low-rank) state-space matrices, with HiPPO bases that can approximate power-law-decaying kernels efficiently. An S4 layer applied to a signal time series is, architecturally, a *learnable causal kernel* — exactly the object the Wiener–Hopf rule writes in closed form.

This suggests a methodological pipeline: pre-train an S4 layer to approximate the impact-adjusted causal kernel $K_+^{-1}$ for known $K$, then fine-tune on realised PnL. The Wiener–Hopf solution provides the analytic warm start and the convergence target in the well-specified limit.

---

## 7. Open Questions and Puzzles

1. **Does the AR(1) × exponential scalar $\lambda \rho$ have a microstructural meaning?** The product appears as the contraction factor of the anticausal Wiener–Hopf factor. A guess: $\lambda \rho$ is the *Pearson correlation between signal innovations and impact relaxation events*, which would make it directly measurable from intraday data.

2. **Robust / $H^\infty$ version.** Replacing the Wiener prefilter with an $H^\infty$ filter (Hassibi–Sayed–Kailath) yields a minimax estimator under spectral ambiguity. Does the impact-adjusted causal half remain Wiener–Hopf, or does the worst-case spectrum perturb $K_+$ as well? The answer determines whether robust trading rules retain the clean two-stage form.

3. **Constraints and conjugate duality.** Position limits, no-short constraints, and inventory penalties break the quadratic structure. A Lagrangian-dual reformulation should preserve the *form* of Wiener–Hopf with a state-dependent multiplier; making this precise is open.

4. **Information bound (Conjecture in §4)**. Is there an explicit information-theoretic upper bound on $\mathcal{J}^\star$ in terms of the predictive information rate of the signal and a complexity measure of $K$? This would give a model-free "alpha capacity" of a market.

5. **Mean-field fixed point under power-law impact.** The crowding fixed point of §5 is well-studied for exponential kernels; under power-law $K$ it has not been worked out, and the rough-volatility microfoundation suggests it may exhibit non-trivial multi-equilibrium structure.

6. **When does the separation principle fail least gracefully?** The paper's clean two-stage rule assumes Gaussian-linear everything. The first-order correction in non-Gaussianity (or in a polynomial cost) is, conjecturally, a *cumulant-correction* to the Wiener prefilter — but the cleanest way to express it is open.

---

## 8. Synthesis

The paper draft's Wiener–Hopf optimal-trading result is one node in a dense graph of equivalences:

| From the paper                          | Equivalent / parent object                                  |
|----------------------------------------|-------------------------------------------------------------|
| Causal Wiener–Hopf factor $K_+$         | Kolmogorov–Szegő innovation filter                          |
| Two-stage rule under noisy signal       | LQG separation principle (Kalman, Wonham, Åström)           |
| Power-law impact ⇒ fractional derivative| No-arbitrage in nearly-unstable Hawkes (Jusselin–Rosenbaum) |
| Vector-signal generalisation            | Matrix-Volterra operator resolvent (Abi Jaber–Neuman–Tuschmann) |
| Dual norm $\|\hat f\|_{K^{-1}}^2$       | Reverse water-filling in Gaussian R(D)                      |
| Alpha capacity of a market              | Predictive information rate (Bialek–Nemenman–Tishby)        |
| Crowding-adjusted kernel                | Mean-field equilibrium kernel (Cardaliaguet–Lehalle)        |
| Closed-form rule as ML baseline         | Signature methods / RL / S4 in linear-Gaussian limit        |

The paper's contribution is best read not as a *new* theorem but as a *bridge*: a sufficiently elementary derivation that makes all of these connections visible at once. Each row in the table above could be the seed of its own extension paper.
