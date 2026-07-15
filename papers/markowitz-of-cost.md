# A Markowitz Theory of Cost: Whitening the Signal in Time

**Status:** New draft. Position + result paper. Reuses established results from `fractional-derivative-optimal-execution.md` (bulk theorem, Wiener–Hopf factorization) and `adapted-convex-duality.md` (unifying skeleton); the contribution here is the *reframing* around the Markowitz analogy and the identification of the fractional derivative as the temporal analog of the inverse covariance.

**Date:** 2026-07-11. **Authors:** TBD.

---

## Abstract

Markowitz (1952) builds the optimal portfolio by solving a gain/risk tradeoff: the return vector is Sharpe-maximized against a quadratic risk penalty $\tfrac12 w^\top \Sigma w$, and the solution $w^\star \propto \Sigma^{-1}\mu$ *whitens the expected-return vector cross-sectionally* — it applies the inverse of the covariance to the predictor. We develop the parallel theory for the gain/**cost** tradeoff of a trader executing against transient market impact. The cost operator $C = G\ast$ is a *non-local* convolution against a decay kernel, so its inverse cannot be applied naively: the classical LQG certainty-equivalence fails because $C$ is not causal on the adapted subspace. The correct object is the *filtration Wiener–Hopf factorization* of $C$ with respect to the optional projection $P_+$: writing $C = C_- C_+$ with $C_\pm$ analytic in the upper/lower half-planes, the inverse of the projected operator is

$$ (P_+ C P_+)^{-1} \;=\; C_+^{-1}\, P_+\, C_-^{-1}, $$

with the projection sitting *between* the causal and anticausal factors. The optimal trading rate is

$$ u^\star_t \;=\; \underbrace{C_+^{-1}}_{\text{causal factor}}\Bigl[\;\underbrace{P_+}_{\text{forecast}}\,\underbrace{C_-^{-1}\alpha}_{\text{anticausal factor}}\;\Bigr](t), $$

read from the inside out: anticausal half-inversion of the *forecast curve*, followed by causal half-inversion of the resulting adapted process. For the empirically dominant case of a power-law kernel $G(t) = c t^{-\gamma}$, $\gamma \in (0,1)$, the symbol factorizes as $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$ with $\beta = (1-\gamma)/2$, and the optimal policy becomes a **fractional derivative of the signal predictor** of order $1-\gamma$. The general structure mirrors Markowitz along four axes: (i) two metrics — gain and quadratic cost — linked by convex duality; (ii) the solution is a linear operator applied to a predictor; (iii) that operator is the inverse-square-root of the cost Hessian on both sides of a projection; (iv) the solution *whitens* the predictor — cross-sectionally in Markowitz, *in time* here. We propose that the fractional derivative of the forecast curve is as basic to cost-managed trading as $\Sigma^{-1}\mu$ is to risk-managed investment.

---

## 1. Introduction: Two Whitening Problems

### 1.1 The Markowitz problem

Fix a universe of $N$ assets with expected excess-return vector $\mu \in \mathbb{R}^N$ and positive-definite return-covariance matrix $\Sigma \in \mathbb{R}^{N\times N}$. The Markowitz (1952) problem is

$$ \max_{w \in \mathbb{R}^N} \; w^\top \mu \;-\; \tfrac{1}{2}\lambda\, w^\top \Sigma w, \tag{M} $$

with $\lambda > 0$ a risk-aversion parameter. The first-order condition is $\mu = \lambda\, \Sigma w^\star$, giving the closed form

$$ \boxed{\; w^\star \;=\; \lambda^{-1}\, \Sigma^{-1}\mu.\;} \tag{M$^\star$} $$

Four features of $(\text{M}^\star)$ are worth naming, because the theory that follows will replicate each one in a different domain:

1. **Two metrics.** *Gain* $w^\top\mu$ and *risk* $\tfrac12 w^\top\Sigma w$ are two quadratic forms on the same space $\mathbb{R}^N$.
2. **Convex duality.** The Lagrangian is quadratic and strictly convex; the FOC is linear, and its solution is unique.
3. **Linear operator on a predictor.** $w^\star$ is a linear image of $\mu$: the predictor of realized returns.
4. **Whitening.** Factor $\Sigma = L L^\top$ (Cholesky). Then $w^\star = \lambda^{-1}L^{-\top}L^{-1}\mu$, i.e. the operator $\Sigma^{-1}$ *first decorrelates the predictor*, then re-scales, then re-decorrelates. In the eigenbasis of $\Sigma$, principal components with high risk get down-weighted proportionally. The solution *whitens* $\mu$ cross-sectionally: it converts a correlated return vector into an uncorrelated one, weights it, and inverts.

The Markowitz rule is not one of many equally-good portfolios; it is the *canonical* map from predictor to position when the disutility is a quadratic risk penalty. Any deviation — Black–Litterman priors, shrinkage estimators of $\Sigma$, factor structure, position constraints — is a *modification of* $(\text{M}^\star)$, keeping the whitening skeleton.

### 1.2 The gain/cost analog

Now consider a single risky asset, traded continuously against a transient impact kernel $G(\cdot)$. A trader observes an $\mathcal{F}_t$-adapted alpha signal $\alpha_t$ predicting per-unit-time gain, and chooses an $\mathcal{F}_t$-adapted trading rate $u_t$. In the Bouchaud–Gatheral (2004) propagator model the execution price at time $t$ is $S_t = P_t - \int_{s\le t} G(t-s) u_s\, ds$, so the cumulative **cost paid to the market** is quadratic in $u$:

$$ \text{Cost}(u) \;=\; \tfrac{1}{2}\!\iint G(|t-v|)\, u_t\, u_v\, dt\, dv, $$

after symmetrizing the causal propagator kernel via bilinear symmetry of $u_t u_v$. The **gain** is linear in $u$: $\text{Gain}(u) = \int u_t\, \alpha_t\, dt$. The gain/cost problem is

$$ \max_{u \in L^2_{\rm adap}(\mathbb{T})} \; \mathbb{E}\!\int u_t\, \alpha_t\, dt \;-\; \tfrac{1}{2}\mathbb{E}\!\iint G(|t-v|)\, u_t\, u_v\, dt\, dv. \tag{C} $$

Compare (C) with (M):

| | Markowitz (M) | Gain–cost (C) |
|---|---|---|
| Decision variable | $w \in \mathbb{R}^N$ (portfolio) | $u \in L^2_{\rm adap}(\mathbb{T})$ (trading rate) |
| Predictor | $\mu \in \mathbb{R}^N$ (expected return) | $\alpha : \mathbb{T} \to \mathbb{R}$ (adapted signal) |
| Quadratic penalty | $\tfrac12 w^\top\Sigma w$ (risk) | $\tfrac12 \langle u, C u\rangle$ (impact cost) |
| Hessian | Covariance $\Sigma$ (finite matrix) | Cost operator $C = G\ast$ (convolution operator) |
| FOC | $\Sigma w = \lambda^{-1}\mu$ | $C u = \alpha - \lambda$ |
| Constraint set | Sometimes $\mathbf{1}^\top w = 1$ | Sometimes $\int u_t\, dt = X_0$; **always** adaptedness |

The last row is the point of departure. In Markowitz, the decision variable ranges over the whole ambient space $\mathbb{R}^N$: there is no analog of adaptedness. In the gain/cost problem the decision must be $\mathcal{F}_t$-adapted at every time $t$, so $u$ is constrained to lie in the *adapted subspace* of $L^2$. This is a genuine constraint because the cost operator $C$ is **non-local**: $(Cu)(t) = \int G(|t-v|)u_v\, dv$ integrates $u$ over the *entire* real line, past and future. Its inverse is likewise non-local. The naive Markowitz-style answer

$$ u^{\rm naive}_t \;=\; C^{-1}(\alpha - \lambda)(t) \tag{naive} $$

is *not adapted*: it depends on $\alpha_s$ for $s > t$, which the trader has not yet observed.

### 1.3 Adapted Wiener–Hopf as the correct inverse

The cure is classical in signal processing but has not, to our knowledge, been laid out in the Markowitz-analog form we adopt here. When one minimizes a quadratic functional over an adapted subspace, the correct FOC is $P_+ \nabla J(u^\star) = 0$, where $P_+$ is the optional projection onto adapted processes. The projected Hessian on the adapted subspace is $P_+ C P_+$, and its inverse is *not* $P_+ C^{-1} P_+$ (that would only be right if $C$ commuted with $P_+$, i.e. was causal to begin with).

The correct inverse is obtained via a **Wiener–Hopf factorization** of $C$: split the cost operator into a product of a causal and an anticausal factor,

$$ C \;=\; C_-\, C_+, \qquad C_+ \text{ causal},\quad C_- \text{ anticausal}, $$

where $C_+$ and its inverse extend analytically and non-vanishingly into one complex half-plane (upper for causal, lower for anticausal); the factorization is unique up to a scalar, exists whenever $C$ is positive-definite with a mild log-integrability condition on its symbol (Krein 1962), and is the operator-theoretic analog of the Cholesky decomposition $\Sigma = L L^\top$. Given this factorization, the inverse of the projected Hessian is

$$ \boxed{\;(P_+ C P_+)^{-1} \;=\; C_+^{-1}\, P_+\, C_-^{-1},\;} \tag{WH} $$

with the projection **between** the two half-factors. The optimal adapted trading rate is therefore

$$ \boxed{\; u^\star \;=\; C_+^{-1}\, P_+\, C_-^{-1}\, \alpha \;=\; C_+^{-1}\Bigl[\, P_+\bigl(C_-^{-1}\alpha\bigr)\Bigr]. \;} \tag{C$^\star$} $$

Read (C$^\star$) from the inside out:

1. Apply the **anticausal factor** $C_-^{-1}$ to the signal $\alpha$. The result is a non-adapted process depending on the future of $\alpha$.
2. **Project it onto the filtration**: $P_+$ replaces future values of $\alpha$ by their conditional expectations. The projected process is the anticausal half-inversion of the *forecast curve* $\bar\alpha(t,\cdot) := \mathbb{E}_t[\alpha_\cdot]$, evaluated on the diagonal.
3. Apply the **causal factor** $C_+^{-1}$ along the time series of intermediates. The result is $\mathcal{F}_t$-adapted at every $t$.

Equation (WH) is the direct analog of the Cholesky-based reading of Markowitz: $\Sigma^{-1} = L^{-\top} L^{-1}$, with $L^{-1}$ whitening $\mu$ and $L^{-\top}$ reweighting it back. The novelty in the temporal setting is only the presence of $P_+$ between the two half-inverses; that projection is *forced* by adaptedness and *absent* in Markowitz because there is no filtration.

### 1.4 The power-law special case: fractional derivative

The Bouchaud–Gatheral empirical result — reinforced by Jusselin–Rosenbaum (2020), who show that power-law impact is the *unique* kernel compatible with no dynamic arbitrage and rough volatility — is that

$$ G(t) \;=\; c\, t^{-\gamma}, \qquad \gamma \in (0, 1). $$

The Fourier symbol on $\mathbb{R}$ is $\hat G(\xi) = c_\gamma |\xi|^{\gamma-1}$ with $c_\gamma = 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$; the symbol of $C^{-1}$ is $c_\gamma^{-1}|\xi|^{1-\gamma}$, the symbol of the symmetric **Riesz fractional derivative** of order $1-\gamma$. The Wiener–Hopf factorization is

$$ |\xi|^{1-\gamma} \;=\; (i\xi)^{\beta}\, (-i\xi)^{\beta}, \qquad \beta \;:=\; \tfrac{1-\gamma}{2}, $$

the two factors being the Fourier symbols of the causal and anticausal Marchaud fractional derivatives $D_+^\beta$ and $D_-^\beta$. So on the whole line

$$ C_+^{-1} \;=\; c_\gamma^{-1/2}\, D_+^\beta, \qquad C_-^{-1} \;=\; c_\gamma^{-1/2}\, D_-^\beta, $$

and equation (C$^\star$) collapses to

$$ \boxed{\; u^\star_t \;=\; \kappa_{1-\gamma}\, \bigl(D_+^\beta\, \zeta\bigr)(t), \qquad \zeta_s \;:=\; \bigl(D_-^\beta\, \bar\alpha(s,\cdot)\bigr)(s), \;} \tag{FD} $$

with $\kappa_{1-\gamma} = c_\gamma^{-1}$ and $\bar\alpha(s,\cdot)$ the time-$s$ forecast curve. The optimal policy is a **fractional derivative of order $1-\gamma$** of an adapted process $\zeta$, which is itself the anticausal fractional half-derivative of the forecast curve. Two half-order operators — one applied to forecasts, one applied causally to the resulting time series — combine to a single full-order operator of order $1-\gamma$, differentiating the alpha signal *fractionally*.

The parallel to Markowitz is now precise. The role of $\Sigma^{-1}$ is played by $\mathbb{D}^{1-\gamma}$: both are the inverse of the appropriate Hessian, both act as a whitener on the predictor, and both admit a symmetric square-root decomposition (Cholesky $L L^\top$ ↔ Wiener–Hopf $D_+^\beta D_-^\beta$). The temporal analog inserts $P_+$ between the two square-roots to enforce adaptedness — the one structural feature of the temporal problem that has no static counterpart.

### 1.5 The four-axis parallel

Restate the axes of §1.1 in the temporal case.

1. **Two metrics.** Gain $\int u_t \alpha_t\,dt$ and cost $\tfrac12 \iint G(|t-v|)u_t u_v\,dt\,dv$ are two quadratic forms on $L^2_{\rm adap}(\mathbb{T})$.
2. **Convex duality.** $\mathcal{C}(u) = \text{Cost}(u) - \text{Gain}(u)$ is strictly convex on $L^2_{\rm adap}$ because $\hat G(\xi) > 0$ on $\xi\ne 0$; the adapted FOC $P_+(Cu - \alpha) = 0$ is linear and has a unique solution.
3. **Linear operator on a predictor.** $u^\star = A[\alpha]$ where $A = C_+^{-1} P_+ C_-^{-1}$ is a linear (adapted) operator on signal paths — the temporal analog of $\lambda^{-1}\Sigma^{-1}$.
4. **Whitening.** Under (FD), the inner step $\zeta_s = (D_-^\beta \bar\alpha(s,\cdot))(s)$ *whitens the forecast curve in time* — it converts a temporally correlated forecast into a process whose autocovariance is diagonal in the Wiener–Hopf sense. The outer $D_+^\beta$ re-weights. In frequency-domain terms, multiplying by $|\xi|^{1-\gamma}$ flattens the power spectrum of a $|\xi|^{\gamma-1}$-tempered signal: an OU alpha with autocorrelation decay $e^{-\theta|t|}$, when passed through the bulk operator, becomes white noise (up to the mean-reversion prefactor $\theta^\beta$; see Remark 3.1).

Markowitz whitens *cross-sectionally*: it decorrelates a return vector across assets. The gain/cost solution whitens *in time*: it decorrelates a signal path across horizons. Both are consequences of the same abstract fact — the optimal action is the inverse-Hessian image of the predictor — instantiated on different index sets (assets in one case; times in the other).

### 1.6 Claim of the paper

We assemble four claims into a single position:

- **(A) The fractional-derivative rule (FD) is the temporal Markowitz.** It bears the same relationship to cost-managed trading that $\Sigma^{-1}\mu$ bears to risk-managed investment: canonical inverse-Hessian on a predictor.
- **(B) Adaptedness demands a projection between the two Cholesky-analog factors.** This is the *only* structural addition compared to Markowitz; it is forced by the temporal ordering of the decision problem and has no cross-sectional analog.
- **(C) Whitening is the unifying operation.** Both problems admit a "square root" of the Hessian; the optimal policy is the inverse image of the predictor after whitening by that square root. In Markowitz the whitening is cross-sectional; in the gain/cost problem it is temporal.
- **(D) Power-law kernel is the empirically canonical special case.** Under the Jusselin–Rosenbaum (2020) no-dynamic-arbitrage-plus-rough-vol theorem, power-law is uniquely singled out; under it the abstract Wiener–Hopf reduces to a *fractional derivative*, an operator with two centuries of engineering pedigree (Oustaloup's CRONE fractional-PID control) but no prior use as the canonical execution formula.

The mathematical facts underlying (A)–(D) are not new individually. The Wiener–Hopf factorization is due to Wiener and Hopf (1931). The optional projection formulation is standard (Wiener 1949; Kailath–Sayed–Hassibi 2000). Half-order Riemann–Liouville factorization of the power-law Fredholm inverse is in Forde–Sánchez-Betancourt–Smith (2022) Theorem 2.2, in bounded-interval operator language, and the operator-resolvent framework of Abi Jaber–Neuman (2022; 2024) subsumes the whole line. What is new in this paper is the *reframing*: recognizing the fractional-derivative rule as **the** basic object of cost-managed trading, on the same footing as the Markowitz rule, and drawing out the four structural parallels (§1.5) that justify that status.

---

## 2. The Markowitz Skeleton, Made Portable

Before doing the gain/cost problem in detail, we extract the four elements of Markowitz in a form that will port unchanged to $L^2_{\rm adap}(\mathbb{T})$.

### 2.1 The abstract program

Let $H$ be a real Hilbert space, $\mu \in H$ a predictor, and $Q : H \to H$ a bounded self-adjoint positive-definite operator (the risk / cost Hessian). Consider

$$ \min_{u \in H} \; \tfrac{1}{2}\langle u, Q u\rangle \;-\; \langle \mu, u\rangle. \tag{P$_0$} $$

Strict convexity of $\tfrac12\langle\cdot, Q\cdot\rangle$ (from positivity of $Q$) makes (P$_0$) admit a unique minimizer

$$ u^\star \;=\; Q^{-1}\mu. \tag{S$_0$} $$

**Cholesky whitening.** Write $Q = R^\ast R$ with $R$ a bounded operator with bounded inverse (Cholesky / symmetric square root; existence is elementary for finite-dim $Q$ and follows from spectral calculus in general). Then

$$ u^\star \;=\; R^{-1}\, R^{-\ast}\, \mu, $$

so the inverse-Hessian action splits into two whitening steps: $R^{-\ast}$ decorrelates $\mu$, and $R^{-1}$ inverts the decorrelation on the answer.

Markowitz is (P$_0$) with $H = \mathbb{R}^N$, $Q = \lambda \Sigma$, $\mu = \mu$; then $R = \lambda^{1/2}L^\top$ where $\Sigma = LL^\top$ is Cholesky.

### 2.2 The adapted program

Now let $H$ be equipped with a **nest** $\{H_t\}_{t \in \mathbb{T}}$: a totally ordered chain of closed subspaces representing the filtration of "the past up to time $t$" (Arveson 1975; Davidson 1988). Let $P_t$ be orthogonal projection onto $H_t$, and let $H_{\rm adap} \subseteq H$ be the adapted subspace: $u \in H_{\rm adap}$ iff $u_t \in H_t$ for all $t$. Let $P_+ : H \to H_{\rm adap}$ be the optional projection.

The adapted analog of (P$_0$) is

$$ \min_{u \in H_{\rm adap}} \; \tfrac{1}{2}\langle u, Q u\rangle \;-\; \langle \mu, u\rangle. \tag{P$_1$} $$

The FOC, obtained by testing against arbitrary adapted variations $\delta u \in H_{\rm adap}$, is

$$ P_+\bigl(Q u^\star - \mu\bigr) \;=\; 0, \tag{FOC$_1$} $$

which says the gradient at the optimum is *anticausal* (has no adapted component). If $Q$ is not causal — i.e. $Q$ does not preserve $H_{\rm adap}$ — then $u^\star \neq P_+(Q^{-1}\mu)$ in general, and the naive Markowitz formula fails.

### 2.3 Wiener–Hopf factorization as adapted Cholesky

The correct FOC solver is a **factorization of $Q$ compatible with the nest**: find $Q = Q_- Q_+$ with $Q_+$ causal (preserves $H_t$ for each $t$) and $Q_-$ anticausal (preserves $H_t^\perp \cup H_t$; equivalently $Q_-^\ast$ is causal). This is a *Wiener–Hopf factorization*; equivalently, an outer factorization inside the nest algebra $\mathcal{T}(\mathcal{N})$ (Arveson 1975).

**Theorem 2.1 (Adapted inverse via Wiener–Hopf).** *Let $Q$ be self-adjoint, positive-definite, and admit a Wiener–Hopf factorization $Q = Q_- Q_+$ with $Q_-^\ast = Q_+$ (or, equivalently, $Q = C_+^\ast C_+$ with $C_+$ causal — the "adapted Cholesky"). Then the unique solution of $(\text{FOC}_1)$ is*

$$ u^\star \;=\; Q_+^{-1}\, P_+\, Q_-^{-1}\, \mu. \tag{S$_1$} $$

The proof is a one-line calculation; see e.g. Wiener (1949) for the scalar prediction case, Kailath–Sayed–Hassibi (2000) ch. 7–8 for the linear-filtering case, and `adapted-convex-duality.md` §3 for the abstract statement inside a nest algebra. Comparing (S$_1$) with (S$_0$):

- The right factor $Q_-^{-1}$ acts on the raw predictor.
- The projection $P_+$ replaces the *non-adapted part* of $Q_-^{-1}\mu$ by its conditional expectation onto the filtration.
- The left factor $Q_+^{-1}$ acts causally on the resulting adapted process.

If $Q$ is causal to begin with, then $P_+$ commutes with $Q_+$ and $Q_-$, and (S$_1$) reduces to (S$_0$) applied to $\mu$. If $Q$ is non-causal — the case of interest — the projection is genuinely inserted between the two half-inverses. This is the *one and only* structural addition of the adapted case relative to the unconstrained Markowitz case.

### 2.4 The four axes, abstractly

For (P$_1$)—(S$_1$):

1. **Two metrics.** $\tfrac12\langle u, Q u\rangle$ (quadratic cost/risk) and $\langle \mu, u\rangle$ (linear gain).
2. **Convex duality.** Strict convexity + adapted constraint gives a unique adapted stationary point.
3. **Linear operator on a predictor.** $u^\star = \mathcal{A}[\mu]$ with $\mathcal{A} = Q_+^{-1} P_+ Q_-^{-1}$.
4. **Whitening.** The map $Q_-^{-1}$ decorrelates $\mu$ (whitens it in the metric induced by $Q$); $P_+$ enforces the temporal information constraint; $Q_+^{-1}$ inverts the decorrelation to produce a well-scaled action.

Markowitz is the special case with trivial nest ($\mathbb{T} = \{*\}$, so $P_+ = \text{id}$). The temporal gain/cost problem is (P$_1$) with $H = L^2(\mathbb{T})$, nest $H_t = \{u \in L^2 : u|_{(t,\infty)} = 0\}$, $Q = C = G\ast$, $\mu = \alpha$. The next section carries this out.

---

## 3. The Gain/Cost Problem in Detail

### 3.1 Setting

Fix a filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t\in\mathbb{T}}, \mathbb{P})$ with $\mathbb{T} \in \{\mathbb{R}, [0,T], [0,\infty)\}$. Let $\alpha \in L^2_{\rm adap}(\mathbb{T})$ be a progressive alpha signal; let $u \in L^2_{\rm adap}(\mathbb{T})$ be an admissible trading rate (sign convention: $u > 0$ is selling). The **forecast curve** is

$$ \bar\alpha(t,s) \;:=\; \begin{cases} \alpha_s, & s\le t, \\ \mathbb{E}_t[\alpha_s], & s > t. \end{cases} $$

The **cost operator** $C : L^2 \to L^2$ is convolution against a symmetric positive-definite decay kernel: $(Cu)(t) = \int G(|t-v|)\, u_v\, dv$. The problem is

$$ \min_{u \in L^2_{\rm adap}(\mathbb{T})} \; \mathcal{C}(u) \;:=\; \tfrac{1}{2}\mathbb{E}\langle u, C u\rangle \;-\; \mathbb{E}\langle u, \alpha\rangle \;+\; \lambda\, \mathbb{E}\langle u, \mathbf{1}\rangle, \tag{C} $$

with $\lambda$ a Lagrange multiplier for a budget/inventory constraint when needed.

### 3.2 The adapted FOC

Testing $\delta\mathcal{C} = 0$ against adapted variations $\delta u$ and using the tower property gives the *conditioned* FOC

$$ P_+\bigl(Cu^\star - \alpha + \lambda\bigr) \;=\; 0 \quad\Longleftrightarrow\quad \mathbb{E}_t[(Cu^\star)(t)] \;=\; \alpha_t - \lambda, \quad t \in \mathbb{T}. \tag{FOC} $$

Equation (FOC) is the temporal analog of the Markowitz normal equation $\lambda \Sigma w^\star = \mu$. The left-hand side involves both the past and the future of $u^\star$ — via non-locality of $C$ — under the *time-$t$ conditional expectation*.

### 3.3 The naive answer, and why it fails

Ignoring adaptedness, one would solve (FOC) by Fourier inversion: $\hat u^{\rm naive}(\xi) = \hat G(\xi)^{-1} \widehat{(\alpha-\lambda)}(\xi)$. This produces a process that depends on $\{\alpha_s : s \in \mathbb{R}\}$, not on $\{\alpha_s : s \le t\}$. It is not admissible.

**LQG certainty equivalence does not apply.** Classical LQG separation (Kwakernaak–Sivan 1972; Bensoussan 1992) permits replacing the state by its conditional mean *only when the cost is a local (pointwise-in-time) function of the state and control, or when the cost operator is causal*. Neither holds here: the impact-cost integral operator is non-local *and* non-causal. Concretely, $(P_+ C P_+)^{-1} \ne P_+ C^{-1} P_+$: composing $P_+$ with a non-causal $C$ does not commute past $C^{-1}$. So the substitute rule "replace $\alpha_s$ by $\bar\alpha(t,s)$ inside $C^{-1}$" (a certainty-equivalent answer) *fails* to satisfy (FOC).

### 3.4 Wiener–Hopf factorization

Factorize the cost operator as $C = C_- C_+$, where the symbols

$$ \hat C_-(\xi)\, \hat C_+(\xi) \;=\; \hat G(\xi), $$

are chosen so that $\hat C_+(\xi)$ extends analytically and non-vanishingly to the upper half-plane, and $\hat C_-(\xi)$ to the lower half-plane. (Existence follows from Krein 1962 when $\int |\log \hat G(\xi)|(1+\xi^2)^{-1} d\xi < \infty$, which holds whenever $\hat G$ is bounded above and below by positive powers of $|\xi|$.) The two factors are unique up to a scalar; we normalize $\hat C_\pm(0) = \hat G(0)^{1/2}$ where meaningful, or use the natural power-law normalization of §4.

Then $C_+$ is *causal* (its time-domain kernel is supported on $\{s \le t\}$) and $C_-$ is *anticausal* (kernel supported on $\{s \ge t\}$); they commute as operators on the whole line, but not with $P_+$. The classical filtration Wiener–Hopf identity (Wiener 1949; Bode–Shannon 1950) reads

$$ \boxed{\;(P_+ C P_+)^{-1} \;=\; C_+^{-1}\, P_+\, C_-^{-1}\;} \tag{WH} $$

on the adapted subspace. Applied to (FOC), it yields

$$ \boxed{\;u^\star \;=\; C_+^{-1}\, P_+\, C_-^{-1}\, (\alpha - \lambda)\;=\; C_+^{-1}\, \bigl[\, P_+\, C_-^{-1}\, \alpha\, \bigr] \;-\; \lambda\, C_+^{-1} C_-^{-1}\,\mathbf{1}.\;} \tag{C$^\star$} $$

The second term collapses to a constant DC offset absorbed by the budget constraint; hereafter we drop it, working with mean-zero $\alpha$. **This is the temporal Markowitz formula.**

### 3.5 Reading (C$^\star$) as causal(anticausal(forecast))

Read the composition inside out:

- **Step 1 (anticausal factor).** Compute $\eta := C_-^{-1}\alpha$. Since $C_-$ has anticausal kernel, $C_-^{-1}$ is also anticausal: $\eta_s$ depends on $\{\alpha_r : r \ge s\}$. This step *whitens $\alpha$ into an anticausal white-noise process* (up to the $C_+$-half of the covariance).
- **Step 2 (adapted projection).** Compute $\zeta_s := (P_+ \eta)(s) = \mathbb{E}_s[\eta_s]$. Because $\eta_s$ depends only on the future of $\alpha$ at time $s$, and $\mathbb{E}_s$ replaces that future by its $\mathcal{F}_s$-conditional expectation, we get

$$ \zeta_s \;=\; \bigl(C_-^{-1}\, \bar\alpha(s,\cdot)\bigr)(s), $$

the anticausal half-inversion of the **forecast curve** $\bar\alpha(s,\cdot)$, evaluated at the current time $s$. The forecast curve appears here — and only here — as the concrete object on which the anticausal factor acts. The intermediate $\zeta$ is $\mathcal{F}_s$-adapted at every $s$.

- **Step 3 (causal factor).** Compute $u^\star_t = (C_+^{-1} \zeta)(t)$. Because $C_+^{-1}$ is causal, this step is a legitimate adapted operation on the process $\{\zeta_s\}_{s\le t}$.

The structural output

$$ u^\star_t \;=\; \underbrace{C_+^{-1}}_{\text{causal factor}}\Bigl(\, \underbrace{C_-^{-1}}_{\text{anticausal factor}}\, \underbrace{\bar\alpha(\cdot,\cdot)}_{\text{forecast curve}} \Bigr)(t) $$

is the temporal analog of $w^\star = L^{-\top}(L^{-1}\mu)$ from the Cholesky reading of Markowitz. **All non-causality of the underlying inverse is quarantined into Step 1**, which acts on the forecast curve — a $\mathcal{F}_s$-measurable object at every $s$ — rather than on the realized path. Only conditional-law forecasting information is required; there is no peeking into the future of the realized $\alpha$.

### 3.6 The Markowitz correspondence, made precise

Compare term-by-term:

| Markowitz | Gain/Cost |
|---|---|
| $\Sigma = L L^\top$ (Cholesky) | $C = C_- C_+$ (Wiener–Hopf) |
| $L^{-1}$: cross-sectional whitening | $C_-^{-1}$: anticausal whitening |
| $L^{-\top}$: inverse whitening | $C_+^{-1}$: causal whitening |
| (no projection) | $P_+$: adapted projection |
| $w^\star = L^{-\top}(L^{-1}\mu)$ | $u^\star = C_+^{-1}(P_+ C_-^{-1}\alpha)$ |
| Predictor: $\mu$ | Predictor: forecast curve $\bar\alpha$ |
| Whitening in asset space | Whitening in time |

The only structural addition in the temporal problem is the projection $P_+$, which is *between* the two Cholesky-analog factors, not outside them. That projection is forced by adaptedness; in the static (cross-sectional) Markowitz case there is no filtration and no projection.

---

## 4. Power-Law Kernel: The Fractional Derivative Rule

The abstract Wiener–Hopf formulation (§3) is general; concreteness requires a kernel. We now specialize to the empirically canonical case.

### 4.1 The kernel

Take $G(t) = c\,t^{-\gamma}$ with $\gamma \in (0,1)$, $c > 0$. Empirical support: Bouchaud–Gefen–Potters–Wyart (2004) and subsequent work fit $\gamma \in [0.4, 0.7]$ on equity data. Structural support: Jusselin–Rosenbaum (2020) prove that under no dynamic arbitrage and consistency with rough volatility, $G$ *must* be power-law, with $\gamma$ tied to the Hurst exponent.

The Fourier symbol on $\mathbb{R}$ is

$$ \hat G(\xi) \;=\; 2c\!\int_0^\infty t^{-\gamma}\cos(\xi t)\, dt \;=\; c_\gamma\, |\xi|^{\gamma-1}, \qquad c_\gamma \;:=\; 2c\, \Gamma(1-\gamma)\sin(\pi\gamma/2). $$

The symbol of $C^{-1}$ is $c_\gamma^{-1}|\xi|^{1-\gamma}$, which is exactly the symbol of the symmetric **Riesz fractional derivative** $\mathbb{D}^{1-\gamma}$.

### 4.2 Wiener–Hopf factorization of the power-law symbol

The absolute-value symbol admits the *canonical* factorization

$$ |\xi|^{1-\gamma} \;=\; (i\xi)^{\beta}\, (-i\xi)^{\beta}, \qquad \beta \;:=\; \tfrac{1-\gamma}{2} \in (0, 1/2), $$

with $(i\xi)^\beta := |\xi|^\beta e^{i\beta\pi\,{\rm sgn}(\xi)/2}$ and its conjugate. The factor $(i\xi)^\beta$ is analytic and non-vanishing in the closed upper half-plane; $(-i\xi)^\beta$ in the closed lower half-plane; and their product recovers $|\xi|^{1-\gamma}$ with no residual constant (the phases cancel exactly). This is the Wiener–Hopf factorization of the bulk symbol on $\mathbb{R}$; it is classical (Samko–Kilbas–Marichev 1993 §7.1; Krein 1962).

The corresponding time-domain factors are the **causal and anticausal Marchaud half-derivatives**

$$ (D_-^\beta f)(s) \;=\; \frac{\beta}{\Gamma(1-\beta)}\!\int_0^\infty\!\!\frac{f(s+h) - f(s)}{h^{1+\beta}}\, dh, \qquad (D_+^\beta f)(s) \;=\; \frac{\beta}{\Gamma(1-\beta)}\!\int_0^\infty\!\!\frac{f(s) - f(s-h)}{h^{1+\beta}}\, dh, $$

with Fourier symbols $(-i\xi)^\beta$ and $(i\xi)^\beta$ respectively. Since $\hat C_\pm = c_\gamma^{1/2}(\pm i\xi)^{-\beta}$, we have

$$ C_+ \;=\; c_\gamma^{1/2}\, I_+^\beta, \qquad C_- \;=\; c_\gamma^{1/2}\, I_-^\beta, \qquad C_+^{-1} \;=\; c_\gamma^{-1/2}\, D_+^\beta, \qquad C_-^{-1} \;=\; c_\gamma^{-1/2}\, D_-^\beta, $$

with $I_\pm^\beta$ the Riemann–Liouville fractional integrals of order $\beta$.

### 4.3 The fractional-derivative rule

Substituting into (C$^\star$):

$$ \boxed{\; u^\star_t \;=\; \kappa_{1-\gamma}\, \bigl(D_+^\beta\, \zeta\bigr)(t), \qquad \zeta_s \;:=\; \bigl(D_-^\beta\, \bar\alpha(s,\cdot)\bigr)(s), \qquad \beta = \tfrac{1-\gamma}{2}, \qquad \kappa_{1-\gamma} = c_\gamma^{-1}. \;} \tag{FD} $$

Equation (FD) is the concrete embodiment of the abstract (C$^\star$) for the power-law kernel. It says: the optimal signal-adaptive trading rate is a *fractional derivative of the forecast curve*, of total order $1-\gamma$, split as a two-step adapted computation:

- **Step 1 (per-time, anticausal on forecast).** At each time $s$, compute the anticausal half-derivative $D_-^\beta$ of the forecast curve $\bar\alpha(s,\cdot)$ and evaluate at the current time $s$. This is a $\mathcal{F}_s$-measurable operation depending only on the conditional law of the future signal.
- **Step 2 (across times, causal on adapted intermediate).** Apply the causal half-derivative $D_+^\beta$ to the resulting adapted process $\{\zeta_s\}$, evaluated at $t$.

The two half-orders sum to $1-\gamma$: the full inverse-Hessian order. Adaptedness is enforced *by the projection between them*.

### 4.4 Special case: Ornstein–Uhlenbeck signal

For $d\alpha_t = -\theta\alpha_t\, dt + \sigma\, dW_t$, the forecast curve is $\bar\alpha(t,s) = e^{-\theta(s-t)}\alpha_t$ for $s > t$, and direct Marchaud integration against the exponential tail gives

$$ (D_-^\beta \bar\alpha(t,\cdot))(t) \;=\; \theta^\beta\, \alpha_t, $$

so $\zeta_t = \theta^\beta \alpha_t$ pathwise, and

$$ u^{\star,\,\rm OU}_t \;=\; \kappa_{1-\gamma}\, \theta^\beta\, (D_+^\beta \alpha)(t). $$

That is: **a causal half-order fractional derivative of the realized OU path**, weighted by a mean-reversion factor. When the signal itself is Markov, Step 1 collapses to a pointwise multiplication, and only the causal half-derivative on the realized path remains. This is the closed-form example that best exposes the operator content.

### 4.5 Numerical implementation

Fractional derivatives discretize to Toeplitz matrix operations. On a uniform grid of $N$ points, $D_\pm^\beta$ is a lower/upper-triangular Toeplitz matrix with entries given by the coefficients of the generating function $(1-z)^\beta$ (equivalently, generalized binomial coefficients). Applying (FD) is therefore

$$ O(N \log N) \text{ per time step via FFT}, $$

versus $O(N^2)$ Nyström inversion of the Fredholm equation (\star). See `experiments/filtering_fracdiff_powerlaw.py` in the companion repository for a working reference implementation. Numerical experiments (`experiments/riesz_split_check.py`, `experiments/bulk_vs_filtration_WH.py`) verify the factorization identity (WH) to machine precision on discrete synthetic signals.

---

## 5. Whitening in Time: The Statistical Content

Section 4 gives the operator formula. This section explains what it does *statistically* — the temporal analog of Markowitz's cross-sectional whitening.

### 5.1 Cross-sectional whitening (Markowitz)

Given returns with covariance $\Sigma = LL^\top$, the transformed vector $\tilde \mu := L^{-1}\mu$ has identity covariance under the *scaled inner product* $\langle x, y\rangle_\Sigma := x^\top \Sigma y$; equivalently, in the eigenbasis of $\Sigma$, each principal-component gain is divided by its principal-component variance. The Markowitz portfolio $w^\star = L^{-\top}\tilde\mu$ then re-expresses this whitened predictor in the original coordinate system: each asset receives weight proportional to its contribution to the *decorrelated* gain.

The economic reading: **positions are allocated in proportion to the marginal contribution of each independent factor to expected return, not to raw expected return**. If two assets are perfectly correlated, $\Sigma$-whitening merges them; if one is idiosyncratically noisy, whitening down-weights it. This is the essence of risk management.

### 5.2 Temporal whitening (gain/cost)

The analog in time. Consider a stationary alpha $\alpha$ with power spectral density $S_\alpha(\xi)$. The signal is *not white*: it has coloration $S_\alpha(\xi)$ inherited from persistence in the underlying return-predicting information. The cost operator has symbol $\hat G(\xi) = c_\gamma |\xi|^{\gamma-1}$: it is *soft on low frequencies* (large kernel value, integrated slowly) and *hard on high frequencies* (small kernel value, integrated fast). This creates a *frequency-dependent tradeoff* — low-frequency components of $\alpha$ can be exploited only at high impact cost per unit trade; high-frequency components are cheaper to exploit but the exploitation window is narrow.

The Wiener–Hopf factors $C_\pm$ split the cost operator into two "half-covariances" analogous to $L$ and $L^\top$. Applying $C_-^{-1} = c_\gamma^{-1/2}D_-^\beta$ to $\alpha$ multiplies its Fourier transform by $c_\gamma^{-1/2}(-i\xi)^\beta$, which whitens the power spectrum by a factor $|\xi|^{2\beta} = |\xi|^{1-\gamma}$. **The alpha becomes flatter across frequencies** — low-frequency (persistent) components are attenuated relative to high-frequency (transient) components, in exact proportion to the extra cost the impact operator would extract from trading them.

After the projection $P_+$ makes the process adapted, the causal factor $C_+^{-1} = c_\gamma^{-1/2}D_+^\beta$ applies the same spectral whitening in the causal direction. The composition produces an $\mathcal{F}_t$-adapted trading rate whose spectral content is *balanced against the frequency-dependent impact cost*: trade fast enough that high-frequency signal is captured, but slow enough that low-frequency signal is exploited without paying disproportionate impact.

In precise terms: for a stationary alpha with $S_\alpha(\xi) \propto |\xi|^{\gamma-1}\cdot g(\xi)$ (roughly the shape of an OU or Volterra signal near $\xi = 0$), the optimal trading rate has power spectral density $S_u(\xi) \propto g(\xi)$: **the "hardness" of the impact operator is exactly cancelled by fractional differentiation, leaving a residual trading-rate spectrum equal to the intrinsic signal information content**. This is the temporal whitening claim.

### 5.3 Whitening is the unifier

Both problems admit an inverse-Hessian operator that can be factored as a "square root times its adjoint" (Cholesky in Markowitz; Wiener–Hopf in gain/cost). The optimal action is the operator applied to the predictor, and the factored form exhibits the action as *decorrelate → project → recorrelate*. In Markowitz there is no projection because there is no filtration; in the gain/cost problem the projection sits between the two square-root factors and is the only structural distinction.

**Whitening is *the* content of the theory.** The mathematical operation performed by both formulas is: apply the inverse of the covariance-analog to the predictor. In Markowitz this is $\Sigma^{-1}\mu$; in the gain/cost problem this is $C^{-1}\alpha$, appropriately projected. The temporal case forces the projection between the two factors, and — for the empirically canonical power-law kernel — the two factors are Marchaud half-derivatives, so the total operator is a *fractional derivative of order $1-\gamma$* applied to the forecast curve.

---

## 6. Discussion

### 6.1 Fractional derivatives as basic objects

If (FD) is the temporal Markowitz, then the fractional derivative $D^{1-\gamma}$ of the forecast curve deserves a place in the working vocabulary of quantitative trading similar to that of $\Sigma^{-1}\mu$. In practice:

- **Signal transformation.** For any candidate alpha $\alpha$, its natural input to the impact-optimal execution is the fractional derivative $D_+^{(1-\gamma)/2}\zeta$, not $\alpha$ itself. This is the temporal analog of "residualizing" a return prediction against the factor covariance.
- **Model comparison.** Two alphas that agree in raw form but differ in their power-spectrum tail are *not* equivalent after $D^{1-\gamma}$: the fractional derivative amplifies high-frequency content by a factor $|\xi|^{1-\gamma}$, so signals with fatter high-frequency tails become disproportionately valuable when execution is impact-limited. This is a testable prediction: signals that look similar under standard IC ranking may differ dramatically after fractional differentiation.
- **Robustness diagnostic.** Mis-specification of the propagator exponent $\gamma$ corresponds to using the wrong order of fractional derivative. Standard CRONE-control stability analysis (Oustaloup 1991; Chen–Petráš–Xue 2009) gives first-order sensitivity of cost degradation to $\Delta\gamma$, providing a quantitative robustness bound.

### 6.2 Boundary corrections: the analog of position constraints

Markowitz on $\mathbb{R}^N$ with no constraints gives (M$^\star$). Adding constraints — e.g. long-only $w \ge 0$, or budget $\mathbf{1}^\top w = 1$ — produces boundary corrections: KKT multipliers and active-set logic. The frictionless answer (M$^\star$) is a *starting point*, deformed by the constraints.

Analogously, on $\mathbb{R}$ with a stationary alpha, (FD) is exact. Restricting to a finite horizon $[0,T]$ with an inventory constraint $X_T = 0$ introduces two homogeneous modes of the bulk equation — spanned by $\phi_1(t) = (t(T-t))^{(\gamma-1)/2}$ and $\phi_2(t) = \tfrac{T-2t}{2}\phi_1(t)$ — whose coefficients are fixed by the boundary data. These are the "Söhngen–Tricomi modes" of the classical airfoil equation (Söhngen 1939; Tricomi 1957) and produce the U-shaped execution profile of Gatheral–Schied–Slynko (2012) when $\alpha \equiv 0$. In the long-horizon regime the boundary corrections scale as $O(T^{\gamma-1})$ while the bulk term is $\Theta(1)$; the fractional-derivative rule is the asymptotic optimum. See `fractional-derivative-optimal-execution.md` §5 for the detailed boundary analysis; the point here is only that the abstract structure — *bulk answer plus boundary correction* — is common to the Markowitz and gain/cost problems, with position constraints in one case and inventory/horizon constraints in the other.

### 6.3 What Markowitz doesn't teach us

Three features of the gain/cost problem *do not* have Markowitz analogs:

1. **The projection $P_+$.** Absent in Markowitz because there is no filtration. Its presence is the whole content of the phrase "adapted Wiener–Hopf": adaptedness sits between the two whitening factors.
2. **The forecast curve.** In Markowitz $\mu$ is a fixed vector, not a stochastic process. In the gain/cost problem the *predictor* is itself an infinite-dimensional object: at each time $t$, the trader carries a whole curve $s \mapsto \bar\alpha(t,s)$ of forecasts. The anticausal factor acts on this curve, not on a point.
3. **The half-order structure.** In Markowitz the Cholesky factor $L$ has no particular "order"; it is just a square root. In the temporal problem the two factors $C_\pm$ have *half* the order of $C^{-1}$: they are $D_\pm^{(1-\gamma)/2}$, not $D_\pm^{1-\gamma}$. The order halving is a genuine feature of the temporal Wiener–Hopf factorization and gives the closed-form OU rule (Remark 4.4) its clean $\theta^\beta$ prefactor.

These are not defects of the analogy — they are the *content* of the temporal generalization.

### 6.4 What Markowitz *does* teach us: the two-metric structure

The deep content of the Markowitz picture is that *there are two objects — a linear predictor and a quadratic penalty — and one convex-duality operation linking them*. That structure is entirely preserved in the gain/cost problem: gain is linear in $u$, cost is quadratic in $u$, and the FOC is a linear equation obtained by convex duality. The identity of the two objects changes (predictor $\mu \to \alpha$; penalty $\Sigma \to C$); the *type* of each object is preserved; and the *operation* that produces the optimal action from them is the same abstract inverse-Hessian-on-predictor rule. What differs is only the ambient space and the presence of a filtration.

The claim of this paper is that the temporal analog is fully as *canonical* as the cross-sectional one: for cost-managed trading against transient impact, the fractional derivative of the forecast curve is the natural first thing to write down, not one of many equivalent formulas.

### 6.5 Related structural work

The convex-duality / nest-algebra abstraction (§2) is developed at length in the companion note `adapted-convex-duality.md`, which treats Wiener–Hopf prediction, Kalman filtering, and optimal trading as three avatars of the same skeleton. The information-theoretic complement — spectral bounds on trading efficiency in bits per dollar — is developed in `info-thermodynamics-trading.md`. The detailed bounded-interval and half-line theorems, boundary-mode scaling, and multi-asset extension are in `fractional-derivative-optimal-execution.md`. The present paper's contribution is *positioning*: naming (FD) as the temporal Markowitz and organizing the structural parallel around four axes (two metrics; convex duality; linear-operator-on-predictor; whitening).

### 6.6 Testable content

The reframing is not vacuous. It generates testable content:

- **Signal ranking.** For a given kernel exponent $\gamma$, ranking candidate alphas by their post-fractional-differentiation Sharpe (rather than raw IC) should give a *strictly better* cost-adjusted PnL prediction than raw IC ranking. This is the analog of using $\Sigma$-adjusted Sharpes rather than raw expected returns for asset selection.
- **Kernel calibration.** The scaling exponent $\gamma$ estimated from empirical impact curves should, under (FD), match the scaling exponent of the *cross-sectional distribution of optimal trading rates* observed in production trading. Mismatches diagnose either kernel mis-specification or non-adaptive execution.
- **Whitening test.** Under (FD), if the alpha signal is stationary with spectrum $S_\alpha \propto |\xi|^{\gamma-1}\cdot g(\xi)$, the optimal trading rate has spectrum $\propto g(\xi)$. Testing whether observed optimal-execution trading rates have flat residual spectrum after removing $g$ is a direct check of (FD)'s statistical claim (§5.2).

---

## 7. Conclusion

Markowitz (1952) is not remembered because the linear-algebra step from $\mu$ and $\Sigma$ to $\Sigma^{-1}\mu$ is deep; it is remembered because it identified a *canonical mapping* from a return predictor to a portfolio via a convex-duality argument. The Markowitz formula is the first thing to write down when the disutility is a quadratic risk penalty.

We have argued that the same is true, in an exactly parallel sense, for cost-managed trading:

$$ \boxed{\; u^\star_t \;=\; \kappa_{1-\gamma}\, \bigl(D_+^\beta\, \zeta\bigr)(t), \qquad \zeta_s \;=\; \bigl(D_-^\beta\, \bar\alpha(s,\cdot)\bigr)(s), \qquad \beta = \tfrac{1-\gamma}{2}, \;} $$

is the first thing to write down when the disutility is a power-law impact-cost penalty. It is a *fractional derivative of order $1-\gamma$ of the forecast curve*, applied via a filtration Wiener–Hopf factorization that whitens the signal in time. It is derived from two metrics — gain and cost — linked by convex duality, exactly as $\Sigma^{-1}\mu$ is derived from two metrics — gain and risk — linked by convex duality. The whitening in Markowitz is cross-sectional; the whitening here is temporal. The projection $P_+$ between the two Cholesky-analog factors is the one structural addition forced by adaptedness.

The mathematical facts are individually classical: Wiener–Hopf factorization is 1931; Marchaud half-derivatives are 1927; the operator-language content of (FD) is implicit in Forde–Sánchez-Betancourt–Smith (2022). What is not yet standard is the *reading*: that the fractional derivative of the forecast curve is to cost-managed trading what the inverse-covariance-times-return is to risk-managed investment. If (FD) is adopted as a working object — a natural transform of any candidate alpha — the practical consequence is that "signals" and "execution" cease to be independent modules, and the impact-adjusted content of a predictor is read directly from its fractional derivative.

---

## References

- Abi Jaber, E.; Neuman, E. *Optimal Liquidation with Signals: the General Propagator Case.* Math. Finance, 2025; arXiv:2211.00447.
- Abi Jaber, E.; Neuman, E.; Tuschmann, S. *Optimal Portfolio Choice with Cross-Impact Propagators.* arXiv:2403.10273, 2024.
- Arveson, W. *Interpolation Problems in Nest Algebras.* J. Funct. Anal. 20, 208–233, 1975.
- Bensoussan, A. *Stochastic Control of Partially Observable Systems.* Cambridge, 1992.
- Bode, H.W.; Shannon, C.E. *A Simplified Derivation of Linear Least Squares Smoothing and Prediction Theory.* Proc. IRE 38, 417–425, 1950.
- Bouchaud, J.-P.; Gefen, Y.; Potters, M.; Wyart, M. *Fluctuations and Response in Financial Markets: The Subtle Nature of 'Random' Price Changes.* Quant. Finance 4, 176–190, 2004.
- Chen, Y.Q.; Petráš, I.; Xue, D. *Fractional Order Control — A Tutorial.* Proc. ACC, 1397–1411, 2009.
- Davidson, K.R. *Nest Algebras.* Longman, 1988.
- Forde, M.; Sánchez-Betancourt, L.; Smith, B. *Optimal trade execution for Gaussian signals with power-law resilience.* Quant. Finance 22(3), 2022.
- Gârleanu, N.; Pedersen, L.H. *Dynamic Trading with Predictable Returns and Transaction Costs.* J. Finance 68(6), 2013.
- Gatheral, J.; Schied, A.; Slynko, A. *Transient linear price impact and Fredholm integral equations.* Math. Finance 22(3), 2012.
- Jusselin, P.; Rosenbaum, M. *No-arbitrage implies power-law market impact and rough volatility.* Math. Finance 30(4), 2020.
- Kailath, T.; Sayed, A.H.; Hassibi, B. *Linear Estimation.* Prentice-Hall, 2000.
- Krein, M.G. *Integral equations on a half-line with kernel depending upon the difference of the arguments.* Amer. Math. Soc. Transl. (2) 22, 1962.
- Kwakernaak, H.; Sivan, R. *Linear Optimal Control Systems.* Wiley, 1972.
- Markowitz, H. *Portfolio Selection.* J. Finance 7, 77–91, 1952.
- Oustaloup, A. *La Commande CRONE.* Hermès, 1991.
- Samko, S.G.; Kilbas, A.A.; Marichev, O.I. *Fractional Integrals and Derivatives.* Gordon and Breach, 1993.
- Söhngen, H. *Die Lösungen der Integralgleichung $g(x) = \int_{-a}^a f(\xi)/(x-\xi)\,d\xi$ und deren Anwendung in der Tragflügeltheorie.* Math. Z. 45, 1939.
- Tricomi, F.G. *Integral Equations.* Interscience, 1957.
- Wiener, N. *Extrapolation, Interpolation and Smoothing of Stationary Time Series.* MIT Press, 1949.
- Wiener, N.; Hopf, E. *Über eine Klasse singulärer Integralgleichungen.* S.-B. Preuss. Akad. Wiss. Berlin, 696–706, 1931.

---

## Notes on relation to companion drafts

This draft is the "position" companion to the technical results developed in:

- `fractional-derivative-optimal-execution.md` — the technical paper: bulk theorem on $\mathbb{R}$, boundary corrections, half-line augmented-symbol W–H, multi-asset extension, full proofs.
- `fractional-derivative-optimal-execution-short.md` — the compressed technical version.
- `adapted-convex-duality.md` — the general nest-algebra skeleton unifying Wiener–Hopf prediction, Kalman filtering, and optimal trading.
- `noisy-signal-impact-trading.md` — the stationary-Wiener-filter setup with noisy signals.
- `info-thermodynamics-trading.md` — spectral information-theoretic bounds on trading efficiency.

The present draft assumes all technical content of those papers and restricts itself to the *positioning* argument: (FD) as the temporal Markowitz. If merged into the main technical paper, this material would sit as a §1-replacement (long introduction) plus a new §"Statistical whitening in time" corresponding to §5 here.
