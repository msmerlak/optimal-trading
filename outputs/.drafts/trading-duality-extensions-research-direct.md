# Research Notes: trading-duality-extensions

## Search queries used (web_search)

1. "matrix Wiener-Hopf spectral factorization multi-asset optimal execution Volterra propagator"
2. "Hawkes process microfoundation power-law market impact Jaisson Rosenbaum Bacry"
3. "predictive information past future mutual information Bialek Nemenman Tishby rate distortion Gaussian"
4. "signature methods optimal execution trading Kalsi Lyons rough path"
5. "LQG separation principle innovations representation Kalman Wonham classical reference"
6. "H-infinity filtering minimax estimation Hassibi Sayed Kailath robust"
7. "Abi Jaber Neuman optimal execution Volterra propagator matrix operator Riccati"
8. "mean field game optimal execution crowding Cardaliaguet Lehalle propagator"
9. "Gaussian rate distortion reverse water-filling spectrum quadratic cost Berger Cover Thomas"
10. "structured state space model S4 long convolution causal filter learnable"

## Anchors selected

### Multi-asset / matrix propagators
- Abi Jaber, Neuman, Tuschmann (2024) "Optimal Portfolio Choice with Cross-Impact Propagators", arXiv:2403.10273 — matrix-valued Volterra propagator + signal; solution via operator resolvent / infinite-dimensional stochastic control. Direct generalization to the matrix Wiener–Hopf setting we want to discuss. https://arxiv.org/abs/2403.10273
- Abi Jaber, Neuman (2022, pub. 2025) "Optimal Liquidation with Signals: the General Propagator Case", arXiv:2211.00447 — single-asset general Volterra propagator with signal. https://arxiv.org/abs/2211.00447
- Schied–Strehle et al. (HAL 2013, arXiv:1310.4471) "Multivariate transient price impact and matrix-valued positive definite functions" — conditions on matrix decay kernels for well-posed multi-asset execution. https://arxiv.org/abs/1310.4471
- Mastromatteo, Benzaquen et al. (2017) "Trading Lightly: Cross-Impact and Optimal Portfolio Execution", arXiv:1702.03838 — empirical multivariate propagators. https://arxiv.org/abs/1702.03838
- Frei et al. (2025) "Multi-asset optimal trade execution with stochastic cross-effects: An Obizhaeva–Wang-type framework", arXiv:2503.05594 — matrix-valued stochastic propagator/resilience. https://arxiv.org/abs/2503.05594

### Microfoundation of power-law impact
- Jusselin, Rosenbaum (2018) "No-arbitrage implies power-law market impact and rough volatility", arXiv:1805.07134 — exactly the bridge we want: no-arbitrage ⇒ power-law impact ⇒ rough volatility, with one-to-one exponent correspondence. https://arxiv.org/abs/1805.07134
- Jaisson, Rosenbaum (2015) "Limit theorems for nearly unstable Hawkes processes", Ann. Appl. Probab. 25(2):600–631 — nearly-unstable Hawkes ⇒ rough volatility scaling limit. https://projecteuclid.org/journals/annals-of-applied-probability/volume-25/issue-2/Limit-theorems-for-nearly-unstable-Hawkes-processes
- Jaisson (2015) "Market impact as anticipation of the order flow imbalance", Quant. Finance 15(7):1123-1135. https://arxiv.org/abs/1402.1288
- Ouazzani Chahdi, Rosenbaum, Szymanski (2026) "A unified theory of order flow, market impact, and volatility", arXiv:2601.23172 — single statistic H₀ ties signed-flow persistence, rough volatility, and power-law impact. https://arxiv.org/abs/2601.23172

### LQG separation principle / innovations
- Bensoussan, Van Schuppen, Willems (2011) "The Separation Principle in Stochastic Control, Redux", arXiv:1103.3005 — modern careful statement; cites Wonham, Bellman, Åström, Kalman–Bucy lineage. https://arxiv.org/abs/1103.3005
- Stengel, Princeton MAE546 LQG notes — textbook statement: optimal control = certainty-equivalence ∘ Kalman filter. https://stengel.mycpanel.princeton.edu/MAE546Seminar24.pdf
- Lund control synthesis notes — historical references Wiener–Kolmogorov / Kalman–Bucy / Wonham. https://www.control.lth.se/fileadmin/control/Education/DoctorateProgram/ControlSystemsSynthesis/2016/lqg.pdf

### H∞ / minimax / robust
- Hassibi–Sayed–Kailath, "H∞ filtering as Kalman filtering in Krein space" (1994/96); LMS as exact minimizer of H∞ error norm. https://www.babak.caltech.edu/pubs/hinfinity.html
- Hassibi book "Indefinite Quadratic Estimation and Control" — provides the minimax framework that would replace the Wiener prefilter under adversarial uncertainty.

### Mean-field / crowding
- Cardaliaguet, Lehalle (2017/2018) "Mean Field Game of Controls and An Application To Trade Crowding", Math Fin Econ 12(3):335-363, arXiv:1610.09904. https://arxiv.org/abs/1610.09904
- Neuman, Voß (2021, arXiv:2106.09267) — N-player ⇒ MFG convergence O(N⁻²) for execution. https://arxiv.org/abs/2106.09267

### Signature methods
- Kalsi, Lyons, Perez Arribas (2020) "Optimal Execution with Rough Path Signatures", SIAM J. Fin. Math., arXiv:1905.00728 — model-free signature-based optimal execution. https://arxiv.org/abs/1905.00728

### Information theory / rate-distortion
- Cover & Thomas, *Elements of Information Theory*, ch. 13 — Gaussian rate-distortion, reverse water-filling on spectrum. https://cs-114.org/wp-content/uploads/2015/01/Elements_of_Information_Theory_Elements.pdf
- Zamir, Kochman, Erez (2008) "Achieving the Gaussian Rate-Distortion Function by Prediction", arXiv:0711.1766 — predictive (time-domain, innovations) realization of Gaussian R(D); deep parallel to causal innovation interpretation. https://arxiv.org/abs/0711.1766
- Bialek, Nemenman, Tishby (2001) "Predictability, Complexity, and Learning", Neural Computation 13:2409 — predictive information I(past;future); three scaling regimes (finite / log T / fractional power-law). https://www.princeton.edu/~wbialek/our_papers/bnt_01a.pdf
- Abdallah, Plumbley (2012) "Predictive Information Rate in Discrete-time Gaussian Processes", arXiv:1206.0304 — PIR closed-form for AR(N); duality with multi-information rate under spectral inversion. https://arxiv.org/abs/1206.0304

### ML / learnable causal filters
- Gu, Goel, Ré (2022) "Efficiently Modeling Long Sequences with Structured State Spaces" (S4), arXiv:2111.00396. https://arxiv.org/abs/2111.00396 — long causal convolutions parameterized by structured (DPLR) state-space matrices; effectively learnable causal kernels, including power-law-like HiPPO bases.

## Key conceptual claims supported by these anchors

C1. The matrix Wiener–Hopf factorisation problem for vector signals is exactly the operator-resolvent / Riccati problem solved in Abi Jaber–Neuman–Tuschmann (2024). Our scalar Wiener–Hopf result is the diagonal special case.

C2. Jusselin–Rosenbaum (1805.07134) gives the microstructural reason a power-law kernel appears in the first place: no-arbitrage at the Hawkes/order-flow level *forces* a power-law impact, in one-to-one correspondence with the rough-volatility exponent. So the "fractional derivative" interpretation of the optimal causal rule is not just a mathematical artefact — it is the unique no-arbitrage-consistent macroscopic kernel.

C3. The Wiener prefilter + impact-adjusted causal rule is a special case of the LQG separation principle (Bensoussan–Van Schuppen–Willems 2011). What is non-trivial is that the "control" half here is itself a Wiener–Hopf factor of the impact kernel rather than a Riccati gain.

C4. The Gaussian rate-distortion function admits a *predictive* time-domain realisation (Zamir–Kochman–Erez 2008) whose innovation filter is the same Kolmogorov–Szegő/Wiener factor that appears in the trading rule. This is more than an analogy: the optimal-trading "kernel innovation" is the same operator as the optimal lossy-source coder's innovation filter.

C5. The predictive information I(past;future) of an AR/Volterra signal is precisely the upper bound on monetisable alpha when impact is incurred in proportion to the signal information used. Bialek–Nemenman–Tishby's three regimes (finite, log T, fractional power-law) translate into three regimes of long-horizon revenue scaling.

C6. Crowding (MFG) replaces the single-agent K by an *effective* kernel K_eff that depends on the equilibrium aggregate strategy; the Wiener–Hopf factorisation is still well-defined in the symmetric MFG case but the factor depends on the population.

C7. Signature methods (Kalsi–Lyons–Perez Arribas) are the natural model-free generalization when the linear-Gaussian assumption fails; the linear Wiener–Hopf rule is the linear projection of the signature expansion.

C8. S4-style structured state-space models implement parameterised causal long convolutions and can in principle *learn* the impact-adjusted causal kernel rather than assume it; the closed-form Wiener–Hopf rule serves as a sanity-check baseline.
