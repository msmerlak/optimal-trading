# Unified treatments of optimal trading and optimal execution

**Author:** Feynman (research note)
**Date:** 2026-06-27
**Context:** Triggered by a reviewer finding on
`papers/fractional-derivative-optimal-execution.md` §5.4 (Wiener–Hopf
half-line), which conflated finite-horizon execution with stationary
signal-tracking. This note surveys the literature on frameworks that
*intentionally* unify the two problems and identifies the natural
meta-cost-functional from which both arise as parameter limits.

---

## 1. The two regimes, traditionally separate

The mathematical-finance literature has long treated two superficially
similar but structurally distinct problems with separate machinery.

### 1.1 Optimal execution

A trader holds an inventory $X_0$ that must be unwound by horizon $T$.
Decision variable: trading rate $u_t$ with $\int_0^T u_t\,dt = X_0$
(equivalently, $X_T = 0$ as a hard terminal constraint). Cost
functional is implementation shortfall:

$$ \mathcal{C}_{\rm exec}(u) \;=\; \mathbb{E}\!\int_0^T \Bigl[\, u_t\,S_t \;+\; \tfrac{1}{2}\eta\, u_t^2 \;-\; u_t\,\alpha_t \,\Bigr]\,dt, \qquad X_T = 0. $$

Canonical models: Almgren–Chriss (2000), Obizhaeva–Wang (2013),
Gatheral–Schied–Slynko (2012), Forde–Sánchez-Betancourt–Smith (2022),
Neuman–Voß (2020), Abi Jaber–Neuman (2022). Horizon is finite.
Inventory is *the* state variable. The trader is *forced* to trade.

### 1.2 Stationary-signal portfolio trading

A trader holds a continuously rebalanced position $X_t$ driven by a
mean-reverting return-forecast signal $\alpha_t$. Decision variable:
trading rate $u_t = dX_t/dt$. Cost functional combines
risk-adjusted forecast capture against quadratic trading costs:

$$ \mathcal{C}_{\rm port}(u) \;=\; \mathbb{E}\!\int_0^\infty e^{-\rho t} \Bigl[\, -X_t\,\alpha_t \;+\; \tfrac{\gamma_{\rm risk}}{2}\,\sigma^2\,X_t^2 \;+\; \tfrac{1}{2}\eta\, u_t^2 \,\Bigr]\,dt. $$

Canonical models: Gârleanu–Pedersen (2013, 2016), Collin-Dufresne–Daniel–
Sağlam (2014), Martin (2014). Horizon is infinite (or stationary). No
terminal constraint. The trader *chooses* the position freely. Risk
penalty $\gamma_{\rm risk} \sigma^2 X_t^2$ regularizes the problem and
gives a finite optimal holding.

### 1.3 Why the regimes look unrelated

| Aspect | Execution | Portfolio trading |
|---|---|---|
| Horizon | Finite $T$ | Infinite (stationary) |
| State | Inventory $X_t$ | Position $X_t$ |
| Terminal | Hard $X_T = 0$ | No constraint |
| Risk | Implementation-shortfall variance | Mean-variance running penalty |
| Signal $\alpha$ | Often deterministic / drifted Brownian | Mean-reverting OU |
| Impact kernel | Power-law / propagator (transient) | Quadratic temporary (often) |
| Solution tool | Fredholm / FBSDE / Volterra control | Riccati ODE |
| Output | One trajectory $u^*$ unwinding $X_0$ | Stationary policy $u^* = f(X,\alpha)$ |

These look like different problems. They are not.

---

## 2. Frameworks that intentionally unify the two

### 2.1 Moreau–Muhle-Karbe–Soner 2017 — small-impact asymptotics

*Trading with Small Price Impact*, Mathematical Finance 27(2), 350–400,
2017. DOI: https://doi.org/10.1111/mafi.12098, arXiv:1402.5304.

A multi-asset utility-maximizing investor faces *linear price impact*
$\lambda\,u_t$. In the small-$\lambda$ limit, the optimal policy is
expanded to first order in $\lambda$. The leading-order behaviour
splits into:

- a frictionless Merton-style portfolio target $X^{\rm fric}_t$, and
- a *correction* $X_t - X^{\rm fric}_t$ that decays toward the target.

The decay equation for the correction is *literally an execution
problem* whose "inventory" is the displacement from the frictionless
target. The authors observe: "These results … unveil close
connections to optimal execution problems and to other market
frictions such as proportional and fixed costs" (abstract). The unifying
mechanism is the *frictionless target* as a moving anchor, with
execution being the special case where the target is held fixed at
zero.

**What is unified.** Linear impact, utility maximization, Markovian
signals, single-asset and multi-asset.

**Limitation.** Only the *small-impact asymptotic* regime; no
transient (propagator) impact; no fractional kernels.

### 2.2 Gârleanu–Pedersen 2013 + Frictions (2016) — multi-signal, persistent

- *Dynamic Trading with Predictable Returns and Transaction Costs*,
  Journal of Finance 68(6), 2309–2340, 2013. DOI: https://doi.org/10.1111/jofi.12080.
- *Dynamic Portfolio Choice with Frictions*, Journal of Economic Theory
  165, 487–516, 2016. https://nbgarleanu.github.io/DynamicPortfolioChoiceWithFrictions.pdf.

The 2013 paper handles multiple mean-reverting signals with quadratic
*transitory* costs and gives the "aim portfolio" closed form. The 2016
*Frictions* paper extends to **both transitory and persistent**
transaction costs — the persistent component is structurally identical
to the propagator-style transient impact used in the execution
literature.

Crucially: the 2016 framework is derived as the *continuous-time limit
of a discrete-time dealer-inventory model*. When the dealer-inventory
mean-reversion is slow, the persistent cost dominates and the optimal
strategy is a smooth, finite-turnover trajectory — i.e. an execution-
like profile. When fast, transitory cost dominates and the strategy is
the partial-adjustment GP rule.

**What is unified.** Linear-quadratic, multi-signal, multi-asset,
combined transitory + persistent costs.

**Limitation.** Persistent cost is exponential (Markov factor), not
power-law / general propagator. Infinite horizon only; finite-horizon
execution with hard terminal $X_T=0$ is a separate calculation.

### 2.3 Cartea–Jaimungal–Penalva 2015 — textbook unification

*Algorithmic and High-Frequency Trading*, Cambridge University Press,
2015. ISBN 978-1-107-09114-6.
https://www.cambridge.org/ae/universitypress/subjects/mathematics/mathematical-finance/algorithmic-and-high-frequency-trading

The book treats execution (large order liquidation, VWAP/TWAP), market
making, statistical arbitrage / pairs, and execution in dark pools all
under a single HJB / stochastic-control template. The unifying step is
a generic value-function ansatz $V(t, x, S, \alpha)$ with
problem-specific terminal conditions:

- $X_T = 0$ with hard penalty → execution.
- Free $X_T$ with running quadratic penalty → market making.
- Free $X_T$ with mean-variance utility → statistical arbitrage.

**What is unified.** Conceptual / pedagogical: the HJB form is the same,
only the boundary data changes.

**Limitation.** Limited to temporary + linear-transient impact; the
power-law / propagator case is not the textbook's focus.

### 2.4 Bouchard–Fukasawa–Herdegen–Muhle-Karbe 2018 — equilibrium

*Equilibrium Returns with Transaction Costs*, Finance and Stochastics
22, 569–601, 2018. arXiv:1707.08464. https://hal.science/hal-01569408v3/document.

Multi-agent equilibrium with heterogeneous mean-variance investors and
quadratic transaction costs. The equilibrium is characterized as the
unique solution of a coupled *linear FBSDE system*. Both endogenous
returns and endogenous trading volumes are recovered. The framework
implicitly unifies trading (each investor's optimization is a GP-style
portfolio problem) with the market-level execution dynamics (aggregate
volume profile).

**What is unified.** Equilibrium + portfolio + transaction-cost
incidence on returns.

**Limitation.** Quadratic costs only; no propagator / power-law.

### 2.5 Abi Jaber–Neuman–Tuschmann 2024 — strongest unified treatment

*Optimal Portfolio Choice with Cross-Impact Propagators*,
arXiv:2403.10273, March 2024. https://arxiv.org/abs/2403.10273.

This is the closest to a *clean* unified framework. The agents face a
**matrix-valued Volterra propagator** for transient cross-impact plus a
temporary impact term, and maximize a **revenue–risk functional** with
a progressively measurable signal. The first-order condition is a
*coupled stochastic Fredholm equation of the second kind*. The abstract
states explicitly: "we provide an implementation of the solutions to
the optimal portfolio choice problem **and to the associated optimal
execution problem**" — both regimes are obtained from the same FOC by
adjusting the terminal data and the running penalty.

The unifying device is the operator-resolvent representation of the
FOC, which is *agnostic* about whether the user supplies (i) a terminal
inventory constraint or (ii) a running quadratic penalty for portfolio
deviation from a target. The same machinery handles both.

**What is unified.**

- Volterra propagator impact (general kernel, including power-law).
- Temporary impact.
- Cross-asset impact via matrix kernel.
- Progressive-measurable signal.
- Portfolio choice **and** execution under one resolvent calculus.

**Limitation.** Stochastic control is infinite-dimensional; solutions
are operator-implicit rather than fully closed-form. Empirical
calibration is sketched only for cross-impact, not for the power-law
exponent.

### 2.6 Webster 2023 — practitioner-oriented unified textbook

*Handbook of Price Impact Modeling*, CRC Press, 2023.
DOI: https://doi.org/10.1201/9781003316923. ISBN 978-1-032-32822-5.

Industry-oriented treatment. Webster (D. E. Shaw) develops a single
price-impact framework that is used for both **execution** (pre-trade
TCA, schedule optimization) and **portfolio management** (alpha
shrinkage, capacity, drawdown attribution). The unifying object is the
*impact state variable* — the price displacement induced by historical
trading, which is the natural extension of the propagator kernel to a
sufficient statistic carried as part of the state.

**What is unified.** Execution costing, alpha discount under impact,
portfolio sizing, capacity, and live-trading attribution.

**Limitation.** Practitioner book; mathematical treatment is lighter
than the academic literature.

### 2.7 Mean-quadratic-variation reformulation — Forsyth et al.

*Optimal trade execution: A mean–quadratic-variation approach*, J.
Econ. Dyn. Control 36(12), 1971–1991, 2012.
https://www.sciencedirect.com/science/article/abs/pii/S0165188912001236.

Replaces mean-variance with mean-quadratic-variation. This pushes
execution into a form that is *time-consistent* and Bellman-amenable,
which makes it sit naturally alongside portfolio choice (which is also
time-consistent under MQV). Not a full unification but a step that
removes the artificial divide caused by time-inconsistent
mean-variance in the Almgren–Chriss formulation.

---

## 3. The unifying meta-cost-functional

All seven frameworks above can be read as different parameter regimes
of a single Volterra–quadratic cost functional:

$$ \boxed{ \mathcal{C}(u) \;=\; \mathbb{E}\!\int_0^T \!\!\Bigl[\, \underbrace{u_t\,\mathcal{G}u(t)}_{\text{transient/propagator impact}} \;+\; \underbrace{\tfrac{1}{2}\eta\,u_t^2}_{\text{temporary impact}} \;+\; \underbrace{\tfrac{\gamma_{\rm risk}}{2}\sigma^2 X_t^2}_{\text{inventory risk}} \;-\; \underbrace{u_t\,\alpha_t}_{\text{signal capture}} \Bigr]\,dt \;+\; \underbrace{\tfrac{\Lambda}{2}(X_T-X^*)^2}_{\text{soft terminal}} } $$

where $\mathcal{G}u(t) := \int_0^t G(t-s)\,u_s\,ds$ is the propagator
convolution. The five knobs $(T, \Lambda, \gamma_{\rm risk}, \eta, G)$
parameterise *the entire literature*.

### 3.1 Recovering each regime

| Regime | $T$ | $\Lambda$ | $\gamma_{\rm risk}$ | $\eta$ | $G$ |
|---|---|---|---|---|---|
| Almgren–Chriss execution | $<\infty$ | $\to\infty$ | mean-var | $>0$ | linear permanent only |
| Obizhaeva–Wang | $<\infty$ | $\to\infty$ | 0 | $>0$ | $\rho e^{-\rho t}$ |
| Gatheral–Schied–Slynko | $<\infty$ | $\to\infty$ | 0 | 0 | $t^{-\gamma}$ |
| Forde–S.B.–Smith 2022 | $<\infty$ | $\to\infty$ | 0 | 0 | $t^{-\gamma}$ + Gaussian Volterra $\alpha$ |
| Neuman–Voß 2020 | $<\infty$ | $\to\infty$ | 0 | $>0$ | $\rho e^{-\rho t}$ |
| Abi Jaber–Neuman 2022 | $<\infty$ | $\to\infty$ | 0 | $\ge 0$ | general |
| **Gârleanu–Pedersen 2013** | $\to\infty$ | 0 | $>0$ | $>0$ | none |
| **Gârleanu–Pedersen 2016** | $\to\infty$ | 0 | $>0$ | $>0$ | exponential |
| Moreau–Muhle-Karbe–Soner 2017 | finite | utility | utility | $\to 0$ | linear |
| **Abi Jaber–Neuman–Tuschmann 2024** | finite | flexible | $\ge 0$ | $\ge 0$ | general matrix Volterra |
| Bouchard et al. 2018 (equilibrium) | $\to\infty$ | 0 | $>0$ | $>0$ | none |

The two regimes the user-paper conflates are:
- **Finite-horizon execution** = $\Lambda \to \infty$, $\gamma_{\rm risk}=0$, $T<\infty$.
- **§5.4 Wiener–Hopf "infinite-horizon execution"** = $\Lambda=0$,
  $T\to\infty$, $\gamma_{\rm risk}=?$, $\alpha$ stationary.

If $\gamma_{\rm risk}=0$ in the latter, the cost functional is *unbounded
below* (the trader can scale $u$ arbitrarily large to capture any
finite-mean signal forever) — i.e. the problem is ill-posed. **A
nonzero $\gamma_{\rm risk}$ is required for well-posedness of the §5.4
W–H regime**, which makes it a Gârleanu–Pedersen-style portfolio
problem, *not* an execution problem.

### 3.2 Where the §5.4 fix should land

Two honest options for the paper:

**Option A — relabel §5.4 as the GP/portfolio companion.** Add a
running $\frac{1}{2}\gamma_{\rm risk}\sigma^2 X_t^2$ penalty to the
cost, re-derive (★_WH) with the penalty in place, and present the
W–H factorization as the *propagator-extension of Gârleanu–Pedersen
2013*. This is a genuine contribution (GP 2013/2016 use exponential
persistent cost; the W–H factorization extends them to power-law
kernels) and the framing is honest.

**Option B — use the AJNT 2024 framework.** Cite Abi Jaber–Neuman–
Tuschmann 2024 as the encompassing setting; present the finite-horizon
result of Theorem 4.1 as the *Sonine-pair specialization* of their
operator-resolvent FOC under power-law $G$ and hard terminal, and §5.4
W–H as the *stationary specialization* under power-law $G$ and running
risk penalty. Both are then corollaries of a known unified framework
rather than rederivations.

Option B is cleaner because it puts the paper in a well-developed
recent literature (AJNT) rather than reinventing the unification.
Option A is more original but requires more work and a new theorem.

---

## 4. Open gaps in the unified treatments

Even AJNT 2024, the strongest unified work, leaves several gaps that
the current paper could plausibly fill:

1. **Closed-form Sonine inversion** for power-law $G$. AJNT give
   operator-resolvent representations; explicit closed forms via Sonine
   pairs / Riesz fractional derivatives on $[0,T]$ are not in their
   paper. Theorem 4.1 of the current draft fills this if F1–F3 from
   the reviewer pass are fixed.

2. **Wiener–Hopf factorization of the matrix Volterra propagator.** The
   AJNT 2024 cross-impact framework uses operator resolvents; an
   explicit W–H factorization of the matrix symbol
   $\widehat{\mathbf{G}}(\xi)$ on the half-line is not in the
   literature. The current draft's §5.4 (with Option A or B) is a step
   in that direction.

3. **CRONE / fractional-PID translation.** None of the unified
   treatments explicitly cross-reference the engineering CRONE
   literature, which gives ready-made robustness diagnostics and
   tuning rules. The current draft's §8.1 + the companion lit review
   `outputs/crone-control-optimal-trading.md` start this translation.

4. **Empirical calibration of the meta-functional.** No paper jointly
   fits all five knobs $(T, \Lambda, \gamma_{\rm risk}, \eta, G)$ on a
   single dataset. Most papers fix $\Lambda$ at one extreme (0 or
   $\infty$) and infer the rest.

5. **Time-consistent risk measures.** Mean-variance is
   time-inconsistent; mean-quadratic-variation (Forsyth 2012) is
   time-consistent; entropic / CVaR risk is partially time-consistent.
   No unified treatment exists across all three risk choices.

---

## 5. Synthesis

**The unification exists.** Abi Jaber–Neuman–Tuschmann 2024
(arXiv:2403.10273) provides the single operator-resolvent calculus that
covers both portfolio choice and execution for Volterra propagators
with predictive signals. Gârleanu–Pedersen 2013/2016 is the
linear-quadratic / exponential-kernel precursor. Moreau–Muhle-Karbe–
Soner 2017 unifies the small-impact regime. Cartea–Jaimungal–Penalva
2015 unifies pedagogically.

**The meta-cost-functional of §3 is the right object.** Every published
result is a parameter-limit of one quadratic Volterra functional with
five knobs: horizon, terminal-stiffness, risk penalty, temporary
impact, and propagator kernel.

**For the §5.4 problem in `papers/fractional-derivative-optimal-execution.md`,**
the honest fix is to (i) add an inventory risk penalty
$\frac{1}{2}\gamma_{\rm risk}\sigma^2 X_t^2$ (otherwise the
infinite-horizon problem is ill-posed) and (ii) acknowledge AJNT 2024
as the encompassing framework. The W–H factorization then becomes the
explicit closed-form solution of AJNT's resolvent equation in the
power-law / stationary regime — a contribution, not a re-derivation.

---

## 6. Recommended reading order for the user

1. **Abi Jaber–Neuman–Tuschmann 2024** (arXiv:2403.10273) — the
   unified operator-resolvent framework. Read §2 and the FOC in §3
   first; this is the natural framing for the current paper.
2. **Gârleanu–Pedersen 2016** *Dynamic Portfolio Choice with Frictions*
   — the linear-quadratic precursor with persistent costs. Read for
   the GP-style "aim portfolio" intuition and for the discrete-to-
   continuous-time limit argument.
3. **Moreau–Muhle-Karbe–Soner 2017** (Math. Finance 27) — the
   small-impact asymptotic that makes the execution/portfolio
   connection most transparent.
4. **Abi Jaber–Neuman 2022** (arXiv:2211.00447) — the execution-only
   precursor of AJNT 2024; introduces the stochastic Fredholm
   formulation.
5. **Webster 2023** *Handbook of Price Impact Modeling* — practitioner
   perspective; useful for empirical and live-trading sanity checks.
6. **Cartea–Jaimungal–Penalva 2015** — textbook background and HJB-
   style unification under one value-function template.

---

## 7. References

- Abi Jaber, E.; Neuman, E. *Optimal Liquidation with Signals: the
  General Propagator Case.* Math. Finance 35, 2025.
  arXiv:2211.00447 (Nov 2022). https://arxiv.org/abs/2211.00447.
  DOI: https://doi.org/10.1111/mafi.12465.
- Abi Jaber, E.; Neuman, E.; Tuschmann, S. *Optimal Portfolio Choice
  with Cross-Impact Propagators.* arXiv:2403.10273 (Mar 2024).
  https://arxiv.org/abs/2403.10273.
- Bouchard, B.; Fukasawa, M.; Herdegen, M.; Muhle-Karbe, J.
  *Equilibrium Returns with Transaction Costs.* Finance and Stochastics
  22, 569–601, 2018. arXiv:1707.08464. https://hal.science/hal-01569408v3/document.
- Cartea, Á.; Jaimungal, S.; Penalva, J. *Algorithmic and High-Frequency
  Trading.* Cambridge University Press, 2015. ISBN 978-1-107-09114-6.
- Forsyth, P. A.; Kennedy, J. S.; Tse, T.; Windcliff, H. *Optimal
  trade execution: a mean–quadratic-variation approach.* J. Econ. Dyn.
  Control 36(12), 1971–1991, 2012.
  https://www.sciencedirect.com/science/article/abs/pii/S0165188912001236.
- Gârleanu, N.; Pedersen, L. H. *Dynamic Trading with Predictable
  Returns and Transaction Costs.* J. Finance 68(6), 2309–2340, 2013.
  DOI: https://doi.org/10.1111/jofi.12080.
- Gârleanu, N.; Pedersen, L. H. *Dynamic Portfolio Choice with
  Frictions.* J. Econ. Theory 165, 487–516, 2016.
  https://nbgarleanu.github.io/DynamicPortfolioChoiceWithFrictions.pdf.
- Moreau, L.; Muhle-Karbe, J.; Soner, H. M. *Trading with Small Price
  Impact.* Math. Finance 27(2), 350–400, 2017. arXiv:1402.5304.
  DOI: https://doi.org/10.1111/mafi.12098.
- Webster, K. T. *Handbook of Price Impact Modeling.* CRC Press,
  2023. DOI: https://doi.org/10.1201/9781003316923.

(See `outputs/unified-trading-execution.provenance.md` for source-by-
source notes and the verification log.)
