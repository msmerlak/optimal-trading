# Exploration: Fluctuation-Theorem Analogues in Optimal Trading

*Working note. Algebra is checked where marked "verified"; everything else is conjecture/sketch.*

---

## 1. The question

Maximum caliber produces fluctuation theorems whenever the path measure carries a time-reversal involution $\theta$ that the convex functional respects (notes/maxcal-fluctuation-theorems.md). Optimal execution has a *causal* impact kernel and is not normally formulated with a path measure over strategies. **Is there a meaningful fluctuation-theorem structure in trading?**

The honest answer below: yes, but only if you make a specific MaxCal-style choice that the standard execution literature does not make, and the resulting identity is more "Gibbs-measure tautology applied to a financial cost" than "new physics of markets." Worth working out anyway because it points to where the bridge is real and where it is decorative.

---

## 2. Three different "symmetries" — disentangle first

For a trading kernel $K(t,s)$ on $[0,T]^2$ define:

(a) **Bilinear symmetry**: $K(t,s) = K(s,t)$. This is just "the cost matrix is symmetric." Almost universal in trading models.

(b) **Time-translation invariance + causality**: $K(t,s) = G(t-s)\, \mathbf{1}_{t \geq s}$. Standard propagator models (Obizhaeva–Wang, Bouchaud).

(c) **Time-reversal symmetry of the cost**: $K(T-t, T-s) = K(t,s)$.

(d) **Two-sided / palindromic kernel**: $K(t,s) = G(|t-s|)$. Would require non-causal price dynamics — past *and future* trades both push current price.

**Key observation (verified algebra).** For the standard quadratic impact cost
$$
C[u] = \int_0^T \int_0^t G(t-s)\, u_t u_s \, ds\, dt
$$
with $G$ time-translation invariant, $C[u] = C[\theta u]$ where $(\theta u)_t = u_{T-t}$. Proof: substitute $t' = T-t$, $s' = T-s$, the constraint $s < t$ flips to $t' < s'$, and relabel — same integral.

So the *deterministic impact cost* is automatically time-reversal invariant for any time-homogeneous kernel, even though the underlying dynamics is causal. This means the naive analogue of $\Sigma$ — log-ratio of cost forward vs. reversed — is **identically zero**, and there is no Crooks identity at the level of cost alone.

Bad news for the naive analogy. Good news: we now know where to look for genuine asymmetry.

---

## 3. Where time-reversal genuinely fails

Four sources of asymmetry, in order of how cleanly each maps to an entropy-production analogue:

### 3.1 Boundary inventory (cleanest analogue)

Liquidation: $X_0 = Q,\, X_T = 0$. Acquisition: $X_0 = 0,\, X_T = Q$. The time-reversed strategy of a liquidator is an acquirer; these are different problems and the optimal-cost values differ generically. This is the analogue of a "nonequilibrium initial condition" in stochastic thermodynamics.

### 3.2 Predictable alpha / signal

Asset has predictable drift $\alpha_t$. Realized signal P&L is $\int u_t \alpha_t \, dt$, linear in $u$. Under reversal $u \to \theta u$, this term becomes $\int u_{T-t} \alpha_t \, dt$ — not equal to the original unless $\alpha$ itself is reversal-symmetric (which generic alphas are not). **This is the trading analogue of a non-conservative driving force.**

### 3.3 Permanent impact

Almgren–Chriss splits impact into temporary (decays) + permanent (does not). The permanent component shifts the equilibrium price by $\gamma \cdot \int_0^t u_s\, ds$ — a path-dependent term that depends on cumulative trade. Under reversal, the cumulative trade history flips sign, and the permanent slippage that the *trader herself pays* changes. This is structurally identical to a "non-conservative work" term in Langevin systems.

### 3.4 Stochastic price noise

Realized cost is $C[u] - \int u_t (\sigma \, dB_t)$ + signal — random because of the Brownian term. Distribution of realized cost is what would carry a Crooks-like identity, if one exists.

---

## 4. The MaxCal construction for trading strategies

The execution literature treats $u$ as deterministic (or as the optimum of a stochastic control problem). MaxCal-style: replace this with a *Gibbs measure on strategies*.

### Setup

- $\mathcal{U}$ = adapted square-integrable strategies $u : [0,T] \to \mathbb{R}$ satisfying boundary conditions ($\int u_t\, dt = Q$ for liquidation).
- Reference measure $\mu_0$ on $\mathcal{U}$ — say a Gaussian measure on strategies, formally $\mu_0(du) \propto \exp(-\tfrac{1}{2}\|u\|^2_{L^2}/\sigma_u^2)$ but I am being loose about path-space measures here.
- Cost functional $J[u] = C[u] - \int u_t \alpha_t\, dt$ (impact minus signal P&L).

MaxCal solution: minimize $D_{\mathrm{KL}}(Q\|\mu_0)$ subject to fixed expected cost $\mathbb{E}_Q[J] = j$, giving
$$
\frac{dQ^\star}{d\mu_0}(u) \propto \exp(-\beta J[u]),
$$
with $\beta$ the Lagrange multiplier — interpretable as inverse "trading temperature" / risk-aversion.

This is **entropy-regularized optimal execution**, a known object (see refs in §7). Mean strategy $\mathbb{E}_{Q^\star}[u]$ recovers the standard Lehalle–Neuman optimum as $\beta \to \infty$; finite $\beta$ gives strategy fluctuations.

### Fluctuation-theorem identity (verified algebra modulo measure-theoretic care)

The log-ratio $\Sigma(u) := \log dQ^\star(u) / dQ^\star(\theta u)$ — using $C[u] = C[\theta u]$ and reversal-invariance of $\mu_0$ (Gaussian with covariance kernel that respects $\theta$) — collapses to
$$
\Sigma(u) = -\beta \big( J[u] - J[\theta u] \big) = \beta \int_0^T \big( u_{T-t} - u_t \big) \alpha_t\, dt.
$$

The reversal-asymmetric part is **purely the signal-extraction term**. Impact symmetry kills the rest.

By the same change-of-variables argument as in stochastic thermodynamics, the distribution of $\Sigma$ under $Q^\star$ satisfies a **Crooks-type identity**:
$$
\frac{\rho(\Sigma = \sigma)}{\rho(\Sigma = -\sigma)} = e^\sigma,
$$
and a **Jarzynski-type identity**:
$$
\mathbb{E}_{Q^\star}\!\left[ \exp\!\left( -\beta \int_0^T (u_{T-t} - u_t) \alpha_t\, dt \right) \right] = 1.
$$

**Interpretation.** Among entropy-regularized trading strategies sampled from $Q^\star$, a strategy that extracts more signal than its time-reverse is exponentially more probable, with the ratio set exactly by how much extra signal it extracts. The Jarzynski identity says the *exponential moment* of (signal asymmetry under reversal) is exactly $1$.

### What this *means* in trading language

Pick a random execution policy from $Q^\star$. Run it; also conceptually run its time-reverse. The difference in realized signal P&L between the two is $\Sigma/\beta$. Crooks tells you the strategies that extract more signal forward than backward dominate the Gibbs measure, with quantified ratio.

Boring restatement: in an entropy-regularized strategy ensemble, signal-aligned strategies are exponentially preferred. We already knew this. **The FT is a quantitative tautology, not a new prediction.** What it adds is a one-line *constraint* on the strategy distribution — any sampling scheme for $Q^\star$ (e.g., Langevin sampling for entropy-regularized RL trading) must respect this identity exactly, and violations are a numerical diagnostic.

---

## 5. Where the analogy is real vs. decorative

### Real

1. **Adapted convex skeleton is shared.** Both problems live as $\min J$ over a convex set with a filtration constraint. The first-order condition (Lehalle–Neuman Fredholm equation for trading, Donsker–Varadhan exponential tilt for MaxCal) is the same kind of object.

2. **Entropy-regularized trading naturally carries a MaxCal interpretation.** When you add a KL penalty to encourage exploration (as in RL-based execution), the optimal policy *is* a Gibbs measure on strategies, and all path-measure machinery (Girsanov, change of measure, exponential families) applies directly.

3. **Permanent impact ↔ nonconservative force.** Both add an irreversible "dissipation" term to the cost functional; the formal correspondence is clean.

### Decorative

1. **Time-reversal symmetry of the dynamics**, in the strong sense of full Crooks/Jarzynski with $\beta$ = inverse temperature and $\Sigma$ = thermodynamic entropy production, has no real market counterpart. The trading kernel is causal; the price process is not in equilibrium; there is no $\beta$ except as a hyperparameter.

2. **The "Crooks identity for trading" derived in §4 is a Gibbs-measure tautology.** Any exponential-family measure on any space has a Crooks-like identity for any reversal-asymmetric observable. Trading does not get extra structure from this beyond what entropy-regularized optimization already provides.

3. **There is no obvious "second law of trading."** $\mathbb{E}_{Q^\star}[\Sigma] \geq 0$ specializes to "the Gibbs-optimal strategy on average extracts more signal forward than backward," which is just saying the optimum prefers signal-aligned trajectories. True but vacuous.

---

## 6. Concrete things that would be worth working out

In rough order of payoff vs. effort:

1. **Stationary scalar verification.** For the noisy-signal-impact model in `papers/noisy-signal-impact-trading.md` with exponential decay kernel and AR(1) signal, write the MaxCal/entropy-regularized version explicitly. Compute the Crooks ratio analytically. Check the Jarzynski identity by Gaussian integration. *Expected effort: a few hours of algebra; expected output: a worked example tying the two notes together.*

2. **Permanent-impact + signal version.** Add an Almgren–Chriss permanent-impact term. Compute the analogue of "dissipated work" — how much the trader's own trade costs her via permanent price shift. Verify this enters $\Sigma$ as expected. Check whether the Jarzynski identity gives a *nontrivial* bound on average permanent-impact cost. If so, this is the cleanest new content.

3. **Information-thermodynamic bound on alpha capture.** Sagawa–Ueda generalized Jarzynski to systems with feedback (measurement-based control). The trader using a signal is exactly such a system. Their bound says
$$
\mathbb{E}[\exp(-\beta W_{\mathrm{diss}} - I)] = 1
$$
where $I$ is the mutual information between the signal and the controller's action. Translating: **there is a thermodynamic-style bound on how much alpha you can extract per unit of impact paid, given a fixed mutual information between your signal and your trades.** This could be a real, nontrivial result if worked out for a Gaussian linear model. *Expected effort: a week of careful algebra; expected output: a candidate paper-quality result.*

4. **MFT-style hydrodynamic limit.** Take the high-frequency, many-trader limit (a la macroscopic fluctuation theory). The density–current pair $(\rho_t, j_t)$ analogue would be (inventory density, trade flow). The MFT large-deviation rate function would give the most-probable execution trajectory in a market populated by many similar liquidators. *Expected effort: significant; expected output: cleanest theoretical bridge between the trading and physics literatures in this whole project, if it works.*

5. **Bicausal OT analogue for trading.** No paper in the adapted-OT literature applies these tools to optimal execution, and no execution paper uses bicausal OT. A clean problem statement: what is the bicausal Wasserstein distance between the laws of two execution strategies, and does it give a useful stability / sensitivity bound? *Expected effort: moderate (problem framing is the hard part); expected output: a new application of an existing tool.*

---

## 7. References that bear on this

- **Touchette, H. (2018)**, *Introduction to dynamical large deviations of Markov processes*, Physica A 504, 5. — Tilted-measure machinery used in §4.
- **Sagawa, T. & Ueda, M. (2010)**, *Generalized Jarzynski equality under nonequilibrium feedback control*, Phys. Rev. Lett. 104, 090602. — Information-thermodynamic Jarzynski; key for §6.3.
- **Parrondo, J. M. R., Horowitz, J. M. & Sagawa, T. (2015)**, *Thermodynamics of information*, Nature Physics 11, 131. — Review.
- **Guo, X. & Xu, R. (2022)**, *Stochastic games for fuel follower problem: N vs. MFG*, SIAM J. Control Optim. — One entry point into stochastic control / RL for execution with entropy regularization.
- **Wang, H. & Zhou, X.-Y. (2020)**, *Continuous-time mean–variance portfolio selection: A reinforcement learning framework*, Math. Finance 30, 1273. — Entropy-regularized control in finance; the framework in which the MaxCal-style trading Gibbs measure lives naturally.
- **Lehalle, C.-A. & Neuman, E. (2019)**, *Incorporating signals into optimal trading*, Finance Stoch. 23, 275. — The Fredholm equation that plays the role of the adapted normal equation in trading.
- **Cao, H., Guo, X. & Lee, J.-W. (2024)**, on entropy-regularized continuous-time RL for execution. — Most recent direct application.

---

## 8. Bottom line

The genuine bridge between fluctuation theorems and trading runs through **entropy-regularized execution** with a **non-trivial signal**, and the most interesting candidate result is an **information-thermodynamic bound on alpha capture per unit mutual information between signal and trade** (§6.3). The naive "Crooks identity for trading cost" without a signal is empty because the deterministic impact cost is reversal-invariant.

The framework is a real analogy at the level of *adapted convex duality on a path measure*; it is decorative at the level of *thermodynamic interpretation of trading P&L*. The recommendation is to write up §6.1 as a concrete worked example, and then attempt §6.3 as a candidate result.
