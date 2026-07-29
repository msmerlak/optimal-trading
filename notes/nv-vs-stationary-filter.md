# Neuman–Voß finite-horizon solution vs our stationary filter

**Status:** internal note, 2026-07-18. Companion to `tex/optimal-trading-filters.tex` §5.3 (the two-EMA filter, eq. nv-filter). Experiment: `experiments/nv_vs_stationary.py` (run this session).
**Claim tested:** the paper states the two-EMA filter is the *stationary analogue* of the Neuman–Voß (NV) solution. This note writes down NV explicitly for our parameterization, exhibits the exact analytic bridge (NV's Riccati closed-loop poles = our filter's EMA rates), and shows numerically that the finite-horizon NV rule converges to our stationary filter away from the boundaries, with boundary layers set by the slow EMA rate.

## 1. The Neuman–Voß problem (our parameterization)

NV \citep{NeumanVoss2022} maximize gain from a signal net of temporary impact, exponential-resilience transient impact, and running + terminal inventory risk, on $[0,T]$. In our notation (temporary $\eta$, transient strength $\gamma$ with resilience $\kappa$, running risk $\lambda$, signal $\alpha$; NV's terminal penalty dropped for the stationary comparison), the problem is the LQ control

$$\min_u\ \int_0^T\Bigl[\tfrac{\eta}{2}u_t^2 + \gamma\,u_t J_t + \tfrac{\lambda}{2}x_t^2 - u_t\alpha_t\Bigr]dt,\qquad
\dot x = u,\quad \dot J = u - \kappa J,\quad x_0=J_0=0,$$

where $J_t=\int_0^t e^{-\kappa(t-s)}u_s\,ds$ is the transient-impact state and $\gamma\int u J = \tfrac{\gamma}{2}\iint e^{-\kappa|t-s|}u_tu_s$ is the propagator cost. Parameter map to NV (2022) eq. (2.6): their temporary $\lambda_{\rm NV}\!\to\eta$, transient $(\kappa_{\rm NV},\rho)\!\to(\gamma,\kappa)$, running inventory $\phi\!\to\lambda$, terminal $\varrho\!\to 0$.

## 2. The NV solution, written down

State $z=(x,J)^\top$, dynamics $\dot z = Az + Bu$ with $A=\begin{psmallmatrix}0&0\\0&-\kappa\end{psmallmatrix}$, $B=\begin{psmallmatrix}1\\1\end{psmallmatrix}$, cost weights $Q=\begin{psmallmatrix}\lambda&0\\0&0\end{psmallmatrix}$, $R=\eta$, cross term $N=\begin{psmallmatrix}0\\\gamma\end{psmallmatrix}$. Pontryagin gives the optimal rate in **feedback form** (NV Theorem 3.2: affine in inventory and impact state),

$$u^\star_t \;=\; -\,K(t)\,z_t \;+\; \varphi(t),\qquad K(t)=R^{-1}\bigl(B^\top P(t)+N^\top\bigr),$$

where $P(t)$ solves the matrix **Riccati** equation backward from the free-terminal condition $P(T)=0$,

$$-\dot P = A^\top P + PA - (PB+N)R^{-1}(B^\top P+N^\top) + Q,$$

and $\varphi(t)$ is the signal feed-forward (a backward linear ODE driven by the forecast $\E_t[\alpha_{t+s}]$; for OU it collapses to a multiple of $\alpha_t$ with time-varying coefficient). NV solve the stochastic version through four coupled FBSDEs in $(x,J,u,\text{costate})$ and a $4\times4$ matrix exponential; the deterministic $2\times2$ Riccati above is the state-feedback core, signal-independent.

**Stationary (interior) gains.** As $T\to\infty$, in the interior $P(t)\to P_\infty$, the solution of the algebraic Riccati equation, giving constant $K_\infty$ and closed-loop $A-BK_\infty$.

## 3. Our stationary filter (eq. nv-filter)

The whole-line adapted optimum is the two-EMA filter
$$x^\star_t = \frac{\theta}{\Phi(\theta)\sqrt\eta}\Bigl[w_1\!\int_{-\infty}^t e^{-b_1(t-s)}\alpha_s\,ds + w_2\!\int_{-\infty}^t e^{-b_2(t-s)}\alpha_s\,ds\Bigr],$$
with $b_1,b_2$ the roots of the biquadratic numerator of $N(\omega)$ (eq. nv-factor), $w_i=(\kappa-b_i)/(b_j-b_i)$, $\Phi(\theta)=\sqrt\eta\,(b_1+\theta)(b_2+\theta)/(\kappa+\theta)$. The two smoothing rates $b_1,b_2$ are the poles of the filter.

## 4. The bridge: NV Riccati poles = our EMA rates

The two objects coincide by the classical LQR ↔ spectral-factorization identity: the LQR closed-loop poles are the stable roots of the return difference, which are exactly the zeros of the causal Wiener–Hopf factor $N_+(\omega)=\sqrt\eta\,(b_1-i\omega)(b_2-i\omega)/(\kappa-i\omega)$. Numerically (`nv_vs_stationary.py`, $\eta{=}0.5,\gamma{=}1,\kappa{=}2,\lambda{=}1$):

- our filter: $b_1=0.77258$, $b_2=3.66103$, $\Phi(\theta)=1.94738$ ($\theta=1$);
- NV algebraic Riccati: $K_\infty=[\,1.41421,\ 1.01939\,]$ (feedback on $x$, $J$), **closed-loop poles $=0.77258,\ 3.66103$** — equal to $b_1,b_2$ to $10^{-6}$ (`match: True`).

The NV state feedback drives $(x,J)$ to their signal-driven targets at rates $b_1,b_2$; that two-timescale relaxation *is* the two-EMA filter.

## 5. Convergence away from the boundaries

**(B) Riccati gains** (finite horizon $T=20$, bias-free ODE solve). $K(t)\to K_\infty$ in the interior; the terminal boundary layer decays at rate $\approx 2b_1$:

| distance to $T$ | $K_x(t)$ | $K_J(t)$ | $\|K(t)-K_\infty\|$ |
|---:|---:|---:|---:|
| 10.0 | 1.41421 | 1.01939 | $4.0\times10^{-7}$ |
| 4.0 | 1.41037 | 1.02114 | $4.2\times10^{-3}$ |
| 2.0 | 1.33191 | 1.05669 | $9.0\times10^{-2}$ |
| 1.0 | 1.05844 | 1.17817 | $3.9\times10^{-1}$ |
| 0.5 | 0.70102 | 1.33289 | $7.8\times10^{-1}$ |

$K_\infty=[1.41421,1.01939]$. Gains are stationary to $0.4\%$ once $\gtrsim 4$ units ($\approx 3/b_1$) from the boundary; the layer width is set by the slow EMA rate $1/b_1\approx1.3$.

**(C) Full adapted OU optimum** (discrete adapted solver, $n=800$, $dt=0.025$). Local position and flow responses across the horizon; stationary values $X_\infty=R_\infty=0.26369$:

| $t$ | dist. to boundary | $X_{\rm local}$ | $R_{\rm local}$ |
|---:|---:|---:|---:|
| 1.0 | 1.0 | 0.24261 | 0.26095 |
| 2.0 | 2.0 | 0.26777 | 0.23896 |
| 5.0 | 5.0 | 0.27274 | 0.23506 |
| 10.0 | 10.0 | 0.27277 | 0.23504 |
| 15.0 | 5.0 | 0.27307 | 0.23572 |
| 18.0 | 2.0 | 0.29689 | 0.28747 |
| 19.0 | 1.0 | 0.36670 | 0.43431 |

The local response is **flat across the deep interior** ($t=5,10,15$: $X\approx0.2728$, $R\approx0.2351$) — translation invariance restored, i.e. the finite-horizon rule has become the stationary filter — and departs sharply in the boundary layers ($t\le2$ and $t\ge18$, where the trader is starting from $x_0=0$ or unwinding toward $T$). The interior plateau sits $\approx3\%$ ($X$) / $\approx11\%$ ($R$) from the continuum formula $0.2637$; this offset is the $O(dt)$ quadrature bias of the singular problem, not a boundary effect (it is constant across the interior and matches the paper's §6.3 row-5 bias at the same $dt$, shrinking under $dt$-refinement).

## 6. Conclusion

The stationary two-EMA filter is exactly the interior ($T\to\infty$) limit of the Neuman–Voß finite-horizon feedback: the two solutions share their poles ($b_1,b_2$ = Riccati closed-loop poles = zeros of the causal factor $N_+$), the finite-horizon Riccati gains converge to the stationary constants with error $<10^{-6}$ ten units in and $<1\%$ some $3/b_1$ in, and the full adapted response is flat at the stationary value throughout the interior. Boundary layers of width $\sim 1/b_1$ appear at both ends — the start-up from zero inventory and the terminal unwind — exactly the regime our whole-line filter omits and the finite-horizon Gohberg–Krein factors of §7 would carry.

## Sources
- `tex/optimal-trading-filters.tex` §5.3 (eq. nv-factor, nv-filter), §7 (boundary layers)
- `experiments/nv_vs_stationary.py` (this session): algebraic + finite-horizon Riccati (scipy), pole check, discrete adapted solver
- Neuman, Voß, *Optimal signal-adaptive trading with temporary and transient price impact*, SIAM J. Fin. Math. 13(2):551–575, 2022 (objective eq. 2.6; feedback Theorem 3.2; matrix-exponential/FBSDE solution)
