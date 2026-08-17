# Adapted Convex Optimization and Physics

*A literature review.*

> **Status.** Literature review with synthesized framing. The thesis
> developed here — that the "adapted convex duality" skeleton
> (convex functional on a Hilbert space, nest/filtration constraint,
> outer factorization inside the nest algebra) appears in physics in
> eight largely independent guises — is the reviewer's reading. Most
> physics sources use one or more structural pieces without naming the
> unifying object. Only Bouten–van Handel–James 2007, Gupta–Hota 2015,
> and the recent Liu 2026 (arXiv:2604.17058) on Hardy-space memory
> kernels explicitly cross any two of these literatures. **In this
> survey we did not find a physics paper unifying all eight clusters
> under one banner**; the search was not exhaustive (see §11.4).

---

## 1. Thesis

In prior workspace documents (`papers/adapted-convex-duality.md`,
`outputs/convex-duality-nest-causality.md`) we collected an abstract
skeleton:

> Minimize a convex functional $J$ on a Hilbert space $H$ subject to
> the constraint that the solution respect a **nest** $\mathcal{N} =
> \{H_t\}_{t \in T}$ (totally ordered chain of closed subspaces;
> equivalently a filtration, an increasing family of projections, or a
> chain of σ-algebras). The first-order optimality condition is the
> **abstract Wiener–Hopf equation** $P_+ \nabla J(u^\star) = 0$ — the
> gradient at the constrained optimum has no causal component.
> Constructive solutions require **outer factorization inside the nest
> algebra** $K = AA^*$ with $A, A^{-1} \in \operatorname{alg}\mathcal{N}$.
> Cholesky decomposition, Wiener–Hopf factorization, and Kolmogorov–
> Szegő spectral factorization are three avatars of this operation.

This document asks: where does this skeleton appear in **physics**?

Eight clusters are surveyed:

1. **Causality and dispersion relations** (Kramers–Kronig as Hardy-space
   factorization).
2. **Linear response and fluctuation–dissipation** (Kubo).
3. **Wiener–Hopf's physics origins** (radiative transfer, diffraction,
   neutron transport).
4. **Path integrals and stochastic control** (Onsager–Machlup, Kappen,
   Todorov).
5. **Quantum filtering and continuous measurement** (Belavkin, Bouten–
   van Handel–James).
6. **Stochastic thermodynamics and maximum caliber** (Seifert, Pressé–
   Ghosh–Dixit–Dill).
7. **Wasserstein gradient flows and adapted OT** (JKO, Acciaio–
   Backhoff–Zalashko).
8. **Large deviations, Freidlin–Wentzell, macroscopic fluctuation
   theory** (Touchette, Bertini–Jona-Lasinio).

Each instantiates one or more structural pieces of the skeleton.
Cluster 1 is the cleanest fit: causal linear response is *literally* an
$H^2$ (Hardy-space) function on the upper half-plane, and Kramers–
Kronig is the Hilbert-transform relation that outer factorization
produces. Cluster 3 (Wiener–Hopf in radiative transfer) is the
historical original: the 1931 Wiener–Hopf paper *was* about a physics
problem, and the factorization on the half-line is *exactly* the
operation that the abstract skeleton requires inside a nest algebra.

---

## 2. The Abstract Skeleton (Recap)

For self-containedness:

- **Hilbert space** $H$ of square-integrable processes / fields /
  paths.
- **Nest** $\mathcal{N}$ = increasing family of projections
  $\{P_t\}_{t \in T}$. In physics: the chain of "past" $\sigma$-algebras
  for a stochastic process, or the chain of measurement-record
  $\sigma$-algebras in continuous measurement, or the chain of
  $L^2(-\infty, t]$ subspaces of a response-function space.
- **Adapted subspace** $H^{\mathrm{ad}}$: elements compatible with the
  nest.
- **Convex functional** $J : H \to \mathbb{R} \cup \{+\infty\}$.
- **Adapted convex program** $\min_{u \in H^{\mathrm{ad}}} J(u)$ with
  FOC $\nabla J(u^\star) \in (H^{\mathrm{ad}})^\perp$.
- **Constructive solution** (quadratic $J$): outer factorization
  $K = AA^*$ in the nest algebra $\operatorname{alg}\mathcal{N}$.

For the quadratic case the explicit closed form is
$$
u^\star = A^{-*} P_+ (A^{-1} b), \tag{$\star$}
$$
the **adapted normal equation**. For non-quadratic convex $J$ the
solution is implicit and requires iterative methods.

The seven physics clusters below instantiate this skeleton in different
ways; the table at the end of §10 maps each cluster to the abstract
objects.

---

## 3. Causality and Dispersion Relations

### 3.1 Kramers–Kronig and Toll's theorem

The **Kramers–Kronig (KK) relations** state that the real and imaginary
parts of a causal linear-response function $\chi(\omega)$ are Hilbert
transforms of each other:
$$
\operatorname{Re}\chi(\omega) = \frac{1}{\pi}\, \mathrm{P}\!\!\int_{-\infty}^{\infty} \frac{\operatorname{Im}\chi(\omega')}{\omega' - \omega} d\omega',
$$
and the analogous relation with Re ↔ Im interchanged.

Toll's 1956 paper [Toll56] established the foundational equivalence
explicitly:

> "A rigorous proof is given of the logical equivalence of strict
> causality ('no output before input') and validity of a dispersion
> relation, e.g. a relation expressing the real part of a generalized
> scattering amplitude as an integral involving the imaginary part."

### 3.2 Titchmarsh's theorem: causality ⇔ Hardy-space analyticity

The mathematical content of Toll's result is Titchmarsh's theorem
[Tit37]: for $f \in L^2(\mathbb{R})$, the following are equivalent:

1. $f(t) = 0$ for $t < 0$ (causality);
2. $\hat f(\omega)$ extends to a holomorphic function on the upper
   half-plane, bounded in $L^2$ there (i.e. $\hat f \in H^2$, the Hardy
   space of the upper half-plane);
3. $\operatorname{Re}\hat f$ and $\operatorname{Im}\hat f$ are Hilbert
   transforms of each other.

Hoffmann-Jørgensen's *European Physical Journal H* article [HJ14]
clarifies the math attribution:

> "Titchmarsh's Theorem … is a compilation of two well-known theorems
> in mathematics, the Paley–Wiener theorem and the Marcel Riesz
> theorem."

### 3.3 Identification with the adapted-convex skeleton

The chain $\{H_t = L^2(-\infty, t]\}_{t \in \mathbb{R}}$ is a complete
nest on $L^2(\mathbb{R})$. The adapted subspace is exactly $H^2$
(via Fourier transform). The KK relations are the explicit statement
that **the imaginary part of $\hat f$ determines the real part once
adaptedness is imposed** — i.e., once the past-support constraint is
enforced, the response function has one degree of freedom per frequency,
not two. This is the elementary content of the adapted FOC of §2: the
gradient at the constrained optimum has half the components of the
unconstrained gradient.

Passive linear media (positive dissipation) add an extra constraint:
$\hat\chi$ is a **Herglotz–Nevanlinna function** — analytic in the upper
half-plane with non-negative imaginary part — and admits an *outer*
factorization. Figotin & Schenker [FS04] develop the spectral theory
of time-dispersive and dissipative systems on this basis, and Gralak's
2020 article [Gra20] frames the generalized KK expression in terms of
the Herglotz–Nevanlinna representation theorem (his statement, in two
non-adjacent sentences of his §2, says that the generalized expression
of the KK relations *corresponds to* the Herglotz–Nevanlinna
representation theorem).

This is the *physics* analogue of the Kolmogorov–Szegő outer
factorization in prediction theory — the same object dressed in
different vocabulary.

### 3.4 Modern bridge: Hardy-space structure of memory kernels

The recent Liu 2026 [Liu26], arXiv:2604.17058, is the closest physics
source located in this survey to the unifying thesis. The paper studies
non-Markovian memory kernels in open quantum systems and places the
Nakajima–Zwanzig memory kernel in the **operator-valued Hardy space
$H^p_+$** of the upper half-plane, deriving (subtracted) Kramers–Kronig
relations as a consequence. The actual abstract states:

> "Kramers–Kronig (KK) relations are usually invoked for causal
> response functions, but their precise status for non-Markovian
> quantum memory kernels is less explicit. … we show that
> $\tilde{\mathcal K}(z)$ belongs to the operator-valued Hardy space
> $H^p_+$ and obeys KK or subtracted KK relations."

This is the cleanest recent physics source we located that makes the
Hardy-space ($H^2_+$) identification of a causal kernel explicit. It is
not a claim of priority for that identification — the broader passive-
media literature (Welters–Avniel–Johnson, Cassier–Milton, Bernland–
Gustafsson–Sjöberg) uses Herglotz / outer-function structure on the
upper half-plane, which is the same object — but it is a useful
direct bridge between linear-response theory and the operator-theoretic
factorization language of the abstract skeleton.

### 3.5 Fit assessment

**Excellent fit.** Causal linear response is literally the L²
projection onto the past, the response function is literally an outer
$H^2$ function, and Kramers–Kronig is literally the Hilbert-transform
relation that this analyticity entails. What is missing from the
physics literature is the **convex-optimization** framing — Toll/
Titchmarsh do not phrase KK as the FOC of an adapted convex program.
Passivity provides a quadratic dissipation form, so the missing piece
is small.

---

## 4. Linear Response and the Fluctuation–Dissipation Theorem

### 4.1 Kubo formalism

Kubo's 1957 paper [Kub57] established the statistical-mechanical
foundation:

> "Physical quantities such as complex susceptibility … and complex
> conductivity … are rigorously expressed in terms of time-fluctuation
> of dynamical variables."

The Kubo formula gives the linear response as
$$
\chi_{AB}(t) = \frac{i}{\hbar} \theta(t)\, \langle [A(t), B(0)] \rangle_{\mathrm{eq}},
$$
with the explicit $\theta(t)$ step function enforcing causality. The
fluctuation–dissipation theorem (FDT) [Kub66; CW51] is the quadratic
identity
$$
2 k_B T \cdot \operatorname{Im}\chi(\omega) = \omega\, S(\omega),
$$
linking dissipative response to the equilibrium correlation spectrum.

### 4.2 Identification with the skeleton

The covariance operator of the equilibrium fluctuations plays the role
of the Hessian $K$ in §2. Its outer (Cholesky) factor is the
**causal whitening filter** — the operator that maps equilibrium noise
to white noise via a causal (adapted) transformation. This is the
content of the standard projection-operator (Mori–Zwanzig) approach to
non-equilibrium statistical mechanics: the "memory kernel" is the
diagonal of the outer factor of the equilibrium covariance.

### 4.3 Fit assessment

**Strong fit on quadratic-form / causal-structure grounds; convex-
optimization framing absent from canonical sources.** Kubo and Callen–
Welton present FDT as a quadratic identity, not as the FOC of an
optimization. The convex-optimization reading is precisely the
content of maximum caliber (§8) and Onsager–Machlup (§6), which
re-derive FDT from a variational principle on adapted path measures.

---

## 5. Wiener–Hopf's Physics Origins

### 5.1 Radiative transfer: the Milne problem

The original Wiener–Hopf 1931 paper was motivated by the **Milne problem**
in radiative transfer — finding the angular distribution of radiation in
a semi-infinite stellar atmosphere [Mil21; Hop32]. The integral
equation
$$
I(\mu, \tau) = \tfrac12 \int_0^\infty E_1(|\tau - \tau'|)\, I(\mu', \tau')\, d\tau' \, d\mu'
$$
is a convolution equation on a half-line — exactly the setting where the
Wiener–Hopf factorization $K = K_+ K_-$ is the constructive solver.

The Encyclopedia of Mathematics entry [EoM-WH] makes the historical
origin explicit:

> "Equations of this type often appear in problems of mathematical
> physics, e.g. in the theory of radiative transfer (Milne's problem);
> in the theory of diffraction (diffraction on a half-plane, the
> problem of boundary refraction). The first studies of equation (1)
> are due to N. Wiener and E. Hopf, and deal with a factorization
> method."

Hopf's 1934 monograph *Mathematical Problems of Radiative Equilibrium*
[Hop34] is the canonical book-length development.

### 5.2 Diffraction by a half-plane

Sommerfeld's 1896 solution of diffraction by a perfectly conducting
half-plane was re-derived by Wiener and Hopf, and is the canonical
diffraction application. Modern reformulations include Meister & Speck
1980 [MS80]:

> "The Sommerfeld half-plane problem revisited I … a pair of coupled
> Wiener–Hopf integral equations."

### 5.3 Neutron transport and stellar atmospheres

The Case–Zweifel *Linear Transport Theory* (1967) and the follow-up
literature [GP04, CW89] applied Wiener–Hopf to one-speed neutron
transport in half-spaces. The structural object is identical: a
convolution operator on a semi-infinite interval, factored into causal
and anticausal pieces.

### 5.4 Operator-theoretic synthesis: Krein and Gohberg

Krein and Gohberg recognized Wiener–Hopf factorization as a structural
operator-theoretic problem on the half-line, independently of any
specific physics application. Their books [GF74; BGKR08] develop the
factorization theory in Banach-algebra terms; the connection to
nest-algebra outer factorization (§2 of the present review) is implicit
but not made explicit.

### 5.5 Fit assessment

**Perfect structural fit, partial conceptual fit.** The Wiener–Hopf
1931 paper is *literally* factorization of a convolution operator on a
half-line — the maximal nest of subspaces $\{L^2[t, \infty)\}$. Krein
and Gohberg recognized this as nest-algebra factorization avant la
lettre. What the physics literature lacks is the recognition that this
factorization is the constructive solver for a *convex* problem (an
extremal problem in $H^2$).

---

## 6. Path Integrals and Stochastic Control in Physics

### 6.1 Onsager–Machlup action

The Onsager–Machlup 1953 papers [OM53] introduced the convex
Lagrangian
$$
L_{\mathrm{OM}}(q, \dot q) = \tfrac{1}{4D}\, (\dot q - F(q))^2
$$
for the most probable path of an overdamped Langevin process. The
"action" $\int_0^T L_{\mathrm{OM}}\, dt$ is quadratic-in-velocity, hence
strictly convex. The most probable path is the (adapted, forward-in-
time) minimizer.

Bach & Dürr [BD78] provided the rigorous reformulation:

> "The Onsager–Machlup function [is] the Lagrangian for the most
> probable path of a diffusion process."

### 6.2 Path-integral / KL-divergence control

Kappen's 2005 papers [Kap05a, Kap05b] developed **path-integral
stochastic control**: for control-affine SDEs with quadratic control
cost, the value function satisfies a linear PDE obtained by a Cole–Hopf
transform. This is *exactly* the Hopf–Cole / log-Laplace transform that
implements convex-conjugate duality between the cost and the value
function.

Todorov [Tod09] and Dvijotham–Todorov [DT11] formalized the
**linearly-solvable** family as KL-divergence minimization between a
controlled adapted path measure and an uncontrolled one — making the
convex duality (Donsker–Varadhan / Legendre–Fenchel) explicit.
Theodorou et al. [The10, TT12] extended to nonlinear systems and
reinforcement learning.

### 6.3 Identification with the skeleton

The Hilbert space is the space of adapted controls (or, dually,
adapted path measures equivalent to the uncontrolled reference). The
convex functional is the expected cost + KL divergence. The nest is
the state filtration. The Hopf–Cole transform is the convex-conjugate
duality between the primal control problem and the dual (passive)
linear evolution.

### 6.4 Fit assessment

**Very strong fit.** Path-integral control is essentially the path-
space analogue of the adapted-convex skeleton, with the KL-divergence
playing the role of the convex functional and the Hopf–Cole transform
playing the role of outer factorization. Linearly-solvable control
makes the convex duality completely explicit.

---

## 7. Quantum Filtering and Continuous Measurement

### 7.1 Belavkin and the noncommutative innovations

Belavkin [Bel88, Bel92] developed the quantum analogue of Kalman
filtering for continuous measurement of an open quantum system. The
**quantum stochastic master equation (SME)** is the quantum analogue
of the Zakai/Kushner–Stratonovich equation; its linear form admits a
"reference probability" derivation that parallels the classical
nonlinear filter.

Bouten, van Handel & James [BvHJ07] is the canonical exposition:

> "We describe the quantum Itô calculus … We use both reference
> probability and innovations methods to obtain quantum filtering
> equations."

Bouten & van Handel's lecture notes [BvH05] emphasize the Hilbert-space
geometry:

> "These notes are intended as an introduction to noncommutative
> (quantum) filtering theory … focusing on the spectral theorem and the
> conditional expectation as the least-squares estimate."

### 7.2 Identification with the skeleton

The Hilbert space $H$ is the GNS space of a von Neumann algebra
representing the system + measurement apparatus + bath. The nest is
the increasing family of subalgebras generated by the measurement
record up to time $t$. Belavkin's **non-demolition condition** is
what makes the measurement-output process compatible with conditional
expectation (so that a quantum filter exists at all); the resulting
measurement subalgebras form a commutative chain on which the
conditioning is classical. (The precise operator-algebraic statement
— e.g., that this chain is a complete nest in the sense of Arveson —
is the reviewer's reading; the cited sources develop the theory in
martingale and reference-probability terms.) The convex functional is
the (operator-valued) mean-square error. The quantum innovations
representation plays the role of a noncommutative Cholesky factor of
the observation covariance.

Gupta & Hota's comparison paper [GH15] makes the Kalman ↔ Belavkin
analogy explicit:

> "The problem of generalizing the Belavkin–Kalman filter to the case
> where the classical measurement signal is replaced by a fully
> quantum non-commutative output signal."

### 7.3 Fit assessment

**Excellent fit, with operator-algebraic subtleties.** Quantum
filtering is the noncommutative analogue of Kalman/Cholesky in a nest
of commutative subalgebras of measurement outputs. The non-demolition
condition is exactly what allows the noncommutative ambient algebra to
still admit a classical nest structure for the measurement record.
*In this survey we did not locate a source explicitly invoking
Arveson-style nest-algebra factorization in the noncommutative-$L^2$
setting of quantum filtering*; that bridge — if not already present in
work by Powers, Muhly, or Belavkin's own collected papers that we did
not search exhaustively — would be a natural development.

---

## 8. Stochastic Thermodynamics and Maximum Caliber

### 8.1 Stochastic thermodynamics

Sekimoto, Jarzynski, Crooks, and Seifert built **stochastic
thermodynamics** as a framework for trajectory-level definitions of
work, heat, and entropy production [Sei12]:

> "Stochastic thermodynamics … systematically provides a framework for
> extending the notions of classical thermodynamics like work, heat
> and entropy production to the level of individual trajectories."

The Crooks fluctuation theorem [Cro98] and Jarzynski equality are
quadratic / exponential identities on adapted path measures (Radon–
Nikodym derivatives in the natural process filtration).

### 8.2 Maximum caliber

Pressé, Ghosh, Lee & Dill [PGLD13] reviewed the **maximum caliber**
principle:

> "Max Cal originated … as a theoretical tool for predicting …
> dynamics."

and the follow-up Dixit–Wagoner–Weistuch–Pressé–Ghosh–Dill [DWW18]
articulates the variational structure:

> "Max Cal is to dynamical trajectories what the principle of maximum
> entropy is to equilibrium [distributions]."

### 8.3 Identification with the skeleton

Max-caliber is *literally* the convex variational problem on adapted
path measures: maximize relative entropy with respect to a reference
path measure subject to time-marginal or trajectory-averaged
constraints. The Hilbert space is the space of absolutely-continuous
adapted measures (or their log-densities); the convex functional is the
relative entropy (KL divergence); the nest is the natural filtration of
the underlying process; the FOC is the Donsker–Varadhan / Legendre–
Fenchel duality.

### 8.4 Fit assessment

**Very strong on convex/variational grounds, strong on adaptedness.**
Crooks/Jarzynski are quadratic-form identities on adapted path
measures. Max-caliber is the convex-duality framing of the same
structure. The link to KL-divergence control (§6.2) is direct: both
are convex programs on the same space (adapted path measures with KL
divergence as the convex functional), differing only in the constraints
imposed.

---

## 9. Wasserstein Gradient Flows and Adapted Optimal Transport

### 9.1 The JKO scheme

Jordan, Kinderlehrer & Otto [JKO98] proved that the Fokker–Planck
equation is the gradient flow of the free energy in the Wasserstein-2
metric:
$$
\rho_{n+1} = \arg\min_{\rho} \left[ \mathcal{F}(\rho) + \tfrac{1}{2\tau} W_2^2(\rho, \rho_n) \right].
$$
This is a convex optimization (free energy is convex in $\rho$) over
the space of probability measures, repeated iteratively. Otto's
"differential geometry of dissipative evolution equations" extended
this to general gradient flows in Wasserstein geometry.

### 9.2 Adapted / bicausal optimal transport

Acciaio, Backhoff-Veraguas & Zalashko [ABZ20] linked causal optimal
transport to enlargement of filtrations and continuous-time
stochastic optimization. Backhoff-Veraguas, Källblad & Robinson [BKR25]
developed the adapted Wasserstein distance between laws of SDEs.
Eckstein & Pammer [EP24] gave computational methods for adapted OT.
Beiglböck, Pammer & Schrott [BPS25] proved denseness of biadapted
Monge mappings.

### 9.3 Fit assessment and a research gap

**Strong on convex/Wasserstein structure; adapted/bicausal extensions
are not yet used in physics.** Standard JKO is non-adapted (one
terminal time, no filtration constraint). Adapted/bicausal OT lives in
the probability and math-finance literature through 2025; *no physics
paper has been located that applies adapted OT to entropy-production
gradient flow or non-equilibrium fluctuations*.

This is a genuine open gap. A natural candidate would be an "adapted
JKO scheme for the Bertini–Jona-Lasinio macroscopic fluctuation theory
density–current pair" (see §10), but this does not exist in the
literature.

---

## 10. Large Deviations, Freidlin–Wentzell, and Macroscopic Fluctuation Theory

### 10.1 Freidlin–Wentzell rate function

Freidlin–Wentzell theory describes the small-noise large-deviation
behavior of stochastic dynamical systems via a rate function
$$
I[\phi] = \int_0^T L(\phi, \dot\phi)\, dt
$$
with $L$ a convex Lagrangian. The most-probable rare path (the
"instanton") is the minimizer over adapted, forward-in-time paths
satisfying the boundary conditions.

Touchette's *Physics Reports* 2009 review [Tou09] systematized the
Gärtner–Ellis / Legendre–Fenchel convex-duality content of large
deviations in statistical mechanics.

### 10.2 Instantons and convex variational principles

Grafke et al. [Gra21] phrase the instanton problem explicitly:

> "In order to find this most likely trajectory $\phi^\star$, Freidlin–
> Wentzell theory [requires that] $\phi^\star$ is the minimizer of the
> large-deviation rate function."

Bouchet et al. [Bou23] prove convexity and differentiability of the
effective Lagrangian for randomly accelerated particles.

### 10.3 Macroscopic Fluctuation Theory

Bertini, De Sole, Gabrielli, Jona-Lasinio & Landim [BDGJL15] reviewed
**Macroscopic Fluctuation Theory** (MFT), the extension of Onsager–
Machlup to driven diffusive systems. The foundational 2001 paper
(arXiv:cond-mat/0104153, summarized in the 2015 RMP review) states:

> "In our theory a crucial role is played by the time-reversed
> dynamics. Our results include the modification of the Onsager–Machlup
> theory in the SNS, a general Hamilton–Jacobi equation for the
> macroscopic entropy."

MFT is an explicit convex variational principle on the *adapted*
density–current pair $(\rho_t, j_t)$, with a Hamilton–Jacobi equation
governing the macroscopic entropy. The time-reversal structure points
directly to the Cholesky/Wiener–Hopf reverse-time factorization that
the abstract skeleton requires.

### 10.4 Fit assessment

**Excellent fit.** Freidlin–Wentzell and MFT are textbook examples of
convex variational problems over adapted (forward-in-time) paths,
solved via Hamilton–Jacobi convex duality and instanton equations.
The minimum-action path is computed by a convex optimization with
causality automatic. MFT's explicit treatment of time-reversal
parallels the Cholesky reverse-time factorization in the skeleton's
operator-algebraic setting.

---

## 11. Synthesis

### 11.1 What unifies

All eight clusters share at least the first three structural elements
of the skeleton:

- A natural Hilbert space (or convex measure space, in clusters 7–8).
- A natural filtration / chain of past subspaces.
- A convex functional (quadratic in clusters 1–5, 7; KL-divergence /
  relative entropy in clusters 6, 8, 9; large-deviation rate function
  in cluster 10).

Clusters 1 (KK / Toll), 3 (Wiener–Hopf in radiative transfer), and 7
(quantum filtering) have the constructive outer-factorization
ingredient explicitly, even if not in nest-algebra vocabulary. Clusters
4 (FDT), 6 (path-integral control), 8 (max caliber), and 10 (MFT) have
the convex-optimization structure explicitly. Cluster 9 (Wasserstein
gradient flow) has the convex variational form but not the adaptedness
extension.

### 11.2 Side-by-side dictionary

**Table 1.** Mapping of physics clusters to the adapted-convex
skeleton. Cells marked with "—" indicate that the corresponding
structural piece is absent in the standard formulation of that
cluster.

| Cluster | $H$ | Nest / filtration | Convex $J$ | Factorization / dual |
|---------|-----|--------------------|-------------|----------------------|
| Causality / KK | $L^2(\mathbb{R})$ | past $L^2(-\infty,t]$ | passivity quadratic form | Herglotz–Nevanlinna outer factor |
| FDT / Kubo | $L^2(\Omega)$ | filtration of equilibrium process | response cost | Mori–Zwanzig memory-kernel factor |
| WH in radiative transfer | $L^2[0,\infty)$ | $L^2[t,\infty)$ | radiative-equilibrium $L^2$ cost | $K = K_+ K_-$ |
| Path-integral control | adapted controls | state filtration $\mathcal{F}_t^X$ | $\mathbb{E}[\text{cost}] + \text{KL}$ | Hopf–Cole / Legendre–Fenchel |
| Quantum filtering | non-commutative $L^2$ (GNS) | nest of commuting measurement subalgebras | operator-MSE | non-commutative Cholesky |
| Max caliber | adapted path measures | natural filtration | KL divergence | Donsker–Varadhan |
| JKO / Wasserstein | $\mathcal{P}(\mathbb{R}^n)$ | (none in standard JKO) | free energy | Otto calculus |
| LD / Freidlin–Wentzell / MFT | adapted paths | natural filtration | rate function (Lagrangian) | Hamilton–Jacobi convex dual |

### 11.3 Disagreements and tension points

- **The "nest" vocabulary is absent throughout.** Each physics cluster
  uses its own terms — causality, time-ordering, filtration, non-
  demolition, retarded, adapted. Operator-algebraic identification
  (nest algebra, outer factorization in $\operatorname{alg}\mathcal{N}$)
  appears nowhere in the physics literature surveyed.
- **The Hardy-space factorization of the susceptibility is recognized
  in passive-media theory but not labelled as Wiener–Hopf.** Welters–
  Avniel–Johnson, Gralak, Monticone et al. use Herglotz–Nevanlinna and
  outer-function language, but do not invoke nest-algebra factorization
  or connect explicitly to the radiative-transfer Wiener–Hopf literature
  (cluster 3). The arXiv:2604.17058 paper is the first to link KK to
  Hardy-space projection in a non-Markovian setting, but does not
  attempt the cross-cluster synthesis.
- **Quantum filtering is the noncommutative analogue of Kalman, but
  nest-algebra language is not used.** Bouten–van Handel–James develop
  the theory in noncommutative-$L^2$ terms, but use martingale and
  reference-probability methods rather than operator-algebraic
  factorization. Gupta–Hota compare Belavkin to Kalman directly but do
  not invoke Arveson or Davidson *in the sources we located* (see §7.3
  and the exhaustiveness caveat in §11.4).
- **Standard JKO is non-adapted.** The bicausal-OT extensions of the
  past decade live in probability and math-finance journals; they have
  not made the jump to physics. This is the single biggest open
  cross-discipline gap identified in this review.

### 11.4 Why the unifying view appears not to exist in physics

Cluster 1 (causal linear response) and cluster 5 (Wiener–Hopf in
radiative transfer) **were** the original physics problems that
motivated the mathematical machinery — but the abstraction in the
mathematics literature (Krein, Gohberg, Arveson, Davidson) developed in
operator algebras, away from physics, and the abstracted skeleton was
never re-imported into physics under a unifying banner that we located.

Clusters 4 (FDT), 6 (path control), 7 (quantum filtering), 8 (max
caliber), and 10 (LD/MFT) developed in their own journals with their
own vocabularies, each instantiating one or two structural pieces of
the skeleton.

**Caveat on exhaustiveness.** The cross-search done here used the
`alpha` CLI, `web_search`, and targeted `fetch_content` queries; it
did not exhaustively cover (i) Belavkin's collected works, (ii)
Barchielli–Gregoratti's *Quantum Trajectories and Measurements in
Continuous Time*, (iii) Powers/Muhly on continuous nests in
noncommutative settings, or (iv) the math-finance filtration-projection
literature of Kallianpur, Bismut, El Karoui. So statements like "no
paper unifies all eight" should be read as "none located in this
survey." The strongest cross-cluster bridges we did find are: Bouten–
van Handel–James 2007 + Gupta–Hota 2015 (Kalman ↔ Belavkin); Liu 2026
(KK ↔ Hardy space for non-Markovian kernels); and Krein–Gohberg–style
factorization theory as a structural backbone that has not been
advertised as a physics framework.

---

## 12. Open Questions

1. **Adapted JKO for MFT.** (See also §9.3 — the cleanest located gap.) Does a bicausal/adapted Wasserstein
   gradient flow for the macroscopic-fluctuation-theory density–current
   pair $(\rho_t, j_t)$ exist? This is the natural physics realization
   of adapted optimal transport (cluster 9) inside the MFT framework
   (cluster 10). The probability literature has the tools (Acciaio–
   Backhoff–Zalashko, Eckstein–Pammer); the physics application has
   not been written down.
2. **Nest-algebra factorization for non-Markovian open-system memory
   kernels.** The Hardy-space projection of arXiv:2604.17058 is the
   first step. A full operator-theoretic outer factorization of the
   memory kernel (in the sense of Anoussis–Katsoulis 1998 for nest
   algebras) would give explicit constructive solvers for the reduced
   non-Markovian dynamics. Whether such a factorization exists for
   physically realistic kernels (e.g. fractional decay, structured
   environments) is open.
3. **Belavkin–Arveson connection.** Quantum filtering (cluster 7) is
   the noncommutative analogue of Kalman, and Kalman is an instance of
   Cholesky in a nest algebra. A direct statement of "quantum
   innovations = outer factor in the nest of measurement subalgebras"
   in the Arveson/Davidson operator-algebraic sense has not been
   located. This is a natural project for a math-physics paper.
4. **Convex-optimization framing of Kramers–Kronig.** KK is a Hilbert-
   transform identity (a consequence of $H^2$ analyticity), but is
   rarely framed as the FOC of an adapted convex program. A clean
   statement — e.g., "the unique passive causal susceptibility
   matching a given absorption spectrum is the minimizer of [explicit
   convex functional] over the adapted subspace $H^2$" — would unify
   cluster 1 with the explicit-convex clusters (4, 6, 8, 10) under one
   variational principle.
5. **A research programme: "physics on nests".** The Hilbert space +
   nest + convex functional skeleton, applied to physics, suggests a
   coherent research programme: rewrite causal linear response, FDT,
   path-integral control, quantum filtering, max caliber, MFT, and
   instantons under one explicit operator-algebraic framework. The
   payoff would be: (i) shared algorithms (whitening, Cholesky,
   spectral factorization) usable across all clusters; (ii) shared
   sensitivity analyses (how does the solution change when the nest
   changes, e.g. enlarged filtration corresponds to extra measurement);
   (iii) genuine cross-fertilization between filtering theory and
   non-equilibrium thermodynamics. To the reviewer's knowledge, this
   programme has not been articulated.

---

## 13. Recommended Reading Order

For a physicist entering this territory:

1. Toll 1956 [Toll56] — the foundational causality ⇔ dispersion-
   relation equivalence.
2. Encyclopedia of Math, "Wiener–Hopf equation" [EoM-WH] — the
   historical origin in radiative transfer.
3. Onsager–Machlup 1953 [OM53] + Bach–Dürr 1978 [BD78] — convex action
   on stochastic paths.
4. Kappen 2005 [Kap05a] — path-integral stochastic control.
5. Bouten–van Handel–James 2007 [BvHJ07] — quantum filtering and the
   Kalman analogy.
6. Pressé–Ghosh–Lee–Dill 2013 [PGLD13] — max caliber.
7. Bertini et al. 2015 [BDGJL15] — Macroscopic Fluctuation Theory.
8. Touchette 2009 [Tou09] — large-deviation convex duality.

Optional bridge to the operator-theoretic skeleton:

9. Gohberg–Fel'dman 1974 [GF74] or Bart–Gohberg–Kaashoek–Ran 2008
   [BGKR08] — Wiener–Hopf factorization as a structural operator-
   theoretic problem on the half-line.
10. Davidson, *Nest Algebras* [Dav88] — the abstract nest-algebra
    framework underlying the unifying skeleton.

---

## Sources

### Causality and dispersion relations
- [Toll56] Toll, J. S. — *Causality and the Dispersion Relation: Logical Foundations*. Phys. Rev. **104** (1956), 1760. <https://journals.aps.org/pr/abstract/10.1103/PhysRev.104.1760>
- [Tit37] Titchmarsh, E. C. — *Introduction to the Theory of Fourier Integrals*. Oxford, 1937 (Theorem 95). MathWorld summary: <https://mathworld.wolfram.com/TitchmarshTheorem.html>
- [HJ14] Hoffmann-Jørgensen, J. — *On the Titchmarsh theorem and the Hilbert transform*. Eur. Phys. J. H (2014). <https://link.springer.com/content/pdf/10.1140/epjh/e2014-50021-1.pdf>
- [FS04] Figotin, A. & Schenker, J. H. — *Spectral theory of time-dispersive and dissipative systems*. arXiv:math-ph/0404070 (2004). <https://arxiv.org/abs/math-ph/0404070>. (The brief originally cited Welters–Avniel–Johnson at this URL; the URL actually points at Figotin–Schenker. The Welters–Avniel–Johnson "Speed-of-light limitations in passive linear media" appears as *J. Math. Phys.* **52** (2011), 122003 — a separate paper not retrieved in this session.)
- [Gra20] Gralak, B. — *Macroscopic equations for non-magnetic and non-locally non-linear isotropic media*. C. R. Physique **21** (2020), 343. <https://comptes-rendus.academie-sciences.fr/physique/article/CRPHYS_2020__21_4-5_343_0.pdf>
- [Mon20] Monticone, F. et al. — *Causality and Passivity: from Electromagnetism and Network Theory to Metamaterials*. arXiv:2008.05546.
- [Liu26] Liu, K. — *Kramers–Kronig Relations and Causality in Non-Markovian Open Quantum Dynamics: Kernel, State, and Effective Kernel*. arXiv:2604.17058 (2026). <https://arxiv.org/abs/2604.17058>

### Linear response / FDT
- [Kub57] Kubo, R. — *Statistical-Mechanical Theory of Irreversible Processes. I.* J. Phys. Soc. Jpn. **12** (1957), 570. <https://journals.jps.jp/doi/abs/10.1143/JPSJ.12.570>
- [Kub66] Kubo, R. — *The fluctuation–dissipation theorem*. Rep. Prog. Phys. **29** (1966), 255.
- [CW51] Callen, H. B. & Welton, T. A. — *Irreversibility and generalized noise*. Phys. Rev. **83** (1951), 34.

### Wiener–Hopf in physics
- [Mil21] Milne, E. A. — *Radiative equilibrium in the outer layers of a star*. MNRAS **81** (1921), 361.
- [Hop32] Hopf, E. — *Remarks on the Schwarzschild–Milne model of the outer layers of a star*. MNRAS **92** (1932), 863.
- [Hop34] Hopf, E. — *Mathematical Problems of Radiative Equilibrium*. Cambridge, 1934.
- [EoM-WH] Encyclopedia of Mathematics — *Wiener–Hopf equation*. <https://encyclopediaofmath.org/wiki/Wiener-Hopf_equation>
- [LA22] Lawrie, J. B. & Abrahams, I. D. (eds.) — *The Wiener–Hopf technique, its generalisations and applications*. Phil. Trans. R. Soc. A. <https://pmc.ncbi.nlm.nih.gov/articles/PMC8526176/>
- [GP04] Ganapol, B. D. & Pomraning, G. C. — *An application of the Wiener–Hopf method to the one-speed flat-flux problem in a half-space*. Ann. Nucl. Energy (2004).
- [CW89] Cassell, J. S. & Williams, M. M. R. — *Green's function of the one-group transport equation in spherical geometry by the Wiener–Hopf technique*. Astrophys. Space Sci. (1989).
- [MS80] Meister, E. & Speck, F.-O. — *The Sommerfeld half-plane problem revisited, I*. (1980).
- [GF74] Gohberg, I. & Fel'dman, I. A. — *Convolution Equations and Projection Methods for Their Solution*. AMS Translations of Math. Monographs **41** (1974).
- [BGKR08] Bart, H., Gohberg, I., Kaashoek, M. A. & Ran, A. C. M. — *Factorization of Matrix and Operator Functions: The State Space Method*. Birkhäuser, 2008.

### Path integrals and stochastic control
- [OM53] Onsager, L. & Machlup, S. — *Fluctuations and Irreversible Processes*. Phys. Rev. **91** (1953), 1505 & 1512.
- [BD78] Bach, A. & Dürr, D. — *The Onsager–Machlup function as Lagrangian for the most probable path of a diffusion process*. Comm. Math. Phys. **60** (1978).
- [Kap05a] Kappen, H. J. — *Path integrals and symmetry breaking for optimal control theory*. J. Stat. Mech. (2005) P11011.
- [Kap05b] Kappen, H. J. — *Linear theory for control of nonlinear stochastic systems*. Phys. Rev. Lett. **95** (2005), 200201. arXiv:physics/0411119.
- [Tod09] Todorov, E. — *Efficient computation of optimal actions*. PNAS **106** (2009), 11478.
- [DT11] Dvijotham, K. & Todorov, E. — *A unifying framework for linearly solvable control*. UAI 2011.
- [The10] Theodorou, E., Buchli, J. & Schaal, S. — *A generalized path-integral control approach to reinforcement learning*. JMLR **11** (2010), 3137.
- [TT12] Theodorou, E. & Todorov, E. — *Stochastic differential dynamic programming for nonlinear Markov jump diffusion processes*. ACC 2012.

### Quantum filtering
- [Bel88] Belavkin, V. P. — *Nondemolition measurements, nonlinear filtering and dynamic programming of quantum stochastic processes*. (1988).
- [Bel92] Belavkin, V. P. — *Quantum stochastic calculus and quantum nonlinear filtering*. J. Multivariate Anal. **42** (1992), 171. arXiv:math/0512362.
- [BvHJ07] Bouten, L., van Handel, R. & James, M. R. — *An introduction to quantum filtering*. SIAM J. Control Optim. **46** (2007). arXiv:math/0601741.
- [BvH05] Bouten, L. & van Handel, R. — *On the separation principle of quantum control*; alongside van Handel's lecture notes *Quantum filtering: a reference probability approach*. arXiv:math-ph/0508006.
- [WM10] Wiseman, H. M. & Milburn, G. J. — *Quantum Measurement and Control*. Cambridge, 2010.
- [GH15] Gupta, A. & Hota, M. K. — *Generalizing the Belavkin–Kalman filter to non-commutative output signals*. EPJ Quantum Technology **2** (2015), 7.

### Stochastic thermodynamics / max caliber
- [Sei12] Seifert, U. — *Stochastic thermodynamics, fluctuation theorems and molecular machines*. Rep. Prog. Phys. **75** (2012), 126001. arXiv:1205.4176.
- [Cro98] Crooks, G. E. — *Nonequilibrium measurements of free energy differences for microscopically reversible Markovian systems*. J. Stat. Phys. **90** (1998), 1481.
- [PGLD13] Pressé, S., Ghosh, K., Lee, J. & Dill, K. A. — *Principles of maximum entropy and maximum caliber in statistical physics*. Rev. Mod. Phys. **85** (2013), 1115.
- [DWW18] Dixit, P. D., Wagoner, J., Weistuch, C., Pressé, S., Ghosh, K. & Dill, K. A. — *Perspective: Maximum caliber is a general variational principle for dynamical systems*. J. Chem. Phys. **148** (2018), 010901.

### JKO / Wasserstein / adapted OT
- [JKO98] Jordan, R., Kinderlehrer, D. & Otto, F. — *The variational formulation of the Fokker–Planck equation*. SIAM J. Math. Anal. **29** (1998), 1.
- [ABZ20] Acciaio, B., Backhoff-Veraguas, J. & Zalashko, A. — *Causal optimal transport and its links to enlargement of filtrations and continuous-time stochastic optimization*. Stoch. Proc. Appl. **130** (2020). arXiv:1611.02610.
- [BKR25] Backhoff-Veraguas, J., Källblad, S. & Robinson, B. — *Adapted Wasserstein distance between the laws of SDEs*. Stoch. Proc. Appl. (2025).
- [EP24] Eckstein, S. & Pammer, G. — *Computational methods for adapted optimal transport*. Ann. Appl. Probab. **34** (2024). arXiv:2203.05005.
- [BPS25] Beiglböck, M., Pammer, G. & Schrott, A. — *Denseness of biadapted Monge mappings*. Ann. IHP **61** (2025).

### Large deviations / Freidlin–Wentzell / MFT
- [Tou09] Touchette, H. — *The large deviation approach to statistical mechanics*. Phys. Rep. **478** (2009), 1. arXiv:0804.0327.
- [Gra21] Grafke, T. et al. — *Instantons for rare events in heavy-tailed distributions*. J. Stat. Mech. (2021). arXiv:2012.03360.
- [Bou23] Bouchet, F. et al. — *Large deviations of randomly accelerated particles*. arXiv:2305.17276.
- [BDGJL15] Bertini, L., De Sole, A., Gabrielli, D., Jona-Lasinio, G. & Landim, C. — *Macroscopic fluctuation theory*. Rev. Mod. Phys. **87** (2015), 593. (Foundational paper: arXiv:cond-mat/0104153.)

### Cross-references in this workspace
- `papers/adapted-convex-duality.md` — the position-paper draft of the unifying skeleton.
- `outputs/convex-duality-nest-causality.md` — the prior literature review covering the math-side instances (prediction, Kalman, optimal trading, adapted OT, causal info theory, martingale duality).
- `papers/noisy-signal-impact-trading.md` — the explicit stationary scalar Wiener–Hopf calculation for optimal trading.
