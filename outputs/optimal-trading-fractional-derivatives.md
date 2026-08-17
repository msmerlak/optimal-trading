# Optimal Trading and Fractional Derivatives: A Literature Review

**Date:** 2026-05-30 (updated 2026-05-30, gap-fill pass)
**Scope:** Intersection of fractional calculus (fractional derivatives, fractional Brownian motion, rough volatility) with optimal trading, execution, and portfolio optimization in mathematical finance.

---

## 1. Introduction & Motivation

Classical mathematical finance rests on semimartingale price processes-geometric Brownian motion, diffusions, and Lévy processes-which obey the Markov property and the fundamental theorems of asset pricing. Yet empirical evidence consistently reveals features that these models struggle to capture:

- **Long memory in volatility:** Autocorrelation of absolute or squared returns decays as a power law, not exponentially (Baillie, Bollerslev & Mikkelsen, 1996; Comte & Renault, 1998).
- **Roughness of volatility paths:** High-frequency data show log-volatility behaves like a fractional Brownian motion (fBm) with Hurst exponent $H \approx 0.1$, far rougher than a standard Brownian motion (Gatheral, Jaisson & Rosenbaum, 2018).
- **Power-law decay of price impact:** Empirical market impact from large orders decays as a power law $t^{-\beta}$ rather than exponentially, naturally linking to fractional integral kernels (Bouchaud, Farmer & Lillo, 2009; Gatheral, 2010).

These observations motivate the use of **fractional calculus**-derivatives and integrals of non-integer order-as a modeling tool in finance, particularly for problems of optimal trading, execution, and portfolio construction. This review surveys the resulting literature, which spans roughly 1997-2026 and intersects stochastic analysis, optimal control, market microstructure, and econophysics. A unifying thread running through recent work (2024-2026) is the convergence of microstructural models, rough volatility, and Volterra-type control into a single coherent picture-anchored by the Muhle-Karbe, Rosenbaum et al. (2026) unified theory (§5.4).

---

## 2. Mathematical Background

### 2.1 Fractional Calculus Primer

Fractional calculus generalizes differentiation and integration to non-integer orders. The three principal operators used in finance are:

**Riemann-Liouville fractional integral** of order $\alpha > 0$:

$$I^{\alpha} f(t) = \frac{1}{\Gamma(\alpha)} \int_0^t (t-s)^{\alpha-1} f(s)\, ds$$

**Caputo fractional derivative** of order $\alpha \in (0,1)$:

$${}^C D^{\alpha} f(t) = \frac{1}{\Gamma(1-\alpha)} \int_0^t (t-s)^{-\alpha} f'(s)\, ds$$

**Riemann-Liouville fractional derivative:**

$${}^{RL} D^{\alpha} f(t) = \frac{d}{dt} \frac{1}{\Gamma(1-\alpha)} \int_0^t (t-s)^{-\alpha} f(s)\, ds$$

The Caputo derivative is preferred in initial-value problems because it allows classical initial conditions. The key feature distinguishing these from integer-order operators is **non-locality**: the fractional derivative at time $t$ depends on the entire history $[0,t]$, providing a natural mechanism for modeling memory effects.

### 2.2 Fractional Brownian Motion (fBm)

Fractional Brownian motion $B^H_t$, introduced by Mandelbrot and Van Ness (1968), is the unique continuous, mean-zero Gaussian process with covariance:

$$E[B^H_s B^H_t] = \frac{1}{2}\left(|t|^{2H} + |s|^{2H} - |t-s|^{2H}\right)$$

where $H \in (0,1)$ is the **Hurst exponent**. Key properties:
- $H = 1/2$: standard Brownian motion (independent increments).
- $H > 1/2$: positively correlated increments (long memory, persistence).
- $H < 1/2$: negatively correlated increments (anti-persistence, roughness).

Crucially, fBm is **not a semimartingale** for $H \neq 1/2$, which has profound consequences for arbitrage theory (§3).

### 2.3 Connection Between fBm and Fractional Derivatives

The Mandelbrot-Van Ness representation links fBm to fractional integration:

$$B^H_t = \frac{1}{\Gamma(H + 1/2)} \int_{-\infty}^t \left[(t-s)^{H-1/2} - (-s)_+^{H-1/2}\right] dW_s$$

This reveals fBm as essentially a fractional integral (of order $H - 1/2$) of white noise. When $H < 1/2$, this is a fractional derivative of the Brownian path, producing rough trajectories. This representation underpins the "rough volatility" program (§5).

---

## 3. The Arbitrage Problem: Foundational Results

The non-semimartingale nature of fBm created a fundamental tension with no-arbitrage theory, resolved through a sequence of landmark papers:

### 3.1 Arbitrage Exists in Frictionless fBm Markets

**Rogers (1997)** demonstrated that if log-prices follow fBm with $H \neq 1/2$, then arbitrage opportunities exist in continuous time with zero transaction costs. The proof exploits the predictability of fBm increments from path history. This result initially seemed to rule out fBm as a viable price model.

**Cheridito (2003)** refined this by showing that arbitrage persists for $H \in (0, 3/4)$ even under discrete-time trading, but for $H \in (3/4, 1)$, discrete trading at a fixed frequency eliminates arbitrage. The critical threshold $H = 3/4$ arises from the condition for fBm increments to behave like a semimartingale at a given time scale.

### 3.2 No Arbitrage Under Transaction Costs

**Guasoni (2006)** established that proportional transaction costs restore no-arbitrage for fBm price processes. The key insight: transaction costs prevent the rapid trading needed to exploit the predictability of fBm. This result opened the door for using fBm in models with realistic market frictions.

**Czichowsky, Schachermayer, Peyre & Yang (2018)** extended this program by constructing **shadow prices**-fictitious frictionless price processes taking values in the bid-ask spread-for exponential fBm under transaction costs. This enabled the derivation of optimal portfolio strategies by reducing the problem with frictions to a frictionless problem for the shadow price.

### 3.3 Practical Discretization of fBm Arbitrage Strategies

**Lamert, Auer & Wunderlich (2025, MMOR; arXiv:2311.15635)** revisit the Shiryaev (1998) and Salopek (1998) continuous-time arbitrage strategies for fBm markets and evaluate their *practical usefulness* after discretization and introduction of transaction costs. Monte Carlo simulations show both strategies remain promising with respect to terminal portfolio values and loss probabilities. The discretization error analysis provides conditions under which the theoretical strategies survive the transition to implementable form-an important bridge between the theoretical arbitrage results and real trading.

### 3.4 Implications for Optimal Trading

These results establish a nuanced landscape: fBm price models are economically meaningful only when market frictions (transaction costs, discrete trading, price impact) are explicitly included. This has directed the literature toward models where fractional features interact with trading costs-precisely the setting relevant for optimal execution.

---

## 4. Fractional Models of Price Dynamics

### 4.1 Fractional Black-Scholes Equation

Replacing the time derivative in the Black-Scholes PDE with a Caputo fractional derivative of order $\alpha \in (0,1]$ yields the **time-fractional Black-Scholes equation**:

$${}^C D_t^{\alpha} V + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$$

This models sub-diffusive dynamics where price changes exhibit memory. Multiple papers have developed analytical and numerical solutions:
- Homotopy perturbation methods (Kumar, Singh & Kumar, 2012; Elbeleze, Kılıçman & Taib, 2013).
- Cubic spline discretization on uniform meshes (Kaur & Natesan, 2023).
- Sumudu transform iterative methods (recent work, 2025).

**Interpretation caveat:** The economic justification for replacing the time derivative with a fractional one remains debated. Some authors argue it captures anomalous diffusion (sub- or super-diffusive returns), while critics note that the resulting pricing formulas may violate basic no-arbitrage constraints unless carefully constrained.

### 4.2 Fractional Diffusion Models (FMLS, CGMY, KoBoL)

**Cartea and del-Castillo-Negrete (2007)** showed that several important Lévy process models-the Finite Moment Log-Stable (FMLS) model, the CGMY model, and the KoBoL model-all lead to **fractional partial differential equations** for option prices. Specifically, these Lévy processes generate option pricing PDEs involving **fractional spatial derivatives** (Riesz-Feller operators), not just fractional time derivatives. This established a principled connection between Lévy-driven asset dynamics and fractional calculus, grounded in the theory of stable distributions rather than ad hoc modifications of the diffusion equation.

### 4.3 Continuous-Time Random Walk (CTRW) Approach

The econophysics community has used fractional calculus through the **continuous-time random walk** framework (Scalas, Gorenflo & Mainardi, 2000; Mainardi, 2020). Here, the waiting times between trades follow a heavy-tailed distribution, leading to fractional Fokker-Planck equations that describe the evolution of the price probability density. This provides a microstructural justification for fractional dynamics: the non-Markovian behavior arises from the empirical distribution of inter-trade durations.

---

## 5. Rough Volatility and Optimal Trading

### 5.1 The Rough Volatility Revolution

The most impactful recent application of fractional calculus to finance is the **rough volatility** program initiated by Gatheral, Jaisson, and Rosenbaum (2018, "Volatility is Rough," arXiv:1410.3394). Their key empirical finding: log-volatility of equity indices behaves as fBm with $H \approx 0.1$ across all reasonable time scales. This is dramatically rougher than standard Brownian motion ($H = 0.5$) and contradicts classical stochastic volatility models.

The **rough Bergomi model** (Bayer, Friz & Gatheral, 2016) and the **rough Heston model** (El Euch & Rosenbaum, 2019) formalize this observation. In the rough Heston model, the variance process satisfies a Volterra-type equation:

$$V_t = V_0 + \frac{1}{\Gamma(\alpha)} \int_0^t (t-s)^{\alpha-1} \lambda(\theta - V_s)\,ds + \frac{\nu}{\Gamma(\alpha)} \int_0^t (t-s)^{\alpha-1} \sqrt{V_s}\, dW_s$$

where $\alpha = H + 1/2 \in (0.5, 1)$. El Euch and Rosenbaum (2019) derived the characteristic function of this model by showing it satisfies a fractional Riccati equation-a major analytical breakthrough that enabled option pricing and hedging in the rough framework.

### 5.2 Optimal Execution Under Rough Volatility

**Kalsi, Lyons, and Perez Arribas (2020)** developed optimal execution strategies when the price process is a geometric rough path. Using the **signature method** from rough path theory, they constructed approximate solutions to the optimal execution problem without requiring the price process to be Markovian or a semimartingale. Their framework is general: it requires only that the price is a geometric rough path and the price impact function is continuous in trading speed. This approach sidesteps the non-Markovian difficulties of fBm by working directly with path signatures as sufficient statistics.

**Webb (2024)** applied fractional stochastic volatility (FSV) models to market microstructure and optimal execution, using high-frequency data (2015-2020) across equities, FX, and futures. The paper reported Hurst exponent estimates of $H \approx 0.65$ (aggregated across asset classes, indicating long-memory persistence) and claimed a 15% reduction in execution costs using FSV-based adaptive algorithms compared to conventional methods. **Caution:** This paper's empirical claims are preliminary and not independently reproduced. The reported $H = 0.65$ is substantially higher than the $H \approx 0.1$ found by Gatheral et al. for volatility roughness-the discrepancy reflects different estimands (price persistence vs. volatility roughness) and different asset classes, but the paper does not adequately distinguish these. The 15% cost reduction claim lacks reproducible algorithmic detail and rests on a single study in a non-top-tier venue.

### 5.3 High-Frequency Trading with fBm

**Guasoni, Mishura, and Rásonyi (2021)** obtained a striking result for trading an asset whose price follows fBm. In the high-frequency limit, conditionally expected increments of fBm converge to white noise, making the problem tractable. They derived:

- **Explicit locally mean-variance optimal strategies** for fBm price processes.
- **Without trading costs:** Risk-adjusted profits are linear in the trading horizon and increase asymmetrically in $H$-both very rough ($H \ll 1/2$) and very persistent ($H \gg 1/2$) paths yield higher profits than standard Brownian motion.
- **With trading costs:** Optimal strategies and profits depend on $H$ and the cost structure in nontrivial ways.

This paper provides one of the cleanest analytical results connecting fractional dynamics to optimal trading strategies.

---

## 6. Optimal Execution with Fractional Impact Kernels

### 6.1 Propagator Models with Power-Law Decay

A major strand of the optimal execution literature models transient price impact via **propagator** (or **decay kernel**) models. The price distortion from trading decays according to a kernel $G(t)$, and the price at time $t$ is:

$$S_t = S_0 + \int_0^t G(t-s)\, d\xi_s + \text{martingale noise}$$

where $\xi_t$ is the cumulative trading strategy. **Obizhaeva and Wang (2013)** used exponential decay $G(t) = e^{-\rho t}$, while empirical evidence suggests **power-law decay** $G(t) \sim t^{-\gamma}$ for $\gamma \in (0,1)$-precisely a fractional kernel.

### 6.2 Gatheral, Schied & Slynko (2011)

Gatheral, Schied, and Slynko (2012) studied transient linear price impact in continuous time, showing that the optimal execution problem reduces to a **Fredholm integral equation of the second kind**. When the propagator kernel is a power law $G(t) = t^{-\gamma}$, the integral equation has a Volterra structure with a weakly singular kernel-exactly the type arising in fractional calculus. They established conditions on $G$ under which price manipulation (profitable round trips) is excluded, providing a no-manipulation analogue of the no-arbitrage condition for propagator models.

### 6.3 General Propagator Models with Signals

**Abi Jaber, Neuman, and Voss (2022, arXiv:2211.00447)** extended the theory to general Volterra-type propagators with signals (predictive information). Using infinite-dimensional stochastic control, they characterized optimal strategies for revenue-risk functionals under power-law kernels with possible singularities. Their explicit formulas can handle the empirically relevant case of singular (fractional) propagator kernels, directly connecting optimal execution to fractional integral equations.

**Abi Jaber, Bondi, De Carvalho, Neuman & Tuschmann (2025, arXiv:2503.04323)** considered nonlinear transient price impact with power-law decay, showing that optimal trading satisfies a **nonlinear stochastic Fredholm equation** with both forward and backward components-a significantly more complex structure than the linear case. They proved existence and uniqueness under a monotonicity condition and introduced a convergent iterative scheme for numerical computation.

### 6.4 Trading with Market Resistance and Concave Impact

**Ouazzani Chahdi, De Carvalho & Szymanski (2026, arXiv:2601.03215)** extend the propagator framework by introducing *endogenous market resistance*: a sophisticated counterparty who partially detects metaorders and trades against them. The model features a **concave transient impact** driven by a **power-law propagator** with a resistance term responding to the trader's rate via a fixed-point equation. The first-order optimality condition yields a (non)linear stochastic Fredholm equation. The authors prove existence and uniqueness when resistance is linear, existence under convexity, and provide an iterative scheme with exponential convergence. This paper operationalizes the empirical square-root law within the propagator framework and demonstrates that adversarial market resistance qualitatively changes optimal round-trip strategies.

### 6.5 Multi-Asset Cross-Impact with Volterra Propagators

**Abi Jaber, Neuman & Tuschmann (2024/2026, arXiv:2403.10273)** solve the **multi-asset optimal portfolio choice problem** with transient cross-impact driven by a **matrix-valued Volterra propagator** (including power-law kernels). The first-order condition reduces to a coupled system of stochastic Fredholm equations of the second kind, solved explicitly via operator resolvents. Key contributions:
- **No-manipulation conditions** for the matrix-valued propagator.
- Explicit solutions showing how cross-impact creates *spill-over effects*: optimal trading in one asset depends on impact decay and alpha signals in correlated assets.
- Implementation provided for practical computation.

This paper directly fills the "multi-asset fractional execution" gap identified in v1 of this review.

**Ackermann, Kruse & Urusov (2025, arXiv:2503.05594)** generalize the Obizhaeva-Wang framework to **multiple assets with stochastic matrix-valued cross-impact and resilience**. Using linear-quadratic stochastic control, they reveal *cross-hedging effects*: it can be optimal to trade in an asset despite having no initial position, purely due to cross-impact dynamics.

### 6.6 Optimal Execution on DeFi AMMs

**Baude, Challet & Muni Toke (2026, arXiv:2601.03799)** study optimal liquidation on Uniswap v2/v3 with transient impact modeled as either exponential or approximately **power-law decay**. For Uniswap v2, they obtain closed-form optimal strategies; for v3 with concentrated liquidity, they use dynamic programming with discretization. This extends the power-law transient impact framework from traditional LOB markets to decentralized automated market makers.

### 6.7 Optimal Execution Under Liquidity Uncertainty

**Chevalier, Hafsi, Ly Vath & Pulido (2025, arXiv:2506.11813)** formulate optimal execution as a **singular stochastic control problem** with a *stochastic volume effect* (jump-diffusion) and *regime-switching liquidity* (Markov chain). The value function is the unique viscosity solution of a system of variational HJB inequalities. The free boundary between execution and continuation regions depends on the liquidity regime.

### 6.8 Game-Theoretic Extensions

**Campbell and Nutz (2025, arXiv:2501.09638)** studied $N$-player optimal execution games in the Obizhaeva-Wang framework with transient impact. Without regularization by instantaneous trading costs, no equilibrium exists. With regularization, a unique equilibrium is derived in closed form.

**Guo & Jin (2025, arXiv:2504.06717)** bridge optimal execution and market making in a single stochastic game: market makers set quotes strategically while execution traders optimize schedules. The Nash equilibrium is characterized by coupled forward-backward SDEs. Permanent price impact is re-derived endogenously from market makers' quoting strategies.

---

## 7. Portfolio Optimization with Fractional Dynamics

### 7.1 Merton Problem Under fBm

The classical Merton (1971) portfolio problem has been extended to fBm-driven markets:

- **Hu, Øksendal, and Sulem (2003)** solved the Merton problem with fBm ($H > 1/2$) using Skorohod-sense stochastic integrals. For logarithmic utility, they obtained explicit optimal consumption and portfolio strategies. The Skorohod approach avoids the arbitrage issues of pathwise integration.

- **An optimal portfolio problem with fBm** (Wuhan Univ. J. Natural Sciences, 2022) used the HJB equation approach for $H \in (0,1)$ and compared results with the standard Black-Scholes market ($H = 1/2$).

### 7.2 Shadow Prices and Portfolio Optimization Under Transaction Costs

The shadow price approach of **Czichowsky, Peyre, Schachermayer, and Yang (2018)** enables utility maximization under proportional transaction costs when prices follow fBm. The idea: find a "shadow price" process (a semimartingale within the bid-ask spread) such that the frictionless optimal portfolio for this shadow price also solves the original problem with transaction costs. For power utility functions and exponential fBm, they proved existence of shadow prices and optimal strategies, reconciling fractional price models with mainstream portfolio theory.

### 7.3 Volterra Heston and Merton's Problem

**Han and Wong (2021)** investigated Merton's portfolio problem under the **Volterra Heston model**, where the variance process is driven by a Volterra equation with fractional kernel. Despite the non-Markovian, non-semimartingale structure, they obtained semi-closed-form optimal strategies for power and exponential utilities using the martingale optimality principle with an auxiliary Markovian lifting.

**Dro & Gnabeyeu (2026, arXiv:2605.00688)** extend this to **multivariate affine Volterra models with jumps** (Poisson random measure). They solve the Merton problem for exponential, power, and logarithmic utility in a multi-asset rough Heston setting with jumps, using the martingale optimality principle and a novel Riccati BSDEJ (backward SDE with jumps). Numerical experiments on a two-dimensional rough Heston model illustrate how both roughness and jump components affect optimal strategies.

### 7.4 Mean-Variance under Multivariate Rough Volterra Models

**Gnabeyeu (2026, arXiv:2604.01300)** solves the **continuous-time Markowitz mean-variance problem** under a multivariate class of *fake stationary affine Volterra models*-a generalization of rough Heston that captures both short- and long-maturity behavior. The optimal feedback control and efficient frontier are characterized via a stochastic-factor Riccati BSDE, with explicit solutions depending on multi-dimensional Riccati-Volterra equations. Numerical experiments show the impact of rough volatilities and stochastic correlations on optimal Markowitz strategies-one of the first papers to address multi-asset Markowitz under rough volatility.

### 7.5 Fractional Kelly Strategies

The **fractional Kelly strategy** literature (distinct from fractional calculus, but conceptually overlapping) studies investing a fraction of the Kelly-optimal portfolio. Under fBm dynamics specifically, **Lam and Chu (2018)** derived the Kelly-optimal fraction for fBm increments, finding that it depends on the investment horizon-a feature absent in the standard i.i.d. returns case. This horizon dependence directly reflects the autocorrelation structure encoded in $H$.

---

## 8. Market Making Under Rough Volatility

Market-making under rough volatility was identified as an open question in v1 of this review. Recent work has begun to address it.

**Rosenbaum & Zhang (2022/2025, arXiv:2212.10164)** formulate a **multi-asset market-making problem under the quadratic rough Heston (QRH) model** for SPX and its derivatives (VIX futures, SPX/VIX options). The QRH model captures joint SPX/VIX smile calibration with a single Brownian motion and rough volatility ($H \approx 0.1$). The market maker maximizes expected terminal wealth minus inventory risk penalties. Key features:
- The non-Markovian fractional kernel is approximated by a sum of exponentials (multi-factor Markovian lifting), enabling dynamic programming.
- A **quadratic approximation** to the Hamiltonian yields asymptotically closed-form optimal quoting strategies, addressing the curse of dimensionality.
- All inventory risk is reducible to SPX delta exposure under the QRH model, simplifying the multi-asset hedging problem.

This is the first paper to bring rough volatility models into the market-making literature with tractable solutions.

---

## 9. Reinforcement Learning for Fractional Execution

Another open question from v1 was whether model-free RL methods can learn optimal execution strategies that implicitly capture fractional dynamics. Several recent papers address this.

**Micheli & Monod (2024, arXiv:2410.13493)** introduce an actor-critic algorithm (based on DDPG) for **online optimal execution with general transient decay kernels**, including power-law kernels. The non-Markovian structure of transient impact (which makes the problem infinite-dimensional under classical methods) is handled by the RL agent's memory. Numerical experiments show that the algorithm successfully approximates optimal strategies across exponential, power-law, and mixed kernels, and adapts to time-varying parameters without recalibration.

**Huang, Jia & Zhou (2024, arXiv:2407.17226)** prove a **sublinear regret bound** of $O(N^{3/4})$ for an actor-critic RL algorithm applied to continuous-time linear-quadratic control with state- and control-dependent volatility. While not specific to fractional dynamics, this provides theoretical foundations for RL-based approaches to the class of LQ problems that include stylized optimal execution models.

A closely related paper published in *Finance & Stochastics* (2026) by the same group derives an actor-critic algorithm for optimal execution under the Almgren-Chriss model with Shannon-entropy regularization, obtaining closed-form optimal (Gaussian) policies and error analysis. This represents the first rigorous convergence analysis of RL for optimal execution in a top-tier journal.

---

## 10. Fractional Optimal Control: Theory

### 10.1 Hamilton-Jacobi-Bellman Equations for Fractional Systems

**Gomoyunov (2020)** established a rigorous **dynamic programming principle** for optimal control of Caputo fractional-order systems in a SIAM J. Control and Optimization paper. The value function satisfies a fractional HJB equation, but defined on a space of histories (not states) due to the non-Markovian nature of fractional dynamics. This work provides the theoretical foundation for Caputo-type optimal control in finance.

**Gomoyunov (2023)** clarified the relationship between the Pontryagin maximum principle and the HJB equation for fractional-order systems (*Differential Equations* 59, 1520-1526), showing that under suitable regularity conditions, the two approaches yield consistent necessary conditions-analogous to the classical result for integer-order systems but with additional technical subtleties.

### 10.2 Stochastic Fractional Optimal Control in Finance

**Jafari, Mahmoudi, and Eghbali (2024)** proposed methods for stochastic-fractional optimal control problems applied to portfolio management. They derived an equivalent reformulation of the stochastic-fractional problem that admits a classical HJB equation, enabling standard dynamic programming techniques to be applied indirectly. This approach avoids the infinite-dimensional state space problem by exploiting specific structural properties of the fractional dynamics.

### 10.3 Numerical Methods for Fractional HJB Equations

Numerical solution of fractional HJB equations is an active research front:

- **Jakobsen and Karlsen (2023, arXiv:2308.16434)** proved convergence rates for monotone approximation schemes of fractional HJB equations, including difference-quadrature schemes and approximations based on powers of discrete Laplacians. They achieved formally second-order methods.

- **Preconditioned Policy-Krylov methods** (Chen et al., 2024) combine policy iteration with Krylov subspace methods for fractional partial integro-differential HJB equations arising in finance, handling the non-locality of fractional operators efficiently.

- **Time-fractional Fokker-Planck optimal control** (Camilli et al., 2020, arXiv:2006.03518) studied numerical approximation of coupled backward-HJB / forward-Fokker-Planck systems with fractional time derivatives, relevant for mean-field-type control problems with anomalous diffusion.

---

## 11. Empirical Evidence & Calibration

### 11.1 Hurst Exponent Estimation

The Hurst exponent $H$ is the central empirical parameter. Methods include:
- **R/S (rescaled range) analysis** - classical but biased for short series.
- **Detrended fluctuation analysis (DFA)** - robust to non-stationarity.
- **Generalized Hurst exponent (GHE)** - uses $q$-th order moments.
- **Wavelet-based estimators** - efficient for multiscale analysis.

**Sánchez-Granero et al. (2022)** proposed improved estimation procedures based on distributional equality, showing better accuracy especially for small samples.

Key empirical findings:
- **Volatility roughness:** $H \approx 0.1$ for equity index volatility (Gatheral et al., 2018). This is the most robust and impactful finding.
- **Returns:** Generally $H \approx 0.5$ (consistent with efficient markets), but some studies find weak long memory in absolute returns or specific markets.
- **Long memory in volatility:** $H > 0.5$ in FIGARCH-type models for longer horizons (Baillie et al., 1996).

The apparent contradiction ($H < 0.5$ for volatility roughness vs. $H > 0.5$ for volatility persistence) is resolved by recognizing these refer to different time scales and different definitions of $H$. Rough volatility ($H \approx 0.1$) describes the local regularity of volatility paths, while long memory ($H > 0.5$) describes the slow decay of autocorrelations. Both can coexist.

### 11.2 Empirical Market Impact

- Power-law decay of price impact is well-documented empirically (Bouchaud, Farmer & Lillo, 2009; Gatheral, 2010).
- The exponent $\gamma$ in $G(t) \sim t^{-\gamma}$ is estimated at $\gamma \approx 0.5$-$0.7$ across various markets and time scales.
- This fractional decay directly enters optimal execution models (§6) and determines the character of optimal trading strategies.

### 11.3 Calibration Challenges

Calibration of fractional models faces several challenges:
- **Non-Markovian structure** makes likelihood computation expensive (path-dependent).
- **Rough models** require specialized simulation techniques (e.g., hybrid schemes by Bennedsen, Lunde & Pakkanen, 2017).
- **Model selection** between different fractional orders remains empirically difficult.

---

## 12. Open-Source Tools & Reproducibility

The following tools and libraries are available:

- **roughvol** (Python): Simulation and calibration of rough volatility models. Associated with the rough volatility literature (Bayer, Friz, Gatheral).
- **rBergomi** (various implementations): Simulation of the rough Bergomi model.
- **fbm** (Python, R packages): Simulation of fractional Brownian motion via Cholesky decomposition or Hosking's method.
- **FracDiff** (R): Fractional differencing for time series analysis.

Reproducibility remains a challenge: many key theoretical results (Gatheral-Schied-Slynko, El Euch-Rosenbaum) are analytically derived, but the empirical calibration pipelines (Hurst estimation, impact decay estimation) vary substantially across implementations. No widely adopted benchmark dataset exists for comparing fractional trading models.

---

## 13. Consensus, Disagreements, and Open Questions

### Consensus
1. **Volatility is rough**: The empirical evidence for $H \approx 0.1$ in equity volatility is strong and reproducible across markets (Gatheral et al., 2018; El Euch & Rosenbaum, 2019). Now further supported by the Muhle-Karbe et al. (2026) unified theory deriving it from order flow microstructure.
2. **Power-law impact kernels matter**: Optimal execution with fractional decay kernels produces qualitatively different strategies than exponential decay models. The framework has been extended to multi-asset (Abi Jaber et al., 2024; Ackermann et al., 2025), concave impact with resistance (Ouazzani Chahdi et al., 2026), and DeFi AMMs (Baude et al., 2026).
3. **Transaction costs resolve the arbitrage problem**: fBm is viable as a price model when frictions are included (Guasoni, 2006; Czichowsky et al., 2018). Lamert et al. (2025) show discretized arbitrage strategies remain profitable even with costs.
4. **Fractional HJB theory is maturing**: Dynamic programming for Caputo systems is now rigorous (Gomoyunov, 2020). Signature-based and Markovian-lifting methods provide practical computational tools (Bank et al., 2024; Rosenbaum & Zhang, 2022).
5. **NEW: The field is consolidating**: The previously disparate threads of rough volatility, power-law impact, and Volterra control are converging into a unified picture (Muhle-Karbe et al., 2026).

### Disagreements / Tensions
1. **Economic interpretation of fractional time derivatives**: Replacing $\partial_t$ with ${}^C D_t^\alpha$ in Black-Scholes lacks a clear microeconomic justification. Is it a modeling convenience or does it reflect a genuine anomalous diffusion mechanism?
2. **Rough vs. long memory**: Whether $H < 0.5$ (rough) or $H > 0.5$ (persistent) better describes financial volatility depends on the time scale and estimation method. The coexistence of both features in the same process remains theoretically subtle.
3. **Practical value of fractional models for execution**: While fractional impact kernels better fit empirical data, the improvement in out-of-sample execution performance over simpler models (e.g., Almgren-Chriss with exponential decay) is not always demonstrated convincingly.
4. **Stochastic integration conventions**: Results for fBm-driven portfolio problems depend sensitively on whether Skorohod, Wick, or pathwise integration is used, leading to different optimal strategies that are hard to compare economically.

### Open Questions (updated)
1. ~~**Unified framework**~~: **Substantially addressed** by Muhle-Karbe et al. (2026, arXiv:2601.23172), who show rough volatility, power-law impact, and long-memory order flow all arise from a single parameter $H_0 \approx 3/4$. Remaining open: extending this to multi-asset settings and empirically validating the scaling-limit predictions on modern data.
2. ~~**Reinforcement learning meets fractional dynamics**~~: **Partially addressed** by Micheli & Monod (2024, arXiv:2410.13493) with DDPG for general decay kernels, and by Huang, Jia & Zhou (2024, arXiv:2407.17226) with regret bounds for continuous-time LQ RL. Remaining open: RL with *rough volatility* state dynamics (not just impact kernels), and theoretical guarantees for non-LQ fractional problems.
3. ~~**Market-making under rough volatility**~~: **Addressed** by Rosenbaum & Zhang (2022/2025, arXiv:2212.10164) for multi-asset market making under quadratic rough Heston. Remaining open: empirical validation and extension to intraday time scales.
4. ~~**Multi-asset fractional execution**~~: **Addressed** by Abi Jaber, Neuman & Tuschmann (2024, arXiv:2403.10273) with matrix-valued Volterra propagators and by Ackermann, Kruse & Urusov (2025, arXiv:2503.05594) with stochastic cross-impact. Remaining open: empirical comparison against single-asset baselines and calibration to cross-impact data.
5. **Empirical validation of fractional optimal control**: Still largely open. Most fractional HJB results remain theoretical.
6. **Regulatory implications**: Unchanged. How should regulators stress-test non-semimartingale models?
7. **NEW: DeFi execution with fractional impact**: Baude et al. (2026, arXiv:2601.03799) open the door to power-law transient impact on AMMs, but the empirical evidence for power-law decay in DeFi markets is thin.
8. **NEW: Scalable numerical methods for rough Volterra control**: The multi-factor Markovian lifting (sum-of-exponentials approximation of fractional kernels) is becoming standard, but error bounds and the choice of number of factors remain under-studied.
9. **NEW: Adversarial/strategic fractional execution**: Game-theoretic models (Campbell & Nutz, Guo & Jin, Ouazzani Chahdi et al.) are emerging but have not been combined with *fractional* kernels in multi-player equilibria.

---

## 14. Conclusion

The intersection of fractional calculus and optimal trading has produced a rich and rapidly evolving literature. The field is organized around three main pillars:

1. **Fractional price/volatility models** (fBm, rough volatility, fractional Black-Scholes) that capture empirically observed memory and roughness features.
2. **Optimal execution with fractional impact kernels** (power-law propagators, Fredholm/Volterra integral equations) that model realistic transient price impact.
3. **Fractional optimal control theory** (fractional HJB equations, Pontryagin principles for Caputo systems) that provides the mathematical machinery for solving these problems.

The strongest empirical support is for rough volatility models and power-law impact kernels. The weakest link remains the gap between theoretical optimality results and demonstrated practical improvement in trading performance. Future work should prioritize empirical validation, multi-asset extensions, and computational methods that make fractional models actionable in real-time trading systems.

---

## Key References

1. Abi Jaber, E., Bondi, A., De Carvalho, N., Neuman, E. & Tuschmann, S. (2025). "Fredholm approach to nonlinear propagator models." *Finance & Stochastics*, to appear. [arXiv:2503.04323](https://arxiv.org/abs/2503.04323)
2. Abi Jaber, E., Neuman, E. & Tuschmann, S. (2024/2026). "Optimal portfolio choice with cross-impact propagators." [arXiv:2403.10273](https://arxiv.org/abs/2403.10273)
3. Abi Jaber, E., Neuman, E. & Voss, M. (2022). "Optimal liquidation with signals: the general propagator case." [arXiv:2211.00447](https://arxiv.org/abs/2211.00447)
4. Ackermann, J., Kruse, T. & Urusov, M. (2025). "Multi-asset optimal trade execution with stochastic cross-effects: An Obizhaeva–Wang-type framework." [arXiv:2503.05594](https://arxiv.org/abs/2503.05594)
5. Almgren, R. & Chriss, N. (2001). "Optimal execution of portfolio transactions." *J. Risk* 3, 5–39.
6. Alòs, E., Burés, Ò., de Santiago, R. & Vives, J. (2025). "Volatility modeling with rough paths: A signature-based alternative to classical expansions." [arXiv:2507.23392](https://arxiv.org/abs/2507.23392)
7. Baillie, R.T., Bollerslev, T. & Mikkelsen, H.O. (1996). "Fractionally integrated GARCH." *J. Econometrics* 74, 3–30.
8. Bank, P. & Bielert, F. (2025). "Causal Hamilton-Jacobi-Bellman equations for anticipative stochastic optimal control." [arXiv:2507.08657](https://arxiv.org/abs/2507.08657)
9. Bank, P., Bayer, C., Hager, P.P., Riedel, S. & Nauen, T. (2024). "Stochastic control with signatures." [arXiv:2406.01585](https://arxiv.org/abs/2406.01585)
10. Baude, B., Challet, D. & Muni Toke, I. (2026). "Optimal execution on Uniswap v2/v3 under transient price impact." [arXiv:2601.03799](https://arxiv.org/abs/2601.03799)
11. Bayer, C., Friz, P. & Gatheral, J. (2016). "Pricing under rough volatility." *Quantitative Finance* 16(6), 887–904.
12. Bouchaud, J.-P., Farmer, J.D. & Lillo, F. (2009). "How markets slowly digest changes in supply and demand." In *Handbook of Financial Markets: Dynamics and Evolution*, 57–160.
13. Campbell, S. & Nutz, M. (2025). "Optimal execution among N traders with transient price impact." [arXiv:2501.09638](https://arxiv.org/abs/2501.09638)
14. Cartea, Á. & del-Castillo-Negrete, D. (2007). "Fractional diffusion models of option prices in markets with jumps." *Physica A* 374, 749–763. [SSRN:934809](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=934809)
15. Cheridito, P. (2003). "Arbitrage in fractional Brownian motion models." *Finance & Stochastics* 7, 533–553. [Springer](https://link.springer.com/article/10.1007/s007800300101)
16. Chevalier, E., Hafsi, Y., Ly Vath, V. & Pulido, S. (2025). "Optimal execution under liquidity uncertainty." [arXiv:2506.11813](https://arxiv.org/abs/2506.11813)
17. Comte, F. & Renault, E. (1998). "Long memory in continuous-time stochastic volatility models." *Math. Finance* 8, 291–323.
18. Czichowsky, C., Peyre, R., Schachermayer, W. & Yang, J. (2018). "Shadow prices, fractional Brownian motion, and portfolio optimisation under transaction costs." *Finance & Stochastics* 22(1).
19. Di Nunno, G., Kubilius, K., Mishura, Yu. & Yurchenko-Tytarenko, A. (2023). "From constant to rough: A survey of continuous volatility modeling." [arXiv:2309.01033](https://arxiv.org/abs/2309.01033)
20. Dro, S.B. & Gnabeyeu, E. (2026). "Optimal Merton's problem under multivariate affine Volterra models with jumps." [arXiv:2605.00688](https://arxiv.org/abs/2605.00688)
21. El Euch, O. & Rosenbaum, M. (2019). "The characteristic function of rough Heston models." *Math. Finance* 29, 3–38. [arXiv:1609.02108](https://arxiv.org/abs/1609.02108)
22. Gatheral, J. (2010). "No-dynamic-arbitrage and market impact." *Quantitative Finance* 10(7), 749–759.
23. Gatheral, J., Jaisson, T. & Rosenbaum, M. (2018). "Volatility is rough." *Quantitative Finance* 18(6), 933–949. [arXiv:1410.3394](https://arxiv.org/abs/1410.3394)
24. Gatheral, J., Schied, A. & Slynko, A. (2012). "Transient linear price impact and Fredholm integral equations." *Math. Finance* 22(3), 445–474. [SSRN:1531466](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1531466)
25. Gnabeyeu, E. (2026). "On the mean-variance problem through the lens of multivariate fake stationary affine Volterra dynamics." [arXiv:2604.01300](https://arxiv.org/abs/2604.01300)
26. Gomoyunov, M.I. (2020). "Dynamic programming principle and Hamilton–Jacobi–Bellman equations for fractional-order systems." *SIAM J. Control Optim.* [DOI:10.1137/19M1279368](https://epubs.siam.org/doi/10.1137/19M1279368)
27. Gomoyunov, M.I. (2023). "On the relationship between the Pontryagin maximum principle and the HJB equation for fractional-order systems." *Differential Equations* 59, 1520–1526. [Springer](https://link.springer.com/article/10.1134/S0012266123011006X)
28. Guasoni, P. (2006). "No arbitrage under transaction costs, with fractional Brownian motion and beyond." *Math. Finance* 16, 569–582.
29. Guasoni, P., Mishura, Y. & Rásonyi, M. (2021). "High-frequency trading with fractional Brownian motion." *Finance & Stochastics* 25(2). [Springer](https://link.springer.com/article/10.1007/s00780-020-00439-y)
30. Guo, I. & Jin, S. (2025). "Optimal execution and macroscopic market making." [arXiv:2504.06717](https://arxiv.org/abs/2504.06717)
31. Han, B. & Wong, H.Y. (2021). "Merton's portfolio problem under Volterra Heston model." *Finance Research Letters* 39. [RePEc](https://ideas.repec.org/a/eee/finlet/v39y2021ics1544612319312917.html)
32. Hu, Y., Øksendal, B. & Sulem, A. (2003). "Optimal consumption and portfolio in a Black–Scholes market driven by fBm." *Infinite Dimensional Anal., Quantum Probab. & Related Topics* 6(4).
33. Huang, Y., Jia, Y. & Zhou, X.Y. (2024). "Sublinear regret for a class of continuous-time linear-quadratic reinforcement learning problems." [arXiv:2407.17226](https://arxiv.org/abs/2407.17226)
34. Kalsi, J., Lyons, T. & Perez Arribas, I. (2020). "Optimal execution with rough path signatures." *SIAM J. Financial Math.* [arXiv:1905.00728](https://arxiv.org/abs/1905.00728)
35. Lamert, K., Auer, B.R. & Wunderlich, R. (2025). "Discretization of continuous-time arbitrage strategies in financial markets with fractional Brownian motion." *Math. Methods Oper. Res.* 101(2), 163–218. [arXiv:2311.15635](https://arxiv.org/abs/2311.15635)
36. Mainardi, F. (2020). "On the advent of fractional calculus in econophysics via continuous-time random walk." *Mathematics* 8(4), 641. [MDPI](https://www.mdpi.com/2227-7390/8/4/641)
37. Mandelbrot, B.B. & Van Ness, J.W. (1968). "Fractional Brownian motions, fractional noises and applications." *SIAM Review* 10, 422–437.
38. Micheli, A. & Monod, M. (2024). "Deep reinforcement learning for online optimal execution strategies." [arXiv:2410.13493](https://arxiv.org/abs/2410.13493)
39. Muhle-Karbe, J., Ouazzani Chahdi, Y., Rosenbaum, M. & Szymanski, G. (2026). "A unified theory of order flow, market impact, and volatility." [arXiv:2601.23172](https://arxiv.org/abs/2601.23172)
40. Obizhaeva, A.A. & Wang, J. (2013). "Optimal trading strategy and supply/demand dynamics." *J. Financial Markets* 16, 1–32.
41. Ouazzani Chahdi, Y., De Carvalho, N. & Szymanski, G. (2026). "Trading with market resistance and concave price impact." [arXiv:2601.03215](https://arxiv.org/abs/2601.03215)
42. Rogers, L.C.G. (1997). "Arbitrage with fractional Brownian motion." *Math. Finance* 7, 95–105.
43. Rosenbaum, M. & Zhang, J. (2022/2025). "Multi-asset market making under the quadratic rough Heston." [arXiv:2212.10164](https://arxiv.org/abs/2212.10164)
44. Scalas, E., Gorenflo, R. & Mainardi, F. (2000). "Fractional calculus and continuous-time finance." *Physica A* 284, 376–384.
45. Webb, A. (2024). "Applications of fractional stochastic volatility models to market microstructure theory and optimal execution strategies." *Front. Appl. Math. Stat.* 10:1456746. [Frontiers](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2024.1456746/full)
46. Xodarev, A. (2026). "On the structural foundations of signature volatility models." [arXiv:2605.17142](https://arxiv.org/abs/2605.17142)
