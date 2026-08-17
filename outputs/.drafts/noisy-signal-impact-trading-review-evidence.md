# Evidence Notes — Review of `noisy-signal-impact-trading`

## Artifact inspected

- **Primary artifact:** `papers/noisy-signal-impact-trading.md`
- **Source type:** local Markdown research draft
- **Length:** 48,670 characters, 597 lines (`python` count)
- **Title:** “Optimal Trading with Noisy Signals and Persistent Impact: Wiener–Hopf Duality and the Innovation Principle”
- **No figures found.** One comparison table found at lines 481–489.

## Local sources and commands inspected

- `papers/noisy-signal-impact-trading.md` — read directly with line-number inspection.
- `experiments/markov_closure_check.py` — inspected script.
- `experiments/results/markov_closure_check.out` — inspected saved output.
- Ran: `python3 experiments/markov_closure_check.py | tee /tmp/noisy_signal_markov_review_run.out`
- Ran alpha CLI through bash:
  - `alpha get 1704.00847`
  - `alpha get 2211.00447`
  - `alpha get 2403.10273`
- Fetched external sources with `fetch_content` response id `mpu86fv57atczh`:
  - `https://docs.lhpedersen.com/DynamicTrading.pdf`
  - `https://arxiv.org/abs/1704.00847`
  - `https://arxiv.org/abs/2211.00447`
  - `https://arxiv.org/abs/2403.10273`
  - `https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26`
- Subagents used:
  - `researcher` for literature/novelty review.
  - `reviewer` for mathematical/reproducibility review.

## Claimed contributions and positioning observed in artifact

- Draft status note says: “First complete draft” and “All derivations are original unless cited. Claims marked tentative have not been cross-checked against the full literature.”
- Abstract claims:
  - Stationary optimal trading with noisy predictor and persistent/transient impact kernel `K`.
  - Legendre–Fenchel dual norm interpretation.
  - Unconstrained solution solves `K*x=f`.
  - Causality handled by Wiener–Hopf factorization `K=K_+K_-`.
  - AR(1) signal + exponential impact reduces to scalar anticausal projection and first-order causal difference / “kernel innovation.”
  - Power-law kernels lead to causal fractional derivatives.
  - Additive observation noise yields a two-stage rule: Wiener denoise, then impact-adjusted causal rule.
- Related work section already narrows several claims: Section 4 solution is called “standard” (line 128); Section 9 identifies Lehalle–Neuman, Abi Jaber–Neuman, AJN–Tuschmann, and Forde/Sánchez-Betancourt et al. as close precedents.

## Key methods and equations observed

### Objective and stochastic filter formulation

- Lines 64–72 define a stationary causal filter `H` and objective:
  - `J(H)=E[f_t x_t] - 1/2 E[x_t (K*x)_t]`
  - spectral form: `∫ H S_f - 1/2 ∫ |H|^2 Khat S_f`.
- This is a stochastic filter optimization weighted by signal spectrum `S_f`.

### Legendre–Fenchel duality

- Lines 92–100 define the conjugate of `1/2 ||x||_K^2` as `1/2 ||f||_{K^{-1}}^2` with unconstrained optimizer `x*=K^{-1}*f`.
- This is mathematically standard for strictly positive quadratic forms, but the text should separate deterministic sequence-space duality from stochastic per-period filter optimization.

### Causal Wiener–Hopf derivation

- Lines 116–126 state projection FOC `[K*x-f]_+=0` and solution
  `xhat = K_+^{-1} [ fhat / K_- ]_+`.
- Evidence issue: this omits the `S_f` weighting that appears in objective (1), unless `[·]_+` is explicitly interpreted as projection in the closed past of the signal rather than ordinary Laurent truncation. Later Section 5.5 moves toward conditional-expectation projection, which partly repairs the interpretation.

### AR(1) × exponential kernel

- Lines 151–157 set `f_t=rho f_{t-1}+eps_t`, `K(n)=lambda^{|n|}`, and factors:
  - `K_+=(sqrt(1-lambda^2))/(1-lambda z^{-1})`
  - `K_-=(sqrt(1-lambda^2))/(1-lambda z)`.
- Lines 163–192 derive scalar collapse:
  - `[ fhat/K_- ]_+ = ((1-lambda rho)/sqrt(1-lambda^2)) fhat`.
- Lines 198–204 give clean-signal policy:
  - `x_t = ((1-lambda rho)/(1-lambda^2))(f_t - lambda f_{t-1})`.
- Algebra check: `K(z)H(z)= (1-lambda*rho)/(1-lambda*z)`. For the stochastic AR(1) FOC, `S_f(z)(1-KH)` simplifies to a purely anticausal term proportional to `z/((1-lambda z)(1-rho z))`, supporting the AR(1) policy under the weighted projection interpretation.
- Notation issue: line 152 writes `fhat(z)=sigma/(1-rho z^{-1})`; this is the innovations-to-signal transfer function, not the z-transform of a realized stationary path.

### Markov closure

- Lines 221–274 derive `[K_-^{-1}f]_+(t)=E[(K_-^{-1}*f)_t | F_t] = sum a_m E[f_{t+m}|F_t]` and for AR(1) collapses to `K_-^{-1}(rho) f_t`.
- This is the clearest justification of the scalar-collapse result and should be promoted earlier to reconcile the stochastic objective with the projection notation.

### Power-law / fractional derivative section

- Lines 302–318: `K(n)~|n|^{-beta}`, `Khat~C|omega|^{beta-1}`, `K_+^{-1}~(-i omega)^((1-beta)/2)`, so optimal trade is stated as proportional to a causal fractional derivative.
- Evidence issue: these are low-frequency/asymptotic statements (`~`) and the kernel is non-summable (line 314); the text at line 316 states “The optimal trade is therefore...” more strongly than the derivation supports.
- Lines 326–354 derive OU × power-law scalar `kappa^alpha`; line 354 says the integral identity on `alpha in (0,1)` is verified numerically in the script.
- Ran script output shows continuous-time numerical ratios:
  - alpha 0.1: ratio 0.70408
  - alpha 0.25: ratio 0.95411
  - alpha 0.5: ratio 0.99821
  - alpha 0.75: ratio 0.99733
  - alpha 0.9: ratio 0.90539
  This is a useful sanity check but not a numerical verification over `(0,1)`, especially near endpoints.
- Lines 361–374: discrete fractional differencing check claims seven-decimal agreement on a grid. The script output supports the displayed grid values for alpha `{0.25,0.5,0.75}` and rho `{0.3,0.7,0.95}`.

### Noisy predictor and separation

- Lines 393–425 give additive-noise model, causal Wiener filter, non-causal Wiener ratio, and separation proposition.
- Claim is plausible as a classical linear-Gaussian/LQG certainty-equivalence result, but novelty should be stated as application/composition in this stationary propagator setting rather than as a new separation principle.
- Lines 455–467 correctly warn that the filtered signal is ARMA(1,1), so the AR(1) scalar collapse does not directly apply; however, the heading “full solution” at line 447 is too strong because the noisy closed form is deferred to future work.

## Reported metrics and reproducibility facts

- No empirical performance metrics are reported for the proposed trading policy.
- Limitations section line 523 explicitly says all results are theoretical and proposes a future simulation.
- Reproducible local code exists for narrow mathematical sanity checks only:
  - `experiments/markov_closure_check.py`
  - `experiments/results/markov_closure_check.out`
- No code/notebook was found for:
  - simulation of AR(1) + exponential impact policy performance,
  - Sharpe or PnL comparisons against `x_t=f_t`,
  - exact noisy AR(1) closed form,
  - table-entry generation.

## Figures and tables

- No figures found.
- Table 1 (lines 481–489) mixes exact, asymptotic, model-analogue, and ill-posed entries:
  - Exponential and white rows are exact under stated assumptions.
  - Power-law continuous OU row is asymptotic/scaling unless full operator normalization/domain is supplied.
  - Fractional differencing row is a discrete ARFIMA analogue, not the literal discrete power-law kernel.
  - Flat/permanent row is singular/ill-posed.

## External literature evidence inspected

### Gârleanu & Pedersen (2013), “Dynamic Trading with Predictable Returns and Transaction Costs”

- Source: `https://docs.lhpedersen.com/DynamicTrading.pdf`
- Fetched text states the transaction-cost specification is “sufficiently rich to allow for both purely transitory and persistent costs,” and Section IV is “Persistent Transaction Costs.”
- This conflicts with the draft’s line 495 characterization of GP13 as purely “quadratic instantaneous transaction costs (no transient impact).” GP is not the same Bouchaud/Gatheral convolutional propagator model, but the contrast should be softened.

### Lehalle & Neuman (2019), “Incorporating Signals into Optimal Trading,” arXiv:1704.00847

- Sources: `alpha get 1704.00847`; `https://arxiv.org/abs/1704.00847`
- Abstract says they incorporate a Markovian signal into the Gatheral–Schied–Slynko optimal trading framework and derive an explicit singular optimal strategy for OU signal plus exponentially decaying transient market impact.
- This is a direct precedent for signal + exponential transient impact; the draft should claim a stationary spectral analogue, not broad novelty.

### Abi Jaber & Neuman, “Optimal Liquidation with Signals: the General Propagator Case,” arXiv:2211.00447

- Sources: `alpha get 2211.00447`; `https://arxiv.org/abs/2211.00447`
- Abstract says they treat transient Volterra propagators, temporary price impact, progressively measurable price-predicting signals, operator-valued Riccati/BSDE, analytic solution, and implementability for singular kernels such as power laws.
- This heavily overlaps any broad “general propagator + signal” claim.

### Abi Jaber, Neuman & Tuschmann, “Optimal Portfolio Choice with Cross-Impact Propagators,” arXiv:2403.10273

- Sources: `alpha get 2403.10273`; `https://arxiv.org/abs/2403.10273`
- Abstract says they solve continuous-time portfolio choice with matrix-valued Volterra cross-impact, temporary impact, progressively measurable alpha signals, operator resolvents, stochastic Fredholm equations, and alpha-decay effects.
- This supports narrowing novelty to scalar stationary convolution/Wiener–Hopf exposition and AR(1) collapse.

### Forde/Sánchez-Betancourt et al., “Optimal trade execution for Gaussian signals with power-law resilience”

- Source: `https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26`
- ORA abstract says they characterize signal-adaptive liquidation under power-law resilience and Gaussian signals including OU/fBm, with Fredholm equations “solved in terms of fractional derivatives.”
- This is a very close precedent to the draft’s power-law/fractional-derivative claim.

## Subagent evidence summary

- `researcher` found strongest novelty-safe framing: self-contained stationary convolution/filter derivation; AR(1)+exponential scalar collapse; noisy-observation composition. It warned against broad novelty claims for propagators, signals, Fredholm equations, power-law fractional derivatives, or separation principles.
- `reviewer` independently identified the main mathematical blocker: mismatch between the `S_f`-weighted stochastic objective and the unweighted deterministic projection FOC in Section 4. It also confirmed AR(1) algebra, the lack of figures, the one-table inventory, and reproducibility of the narrow script output.

## Open/blocked checks

- I did not do a full proof audit of the spectral factorization existence conditions for all kernels claimed.
- I did not search exhaustively for prior appearances of the exact AR(1) scalar-collapse formula under alternate notation in signal-processing literature.
- I did not run any trading simulation, because the artifact provides no simulation package for the main policy-performance claims and itself marks empirical validation as future work.
