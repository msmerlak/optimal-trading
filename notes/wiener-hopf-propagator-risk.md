# Wiener–Hopf solution with propagator and risk: sketch

**Status:** internal research note, 2026-07-18. Companion to `tex/factorization-optimal-trading.tex` (whose §5.6 states the problem in one paragraph), `notes/geometry-optimal-trading-dual-norms.md` (the dual-space frame), and the extensions memo.
**Verification convention:** [derived] = worked out in this note with the derivation shown or sketched; [limit-checked] = reduces correctly to independently known special cases at both ends; [validated] = numerical experiment exists; [open] = stated, not established. No result below is numerically validated yet for $\lambda>0$; the discrete check is step 1 of the open items.

---

## 1. Problem and the position-coordinate reduction

Objective over adapted rates $u$, with position $x_t = \int_{-\infty}^t u_s\,ds$:

$$\max_u\; \E\!\int u_t\alpha_t\,dt \;-\; \frac{\gamma}{2}\,\E\!\iint G(|t-s|)u_tu_s\,dt\,ds \;-\; \frac{\lambda}{2}\,\E\!\int x_t^2\,dt .$$

The Hessian symbol in rate coordinates is

$$q(\xi) \;=\; \gamma\hat C(\xi) + \frac{\lambda}{\xi^2}, \qquad \text{adapted FOC:}\quad \E_t[(Qu^\star)(t)] = \alpha_t .$$

**Reduction.** Since $|\hat u|^2 = \xi^2|\hat x|^2$, the full quadratic form is $\langle x, N(D)x\rangle$ with

$$N(\xi) \;=\; \gamma\hat C(\xi)\,\xi^2 + \lambda,$$

and integration by parts turns the gain into $\E\int x_t\mu_t\,dt$ with $\mu = -\dot\alpha$ (the drift; $\alpha_t = \E_t[\text{remaining price change}]$ makes $\mu$ the instantaneous expected return). The rate problem with impact + risk is the paper's pure-propagator problem **for the position**, with cost symbol $N$ and signal $\mu$:

$$\E_t[(Nx^\star)(t)] = \mu_t, \qquad u^\star = \dot x^\star .$$

FOC equivalence [derived]: if $\E_s[(Nx^\star)(s)] = \mu_s$ for all $s$, then $\E_t[(Qu^\star)(t)] = \int_t^\infty \E_t[(Nx^\star)(s)]\,ds = -\int_t^\infty \partial_s\bar\alpha(t,s)\,ds = \alpha_t$, using the tower property and forecast decay $\bar\alpha(t,\infty)=0$. The $x\in L^2$ admissibility forced by the risk term is the same decay condition.

## 2. Factorization

$q = N/[(-i\xi)(i\xi)]$ factors term by term: $N = N_-N_+$ by Wiener–Hopf ($N>0$, even, $\log N/(1+\xi^2)\in L^1$), and $(-i\xi)$ is causal (integration $I_+$ has symbol $1/(-i\xi)$). So

$$q = Q_-Q_+,\qquad Q_+(\xi) = \frac{N_+(\xi)}{-i\xi},\qquad Q_- = \overline{Q_+},$$

i.e. $Q_+ = N_+(D)\circ I_+$: the causal factor of the joint problem is "integrate, then color by the causal factor of $N$" — the operator form of the position reduction. [derived]

**Power law + risk.** $N(\xi) = \gamma c_\beta|\xi|^{1+\beta} + \lambda$, crossover $\xi_c = (\lambda/\gamma c_\beta)^{1/(1+\beta)}$. Asymptotically $N_+ \approx (\gamma c_\beta)^{1/2}(-i\xi)^{(1+\beta)/2}$ above $\xi_c$ (recovering the paper's factor for the rate) and $N_+\approx\lambda^{1/2}$ below. No elementary closed form for the factor; the Szegő representation
$$\Phi_N(\theta) := N_+(i\theta) = \exp\Bigl[\frac{\theta}{2\pi}\int\frac{\log N(t)}{\theta^2+t^2}\,dt\Bigr]$$
suffices for every evaluation below. [derived]

**Exponential + risk (fully closed form).** $N(\xi) = \bigl[(2\kappa\gamma+\lambda)\xi^2 + \lambda\kappa^2\bigr]/(\kappa^2+\xi^2)$ is rational:
$$N_+(\xi) = \sqrt{A}\;\frac{m - i\xi}{\kappa - i\xi},\qquad A = 2\kappa\gamma+\lambda,\qquad m = \kappa\sqrt{\lambda/A}\;<\kappa,$$
so $\Phi_N(\theta) = \sqrt A\,(m+\theta)/(\kappa+\theta)$. [derived]

## 3. General solution

Three-step recipe at position level, then differentiate:

$$x^\star = N_+^{-1}\,P_+\,N_-^{-1}\,\mu, \qquad
\zeta^x_s = \bigl(N_-^{-1}\bar\mu(s,\cdot)\bigr)(s), \quad \bar\mu(s,r) = -\partial_r\bar\alpha(s,r),
\qquad u^\star = \dot x^\star .$$

Anticausal whitening of the **drift forecast curve**, adapted projection, causal coloring — the paper's architecture with $(C,\alpha)$ replaced by $(N,\mu)$. For a stationary Gaussian signal generating its own filtration, the innovations form is $\hat g_x = N_+^{-1}\Pi_+[N_-^{-1}\varphi^\mu_+]$ with $\varphi^\mu_+ = (i\xi)\varphi_+$, and the value rate is $v_{\rm ad} = \frac{1}{4\pi}\|\Pi_+(N_-^{-1}\varphi^\mu_+)\|^2$. [derived, same proofs as the paper's §5.5 appendix]

Finite interval: the Gohberg–Krein version applies to $N$ on $[0,T]$ with the **terminal-anchored** causal factor (the review's C1 lesson carries over verbatim); the integration-by-parts boundary terms and liquidation constraints join the $\alpha^{\rm eff}$/multiplier machinery. [open — boundary terms not worked out]

## 4. OU closed forms

OU signal, rate $\theta$, innovation variance $\sigma^2$, own filtration. The drift forecast curve is $\bar\mu(s,r) = \theta e^{-\theta(r-s)}\alpha_s$, so Laplace evaluation gives $\zeta^x_s = \theta\alpha_s/\Phi_N(\theta)$.

**Position response** $X(\theta) := \E[x^\star_t\mid\alpha_t]/\alpha_t$:
$$X(\theta) = \frac{\theta}{\Phi_N(\theta)^2} \;>\;0 \quad\text{always}.$$
The position filter $\hat g_x = (\theta/\Phi_N)N_+^{-1}\varphi_+$ decays at high frequency for every kernel (the $\varphi_+$ decay dominates any atom of $N_+^{-1}$), so no forward-convention correction arises. [derived; limit-checked: $\lambda$-only gives $\theta/\lambda$, matching $x = \theta\alpha/\lambda$ directly; $\gamma$-only power law gives $\theta^{-\beta}/\gamma c_\beta$, matching the paper's filter integrated to position by two independent routes]

**Flow response** $R(\theta) := \lim_{q\downarrow0}\E[u^\star_{t+q}\mid\alpha_t]/\alpha_t$: the flow filter $\hat g_u = (-i\xi)\hat g_x$ has atom $a_0 = \theta\sigma c_1/\Phi_N$ with
$$c_1 = \lim_{|\xi|\to\infty}\frac{1}{N_+(\xi)} = \bigl[\lambda - 2\gamma G'(0^+)\bigr]^{-1/2}\ \ (\text{kink kernels}),\qquad c_1 = 0\ \ (\text{power-law cusp, any }\lambda\ge0\text{ with }\gamma>0),$$
and the atom subtraction gives
$$R(\theta) = \frac{\theta^2}{\Phi_N(\theta)}\Bigl[\frac{1}{\Phi_N(\theta)} - 2c_1\Bigr].$$
[derived; limit-checked at both ends: $\lambda\to0$ exponential recovers $(\kappa^2-\theta^2)/2\kappa\gamma$ exactly; $\lambda\to0$ power law recovers $\theta^{1-\beta}/\gamma c_\beta$; $\gamma\to0$ recovers the pure-risk $-\theta^2/\lambda$]

**Contrarian criterion.** $\operatorname{sign}R = \operatorname{sign}\bigl(1 - 2c_1\Phi_N(\theta)\bigr)$; positions never flip, only flows.
- Power law + risk: $c_1 = 0$, so $R>0$ and $X>0$ at every signal speed and every $\lambda$. Risk rescales through $\Phi_N$ but never induces contrarian flow. [derived]
- Exponential + risk: flip at $\theta^* = \kappa - 2m = \kappa\bigl[1 - 2\sqrt{\lambda/(2\kappa\gamma+\lambda)}\bigr]$. Risk lowers the pure-impact threshold $\theta^*=\kappa$, and $\theta^*\le0$ — contrarian flow at all speeds — once $\lambda \ge 2\kappa\gamma/3$. [derived; $\lambda\to0$ check gives $\theta^*=\kappa$]

Mechanism, restating the geometry note: contrarian flow is carried by the innovation atom, which exists iff singular rates have finite cost under the *combined* metric; the risk term contributes $\lambda^{-1/2}$-type atom mass on its own (positions jump toward the Markowitz target), the power-law impact term destroys the atom, the exponential term preserves it.

**Value.**
$$v_{\rm ad} = \frac{\sigma^2\theta}{4\,\Phi_N(\theta)^2} = \frac{\sigma^2}{4}\,X(\theta),$$
from $\Pi_+(N_-^{-1}\varphi^\mu_+) = (\theta/\Phi_N)\varphi_+$ (pole cancellation; the $N_-^{-1}$ atom is annihilated by the projection because it loads on the contemporaneous innovation). [derived; limit-checked: $\lambda\to0$ gives $\sigma^2\theta^{-\beta}/4\gamma c_\beta$, the paper's §5.5 value]

**Finiteness of the anticipative benchmark.** $v_{\rm ant} = \frac{1}{4\pi}\int S_\alpha\,\xi^2/N(\xi)\,d\xi$ converges iff the impact kernel is singular enough at the origin relative to the signal's high-frequency content. Power law + risk + OU: finite, and the causality angle $\cos^2 = v_{\rm ad}/v_{\rm ant}$ is a function of $(\theta/\xi_c,\beta)$ alone, tending to $\sin(\pi\beta/2)$ for $\theta\gg\xi_c$ and to $0$ linearly in $\theta$ for $\theta\ll\xi_c$ (the anticipative trader monetizes the slow signal's fast innovations; the adapted trader cannot). Exponential + risk + OU: $v_{\rm ant}=\infty$ while $v_{\rm ad}<\infty$ — the angle degenerates to zero, and the anticipative benchmark stops being informative for kink kernels without temporary impact. [derived-sketch]

## 5. Consistency ledger

| Claim | Check | Status |
|---|---|---|
| FOC equivalence rate ↔ position | tower + forecast decay, shown in §1 | derived |
| $N_+$ for exponential + risk | direct rational factorization; $\lambda\to0$, $\gamma\to0$ ends | derived, limit-checked |
| $X = \theta/\Phi_N^2$ | pure risk ($\theta/\lambda$) and pure power-law impact ($\theta^{-\beta}/\gamma c_\beta$, two routes) | derived, limit-checked |
| $R = (\theta^2/\Phi_N)[1/\Phi_N - 2c_1]$ | exponential $\lambda\to0$: $(\kappa^2-\theta^2)/2\kappa\gamma$; power law $\lambda\to0$: $\theta^{1-\beta}/\gamma c_\beta$; $\gamma\to0$: $-\theta^2/\lambda$ | derived, limit-checked |
| $c_1 = [\lambda-2\gamma G'(0^+)]^{-1/2}$ | reproduces $1/\sqrt{2\kappa\gamma}$, $1/\sqrt\lambda$, $0$ in the three corners | derived |
| $\theta^* = \kappa-2m$; always-contrarian iff $\lambda\ge2\kappa\gamma/3$ | algebra from criterion; $\lambda\to0$ end | derived, limit-checked |
| $v_{\rm ad} = \sigma^2 X/4$ | $\lambda\to0$ end matches paper §5.5; also equals $\tfrac12 R\,\mathrm{Var}(\alpha)/\theta$ identity | derived, limit-checked |
| Any $\lambda>0$ formula, numerically | — | **not run** |

The mixture-experiment episode (naive continuation refuted at $\lambda=0$) is the standing reason none of the $\lambda>0$ formulas should enter a draft before the discrete check runs.

## 6. Open items

1. **Numerical validation** [decisive, cheap]: extend `experiments/extension_response_check.py` with the risk term — discretely, add $\lambda\,L^\top L\,dt^2$ to the cost matrix ($L$ = lower-triangular cumulative-sum matrix), rerun the UL-factorization solver, measure $X$, $R$ against §4 for (i) exponential + risk across $\theta^*(\lambda)$, (ii) power-law + risk positivity, (iii) the always-contrarian regime $\lambda>2\kappa\gamma/3$.
2. Closed form or quadrature for the causality angle $F_\beta(\theta/\xi_c)$; check the two limits in §4.
3. Finite-interval version: boundary terms of the integration by parts, liquidation constraint, terminal-anchored factor for $N$ on $[0,T]$.
4. Special-$\beta$ hunts for closed-form $N_\pm$ (e.g. $1+\beta = 3/2$) are low priority: every quantity of interest evaluates through $\Phi_N$.
5. If validated, §4 upgrades the draft's §5.6 from one paragraph to a worked section, and the exponential+risk threshold $\theta^*(\lambda)$ is the natural headline example.

## Sources

- `tex/factorization-optimal-trading.tex` — §5.1 (response function, $\lambda=0$ validated), §5.5 (innovations/value, $\lambda=0$), §5.6 (gain–risk–cost symbol)
- `notes/geometry-optimal-trading-dual-norms.md` — dual-space frame; flow-vs-position subtlety; pure-risk checks
- `outputs/factorization-optimal-trading-extensions.md` — response-formula derivation and validation at $\lambda=0$
- `experiments/extension_response_check.py` — validated $\lambda=0$ numerics; refuted naive continuation (cautionary precedent)
