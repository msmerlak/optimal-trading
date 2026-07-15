# PNAS Round 1 — Hostile-but-fair reviewer objections

**Target:** `papers/markowitz-of-cost-pnas.md`
**Role:** hostile PNAS reviewer (execution / stochastic-control camp).
**Not reviewed by me this pass:** prior round-1 subreviews (novelty, math, style) already exist in `reviews/`. I read `pnas-round1-novelty.md` for citation ground truth (arXiv:2512.12111 verified, FSS2022 correctly attributed) but treat the paper as a fresh submission.

---

## (a) Novelty-positioning blockers

### N1. Claim (iii) "closed-form bulk term where general-propagator theory offered only implicit resolvent representations" is overstated w.r.t. Abi Jaber–Neuman (ref [7]).

- The Abstract and §1.3(iii) frame the fractional-derivative formula (12) as filling a gap left by AJN 2025. The gap is real (AJN give an operator resolvent, not a closed form), but the *delta* is not made rigorous: there is no lemma showing (12) is the whole-line, stationary, scalar-power-law specialization of the AJN resolvent equation. A reviewer from the AJN camp will read this as sleight of hand — the resolvent equation in ref [7] can, in principle, be solved by Fourier methods on ℝ under stationarity, and the answer *must* be (12) or equivalent. The paper should explicitly derive (12) as a limit/specialization of AJN's Theorem (or state and prove that the two are equivalent under the stated hypotheses). Without this, "closed form where they had only resolvents" reads as marketing.
- **Suggested fix:** add a Remark or short section: "AJN Theorem X reduces to (12) when: (a) horizon is $\mathbb{R}$, (b) kernel is $c|t|^{-\gamma}$, (c) signal is stationary, (d) no temporary impact." One paragraph, no proofs beyond a Fourier identity.

### N2. Claim (ii) — the filtration Wiener–Hopf identity $(P_+CP_+)^{-1} = C_+^{-1}P_+ C_-^{-1}$ — is very close to classical Wiener–Kolmogorov prediction.

- The identity is Wiener 1949 (ref [13]) transferred to the adapted-process subspace. The paper says as much ("stochastic-processes analog of the deterministic Wiener–Hopf inversion, transferred to the adapted subspace via nest-algebra outer factorization (14, 15)"). But then §1.3 lists it as one of three delimiting contributions. A hostile reviewer will say: this is textbook causal realization / spectral factorization; nest-algebra outer factorization (Arveson '75, Davidson '88) is exactly this construction; and Krein '62 (ref [12]) covers half-line convolution inversion.
- Missing citations that sharpen the delta:
  - Kailath, *Lectures on Wiener and Kalman Filtering* — innovations representation of the causal Wiener filter is (P+CP+)^-1 P+ in prediction language.
  - Rozanov, *Stationary Random Processes* — spectral factorization on ℝ.
  - Hansen–Sargent time-series macro literature uses the same identity for stochastic optimal control with quadratic costs (though not for execution).
- **Suggested fix:** demote (ii) from "contribution" to "tool"; the paper's actual novelty is the *application* of this classical machinery to the propagator problem with adapted signal (which no one has done in this form) and the resulting fractional-derivative formula (iii).

### N3. Claim (iii) — fractional-derivative reduction — half-order Marchaud factorization is already in FSS2022 (ref [10]).

- Prior round-1 novelty audit (`reviews/pnas-round1-novelty.md`) confirms FSS2022 Theorem 2.2 contains $T = B^{-1}I_\nu B$ with $r=(1-\gamma)/2$ on bounded intervals. The paper credits this (§1.3(iii) "The half-order factorization was implicit in (10)"; §1.2 mentions FSS). The remaining novelty is:
  1. The whole-line stationary formulation with a *general adapted* signal (FSS restrict to Gaussian signals on a bounded interval).
  2. The forecast curve $\bar\alpha(s,\cdot)$ as the operated-on object.
  3. The reading of (12) as "$D_+^\beta$ acts on adapted whitened $\zeta_s$".
- This is genuine but incremental. The Abstract's phrasing "the optimal trading rate is a fractional derivative of the signal, of order set by the impact-decay exponent" would be read by Forde/Sánchez-Betancourt/Smith as claiming their result. The Significance Statement is worse.
- **Suggested fix:** the Sig Statement and Abstract must acknowledge FSS in one clause. The prior novelty review already flagged this; it is a real submission blocker. Example: "Extending the half-order Riemann–Liouville structure of Forde–Sánchez-Betancourt–Smith to a general adapted signal on the whole line, we show that…"

### N4. Neuman–Voß (ref [6]) is correctly bracketed as exponential-kernel only — no issue.

### N5. Missing prior art on stochastic quadratic-cost with convolution Hessian.

- Gârleanu–Pedersen 2013/2016 "Dynamic trading with predictable returns and transaction costs" solves a similar gain–cost problem with quadratic transaction costs and mean-reverting alpha, in closed form, and *is* known in the execution literature. Their cost is instantaneous (not transient), but the structural analogy — linear gain against quadratic cost of trading rate, adapted signal, closed-form linear operator on the forecast — is essentially the Markowitz correspondence the paper is claiming. It should be cited and distinguished (their Hessian is diagonal/local; ours is non-local convolution — that is the delta).
- Collin-Dufresne–Daniel–Sağlam "Liquidity regimes and optimal dynamic asset allocation" (2020, JFE) is another close cousin.

---

## (b) Exposition / scope objections a hostile reviewer would raise

### E1. The Markowitz analogy is formal, not structural. Reviewers will resist "Markowitz for cost".

- Markowitz penalizes *variance* (aleatory risk). This paper penalizes *cost* (a deterministic-in-schedule quadratic). Both are quadratic forms, but the semantic content is different. Table 1 papers this over.
- The whitening/factorization analogy is closer to **Wiener–Kolmogorov prediction** than to Markowitz. Prediction theory factorizes a spectral density into causal × anticausal halves; that is exactly $C = C_-C_+$. Markowitz factorization ($\Sigma = LL^\top$) has no causality structure — it is a *symmetric* factorization over an unordered index set. The paper's "Adapted Cholesky factorization" row in Table 1 conflates two different constructions.
- A hostile referee will ask: why not call this "Wiener–Kolmogorov prediction for cost-optimal execution"? The answer is that Markowitz is a stronger branding hook — but the reviewer will call the paper on it.
- **Response strategy for authors:** keep the Markowitz correspondence as an expository device (§3) but soften §1.1's "temporal counterpart of Markowitz" to "temporal counterpart of the mean–variance / Wiener-prediction quadratic optimum tradition". Or embrace the Wiener framing explicitly and reduce Markowitz to one paragraph.

### E2. §1.3(i) and §4.1 — inventory-as-signal reframing is under-justified.

- The claim: terminal-inventory constraint $\int u_t\,dt = -X_0$ contributes a constant $\lambda_1 \mathbf{1}_{[0,T]}$ to the effective signal via KKT, and $D_\pm^\beta \mathbf{1}_{[0,T]}$ produces the Söhngen–Tricomi modes.
- Problems a hostile reviewer will raise:
  1. **Ambient space mismatch.** The main theorem is on ℝ with stationary signal. A constant times $\mathbf{1}_{[0,T]}$ is *not* stationary, *not* in $L^2(\mathbb R)$, and injects a bounded-interval object into a whole-line theorem. §4.1 needs to either (a) restate the theorem on $[0,T]$, or (b) explicitly say "the following is heuristic / to be developed in a companion paper".
  2. **Well-posedness on $[0,T]$ is not proved.** FSS2022 does this. Cite them for it and say "with well-posedness inherited from [10]", or prove it.
  3. **Boundary regularity.** $(t(T-t))^{(\gamma-1)/2}$ is not in $L^2([0,T])$ for $\gamma < 1/2$? Actually it is (the singularity is integrable in $L^2$ iff $\gamma > 0$; check). But its rate-of-execution interpretation near endpoints is delicate. The paper says the modes are "$O(T^{\gamma-1})$ correction on interior regions" which is dimensionally suspicious — this depends on $|X_0|$ magnitude, not just $T$.
  4. **Choice of function space.** For finite $T$, the natural space is $L^2([0,T])$ with a Riesz-potential subspace; the paper never states this.
- §4.1 is trying to do too much in one paragraph. Either promote to a proposition with hypotheses and cite FSS for the finite-$T$ well-posedness, or explicitly demote to "heuristic sketch, to appear in [companion paper]".

### E3. §2.1 spectral-decay hypothesis $\int (1+|\xi|^{2(1-\gamma)+\epsilon})S_\alpha(\xi)\,d\xi < \infty$.

- Stated clearly and used correctly in the admissibility check at the end of §5. Good.
- But a reviewer will note this *excludes* the most interesting signals in practice: signals with rough / fractional-Brownian components (Hurst < 1/2) have spectral density blowing up at high frequency. This restricts the theorem to relatively smooth signals. The OU example (§2.7) satisfies it trivially. State this limitation.
- **Suggested fix:** add one sentence: "The hypothesis restricts to signals whose forecast curve lies in $H^{(1-\gamma)/2 + \epsilon/2}$; rough signals (fractional-noise driven, $H < 1/2$) may require distributional interpretation of $D_+^\beta$." Points forward, doesn't overpromise.

### E4. §2.7 OU example: correct but under-exploited.

- Formula (15) $u^{\star,\text{OU}}_t = \kappa_{1-\gamma}\theta^\beta (D_+^\beta \alpha)(t)$ is compelling and computable. A reviewer will ask: **plot it**. On a simulated OU path with realistic $\gamma \in (0.2, 0.6)$ and $\theta$, how does the fractional-derivative schedule differ from the naive $\alpha_t/c$ (myopic) rule or the exponential-kernel Riccati (NV)? This is the single most useful figure the paper could add.

### E5. Fractional-PID / CRONE connection (§1.3(iii) closing, refs [18], [19]).

- Currently ornamental. The paper says "connects to fractional-order control (18, 19) not previously connected to execution". True at the citation level, but no technical content is transferred — no gain-margin analysis, no robustness result, no PID-tuning claim carried across. A hostile reviewer will say: "this is a name-drop; either the CRONE connection provides a control-theoretic insight (e.g., robustness of $u^\star$ under model misspecification of $\gamma$), or delete."
- Prior-round novelty audit judged the "first crossing" claim defensible in the sense that no execution paper cites CRONE. That defends the sentence's factual accuracy, not its substantive content. The two are different bars.
- **Suggested fix:** either (a) add one substantive result borrowed from CRONE (e.g., derivative-order sensitivity: how does $u^\star$ respond to $\gamma \to \gamma + \delta\gamma$? — this is exactly a fractional-order sensitivity question and CRONE has answers), or (b) demote to a one-sentence "we note that (12) is a fractional-order controller in the sense of CRONE (18, 19); a control-theoretic robustness analysis is deferred" — and don't list the connection as a contribution.

### E6. Multi-asset extension §4.3.

- Assumes $\mathbf{G}(t) = t^{-\gamma}\mathbf{C}$ — separable, single decay exponent across all pairs. This is a *very* strong assumption; empirical cross-impact matrices show heterogeneous decay (Abi Jaber–Neuman–Tuschmann [8] specifically addresses this). One sentence acknowledging that the AJNT framework covers non-separable cross-impact and (12) does not.

### E7. Data availability statement.

- "No empirical data are used" — fine for the mathematical content, but PNAS reviewers may still request an illustrative figure (see E4).

---

## (c) Likely revision demands, ranked by importance

1. **Numerical illustration (must-have).** At minimum: one figure comparing $u^\star$ on the OU example (formula 15) against a myopic $\alpha_t/c$ and against Neuman–Voß exponential-kernel schedule, at $\gamma = 0.4$. Ideally: a second figure for the inventory-only limit recovering GSS's U-shape. PNAS papers with no figures are rare in Applied Math and effectively never in Economic Sciences.

2. **Finite-$T$ theorem or explicit demotion of §4.1 to heuristic (must-have).** Either state and prove a finite-horizon version of Theorem 1 with the KKT-multiplier / Söhngen–Tricomi mode decomposition rigorous, or explicitly demote §4.1 to "heuristic derivation, rigorous finite-horizon result in companion paper [ref]". As written, §4.1 mixes whole-line and bounded-interval objects without a well-posedness citation.

3. **Explicit reduction from AJN resolvent to (12) (should-have).** A Remark or half-page showing that AJN Theorem X, specialized to the whole-line stationary scalar power-law setting, yields (12). This kills the "closed form vs. resolvent" novelty complaint at its root.

4. **Sharpen novelty acknowledgment in Sig Statement and Abstract (should-have).** One clause crediting FSS2022 for the half-order factorization; one clause crediting the Wiener–Kolmogorov / nest-algebra tradition for (11). The technical body already does this; the front matter must match.

5. **State the spectral-density hypothesis limitation up front (nice-to-have).** One sentence in §2.1 that this excludes fractional-noise-driven rough signals.

6. **Substantive CRONE content or demote (nice-to-have).** Either derive a sensitivity result to $\gamma$ from CRONE machinery, or remove the "not previously connected" claim to a single acknowledging sentence.

---

## (d) Strengths

- **Formula (12) is clean, closed-form, and immediately implementable.** The three-step reading in §2.6 (anticausal whitening of forecast curve → conditional projection → causal fractional derivative) is genuinely illuminating and is the paper's best expository move.

- **OU example (15) is a clean sanity check** showing the general two-step formula collapses to a pointwise multiplication for Markov signals. This is the right example to keep, and (as noted) the right example to *plot*.

- **Duality between cost norm (3) and tradeability norm (4)** is a useful organizing principle. §1.1's derivation of the value $\tfrac12\|\alpha\|_{C^{-1}}^2$ as the temporal counterpart of the Sharpe-ratio value is memorable and probably re-usable.

- **Table 1 is well-constructed** despite the caveat in E1: it is the right expository device even if the "Cholesky" row conflates two different factorizations, and a reader will absorb the structural correspondence quickly.

- **Admissibility hypothesis stated and used.** §2.1 states $\int(1+|\xi|^{2(1-\gamma)+\epsilon})S_\alpha < \infty$; §5 closes with the corresponding Plancherel check. Many propagator papers gloss this.

- **Attribution is generally honest.** §1.2 credits GSS, NV, AJN, AJNT, FSS by name and role; §1.3(iii) explicitly says the half-order factorization was "implicit in (10)". The prior novelty audit confirmed citations survive scrutiny. This is above the median for arXiv-stage manuscripts and will help with reviewer goodwill.

- **The Markowitz framing is a strong hook for PNAS's cross-disciplinary readership** even where the analogy is formal. A general applied-math or economics reader will grasp the correspondence in one page. For this venue, that matters.

---

## Summary judgment

Not a rejection. This is a revise-and-resubmit with two must-fix items (numerical figure; finite-$T$ status of §4.1) and two should-fix items (AJN reduction; sharpen novelty in front matter). The technical content is correct as far as the whole-line stationary theorem goes and the exposition is well-organized. The main risk is that a reviewer from the AJN or FSS camp reads the Sig Statement/Abstract before the intro and forms a "this is my result" impression that the body then has to walk back.
