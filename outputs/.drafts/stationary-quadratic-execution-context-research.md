# Research: Quadratic cost / linear impact and stationary whole-line execution — literature context

## Summary
Quadratic execution cost (equivalently linear price-impact response) is the standard modelling assumption in the theoretical optimal-execution literature from Bertsimas–Lo (1998) and Almgren–Chriss (2000) through the propagator / Fredholm / resolvent papers of Gatheral–Schied–Slynko (2012), Neuman–Voß (2022) and Abi Jaber–Neuman (2025); the concave "square-root" law of Lillo–Farmer–Mantegna (2003) and Tóth et al. (2011) is treated as an empirical fact about metaorders that is usually deferred to small-cost asymptotics (Guasoni–Weber 2020, Brokmann–Itkin–Muhle-Karbe–Schmidt 2024) rather than solved directly. Essentially all of the signal-adaptive theory works on a finite horizon $[0,T]$ with a terminal-inventory constraint; genuinely stationary / whole-line signal-adaptive formulations are rare, and the standard airfoil-equation treatment (Söhngen 1939, Tricomi 1957) delivers boundary-layer weights $(t(T-t))^{(\beta-1)/2}$ that are exactly the objects a stationary formulation is designed to strip away.

## A. Quadratic-cost / linear-impact lineage

The lineage begins with **Bertsimas & Lo (1998)**, "Optimal control of execution costs," *J. Financial Markets* 1(1), 1–50, doi:10.1016/S1386-4181(97)00012-8, who set up discrete-time execution with a linear permanent-impact term and derive a naive-diversification (uniform slicing) solution by dynamic programming. **Almgren & Chriss (2000)**, "Optimal execution of portfolio transactions," *J. Risk* 3(2), 5–39, doi:10.21314/JOR.2001.041, add mean-variance risk and separate temporary from permanent impact; both are linear in the trading rate, so the execution cost is quadratic in the rate. The Almgren–Chriss efficient frontier is the canonical closed form and remains the reference model.

The next wave modelled *transient* impact through a decay kernel $G$: the price move at $t$ from a trade $\dot X_s$ at $s<t$ is $G(t-s)\dot X_s$, and the trader pays $\tfrac12\int\!\!\int G(|t-s|)\dot X_t\dot X_s\,ds\,dt$. **Obizhaeva & Wang (2013)**, "Optimal trading strategy and supply/demand dynamics," *J. Financial Markets* 16(1), 1–32 (SSRN 686168, 2005 working paper), take a block-shape LOB with exponential resilience — $G(u)=\lambda e^{-\rho u}$; the optimal strategy is two block trades plus a continuous middle piece. **Alfonsi, Fruth & Schied (2010)**, "Optimal execution strategies in limit order books with general shape functions," *Quantitative Finance* 10(2), 143–157, arXiv:0708.1756, extend to arbitrary LOB density (still exponential resilience of volume or of price), giving a nonlinear impact function but quadratic-in-rate cost. **Gatheral (2010)**, "No-dynamic-arbitrage and market impact," *Quantitative Finance* 10(7), 749–759, characterises which decay kernels avoid price-manipulation strategies; power-law $G(u)=u^{-\beta}$ with $0<\beta<1$ is admissible. **Gatheral, Schied & Slynko (2012)**, "Transient linear price impact and Fredholm integral equations," *Math. Finance* 22(3), 445–474, doi:10.1111/j.1467-9965.2011.00478.x, formulate optimal liquidation as a quadratic form on strategies whose stationarity condition is a first-kind Fredholm integral equation with kernel $G$; positive-definiteness of $G$ (Bochner) rules out price manipulation. **Bouchaud, Gefen, Potters & Wyart (2004)**, "Fluctuations and response in financial markets: the subtle nature of 'random' price changes," *Quantitative Finance* 4(2), 176–190, arXiv:cond-mat/0307332, introduce the empirical propagator with power-law decay; this is the microstructure counterpart of the theoretical kernel.

Consensus: all of these papers assume a quadratic form in the trading rate/schedule; disagreement is only about the shape of the kernel (block/exponential/power-law/general PD).

## B. Concave / square-root impact alternative

Empirically, the price move induced by a metaorder of size $Q$ scales like $\sqrt{Q}$, not $Q$. **Lillo, Farmer & Mantegna (2003)**, "Master curve for price-impact function," *Nature* 421, 129–130, arXiv:cond-mat/0207428, first document a concave master curve across NYSE stocks with exponent ≈ 1/2 in the large-$Q$ regime. **Almgren, Thum, Hauptmann & Li (2005)**, "Direct estimation of equity market impact," *Risk* 18, 57–62, fit a Citigroup dataset with permanent impact ∝ $Q^{0.5}$ and temporary impact ∝ (rate)$^{0.6}$. **Tóth, Lempérière, Deremble, de Lataillade, Kockelkoren & Bouchaud (2011)**, "Anomalous price impact and the critical nature of liquidity in financial markets," *Phys. Rev. X* 1, 021006, arXiv:1105.1694, propose a latent-order-book / locally-linear-supply theory that generates $\sqrt{Q}$ generically. **Bouchaud, Bonart, Donier & Gould (2018)**, *Trades, Quotes and Prices*, CUP, is the standard reference textbook.

Reconciliation with the theory papers of §A rests on regime separation: the square-root law is a statement about the *cumulative* impact of a *metaorder* of finite size $Q$, whereas theory papers model the *instantaneous* impact of a *rate* $\dot X$ and integrate. **Bouchaud (2010)** and **Farmer, Gerig, Lillo & Waelbroeck** show a locally-linear propagator with long-memory order flow reproduces $\sqrt{Q}$ under a fair-pricing / martingale-price constraint. See also **Jusselin & Rosenbaum (2020)**, "A simple microstructural explanation of the concavity of price impact," arXiv:2001.01860. Practically, **Guasoni & Weber (2020)**, "Nonlinear price impact and portfolio choice," *Math. Finance* 30(2), 341–376, and **Brokmann, Itkin, Muhle-Karbe & Schmidt (2024)**, "Tackling nonlinear price impact with linear strategies," *Math. Finance* 34, doi:10.1111/mafi.12449, show that linear-impact (quadratic-cost) strategies retain near-optimal performance when the true impact is a concave power law with realistic parameters. **Muhle-Karbe, Wang & Webster (2024)**, "Stochastic liquidity as a proxy for nonlinear price impact," *Operations Research* 72(2), 425–450 (SSRN 4286108), argue that a linear model with a stochastic liquidity coefficient can absorb most of the concavity. The typical justification cited in theory papers is: (i) tractability and existence of closed forms; (ii) the linear model is the small-order limit; (iii) the loss from misspecifying concavity with the wrong linear kernel is second-order in impact size.

## C. Stationary / whole-line vs. finite-horizon formulations

Essentially every paper in §A works on $[0,T]$ with $X_0=x_0$, $X_T=0$ (liquidation) or $X_T$ free with a running risk penalty. Signal-adaptive versions (Cartea–Jaimungal, **Cartea, Jaimungal & Penalva (2015)** *Algorithmic and High-Frequency Trading*, CUP; **Cartea, Donnelly & Jaimungal (2018)** "Enhancing trading strategies with order book signals," *Applied Math. Finance* 25(1)) all keep the finite horizon. **Lehalle & Neuman (2019)**, "Incorporating signals into optimal trading," *Finance & Stochastics* 23(2), 275–311, and **Neuman & Voß (2022)** (see §E) are also finite-horizon.

Stationary / infinite-horizon execution work is comparatively thin and mostly outside the transient-impact signal-adaptive setting. The infinite-horizon Merton problem with **proportional transaction costs** (Davis–Norman 1990; Shreve–Soner 1994) is stationary but not an execution problem. **Kallsen & Muhle-Karbe (2017)** "The general structure of optimal investment and consumption with small transaction costs," *Math. Finance* 27(3), 659–703, arXiv:1303.3148, and **Guasoni & Weber (2017)** "Dynamic trading volume," *Math. Finance* 27(2), doi:10.1111/mafi.12099, work at the long-run / ergodic scale but the friction is proportional, not quadratic. **Gârleanu & Pedersen (2013)**, "Dynamic trading with predictable returns and transaction costs," *J. Finance* 68(6), 2309–2340, is a genuinely stationary quadratic-cost portfolio-choice paper with signals (multi-factor mean-reverting alphas), but they use only *temporary* quadratic cost — no transient kernel. Their solution is an ergodic Riccati and the target strategy tracks a signal-dependent aim-portfolio. **Muhle-Karbe, Wang & Webster (2024)** and **Cartea, Jaimungal & Sánchez-Betancourt (2022)** work in stationary regimes for market making but the inventory-execution primitive is not the same. **Some Computations for Optimal Execution with Monotone Strategies** (Dolinsky, arXiv:2411.10726, 2024) is a rare infinite-horizon Almgren–Chriss / linear-impact study, but without transient kernel or exogenous signal.

Bottom line: a *stationary, whole-line, signal-adaptive execution* problem with a *transient* (Volterra) impact kernel appears to have very few direct antecedents; Gârleanu–Pedersen is the closest in spirit but has no transient impact.

## D. Airfoil-equation / Söhngen–Tricomi lineage in finance

The finite-interval singular integral equation
$\displaystyle \frac{1}{\pi}\int_0^T \frac{f(s)}{t-s}\,ds = g(t),\quad 0<t<T$
is Söhngen's airfoil equation (Söhngen, *Luftfahrtforschung*, 1939) and its inversion theory is in **Tricomi (1957)**, *Integral Equations*, Interscience, ch. 4, and in the paper **Tricomi**, "On the finite Hilbert transformation," *Quart. J. Math.* 2 (1951), 199–211. The general finite-interval fractional / power-kernel Cauchy equation reduces to it via half-order Riemann–Liouville integrals $I^{1/2}$: writing $G(u)=u^{-\beta}$ and using $I^{(1-\beta)/2}$ symmetrically on both sides collapses the propagator equation to a Cauchy-kernel equation, and the Söhngen–Tricomi inversion produces the characteristic weight $\omega(t)=(t(T-t))^{(\beta-1)/2}$. For $0<\beta<1$ this weight is integrable but unbounded at both endpoints — these are the *boundary layers*.

**Forde, Sánchez-Betancourt & Smith (2022)**, "Optimal trade execution for Gaussian signals with power-law resilience," *Quantitative Finance* 22(3), 585–596, doi:10.1080/14697688.2021.1950919, apply exactly this machinery to execution: with a Gaussian signal and pure transient power-law kernel and no temporary impact, the optimal selling *speed* solves a family of linear Fredholm equations whose kernel is the finite-interval fractional integral, inverted by Tricomi's formula. The optimal $u^*(t)$ carries the boundary-layer weight $(t(T-t))^{(\beta-1)/2}$: it blows up at both endpoints of $[0,T]$ (the classical spike-and-tail of Obizhaeva–Wang in the power-law limit). See also **Gatheral, Schied & Slynko (2012)** and **Alfonsi, Schied & Slynko (2012)** "Order book resilience, price manipulation, and the positive portfolio problem," *SIAM J. Financial Math.* 3(1), for related Fredholm/positive-definiteness analyses.

An "interior asymptotic far from boundaries" is meaningful precisely because the airfoil solution factorises into (a) the singular Söhngen weight, times (b) a smoother "regular part" driven by the signal. For $T\to\infty$ (or equivalently for $t$ far from $0$ and from $T$) the boundary weight tends to a constant on compact subsets, and the regular part converges to a translation-invariant solution of the *whole-line* singular integral equation. This is the ergodic / stationary regime that a whole-line signal-adaptive formulation isolates directly, bypassing the endpoint singularities that dominate any finite-$T$ Söhngen inversion.

## E. Signal-adaptive execution 2020–2025 landscape

Two main technical routes to signal-adaptive execution with a Volterra propagator have emerged.

**Resolvent / Fredholm route.** **Neuman & Voß (2022)**, "Optimal signal-adaptive trading with temporary and transient price impact," *SIAM J. Financial Math.* 13(2), 551–575, arXiv:2002.09549, treat linear temporary + exponential transient impact on a finite horizon with a general finite-variation signal. Solution is a coupled system of four forward–backward SDEs, explicit for exponential kernels. **Abi Jaber & Neuman (2025)**, "Optimal liquidation with signals: the general propagator case," *Math. Finance* 35(4), 841–866, arXiv:2211.00447, extend to a general Volterra propagator using infinite-dimensional stochastic control (lifting to an operator-valued Riccati). The value function is characterised through the *resolvent of the second kind* of the propagator; when temporary impact is present the free-boundary problem is well-posed and closed-form up to solving the resolvent equation. **Abi Jaber, Neuman & Tuschmann (2024/2025)**, "Optimal portfolio choice with cross-impact propagators," arXiv:2403.10273, *Math. Finance*, doi:10.1111/mafi.70025, extend the resolvent method to matrix-valued cross-impact propagators. **Abi Jaber, De Carvalho & Pham (2024)**, "Trading with propagators and constraints: applications to optimal execution and battery storage," arXiv:2409.12098, add inequality constraints (nonnegative inventory / rates) and solve via a Lagrangian / infinite-dimensional stochastic Pontryagin approach; battery storage is a stationary-flavour application but the mathematical horizon is still finite. All of these use finite horizon $[0,T]$ with terminal inventory constraint.

**Wiener–Hopf / airfoil route.** **Forde, Sánchez-Betancourt & Smith (2022)** (see §D) use Söhngen–Tricomi on the pure power-law resilience problem to get a Gaussian Volterra representation of the optimal speed. **Kuchler / Bank–Voß** and later work uses Riesz-transform / Wiener–Hopf techniques for singular controls. Whole-line / stationary versions of Wiener–Hopf-type solutions exist for classic control problems but rarely for the signal-adaptive execution problem with transient impact.

Closed forms: Neuman–Voß closed under exponential $G$; Abi Jaber–Neuman closed given the resolvent (integral formula); Forde–SB–Smith closed for pure power-law resilience with Gaussian signal; Gârleanu–Pedersen (2013) closed for temporary-only quadratic with linear-Gaussian signals on infinite horizon. None of the propagator papers is set on the whole line with an ergodic signal.

## Comparison table (15 papers)

| Paper | Kernel | Cost form | Horizon | Signal | Technique | Closed form |
|---|---|---|---|---|---|---|
| Bertsimas & Lo 1998 | none (perm. only) | quad. in rate | finite | no | DP | yes |
| Almgren & Chriss 2000 | temp. + perm., linear | quad. in rate | finite | no | calculus of variations | yes |
| Bouchaud–Gefen–Potters–Wyart 2004 | empirical propagator (power-law) | — (descriptive) | — | — | econometrics | — |
| Obizhaeva & Wang 2013 | block LOB, exp. resilience | quad. in schedule | finite | no | DP / two blocks + interior | yes |
| Alfonsi–Fruth–Schied 2010 | general LOB shape, exp. resilience | quadratic form | finite | no | variational | yes (up to shape) |
| Gatheral 2010 | general $G$ | quadratic form | — | no | no-arb. characterisation | — |
| Gatheral–Schied–Slynko 2012 | general PD $G$ | quadratic form | finite | no | Fredholm 1st kind | reduction only |
| Gârleanu & Pedersen 2013 | temporary only | quad. in rate | **infinite** | **yes** (Gaussian) | Riccati / DP | **yes** |
| Lehalle & Neuman 2019 | temp. + exp. transient | quad. in rate | finite | yes (OU + others) | BSDE | yes (exp. kernel) |
| Neuman & Voß 2022 | temp. + exp. transient | quad. in rate | finite | yes (FV) | FBSDE | yes (exp.) |
| Forde–Sánchez-Betancourt–Smith 2022 | power-law resilience, no temp. | quadratic form | finite | yes (Gaussian) | Söhngen–Tricomi / airfoil | yes |
| Abi Jaber & Neuman 2025 | general Volterra $G$ + temp. | quad. + quadratic form | finite | yes | infinite-dim. control, resolvent | up to resolvent |
| Abi Jaber–Neuman–Tuschmann 2024 | matrix Volterra cross-impact | quad. form | finite | yes | resolvent | up to resolvent |
| Abi Jaber–De Carvalho–Pham 2024 | general $G$ + constraints | quad. form | finite | yes | Lagrangian / KKT | numeric |
| Brokmann–Itkin–Muhle-Karbe–Schmidt 2024 | nonlinear (power) impact | non-quadratic | finite | yes | perturbation | approximate |

## Explicit answers

(i) **Is quadratic cost the standard modelling assumption in theoretical execution literature?** Yes. From Bertsimas–Lo and Almgren–Chriss onward, essentially every theoretical paper that derives an optimal execution *strategy* in closed or semi-closed form assumes cost quadratic in the trading rate / schedule (equivalently, linear price impact). The concave / square-root literature is empirical or descriptive, and even its theoretical extensions (Guasoni–Weber; Brokmann et al.) treat concavity as a perturbation of the linear model.

(ii) **Is the paper being reviewed one of the first to work in a stationary / whole-line setting with a signal?** With the caveat that Gârleanu & Pedersen (2013) already gave a stationary infinite-horizon signal-adaptive quadratic-cost solution — but with *temporary impact only*, no transient kernel — a stationary / whole-line formulation with an exogenous stochastic signal and a *transient (Volterra) propagator* appears to be new. All published propagator + signal papers (Lehalle–Neuman, Neuman–Voß, Forde–SB–Smith, Abi Jaber–Neuman, Abi Jaber–Neuman–Tuschmann, Abi Jaber–De Carvalho–Pham) use finite horizon with terminal inventory constraints. The whole-line stationary regime should be positioned as the ergodic complement of these finite-horizon results.

(iii) **How does the "interior asymptotic far from boundaries" framing fit with the classical airfoil boundary-layer treatment?** In the Söhngen–Tricomi inversion of the finite-interval power-law-propagator problem, the optimal control decomposes as (Söhngen weight $(t(T-t))^{(\beta-1)/2}$) $\times$ (regular signal-driven part). The first factor is a pure boundary phenomenon: it blows up at $0$ and $T$ and encodes the endpoint block trades of the Obizhaeva–Wang / Alfonsi–Fruth–Schied solution. The second factor is what a whole-line stationary formulation directly computes. As $T\to\infty$, on compact subsets $t\in[a,T-a]$ the weight is $O(1)$ and the regular part converges to the translation-invariant solution of the *whole-line* singular integral equation; this is the interior asymptotic. The stationary / whole-line formulation is therefore the natural setting to isolate the signal-tracking content of the strategy from the terminal-condition transients, rather than an unrelated modelling choice.

## Sources

- Kept:
  - Bertsimas & Lo 1998, doi:10.1016/S1386-4181(97)00012-8 — origin of DP execution.
  - Almgren & Chriss 2000, doi:10.21314/JOR.2001.041 — canonical quadratic-cost model.
  - Obizhaeva & Wang 2013, *J. Financial Markets* 16(1) — block LOB, exponential resilience.
  - Alfonsi–Fruth–Schied 2010, arXiv:0708.1756 — general shape LOB.
  - Gatheral 2010, doi:10.1080/14697680903373692 — no-arbitrage for propagator.
  - Gatheral–Schied–Slynko 2012, doi:10.1111/j.1467-9965.2011.00478.x — Fredholm form.
  - Bouchaud–Gefen–Potters–Wyart 2004, arXiv:cond-mat/0307332 — empirical propagator.
  - Lillo–Farmer–Mantegna 2003, Nature 421:129 — master curve, $\sqrt Q$.
  - Almgren–Thum–Hauptmann–Li 2005, *Risk* 18 — direct estimation, $Q^{0.5}$ perm., rate$^{0.6}$ temp.
  - Tóth et al. 2011, arXiv:1105.1694 — anomalous impact / latent-book theory.
  - Bouchaud–Bonart–Donier–Gould 2018, CUP — textbook consensus.
  - Gârleanu & Pedersen 2013, *J. Finance* 68 — stationary signal-adaptive quadratic-cost (temp. only), key comparator.
  - Guasoni & Weber 2020, doi:10.1111/mafi.12234 — nonlinear power impact, long-run.
  - Brokmann–Itkin–Muhle-Karbe–Schmidt 2024, doi:10.1111/mafi.12449 — linear strategies for nonlinear impact.
  - Neuman & Voß 2022, arXiv:2002.09549 — signal + temp + exp transient, FBSDE.
  - Abi Jaber & Neuman 2025, arXiv:2211.00447 — general propagator resolvent.
  - Abi Jaber–Neuman–Tuschmann 2024, arXiv:2403.10273 — cross-impact.
  - Abi Jaber–De Carvalho–Pham 2024, arXiv:2409.12098 — constraints, battery.
  - Forde–Sánchez-Betancourt–Smith 2022, doi:10.1080/14697688.2021.1950919 — Söhngen–Tricomi with signal.
  - Tricomi 1957, *Integral Equations*, Interscience — airfoil inversion.
  - Muhle-Karbe–Wang–Webster 2024, SSRN 4286108 — stochastic-liquidity proxy for concavity.
  - Kallsen & Muhle-Karbe 2017, arXiv:1303.3148 — long-run proportional costs (context).
  - Guasoni & Weber 2017, doi:10.1111/mafi.12099 — dynamic trading volume (context).

- Dropped:
  - Cartea–Jaimungal market-making papers (2018 order-book signals; 2020 alpha signals) — market-making, not execution primitive.
  - Dolinsky arXiv:2411.10726 (2024, monotone strategies infinite-horizon) — narrow, no signal, no transient.
  - Jusselin–Rosenbaum 2020 concavity explanation — tangential to modelling choice question.
  - Sohngen 1939 primary reference — cited via Tricomi 1957.

## Gaps

- Have not directly verified whether any 2023–2025 preprint sets up a *stationary* whole-line signal-adaptive execution with transient impact; the closest known works (Gârleanu–Pedersen; Abi Jaber–De Carvalho–Pham battery-storage) are either without transient kernel or still finite-horizon. A targeted arXiv search on "stationary" + "propagator" + "signal" would firm this claim.
- The precise asymptotic statement "regular part of the Söhngen solution converges to whole-line solution as $T\to\infty$ uniformly on compacts" is stated here as a natural consequence of the Tricomi inversion but not sourced to a specific reference; if needed, a citation to Tricomi 1957 Ch. 4 or Söhngen's 1939 original will suffice, or the paper being reviewed should prove it directly.
- Suggested next steps: (i) alpha-CLI pull of Abi Jaber–Neuman 2025 §2 to confirm the finite-horizon set-up and terminal-inventory constraint; (ii) check Bank–Voß / Bank–Soner–Voß papers on singular control with transient impact for any stationary variant; (iii) confirm Gârleanu–Pedersen 2013 uses only temporary impact — the standard reading.
