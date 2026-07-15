# Closed-Form Optimal Trading Against a Signal via Factorization of the Impact Cost Operator

**Authors:** TBD

**Classification:** Physical Sciences — Applied Mathematics / Economic Sciences.

**Keywords:** optimal trading; market impact; propagator model; Wiener–Hopf factorization; Gohberg–Krein factorization; fractional calculus; adapted stochastic control.

---

## Significance Statement

Trading a large order against a return-predicting signal with transient price impact requires choosing a rate that trades expected gain against the cost of moving the price. The problem has the convex-quadratic structure of Markowitz portfolio choice, with the impact operator playing the role of the return covariance, but the trading rate must use only past information and the impact operator is non-local in time. We solve this in closed form for a general stationary adapted signal using the causal-anticausal factorization of the impact cost operator: Wiener–Hopf on the whole line, Gohberg–Krein on a finite horizon. For power-law impact, the optimal rate is a fractional derivative of the forecast curve, of order set by the impact-decay exponent.

---

## Abstract

We solve the problem of maximizing expected gain from a return-predicting signal net of the impact cost of one's own trades, under a propagator impact model with a general symmetric positive-definite kernel. The Euler–Lagrange condition is a linear integral equation on trading schedules with a non-local, non-diagonal Hessian; the adaptedness constraint that trades use only past information couples this equation to a filtration structure absent from the deterministic literature. We show that the constraint is resolved by a causal-anticausal factorization of the cost operator — Wiener–Hopf on the whole line, Gohberg–Krein / Arveson outer factorization on a finite interval — combined with the adapted projection $P_+$. The resulting closed-form optimal rate is the causal square-root inverse of the impact operator applied to the adapted projection of its anticausal square-root inverse applied to the forecast curve. For the empirically supported power-law kernel with exponent $\beta\in(0,1)$, the whole-line factors are the Marchaud fractional integrals of an order depending on $\beta$, and the closed form collapses to a fractional derivative of order $1-\beta$ of the forecast curve. On a finite horizon $[0,T]$ the factorization is a weight-conjugated fractional integral, and the optimal rate is a boundary-deformed fractional derivative that converges pointwise to the whole-line fractional derivative in the interior at rate $O((\text{dist to boundary})^{-\nu})$.

---

## 1. Introduction

### 1.1 The gain–cost problem

Institutional trading of large orders — index rebalances, algorithmic strategies against short-horizon forecasts, hedges against derivative books — routinely moves quantities that are large multiples of top-of-book depth. Empirical studies of trade-and-quote data (1, 2, 3, 4) establish that each child order pushes the mid-price against the trader's direction and that the resulting *transient impact* is well described by a translation-invariant propagator kernel $G(t-s)$ that decays with lag: the price at time $t$ carries a term $\int_{s\le t}G(t-s)\,u_s\,ds$ from the trader's own past rate $u$. The cost of a large parent order therefore depends on the whole path of its execution schedule, not only on its instantaneous rate.

When the trader holds a return-predicting signal $\alpha_t$ — a short-horizon forecast of price change conditional on time-$t$ information — the gain from trading in the signal's direction competes with the impact cost of moving into the position. Under the propagator model of Bouchaud, Gefen, Potters and Wyart, extended by Gatheral (2, 3), the expected P\&L of an adapted rate $u\in L^2_{\rm adap}$ is a linear gain against a quadratic cost, and the *gain–cost problem* is

$$ \max_{u\in L^2_{\rm adap}}\ \mathbb{E}\!\int u_t\,\alpha_t\,dt \;-\; \tfrac{\gamma}{2}\,\mathbb{E}\!\iint G(|t-v|)\, u_t\, u_v\,dt\,dv, \tag{1} $$

with $\gamma>0$ a cost-aversion coupling. Write $C$ for the symmetric convolution $(Cu)(t) = \int G(|t-v|)u_v\,dv$, positive-definite ($\hat C(\xi)\ge 0$) to rule out static round-trip arbitrage. Two kernels run through the paper: the empirically supported power law $G(t) = |t|^{-\beta}$, $\beta\in(0,1)$ estimated at $0.2$–$0.6$ across markets and asset classes (1, 2, 3, 4), with symbol $\hat C(\xi) = c_\beta|\xi|^{\beta-1}$ and $c_\beta = 2\Gamma(1-\beta)\sin(\pi\beta/2)$; and the tractable exponential $G(t) = e^{-\kappa|t|}$, $\kappa>0$, with symbol $2\kappa/(\kappa^2+\xi^2)$. The power-law kernel is locally integrable but decays too slowly to be integrable at infinity for $\beta\le 1$; equivalently its symbol has a low-frequency singularity, and $C$ is unbounded on $L^2(\mathbb{R})$. The operator is well-defined between homogeneous Sobolev spaces, $C\colon \dot H^{-\nu}\to \dot H^\nu$ with $\nu=(1-\beta)/2$, and becomes a bounded operator on $L^2$ after either finite-horizon truncation to $[0,T]$ (the resulting kernel is weakly singular and $G_T$ is bounded on $L^2([0,T])$) or the addition of a temporary-impact regularizer $\tfrac12\eta u_t^2$ (§5.2). The exponential kernel is bounded on $L^2(\mathbb{R})$ without regularization. Our Fourier convention is $\hat f(\xi) = \int e^{i\xi t}f(t)\,dt$; a causal function (support in $t\ge 0$) has Fourier transform analytic in the upper half-plane.

**Analogy with Markowitz portfolio choice.** Problem (1) has the same convex-quadratic structure as the mean–variance portfolio problem (5, 6),
$$ \max_{w\in\mathbb{R}^N}\ w^\top\mu \;-\; \tfrac{1}{2}\lambda\, w^\top\Sigma w, \tag{2} $$
under the correspondence
$$ (w,\,\mu,\,\Sigma,\,\lambda) \;\longleftrightarrow\; (u,\,\alpha,\,C,\,\gamma). $$
The Markowitz optimum is $w^\star = \lambda^{-1}\Sigma^{-1}\mu$ with value $\tfrac{1}{2\lambda}\mu^\top\Sigma^{-1}\mu$ (the Mahalanobis norm of expected return, squared). The direct analog $u^\star = \gamma^{-1}C^{-1}\alpha$ would be the optimum of the trading problem if the schedule were unconstrained. Two features of the temporal problem block the direct analog:

*(i) Non-locality of the Hessian.* $C$ is a temporal convolution against a symmetric kernel, so $(Cu)(t)$ depends on $u_v$ for $v$ both before and after $t$.

*(ii) Adaptedness of the feasible set.* The trading rate $u_t$ at time $t$ must be $\mathcal{F}_t$-measurable; computing $(C^{-1}\alpha)_t$ requires future values of $\alpha$ which the trader does not have.

Both obstructions are resolved by the same tool: a causal-anticausal factorization $C = C_- C_+$ of the cost operator, combined with the adapted projection onto past-measurable processes. The factorization is Wiener–Hopf on the whole line and Gohberg–Krein on a finite interval. Once one is in place, the closed-form optimal trading rate is the causal square-root inverse of $C$ applied to the projection onto the past of its anticausal square-root inverse applied to the forecast curve — an operator recipe with no dependence on the specific kernel other than through the factorization itself. The Markowitz analogy motivates the setup; the paper works inside the operator framework of (1).

### 1.2 Prior treatments of problem (1)

Problem (1) has been treated in the mathematical execution literature under several kernel and signal specifications, all on a bounded interval $[0,T]$ with a terminal-inventory constraint.

*Deterministic constant-signal case.* Almgren and Chriss (7) introduced the finite-horizon execution problem with quadratic cost and derived closed-form schedules for exponential kernels. Obizhaeva and Wang (8) treated the same problem in a limit-order-book resilience framework. Gatheral, Schied and Slynko (9) solved the power-law-kernel case using Fredholm techniques, obtaining the U-shaped schedule with $(t(T-t))^{(\beta-1)/2}$ Söhngen–Tricomi boundary weights. In these papers the "signal" is a constant Lagrange multiplier fixed by the terminal-inventory constraint.

*Stochastic-signal case, exponential kernel.* Neuman and Voß (10) solved (1) for the exponential resilience kernel with a general semimartingale signal. The Markov property of the exponential kernel reduces the problem to a finite-dimensional linear-quadratic control via state augmentation, with a Riccati closed form. Cartea, Jaimungal and Penalva (11) develop the broader algorithmic-trading framework in which such signal-adaptive execution problems arise.

*Stochastic-signal case, general kernel.* Abi Jaber and Neuman (12) formulated the general adapted-signal problem in infinite-dimensional stochastic control terms; closed-form solutions require kernel-specific reductions. Abi Jaber and coauthors extended this to matrix-valued cross-impact kernels (13) and to constrained trading including battery-storage applications (14).

*Stochastic-signal case, power-law kernel.* Forde, Sánchez-Betancourt and Smith (15) solved the finite-horizon power-law problem for Gaussian signals by observing that the finite-interval cost operator admits the factorization $G_T = T\,T^*$ with $T$ a Volterra operator of Riemann–Liouville type, following Porter and Stirling (16, Examples 6.2, 9.2). The kernel of the Volterra representation of the optimal rate is expressed in terms of the fractional-integral factor $T$ inverted via the Chakrabarti–George Abel formula (17).

*Deterministic factorization theory.* Wiener and Hopf (18) introduced the factorization of scalar Fourier symbols on a half-line as the basis for solving convolution integral equations. Krein (19) developed the corresponding half-line integral-equation theory, and Wiener (20) applied the factorization to stationary linear prediction. Gohberg and Krein (21) established the finite-interval factorization $I+K = (I+L^*)(I+L)$ for positive kernels via Volterra triangularization, and Arveson (22) generalized the picture to positive operators on Hilbert spaces equipped with a continuous nest of projections, giving the outer-factorization theorem that subsumes both.

Across the execution literature the optimal trading rate is expressed as the solution of a horizon-tied Fredholm equation, as an integral against a resolvent kernel depending on $T$, or as Riccati feedback. Söhngen–Tricomi endpoint modes and terminal-inventory multipliers appear explicitly, and the signal enters through these horizon-tied objects. This paper establishes the connection between the finite-interval $T\,T^*$ factorization of (15, 16) and its infinite-horizon Wiener–Hopf limit, and gives the corresponding closed-form dependence of the optimal rate on the trader's forecast curve.

### 1.3 Contribution

We give a unified factorization framework for problem (1), covering both the whole-line stationary case and the finite-interval case, and a closed formula for the optimal adapted trading rate in terms of the trader's forecast curve.

**(i) The role of the forecast curve.** For an adapted signal $\alpha$ on $\mathbb{R}$, define the *forecast curve* at time $t$ as
$$ \bar\alpha(t,s) \;=\; \begin{cases}\alpha_s, & s\le t,\\ \mathbb{E}_t[\alpha_s], & s>t,\end{cases} $$
the $\mathcal{F}_t$-measurable function that records the realized past and the conditional-expectation future of the signal. The optimal trading rate at time $t$ is a specific linear functional of $\bar\alpha(t,\cdot)$, and the operator that produces it is horizon-independent up to boundary deformation.

**(ii) The factorization identity.** The adapted Wiener–Hopf identity
$$ (P_+\, C\, P_+)^{-1} \;=\; C_+^{-1}\, P_+\, C_-^{-1}, \tag{3} $$
holds for any factorization $C = C_-\, C_+$ into a causal $C_+$ (kernel supported on $\{s\le t\}$) and its adjoint $C_-$, and any orthogonal projection $P_+$ onto the adapted subspace of a filtered $L^2$ space. On the whole line the factorization is Wiener–Hopf; on $[0,T]$ it is Gohberg–Krein applied to the finite-interval cost operator $G_T$, giving $G_T = T\,T^*$ with $T$ Volterra. In both cases the optimal rate is
$$ u^\star \;=\; \gamma^{-1}\, C_+^{-1}\, P_+\, C_-^{-1}\,\alpha, \tag{4} $$
The three-step composition whitens the signal by the anticausal square-root inverse (using the forecast curve for future values), projects onto the past to obtain an adapted whitened signal, and un-whitens by the causal square-root inverse (which preserves adaptedness).

**(iii) Power-law closed form.** For the power-law kernel, the Wiener–Hopf factors on the whole line are the Marchaud fractional integrals $C_\pm = c_\beta^{1/2}\,I_\pm^\nu$ with $\nu = (1-\beta)/2$. Substituting into (4) yields
$$ u^\star_t \;=\; \gamma^{-1}\,\kappa_{1-\beta}\, (D_+^\nu\,\zeta)(t), \qquad \zeta_s \;=\; \bigl(D_-^\nu\,\bar\alpha(s,\cdot)\bigr)(s), \tag{5} $$
a fractional derivative of total order $1-\beta$ applied to the forecast curve, with $\kappa_{1-\beta} = c_\beta^{-1}$. On a finite horizon $[0,T]$, the Gohberg–Krein factors are the *weight-conjugated* fractional integrals
$$ T \;=\; B^{-1}\, I_+^\nu\, B, \qquad T^* \;=\; B\, I_-^\nu\, B^{-1}, \tag{6} $$
where $B$ is multiplication by the Söhngen–Tricomi endpoint weight, and the optimal rate is the *boundary-deformed* fractional derivative
$$ u^{\star,T}_t \;=\; \gamma^{-1}\, c_\beta^{-1}\, B(t)^{-1}\,\bigl(D_+^\nu\, B\, P_+\, B\, D_-^\nu\, B^{-1}\,\alpha^{\rm eff}\bigr)(t), \tag{7} $$
with $\alpha^{\rm eff}$ the effective signal (base signal plus KKT-multiplier corrections for the endpoint constraints). Far from the boundary, $B$ becomes locally constant and (7) collapses to (5). The rate of convergence is $O(d(t)^{-\nu})$ with $d(t)=\min(t,T-t)$, giving a quantitative interior asymptotic and quantitative control on the horizon-truncation error.

The three-step architecture — anticausal whitening, projection, causal coloring — parallels Wiener–Kolmogorov linear prediction of a stationary process from its own past (20), with the cost outer factor $C_+$ playing the role of the process spectral square-root $S_+$. The factorization identity (3) appears in nest-algebra operator theory (22); its use to close the signal-adaptive gain-cost trading problem gives the resulting fractional-derivative formula (5)–(7). Applied to the finite-interval Gohberg–Krein factors of (15, 16), Lemma 1 reproduces the operator form of Forde–Sánchez-Betancourt–Smith (15, Thm 2.2). The whole-line stationary Wiener–Hopf treatment, the forecast-curve representation of the acausal step, and the quantitative interior asymptotic (Proposition 3) are the new content.

---

## 2. The Gain–Cost Problem in Operator Form

### 2.1 Setup

Fix a filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t\in\mathbb{R}}, \mathbb{P})$ satisfying the usual conditions. The signal $\alpha$ is a mean-zero, progressively measurable process with stationary spectral density $S_\alpha(\xi)$ satisfying $\int(1+|\xi|^{2(1-\beta)+\epsilon})\,S_\alpha(\xi)\,d\xi<\infty$ for some $\epsilon>0$. Let $L^2 = L^2(\Omega\times\mathbb{R})$ with reference measure $\mathbb{P}\otimes dt$, and let $L^2_{\rm adap}\subset L^2$ denote the closed subspace of adapted processes: those $u$ with $u_t\in\mathcal{F}_t$ for a.e.\ $t$. Denote by $P_+$ the $L^2$-orthogonal projection onto $L^2_{\rm adap}$; pointwise,
$$ (P_+ X)_s \;=\; \mathbb{E}_s[X_s], $$
which coincides with the optional projection restricted to $L^2$.

The cost operator $C$ is the deterministic convolution against a symmetric kernel $G$,
$$ (Cu)(t) \;=\; \int G(|t-v|)\, u_v\, dv, \qquad \hat C(\xi)\ge 0 \text{ on } \xi\ne 0, $$
acting on $L^2$ diagonally in $\omega$. Positive-definiteness of $\hat C$ ensures strict convexity of the quadratic penalty in (1) on $L^2_{\rm adap}$. For the power-law kernel $C$ is unbounded on $L^2(\mathbb{R})$ (§1.1); we interpret $C\colon \dot H^{-\nu}\to \dot H^\nu$ between homogeneous Sobolev spaces, so that $P_+ C P_+$ is a symmetric strictly positive form on $L^2_{\rm adap}\cap\dot H^{-\nu}$ and the standing spectral hypothesis on $\alpha$ ensures $u^\star\in L^2_{\rm adap}$. On the finite interval $[0,T]$ the kernel is weakly singular and $G_T$ is bounded on $L^2([0,T])$ without further regularization.

The *forecast curve* at time $t$ is
$$ \bar\alpha(t,s) \;=\; \begin{cases}\alpha_s, & s\le t,\\ \mathbb{E}_t[\alpha_s], & s>t.\end{cases} \tag{8} $$

### 2.2 The adapted first-order condition

Taking the Gâteaux derivative of the objective in (1) against adapted variations $\delta u\in L^2_{\rm adap}$ and using $\mathbb{E}[u\,\mathbb{E}_t[\cdot]] = \mathbb{E}[u\cdot]$ for adapted $u$ gives the *adapted first-order condition*
$$ \gamma\,\mathbb{E}_t\!\bigl[(C u^\star)(t)\bigr] \;=\; \alpha_t \quad\text{for a.e.\ } t. \tag{9} $$
Equivalently in operator form: $\gamma\, P_+ C P_+\, u^\star = \alpha$ with $u^\star, \alpha \in L^2_{\rm adap}$.

The Hessian $\gamma\, P_+ C P_+$ is a symmetric strictly positive operator on $L^2_{\rm adap}$ (strict convexity follows from $\hat C>0$ on $\xi\ne 0$ via Plancherel applied to the extension by zero of any adapted $u$). It admits a bounded two-sided inverse, and (9) has a unique solution
$$ u^\star \;=\; \gamma^{-1}\,(P_+\, C\, P_+)^{-1}\,\alpha. \tag{10} $$
The remainder of the paper computes the projected inverse in closed form.

---

## 3. Factorization of the Cost Operator

The strategy is to split $C$ as a causal-anticausal product and reduce the projected inverse to a three-step alternating operator. This section states the factorization in both settings — whole line and finite interval — and proves the projected-inverse identity that underlies the closed-form solution.

### 3.1 Whole line: Wiener–Hopf factorization

**Proposition 1 (Wiener–Hopf factorization).** *Let $\hat C(\xi)\ge 0$ with $\log\hat C(\xi)/(1+\xi^2)\in L^1(\mathbb{R})$. Then $\hat C$ admits a factorization*
$$ \hat C(\xi) \;=\; \hat C_-(\xi)\,\hat C_+(\xi), \tag{11} $$
*with $\hat C_+$ analytic and non-vanishing in the closed upper half-plane, $\hat C_-$ analytic in the closed lower half-plane, and $\overline{\hat C_+(\xi)} = \hat C_-(\xi)$; equivalently $C_+^* = C_-$. In the time domain, $C_+$ has kernel supported on $\{s\le t\}$ (causal Volterra) and $C_-$ on $\{s\ge t\}$ (anticausal). The factorization is unique up to a positive multiplicative constant.*

Existence is classical (18, 19). For the two kernels of interest:

*Power-law.* $\hat C(\xi) = c_\beta|\xi|^{\beta-1} = c_\beta\,(i\xi)^{-\nu}\,(-i\xi)^{-\nu}$ with $\nu = (1-\beta)/2$ and standard branches. The time-domain factors are the causal and anticausal Riemann–Liouville fractional integrals of order $\nu$:
$$ C_+ \;=\; c_\beta^{1/2}\,I_+^\nu, \quad (I_+^\nu f)(t) = \tfrac{1}{\Gamma(\nu)}\!\int_{-\infty}^{t}(t-s)^{\nu-1}f(s)\,ds; \qquad C_- \;=\; c_\beta^{1/2}\,I_-^\nu. \tag{12} $$
Inverses are the Marchaud fractional derivatives $C_\pm^{-1} = c_\beta^{-1/2}\, D_\pm^\nu$ (23, §5.4). In the notation of (11), $\hat C_+(\xi) = c_\beta^{1/2}(-i\xi)^{-\nu}$ (analytic in the upper half-plane) and $\hat C_-(\xi) = c_\beta^{1/2}(i\xi)^{-\nu}$.

*Exponential.* $\hat C(\xi) = 2\kappa/(\kappa^2+\xi^2) = \sqrt{2\kappa}/(\kappa-i\xi)\cdot\sqrt{2\kappa}/(\kappa+i\xi)$. The inverses of the factors are the first-order differential operators $C_+^{-1} = (2\kappa)^{-1/2}(\kappa+\partial_t)$ and $C_-^{-1} = (2\kappa)^{-1/2}(\kappa-\partial_t)$.

### 3.2 Finite interval: Gohberg–Krein factorization

On $[0,T]$ translation invariance is lost, Fourier factorization does not apply, and the appropriate analog is the Volterra-triangular factorization of Gohberg and Krein (21), abstractly the Arveson outer factorization on a continuous nest (22).

**Proposition 2 (Gohberg–Krein factorization).** *Let $G_T$ be the restriction of $C$ to $L^2([0,T])$, viewed as an integral operator with kernel $G(|t-v|)\mathbf{1}_{[0,T]^2}$. If $G_T$ is a strictly positive compact perturbation of the identity on $L^2([0,T])$ (equivalently, its symbol satisfies the whole-line Wiener–Hopf hypothesis), then $G_T$ admits a factorization*
$$ G_T \;=\; T\, T^*, \tag{13} $$
*with $T$ a bounded Volterra operator on $L^2([0,T])$: its kernel is supported on $\{s\le t\}\cap[0,T]^2$, and $T^*$ is the adjoint (kernel supported on $\{s\ge t\}$). The factor $T$ is unique up to a left unitary on $L^2([0,T])$.*

The factorization is the Arveson outer factorization of the positive operator $G_T$ with respect to the continuous nest of projections $\{P_{[0,t]}\}_{t\in[0,T]}$ (22, Thm.\ 4.4.2; 16, Ex.\ 6.2/9.2).

*Power-law case.* The classical explicit construction (15, 16) gives
$$ (T\varphi)(t) \;=\; \int_0^t \kappa(s,t)\,\varphi(s)\,ds, \qquad \kappa(s,t) \;=\; c_\beta^{1/2}\,(t/s)^{(1-\beta)/2}\,(t-s)^{\nu-1}/\Gamma(\nu), \tag{14} $$
Equivalently, $T$ is a causal Riemann–Liouville integral of order $\nu$ conjugated by an endpoint-weight multiplication:
$$ T \;=\; c_\beta^{1/2}\, B^{-1}\, I_+^\nu\, B, \qquad T^* \;=\; c_\beta^{1/2}\, B\, I_-^\nu\, B^{-1}, \qquad B(t) = t^{-\nu}, \tag{15} $$
so that $G_T = T\,T^* = c_\beta\, B^{-1}\, I_+^\nu\, B^2\, I_-^\nu\, B^{-1}$ is the weight-conjugated form consistent with the whole-line factorization (12). Here $B$ is multiplication by an unbounded weight on $L^2([0,T])$; $T$ acts boundedly between the weighted Sobolev spaces of Porter–Stirling (16, Ex. 6.2/9.2) and Samko–Kilbas–Marichev (23, §13.5).

The Volterra factor $T$ is a causal fractional integrator of order $\nu$ sandwiched between endpoint-weight multiplications; the weight absorbs the loss of translation invariance at the left endpoint. The Gohberg–Krein outer factor is unique only up to a left unitary, and the choice above pins it to the left-endpoint nest $\{P_{[0,t]}\}$; the resulting $T$ breaks manifest $t\leftrightarrow T{-}t$ symmetry while $G_T=TT^*$ preserves it.

### 3.3 The adapted projected inverse

**Lemma 1 (Adapted inverse via causal-anticausal factorization).** *Let $\mathcal{H}$ be either $L^2(\mathbb{R})$ or $L^2([0,T])$, tensored with $L^2(\Omega)$ against the filtered measure. Let $C = C_-\, C_+$ be a factorization of a symmetric strictly positive operator on $\mathcal{H}$ into a causal Volterra factor $C_+$ (kernel supported on $\{s\le t\}$) and its adjoint $C_- = C_+^*$. Let $P_+$ be the $L^2$-orthogonal projection onto adapted processes. Then on the adapted subspace,*
$$ (P_+\, C\, P_+)^{-1} \;=\; C_+^{-1}\, P_+\, C_-^{-1}. \tag{16} $$

*Proof.* Causality of $C_+$ (kernel on $\{s\le t\}$) gives $P_+^\perp\, C_+\, P_+ = 0$: $C_+$ maps adapted processes to adapted processes, so $C_+^{-1}$ commutes with $P_+$ on adapted inputs. The adjoint identity is $P_+\, C_-\, P_+^\perp = 0$. For adapted $u$, $P_+ C P_+ u = P_+ C_- C_+ u = P_+ C_-\cdot(C_+ u)$; applying $C_+^{-1} P_+ C_-^{-1}$ gives $C_+^{-1} P_+ C_-^{-1}\, P_+ C_- (C_+ u)$; the inner action $P_+ C_-^{-1} P_+ C_-$ acts as $P_+$ on the adapted vector $C_+ u$, so the composition returns $u$. The abstract statement covers both the Wiener–Hopf whole-line factorization and the Gohberg–Krein/Arveson finite-interval factorization, since only causality of $C_+$ and self-adjointness of $C$ enter. $\blacksquare$

### 3.4 Closed-form optimal trading rate

Combining (10) and (16):

**Theorem 1 (Closed-form optimal rate).** *Under the hypotheses of §2.1, the unique adapted solution of (9) is*
$$ u^\star \;=\; \gamma^{-1}\, C_+^{-1}\, P_+\, C_-^{-1}\, \alpha, \tag{17} $$
*understood in either setting: on the whole line with $C_\pm$ the Wiener–Hopf factors, or on $[0,T]$ with $C_\pm = T$, $T^*$ the Gohberg–Krein factors of $G_T$ and $\alpha$ replaced by the effective signal $\alpha^{\rm eff} = \alpha + \sum_k\mu_k\psi_k$ built by adjoining KKT multipliers for each linear position constraint.*

The acausal factor $C_-^{-1}$ applied to the adapted signal $\alpha$ at time $s$ requires the future path $\{\alpha_r\}_{r\ge s}$, which is not in $\mathcal{F}_s$. The adapted projection replaces this future by its conditional expectation, and commutation of the deterministic operator $C_-^{-1}$ with conditional expectation on the argument variable (24, Prop. 2.6.13) gives
$$ \bigl(P_+\, C_-^{-1}\,\alpha\bigr)_s \;=\; \bigl(C_-^{-1}\,\bar\alpha(s,\cdot)\bigr)(s). \tag{18} $$
The optimal rate is therefore
$$ u^\star_t \;=\; \gamma^{-1}\,C_+^{-1}\,\zeta\,\bigl|_{t}, \qquad \zeta_s \;=\; \bigl(C_-^{-1}\,\bar\alpha(s,\cdot)\bigr)(s). \tag{19} $$
The forecast curve enters only through the inner $C_-^{-1}$ step; $C_+^{-1}$ then samples the adapted process $\zeta$ over $s\le t$, producing an $\mathcal{F}_t$-measurable rate.

### 3.5 The value of the problem

The value attained at $u^\star$ has the tradeability-norm form
$$ V(\alpha) \;=\; \tfrac{1}{2\gamma}\,\|P_+\, C_-^{-1}\,\alpha\|_{L^2}^2 \;=\; \tfrac{1}{2\gamma}\,\mathbb{E}\!\int|\zeta_s|^2\,ds, \tag{20} $$
by convex duality of the quadratic Legendre transform in $L^2_{\rm adap}$. Define the *tradeability norm* $\|\alpha\|_{\rm trad} := (\gamma^{-1}\,\mathbb{E}\!\int|P_+\, C_-^{-1}\alpha|^2)^{1/2} = (2V(\alpha))^{1/2}$. On the whole line under the power-law kernel this becomes the fractional Sobolev $H^{(1-\beta)/2}$-norm of the forecast curve: signal value is weighted by $|\xi|^{1-\beta}$ in the frequency domain, so faster-decaying forecasts of a given power spectrum carry more per-unit-variance tradeable value than slower-decaying ones.

---

## 4. The Power-Law Kernel

The Wiener–Hopf and Gohberg–Krein factors under the power-law kernel are fractional integrals. Theorem 1 reduces, on the whole line, to a fractional derivative of the forecast curve; on a finite interval, to a boundary-deformed fractional derivative.

### 4.1 Bulk formula on the whole line

Substituting $C_\pm^{-1} = c_\beta^{-1/2}\,D_\pm^\nu$ into (19):

**Corollary 1 (Power-law bulk formula).** *For $G(t) = |t|^{-\beta}$ with $\beta\in(0,1)$, $\nu = (1-\beta)/2$, and $\alpha$ stationary adapted satisfying the standing spectral hypothesis of §2.1,*
$$ u^\star_t \;=\; \gamma^{-1}\,\kappa_{1-\beta}\,(D_+^\nu\,\zeta)(t), \qquad \zeta_s \;=\; \bigl(D_-^\nu\,\bar\alpha(s,\cdot)\bigr)(s), \tag{21} $$
*with $\kappa_{1-\beta} = c_\beta^{-1}$.*

The intermediate process $\zeta$ has stationary power spectrum $c_\beta^{-1}|\xi|^{1-\beta}\,S_\alpha(\xi)$: the inner fractional differentiation $D_-^\nu$ cancels the frequency dependence of the impact operator, and the outer $D_+^\nu$ colors the whitened process causally. The composition is a fractional derivative of total order $1-\beta$ acting on the forecast curve.

For OU $\alpha$ with mean-reversion rate $\theta$, direct Marchaud integration against the exponential forecast tail gives $(D_-^\nu\bar\alpha(t,\cdot))(t) = \theta^\nu\alpha_t$, so
$$ u^{\star,\,\rm OU}_t \;=\; \gamma^{-1}\,\kappa_{1-\beta}\,\theta^\nu\,(D_+^\nu\alpha)(t), \qquad \mathbb{E}\bigl[u^{\star,\,\rm OU}_t\,\bigm|\,\alpha_t\bigr] \;=\; \gamma^{-1}\,\kappa_{1-\beta}\,\theta^{1-\beta}\,\alpha_t, \tag{22} $$
positive for every $\beta\in(0,1)$ and every $\theta>0$: the scale-free causal inverse has no zero on the imaginary axis, so no sign-flip phase transition occurs as $\theta$ varies (contrast the exponential kernel, §5.1). The OU signal satisfies the standing spectral hypothesis of §2.1 for $\beta>1/2$; for $\beta\le 1/2$ the OU spectrum $\sigma^2/(\theta^2+\xi^2)$ fails high-frequency integrability against $|\xi|^{2(1-\beta)+\epsilon}$, and (22) is made rigorous by adding a temporary-impact regularization (§5.2) or by working with increments of $\alpha$.

### 4.2 Boundary-deformed formula on a finite interval

Substituting (15) into Theorem 1:

**Corollary 2 (Power-law finite-interval formula).** *For $G(t) = |t|^{-\beta}$ on $[0,T]$, the adapted optimal rate is*
$$ u^{\star,T}_t \;=\; \gamma^{-1}\,c_\beta^{-1}\, B(t)^{-1}\,\bigl(D_+^\nu\, B\, P_+\, B\, D_-^\nu\, B^{-1}\,\alpha^{\rm eff}\bigr)(t), \tag{23} $$
*where $B(t) = t^{-\nu}$ (the multiplications by $B$ commute with $P_+$ since $B$ is deterministic; the split form emphasises the origin of each $B$ from the $T$ and $T^*$ factors) and $\alpha^{\rm eff} = \alpha + \sum_k\mu_k\psi_k$ is the effective signal including KKT-multiplier corrections for endpoint constraints; the multipliers $\mu_k$ solve a finite linear system from the constraint equations.*

The composition applies, in order: (i) endpoint weight $B^{-1}$ to the effective signal; (ii) anticausal Marchaud derivative $D_-^\nu$; (iii) reweighting by $B$; (iv) adapted projection; (v) reweighting by $B$; (vi) causal Marchaud derivative $D_+^\nu$; (vii) endpoint weight $B^{-1}$. The three multiplication operators arise from the two Gohberg–Krein factorizations of (15) substituted into $u^\star = \gamma^{-1}T^{-1}P_+(T^*)^{-1}\alpha^{\rm eff}$.

Formula (23) is a *boundary-deformed fractional derivative*: the whole-line composition $D_+^\nu\,P_+\,D_-^\nu$ of (21) is preserved as the operator core; the boundary weights $B, B^{-1}$ sandwich it and absorb the two-endpoint geometry into local multiplicative rescalings.

### 4.3 Interior asymptotic and rate of convergence

As $T\to\infty$, (23) converges pointwise to (21) in the interior. Let $d(t) = \min(t,T-t)$ be the distance from $t$ to the nearest boundary. Centering at the midpoint $t = T/2 + t'$, the weight $B(T/2+t') = (T/2+t')^{-\nu}$ factors as a $T$-dependent scalar $(T/2)^{-\nu}$ times a slowly varying interior factor $(1+2t'/T)^{-\nu}$. The scalar cancels in the $B^{-1}\cdot B$ conjugations of (23), and the interior factor converges to 1 uniformly on compact $t'$ sets. Similarly, the Volterra kernel $\kappa(s,t)$ of (14) satisfies $(t/s)^{(1-\beta)/2}\to 1$ centered at the interior, and $\kappa(T/2+s',T/2+t')\to c_\nu(t'-s')^{\nu-1}$, the whole-line causal Riemann–Liouville kernel.

**Proposition 3 (Interior error bound).** *For $\alpha$ bounded and effective signal with $\|\alpha^{\rm eff}\|_{\rm trad}<\infty$,*
$$ \bigl|u^{\star,T}_t - u^{\star,\mathbb{R}}_t\bigr| \;\le\; C_1(\beta)\,\|\alpha\|_{L^\infty}\, d(t)^{-\nu} \;+\; C_2(\beta)\,\|\alpha^{\rm eff}\|_{\rm trad}\, T^{-\nu}\, d(t)^{-\nu}, \tag{24} $$
*with $\nu = (1-\beta)/2$ and $C_1(\beta), C_2(\beta)$ $\beta$-dependent constants.*

The first term is the Marchaud truncation error from cutting the fractional-derivative tail at the boundary; the second is the contribution of the two Söhngen–Tricomi endpoint modes (see §4.4) with KKT coefficients bounded uniformly in $T$ (15, Prop. 3.2). For empirical $\beta\in(0.2,0.6)$, $\nu\in(0.2,0.4)$, giving slow $d(t)^{-\nu}$ interior convergence — a quantitative expression of the long spatial memory of the impact kernel.

### 4.4 Söhngen–Tricomi endpoint modes

The finite-interval solution (23) includes an endpoint contribution from the KKT multipliers. Each linear constraint $\int_0^T\psi_k(t)u_t\,dt = c_k$ produces one multiplier $\mu_k$ and adds $\mu_k\psi_k$ to the effective signal; the corresponding contribution to $u^{\star,T}$ is $\mu_k\, G_T^{-1}\psi_k$. For the terminal-inventory constraint $\psi_1 \equiv 1$, this contribution is proportional to
$$ G_T^{-1}(1)(t) \;\propto\; \bigl(t(T-t)\bigr)^{(1-\beta)/2}, $$
a smooth bump vanishing at the endpoints (9, Ex. 2.30; 15, eq. 22).

The associated *Söhngen–Tricomi weights* $(t(T-t))^{(\beta-1)/2}$ and $\tfrac{T-2t}{2}(t(T-t))^{(\beta-1)/2}$ appear as the two-dimensional null space of the intermediate operator obtained by differentiating and weight-conjugating $G_T u = f$ into a Cauchy-kernel airfoil equation (25, 26; 23, §13.5). They encode the two endpoint degrees of freedom in the schedule and are set by KKT multipliers on endpoint constraints (initial inventory, terminal inventory, intermediate pegs). In the interior long-horizon limit these boundary contributions decay pointwise as $T^{-\nu}$, giving the second term of (24).

---

## 5. Discussion

### 5.1 Exponential kernel

Substituting the exponential-kernel factors into Theorem 1 gives
$$ u^{\star,\,\rm exp}_t \;=\; \frac{1}{2\kappa\gamma}\,(\kappa+\partial_t)\,\zeta_t, \qquad \zeta_s \;=\; (\kappa-\partial_r)\,\bar\alpha(s,r)\bigl|_{r=s^+}. \tag{25} $$
For OU $\alpha$ with mean reversion $\theta$: $\zeta_s = (2\kappa)^{-1/2}(\kappa+\theta)\alpha_s$ and
$$ u^{\star,\,\rm exp}_t \;=\; \frac{\kappa+\theta}{2\kappa\gamma}\bigl[(\kappa-\theta)\alpha_t + \sigma\dot W_t\bigr], \qquad \mathbb{E}\bigl[u^{\star,\,\rm exp}_t\,\bigm|\,\alpha_t\bigr] \;=\; \frac{\kappa^2-\theta^2}{2\kappa\gamma}\,\alpha_t. \tag{26} $$
The conditional expectation flips sign at $\theta = \kappa$: signals decaying faster than the impact tail are traded against on average, since the impact tail from any signal-following trade would outlive the signal itself. The power-law analog (22) has no such sign flip — the scale-free causal inverse has a branch point at $\xi=0$ and no zero on the imaginary axis, so no zero–pole crossing occurs as $\theta$ varies.

### 5.2 Temporary impact

Adding a temporary-impact term $\tfrac12\eta u_t^2$ modifies the FOC symbol to $M(\xi) = c_\beta|\xi|^{\beta-1}+\eta/\gamma$. The added constant provides high-frequency coercivity that the pure power-law symbol lacks, so $u^\star\in L^2$ without spectral-decay assumptions on $\alpha$. Wiener–Hopf factorization of $M$ gives modified one-sided factors; the crossover frequency $\xi_* = (\gamma c_\beta/\eta)^{1/(1-\beta)}$ separates a long-memory fractional regime ($|\xi|\ll\xi_*$) from a myopic signal-following regime ($|\xi|\gg\xi_*$) in which $u^\star\approx\alpha/\eta$. The $\eta\to 0$ limit is singular but recovers (21) under the spectral-decay hypothesis of §2.1.

### 5.3 Multi-asset extension

For a cross-impact kernel $\mathbf{K}(t) = |t|^{-\beta}\mathbf{A}$ with $\mathbf{A} = Q\Lambda Q^\top$ symmetric positive-definite, Theorem 1 diagonalizes in the eigenbasis of $\mathbf{A}$: the scalar fractional-derivative rule (21) applies independently to each principal-component alpha with eigenvalue prefactor $\Lambda_{ii}^{-1}$.

### 5.4 Numerical implementation

Fractional derivatives discretize to Toeplitz matrices. On a uniform grid of $N$ points, $D_\pm^\nu$ is a lower- or upper-triangular Toeplitz whose entries are generalized binomial coefficients from the expansion of $(1-z)^\nu$. Evaluating (21) costs $O(N\log N)$ per time step via FFT, compared with $O(N^2)$ Nyström inversion of the Fredholm equation. The finite-interval formula (23) adds two diagonal multiplications by $B$ and $B^{-1}$, preserving the $O(N\log N)$ cost.

### 5.5 Role of the forecast curve

Theorem 1 makes explicit that the optimal rate at time $t$ depends on the *entire* forecast curve $\bar\alpha(t,\cdot)$. The stationary time series of optimal rates against a given signal is a deterministic functional of the family of forecast curves. Two implications for practice.

*Signal engineering.* The tradeable value $V(\alpha) = \tfrac{1}{2\gamma}\mathbb{E}|\zeta|^2$ from (20) weights the forecast spectrum by $|\xi|^{1-\beta}$, an operational specification that differs from an $R^2$ of the signal against future returns. Two signals with identical $R^2$ can differ arbitrarily in tradeable value once their timescales differ, and the fractional-order weighting gives an operational specification of what makes one forecast better than another for a given impact kernel.

*Forecast horizon.* The Marchaud representation of $D_-^\nu$ averages forecast increments $\bar\alpha(s,r) - \bar\alpha(s,s)$ over all future lags $r > s$ with weight $(r-s)^{-1-\nu}$. Forecasts are required over all horizons; horizon truncation gives an error decaying like $r_{\max}^{-\nu}$ in the maximum forecast horizon.

---

## 6. Concluding Remarks

The gain–cost trading problem admits a closed-form solution once the causal-anticausal factorization of the impact cost operator is in place: Wiener–Hopf on the whole line, Gohberg–Krein on a finite interval, both instances of Arveson outer factorization for positive operators on a continuously nested Hilbert space. The optimal adapted rate is the causal square-root inverse of the cost operator applied to the adapted projection of its anticausal square-root inverse applied to the trader's forecast curve, an operator recipe insensitive to the kernel beyond the factorization itself.

For the power-law kernel, the whole-line factors are the Marchaud fractional integrals, and the recipe collapses to a fractional derivative of order $1-\beta$ applied to the forecast curve. On a finite horizon the fractional integrals acquire endpoint-weight conjugations from the Gohberg–Krein factorization, and the optimal rate is a boundary-deformed fractional derivative that converges to the bulk formula in the interior at rate $O(d(t)^{-\nu})$.

The joint gain–risk–cost problem inherits the same operator structure once the two frictions share a coordinate. Cost acts on the trading rate $u$; a mean–variance holding penalty $\tfrac{\lambda}{2}\mathbb{E}\int x_t^\top\Sigma x_t\,dt$ acts on the position $x_t = \int_{-\infty}^t u_s\,ds$, which in rate coordinates is the operator with Fourier symbol $\lambda\Sigma/\xi^2$. Adding it to (1) replaces $C$ by the symbol $\gamma\hat C(\xi) + \lambda\Sigma/\xi^2$ — still a positive Toeplitz operator, admitting Wiener–Hopf and Gohberg–Krein factorization, to which Lemma 1 applies without modification. The pure trading limit ($\lambda\to 0$) and the pure holding limit ($\gamma\to 0$) are the two boundaries of this joint factorization.

---

## 7. Materials and Methods

**Proof of Lemma 1 (whole-line case).** With $C_\pm = c_\beta^{1/2} I_\pm^\nu$ on $L^2(\mathbb{R})$, $C_\pm$ are Hilbert-space isomorphisms between $\dot H^{-\nu}$ and $L^2$ (respectively $L^2$ and $\dot H^\nu$) by Plancherel and the symbol $c_\beta^{1/2}|\xi|^{(\beta-1)/2}$. Their adjointness $C_+^* = C_-$ follows from the kernel-flip $(t-s)^{\nu-1}\mathbf{1}_{s\le t}\mapsto(s-t)^{\nu-1}\mathbf{1}_{t\le s}$. On $L^2_{\rm adap}\cap\dot H^{-\nu}$ the composition $P_+ C P_+$ is bounded, symmetric, and strictly positive (from $\hat C > 0$ on $\xi\ne 0$), hence boundedly invertible on its range. Causality of $C_+$ implies $P_+^\perp C_+ P_+ = 0$, so $C_+$ preserves $L^2_{\rm adap}$ and $C_+^{-1}$ commutes with $P_+$ on adapted inputs. The adjoint identity $P_+ C_- P_+^\perp = 0$ follows. Taking adjoints of $C_+^{-1}\colon L^2 \to \dot H^{-\nu}$ gives $P_+ C_-^{-1} P_+^\perp = 0$ as well, so $C_-^{-1}$ preserves $L^2_{\rm adap}^\perp$. For adapted $u$: $P_+ C P_+ u = P_+ C_- C_+ u$; applying $C_+^{-1} P_+ C_-^{-1}$ returns $u$ via $P_+ C_-^{-1} P_+ C_-$ acting as $P_+$ on the adapted vector $C_+ u$.

**Proof of Lemma 1 (finite-interval case).** Replace $C_\pm$ by the Gohberg–Krein factors $T, T^*$ of Proposition 2. Volterra causality of $T$ (kernel on $\{s\le t\}\cap[0,T]^2$) gives $P_+^\perp T P_+ = 0$ and $P_+ T^* P_+^\perp = 0$; the composition argument of the whole-line case then applies verbatim.

**Existence of the outer factor.** The Wiener–Hopf factorization on $\mathbb{R}$ under the log-integrability hypothesis is classical (18, 19). The finite-interval $G_T = TT^*$ factorization is Arveson's outer factorization theorem for positive operators on a continuous nest (22, Thm 4.4.2); an equivalent constructive proof for symmetric weakly-singular integral kernels via spectral square root is in (16, Ex. 6.2/9.2); the explicit weight-conjugation form (14)–(15) for the power-law kernel is derived in (15, pp. 590–591).

**Proof of Corollary 1.** Define the candidate $u^{\rm cand}_t := \gamma^{-1}\kappa_{1-\beta}(D_+^\nu\zeta)(t)$. Adaptedness: $D_+^\nu$ at time $t$ depends only on $\{\zeta_s\}_{s\le t}$, and each $\zeta_s \in \mathcal{F}_s\subset\mathcal{F}_t$ by (18) and $\mathcal{F}_s$-measurability of the forecast curve. FOC verification proceeds in three steps.

*Step (a).* Conditional Fubini (27, Thm 14.16) applied to the Marchaud representation gives $\mathbb{E}_t[(D_+^\nu\zeta)(v)] = (D_+^\nu \hat\zeta_t)(v)$ with $\hat\zeta_t(s) := \mathbb{E}_t[\zeta_s]$.

*Step (b).* For $s \le t$: $\zeta_s \in \mathcal{F}_s\subset\mathcal{F}_t$, so $\hat\zeta_t(s) = \zeta_s$. For $s > t$: by tower and conditional Fubini applied at conditioning time $t$, $\hat\zeta_t(s) = (D_-^\nu\bar\alpha(t,\cdot))(s)$.

*Step (c).* The symbol identity $\hat C(\xi)(-i\xi)^\nu = c_\beta(i\xi)^{-\nu}$ yields the operator identity $C\,D_+^\nu = c_\beta I_-^\nu$ on $L^2(\mathbb{R})$. Substituting and using $\gamma\kappa_{1-\beta} = \gamma/c_\beta$:
$$ \gamma\,\mathbb{E}_t\!\bigl[(Cu^{\rm cand})(t)\bigr] = (I_-^\nu\hat\zeta_t)(t) = (I_-^\nu D_-^\nu\bar\alpha(t,\cdot))(t) = \bar\alpha(t,t) = \alpha_t, $$
using $I_-^\nu D_-^\nu = \mathrm{id}$ on $H^\nu(\mathbb{R})$ (23, §5.3 Thm 5.3), applied to the future-half-line piece of the forecast curve, which is in $H^\nu$ pathwise under the standing spectral hypothesis, and the fact that $I_-^\nu$ at $t$ samples only $\hat\zeta_t(s)$ for $s\ge t$, where Step (b) gives the closed form.

*Uniqueness.* $\hat C(\xi) = c_\beta|\xi|^{\beta-1}>0$ on $\xi\ne 0$, so the quadratic penalty in (1) is strictly convex on $L^2_{\rm adap}$ and the adapted FOC has a unique solution.

*Admissibility.* The spectral hypothesis ensures $|\xi|^{1-\beta}\widehat{\bar\alpha}(\xi)\in L^2$ pathwise, so $u^\star\in L^2_{\rm adap}$ by Plancherel. $\blacksquare$

**Proof of Corollary 2.** The anticausal Marchaud derivative $D_-^\nu$ in (23) acts on $\alpha^{\rm eff}$ extended by zero outside $[0,T]$, the natural convention for the finite-interval Volterra calculus (23, §13.5). Substitute (15) into (17): $u^{\star,T} = \gamma^{-1}\,T^{-1}\,P_+\,(T^*)^{-1}\,\alpha^{\rm eff}$ with $T^{-1} = c_\beta^{-1/2}\, B^{-1} D_+^\nu B$ and $(T^*)^{-1} = c_\beta^{-1/2}\, B D_-^\nu B^{-1}$ (inverting (15) using $(I_\pm^\nu)^{-1} = D_\pm^\nu$). Collecting the two $c_\beta^{-1/2}$ factors into $c_\beta^{-1}$ gives (23). $T^{-1}$ is a Volterra operator between the appropriate weighted Sobolev spaces (23, §13.5), not on $L^2$ directly. Adaptedness follows from causality of $T^{-1}$ (Volterra inverse of Volterra is Volterra). $\blacksquare$

**Proof of Proposition 3.** The Marchaud tail bound: $|(D_-^\nu f)(s) - (D_-^{\nu,[0,T]}f)(s)| \le \tfrac{2\|f\|_\infty}{\nu}(T-s)^{-\nu}$ from
$$ (D_-^\nu f)(s) = \tfrac{\nu}{\Gamma(1-\nu)}\!\int_0^\infty \tfrac{f(s)-f(s+r)}{r^{1+\nu}}\,dr, $$
truncated at $r = T-s$. Symmetrically the outer $D_+^\nu$ contributes a tail bounded by $t^{-\nu}$. The dominant interior truncation is on the closer boundary, giving the first term of (24). The Söhngen–Tricomi mode $\phi_1(t) = [t(T-t)]^{(\beta-1)/2}$ satisfies $|\phi_1(t)|\le d(t)^{-\nu}(T-d(t))^{-\nu}\le d(t)^{-\nu}(T/2)^{-\nu}$, and its KKT coefficient is bounded uniformly in $T$ by $\|\alpha^{\rm eff}\|_{\rm trad}$ (15, Prop. 3.2). This gives the second term of (24). $\blacksquare$

**Data availability.** No empirical data are used in this paper.

---

## References

1. Lillo F, Farmer JD, Mantegna RN (2003) Master curve for price-impact function. *Nature* 421:129–130.
2. Bouchaud J-P, Gefen Y, Potters M, Wyart M (2004) Fluctuations and response in financial markets: The subtle nature of 'random' price changes. *Quant. Finance* 4:176–190.
3. Gatheral J (2010) No-dynamic-arbitrage and market impact. *Quant. Finance* 10:749–759.
4. Jusselin P, Rosenbaum M (2020) No-arbitrage implies power-law market impact and rough volatility. *Math. Finance* 30:1309–1336.
5. Markowitz H (1952) Portfolio selection. *J. Finance* 7:77–91.
6. Merton RC (1972) An analytic derivation of the efficient portfolio frontier. *J. Financial and Quant. Anal.* 7:1851–1872.
7. Almgren R, Chriss N (2001) Optimal execution of portfolio transactions. *J. Risk* 3:5–39.
8. Obizhaeva AA, Wang J (2013) Optimal trading strategy and supply/demand dynamics. *J. Fin. Markets* 16:1–32.
9. Gatheral J, Schied A, Slynko A (2012) Transient linear price impact and Fredholm integral equations. *Math. Finance* 22:445–474.
10. Neuman E, Voß M (2022) Optimal signal-adaptive trading with temporary and transient price impact. *SIAM J. Financial Math.* 13:551–575.
11. Cartea Á, Jaimungal S, Penalva J (2015) *Algorithmic and High-Frequency Trading* (Cambridge Univ. Press).
12. Abi Jaber E, Neuman E (2025) Optimal liquidation with signals: The general propagator case. *Math. Finance* (arXiv:2211.00447).
13. Abi Jaber E, Neuman E, Tuschmann S (2024) Optimal portfolio choice with cross-impact propagators. arXiv:2403.10273.
14. Abi Jaber E, De Carvalho N, Pham H (2024) Trading with propagators and constraints: Applications to optimal execution and battery storage. arXiv:2409.12098.
15. Forde M, Sánchez-Betancourt L, Smith B (2022) Optimal trade execution for Gaussian signals with power-law resilience. *Quant. Finance* 22:585–596.
16. Porter D, Stirling DSG (1990) *Integral Equations: A Practical Treatment from Spectral Theory to Applications* (Cambridge Univ. Press).
17. Chakrabarti A, George AJ (1994) A formula for the solution of general Abel integral equation. *Appl. Math. Lett.* 7:87–90.
18. Wiener N, Hopf E (1931) Über eine Klasse singulärer Integralgleichungen. *S.-B. Preuss. Akad. Wiss. Berlin* 696–706.
19. Krein MG (1962) Integral equations on a half-line with kernel depending upon the difference of the arguments. *Amer. Math. Soc. Transl.* (2) 22:163–288.
20. Wiener N (1949) *Extrapolation, Interpolation and Smoothing of Stationary Time Series* (MIT Press).
21. Gohberg IC, Krein MG (1970) *Theory and Applications of Volterra Operators in Hilbert Space* (Amer. Math. Soc.).
22. Arveson W (1975) Interpolation problems in nest algebras. *J. Funct. Anal.* 20:208–233.
23. Samko SG, Kilbas AA, Marichev OI (1993) *Fractional Integrals and Derivatives: Theory and Applications* (Gordon and Breach).
24. Hytönen T, van Neerven J, Veraar M, Weis L (2016) *Analysis in Banach Spaces, Vol. I* (Springer).
25. Söhngen H (1939) Die Lösungen der Integralgleichung und deren Anwendung in der Tragflügeltheorie. *Math. Z.* 45:245–264.
26. Tricomi FG (1951) On the finite Hilbert transformation. *Quart. J. Math.* 2:199–211.
27. Klenke A (2014) *Probability Theory: A Comprehensive Course*, 2nd ed. (Springer).
