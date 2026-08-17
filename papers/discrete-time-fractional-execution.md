# Discrete-time optimal execution with power-law impact: bulk and half-line solutions without budget constraint

**Companion to** `fractional-derivative-optimal-execution.md`. Discrete-time version. No terminal-inventory / budget constraint. Explicit closed-form policies on $\mathbb{Z}$ and $\mathbb{Z}_{\ge 0}$ via DTFT symbol inversion and discrete Wiener–Hopf (Toeplitz) factorization.

## Abstract

We treat the signal-adaptive optimal-execution problem in discrete time with a symmetric power-law market-impact kernel $G_k = c\,k^{-\gamma}$, $\gamma\in(0,1)$, and constant temporary impact $\eta$, in the absence of any terminal-inventory or budget constraint. Two domains are solved explicitly: the whole line $\mathbb{Z}$ (bulk problem) and the half-line $\mathbb{Z}_{\ge 0}$ (Wiener–Hopf problem). On $\mathbb{Z}$ the optimal rate is the convolution of the (forecast) signal with a resolvent kernel whose discrete-time Fourier transform (DTFT) is $1/\hat G(\theta)$, where $\hat G(\theta) = 2\eta + 2c\,\mathrm{Re}\,\mathrm{Li}_\gamma(e^{i\theta})$; at low frequency this is the discrete Riesz fractional derivative of order $1-\gamma$ of the signal, matching the continuous bulk theorem in the small-lattice-spacing limit. On $\mathbb{Z}_{\ge 0}$ the optimal rate is the Wiener–Hopf (Toeplitz) inversion $\hat G_+^{-1}\Pi_+\hat G_-^{-1}\bar\alpha_t(\cdot)$, where $\hat G = \hat G_+\hat G_-$ is the multiplicative Szegő factorization on the unit circle. Adaptedness of both policies is handled via the discrete forecast curve $\bar\alpha_t(s) = \mathbb{E}[\alpha_s\mid\mathcal{F}_t]$ and a discrete optional-projection identity (Proposition 1.4) that quarantines all non-causality in a single forecast-consuming step. Without a budget constraint, no homogeneous boundary correction is present. Both policies are $O(N\log N)$ via FFT. The construction reduces to the continuous bulk and half-line policies of the companion paper in the fine-grid limit.

## 1. Setup

### 1.1 Problem

Fix $\gamma\in(0,1)$, $c>0$, $\eta > 0$. The (symmetric) discrete-time propagator kernel is
$$G_k \;=\; \begin{cases} 2\eta & k = 0, \\ c\,|k|^{-\gamma} & k\in\mathbb{Z}\setminus\{0\}. \end{cases}$$
An admissible trading rate is $u\in\ell^2(\mathbb{Z})$ (bulk) or $u\in\ell^2(\mathbb{Z}_{\ge 0})$ (half-line). A deterministic signal $\alpha\in\ell^2$ is given. The cost functional on domain $\mathbb{T}\in\{\mathbb{Z},\mathbb{Z}_{\ge 0}\}$ is
$$J_\mathbb{T}(u) \;=\; \tfrac12\sum_{t,s\in\mathbb{T}} G_{|t-s|}\,u_t u_s \;-\; \sum_{t\in\mathbb{T}} \alpha_t\,u_t.$$
Note the diagonal $G_0 = 2\eta$ absorbs the temporary-impact term $\eta u_t^2$ into the quadratic form: $\tfrac12 G_0 u_t^2 = \eta u_t^2$. **No budget or terminal-inventory constraint is imposed.** In particular there is no Lagrange multiplier and no boundary correction to enforce $\sum u_t = X_0$; the optimal rate is purely signal-driven.

### 1.2 First-order condition

Stationarity of $J_\mathbb{T}$ gives, on the respective domain,
$$(G*_\mathbb{T} u)_t \;:=\; \sum_{s\in\mathbb{T}} G_{|t-s|}\,u_s \;=\; \alpha_t, \qquad t\in\mathbb{T}. \tag{$\star_\mathbb{T}$}$$
This is a linear equation in $u$: a discrete convolution on $\mathbb{Z}$ (translation-invariant), or a Toeplitz equation on $\mathbb{Z}_{\ge 0}$ (Wiener–Hopf).

### 1.2.1 Filtration and adapted setting

Fix a filtered probability space $(\Omega,\mathcal{F},(\mathcal{F}_t)_{t\in\mathbb{T}},\mathbb{P})$ and let $\alpha=(\alpha_t)_{t\in\mathbb{T}}$ be a square-integrable $(\mathcal{F}_t)$-adapted signal. An admissible rate is $(\mathcal{F}_t)$-adapted with $\mathbb{E}\sum u_t^2 < \infty$. The **discrete forecast curve** at time $t$ is
$$\bar\alpha_t(s) \;:=\; \mathbb{E}[\alpha_s\mid \mathcal{F}_t], \qquad s\in\mathbb{T},$$
so $\bar\alpha_t(s) = \alpha_s$ for $s\le t$ (past observed) and is a genuine conditional forecast for $s>t$. The deterministic setup of §1.1 is the degenerate case $\bar\alpha_t = \alpha$ (full-information filtration).

**Adapted FOC.** Taking $\mathcal{F}_t$-conditional expectations of $(\star_\mathbb{T})$ gives the adapted first-order condition
$$\sum_{s\in\mathbb{T}} G_{|t-s|}\,\mathbb{E}[u_s\mid\mathcal{F}_t] \;=\; \bar\alpha_t(t) \;+\; \sum_{s\ne t} G_{|t-s|}\bigl(\bar\alpha_t(s) - \alpha_s\bigr)\mathbf{1}_{s\le t}, \qquad t\in\mathbb{T}. \tag{$\star^{\mathcal{F}}_\mathbb{T}$}$$
Equivalently: the deterministic solution formulas of §2–§3 apply *pointwise in $t$*, with $\alpha$ replaced by $\bar\alpha_t(\cdot)$ (i.e. actual past and forecast future). This is the discrete analogue of the continuous adapted FOC $(\star^{\mathcal{F}})$ / $(\star^{\mathcal{F}}_{\rm WH})$ of §2.3 of the companion paper. Adaptedness of $u^*$ is then a consequence of the causal structure of the solution operator (verified in Proposition 4.1 below); it is *not* a separate constraint imposed on top of $(\star^{\mathcal{F}}_\mathbb{T})$.

### 1.3 Positivity of the symbol

The DTFT of the kernel is
$$\hat G(\theta) \;:=\; \sum_{k\in\mathbb{Z}} G_{|k|}\,e^{-ik\theta} \;=\; 2\eta \;+\; 2c\sum_{k=1}^\infty \frac{\cos(k\theta)}{k^\gamma} \;=\; 2\eta \;+\; 2c\,\mathrm{Re}\,\mathrm{Li}_\gamma(e^{i\theta}),$$
where $\mathrm{Li}_\gamma(z) = \sum_{k\ge 1} z^k/k^\gamma$ is the polylogarithm. For $\gamma\in(0,1)$ the series $\sum \cos(k\theta)/k^\gamma$ is bounded below by $-\bar\eta(\gamma)$ with
$$\bar\eta(\gamma) \;:=\; -\sum_{k=1}^\infty \frac{(-1)^k}{k^\gamma} \;=\; (1 - 2^{1-\gamma})|\zeta(\gamma)|,$$
attained at $\theta = \pi$ (Dirichlet eta function; $\zeta(\gamma) < 0$ on $(0,1)$).

**Assumption (H).** *$\eta > c\,\bar\eta(\gamma)$.* Under (H), $\hat G(\theta) > 0$ for all $\theta\in[-\pi,\pi]$, and the Toeplitz operator with symbol $\hat G$ is positive-definite on both $\ell^2(\mathbb{Z})$ and $\ell^2(\mathbb{Z}_{\ge 0})$. The cost $J_\mathbb{T}$ is strictly convex, so the FOC $(\star_\mathbb{T})$ has a unique minimizer.

### 1.4 Low- and high-frequency asymptotics of $\hat G$

The polylogarithm has the classical expansion (Erdélyi 1953 §1.11; Wood 1992)
$$\mathrm{Li}_\gamma(e^{i\theta}) \;=\; \Gamma(1-\gamma)\,(-i\theta)^{\gamma-1} \;+\; \sum_{k\ge 0} \frac{\zeta(\gamma-k)}{k!}\,(i\theta)^k, \qquad |\theta|\to 0,$$
whose real part gives
$$\hat G(\theta) \;=\; c_\gamma\,|\theta|^{\gamma-1} \;+\; \bigl(2\eta + 2c\,\zeta(\gamma)\bigr) \;+\; O(\theta^2), \qquad c_\gamma := 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2).$$
This matches the continuous kernel's Fourier symbol $c_\gamma|\xi|^{\gamma-1}+\eta_{\rm cts}$ at low frequency, up to a finite renormalization $\eta \mapsto \eta + c\,\zeta(\gamma)$ of the temporary-impact constant that reflects the lattice-vs-continuum discretization. At high frequency (near $\theta = \pm\pi$), $\hat G(\theta) = 2\eta - 2c\bar\eta(\gamma) + O((\pi-|\theta|)^2)$, a positive constant under (H).

## 2. Bulk theorem on $\mathbb{Z}$

### 2.1 DTFT inversion

**Theorem 1 (Discrete bulk theorem, deterministic).** *Under (H), the unique $\ell^2(\mathbb{Z})$ solution of $(\star_\mathbb{Z})$ is*
$$u^*_t \;=\; \frac{1}{2\pi}\int_{-\pi}^{\pi} \frac{\hat\alpha(\theta)}{\hat G(\theta)}\,e^{i\theta t}\,d\theta \;=\; \sum_{k\in\mathbb{Z}} R_k\,\alpha_{t-k}, \qquad R_k := \frac{1}{2\pi}\int_{-\pi}^\pi \frac{e^{ik\theta}}{\hat G(\theta)}\,d\theta,$$
*where $\hat\alpha(\theta) = \sum_t \alpha_t e^{-it\theta}$ is the DTFT of the signal and $R\in\ell^2(\mathbb{Z})$ is the resolvent kernel.*

**Proof.** The Toeplitz operator with symbol $\hat G$ is $L^2$-unitarily equivalent to multiplication by $\hat G$ under the DTFT. Under (H), $\hat G$ is bounded above and bounded away from zero on the circle, so $1/\hat G\in L^\infty$ and the inverse operator has symbol $1/\hat G$. Convolution with $R$ is the inverse. $\blacksquare$

**Theorem 1$'$ (Discrete bulk theorem, adapted).** *Under (H) applied to $(\star^{\mathcal{F}}_\mathbb{Z})$, and assuming $\bar\alpha_t(\cdot)\in\ell^2(\mathbb{Z})$ a.s. for each $t$, the optimal $(\mathcal{F}_t)$-adapted trading rate is*
$$u^*_t \;=\; \sum_{k\in\mathbb{Z}} R_k\,\bar\alpha_t(t-k), \qquad t\in\mathbb{Z},$$
*i.e. the deterministic resolvent kernel $R$ convolved against the time-$t$ forecast curve $\bar\alpha_t(\cdot)$, evaluated at the diagonal $s=t$.*

**Proof (deferred).** Requires the causal/anti-causal factorization of $R$ and the discrete optional-projection identity. See Corollary 1.5 and Remark 1.6 below. $\blacksquare$

**Warning.** The naive derivation “apply $\mathbb{E}[\cdot\mid\mathcal{F}_t]$ to the deterministic solution $u^{\rm det}_t = \sum_k R_k\alpha_{t-k}$ and pull the conditional expectation inside the deterministic sum” yields the same right-hand side but is **not a valid derivation** of adapted optimality: $u^{\rm det}$ is not $(\mathcal{F}_t)$-adapted (its value at $t$ uses $\alpha_s$ for $s>t$), so pointwise conditioning does not in general produce the minimizer of the cost over the *adapted* admissible set. Adapted optimality requires a genuine projection argument at the operator level, not at the pathwise level. That the two recipes coincide on the diagonal is a *theorem* (the optional-projection identity of Proposition 1.4 applied to both factors of the causal/anti-causal split), not a triviality.

### 2.1.1 Causal / anti-causal split and the optional-projection identity

The Grünwald–Letnikov factorization of Corollary 1.1 refactors $u^*$ into a two-stage adapted filter. Write $\hat G(\theta)^{-1} = P_+(\theta)\,P_-(\theta) + \tilde R(\theta)$ with the leading half-order symbols
$$P_+(\theta) := \kappa_{1-\gamma}^{1/2}\,(1-e^{-i\theta})^\beta, \qquad P_-(\theta) := \kappa_{1-\gamma}^{1/2}\,(1-e^{i\theta})^\beta, \qquad \beta = (1-\gamma)/2,$$
causal / anti-causal on the lattice respectively. The corresponding time-domain operators $\Delta_+^\beta$, $\Delta_-^\beta$ act on any $\ell^2$ sequence $f$ by
$$(\Delta_+^\beta f)_t = \sum_{k\ge 0}(-1)^k \binom{\beta}{k} f_{t-k}, \qquad (\Delta_-^\beta f)_t = \sum_{k\ge 0}(-1)^k \binom{\beta}{k} f_{t+k},$$
the standard causal and anti-causal Grünwald–Letnikov half-order differences. The bulk factorization then reads
$$u^*_t \;=\; \Delta_+^\beta\bigl[\Delta_-^\beta \alpha\bigr]_t \;+\; \text{(bounded correction)}.$$

The anti-causal step $\Delta_-^\beta\alpha$ requires future values of $\alpha$, so this decomposition is *not adapted* at the level of $\alpha$. It is adapted at the level of the forecast curve:

**Proposition 1.4 (Discrete optional projection).** *For $\alpha$ adapted and square-integrable, the optional projection commutes with $\Delta_-^\beta$ evaluated at the diagonal:*
$$\mathbb{E}\!\left[(\Delta_-^\beta\alpha)_t \,\middle|\, \mathcal{F}_t\right] \;=\; \bigl(\Delta_-^\beta\bar\alpha_t(\cdot)\bigr)(t), \qquad t\in\mathbb{Z},$$
*i.e. applying the anti-causal half-order difference to the forecast curve $\bar\alpha_t(\cdot)$ at time $t$ yields the $\mathcal{F}_t$-optional projection of the anti-causal half-order difference of $\alpha$.*

**Proof.** $\Delta_-^\beta$ acts linearly and its kernel $(-1)^k\binom{\beta}{k}$ is deterministic; interchange conditional expectation with the (deterministic, absolutely convergent for $\beta\in(0,1)$ against $\ell^2$) sum. Convergence of the sum in $L^2(\mathbb{P})$ is standard: the coefficients $(-1)^k\binom{\beta}{k}$ are $O(k^{-1-\beta})$ and $\alpha\in\ell^2$ pathwise a.s. under (H). $\blacksquare$

**Corollary 1.5 (Adapted two-stage filter).** *Combining Proposition 1.4 with the causality of $\Delta_+^\beta$, the adapted bulk optimizer admits the two-stage realization*
$$u^*_t \;=\; \Delta_+^\beta\!\left[\,P^{\rm o}\bigl(\Delta_-^\beta\alpha\bigr)\,\right]_t \;+\; \text{(bounded correction)},$$
*where $P^{\rm o}$ denotes the optional projection (mapping any $\ell^2$ process $X$ to the adapted process $(P^{\rm o}X)_s := \mathbb{E}[X_s\mid\mathcal{F}_s]$), and the outer $\Delta_+^\beta$ acts causally on the resulting adapted sequence. All non-causality is quarantined in the inner anti-causal $\Delta_-^\beta$ step, and adaptedness is enforced by the projection **between** the two half-order factors, not after their composition.*

**Proof.** The unconstrained (deterministic) optimizer over all $\ell^2$ trading rates has cost $-\tfrac12\langle\alpha,R\alpha\rangle$; restricting to $(\mathcal{F}_t)$-adapted rates is a linear-subspace constraint. Standard Hilbert-space projection (Cauchy–Schwarz on the causal/anti-causal split of the cost) gives that the constrained minimizer equals the unconstrained minimizer *after inserting the optional projection between the two square-roots of the operator $R$*, i.e. between the causal and anti-causal factors of the (leading part of the) Grünwald–Letnikov factorization. This is the discrete/lattice version of the FSS2022 / companion-paper argument (§4.2–§4.3). The bounded-correction term $\tilde R$ is treated the same way with $P^{\rm o}$ inserted between its own causal/anti-causal split (which exists under (H) by the same Szegő argument). $\blacksquare$

**Remark 1.6 (Reconciliation with Theorem 1$'$).** Corollary 1.5 is the *derivation* of the adapted bulk optimizer. Theorem 1$'$ is the compact *forecast-curve form* of the same object: evaluating Corollary 1.5 at time $t$ and applying Proposition 1.4 to the outer $\Delta_+^\beta$ acting on $P^{\rm o}(\Delta_-^\beta\alpha)$ (in reverse: recombine into a single convolution by the resolvent kernel $R$ applied to the forecast curve $\bar\alpha_t(\cdot)$ on the diagonal). The two identities
$$\Delta_+^\beta\bigl[P^{\rm o}(\Delta_-^\beta\alpha)\bigr]_t \;=\; \bigl(\Delta_+^\beta\,\Delta_-^\beta\,\bar\alpha_t(\cdot)\bigr)(t)$$
and (adding back the bounded correction)
$$u^*_t \;=\; \sum_{k\in\mathbb{Z}} R_k\,\bar\alpha_t(t-k)$$
are equivalent on the diagonal, and their equivalence is *exactly* the content of the optional-projection identity of Proposition 1.4 applied to both sides. Neither is a trivial rearrangement of the other; the equality is a nontrivial consequence of the fact that the propagator problem has a translation-invariant resolvent whose causal/anti-causal factorization commutes with optional projection on the diagonal.

### 2.2 Discrete Riesz fractional derivative

The multiplication operator $1/\hat G(\theta)$ on the unit circle is the DTFT-symbol characterization of a *discrete symmetric Riesz fractional derivative* modulated by the finite temporary-impact term. To make the fractional structure explicit, decompose
$$\frac{1}{\hat G(\theta)} \;=\; \frac{1}{c_\gamma|\theta|^{\gamma-1} + \eta_{\rm eff}} \;+\; r(\theta), \qquad \eta_{\rm eff} := 2\eta + 2c\,\zeta(\gamma),$$
where $r(\theta) = O(\theta^2)$ near the origin and is bounded on $[-\pi,\pi]$. The leading term is the low-frequency continuous symbol; the residual $r$ encodes the finite-lattice corrections.

**Corollary 1.1 (Grünwald–Letnikov form).** *Let $\Delta_+^\beta$ and $\Delta_-^\beta$ denote the causal and anti-causal Grünwald–Letnikov half-order differences with symbols $(1-e^{-i\theta})^\beta$ and $(1-e^{i\theta})^\beta$, and let $\beta = (1-\gamma)/2$. Then*
$$u^*_t \;=\; \kappa_{1-\gamma}\,\bigl(\Delta_+^\beta\,\Delta_-^\beta\,\alpha\bigr)_t \;+\; \bigl(\tilde R * \alpha\bigr)_t, \qquad \kappa_{1-\gamma} = c_\gamma^{-1},$$
*where $\tilde R$ is a bounded, exponentially localized correction kernel encoding the difference between the lattice symbol $1/\hat G(\theta)$ and the continuous approximation $c_\gamma^{-1}(1-e^{-i\theta})^\beta(1-e^{i\theta})^\beta = c_\gamma^{-1}\bigl(2\sin(\theta/2)\bigr)^{1-\gamma}$.*

**Proof.** The Grünwald–Letnikov product symbol $(2\sin(\theta/2))^{1-\gamma} = |\theta|^{1-\gamma}(1+O(\theta^2))$, matching the continuous fractional derivative's low-frequency behaviour. Write $1/\hat G(\theta) = \kappa_{1-\gamma}(2\sin(\theta/2))^{1-\gamma}\,+\,\tilde R(\theta)$ with $\tilde R = O(\theta^{3-\gamma})$ near zero and bounded on the whole circle. Inverse-DTFT gives the stated split. $\blacksquare$

**Remark 1.2.** The identity
$$(1-e^{-i\theta})^{1/2}(1-e^{i\theta})^{1/2} \;=\; \bigl(2\sin(\theta/2)\bigr)\,\cdot\,i\,\mathrm{sgn}(\theta)\,\cdot\,(-i)^{1/2}(i)^{1/2}$$
requires careful branch bookkeeping; the standard convention takes the principal branch so that the product is $(2\sin(\theta/2))^{1-\gamma}$ (real, positive) times an implicit $\Pi_+$-type projection when applied causally. This is the discrete analogue of the bulk-symbol Wiener–Hopf factorization of §4.3 of the companion paper.

### 2.3 Resolvent-kernel asymptotics

The resolvent $R_k = (2\pi)^{-1}\int e^{ik\theta}/\hat G(\theta)\,d\theta$ inherits the low-frequency structure of $1/\hat G$:

**Proposition 1.3 (Long-lag resolvent tail).** *As $|k|\to\infty$,*
$$R_k \;=\; \frac{\kappa_{1-\gamma}}{|k|^{2-\gamma}}\,\bigl[C_\gamma \;+\; O(|k|^{-2})\bigr], \qquad C_\gamma = \frac{\Gamma(2-\gamma)\sin(\pi(1-\gamma)/2)}{\pi}.$$

**Proof.** Standard stationary-phase / Erdélyi asymptotic on the Fourier integral $\int e^{ik\theta}|\theta|^{1-\gamma}\,d\theta$; the leading power-law decay is dictated by the origin singularity of $1/\hat G$. $\blacksquare$

### 2.4 Recovery of the continuous bulk theorem

Introduce lattice spacing $\Delta t$ and define the continuous-time signal $\alpha_{\rm cts}(t\Delta t) = \alpha_t$, the trading rate $u_{\rm cts}(t\Delta t) = u^*_t/\Delta t$, and the continuous kernel $G_{\rm cts}(\tau) = c\,\tau^{-\gamma}$. In the fine-grid limit $\Delta t\to 0$, the discrete FOC $(\star_\mathbb{Z})$ converges to its continuous analogue, and the discrete bulk solution of Theorem 1 converges pointwise (under mild regularity of $\alpha_{\rm cts}$) to the continuous bulk solution $u_{\rm cts}^*(t) = \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\alpha_{\rm cts}(t)$ of Theorem 4.1 of the companion paper. The lattice contribution $c\,\zeta(\gamma)$ to $\eta_{\rm eff}$ vanishes relative to $\Delta t^{\gamma-1}\to\infty$ in the low-frequency (small-$\theta/\Delta t$) regime.

## 3. Half-line theorem on $\mathbb{Z}_{\ge 0}$

### 3.1 Discrete Wiener–Hopf setup

On $\mathbb{Z}_{\ge 0}$ the FOC $(\star_{\mathbb{Z}_{\ge 0}})$ is a Toeplitz equation: the operator $T[\hat G]:\ell^2(\mathbb{Z}_{\ge 0})\to\ell^2(\mathbb{Z}_{\ge 0})$ with $(T[\hat G]u)_t = \sum_{s\ge 0} G_{|t-s|}u_s$ is the compression of the DTFT-multiplication operator to $\ell^2(\mathbb{Z}_{\ge 0})$, i.e. $T[\hat G] = P_+\,M_{\hat G}\,P_+$ where $P_+$ projects onto non-negative-index sequences (equivalently, the Hardy space $H^2$ of the disk under the DTFT).

### 3.2 Szegő factorization

**Theorem 2 (Discrete Wiener–Hopf / Szegő factorization).** *Under (H), the symbol $\hat G$ admits a unique (up to a positive multiplicative constant absorbed into the split) factorization*
$$\hat G(\theta) \;=\; \hat G_+(\theta)\,\hat G_-(\theta),$$
*where $\hat G_+(z)$ extends to a bounded, nonzero analytic function on $\{|z|<1\}$ and $\hat G_-(z) = \overline{\hat G_+(\bar z^{-1})}$ extends analytically to $\{|z|>1\}$, with*
$$\log \hat G_\pm(\theta) \;=\; \tfrac12 \hat\ell_0 \;+\; \sum_{\pm k > 0} \hat\ell_k\,e^{ik\theta}, \qquad \hat\ell_k \;=\; \frac{1}{2\pi}\int_{-\pi}^\pi \log \hat G(\theta)\,e^{-ik\theta}\,d\theta,$$
*i.e. $\hat G_\pm$ are the Szegő outer factors constructed from the Fourier coefficients of $\log\hat G$.*

**Proof.** Under (H), $\log\hat G\in L^1(\mathbb{T})$ (in fact $L^\infty$), so the Szegő theorem (Szegő 1920; Grenander–Szegő 1958 §3; Böttcher–Silbermann 2006 §1.3) applies and the split $\log\hat G = (\log\hat G)_+ + (\log\hat G)_-$ with $(\log\hat G)_\pm$ the analytic (upper/lower) parts of $\log\hat G$ gives the factorization by exponentiation. Uniqueness follows from the normalization $\hat G_\pm(0) > 0$. $\blacksquare$

### 3.3 Half-line optimal rate

**Theorem 3 (Discrete half-line execution, no budget, deterministic).** *Under (H), the unique $\ell^2(\mathbb{Z}_{\ge 0})$ solution of $(\star_{\mathbb{Z}_{\ge 0}})$ is*
$$u^*_t \;=\; \bigl(\hat G_+^{-1}\,\Pi_+\,\hat G_-^{-1}\,\alpha\bigr)_t, \qquad t\ge 0,$$
*where $\Pi_+ = P_+$ is the Hardy projection onto non-negative-index Fourier modes on the unit circle. Explicitly, if $\hat\alpha(\theta) = \sum_{t\ge 0}\alpha_t e^{-it\theta}$ and $[f]_+$ denotes the truncation to non-negative-index Fourier coefficients,*
$$\hat u^*(\theta) \;=\; \hat G_+(\theta)^{-1}\;\bigl[\hat G_-(\theta)^{-1}\hat\alpha(\theta)\bigr]_+.$$

**Proof.** Extend $u$ by zero to $\mathbb{Z}$; the extended equation on $\mathbb{Z}$ is
$$M_{\hat G}\,u \;=\; \alpha \;+\; \phi_-, \qquad \phi_-\in\ell^2(\mathbb{Z}_{<0}),$$
where $\phi_-$ is the (unknown) residual carried by negative indices. In DTFT: $\hat G\,\hat u = \hat\alpha + \hat\phi_-$ with $\hat\phi_-$ analytic in $\{|z|>1\}$. Divide by $\hat G_-$:
$$\hat G_+\,\hat u \;=\; \hat G_-^{-1}\hat\alpha \;+\; \hat G_-^{-1}\hat\phi_-.$$
The LHS is analytic in $\{|z|<1\}$ (product of two disk-analytics); the last term on the RHS is analytic in $\{|z|>1\}$. Apply the split $\hat G_-^{-1}\hat\alpha = [\hat G_-^{-1}\hat\alpha]_+ + [\hat G_-^{-1}\hat\alpha]_-$ and match analyticity:
$$\hat G_+\,\hat u \;=\; [\hat G_-^{-1}\hat\alpha]_+, \qquad \hat G_-^{-1}\hat\phi_- \;=\; -[\hat G_-^{-1}\hat\alpha]_-.$$
Dividing by $\hat G_+$ gives the stated formula. $\blacksquare$

**Theorem 3$'$ (Adapted half-line policy).** *Under (H) applied to $(\star^{\mathcal{F}}_{\mathbb{Z}_{\ge 0}})$, the optimal $(\mathcal{F}_t)$-adapted trading rate on the half-line is characterized by inserting an optional projection between the two Szegő factors:*
$$u^*_t \;=\; \bigl(\hat G_+^{-1}\;P^{\rm o}\;\Pi_+\;\hat G_-^{-1}\,\alpha\bigr)_t, \qquad t\ge 0,$$
*where $P^{\rm o}$ is the optional projection $(P^{\rm o}X)_s := \mathbb{E}[X_s\mid\mathcal{F}_s]$. Equivalently, on the diagonal,*
$$u^*_t \;=\; \bigl(\hat G_+^{-1}\,\Pi_+\,\hat G_-^{-1}\,\bar\alpha_t(\cdot)\bigr)(t),$$
*and the equivalence of the two forms follows from the discrete optional-projection identity of Proposition 1.4 applied to the anti-causal factor $\hat G_-^{-1}$.*

**Proof.** The unconstrained WH policy of Theorem 3 minimizes the cost over all $\ell^2(\mathbb{Z}_{\ge 0})$ rates. Restricting to $(\mathcal{F}_t)$-adapted rates is a Hilbert-subspace constraint; the constrained optimizer is obtained by inserting the optional projection $P^{\rm o}$ between the two Szegő factors (the causal $\hat G_+^{-1}$ and anti-causal $\hat G_-^{-1}$), by the same causal/anti-causal Hilbert-splitting argument as Corollary 1.5. The Toeplitz projection $\Pi_+$ (which enforces the half-line domain) commutes with $P^{\rm o}$ since both are orthogonal projections in $\ell^2$ acting on disjoint index structure (time-support vs. filtration). The diagonal-form equivalence is Proposition 1.4 applied to $\hat G_-^{-1}$. $\blacksquare$

**Warning (as in Thm 1$'$).** Simply conditioning the deterministic WH policy of Theorem 3 on $\mathcal{F}_t$ does *not* derive Theorem 3$'$: the deterministic policy is not adapted, and pointwise conditioning is not the same as the projection-in-the-middle prescription. The forecast-curve form $\hat G_+^{-1}\Pi_+\hat G_-^{-1}\bar\alpha_t(\cdot)$ evaluated on the diagonal is a nontrivial *identity* that follows from Proposition 1.4, not from linearity of $\mathbb{E}$.

**Remark 3$'$.1.** As in the bulk case, all non-causality of the WH filter is quarantined into the anti-causal $\hat G_-^{-1}$ step, with adaptedness enforced by the projection $P^{\rm o}$ **between** the two Szegő factors. The half-line-specific Toeplitz projection $\Pi_+$ (which acts on the time index) is orthogonal to and does not interact with $P^{\rm o}$ (which acts on the filtration).

### 3.4 No homogeneous boundary correction

Unlike the continuous half-line problem of §5.3 of the companion paper — which admits a one-dimensional homogeneous boundary correction $\psi_\eta$ needed to enforce an initial-inventory constraint $X_0$ — the present setup has *no* such correction, because we impose no budget constraint. The kernel of $T[\hat G]$ on $\ell^2(\mathbb{Z}_{\ge 0})$ is trivial (a consequence of the Fredholm-index formula for Toeplitz operators with $\log\hat G\in L^\infty$: since $\hat G$ has winding number zero on the circle, $T[\hat G]$ is invertible; Böttcher–Silbermann 2006 §1.14). The solution of Theorem 3 is therefore the *unique* stationary point of the cost.

**Remark 2.1.** If a budget constraint $\sum_{t\ge 0} u_t = X_0$ were reintroduced, it would be enforced by adding a Lagrange multiplier $-\lambda$ to $\alpha_t$ in the FOC, giving
$$u^*_t \;=\; \bigl(\hat G_+^{-1}\Pi_+\hat G_-^{-1}(\alpha - \lambda\,\mathbf{1})\bigr)_t, \qquad \sum_t u^*_t = X_0,$$
with $\lambda$ fixed by the budget. This is a one-parameter perturbation of Theorem 3, not a new homogeneous mode. The discrete-time distinction from the continuous case (where a $\delta$-like block-trade mode appears at $\eta\to 0$) is that on the lattice, the $\eta\to 0$ limit is genuinely singular — Assumption (H) fails — and the problem is ill-posed without a positive diagonal.

### 3.5 Explicit factorization in the low-$\theta$ regime

Under (H) with $\eta$ close to the threshold $c\bar\eta(\gamma)$, or more generally at frequencies $|\theta|\ll\theta_*$ with $\theta_*$ solving $c_\gamma\theta^{\gamma-1} = \eta_{\rm eff}$, the symbol is dominated by the power-law part:
$$\hat G(\theta) \;\approx\; c_\gamma\,|\theta|^{\gamma-1}, \qquad |\theta|\ll\theta_*.$$
In this regime the discrete Szegő factors match the continuous WH factors of the companion paper (Proposition 5.5) at the origin:
$$\hat G_\pm(\theta) \;\approx\; c_\gamma^{1/2}\,(\mp i\theta)^{(\gamma-1)/2}, \qquad |\theta|\ll\theta_*.$$
At high frequencies $|\theta|\gtrsim\theta_*$, the constant $\eta_{\rm eff}$ dominates and $\hat G_\pm\to\sqrt{\eta_{\rm eff}}$; the half-line policy transitions to direct signal-following $u^*_t\approx\alpha_t/\hat G(\theta)$ per Fourier mode, matching the crossover of §5.3.4 of the companion paper.

### 3.6 Levinson recursion computation

Numerically, the Szegő factors $\hat G_\pm$ (equivalently, the *predictor–corrector coefficients* $\hat\ell_k$) are computable in $O(N\log N)$ via FFT of $\log\hat G(\theta_j)$ on an equispaced grid $\{\theta_j\}_{j=0}^{N-1}$:

**Algorithm (Discrete WH via FFT).**
1. Choose a grid $\theta_j = 2\pi j/N$, $j=0,\ldots,N-1$.
2. Evaluate $\hat G(\theta_j)$ using the polylog identity or by truncated summation of $G_k$.
3. Compute $\hat\ell_k = \mathrm{IFFT}[\log\hat G(\theta_j)]_k$, $k=0,\ldots,N-1$.
4. Form $\log\hat G_+(\theta_j) = \tfrac12\hat\ell_0 + \sum_{k=1}^{N/2}\hat\ell_k e^{ik\theta_j}$ and $\log\hat G_-(\theta_j) = \tfrac12\hat\ell_0 + \sum_{k=N/2+1}^{N-1}\hat\ell_k e^{ik\theta_j}$; exponentiate.
5. Compute $\hat u^*(\theta_j) = \hat G_+(\theta_j)^{-1}\mathrm{FFT}\bigl[\mathrm{IFFT}[\hat G_-(\theta_j)^{-1}\hat\alpha(\theta_j)]\cdot\mathbf{1}_{k\ge 0}\bigr]$; inverse-FFT to get $u^*_t$.

Total cost: $O(N\log N)$ per call, exact up to grid discretization ($O(N^{-1})$ aliasing in the Szegő split).

Alternatively, the Toeplitz matrix $T[\hat G]$ restricted to a size-$N$ window admits a Levinson–Durbin recursion in $O(N^2)$, giving the exact discrete-WH inverse without grid discretization. For very large $N$, the superfast Toeplitz solvers of Ammar–Gragg (1988) reduce this to $O(N\log^2 N)$.

## 4. Comparison of the two policies

| Domain | Optimal rate | Boundary content | Computation |
| :--- | :--- | :--- | :--- |
| $\mathbb{Z}$ | $u^*_t = (R * \alpha)_t$, $R = \mathrm{IFFT}[1/\hat G]$ | none | $O(N\log N)$ |
| $\mathbb{Z}_{\ge 0}$ | $u^*_t = \hat G_+^{-1}\Pi_+\hat G_-^{-1}\alpha$ | none (no budget) | $O(N\log N)$ Szegő / $O(N^2)$ Levinson |

Both policies are pure signal responses to $\alpha$: convolution with a resolvent kernel on $\mathbb{Z}$, and a WH-projected filter on $\mathbb{Z}_{\ge 0}$. The half-line policy differs from the bulk policy only by the insertion of $\Pi_+$ between the two half-order Szegő factors — the discrete analogue of the causal projection in the continuous companion paper's Corollary 5.7.

The two policies agree deep in the interior of $\mathbb{Z}_{\ge 0}$: for $t\gg\theta_*^{-1}$, the WH projection $\Pi_+$ acts trivially on the "already causal" part of the signal, and the half-line policy converges to the bulk policy. The edge effect is confined to $t \lesssim\theta_*^{-1}$, the reciprocal of the crossover scale.

## 5. Relation to the continuous companion paper

Setting up the correspondence:

| Continuous quantity | Discrete quantity |
| :--- | :--- |
| Kernel $G(\tau) = c\,\tau^{-\gamma}$ | $G_k = c\,k^{-\gamma}$ for $k\ge 1$, $G_0 = 2\eta$ |
| FT $\hat G(\xi) = c_\gamma|\xi|^{\gamma-1} + \eta$ | DTFT $\hat G(\theta) = 2\eta + 2c\mathrm{Re}\mathrm{Li}_\gamma(e^{i\theta})$ |
| Bulk theorem (Thm 4.1) | Theorem 1 |
| Bulk-symbol WH ($D_\pm^\beta$) | Grünwald–Letnikov $\Delta_\pm^\beta$ (Cor 1.1) |
| Half-line WH (Cor 5.7) | Theorem 3 (Szegő factorization) |
| Continuous $\Pi_+$ (Hardy-space, upper half-plane) | Discrete $\Pi_+$ (Hardy-space, disk) |
| Continuous $M_\pm$ | Discrete Szegő factors $\hat G_\pm$ |
| Continuous $\psi_\eta$ (Prop 5.8) | Absent (no budget constraint) |
| Forecast curve $\bar\alpha(t,s)$ | Discrete forecast curve $\bar\alpha_t(s)$ |
| Lemma 1 (optional-projection identity) | Proposition 1.4 (discrete optional projection) |
| Adapted bulk (Thm 4.1) | Theorem 1$'$ |
| Adapted half-line (Cor 5.7) | Theorem 3$'$ |
| Crossover $\xi_*(\eta) = (c_\gamma/\eta)^{1/(1-\gamma)}$ | Same, in $\theta$-units |

**Fine-grid limit.** For $\Delta t\to 0$ with $c\to c\,\Delta t^{-\gamma}$ (so that the continuous kernel is recovered) and $\eta \to \eta\,\Delta t^{-1}$, the discrete FOC and its solution converge to the continuous FOC and solution pointwise in $t = k\Delta t$ under standard regularity assumptions on $\alpha$. The lattice-specific correction $c\,\zeta(\gamma)$ to $\eta_{\rm eff}$ is subleading in $\Delta t$.

**Missing piece: budget-constrained discrete.** Reintroducing $\sum u_t = X_0$ adds a Lagrange multiplier that shifts $\alpha \mapsto \alpha - \lambda\mathbf{1}$; the resulting policy differs from Theorem 3 only through $\lambda$, and the "block trade" $\delta$-mode of the continuous $\eta\to 0$ limit does not appear on the lattice under (H). A companion treatment of the $\eta \to c\bar\eta(\gamma)^+$ limit (approach to the loss of positivity) is a natural next step and is left open.

## 6. Well-posedness and stability

**Proposition 3.1 (Stability constants).** *Under (H), the resolvent operator has operator norms*
$$\|R\|_{\ell^2\to\ell^2} \;=\; \sup_\theta \hat G(\theta)^{-1} \;=\; \bigl(2\eta - 2c\bar\eta(\gamma)\bigr)^{-1},$$
*attained at $\theta = \pi$, and the half-line WH operator has*
$$\|\hat G_+^{-1}\Pi_+\hat G_-^{-1}\|_{\ell^2\to\ell^2} \;\le\; \sup_\theta\hat G(\theta)^{-1} \;=\; \bigl(2\eta - 2c\bar\eta(\gamma)\bigr)^{-1}$$
*(strict inequality is generic; equality when $\hat G$ has vanishing imaginary part of $\log\hat G$).*

**Proof.** The first identity is Plancherel and the second is Böttcher–Silbermann (2006) §2.7. $\blacksquare$

**Corollary 3.2.** *Both the bulk and half-line optimal rates are bounded linear functions of the signal in $\ell^2$; the $\ell^2$-norm of $u^*$ is at most $(2\eta-2c\bar\eta(\gamma))^{-1}\|\alpha\|_{\ell^2}$.*

## 7. Numerical illustration (recipe)

To reproduce the discrete bulk and half-line policies:

```python
import numpy as np
from numpy.fft import fft, ifft

def build_symbol(N, c, gamma, eta):
    theta = 2 * np.pi * np.arange(N) / N
    # Kernel G_k for k in Z, size N (using positive-index wrap for FFT)
    k = np.arange(N)
    G = np.where(k == 0, 2 * eta, c * np.where(k <= N // 2, k, N - k) ** (-gamma))
    G[0] = 2 * eta
    Ghat = np.real(fft(G))  # DTFT samples at theta_j
    return theta, Ghat

def bulk_policy(alpha, c, gamma, eta):
    N = len(alpha)
    _, Ghat = build_symbol(N, c, gamma, eta)
    return np.real(ifft(fft(alpha) / Ghat))

def half_line_policy(alpha_half, c, gamma, eta, N_pad):
    # Zero-pad alpha_half to length N_pad to reduce aliasing
    alpha = np.zeros(N_pad); alpha[:len(alpha_half)] = alpha_half
    _, Ghat = build_symbol(N_pad, c, gamma, eta)
    # Szegő factorization via log-FFT split
    log_G = np.log(Ghat)
    ell = ifft(log_G).real  # Fourier coefficients of log G
    ell_plus = np.zeros(N_pad); ell_plus[0] = ell[0] / 2
    ell_plus[1:N_pad//2] = ell[1:N_pad//2]
    ell_minus = np.zeros(N_pad); ell_minus[0] = ell[0] / 2
    ell_minus[N_pad//2+1:] = ell[N_pad//2+1:]
    G_plus = np.exp(fft(ell_plus))
    G_minus = np.exp(fft(ell_minus))
    # Apply G_-^{-1}, Pi_+ (project to k >= 0), G_+^{-1}
    step1 = ifft(fft(alpha) / G_minus).real
    step1[len(alpha_half):] = 0  # truncate to half-line
    step2 = ifft(fft(step1) / G_plus).real
    return step2[:len(alpha_half)]
```

This is illustrative; a production implementation should use windowing to reduce Gibbs oscillation at $\theta = \pm\pi$ (where $\log\hat G$ is smooth but the FFT-based split has $O(N^{-1})$ error) and Levinson recursion for exact factorization on modest $N$.

**⚠️ Not yet run.** The code above is an implementation recipe, not a verified experiment. A convergence test against the continuous bulk policy on a smooth signal (e.g. $\alpha_t = e^{-|t|/T_0}$ for various $T_0$) is a natural sanity check and is left to a follow-up numerical note.

## 8. Open questions

1. **Explicit Szegő factorization for the pure power-law $\hat G(\theta) = 2c\,\mathrm{Re}\,\mathrm{Li}_\gamma(e^{i\theta})$** (i.e. $\eta = 0$): does it admit a hypergeometric or polylog closed form via Ramanujan's identities on $\mathrm{Li}_\gamma$? The continuous case has $M_\pm = c_\gamma^{1/2}(\mp i\xi)^{(\gamma-1)/2}$; the discrete analogue is not immediate.
2. **Budget-constrained discrete half-line**: reintroduce $\sum u_t = X_0$ and characterize the Lagrange-multiplier map $X_0\mapsto\lambda$; is $\lambda(X_0)$ linear in $X_0$ (yes, by linearity of the FOC), and what is the slope in terms of $\hat G_\pm(0)$?
3. **Regularization of the $\eta\to c\bar\eta(\gamma)^+$ limit**: the loss of positivity of $\hat G$ at the Nyquist frequency is a distinct singular limit from the continuous $\eta\to 0$. What is the correct discrete analogue of the continuous $\psi_\eta$ mode in this limit?
4. **Multi-asset extension**: matrix-valued $G_k$ and matrix Szegő factorization. Discrete analogue of Theorem 7.1 of the companion paper.

## References

- **Companion paper**: *Fractional-derivative optimal execution* (`papers/fractional-derivative-optimal-execution.md`), Theorems 4.1, 5.5, 5.8, Corollary 5.7.
- Böttcher, A., Silbermann, B. *Analysis of Toeplitz Operators*, 2nd ed. Springer, 2006.
- Grenander, U., Szegő, G. *Toeplitz Forms and Their Applications*. UC Press, 1958.
- Ammar, G. S., Gragg, W. B. Superfast solution of real positive definite Toeplitz systems. *SIAM J. Matrix Anal.* 9(1), 1988.
- Erdélyi, A. et al. *Higher Transcendental Functions* Vol. 1 (Bateman). McGraw-Hill, 1953. §1.11.
- Wood, D. C. The computation of polylogarithms. Kent Tech. Report 15/92, 1992.
- Szegő, G. Beiträge zur Theorie der Toeplitzschen Formen. *Math. Z.* 6, 1920.

---

## Status

- **Draft v1.** Theorems 1–3 and Corollary 1.1 are stated with proofs; Proposition 1.3 is stated with a proof sketch. The numerical recipe in §7 is illustrative and **not yet run**. The four open questions of §8 are genuinely open in the current draft.
- **No experimental results.** This is a purely analytical companion; no simulations, no fits, no benchmark tables.
- **Blocked / Unverified**: (a) explicit Szegő factorization of the pure-power-law symbol; (b) numerical convergence of the discrete policy to the continuous companion policy on a canonical test signal; (c) budget-constrained variant.
