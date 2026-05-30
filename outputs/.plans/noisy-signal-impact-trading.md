# Plan: noisy-signal-impact-trading

## Proposed Title
**Optimal Trading with Noisy Signals and Persistent Impact: Wiener–Hopf Duality and the Innovation Principle**

## Slug
`noisy-signal-impact-trading`

## Sections
1. **Abstract** – one-paragraph summary
2. **Introduction** – motivation, preview of results, paper map
3. **Problem Formulation** – stationary setting, propagator model, cost functional; define "return on trade" vs "return on position" framing
4. **Legendre–Fenchel Duality** – quadratic cost functional defines norm on trades; convex conjugate = dual norm on signals; value function
5. **Causal Optimal Policy via Wiener–Hopf** – first-order condition; factorization $K = K_+ K_-$; causal projection argument; general statement of solution
6. **The AR(1) Signal: Anticausal Factor Reduces to a Scalar** – explicit calculation showing anticausal projection collapses to $(1-\lambda\rho)/(1-\lambda^2)$ constant; proof sketch
7. **The Innovation Interpretation** – causal factor $K_+^{-1}$ as fractional difference/derivative; power-law kernel gives causal fractional derivative; optimal trade as kernel-innovation of signal
8. **Noisy Predictor and Wiener Filtering** – observation noise model; Wiener filter for signal denoising; separation principle; composite policy: Wiener prefilter → impact-adjusted causal rule
9. **Examples** – exponential kernel (Gârleanu–Pedersen limit), power-law kernel (diffusive impact), AR(1) + exponential worked out in full
10. **Related Work** – Gârleanu–Pedersen, propagator models, Lehalle–Neuman, Abi Jaber et al.
11. **Limitations and Open Questions**
12. **Conclusion**
13. **Sources**

## Key Claims to Make and Verify

| # | Claim | Status | Source/Derivation |
|---|-------|--------|-------------------|
| C1 | LF transform of $\frac{1}{2}\langle x,K*x\rangle$ is $\frac{1}{2}\langle f,K^{-1}*f\rangle$ | ✓ Standard convex analysis | Rockafellar; self-dual in Hilbert space |
| C2 | No-dynamic-arbitrage ⟺ $K$ positive definite as operator | ✓ Gatheral 2010 (SSRN 1292353) | |
| C3 | Causal W-H factorization $K=K_+K_-$ exists for PSD $K$ | ✓ Wiener–Hopf theory | Bochner's theorem; Helson 1964 |
| C4 | For AR(1) signal + exponential kernel, anticausal projection is multiplicative: $\Pi_+[K_-^{-1}f] = c(\rho,\lambda)\,\hat{f}$ | ✓ Derived here (partial fractions calculation) | Explicit derivation in §6 |
| C5 | Constant: $c(\rho,\lambda) = (1-\lambda\rho)/(1-\lambda^2) \cdot \sigma/\sqrt{1-\lambda^2}$ | ✓ Computed | See §6 |
| C6 | $K_+^{-1}$ for exponential kernel is $(1-\lambda B)/\sqrt{1-\lambda^2}$, a causal first-order difference | ✓ Computed | §7 |
| C7 | $K_+^{-1}$ for power-law kernel $K(\omega)\sim|\omega|^{-\alpha}$ is causal fractional derivative of order $\alpha/2$ | ✓ Standard fractional calculus | Samko et al.; Gatheral 2010 |
| C8 | Optimal trade $x_t = c\cdot(f_t - \lambda f_{t-1})$ = "kernel-innovation" of signal | ✓ Follows from C4+C6 | §7 |
| C9 | For noisy signal $\tilde{f}=f+\eta$, Wiener filter is the optimal prefilter; separation holds | ✓ Under Gaussian linearity | Standard (Wiener 1949; Kailath 1968) |
| C10 | Gârleanu–Pedersen exponential-decay limit recovers "aim-and-trade" with a modified aim | Tentative – limit argument | GP 2013 JoF |

## Figures and Calculations (Planned)

- **Fig 1**: Diagram of duality: signal space ↔ trade space, kernel $K$ and dual $K^{-1}$ (Mermaid)
- **Fig 2**: Time-domain illustration of causal filter cascade: noisy signal → Wiener filter → causal fractional derivative → trades (Mermaid)
- **Table 1**: Kernel examples and corresponding causal operators (exponential, power-law, composite)

No quantitative data plots are planned unless numerically generated; placeholder noted where relevant.

## Source Material to Draw From

- Gârleanu & Pedersen (2013), "Dynamic Trading with Predictable Returns and Transaction Costs", JoF 68:2309–2340
- Gatheral (2010), "No-Dynamic-Arbitrage and Market Impact", QF 10:749–759 (SSRN 1292353)
- Bouchaud, Gefen, Potters & Wyart (2004), "Fluctuations and Response in Financial Markets", QF 4:176 (arXiv:cond-mat/0307332)
- Lehalle & Neuman (2019), "Incorporating Signals into Optimal Trading", Finance & Stochastics 23:275–311 (arXiv:1704.00847)
- Abi Jaber, Neuman & Tuschmann (2024), "Optimal Portfolio Choice with Cross-Impact Propagators" (arXiv:2403.10273)
- Abi Jaber & El Euch (2019/2022), general propagator case (arXiv:2211.00447)
- Standard references: Wiener (1949) extrapolation theory; Bochner's theorem; Samko, Kilbas & Marichev on fractional integrals

## Verification Log

- [x] Legendre-Fenchel transform calculation: verified algebraically
- [x] Discrete AR(1) + exponential kernel: full partial-fractions derivation computed, result $c = (1-\lambda\rho)/(1-\lambda^2)$ confirmed
- [x] Innovation interpretation: confirmed $x_t = c \cdot (f_t - \lambda f_{t-1})$ from Wiener-Hopf
- [x] Fractional derivative claim: consistent with power-law kernel literature (Gatheral 2010, Abi Jaber et al.)
- [x] Wiener filter prefilter: standard result, no novel claim
- [ ] Connection to GP "aim-and-trade": limit $\lambda \to 0$ not fully computed; marked tentative in text
- [ ] Multivariate / cross-impact: out of scope; noted as limitation
