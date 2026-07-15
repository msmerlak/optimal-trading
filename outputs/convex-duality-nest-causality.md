# Convex Duality Inside a Nest as the General Structure of Causality

*A literature review.*

> **Status.** Literature review / position paper. The framework discussed
> is folklore in operator algebra (Arveson, Davidson) and implicit in
> each application area, but **no published paper or survey (2010–2026)
> proposes nest algebras and "adapted convex duality" as a single
> unifying skeleton across prediction, filtering, control, transport,
> information theory, and finance**. This review collects the
> ingredients and the bridges, and explicitly marks the unifying
> reading as the reviewer's framing rather than a stated programme.

---

## 1. Thesis

Causality, in problems of prediction, filtering, stochastic control,
optimal transport, sequential decision-making, and dynamic asset pricing,
admits a single abstract skeleton:

> Minimize a convex functional $J$ on a Hilbert space $H$ subject to the
> constraint that the solution respect a **nest** — a totally ordered
> chain of closed subspaces (or projections, or σ-algebras), typically
> the past up to each time $t$.

The constructive machinery is **factorization inside the nest algebra**
— the operator-theoretic generalization of Cholesky decomposition,
spectral (Szegő) factorization, and Wiener–Hopf factorization — pioneered
by Ringrose [Rin65], Arveson [Arv75], and Davidson [Dav88], and extended
by Power, Anoussis–Katsoulis [AK98], Paulsen–Woerdeman, and others.

Seven literatures speak this skeleton in their own dialects:

1. **Operator algebra**: nest algebras, distance formulae, outer
   factorization.
2. **Prediction theory**: Wiener–Hopf equations, Kolmogorov–Szegő
   spectral factorization, Wold decomposition.
3. **Linear estimation**: Kalman filtering, innovations representations
   as Cholesky/triangular factorizations.
4. **Optimal trading with transient impact**: Bouchaud–Gatheral
   propagator models, Lehalle–Neuman, Abi Jaber–Neuman, stated as
   adapted convex programs whose FOCs are stochastic Fredholm
   equations.
5. **Adapted / causal optimal transport**: Lassalle, Backhoff et al.,
   bicausal couplings and adapted Wasserstein, with explicit
   Kantorovich-type duality restricted to filtration-respecting plans.
6. **Causal information theory**: directed information, causal
   rate–distortion, LQG with directed-information constraints, posed
   as convex programs over causally conditioned kernels.
7. **Mathematical finance via the martingale method**: Karatzas–
   Lehoczky–Shreve–Xu, Kramkov–Schachermayer convex duality between
   adapted wealth processes and equivalent local martingale measures.

The terminology "nest" appears almost exclusively in cluster 1. Each
other cluster uses "filtration", "progressive measurability", "adapted",
or "causally conditioned"; the underlying object is the same.

---

## 2. The Abstract Skeleton

### 2.1 Nest, nest algebra, adapted subspace

Let $H$ be a (real or complex) Hilbert space. A **nest** $\mathcal{N}$ is a
totally ordered family of closed subspaces of $H$, closed under
arbitrary intersections and closed linear spans, containing $\{0\}$ and
$H$ [Rin65, Dav88 §1]. Each $N \in \mathcal{N}$ has an orthogonal
projection $P_N$; the family $\{P_N : N \in \mathcal{N}\}$ is an
increasing family of projections — the abstract analogue of a
filtration.

The **nest algebra** is
$$
\operatorname{alg}\mathcal{N} = \{T \in \mathcal{B}(H) : T N \subseteq N \text{ for all } N \in \mathcal{N}\},
$$
the (weakly closed) algebra of bounded operators that leave every element
of the nest invariant [Arv75, p. 209]. In the finite-dimensional case
with the standard flag, $\operatorname{alg}\mathcal{N}$ is the algebra of
lower-triangular matrices; in the $\ell^2(\mathbb{Z}_+)$ case with the
chain of "first $n$ coordinates", it is the algebra of lower-triangular
infinite matrices; in $L^2(\mathbb{R})$ with $\mathcal{N} =
\{L^2(-\infty, t]\}_t$, it is the algebra of causal (Volterra-type)
convolution operators.

The **adapted subspace** of $H$ relative to $\mathcal{N}$, denoted
$H^{\mathrm{ad}}$, is the set of elements of $H$ compatible with the
nest. In the operator-process correspondence — where an element
$u \in H$ is identified with the multiplication or convolution operator
$M_u$ — adaptedness means $M_u \in \operatorname{alg}\mathcal{N}$.

### 2.2 The convex program

Let $J : H \to \mathbb{R}\cup\{+\infty\}$ be proper, convex, lower
semicontinuous, with subdifferential $\partial J$. The **adapted convex
program** is
$$
u^\star = \arg\min_{u \in H^{\mathrm{ad}}} J(u). \tag{P}
$$
Because $H^{\mathrm{ad}}$ is a closed linear subspace, the first-order
optimality condition is
$$
\partial J(u^\star) \cap (H^{\mathrm{ad}})^\perp \neq \emptyset,
\quad u^\star \in H^{\mathrm{ad}}. \tag{FOC}
$$
In words: at the constrained optimum, the gradient must have **no causal
component** — it lives entirely in the strictly-future complement.

When $J$ is differentiable, $\nabla J(u^\star) \in
(H^{\mathrm{ad}})^\perp$, equivalently $P_+ \nabla J(u^\star) = 0$ where
$P_+$ is the projection onto $H^{\mathrm{ad}}$. We call (FOC) the
**abstract Wiener–Hopf equation**.

### 2.3 The quadratic case and outer factorization

If $J(u) = \tfrac12 \langle u, K u\rangle - \langle b, u\rangle$ with $K
\succ 0$, then (FOC) reads
$$
P_+ (K u^\star - b) = 0, \quad u^\star \in H^{\mathrm{ad}}.
$$
Three subcases of constructive importance:

- **$K \in \operatorname{alg}\mathcal{N}$** (the Hessian respects the
  nest). Then $u^\star = K^{-1} P_+ b$ — done.
- **$K$ does not respect the nest**, but admits an **outer
  factorization inside $\operatorname{alg}\mathcal{N}$**: there exists
  $A \in \operatorname{alg}\mathcal{N}$ with $A^{-1} \in
  \operatorname{alg}\mathcal{N}$ such that $K = A A^*$. Then (FOC)
  decouples and the closed-form solution is
  $$
  u^\star = A^{-*} P_+ (A^{-1} b). \tag{$\star$}
  $$
  This is the **adapted normal equation**.
- **$K \succ 0$ but no outer factor exists**: factorization fails (the
  abstract analogue of $\log S \notin L^1$ in Szegő's theorem). The
  constrained problem may still have a solution but not in closed form.

The existence of the factorization $K = A A^*$ inside the nest algebra
is the central question of operator factorization theory; Anoussis–
Katsoulis prove that for an arbitrary positive operator $A$ on $H$ there
exists $B \in \operatorname{alg}\mathcal{N}$ with $A = B B^*$ iff a
certain log-integrability-type condition holds, and characterize when
$B$ is invertible inside the algebra [AK98, Thm 5]. This is the
operator-theoretic analogue of the Szegő condition.

### 2.4 The dual problem

The Lagrangian relaxation of (P) with multiplier $\mu \in
(H^{\mathrm{ad}})^\perp$ gives
$$
\mathcal{L}(u, \mu) = J(u) - \langle \mu, u\rangle,
$$
and the dual is $\max_{\mu \in (H^{\mathrm{ad}})^\perp} -J^*(b + \mu)$
where $J^*$ is the Legendre–Fenchel conjugate. The optimal multiplier
$\mu^\star$ is the anticausal component of the unconstrained gradient:
$\mu^\star = -P_-(K u^\star_{\mathrm{unc}} - b)$. **In application
terms, $\mu^\star$ measures the value of clairvoyance** — the cost (in
units of $J$) of being forbidden from using strictly future information.

---

## 3. Operator-Algebraic Backbone: Nest Algebras and Outer Factorization

### 3.1 Founding results

The systematic study of nest algebras was initiated by Ringrose [Rin65],
who defined the algebra and identified its Jacobson radical. The
breakthrough giving constructive power to the theory is Arveson's
**distance formula**:
$$
\operatorname{dist}(T, \operatorname{alg}\mathcal{N}) = \sup_{N \in \mathcal{N}} \| P_{N^\perp} T P_N \|,
$$
proved in [Arv75] (Theorem 1.1; the formula is announced informally on
p. 209 and developed in §1 of the paper). The supremum is over the nest of
projections, and the quantity $P_{N^\perp} T P_N$ is the "strictly
upper" piece of $T$ relative to the splitting $H = N \oplus N^\perp$.
The formula reduces interpolation, approximation, and factorization
problems in $\operatorname{alg}\mathcal{N}$ to a sup over a chain of
elementary norms.

Davidson's monograph *Nest Algebras* [Dav88] is the standard reference;
it develops the structure theory, similarity theory, outer factorization,
and the connection to commutative subspace lattices (CSL algebras), which
are the natural generalization to partially ordered information
structures.

### 3.2 Outer factorization in $\operatorname{alg}\mathcal{N}$

Outer factorization in a nest algebra generalizes Cholesky and
Wiener–Hopf factorization. Power proved early outer factorization
results; the definitive characterization is

> **Theorem (Anoussis–Katsoulis 1998 [AK98]).** Let $\mathcal{N}$ be a
> nest of subspaces of a Hilbert space $H$, $\operatorname{alg}\mathcal{N}$
> the corresponding nest algebra, and $A$ a positive operator on $H$.
> Then there exists an operator $B \in \operatorname{alg}\mathcal{N}$
> with $A = BB^*$ if and only if [an explicit log-type integrability
> condition on the diagonal of $A$ relative to the nest] holds.

The factor $B$ is called *outer* when it is invertible inside the algebra
($B^{-1} \in \operatorname{alg}\mathcal{N}$); this is the abstract
analogue of "$S_+$ is an outer function in $H^\infty$" in the stationary
case [Hel64]. Paulsen–Woerdeman [PW16] extend to reverse-Cholesky and
tensor-product nest algebras.

### 3.3 Why this matters for causality

The nest-algebra picture is the precise statement of "operators that
respect causality". A linear operator $T$ on a process space is causal
iff $T \in \operatorname{alg}\mathcal{N}$ for the nest of past subspaces.
A factorization $K = AA^*$ with $A$ causal and invertibly causal is the
mathematical object that turns a *non-causal* quadratic form (the
unconstrained Hessian) into a pair of causal operations (apply $A^{-1}$,
truncate, apply $A^{-*}$). This is what makes the closed-form solution
($\star$) work; it is the operator-theoretic content of every concrete
filter and execution algorithm in the rest of this review.

---

## 4. Prediction Theory: Wiener–Hopf and Kolmogorov–Szegő

### 4.1 Causal projection in the Hilbert space of a stationary process

Let $(X_t)_{t\in\mathbb{Z}}$ be a stationary square-integrable process
on $(\Omega, \mathcal{F}, \mathbb{P})$, and let $H_t =
\overline{\operatorname{span}}\{X_s : s \le t\} \subset L^2(\Omega,
\mathcal{F}, \mathbb{P})$ be the past at time $t$. The chain
$\{H_t\}_{t\in\mathbb{Z}}$ is a nest in $L^2$. The classical
$h$-step-ahead prediction problem,
$$
\hat X_{t+h \mid t} = \arg\min_{Y \in H_t} \mathbb{E}|X_{t+h} - Y|^2,
$$
is an instance of (P) with $J(Y) = \mathbb{E}|X_{t+h} - Y|^2$ (quadratic,
convex) and the adapted subspace $H^{\mathrm{ad}} = H_t$.

### 4.2 The Wiener–Hopf equation as the adapted normal equation

In the stationary frequency-domain setting (spectral density $S(\omega)$
of $X$), the prediction problem reduces to the Wiener–Hopf equation
$$
\int_0^\infty K(t-s)\, h(s)\, ds = r(t), \quad t \ge 0,
$$
whose solution requires the Kolmogorov–Szegő factorization $S = |S_+|^2$
with $S_+$ outer. The recent expository paper by Subba Rao & Yang [SRY21]
makes this exact identification:

> "Let $H_\infty$ and $H_t$ ($t \in \mathbb{Z}$) denote closed subspaces
> of the real Hilbert space $L^2(\Omega, \mathcal{F}, \mathbb{P})$."

— i.e., the nest of past σ-algebras is explicit, and the Wiener–Hopf
equation is derived as the normal equation for projection onto $H_t$.
Helson–Lowdenslager [HL58] established the multivariate analogue, with
condition $\det S(\omega) > 0$ almost everywhere and $\log \det S \in
L^1$. Pourahmadi's text [Pou01] develops the full machinery — Wold
decomposition, outer-spectral factor, Cholesky correspondence — in
Hilbert-space form.

### 4.3 Causal restriction = nest projection

The textbook causal Wiener filter is built by spectral factorization
$S_{xy}/S_{yy}$ followed by causal truncation $[\cdot]_+$. Picinbono &
Bouvet [PB87] state this explicitly:

> "Causality can be presented as a particular reduction of the
> observation space, and the constrained filter can always be obtained
> by projection onto this space."

The "reduction of the observation space" is exactly the projection onto
$H^{\mathrm{ad}}$ in our skeleton.

### 4.4 Fit assessment

**Tight conceptual fit; terminology absent.** Every modern presentation
of prediction theory states the problem as projection onto a chain of
past subspaces and solves it via outer factorization, exactly matching
the abstract skeleton of §2. The word "nest" appears in none of these
sources; the chain is always called a filtration or a sequence of
prediction subspaces.

---

## 5. Linear Estimation: Kalman Filtering and Innovations as Cholesky

### 5.1 Kalman 1960 and Kailath 1968

Kalman's [Kal60] discrete-time linear filter is the closed-form solution
of the quadratic-cost adapted estimation problem
$$
\hat X_t = \arg\min_{\hat X \in L^2(\mathcal{F}_t^Y)} \mathbb{E}\|X_t - \hat X\|^2,
$$
with $\mathcal{F}_t^Y$ the observation filtration. The Riccati equation
is the recursive propagation of the conditional covariance, which —
viewed as an operator on $L^2(\Omega)$ — is the diagonal of a Cholesky
factor of the joint observation covariance.

Kailath's **innovations representation** [Kai68] orthogonalizes the
observation sequence:
$$
\nu_t = Y_t - \mathbb{E}[Y_t \mid \mathcal{F}_{t-1}^Y],
$$
producing a white-noise sequence $(\nu_t)$ such that $\sigma(\nu_1,
\dots, \nu_t) = \sigma(Y_1, \dots, Y_t) = \mathcal{F}_t^Y$. The
transformation $Y \mapsto \nu$ is a *Cholesky factorization of the
observation covariance matrix*; equivalently, an outer factorization of
the covariance operator in the nest algebra of the observation
filtration [Kai68; Kailath–Sayed–Hassibi, *Linear Estimation*, Prentice
Hall 2000, Ch. 7].

### 5.2 Innovations = outer factor in the nest

In our skeleton: $H = L^2(\Omega, \mathcal{F}, \mathbb{P})$, the nest is
$\mathcal{F}^Y_\bullet$, the convex functional is the squared
estimation error, and the unconstrained gradient (the smoother
$\mathbb{E}[X \mid \mathcal{F}^Y_\infty]$) needs to be projected onto
the adapted subspace at each $t$. The innovations representation is
the outer factor $A$ such that the observation covariance $K = A A^*$
with $A$ lower-triangular adapted; the Kalman gain recursion is the
explicit computation of $A^{-*}$ acting on the projected gradient. The
Riccati equation is the *propagation* equation for the diagonal block
of $A$.

### 5.3 Continuous-time and stochastic realization

Frost & Kailath [FK71] extended the innovations approach to continuous
time. Lindquist–Picci's stochastic realization theory frames the
problem as Hardy-space factorization of the spectral density of the
joint process. Both are continuous-time instances of nest-algebra outer
factorization, again without using the term.

### 5.4 Fit assessment

**Very tight fit in substance, zero overlap in terminology.** The
innovations representation is literally a Cholesky factorization
adapted to the observation nest, and the Kalman gain is the
back-substitution step in ($\star$). The connection to Arveson's nest-
algebra outer factorization is geometrically obvious but not made in
the engineering literature.

---

## 6. Optimal Trading with Transient Impact

### 6.1 The propagator model

Bouchaud–Gefen–Potters–Wyart [BGPW04] and Gatheral [Gat10] introduced
the *propagator model*: the mid-price is the cumulative impact of past
trades through a causal kernel $G$, and a trader's expected execution
cost is a quadratic form in the trading rate $x$ with kernel
$K(t-s) = G(|t-s|)$. Gatheral's no-dynamic-arbitrage analysis
characterizes admissible $K$ as positive-definite kernels with specific
power-law decay constraints.

### 6.2 Optimal trading as adapted convex duality

The optimal-trading problem with a signal $f_t$ is
$$
\max_{x \in \mathcal{P}} \mathbb{E}\left[\int_0^T f_t x_t\, dt - \tfrac12 \int_0^T\!\!\int_0^T K(t-s) x_s x_t\, ds\, dt\right],
$$
where $\mathcal{P}$ denotes progressively measurable trading rates —
i.e., the adapted subspace. This is exactly (P) with $J(x) = \tfrac12
\langle x, Kx\rangle - \langle f, x\rangle$.

**Lehalle–Neuman 2019** [LN19] solve this for OU signals and
exponential resilience, deriving the FOC as a stochastic Fredholm
equation of the second kind — geometrically, the projection of
$(Kx - f)$ onto the adapted subspace.

**Abi Jaber–Neuman 2022** [AN22] generalize to arbitrary propagator
kernels. Their published abstract describes the method as an
"infinite dimensional stochastic control approach," characterizing the
value function via a free-boundary $L^2$-valued BSDE coupled with an
*operator-valued Riccati equation*, with explicit solutions for
power-law and other singular impact kernels [AN22, arXiv abstract].
From the perspective of this review, the operator-valued Riccati
equation **is** the propagation of the outer factor of the impact
kernel inside the time-filtration nest — the continuous-time analogue
of the Cholesky/innovations recursion of cluster 3. That identification
is the reviewer's reading, not stated in [AN22] in those words; the
paper's own framing is stochastic control + BSDE + Riccati. The earlier
[LN19] Fredholm-equation FOC is the more direct match to the adapted
normal equation (FOC) of §2.2.

**Abi Jaber–Neuman–Tuschmann 2024** [AJNT24, arXiv:2403.10273] extend to
matrix-valued Volterra propagators (cross-impact), with the explicit
optimal portfolio expressed through operator-valued resolvents — the
multi-asset analogue of the outer factor.

**Gârleanu–Pedersen 2013** [GP13] solve a related but distinct
problem — quadratic instantaneous transaction cost + OU return predictor
— via dynamic programming, producing the "aim and trade" closed form.
Their formulation is convex but stated through HJB, so the adapted-
duality skeleton is implicit only.

### 6.3 Fit assessment

**Tight fit in the Volterra/propagator subliterature.** Abi Jaber–
Neuman and Abi Jaber–Neuman–Tuschmann literally write the problem as
$\min_{u \in \mathcal{P}} \langle Gu, u\rangle - \langle \alpha,
u\rangle$ over progressively measurable strategies and identify the FOC
as the adapted projection of $(Gu - \alpha)$. The "gradient lies in the
strictly-future complement" framing is the geometric reading of the
Fredholm equation; it is not written in those exact words in [AN22],
but it is the substance of their Theorem on optimality.

A companion document `papers/noisy-signal-impact-trading.md` carries
out the stationary scalar case explicitly, with Wiener–Hopf
factorization of $K$ producing closed-form policies for AR(1) ×
exponential and power-law cases.

---

## 7. Adapted / Causal Optimal Transport

### 7.1 Bicausal couplings as a nest constraint

Standard optimal transport minimizes a convex Kantorovich functional
over couplings $\pi(dx, dy)$ of two marginals $\mu, \nu$. Adapted
optimal transport (also called causal or bicausal transport) adds the
constraint that the coupling respect the filtrations on each side: for
each $t$, given the past of $X$ up to $t$, the conditional law of $Y_t$
depends only on $Y$'s past up to $t$, and symmetrically.

**Lassalle 2018** [Las18] introduced "causal transport plans" and
proved a Monge–Kantorovich theorem for them.
**Backhoff–Beiglböck–Lin–Zalashko 2017** [BBLZ17] developed the dynamic
programming principle for causal transport in discrete time.
**Acciaio–Backhoff–Zalashko 2020** [ABZ20, arXiv:1611.02610] linked
causal OT to enlargement-of-filtrations theory and continuous-time
stochastic optimization.
**Backhoff–Bartl–Beiglböck–Eder 2024/2025** [BBBE25, arXiv:2401.11958]
proved **general Kantorovich-type duality and dual attainment for
adapted transport**, the explicit statement of dual variables for the
filtration constraint.

### 7.2 Pflug–Pichler nested distance

The Pflug–Pichler nested distance between filtered processes is the
metric induced by the adapted Wasserstein cost. It motivates much of
the bicausal-OT theory and connects directly to multistage stochastic
optimization.

### 7.3 Fit assessment

**Very tight fit.** Bicausal OT is literally Kantorovich duality on
the closed convex subset of couplings respecting two nests of σ-algebras.
The constraint is filtration adaptedness, the duality is convex, and
the dual variables (in [BBBE25]) are characterized explicitly. This is
arguably the *cleanest non-finance instantiation* of the abstract
skeleton — and the only application area where the adapted-duality
language is used self-consciously.

---

## 8. Causal Information Theory

### 8.1 Directed information and causal rate–distortion

**Massey 1990** [Mas90] introduced directed information,
$$
I(X^n \to Y^n) = \sum_{i=1}^n I(X^i; Y_i \mid Y^{i-1}),
$$
the canonical functional with built-in causal structure (each summand
conditions on the past output, not the future). **Kramer 2003** [Kra03] extended
the framework to general causal channels with feedback.

**Tatikonda–Mitter 2009** [TM09] gave the variational characterization
of feedback capacity as an optimization over causally conditioned input
distributions $p(x^n \| y^{n-1})$ — a convex program on the simplex of
*adapted* (causally conditioned) policies.

### 8.2 LQG with minimum directed information

**Tanaka–Mohajerin Esfahani–Mitter 2018** [TMM18, arXiv:1510.04214]
recast a minimum-information LQG control problem as a semidefinite
program over the Gram matrix of the causal policy. The abstract states:

> "We consider a discrete-time LQG control problem in which Massey's
> directed information from the observed output of the plant to the
> control input is minimized while required control performance is
> attainable."

The SDP is explicitly a convex program over the cone of causal Gram
matrices — block-lower-triangular positive semidefinite matrices, i.e.,
positive matrices in the nest algebra of the time filtration.

### 8.3 Causal RDF on abstract alphabets

**Charalambous–Stavrou–Kourtellaris** [CSK11, CSK12] and Stavrou–
Skoglund–Tanaka [SST20] develop causal rate–distortion theory for
abstract alphabets, with existence and convex-duality arguments over
non-anticipative reproduction kernels. The KKT conditions yield
reverse-water-filling-type solutions analogous to Wiener-filter
spectra.

### 8.4 Fit assessment

**Tight fit.** Causal rate–distortion and minimum-directed-information
LQG are explicit convex programs over the cone of causally conditioned
kernels/policies. The "nest" is the chain of joint past σ-algebras; no
paper uses the word, but the SDP feasibility set in [TMM18] is, by
inspection, the cone of positive elements in the nest algebra of
$\{\mathcal{F}_t\}_t$.

---

## 9. Mathematical Finance: Martingale Duality

### 9.1 The martingale method as adapted convex duality

The Karatzas–Lehoczky–Shreve–Xu [KLSX91] and Kramkov–Schachermayer
[KS99, KS03] martingale-duality approach to utility maximization in
incomplete markets is the most explicitly convex-duality-styled instance
of the skeleton in the finance literature.

The primal problem,
$$
u(x) = \sup_{X \in \mathcal{X}(x)} \mathbb{E}[U(X_T)],
$$
maximizes expected utility over admissible **adapted** wealth processes
$\mathcal{X}(x)$ starting from $x$. The Kramkov–Schachermayer bipolar
theorem identifies the dual cone as the set of equivalent local
martingale densities (or supermartingale deflators) and proves the
duality
$$
v(y) = \inf_{Y \in \mathcal{Y}(y)} \mathbb{E}[V(Y_T)],
\qquad u(x) = \inf_{y > 0}\, [v(y) + xy],
$$
under the asymptotic-elasticity condition.

Czichowsky & Schachermayer [CS15], surveying the duality method in the
transaction-cost setting, write:

> "Cvitanić and Karatzas […] are the first to apply convex duality,
> also called 'the martingale method', to the problem of optimal
> investment and consumption under transaction costs… As dual
> variables Cvitanić and Karatzas use so-called consistent price
> systems."

(In the frictionless setting of [KS99], the dual cone is the set of
equivalent local martingale densities; in the transaction-cost setting
of [CS15] it is the larger cone of consistent price systems.)

### 9.2 The nest interpretation

The primal cone of admissible wealth processes is exactly the cone of
adapted (predictable, in continuous time) processes satisfying a
self-financing constraint and an integrability condition. The dual
variables (martingale densities) are themselves adapted processes, and
the duality pairing
$$
\langle X, Y\rangle = \mathbb{E}[X_T Y_T]
$$
is an inner product on the joint $L^2$ space whose orthogonality
structure is exactly the filtration nest. The Kramkov–Schachermayer
bipolar theorem is then the abstract Fenchel duality (P) ↔ (P*) with
the nest constraint baked into both the primal and dual cones.

### 9.3 Constrained portfolio optimization

Cvitanić–Karatzas [CK92] explicitly extend to constrained adapted
portfolios (no-shorting, position bounds), introducing convex-analysis
machinery (auxiliary unconstrained markets, dual processes) that is
again a Lagrangian relaxation of an adapted convex program.

### 9.4 Fit assessment

**Tight fit.** The primal–dual structure is precisely "minimize convex
functional over adapted processes; dual variables are martingale
measures." The filtration plays the role of the nest, and the bipolar
theorem is the Fenchel duality for the adapted constraint. As in the
other clusters, operator-algebraic language (nest, $\operatorname{alg}
\mathcal{N}$, outer factorization) is absent; the literature speaks of
filtrations, predictable processes, and martingale measures.

---

## 10. Synthesis: What Unifies, What Doesn't

### 10.1 The shared skeleton (recap)

The seven clusters share:

- A Hilbert space (or, in cluster 5 and 9, a more general convex space
  with an inner-product or polarity structure).
- A nest / filtration / chain of σ-algebras / chain of projections.
- A convex functional $J$ (quadratic in clusters 1–6; concave-utility
  or relative-entropy in cluster 9; transport cost in cluster 5;
  directed information in cluster 8).
- An adapted constraint defining a closed convex subset of the ambient
  space.
- A duality structure in which the dual variables live in a complementary
  cone or subspace.
- A constructive solution that requires *factorization respecting the
  nest*: Cholesky (cluster 3), Szegő / Wiener–Hopf (clusters 2, 6),
  outer factor in $\operatorname{alg}\mathcal{N}$ (cluster 1), dual
  Lagrangian / martingale density (clusters 5, 7–9).

### 10.2 What unifies cleanly

The quadratic-Gaussian clusters (2, 3, 6) and the linear-information
clusters (4, 8) admit explicit outer / Cholesky / spectral factorization
inside the nest algebra. In these cases the abstract skeleton has a
constructive solution via ($\star$), and the algorithm reduces to two
nest-preserving operations (apply $A^{-1}$, causally project; apply
$A^{-*}$).

Adapted optimal transport (cluster 5) and martingale duality (cluster 7)
are non-quadratic generalizations: the dual cone is no longer a Hilbert-
space orthogonal complement but a polar cone, and the factorization is
replaced by a more general Fenchel / Kantorovich duality. The skeleton
survives in the sense that the primal program is convex over an adapted
cone and the dual variables live in a polar cone determined by the
nest.

### 10.3 Disagreements and tension points

- **Quadratic vs. general convex.** The closed-form ($\star$) is a
  quadratic phenomenon. For general convex $J$, no nest-respecting
  factorization is known; one must use iterative methods (proximal
  splitting, forward–backward) that respect the nest at each step but
  do not produce a closed form. Whether a "proximal Wiener–Hopf"
  algorithm exists for non-quadratic convex $J$ is open (see §11).
- **Total order vs. partial order.** Nest algebras presuppose a total
  order on the chain of subspaces (the nest is totally ordered). Multi-
  agent / asymmetric-information / multi-filtration problems require
  *commutative subspace lattice (CSL) algebras*, the generalization of
  nest algebras to partial orders [Dav88, ch. 22; Daughtry–Johns].
  Cluster 5 (bicausal OT) already implicitly works with a product of
  two nests, hence two-dimensional CSL structure.
- **Linear vs. nonlinear adaptedness.** The Kalman / innovations
  picture uses linear (Hilbert-space) projection onto the observation
  past. For non-Gaussian filtering, conditional expectation is no
  longer a linear projection and the Cholesky factor of the covariance
  is not the right object. Particle filtering, the Zakai equation, and
  Kushner–Stratonovich live outside the linear-nest-algebra framework.
- **Convex vs. equilibrium.** Mean-field games of optimal execution
  [CL18] couple the adapted convex programs of many agents through a
  fixed-point condition. The single-agent skeleton is intact at the
  best-response level, but the *equilibrium* is no longer a single
  adapted convex program — it is a system.

### 10.4 The taxonomy

**Table 1.** Mapping of each cluster to the abstract skeleton.

| Cluster | $H$ | Nest $\mathcal{N}$ | $J$ | Factorization | Dual variable |
|---------|-----|---------------------|-----|----------------|----------------|
| Operator algebra | abstract $H$ | abstract nest | abstract quadratic | $K=AA^*$ in $\operatorname{alg}\mathcal{N}$ | anticausal complement |
| Prediction | $L^2(\Omega)$ | past $H_t$ | $\|X - \hat X\|^2$ | Szegő $S = \|S_+\|^2$ | strictly-future $L^2$ |
| Kalman / filtering | $L^2(\Omega)$ | observation $\mathcal{F}_t^Y$ | MSE | Cholesky / innovations | smoother residual |
| Optimal trading | progressive $L^2$ | $\mathcal{F}_t$ | $\tfrac12\langle x,Kx\rangle - \langle f,x\rangle$ | Wiener–Hopf $K=K_+K_-$ | value of clairvoyance |
| Adapted OT | couplings | product of two filtrations | Kantorovich cost | (none — non-quadratic) | adapted price function [BBBE25] |
| Causal info theory | causally conditioned $p$ | joint past | directed info | SDP / KKT | Lagrange mult. on $\mathcal{F}_t$ |
| Martingale duality | adapted wealth | $\mathcal{F}_t$ | $-\mathbb{E}[U(X_T)]$ | bipolar duality | martingale density |

### 10.5 Why no one has stated this unifying view

A research-bibliographic search through 2010–2026 (web, alpha CLI,
domain-specific surveys) returned no published paper or monograph that
explicitly proposes nest algebras as a common framework across these
seven clusters. The closest cross-domain bridges are:

- Acciaio–Backhoff–Zalashko 2020 [ABZ20]: causal OT ↔ enlargement of
  filtrations ↔ continuous-time stochastic optimization.
- Tanaka–Esfahani–Mitter 2018 [TMM18]: information theory ↔ LQG via
  convex duality.
- Daughtry & Johns [DJ]: Arveson nests ↔ commutative subspace lattices
  ↔ Wiener–Hopf factorization (MaRDI portal entry; full citation
  details not located in this session).

But no paper crosses operator algebra, prediction theory, optimal
trading, adapted OT, causal information theory, *and* martingale
duality. The unifying programme is a gap.

---

## 11. Open Questions

1. **Adapted proximal duality.** For non-quadratic but convex $J$, is
   there a "proximal Wiener–Hopf" — a constructive algorithm
   $u^\star = \operatorname{prox}^{\mathrm{ad}}_J(b)$ analogous to
   Cholesky for the quadratic case? Forward–backward splitting,
   alternating gradient with causal projection $P_+$, is the candidate.
   This would generalize the explicit Wiener–Hopf formula to the
   non-quadratic convex world (cluster 5: non-Wasserstein-2 OT;
   cluster 9: utility maximization with non-quadratic utilities;
   cluster 8: KL-divergence rate–distortion).
2. **Information-theoretic interpretation of the dual variable.** The
   anticausal multiplier $\mu^\star$ is the "value of clairvoyance"
   (cluster 6) or "shadow price of the filtration constraint" (cluster
   9). Is there a mutual-information identity
   $\|\mu^\star\|^2 \sim I(\text{unconstrained}; \text{future} \mid
   \mathcal{F}_t)$? In the Gaussian-quadratic case this would link the
   anticausal-complement norm to predictive information / excess
   entropy. Tanaka–Mohajerin Esfahani–Mitter [TMM18] establish such a
   link for the LQG-directed-information setting; the general statement
   is open.
3. **When does separation hold?** LQG-style separation of estimation
   and control (cluster 3 + cluster 6) is the composition of two nest-
   preserving operations. Is there a convex-only version of separation
   with quantitative bounds on its suboptimality in terms of how far
   $J$ is from quadratic-Gaussian? Bar-Shalom & Tse's dual control
   results suggest this is hard.
4. **CSL algebras for multi-agent causality.** Mean-field games of
   execution [CL18] and bicausal OT [BBLZ17] both work with multiple
   filtrations. CSL algebras [Dav88, Daughtry–Johns] are the natural
   operator-theoretic framework. Has the connection been exploited
   anywhere?
5. **Nest factorization for rough-volatility / Volterra Hessians.** The
   rough-volatility / fractional-impact kernels of Muhle-Karbe–
   Rosenbaum and Abi Jaber–Neuman produce Hessians that are
   non-rational and non-Markovian. Do they admit outer factorization in
   the nest algebra of the time filtration, and if so, is the factor
   characterized by a finite-state recursion (a "rough Riccati") or
   genuinely infinite-dimensional?
6. **A DSL for adapted convex programs.** The taxonomy of §10.4
   suggests that a small domain-specific language taking $(H,
   \mathcal{N}, J)$ as input and producing the appropriate
   factorization-based solver could unify the implementation of
   Wiener filters, Kalman filters, optimal-trading policies, and bicausal
   OT solvers. The three back-ends would be Szegő, Cholesky, and
   Wiener–Hopf; composition (cluster 3 + cluster 6 = LQG separation)
   would be a language primitive.

---

## 12. Recommended Reading Order

For a researcher entering this territory:

1. Davidson, *Nest Algebras* [Dav88], chapters 1, 2, 9 — the abstract
   framework.
2. Arveson 1975 [Arv75] — distance formula.
3. Anoussis–Katsoulis 1998 [AK98] — when does the outer factor exist.
4. Subba Rao–Yang 2021 [SRY21] — Wiener–Hopf as Hilbert-space projection.
5. Kailath 1968 [Kai68] + Kailath–Sayed–Hassibi Ch. 7 — innovations = Cholesky.
6. Abi Jaber–Neuman 2022 [AN22] — adapted convex duality in optimal trading.
7. Backhoff–Bartl–Beiglböck–Eder 2024/25 [BBBE25] — explicit Kantorovich
   duality for adapted transport.
8. Tanaka–Mohajerin Esfahani–Mitter 2018 [TMM18] — convex-duality LQG
   with directed information.
9. Kramkov–Schachermayer 1999 [KS99] — bipolar duality in math finance.

---

## Sources

### Operator algebra
- [Rin65] Ringrose, J. R. — *On some algebras of operators*. Proc. London Math. Soc. **15** (1965), 61–83. (Exact pagination *unverified* in this session; widely cited as the founding nest-algebra paper.)
- [Arv75] Arveson, W. — *Interpolation problems in nest algebras*. J. Funct. Anal. **20** (1975), 208–233. <https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-arveson/1970s/1975_Interpolation_problems_in_nest_algebras.pdf> / <https://www.sciencedirect.com/science/article/pii/0022123675900415>
- [Dav88] Davidson, K. R. — *Nest Algebras*. Pitman Research Notes in Math. 191, Longman, 1988. <https://www.math.uwaterloo.ca/~krdavids/nestbook.html>
- [AK98] Anoussis, M. & Katsoulis, E. G. — *Factorization in nest algebras*. Trans. AMS **350** (1998), 165–183. <https://www.ams.org/journals/tran/1998-350-01/S0002-9947-98-02057-1/>
- [PW16] Paulsen, V. I. & Woerdeman, H. J. — *Reverse Cholesky factorization and tensor products of nest algebras*. Proc. AMS, arXiv:1704.04323.
- [DJ] Daughtry, J. & Johns, A. — *Arveson nests and operator factorization along commutative subspace lattices* (full reference *unverified*; see <https://portal.mardi4nfdi.de/wiki/Arveson_Nests_and_Operator_Factorization_Along_Commutative_Subspace_Lattices>).

### Prediction theory
- Wiener, N. & Hopf, E. — *Über eine Klasse singulärer Integralgleichungen*. Sitz. Preuss. Akad. Wiss. Berlin (1931).
- Kolmogorov, A. N. — *Stationary sequences in Hilbert space*. Bull. Moscow State Univ. **2** (1941).
- Szegő, G. — *Über die Randwerte einer analytischen Funktion*. Math. Ann. **84** (1921), 232–244.
- [HL58] Helson, H. & Lowdenslager, D. — *Prediction theory and Fourier series in several variables*. Acta Math. **99** (1958).
- [Hel64] Helson, H. — *Lectures on Invariant Subspaces*. Academic Press, 1964.
- [Pou01] Pourahmadi, M. — *Foundations of Time Series Analysis and Prediction Theory*. Wiley, 2001.
- [SRY21] Subba Rao, S. & Yang, J. — *A prediction perspective on the Wiener–Hopf equations*. arXiv:2107.04994. <https://arxiv.org/pdf/2107.04994>
- [PB87] Picinbono, B. & Bouvet, M. — *Constrained Wiener filtering*. IEEE Trans. Inf. Theory **33** (1987), 160–166. doi 10.1109/TIT.1987.105726. HAL: <https://hal.science/hal-01817912/document>

### Kalman / innovations
- [Kal60] Kalman, R. E. — *A new approach to linear filtering and prediction problems*. Trans. ASME J. Basic Eng. **82** (1960), 35–45. doi 10.1115/1.3662552.
- [Kai68] Kailath, T. — *An innovations approach to least-squares estimation, Part I: Linear filtering in additive noise*. IEEE Trans. Aut. Control **13** (1968), 646–655. <https://ieeexplore.ieee.org/document/1099025>
- [FK71] Frost, P. A. & Kailath, T. — *An innovations approach to least-squares estimation, Part III*. IEEE TAC, 1971.

### Optimal trading
- [BGPW04] Bouchaud, J.-P., Gefen, Y., Potters, M. & Wyart, M. — *Fluctuations and response in financial markets*. Quant. Finance **4** (2004), 176–190. arXiv:cond-mat/0307332.
- [Gat10] Gatheral, J. — *No-dynamic-arbitrage and market impact*. Quant. Finance **10** (2010), 749–759. SSRN:1292353.
- [GP13] Gârleanu, N. & Pedersen, L. H. — *Dynamic trading with predictable returns and transaction costs*. J. Finance **68** (2013), 2309–2340. <https://doi.org/10.1111/jofi.12080>
- [LN19] Lehalle, C.-A. & Neuman, E. — *Incorporating signals into optimal trading*. Finance & Stochastics **23** (2019), 275–311. arXiv:1704.00847.
- [AN22] Abi Jaber, E. & Neuman, E. — *Optimal liquidation with signals: the general propagator case*. arXiv:2211.00447; Math. Finance **35** (2025), 841–866.
- [AJNT24] Abi Jaber, E., Neuman, E. & Tuschmann, M. — *Optimal portfolio choice with cross-impact propagators*. arXiv:2403.10273.

### Adapted optimal transport
- [Las18] Lassalle, R. — *Causal transport plans and their Monge–Kantorovich problems*. Stoch. Anal. Appl. **36** (2018), 452–484. <https://hal.science/hal-04683287v1>
- [BBLZ17] Backhoff, J., Beiglböck, M., Lin, Y. & Zalashko, A. — *Causal transport in discrete time and applications*. SIAM J. Optim. **27** (2017), 2528–2562. arXiv:1606.04062.
- [ABZ20] Acciaio, B., Backhoff, J. & Zalashko, A. — *Causal optimal transport and its links to enlargement of filtrations*. Stoch. Proc. Appl. (2020). arXiv:1611.02610.
- [BBBE25] Backhoff, J., Bartl, D., Beiglböck, M. & Eder, M. — *General duality and dual attainment for adapted transport*. Appl. Math. Optim. (2025); arXiv:2401.11958.

### Causal information theory
- [Mas90] Massey, J. L. — *Causality, feedback and directed information*. Proc. ISITA, Waikiki (1990). <https://www.isiweb.ee.ethz.ch/archive/massey_pub/pdf/BI532.pdf>
- [TM09] Tatikonda, S. & Mitter, S. — *The capacity of channels with feedback*. IEEE Trans. Inf. Theory **55** (2009), 323–349. (Volume/pagination *unverified* in this session.)
- [Kra03] Kramer, G. — *Capacity results for the discrete memoryless network*. IEEE Trans. Inf. Theory **49** (2003), 4–7 (and related work); see also Kramer, *Topics in Multi-User Information Theory*, Foundations and Trends in Comm. Inf. Theory **4** (2007). (Exact citation *unverified* in this session.)
- [TMM18] Tanaka, T., Mohajerin Esfahani, P. & Mitter, S. — *LQG control with minimum directed information: semidefinite programming approach*. IEEE TAC **63** (2018), 37–52. arXiv:1510.04214.
- [CSK11] Charalambous, C. D., Stavrou, P. A. & Kourtellaris, C. — *Causal rate distortion function on abstract alphabets*. arXiv:1102.3294, arXiv:1202.0895.
- [SST20] Stavrou, P. A., Skoglund, M. & Tanaka, T. — *Sequential rate–distortion function for control with rate constraints*. arXiv:1906.04217.

### Martingale duality
- [KLSX91] Karatzas, I., Lehoczky, J., Shreve, S. & Xu, G.-L. — *Martingale and duality methods for utility maximization in an incomplete market*. SIAM J. Control Optim. **29** (1991), 702–730. <https://epubs.siam.org/doi/10.1137/0329039>
- [CK92] Cvitanić, J. & Karatzas, I. — *Convex duality in constrained portfolio optimization*. Ann. Appl. Probab. **2** (1992).
- [KS98] Karatzas, I. & Shreve, S. E. — *Methods of Mathematical Finance*. Springer, 1998.
- [KS99] Kramkov, D. & Schachermayer, W. — *The asymptotic elasticity of utility functions and optimal investment in incomplete markets*. Ann. Appl. Probab. **9** (1999), 904–950. <https://projecteuclid.org/journals/annals-of-applied-probability/volume-9/issue-3/The-asymptotic-elasticity-of-utility-functions-and-optimal-investment-in/10.1214/aoap/1029962818.full>
- [KS03] Kramkov, D. & Schachermayer, W. — *Necessary and sufficient conditions in the problem of optimal investment in incomplete semimartingale markets*. Ann. Appl. Probab. **13** (2003), 1504–1516.
- [CS15] Czichowsky, C. & Schachermayer, W. — *Duality theory for portfolio optimisation under transaction costs*. Preprint, 19 August 2015. <https://www.mat.univie.ac.at/~schachermayer/pubs/preprnts/prpr0161.pdf>

### Mean-field games of execution
- [CL18] Cardaliaguet, P. & Lehalle, C.-A. — *Mean field game of controls and an application to trade crowding*. Math. Financial Econ. **12** (2018), 335–363.

### Workspace cross-references
- `papers/noisy-signal-impact-trading.md` — stationary scalar Wiener–Hopf calculation.
- `papers/adapted-convex-duality.md` — position-paper draft of the unifying view.
- `outputs/wiener-hopf-riccati-connection.md` — WH ↔ Riccati equivalence.
- `outputs/trading-duality-extensions.md` — extensions and conjectures.
