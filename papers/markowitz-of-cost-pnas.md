# Fractional Derivatives as the Markowitz Rule for Cost-Managed Trading

**Authors:** TBD

**Classification:** Physical Sciences — Applied Mathematics / Economic Sciences.

**Keywords:** optimal execution; market impact; fractional calculus; Wiener–Hopf factorization; portfolio theory.

---

## Significance Statement

Trading a portfolio is subject to two fundamental limitations: the risk of the positions held and the cost of the trades that establish them. Markowitz's mean–variance theory gives the closed-form solution for the first, trading expected return against variance. We give the corresponding closed form for the second problem: an execution schedule that trades expected gain from a return-predicting signal against the impact cost of one's own trades. Non-locality of the impact operator and the requirement that the schedule use only past information necessitate a filtration Wiener–Hopf factorization, the causal-realization tool of Wiener–Kolmogorov prediction. For the empirically supported power-law impact kernel, the optimal trading rate is a fractional derivative of the signal, of order set by the impact-decay exponent.

---

## Abstract

Portfolio management trades expected gain against two frictions: risk and cost. Markowitz's mean–variance theory solves the pure gain–risk tradeoff in closed form, giving the portfolio that maximizes expected return net of variance. We solve the pure gain–cost tradeoff in closed form: the trading schedule that maximizes expected gain from a return-predicting signal net of the impact cost of its own trades. The two problems share the same convex-quadratic structure, with the impact operator in the role of the return covariance, and differ in one respect: the schedule at each time must use only information available then, so the unconstrained analog of the Markowitz portfolio, obtained by inverting the impact operator, draws on inaccessible future values of the signal. Using a version of the Wiener–Hopf method for stochastic processes, we obtain a closed-form optimal trading rate for a stationary adapted signal; for the empirically supported power-law impact kernel it reduces to a fractional derivative of the trader's forecast curve.

---

## 1. Introduction

### 1.1 Optimal trading against a signal

Institutional trading in equity, futures, and cash markets routinely involves parent orders whose size exceeds by orders of magnitude the volume resting at the top of the visible order book. A portfolio rebalance, an index-fund inflow, or an algorithmic strategy trading on a short-horizon forecast can generate a target position that must be broken into many small child orders and executed over minutes, hours, or days. Empirical studies of trade-and-quote data since the early 2000s (1, 2, 3, 4) have established that each child order pushes the mid-price against the trader's direction and that the resulting *transient impact* is well described by a translation-invariant propagator $G(t-s)$ that decays with lag: the impact at time $t$ of a trade at time $s < t$ enters as $G(t-s)\,u_s$. The cost of a large parent order therefore depends on the whole path of its execution schedule, not only on its instantaneous rate.

When the trader also possesses a return-predicting signal $\alpha_t$ — a short-horizon forecast of price change conditional on time-$t$ information — the execution problem becomes non-trivial. Trading aggressively captures the predictive content of the signal but generates impact cost; trading conservatively saves impact but forfeits gain. Under the propagator model of Bouchaud, Gefen, Potters and Wyart, later extended by Gatheral (2, 3), which represents the executed price as $P_t = P^{(0)}_t + \int_{s\le t} G(t-s)\, u_s\,ds$ with $P^{(0)}$ the unimpacted price, the expected P\&L of an adapted trading policy $u\in L^2_{\rm adap}$ amounts to a linear gain against a quadratic cost, and the resulting *gain–cost problem* is
$$ \max_{u\in L^2_{\rm adap}}\ \mathbb{E}\!\int u_t\,\alpha_t\,dt \;-\; \tfrac{\gamma}{2}\,\mathbb{E}\!\iint G(|t-v|)\, u_t\, u_v\,dt\,dv. \tag{1} $$
The linear term is expected gain from trading in the signal's direction; the quadratic term is the expected impact cost of the policy, symmetrized to reflect price-averaging across the horizon (see §2.1). The scalar $\gamma > 0$ is a cost-aversion coupling. Write $C$ for the symmetric convolution operator $(Cu)(t) = \int G(|t-v|)\,u_v\,dv$ and $\hat C(\xi)$ for its Fourier symbol; $C$ must be positive-definite ($\hat C \ge 0$) to rule out static round-trip arbitrage. We use the Fourier convention $\hat f(\xi) = \int e^{i\xi t}f(t)\,dt$ throughout, under which the Fourier transform of a causal function (support in $t\ge 0$) is analytic in the upper half-plane $\{\operatorname{Im}\xi > 0\}$.

The two kernels developed in §2 are the empirically supported power law $G(t) = |t|^{-\beta}$, $\beta\in(0,1)$ estimated in the range $0.2$–$0.6$ across markets and asset classes (1, 2, 3, 4), with Fourier symbol $\hat C(\xi) = c_\beta|\xi|^{\beta-1}$, $c_\beta := 2\Gamma(1-\beta)\sin(\pi\beta/2)$; and the exponential kernel $G(t) = e^{-\kappa|t|}$, $\kappa>0$, which serves as the tractable one-parameter benchmark used in much of the theoretical execution literature (7, 9). The power-law form matches the observed slow decay of impact tails and produces the fractional-derivative closed form of §2.7; the exponential form recovers a first-order operator with different qualitative behavior in the sign of the optimal trade.

**Optimal execution versus optimal trading.** Two problems share formulation (1) under different feasibility constraints. *Optimal execution* fixes a target quantity $X_0$ and horizon $T$ and imposes $\int_0^T u_t\,dt = -X_0$; the optimizer is driven by the terminal-inventory constraint and boundary layers at $t=0$ and $t=T$, with the signal entering as a perturbation of the constraint-driven schedule. *Optimal trading* takes only the signal $\alpha$ and asks for the schedule that maximizes gain net of cost with no fixed quantity to deliver; boundary conditions are then irrelevant and the optimizer is a stationary functional of $\alpha$. We solve the trading problem on the whole line; the execution problem is recovered as a boundary-corrected specialization (Section 3.1).

**Analogy with mean–variance portfolio choice.** Problem (1) has the same convex-quadratic structure as the mean–variance portfolio problem of Markowitz (5, 6),
$$ \max_{w\in\mathbb{R}^N}\ w^\top\mu \;-\; \tfrac{1}{2}\lambda\, w^\top\Sigma w, \tag{2} $$
in which a portfolio manager trades expected return $w^\top\mu$ against portfolio variance $\tfrac{1}{2}\lambda w^\top\Sigma w$. Both problems maximize a linear gain minus a positive-definite quadratic penalty, and the correspondence
$$ (w,\,\mu,\,\Sigma,\,\lambda) \;\longleftrightarrow\; (u,\,\alpha,\,C,\,\gamma) $$
matches their first-order conditions term-for-term, with $\lambda$ the Markowitz risk aversion and $\gamma$ the execution cost aversion. Both problems inherit a structural identity from Euler homogeneity: gain is linear in the decision variable and cost is quadratic, so at any stationary point of a gain–cost objective
$$ \text{gain} \;=\; 2\,\text{cost}, \qquad \text{net value} \;=\; \text{cost} \;=\; \tfrac12\,\text{gain}. $$
In Markowitz this reads $\tfrac{1}{2\lambda}\mu^\top\Sigma^{-1}\mu$; the same identity holds in (1) at the unconstrained optimum $u^\star = \gamma^{-1}C^{-1}\alpha$. The Markowitz solution $w^\star = \lambda^{-1}\Sigma^{-1}\mu$ suggests the analog $u^\star = \gamma^{-1} C^{-1}\alpha$. Two features of the execution problem obstruct this analogy.

*(i) Non-locality of the Hessian.* $\Sigma$ is a symmetric positive-definite matrix on $\mathbb{R}^N$; $C$ is a temporal convolution against a symmetric kernel $G$, so $(Cu)(t) = \int G(|t-v|)\,u_v\,dv$ depends on $u_v$ for $v$ both before and after $t$.

*(ii) Causality of the feasible set.* The Markowitz feasible set $\mathbb{R}^N$ imposes no ordering on the components of $w$; the execution feasible set $L^2_{\rm adap}$ requires the schedule $u_t$ at time $t$ to be $\mathcal{F}_t$-measurable. Computing $(C^{-1}\alpha)_t$ requires knowledge of $\alpha_s$ for $s > t$, which the trader does not have.

**Convex duality and dual norms.** The Hessian $C$ defines a symmetric positive-definite quadratic form on trading rates,
$$ \|u\|_C^2 := \langle u,\,Cu\rangle = \iint G(|t-v|)\, u_t\, u_v\, dt\, dv, \tag{3} $$
which we call the *cost norm*: the quadratic term of (1) is $\tfrac{\gamma}{2}\|u\|_C^2$. Its convex dual, obtained by Legendre transform of the quadratic cost, is a norm on signals
$$ \|\alpha\|_{C^{-1}}^2 := \langle\alpha,\, C^{-1}\alpha\rangle, \tag{4} $$
which we call the *tradeability norm*: the value of the unconstrained problem $\sup_u\langle u,\alpha\rangle - \tfrac{\gamma}{2}\|u\|_C^2$ equals $\tfrac{1}{2\gamma}\|\alpha\|_{C^{-1}}^2$, attained at $u = \gamma^{-1}C^{-1}\alpha$. This scalar is the exact counterpart of the portfolio value $\tfrac{1}{2\lambda}\|\mu\|_{\Sigma^{-1}}^2$ attained at $w^\star = \lambda^{-1}\Sigma^{-1}\mu$, where $\|\mu\|_{\Sigma^{-1}}^2 = \mu^\top\Sigma^{-1}\mu$ is the Mahalanobis norm of the expected return with respect to the return covariance. Section 2 shows that under the adaptedness constraint, $C^{-1}$ is replaced by $(P_+ C P_+)^{-1} = C_+^{-1} P_+ C_-^{-1}$; for the power-law kernel the value of (1) becomes the fractional Sobolev $H^{(1-\beta)/2}$-norm of the forecast curve.

### 1.2 The optimal execution literature

Problem (1) has been studied under several kernel and signal specifications, all on a bounded interval $[0,T]$ with a terminal-inventory constraint. The constant-signal version (stochastic $\alpha \equiv 0$, effective signal supplied by a terminal-inventory KKT multiplier) with power-law kernel was solved by Gatheral, Schied and Slynko (7) using Fredholm techniques, giving the U-shaped VWAP-type schedule with $(t(T-t))^{(\beta-1)/2}$ boundary layers. Signal-adaptive execution against an *exponential* impact kernel with a general semimartingale signal was solved by Neuman and Voß (8): the exponential kernel reduces the problem to a finite-dimensional linear–quadratic control via Markovian state augmentation, with a Riccati closed form. The general propagator case with an adapted signal was formulated by Abi Jaber and Neuman (9) and treated by infinite-dimensional stochastic control; closed forms are available only in specific specializations. Extensions to matrix-valued cross-impact propagators (10) and to constrained trading with multiple signals and battery-storage applications (11) proceed within the same operator-resolvent framework. On the mathematical side, Forde, Sánchez-Betancourt and Smith (12) observed that the constant-signal Fredholm operator on a bounded interval factorizes through a half-order Riemann–Liouville integral, giving the Söhngen–Tricomi closed form; the relationship between this half-order factorization and the signal-adaptive problem has not been made explicit. Wiener–Hopf and Krein factorization are classical tools in the deterministic control and time-series prediction literature (13–15); their use in the stochastic-signal, filtration-adapted setting has been limited.

Across these treatments the trade rate is expressed as the solution of a Fredholm equation on $[0,T]$, as an integral against a resolvent whose kernel depends on $T$, or as Riccati feedback with terminal state at $T$. Söhngen–Tricomi boundary weights $(t(T-t))^{(\beta-1)/2}$ and terminal-inventory KKT multipliers appear explicitly, and the dependence on the forecast enters through these horizon-tied objects. The whole-line stationary limit isolates a horizon-independent bulk term as an operator acting directly on the forecast curve, which we compute in Section 1.3.

### 1.3 Contribution

We study (1) on the whole line with a stationary adapted signal and give a closed-form solution for its bulk term. Removing the horizon converts the Fredholm equation on $[0,T]$ into a translation-invariant convolution equation on $\mathbb{R}$; the terminal-inventory multiplier and the Söhngen–Tricomi boundary weights drop out, leaving an operator identity that maps the adapted forecast curve to the trade rate. Three points delimit the contribution:

**(i) Bulk term for a general adapted signal.** We work on $\mathbb{R}$ with a stationary adapted signal $\alpha$ and solve (1) in closed form. Linear position constraints — such as the terminal-inventory constraint $\int u_t\,dt = -X_0$ that has driven much of the classical literature — are absorbed into (1) as additive components of the effective signal, one component per constraint, with the constraint's adjoint kernel setting its shape and the KKT multiplier setting its coefficient. The Almgren–Chriss and Gatheral–Schied–Slynko schedules correspond to the constant effective signal produced by a terminal-inventory KKT multiplier; our closed form contains them as the finite-horizon interior asymptotic (Section 3.1).

**(ii) Stochastic-processes Wiener–Hopf.** The adapted first-order condition $\mathbb{E}_t[(Cu^\star)(t)] = \alpha_t$ is solved by a filtration Wiener–Hopf factorization $C = C_- C_+$ into an anticausal and a causal half. The identity we exploit is
$$ (P_+ C P_+)^{-1} = C_+^{-1}\, P_+\, C_-^{-1}, \tag{5} $$
with $P_+$ the $L^2(\Omega\times\mathbb{R})$-orthogonal projection onto adapted processes; pointwise, $(P_+X)_s = \mathbb{E}_s[X_s]$, which coincides with the optional projection restricted to $L^2$. It is the stochastic-processes analog of the deterministic Wiener–Hopf inversion of half-line convolutions (13–15), transferred to the adapted subspace via nest-algebra outer factorization (16, 17). The whole-line stationary case treated here sits outside the bounded-horizon setup of (9), and (5) is the closed-form identity that replaces their resolvent characterization in this regime.

**(iii) Fractional calculus.** For the power-law case, the Fourier symbol $\hat C(\xi) = c_\beta|\xi|^{\beta-1}$ factorizes explicitly as $c_\beta\,(i\xi)^{-\nu}(-i\xi)^{-\nu}$ with $\nu = (1-\beta)/2$, whose time-domain Wiener–Hopf halves are the causal and anticausal Marchaud fractional integrals $I_\pm^\nu$ (18). Substituting into (5) collapses the operator formula into a fractional derivative of the signal of total order $1-\beta$: writing $\bar\alpha(s,\cdot)$ for the trader's forecast curve at time $s$,
$$ u^\star_t = \gamma^{-1}\kappa_{1-\beta}\,(D_+^\nu\zeta)(t), \qquad \zeta_s = (D_-^\nu\bar\alpha(s,\cdot))(s), \tag{6} $$
with $\kappa_{1-\beta} = [2\Gamma(1-\beta)\sin(\pi\beta/2)]^{-1}$. The intermediate $\zeta$ has stationary power spectrum $c_\beta^{-1}|\xi|^{1-\beta}S_\alpha(\xi)$: fractional differentiation cancels the frequency dependence of the impact operator, and $u^\star$ is the causal re-coloring of the whitened forecast. The half-order factorization was implicit in (12); the explicit reduction of the signal-adaptive optimizer to a fractional derivative of the forecast curve is new.

The three-step architecture — whiten by $C_-^{-1}$, project onto the past, un-whiten by $C_+^{-1}$ — parallels Wiener–Kolmogorov linear prediction of a stationary process from its own past (15), with the cost-outer factor $C_+$ replacing the spectral square root $S_+$ of the process. Table 1 summarizes the correspondence with mean–variance portfolio choice; the last three rows record what causality adds.

**Table 1.** Structural correspondence between Markowitz portfolio theory and cost-optimal execution.

| Object | Markowitz | Cost-optimal execution |
|---|---|---|
| Predictor | Expected return $\mu \in \mathbb{R}^N$ | Forecast curve $\bar\alpha(t,\cdot)$ |
| Hessian | Return covariance $\Sigma$ | Impact operator $C$ |
| Scalar coupling | Risk aversion $\lambda$ | Cost aversion $\gamma$ |
| Unconstrained optimum | $\lambda^{-1}\Sigma^{-1}\mu$ | $\gamma^{-1}C^{-1}\alpha$ (not adapted) |
| Whitening (geometric) | $\Sigma^{-1/2}\mu$ (symmetric, optional) | $C_-^{-1}\alpha$ (causal, forced) |
| Feasibility constraint | $\mathbb{R}^N$ or polyhedral (long-only, sector caps) | Adaptedness $L^2_{\rm adap}$ (nested in time) |
| Structure forced by feasibility | KKT / active set on the polyhedron | WH factorization $C = C_-C_+$ and projection $P_+$ |
| Feasible optimum | $\lambda^{-1}\Sigma^{-1}\mu$ (or its KKT projection) | $\gamma^{-1}C_+^{-1}P_+C_-^{-1}\alpha$ |
| Value | $\tfrac{1}{2\lambda}\|\mu\|_{\Sigma^{-1}}^2$ | $\tfrac{1}{2\gamma}\|P_+ C_-^{-1}\alpha\|_{L^2}^2$ |

---

## 2. The Adapted Wiener–Hopf Factorization

### 2.1 Setting

Fix a filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t\in\mathbb{R}}, \mathbb{P})$. The signal $\alpha \in L^2_{\rm adap}(\mathbb{R})$ is a mean-zero progressive process with spectral density $S_\alpha(\xi)$ satisfying appropriate integrability against $\hat C$. The forecast curve is

$$ \bar\alpha(t,s) = \begin{cases}\alpha_s, & s\le t,\\ \mathbb{E}_t[\alpha_s], & s > t.\end{cases} \tag{7} $$

The cost operator $C$ is convolution against a symmetric positive-definite kernel with symbol $\hat C(\xi) \ge 0$. Positive-definiteness rules out static round-trip arbitrage. Two kernels run through the paper:

- **Power-law.** $G(t) = |t|^{-\beta}$, $\beta \in (0,1)$; $\hat C(\xi) = c_\beta|\xi|^{\beta-1}$, $c_\beta = 2\Gamma(1-\beta)\sin(\pi\beta/2)$.
- **Exponential.** $G(t) = e^{-\kappa|t|}$, $\kappa > 0$; $\hat C(\xi) = 2\kappa/(\kappa^2 + \xi^2)$.

### 2.2 The adapted first-order condition

Testing the Gâteaux derivative of (1) against adapted variations $\delta u \in L^2_{\rm adap}$ and using the tower property yields the conditioned first-order condition

$$ \gamma\,\mathbb{E}_t\!\bigl[(Cu^\star)(t)\bigr] = \alpha_t, \qquad t \in \mathbb{R}. \tag{8} $$

Equation (8) is the temporal analog of the Markowitz normal equation $\lambda\Sigma w^\star = \mu$, with conditional expectation projecting the non-local left-hand side onto the current information set.

### 2.3 Wiener–Hopf factorization

The symbol $\hat C(\xi) \ge 0$ admits a multiplicative factorization

$$ \hat C(\xi) = \hat C_-(\xi)\, \hat C_+(\xi), \tag{9} $$

where $\hat C_+$ is analytic and non-vanishing in the closed upper half-plane (equivalently, $C_+$ is causal: kernel supported on $\{s \le t\}$), $\hat C_-$ is analytic in the closed lower half-plane, and $\hat C_-(\xi) = \overline{\hat C_+(\xi)}$ under $C_+^\ast = C_-$. The factorization is unique up to a positive multiplicative constant. Existence follows from Krein's theorem (14) when $\log\hat C$ is integrable against $(1+\xi^2)^{-1}$; the power-law symbol is treated via the regularization $c_\beta|\xi|^{\beta-1}+\varepsilon$ with the pure-power factors recovered as $\varepsilon\to 0$.

### 2.4 The projected inverse

**Lemma 1 (Adapted inverse via Wiener–Hopf).** *Let $C$ admit the factorization $C = C_- C_+$ with $C_+^\ast = C_-$. Then on the adapted subspace $L^2_{\rm adap}(\mathbb{R})$,*

$$ (P_+ C P_+)^{-1} = C_+^{-1}\, P_+\, C_-^{-1}, \tag{10} $$

*where $P_+$ is the $L^2(\Omega\times\mathbb{R})$-orthogonal projection onto adapted processes, equivalent on $L^2$ to the optional projection.*

Proof in Section 5.

### 2.5 The optimal adapted policy

Applying (10) to (8):

**Theorem 1 (Bulk theorem).** *Under the hypotheses of §2.1, the unique adapted minimizer of (1) is*

$$ u^\star \;=\; \gamma^{-1}\, C_+^{-1}\, P_+\, C_-^{-1}\, \alpha. \tag{11} $$

Proof in Section 5.

The acausal factor $C_-^{-1}\alpha$ evaluated at time $s$ requires the future path of $\alpha$; the adapted projection $P_+$ replaces it by the conditional expectation $\mathbb{E}_s[(C_-^{-1}\alpha)(s)]$, which by commutation of the deterministic operator $C_-^{-1}$ with conditional expectation on the $s$-variable [21, Prop. 2.6.13] equals $(C_-^{-1}\bar\alpha(s,\cdot))(s)$. The forecast curve enters only through this inner step. The outer $C_+^{-1}$ then samples the adapted process $\zeta_s := (C_-^{-1}\bar\alpha(s,\cdot))(s)$ over $s\le t$, giving an $\mathcal{F}_t$-adapted rate at every $t$.

### 2.6 Exponential kernel

For $G(t) = e^{-\kappa|t|}$ the factors are $\hat C_\pm(\xi) = \sqrt{2\kappa}/(\kappa\mp i\xi)$; equivalently the causal inverse is the first-order differential operator $C_+^{-1} = (2\kappa)^{-1/2}(\kappa + \partial_t)$ and $C_-^{-1} = (2\kappa)^{-1/2}(\kappa - \partial_t)$. Theorem 1 becomes

$$ u^{\star,\,\rm exp}_t \;=\; \frac{1}{2\kappa\gamma}\,(\kappa+\partial_t)\,\zeta_t, \qquad \zeta_s \;=\; (\kappa - \partial_r)\,\bar\alpha(s,r)\big|_{r=s^+}. \tag{12} $$

For Ornstein–Uhlenbeck $d\alpha_t = -\theta\alpha_t\,dt + \sigma\,dW_t$, $\bar\alpha(s,r) = e^{-\theta(r-s)}\alpha_s$ gives $\zeta_s = (2\kappa)^{-1/2}(\kappa+\theta)\alpha_s$, and using $\dot\alpha_t = -\theta\alpha_t + \sigma\dot W_t$,

$$ u^{\star,\,\rm exp}_t \;=\; \frac{\kappa+\theta}{2\kappa\gamma}\bigl[(\kappa-\theta)\alpha_t + \sigma\dot W_t\bigr], \qquad \mathbb{E}\bigl[u^{\star,\,\rm exp}_t \,\bigm|\, \alpha_t\bigr] \;=\; \frac{\kappa^2 - \theta^2}{2\kappa\gamma}\,\alpha_t. \tag{13} $$

The conditional expectation flips sign at $\theta = \kappa$: for $\theta<\kappa$ the optimizer trades in the direction of the signal on average; for $\theta>\kappa$ it trades against the current signal on average, because the impact tail from any signal-following trade would outlive the signal itself. At the phase boundary $\theta=\kappa$ the level term vanishes and trading is driven only by the innovation.

### 2.7 Power-law kernel

For $G(t) = |t|^{-\beta}$ the symbol factorizes as $\hat C_\pm(\xi) = c_\beta^{1/2}(\mp i\xi)^{-\nu}$ with $\nu = (1-\beta)/2$; the time-domain factors are the Riemann–Liouville fractional integrals $C_\pm = c_\beta^{1/2} I_\pm^\nu$, and their inverses are the Marchaud fractional derivatives $D_\pm^\nu$ (18, §5.4). Theorem 1 becomes a fractional derivative of total order $1-\beta$:

$$ u^{\star,\,\rm pow}_t \;=\; \gamma^{-1}\kappa_{1-\beta}\,(D_+^\nu\zeta)(t), \qquad \zeta_s \;=\; \bigl(D_-^\nu\bar\alpha(s,\cdot)\bigr)(s), \tag{14} $$

with $\kappa_{1-\beta} = [2\Gamma(1-\beta)\sin(\pi\beta/2)]^{-1}$. The intermediate $\zeta$ has stationary power spectrum $c_\beta^{-1}|\xi|^{1-\beta}S_\alpha(\xi)$: fractional differentiation cancels the frequency dependence of the impact operator, and $u^\star$ is the causal re-coloring of the whitened forecast. For OU $\alpha$, direct Marchaud integration against the exponential forecast tail gives $(D_-^\nu\bar\alpha(t,\cdot))(t) = \theta^\nu\alpha_t$ and

$$ u^{\star,\,\rm OU}_t \;=\; \gamma^{-1}\kappa_{1-\beta}\,\theta^\nu\,(D_+^\nu\alpha)(t), \qquad \mathbb{E}\bigl[u^{\star,\,\rm OU}_t \,\bigm|\, \alpha_t\bigr] \;=\; \gamma^{-1}\kappa_{1-\beta}\,\theta^{1-\beta}\,\alpha_t. \tag{15} $$

Unlike the exponential case, the conditional expectation is positive for every $\beta\in(0,1)$ and every $\theta>0$: the scale-free causal inverse $(-i\xi)^\nu$ has a branch point at $\xi=0$ and no zero on the imaginary axis, so no zero–pole crossing with the OU spectral pole occurs as $\theta$ varies, and no sign-flip phase transition exists. In the Marchaud representation, $D_+^\nu$ averages the increments $\alpha_t - \alpha_{t-r}$ over all past scales $r$; each increment is same-signed as $\alpha_t$ in conditional expectation under mean-reverting stationarity, and the multiscale average erases the local level–rate anti-correlation that drives the sign flip at first order.

---

## 3. Discussion

### 3.1 Boundary corrections

Equation (12) holds on $\mathbb{R}$ for a stationary adapted signal. On a bounded horizon $[0,T]$, linear position constraints on the schedule enter (1) through Lagrange multipliers. Each scalar constraint of the form $\int_0^T \psi_k(t)\, u_t\,dt = c_k$ contributes an additive component $\mu_k \psi_k$ to the effective signal,
$$ \alpha^{\rm eff}_t = \alpha_t + \sum_k \mu_k\, \psi_k(t), \qquad t \in [0,T], $$
with $\psi_k$ the constraint's adjoint kernel and $\mu_k$ its Lagrange multiplier. Terminal inventory $\int_0^T u_t\,dt = -X_0$ gives $\psi_1(t) = \mathbf{1}_{[0,T]}(t)$. On the finite interval, (11) is replaced by a Fredholm equation on $[0,T]$; strict positivity of $\hat C$ on $\xi\ne 0$ makes the finite-interval operator $P_{[0,T]}CP_{[0,T]}$ symmetric positive-definite on $L^2([0,T])$, and the effective-signal Fredholm equation is well-posed for every $\alpha^{\rm eff}\in L^2([0,T])$. The solution splits into a bulk term of the form (12) applied to $\alpha^{\rm eff}$ plus a contribution from the two-dimensional nullspace of the free-boundary fractional-derivative operator on $[0,T]$, spanned by the Söhngen–Tricomi modes $\phi_1(t) = (t(T-t))^{(\beta-1)/2}$ and $\phi_2(t) = \tfrac{T-2t}{2}\phi_1(t)$ (19, 20) — the classical solutions of the airfoil integral equation; the KKT multipliers $\{\mu_k\}$ fix the coefficients of these modes.

**Note on the Söhngen–Tricomi modes.** The finite-interval version of the cost operator, $u\mapsto\int_0^T G(|t-v|)u_v\,dv$, is not invertible: two directions in $L^2([0,T])$ produce zero cost gradient in the interior, and any schedule can be shifted along them without changing the interior first-order condition. For the power-law kernel these two directions are
$$ \phi_1(t) = \bigl(t(T-t)\bigr)^{(\beta-1)/2}, \qquad \phi_2(t) = \tfrac{T-2t}{2}\,\phi_1(t), \qquad t\in(0,T), $$
both integrable and both blowing up at the endpoints $t=0$ and $t=T$ (integrable singularities of order $(\beta-1)/2$). $\phi_1$ is symmetric about the midpoint and models a U-shaped schedule with mass concentrated near the two endpoints; $\phi_2$ is antisymmetric and models a schedule that pushes toward one endpoint and pulls back from the other. They arise historically as the two homogeneous solutions of the airfoil integral equation for the pressure jump across a thin airfoil in incompressible flow (Söhngen, 1939; Tricomi, 1951), where they encode the two degrees of freedom in fitting the flow to leading- and trailing-edge boundary data. In the execution problem they play the same role: their coefficients are set by the endpoint constraints of the schedule (initial and terminal inventory), and interior variations orthogonal to $\alpha^{\rm eff}$ can be absorbed into them at no cost.

 Forde–Sánchez-Betancourt–Smith (12) treat the finite-horizon problem via a half-order Riemann–Liouville factorization and show that for fixed $X_0$ and bounded stochastic signal the KKT coefficients solving the two-mode linear system are bounded uniformly in $T$ for signals with $\Theta(1)$ tradeability norm (12, Prop. 3.2); combined with the $L^2([\varepsilon T,(1-\varepsilon)T])$-norm scaling $T^{\beta-1/2}$ of $\phi_{1,2}$, the boundary contribution is $o(1)$ on interior regions in the long-horizon limit, and (12) is the interior asymptotic.

### 3.2 Temporary impact

Adding a temporary-impact term $\tfrac12 \eta u_t^2$ to the cost — modelling instantaneous liquidity charged in addition to the propagator kernel — modifies the FOC symbol to $M(\xi) = c_\beta|\xi|^{\beta-1} + \eta/\gamma$. The added $\eta/\gamma$ term provides high-frequency coercivity that the pure power-law symbol lacks, so the optimal rate is now in $L^2$ without any spectral-decay assumption on $\alpha$. Krein factorization of $M$ yields a modified pair of one-sided factors; the crossover frequency $\xi_\ast = (\gamma c_\beta/\eta)^{1/(1-\beta)}$ separates a long-memory fractional regime ($|\xi| \ll \xi_\ast$) from a myopic signal-following regime ($|\xi| \gg \xi_\ast$) in which $u^\star_t \approx \alpha_t/\eta$. The $\eta \to 0$ limit is singular (high-frequency coercivity is lost) but under the spectral-decay hypothesis of §2.1 recovers (12).

### 3.3 Multi-asset extension

For a cross-impact kernel $\mathbf{K}(t) = |t|^{-\beta}\mathbf{A}$ with $\mathbf{A} = Q\Lambda Q^\top$ symmetric positive-definite, Theorem 1 diagonalizes in the eigenbasis of $\mathbf{A}$: the scalar fractional-derivative rule applies independently to each principal-component alpha with an eigenvalue prefactor.

### 3.4 Numerical implementation

Fractional derivatives discretize to Toeplitz matrix operations. On a uniform grid of $N$ points, $D_\pm^\nu$ is a lower- or upper-triangular Toeplitz matrix whose entries are generalized binomial coefficients from the expansion of $(1-z)^\nu$. Evaluating (12) costs $O(N\log N)$ per time step via FFT, compared with $O(N^2)$ Nyström inversion of the Fredholm equation.

---

## 4. Concluding remarks

The gain–cost tradeoff has the same convex-quadratic architecture as the gain–risk tradeoff Markowitz closed in 1952: an inverse Hessian applied to expected return, a Mahalanobis norm as the value function, a feasibility constraint fixing the form of the inverse. In the temporal problem the constraint is adaptedness, and the inverse-Hessian identity carries a projection $P_+$ between the two Wiener–Hopf halves. For the power-law kernel the closed form is a fractional derivative of order $1-\beta$ applied to the forecast curve — one operator that converts any signal timescale into an optimal-trade timescale, with no tuning per signal.

Two practical implications follow. First, a signal's economic value depends on its interaction with the impact kernel through a spectral high-pass: the identity $V(\alpha) = \tfrac{1}{2\gamma}\|P_+ C_-^{-1}\alpha\|^2$ weights the forecast spectrum by $|\xi|^{1-\beta}$, so a fast-decaying OU signal of unit variance carries value $\propto\theta^{1-\beta}$, larger than a slow-decaying one; two signals with identical $R^2$ against future returns can differ arbitrarily in tradeable value once their timescales differ. Second, the qualitative gap between the two kernels — sign-flip phase boundary at $\theta=\kappa$ under the exponential, no boundary under the power law — turns the choice of impact model into a strategy-prescription choice: the same OU signal is followed on average under one kernel and fought on average under the other when its decay is faster than impact resilience.

The joint gain–risk–cost problem inherits the same operator structure once the two frictions are placed in the same coordinates. Cost acts on the trading rate $u$; a mean–variance holding penalty $\tfrac{\lambda}{2}\mathbb{E}\int x_t^\top\Sigma x_t\,dt$ acts on the position $x_t = \int_{-\infty}^t u_s\,ds$, which in rate coordinates is the operator $\lambda I_+^\ast\Sigma I_+$ with Fourier symbol $\lambda\Sigma/\xi^2$. Adding it to (1) replaces $C$ by the operator with symbol $\gamma\hat C(\xi) + \lambda\Sigma/\xi^2$ — no longer scale-free, with different frequency dependence at high and low frequency, but still a positive Toeplitz operator to which the projected-inverse identity of Lemma 1 applies. Markowitz portfolio choice ($\gamma\to 0$) and cost-optimal trading ($\lambda\to 0$) appear as two limits of this joint factorization, and the joint solution interpolates between them.

---

## 5. Materials and Methods

**Proof of Lemma 1.** The convolution $C$ is a Hilbert-space isomorphism $\dot H^{-\nu}(\mathbb R)\to\dot H^{\nu}(\mathbb R)$ with $\nu=(1-\beta)/2$ by Plancherel and the symbol $\hat C(\xi)=c_\beta|\xi|^{\beta-1}$; the individual factors $C_\pm = c_\beta^{1/2}I_\pm^\nu$ are the corresponding Hilbert-space isomorphisms $L^2(\mathbb R)\to\dot H^\nu(\mathbb R)$ and $\dot H^{-\nu}(\mathbb R)\to L^2(\mathbb R)$, with $C_+^\ast = C_-$ following from the kernel-flip $(t-s)^{\nu-1}\mathbf 1_{s\le t}\mapsto (s-t)^{\nu-1}\mathbf 1_{t\le s}$. On the intersection $L^2_{\rm adap}\cap\dot H^{-\nu}$ the composition $P_+CP_+$ is a bounded, symmetric, strictly positive operator (strict convexity of the quadratic penalty in (1) on $L^2_{\rm adap}$ from $\hat C(\xi)>0$ on $\xi\ne 0$), hence bounded below and boundedly invertible on its range; the two-sided inverse claimed in (11) is therefore well-defined. Causality provides two triangularity identities. First, $P_+^\perp C_+ P_+ = 0$: the kernel of $C_+ = c_\beta^{1/2}I_+^\nu$ is supported on $\{s\le t\}$, so $C_+$ preserves $L^2_{\rm adap}$, and consequently $C_+^{-1}$ commutes with $P_+$ on adapted inputs. Second (adjoint statement, using $C_-=C_+^\ast$), $P_+ C_- P_+^\perp = 0$, whence $P_+ C_-^{-1} = P_+ C_-^{-1} P_+$ on adapted inputs. For $u\in L^2_{\rm adap}$, $P_+ C P_+ u = P_+ C_- C_+ u = P_+ C_- \cdot(C_+ u)$; applying $C_+^{-1} P_+ C_-^{-1}$ gives $C_+^{-1} P_+ C_-^{-1} P_+ C_- (C_+ u) = C_+^{-1}(C_+ u) = u$, since $P_+ C_-^{-1} P_+ C_-$ acts as $P_+$ on the adapted vector $C_+ u$. The nest-algebra outer factorization used above is Arveson's outer factorization theorem for positive Toeplitz operators in a continuous nest (16, Thm 4.4.2; 17, §7.4).

**Proof of Theorem 1.** Define the candidate $u^{\rm cand}_t := \gamma^{-1}\kappa_{1-\beta}(D_+^\nu\zeta)(t)$. Adaptedness: $D_+^\nu$ at time $t$ depends only on $\{\zeta_s\}_{s\le t}$, and each $\zeta_s \in \mathcal{F}_s \subset \mathcal{F}_t$ by (12) and $\mathcal{F}_s$-measurability of the forecast curve. FOC verification proceeds in three steps.

*Step (a).* Conditional Fubini (22, Thm 14.16) applied to the Marchaud representation gives $\mathbb{E}_t[(D_+^\nu\zeta)(v)] = (D_+^\nu \hat\zeta_t)(v)$ with $\hat\zeta_t(s) := \mathbb{E}_t[\zeta_s]$.

*Step (b).* For $s \le t$: $\zeta_s \in \mathcal{F}_s \subset \mathcal{F}_t$, so $\hat\zeta_t(s) = \zeta_s$. For $s > t$: by the tower property and conditional Fubini applied at conditioning time $t$, $\hat\zeta_t(s) = (D_-^\nu\bar\alpha(t,\cdot))(s)$.

*Step (c).* The symbol identity $\hat C(\xi)(-i\xi)^\nu = c_\beta(i\xi)^{-\nu}$ yields the operator identity $C\, D_+^\nu = c_\beta I_-^\nu$ on $L^2(\mathbb{R})$. Substituting and using $\gamma\kappa_{1-\beta} = \gamma/c_\beta$:

$$ \gamma\,\mathbb{E}_t\!\bigl[(Cu^{\rm cand})(t)\bigr] = (I_-^\nu\hat\zeta_t)(t) = (I_-^\nu D_-^\nu\bar\alpha(t,\cdot))(t) = \bar\alpha(t,t) = \alpha_t, $$

using $I_-^\nu D_-^\nu = \text{id}$ on $H^\nu(\mathbb{R})$ (18, §5.3 Thm 5.3) and the fact that $I_-^\nu$ at $t$ samples only $\hat\zeta_t(s)$ for $s \ge t$, where Step (b) gives the closed form.

*Uniqueness.* $\hat C(\xi) = c_\beta|\xi|^{\beta-1} > 0$ on $\xi \ne 0$, so the quadratic penalty in (1) is strictly convex on $L^2_{\rm adap}$ and the adapted FOC has a unique solution.

*Admissibility.* The PSD hypothesis $\int(1+|\xi|^{2(1-\beta)+\epsilon})S_\alpha(\xi)\,d\xi < \infty$ ensures $|\xi|^{1-\beta}\widehat{\bar\alpha}(\xi) \in L^2$ pathwise, so $u^{\rm bulk} \in L^2_{\rm adap}$ by Plancherel. $\blacksquare$

**Data availability.** No empirical data are used in this paper.

---

## References

1. Lillo F, Farmer JD, Mantegna RN (2003) Master curve for price-impact function. *Nature* 421:129–130.
2. Bouchaud J-P, Gefen Y, Potters M, Wyart M (2004) Fluctuations and response in financial markets: The subtle nature of 'random' price changes. *Quant. Finance* 4:176–190.
3. Gatheral J (2010) No-dynamic-arbitrage and market impact. *Quant. Finance* 10:749–759.
4. Jusselin P, Rosenbaum M (2020) No-arbitrage implies power-law market impact and rough volatility. *Math. Finance* 30:1309–1336.
5. Markowitz H (1952) Portfolio selection. *J. Finance* 7:77–91.
6. Merton RC (1972) An analytic derivation of the efficient portfolio frontier. *J. Financial and Quant. Anal.* 7:1851–1872.
7. Gatheral J, Schied A, Slynko A (2012) Transient linear price impact and Fredholm integral equations. *Math. Finance* 22:445–474.
8. Neuman E, Voß M (2022) Optimal signal-adaptive trading with temporary and transient price impact. *SIAM J. Financial Math.* 13:551–575.
9. Abi Jaber E, Neuman E (2025) Optimal liquidation with signals: The general propagator case. *Math. Finance* (arXiv:2211.00447).
10. Abi Jaber E, Neuman E, Tuschmann S (2024) Optimal portfolio choice with cross-impact propagators. arXiv:2403.10273.
11. Abi Jaber E, De Carvalho N, Pham H (2024) Trading with propagators and constraints: Applications to optimal execution and battery storage. arXiv:2409.12098.
12. Forde M, Sánchez-Betancourt L, Smith B (2022) Optimal trade execution for Gaussian signals with power-law resilience. *Quant. Finance* 22:585–596.
13. Wiener N, Hopf E (1931) Über eine Klasse singulärer Integralgleichungen. *S.-B. Preuss. Akad. Wiss. Berlin* 696–706.
14. Krein MG (1962) Integral equations on a half-line with kernel depending upon the difference of the arguments. *Amer. Math. Soc. Transl.* (2) 22:163–288.
15. Wiener N (1949) *Extrapolation, Interpolation and Smoothing of Stationary Time Series* (MIT Press).
16. Arveson W (1975) Interpolation problems in nest algebras. *J. Funct. Anal.* 20:208–233.
17. Davidson KR (1988) *Nest Algebras* (Longman).
18. Samko SG, Kilbas AA, Marichev OI (1993) *Fractional Integrals and Derivatives: Theory and Applications* (Gordon and Breach).
19. Söhngen H (1939) Die Lösungen der Integralgleichung und deren Anwendung in der Tragflügeltheorie. *Math. Z.* 45:245–264.
20. Tricomi FG (1957) *Integral Equations* (Interscience).
21. Hytönen T, van Neerven J, Veraar M, Weis L (2016) *Analysis in Banach Spaces, Vol. I* (Springer).
22. Klenke A (2014) *Probability Theory: A Comprehensive Course*, 2nd ed. (Springer).
