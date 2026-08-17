# Evidence notes: novelty of bulk fractional-derivative-of-forecast solution

## Core formula under review

$$ u^{\rm bulk}_t = \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t),\qquad \kappa_{1-\gamma} = \frac{1}{2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)} $$

— a Riesz fractional derivative of order $1-\gamma$, applied to the conditional
forecast curve, for the propagator model with symmetrized power-law kernel
$G(t)=c|t|^{-\gamma}$, $\gamma\in(0,1)$.

## Most directly competing prior art

### A. Forde, Sánchez-Betancourt, Smith (Quant. Finance, 2022)

**arXiv/DOI:** https://doi.org/10.1080/14697688.2021.1950919 ; full PDF at
https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26/files/srf55z9197

**Setup:** identical to ours — propagator price impact $S_t = P_t + \int_0^t G(t-s)dX_s$
with $G(t)=ct^{-\gamma}$, $\gamma\in(0,1)$; Gaussian signal $\xi_t = \mathbb{E}_t[P_T - P_t]$;
optimization over progressively measurable controls with full liquidation.

**Result:** the optimal trading speed is a Gaussian Volterra process
$\hat u_t = \bar u(t) + \int_0^t k(v,t)dW_v$ where $k(v,\cdot)$ and $\bar u$ solve
Fredholm integral equations of the first kind. The Fredholm operator
$(G_1\phi)(t) = \int_0^1 \phi(s) G(t-s)ds$ is inverted via the Chakrabarti–George
(1994) explicit Abel-type formula.

**Crucial passage (p.592, third bullet):**
> "Then we can further re-write $T$ as $T = B^{-1} I_\nu B$, where $B$ is the bounded
> operator on $L^2$ which multiplies functions by $t^{-(1-\nu)/2}$ and $I_\nu$ is the
> **Riemann–Liouville operator** ... so $I_\nu^{-1} = \Gamma(1-r)D^r$, where $I_r$ and
> $D^r$ are the **fractional derivative operators of order $r$**."

with $r = (1-\gamma)/2 = \beta$. This is exactly the **multiplicative Wiener–Hopf
factorization at the half-order $\beta$** that our paper uses in §4.3, applied on
the bounded interval and conjugated by the weight operator $B$.

**Implication:** the FSS2022 paper already (i) recognizes that the bounded-interval
power-law Fredholm inverse decomposes into half-order Riemann–Liouville fractional
derivatives, and (ii) explicitly invokes the operator factorization $G_1 = TT^*$
(Porter–Stirling 1990) that is the operator-language form of the multiplicative
Wiener–Hopf factorization $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$.

**What FSS2022 does NOT do:**
- Does not write the answer as $\mathbb{D}^{1-\gamma}$ acting on the forecast curve.
  Their ansatz is $\hat u_t = \bar u(t) + \int_0^t k(v,t)dW_v$ — a Brownian-driven
  Volterra construction whose kernel $k$ is determined by Fredholm inversion.
- Does not formulate the problem on $\mathbb{R}$ as a translation-invariant bulk
  problem; lives on $[0,T]$ throughout.
- Does not separate bulk vs. boundary structurally; the U-shape and the signal
  contribution emerge entangled via the Chakrabarti–George inversion formula.
- Does not connect to CRONE / fractional PID.
- Final formulas are presented as triple integrals with incomplete-Beta /
  hypergeometric-style special functions (e.g. their equation (26) for the
  rough-signal case is a multi-line expression with $B(z,a,b)$ and $\Gamma$ ratios).
- The Fourier symbol $\hat G(\xi) = c_\gamma |\xi|^{\gamma-1}$ appears in their
  Appendix only for proving positivity / Sobolev-norm equivalence; it is not used
  to define a non-local Riesz derivative.

### B. Abi Jaber & Neuman, *Optimal Liquidation with Signals: the General Propagator Case* (arXiv:2211.00447, v2 Sep 2025, to appear in Math. Finance)

**URL:** https://arxiv.org/abs/2211.00447 ; PDF examined.

**Setup:** bounded interval $[0,T]$, general (not necessarily convolution)
non-negative-definite Volterra kernel, progressively measurable signal $\alpha_t =
\mathbb{E}_t[S_T - S_t]$, instantaneous + transient impact, terminal-inventory penalty,
risk-aversion penalty.

**Result:** value function characterized via an operator-valued Riccati equation and
$L^2$-valued backward stochastic differential equation; explicit operator-resolvent
formulas; Nyström + LSMC numerical scheme. Power-law kernel $H(t)=1/t^\beta$ with
$\beta\in(0,1/2)$ is covered as Example 2.5(2).

**Key passages (introduction):**
- "We characterize the value function in terms of a solution to a free-boundary
  $L^2$-valued backward stochastic differential equation and an operator-valued
  Riccati equation. We then derive analytic solutions to these equations which
  yields an explicit expression for the optimal trading strategy."

**What it does NOT do:** the word "fractional" appears only as a *descriptor* of the
kernel ("fractional kernel", "fractional Brownian motion"), never as the operator
giving the solution. The optimal strategy is given in operator/resolvent form, not
as a fractional derivative of the forecast curve.

### C. Abi Jaber, Neuman, Tuschmann, *Optimal Portfolio Choice with Cross-Impact Propagators* (arXiv:2403.10273, March 2024)

**URL:** https://arxiv.org/abs/2403.10273

**Setup:** matrix-valued Volterra propagator (cross-impact), revenue-risk objective,
progressively measurable signal. Linear-quadratic.

**Result:** explicit operator-resolvent solution. Same overall framework as B,
extended to multi-asset.

**No fractional-derivative-of-forecast formulation.**

### D. Abi Jaber, Bondi, De Carvalho, Neuman, Tuschmann, *Fredholm Approach to Nonlinear Propagator Models* (arXiv:2503.04323, March 2025)

**URL:** https://arxiv.org/abs/2503.04323

**Setup:** non-linear price impact $h(D_t^X)$ with general Volterra propagator
$G(t,s)$ including power-law. Single-asset optimal execution with alpha signal.

**Result:** FOC is a *non-linear* stochastic Fredholm equation; iterative solver
with convergence rate; numerical results for power-law (via sum-of-exponentials
approximation).

**No fractional-derivative-of-forecast formulation.** Uses sum-of-exponentials
approximation for power-law numerics — i.e. avoids the fractional-operator structure
rather than exploiting it.

### E. Gatheral, Schied, Slynko, *Transient linear price impact and Fredholm integral equations* (Math. Finance, 2012)

**Setup:** deterministic case (no signal), bounded interval, convex/non-increasing
kernel including power-law.

**Result:** FOC is a Fredholm equation; explicit U-shape closed form for power-law
case via Abel-equation inversion (their Example 2.30):
$u^0(t) = c_1 (t(T-t))^{(1-\gamma)/2 - 1}$.

**No signal, no forecast curve, no fractional-derivative operator language.**
This is the deterministic skeleton on top of which FSS2022 built the
signal-adaptive extension.

## Adjacent literature without direct overlap

### F. Neuman & Voß, *Optimal signal-adaptive trading with temporary and transient price impact* (SIAM J. Financial Math., 2022)

**Setup:** exponential propagator (Obizhaeva–Wang) + temporary impact + general
square-integrable semimartingale signal.

**Result:** explicit FBSDE-system solution. Affine-linear feedback law in inventory
and an auxiliary state. Power-law not covered (the exponential propagator makes the
problem state-Markovian).

### G. Cartea & Jaimungal (2016); Cartea, Jaimungal, Penalva textbook (2015); Lehalle–Neuman (2019)

Signal-adaptive trading in various settings (mostly Almgren–Chriss / Obizhaeva–Wang
frameworks). No fractional-derivative-of-forecast formulation.

### H. Gârleanu & Pedersen, *Dynamic Trading with Predictable Returns and Transaction Costs* (J. Finance, 2013)

Linear-quadratic, mean-reverting alpha, *quadratic* transaction cost (no propagator
memory). Closed-form feedback law involves matrix Riccati. Conceptually different —
the cost structure has no power-law/Volterra memory, so no fractional operators.

### I. Almgren–Chriss (2000/2001) and Obizhaeva–Wang (2013)

Constant temporary impact / exponential propagator — both lead to ODE/Riccati
closed forms without fractional operators.

### J. Curato, Gatheral, Lillo, *Optimal execution with non-linear transient market impact* (Quant. Finance, 2017)

Non-linear power-law impact; Urysohn integral equations; numerical solution. No
fractional-operator formulation.

### K. Fractional control / CRONE / Oustaloup (1991, 2000)

Fractional PID controllers — control engineering literature, mechanical/biological
systems. Apply fractional differentiators of order $0<\alpha<1$ in feedback loops.
**No application to optimal execution in this literature.**

### L. Survey: *Fractional Calculus in Optimal Control and Game Theory* (arXiv:2512.12111, Dec 2025)

**URL:** https://arxiv.org/abs/2512.12111

Reviews fractional calculus in control: Caputo, Riemann–Liouville, Grünwald–Letnikov
operators; Oustaloup frequency-domain realizations; sum-of-exponentials
approximations; fractional Pontryagin/HJB; fractional LQR / MPC / PID. Domains
covered: physical, biological, engineered systems. **Optimal execution is not
mentioned.**

## Classical machinery (used but not novel)

- **Riesz fractional derivative via Fourier symbol $|\xi|^{1-\gamma}$:** Stein 1970
  §V.1; Samko–Kilbas–Marichev 1993 §7.1. Textbook.
- **Wiener–Hopf factorization $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$:**
  SKM 1993; classical Wiener–Hopf 1931; Noble 1958; Krein 1962.
- **Wiener filter / causal realization:** Wiener 1949 *Extrapolation, Interpolation, and Smoothing of Stationary Time Series*.
- **Bouchaud propagator origin:** Bouchaud–Gefen–Potters–Wyart 2004; Gatheral 2010.
- **Chakrabarti–George (1994) Abel inversion formula** for the bounded-interval
  power-law Fredholm.

## Comparison matrix

| Feature | Our paper | FSS2022 | Abi Jaber-Neuman | Neuman-Voß | Gatheral-Schied-Slynko | CRONE lit. |
|---|---|---|---|---|---|---|
| Power-law propagator $G\propto t^{-\gamma}$ | ✓ | ✓ | ✓ | ✗ (exp only) | ✓ | n/a |
| Stochastic signal | ✓ | ✓ (Gaussian) | ✓ (general prog.) | ✓ (semi-mart.) | ✗ | n/a |
| Fractional derivative explicitly | ✓ Riesz | ✓ R–L (half-order, on $[0,T]$) | ✗ | ✗ | ✗ | ✓ (different problem) |
| Acts directly on **forecast curve** $\bar\alpha(t,\cdot)$ | ✓ | ✗ (Volterra ansatz on $W$) | ✗ (Riccati) | ✗ | n/a | n/a |
| Whole-line / translation-invariant bulk | ✓ | ✗ | ✗ | ✗ | ✗ | n/a |
| Bulk/boundary decomposition | ✓ | ✗ | ✗ | ✗ | ✗ | n/a |
| Wiener–Hopf multiplicative factorization | ✓ (on $\mathbb{R}$) | ✓ (on $[0,1]$, via $G_1=TT^*$) | ✗ | ✗ | ✗ | n/a |
| CRONE / fractional-PID link | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ |

## Bottom-line novelty assessment

**Not novel:**
1. Power-law-kernel optimal execution with signal is well-trodden (FSS2022,
   Abi Jaber–Neuman 2022/24/25).
2. The fact that the bounded-interval Fredholm inverse for $G=ct^{-\gamma}$
   factorizes through Riemann–Liouville half-order operators is **explicitly known
   and used** in FSS2022 (their decomposition $T = B^{-1}I_\nu B$, $r=(1-\gamma)/2$).
3. The certainty-equivalence substitution $\alpha\to\bar\alpha$ is implicit
   throughout the signal-adaptive-trading literature, even when not named.

**Partially novel (re-organization of known content):**
4. Writing the answer as $\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$ on $\mathbb{R}$
   in clean Riesz form, rather than as a Volterra-ansatz solution to a Fredholm
   equation or a BSDE / operator-resolvent expression. This is a reorganization, not
   a new result, but it is genuinely new presentation — no paper writes it this way.
5. The bulk/boundary spine — treating the whole-line translation-invariant case as
   the primary object and bounded-interval / half-line as boundary perturbations —
   is novel framing.
6. The forecast curve $\bar\alpha(t,\cdot)$ as an explicit object on which a
   deterministic non-causal operator acts is a useful re-presentation; existing
   work substitutes conditional expectations inside expressions but does not name
   the resulting curve.

**Novel:**
7. The explicit bridge to CRONE / Oustaloup fractional-PID control. No
   optimal-execution paper draws this connection; the 2025 survey of fractional
   calculus in control does not cover optimal execution. This is a true
   contribution at the field-bridging level.
8. The careful distinction between two Wiener–Hopf factorizations (bulk-symbol on
   $\mathbb{R}$ acting at the operator level for all domains; augmented-symbol on
   $[0,\infty)$ as the half-line boundary-mode picker). FSS2022 use only the
   bounded-interval Porter–Stirling factorization without this domain-level
   conceptual separation.

## Inspected sources & URLs

- FSS2022 PDF: https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26/files/srf55z9197
- Abi Jaber–Neuman 2022 (v2 2025): https://arxiv.org/abs/2211.00447 / https://arxiv.org/pdf/2211.00447v2
- Abi Jaber–Neuman–Tuschmann 2024: https://arxiv.org/abs/2403.10273
- Abi Jaber et al. (nonlinear) 2025: https://arxiv.org/abs/2503.04323
- Fractional Calculus in Optimal Control survey: https://arxiv.org/abs/2512.12111
- Gatheral–Schied–Slynko 2012: cited in FSS2022 and Abi Jaber–Neuman 2022 (their refs)
- Neuman–Voß 2022: cited in FSS2022 (their ref) and Abi Jaber–Neuman 2022 (their ref [38])
- Cross-checked propagator-literature list against the paper's own §6 references.
