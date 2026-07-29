# Evidence Log — Solution methods for optimal trading with impact

Object: `v2/optimal-trading-filters-v2.tex`. Question: does it accurately represent existing solution methods; are any missing?

## A. Method-family taxonomy (source-backed)

| Family | Representative works | Solution object | Source |
|---|---|---|---|
| Deterministic calculus of variations → Fredholm 2nd kind | Almgren–Chriss 2001; Gatheral–Schied–Slynko 2012 | Fredholm integral equation of the 2nd kind (via non-classical CoV) | GSS SSRN 1531466 / Math Finance 22:445 ; "Optimal Execution with Transient Impact" SSRN 2183685 |
| Stochastic control / HJB / DP (LQ) | Cartea–Jaimungal 2013; Gârleanu–Pedersen 2013/2016 | HJB value function; LQ closed form (aim portfolio) | NV 2002.09549 ("among the first were Cartea & Jaimungal"); GP JoF 10.1111/jofi.12080 |
| FBSDE / stochastic maximum principle / convex-analytic | Neuman–Voß 2022; Bank–Soner–Voß 2017; Lehalle–Neuman 2019 | System of coupled forward–backward SDEs | NV 2002.09549 ("system of four coupled forward-backward SDEs … probabilistic and convex analytic approach") |
| Infinite-dim stochastic control → free-boundary BSDE + operator Riccati | Abi Jaber–Neuman 2022/2025 | free-boundary L²-valued BSDE + operator-valued Riccati equation | AJN arXiv 2211.00447v2 abstract |
| Variational → **stochastic Fredholm** equation (+ constraints via multipliers) | Abi Jaber–De Carvalho–Pham 2024; nonlinear: Fredholm-approach 2025 | linear stochastic Fredholm equation; Lagrange multipliers + conditional expectations | arXiv 2409.12098 abstract; 2503.04323 |
| Operator resolvent | Abi Jaber–Neuman–Tuschmann (cross-impact) | explicit via operator resolvents | mafi.70025 / SSRN 4759758 abstract |
| Wiener chaos / Fredholm on chaos | Forde–Sánchez-Betancourt–Smith 2022 | stochastic Fredholm solved on Wiener chaos | (paper cite; consistent with Fredholm family) |
| Wiener–Hopf / spectral factorization | **this paper**; econ precedent: Hansen–Sargent, Whiteman | causal factorization + causal projection (closed-form filter) | MaRDI "Spectral utility, Wiener-Hopf techniques, and rational expectations" Q1109666 |
| Signature / rough-path (approximate) | Kalsi–Lyons–Perez Arribas 2020; Futter–Horvath–Wiese "Signature Trading" 2023 | linear functional on the path signature | arXiv 1905.00728; 2308.15135 |
| RL / deep-learning numerical | deep-signature FBSDE; Signature-Q-Learning | learned policy / neural FBSDE solver | aimsciences 10.3934/naco.2022028; GH phaelicks |

## B. Verification of the paper's specific attributions

- **GSS = deterministic/Fredholm** — CONFIRMED. "Fredholm integral equation of the second kind" via calculus of variations. [SSRN 1531466; SSRN 2183685]
- **GP = LQ/DP closed-form aim** — CONFIRMED. "closed-form optimal dynamic portfolio policy … aim portfolio." [10.1111/jofi.12080]
- **NV/BSV/LN = FBSDE / signal-adaptive** — CONFIRMED. NV: "system of four coupled forward-backward SDEs … probabilistic and convex analytic approach." [2002.09549]
- **AJNT = operator resolvent** — CONFIRMED. "solve … explicitly in terms of operator resolvents." [mafi.70025]
- **AJN = "linear stochastic Volterra equation of the second kind"** (paper §1.4) — NOT SUPPORTED by AJN's abstract. AJN characterize the value function via a "free-boundary L²-valued backward stochastic differential equation and an operator-valued Riccati equation." AJN call the *propagator* "Volterra-type"; the *equation* the control solves is (in the variational form of the school) a stochastic **Fredholm** equation, not Volterra. [AJN 2211.00447v2 abstract; AJ–DC–Pham 2409.12098 "linear stochastic Fredholm equation"]

## C. Missing references / methods (relative to the paper's bib)

Paper bib (v2/optimal-trading-filters.bib) cites: Markowitz, Merton, Rockafellar–Wets, GP×2, Almgren–Chriss, Obizhaeva–Wang, Bouchaud+, Gatheral, Lillo+, Jusselin–Rosenbaum, GSS, Lehalle–Neuman, Neuman–Voß, Bank–Soner–Voß, Abi Jaber–Neuman, Abi Jaber–Neuman–Tuschmann, Forde+, Wiener–Hopf, Wiener, Whittle, Gohberg–Krein, Arveson, Samko+, Noble, Krein, Lions–Magenes, Chakrabarti–George, Alfonsi–Schied–Slynko.

NOT cited:
1. **Abi Jaber, De Carvalho, Pham (2024), "Trading with propagators and constraints"** [arXiv 2409.12098, Sep 2024]. General propagator + **linear functional constraints via Lagrange multipliers and their conditional expectations**, solved as a stochastic Fredholm equation; constraint examples include no-shorting, no-buying, stochastic stop-trading. **Directly parallels the paper's §4** (α^eff = α + Σ ξ_k ψ_k; terminal x_T=0; multipliers with vanishing optional projection). Strongest missing-citation finding.
2. **Cartea & Jaimungal** — signal-in-execution originators. NV credit them as "among the first … to account for a Markovian signal in an optimal execution problem" (Almgren–Chriss impact) [NV pdf]. LN cite the framework as *Modeling Asset Prices for Algorithmic and High Frequency Trading*, Appl. Math. Finance 20(6):512–547 (2013). A closer execution paper is *Incorporating Order-Flow into Optimal Execution* (Math. Financial Econ., 2016). CORRECTION (reviewer W2): my earlier invented title "Optimal execution with Markovian signal" was wrong; AMF 20:512–547 = "Modeling Asset Prices…". Exact CJ ref (2013 vs 2016) to confirm against NV bib. Uncited by the paper. Sources: https://ideas.repec.org/a/taf/apmtfi/v20y2013i6p512-547.html ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2557457 (2016 order-flow).
3. **Signature methods** — Kalsi–Lyons–Perez Arribas (2020) "Optimal Execution with Rough Path Signatures" [1905.00728]; "Signature Trading" [2308.15135]. Distinct solution paradigm (linear functionals on signatures) for execution with signals. Not mentioned.
4. **Frequency-domain LQ / Wiener–Hopf in economics** — Hansen–Sargent, Whiteman ("Spectral utility, Wiener-Hopf techniques, and rational expectations"). Precedent for using Wiener–Hopf/spectral factorization to solve LQ dynamic-optimization in the frequency domain. Relevant methodological ancestor; uncited.
5. (Boundary / out of scope) RL / deep-BSDE numerical solvers; Cartea et al. stochastic-price-impact (SIAM 2023, 21m1394473); self-exciting/Hawkes order-flow execution.

## D. Notes on scope
- Paper scope = LQ, temporary + transient (propagator) + inventory risk, predictive signal, closed-form. Signature/RL/nonlinear-Fredholm are outside the closed-form/stationary scope but are genuine alternative solution methods → belong in a one-line boundary statement, not necessarily full treatment.
- The paper's *abstract-level* claim ("integral equation or an equivalent forward–backward system") is accurate and covers Fredholm (GSS/AJ–DC–Pham/Forde), infinite-dim-control-BSDE (AJN), and FBSDE (NV/BSV/LN). The imprecision is localized to §1.4's "Volterra equation of the second kind" for AJN.

## E. Sources consulted (URLs)
- GSS: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1531466 ; https://doi.org/10.1111/j.1467-9965.2011.00478.x
- Optimal Execution with Transient Impact: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2183685
- GP: https://doi.org/10.1111/jofi.12080
- NV: https://arxiv.org/abs/2002.09549
- LN: https://link.springer.com/content/pdf/10.1007/s00780-019-00382-7.pdf ; https://ar5iv.labs.arxiv.org/html/1704.00847
- AJN: https://arxiv.org/abs/2211.00447 (v2 abstract)
- AJNT: https://doi.org/10.1111/mafi.70025 ; https://doi.org/10.2139/ssrn.4759758
- AJ–DC–Pham: https://arxiv.org/abs/2409.12098
- Nonlinear Fredholm: https://arxiv.org/html/2503.04323
- Cartea–Jaimungal (via NV): https://ar5iv.labs.arxiv.org/html/2002.09549
- Signatures: https://arxiv.org/pdf/1905.00728 ; https://ar5iv.labs.arxiv.org/html/2308.15135
- Wiener–Hopf frequency-domain LQ (econ): https://portal.mardi4nfdi.de/wiki/Item:Q1109666
- Optimal Execution review (survey): https://portal.mardi4nfdi.de/wiki/Optimal_Execution:_A_Review
- Politecnico thesis flagging existence gap in AJ et al. 2024: https://www.politesi.polimi.it/retrieve/fdda7e71-eb23-407c-8701-ba300c16f73d/tesi_formato.pdf
