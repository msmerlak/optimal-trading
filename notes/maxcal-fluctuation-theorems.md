# How Fluctuation Theorems Drop Out of Maximum Caliber

A more careful derivation than the one-line claim in `notes/maximum-caliber.md`.

---

## 1. Setup: path measure, time reversal, exponential family

Let $\Omega$ be the space of trajectories $\omega = \{x_t\}_{t \in [0,T]}$ of some Markov (or more general) process. Two pieces of structure:

- **A reference path measure** $\mathcal{P}$ on $\Omega$ — typically the *equilibrium* law of the unperturbed system. For a Langevin process $dx_t = -\nabla V(x_t)\,dt + \sqrt{2/\beta}\,dW_t$ this is the law of the equilibrium diffusion.
- **A time-reversal involution** $\theta : \Omega \to \Omega$ that maps $\omega = (x_t)_{t \in [0,T]}$ to $\tilde\omega = (x_{T-t})_{t \in [0,T]}$ (with momenta flipped if present).

Detailed balance for $\mathcal{P}$ is the statement $\mathcal{P} = \mathcal{P} \circ \theta$ — the reference measure is invariant under time reversal.

Now apply MaxCal with constraints $\{F_k\}$ that **need not be even under $\theta$**. The MaxCal solution is the exponentially tilted measure
$$
\frac{dQ}{d\mathcal{P}}(\omega) = \frac{1}{Z(\lambda)} \exp\!\left( \sum_k \lambda_k F_k(\omega) \right).
$$

This is the entire setup. Everything below is a consequence of how this measure transforms under $\theta$.

---

## 2. The key object: the entropy-production functional

Define
$$
\Sigma(\omega) \;:=\; \log \frac{dQ}{dQ \circ \theta}(\omega).
$$
This is the log-Radon–Nikodym derivative between the **forward** path measure and the **time-reversed** path measure. It is a functional of trajectories — a number assigned to each $\omega$.

Plugging in the exponential tilt and using $\mathcal{P} = \mathcal{P} \circ \theta$:
$$
\frac{dQ}{dQ \circ \theta}(\omega)
= \frac{dQ/d\mathcal{P}(\omega)}{dQ/d\mathcal{P}(\theta\omega)}
= \exp\!\left( \sum_k \lambda_k \big[ F_k(\omega) - F_k(\theta\omega) \big] \right).
$$

So
$$
\boxed{\; \Sigma(\omega) = \sum_k \lambda_k \big[ F_k(\omega) - F_k(\theta\omega) \big]. \;}
$$

This is the **time-antisymmetric part** of the log-tilt. Three immediate observations:

1. If every constraint $F_k$ is even under $\theta$ (e.g. mean energy), then $\Sigma \equiv 0$. No fluctuation theorem content.
2. If a constraint $F_k$ is odd under $\theta$ (e.g. heat current, work done, particle displacement under a driving force), then $\Sigma$ picks up $2\lambda_k F_k(\omega)$ from that constraint.
3. By construction $\Sigma(\theta\omega) = -\Sigma(\omega)$.

The interpretation of $\Sigma$ as **entropy production along the trajectory** is what gives this object its physical content. In Langevin systems driven by a non-conservative force, $\Sigma$ is exactly $\beta \cdot \mathrm{(heat dissipated to bath)}$. The MaxCal construction reproduces this without ever postulating it: $\Sigma$ is whatever the log-RN derivative happens to be.

---

## 3. Crooks fluctuation theorem

For any measurable functional $g : \Omega \to \mathbb{R}$,
$$
\mathbb{E}_Q\big[g(\omega)\big]
= \int g(\omega) \, dQ(\omega)
= \int g(\omega) \cdot \frac{dQ}{dQ\circ\theta}(\omega) \, d(Q\circ\theta)(\omega).
$$
Change variables $\omega \to \theta\omega$ in the last integral and use $\theta^2 = \mathrm{id}$, $\Sigma(\theta\omega) = -\Sigma(\omega)$:
$$
\mathbb{E}_Q[g] = \mathbb{E}_Q\big[ g(\theta\omega) \cdot e^{-\Sigma(\omega)} \big] \quad\text{... no, do this with the densities directly.}
$$

Cleaner derivation. Let $\rho(\sigma) := $ probability density of $\Sigma(\omega)$ under $Q$. Then
$$
\rho(\sigma) = \int \delta(\Sigma(\omega) - \sigma) \, dQ(\omega).
$$
Insert $1 = \frac{dQ}{dQ\circ\theta}(\omega) \cdot \frac{dQ\circ\theta}{dQ}(\omega) = e^{\Sigma(\omega)} \cdot e^{-\Sigma(\omega)}$ and use $\Sigma(\theta\omega) = -\Sigma(\omega)$:
$$
\rho(\sigma)
= \int \delta(\Sigma(\omega) - \sigma) \cdot e^{\Sigma(\omega)} \, d(Q\circ\theta)(\omega)
= e^{\sigma} \int \delta(-\Sigma(\theta\omega) - \sigma) \, dQ(\theta\omega).
$$
Substituting $\omega' = \theta\omega$:
$$
\rho(\sigma) = e^{\sigma} \int \delta(\Sigma(\omega') + \sigma) \, dQ(\omega') = e^{\sigma}\, \rho(-\sigma).
$$
This is **Crooks fluctuation theorem**:
$$
\boxed{\; \frac{\rho(\sigma)}{\rho(-\sigma)} = e^{\sigma}. \;}
$$
Positive entropy-production trajectories are exponentially more probable than their negative-entropy-production reverses, with the ratio set exactly by the entropy produced.

In its original physical statement (Crooks 1999, applied to a driven system being switched from one Hamiltonian to another):
$$
\frac{P_{\mathrm{fwd}}(W)}{P_{\mathrm{rev}}(-W)} = e^{\beta(W - \Delta F)},
$$
where $W$ is the work done and $\Delta F$ the free-energy difference. The MaxCal derivation just gave this for **any** odd constraint — work is one example.

---

## 4. Jarzynski equality (integral FT)

Crooks immediately implies the **integral fluctuation theorem**:
$$
\mathbb{E}_Q\!\left[ e^{-\Sigma} \right] = \int e^{-\sigma} \rho(\sigma)\, d\sigma = \int \rho(-\sigma)\, d\sigma = 1.
$$
So
$$
\boxed{\; \mathbb{E}_Q\!\left[ e^{-\Sigma} \right] = 1. \;}
$$

For the work/free-energy case this is
$$
\mathbb{E}\!\left[ e^{-\beta W} \right] = e^{-\beta \Delta F} \quad\Longleftrightarrow\quad \Delta F = -\beta^{-1} \log \mathbb{E}\!\left[ e^{-\beta W} \right],
$$
the **Jarzynski equality** (1997). Jensen's inequality then gives the second law as a corollary:
$$
\langle W \rangle \geq \Delta F.
$$

The entire chain — Crooks → integral FT → Jarzynski → second law — falls out of the single algebraic identity $\Sigma(\theta\omega) = -\Sigma(\omega)$ plus the change-of-variables formula. **No physics input beyond:**

1. A reference measure $\mathcal{P}$ that is time-reversal invariant (detailed balance at equilibrium).
2. Constraints $\{F_k\}$ in the MaxCal program that are odd under time reversal.

---

## 5. What MaxCal contributes (and what it doesn't)

### What MaxCal contributes

- **A canonical place for $\Sigma$ to come from.** Without MaxCal, the entropy-production functional looks like an *ansatz* one writes down for a specific model. With MaxCal, $\Sigma$ is automatically defined as the time-antisymmetric part of $\log dQ/d\mathcal{P}$, and its form $\Sigma = \sum_k \lambda_k [F_k - F_k\circ\theta]$ is forced by the exponential-family structure.

- **A reason the Lagrange multipliers are the right thing.** $\lambda_k$ is the conjugate variable to constraint $F_k$ — for work, $\lambda$ is $\beta$ (inverse temperature). The Jarzynski exponent $e^{-\beta W}$ is *literally* $e^{-\Sigma}$ with $\Sigma = \beta \cdot W$, and the $\beta$ appears as the Lagrange multiplier conjugate to mean energy. MaxCal makes the temperature-as-multiplier identification structural, not coincidental.

- **A bridge to large deviations.** The cumulant generating function $\log \mathbb{E}_Q[e^{s\Sigma}]$ in the long-time limit is the Legendre dual of the large-deviation rate function for $\Sigma/T$. The Gallavotti–Cohen symmetry $I(\sigma) - I(-\sigma) = -\sigma$ of this rate function is the long-time, large-deviation form of Crooks, and it sits naturally in the MaxCal scaffolding.

### What MaxCal does not contribute

- **MaxCal does not derive the second law from nothing.** It derives the second law from (i) a time-reversal-invariant reference measure and (ii) the choice of odd constraints. Both inputs are physics modeling assumptions. The achievement is showing that *given* these inputs, the fluctuation theorems are automatic — not that the inputs themselves are necessary.

- **MaxCal does not tell you what $\mathcal{P}$ should be.** For Langevin systems one usually takes $\mathcal{P}$ to be the equilibrium law, which already encodes detailed balance. Choosing $\mathcal{P}$ is a separate modeling step.

- **MaxCal does not handle absolutely continuous transitions automatically.** Strict positivity of $dQ/d\mathcal{P}$ (no forbidden trajectories) is needed for the Radon–Nikodym manipulations. Hard constraints (e.g. confinement to a region) break the framework and have to be handled by limits or by enlarging the reference measure.

---

## 6. Connection to the adapted-convex skeleton

Why this matters for the broader project:

Fluctuation theorems are exact identities on the **adapted path measure** $Q$. They are statements about how $Q$ transforms under $\theta$, and they make sense only because $Q$ is defined on the full path space carrying a filtration. In the abstract-skeleton language:

- The chain $\{H_t\}$ is the natural filtration of the process.
- The convex functional is $D_{\mathrm{KL}}(Q \| \mathcal{P})$.
- The optimality condition (FOC) is the exponential tilt.
- The **fluctuation theorem is a symmetry of the optimal $Q$ under the time-reversal involution $\theta$ on the underlying nest.**

This is the piece that has no analogue in pure prediction/filtering theory: filtering nests are *causal* (one-directional), so there is no involution $\theta$ to symmetrize against. Fluctuation theorems are what you get when the nest carries a reversal involution and the convex functional (relative entropy) is itself reversal-covariant. Equivalently: fluctuation theorems are the operator-algebraic statement that the outer factorization $dQ/d\mathcal{P}$ commutes (up to sign of $\Sigma$) with $\theta$.

In trading the analogue is **time-symmetric impact kernels**: if the propagator $K(t,s)$ has a reflection symmetry, the FOC of the optimal-execution program has an analogous involution, and identities resembling fluctuation theorems hold for the cost functional under trajectory reversal. This is unexplored in the trading literature and a natural cross-pollination opening — see open question 1 in `outputs/adapted-convex-optimization-physics.md`.

---

## 7. Concrete worked example: overdamped Langevin in a driven potential

To make the abstraction concrete. Take
$$
dx_t = \big[ -\nabla V(x_t) + f(x_t, t) \big] dt + \sqrt{2/\beta}\, dW_t,
$$
with $V$ a conservative potential and $f$ a (possibly non-conservative) external force, on $[0, T]$.

- Reference measure $\mathcal{P}$ = law of the *undriven* process ($f \equiv 0$). This satisfies detailed balance w.r.t. $e^{-\beta V}$.
- Constraint: fix the expected work done by the driving force, $W(\omega) = \int_0^T f(x_t, t) \circ dx_t$ (Stratonovich).
- MaxCal solution: $dQ/d\mathcal{P} \propto e^{\beta W(\omega)}$ — this is the **Girsanov formula** for the driven process, recovered from MaxCal with $\lambda = \beta$.

Under time reversal $\theta$, $W$ flips sign (it is a stochastic line integral against $dx_t$, which reverses). So
$$
\Sigma(\omega) = \beta \big[ W(\omega) - W(\theta\omega) \big] = 2\beta W(\omega),
$$
not quite — actually for the standard Crooks setup with switching protocol one gets $\Sigma = \beta(W - \Delta F)$ via a more careful treatment of the changing potential. The takeaway is the same: $\Sigma$ is linear in $W$, the proportionality constant is $\beta$, and the FT $\mathbb{E}[e^{-\beta(W - \Delta F)}] = 1$ recovers Jarzynski.

The MaxCal lens just makes it visible that **the Girsanov density and the fluctuation-theorem exponent are the same object**, differing only in whether you read it forward or against the time-reversed reference.

---

## 8. References for this specific derivation

- **Maes, C. (1999)**, *The fluctuation theorem as a Gibbs property*, J. Stat. Phys. 95, 367. — The cleanest derivation of Crooks-type relations from the Radon–Nikodym structure of path measures. Independent of MaxCal but reaches the same algebraic identity.
- **Crooks, G. E. (1999)**, *Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences*, Phys. Rev. E 60, 2721. — Original Crooks paper.
- **Jarzynski, C. (1997)**, *Nonequilibrium equality for free energy differences*, Phys. Rev. Lett. 78, 2690.
- **Seifert, U. (2012)**, *Stochastic thermodynamics, fluctuation theorems and molecular machines*, Rep. Prog. Phys. 75, 126001. — Standard review; §4 has the path-measure derivation in the form used above.
- **Chetrite, R. & Gawȩdzki, K. (2008)**, *Fluctuation relations for diffusion processes*, Commun. Math. Phys. 282, 469. — Rigorous treatment of the Girsanov / time-reversal structure.
- **Dixit, Wagoner, Weistuch, Pressé, Ghosh & Dill (2018)**, *Maximum caliber is a general variational principle for dynamical systems*, J. Chem. Phys. 148, 010901. — Explicit positioning of fluctuation theorems as MaxCal consequences.
