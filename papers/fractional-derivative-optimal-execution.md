# Optimal Execution as a Fractional Derivative of the Alpha Signal: Bulk and Boundary

**Status:** Skeleton draft (v2). Proofs sketched in body, full arguments in appendices with `⚠️ + TODO` markers where load-bearing technical lemmas remain deferred. No numerical experiments have been run; placeholders are marked `TODO`.

**Version:** v2 (bulk/boundary spine).

**Date:** 2026-06-27

**Authors:** TBD

---

## Abstract

Under the Bouchaud-Gatheral propagator model with power-law decay kernel $G(t) = c\,t^{-\gamma}$, $\gamma \in (0,1)$, the optimal signal-adaptive trading rate decomposes universally as a translation-invariant **bulk term** plus a domain-dependent **boundary correction**:

$$ u^*_t \;=\; u^{\rm bulk}_t \;+\; \mathcal{B}(t). $$

The bulk term is intrinsic: it is the inverse of the propagator symbol $|\xi|^{\gamma-1}$ in Fourier on $\mathbb{R}$, and equals the **symmetric Riesz fractional derivative of order $1-\gamma$** applied to the $\mathcal{F}_t$-conditional forecast curve of the alpha signal,

$$ u^{\rm bulk}_t \;=\; \kappa_{1-\gamma}\, \mathbb{D}^{1-\gamma}\!\bigl(\bar\alpha(t,\cdot) - \lambda\bigr)(t),\qquad \kappa_{1-\gamma} = \frac{1}{2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)}. $$

The boundary correction $\mathcal{B}$ is any solution of the homogeneous bulk equation chosen to match the domain's boundary data. Three specializations exhaust the cases of interest: (i) the whole line, where $\mathcal{B} = 0$; (ii) the bounded interval $[0,T]$ with initial inventory $X_0$ and terminal constraint $X_T = 0$, where $\mathcal{B}$ is a two-parameter family of Söhngen-Tricomi modes $(t(T-t))^{(\gamma-1)/2}$ - and where **the boundary correction is $O((X_0+\|\bar\alpha\|_\infty)/T)$ on bulk regions** while the bulk term is $\Theta(1)$, so the fractional-derivative rule is the asymptotic optimum as $T\to\infty$ (Proposition 5.3, Corollary 5.4); (iii) the half-line $[0,\infty)$ with constant temporary impact $\eta\ge 0$, where the boundary correction is selected by **Wiener-Hopf factorization** of the symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ and a crossover scale $\xi_*(\eta)$ separates a long-memory fractional regime from a myopic signal-following regime, with the pure bulk solution recovered as $\eta \to 0$. The unified bulk/boundary framework places the explicit Söhngen solution of Gatheral-Schied-Slynko (2012), the Riemann-Liouville solution of Forde-Sánchez-Betancourt-Smith (2022), and the operator-resolvent calculus of Abi Jaber-Neuman (2022) and Abi Jaber-Neuman-Tuschmann (2024, arXiv:2403.10273) on a single axis on which only the boundary data change. We extend the bulk theorem to multi-asset cross-impact via a matrix-valued fractional derivative that diagonalizes in the eigenbasis of the cross-impact matrix (Theorem 7.1). The construction is the execution-theoretic instance of Oustaloup's fractional-PID / CRONE control: optimal control with power-law memory is fractional control on the signal.

---

## 1. Introduction

### 1.1 The bulk/boundary picture

Propagator models with power-law decay kernel $G(t) \sim t^{-\gamma}$, $\gamma\in(0,1)$, dominate empirical work on market impact in equities (Bouchaud-Gefen-Potters-Wyart 2004; Gatheral 2010; Jusselin-Rosenbaum 2020 show power-law impact is the unique kernel compatible with no-arbitrage and rough volatility). The first-order condition of the corresponding signal-adaptive execution problem is, in all standard formulations, a linear integral equation in the trading rate against the propagator kernel. The Fourier symbol of the kernel is $|\xi|^{\gamma-1}$ on $\mathbb{R}$, up to a constant. **Inverting this symbol is the bulk problem; it produces a fractional derivative of order $1-\gamma$.** Everything else in the optimal-execution problem - terminal-inventory constraints, initial inventory, finite or infinite horizon, presence or absence of temporary impact - enters through *boundary corrections* that select among the homogeneous solutions of the bulk equation.

This split is the organizing insight of the paper. It is universal:

| Domain | Boundary data | Form of $\mathcal{B}$ |
|---|---|---|
| $\mathbb{R}$ (stationary) | none | $\mathcal{B}\equiv 0$ |
| $[0,T]$, $X_0$ given, $X_T = 0$ | two endpoints | Söhngen mode $(t(T-t))^{(\gamma-1)/2}$ plus second mode, two parameters |
| $[0,\infty)$, $X_0$ given, decay at $\infty$ | one endpoint plus admissibility | one homogeneous mode picked by W-H factorization |

The bulk operator - the symmetric Riesz fractional derivative $\mathbb{D}^{1-\gamma}$ - is the same in every row. What changes per problem is only $\mathcal{B}$. Wiener-Hopf factorization is *one tool* for computing $\mathcal{B}$ on the half-line; the Söhngen-Tricomi inversion is the analogous tool on $[0,T]$. Neither is a separate theorem; each is a specialization of the bulk inversion to a domain.

### 1.2 Contributions

1. **Bulk theorem (Theorem 4.1).** Stated and proved once on $\mathbb{R}$ by Fourier symbol inversion. The bulk optimal rate is the symmetric Riesz fractional derivative of order $1-\gamma$ of the conditional-forecast curve, with explicit constant $\kappa_{1-\gamma} = (2c\Gamma(1-\gamma)\sin(\pi\gamma/2))^{-1}$. Adaptedness is handled via the forecast curve $\bar\alpha(t,\cdot)$ and discussed once. The structural fact that the power-law-kernel Fredholm inverse decomposes through half-order Riemann-Liouville operators is already implicit in Forde-Sánchez-Betancourt-Smith (2022) Theorem 2.2 (their decomposition $T = B^{-1}I_\nu B$, $r=(1-\gamma)/2$); our contribution here is the clean Riesz-on-$\mathbb{R}$ presentation, free of bounded-interval weight conjugation, and the identification of the forecast curve as the explicit object on which the operator acts.
2. **Bulk-symbol Wiener-Hopf factorization (§4.3).** The bulk Riesz operator factorizes as $\mathbb{D}^{1-\gamma} = D_+^\beta D_-^\beta$ with $\beta=(1-\gamma)/2$, yielding a two-step adapted realization (anticausal half-order derivative on the forecast curve, then causal half-order derivative on the result) that quarantines all non-causality in a forecast-consuming step. The factorization is classical (SKM 1993; Krein 1962); its operator-language form on the bounded interval is Porter-Stirling (1990) / FSS2022. Our contribution is the domain-level distinction between this bulk-symbol factorization on $\mathbb{R}$ and the augmented-symbol factorization $M(\xi)=c_\gamma|\xi|^{\gamma-1}+\eta$ on the half-line (§5.3).
3. **Boundary correction principle (§5.1).** $\mathcal{B}$ is any element of the kernel of the bulk operator chosen to match the domain's boundary data. Two- and one-parameter homogeneous families suffice for the two cases of interest.
4. **Bounded-interval corollary (Corollary 5.2).** Specialization to $[0,T]$ with $X_T = 0$ recovers the closed-form Söhngen-Tricomi policy, including the U-shape of Gatheral-Schied-Slynko (2012) in the $\alpha\equiv 0$ case; the Forde-Sánchez-Betancourt-Smith (2022) Gaussian-Volterra policy is recovered conjecturally.
5. **Boundary $O(1/T)$ in the bulk (Proposition 5.3, Corollary 5.4).** For fixed initial inventory $X_0$ and bounded stationary signal, $|\mathcal{B}_{1-\gamma}(t)| = O((X_0+M)/T)$ uniformly on bulk regions $t\in[\epsilon T,(1-\epsilon)T]$, while the bulk term is $\Theta(1)$. The bound is *not* uniform - $\mathcal{B}$ diverges like $t^{(\gamma-1)/2}$ at the endpoints - but the long-horizon limit selects the pure bulk solution: $u^*_t = u^{\rm bulk}_t + O(1/T)$ in the bulk. This is the quantitative content of the "stationary problem is the heart of the matter" picture.
6. **Half-line corollary via augmented-symbol Wiener-Hopf (Corollary 5.7, §5.3).** With constant temporary impact $\tfrac12\eta u_t^2$, $\eta\ge 0$, the boundary correction is fixed by W-H factorization of the augmented symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ on $[0,\infty)$ (distinct from the bulk-symbol factorization of contribution 2). For $\eta>0$ a crossover frequency $\xi_*(\eta)$ separates a long-memory fractional regime from a myopic signal-following regime; the $\eta\to 0$ limit recovers the pure bulk solution and makes §5.3 the half-line analogue of the bulk theorem.
7. **Mittag-Leffler resolvent on $[0,T]$ with temporary impact (Theorem 6.1).** Combining bounded-interval boundary correction with temporary impact $\eta>0$ gives a kernel built from $E_{1-\gamma,1-\gamma}$ with prefactor $c\,\Gamma(1-\gamma)$.
8. **Multi-asset extension (Theorem 7.1).** Cross-impact matrix diagonalization decouples the vector bulk theorem into scalar bulk problems on principal-component signals.
9. **Execution-CRONE bridge (§8).** Optimal execution under a power-law propagator is the execution-theoretic instance of Oustaloup's fractional-PID / CRONE control: optimal control of a system with power-law memory is fractional control on the (forecasted) error signal. To our knowledge this bridge is drawn here for the first time; the optimal-execution literature does not cite CRONE, and the December 2025 survey of fractional calculus in optimal control and game theory (arXiv:2512.12111) does not cover optimal execution.

The bulk/boundary spine puts AJN (2022), AJNT (2024, arXiv:2403.10273), GP (2013), GSS (2012), Forde et al. (2022), Cartea-Jaimungal (2016), Neuman-Voß (2022), Moreau-Muhle-Karbe-Soner (2017) on a single axis: all are the same bulk solution with different boundary data and different regularizers. The execution-theoretic content of the fractional-PID / CRONE engineering tradition (Oustaloup 1991 ff.; survey arXiv:2512.12111) is the *bulk theorem*, not any single problem-specific result.

### 1.3 Related work and positioning

The literature splits along three lines.

- **Closest prior art: Forde-Sánchez-Betancourt-Smith (2022).** FSS2022 solve the bounded-interval signal-adaptive propagator problem with the *identical* kernel $G(t)=ct^{-\gamma}$ and Gaussian signals. The proof of their Theorem 2.2 explicitly factorizes the Fredholm operator on $L^2[0,1]$ as $T = B^{-1} I_\nu B$, where $B$ is multiplication by $t^{-(1-\gamma)/4}$ and $I_\nu$ is the **Riemann-Liouville operator of order $r = (1-\gamma)/2$** - i.e., the operator-language form of the multiplicative Wiener-Hopf / Porter-Stirling (1990) factorization $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$ that we use in §4.3 (with $\beta = r$). The structural fractional-operator insight is therefore *not new* with the present paper; what is new is (i) the clean Riesz-on-$\mathbb{R}$ presentation that drops the bounded-interval weight conjugation by $B$, (ii) the identification of the forecast curve $\bar\alpha(t,\cdot)$ as the explicit object on which the operator acts (FSS2022 use a Volterra-on-Brownian ansatz $\hat u_t = \bar u(t) + \int_0^t k(v,t)dW_v$ instead), (iii) the bulk/boundary spine that unifies bounded-interval, half-line, and whole-line cases on a single axis, and (iv) the explicit bridge to CRONE / fractional-PID control (§8). The final FSS2022 formulas are presented via the Chakrabarti-George (1994) Abel-inversion as triple integrals with incomplete-Beta and Gamma-ratio prefactors; the present Riesz form is more compact and is $O(N\log N)$ FFT-computable.
- **Other closed-form lines.** Gatheral-Schied-Slynko (2012) solve the Abel equation for $\alpha\equiv 0$ on $[0,T]$ without naming the fractional derivative. Curato-Gatheral-Lillo (2017) extend to nonlinear transient impact. Both are bounded-interval results; under the bulk/boundary spine they are corollaries of Theorem 4.1 with the §5.2 boundary correction.
- **Operator-resolvent lines.** Abi Jaber-Neuman (2022) and Abi Jaber-Neuman-Tuschmann (2024, arXiv:2403.10273) give the encompassing operator-resolvent FOC for matrix Volterra propagators with terminal-inventory constraints and temporary-and-transient impact, on both finite intervals and half-lines; Abi Jaber-Bondi-De Carvalho-Neuman-Tuschmann (2025, arXiv:2503.04323) extend to nonlinear price impact. Their resolvent framework specializes to the explicit closed forms of this paper under (i) scalar power-law kernel, (ii) stationary signal, (iii) translation invariance of the chosen domain; "fractional" appears in those works only as a descriptor of the kernel, not as the operator yielding the solution.
- **Stationary / portfolio-choice lines.** Gârleanu-Pedersen (2013) solve the stationary problem with exponential impact and running inventory-risk penalty; Moreau-Muhle-Karbe-Soner (2017) give the small-impact asymptotic that unifies portfolio choice with execution-style decay toward a frictionless target; Cartea-Jaimungal (2016) and Neuman-Voß (2022) cover signal-adaptive baselines with exponential resilience. Under our spine these are bulk problems with different kernels (exponential rather than power-law) and different regularizers (running inventory cost rather than temporary impact); the bulk inversion is no longer a fractional derivative but the spine - bulk first, boundary second - remains the same.
- **Fractional-control lines.** Oustaloup (1991; Oustaloup et al. 2000) and the CRONE / fractional-PID engineering tradition apply fractional differentiators of order $\alpha\in(0,1)$ in feedback loops for systems with power-law memory; the December 2025 survey arXiv:2512.12111 covers fractional Pontryagin / HJB / LQR / MPC / PID across physical, biological, and engineered systems but does not include optimal execution. Conversely, the optimal-execution literature does not cite CRONE. The bridge in §8 is the first crossing between these two literatures of which we are aware.

The companion literature reviews `outputs/fractional-kernels-optimal-execution.md`, `outputs/unified-trading-execution.md`, and `outputs/bulk-fractional-forecast-novelty.md` provide further detail on each branch.

Our explicit contribution: **the bulk theorem on $\mathbb{R}$ as a standalone result, the bulk/boundary spine as the organizing structure, and the CRONE bridge as a cross-field connection**. The fractional-derivative structural fact is, on its substantive content, a re-presentation of insights present in FSS2022 (operator language) and classical fractional-calculus / Wiener-Hopf theory (SKM 1993; Krein 1962; Noble 1958). The novelty is in the presentation, the unification, and the cross-field bridge - not in a new mathematical theorem about power-law-kernel Fredholm inverses.

---

## 2. Setting

### 2.1 Propagator model with power-law impact

Fix a filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t\in\mathbb{T}}, \mathbb{P})$ where the time domain $\mathbb{T} \in \{\mathbb{R}, [0,T], [0,\infty)\}$ is one of the three cases of interest. An admissible trading rate $u \in \mathcal{U}_\mathbb{T}$ is a real-valued $\mathcal{F}_t$-progressive process with $u\in L^2_{\rm loc}(\mathbb{T})$, plus a domain-specific integrability tail condition that we state per case. The inventory evolves as $dX_t = -u_t\,dt$ from a given $X_0$, with sign convention $u > 0$ ≡ selling.

The execution price is

$$ S_t \;=\; P_t \;-\; \int G(t-s)\,u_s\,ds, $$

where $P_t$ is an exogenous unaffected price, the integral is taken over $\{s\in\mathbb{T}: s\le t\}$ (causal), and the decay kernel is

$$ G(t) \;=\; c\,t^{-\gamma}, \qquad \gamma\in(0,1),\ c>0,\ t>0. $$

The kernel exponent $\gamma$ is the *propagator exponent* throughout (decision D1 = B in the companion v1-to-v2 migration note); the inverting fractional derivative carries the complementary order $1-\gamma$.

### 2.2 Signal and forecast curve

The trader observes a signal $\alpha_t$ that is $\mathcal{F}_t$-progressive and locally square-integrable. We give two equivalent semantic interpretations of $\alpha$, picked per domain:

- **Bounded-interval interpretation $\mathbb{T}=[0,T]$.** $\alpha_t = \mathbb{E}_t[P_T - P_t]$, the cumulative expected price change to the terminal horizon. This forces $\alpha_T \equiv 0$, which is consistent with the boundary condition $\bar\alpha(t,T)\to 0$ as $t\to T$ used in the bounded-interval boundary correction (§5.2). The identically-zero term $\mathbb{E}_t[\alpha_T]$ that appeared in v1 drafts is therefore omitted throughout (decision D3 = A).
- **Stationary / half-line interpretation $\mathbb{T}\in\{\mathbb{R},[0,\infty)\}$.** $\alpha_t$ is the instantaneous level of a stationary forecastable price-innovation process (e.g. an OU drift). The cumulative-to-terminal definition no longer applies and the average-cost-per-unit-time objective replaces the cumulative objective.

Both interpretations have the same dimensions \$/share. The dual semantics is one of the artefacts that motivates the bulk/boundary split: the *bulk* operator does not care which semantics is in force, because it is translation-invariant; only the *boundary correction* distinguishes the two.

**Forecast curve.** Define the $\mathcal{F}_t$-conditional forecast curve

$$ \bar\alpha(t,s) \;:=\; \begin{cases} \alpha_s, & s\le t, \\ \mathbb{E}_t[\alpha_s], & s > t,\end{cases} $$

so that for each fixed $t$ the map $s\mapsto\bar\alpha(t,s)$ is $\mathcal{F}_t$-measurable on the entire domain $\mathbb{T}$. The forecast curve is what the bulk operator acts on; using it (rather than the realized path $\alpha_\cdot$) keeps the policy $u^*_t$ $\mathcal{F}_t$-adapted even though the bulk operator is non-causal. Economically, $\bar\alpha(t,s)$ is the trader's time-$t$ best forecast of the signal's value at time $s$; it summarizes all that is knowable about the future signal path from current information. We discuss adaptedness in detail once, in §4 immediately after the bulk theorem.

### 2.3 Cost functional

The cost functional in the bounded-interval case is

$$ \mathcal{C}_T(u) \;=\; \mathbb{E}\!\left[\int_0^T u_t\,(P_t - S_t)\,dt\right] \;-\; \mathbb{E}\!\left[\int_0^T u_t\,\alpha_t\,dt\right], $$

minimized over admissible $u$ with $X_T = 0$ via a Lagrange multiplier $\lambda$. Substituting the propagator expression for $S_t$ and symmetrizing the kernel via $G_{\rm sym}(t) = \tfrac12(G(t)+G(-t))$ on $[-T,T]$ gives, up to boundary corrections,

$$ \mathcal{C}_T(u) \;=\; \tfrac12\mathbb{E}\!\int_0^T\!\!\int_0^T G(|t-v|)\,u_t\,u_v\,dt\,dv \;-\; \mathbb{E}\!\int_0^T u_t\,\alpha_t\,dt \;+\; \lambda\!\left(\int_0^T u_t\,dt - X_0\right). $$

The Euler-Lagrange variation in $\delta u$ yields the *Fredholm equation of the first kind*

$$ \int_0^T G(|t-v|)\,u^*_v\,dv \;=\; \alpha_t \;-\; \lambda, \qquad t\in(0,T). \tag{$\star$} $$

In the half-line case with temporary impact $\tfrac12\eta u_t^2$ and without a terminal constraint, the analogous first-order condition on the average-cost-per-unit-time objective is the *Wiener-Hopf equation of the second kind*

$$ \eta\,u^*_t \;+\; \int_0^\infty G(|t-v|)\,u^*_v\,dv \;=\; \alpha_t, \qquad t\ge 0. \tag{$\star_{\rm WH}$} $$

In the whole-line / stationary case, the FOC is the *translation-invariant convolution equation*

$$ \int_{\mathbb{R}} G(|t-v|)\,u^*_v\,dv \;=\; \alpha_t \;-\; \lambda, \qquad t\in\mathbb{R}, \tag{$\star_{\rm bulk}$} $$

with $\lambda$ interpreted as a constant DC offset (zero for zero-mean stationary $\alpha$, in which case it can be omitted).

**Stochastic FOC.** Equations $(\star)$, $(\star_{\rm WH})$, $(\star_{\rm bulk})$ as written are pathwise FOCs valid for deterministic $\alpha$. For an adapted stochastic signal and adapted admissible $u$, an $\mathcal{F}_t$-measurable variation $\delta u_t$ cannot probe $u^*_v$ for $v>t$ pathwise; the Gâteaux derivative of $\mathcal{C}$ tested against adapted variations satisfies, by Fubini and adaptedness of $\delta u_t$,

$$ 0 \;=\; \delta\mathcal{C} \;=\; \mathbb{E}\!\int\!\Bigl(\!\!\int\! G(|t-v|)\,u^*_v\,dv - \alpha_t\Bigr)\delta u_t\,dt \;=\; \mathbb{E}\!\int\!\mathbb{E}_t\!\Bigl[\!\!\int\! G(|t-v|)\,u^*_v\,dv - \alpha_t\Bigr]\delta u_t\,dt, $$

which forces the $\mathcal{F}_t$-conditioned FOCs

$$ \int_0^T G(|t-v|)\,\mathbb{E}_t[u^*_v]\,dv \;=\; \alpha_t - \lambda_t, \qquad t\in(0,T), \tag{$\star^{\mathcal{F}}$} $$

$$ \eta\,u^*_t \;+\; \int_0^\infty G(|t-v|)\,\mathbb{E}_t[u^*_v]\,dv \;=\; \alpha_t, \qquad t\ge 0, \tag{$\star_{\rm WH}^{\mathcal{F}}$} $$

$$ \int_{\mathbb{R}} G(|t-v|)\,\mathbb{E}_t[u^*_v]\,dv \;=\; \alpha_t - \lambda, \qquad t\in\mathbb{R}. \tag{$\star_{\rm bulk}^{\mathcal{F}}$} $$

On the bounded interval the multiplier $\lambda_t$ enforcing $\int_0^T u_t\,dt = X_0$ is in general $\mathcal{F}_T$-measurable; projecting onto $\mathcal{F}_t$ replaces it by the martingale $\mathbb{E}_t[\lambda_T]$, which we continue to denote $\lambda$ when stationarity makes it constant. The diagonal $\eta u^*_t$ term in $(\star_{\rm WH}^{\mathcal{F}})$ is already $\mathcal{F}_t$-measurable.

**Forecast tower lemma.** *For all $t\le v$ and $s\in\mathbb{R}$, $\;\mathbb{E}_t[\bar\alpha(v,s)] = \bar\alpha(t,s).$*

*Proof.* Split on $s$. If $s\le t$, then $s\le v$ as well, so $\bar\alpha(v,s)=\alpha_s$ is $\mathcal{F}_s\subset\mathcal{F}_t$-measurable and $\mathbb{E}_t[\alpha_s] = \alpha_s = \bar\alpha(t,s)$. If $t<s\le v$, then $\bar\alpha(v,s)=\alpha_s$ and $\mathbb{E}_t[\alpha_s]=\bar\alpha(t,s)$ by definition (§2.2). If $s>v$, then $\bar\alpha(v,s)=\mathbb{E}_v[\alpha_s]$ and $\mathbb{E}_t[\mathbb{E}_v[\alpha_s]]=\mathbb{E}_t[\alpha_s]=\bar\alpha(t,s)$ by the tower property of conditional expectation. $\square$

**Candidate policy and emergence of the forecast curve.** The deterministic bulk FOC $(\star_{\rm bulk})$ inverts on $\mathbb{R}$ to $u^{\rm det}_t = c_\gamma^{-1}\mathbb{D}^{1-\gamma}(\alpha-\lambda)(t)$, where $c_\gamma = 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$ arises from $\hat G(\xi)=c_\gamma|\xi|^{\gamma-1}$ (§3.1, §4.1). Replacing the realized path by the forecast curve yields the $\mathcal{F}_v$-adapted candidate

$$ u^{\rm cand}_v \;:=\; c_\gamma^{-1}\,\mathbb{D}^{1-\gamma}\bigl(\bar\alpha(v,\cdot)-\lambda\bigr)(v). \tag{$\sharp$} $$

Adaptedness holds because, for each fixed $v$, the map $s\mapsto\bar\alpha(v,s)$ is $\mathcal{F}_v$-measurable on all of $\mathbb{R}$ (§2.2), and $\mathbb{D}^{1-\gamma}$ acts in the $s$-variable as a deterministic operator. By linearity of $\mathbb{D}^{1-\gamma}$ and Fubini (justified under the spectral integrability hypothesis stated in Theorem 4.1), conditional expectation commutes through the operator; combined with the forecast tower lemma this gives, for $t\le v$,

$$ \mathbb{E}_t[u^{\rm cand}_v] \;=\; c_\gamma^{-1}\,\mathbb{D}^{1-\gamma}\bigl(\mathbb{E}_t\bar\alpha(v,\cdot)-\lambda\bigr)(v) \;=\; c_\gamma^{-1}\,\mathbb{D}^{1-\gamma}\bigl(\bar\alpha(t,\cdot)-\lambda\bigr)(v). $$

Substituting into the LHS of $(\star_{\rm bulk}^{\mathcal{F}})$ and using $\hat G(\xi)\cdot|\xi|^{1-\gamma}=c_\gamma$ at the convolution level,

$$ \int_{\mathbb{R}}\! G(|t-v|)\,\mathbb{E}_t[u^{\rm cand}_v]\,dv \;=\; c_\gamma^{-1}\bigl(G\ast\mathbb{D}^{1-\gamma}(\bar\alpha(t,\cdot)-\lambda)\bigr)(t) \;=\; \bar\alpha(t,t)-\lambda \;=\; \alpha_t-\lambda, $$

so the candidate satisfies the conditioned FOC pointwise in $t$. The quadratic form $u\mapsto\tfrac12\mathbb{E}\!\int\!\int G(|t-v|)u_t u_v\,dt\,dv$ is positive ($\hat G(\xi)=c_\gamma|\xi|^{\gamma-1}\ge 0$) and the cost $\mathcal{C}$ is strictly convex in $u$ on the adapted Hilbert space $L^2_{\rm adap}\subset L^2(\Omega\times\mathbb{T})$. The conditioned FOC is therefore both necessary and sufficient for an adapted minimizer, and the candidate $u^{\rm cand}$ is the unique element of $L^2_{\rm adap}$ satisfying it — i.e. the unique optimum. This is the standard linear–quadratic certainty-equivalence pattern (Bensoussan 1992; Kwakernaak–Sivan 1972) applied with a non-local Riesz kernel; an alternative BSDE-based derivation for related Volterra propagators is in Abi Jaber–Neuman (2022) cited in §6.4.

The forecast curve thus *emerges* from the combination of (i) the conditioned FOC, (ii) the forecast tower lemma, and (iii) linearity of $\mathbb{D}^{1-\gamma}$ — not from a direct "substitution" into the cost functional. The bounded-interval and half-line specializations of §5 follow by the same template with $(\star^{\mathcal{F}})$ and $(\star_{\rm WH}^{\mathcal{F}})$ replacing $(\star_{\rm bulk}^{\mathcal{F}})$ and the domain of integration restricted; the boundary corrections of §5 act on the kernel of the bulk operator and are derived separately. Adaptedness of the resulting policy is recapped once, in §4.2.

### 2.4 The bulk problem

**Definition 2.1 (Bulk problem).** The *bulk problem* is the translation-invariant convolution equation $(\star_{\rm bulk})$ on $\mathbb{R}$ with stationary $\alpha$. Its solution $u^{\rm bulk}_t$ is intrinsic to the kernel $G$ and the forecast $\bar\alpha(t,\cdot)$: it does not depend on any boundary data.

The bounded-interval FOC $(\star)$ and the half-line FOC $(\star_{\rm WH})$ are both **inhomogeneous restrictions of the bulk problem to a domain with boundary data**. Their solutions decompose as

$$ u^*_t \;=\; u^{\rm bulk}_t \;+\; \mathcal{B}(t), $$

where $u^{\rm bulk}$ is determined by inverting the bulk symbol (§4) and $\mathcal{B}$ lives in the kernel of the bulk operator and is fixed by the domain's boundary data (§5).

### 2.5 Standing economic assumptions

Throughout the paper: single risky asset; no short-sale or inventory-band constraint beyond $X_T = 0$ where applicable; no funding cost on cash; risk-neutral cost functional. The multi-asset extension is taken up in §7. The half-line specialization in §5.3 adds a constant temporary-impact term $\tfrac12\eta u_t^2$, $\eta\ge 0$, with economic interpretation as spread/slippage cost (per Obizhaeva-Wang 2013, AJN 2022, AJNT 2024). We do *not* impose a Gârleanu-Pedersen running inventory-risk penalty $\tfrac12\gamma_{\rm risk}\sigma^2 X_t^2$ anywhere; the GP regime introduces a structurally different symbol shift (by $\gamma_{\rm risk}\sigma^2/\xi^2$) and is left to future work (§6.5).

---

## 3. Fractional-calculus preliminaries

### 3.1 Riemann-Liouville and Marchaud operators

For $\nu\in(0,1)$ and $f$ locally integrable on a domain $\mathbb{T}\supseteq[a,b]$, the *left* Riemann-Liouville fractional integral and derivative on $[a,b]$ are

$$ (I^\nu_+ f)(t) \;:=\; \frac{1}{\Gamma(\nu)}\int_a^t (t-s)^{\nu-1}f(s)\,ds, \qquad (D^\nu_+ f)(t) \;:=\; \frac{1}{\Gamma(1-\nu)}\frac{d}{dt}\!\int_a^t (t-s)^{-\nu}f(s)\,ds, $$

with right-sided analogues $I^\nu_-, D^\nu_-$ obtained by reflecting the limits of integration. The Marchaud representation extends the derivative to functions of low regularity by a finite-difference formula; we invoke it when boundary regularity is delicate. Standard references: Podlubny (1999); Samko-Kilbas-Marichev (1993).

### 3.2 Symmetric Riesz fractional derivative

The bulk operator of this paper is the **symmetric Riesz fractional derivative of order $1-\gamma$**, denoted $\mathbb{D}^{1-\gamma}$. On the whole line $\mathbb{R}$ it is defined by its Fourier symbol:

$$ \widehat{\mathbb{D}^{1-\gamma} f}(\xi) \;=\; |\xi|^{1-\gamma}\,\hat f(\xi), \qquad \xi\in\mathbb{R}. $$

Equivalently, $\mathbb{D}^{1-\gamma} = \tfrac{1}{2\sin(\pi\gamma/2)}(D^{1-\gamma}_+ + D^{1-\gamma}_-)$ as operators on Schwartz functions on $\mathbb{R}$ (using $\cos(\pi(1-\gamma)/2) = \sin(\pi\gamma/2)$); the half-sum form is useful for explicit calculations on the line and we use it interchangeably with the symbol form below.

On the bounded interval $[0,T]$ we adopt the **Söhngen-Tricomi weighted finite-Hilbert form** (Söhngen 1939; Tricomi 1957 §4.3; Samko-Kilbas-Marichev 1993 §13.2 Theorem 13.2; we cite this as **SKM 1993 §13.2 Thm 13.2** throughout):

$$ \bigl(\mathbb{D}^{1-\gamma}_{[0,T]} f\bigr)(s) \;=\; \frac{\sin(\pi\nu)}{\pi^2}\,(s(T-s))^{-\nu}\,\frac{d}{ds}\!\int_0^T \frac{(v(T-v))^\nu}{v-s}\,f(v)\,dv, \quad \nu = \tfrac{1-\gamma}{2}, $$

with the integral interpreted as a Cauchy principal value. The operator $\mathbb{D}^{1-\gamma}_{[0,T]}$ is the (unique up to a null space spanned by $(s(T-s))^{(\gamma-1)/2}$ and a second mode) inverse of the symmetric power-law convolution $\int_0^T |t-v|^{-\gamma}(\cdot)\,dv$ on $[0,T]$, in the sense that the composition equals the constant $c_\gamma := 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$ times the identity modulo the boundary null space. The constant $c_\gamma$ is the Fourier symbol prefactor: $\widehat{c|t|^{-\gamma}}(\xi) = c_\gamma|\xi|^{\gamma-1}$ on $\mathbb{R}$ (Stein 1970 §V.1; SKM 1993 §7.1).

### 3.3 The constant $\kappa_{1-\gamma}$

The inversion-of-kernel-symbol constant that appears in the bulk theorem is

$$ \boxed{\;\kappa_{1-\gamma} \;:=\; \frac{1}{c_\gamma} \;=\; \frac{1}{2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)}.\;} $$

This constant is the same on $\mathbb{R}$, on $[0,T]$, and on $[0,\infty)$: it depends only on the kernel exponent $\gamma$ and the scale $c$, not on the domain. The v1 form $\kappa = (c\Gamma(1-\gamma))^{-1}$ was a normalization error (decision D5 = A in the migration note); the corrected form above aligns the bulk-on-$\mathbb{R}$, bounded-interval, and half-line normalizations to a single constant.

### 3.4 Sonine pairs

A *Sonine pair* on an interval $I$ is a pair of kernels $(K,L)$ on $I$ with $K*L = \mathbf{1}_I$ (the constant function), equivalently acting as mutual inverses up to a constant under convolution. On the half-line, the Sonine pair relevant to our paper is

$$ K(t) = c\,t^{-\gamma}, \qquad L(t) = \text{(complementary kernel, see Samko-Kilbas-Marichev §10.4)}, $$

which underlies the Riemann-Liouville inversion of the half-line propagator. The bounded-interval version requires the finite-Hilbert correction of §3.2 and is the basis for Corollary 5.2.

### 3.5 Mittag-Leffler functions

The two-parameter Mittag-Leffler function

$$ E_{\alpha,\beta}(z) \;:=\; \sum_{k=0}^\infty \frac{z^k}{\Gamma(\alpha k + \beta)} $$

appears as the resolvent kernel when temporary impact $\eta > 0$ is combined with the bounded-interval setup (§6.1, Theorem 6.1): $R_{\gamma,\eta}$ involves $E_{1-\gamma,\,1-\gamma}$ with indices dictated by the kernel exponent.

---

## 4. The bulk solution

### 4.1 Statement

**Theorem 4.1 (Bulk theorem).** *Let $G(t) = c\,t^{-\gamma}$ with $\gamma\in(0,1)$, $c > 0$. Let $\alpha$ be a stationary mean-zero $\mathcal{F}_t$-progressive process with finite power spectral density $S_\alpha(\xi)$ satisfying $\int (1+|\xi|^{2(1-\gamma)}) S_\alpha(\xi)\,d\xi < \infty$. Let $\lambda\in\mathbb{R}$ be a constant DC offset (zero for zero-mean $\alpha$). Then the unique stationary $L^2(\mathbb{R})$ solution $u^{\rm bulk}$ of the bulk first-order condition $(\star_{\rm bulk})$ is*

$$ \boxed{\; u^{\rm bulk}_t \;=\; \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\!\bigl(\bar\alpha(t,\cdot) - \lambda\bigr)(t),\qquad \kappa_{1-\gamma} = \frac{1}{2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)}.\;} $$

*The right-hand side is $\mathcal{F}_t$-measurable through the forecast curve $\bar\alpha(t,\cdot)$ of §2.2, so the policy is admissible.*

**Remark 4.1.1 (attribution).** The structural content of Theorem 4.1 - that the optimal control for a propagator $G\propto t^{-\gamma}$ is given by a fractional operator of order $1-\gamma$ - is, in operator language and on the bounded interval, in Forde-Sánchez-Betancourt-Smith (2022) Theorem 2.2 proof: they factorize the Fredholm operator $T = B^{-1}I_\nu B$ with $I_\nu$ the Riemann-Liouville operator of order $r=(1-\gamma)/2$ and write $I_\nu^{-1} = \Gamma(1-r)D^r$. Combining the two half-order $D^r$ factors (anticausal $\times$ causal) gives a full Riesz operator of order $1-\gamma$ conjugated by the weight $B$ (multiplication by $t^{-(1-\gamma)/4}$); the present theorem drops the weight conjugation by working on the translation-invariant whole line and re-expresses the result in standard fractional-calculus textbook idiom (Riesz of order $1-\gamma$ acting on the forecast curve), with all problem-specific structure pushed into boundary corrections (§5). The bulk-symbol Wiener-Hopf factorization $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$ (§4.3) is classical (SKM 1993; Krein 1962; Noble 1958); its bounded-interval operator form is Porter-Stirling (1990) / FSS2022. See `outputs/bulk-fractional-forecast-novelty.md` for a complete novelty audit.

**Proof.** Fix $t\in\mathbb{R}$ and consider the $\mathcal{F}_v$-adapted candidate $u^{\rm cand}_v := c_\gamma^{-1}\mathbb{D}^{1-\gamma}(\bar\alpha(v,\cdot)-\lambda)(v)$ of §2.3, equation $(\sharp)$, with $c_\gamma := 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$ so that $\kappa_{1-\gamma}=c_\gamma^{-1}$. The symmetric kernel $G(|s|)=c|s|^{-\gamma}$ has Fourier symbol $\hat G(\xi)=c_\gamma|\xi|^{\gamma-1}$ (Stein 1970 §V.1; SKM 1993 §7.1), and by Plancherel applied to the convolution in the $s$-variable of the (deterministic, $\mathcal{F}_t$-measurable) function $\bar\alpha(t,\cdot)-\lambda$,

$$ \bigl(G\ast\mathbb{D}^{1-\gamma}(\bar\alpha(t,\cdot)-\lambda)\bigr)(s) \;=\; \mathcal{F}^{-1}\!\bigl[c_\gamma|\xi|^{\gamma-1}\cdot|\xi|^{1-\gamma}\,\widehat{(\bar\alpha(t,\cdot)-\lambda)}(\xi)\bigr](s) \;=\; c_\gamma\,(\bar\alpha(t,s)-\lambda). $$

Evaluating at $s=t$ and using $\bar\alpha(t,t)=\alpha_t$ together with the forecast tower lemma of §2.3 (which gives $\mathbb{E}_t[u^{\rm cand}_v] = c_\gamma^{-1}\mathbb{D}^{1-\gamma}(\bar\alpha(t,\cdot)-\lambda)(v)$ for $t\le v$),

$$ \int_{\mathbb{R}} G(|t-v|)\,\mathbb{E}_t[u^{\rm cand}_v]\,dv \;=\; c_\gamma^{-1}\bigl(G\ast\mathbb{D}^{1-\gamma}(\bar\alpha(t,\cdot)-\lambda)\bigr)(t) \;=\; \alpha_t - \lambda. $$

Hence $u^{\rm cand}$ satisfies the conditioned bulk FOC $(\star_{\rm bulk}^{\mathcal{F}})$. The constant offset $\lambda$ contributes only to the $\xi=0$ mode (suppressed under the zero-mean assumption on $\alpha$). Strict convexity of $\mathcal{C}$ on the adapted subspace $L^2_{\rm adap}\subset L^2(\Omega\times\mathbb{R})$ — the kernel symbol $\hat G(\xi)=c_\gamma|\xi|^{\gamma-1}$ is non-negative — implies that the conditioned FOC has a unique adapted solution, so $u^{\rm bulk}_t = u^{\rm cand}_t = c_\gamma^{-1}\mathbb{D}^{1-\gamma}(\bar\alpha(t,\cdot)-\lambda)(t)$. The integrability assumption $\int(1+|\xi|^{2(1-\gamma)})S_\alpha(\xi)\,d\xi<\infty$ ensures $|\xi|^{1-\gamma}\widehat{\bar\alpha}\in L^2$ pathwise, so $u^{\rm bulk}\in L^2_{\rm adap}$ by Plancherel. Adaptedness through $\bar\alpha(t,\cdot)$ is by construction of the forecast curve (§2.2). $\blacksquare$

### 4.2 Adaptedness and the forecast curve

As derived in §2.3 via the forecast tower lemma and the candidate $(\sharp)$, the operative FOC for adapted controls is the $\mathcal{F}_t$-conditioned form $(\star_{\rm bulk}^{\mathcal{F}})$, whose unique adapted solution is the symbol-inverted candidate written in $\bar\alpha(t,\cdot)$ rather than the realized $\alpha$. This subsection records two remaining facts about why this is admissible and what it looks like in implementation.

*Why the forecast curve is the right object.* The Riesz operator $\mathbb{D}^{1-\gamma}$ is *non-causal*: its half-sum form $\tfrac{1}{2\sin(\pi\gamma/2)}(D^{1-\gamma}_+ + D^{1-\gamma}_-)$ includes the right-sided derivative $D^{1-\gamma}_-$, which depends on the underlying function on the future $\{s > t\}$. Applied to the realized path $\alpha_\cdot$, this would not be $\mathcal{F}_t$-measurable. Applied to $\bar\alpha(t,\cdot)$, it is: for each fixed $t$, the map $s\mapsto\bar\alpha(t,s)$ is $\mathcal{F}_t$-measurable on the whole real line because it is the conditional-expectation projection of the realized path. Applying a deterministic (non-causal) integral operator in the $s$-variable to an $\mathcal{F}_t$-measurable curve produces an $\mathcal{F}_t$-measurable value at $t$.

*Implementation.* Only a model of the conditional law of $\alpha$ - e.g. an OU drift, a Volterra-Gaussian process, or any forecastable $\mathcal{F}_t$-Markov structure - is needed. For an OU signal $d\alpha_t = -\theta\alpha_t\,dt + \sigma\,dW_t$, the forecast curve is simply $\bar\alpha(t,s) = e^{-\theta(s-t)}\alpha_t$ for $s > t$; the Riesz derivative reduces to an integral against exponential decay times the realized signal $\alpha_t$.

This adaptedness discussion *will not be repeated in §5*: the boundary corrections inherit the same forecast-curve construction via $(\star^{\mathcal{F}})$ and $(\star_{\rm WH}^{\mathcal{F}})$.

### 4.3 Wiener-Hopf factorization and the causal realization

The Riesz operator $\mathbb{D}^{1-\gamma}$ is non-causal in $s$, but its action on the forecast curve $\bar\alpha(t,\cdot)$ is $\mathcal{F}_t$-measurable (§4.2). This subsection shows that the bulk symbol admits a **Wiener-Hopf factorization** that exposes the optimal policy as a two-step adapted pipeline: an anticausal half-order derivative applied to forecasts, followed by a causal half-order derivative applied to the result. This is the optimal-execution analog of Wiener's spectral-factorization causal realization (Wiener 1949; Wiener-Hopf 1931; Noble 1958 §2.4).

Set $\beta := (1-\gamma)/2 \in (0,1/2)$. The bulk symbol factorizes on $\mathbb{R}\setminus\{0\}$ as

$$ |\xi|^{1-\gamma} \;=\; (i\xi)^{\beta}\,(-i\xi)^{\beta}, \qquad (i\xi)^{\beta} := |\xi|^{\beta} e^{i\beta\pi\,\mathrm{sgn}(\xi)/2}, \tag{4.3.1} $$

with principal branches (SKM 1993 §7.1). The factors $(i\xi)^\beta$ and $(-i\xi)^\beta$ extend analytically and non-vanishingly to the upper and lower complex half-planes respectively - the defining property of a Wiener-Hopf factorization - and are the Fourier symbols of the causal and anticausal Marchaud derivatives $D_+^\beta$, $D_-^\beta$ (SKM 1993 §5.4, §7.1):

$$ \widehat{D_+^\beta f}(\xi) \;=\; (i\xi)^\beta\,\hat f(\xi), \qquad \widehat{D_-^\beta f}(\xi) \;=\; (-i\xi)^\beta\,\hat f(\xi). $$

Operator-side, (4.3.1) gives

$$ \mathbb{D}^{1-\gamma} \;=\; D_+^{(1-\gamma)/2}\,D_-^{(1-\gamma)/2}, \tag{4.3.2} $$

with **no extra constant** (the half-plane phases cancel exactly) and the factors commuting on Schwartz functions. The bulk policy of Theorem 4.1 therefore admits the factored form

$$ \boxed{\; u^{\rm bulk}_t \;=\; \kappa_{1-\gamma}\,D_+^{(1-\gamma)/2}\!\Bigl[D_-^{(1-\gamma)/2}\,\bar\alpha(t,\cdot)\Bigr](t).\;} \tag{4.3.3} $$

**Two-step causal realization.** Read (4.3.3) as a two-step adapted computation:

1. *Anticausal factor on forecasts.* Form $g^{(t)}(s) := D_-^{(1-\gamma)/2}\bar\alpha(t,\cdot)(s)$. The Marchaud form (§3.2) gives $g^{(t)}(s)$ as an integral of $\bar\alpha(t,r) - \bar\alpha(t,r+\cdot)$ over $r\ge s$, i.e. depending on the forecast curve to the *future of $s$*. Because $\bar\alpha(t,\cdot)$ is $\mathcal{F}_t$-measurable on the whole real line (§4.2), so is $g^{(t)}(s)$ for every $s$. Future information enters only through this step, and only via the forecast model.
2. *Causal factor on the result.* Apply $D_+^{(1-\gamma)/2}$ to $g^{(t)}$ and evaluate at $s=t$. The Marchaud form (§3.2) for $D_+^{(1-\gamma)/2}$ integrates over $u>0$, sampling $g^{(t)}(s)$ for $s\le t$ only - i.e. *causally in the intermediate function*.

The non-causality of $\mathbb{D}^{1-\gamma}$ is therefore quarantined entirely in the forecast-consuming step (1). Step (2) is causal in the prediction-corrected intermediate, exactly as in the classical Wiener filter where causality of the realization is restored by absorbing the anticausal spectral factor into a prediction operation on the input.

**Order halving.** Each factor in (4.3.2) has order $\beta = (1-\gamma)/2 < 1/2$, half the order of the Riesz operator. The factored form is consequently better-behaved numerically: each factor is less singular than $\mathbb{D}^{1-\gamma}$, and standard Marchaud-form quadratures converge faster.

**Parametric dependence of the intermediate.** The intermediate $g^{(t)}$ depends on the conditioning time $t$ as a parameter; as $t$ advances, $g^{(t)}$ is rebuilt from the updated forecast curve $\bar\alpha(t,\cdot)$. The decomposition (4.3.3) is *not* the diagonal trace of a single process filtered causally along time: the operation $\tau\mapsto D_-^{\beta}\bar\alpha(\tau,\cdot)(\tau)$ followed by $D_+^{\beta}$ along the $\tau$-axis gives a *different* (and suboptimal) policy, since it discards how the forecast curve depends on $t$ off the diagonal. Operator composition in (4.3.3) is in the $s$-variable of the fixed time-$t$ curve, not along the conditioning-time axis. See `notes/riesz-factorization-wiener-hopf.md` §7 for the cautionary calculation.

**Complementary additive form.** A separate algebraic identity - not a Wiener-Hopf factorization, but the additive half-sum representation of the Riesz derivative - reads

$$ \mathbb{D}^{1-\gamma} \;=\; \frac{1}{2\sin(\pi\gamma/2)}\bigl(D_+^{1-\gamma} + D_-^{1-\gamma}\bigr), \tag{4.3.4} $$

with full-order one-sided operators (SKM 1993 §12.1 (12.5); $\cos(\pi(1-\gamma)/2) = \sin(\pi\gamma/2)$). Evaluated on the forecast curve at $s=t$, (4.3.4) **support-splits at the diagonal**: $D_+^{1-\gamma}\bar\alpha(t,\cdot)(t)$ uses only $\{s\le t\}$-values (the realized signal path), and $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t)$ uses only $\{s\ge t\}$-values (the forecast tail). This is structurally different from (4.3.3): it is a sum, not a composition, of full-order rather than half-order operators, and the decomposition is at the evaluation point rather than at the operator level. It is the natural form for **closed-form evaluation** when the forecast model produces a tractable $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t)$. For example, for an OU signal $d\alpha_t = -\theta\alpha_t\,dt + \sigma\,dW_t$ with forecast $\bar\alpha(t,s) = e^{-\theta(s-t)}\alpha_t$ for $s>t$,

$$ D_-^{1-\gamma}\bar\alpha(t,\cdot)(t) \;=\; \theta^{1-\gamma}\,\alpha_t, \tag{4.3.5} $$

by direct Marchaud integration against the exponential tail ($\int_0^\infty u^{-(2-\gamma)}(1-e^{-\theta u})\,du = \Gamma(\gamma)\theta^{1-\gamma}/(1-\gamma)$, equivalently $\int_0^\infty u^{-1-\beta}(1-e^{-\theta u})\,du = \Gamma(1-\beta)\theta^\beta/\beta$ at half order). The bulk policy for OU then reads

$$ u^{\rm bulk}_t \;=\; \frac{\kappa_{1-\gamma}}{2\sin(\pi\gamma/2)}\bigl[(D_+^{1-\gamma}\alpha)(t) \;+\; \theta^{1-\gamma}\,\alpha_t\bigr], \tag{4.3.6} $$

where $(D_+^{1-\gamma}\alpha)(t)$ is the causal Marchaud derivative of the realized OU path. The realized-signal contribution is a hyperbolically-weighted moving average of past signal increments; the forecast contribution collapses to a simple multiplier of the current state, scaled by the mean-reversion rate to the power $1-\gamma$.

**Scope across domains.** The factorization (4.3.2)-(4.3.3) holds on $\mathbb{R}$ and is inherited by the bulk part of the bounded-interval and half-line problems of §5: the bulk operator is the same translation-invariant Riesz operator everywhere; only the boundary correction differs. The Wiener-Hopf factorization invoked in §5.3 is a **distinct** construction - the spectral factorization of the $\eta$-**augmented** symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ - used there to resolve the half-line domain ambiguity and select the decaying boundary mode. The two W-H constructions operate on different symbols and serve different purposes; we keep them notationally distinct.

### 4.4 Extension: bulk with temporary impact

When a constant temporary-impact term $\tfrac12\eta u_t^2$, $\eta\ge 0$, is added to the cost (as it must be on the half-line for well-posedness; see §5.3), the bulk FOC on $\mathbb{R}$ becomes

$$ \eta\,u^{\rm bulk}_t \;+\; \int_\mathbb{R} G(|t-v|)\,u^{\rm bulk}_v\,dv \;=\; \bar\alpha(t,\cdot)(t) \;-\; \lambda. $$

In Fourier on $\mathbb{R}$ the symbol becomes

$$ M(\xi) \;:=\; \hat G(\xi) + \eta \;=\; c_\gamma|\xi|^{\gamma-1} + \eta, $$

and the bulk solution is the symbol-inverse multiplier:

$$ \hat u^{\rm bulk}(\xi) \;=\; \bigl(c_\gamma|\xi|^{\gamma-1} + \eta\bigr)^{-1}\,\widehat{(\bar\alpha-\lambda)}(\xi). $$

**Special limit $\eta\to 0$.** The symbol becomes pure power-law, $M(\xi)\to c_\gamma|\xi|^{\gamma-1}$, and the inverse multiplier becomes $c_\gamma^{-1}|\xi|^{1-\gamma}$ - i.e. exactly the fractional derivative of Theorem 4.1. The $\eta\to 0$ limit therefore recovers the pure bulk solution; the temporary impact is a regularizer in the high-frequency tail (since $c_\gamma|\xi|^{\gamma-1}\to 0$ as $|\xi|\to\infty$ for $\gamma<1$, the inverse symbol grows, and $\eta>0$ bounds the inverse below by $\eta^{-1}$).

**Crossover scale.** The two terms in $M(\xi)$ are equal at the frequency

$$ \boxed{\;\xi_*(\eta) \;:=\; \bigl(c_\gamma/\eta\bigr)^{1/(1-\gamma)}.\;} $$

For $|\xi|\ll\xi_*$, the propagator term dominates and the policy behaves like a fractional derivative; for $|\xi|\gg\xi_*$, the temporary-impact term dominates and the policy behaves like $u^{\rm bulk}\approx \bar\alpha/\eta$, i.e. direct signal-following. The scale $\xi_*$ separates the long-memory and myopic regimes; we return to its economic interpretation in §5.3 and §8.

### 4.5 Sign convention and Euler-Lagrange derivation

We record the sign convention once. The cost functional of §2.3,

$$ \mathcal{C}(u) \;=\; \tfrac12\mathbb{E}\!\!\int\!\!\int G(|t-v|) u_t u_v\,dt\,dv \;-\; \mathbb{E}\!\!\int u_t\,\alpha_t\,dt \;+\; \lambda\!\!\int u_t\,dt, $$

has Gâteaux derivative in direction $\delta u$:

$$ \delta\mathcal{C} \;=\; \mathbb{E}\!\!\int\!\!\int G(|t-v|)\,u_v\,\delta u_t\,dt\,dv \;-\; \mathbb{E}\!\!\int \alpha_t\,\delta u_t\,dt \;+\; \lambda\!\!\int \delta u_t\,dt. $$

Setting $\delta\mathcal{C} = 0$ for all $\delta u$ gives the FOC with RHS $\alpha_t - \lambda$ (the $\lambda$ enters with the same sign as the budget term contributed). This is the sign convention of $(\star)$, $(\star_{\rm bulk})$, $(\star_{\rm WH})$, and propagates verbatim to Theorem 4.1 and the boundary-corrected results of §5.

### 4.6 Interpretation

The bulk solution is the fractional differentiator of order $1-\gamma$ applied to the conditionally expected signal. Four observations:

1. **Memory.** Standard PID uses $D^0 = \mathrm{id}$ and $D^1 = d/dt$; bulk execution uses $D^{1-\gamma}$ with $\gamma\in(0,1)$, i.e. an order strictly between identity and full differentiation - the hallmark of Oustaloup's CRONE fractional-PID control.
2. **Roughness.** For Hölder-$\beta$ signals with $\beta > 1-\gamma$, the fractional derivative is pointwise defined; rougher signals require Marchaud regularization.
3. **Compute.** The Riesz fractional derivative discretizes to a Toeplitz matrix-vector product on a uniform grid, hence $O(N\log N)$ via FFT - versus $O(N^2)$ for Nyström inversion of $(\star)$. See Appendix D.
4. **Robustness diagnostic.** Mis-specification of $\gamma$ has a sharp analytic interpretation as the wrong order of differentiation, with cost degradation first-order in $\Delta\gamma$ (see the CRONE-2 stability analysis recalled in §8).

---

## 5. Boundary corrections

The bulk solution of Theorem 4.1 lives on $\mathbb{R}$. Every *restriction* of the bulk problem to a smaller domain with boundary data introduces a *homogeneous solution* of the bulk equation, picked to enforce the boundary data. We treat the principle abstractly in §5.1 and specialize to the two cases of interest - the bounded interval $[0,T]$ (§5.2) and the half-line $[0,\infty)$ (§5.3) - in the following subsections.

### 5.1 The general principle

Let $\mathcal{L}$ denote the bulk operator on the domain $\mathbb{T}\subseteq\mathbb{R}$: $\mathcal{L}u = G*u$ in the linear-impact case, or $\mathcal{L}u = \eta u + G*u$ when temporary impact is included. A solution of the restricted FOC $\mathcal{L}u = f$ on $\mathbb{T}$ with boundary data $\mathcal{B}\mathit{ndy}(u) = b$ on $\partial\mathbb{T}$ admits the decomposition

$$ u^*_t \;=\; u^{\rm bulk}_t \;+\; \mathcal{B}(t), $$

where $u^{\rm bulk}$ is the bulk solution of $\mathcal{L}u = f$ on the natural extension of $\mathbb{T}$ to $\mathbb{R}$ (by stationary or zero extension of the data, as appropriate), and $\mathcal{B}$ solves the *homogeneous* equation $\mathcal{L}\mathcal{B} = 0$ on $\mathbb{T}$ with boundary data $\mathcal{B}\mathit{ndy}(\mathcal{B}) = b - \mathcal{B}\mathit{ndy}(u^{\rm bulk})$.

The kernel of $\mathcal{L}$ on $\mathbb{T}$ is a finite-dimensional space (with dimension equal to the number of boundary conditions), spanned by *homogeneous modes*. For the symmetric power-law kernel, the homogeneous modes are explicit:
- On $[0,T]$ with the symmetric Abel operator, the kernel is two-dimensional, spanned by $(t(T-t))^{(\gamma-1)/2}$ and a second mode (the airfoil-equation second null function, see SKM 1993 §13.2 Remark 13.3).
- On $[0,\infty)$ with the symmetric power-law kernel and temporary impact, the kernel is one-dimensional, spanned by the decaying-at-infinity Wiener-Hopf homogeneous mode picked out by factorization $M = M_+ M_-$ (§5.3).
- On $\mathbb{R}$, the kernel is zero-dimensional (no nonzero decaying-at-infinity stationary solution to $\mathcal{L}u = 0$), so $\mathcal{B}\equiv 0$ and the bulk solution is the entire answer.

The *form* of the boundary correction is universal: a linear combination of homogeneous modes with coefficients fixed by the boundary data. The *content* differs per domain only through (i) the dimension of the kernel and (ii) the explicit form of the homogeneous modes.

*Inheritance of the forecast curve.* The decomposition $u^* = u^{\rm bulk} + \mathcal{B}$ is applied to the $\mathcal{F}_t$-conditioned FOC of §2.3, i.e. to $(\star^{\mathcal{F}})$ on $[0,T]$ and $(\star_{\rm WH}^{\mathcal{F}})$ on $[0,\infty)$. The bulk part inverts the same translation-invariant symbol as on $\mathbb{R}$ and therefore acts on $\bar\alpha(t,\cdot)$ exactly as in Theorem 4.1. The boundary correction $\mathcal{B}$ solves the *homogeneous* equation $\mathcal{L}\mathcal{B} = 0$ and is therefore independent of $\alpha$; its coefficients are fixed by boundary data (initial inventory, terminal constraint, decay-at-infinity) that involve $\bar\alpha(t,\cdot)$ only through the budget integral of $u^{\rm bulk}$. In particular, the substitution "$\alpha_s\mapsto\bar\alpha(t,s)$ for $s>t$" in the bounded-interval and half-line policies of §5.2 and §5.3 is not an additional assumption: it is inherited from §2.3 verbatim.

### 5.2 Bounded interval $[0,T]$ with terminal inventory constraint

We now specialize to $\mathbb{T} = [0,T]$ with initial inventory $X_0$ and terminal constraint $X_T = 0$.

#### 5.2.1 Homogeneous modes

The kernel of the symmetric Abel operator $\mathcal{L}u = \int_0^T |t-v|^{-\gamma}u_v\,dv$ on $[0,T]$ is two-dimensional, spanned by the **Söhngen-Tricomi modes**:

$$ \phi_1(t) = \bigl(t(T-t)\bigr)^{(\gamma-1)/2}, \qquad \phi_2(t) = \frac{T-2t}{2}\bigl(t(T-t)\bigr)^{(\gamma-1)/2}. $$

Both are integrable on $(0,T)$ since the exponent $(\gamma-1)/2 \in (-1/2,0)$, hence the integral is convergent at both endpoints (Tricomi 1957 §4.3; SKM 1993 §13.2 Remark 13.3 records the airfoil equation analog). The first mode $\phi_1$ is the GSS U-shape; the second mode $\phi_2$ is an odd correction that enables matching both endpoint conditions independently.

#### 5.2.2 The bounded-interval policy

**Corollary 5.2 (Bounded-interval execution; demoted v1 Theorem 4.1).** *Under the assumptions of Theorem 4.1, restricted to $\mathbb{T} = [0,T]$ with initial inventory $X_0$ and terminal constraint $X_T = 0$, the optimal trading rate is*

$$ u^*_t \;=\; \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}_{[0,T]}\!\bigl(\bar\alpha(t,\cdot) - \lambda\bigr)(t) \;+\; \mathcal{B}_{1-\gamma}(t), \qquad t\in(0,T), $$

*with*

$$ \mathcal{B}_{1-\gamma}(t) \;=\; c_1\,\phi_1(t) \;+\; c_2\,\phi_2(t) \;=\; c_1\,\bigl(t(T-t)\bigr)^{(\gamma-1)/2} \;+\; c_2\,\frac{T-2t}{2}\,\bigl(t(T-t)\bigr)^{(\gamma-1)/2}, $$

*and the coefficients $c_1, c_2, \lambda$ jointly determined by the two boundary conditions $X_0$ (initial inventory) and $X_T = 0$ (terminal inventory) under the budget constraint $\int_0^T u^*_t\,dt = X_0$.*

**Proof.** Decompose $u^* = u^{\rm bulk} + \mathcal{B}_{1-\gamma}$ following §5.1. The bulk part is Theorem 4.1 with the bounded-interval form of the Riesz operator (§3.2). The boundary correction $\mathcal{B}_{1-\gamma}$ lies in the kernel of the bounded-interval Abel operator and is therefore a linear combination of the modes $\phi_1, \phi_2$ of §5.2.1. The two coefficients $c_1, c_2$ are fixed by the two boundary conditions (initial inventory $X_0$, which fixes $\int_0^T u^*\,dt = X_0$, and terminal inventory $X_T = 0$, which combined with the budget gives the second condition); $\lambda$ is the corresponding Lagrange multiplier. Full SKM 1993 §13.2 Thm 13.2 derivation: Appendix A.2. ∎

#### 5.2.3 Economic interpretation of the U-shape

The leading Söhngen mode $\phi_1(t) = (t(T-t))^{(\gamma-1)/2}$ has two natural interpretations.

At $t \to 0^+$, no past trading has populated the impact tail, so $\int_0^{0^+} G(t-s)\,u_s\,ds = 0$ and trading is cheap because no transient impact has yet accumulated against this trade.

At $t \to T^-$, no future trades will be penalized by the outgoing tail of the current trade's impact, because trading ceases at $T$; so trading is again cheap.

The interior ($t = T/2$, say) pays for both tails simultaneously and is most expensive. The U-shape is therefore the trader's exploitation of these two cheap-trading windows. The exponent $(\gamma-1)/2 \in (-1/2, 0)$ encodes that the boundary effect is sharper when the kernel is *less* singular (smaller $\gamma$ ⇒ more divergent U-shape) and milder when the kernel is more singular (larger $\gamma$ ⇒ flatter U).

#### 5.2.4 Recovery of disclosed special cases

**Corollary 5.2.1 (GSS zero-signal limit).** *When $\bar\alpha(t,\cdot)\equiv 0$, the bulk term vanishes and $u^*_t = c_1\bigl(t(T-t)\bigr)^{(\gamma-1)/2}$ with $c_1$ fixed by the budget, recovering the Gatheral-Schied-Slynko (2012) U-shaped Abel solution. Numerical check at $\gamma = 1/2$ gives $u^*_t \propto [t(T-t)]^{-1/4}$, matching the exponent $-\nu = -1/4$ of GSS.*

**Conjecture 5.2.2 (Forde-Sánchez-Betancourt-Smith Gaussian Volterra recovery).** *When $\alpha_t = \int_0^t (t-s)^{H-1/2}\,dW_s$ for $H\in(0,1/2)$, the conditional forecast curve becomes a Riemann-Liouville fractional integral of order $H+1/2$ of $dW$, and the bounded-interval policy of Corollary 5.2 is expected to reduce to the fractional-Beta kernel of Forde et al. (2022) eq. (26).* **A rigorous proof requires a direct kernel-matching argument on $[0,T]$**: the half-line semigroup identity $D^\nu I^\mu = I^{\mu-\nu}$ does *not* apply cleanly to the symmetric Riesz operator on a bounded interval (boundary weights $(s(T-s))^{\mp\nu}$ break the half-line semigroup). Per decision D4 = A, we leave the recovery as a conjecture; the structural sketch is in Appendix A.5.

⚠️ **TODO** (kernel-matching computation against Forde et al. 2022 eq. (26) on $[0,T]$).

#### 5.2.5 Boundary correction is $O(1/T)$ in the bulk region

The bulk/boundary picture suggests, and we now verify, that for long horizons the boundary correction is small relative to the bulk in the interior of $[0,T]$. This is the quantitative content of the "stationary problem is the heart of the matter" assertion.

**Proposition 5.3 (Boundary correction is $O(1/T)$ in the bulk region).** *Fix $\gamma\in(0,1)$, initial inventory $X_0\in\mathbb{R}$ (treated as fixed and $O(1)$ in $T$), and terminal constraint $X_T = 0$. Let $\alpha$ be a bounded stationary signal, $\|\bar\alpha\|_\infty \le M < \infty$. Fix $\epsilon\in(0,1/2)$. Then the boundary correction $\mathcal{B}_{1-\gamma}$ of Corollary 5.2 satisfies*

$$ \sup_{t\in[\epsilon T,\,(1-\epsilon)T]} \bigl|\mathcal{B}_{1-\gamma}(t)\bigr| \;=\; O\!\left(\frac{X_0 + M}{T}\right) \qquad \text{as } T \to \infty, $$

*while the bulk term $\kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}(\bar\alpha-\lambda)(t)$ remains $\Theta(1)$ in $T$ (since $\bar\alpha$ is $O(1)$ and $\mathbb{D}^{1-\gamma}$ is bounded on suitable spaces, e.g. $L^\infty\cap H^{1-\gamma}$ under the PSD bound). The bound is NOT uniform: near the endpoints, $\mathcal{B}_{1-\gamma}(t)$ diverges as $\bigl|t\,(T-t)\bigr|^{(\gamma-1)/2}$, integrably but unboundedly.*

**Proof sketch.** The budget constraint $\int_0^T u^*_t\,dt = X_0$ forces

$$ c_1\int_0^T \phi_1(t)\,dt \;+\; c_2\int_0^T \phi_2(t)\,dt \;=\; X_0 \;-\; \int_0^T u^{\rm bulk}_t\,dt. $$

The leading integral evaluates to (substitute $t = sT$, $dt = T\,ds$):

$$ \int_0^T \bigl(t(T-t)\bigr)^{(\gamma-1)/2}\,dt \;=\; T^\gamma\,B\!\left(\tfrac{\gamma+1}{2},\tfrac{\gamma+1}{2}\right), $$

with $B$ the Beta function. (The second-mode integral $\int_0^T \phi_2\,dt = 0$ by oddness about $t = T/2$.) The bulk contribution to the cumulative trade is, for an OU or otherwise ergodic signal, $\int_0^T u^{\rm bulk}_t\,dt = O(\sqrt{T})$ (random-walk scaling) or even $O(1)$ (if the signal is mean-zero with sufficiently fast mixing for the fractional-derivative output to be mean-zero and integrable). In either case the right-hand side is dominated by $X_0$ plus a $O(M)$ deterministic envelope, so

$$ |c_1| \;=\; \Theta\!\left(\frac{X_0 + M}{T^\gamma}\right). $$

The terminal-inventory condition then fixes $c_2$ of the same order. Substituting back and evaluating at $t = sT$ for fixed $s\in[\epsilon, 1-\epsilon]$:

$$ \mathcal{B}_{1-\gamma}(sT) \;=\; \Theta\!\left(\frac{X_0+M}{T^\gamma}\right)\cdot\bigl(s(1-s)T^2\bigr)^{(\gamma-1)/2} \;=\; \Theta\!\left(\frac{X_0+M}{T}\right)\cdot\bigl(s(1-s)\bigr)^{(\gamma-1)/2}. $$

The factor $(s(1-s))^{(\gamma-1)/2}$ is bounded on $s\in[\epsilon, 1-\epsilon]$ by $(\epsilon(1-\epsilon))^{(\gamma-1)/2}$, so the supremum bound follows with implicit constant proportional to $(\epsilon(1-\epsilon))^{(\gamma-1)/2}\cdot B(\tfrac{\gamma+1}{2},\tfrac{\gamma+1}{2})^{-1}$.

The non-uniformity is immediate: as $s\to 0$ or $s\to 1$, $(s(1-s))^{(\gamma-1)/2}\to\infty$, so the bound degenerates near the endpoints. The boundary term *is* integrable on $[0,T]$ in the $L^1$ sense (since $(\gamma-1)/2 > -1/2$) but is unbounded pointwise near the endpoints. Full argument with quantitative constants: Appendix A.2 Part 2. ∎

**Corollary 5.4 (Bulk as long-horizon asymptotic optimum).** *Under the assumptions of Proposition 5.3,*

$$ u^*_t \;=\; u^{\rm bulk}_t \;+\; O\!\left(\frac{X_0+M}{T}\right) \qquad \text{uniformly for } t\in[\epsilon T,(1-\epsilon)T],\ \text{as }T\to\infty. $$

*In particular, the bulk solution is the leading-order optimal trading rate in the long-horizon limit, with the bounded-interval boundary correction contributing only a $1/T$ relative perturbation in the interior.*

This corollary makes precise the previously vague "boundary corrections absorbed into $\mathcal{B}$" sentence flagged by the Round 2 math reviewer. It also justifies the spine: the bulk theorem is the load-bearing result, and the boundary correction on $[0,T]$ is asymptotically subdominant on the bulk region.

⚠️ **TODO** (precise constant for $\int_0^T u^{\rm bulk}\,dt$ for OU and Volterra-Gaussian signals; current sketch uses $O(\sqrt{T})$ random-walk bound which is conservative for mean-reverting signals).

### 5.3 Half-line $[0,\infty)$ with temporary impact

We now specialize to $\mathbb{T} = [0,\infty)$ with initial inventory $X_0$ given, decay at infinity required, and stationary signal $\alpha$ on the half-line. This is the *stationary* analogue of §5.2 and is the most natural domain for the "fractional derivative is the optimal trading rule" claim because it is the closest to the bulk setting (just remove $t < 0$).

#### 5.3.1 Well-posedness via temporary impact

Dropping the terminal constraint and taking $T = \infty$ creates two distinct issues:

1. *Cumulative integrability.* The cumulative cost $\int_0^\infty u_t(G*u)\,dt$ is generically $+\infty$ for any nonzero stationary policy (since the integrand is stationary positive). This is generic - not specific to power-law impact - and we handle it by reformulating the objective as **average cost per unit time**. This is the convention used in GP 2013 (with discounting) and in the steady-state regime of AJN 2022 and AJNT 2024.
2. *Inverse symbol unboundedness.* The bare inverse symbol $c_\gamma^{-1}|\xi|^{1-\gamma}$ is unbounded as $|\xi|\to\infty$, so the bare optimum $u^*$ is generically not in $L^2$ for stationary signals with finite PSD. A coercive regularizer is required.

We adopt the **temporary-impact regularizer** $\tfrac12\eta u_t^2$ with $\eta > 0$ (per decision D6 = A′). Economically $\eta$ models spread/slippage/fill-rate friction - the per-trade cost of immediacy - as in Obizhaeva-Wang (2013), AJN (2022), AJNT (2024). Mathematically $\eta$ shifts the FOC symbol to $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$, bounding the inverse symbol $M(\xi)^{-1}$ above by $\eta^{-1}$ at high frequency. The bare problem ($\eta = 0$) is recovered as a limit in §5.3.3.

We do **not** add a Gârleanu-Pedersen running inventory-risk penalty $\tfrac12\gamma_{\rm risk}\sigma^2 X_t^2$ here; that regularizer shifts the symbol by $\gamma_{\rm risk}\sigma^2/\xi^2$ (low-frequency regularization) and the corresponding W-H factorization is no longer a closed-form power. See §6.5 for a pointer.

#### 5.3.2 Augmented-symbol Wiener-Hopf as the tool for picking the boundary mode

The Wiener-Hopf factorization invoked here is **distinct from the bulk-symbol factorization of §4.3**. §4.3 factorizes the bare Riesz symbol $|\xi|^{1-\gamma}$ on $\mathbb{R}$ to expose the causal realization of the bulk policy on every domain (no half-line content). The present subsection factorizes the *augmented* symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1}+\eta$ specifically to resolve the half-line domain ambiguity - it is what selects the decaying-at-infinity boundary mode. The two factorizations act on different symbols and do different jobs; we keep them notationally distinct.

The Fourier symbol of the half-line FOC $(\star_{\rm WH})$ is

$$ M(\xi) \;:=\; \hat G(\xi) + \eta \;=\; c_\gamma|\xi|^{\gamma-1} + \eta, \qquad c_\gamma = 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2), $$

defined on $\mathbb{R}\setminus\{0\}$. For $\eta > 0$ the symbol is strictly positive everywhere on $\mathbb{R}\setminus\{0\}$, bounded below by $\eta$ at infinity, and integrable against $\log$ at the origin (since $|\xi|^{\gamma-1}$ is locally integrable for $\gamma\in(0,1)$).

**Proposition 5.5 (Wiener-Hopf factorization of $M$).** *For each $\eta > 0$, the symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ admits a canonical Wiener-Hopf factorization*

$$ M(\xi) \;=\; M_+(\xi)\,M_-(\xi), $$

*with $M_+$ (resp. $M_-$) analytic and nonzero in the closed upper (resp. lower) complex half-plane $\{\mathrm{Im}\,\xi \ge 0\}$ (resp. $\{\mathrm{Im}\,\xi \le 0\}$). The factorization is unique up to a multiplicative real sign and exists by Krein's theorem (Krein 1962; Noble 1958 §2.4), since $M$ satisfies the Krein integrability condition $\int_\mathbb{R} \log(1+|\xi|)\,\bigl|\log M(\xi)\bigr|\,(1+\xi^2)^{-1}\,d\xi < \infty$. For $\eta = 0$ the symbol degenerates to a pure power-law and factorizes in closed form as*

$$ M_\pm(\xi) \;=\; c_\gamma^{1/2}\,(\mp i\xi)^{(\gamma-1)/2}, $$

*with the principal branch on $\mathbb{C}\setminus(-\infty,0]$.*

**Proof.** For $\eta > 0$: the Krein integrability condition is verified explicitly in Appendix A.3 (low- and high-frequency tails are both bounded). For $\eta = 0$: $|\xi|^{\gamma-1} = ((-i\xi)(i\xi))^{(\gamma-1)/2}$ on $\mathbb{R}\setminus\{0\}$ by branch-cut bookkeeping; analyticity of $(\mp i\xi)^{(\gamma-1)/2}$ in the corresponding half-planes is immediate from the principal branch. Full argument: Appendix A.3. ∎

#### 5.3.3 The half-line policy

**Corollary 5.7 (Half-line execution via Wiener-Hopf).** *Under the setup of §5.3.1 with $\eta > 0$, the optimal half-line trading rate is*

$$ u^*_t \;=\; \bigl(M_+^{-1}\,\Pi_+\,M_-^{-1}\bigr)\bigl[\bar\alpha^\infty(t,\cdot)\bigr](t), \qquad t \ge 0, $$

*where $\Pi_+$ is the projection onto causal functions on $[0,\infty)$ and $\bar\alpha^\infty(t,\cdot)$ is the half-line forecast curve of §2.2. In the special limit $\eta\to 0$, the factorization becomes the closed form of Proposition 5.5 and the policy reduces to*

$$ u^*_t \;=\; \kappa_{1-\gamma}\,D^{(1-\gamma)/2}_+\,\Pi_+\,D^{(1-\gamma)/2}_-\bigl[\bar\alpha^\infty(t,\cdot)\bigr](t), $$

*i.e. the causal Riesz fractional derivative of order $1-\gamma$ of the forecast curve, which is exactly the **bulk solution** of Theorem 4.1 restricted to $[0,\infty)$. The constant matches the bulk constant: $\kappa_{1-\gamma} = c_\gamma^{-1}$ throughout.*

The $\eta\to 0$ limit makes §5.3 the half-line analogue of the bulk theorem: in this limit the boundary correction degenerates to the single mode required by the initial inventory $X_0$ (a delta at $t = 0$, formally absorbed into the projection $\Pi_+$), and the fractional-derivative content of the policy is the full content. For $\eta > 0$ the W-H factorization picks out the homogeneous mode required to enforce both the initial-inventory and the decay-at-infinity conditions.

#### 5.3.4 Crossover scale and slow-vs-fast trading

For $\eta > 0$ the symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ has the *crossover frequency*

$$ \xi_*(\eta) \;:=\; \bigl(c_\gamma / \eta\bigr)^{1/(1-\gamma)}, $$

at which the propagator and temporary-impact terms are equal. At frequencies $|\xi| \ll \xi_*$ the propagator term dominates, $M(\xi)\approx c_\gamma|\xi|^{\gamma-1}$, and the inverse-symbol policy behaves like the *fractional derivative of order $1-\gamma$* of the bulk theorem - slow components of the signal are traded via the long-memory fractional rule. At frequencies $|\xi|\gg\xi_*$ the temporary-impact term dominates, $M(\xi)\approx\eta$, and the optimal rate behaves like *direct signal-following* $u^*_t \approx \bar\alpha_t/\eta$ - fast components are traded by immediate response, because the impact resets between successive trades.

The reciprocal scale $1/\xi_*$ in the time domain is the **propagator memory horizon relative to the spread cost**: signals slower than this horizon get fractionally differentiated; signals faster get followed directly. A single parameter $\eta/c_\gamma$ tunes between the long-memory and myopic regimes.

This crossover structure is the half-line analogue of the boundary-vs-bulk decomposition on $[0,T]$: in both cases the fractional-derivative content is the bulk part, and a problem-specific regularizer ($X_T = 0$ on $[0,T]$, $\eta > 0$ on $[0,\infty)$) introduces a domain-scale-dependent correction.

**AJNT framing caveat.** The W-H factorization here is the frequency-domain image of the operator-resolvent calculus of Abi Jaber-Neuman-Tuschmann (2024, arXiv:2403.10273) *only* under the §5.3 specializations: (i) scalar power-law kernel, (ii) stationary signal, (iii) constant temporary impact, (iv) half-line domain. The general AJNT resolvent does not in general reduce to a Fourier multiplier (their FOC is a stochastic Fredholm equation of the second kind, solved by an operator resolvent that uses the matrix Volterra structure non-translation-invariantly). Our specialization is therefore the explicit half-line / power-law case of their framework.

---

## 6. Limits, special cases, and connections

### 6.1 Bounded interval with temporary impact: Mittag-Leffler resolvent

Adding temporary impact $\tfrac12\eta u_t^2$ to the bounded-interval problem of §5.2 changes the FOC from the first-kind Fredholm equation $(\star)$ to the second-kind equation

$$ 2\eta\,u^*_t \;+\; \int_0^T G(|t-v|)\,u^*_v\,dv \;=\; \alpha_t - \lambda. \tag{$\star\star$} $$

The bulk part of the solution is the inverse of the second-kind symbol on $\mathbb{R}$ - i.e. the inverse of $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ acting on the forecast curve - exactly as in §4.4. The boundary correction is the bounded-interval homogeneous solution, modulated by the temporary-impact regularization. The combined kernel is expressible via the two-parameter Mittag-Leffler function.

**Theorem 6.1 (Mittag-Leffler resolvent on $[0,T]$).** *Under $(\star\star)$ with projection onto $\mathcal{F}_t$ as in §4.2, the optimal rate is*

$$ u^*_t \;=\; \int_0^T R_{\gamma,\eta}(t,s)\,\bigl(\bar\alpha(t,s) - \lambda\bigr)\,ds \;+\; \mathcal{B}^{\eta}_{1-\gamma}(t), $$

*where, away from the boundary $\{0,T\}$ of the interval,*

$$ R_{\gamma,\eta}(t,s) \;=\; \frac{1}{2\eta}\,\delta(t-s) \;-\; \frac{c\,\Gamma(1-\gamma)}{(2\eta)^2}\,|t-s|^{-\gamma}\, E_{1-\gamma,\,1-\gamma}\!\left(-\frac{c\,\Gamma(1-\gamma)}{2\eta}\,|t-s|^{1-\gamma}\right). $$

*Boundary-correction modulation $\mathcal{B}^{\eta}_{1-\gamma}$ takes the same Söhngen-mode shape as in §5.2, with coefficients $\eta$-dependent through the budget constraint. The limit $c\to 0$ recovers $R_{\gamma,\eta}\to(2\eta)^{-1}\delta$ (no impact), and $\eta\to 0$ recovers Theorem 4.1.*

**Proof.** Neumann series of the Volterra operator $\eta^{-1} G*$, identifying iterated power-law convolutions via Mittag-Leffler. Full computation: Appendix A.4. ⚠️ **TODO** (quantitative finite-interval HLS bound on Neumann radius; boundary-tail correction to interior $R_{\gamma,\eta}$). ∎

**Remark 6.1.1.** The $\eta\to\infty$ limit gives $R_{\gamma,\eta}\to (2\eta)^{-1}\delta$ and $u^*_t \to (2\eta)^{-1}(\bar\alpha(t,t) - \lambda) = (2\eta)^{-1}(\alpha_t - \lambda)$, i.e. the *Cartea-Jaimungal (2016) myopic policy* - not the Almgren-Chriss inventory-tracking $u\propto X/(T-t)$ (those are distinct regimes).

### 6.2 Almgren-Chriss and Obizhaeva-Wang

The Almgren-Chriss (2001) policy is the $\eta\to\infty$ / $c\to 0$ degeneration of $(\star\star)$, which collapses the propagator term and leaves a pure quadratic-cost problem solved by linear-in-inventory inventory-tracking. Theorem 4.1's bulk content is absent in that limit (no propagator means no fractional derivative); the AC policy is therefore the *trivial* bulk limit.

Obizhaeva-Wang (2013) uses an exponential decay kernel $G(t) = \rho\,e^{-\rho t}$ rather than a power-law. **Theorem 4.1 does NOT recover OW by taking $\gamma\to 1^-$**: as $\gamma\to 1^-$, the power-law $c|t|^{-\gamma}$ becomes more singular at the origin, not exponential. An analogous derivation with $G(t) = \rho e^{-\rho t}$ gives the OW resolvent via $E_{1,1}(z) = e^z$ in closed form, but it is a separate Markov-Riccati computation; the bridge between the exponential and power-law regimes goes through the multi-exponential approximation of the power-law kernel (Abi Jaber-El Euch 2019; Abi Jaber 2019).

### 6.3 Forde-Sánchez-Betancourt-Smith (2022) [closest prior art]

FSS2022 solve the bounded-interval signal-adaptive propagator problem with the *identical* kernel $G(t)=ct^{-\gamma}$, $\gamma\in(0,1)$, and Gaussian Volterra signals $\xi_t = \mathbb{E}_t[P_T - P_t]$ with full liquidation $X_T=0$. The FOC they solve is the same Fredholm equation $(\star)$ on $[0,T]$ that our §2.3 derives. They prove (Theorem 2.2) that the Fredholm operator on $L^2[0,1]$ factorizes as $T = B^{-1} I_\nu B$ with $B$ multiplication by $t^{-(1-\gamma)/4}$ and $I_\nu$ the **Riemann-Liouville operator of order $r=(1-\gamma)/2$**, and invoke $I_\nu^{-1} = \Gamma(1-r)D^r$ to invert.

This is, structurally, the same content as our §4.3 multiplicative bulk-symbol Wiener-Hopf factorization $\mathbb{D}^{1-\gamma} = D_+^{(1-\gamma)/2} D_-^{(1-\gamma)/2}$, in operator language and conjugated by the boundary-weight $B$ that handles the bounded-interval endpoints. The substantive fractional-operator insight is **present in FSS2022** and we do not claim it as original to this paper.

Our explicit contribution relative to FSS2022:

- **Whole-line presentation.** Theorem 4.1 is stated and proved on $\mathbb{R}$, without bounded-interval weight conjugation; this isolates the fractional-derivative content from the boundary device.
- **Forecast curve as explicit object.** We identify the conditional forecast curve $\bar\alpha(t,\cdot)$ as the function on which the operator acts. FSS2022 use a Volterra-on-Brownian ansatz $\hat u_t = \bar u(t) + \int_0^t k(v,t)dW_v$ and absorb conditional expectations into kernel determination; the forecast curve does not appear as a named object.
- **Bulk/boundary spine.** Treating the whole-line translation-invariant case as primary, with bounded-interval (§5.2), half-line with temporary impact (§5.3), and Mittag-Leffler resolvent (Theorem 6.1) as boundary-perturbed restrictions, is a structural choice. FSS2022 work entirely on $[0,T]$.
- **Compact Riesz form.** The final FSS2022 formulas (e.g. their eq. (26) for rough Volterra signals) are triple integrals with incomplete-Beta and Gamma-ratio prefactors via Chakrabarti-George (1994) Abel inversion. The Riesz form $\kappa_{1-\gamma}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$ is more compact and is $O(N\log N)$ FFT-computable (Appendix D).
- **CRONE bridge (§8).** Not in FSS2022.

Conjecture 5.2.2 records the (currently open) direct kernel-matching argument that would explicitly show FSS2022's Gaussian-Volterra formula reducing to the bounded-interval Corollary 5.2 evaluated on the appropriate forecast curve.

### 6.4 Abi Jaber-Neuman / Abi Jaber-Neuman-Tuschmann / Abi Jaber et al.

The operator-resolvent FOC of Abi Jaber-Neuman (2022; v2 arXiv:2211.00447 Sep 2025) and Abi Jaber-Neuman-Tuschmann (2024, arXiv:2403.10273) is the encompassing framework that covers both the bounded-interval and half-line specializations of this paper, as well as multi-asset cross-impact (§7). Abi Jaber-Bondi-De Carvalho-Neuman-Tuschmann (2025, arXiv:2503.04323) extend to nonlinear price impact via stochastic Fredholm equations solved by iterative scheme with sum-of-exponentials approximation for the power-law numerics. Their FOCs are stochastic Fredholm equations of the second kind, solved by operator resolvents on matrix Volterra propagators; "fractional" appears in those works only as a descriptor of the kernel, not as the operator yielding the solution. Our explicit contribution relative to AJN/AJNT/ABDCNT:

- **The bulk theorem** (Theorem 4.1) gives the explicit closed-form symbol-inversion that their FOC reduces to in the scalar translation-invariant case.
- **Corollary 5.2** gives the explicit Söhngen-Tricomi form of their FOC on $[0,T]$.
- **§5.3** gives the explicit augmented-symbol Wiener-Hopf factorization of their FOC on $[0,\infty)$.
- **Proposition 5.3** gives the explicit $O(1/T)$ scaling that makes the bulk solution the long-horizon asymptotic.

Reading AJN/AJNT/ABDCNT as the abstract framework and this paper as the explicit specialization (with all the closed forms that the AJN/AJNT framework provides only implicitly) is the correct relationship.

### 6.5 Gârleanu-Pedersen pointer

Gârleanu-Pedersen (2013) solve the stationary trading problem with exponential impact kernel and running inventory-risk penalty $\tfrac12\gamma_{\rm risk}\sigma^2 X_t^2$. Specializing to the power-law kernel of this paper and keeping the GP risk penalty shifts the half-line symbol from $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ to $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \gamma_{\rm risk}\sigma^2/\xi^2$ (or $+ \eta + \gamma_{\rm risk}\sigma^2/\xi^2$ if both are present). The W-H factorization remains valid by Krein's theorem but is no longer a closed-form power of $\xi$, instead carrying a Blaschke-type factor encoding the holding-deviation mode. We leave the GP-with-power-law treatment to future work; see `outputs/unified-trading-execution.md` §2.5 for the AJNT (2024) framework, of which both the temporary-impact and inventory-penalty variants are corollaries.

### 6.6 Moreau-Muhle-Karbe-Soner small-impact asymptotic

Moreau-Muhle-Karbe-Soner (MMS, 2017) develop a small-impact asymptotic that unifies utility-maximizing portfolio choice with execution-style decay toward a frictionless target. Their setting is *orthogonal* to the bulk/boundary spine: MMS work in the small-$c$ limit where the propagator kernel is a perturbation of the frictionless problem, whereas this paper works in the *finite-$c$* regime where the kernel structure (power-law, exponential, etc.) is the leading-order phenomenon. The two views are complementary; MMS provides the bridge to the broader portfolio-choice literature.

### 6.7 Cartea-Jaimungal and Neuman-Voß

Cartea-Jaimungal (2016) and Neuman-Voß (2022) provide signal-adaptive baselines with exponential resilience. As noted in §6.2, these are the exponential-kernel analogues of our results, and inherit the *bulk-as-Markov-Riccati-resolvent* structure rather than the bulk-as-fractional-derivative structure. The bulk/boundary spine still applies; the bulk operator just is not a fractional derivative.

---

## 7. Multi-asset cross-impact: matrix fractional derivative

### 7.1 Setting

Let $u_t\in\mathbb{R}^d$ be a vector trading rate, $\alpha_t\in\mathbb{R}^d$ a vector signal, and the cross-impact kernel a matrix-valued power-law

$$ G(t) \;=\; t^{-\gamma}\,\mathbf{C}, \qquad \mathbf{C}\in\mathbb{R}^{d\times d}_{\mathrm{sym},+}, $$

with the same exponent $\gamma$ across asset pairs. The standing §2.5 no-short-sale assumption is understood componentwise; for long-short pairs trading or basket execution where shorting individual legs is intrinsic, the per-component constraint is dropped and the policy in Theorem 7.1 remains valid since the FOC is linear in $u$ and the vector budget constraint $\int_0^T u^*_t\,dt = X_0$ handles arbitrary signs of $X_0$.

### 7.2 Statement

**Theorem 7.1 (Matrix bulk theorem).** *Under linear impact, the vector bulk solution is*

$$ u^{\rm bulk}_t \;=\; \mathbf{C}^{-1}\,\kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\bigl[\bar{\boldsymbol\alpha}(t,\cdot) - \boldsymbol\lambda\bigr](t), $$

*where $\bar{\boldsymbol\alpha}(t,\cdot)$ is the vector forecast curve (componentwise as in §2.2) and $\boldsymbol\lambda$ is the vector Lagrange multiplier enforcing the vector budget constraint. Equivalently, diagonalizing $\mathbf{C} = Q\Lambda Q^\top$, the policy decouples into $d$ scalar bulk problems on the principal-component signals $Q^\top\bar{\boldsymbol\alpha}$.*

*On $[0,T]$, the bulk solution is augmented by the per-asset boundary correction $\mathcal{B}^{\rm vec}_{1-\gamma}(t)\in\mathbb{R}^d$ fixed by the vector boundary data, as in Corollary 5.2 applied componentwise in the principal-component basis.*

**Proof.** Componentwise application of Theorem 4.1 in the eigenbasis, then return to the original basis using $\mathbb{D}^{1-\gamma}$ commuting with the constant matrix $Q$. Full argument: Appendix C. ∎

The bulk/boundary spine extends transparently to matrix-valued kernels: the diagonalization picks out scalar bulk problems on principal-component signals, and each scalar bulk problem inherits its boundary correction in the same way. The fractional-derivative content is therefore inherited by each principal component independently.

---

## 8. Connection to fractional PID / CRONE control

### 8.1 CRONE in one paragraph

The Oustaloup CRONE controllers (Commande Robuste d'Ordre Non Entier, since the early 1990s; see Oustaloup 1991 and the survey arXiv:2512.12111 for a recent overview) are built on the principle that optimal control of systems with power-law memory uses fractional-order derivatives of the error signal. The CRONE-2 design in particular constructs a constant-phase open-loop template by absorbing the plant's fractional integrator into a fractional controller of complementary order. On the symbol side this is the factorization $M(\xi) = M_+(\xi)M_-(\xi)$; in CRONE this is the *controller-plant* split, and in our §5.3 it is the Wiener-Hopf *causal-anticausal* split.

### 8.2 The execution-CRONE correspondence

The bulk theorem (Theorem 4.1) is the execution-theoretic instance of the CRONE principle. Identifications:

| Engineering (CRONE-2) | Execution |
|---|---|
| Plant with fractional integrator | Propagator $G$ with power-law decay |
| Error signal | Conditionally expected alpha $\bar\alpha$ |
| Fractional controller order | Order $1-\gamma$ |
| Frequency-band template | Spectral content of forecast curve |
| Gain margin | Crossover scale $\xi_*(\eta)$ in §5.3 |
| CRONE second-generation factorization | W-H factorization $M = M_+ M_-$ in §5.3 |

The crossover scale $\xi_*(\eta)$ has a direct CRONE interpretation as the *gain-margin frequency* separating the long-memory and myopic regimes. The fractional-PID and CRONE traditions developed the symbol-side analysis of this scale in the 1990s; our §5.3 is the explicit execution-theoretic instance.

### 8.3 Note on terminology

"Fractional PID" (Podlubny 1999's PI$^\lambda$D$^\mu$ class) and "CRONE" (Oustaloup's robust-control family) are related but not identical. CRONE includes specific frequency-template robustness designs (CRONE-1/2/3) that go beyond a single fractional integrator or differentiator. We treat the two interchangeably where the specific design distinction does not bite; see the companion review `outputs/crone-control-optimal-trading.md` for the taxonomy.

### 8.4 Implications

- **Interpretability.** The fractional-derivative form gives a single scalar (the kernel exponent $\gamma$, with inverting order $1-\gamma$) that controls policy aggressiveness as a function of signal staleness.
- **Compute.** FFT-based fractional derivatives on $[0,T]$ run in $O(N\log N)$ versus $O(N^2)$ for Nyström.
- **Robustness diagnostics.** Mis-specification of $\gamma$ has a sharp analytic interpretation as the wrong order of differentiation, with cost degradation first-order in $\Delta\gamma$ via standard CRONE sensitivity analysis.
- **Baseline for learned policies.** RL and neural-SDE execution policies should be benchmarked against the bulk policy on identical data.

---

## 9. Empirical protocol and conclusion

### 9.1 Estimation, backtest, sensitivity (planned; not yet run)

The intended protocol:

1. **Estimation.** Fit $\gamma$ from response functions $R(\ell) := \mathbb{E}[\epsilon_t(p_{t+\ell}-p_t)]$ on TAQ-level data following Bouchaud-Gefen-Potters-Wyart (2004) on a held-out month; bootstrap CIs over 30-minute windows.
2. **Policy backtest.** Replay the bulk policy of Theorem 4.1 and the bounded-interval policy of Corollary 5.2 on a held-out test month with $(\hat c,\hat\gamma)$ and compare implementation shortfall vs. (i) Almgren-Chriss, (ii) TWAP, (iii) Nyström discretization of $(\star)$ at the same $(\hat c,\hat\gamma)$.
3. **Sensitivity / mis-specification stress.** Perturb $(\hat c,\hat\gamma)$ by $\pm 1\sigma_{\rm bootstrap}$ and measure cost degradation; test the CRONE-derived prediction (companion review §4.1) that degradation is first-order in $\Delta\gamma$ and zeroth-order in $\Delta c$.
4. **Crossover-scale check.** Estimate $\eta$ from realized spread/slippage cost; compute $\xi_*(\hat\eta)$; verify that high- and low-frequency policy components transition at $\xi_*$ as predicted by §5.3.
5. **$O(1/T)$ scaling check.** Vary $T$ across several decades on synthetic data with known $X_0$ and verify the Proposition 5.3 / Corollary 5.4 scaling of the boundary correction.

> **No experimental results are available yet.** Raw artifacts will be deposited in `experiments/fractional-execution/` once the protocol above has been executed.

### 9.2 Open problems

- Forde-recovery proof via direct kernel-matching on $[0,T]$ (Conjecture 5.2.2).
- Full Fredholm well-posedness proof on $[0,T]$ with the symmetric Riesz operator under the §4.1 PSD assumption.
- Quantitative finite-interval HLS bound supporting the Theorem 6.1 Neumann radius (Appendix A.4 hand-wave).
- GP-with-power-law W-H factorization (§6.5).
- Rough $\alpha$ extension (Marchaud regularization, Hölder exponent $\beta\le 1-\gamma$).
- Non-quadratic temporary impact (Curato-Gatheral-Lillo 2017 style).
- Numerical experiments (Appendix E plan).

### 9.3 Conclusion

Power-law propagator impact and fractional calculus are two sides of the same coin. **The optimal signal-adaptive execution rate is the sum of a translation-invariant bulk term and a domain-dependent boundary correction. The bulk term is the symmetric Riesz fractional derivative of order $1-\gamma$ of the conditional forecast curve, intrinsic to the kernel and independent of the domain. Boundary corrections are problem-specific homogeneous solutions of the bulk equation; on $[0,T]$ they are Söhngen-Tricomi modes that scale as $O(1/T)$ in the bulk region, on $[0,\infty)$ they are picked out by Wiener-Hopf factorization, and on $\mathbb{R}$ they vanish.** The unified spine puts GSS (2012), Forde et al. (2022), AJN (2022), AJNT (2024), GP (2013), MMS (2017), and the CRONE engineering tradition on a single axis on which only the boundary data change. Closed-form, FFT-computable, and serving as a benchmark against which all operator-theoretic, FBSDE, and learned policies can be measured.

---

## Appendices

The proofs below are written at the level of structural arguments, with technical regularity, measurability, and integrability conditions deferred to the indicated standard references. Items flagged ⚠️ + TODO require additional rigor before the appendices are submission-ready.

### Appendix A. Proofs

#### A.1 Proof of Theorem 4.1 (bulk on $\mathbb{R}$)

The bulk FOC $(\star_{\rm bulk})$ on $\mathbb{R}$ is the translation-invariant convolution equation $G*u = \bar\alpha - \lambda$. Take Fourier on $\mathbb{R}$:

$$ \hat G(\xi)\,\hat u(\xi) \;=\; \widehat{(\bar\alpha-\lambda)}(\xi). $$

The Fourier transform of the symmetric power-law kernel $G(|t|) = c|t|^{-\gamma}$ on $\mathbb{R}$ is

$$ \hat G(\xi) \;=\; 2c\int_0^\infty t^{-\gamma}\cos(\xi t)\,dt \;=\; 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)\,|\xi|^{\gamma-1}, $$

using the standard tabulated integral $\int_0^\infty t^{-\gamma}\cos(\xi t)\,dt = \Gamma(1-\gamma)\sin(\pi\gamma/2)|\xi|^{\gamma-1}$ for $\gamma\in(0,1)$ (Gradshteyn-Ryzhik 3.761.9; Stein 1970 §V.1; SKM 1993 §7.1). Write $c_\gamma := 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$. Then

$$ \hat u(\xi) \;=\; c_\gamma^{-1}\,|\xi|^{1-\gamma}\,\widehat{(\bar\alpha - \lambda)}(\xi). $$

The constant $\lambda$ contributes only at $\xi = 0$, which we ignore under the stationarity / zero-mean assumption. By the definition of $\mathbb{D}^{1-\gamma}$ via Fourier symbol (§3.2), the right-hand side is $c_\gamma^{-1}\,\widehat{\mathbb{D}^{1-\gamma}\bar\alpha}(\xi)$, so by Plancherel

$$ u(t) \;=\; c_\gamma^{-1}\,\mathbb{D}^{1-\gamma}\bar\alpha(t) \;=\; \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\bar\alpha(t). $$

Integrability of $|\xi|^{1-\gamma}\hat{\bar\alpha}(\xi)$ in $L^2$ follows from the assumed PSD bound; uniqueness in $L^2$ stationary solutions follows from the symbol being nonzero a.e. on $\mathbb{R}$. Adaptedness is from the forecast curve being $\mathcal{F}_t$-measurable (§4.2). ∎

#### A.2 Proof of Corollary 5.2 and Proposition 5.3

**Part 1: Corollary 5.2 via SKM 1993 §13.2 Thm 13.2.**

The bounded-interval FOC $(\star)$ is, after projection onto $\mathcal{F}_t$ (§4.2 of v1 / present §4.2), the deterministic-in-$\mathcal{F}_t$ Fredholm equation in the forecast curve:

$$ \int_0^T |s-v|^{-\gamma}\,v_t(v)\,dv \;=\; c^{-1}\bigl(\bar\alpha(t,s) - \lambda\bigr), \qquad s\in(0,T), $$

where $v_t(\cdot) := \mathbb{E}_t[u^*_\cdot]$ for $\cdot \ge t$ and $v_t(\cdot) = u^*_\cdot$ for $\cdot < t$.

SKM 1993 §13.2 Theorem 13.2 (the "airfoil equation" form) inverts the symmetric Abel equation $\int_0^T |s-v|^{-\gamma}\phi(v)\,dv = \psi(s)$ on $[0,T]$ as

$$ \phi(s) \;=\; \frac{\sin(\pi\nu)}{\pi^2}\,(s(T-s))^{-\nu}\,\frac{d}{ds}\!\int_0^T \frac{(v(T-v))^\nu}{v-s}\,\psi(v)\,dv \;+\; c_1\,(s(T-s))^{-\nu} \;+\; c_2\,\phi_2(s), $$

with $\nu = (1-\gamma)/2$, principal-value integral, and two-parameter homogeneous-solution space spanned by $\phi_1 = (s(T-s))^{-\nu}$ and the airfoil second mode $\phi_2$. The prefactor $\sin(\pi\nu)/\pi^2 = \cos(\pi\gamma/2)/\pi^2$ is the standard airfoil-equation constant (SKM 1993 §13.2 eq. 13.20); **this paper does not invoke Chakrabarti-George (1994), whose formula treats the asymmetric kernel $(s^\alpha - v^\alpha)^{-\beta}$, not the symmetric $|s-v|^{-\gamma}$ form needed here.**

Identifying the symmetric Riesz operator $\mathbb{D}^{1-\gamma}_{[0,T]}$ via §3.2 (its half-sum / Söhngen-Tricomi form) and using the kernel Fourier symbol $\hat G(\xi) = c_\gamma|\xi|^{\gamma-1}$ with $c_\gamma = 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$, the airfoil-equation prefactor and the kernel constant combine via the reflection identity $\Gamma(1-\gamma)\Gamma(\gamma) = \pi/\sin(\pi\gamma)$ and $\sin(\pi\gamma) = 2\sin(\pi\gamma/2)\cos(\pi\gamma/2)$ to give the overall normalization

$$ v_t(s) \;=\; \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}_{[0,T]}\!\bigl(\bar\alpha(t,s) - \lambda\bigr) \;+\; c_1\,\phi_1(s) \;+\; c_2\,\phi_2(s), $$

where the modes $\phi_1, \phi_2$ are those of §5.2.1. The reconciliation of the airfoil prefactor $\sin(\pi\nu)/\pi^2$ with the kernel-symbol constant $c_\gamma = 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$ uses the Euler reflection identity

$$ \Gamma(1-\gamma)\,\Gamma(\gamma) \;=\; \frac{\pi}{\sin(\pi\gamma)}, \qquad \sin(\pi\gamma) \;=\; 2\sin(\pi\gamma/2)\cos(\pi\gamma/2), $$

so $\sin(\pi\nu)/\pi^2 = \cos(\pi\gamma/2)/\pi^2$ combines with $c$ and $\Gamma(1-\gamma)$ to give the inverse $c_\gamma^{-1} = \kappa_{1-\gamma}$ as claimed. The two-parameter homogeneous family $\{c_1\phi_1 + c_2\phi_2\}$ is the boundary correction $\mathcal{B}_{1-\gamma}$ of §5.2.1; coefficients $c_1, c_2$ are fixed by the budget constraint $\int_0^T u^*_t\,dt = X_0$ and the terminal constraint $X_T = 0$, which together with the Lagrange-multiplier equation for $\lambda$ form a $3\times 3$ linear system. Setting $v_t(\cdot)|_{<t} = u^*$ identifies $v_t(t) = u^*_t$, completing Corollary 5.2.

*⚠️ hand-waved:* the $3\times 3$ system for $(c_1, c_2, \lambda)$ is non-singular for generic $\bar\alpha$ and $X_0$ (the homogeneous modes are linearly independent on $L^1(0,T)$); a full rank verification with explicit determinant formula is omitted. **TODO**: write out the system explicitly and verify non-singularity using the Beta-function identity of §5.2.5.

**Part 2: Proof of Proposition 5.3 ($|\mathcal{B}_{1-\gamma}| = O((X_0+M)/T)$ on bulk regions).**

Following the proof sketch of §5.2.5, we make the quantitative steps explicit.

*Step 1 (cumulative-trade constraint).* The budget condition $\int_0^T u^*_t\,dt = X_0$ with the decomposition $u^* = u^{\rm bulk} + \mathcal{B}_{1-\gamma}$ yields

$$ \int_0^T \mathcal{B}_{1-\gamma}(t)\,dt \;=\; X_0 \;-\; \int_0^T u^{\rm bulk}_t\,dt. \tag{A.2.1} $$

*Step 2 (bulk cumulative bound).* For a bounded stationary signal $\|\bar\alpha\|_\infty \le M$, the fractional derivative $\mathbb{D}^{1-\gamma}_{[0,T]}\bar\alpha$ is in $L^p(0,T)$ for $p < 2/(1-\gamma)$ with norm $\le C_p\,M$ (Hardy-Littlewood-Sobolev / SKM 1993 §13.4); integrating over $[0,T]$ and applying Hölder,

$$ \Bigl|\int_0^T u^{\rm bulk}_t\,dt\Bigr| \;\le\; \kappa_{1-\gamma}\,T^{1-1/p}\,C_p\,M \;=\; O(T^{1-1/p}\,M). $$

For $p$ slightly above $1$, this is $O(M)$ up to logarithmic factors; in any case sub-linear in $T$ for any fixed bounded $\bar\alpha$. (For OU signals the cumulative bulk is in fact $O(1)$ in $T$ in mean, by stationarity and the bounded-variance argument of GP 2013; we use the more conservative bound here.)

*Step 3 (coefficient scaling).* The second mode integrates to zero by symmetry: $\int_0^T \phi_2(t)\,dt = \int_0^T (T-2t)/2 \cdot (t(T-t))^{(\gamma-1)/2}\,dt = 0$ (odd integrand under $t\mapsto T-t$). So (A.2.1) becomes a constraint on $c_1$ alone:

$$ c_1 \int_0^T \phi_1(t)\,dt \;=\; X_0 \;-\; O(T^{1-1/p}\,M). $$

With $\int_0^T (t(T-t))^{(\gamma-1)/2}\,dt = T^\gamma\,B(\tfrac{\gamma+1}{2},\tfrac{\gamma+1}{2})$ via the substitution $t = sT$,

$$ |c_1| \;=\; \Theta\!\left(\frac{X_0 + M}{T^\gamma}\right) \qquad \text{as }T\to\infty. \tag{A.2.2} $$

The terminal-inventory condition $X_T = 0$ combined with the budget gives a second linear equation; standard linear algebra (the second-mode endpoint behavior $\phi_2(t) = (T-2t)/2 \cdot (t(T-t))^{(\gamma-1)/2}$ scales as $T \cdot T^{\gamma-1} = T^\gamma$ at endpoints) gives $|c_2| = \Theta((X_0+M)/T^\gamma)$ of the same order.

*Step 4 (pointwise bound on bulk region).* Evaluate $\mathcal{B}_{1-\gamma}$ at $t = sT$ with $s \in [\epsilon, 1-\epsilon]$:

\begin{align*}
\bigl|\mathcal{B}_{1-\gamma}(sT)\bigr| &\le |c_1|\cdot\bigl(s(1-s)T^2\bigr)^{(\gamma-1)/2} \;+\; |c_2|\cdot\bigl|\tfrac{(1-2s)T}{2}\bigr|\,\bigl(s(1-s)T^2\bigr)^{(\gamma-1)/2} \\
&\le \Theta\!\left(\frac{X_0+M}{T^\gamma}\right)\cdot T^{\gamma-1}\bigl(s(1-s)\bigr)^{(\gamma-1)/2}\,(1 + T \cdot T^0) \\
&= \Theta\!\left(\frac{X_0+M}{T}\right)\cdot\bigl(s(1-s)\bigr)^{(\gamma-1)/2}\,(1 + O(1)).
\end{align*}

The prefactor $(s(1-s))^{(\gamma-1)/2}$ is bounded by $(\epsilon(1-\epsilon))^{(\gamma-1)/2} =: C_\epsilon$ uniformly on $[\epsilon, 1-\epsilon]$. Hence

$$ \sup_{t\in[\epsilon T, (1-\epsilon)T]} \bigl|\mathcal{B}_{1-\gamma}(t)\bigr| \;\le\; C_\epsilon\cdot \Theta\!\left(\frac{X_0+M}{T}\right) \;=\; O\!\left(\frac{X_0+M}{T}\right). $$

*Step 5 (non-uniformity).* As $s\to 0^+$ or $s\to 1^-$, $(s(1-s))^{(\gamma-1)/2}\to\infty$ since $(\gamma-1)/2 < 0$. The bound is therefore **not** uniform on $[0,T]$; $\mathcal{B}_{1-\gamma}$ diverges integrably at both endpoints, consistent with the GSS U-shape. ∎

**Corollary 5.4 (Bulk as long-horizon asymptotic optimum).** *Immediate from Part 2:*

$$ \sup_{t\in[\epsilon T, (1-\epsilon)T]} \bigl|u^*_t - u^{\rm bulk}_t\bigr| \;=\; O\!\left(\frac{X_0+M}{T}\right) \qquad \text{as }T\to\infty. $$

*The bulk solution is the leading-order optimal trading rate on the bulk region, with subleading $O(1/T)$ correction.* ∎

*⚠️ hand-waved:* (i) the constant in Step 2 depends on the HLS-type estimate of $\mathbb{D}^{1-\gamma}_{[0,T]}$ on $L^\infty$, which we sketch rather than prove (the standard Riesz-potential estimate is on $\mathbb{R}$, not on a bounded interval; the bounded-interval version requires the weighted Sobolev estimates of SKM 1993 §13.4-13.5). (ii) the $\Theta$ bounds for $c_1, c_2$ assume the $3\times 3$ linear system of Part 1 is well-conditioned in $T$; explicit verification is **TODO**. (iii) the Step 2 bulk cumulative bound uses a conservative $O(M)$ estimate; for stationary OU signals one can sharpen to $O(\sigma\sqrt{T/\theta})$ in mean, but the $T\to\infty$ rate is unchanged.

#### A.3 Proof of Proposition 5.5 and Corollary 5.7 (Wiener-Hopf factorization)

**Part 1: Krein factorization for $\eta > 0$.**

The symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ on $\mathbb{R}\setminus\{0\}$ satisfies:

- *Positivity.* $M(\xi) \ge \eta > 0$ everywhere, with strict inequality away from $\xi = 0$ where $M(\xi) \to \infty$.
- *Bounded above at infinity.* $\lim_{|\xi|\to\infty} M(\xi) = \eta$ since $|\xi|^{\gamma-1}\to 0$ for $\gamma < 1$.
- *Logarithmic behavior.* $\log M(\xi) \to \log\eta$ as $|\xi|\to\infty$; $\log M(\xi) = (\gamma-1)\log|\xi| + \log c_\gamma + O(|\xi|^{1-\gamma}/\eta)$ as $\xi\to 0$.

The Krein integrability condition

$$ \int_\mathbb{R} \frac{\bigl|\log M(\xi)\bigr|}{1+\xi^2}\,d\xi \;<\; \infty $$

is verified by splitting $\mathbb{R} = [-1,1] \cup \{|\xi| > 1\}$:

- On $\{|\xi| > 1\}$: $|\log M| \le |\log\eta| + O(|\xi|^{\gamma-1})$, which against $(1+\xi^2)^{-1}$ is dominated by $|\log\eta|\cdot\arctan$ plus a convergent power-law tail.
- On $[-1, 1]\setminus\{0\}$: $|\log M| \le |\log c_\gamma| + |1-\gamma|\cdot|\log|\xi||$, integrable at $\xi = 0$ for any $\gamma \in (0,1)$ since $\int_0^1 |\log\xi|\,d\xi = 1 < \infty$.

Krein's theorem (Krein 1962; Noble 1958 §2.4) therefore yields a unique-up-to-sign factorization $M = M_+\cdot M_-$ with $M_\pm$ analytic and zero-free in the closed upper/lower half-planes. For general $\eta > 0$, $M_\pm$ are *not* closed-form powers of $\xi$; they admit the Cauchy-integral representation

$$ \log M_+(\xi) \;=\; \frac{1}{2\pi i}\int_\mathbb{R} \frac{\log M(s)}{s - \xi}\,ds, \qquad \mathrm{Im}\,\xi > 0, $$

and analogously for $M_-$ with $\mathrm{Im}\,\xi < 0$, by the standard Plemelj formula.

**Part 2: Closed-form factorization for $\eta = 0$.**

For $\eta = 0$ the symbol is $M(\xi) = c_\gamma|\xi|^{\gamma-1}$. Using

$$ |\xi|^{\gamma-1} \;=\; \bigl((-i\xi)\,(i\xi)\bigr)^{(\gamma-1)/2} \qquad (\xi\in\mathbb{R}\setminus\{0\}), $$

with the principal branch of $z^{(\gamma-1)/2}$ on $\mathbb{C}\setminus(-\infty, 0]$, we obtain the explicit factorization

$$ M_+(\xi) \;=\; c_\gamma^{1/2}\,(-i\xi)^{(\gamma-1)/2}, \qquad M_-(\xi) \;=\; c_\gamma^{1/2}\,(i\xi)^{(\gamma-1)/2}. $$

*Analyticity check.* The map $\xi \mapsto -i\xi$ sends the upper half-plane $\{\mathrm{Im}\,\xi > 0\}$ to the right half-plane $\{\mathrm{Re}\,z > 0\}$, on which the principal branch of $z^{(\gamma-1)/2}$ is analytic; analogously for $M_-$.

*Branch verification on $\mathbb{R}$.* For $\xi > 0$: $-i\xi = \xi e^{-i\pi/2}$ so $(-i\xi)^{(\gamma-1)/2} = \xi^{(\gamma-1)/2}e^{-i\pi(\gamma-1)/4}$; similarly $(i\xi)^{(\gamma-1)/2} = \xi^{(\gamma-1)/2}e^{i\pi(\gamma-1)/4}$. Their product is $\xi^{\gamma-1}$ with the phases cancelling. For $\xi < 0$: $-i\xi = |\xi|e^{i\pi/2}$, $i\xi = |\xi|e^{-i\pi/2}$, and the analogous cancellation gives $|\xi|^{\gamma-1}$. So $M_+(\xi)M_-(\xi) = c_\gamma|\xi|^{\gamma-1}$ on $\mathbb{R}\setminus\{0\}$ as required.

*Identification with one-sided Riemann-Liouville integrals.* By the standard correspondence $(-i\xi)^\beta = \widehat{D_+^\beta}(\xi)$ for $\beta \in (-1, 1)$ (SKM 1993 §7.1, taking $\beta < 0$ to mean the fractional integral of order $-\beta$), $M_+$ is the Fourier multiplier of the *causal* Riemann-Liouville integral $I_+^{(1-\gamma)/2}$ of order $(1-\gamma)/2$, and $M_-$ the analogous *anti-causal* integral $I_-^{(1-\gamma)/2}$. Their inverses $M_\pm^{-1}$ are the corresponding derivatives $D_\pm^{(1-\gamma)/2}$; $M_+^{-1}\Pi_+ M_-^{-1}$ acts as a causal Riesz fractional derivative of total order $1 - \gamma$ on $[0,\infty)$.

**Part 3: Half-line policy and crossover scale (Corollary 5.7).**

Given the factorization, the standard W-H solution recipe (Noble 1958 §2.4) for $(\star_{\rm WH})$ on $[0,\infty)$ is: project the inverted FOC to causal functions via

$$ \hat u^*(\xi) \;=\; M_+(\xi)^{-1}\,\Pi_+\!\Bigl[M_-(\xi)^{-1}\,\widehat{\bar\alpha^\infty(t,\cdot)}(\xi)\Bigr], $$

where $\Pi_+$ is the projection onto $\{f : f|_{(-\infty, 0)} = 0\}$ (equivalently, the upper-half-plane Hardy-space projection). This is Corollary 5.7.

The crossover scale $\xi_*(\eta) = (c_\gamma/\eta)^{1/(1-\gamma)}$ of §5.3.4 is the frequency at which $c_\gamma|\xi|^{\gamma-1} = \eta$. At $|\xi| \ll \xi_*$, $M(\xi) \approx c_\gamma|\xi|^{\gamma-1}$, $M_\pm \approx c_\gamma^{1/2}(\mp i\xi)^{(\gamma-1)/2}$, and the policy behaves like the $\eta = 0$ bulk limit (fractional derivative of order $1-\gamma$). At $|\xi| \gg \xi_*$, $M(\xi) \approx \eta$, $M_\pm \approx \sqrt{\eta}$, and the policy becomes $\hat u^*(\xi) \approx \eta^{-1}\,\Pi_+\widehat{\bar\alpha^\infty}(\xi)$ - direct signal-following.

**Part 4: AJNT framing caveat.**

The operator-resolvent calculus of Abi Jaber-Neuman-Tuschmann (2024, arXiv:2403.10273) solves the general (matrix-valued, non-translation-invariant, finite-horizon) propagator FOC by inverting a stochastic Fredholm operator of the second kind. Our Fourier-multiplier factorization reduces to a special case of the AJNT resolvent only under all of the §5.3 assumptions: (a) scalar; (b) power-law kernel; (c) constant temporary impact; (d) stationary signal; (e) half-line. Outside this regime the AJNT resolvent need not be a Fourier multiplier and the W-H factorization need not be closed-form. ∎

*⚠️ hand-waved:* (i) the projection $\Pi_+$ requires $M_-^{-1}\widehat{\bar\alpha^\infty}(\cdot)$ to be in $L^2$ near $\xi = 0$ - for $\eta = 0$, $M_-^{-1}$ grows as $|\xi|^{(1-\gamma)/2}$ at zero, requiring the forecast PSD to vanish faster than $|\xi|^{\gamma-1}$ as $\xi\to 0$; for $\eta > 0$, $M_-^{-1}$ is bounded and the issue does not arise. **TODO**: explicit $L^2$-mapping bound. (ii) the Krein integrability constants in Part 1 are not made quantitative; standard but worth checking against AJN (2022).

### Appendix B. Mittag-Leffler resolvent on $[0,T]$ (Theorem 6.1)

#### B.1 Neumann series for the second-kind Fredholm equation

The second-kind equation $(\star\star)$, after the projection step of §4.2, reads

$$ 2\eta\,v_t(s) + c\!\int_0^T |s-v|^{-\gamma}\,v_t(v)\,dv \;=\; f_t(s), \qquad f_t(s) := \bar\alpha(t,s)-\lambda. \tag{B.1} $$

Write $\mathcal{G}$ for the integral operator (kernel $|s-v|^{-\gamma}$, so $c\mathcal{G}$ is the operator on the LHS) and divide by $2\eta$: $(I + (2\eta)^{-1} c\,\mathcal{G})\,v_t = (2\eta)^{-1} f_t$. For $\|(2\eta)^{-1} c\,\mathcal{G}\|_{L^2(0,T)} < 1$ the Neumann series

$$ v_t \;=\; (2\eta)^{-1}\sum_{n=0}^\infty (-1)^n\,\bigl((2\eta)^{-1}c\bigr)^{n}\,\mathcal{G}^n\,f_t $$

converges in $L^2(0,T)$. The operator norm of $\mathcal{G}$ on $(0,T)$ is bounded by the bounded-interval weighted Sobolev estimates of SKM 1993 §13.4-13.5; the whole-line Riesz-potential bound of SKM 1993 §8.3 is strictly larger and serves as a coarse fallback. *⚠️ hand-waved: an explicit finite-interval HLS-restricted constant is required to make the Neumann radius effective. TODO.*

#### B.2 Mittag-Leffler identification of iterated power-law convolutions

The iterated symmetric power-law kernel $|t|^{-\gamma} *_{[0,T]} \cdots *_{[0,T]} |t|^{-\gamma}$ ($n$-fold) coincides on the half-line with the one-sided Riemann-Liouville iterate $(t^{-\gamma})^{*n}$, whose Laplace transform is $[\Gamma(1-\gamma)\, p^{\gamma-1}]^n$ by the convolution rule. Inverse Laplace gives

$$ (t^{-\gamma})^{*n}(t) \;=\; \frac{\Gamma(1-\gamma)^n}{\Gamma\bigl(n(1-\gamma)\bigr)}\, t^{n(1-\gamma)-1}. $$

Substituting into the Neumann series of B.1 (writing $a := c\Gamma(1-\gamma)/(2\eta)$) and summing the $n\ge 1$ tail,

$$ \sum_{n\ge 1} (-1)^n\,\bigl((2\eta)^{-1}c\bigr)^n\,(t^{-\gamma})^{*n}(t) \;=\; -\,\frac{c\,\Gamma(1-\gamma)}{2\eta}\,|t|^{-\gamma}\, E_{1-\gamma,\,1-\gamma}\!\bigl(-a\,|t|^{1-\gamma}\bigr), $$

using $\sum_{k\ge 0} z^k/\Gamma((k+1)(1-\gamma)) = E_{1-\gamma,1-\gamma}(z)$. Multiplying by $(2\eta)^{-1}$ and adding the $n=0$ delta term,

$$ R_{\gamma,\eta}(t,s) \;=\; \frac{1}{2\eta}\,\delta(t-s) \;-\; \frac{c\,\Gamma(1-\gamma)}{(2\eta)^2}\,|t-s|^{-\gamma}\, E_{1-\gamma,\,1-\gamma}\!\bigl(-a\,|t-s|^{1-\gamma}\bigr), $$

which is the kernel $R_{\gamma,\eta}$ of Theorem 6.1, with prefactor $c\,\Gamma(1-\gamma)$ on the non-delta term made explicit. The $c\to 0$ limit gives $R_{\gamma,\eta} \to (2\eta)^{-1}\delta$ (Almgren-Chriss myopic); $\eta\to 0$ recovers Corollary 5.2 with $\kappa_{1-\gamma} = c_\gamma^{-1}$.

*⚠️ hand-waved:* the symmetric two-sided convolution on the finite interval is replaced here by a half-line convolution to compute the iterated kernel; boundary effects on $[0,T]$ enter through $\mathcal{B}_{1-\gamma}$ as in A.2 and modify $R_{\gamma,\eta}$ near $s,t\in\{0,T\}$. By the Prop 5.3 $O(1/T)$ bound, the Mittag-Leffler identification is exact on the bulk region $[\epsilon T,(1-\epsilon)T]$ up to $O(1/T)$ corrections. **TODO**: derive the precise endpoint-correction tail bound, or restate Theorem 6.1 explicitly as "on the bulk region of $[0,T]$."

#### B.3 Limits

- $\eta\to\infty$: keep only the $n=0$ term of B.1 - Almgren-Chriss myopic.
- $\eta\downarrow 0$: delta term singular, resolvent reduces to inverse of $\mathcal{G}$ → Corollary 5.2 via A.2.
- $\gamma\to 1^-$: kernel $|t|^{-\gamma}\to\delta'$-like singularity; Mittag-Leffler index $1-\gamma\to 0$; does *not* recover Obizhaeva-Wang exponential resilience (which corresponds to $G(t) = \rho e^{-\rho t}$, not a $\gamma$-limit of $t^{-\gamma}$). See §6.2 for the explicit distinction.

### Appendix C. Proof of Theorem 7.1 (matrix fractional derivative)

*Note on notation:* in this appendix $\lambda_i$ denotes the $i$-th eigenvalue of the cross-impact matrix $\mathbf{C}$, while $\tilde\lambda_i$ denotes the $i$-th component of the rotated Lagrange-multiplier vector (collision with the scalar $\lambda$ of §2.4 is unavoidable; tildes mark rotated coordinates).

Let $\mathbf{C}\in\mathbb{R}^{d\times d}_{\mathrm{sym},+}$ with $\mathbf{C} = Q\Lambda Q^\top$, $\Lambda = \mathrm{diag}(\lambda_1,\dots,\lambda_d)$, $\lambda_i>0$. Change variables $\tilde u_t := Q^\top u_t$, $\tilde\alpha_t := Q^\top \alpha_t$. The vector cost functional decouples into $d$ scalar cost functionals

$$ \tilde{\mathcal{C}}_i(\tilde u_i) \;=\; \tfrac{1}{2}\lambda_i\,\mathbb{E}\!\!\int\!\!\int |t-v|^{-\gamma}\tilde u_{i,t}\tilde u_{i,v}\,dt\,dv \;-\; \mathbb{E}\!\!\int \tilde u_{i,t}\,\tilde\alpha_{i,t}\,dt, $$

each solved by Theorem 4.1 / Corollary 5.2 component-wise with effective impact constant $c_i = \lambda_i c$:

$$ \tilde u^*_{i,t} \;=\; \frac{1}{\lambda_i}\,\kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}_{[0,T]}\!\bigl[s\mapsto \widetilde{\bar\alpha}_i(t,s) - \tilde\lambda_i\bigr](t) \;+\; \mathcal{B}_{1-\gamma,i}(t). $$

Stacking and returning to the original basis $u^*_t = Q\tilde u^*_t$:

$$ u^*_t \;=\; \mathbf{C}^{-1}\, Q\,\bigl(\kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}_{[0,T]}\bigr)\,Q^\top\bigl[\bar{\boldsymbol\alpha}(t,\cdot) - \boldsymbol\lambda\bigr](t) \;+\; \mathcal{B}^{\mathrm{vec}}_{1-\gamma}(t), $$

which is Theorem 7.1: $\mathbb{D}^{1-\gamma}_{[0,T]}$ commutes with constant matrices $Q, Q^\top$ (acts on the time variable only), and $Q\Lambda^{-1}Q^\top = \mathbf{C}^{-1}$. ∎

*⚠️ hand-waved:* the budget constraints in the eigenbasis are $\int_0^T \tilde u^*_{i,t}\,dt = (Q^\top X_0)_i$, which fixes the $d$ Lagrange multipliers $\tilde\lambda_i$. Translating back gives $\boldsymbol\lambda = Q\tilde{\boldsymbol\lambda}$. The Prop 5.3 $O(1/T)$ bound applies coordinate-wise on the bulk region.

### Appendix D. FFT-based discretization of $\mathbb{D}^{1-\gamma}_{[0,T]}$

The Söhngen-Tricomi form of §3.2,

$$ \mathbb{D}^{1-\gamma}_{[0,T]} f(s) \;=\; \frac{\sin(\pi\nu)}{\pi^2}\,(s(T-s))^{-\nu}\,\frac{d}{ds}\!\int_0^T \frac{(v(T-v))^\nu}{v-s}\,f(v)\,dv, $$

admits an FFT-based discretization. On a uniform grid $t_k = kh$, $k = 0,\dots,N$, $h = T/N$:

1. Pre-multiply $f$ by the right weight: $\tilde f(t_j) := (t_j(T-t_j))^\nu f(t_j)$.
2. Evaluate the principal-value Hilbert transform $H\tilde f(s) := \mathrm{p.v.}\int_0^T (v-s)^{-1}\tilde f(v)\,dv$ on the grid via Toeplitz matrix-vector product (FFT, $O(N\log N)$); the principal-value diagonal entry is regularized by the standard endpoint formula (Bertero-Boccacci 1998).
3. Apply $d/ds$ by centred finite difference, then multiply by $(s(T-s))^{-\nu}\sin(\pi\nu)/\pi^2$.

For the boundary term $\mathcal{B}_{1-\gamma}$, evaluate the closed form pointwise on the grid; the coefficients $c_1, c_2$ are fixed by the budget and terminal-inventory equations (see Appendix A.2 Part 1).

**Alternative: symmetric Grünwald-Letnikov stencil on $\mathbb{R}$.** The half-sum operator $\tfrac12(D^{1-\gamma}_+ + D^{1-\gamma}_-)$ on $\mathbb{R}$ has the well-known symmetric Grünwald-Letnikov stencil $h^{-(1-\gamma)}\sum_j w^{(1-\gamma)}_{|k-j|} f(t_j)$ with $w^{(1-\gamma)}_m = (-1)^m\binom{1-\gamma}{m}$ (Çelik-Duman 2012; Podlubny 1999 §7). Because §3.2 defines $\mathbb{D}^{1-\gamma}$ on $\mathbb{R}$ as exactly $(2\sin(\pi\gamma/2))^{-1}$ times this half-sum, the unweighted symmetric Grünwald stencil discretizes $\mathbb{D}^{1-\gamma}$ on $\mathbb{R}$ correctly *up to the $1/(2\sin(\pi\gamma/2))$ Riesz-normalization rescaling.* On $[0,T]$ one must further (a) apply the rescaling, (b) add the boundary correction $\mathcal{B}_{1-\gamma}$ to capture the $(s(T-s))^{\mp\nu}$ endpoint weights that the unweighted stencil does not see. Without this correction the discretization converges to the wrong operator near the endpoints.

A streaming realization uses the Oustaloup recursive approximation (Oustaloup et al. 2000); see `outputs/crone-control-optimal-trading.md` §4.2.

*⚠️ hand-waved:* (i) the precise quadrature for the principal-value Hilbert transform with polynomial weights needs to be specified (SKM 1993 §13.4 sketches the spectral approach via Jacobi polynomials, the production-grade alternative to the Toeplitz scheme above with spectral accuracy on $[0,T]$); (ii) the boundary correction for the symmetric Grünwald stencil is folded into the $\mathcal{B}_{1-\gamma}$ degree of freedom in practice, but a quantitative endpoint-accuracy bound requires the WSGD shifted variant of Tian-Zhou-Deng (2015) / Çelik-Duman (2012). **TODO**: benchmark Jacobi-spectral and WSGD variants on the Corollary 5.2.1 U-shape and report endpoint accuracy.

### Appendix E. Empirical estimation of $\gamma$ and sensitivity analysis

*Pending data.* The intended protocol:

1. **Estimation.** Fit $\gamma$ from response functions $R(\ell) := \mathbb{E}[\epsilon_t(p_{t+\ell}-p_t)]$ on TAQ-level data following Bouchaud-Gefen-Potters-Wyart (2004) on a held-out month; bootstrap CIs over 30-minute windows.
2. **Policy backtest.** Replay the bulk policy of Theorem 4.1 (restricted to $[0,T]$ via Corollary 5.2, with boundary correction) on the held-out test month with $(\hat c, \hat\gamma)$; compare implementation shortfall vs. (i) Almgren-Chriss, (ii) TWAP, (iii) Nyström discretization of $(\star)$ at the same $(\hat c,\hat\gamma)$, (iv) the bulk-only solution (no boundary correction) to test the Cor 5.4 $O(1/T)$ scaling.
3. **Sensitivity / mis-specification stress.** Perturb $(\hat c,\hat\gamma)$ by $\pm 1\sigma_{\mathrm{bootstrap}}$ and measure cost degradation; test the CRONE-derived prediction (see `outputs/crone-control-optimal-trading.md` §4.1) that degradation is first-order in $\Delta\gamma$ and zeroth-order in $\Delta c$.
4. **Bulk vs boundary diagnostic.** Plot $u^* - u^{\rm bulk}$ on the bulk region $[\epsilon T,(1-\epsilon)T]$ as a function of $T$, expect $O(1/T)$ scaling per Cor 5.4.

> **No experimental results are available yet.** Raw artifacts will be deposited in `experiments/fractional-execution/` once the protocol above has been executed.

---

## References *(condensed; full bibliography in companion `.bib`)*

- Abi Jaber, E. *Lifting the Heston model.* Quant. Finance 19(12), 1995-2013, 2019. https://doi.org/10.1080/14697688.2019.1615113
- Abi Jaber, E.; El Euch, O. *Multifactor approximation of rough volatility models.* SIAM J. Financial Math. 10(2), 309-349, 2019. https://doi.org/10.1137/18M1170236
- Abi Jaber, E.; Bondi, A.; De Carvalho, N.; Neuman, E.; Tuschmann, S. *Fredholm Approach to Nonlinear Propagator Models.* arXiv:2503.04323, 2025.
- Abi Jaber, E.; Neuman, E. *Optimal Liquidation with Signals: the General Propagator Case.* Math. Finance, to appear; arXiv:2211.00447 (Nov 2022). https://doi.org/10.1111/mafi.12465
- Abi Jaber, E.; Neuman, E.; Tuschmann, S. *Optimal Portfolio Choice with Cross-Impact Propagators.* arXiv:2403.10273, March 2024.
- Almgren, R.; Chriss, N. *Optimal execution of portfolio transactions.* J. Risk 3(2), 5-39, 2000/2001. https://doi.org/10.21314/JOR.2001.041
- Bensoussan, A. *Stochastic Control of Partially Observable Systems.* Cambridge University Press, 1992.
- Bouchaud, J.-P.; Gefen, Y.; Potters, M.; Wyart, M. *Fluctuations and response in financial markets: the subtle nature of 'random' price changes.* Quant. Finance 4(2), 176-190, 2004. https://doi.org/10.1080/14697680400000022
- Cartea, Á.; Jaimungal, S. *Incorporating order-flow into optimal execution.* Math. Financ. Econ. 10(3), 339-364, 2016. https://doi.org/10.1007/s11579-016-0162-z
- Cartea, Á.; Jaimungal, S.; Penalva, J. *Algorithmic and High-Frequency Trading.* Cambridge University Press, 2015.
- Çelik, C.; Duman, M. *Crank-Nicolson method for the fractional diffusion equation with the Riesz fractional derivative.* J. Comput. Phys. 231, 1743-1750, 2012. https://doi.org/10.1016/j.jcp.2011.11.008
- Curato, G.; Gatheral, J.; Lillo, F. *Optimal execution with non-linear transient market impact.* Quant. Finance 17(1), 41-54, 2017. arXiv:1412.4839.
- Forde, M.; Sánchez-Betancourt, L.; Smith, B. *Optimal trade execution for Gaussian signals with power-law resilience.* Quant. Finance 22(3), 585-596, 2022. https://doi.org/10.1080/14697688.2021.1950919
- Gârleanu, N.; Pedersen, L. H. *Dynamic Trading with Predictable Returns and Transaction Costs.* J. Finance 68(6), 2309-2340, 2013. https://doi.org/10.1111/jofi.12080
- Gatheral, J. *No-dynamic-arbitrage and market impact.* Quant. Finance 10(7), 749-759, 2010. https://doi.org/10.1080/14697680903373692
- Gatheral, J.; Schied, A.; Slynko, A. *Transient linear price impact and Fredholm integral equations.* Math. Finance 22(3), 445-474, 2012. https://doi.org/10.1111/j.1467-9965.2011.00478.x
- Jusselin, P.; Rosenbaum, M. *No-arbitrage implies power-law market impact and rough volatility.* Math. Finance 30(4), 1309-1336, 2020. arXiv:1805.07134. https://doi.org/10.1111/mafi.12245
- Krein, M. G. *Integral equations on a half-line with kernel depending upon the difference of the arguments.* Amer. Math. Soc. Transl. (2) 22, 163-288, 1962 (English translation of the 1958 Russian original).
- Kwakernaak, H.; Sivan, R. *Linear Optimal Control Systems.* Wiley-Interscience, 1972.
- Moreau, L.; Muhle-Karbe, J.; Soner, H. M. *Trading with Small Price Impact.* Math. Finance 27(2), 350-400, 2017. arXiv:1402.5304. https://doi.org/10.1111/mafi.12098
- Neuman, E.; Voß, M. *Optimal Signal-Adaptive Trading with Temporary and Transient Price Impact.* SIAM J. Financial Math. 13(2), 551-575, 2022. arXiv:2002.09549.
- Noble, B. *Methods Based on the Wiener-Hopf Technique for the Solution of Partial Differential Equations.* Pergamon Press, 1958.
- Novokshenov, V. Yu. *Convolution equations on a finite segment and factorization of elliptic matrices.* Mat. Zametki 97(3), 442-454, 2015. https://doi.org/10.4213/mzm10453
- Obizhaeva, A. A.; Wang, J. *Optimal trading strategy and supply/demand dynamics.* J. Financial Markets 16(1), 1-32, 2013. https://doi.org/10.1016/j.finmar.2012.09.001
- Oustaloup, A. *La commande CRONE.* Hermès, Paris, 1991.
- Oustaloup, A.; Levron, F.; Mathieu, B.; Nanot, F. M. *Frequency-band complex noninteger differentiator: characterization and synthesis.* IEEE Trans. Circuits Syst. I 47(1), 25-39, 2000. https://doi.org/10.1109/81.817385
- Podlubny, I. *Fractional Differential Equations.* Academic Press, 1999.
- Samko, S. G.; Kilbas, A. A.; Marichev, O. I. *Fractional Integrals and Derivatives: Theory and Applications.* Gordon and Breach, 1993.
- Söhngen, H. *Die Lösungen der Integralgleichung $g(x) = (1/2\pi)\int_{-a}^a f(\xi)/(x-\xi)\,d\xi$ und deren Anwendung in der Tragflügeltheorie.* Math. Z. 45, 245-264, 1939.
- Stein, E. M. *Singular Integrals and Differentiability Properties of Functions.* Princeton University Press, 1970.
- Tian, W.; Zhou, H.; Deng, W. *A class of second order difference approximations for solving space fractional diffusion equations.* Math. Comp. 84, 1703-1727, 2015. https://doi.org/10.1090/S0025-5718-2015-02917-2
- Tricomi, F. G. *Integral Equations.* Interscience, New York, 1957.
- Webster, K. T. *Handbook of Price Impact Modeling.* Chapman & Hall/CRC, 2023.
- *Fractional Calculus in Optimal Control and Game Theory: A Survey.* arXiv:2512.12111, 2025.

*Chakrabarti-George (1994) - removed as primary reference for Appendix A.2 per decision D5 = A; their formula treats the asymmetric kernel $(s^\alpha - v^\alpha)^{-\beta}$, not the symmetric $|s-v|^{-\gamma}$ needed here. Retained in v1 archive bibliography for historical reference only.*

---

## Changelog - v2 rewrite (2026-06-27)

Full end-to-end restructure around the **bulk/boundary spine**, per the user-approved plan `papers/.plans/fractional-derivative-optimal-execution.v2-restructure.md`. The v1 paper is archived at `papers/archive/fractional-derivative-optimal-execution.v1.md`; see also the migration note `papers/fractional-derivative-optimal-execution.v1-to-v2.md`.

**Spine change.** Reframed the entire paper around the universal decomposition $u^* = u^{\rm bulk} + \mathcal{B}$. The fractional derivative is the bulk inverse of the translation-invariant propagator symbol, not a property of either the bounded-interval or half-line problem in particular. Wiener-Hopf factorization is a *tool* for computing $\mathcal{B}$ on the half-line, demoted from its own §5.4 (v1) to a subsection §5.3 (v2). The Söhngen-Tricomi inversion is the analogous tool on $[0,T]$.

**Theorem hierarchy.**
- Theorem 4.1 (v2): bulk theorem stated on $\mathbb{R}$ by Fourier symbol inversion. The single load-bearing main result.
- Corollary 5.2 (v2): bounded-interval execution on $[0,T]$. *This is the v1 Theorem 4.1, demoted to a corollary.*
- Proposition 5.3 (v2, **new**): $|\mathcal{B}_{1-\gamma}(t)| = O((X_0+M)/T)$ uniformly on bulk regions $[\epsilon T, (1-\epsilon)T]$. Quantitative justification of the bulk-as-asymptotic-optimum picture.
- Corollary 5.4 (v2, **new**): $u^* = u^{\rm bulk} + O(1/T)$ on bulk regions; bulk solution is the long-horizon optimum.
- Proposition 5.5 / Corollary 5.7 (v2): half-line policy via Wiener-Hopf factorization for general $\eta \ge 0$, with closed-form for $\eta = 0$ recovering the bulk theorem restricted to $[0,\infty)$.
- Theorem 6.1 (v2): Mittag-Leffler resolvent on $[0,T]$ with temporary impact $\eta > 0$ - the second-kind Fredholm regularization. *Was v1 Theorem 5.1.*
- Theorem 7.1 (v2): matrix fractional derivative for multi-asset cross-impact, by eigenbasis diagonalization of the bulk theorem. *Was v1 Theorem 6.1.*

**Decision D5 = A applied.** Riesz normalization corrected throughout: $\kappa_{1-\gamma} = 1/c_\gamma = (2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2))^{-1}$. Appendix A.2 rewritten to cite SKM 1993 §13.2 Theorem 13.2 (airfoil-equation form). Chakrabarti-George (1994) dropped as the primary reference; their formula treats the asymmetric kernel, not the symmetric form needed.

**Decision D6 = A′ applied.** §5.3 (was §5.4) reformulated with general temporary impact $\tfrac12\eta u_t^2$, $\eta \ge 0$. Symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ has crossover scale $\xi_*(\eta) = (c_\gamma/\eta)^{1/(1-\gamma)}$ separating the long-memory fractional regime ($|\xi| \ll \xi_*$) from the myopic signal-following regime ($|\xi| \gg \xi_*$). $\eta \to 0$ limit recovers the bulk theorem restricted to $[0,\infty)$, making §5.3 the half-line analogue of §4. Gârleanu-Pedersen running risk penalty no longer used as regularizer; pointer to GP retained in §6.5.

**Bibliography polish.** Söhngen (1939), Çelik-Duman (2012), Podlubny (1999), Stein (1970), Cartea-Jaimungal-Penalva (2015), Webster (2023) added; Bouchaud et al. corrected to 2004; Krein 1962 noted as English translation of 1958 Russian original.

**Economic gloss & framing.** §5.2.3 added: U-shape via cheap-trading windows at $t \to 0^+$ and $t \to T^-$ (resolves Round 2 finance F1). §5.3.4 AJNT framing caveat (resolves Round 2 finance M2).

**Carried over from v1 Round 1 changelog (historical record).** D1 = B (kernel exponent $\gamma$, derivative order $1-\gamma$). D3 = A removal of $\mathbb{E}_t[\alpha_T]$. D4 = A downgrade of Forde recovery to conjectural (now Conjecture 5.2.2). M4 notation, M5 adaptedness, F2 boundary exponent, F3 Mittag-Leffler prefactor, M1 contribution positioning vs AJN/AJNT, M2 standing assumptions in §2 - all preserved in v2 under the new spine.

**Deferred in v2 (open).**
- Math: full Fredholm well-posedness proof; explicit $3\times 3$ system non-singularity verification for $(c_1, c_2, \lambda)$; HLS-restricted bound on bounded interval; Krein integrability quantitative constants; $L^2$ admissibility for the half-line projection $\Pi_+$.
- Recovery: Forde-Sánchez-Betancourt-Smith (2022) kernel-matching proof (Conjecture 5.2.2).
- Numerical: Jacobi-spectral vs WSGD endpoint accuracy benchmark; Cor 5.4 $O(1/T)$ scaling diagnostic.
- Empirical: estimation, backtest, sensitivity (App E protocol; no data yet).
- Sharper Prop 5.3 Step 2 constant: OU-specific $O(\sigma\sqrt{T/\theta})$.
