# Optimal Execution as a Fractional Derivative of the Alpha Signal

**Status:** Working paper.  **Date:** 2026-06-30.  **Authors:** TBD

---

## Abstract

Under a Bouchaud–Gatheral propagator with power-law kernel $G(t)=ct^{-\gamma}$, $\gamma\in(0,1)$, the optimal signal-adaptive trading rate decomposes as $u^*_t = u^{\rm bulk}_t + \mathcal{B}(t)$. The bulk term — intrinsic to the kernel, independent of domain — is an adapted trading rate whose form is the filtration Wiener–Hopf ansatz:
$$u^{\rm bulk}_t = \kappa_{1-\gamma}\,(D_+^\beta\zeta)(t),\qquad \zeta_s := \bigl(D_-^\beta\bar\alpha(s,\cdot)\bigr)(s),\quad \beta:=\tfrac{1-\gamma}{2},$$
with $\kappa_{1-\gamma}=[2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)]^{-1}$ and $\bar\alpha(t,\cdot)$ the conditional forecast curve. The boundary correction $\mathcal{B}$ lives in the kernel of the bulk operator and is chosen to match domain boundary data; it is $O(T^{\gamma-1})$ in the bulk region of $[0,T]$ for fixed inventory and bounded signal. Three specializations — whole line ($\mathcal{B}=0$), bounded interval (Söhngen–Tricomi modes), half-line (augmented-symbol Wiener–Hopf) — exhaust the cases of practical interest. The framework unifies Gatheral–Schied–Slynko (2012), Forde–Sánchez-Betancourt–Smith (2022), and Abi Jaber–Neuman (2022) on a single axis.

---

## 1. Introduction

Let $G(t)=ct^{-\gamma}$ be a power-law market-impact kernel. The first-order condition of any signal-adaptive execution problem is a linear integral equation in the trading rate against $G$. The Fourier symbol of $G$ on $\mathbb{R}$ is $c_\gamma|\xi|^{\gamma-1}$; inverting it produces a fractional derivative of order $1-\gamma$. All problem-specific structure — terminal inventory, finite horizon, temporary impact — enters only through *boundary corrections* that lie in the kernel of this bulk operator. This bulk/boundary decomposition is the organizing principle of the paper.

**Closest prior work.** Forde–Sánchez-Betancourt–Smith (2022; FSS2022) solve the bounded-interval case with the identical kernel and Gaussian signals. Their proof factorizes the Fredholm operator as $T=B^{-1}I_\nu B$ with $I_\nu$ the Riemann–Liouville operator of order $\beta=(1-\gamma)/2$, which is the operator-language content of our Theorem 1. Our contributions are: (i) the whole-line statement free of bounded-interval weight conjugation; (ii) explicit identification of the forecast curve $\bar\alpha(t,\cdot)$ as the operated-on object, clarifying adaptedness; (iii) Lemma 1 (optional projection of the anticausal half-derivative), which bridges the stochastic and deterministic half of the argument; (iv) the $O(T^{\gamma-1})$ boundary scaling (Proposition 1); (v) the multi-asset extension. Gatheral–Schied–Slynko (2012; GSS) solve the zero-signal Abel equation on $[0,T]$ (recovered as Corollary 2 below). Abi Jaber–Neuman (2022; AJN) and Abi Jaber–Neuman–Tuschmann (2024; AJNT) give the encompassing operator-resolvent framework; the closed forms here are the scalar power-law specialization.

---

## 2. Setting

**Propagator model.** Fix a probability space with filtration $(\mathcal{F}_t)$. An admissible control $u\in L^2_{\rm adap}(\mathbb{T})$ trades at rate $u_t$ (positive = selling). Here $L^2_{\rm adap}(\mathbb{T}):=\{u:\Omega\times\mathbb{T}\to\mathbb{R}: u$ is $\mathcal{F}_t$-progressive, $\mathbb{E}\int_\mathbb{T} u_t^2\,dt<\infty\}$. The cost functional is
$$\mathcal{C}(u) = \tfrac{1}{2}\mathbb{E}\iint G(|t-v|)u_tu_v\,dt\,dv - \mathbb{E}\int u_t\alpha_t\,dt + \lambda\!\int u_t\,dt,$$
with $G(t)=ct^{-\gamma}$, $c>0$, $\gamma\in(0,1)$, and $\lambda$ a Lagrange multiplier for the budget constraint $\int u_t\,dt=X_0$. The symmetric quadratic form $\tfrac12 G(|t-v|)$ arises from the causal propagator cost $\int u_t\int_{s\le t}G(t-s)u_s\,ds\,dt$ since the half-planes $\{s\le t\}$ and $\{s\ge t\}$ contribute equally by bilinear symmetry of $u_tu_s$; their average is $\tfrac12 G(|t-v|)$.

**Forecast curve.** The $\mathcal{F}_t$-conditional forecast of $\alpha$ is
$$\bar\alpha(t,s):=\begin{cases}\alpha_s,&s\le t,\\\mathbb{E}_t[\alpha_s],&s>t.\end{cases}$$

**Forecast tower lemma.** *For $t\le v$ and all $s$: $\mathbb{E}_t[\bar\alpha(v,s)]=\bar\alpha(t,s).$* (Proof: tower property of conditional expectation, splitting on $s\le t$, $t<s\le v$, $s>v$.)

**Conditioned first-order conditions.** Testing $\delta\mathcal{C}=0$ against adapted variations gives, after conditioning on $\mathcal{F}_t$:
$$\int_\mathbb{R} G(|t-v|)\,\mathbb{E}_t[u^*_v]\,dv = \alpha_t-\lambda \tag{$\star_\mathbb{R}$}$$
on $\mathbb{R}$, with analogous forms $(\star_{[0,T]})$ and $(\star_{[0,\infty)})$ on the respective domains.

**Fractional operators.** Write $D_\pm^\beta$ for the causal/anticausal Marchaud fractional derivatives of order $\beta\in(0,1)$:
$$(D_-^\beta f)(s)=\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{f(s+h)-f(s)}{h^{1+\beta}}\,dh,$$
and symmetrically for $D_+^\beta$. Their Fourier symbols are $(\pm i\xi)^\beta$ (SKM 1993 §5.4). Set $c_\gamma:=2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$, $\kappa_{1-\gamma}:=c_\gamma^{-1}$.

---

## 3. Main Results

### 3.1 Bulk theorem

**Lemma 1** (Optional projection of the anticausal half-derivative). *Let $\alpha$ be progressively measurable with $\mathbb{E}\!\int_0^\infty h^{-1-\beta}|\alpha_{s+h}-\alpha_s|\,dh<\infty$ for each $s$. Then*
$$(P_+D_-^\beta\alpha)(s)=\bigl(D_-^\beta\bar\alpha(s,\cdot)\bigr)(s)\quad\text{a.s., for a.e. }s,$$
*where $P_+$ is the optional projection $(P_+X)(s)=\mathbb{E}_s[X_s]$.*

(Proof in Appendix A.1.)

**Theorem 1** (Bulk theorem). *Assume one of: (a) $\alpha$ is stationary and mean-zero with $\int(1+|\xi|^{2(1-\gamma)+\epsilon})S_\alpha(\xi)\,d\xi<\infty$ for some $\epsilon>0$ (whole-line and half-line cases); or (b) $\alpha_t=\mathbb{E}_t[P_T-P_t]$ on $[0,T]$, extended by $\alpha_t\equiv 0$ for $t\notin[0,T]$, with $\bar\alpha(t,\cdot)\in H^{1-\gamma}(\mathbb{R})$ for a.e. $t$ (bounded-interval case; Corollary 1 supplies the boundary correction $\mathcal{B}$ that enforces the $[0,T]$ inventory constraints). In both cases suppose the Marchaud integrability of Lemma 1 holds. In case (b) the extension by zero contributes an integrable jump to the Marchaud kernel at $h=T-s$. Set $\beta=(1-\gamma)/2$ and define the $\mathcal{F}_s$-adapted process*
$$\zeta_s:=\bigl(D_-^\beta\bar\alpha(s,\cdot)\bigr)(s).$$
*Then the unique adapted minimizer of $\mathcal{C}$ satisfying $(\star_\mathbb{R})$ is*
$$\boxed{u^{\rm bulk}_t = \kappa_{1-\gamma}(D_+^\beta\zeta)(t).}$$

(Proof in Appendix A.2.)

**Remark 1** (OU signal). For $d\alpha_t=-\theta\alpha_t\,dt+\sigma\,dW_t$, the forecast is $\bar\alpha(t,s)=e^{-\theta(s-t)}\alpha_t$ for $s>t$, giving $\zeta_s=\theta^\beta\alpha_s$ and $u^{\rm bulk}_t=\kappa_{1-\gamma}\theta^\beta(D_+^\beta\alpha)(t)$.

**Remark 2** (Attribution). The structural content — half-order RL factorization with $\beta=(1-\gamma)/2$ — is present in FSS2022 Theorem 2.2 in operator language on $[0,1]$. The whole-line filtration-W-H form and the forecast-curve identification are new.

### 3.2 Boundary corrections

Any solution of $u^*=u^{\rm bulk}+\mathcal{B}$ with $\mathcal{L}\mathcal{B}=0$ (homogeneous bulk equation) on $\mathbb{T}$ and $\mathcal{B}$ matching the domain's boundary data is the optimal policy on $\mathbb{T}$. The kernel of the symmetric Abel operator on each domain is:

| Domain | $\dim\ker$ | Homogeneous modes |
|---|---|---|
| $\mathbb{R}$ | 0 | none; $\mathcal{B}\equiv 0$ |
| $[0,T]$ | 2 | $\phi_1(t)=(t(T{-}t))^{(\gamma-1)/2}$, $\phi_2(t)=\frac{T-2t}{2}\phi_1(t)$ |
| $[0,\infty)$, $\eta>0$ | 1 | decaying W-H mode (§3.4) |

**Corollary 1** (Bounded-interval execution). *Under the assumptions of Theorem 1, restricted to $[0,T]$ with $X_0$ and $X_T=0$,*
$$u^*_t = \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}_{[0,T]}\bigl(\bar\alpha(t,\cdot)-\lambda\bigr)(t) + c_1\phi_1(t)+c_2\phi_2(t),$$
*where $\mathbb{D}^{1-\gamma}_{[0,T]}$ is the Söhngen–Tricomi inversion of the symmetric Abel kernel on $[0,T]$ (SKM 1993 §13.2 Thm 13.2), and $(c_1,c_2,\lambda)$ are fixed by the terminal-inventory / budget constraint $\int_0^T u^*_t\,dt=X_0$ (a single equation, since $X_T=X_0-\int u$), the null-mode optimality condition $\langle\mathcal{B},\phi_2\rangle_{L^2}=0$ (the $\phi_2$-component of $u^*$ is unconstrained by budget and set to minimize cost), and the frictionless-budget Lagrange condition on $\lambda$.*

*When $\bar\alpha\equiv 0$, this gives $u^*_t\propto(t(T-t))^{(\gamma-1)/2}$, recovering Gatheral–Schied–Slynko (2012).*

(Proof in Appendix A.3.)

**Proposition 1** (Boundary scaling). *Fix $\varepsilon\in(0,\tfrac12)$. For bounded $\bar\alpha$ with $\|\bar\alpha\|_\infty\le M$,*
$$\sup_{t\in[\varepsilon T,(1-\varepsilon)T]}|\mathcal{B}_{1-\gamma}(t)|=O\!\left(\frac{X_0+M T^\gamma}{T}\right)=O(T^{\gamma-1})\quad\text{as }T\to\infty\text{ (fixed }X_0,M\text{)},$$
*while $u^{\rm bulk}=\Theta(1)$. Since $\gamma<1$ the boundary correction vanishes and $u^*_t=u^{\rm bulk}_t+o(1)$ uniformly on $[\varepsilon T,(1-\varepsilon)T]$; the bulk solution is the long-horizon asymptotic optimum. The bound is not uniform near the endpoints, where $\mathcal{B}$ diverges as $(t(T-t))^{(\gamma-1)/2}$.*

(Proof in Appendix A.4.)

### 3.3 Mittag-Leffler resolvent with temporary impact

Adding $\tfrac12\eta u_t^2$ ($\eta>0$) to the $[0,T]$ problem gives second-kind FOC $(\eta u^*+G*u^*=\alpha-\lambda)$. A Neumann expansion of $(I+(2\eta)^{-1}c\mathcal{G})^{-1}$, combined with the convolution identity $(t^{-\gamma})^{*n}(t)=\Gamma(1-\gamma)^n t^{n(1-\gamma)-1}/\Gamma(n(1-\gamma))$, yields:

**Theorem 2** (Mittag-Leffler resolvent). *On the bulk region of $[0,T]$ and under the Neumann convergence hypothesis $\|(2\eta)^{-1}c\mathcal{G}\|_{L^2(0,T)}<1$,*
$$u^*_t=\int_0^T R_{\gamma,\eta}(t,s)(\bar\alpha(t,s)-\lambda)\,ds+\mathcal{B}^\eta_{1-\gamma}(t),$$
$$R_{\gamma,\eta}(t,s)=\frac{1}{2\eta}\delta(t{-}s)-\frac{c\Gamma(1-\gamma)}{(2\eta)^2}|t{-}s|^{-\gamma}E_{1-\gamma,1-\gamma}\!\Bigl(-\tfrac{c\Gamma(1-\gamma)}{2\eta}|t{-}s|^{1-\gamma}\Bigr).$$
*The limits $c\to 0$ and $\eta\to 0$ recover the myopic and bulk-only policies respectively.*

### 3.4 Half-line via augmented-symbol Wiener–Hopf

With $\eta>0$ on $[0,\infty)$, the FOC symbol is $M(\xi)=c_\gamma|\xi|^{\gamma-1}+\eta$. By Krein's theorem ($\int|\log M(\xi)|(1+\xi^2)^{-1}d\xi<\infty$), $M=M_+M_-$ with $M_\pm$ analytic and nonzero in the closed upper/lower half-planes. For $\eta=0$: $M_\pm(\xi)=c_\gamma^{1/2}(\mp i\xi)^{(\gamma-1)/2}$ in closed form.

**Corollary 2** (Half-line execution). *The optimal half-line rate is $u^*_t=(M_+^{-1}\Pi_+M_-^{-1})[\bar\alpha^\infty(t,\cdot)](t)$, where $\Pi_+$ projects onto causal functions. As $\eta\to 0$ this reduces to Theorem 1 restricted to $[0,\infty)$.*

The crossover frequency $\xi_*(\eta)=(c_\gamma/\eta)^{1/(1-\gamma)}$ separates a long-memory fractional regime ($|\xi|\ll\xi_*$) from myopic signal-following ($|\xi|\gg\xi_*$).

### 3.5 Multi-asset extension

Let $G(t)=t^{-\gamma}\mathbf{C}$ with $\mathbf{C}\in\mathbb{R}^{d\times d}_{\rm sym,+}$, $\mathbf{C}=Q\Lambda Q^\top$.

**Theorem 3** (Matrix bulk theorem). *The optimal vector bulk rate is*
$$\mathbf{u}^{\rm bulk}_t=\mathbf{C}^{-1}\kappa_{1-\gamma}(D_+^\beta\boldsymbol\zeta)(t),\qquad \boldsymbol\zeta_s:=(D_-^\beta\bar{\boldsymbol\alpha}(s,\cdot))(s),$$
*applied componentwise in the $Q$-eigenbasis. The scalar Theorem 1 holds independently on each principal-component signal.*

---

## References

- Abi Jaber, E.; Neuman, E. *Optimal Liquidation with Signals: the General Propagator Case.* Math. Finance, 2025; arXiv:2211.00447.
- Abi Jaber, E.; Neuman, E.; Tuschmann, S. *Optimal Portfolio Choice with Cross-Impact Propagators.* arXiv:2403.10273, 2024.
- Forde, M.; Sánchez-Betancourt, L.; Smith, B. *Optimal trade execution for Gaussian signals with power-law resilience.* Quant. Finance 22(3), 2022.
- Gatheral, J.; Schied, A.; Slynko, A. *Transient linear price impact and Fredholm integral equations.* Math. Finance 22(3), 2012.
- Gârleanu, N.; Pedersen, L.H. *Dynamic Trading with Predictable Returns and Transaction Costs.* J. Finance 68(6), 2013.
- Jusselin, P.; Rosenbaum, M. *No-arbitrage implies power-law market impact and rough volatility.* Math. Finance 30(4), 2020.
- Krein, M.G. *Integral equations on a half-line...* Amer. Math. Soc. Transl. (2) 22, 1962.
- Moreau, L.; Muhle-Karbe, J.; Soner, H.M. *Trading with Small Price Impact.* Math. Finance 27(2), 2017.
- Noble, B. *Methods Based on the Wiener-Hopf Technique.* Pergamon, 1958.
- Samko, S.G.; Kilbas, A.A.; Marichev, O.I. *Fractional Integrals and Derivatives.* Gordon and Breach, 1993. [SKM]
- Söhngen, H. *Die Lösungen der Integralgleichung...* Math. Z. 45, 1939.
- Tricomi, F.G. *Integral Equations.* Interscience, 1957.

---

## Appendix A. Proofs

### A.1 Proof of Lemma 1

By the Marchaud representation (SKM 1993 §5.4 eq. (5.57)):
$$(D_-^\beta\alpha)(s)=\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{\alpha_{s+h}-\alpha_s}{h^{1+\beta}}\,dh.$$
Under the hypothesis $\mathbb{E}\!\int_0^\infty h^{-1-\beta}|\alpha_{s+h}-\alpha_s|\,dh<\infty$, the integrand is in $L^1(\Omega\times[0,\infty), dP\otimes h^{-1-\beta}dh)$. By the conditional Fubini theorem (Klenke 2014, Thm 14.16), for a.e. $\omega$ the conditional expectation commutes with the integral:
\begin{align*}
(P_+D_-^\beta\alpha)(s)
&=\mathbb{E}_s\!\left[\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{\alpha_{s+h}-\alpha_s}{h^{1+\beta}}\,dh\right]\\
&=\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{\mathbb{E}_s[\alpha_{s+h}]-\alpha_s}{h^{1+\beta}}\,dh\\
&=\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{\bar\alpha(s,s+h)-\bar\alpha(s,s)}{h^{1+\beta}}\,dh
=(D_-^\beta\bar\alpha(s,\cdot))(s),
\end{align*}
using $\mathbb{E}_s[\alpha_{s+h}]=\bar\alpha(s,s+h)$ (definition of $\bar\alpha$) and $\mathbb{E}_s[\alpha_s]=\alpha_s$ ($\alpha_s\in\mathcal{F}_s$). The last line is the Marchaud representation of $D_-^\beta$ applied to the deterministic function $u\mapsto\bar\alpha(s,u)$, evaluated at $u=s$. $\blacksquare$

**Adaptedness of $\zeta_s$.** By Lemma 1, $\zeta_s=D_-^\beta\bar\alpha(s,\cdot)(s)$. Since $\bar\alpha(s,\cdot)$ is $\mathcal{F}_s$-measurable (as an $H^\beta$-valued random variable) and $D_-^\beta:H^\beta\to L^2$ is a bounded deterministic operator, $\zeta_s\in\mathcal{F}_s$.

### A.2 Proof of Theorem 1

**Candidate.** Define $u^{\rm cand}_t:=\kappa_{1-\gamma}(D_+^\beta\zeta)(t)$. Since $D_+^\beta$ at time $t$ depends only on $\{\zeta_s\}_{s\le t}$ and each $\zeta_s\in\mathcal{F}_s\subset\mathcal{F}_t$, the candidate is adapted.

**FOC verification.** We show $\mathbb{E}_t[(Cu^{\rm cand})(t)]=\alpha_t$.

*Step 1: commute $\mathbb{E}_t$ through $D_+^\beta$.* The Marchaud representation of $D_+^\beta$ is
$$(D_+^\beta\zeta)(v)=\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{\zeta_{v-h}-\zeta_v}{h^{1+\beta}}\,dh.$$
Assume additionally $\mathbb{E}\!\int_0^\infty h^{-1-\beta}|\zeta_{v-h}-\zeta_v|\,dh<\infty$ (this holds in case (a) via Plancherel: $\mathbb{E}|\zeta_{v-h}-\zeta_v|^2\le C h^{2\beta+\epsilon}\|S_\alpha\cdot|\xi|^{2(1-\gamma)+\epsilon}\|_{L^1}$, giving $\mathbb{E}|\zeta_{v-h}-\zeta_v|\le Ch^{\beta+\epsilon/2}$ by Cauchy–Schwarz, and hence $\int_0^1 h^{-1+\epsilon/2}\,dh<\infty$ near zero; the tail is controlled by the trivial bound $\mathbb{E}|\zeta_{v-h}-\zeta_v|\le 2\|\zeta\|_{L^2(\Omega)}$); then conditional Fubini gives $\mathbb{E}_t[(D_+^\beta\zeta)(v)]=(D_+^\beta\hat\zeta_t)(v)$ where $\hat\zeta_t(s):=\mathbb{E}_t[\zeta_s]$.

*Step 2: compute $\hat\zeta_t(s)$.*
- $s\le t$: $\zeta_s\in\mathcal{F}_s\subset\mathcal{F}_t$, so $\hat\zeta_t(s)=\zeta_s$.
- $s>t$: By Lemma 1, $\zeta_s=\mathbb{E}_s[(D_-^\beta\alpha)(s)]$. By the tower property ($t\le s$), $\mathbb{E}_t[\zeta_s]=\mathbb{E}_t[(D_-^\beta\alpha)(s)]$. Now apply Marchaud + conditional Fubini at conditioning time $t$ (not $s$): for $s>t$ and $h>0$, $s+h>s>t$, so $\mathbb{E}_t[\alpha_{s+h}]=\bar\alpha(t,s+h)$ and $\mathbb{E}_t[\alpha_s]=\bar\alpha(t,s)$. Therefore
$$\mathbb{E}_t[(D_-^\beta\alpha)(s)]=\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{\bar\alpha(t,s+h)-\bar\alpha(t,s)}{h^{1+\beta}}\,dh=(D_-^\beta\bar\alpha(t,\cdot))(s).$$

*Step 3: close the FOC.* The symbol identity (Appendix B, eq. (B.1)) gives $G\ast D_+^\beta=c_\gamma I_-^\beta$ on $L^2$, where $I_-^\beta$ is the anticausal RL integral of order $\beta$. Substituting:
$$\mathbb{E}_t[(Cu^{\rm cand})(t)]=c_\gamma^{-1}(G\ast D_+^\beta\hat\zeta_t)(t)=(I_-^\beta\hat\zeta_t)(t).$$
Since $I_-^\beta$ at $t$ uses only $\hat\zeta_t(s)$ for $s\ge t$ — and for $s\ge t$ we have $\hat\zeta_t(s)=(D_-^\beta\bar\alpha(t,\cdot))(s)$ — the composition gives:
$$(I_-^\beta\hat\zeta_t)(t)=(I_-^\beta D_-^\beta\bar\alpha(t,\cdot))(t)=\bar\alpha(t,t)=\alpha_t,$$
using $I_-^\beta D_-^\beta=\text{id}$ on $H^\beta(\mathbb{R})$ (SKM 1993 §5.3 Thm 5.3). The conditioned FOC $(\star_\mathbb{R})$ is satisfied (the DC offset $\lambda$ contributes only to the $\xi=0$ mode, suppressed under the PSD hypothesis).

**Uniqueness.** $\mathcal{C}$ is strictly convex on $L^2_{\rm adap}$ since $\hat G(\xi)=c_\gamma|\xi|^{\gamma-1}>0$ for $\xi\ne 0$; the FOC is necessary and sufficient.

**$L^2$ admissibility.** The PSD hypothesis $\int(1+|\xi|^{2(1-\gamma)+\epsilon})S_\alpha\,d\xi<\infty$ ensures $|\xi|^{1-\gamma}\widehat{\bar\alpha}\in L^2$ pathwise, so $u^{\rm bulk}\in L^2_{\rm adap}$ by Plancherel. $\blacksquare$

### A.3 Proof of Corollary 1

After conditioning on $\mathcal{F}_t$, the bounded-interval FOC $(\star_{[0,T]})$ becomes the deterministic symmetric Abel equation in the forecast:
$$\int_0^T|s-v|^{-\gamma}v_t(v)\,dv=c^{-1}(\bar\alpha(t,s)-\lambda),\qquad s\in(0,T).$$
SKM 1993 §13.2 Theorem 13.2 inverts this as
$$v_t(s)=\kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}_{[0,T]}(\bar\alpha(t,\cdot)-\lambda)(s)+c_1\phi_1(s)+c_2\phi_2(s),$$
where $\mathbb{D}^{1-\gamma}_{[0,T]}$ is the Söhngen–Tricomi operator (§3.2 of SKM), $\phi_1(s)=(s(T-s))^{(\gamma-1)/2}$, and $\phi_2(s)=\frac{T-2s}{2}\phi_1(s)$ span the two-dimensional kernel of the symmetric Abel operator on $[0,T]$. The normalization constant $\kappa_{1-\gamma}=c_\gamma^{-1}$ follows from the airfoil-equation prefactor $\sin(\pi\nu)/\pi^2$ (with $\nu=(1-\gamma)/2$) combined with the kernel symbol $c_\gamma=2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$, using the Euler reflection identity $\Gamma(1-\gamma)\Gamma(\gamma)=\pi/\sin(\pi\gamma)$. Setting $v_t(s)|_{s=t}=u^*_t$ completes the corollary. The constants $(c_1,c_2,\lambda)$ are determined by the terminal-inventory / budget constraint $\int_0^T u^*_t\,dt=X_0$ (a single equation since $X_T=X_0-\int u$), the null-mode optimality condition $\langle\mathcal{B},\phi_2\rangle_{L^2}=0$, and the Lagrange stationarity for $\lambda$. $\blacksquare$

### A.4 Proof of Proposition 1

The null mode $\phi_2$ lies in the kernel of the symmetric Abel operator and satisfies $\int_0^T\phi_2\,dt=0$, so any $c_2$ leaves both the cost and the budget invariant. We adopt the minimum-$L^2$-norm selection $\langle u^*,\phi_2\rangle_{L^2}=0$, which gives $c_2=-\langle u^{\rm bulk},\phi_2\rangle/\|\phi_2\|_{L^2}^2$. By the substitution $t=sT$: $\phi_1(sT)=T^{\gamma-1}(s(1-s))^{(\gamma-1)/2}$ so $\|\phi_1\|_{L^1}=\Theta(T^\gamma)$; $\phi_2(sT)=(T^\gamma/2)(1-2s)(s(1-s))^{(\gamma-1)/2}$ so $\|\phi_2\|_{L^2}^2=\Theta(T^{2\gamma+1})$. Using $\|u^{\rm bulk}\|_{L^2([0,T])}=O(MT^{\gamma-1/2})$ (from the interior bound $u^{\rm bulk}=O(MT^{\gamma-1})$ combined with the $[\varepsilon T,(1-\varepsilon)T]$ region) and Cauchy–Schwarz gives $|c_2|=O(M/T)$.

For $c_1$: since $\phi_2$ integrates to zero, the budget constraint reduces to $c_1\int_0^T\phi_1\,dt=X_0-\int_0^T u^{\rm bulk}_t\,dt$. Boundedness of the Söhngen–Tricomi inversion operator on $L^\infty([0,T])$ (SKM 1993 §13.4) yields $|\int_0^T u^{\rm bulk}|=O(MT^\gamma)$, so $|c_1|=O((X_0+MT^\gamma)/T^\gamma)$.

Evaluating at fixed $s\in[\varepsilon,1-\varepsilon]$: $\phi_1(sT)=\Theta(T^{\gamma-1})$ uniform, $|\phi_2(sT)|\le CT^\gamma$ uniform. Hence
$$|c_1\phi_1(sT)|=O((X_0+MT^\gamma)/T),\qquad |c_2\phi_2(sT)|=O(MT^{\gamma-1}).$$
Both terms are $O((X_0+MT^\gamma)/T)$; the two boundary modes contribute at the same order. Therefore
$$\sup_{s\in[\varepsilon,1-\varepsilon]}|\mathcal{B}_{1-\gamma}(sT)|=O\!\left(\frac{X_0+MT^\gamma}{T}\right)=O(T^{\gamma-1})\text{ as }T\to\infty\text{ (fixed }X_0,M\text{)}.$$

Near the endpoints $\phi_1(t)$ diverges as $(t(T-t))^{(\gamma-1)/2}$, confirming non-uniformity. $\blacksquare$

---

## Appendix B. Key Fourier Identities

**Kernel symbol.** $\hat G(\xi)=2c\int_0^\infty t^{-\gamma}\cos(\xi t)\,dt=c_\gamma|\xi|^{\gamma-1}$ with $c_\gamma=2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)$ (GR 3.761.9; SKM §7.1).

**Wiener–Hopf factorization of the bulk symbol.** With $\beta=(1-\gamma)/2$:
$$|\xi|^{1-\gamma}=(i\xi)^\beta(-i\xi)^\beta,\qquad (i\xi)^\beta:=|\xi|^\beta e^{i\beta\pi\,{\rm sgn}(\xi)/2}.\tag{B.1}$$
$(i\xi)^\beta$ and $(-i\xi)^\beta$ are analytic and nonzero in the closed upper and lower half-planes respectively (SKM §7.1). Their time-domain counterparts are $D_+^\beta$ and $D_-^\beta$.

**Key symbol identity.**
$$\hat G(\xi)\cdot(i\xi)^\beta=c_\gamma|\xi|^{\gamma-1+\beta}e^{i\beta\pi\,{\rm sgn}(\xi)/2}=c_\gamma(-i\xi)^{-\beta},\tag{B.2}$$
using $\gamma-1+\beta=-\beta$. In time domain: $G\ast D_+^\beta=c_\gamma I_-^\beta$ on $L^2(\mathbb{R})$ with $I_-^\beta$ the anticausal RL integral of order $\beta$.

**Inverse relation.** $I_-^\beta D_-^\beta={\rm id}$ on $H^\beta(\mathbb{R})$ (SKM §5.3 Thm 5.3).
