# Adapted Convex Duality: A Common Skeleton for Wiener–Hopf, Kalman, and Optimal Trading

---

> **Draft status:** First draft. Position paper. The framework is standard
> piece-by-piece (Hilbert-space convex optimization, nest algebras, spectral
> factorization, LQG separation); the contribution is a unifying reading,
> not a new theorem. Claims marked *tentative* have not been cross-checked
> against the full operator-theoretic literature.

---

## Abstract

A surprising number of problems in prediction, filtering, and control admit
the same skeleton:

> **Minimize a convex functional on a Hilbert space, subject to the constraint
> that the solution respect a nest (a totally ordered chain of closed
> subspaces, typically the filtration of "the past").**

Wiener–Hopf prediction, Kolmogorov–Szegő spectral factorization, the Kalman
filter, the Gârleanu–Pedersen and Bouchaud–Gatheral optimal-trading
problems, and even certain LQG control problems are all of this form. In
each case the unconstrained gradient lives in the *full* Hilbert space; the
nest constraint forces the first-order condition into the *anticausal
complement*, and the constructive solution requires a factorization of the
quadratic form (the Hessian) *inside the nest algebra*. The Cholesky
factorization, the innovations representation, and the Wiener–Hopf spectral
factorization are three avatars of the same operation. We call this skeleton
**adapted convex duality**. The note collects the abstract setup, three
canonical instances, the factorization theorem that makes the FOC solvable,
and a list of cases where the skeleton survives, deforms, or breaks (rough
volatility, non-Gaussian filtering, non-quadratic $J$).

---

## 1. Introduction

### 1.1 The shared structure

Consider three classical problems.

**(W) Wiener–Hopf prediction.** Given a stationary scalar process $y_t$
with spectral density $S(\omega)$, find the best linear *causal* predictor
of $y_{t+h}$ from the past $\{y_s : s \le t\}$. The solution uses the
spectral factorization $S = |S_+|^2$ with $S_+$ outer (causal) and applies
a causal projection to the unconstrained predictor.

**(K) Kalman filtering.** Given an observation process $Y_t = HX_t + V_t$,
find the best (minimum-variance) estimator $\hat X_t$ of the latent state
$X_t$ that is **adapted** to the observation filtration $\mathcal{F}_t^Y$.
The solution proceeds by orthogonalizing the observations into innovations
$\nu_t = Y_t - H\hat X_{t|t-1}$, computing covariances recursively, and
expressing $\hat X_t$ as a causal linear functional of $\nu$.

**(T) Optimal trading with transient impact.** Given a signal $f_t$
predicting per-trade return and a positive-definite impact kernel $K$, find
the adapted trade rate $x_t$ minimizing the stationary cost
$\frac{1}{2}\langle x, Kx\rangle - \langle f, x\rangle$. The unconstrained
optimum solves $Kx^\star = f$ (a Fredholm/convolution equation); imposing
causality requires the Wiener–Hopf factorization $K = K_+ K_-$ and gives
the causal rule $x^\star_t = [K_-^{-1} \widetilde f]_+$ with
$\widetilde f = K_+^{-1} f$.

The three problems look superficially different — one is prediction, one
is filtering, one is control — but they share the *same three structural
ingredients*:

1. A **Hilbert space** $H$ (square-summable processes, $L^2$ of a
   probability space, etc.).
2. A **convex (quadratic) functional** $J : H \to \mathbb{R}$ whose
   unconstrained minimizer is easy to describe.
3. A **nest** $\mathcal{N} = \{H_t\}_{t\in T}$: a totally ordered family
   of closed subspaces (the past up to time $t$).

The shared problem is

$$\min_{u} J(u) \quad \text{subject to } u \text{ is \emph{adapted} to } \mathcal{N},$$

where "adapted" means $u_t \in H_t$ for each $t$ in the appropriate sense,
or equivalently that the operator built from $u$ leaves every $H_t$
invariant.

### 1.2 Why these problems collapse to one

The unifying observation is dual:

- **Primal**: the feasible set is the closed convex cone (in fact, a
  closed subspace) of nest-respecting elements.
- **Dual / FOC**: at the constrained optimum $u^\star$, the gradient
  $\nabla J(u^\star)$ must be **orthogonal to every adapted perturbation**.
  Equivalently, $\nabla J(u^\star)$ lies in the **anticausal complement**
  of the nest. In WH notation, $[\nabla J(u^\star)]_+ = 0$.

This is just the KKT condition for a convex problem with linear-subspace
constraint. What is *nontrivial* is that the gradient itself involves the
quadratic form $K$ (the metric, the covariance, the impact kernel), and
this $K$ does not in general respect the nest. The constructive solution
requires factoring $K$ into pieces that *do* respect the nest:

- $K = LL^*$ with $L$ lower-triangular (Cholesky / Kalman innovations);
- $S = S_+\overline{S_+}$ with $S_+$ outer (Kolmogorov–Szegő);
- $K = K_+ K_-$ with $K_\pm$ causal/anticausal Hardy-space factors
  (Wiener–Hopf).

All three are special cases of **factorization inside a nest algebra**
[Arveson 1975, Davidson 1988]. The nest algebra
$\mathcal{T}(\mathcal{N})$ is the (weak-operator-closed) algebra of
bounded operators on $H$ that leave every $H_t$ invariant; its self-adjoint
generators are precisely the *adapted* processes. A factorization
$K = AA^*$ with $A \in \mathcal{T}(\mathcal{N})$ is what makes the
constrained FOC solvable in closed form, by reducing it to two
nest-preserving inversions.

### 1.3 What this draft adds

The pieces are individually classical. What we hope to make explicit:

1. A clean restatement of all three problems as instances of one convex
   program (§2).
2. A side-by-side dictionary mapping convex/factorization vocabulary
   across the three fields (§3, Table 1).
3. The factorization theorem stated once and instantiated three times
   (§4).
4. A taxonomy of which generalizations preserve the skeleton (LQG
   separation, matrix WH, multi-asset trading), deform it (rough
   volatility = factorization without a lower bound on order), or break
   it (non-Gaussian filtering, non-quadratic $J$, mean-field crowding)
   (§5).
5. Open questions, including: does an "adapted proximal operator" exist
   for non-quadratic but convex $J$, generalizing WH to the
   $f$-divergence world? (§6).

---

## 2. The Abstract Framework

### 2.1 Nests and the adapted subspace

Let $H$ be a real Hilbert space. A **nest** $\mathcal{N}$ on $H$ is a
totally ordered family $\{H_t\}_{t\in T}$ of closed subspaces, with
$H_s \subseteq H_t$ for $s \le t$, containing $\{0\}$ and $H$, and closed
under arbitrary intersections and closed linear spans (a complete nest in
the sense of Ringrose 1965).

The **projection** onto $H_t$ is denoted $P_t$, and the family
$\{P_t\}_{t\in T}$ is an increasing family of orthogonal projections —
this is the operator-theoretic stand-in for a filtration.

The **adapted subspace** is

$$H^{\mathrm{ad}} = \{u \in H : \text{$u$ is compatible with } \mathcal{N}\}.$$

Concretely, "compatible" means one of three equivalent things in our
canonical examples:

- *Process interpretation*: $u = (u_t)_{t\in T}$ with $u_t \in H_t$ for each
  $t$ (so $u$ is **adapted** to the filtration).
- *Operator interpretation*: the multiplication/convolution operator
  $M_u$ built from $u$ lies in the nest algebra
  $\mathcal{T}(\mathcal{N})$.
- *Causal-projection interpretation*: $P_+ u = u$, where $P_+$ is the
  projection onto the causal (lower-triangular) part.

The orthogonal complement $H^{\mathrm{ad},\perp}$ is the **anticausal
complement** (also called strictly-future, or strictly-upper).

### 2.2 The adapted convex program

Let $J : H \to \mathbb{R} \cup \{+\infty\}$ be proper, lower-semicontinuous,
convex, and differentiable on its interior. The **adapted convex program**
is

$$\boxed{\quad u^\star = \arg\min_{u \in H^{\mathrm{ad}}} J(u). \quad} \tag{P}$$

Because $H^{\mathrm{ad}}$ is a closed subspace, the constraint is linear,
and the first-order optimality condition is

$$\boxed{\quad \nabla J(u^\star) \in H^{\mathrm{ad},\perp}, \quad u^\star \in H^{\mathrm{ad}}. \quad} \tag{FOC}$$

Equivalently, $P_+ \nabla J(u^\star) = 0$. In words: **the gradient at
the constrained optimum has no causal component**.

This is the *abstract Wiener–Hopf equation*.

### 2.3 The quadratic case

If $J(u) = \frac{1}{2}\langle u, Ku\rangle - \langle b, u\rangle$ with
$K$ self-adjoint and positive definite, then $\nabla J(u) = Ku - b$ and
(FOC) reads

$$P_+ (Ku^\star - b) = 0, \quad P_+ u^\star = u^\star.$$

If $K$ already respected the nest (i.e., $K \in \mathcal{T}(\mathcal{N})$
and self-adjoint $\Rightarrow$ $K$ diagonal), the FOC would trivially
give $u^\star = K^{-1}P_+ b$ — done. The interesting case is when $K$
*does not* respect the nest: it mixes past and future, the unconstrained
solution $K^{-1}b$ is non-adapted, and we need to do work.

The work is **nest factorization**: find $A \in \mathcal{T}(\mathcal{N})$
(adapted, lower-triangular, causal) such that $K = AA^*$. Then write
$\widetilde u = A^* u$, $\widetilde b = A^{-1} b$. The cost becomes

$$J(u) = \frac{1}{2}\|\widetilde u\|^2 - \langle \widetilde b, \widetilde u\rangle,$$

a free quadratic in $\widetilde u$. The adapted constraint on $u$ translates
to *some* constraint on $\widetilde u$; if $A$ has an adapted inverse —
i.e., $A^{-1} \in \mathcal{T}(\mathcal{N})$, which holds iff $A$ is
**outer** — then $\widetilde u = A^* u$ is adapted in $H^{\mathrm{ad},*}$
(upper-triangular). The whitened problem is a *prediction* problem:
project $\widetilde b$ onto the upper-triangular subspace.

Explicitly, the optimal $u^\star$ is

$$\boxed{\quad u^\star = A^{-*} P_- (A^{-1} b), \quad} \tag{$\star$}$$

where $P_- = I - P_+$ projects onto the upper-triangular (anticausal)
subspace and the operations are read right-to-left. In the stationary
shift-invariant case this is exactly the Wiener–Hopf solution; in the
finite-dimensional case it is Cholesky-then-back-substitute; in the
Kalman case it is innovations-then-causal-regression. Equation ($\star$)
is the **adapted normal equation**.

### 2.4 What goes wrong without the nest

If we drop adaptedness, $u^\star_{\mathrm{unc}} = K^{-1} b$. The Bayesian/
non-causal smoother, the unconstrained least-squares estimator, the
clairvoyant ("look-ahead") trading rule. Each is the gradient zero of $J$.
The nest constraint is what introduces the **information geometry** of
time. The factorization $K = AA^*$ is the operator that turns the
non-causal smoother into the causal filter; it is literally the
information-flow structure.

---

## 3. Three Instances

### 3.1 Wiener–Hopf prediction

- $H = L^2(\mathbb{R})$ (or $\ell^2(\mathbb{Z})$).
- Nest: $H_t = L^2((-\infty, t])$, projections $P_t$ are the
  causal-truncation operators.
- $J(u) = \frac{1}{2}\langle u, Su\rangle - \langle b, u\rangle$, where
  $S$ is multiplication by the spectral density in the Fourier domain
  (so a self-adjoint, positive convolution operator in the time domain).
- Adapted = causal: $u \in H^+$ (Hardy space of the upper half-plane).

The factorization $S = S_+ \overline{S_+}$ with $S_+$ outer is exactly
Kolmogorov–Szegő. The adapted normal equation gives

$$u^\star = S_+^{-1}\bigl[\overline{S_+}^{-1} b\bigr]_+,$$

with $[\cdot]_+$ the causal projection. This is the classical
Wiener–Hopf formula [Wiener–Hopf 1931, Kolmogorov 1939, Szegő 1939].

**Convex content**: minimum mean-squared error in the causal class.
**Nest content**: $S_+$ lives in the nest algebra
$\mathcal{T}(L^2_{\le t})$ (multiplication by an $H^\infty$ outer function
is causal).
**Solution preserves the nest** because $S_+^{-1}$ is also outer
(Beurling–Lax–Halmos invariant-subspace theorem ensures the existence
of such a factor when $\log S \in L^1$).

### 3.2 Kalman filter

- $H = L^2(\Omega, \mathcal{F}, \mathbb{P}; \mathbb{R}^n)$ with the
  observation filtration $\mathcal{F}_t^Y$.
- Nest: $H_t = L^2(\Omega, \mathcal{F}_t^Y, \mathbb{P})$, projections
  $P_t = \mathbb{E}[\cdot \mid \mathcal{F}_t^Y]$.
- $J(\hat X) = \mathbb{E}\|X - \hat X\|^2$, convex (quadratic in $\hat X$).
- Adapted = $\hat X_t$ measurable w.r.t. $\mathcal{F}_t^Y$.

The covariance operator of the observation process $Y$ on $L^2$ plays the
role of $K$. The **innovations representation** $\nu_t = Y_t - \mathbb{E}[
Y_t \mid \mathcal{F}_{t-1}^Y]$ is exactly the Cholesky factorization
$K = LL^*$ with $L$ lower-triangular adapted; equivalently, the
Gram–Schmidt orthogonalization of the observation history with respect
to the filtration [Kailath 1968, Frazho–Foias 1980s].

The Kalman recursion is then the explicit formula ($\star$) restricted to
linear-Gaussian state-space models, where the lower-triangular factor
admits a finite-state Riccati recursion. The Riccati equation is *exactly*
the propagation of the inverse-covariance block of $L$.

**Solution preserves the nest**: $\hat X_t \in \mathcal{F}_t^Y$ by
construction, because the Cholesky factor and its inverse live in the
nest algebra (both lower-triangular).

### 3.3 Optimal trading with transient impact

- $H = \ell^2(\mathbb{Z})$ in the stationary case, or
  $L^2(\Omega, \mathcal{F}, \mathbb{P})$ with the public-information
  filtration $\mathcal{F}_t$ in the stochastic-signal case.
- Nest: $\mathcal{F}_t = $ history of the signal and trade flow up to $t$.
- $J(x) = \frac{1}{2}\langle x, Kx\rangle - \langle f, x\rangle$, with
  $K$ the symmetrized impact kernel (positive definite under
  no-dynamic-arbitrage, see [Gat10]) and $f$ the signal.
- Adapted = causal trading rule.

The Wiener–Hopf factorization $K = K_+ K_-$ exists when $K$ has finite
"trace" / log-integrable spectrum. The adapted normal equation gives the
causal rule

$$x^\star_t = K_-^{-1} \bigl[K_+^{-1} f\bigr]_+,$$

with the explicit $\rho^m$ scalar collapse in the AR(1) × exponential
case and the fractional-derivative form in the power-law case (see the
companion draft `papers/noisy-signal-impact-trading.md`, §5–6, for the
calculation).

**Solution preserves the nest**: $x^\star$ is adapted because
$K_-^{-1}$ acts causally on a quantity that has already been causally
projected. In the noisy-signal extension, the optimal rule is the
composition *Wiener pre-filter ∘ adapted impact rule* — a separation of
estimation and control that is precisely the LQG separation principle
re-read as composition of two nest-preserving operations.

### 3.4 Dictionary

**Table 1.** A side-by-side dictionary of adapted convex duality.

| Abstract object        | Wiener–Hopf prediction      | Kalman filter                    | Optimal trading                  |
|------------------------|------------------------------|-----------------------------------|-----------------------------------|
| Hilbert space $H$      | $L^2(\mathbb{R})$            | $L^2(\Omega, \mathcal{F}, \mathbb{P})$ | $\ell^2(\mathbb{Z})$ / process $L^2$ |
| Nest $\{H_t\}$         | Past $L^2_{\le t}$           | $L^2(\mathcal{F}_t^Y)$            | $L^2(\mathcal{F}_t)$              |
| Convex $J$             | $\tfrac12\|y - u\|^2_S$      | $\mathbb{E}\|X - \hat X\|^2$      | $\tfrac12\langle x,Kx\rangle - \langle f,x\rangle$ |
| Hessian $K$            | Spectral density $S$         | Observation covariance            | Impact kernel                     |
| Factorization $K=AA^*$ | Kolmogorov–Szegő $S=|S_+|^2$ | Cholesky / innovations $LL^*$     | Wiener–Hopf $K_+ K_-$             |
| Outer / lower factor   | $S_+$                        | $L$                               | $K_+$                             |
| Solution ($\star$)     | Causal Wiener filter         | Kalman gain × innovation          | Causal trading rule               |
| Anticausal complement  | Strictly-future $L^2$        | $\mathcal{F}^Y_\infty \ominus \mathcal{F}_t^Y$ | Strictly-future trades       |
| FOC                    | $[Su^\star - b]_+ = 0$       | $\mathbb{E}[X - \hat X \mid \mathcal{F}_t^Y]=0$ | $[Kx^\star - f]_+ = 0$    |
| Separation principle   | Whitening + best predictor   | Estimator + LQR feedback          | Wiener prefilter + impact rule    |

The conceptual punchline: the same three lines (Hilbert space, nest,
convex $J$) span three different problem classes. The "solve" step is
the same in each: factor the Hessian inside the nest algebra; apply
($\star$).

---

## 4. The Factorization Theorem

### 4.1 Statement (informal)

Let $H$ be a Hilbert space with complete nest $\mathcal{N}$, and let
$K : H \to H$ be a self-adjoint positive operator. Then under regularity
conditions (e.g., $K$ is a bounded perturbation of identity, or $\log K$
is suitably integrable in the spectral case), there exists an outer factor
$A \in \mathcal{T}(\mathcal{N})$ with bounded inverse $A^{-1} \in
\mathcal{T}(\mathcal{N})$ such that $K = AA^*$.

Three specializations:

- **Cholesky** (finite-dimensional, $\mathcal{N}$ the standard flag):
  always exists for $K > 0$.
- **Wiener–Hopf** (shift-invariant, stationary): exists iff
  $\int \log S(\omega)\, d\omega > -\infty$ (Szegő's condition).
- **Arveson–Larson outer factorization** (general nest algebras): exists
  under positive-definiteness and a log-integrability/regularity
  condition, with explicit constructions via Riesz–Herglotz / Wold–type
  decompositions [Arveson 1975, Pitts 1988, Davidson 1988].

### 4.2 Why this is the engine

Given factorization $K = AA^*$ inside the nest, the adapted FOC
$P_+(Ku - b) = 0$ becomes

$$P_+(AA^* u - b) = 0 \;\Longleftrightarrow\; A P_+(A^* u - A^{-1} b) = 0$$

(using that $A \in \mathcal{T}(\mathcal{N})$ commutes with $P_+$ on the
range, *modulo a careful statement* — strictly: $A$ maps adapted to
adapted, and the truncation respects the algebra). Therefore

$$P_+(A^* u - A^{-1} b) = 0,$$

i.e., $A^* u^\star = P_+ (A^{-1} b)$, giving ($\star$):

$$u^\star = A^{-*} P_+(A^{-1} b).$$

The whole "art" is finding $A$. In the three canonical problems, $A$ is
respectively: the outer spectral factor (WH), the Cholesky factor with
adapted entries (Kalman, via Riccati), and the causal kernel factor
(trading).

### 4.3 What the dual problem looks like

Lagrangian relaxation of (P) with multiplier $\mu \in H^{\mathrm{ad},\perp}$
(the anticausal complement) gives

$$\mathcal{L}(u, \mu) = J(u) - \langle \mu, u\rangle$$

with unconstrained primal optimum $u(\mu) = (\nabla J)^{-1}(\mu)$. In the
quadratic case, $u(\mu) = K^{-1}(b + \mu)$. The dual problem is

$$\max_{\mu \in H^{\mathrm{ad},\perp}} -J^*(\mu + b) + \text{const},$$

with $J^*$ the Legendre–Fenchel conjugate. The dual optimum
$\mu^\star$ is the *anticausal component of the unconstrained gradient*:
$\mu^\star = -P_- (Kx^\star_{\mathrm{unc}} - b)$. This is what is
"thrown away" by causality — the value of the look-ahead information the
adapted policy cannot use.

In the trading instance, $\mu^\star$ is the cost (in PnL units) of not
seeing the future signal — a quantitative *value of clairvoyance*.

---

## 5. What Survives, What Deforms, What Breaks

### 5.1 What survives the skeleton

These extensions stay inside adapted convex duality:

- **Matrix Wiener–Hopf / multi-asset trading.** $H = \ell^2(\mathbb{Z};
  \mathbb{R}^n)$, $K$ matrix-valued positive convolution. Factorization
  becomes matrix WH ([Gohberg–Krein 1958]; for trading,
  [Abi Jaber–Neuman–Tuschmann 2024]).
- **LQG control with partial observation.** $J = $ control cost,
  nest = observation filtration. The separation principle is the
  composition of two nest-preserving operations: Kalman filter
  (estimation, $\hat X_t$ adapted to $\mathcal{F}_t^Y$) and LQR
  feedback (control, $u_t = -L_t \hat X_t$ adapted). This is the
  paradigmatic example of nest-preserving composition.
- **Gârleanu–Pedersen** [GP13]. Quadratic transaction cost +
  OU return predictor + risk-aversion. The "aim portfolio" is the
  unconstrained minimizer; the "trading rate" is the adapted projection.
- **Causal optimal transport / adapted Wasserstein** [Backhoff–Pammer–
  Schachermayer]. Convex (Kantorovich) functional + nest constraint
  (couplings preserving the filtration). Same skeleton, different convex
  $J$.

### 5.2 What deforms

These keep the skeleton but lose a clean factorization:

- **Rough volatility / fBm signals** (Hurst $H \neq 1/2$). The spectral
  density behaves like $|\omega|^{1-2H}$; the Szegő condition still
  holds for $H \in (0,1)$, so a WH factor exists, but it is no longer
  rational — it is a fractional power. The causal solution becomes a
  *fractional* derivative/integral. The nest is preserved, but the
  nest-algebra factor is now an unbounded operator with a non-polynomial
  symbol. (See [Forde–Sánchez-Betancourt et al.], [Muhle-Karbe–
  Rosenbaum 2026, arXiv:2601.23172].)
- **Volterra propagator kernels** [Abi Jaber–Neuman 2022,
  arXiv:2211.00447]. Non-stationary, non-shift-invariant $K$. The
  factorization is no longer Fourier-diagonal; one uses operator-valued
  Riccati or Fredholm resolvents. Still adapted convex duality, but the
  factorization theorem is constructive in a Banach-algebra sense, not
  the explicit Szegő formula.
- **Hidden-Markov / regime-switching signals.** The signal $f_t$ is not
  $\mathcal{F}_t$-measurable; one first projects onto the observation
  filtration (a Wonham/HMM filter) and then applies the adapted control.
  Same skeleton, with the nest being the observation filtration rather
  than the full signal filtration.

### 5.3 What breaks

The skeleton genuinely fails in:

- **Non-quadratic, non-convex $J$.** Without convexity, the FOC
  $P_+ \nabla J(u^\star) = 0$ is no longer sufficient; one needs
  variational inequalities and proximal methods, and no general nest
  factorization exists.
- **Non-Gaussian filtering.** The Kalman/innovations skeleton uses
  *linear* projection; for non-Gaussian models, the conditional
  expectation is no longer linear, and the Cholesky factor of the
  covariance is not the right object. Particle filters live outside
  this framework.
- **Mean-field / equilibrium crowding.** Adding strategic interaction
  between traders couples the convex programs across agents (MFG /
  $N$-player games). The fixed-point equation no longer reduces to a
  single nest-respecting factorization; it is a *system* of coupled
  adapted programs. (See [Cardaliaguet–Lehalle 2017], MFG of optimal
  execution.)
- **Adapted optimization with a non-convex feasible set.** Inventory
  constraints (no shorting, position caps) make the feasible set a
  convex cone *strictly smaller* than $H^{\mathrm{ad}}$; the FOC
  becomes a complementarity condition; closed-form WH is lost.

---

## 6. Conjectures and Open Questions

1. **Adapted proximal duality.** For non-quadratic convex $J$, is there
   a "proximal Wiener–Hopf" — a recursive computation of $u^\star =
   \mathrm{prox}^{\mathrm{ad}}_J(b)$ analogous to Cholesky for the
   quadratic case? Conjecture: yes, via a *splitting* algorithm
   alternating gradient steps in $H$ with causal projection $P_+$,
   convergent under standard convexity + smoothness conditions. This
   would give a unified Forward–Backward style algorithm for adapted
   convex problems, generalizing the explicit WH formula. [tentative]

2. **Information-theoretic FOC.** The anticausal multiplier $\mu^\star$
   measures "wasted look-ahead." Is there a precise identity linking
   $\|\mu^\star\|^2$ to a mutual-information quantity
   $I(u^\star_{\mathrm{unc}}; \text{future} \mid \mathcal{F}_t)$? In
   the Gaussian-quadratic case the answer is yes (it is the
   predictive-information / excess-entropy rate of the signal–trade
   joint process); in the general convex case this is the right
   conjecture. [tentative]

3. **When does separation hold?** The LQG-style separation of estimation
   and control is exact when (i) $J$ is quadratic, (ii) noise is
   Gaussian, (iii) the nest is the observation filtration. Outside this,
   separation generically fails (dual control, Bar-Shalom–Tse). Is there
   a *convex-only* version of separation, with bounds on its suboptimality
   in terms of how far $J$ is from quadratic? [tentative]

4. **Nest algebras for path-dependent volatility.** Path-dependent
   volatility models (Guyon–Lekeufack 2023, hypertraded volatility)
   produce a non-Markovian, history-dependent Hessian. Does the
   resulting $K$ admit a *finite-memory* nest factorization, or is the
   factorization always infinite-dimensional? This is the operator-
   theoretic version of the Markovian-lift question. [tentative]

5. **Adapted convex duality as a programming abstraction.** Could one
   build a small DSL where the user specifies $(H, \mathcal{N}, J)$ and
   the compiler produces the appropriate factorization-based solver?
   The three instances above would be three back-ends (Szegő, Cholesky,
   Wiener–Hopf), and the DSL would handle composition (Wiener prefilter
   + trading rule, Kalman + LQR).

---

## 7. Discussion

The unifying view has three consequences worth restating plainly:

1. **The Riccati equation, Wiener–Hopf factorization, and Cholesky
   decomposition are the same operation** — outer factorization of a
   positive operator inside a nest algebra. The Riccati equation is the
   finite-state-space recursion for the Cholesky factor of the
   covariance of a linear-Gaussian process; the Wiener–Hopf factorization
   is the stationary shift-invariant analogue; Cholesky is the
   finite-dimensional case. (See the companion note
   `outputs/wiener-hopf-riccati-connection.md`.)

2. **The separation principle is the statement that the composition of
   two nest-preserving operators is nest-preserving.** LQG separation
   (estimator + controller), the noisy-signal trading separation
   (Wiener prefilter + impact rule), and the prediction–smoothing
   decomposition are all instances. The genuine content is that the
   *optimum* over adapted policies factors as a composition over
   adapted policies — which is true exactly when the optimization is
   convex-quadratic-Gaussian.

3. **The hard part of any new problem of this form is the factorization,
   not the optimization.** Once the Hessian is factored inside the
   nest, the solution is mechanical (back-substitution). Therefore
   research in this family translates to research on factorization
   theorems for new classes of operators: rough-vol kernels (fractional
   Szegő), Volterra propagators (operator-valued Riccati), matrix /
   multi-asset cases (matrix WH), regime-switching (Wonham filter +
   adapted recursion). Each "new model" in the field is, structurally,
   a new factorization problem.

This reading suggests that progress in optimal trading, optimal control,
optimal filtering, and even adapted optimal transport is bottlenecked by
*operator factorization theory*, not by stochastic analysis. A practical
upshot: when a new impact / signal / risk model is proposed, the first
question to ask is "does the Hessian admit a nest factorization, and is
the factor explicit?" — that determines whether the model is solvable.

---

## 8. Limitations

- **The framework is convex-quadratic-centric.** The cleanest examples
  are quadratic; non-quadratic convex $J$ are sketched but not worked
  out (see §6.1).
- **The nest is assumed totally ordered.** Partial orders (multi-agent
  information, asymmetric information) require *commutative subspace
  lattices* (CSL algebras), a generalization of nest algebras
  [Arveson 1974, Davidson 1988]. We have not treated this.
- **Continuous-time technicalities.** The factorization theorems are
  stated under regularity (boundedness, log-integrability). For
  unbounded operators (e.g., differential operators in continuous-time
  LQG), the abstract statements need care; the explicit results all
  hold in the appropriate domain.
- **No new theorems.** This is a position paper. Every concrete
  factorization or optimum statement is in the cited literature. The
  contribution is the dictionary and the framing.

---

## Sources

- Arveson, W. — *Interpolation problems in nest algebras*. J. Funct.
  Anal. **20** (1975), 208–233. [DOI](https://doi.org/10.1016/0022-1236(75)90041-5).
  The original nest-algebra factorization paper.
- Davidson, K. R. — *Nest Algebras*. Pitman Research Notes in Math.
  191, Longman, 1988. Standard reference for the operator-algebraic
  framework used in §2 and §4.
- Kolmogorov, A. N. — *Stationary sequences in Hilbert space*. Bull.
  Moscow State Univ. **2** (1941). Original prediction theorem.
- Szegő, G. — *Über die Randwerte einer analytischen Funktion*. Math.
  Ann. **84** (1921), 232–244. Original spectral factorization.
- Wiener, N. & Hopf, E. — *Über eine Klasse singulärer Integralgleichungen*.
  Sitz. Preuss. Akad. Wiss. Berlin (1931). Original WH equation.
- Kalman, R. E. — *A new approach to linear filtering and prediction
  problems*. Trans. ASME J. Basic Eng. **82** (1960), 35–45.
- Kailath, T. — *An innovations approach to least-squares estimation,
  part I*. IEEE Trans. Aut. Control **13** (1968), 646–655. Innovations
  = Cholesky.
- Gohberg, I. & Krein, M. — *Systems of integral equations on a half line
  with kernels depending on the difference of arguments*. AMS Transl.
  **14** (1960), 217–287. Matrix WH.
- Gârleanu, N. & Pedersen, L. H. — *Dynamic trading with predictable
  returns and transaction costs*. J. Finance **68** (2013), 2309–2340.
  [PDF](https://docs.lhpedersen.com/DynamicTrading.pdf).
- Gatheral, J. — *No-dynamic-arbitrage and market impact*. Quant. Finance
  **10** (2010), 749–759. PD condition on $K$.
- Bouchaud, J.-P., Gefen, Y., Potters, M. & Wyart, M. — *Fluctuations
  and response in financial markets: the subtle nature of "random" price
  changes*. Quant. Finance **4** (2004), 176–190.
  [arXiv:cond-mat/0307332](https://arxiv.org/abs/cond-mat/0307332).
- Lehalle, C.-A. & Neuman, E. — *Incorporating signals into optimal
  trading*. Finance & Stochastics **23** (2019), 275–311.
  [arXiv:1704.00847](https://arxiv.org/abs/1704.00847).
- Abi Jaber, E. & Neuman, E. — *Optimal liquidation with signals: the
  general propagator case*. (2022).
  [arXiv:2211.00447](https://arxiv.org/abs/2211.00447).
- Abi Jaber, E., Neuman, E. & Tuschmann, M. — *Optimal portfolio choice
  with cross-impact propagators*. (2024).
  [arXiv:2403.10273](https://arxiv.org/abs/2403.10273).
- Forde, M., Sánchez-Betancourt, L. et al. — *Optimal trade execution
  for Gaussian signals with power-law resilience*.
  [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26).
- Muhle-Karbe, J., Rosenbaum, M. et al. — *Unified theory of rough
  volatility and power-law impact*. (2026).
  [arXiv:2601.23172](https://arxiv.org/abs/2601.23172).
- Backhoff, J., Beiglböck, M., Lin, Y. & Zalashko, A. — *Causal
  transport in discrete time and applications*. SIAM J. Optim. **27**
  (2017), 2528–2562. Adapted optimal transport.
- Cardaliaguet, P. & Lehalle, C.-A. — *Mean field game of controls and
  an application to trade crowding*. Math. Financial Econ. **12** (2018),
  335–363.

## Cross-references in this workspace

- `papers/noisy-signal-impact-trading.md` — the explicit calculations for
  the optimal-trading instance (§3.3 here).
- `outputs/wiener-hopf-riccati-connection.md` — the equivalence between
  WH spectral factorization and the Riccati equation as Cholesky-in-the-
  nest.
- `outputs/trading-duality-extensions.md` — companion note on extensions
  (LQG separation, MFG, matrix WH, rate–distortion).
