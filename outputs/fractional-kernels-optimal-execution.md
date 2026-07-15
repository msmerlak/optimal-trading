# Power-law impact kernels and fractional derivatives in optimal execution: a literature review

**Date:** 2026-06-27
**Scope:** Has anyone, in the optimal-execution / optimal-trading literature, explicitly written the optimal trading policy as a fractional derivative (Riemann–Liouville, Caputo, Marchaud, Riesz) of the alpha signal — exploiting the fact that the inverse of a power-law convolution kernel is a fractional operator?

---

## 1. TL;DR

**Yes — but the link is made cleanly in only one paper, and is implicit (via the Abel integral equation) in the foundational propagator-model literature.**

The mathematical fact behind the question is standard fractional-calculus folklore: the Riemann–Liouville fractional integral of order $\alpha\in(0,1)$ is convolution with $t^{\alpha-1}/\Gamma(\alpha)$, so any optimality condition of the form

$$\int_0^t (t-s)^{\alpha-1}\, u^*(s)\, ds = \text{(signal)}(t)$$

is an Abel integral equation, and its formal inverse is a Marchaud / Riemann–Liouville fractional derivative of order $\alpha$ applied to the right-hand side. The propagator model of Bouchaud et al. (2004) and Gatheral (2010) gives exactly that integral equation when the decay kernel is taken to be a power-law $G(t)=ct^{-\gamma}$ — which is the empirically supported case.

Despite this near-tautology, the optimal-execution literature has been slow to write the policy as "fractional derivative of the signal" in plain language. The explicit connection appears in:

1. **Forde, Sánchez-Betancourt, Smith (Quantitative Finance, 2022)** — the only paper found that writes the operator inverse of the power-law impact Fredholm equation explicitly using the Riemann–Liouville fractional integral $I_\nu$ and its inverse $D_r$ (a fractional derivative), and then gives a closed-form fractional-Beta-type kernel for the signal-adaptive optimal selling speed.
2. **Gatheral, Schied, Slynko (Mathematical Finance, 2012)** — solves the zero-signal power-law case as the **Abel equation**, recovering the canonical U-shaped $(t(T-t))^{(1-\gamma)/2-1}$ schedule. This is fractional-derivative inversion by name, though not labelled as such.
3. **Curato, Gatheral, Lillo (Quant. Finance, 2017, §2.2)** — same Abel-equation observation in the nonlinear-impact setting.
4. **Abi Jaber, Neuman (and co-authors, 2022–2025)** — explicitly call $K(t,s)=c(t-s)^{\alpha-1}$ the **"fractional kernel"** and analyze optimal execution with it, but solve the resulting Volterra/Fredholm problem via operator inversion or Nyström discretization rather than writing the optimal $u^*$ as a fractional derivative of the signal.

So the answer is: the structural identity *kernel inversion = fractional derivative* is **explicit in Forde et al. (2022)** for the linear-impact / Gaussian-signal case and **implicit** (Abel equation) throughout the rest of the power-law propagator literature. To my knowledge, no paper writes a clean "optimal rate $= D^\alpha (\text{alpha}_t)$" closed form in the spirit of fractional-PID control. That gap is real.

---

## 2. Why the question almost answers itself: the math

Let the execution price be $S_t = P_t + \int_0^t G(t-s)\,dX_s$ with $X_t = X_0 - \int_0^t u_s\,ds$ (Gatheral 2010 propagator model). For a Gaussian signal $\xi_t$, zero temporary impact, and linear cost, the Pontryagin first-order condition for $u^*$ is the **Fredholm integral equation of the first kind**

$$\int_0^T G(|t-v|)\, u^*(v)\, dv = \lambda - \xi_t, \qquad t\in[0,T], \tag{$\star$}$$

with $\lambda$ enforcing $X_T=0$.

If $G(t)=c\,t^{-\gamma}$ with $\gamma\in(0,1)$, then on $(0,T)$ this is (after splitting on $\{v<t\}$ vs $\{v>t\}$) a generalized **Abel integral equation**. The Riemann–Liouville integral operator $I^\nu\!:f\mapsto \frac{1}{\Gamma(\nu)}\int_0^t (t-s)^{\nu-1}f(s)\,ds$ has inverse the Riemann–Liouville fractional derivative

$$D^\nu f(t) = \frac{1}{\Gamma(1-\nu)}\frac{d}{dt}\int_0^t (t-s)^{-\nu} f(s)\,ds.$$

So formally $u^* = D^{1-\gamma}(\lambda - \xi)$ up to boundary/symmetry corrections (the two-sided $|t-v|^{-\gamma}$ kernel makes the inversion a Riesz-type fractional derivative on $[0,T]$ with the Sonine pair structure). This is the punchline the question is pointing at.

---

## 3. Direct hits

### 3.1 Forde, Sánchez-Betancourt, Smith — *"Optimal trade execution for Gaussian signals with power-law resilience"* (Quantitative Finance 22(3), 2022)

This is the closest match to the question. From the published PDF (§2.2, pp. 590–591):

> "Then we can further re-write $T$ as $T = B^{-1} I_\nu B$, where $B$ is the bounded operator on $L^2$ which multiplies functions by $t^{-(1-\nu)/2}$ and $I_\nu$ is the Riemann–Liouville operator $(I^\nu\varphi)(t) := \int_0^t (t-s)^{-\tfrac12(1+\gamma)}\varphi(s)\,ds = \frac{1}{\Gamma(1-r)} I^r$ where $r = \tfrac12 - \tfrac12\gamma$ so $I_\nu^{-1} = \Gamma(1-r)\, D^r$, where $I^r$ and $D^r$ are the fractional derivative operators of order $r$."

They then quote Chakrabarti–George (1994)'s explicit solution to the generalized Abel equation, producing a closed-form $k(u,t)$ for the optimal selling speed when the signal is a Riemann–Liouville (rough) Gaussian Volterra process. The resulting expression (their eq. (26)) is built from incomplete Beta integrals and Gamma functions — exactly the algebra one gets from applying a fractional-Beta operator to a power-law signal.

Key claim verbatim from abstract: *"Fredholm integral equations of the first kind which can be solved in terms of fractional derivatives"*. Source: https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26 ; DOI: https://doi.org/10.1080/14697688.2021.1950919.

Caveats:
- The fractional-derivative inversion appears in the *proof / construction* of the Fredholm solution, not as the final stated policy. A user reading only Theorem 2.2 will see a Gaussian Volterra process, not "fractional derivative of $\xi$".
- Temporary price impact ($\eta u_t$) converts $(\star)$ into a Fredholm equation of the second kind whose inversion is no longer a pure fractional derivative (it becomes the resolvent of a power-law-plus-identity kernel — closer to a Mittag-Leffler operator).
- Authors restrict to Gaussian signals to make the conditional expectations $E_t \xi_v$ tractable.

### 3.2 Gatheral, Schied, Slynko — *"Transient linear price impact and Fredholm integral equations"* (Math. Finance 22, 2012)

The foundational reference. For the *no-signal* case with power-law decay $G(t)=ct^{-\gamma}$, the optimal execution density is

$$u^*_0(t) = c_1\, \bigl(t(T-t)\bigr)^{\tfrac12(1-\gamma)-1},$$

a symmetric U-shape. This is exactly the solution to the symmetric Abel equation on $[0,T]$, i.e. the result of applying the symmetric (Riesz) fractional inversion of order $\gamma$ to a constant. The paper does not use the words "fractional derivative", but the result is the canonical fractional-calculus inversion of a power-law kernel.
DOI: https://doi.org/10.1111/j.1467-9965.2011.00478.x ; SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1531466.

### 3.3 Curato, Gatheral, Lillo — *"Optimal execution with non-linear transient market impact"* (Quant. Finance 17(1), 2017)

§2.2 makes the Abel-equation reduction explicit for power-law impact and uses it as the benchmark closed-form solution against which nonlinear-impact homotopy schemes are compared.
arXiv: https://arxiv.org/abs/1412.4839.

---

## 4. Adjacent: the "fractional kernel" branch (Abi Jaber, Neuman, and co-authors)

These papers adopt the *name* "fractional kernel" for the power-law convolution kernel of optimal-execution propagator models, but their solution method is operator-theoretic (resolvents, Riccati equations, Nyström discretization) rather than expressing $u^*$ as a fractional derivative of $\alpha_t$.

- **Abi Jaber, Neuman — *"Optimal Liquidation with Signals: the General Propagator Case"*** (arXiv 2211.00447, 2022; SIAM J. Financial Math. 2024). Calls $K(t,s)=c(t-s)^{\alpha-1}\mathbf{1}_{t>s}$ the *fractional kernel* (eq. (2.7) of the constraints follow-up paper). Provides an explicit operator formula for $u^*$ but does not unpack it as a fractional derivative. https://arxiv.org/abs/2211.00447.
- **Abi Jaber, Hauzy, Neuman — *"Trading with propagators and constraints"*** (arXiv 2409.12098, 2024). Same terminology and operator approach with constraints; numerical Nyström solution. https://arxiv.org/abs/2409.12098.
- **Abi Jaber, Bondi, De Carvalho, Neuman, Tuschmann — *"Fredholm Approach to Nonlinear Propagator Models"*** (arXiv 2503.04323, 2025). Nonlinear stochastic Fredholm equation with the *fractional kernel*; multi-exponential approximation used to make computation tractable, with explicit numerical comparison to the true fractional/power-law kernel. https://arxiv.org/abs/2503.04323.
- **Neuman, Voß — *"Optimal Signal-Adaptive Trading with Temporary and Transient Price Impact"*** (SIAM J. FinMath 2022). Exponential resilience, FBSDE solution — not fractional, but the standard signal-adaptive baseline that Forde et al. (2022) compares against. https://arxiv.org/abs/2002.09549.

These works recognize the fractional structure in the *kernel* but not in the *policy*. That is the gap the question identifies.

---

## 5. Why power-law impact is the right kernel to fractionally invert

Two independent threads justify the power-law decay assumption that makes fractional-derivative inversion natural:

- **Empirical**: Bouchaud, Gefen, Potters, Wyart (2004) showed propagator impact $G(t)\sim t^{-\beta}$ with $\beta\approx 0.2$–$0.5$ for individual-trade response in equity markets. https://iopscience.iop.org/article/10.1088/1469-7688/4/2/007.
- **Theoretical**: Jusselin and Rosenbaum (Math. Finance 2020) prove *"No-arbitrage implies power-law market impact and rough volatility"* — the impact function is forced to be of power-law type with exponent matched to the Hurst parameter of rough volatility. https://doi.org/10.1111/mafi.12254 ; arXiv: https://arxiv.org/abs/1805.07134.

So the very kernel against which Forde et al. invert is the unique no-arbitrage-compatible choice, which strengthens the case that "optimal policy = fractional derivative of signal" is the right *canonical* statement of the linear-impact result.

---

## 6. Map of approaches

```mermaid
flowchart LR
  A[Power-law impact kernel<br/>G(t) = c t^{-γ}] --> B[First-order condition<br/>Fredholm/Volterra eq.]
  B --> C{How is the kernel<br/>inverted?}
  C -->|Explicit fractional-<br/>derivative inversion| D[Forde, Sánchez-Betancourt,<br/>Smith QF 2022]
  C -->|Abel-equation closed form| E[Gatheral-Schied-Slynko 2012<br/>Curato-Gatheral-Lillo 2017]
  C -->|Operator/Nyström,<br/>resolvent, FBSDE| F[Abi Jaber-Neuman 2022/24<br/>Hauzy 2024; nonlinear 2025]
  C -->|Approximation by sum<br/>of exponentials| G[Fredholm nonlinear<br/>propagator 2025]
  H[No-arbitrage forces<br/>power-law impact] -.justifies.-> A
  H --> I[Jusselin-Rosenbaum 2020]
```

---

## 7. What is *missing*

The literature has not (to my reading) produced a clean policy statement of the form

$$u^*_t = D^{\alpha}_t\bigl(\text{conditional-expected-signal}_t\bigr) + \text{boundary terms}$$

even though Forde et al. essentially derive this in disguise for the linear, Gaussian-signal, no-temporary-impact case. Specifically:

- No paper writes the **Marchaud** or **Caputo** form of the optimal policy, which would be the natural finite-horizon expression (the standard $D^\alpha$ on $[0,T]$ requires careful boundary handling — the symmetric Abel solution naturally suggests a Riesz-type two-sided fractional derivative).
- No paper draws the explicit analogy to **fractional PID** controllers (e.g. Oustaloup's CRONE control), although that is exactly the engineering literature where "optimal control with power-law memory $\Leftrightarrow$ fractional derivative of the error signal" is canonical (recent survey: arXiv 2512.12111, *"Fractional Calculus in Optimal Control and Game Theory"*).
- With **temporary impact** $\eta u_t$, the policy becomes the resolvent of *(identity + power-law)*, which is governed by **Mittag–Leffler** functions $E_\alpha(\cdot)$. This Mittag-Leffler connection is also not made explicitly in any execution paper I found.
- **Cross-impact / multi-asset** power-law propagators (Abi Jaber et al. 2403.10273) are an obvious next venue: a matrix fractional-derivative policy.

---

## 8. Consensus, disagreements, open questions

**Consensus.** Power-law impact is the right kernel (empirically and by no-arbitrage). The optimal-execution Fredholm equation for the zero-signal case is the Abel equation. The signal-adaptive extension preserves the power-law/fractional structure.

**Disagreements.** None on the math, but a notation/language gap: the Abi Jaber–Neuman line calls $t^{\alpha-1}$ the "fractional kernel" yet does not surface the implied fractional-derivative inversion; the Forde line surfaces it but only in a Gaussian-signal special case.

**Open questions / next experiments.**
1. **Write the canonical statement.** Derive and publish: for $G(t)=ct^{-\gamma}$, no temporary impact, finite horizon, and a general $\mathcal{F}_t$-progressive signal $\alpha_t$, the optimal trading rate is (up to boundary corrections) the symmetric fractional derivative of order $\gamma$ applied to $E_t[\alpha_T]-E_t[\alpha_t]$. Forde et al. did the Gaussian case; the general statement seems doable.
2. **Mittag–Leffler with temporary impact.** Identify the operator semigroup for $(I + \eta^{-1} G)^{-1}$ explicitly; this should yield Mittag-Leffler resolvent kernels.
3. **Multi-asset cross-impact fractional derivative.** Matrix-valued fractional derivative as the optimal cross-impact policy.
4. **Empirical fit.** Estimate $\gamma$ from impact data and *compare* the fractional-derivative-of-signal policy against operator/Nyström numerics on identical data. Does the closed form yield equivalent fills with vastly cheaper compute?
5. **Reinforcement-learning baseline.** A fractional-derivative-of-signal policy is a strong analytical baseline against which to benchmark learned execution policies.

---

## 9. Sources (consolidated)

Primary (read or partially read here):
- Forde, M.; Sánchez-Betancourt, L.; Smith, B. *Optimal trade execution for Gaussian signals with power-law resilience.* Quantitative Finance 22(3), 585–596 (2022). https://doi.org/10.1080/14697688.2021.1950919 ; open PDF: https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26
- Gatheral, J.; Schied, A.; Slynko, A. *Transient linear price impact and Fredholm integral equations.* Math. Finance 22, 445–474 (2012). https://doi.org/10.1111/j.1467-9965.2011.00478.x ; SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1531466
- Curato, G.; Gatheral, J.; Lillo, F. *Optimal execution with non-linear transient market impact.* Quant. Finance 17(1), 41–54 (2017). https://arxiv.org/abs/1412.4839
- Abi Jaber, E.; Neuman, E. *Optimal Liquidation with Signals: the General Propagator Case.* arXiv:2211.00447 (2022, SIFIN 2024). https://arxiv.org/abs/2211.00447
- Abi Jaber, E.; Hauzy, N.; Neuman, E. *Trading with propagators and constraints.* arXiv:2409.12098 (2024). https://arxiv.org/abs/2409.12098
- Abi Jaber, E.; Bondi, A.; De Carvalho, N.; Neuman, E.; Tuschmann, S. *Fredholm Approach to Nonlinear Propagator Models.* arXiv:2503.04323 (2025). https://arxiv.org/abs/2503.04323
- Neuman, E.; Voß, M. *Optimal Signal-Adaptive Trading with Temporary and Transient Price Impact.* arXiv:2002.09549 (2020). https://arxiv.org/abs/2002.09549
- Jusselin, P.; Rosenbaum, M. *No-arbitrage implies power-law market impact and rough volatility.* Math. Finance (2020). https://doi.org/10.1111/mafi.12254 ; arXiv: https://arxiv.org/abs/1805.07134
- Bouchaud, J.-P.; Gefen, Y.; Potters, M.; Wyart, M. *Fluctuations and response in financial markets.* Quant. Finance 4, 176 (2003). https://iopscience.iop.org/article/10.1088/1469-7688/4/2/007
- Gatheral, J. *No-dynamic-arbitrage and market impact.* Quant. Finance 10(7), 749–759 (2010). https://doi.org/10.1080/14697680903373692

Engineering / fractional-control context (not finance):
- *Fractional Calculus in Optimal Control and Game Theory: A Survey.* arXiv:2512.12111 (2025). https://arxiv.org/abs/2512.12111

Adjacent / contrast:
- Gârleanu, N.; Pedersen, L. H. *Dynamic Trading with Predictable Returns and Transaction Costs.* J. Finance 68(6), 2309–2340 (2013). https://doi.org/10.1111/jofi.12080 — exponential / quadratic-cost benchmark, no fractional structure.
- Cartea, Á.; Jaimungal, S. *Incorporating order-flow into optimal execution.* Math. Financ. Econ. 10, 339–364 (2016) — signal-following baseline cited by Forde et al.
- Kalsi, J.; Lyons, T.; Perez Arribas, I. *Optimal Execution with Rough Path Signatures.* SIAM J. FinMath 11(2) (2020) — alternative signature-based path representation.
