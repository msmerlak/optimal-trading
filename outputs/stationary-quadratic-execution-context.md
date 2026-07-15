# Stationary Quadratic-Cost Optimal Execution: Literature Context

**Slug:** `stationary-quadratic-execution-context`
**Date:** 2026-07-11
**Purpose:** Position the two central modeling assumptions of the paper *Fractional Derivatives as the Markowitz Rule for Cost-Managed Trading* — (i) quadratic execution cost / linear price impact, and (ii) stationary trading on the whole line — in the optimal-execution literature.

---

## 1. The two assumptions and why they matter

The paper under review solves the gain–cost problem
$$\max_{u\in L^2_{\rm adap}(\mathbb{R})}\ \mathbb{E}\!\int u_t\alpha_t\,dt \;-\; \tfrac{\gamma}{2}\iint |t-s|^{-\beta}\,u_t u_s\,dt\,ds$$
on the whole line, for an adapted stationary signal $\alpha$ and a power-law impact kernel. Two modeling assumptions are load-bearing:

**(A1) Quadratic cost.** The cost of an execution schedule is a bilinear form in the trading rate: $\tfrac{\gamma}{2}\langle u, C u\rangle$ with $C$ the convolution against $|t|^{-\beta}$. Equivalently, price impact is linear in the trade — a trade of twice the size moves the price twice as far.

**(A2) Stationary trading on the whole line.** The problem is set on $\mathbb{R}$ rather than on a bounded interval $[0,T]$, and the signal $\alpha$ is stationary. There is no terminal-inventory constraint and no boundary layer near $t=0$ or $t=T$; the paper solves the "bulk" or "interior" asymptotic problem.

Both assumptions are consequential. (A1) is the standard theoretical assumption in the optimal-execution literature but is empirically contested by the square-root law of large-metaorder impact. (A2) is comparatively rare in the propagator literature; almost all published signal-adaptive execution work is finite-horizon with a terminal-inventory constraint. This document maps where the paper's assumptions sit in the surrounding scholarship.

---

## 2. Assumption A1: Quadratic cost is the standard theoretical assumption

### 2.1 The lineage

Quadratic cost (linear impact) has been the workhorse assumption of optimal execution since the origin of the field. **Bertsimas & Lo (1998)** [1] set up discrete-time execution with a linear permanent-impact term and derive uniform slicing by dynamic programming. **Almgren & Chriss (2000)** [2] added mean-variance risk and separated temporary from permanent impact — both linear in the trading rate, so the cost is quadratic — and produced the mean-variance efficient frontier for execution that remains the standard reference model.

The next wave added *transient* impact through a decay kernel: the price at $t$ is depressed by $\int_{s<t}G(t-s)\dot X_s\,ds$, giving a quadratic-form cost $\tfrac12\iint G(|t-s|)\dot X_t\dot X_s\,ds\,dt$. **Obizhaeva & Wang (2013)** [3] took a block-shape limit-order-book with exponential resilience. **Alfonsi, Fruth & Schied (2010)** [4] generalized to arbitrary LOB shape with exponential resilience of volume or price. **Gatheral (2010)** [5] characterized which decay kernels avoid dynamic price-manipulation strategies; power-law $G(u)=u^{-\beta}$ with $0<\beta<1$ is admissible. **Gatheral, Schied & Slynko (2012)** [6] formulated optimal liquidation on $[0,T]$ as a quadratic form on strategies whose first-order condition is a Fredholm integral equation of the first kind. **Bouchaud, Gefen, Potters & Wyart (2004)** [7] introduced the empirical propagator with power-law decay.

Every paper in this lineage takes the cost quadratic in the trading rate. Disagreement in the theoretical literature is only about the *shape* of the impact kernel: block, exponential, power-law, or general positive-definite.

### 2.2 The empirical challenge: the square-root law

Empirically, the price move induced by a *metaorder* of total size $Q$ scales as $\sqrt{Q}$, not $Q$. **Lillo, Farmer & Mantegna (2003)** [8] documented a concave master curve across NYSE stocks with large-$Q$ exponent close to $1/2$. **Almgren, Thum, Hauptmann & Li (2005)** [9] fit a Citigroup dataset with permanent impact $\propto Q^{0.5}$ and temporary impact $\propto$ (rate)$^{0.6}$. **Tóth, Lempérière, Deremble, de Lataillade, Kockelkoren & Bouchaud (2011)** [10] proposed a latent-order-book / locally-linear-supply theory that generates $\sqrt{Q}$ generically. The textbook synthesis is **Bouchaud, Bonart, Donier & Gould (2018)** [11].

### 2.3 Reconciliation

The theoretical literature reconciles quadratic cost with square-root empirics via regime separation. The square-root law describes the *cumulative* impact of a metaorder of finite size $Q$; the theoretical propagator describes the *instantaneous* impact of an infinitesimal rate $\dot X$. A locally linear propagator with long-memory order flow can reproduce $\sqrt{Q}$ under a martingale-price constraint. **Nadtochiy (2020)** [12] gives a microstructural explanation of the concavity of price impact.

Practically, three arguments justify the choice of quadratic cost in theoretical work:

1. **Tractability.** Only the linear case admits closed forms via Fredholm, Riccati, or Wiener–Hopf techniques.
2. **Small-order limit.** Linear impact is the leading-order expansion of any smooth impact function around zero.
3. **Second-order robustness.** **Guasoni & Weber (2020)** [13] show that linear-impact strategies retain near-optimal performance when true impact is a concave power law with realistic parameters. **Brokmann, Itkin, Muhle-Karbe & Schmidt (2024)** [14] give explicit results for using linear strategies with nonlinear impact. **Muhle-Karbe, Wang & Webster (2024)** [15] show a linear model with a stochastic liquidity coefficient can absorb most of the observed concavity.

**Consequence for the paper.** The quadratic-cost assumption is the mainstream modeling choice in theoretical execution and is empirically defensible for small trades and near-optimal for moderate trades. It is not a niche or contested assumption; it is the one under which nearly all closed-form execution results have been obtained.

---

## 3. Assumption A2: Stationary whole-line trading is a rare setting

### 3.1 The finite-horizon default

Essentially every paper in the transient-impact lineage of §2.1 works on a bounded horizon $[0,T]$ with $X_0=x_0$ and $X_T=0$ (liquidation) or with a running risk penalty. This is inherited from Almgren–Chriss, where "execute a parent order of size $X_0$ by time $T$" is the operational primitive.

Signal-adaptive extensions preserve the finite horizon:

- **Cartea, Jaimungal & Penalva (2015)** [16] and the associated signal-adaptive papers work on $[0,T]$ with terminal inventory constraints.
- **Lehalle & Neuman (2019)** [17] incorporate OU and other signals into optimal execution on $[0,T]$.
- **Neuman & Voß (2022)** [18] add general finite-variation signals with linear temporary + exponential transient impact, still on $[0,T]$.
- **Forde, Sánchez-Betancourt & Smith (2022)** [19] treat pure power-law resilience with a Gaussian signal on $[0,T]$ via Söhngen–Tricomi inversion.
- **Abi Jaber & Neuman (2025)** [20] extend to general Volterra propagator on $[0,T]$ using infinite-dimensional stochastic control; the value function is characterized through the resolvent of the second kind of the propagator.
- **Abi Jaber, Neuman & Tuschmann (2024)** [21] extend the resolvent method to matrix-valued cross-impact.
- **Abi Jaber, De Carvalho & Pham (2024)** [22] add inequality constraints with applications to battery storage; horizon is still finite.

The finite-horizon default is deeply entrenched. It aligns with the practical parent-order framing, provides a natural terminal-inventory constraint that pins down the KKT multipliers, and gives the Fredholm operator on $[0,T]$ a bounded domain on which its inverse can be constructed by Söhngen–Tricomi or Riccati methods.

### 3.2 Stationary/infinite-horizon execution: a thin literature

Genuinely stationary or infinite-horizon execution work is rare and mostly outside the transient-impact + signal setting.

**Merton with proportional costs.** The infinite-horizon Merton problem with proportional transaction costs (Davis–Norman 1990; Shreve–Soner 1994) is stationary but is a *portfolio-choice* problem with a different friction structure and no signal-adaptive execution primitive. Related long-run work includes **Kallsen & Muhle-Karbe (2017)** [23] on the general asymptotic structure of small proportional costs.

**Gârleanu & Pedersen (2013)** [24] is the closest antecedent to the paper under review. They solve a stationary infinite-horizon quadratic-cost portfolio-choice problem with multi-factor mean-reverting alpha signals. The friction is *temporary quadratic cost only* — no transient kernel, no propagator, no Volterra structure. The solution is an ergodic Riccati and the optimal position tracks a signal-dependent aim portfolio. The paper under review can be viewed as extending Gârleanu–Pedersen from temporary-only to transient impact by replacing the pointwise Riccati with a Wiener–Hopf factorization.

**Market making** work in stationary regimes (Cartea, Jaimungal and coauthors) uses different mathematical primitives — inventory-driven quoting — not directly comparable.

**Dolinsky (2024)** [25] is a rare infinite-horizon Almgren–Chriss / linear-impact study for monotone strategies, but without transient kernel or exogenous signal.

**Consequence for the paper.** A stationary, whole-line, signal-adaptive execution problem with a *transient (Volterra) impact kernel* appears not to have been solved in closed form in the prior literature we have surveyed. Gârleanu–Pedersen is the closest in spirit but has only temporary impact; every propagator + signal paper we identified (Lehalle–Neuman, Neuman–Voß, Forde–SB–Smith, Abi Jaber–Neuman, Abi Jaber–Neuman–Tuschmann, Abi Jaber–De Carvalho–Pham) uses finite horizon.

---

## 4. The airfoil boundary vs. interior-asymptotic connection

### 4.1 The Söhngen–Tricomi machinery

The finite-interval singular integral equation with Cauchy kernel is Söhngen's 1939 airfoil equation. Its inversion is in **Tricomi (1957)** [26]. For the finite-interval power-law-propagator problem on $[0,T]$, the FOC reduces via half-order Riemann–Liouville integrals $I^{(1-\beta)/2}$ to a Cauchy-kernel equation, and the Söhngen–Tricomi inversion produces the boundary-weight
$$\omega(t) = \bigl(t(T-t)\bigr)^{(\beta-1)/2}, \qquad 0<t<T.$$
For $0<\beta<1$ this weight is integrable but unbounded at both endpoints: the boundary layers of the execution problem.

### 4.2 Boundary layers vs. interior

**Forde, Sánchez-Betancourt & Smith (2022)** [19] apply exactly this machinery to signal-adaptive execution: with a Gaussian signal, pure transient power-law kernel, and no temporary impact, the optimal speed solves a family of linear Fredholm equations whose kernel is the finite-interval fractional integral. The optimal $u^\star(t)$ carries the boundary weight $\omega(t)$, which blows up at both endpoints — the spike-and-tail structure familiar from Obizhaeva–Wang in the power-law limit.

The Söhngen solution factorizes as
$$u^\star(t) \;=\; \omega(t) \times [\text{regular signal-driven part}].$$
The weight-times-regular structure is standard for Cauchy-kernel Fredholm inversion on a bounded interval (Tricomi 1957 [26] Ch. IV) and appears in the execution context in Forde–SB–Smith [19] as the closed form of the optimal speed. The regular part is what a whole-line stationary formulation directly computes. As $T\to\infty$, on compact subsets $t\in[\varepsilon T, (1-\varepsilon)T]$ the boundary weight is $O(1)$ and the regular part is expected to converge to the translation-invariant solution of the whole-line singular integral equation, uniformly on compact interior subsets. This convergence is the substantive content of the interior asymptotic of the paper under review (§4.1 there); Tricomi's finite-interval inversion establishes the factorization but does not directly state the $T\to\infty$ compact-interior limit, which the paper under review must establish on its own.

### 4.3 Consequence for the paper

The interior-far-from-boundaries framing isolates the signal-tracking content of the strategy from the terminal-condition transients that dominate any finite-$T$ Söhngen inversion. The paper's Section 4.1 argument — that the bulk fractional-derivative solution is the interior asymptotic, with boundary corrections spanned by the two Söhngen–Tricomi modes $(t(T-t))^{(\beta-1)/2}$ and $\tfrac{T-2t}{2}(t(T-t))^{(\beta-1)/2}$ — is the honest statement of this decomposition.

---

## 5. Positioning: a comparison map

The literature can be organized along three binary axes: impact model (quadratic-cost vs. concave), horizon (finite vs. stationary), and signal (yes vs. no). The paper under review occupies the (quadratic, stationary, signal) cell.

| Paper | Kernel | Cost form | Horizon | Signal | Technique | Closed form |
|---|---|---|---|---|---|---|
| Bertsimas & Lo 1998 [1] | permanent only | quad. in rate | finite | no | DP | yes |
| Almgren & Chriss 2000 [2] | temp. + perm., linear | quad. in rate | finite | no | calc. of variations | yes |
| Bouchaud et al. 2004 [7] | empirical propagator | — | — | — | econometrics | — |
| Obizhaeva & Wang 2013 [3] | block LOB, exp. resilience | quad. in schedule | finite | no | DP / block + interior | yes |
| Alfonsi–Fruth–Schied 2010 [4] | general LOB, exp. resilience | quad. form | finite | no | variational | yes (up to shape) |
| Gatheral 2010 [5] | general $G$ | quad. form | — | no | no-arb. char. | — |
| Gatheral–Schied–Slynko 2012 [6] | general PD $G$ | quad. form | finite | no | Fredholm 1st kind | reduction only |
| Gârleanu & Pedersen 2013 [24] | temporary only | quad. in rate | **stationary** | **yes** (Gaussian) | Riccati | **yes** |
| Lehalle & Neuman 2019 [17] | temp. + exp. transient | quad. in rate | finite | yes | BSDE | yes (exp.) |
| Neuman & Voß 2022 [18] | temp. + exp. transient | quad. in rate | finite | yes (FV) | FBSDE | yes (exp.) |
| Forde–SB–Smith 2022 [19] | power-law resilience | quad. form | finite | yes (Gaussian) | Söhngen–Tricomi | yes |
| Abi Jaber & Neuman 2025 [20] | general Volterra + temp. | quad. + form | finite | yes | infinite-dim. control | up to resolvent |
| AJ–Neuman–Tuschmann 2024 [21] | matrix Volterra | quad. form | finite | yes | resolvent | up to resolvent |
| AJ–De Carvalho–Pham 2024 [22] | general $G$ + constraints | quad. form | finite | yes | Lagrangian | numerical |
| Brokmann et al. 2024 [14] | nonlinear power | non-quadratic | finite | yes | perturbation | approximate |
| **Paper under review** | **power-law transient** | **quad. form** | **stationary (whole line)** | **yes** | **Wiener–Hopf** | **yes (fractional derivative)** |

Two observations follow.

**The paper's assumptions are individually standard.** Quadratic cost is the workhorse of theoretical execution. Power-law transient impact is the empirically supported kernel shape (Bouchaud, Gatheral, Forde–SB–Smith). Signal-adaptive formulations are a decade-old research program.

**Their combination is uncommon.** We are not aware of a prior paper combining: quadratic cost, transient (Volterra) impact, adapted stochastic signal, and stationary/whole-line horizon. Gârleanu–Pedersen has stationary + signal + quadratic-cost but *no transient kernel*. Neuman–Voß, Forde–SB–Smith, Abi Jaber–Neuman have transient kernel + signal but on *finite horizon*. The stationary/whole-line signal-adaptive Volterra problem is a gap in the literature (with the caveat that no exhaustive arXiv/SSRN search has been performed).

---

## 6. What the paper contributes

Given the map in §5, the paper contributes three items that are not present in the antecedents surveyed:

1. **A filtration Wiener–Hopf identity $(P_+ C P_+)^{-1} = C_+^{-1} P_+ C_-^{-1}$** for the adapted inverse of a translation-invariant positive kernel. This is the operator identity that replaces the resolvent characterization of Abi Jaber–Neuman [20] in the stationary/whole-line regime.

2. **A closed-form fractional-derivative optimizer for the power-law kernel.** Substituting the Marchaud/Riemann–Liouville factorization $C_\pm = c_\beta^{1/2}I_\pm^{(1-\beta)/2}$ into the WH identity collapses the operator formula to a fractional derivative of the forecast curve of total order $1-\beta$. The half-order factorization is implicit in Forde–SB–Smith [19] at their Cauchy-kernel reduction step; the explicit signal-adaptive fractional-derivative form of the optimizer appears to be new.

3. **A Markowitz-style structural correspondence.** The paper reads the quadratic-form solution through a Markowitz analogy — cost operator $\leftrightarrow$ return covariance, tradeability norm $\leftrightarrow$ Mahalanobis norm — with the Wiener–Hopf factorization playing the role of the missing structure forced by causality. This framing is unavailable in the resolvent or Fredholm formulations of the prior signal-adaptive literature.

---

## 7. What the paper does not address

The 2×2×2 map exposes the boundaries of the paper's contribution:

- **Concave impact.** The square-root law and its theoretical descendants (Tóth et al. [10], Guasoni–Weber [13], Brokmann et al. [14]) are outside the paper's scope. Wiener–Hopf factorization is a Hilbert-space property tied to the quadratic form and does not obviously extend to nonlinear cost. Concave-impact optimal execution remains a distinct research program.
- **Terminal-inventory / finite-horizon problems.** Almgren–Chriss and Gatheral–Schied–Slynko trajectories are the finite-horizon interior limit of the paper's stationary solution (§4.1), but the finite-interval boundary layers are handled classically by Söhngen–Tricomi rather than by the paper's machinery. The bulk formula recovers finite-horizon results in the interior asymptotic.
- **Constrained trading.** Nonnegative-inventory, rate-cap, and battery-storage constraints (Abi Jaber–De Carvalho–Pham [22]) require Lagrangian machinery not developed in the paper.
- **Non-stationary signals.** The paper's Wiener–Hopf identity uses translation invariance of $C$. Non-stationary signals require regeneration of the factorization at every time.
- **Cross-impact.** Matrix-valued cross-impact propagators (Abi Jaber–Neuman–Tuschmann [21]) are treated only in a passing extension.

---

## 8. Consensus, disagreements, and open questions

**Consensus in the literature.**
- Quadratic cost / linear impact is the standard modeling assumption for closed-form theoretical execution results.
- Power-law transient impact with exponent $\beta \in [0.2, 0.6]$ is the empirically favored kernel shape.
- Signal-adaptive execution matters and admits closed forms in specific settings (exponential kernel, Gaussian signals, or via resolvent).

**Disagreements.**
- Whether concave impact should be modeled directly (Tóth et al., Guasoni–Weber) or absorbed into linear proxies (Brokmann et al., Muhle-Karbe–Wang–Webster). The paper implicitly takes the second position.
- Whether the natural setting is finite-horizon with terminal inventory (the entire propagator literature) or stationary with an interior asymptotic (Gârleanu–Pedersen and the paper under review). This is a modeling-cultural split, not a technical disagreement.

**Open questions surfaced by the review.**
- Extension of the Wiener–Hopf machinery to concave/nonlinear cost — apparently obstructed, since factorization is a Hilbert-space property.
- Rigorous convergence of the finite-horizon Söhngen–Tricomi regular part to the whole-line solution as $T\to\infty$ uniformly on compact interior subsets. This is stated in Section 4.1 of the paper under review as an $o(1)$ interior asymptotic; a direct citation to Tricomi's 1957 monograph or a self-contained proof would firm the claim.
- Whether the tradeability functional $\|P_+ C_-^{-1}\alpha\|^2$ can be used as a signal-design objective, replacing the standard information-coefficient or MSE loss. This is the natural follow-up direction identified alongside the paper.
- Empirical calibration: for $\beta \in [0.2, 0.6]$ (Lillo et al. [8], Almgren et al. [9]), the fractional-derivative order $\nu = (1-\beta)/2 \in [0.2, 0.4]$ is well within regularization-stable range for standard fractional-calculus discretizations.

---

## References

1. Bertsimas D, Lo AW (1998) Optimal control of execution costs. *J. Financial Markets* 1(1):1–50. doi:10.1016/S1386-4181(97)00012-8.
2. Almgren R, Chriss N (2000) Optimal execution of portfolio transactions. *J. Risk* 3(2):5–39. doi:10.21314/JOR.2001.041.
3. Obizhaeva AA, Wang J (2013) Optimal trading strategy and supply/demand dynamics. *J. Financial Markets* 16(1):1–32.
4. Alfonsi A, Fruth A, Schied A (2010) Optimal execution strategies in limit order books with general shape functions. *Quantitative Finance* 10(2):143–157. arXiv:0708.1756.
5. Gatheral J (2010) No-dynamic-arbitrage and market impact. *Quantitative Finance* 10(7):749–759.
6. Gatheral J, Schied A, Slynko A (2012) Transient linear price impact and Fredholm integral equations. *Math. Finance* 22(3):445–474. doi:10.1111/j.1467-9965.2011.00478.x.
7. Bouchaud J-P, Gefen Y, Potters M, Wyart M (2004) Fluctuations and response in financial markets: The subtle nature of 'random' price changes. *Quantitative Finance* 4(2):176–190. arXiv:cond-mat/0307332.
8. Lillo F, Farmer JD, Mantegna RN (2003) Master curve for price-impact function. *Nature* 421:129–130. arXiv:cond-mat/0207428.
9. Almgren R, Thum C, Hauptmann E, Li H (2005) Direct estimation of equity market impact. *Risk* 18:57–62.
10. Tóth B, Lempérière Y, Deremble C, de Lataillade J, Kockelkoren J, Bouchaud J-P (2011) Anomalous price impact and the critical nature of liquidity in financial markets. *Phys. Rev. X* 1:021006. arXiv:1105.1694.
11. Bouchaud J-P, Bonart J, Donier J, Gould M (2018) *Trades, Quotes and Prices: Financial Markets Under the Microscope*. Cambridge University Press.
12. Nadtochiy S (2020) A simple microstructural explanation of the concavity of price impact. arXiv:2001.01860.
13. Guasoni P, Weber MO (2020) Nonlinear price impact and portfolio choice. *Math. Finance* 30(2):341–376. doi:10.1111/mafi.12234.
14. Brokmann X, Itkin D, Muhle-Karbe J, Schmidt P (2024) Tackling nonlinear price impact with linear strategies. *Math. Finance* 34. doi:10.1111/mafi.12449.
15. Muhle-Karbe J, Wang Z, Webster K (2024) Stochastic liquidity as a proxy for nonlinear price impact. *Operations Research* 72(2):425–450. SSRN 4286108.
16. Cartea Á, Jaimungal S, Penalva J (2015) *Algorithmic and High-Frequency Trading*. Cambridge University Press.
17. Lehalle C-A, Neuman E (2019) Incorporating signals into optimal trading. *Finance & Stochastics* 23(2):275–311.
18. Neuman E, Voß M (2022) Optimal signal-adaptive trading with temporary and transient price impact. *SIAM J. Financial Math.* 13(2):551–575. arXiv:2002.09549. doi:10.1137/20M1375486.
19. Forde M, Sánchez-Betancourt L, Smith B (2022) Optimal trade execution for Gaussian signals with power-law resilience. *Quantitative Finance* 22(3):585–596. doi:10.1080/14697688.2021.1950919.
20. Abi Jaber E, Neuman E (2025) Optimal liquidation with signals: The general propagator case. *Math. Finance* 35(4):841–866. arXiv:2211.00447. doi:10.1111/mafi.12465.
21. Abi Jaber E, Neuman E, Tuschmann S (2024) Optimal portfolio choice with cross-impact propagators. arXiv:2403.10273.
22. Abi Jaber E, De Carvalho N, Pham H (2024) Trading with propagators and constraints: Applications to optimal execution and battery storage. arXiv:2409.12098.
23. Kallsen J, Muhle-Karbe J (2017) The general structure of optimal investment and consumption with small transaction costs. *Math. Finance* 27(3):659–703. arXiv:1303.3148.
24. Gârleanu N, Pedersen LH (2013) Dynamic trading with predictable returns and transaction costs. *J. Finance* 68(6):2309–2340. doi:10.1111/jofi.12080.
25. Dolinsky Y (2024) Some computations for optimal execution with monotone strategies. arXiv:2411.10726.
26. Tricomi FG (1957) *Integral Equations*. Interscience Publishers.
