# Maximum Caliber

## The principle

**Maximum caliber (MaxCal)** is the dynamical extension of Jaynes's maximum-entropy principle. Where MaxEnt picks the *equilibrium* distribution that maximizes Shannon entropy subject to constraints on time-averaged observables, MaxCal picks the *path-space measure* (a probability distribution over whole trajectories) that maximizes path entropy subject to constraints on trajectory-level observables.

The name is E. T. Jaynes's, from his 1980 paper *The Minimum Entropy Production Principle*: "caliber" is to a *tube of trajectories* what "entropy" is to a *set of microstates*. Same functional, different domain.

## Formal statement

Let $\mathcal{P}$ be a reference path measure on trajectories $\{x_t\}_{t \in [0,T]}$ (often: the uncontrolled / equilibrium / Brownian process). Among all path measures $Q$ on the same space, choose
$$
Q^\star = \arg\min_Q\; D_{\mathrm{KL}}(Q \,\|\, \mathcal{P}) \quad \text{subject to} \quad \mathbb{E}_Q[F_k] = f_k,
$$
where $F_k$ are trajectory functionals (e.g. average current, dwell time in a state, mean displacement). The solution is the **exponential-tilted** path measure
$$
\frac{dQ^\star}{d\mathcal{P}} \propto \exp\!\left(\sum_k \lambda_k F_k\right),
$$
with Lagrange multipliers $\lambda_k$ chosen to satisfy the constraints. This is *literally* the Donsker–Varadhan / Legendre–Fenchel dual of a large-deviation rate function.

When the reference measure is white noise and the constraint is the mean drift, $Q^\star$ is the law of an Ornstein–Uhlenbeck or general Langevin process — MaxCal *recovers* stochastic dynamics from a variational principle on path entropy.

## Why it matters in physics

1. **Reproduces stochastic thermodynamics from one principle.** Fluctuation theorems (Jarzynski, Crooks) fall out as identities on the exponential family of tilted path measures. The entropy production along a trajectory is the log-Radon–Nikodym derivative between forward and time-reversed path measures — exactly what MaxCal's exponential family produces.

2. **Reproduces FDT.** Linear response of $Q^\star$ to a perturbation of the constraint $f_k$ has the quadratic-form structure of Kubo's formula, with the path-covariance playing the role of the susceptibility.

3. **Reproduces Onsager–Machlup.** For small perturbations from equilibrium, $-\log dQ^\star/d\mathcal{P}$ is the Onsager–Machlup action — the convex Lagrangian on paths.

4. **Inference tool.** Given experimental trajectories (single-molecule pulling, ion channel recordings), MaxCal is the principled way to fit a dynamical model with the minimum extra assumptions beyond what the data constrain. This is how Pressé, Dill, Ghosh and collaborators have actually deployed it.

## Connection to the adapted-convex skeleton

MaxCal is one of the cleanest physics instances of the abstract skeleton:

| Skeleton element | MaxCal realization |
|---|---|
| Hilbert / convex space $H$ | adapted path measures absolutely continuous w.r.t. $\mathcal{P}$ |
| Nest $\{H_t\}$ | natural filtration $\{\mathcal{F}_t\}$ of the trajectory |
| Convex functional $J$ | $D_{\mathrm{KL}}(Q\|\mathcal{P})$ (strictly convex in $Q$) |
| Constraint | $\mathbb{E}_Q[F_k] = f_k$ |
| FOC / dual | exponential tilt with Lagrange multipliers $\lambda_k$ |
| Outer factorization | the tilted measure $dQ^\star/d\mathcal{P}$ factorizes as a product over time increments because KL on adapted measures decomposes additively along the filtration (chain rule for relative entropy) |

The chain rule
$$
D_{\mathrm{KL}}(Q \| \mathcal{P}) = \sum_t \mathbb{E}_Q\!\left[ D_{\mathrm{KL}}\!\left(Q(\cdot\mid\mathcal{F}_t) \,\|\, \mathcal{P}(\cdot\mid\mathcal{F}_t)\right) \right]
$$
is the path-measure analogue of Cholesky factorization in the nest of increasing $\sigma$-algebras. Each term is the local one-step KL between conditional laws — the "Cholesky diagonal entry" at time $t$.

## Connection to other things in this workspace

- **KL control / Kappen / Todorov (cluster 6 of the physics review).** Same functional, different problem statement. Path-integral control *adds* a state-cost term to KL and minimizes; MaxCal *constrains* expectations and minimizes pure KL. The Hopf–Cole linearization works in both because the underlying convex object is identical.

- **Large deviations / Touchette / Freidlin–Wentzell (cluster 10).** MaxCal *is* the Donsker–Varadhan variational principle viewed from the inference side rather than the asymptotic-probability side. The rate function and the MaxCal Lagrangian are convex conjugates.

- **Optimal trading.** Trading-cost minimization with a market-impact penalty has *exactly* this structure: minimize an expected quadratic cost (analogue of $J$) over adapted strategies (the nest), with the impact kernel playing the role of a covariance. The Lehalle–Neuman Fredholm equation is the FOC of the same kind of adapted convex program — quadratic rather than KL, but same skeleton. The reason you can swap "stochastic thermodynamics" and "optimal execution" with very little vocabulary change is that both live on the adapted-path-measure side of MaxCal.

## Key references

- Jaynes 1980 — coined "caliber."
- **Pressé, Ghosh, Lee & Dill 2013**, *Principles of maximum entropy and maximum caliber in statistical physics*, **Rev. Mod. Phys. 85, 1115**. The standard review.
- **Dixit, Wagoner, Weistuch, Pressé, Ghosh & Dill 2018**, *Perspective: Maximum caliber is a general variational principle for dynamical systems*, **J. Chem. Phys. 148, 010901**. The "this is one principle behind everything" pitch.
- Stock, Ghosh & Dill 2008 — clean derivation of two-state kinetics from MaxCal.
- Ghosh, Dixit, Agozzino & Dill 2020, *The Maximum Caliber Variational Principle for Nonequilibria*, Annu. Rev. Phys. Chem. — newer pedagogical review.

## What MaxCal does *not* do

- It does not by itself pick the constraints. You still have to know what trajectory observables to fix — that's modeling input.
- It does not enforce time-reversal symmetry or detailed balance unless you constrain those explicitly. Driven systems are perfectly natural in MaxCal; this is why it generalizes to stochastic thermodynamics.
- It is not a derivation of the second law from nothing — it is a variational *parametrization* of dynamics consistent with given empirical constraints.

The cleanest one-line summary: **MaxCal = maximum entropy on path space**, and "path space" automatically carries a filtration, which is why it slots into the adapted-convex skeleton without extra work.
