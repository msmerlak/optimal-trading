# DRAFT — Appendix to be appended to `papers/noisy-signal-impact-trading.md`

This file contains only the new appendix sections (A and B) and a short reference cross-reference. They are intended to be inserted **between §11 Conclusion and `## Sources`** of the main paper.

---

## Appendix A. Definitions

This appendix collects the formal objects used implicitly throughout the paper. Conventions: time index $t \in \mathbb{Z}$ in discrete sections, $t \in \mathbb{R}$ in continuous sections (§6.2, §6.3, §8.2); the unit circle is $\mathbb{T} = \{z \in \mathbb{C} : |z|=1\}$; for a real-valued time series $x$, we write $\hat x(z) = \sum_t x_t z^{-t}$ for the bilateral $z$-transform when it converges, and $\hat x(\omega) = \hat x(e^{i\omega})$ on $\mathbb{T}$.

**Definition A.1 (Signal and trade-rate processes).** A *signal* $f = (f_t)_{t\in\mathbb{Z}}$ is a real, zero-mean, wide-sense-stationary (WSS) process with absolutely summable autocovariance $\gamma_f(k) = \mathbb{E}[f_t f_{t+k}]$, equivalently a continuous positive spectral density $S_f$ on $\mathbb{T}$. A *trade-rate process* $x = (x_t)_{t\in\mathbb{Z}}$ is any real process adapted to a given filtration $\{\mathcal F_t\}$; the *position* is $q_t = \sum_{s \le t} x_s$. The *causal admissible class* $\mathcal A^c$ consists of WSS $x$ of the form $x_t = (H * f)_t$ with $H : \mathbb{Z}_{\ge 0} \to \mathbb{R}$ satisfying $\sum_k H(k)^2 S_f$-essentially bounded, so that $\mathbb{E}[x_t^2] < \infty$.

**Definition A.2 (Admissible impact kernel).** An *admissible symmetric impact kernel* is a real function $K : \mathbb{Z} \to \mathbb{R}$ with $K(n) = K(-n)$, $\sum_n |K(n)| < \infty$ or — for the power-law case — $K$ a positive-definite tempered distribution, and Fourier transform $\hat K(\omega) > 0$ for all $\omega \in \mathbb{T}$ (resp. for all $\omega \in \mathbb{R}$). The continuous-time analogue $K : \mathbb{R} \to \mathbb{R}$ has the same definition with $\mathbb{R}$ replacing $\mathbb{Z}$ and Fourier transform on $\mathbb{R}$. The *one-sided* kernel is $G(n) := K(n)$ for $n \ge 0$ (§2.1).

**Definition A.3 (Cost inner product and cost norm).** For $x, x' \in \ell^2(\mathbb{Z})$,
$$
\langle x, x'\rangle_K \;:=\; \sum_{s,t} x_t\, K(t-s)\, x'_s \;=\; \int_{-\pi}^{\pi} \hat x(\omega)^* \hat K(\omega)\, \hat x'(\omega)\,\frac{d\omega}{2\pi},
$$
with associated norm $\|x\|_K^2 := \langle x,x\rangle_K$. Positivity of $\hat K$ (Definition A.2) makes $\langle\cdot,\cdot\rangle_K$ an inner product on $\ell^2$ (cf. Theorem B.1).

**Definition A.4 (Hardy spaces and causal/anticausal projections).** Let $L^2(\mathbb{T})$ be square-integrable functions on the unit circle with the Plancherel inner product $\langle f, g\rangle = \int f^* g\, d\omega/(2\pi)$. The *causal Hardy space* $H^2_+(\mathbb{T})$ is the closed subspace of $L^2(\mathbb{T})$ spanned by $\{e^{-ik\omega} : k \ge 0\}$ — equivalently, the boundary values of functions analytic on $\{|z| > 1\}$ and decaying at infinity. The *anticausal* Hardy space $H^2_-(\mathbb{T})$ is the orthogonal complement, spanned by $\{e^{ik\omega} : k \ge 1\}$. The *causal projection* $[\cdot]_+ : L^2(\mathbb{T}) \to H^2_+$ and *anticausal projection* $[\cdot]_-$ are the orthogonal projections; in $z$-transform terms, $[\sum_k c_k z^{-k}]_+ = \sum_{k \ge 0} c_k z^{-k}$ and $[\cdot]_- = I - [\cdot]_+$.

**Definition A.5 (Outer spectral factor).** An admissible spectral density $\hat K$ (Definition A.2) satisfies the *Szegő / Paley–Wiener condition*
$$
\int_{-\pi}^{\pi} \log \hat K(\omega)\,\frac{d\omega}{2\pi} \;>\; -\infty. \tag{A.1}
$$
Under (A.1) there exists a unique (up to a unimodular constant) *outer function* $\hat K_+ \in H^2_+$ with $\hat K(\omega) = |\hat K_+(\omega)|^2 = \hat K_+(\omega)\,\hat K_-(\omega)$, where $\hat K_-(\omega) := \overline{\hat K_+(\omega)} = \hat K_+(\omega^{-1})$ is the anticausal factor (see Theorem B.4). Both $\hat K_+$ and $\hat K_+^{-1}$ lie in $H^2_+$ in the bounded case; in the power-law case the same factorisation is defined via the upper-half-plane analogue with $\hat K_+(\omega) \propto (i\omega)^{(\beta-1)/2}$.

**Definition A.6 (Causal Wiener filter).** Given an observation $\tilde f_t = f_t + \eta_t$ with $\eta \perp f$ both WSS, the *causal Wiener filter* is the unique $W \in H^2_+$ minimising $\mathbb{E}[(f_t - (W*\tilde f)_t)^2]$. Its closed form is
$$
\hat W(z) \;=\; \frac{1}{\hat\phi^+(z)}\Bigg[\frac{S_f(z)}{\hat\phi^-(z)}\Bigg]_+,
$$
where $S_{\tilde f} = \hat\phi^+\hat\phi^-$ is the spectral factorisation of the observed spectrum (Wiener 1949).

**Definition A.7 (Marchaud anticausal fractional derivative).** For $\alpha \in (0, 1)$ and $f$ a function on $\mathbb{R}$ with sufficient regularity (Hölder $\beta > \alpha$ suffices), the *anticausal Marchaud fractional derivative* of order $\alpha$ is
$$
(\mathcal D^\alpha_- f)(t) \;:=\; \frac{1}{\Gamma(-\alpha)}\int_0^\infty s^{-\alpha-1}\,[f(t+s) - f(t)]\,ds, \tag{A.2}
$$
and the *causal* Marchaud derivative $\mathcal D^\alpha_+ f$ is given by $s \mapsto -s$ in (A.2). The regularising subtraction $-f(t)$ makes the integral converge despite the non-integrability of $s^{-\alpha-1}$ at $s=0$ (Samko–Kilbas–Marichev 1993, §5).

**Definition A.8 (Discrete fractional difference operator).** With $L$ the backward shift $(Lf)_t = f_{t-1}$, the *causal fractional difference of order $\alpha \in \mathbb{R}$* is
$$
\Delta^\alpha_+ \;:=\; (1 - L)^\alpha \;=\; \sum_{m \ge 0} \binom{\alpha}{m}(-L)^m,
\qquad \binom{\alpha}{m} \;=\; \frac{\alpha(\alpha-1)\cdots(\alpha-m+1)}{m!}, \tag{A.3}
$$
with the generalised binomial coefficients. The *anticausal* version $\Delta^\alpha_- = (1 - L^{-1})^\alpha$ replaces $L$ by $L^{-1}$. Convergence in $\ell^2$ on stationary inputs holds for $\alpha > -1/2$ (Granger–Joyeux 1980; Hosking 1981).

**Definition A.9 (Kernel innovation).** For an admissible kernel $K$ with outer factor $K_+$ (Definition A.5) and signal $f$, the *kernel innovation of $f$ with respect to $K$* is
$$
\iota^K_t \;:=\; (K_+^{-1} * f)_t.
$$
For $K(n) = \lambda^{|n|}$ this is $(f_t - \lambda f_{t-1})/\sqrt{1-\lambda^2}$ (eq. (12)); for the continuous-time power-law kernel it is the causal Marchaud derivative $\mathcal D^{(1-\beta)/2}_+ f$ (eq. (14)); for the discrete fractional-differencing kernel it is $\Delta^\alpha_+ f$ (Table 1).

---

## Appendix B. Proofs

Each theorem corresponds to a load-bearing claim in the main text; the cross-reference is given in the statement.

### B.1 Positive-definiteness ⇔ No dynamic arbitrage (§2.4)

**Theorem B.1.** *Let $K$ be a real, symmetric kernel on $\mathbb{Z}$ with absolutely summable autocovariance, and let $\hat K$ denote its Fourier transform on $\mathbb{T}$. The following are equivalent:*

1. *The cost form $\mathcal C(x) = \tfrac{1}{2}\sum_{s,t} x_s K(t-s) x_t$ is strictly positive on every finite-support sequence $x \ne 0$.*
2. $\hat K(\omega) > 0$ for almost every $\omega \in \mathbb{T}$.
3. *No finite-support round-trip $x$ (i.e. $\sum_t x_t = 0$, $x_t = 0$ outside a finite window) has $\mathcal C(x) \le 0$; equivalently, no manipulation strategy generates a positive expected price increment with negative cost (Gatheral [Gat10]).*

*Proof.* (1) $\Leftrightarrow$ (2) is Bochner's theorem. By the Parseval–Plancherel identity, for any finite-support $x$ with $z$-transform $\hat x \in L^2(\mathbb{T})$,
$$
2\,\mathcal C(x) \;=\; \langle x, K*x\rangle \;=\; \int_{-\pi}^{\pi} |\hat x(\omega)|^2\, \hat K(\omega)\,\frac{d\omega}{2\pi}. \tag{B.1}
$$
If $\hat K > 0$ a.e., (B.1) shows $\mathcal C(x) > 0$ for $x \ne 0$ (since $\hat x \not\equiv 0$). Conversely, if $\hat K(\omega_0) < 0$ on a positive-measure set, choose a band-limited $x$ with $|\hat x|$ supported there; then (B.1) gives $\mathcal C(x) < 0$, contradicting positivity.

(2) $\Leftrightarrow$ (3) is Theorem 1 of Gatheral [Gat10]: a round-trip strategy has expected revenue $-\mathcal C(x)$ (the negative of the impact cost), so a profitable round-trip exists iff $\mathcal C(x) < 0$ for some $x$ with $\sum_t x_t = 0$, which by (B.1) is iff $\hat K$ takes negative values. $\square$

### B.2 Legendre–Fenchel duality (§3.2, eq. (2))

**Theorem B.2.** *Let $\phi(x) = \tfrac{1}{2}\|x\|_K^2$ with $K$ admissible (Def. A.2). Then the convex conjugate $\phi^*(f) = \sup_x[\langle f,x\rangle - \phi(x)]$ equals $\tfrac{1}{2}\|f\|_{K^{-1}}^2$, with the supremum attained at $x^\star = K^{-1} * f$.*

*Proof.* Differentiate the concave functional $x \mapsto \langle f, x\rangle - \tfrac{1}{2}\langle x, K*x\rangle$: the FOC reads $f - K*x = 0$, so $x^\star = K^{-1}*f$ (well-defined since $\hat K > 0$ a.e., so $\hat K^{-1} \in L^\infty_{\text{loc}}$). Substituting,
$$
\phi^*(f) \;=\; \langle f, x^\star\rangle - \tfrac{1}{2}\langle x^\star, K*x^\star\rangle \;=\; \langle f, K^{-1}*f\rangle - \tfrac{1}{2}\langle K^{-1}*f, f\rangle \;=\; \tfrac{1}{2}\|f\|_{K^{-1}}^2. \quad\square
$$

### B.3 Wiener–Hopf first-order condition (§4.1, eqs. (4)–(6))

**Theorem B.3.** *Let $K$ be admissible. The functional $\mathcal J(x) = \langle f, x\rangle - \tfrac{1}{2}\langle x, K*x\rangle$ has a unique maximiser on the causal subspace $\mathcal A^c$. The maximiser $x^*$ is characterised by*
$$
\big[K*x^* - f\big]_+ \;=\; 0, \tag{B.2}
$$
*and is given in $z$-transform form by*
$$
\hat x^*(z) \;=\; \hat K_+^{-1}(z)\,\bigl[\hat f(z) / \hat K_-(z)\bigr]_+. \tag{B.3}
$$

*Proof.* Causal admissible $x$ form a closed convex subspace of $L^2(\mathbb{T})$ in $z$-transform (Def. A.4). Strict concavity of $\mathcal J$ follows from Theorem B.1, giving uniqueness. The FOC requires the Gâteaux derivative $D\mathcal J(x)[h] = \langle f - K*x, h\rangle$ to vanish for all causal $h$, i.e. $f - K*x \perp H^2_+$, equivalently $[K*x - f]_+ = 0$.

Factor $\hat K = \hat K_+ \hat K_-$ (Theorem B.4). Set $\hat y(z) := \hat K_+(z)\hat x(z)$, which lies in $H^2_+$ iff $\hat x$ does (since $\hat K_+$ is outer). Then $\hat K(z)\hat x(z) = \hat K_-(z)\hat y(z)$, and (B.2) becomes
$$
[\hat K_-(z)\hat y(z) - \hat f(z)]_+ = 0
\;\Longleftrightarrow\; \hat y(z) - [\hat f(z)/\hat K_-(z)]_+ \in H^2_-,
$$
using that multiplication by anticausal $\hat K_-$ preserves $H^2_-$. Since $\hat y \in H^2_+$, the difference must vanish: $\hat y(z) = [\hat f(z)/\hat K_-(z)]_+$, giving (B.3). $\square$

### B.4 Spectral factorisation (§4.2)

**Theorem B.4 (Szegő factorisation).** *Let $\hat K \in L^1(\mathbb{T})$ with $\hat K \ge 0$ and the Paley–Wiener / Szegő condition $\int \log \hat K\,d\omega/(2\pi) > -\infty$ (eq. (A.1)). Then there exists a unique outer function $\hat K_+ \in H^2_+$ with $\hat K_+(\infty) > 0$ and $|\hat K_+(\omega)|^2 = \hat K(\omega)$ a.e. Setting $\hat K_-(\omega) := \overline{\hat K_+(\omega)}$ gives $\hat K = \hat K_+\hat K_-$.*

*Proof.* Standard; we record the construction. Define
$$
\hat K_+(z) \;:=\; \exp\!\Bigg(\tfrac{1}{2}\int_{-\pi}^{\pi}\log\hat K(\theta)\,\frac{e^{i\theta}+z^{-1}}{e^{i\theta}-z^{-1}}\,\frac{d\theta}{2\pi}\Bigg), \qquad |z| > 1, \tag{B.4}
$$
which is the exponential of the *Schwarz integral* of $\tfrac{1}{2}\log\hat K$. By construction $\hat K_+$ is analytic and zero-free on $\{|z|>1\}$; its non-tangential boundary values exist a.e. and satisfy $|\hat K_+(\omega)|^2 = \exp(\log\hat K(\omega)) = \hat K(\omega)$. Outer functions are characterised by maximising $|\hat K_+(\infty)| = \exp(\int \tfrac{1}{2}\log\hat K\,d\omega/(2\pi))$ among $H^2_+$ functions with the same modulus on $\mathbb{T}$ (Hoffman, *Banach Spaces of Analytic Functions*, Ch. 5); uniqueness up to a unimodular constant follows. The normalisation $\hat K_+(\infty) > 0$ fixes that constant.

For the power-law continuous-time case $\hat K(\omega) = c|\omega|^{\beta-1}$, the analogous outer function on the upper half-plane is $\hat K_+(\omega) = c^{1/2}(i\omega)^{(\beta-1)/2}$ with the principal branch; this is the standard fractional-integration symbol (Samko–Kilbas–Marichev 1993, §7), and recovers (13). $\square$

*Remark.* The Szegő condition (A.1) is satisfied by every kernel considered in the paper: the exponential kernel $\hat K(\omega) = (1-\lambda^2)/|1-\lambda e^{-i\omega}|^2$ is bounded away from $0$, hence $\log \hat K \in L^\infty(\mathbb{T})$; the power-law kernel has only a logarithmic singularity in $\log \hat K$ at $\omega = 0$, which is integrable.

### B.5 AR(1) Markov-closure identity (§5.5, eq. (12c))

**Theorem B.5.** *Let $f$ be a WSS AR(1) process with $f_t = \rho f_{t-1} + \epsilon_t$, $|\rho| < 1$, $\epsilon_t$ i.i.d. with $\mathbb{E}\epsilon_t^2 = \sigma^2 < \infty$. Let $\hat K_-^{-1}(z) = \sum_{m \ge 0} a_m z^m$ converge for $|z| \le |\rho|^{-1}$. Then the causal projection of the anticausal filter satisfies*
$$
[K_-^{-1} * f]_+(t) \;=\; \hat K_-^{-1}(\rho)\, f_t, \quad\text{a.s.} \tag{B.5}
$$
*If $f$ is in addition Gaussian, the equality holds in $L^2(\mathbb{P})$ with $[\cdot]_+$ the orthogonal projection onto the $\sigma$-algebra $\mathcal F_t^f$; for general WSS $f$ it holds with $[\cdot]_+$ the linear projection onto $\overline{\mathrm{span}}\{f_s : s \le t\}$.*

*Proof.* The action of $K_-^{-1}$ as an anticausal sum (eq. (12a)) is $(K_-^{-1}*f)_t = \sum_{m \ge 0} a_m f_{t+m}$, which converges in $L^2$ when $\sum_m a_m^2 \rho^{2m} < \infty$ — guaranteed by the convergence assumption.

For Gaussian $f$, the deterministic causal projection $[\cdot]_+$ on $z$-transforms coincides with conditional expectation onto $\mathcal F_t^f$ (Doob, *Stochastic Processes*, Ch. XII §5; this is the standard equivalence of orthogonal projection in $L^2$ to conditional expectation for jointly Gaussian families). For general WSS $f$, it equals the wide-sense linear projection (Hannan, *Multiple Time Series*, Ch. III). In either case, by linearity and dominated convergence,
$$
[K_-^{-1}*f]_+(t) \;=\; \sum_{m \ge 0} a_m\, \mathbb{E}[f_{t+m}\mid \mathcal F_t^f]. \tag{B.6}
$$
The AR(1) Markov property gives $\mathbb{E}[f_{t+m}\mid \mathcal F_t^f] = \rho^m f_t$ (iterate the recursion: $f_{t+1} = \rho f_t + \epsilon_{t+1}$ with $\epsilon_{t+1} \perp \mathcal F_t^f$). Substituting into (B.6),
$$
[K_-^{-1}*f]_+(t) \;=\; \Big(\sum_{m \ge 0} a_m \rho^m\Big)\,f_t \;=\; \hat K_-^{-1}(\rho)\,f_t. \quad\square
$$

*Verification of (10).* For the exponential kernel, $\hat K_-^{-1}(z) = (1-\lambda z)/\sqrt{1-\lambda^2}$, so $\hat K_-^{-1}(\rho) = (1-\lambda\rho)/\sqrt{1-\lambda^2}$, reproducing the §5.3 partial-fraction result.

### B.6 Frullani / Γ-identity for OU × power-law (§6.3, eq. (15b))

**Theorem B.6.** *For $\alpha \in (0,1)$ and $\kappa > 0$,*
$$
\int_0^\infty s^{-\alpha-1}\,(e^{-\kappa s} - 1)\,ds \;=\; \Gamma(-\alpha)\,\kappa^\alpha. \tag{B.7}
$$
*Consequently, if $f$ is an OU process with mean-reversion rate $\kappa$ ($\mathbb{E}[f(t+s)|\mathcal F_t] = e^{-\kappa s}f(t)$), the Marchaud anticausal derivative $\mathcal D^\alpha_-$ (Def. A.7) satisfies $\mathbb{E}[(\mathcal D^\alpha_- f)(t)\mid \mathcal F_t] = \kappa^\alpha f(t)$.*

*Proof.* Substitute $u = \kappa s$:
$$
\int_0^\infty s^{-\alpha-1}(e^{-\kappa s}-1)\,ds \;=\; \kappa^\alpha \int_0^\infty u^{-\alpha-1}(e^{-u}-1)\,du.
$$
For the right-hand integral, integrate by parts with $dv = (e^{-u}-1)\,du$ and $w = u^{-\alpha-1}$; both boundary terms vanish for $\alpha \in (0,1)$ (the integrand $u^{-\alpha}(e^{-u}-1)$ is $O(u^{1-\alpha}) \to 0$ at $0$ and $O(u^{-\alpha}e^{-u}) \to 0$ at $\infty$), giving
$$
\int_0^\infty u^{-\alpha-1}(e^{-u}-1)\,du \;=\; -\frac{1}{\alpha}\int_0^\infty u^{-\alpha}\,e^{-u}\,du \;\cdot\;(-1) \cdot (-1) \;=\; -\frac{1}{\alpha}\,\Gamma(1-\alpha),
$$
where $\int_0^\infty u^{-\alpha}e^{-u}\,du = \Gamma(1-\alpha)$ by the definition of the Gamma function. The functional equation $\Gamma(1-\alpha) = -\alpha\,\Gamma(-\alpha)$ then yields
$$
\int_0^\infty u^{-\alpha-1}(e^{-u}-1)\,du \;=\; -\frac{1}{\alpha}\cdot(-\alpha\Gamma(-\alpha)) \;=\; \Gamma(-\alpha),
$$
which proves (B.7). The OU consequence follows by linearity of conditional expectation applied to (A.2) using $\mathbb{E}[f(t+s)-f(t)\mid\mathcal F_t] = (e^{-\kappa s}-1)f(t)$. $\square$

*Numerical sanity.* The identity (B.7) is verified by `experiments/markov_closure_check.py`. The script's output `experiments/results/markov_closure_check.out` records the ratio of a crude trapezoidal estimate of the LHS to $\Gamma(-\alpha)$; mid-range $\alpha \in [0.25, 0.75]$ agrees to within 0.5%, while the endpoints lose precision as expected for a non-adaptive quadrature applied to a singular integrand. The identity itself is exact.

### B.7 ARFIMA / generalised binomial closure (§6.3, eq. (15c))

**Theorem B.7.** *Let $\Delta^\alpha_- = (1 - L^{-1})^\alpha$ (Def. A.8, anticausal version) and $f$ AR(1) with parameter $\rho$, $|\rho|<1$. Then*
$$
[\Delta^\alpha_- f]_+(t) \;=\; (1-\rho)^\alpha\, f_t. \tag{B.8}
$$

*Proof.* The anticausal fractional difference has $z$-transform $\hat{\Delta}^\alpha_-(z) = (1-z)^\alpha$, expanding to $\sum_{m\ge 0}\binom{\alpha}{m}(-z)^m$ (the generalised binomial series; Hosking 1981 Theorem 1; Granger–Joyeux 1980). Setting $a_m = \binom{\alpha}{m}(-1)^m$ and applying Theorem B.5,
$$
[\Delta^\alpha_- f]_+(t) \;=\; \Big(\sum_{m\ge 0}\binom{\alpha}{m}(-\rho)^m\Big) f_t \;=\; (1-\rho)^\alpha\, f_t,
$$
where the final equality is the generalised binomial theorem evaluated at $-\rho$ for $|\rho| < 1$. The series converges absolutely for $|\rho| < 1$ and all $\alpha \in \mathbb{R}$; for $\alpha \in (-1/2, 1/2)$ the operator preserves WSS $\ell^2$ inputs (Hosking 1981 §2). $\square$

*Numerical sanity.* The series identity $\sum_{m\ge 0}\binom{\alpha}{m}(-\rho)^m = (1-\rho)^\alpha$ is verified to $\sim 7$ decimal places for $\alpha \in \{0.25, 0.5, 0.75\}$ and $\rho \in \{0.3, 0.7, 0.95\}$ in `experiments/markov_closure_check.py` (output file `experiments/results/markov_closure_check.out`).

### B.8 Separation principle (§7.3)

**Theorem B.8 (Denoise-then-trade).** *Let $f, \eta$ be independent, jointly Gaussian, zero-mean, WSS processes; let $\tilde f_t = f_t + \eta_t$, and let the agent observe the filtration $\tilde{\mathcal F}_t = \sigma(\tilde f_s : s \le t)$. Assume $K$ is admissible (Def. A.2). Then the maximiser of $\mathcal J(x) = \mathbb{E}[f_t x_t - \tfrac{1}{2}x_t(K*x)_t]$ over $\tilde{\mathcal F}$-causal WSS $x$ is*
$$
\hat x^*(z) \;=\; \hat K_+^{-1}(z)\,\bigl[\hat f^W(z)/\hat K_-(z)\bigr]_+, \tag{B.9}
$$
*where $f^W_t := \mathbb{E}[f_t \mid \tilde{\mathcal F}_t]$ is the causal Wiener filter output (Def. A.6).*

*Proof.* Decompose $\mathcal J$ by tower property: for any $\tilde{\mathcal F}$-causal $x$,
$$
\mathbb{E}[f_t x_t] = \mathbb{E}\big[\mathbb{E}[f_t\mid \tilde{\mathcal F}_t]\,x_t\big] = \mathbb{E}[f^W_t\, x_t],
$$
using $x_t \in \tilde{\mathcal F}_t$. The cost term $\mathbb{E}[x_t(K*x)_t]$ depends only on $x$. Therefore
$$
\mathcal J(x) \;=\; \mathbb{E}[f^W_t x_t] - \tfrac{1}{2}\mathbb{E}[x_t(K*x)_t], \tag{B.10}
$$
which is **the clean-signal problem with $f$ replaced by $f^W$**, optimised over $\tilde{\mathcal F}$-causal $x$. Since $f^W$ is itself $\tilde{\mathcal F}$-causal (causal Wiener filter, Def. A.6), the causal-functions-of-$f^W$ class is identical to causal-functions-of-$\tilde f$ that respect $\tilde{\mathcal F}_t$-measurability. Applying Theorem B.3 with $f \leftarrow f^W$ gives (B.9). Joint Gaussianity ensures $\mathbb{E}[f_t\mid\tilde{\mathcal F}_t]$ is the linear Wiener filter, justifying the use of (B.9) inside the linear Wiener–Hopf machinery. $\square$

*Remark (certainty equivalence).* Outside the Gaussian regime, $f^W_t = \mathbb{E}[f_t\mid\tilde{\mathcal F}_t]$ need not be a linear functional of $\tilde f$; the wide-sense linear best estimate still satisfies (B.10) with $f^W$ replaced by the linear projection, yielding the linear-optimal policy (21) of §7.4. This is the *certainty-equivalence* version of the separation principle (Wiener 1949; Kalman 1960; cf. §9).

---

### Cross-reference index

| Theorem | Statement in main text | Page/section |
|---|---|---|
| B.1 | PD ⇔ no dyn-arb | §2.4 |
| B.2 | $\phi^*(f) = \tfrac12 \|f\|_{K^{-1}}^2$ | §3.2, eq. (2)–(3) |
| B.3 | Wiener–Hopf optimum | §4.1, eqs. (4)–(6) |
| B.4 | Szegő factorisation | §4.2 |
| B.5 | Markov-closure scalar identity | §5.5, eq. (12c) |
| B.6 | $\Gamma(-\alpha)\kappa^\alpha$ identity | §6.3, eq. (15b) |
| B.7 | $(1-\rho)^\alpha$ identity | §6.3, eq. (15c) |
| B.8 | Denoise-then-trade | §7.3 |

---

*End of appendix draft.*
