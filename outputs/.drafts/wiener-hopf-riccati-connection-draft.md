# Wiener–Hopf and Riccati: Two Faces of the Same Object

**Companion note to** `papers/noisy-signal-impact-trading.md` and `outputs/trading-duality-extensions.md`.
**Date:** 2026-05-31.
**Status:** Expository synthesis. No new theorems; conjectures flagged.

---

## Executive Summary

The trading paper solves a stationary infinite-horizon optimal-trading problem by **Wiener–Hopf factorisation** of the impact kernel $K = K_+ K_-$. The companion note observed in one line that this is "the LQG separation principle in disguise" and that "the control half of LQG is usually a finite-dimensional Riccati equation". This note unpacks that line.

The summary in one sentence: *for stationary infinite-horizon problems with rational kernels, the Wiener–Hopf causal factor $K_+$ and the rational spectral factor built from the stabilising solution of an algebraic Riccati equation are the same object — one expressed in frequency domain, the other in state space.* The Kalman–Yakubovich–Popov (KYP) lemma is the triangle that makes the equivalence formal.

The note covers:

1. What each method solves, in its native problem class.
2. The triangle: positive-real frequency-domain ⇔ LMI/dissipativity time-domain ⇔ algebraic Riccati. (KYP.)
3. Stochastic realisation theory as the explicit bridge: spectral density ↔ ARE solutions ↔ innovations representation = Kalman filter = Wiener filter.
4. Constructive translation in both directions.
5. The trading-paper specialisation: the AR(1) × exponential closed-form (paper eq. 12) *is* the solution of a 2-D discrete algebraic Riccati equation.
6. Where the methods diverge: non-rational kernels (operator Riccati, à la Abi Jaber–Miller–Pham 2019), finite horizon (Riccati ODE wins), $H^\infty$ / robust (Krein-space indefinite Riccati).
7. When to reach for which.

---

## 1. What Each Method Solves

### 1.1 Wiener–Hopf factorisation

*Problem class.* Convex quadratic problems over functions on $\mathbb{Z}$ or $\mathbb{R}$ involving convolution operators. Concretely, given a stationary objective

$$\mathcal{J}(x) = \langle f, x\rangle - \tfrac12 \langle x, K * x\rangle$$

with convolution kernel $K$ on the integers, maximise over $x$ in some causal subspace.

*Tool.* Spectral factorisation of $\hat K(\omega) = K_+(\omega) K_-(\omega)$ where $K_+$ is causal-analytic in $|z| > 1$ and $K_-$ anticausal-analytic in $|z| < 1$ (or vice-versa). The causal-projection operator $[\,\cdot\,]_+$ enforces the causality constraint in frequency domain.

*Origins.* Kolmogorov, Krein, Gohberg, Wiener.

*Strengths.* Frequency-domain transparency. Handles non-rational kernels (Hardy-space operators) gracefully. Independent of any state-space realisation.

### 1.2 Riccati equation

*Problem class.* Linear quadratic regulator (LQR) or LQG with state-space dynamics

$$x_{t+1} = A x_t + B u_t + w_t, \quad y_t = C x_t + v_t$$

and quadratic cost $\sum_t (x_t^\top Q x_t + u_t^\top R u_t)$.

*Tool.* The infinite-horizon optimal feedback is $u_t^\star = -F\,\hat x_t$ where $F = (R + B^\top P B)^{-1} B^\top P A$ and $P$ is the stabilising solution of the **discrete algebraic Riccati equation** (DARE)

$$P = A^\top P A - A^\top P B (R + B^\top P B)^{-1} B^\top P A + Q.$$

For estimation, the dual DARE gives the steady-state Kalman gain.

*Origins.* Kalman 1960, Kalman–Bucy 1961.

*Strengths.* Time-varying / finite-horizon extensions via the Riccati differential equation (RDE) are immediate. Easy to implement when state dimension is small. State-space view aligns with physical/engineering models.

### 1.3 Why they look like rivals

Naïvely the two methods occupy different worlds:

| Wiener–Hopf | Riccati |
|---|---|
| Frequency-domain | State-space |
| Operator on $\ell^2(\mathbb{Z})$ | Matrix equation in $\mathbb{R}^{n\times n}$ |
| Hardy-space projection | Stabilising-solution selection |
| Natural for convolution problems | Natural for differential/difference dynamics |

They look like different mathematics. They are not.

---

## 2. The KYP Triangle

The Kalman–Yakubovich–Popov (KYP) lemma — also called the positive-real lemma — is the formal equivalence linking three statements about a rational transfer matrix $G(z)$ (Anderson 1999 review; MIT 6.245 ch. 8 notes).

For an LTI system $G(z) = C(zI - A)^{-1}B + D$:

**(F) Frequency-domain.** $G(z) + G^*(z) \succeq 0$ on the unit circle $|z|=1$.

**(T) Time-domain / dissipativity.** There exists a quadratic storage function $V(x) = x^\top P x$ with $P \succeq 0$ such that the system dissipates the supply rate $u^\top y + y^\top u$ along all trajectories.

**(R) Riccati.** There exists $P \succeq 0$ satisfying the linear matrix inequality (LMI)

$$\begin{pmatrix} A^\top P A - P & A^\top P B - C^\top \\ B^\top P A - C & B^\top P B + B^\top P B^\top - D - D^\top \end{pmatrix} \preceq 0,$$

which, under regularity, is equivalent to an algebraic Riccati *equation*.

**Equivalence (KYP).** (F) ⇔ (T) ⇔ (R).

The bridge to *spectral factorisation* is then: if $\Phi(z) := G(z) + G^*(z) \succeq 0$ is rational, then by KYP there exists $P$ solving an ARE such that the *stabilising* solution $P_+$ generates a stable, minimum-phase spectral factor $W(z)$ with $\Phi(z) = W^*(z) W(z)$. This $W$ is the Wiener–Hopf causal factor.

So: **Wiener–Hopf spectral factorisation = stabilising-ARE construction**, for rational spectra. The exposition in Anderson (1973, SIAM J. Control) makes this one-to-one correspondence between ARE solutions and rational factorisations explicit and progressive: as we specialise from arbitrary symmetric solutions to Hermitian to stabilising to positive-definite, we step through symmetric/Hermitian/stable/minimum-phase factorisations.

---

## 3. Stochastic Realisation Theory: The Explicit Bridge

The cleanest statement of the equivalence — and the one that maps most directly onto the trading paper's setting — comes from *stochastic realisation theory* (Akaike, Faurre, Lindquist–Picci).

**Setup.** A stationary Gaussian process $y_t$ with rational spectral density $\Phi(\omega)$. Find all minimal state-space models $x_{t+1} = Ax_t + Bw_t$, $y_t = Cx_t + Dw_t$ (with $w$ white noise) whose output spectrum equals $\Phi$.

**Lindquist–Picci theorem (1979).** The set of all minimal Markovian realisations of $y$ is in one-to-one correspondence with the set of all solutions $P$ of a certain *algebraic Riccati inequality*. The minimal element of this set gives the **forward innovations representation**; the maximal element gives the backward one. Both correspond to specific Wiener–Hopf factorisations of $\Phi$.

**Consequence.** The steady-state Kalman filter — the recursive innovations form — is the time-domain realisation of the causal Wiener filter. They are not approximations of each other; they are the same operator written in two notations.

**Implication for the trading paper.** The §7 separation result — "Wiener filter the noisy signal, then apply the impact-adjusted causal rule" — is the steady-state form of an LQG/Kalman two-stage decomposition. The "Wiener filter" is the stationary Kalman filter for the AR(1) signal plus i.i.d. observation noise; its Riccati equation has a 1-D state and a scalar quadratic, with closed-form fixed point.

---

## 4. Constructive Translation in Both Directions

### 4.1 State-space → Wiener–Hopf factor

Given $(A, B, C, D)$ realising a transfer matrix $G(z)$ whose para-Hermitian part $\Phi := G + G^*$ is positive on the unit circle:

1. Solve the stabilising DARE for $P$.
2. Form the inner-outer / spectral factor $W(z) = C(zI - A)^{-1} K + L$, where $K, L$ are obtained from $P, B, D$ by an explicit linear formula (see Sayed–Kailath 2001 survey; Varga 2000 IEEE TAC; Zhou–Doyle–Glover *Robust and Optimal Control*).
3. Then $W^*(z) W(z) = \Phi(z)$ on $|z|=1$, $W$ is causal-stable, and $W$ is the Wiener–Hopf causal factor up to a unitary on the right.

Varga (2000) emphasises a practical benefit: the ARE one solves has order equal to the (often small) McMillan degree of $G$, not the (potentially much larger) degree of $\Phi$.

### 4.2 Wiener–Hopf factor → state-space

Going the other way is harder when one starts with a non-state-space description of $\Phi$ (e.g. a kernel given by its autocorrelation sequence).

1. Compute a minimal realisation of $\Phi(z)$ from its autocorrelation (Ho–Kalman / subspace identification, or partial-fraction expansion when $\Phi$ is rational).
2. Apply the route of §4.1 to obtain the spectral factor.
3. Read off $(A, B, C, D)$ of the factor.

If $\Phi$ is not rational, step 1 fails: no finite-dimensional state-space realisation exists. This is the regime where Wiener–Hopf still works but Riccati must be replaced by its operator-valued generalisation (§6).

---

## 5. Worked Example: AR(1) × Exponential as a 2-D DARE

The trading paper's signature closed-form result (eq. 12) is

$$x_t = \frac{1-\lambda\rho}{1-\lambda^2}\,(f_t - \lambda f_{t-1}),$$

for AR(1) signal $f$ with persistence $\rho$ and exponential impact kernel $K(n) = \lambda^{|n|}$.

This problem is **equivalent to a standard LQ stochastic control problem with a 2-D state**, and the closed form *is* the gain of a 2×2 discrete algebraic Riccati equation. The equivalence is general for Obizhaeva–Wang-type exponential-resilience execution problems (Bank & Voß 2022; Cartea, Jaimungal et al.).

**State construction.** Define the impact state $J_t := \sum_{s \le t} \lambda^{t-s} x_s$, satisfying $J_{t+1} = \lambda J_t + \lambda x_{t+1}$ (geometric decay). The per-period expected reward is then a quadratic form in the state vector $z_t := (f_t, J_{t-1})^\top$ and the control $x_t$:

- *Dynamics:*
  $$z_{t+1} = \begin{pmatrix} \rho & 0 \\ 0 & \lambda \end{pmatrix} z_t + \begin{pmatrix} 0 \\ \lambda \end{pmatrix} x_t + \begin{pmatrix} 1 \\ 0 \end{pmatrix}\epsilon_{t+1},$$
- *Stage reward:* $f_t x_t - \tfrac12 \langle x, K x\rangle_{\text{stage contribution}}$, which under the OW-style accounting decomposes as a quadratic in $(z_t, x_t)$ with cross-term coupling $J_{t-1}$ to $x_t$.

The standard LQ optimal feedback is $x_t^\star = -F z_t$ for a $1\times 2$ gain matrix $F$, with $F$ computed from the stabilising DARE solution $P \in \mathbb{R}^{2\times 2}$. Writing out the closed form $-F z_t = \alpha f_t + \beta J_{t-1}$ and substituting $J_{t-1}$'s recursion back into pure-signal language gives (12) exactly. (The Riccati arithmetic is tedious but mechanical; the structural point is that the 2-D DARE has a closed-form solution because the system is triangular and the cost is rank-one in the control.)

**Sanity-check from `experiments/closed_form_vs_operator.py`.** The discrete operator-resolvent solver — which is the *normal-equations* form of the same problem, not the state-space form — recovers (12) to machine precision (residual $2.6 \times 10^{-15}$) on simulated paths. Three computational routes (Wiener–Hopf in frequency domain, discrete Wiener–Hopf normal equations, and the LQ/DARE state-space approach) therefore deliver the *same* policy for this problem. The first two are confirmed numerically in the experiment; the third is established by the Bank–Voß reduction.

**Reading.** Equation (12) is *both* "the kernel innovation of the signal weighted by signal–kernel alignment" (the Wiener–Hopf reading in the paper) and "the optimal LQ feedback gain on a 2-D state with the impact-state acting as a co-state variable" (the Riccati reading). The two are the same number, written in different bookkeeping.

---

## 6. Where the Methods Diverge

### 6.1 Non-rational kernels: operator Riccati

If $\hat K(\omega)$ is *not* a finite-degree rational function — power-law kernels $|\tau|^{-\beta}$, fractional Brownian spectra, rough-volatility Volterra kernels — then no finite-dimensional state-space realisation exists for the kernel-induced dynamics. Two consequences:

- The Wiener–Hopf factor $K_+$ still exists as an operator on a Hardy space, and the trading-paper construction (causal projection + division by $K_+$) still works abstractly. The factor is no longer a rational function; in the power-law case it is a fractional integral/derivative (paper §6.2).
- The Riccati equation must become *operator-valued*. **Abi Jaber, Miller & Pham (2019, arXiv:1911.01903)** establish existence and uniqueness of infinite-dimensional Riccati equations in $L^1(\mu \otimes \mu)$ — a space of signed matrix measures — for stochastic Volterra control problems. The companion paper (arXiv:1911.01900) gives the LQ control framework that subsumes the matrix-Volterra impact propagators of Abi Jaber–Neuman–Tuschmann.

So the "Wiener–Hopf in frequency domain" route generalises directly; the "Riccati in state space" route generalises only after promoting state space to a function space. The two routes still solve the same problem, but the operator-Riccati machinery is substantially heavier than its finite-dimensional cousin.

### 6.2 Finite-horizon and time-varying

For finite-horizon problems $\sum_{t=0}^{T} (\dots)$ with terminal constraint $x_T = \bar x$, the **Riccati differential/difference equation** (RDE, DRDE) is the natural object: it propagates the value function backward in time. Each time slice gives a different Kalman gain.

Wiener–Hopf, being inherently stationary (a single spectral factor for the whole problem), does not generalise as cleanly. Finite-horizon extensions exist (truncated Wiener–Hopf integral equations, the Krein–Sobolev factorisation), but for engineering purposes the Riccati route dominates this regime.

Practical reading: the trading paper works in the infinite-horizon stationary limit *because* Wiener–Hopf is cleanest there. The Bank–Voß / Abi Jaber–Neuman finite-horizon execution papers work in Riccati-style for the same reason.

### 6.3 H∞, robustness, and Krein-space Riccati

Replacing the expected quadratic cost with a *worst-case* (H∞) cost replaces the $L^2$ inner product with an *indefinite* one (negative weights on the disturbance, positive on the error). The resulting estimator and controller satisfy a Riccati equation with **indefinite quadratic term** — geometrically, a Krein-space Riccati (Hassibi, Sayed & Kailath 1999, *Indefinite Quadratic Estimation and Control*; SIAM monograph).

The frequency-domain image of this Krein-space Riccati is a Wiener–Hopf factorisation on an indefinite (Krein) space rather than a Hilbert space. The duality survives, but Hilbert-space spectral factorisation is replaced by $J$-spectral factorisation (for a Krein form $J$).

This is the framework that would formalise the robust-trading conjecture in `outputs/trading-duality-extensions.md` §7: replace the Wiener prefilter with an $H^\infty$ filter under spectral ambiguity → the impact-adjusted causal half then becomes a $J$-spectral factor of $K$ rather than a Wiener–Hopf factor.

### 6.4 Computational pragmatics

When state dimension is small (≤ few hundred), Riccati wins: one matrix equation, mature solvers (Hewer iteration, Schur method, MATLAB `dare`).

When state dimension is very large or the kernel is non-rational, Riccati becomes infeasible. **Martini et al. (2022, arXiv:2201.00361)** describe exactly this regime in fluid-mechanics control problems with many DOFs: they explicitly switch to Wiener–Hopf / resolvent methods because the corresponding Riccati equation is unmanageable. The trading analogue is high-dimensional multi-asset cross-impact: the operator-Riccati of Abi Jaber–Miller–Pham is the principled framework, but for practical estimation a Wiener–Hopf / resolvent route may be lighter.

---

## 7. When to Reach for Which

A working heuristic, summarising the above:

| Situation | Reach for |
|---|---|
| Stationary infinite-horizon, rational kernel | Either; Wiener–Hopf gives a transparent frequency-domain formula |
| Finite-horizon with terminal constraint | Riccati (RDE / DRDE) |
| Time-varying dynamics or noise | Riccati |
| Non-rational kernel (power-law, fBm, rough vol) | Wiener–Hopf in frequency domain; operator Riccati if state-space formalism needed |
| Very large state dimension | Wiener–Hopf / resolvent methods |
| Worst-case / H∞ / robust | Krein-space Riccati + $J$-spectral factorisation |
| Pedagogical clarity for a single signal model | Whichever native domain matches the signal |

For the trading paper: stationary infinite-horizon, simple kernels (exponential, power-law, ARFIMA) → Wiener–Hopf is the right choice and explains why the AR(1) × exponential case admits a one-line closed form, and why the power-law case naturally produces a fractional derivative. Translating into Riccati language adds notation without insight, *except* when one wants to verify against an LQ-control numerical implementation (Bank–Voß) or to extend to finite-horizon / terminal-liquidation problems.

---

## 8. Synthesis: Two Faces, One Object

The relationship is best stated as a translation table.

| Wiener–Hopf | Riccati |
|---|---|
| Spectral density $\Phi(\omega)$ | Rational realisation $(A, B, C, D)$ with $\Phi = (G + G^*)$ |
| Causal factor $K_+(z)$ | Spectral factor built from stabilising ARE solution $P_+$ |
| Anticausal factor $K_-(z)$ | Co-state / adjoint dynamics |
| Causal projection $[\,\cdot\,]_+$ | Stabilising-solution selection |
| Innovation filter $1/K_+$ | Steady-state Kalman gain |
| Frequency-domain projection of $\hat f / K_-$ | DP / HJB-optimal feedback policy |
| AR(1) × exponential scalar collapse | Closed-form solution of a 2-D DARE |
| Power-law kernel Wiener–Hopf | Operator Riccati of Abi Jaber–Miller–Pham |
| $H^\infty$ → $J$-spectral factorisation | Krein-space (indefinite) Riccati of Hassibi–Sayed–Kailath |
| Multi-asset matrix WH (Abi Jaber–Neuman–Tuschmann) | Matrix operator Riccati |

In the language of the trading paper: the §5 closed form is the rational case, the §6 power-law case is the operator case, the §7 noisy-signal separation is the LQG separation theorem with a 1-D Kalman filter, and the §8 examples are the meeting points where both routes yield the same explicit numbers.

The Wiener–Hopf framing is *not* a substitute for Riccati; it is the same answer viewed through a different window — one whose glass is clearest when the problem is stationary, the kernel may be non-rational, and the geometry of the answer matters more than the recursive algorithm to compute it.

---

## 9. Open Questions

1. **The cleanest reduction of paper eq. (12) to a 2×2 DARE.** A worked-out matrix calculation taking the Bank–Voß state augmentation and producing eq. (12) by Riccati arithmetic — useful as a textbook-style appendix to the paper.

2. **Operator Riccati for ARFIMA-spectrum kernels.** The Abi Jaber–Miller–Pham framework treats general Volterra kernels. Does the discrete ARFIMA spectrum $\hat K(\omega) = (2\sin\omega/2)^{-2\alpha}$ admit a clean operator-Riccati statement whose stabilising solution recovers the $(1-\rho)^\alpha$ scalar of paper eq. (15c)?

3. **Krein-space version of the trading rule.** Concrete: replace expected-utility by worst-case-spectrum and derive the corresponding $J$-spectral factorisation. Does the impact-adjusted causal rule of the paper survive, or does the worst-case spectrum perturb $K_+$ itself?

4. **Numerical comparison.** A side-by-side benchmark of (a) frequency-domain Wiener–Hopf, (b) discrete normal equations, (c) DARE-based LQ solution on the AR(1) × exponential problem would be a clean reproducibility artefact. Routes (a) and (b) are already in `experiments/closed_form_vs_operator.py`; (c) is missing.
