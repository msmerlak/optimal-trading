# Review — Optimal Trading with Noisy Signals and Persistent Impact

**Artifact reviewed:** `papers/noisy-signal-impact-trading.md`  
**Source type:** local Markdown research draft  
**Review slug:** `noisy-signal-impact-trading`  
**Evidence notes:** `outputs/.drafts/noisy-signal-impact-trading-review-evidence.md`

## Summary Assessment

This is a clear and promising theoretical note with a useful pedagogical angle: it recasts stationary optimal trading with linear transient impact as a causal filtering/Wiener–Hopf problem and gives an intuitive AR(1) × exponential-kernel “kernel innovation” rule. The strongest contribution is the explicit scalar-collapse explanation for Markov signals, especially the conditional-expectation view in §5.5. The noisy-signal composition is also useful, but it is best framed as a classical Wiener/LQG separation result applied to this stationary execution filter.

The draft is **not ready as a research submission without major revision**. The main technical problem is that the stochastic objective in §2.3 is an `S_f`-weighted causal-filter optimization, while §4 states an unweighted deterministic projection FOC `[K*x-f]_+=0`. The AR(1) closed form appears algebraically sound under the correct weighted/conditional-projection interpretation, but the general derivation needs to be made internally consistent. The novelty claims also need narrowing because signals with transient propagator impact, OU/exponential cases, general Volterra propagators, and power-law/fractional-derivative execution already have close precedents.

**Recommendation:** **Major revision / weak reject if submitted as-is.** I would encourage revision rather than abandonment: the note can become a strong expository/theoretical contribution if it (i) fixes the projection-space formulation, (ii) narrows novelty, (iii) labels power-law results as asymptotic or supplies full operator conditions, and (iv) adds at least a minimal simulation for the AR(1) rule.

## Strengths

1. **Readable, self-contained derivation path.** The draft is unusually accessible for Wiener–Hopf/propagator execution material and explains the cost norm / dual norm idea clearly.
2. **Strong AR(1) × exponential worked example.** Equations (7)–(12) are transparent, and the final rule
   \[
   x_t=\frac{1-\lambda\rho}{1-\lambda^2}(f_t-\lambda f_{t-1})
   \]
   is a compact result with useful interpretation.
3. **Good Markov-closure intuition.** Section 5.5 is the most convincing part of the note: it explains scalar collapse as conditional expectation of an anticausal future integral, rather than just partial-fraction algebra.
4. **Honest limitations section.** The draft explicitly acknowledges scalar/single-asset scope, stationarity, lack of risk aversion, Gaussianity, and missing empirical validation.
5. **Some reproducibility support.** The local script `experiments/markov_closure_check.py` is runnable and supports the discrete fractional-difference grid checks. I ran it and reproduced the saved output pattern.

## Critical Issues

### C1. The causal first-order condition is inconsistent with the stated stochastic objective

- **Where:** §2.3, lines 64–72; §4.1, lines 116–126.
- **Issue:** The paper first optimizes over causal filters `H` with objective
  \[
  \mathcal J(H)=\int H(\omega)S_f(\omega)\,d\omega-\frac12\int |H(\omega)|^2\hat K(\omega)S_f(\omega)\,d\omega.
  \]
  For this problem, causal variations give an orthogonality/projection condition in an `S_f`-weighted prediction space. But §4 writes the deterministic/pathwise condition
  \[
  [K*x-f]_+=0
  \]
  and the unweighted Wiener–Hopf inverse formula as if ordinary Laurent truncation sufficed.
- **Why it matters:** This is not just notation. If the optimization variable is a causal filter applied to a stochastic signal, the signal spectrum affects the causal projection. The draft later uses conditional expectation in §5.5, which is closer to the right formulation, but this needs to be the governing definition from the start.
- **Suggested fix:** Rewrite §4 in one of two consistent ways:
  1. **Stochastic filtering formulation:** define `[·]_+` as orthogonal projection onto the closed linear span of the signal past under the stationary inner product, and carry the signal spectral factor explicitly; or
  2. **Deterministic sequence formulation:** first solve a pathwise deterministic causal inverse problem for a fixed `f`, then separately prove that the proposed filter is optimal for the stochastic AR(1) objective.

### C2. The paper overstates the exactness of the power-law/fractional-derivative result

- **Where:** §6.2–§6.3, especially lines 302–318 and 326–354.
- **Issue:** The derivation uses low-frequency asymptotics (`~`) for a non-summable power-law kernel and then states “The optimal trade is therefore...” a causal fractional derivative. This reads as an exact policy, but the presented argument only supports a scaling/asymptotic statement unless full spectral factorization, constants, domains, and regularization are supplied.
- **Why it matters:** The power-law/fractional-derivative connection is a central claim and also close to existing work on power-law resilience and Gaussian signals. If the paper presents an asymptotic stationary heuristic as an exact theorem, reviewers will object.
- **Suggested fix:** Label the result as “low-frequency/asymptotic stationary scaling” or add a theorem with precise kernel class, factorization normalization, function space, and proof.

### C3. Novelty is too broad relative to close prior work

- **Where:** Abstract, §1, §4.1 line 128, §9.
- **Issue:** The draft is already careful in places, but it still risks implying novelty for general “signals + transient impact + Wiener/Fredholm/operator” structure. Several close precedents exist:
  - Lehalle & Neuman incorporate Markovian signals into transient-impact optimal trading and derive an OU + exponential-resilience strategy.
  - Abi Jaber & Neuman treat general Volterra propagators with progressively measurable signals and power-law kernels.
  - Abi Jaber, Neuman & Tuschmann solve cross-impact propagator portfolio choice with alpha signals via stochastic Fredholm equations/operator resolvents.
  - Forde/Sánchez-Betancourt et al. treat Gaussian signals with power-law resilience and fractional-derivative solutions.
- **Suggested novelty statement:** “We give a self-contained stationary scalar convolution/filter derivation; in the AR(1)+exponential case, the anticausal Wiener–Hopf projection collapses to an explicit scalar, yielding a kernel-innovation rule; additive observation noise composes classical causal Wiener filtering with this execution filter.”

## Major Issues

### M1. `\hat f(z)=\sigma/(1-\rho z^{-1})` is misleading for a stationary AR(1) path

- **Where:** §5.1, line 152.
- **Issue:** This is the transfer function from innovations to the AR(1) signal, not the z-transform of a realized stationary signal. The partial-fraction calculation is valid as a filter/projection calculation, but the notation invites a deterministic-transform misreading.
- **Fix:** Say explicitly: “We use the innovations representation; formally `f = A ε` with transfer `A(z)=...`. The projection calculation is in the closed linear span of innovations/signal history.”

### M2. “Kernel innovation” should not be called the statistical innovation of `f` unless `λ=ρ`

- **Where:** §6.1, line 292.
- **Issue:** The draft says `f_t-λf_{t-1}` is “precisely the one-step-ahead innovation of `f` in the AR(1) model with parameter `λ`.” But the actual AR(1) signal innovation is `f_t-ρf_{t-1}`. The draft’s expression is a kernel-whitened/backward-differenced signal.
- **Fix:** Replace with “the one-step residual under a reference AR(1) parameter equal to the kernel decay `λ`” or simply “the kernel-whitened causal difference.”

### M3. The noisy AR(1) example is titled “full solution” but does not give the full noisy solution

- **Where:** §8.1, lines 447–467.
- **Issue:** The section correctly notes that the filtered signal is ARMA(1,1), that scalar collapse does not apply, and that the exact closed form is future work. That is not a “full solution.”
- **Fix:** Rename to “Clean-signal full solution and noisy-signal operator form,” or complete the ARMA partial-fraction closed form.

### M4. Continuous-time numerical “verification” is overstated

- **Where:** §6.3, line 354; `experiments/markov_closure_check.py`; `experiments/results/markov_closure_check.out`.
- **Observed run output:** ratios for the continuous integral identity were approximately 0.70408 at `α=0.1`, 0.95411 at `α=0.25`, 0.99821 at `α=0.5`, 0.99733 at `α=0.75`, and 0.90539 at `α=0.9`.
- **Issue:** This is a sanity check, not numerical verification over `α∈(0,1)`, especially near endpoints.
- **Fix:** Say “sanity-checked numerically at selected mid-range values; endpoint quadrature is crude.” If keeping a verification claim, use adaptive quadrature and record tolerances.

### M5. Table 1 mixes exact, asymptotic, analogue, and singular rows

- **Where:** §8.3, lines 481–489.
- **Issue:** The exponential and temporary rows are exact under the model. The power-law row is asymptotic/scaling; the fractional-differencing row is a discrete analogue rather than the literal discrete power-law kernel; the flat/permanent row is singular.
- **Fix:** Add a “status” column: `exact`, `asymptotic`, `model analogue`, `singular/regularized`.

### M6. Related-work comparison to Gârleanu–Pedersen is too sharp

- **Where:** §9, line 495.
- **Issue:** The draft describes GP13 as “quadratic instantaneous transaction costs (no transient impact).” The GP paper explicitly says its cost specification allows both transitory and persistent costs and contains a Section IV on persistent transaction costs. GP is not the same as a Bouchaud/Gatheral symmetric convolution propagator, but the draft’s contrast is inaccurate.
- **Fix:** Soften to: “GP13 uses a dynamic portfolio model with quadratic transaction costs and also treats persistent price distortions, but not the same stationary symmetric propagator convolution problem studied here.”

## Minor Issues

1. **Positive-definiteness/no-dynamic-arbitrage wording is too compressed.** Lines 74–76 should say this is the relevant condition in the linearized symmetric quadratic-cost submodel, not the full generality of Gatheral’s nonlinear market-impact framework.
2. **Equation (1) should mention reality/conjugation conventions.** The linear term `∫ H S_f` is real under symmetry for real filters, but a reviewer may expect `Re` or conjugation conventions.
3. **Bochner / spectral factorization statement needs assumptions.** Line 132 says Bochner guarantees unique factorization. Strictly, outer factorization needs log-integrability and minimum-phase/normalization conditions; state them or cite a standard result.
4. **“Empirically relevant” is unsupported.** Line 147 calls AR(1)+exponential “empirically relevant,” but no calibration/data evidence is provided. Use “tractable and commonly used” unless evidence is added.
5. **Discrete literal power-law section is useful but unfinished.** §6.3 notes Lerch/polylog behavior but does not derive it; mark it explicitly as a conjectural/sketch paragraph or move to limitations.
6. **No empirical baselines.** The proposed benchmark `x_t=f_t` appears only as future work. A minimal simulation would materially improve the paper.
7. **Source key inconsistency.** The draft references `[AJN22; AJN24]` in limitations, while Sources list “Abi Jaber & Neuman (2022) [AN22]”; align keys.
8. **No figures, but table provenance should be explicit.** Since Table 1 is derivation-based, state which rows are proved in the paper and which are literature/asymptotic summaries.

## Reproducibility and Verification

**Verification performed:**

- Read the local draft `papers/noisy-signal-impact-trading.md` directly.
- Inspected and ran `experiments/markov_closure_check.py`.
- Inspected `experiments/results/markov_closure_check.out`.
- Used alpha CLI for arXiv sources `1704.00847`, `2211.00447`, and `2403.10273`.
- Fetched primary/source pages for GP13, Lehalle–Neuman, Abi Jaber–Neuman, AJN–Tuschmann, and Forde/Sánchez-Betancourt et al.
- Used `researcher` and `reviewer` subagents; their findings were consistent with the main issues above.

**What checks passed:**

- The partial-fraction algebra in §5.2–§5.4 is internally consistent.
- The final AR(1) × exponential policy satisfies the expected weighted projection structure when interpreted through AR(1) conditional prediction.
- The discrete fractional-difference grid check in the local script reproduces the displayed agreement for the tested `α,ρ` values.
- The draft’s claim of “no figures” is consistent with file inspection; one table exists.

**What remains unverified or blocked:**

- No full proof audit of spectral factorization/domain assumptions for the power-law kernel was performed.
- No exhaustive search was performed for the exact AR(1) scalar-collapse formula under alternate signal-processing notation.
- No empirical PnL/Sharpe simulation was run because the artifact does not provide a main-policy simulation package and itself marks empirical validation as future work.
- The continuous-time integral script is too crude near endpoints to support the current “verified on `α∈(0,1)`” wording.

## Inline Annotations

- **§2.3 / Eq. (1):** Define the Hilbert space and projection inner product. If `S_f` weights the objective, it must appear in the causal FOC or in the definition of `[·]_+`.
- **§2.4:** Replace “equivalent to absence of dynamic arbitrage” with “in this linear symmetric quadratic-cost setting, positive semidefiniteness is the no-profitable-round-trip condition.”
- **§4.1 / Eq. (4)–(6):** This is the central revision point. Re-derive with `S_f`, or explicitly switch to a deterministic problem and later prove stochastic optimality.
- **§5.1 / Eq. (7):** Clarify that `\hat f` is an innovations transfer function / formal spectral representation, not a realized path transform.
- **§5.5:** Promote this section earlier or refer to it before §4’s projection formula; it gives the right probabilistic interpretation.
- **§6.1:** Replace “one-step-ahead innovation of `f`” with “kernel-relative innovation” or “kernel-whitened difference.”
- **§6.2 / Eq. (13)–(15):** Add “low-frequency/asymptotic” in the theorem statement and table, unless exact conditions are supplied.
- **§6.3 / line 354:** Downgrade “verified” to “sanity-checked numerically,” or improve the quadrature.
- **§7.3 / Eq. (20):** Cite classical separation/certainty equivalence explicitly and frame novelty as the composition with the stationary execution filter.
- **§8.1 heading:** Rename because the noisy case is not fully solved.
- **Table 1:** Add exact/asymptotic/analogue/singular status labels.
- **§9 GP13 paragraph:** Correct the description of GP’s persistent transaction-cost extension.

## Recommendation

**Major revision required.** The paper has a strong expository core and a potentially valuable compact AR(1) result, but the present version would likely draw serious reviewer objections on mathematical formulation and novelty positioning. I would revise around the following priorities:

1. Fix the weighted stochastic projection/Wiener–Hopf derivation.
2. State a narrow, defensible contribution claim.
3. Recast power-law statements as asymptotic unless full operator details are provided.
4. Add a minimal simulation: AR(1) signal + exponential kernel, comparing policy (12) to `x_t=f_t` and perhaps a lagged/temporary-impact baseline across `λ,ρ`.
5. Clean up terminology and table status labels.

## Sources

- Local artifact: `papers/noisy-signal-impact-trading.md`
- Evidence notes: `outputs/.drafts/noisy-signal-impact-trading-review-evidence.md`
- Local experiment script: `experiments/markov_closure_check.py`
- Local experiment output: `experiments/results/markov_closure_check.out`
- Gârleanu & Pedersen (2013), “Dynamic Trading with Predictable Returns and Transaction Costs”: https://docs.lhpedersen.com/DynamicTrading.pdf
- Lehalle & Neuman (2019), “Incorporating Signals into Optimal Trading,” arXiv:1704.00847: https://arxiv.org/abs/1704.00847
- Abi Jaber & Neuman, “Optimal Liquidation with Signals: the General Propagator Case,” arXiv:2211.00447: https://arxiv.org/abs/2211.00447
- Abi Jaber, Neuman & Tuschmann, “Optimal Portfolio Choice with Cross-Impact Propagators,” arXiv:2403.10273: https://arxiv.org/abs/2403.10273
- Forde/Sánchez-Betancourt et al., “Optimal trade execution for Gaussian signals with power-law resilience”: https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26
- Bouchaud, Gefen, Potters & Wyart (2004), “Fluctuations and Response in Financial Markets,” arXiv:cond-mat/0307332: https://arxiv.org/abs/cond-mat/0307332
