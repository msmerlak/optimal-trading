# Round 2 Verification — papers/noisy-signal-impact-trading.md

Scope: verify only the 9 patch items listed in the assignment. No other sections re-reviewed.

---

## Item 1 — §5.4 Limit cases — **PASS**

Direct substitution into eq (12) with $c(\rho,\lambda) = (1-\lambda\rho)/(1-\lambda^2)$:

- $\lambda\to 0$: $c \to 1/1 = 1$; $x_t \to f_t - 0 = f_t$. ✓
- $\rho\to 0$: $c \to 1/(1-\lambda^2)$; $x_t \to (f_t-\lambda f_{t-1})/(1-\lambda^2)$. ✓
- $\rho\to\lambda$: $c \to (1-\lambda^2)/(1-\lambda^2) = 1$; $x_t \to f_t - \lambda f_{t-1}$. ✓
- $\rho\to 1$: $c \to (1-\lambda)/(1-\lambda^2) = 1/(1+\lambda)$; $x_t \to (f_t-\lambda f_{t-1})/(1+\lambda)$. ✓

All four arithmetic claims hold.

---

## Item 2 — §4.1 New derivation (eqs 4–6) — **PASS (with minor note)**

(a) The gradient of $\langle f,x\rangle - \tfrac12 \langle x, K*x\rangle$ in $x$ is $f - K*x$. Imposing stationarity on the causal subspace gives $[K*x - f]_+ = 0$, i.e. the residual is purely anticausal (orthogonality of residual to causal test functions). Equation (4) is the correct causal FOC.

(b) Setting $y = K_+ * x$ (causal since $K_+$ is the outer/causal factor) yields $K*x = K_- * y$, so (4) becomes $[K_- y - f]_+ = 0$. The standard Wiener–Hopf solution $\hat y = [\hat f/\hat K_-]_+$ follows because $K_-$ is anticausal with $K_-(\infty)$ finite and zero-free outside the disk, so the map $y \mapsto [K_- y]_+$ on the causal subspace is invertible with inverse $g \mapsto [g/K_-]_+$. The text's one-line justification ("multiplication by anticausal $\hat K_-$ followed by causal projection is invertible on the causal subspace") is correct but terse; this is standard textbook Wiener–Hopf and acceptable for a pedagogical note.

(c) Boxed eq (6), $\hat x(z) = \hat K_+^{-1}(z)[\hat f(z)/\hat K_-(z)]_+$, is the standard Wiener–Hopf causal solution and unchanged in content from the prior boxed result. ✓

- Note (OPTIONAL): could add one sentence noting that invertibility of $y\mapsto [K_- y]_+$ uses outer-ness of $K_-$. Not blocking.

---

## Item 3 — §8.1 Rewrite — **PASS**

(a) The broken half-formula `(...)` and inline TODO are gone. ✓
(b) Wiener-filtered AR(1)+white-noise: $S_{\tilde f}$ admits a rational spectral factorisation with denominator $(1-\rho z^{-1})$ inherited from $S_f$ and numerator $(1-\lambda_W z^{-1})$ from solving the quadratic factorisation equation. The causal Wiener filter output therefore has pole $\rho$ and zero $\lambda_W$ — i.e., ARMA(1,1). Statement is correct. ✓
(c) Eq (22) is now explicitly tagged "heuristic; low-noise limit" both in the prose and inline next to the equation. ✓
(d) The "important caveat" paragraph correctly disclaims the scalar-collapse and labels the closed form as future work. No new unjustified arithmetic.

---

## Item 4 — §1 and §9 GP13 rewrites — **PASS**

§1: "The seminal framework of Gârleanu and Pedersen [GP13] resolves an analogous tension in closed form for **quadratic instantaneous transaction costs** (no transient impact) with OU return-predicting factors..." Correctly describes GP13. No claim of nesting. ✓

§9: "quadratic instantaneous transaction costs (not a transient impact propagator)... conceptually parallel to our (12) but is *not nested* in our framework... We make no claim of an exact correspondence." ✓

---

## Item 5 — Sources appendix — **PASS**

- Entry 6: "Abi Jaber & Neuman (2022) [AN22] — Optimal Liquidation with Signals: The General Propagator Case. arXiv:2211.00447". ✓
- Entry 8 (GSS12): DOI `10.1111/j.1467-9965.2011.00478.x` present. ✓
- Entry 9: Alfonsi, Schied & Slynko (2012). ✓
- Entry 10: Obizhaeva & Wang (2013). ✓
- Entry 11: Neuman & Voß (2022), arXiv 2002.09549. ✓
- Entry 12: Forde, Sánchez-Betancourt et al. [FSB+]. ✓
- Entry 13: Bouchaud, Bonart, Donier & Gould (2018). ✓
- Numbering 1–15 contiguous, no duplicates, no skips. ✓

---

## Item 6 — §2.3 half-impact note — **PASS**

Note appears just after the symmetrised-kernel definition (in §2.2, the section that actually contains the symmetrised kernel — task referred to §2.3 but the substantive requirement is met):

> "We adopt the standard *execution-at-mid* convention in which the trader pays only half of the contemporaneous self-impact $G(0)$; this convention is what allows the cost to be written cleanly as the symmetric quadratic form with $K(0) = G(0)$."

Single sentence, in correct location. ✓ (Minor: task labelled it §2.3 but content is in §2.2 — not a defect.)

---

## Item 7 — §6.2 distributional note — **PASS**

> "Note that for $\beta\in(0,1)$ the symmetric kernel $K(n) = |n|^{-\beta}$ is *not* absolutely summable; it must be interpreted as a positive-definite tempered distribution whose Fourier transform $\hat K(\omega)\sim |\omega|^{\beta-1}$ is locally integrable at the origin (cf. [Gat10] for the no-arbitrage admissibility of such kernels)."

Mathematically accurate (the function is in $\mathcal S'$, defines a positive-definite tempered distribution; $\hat K \sim |\omega|^{\beta-1}$ is locally integrable on the circle for $\beta>0$). ✓

---

## Item 8 — §9 LN19 / AJN24 / Forde — **PASS**

(a) LN19: "linear transient impact with exponential resilience (Obizhaeva–Wang style), plus linear temporary impact". No longer claims "general class of decay kernels". ✓
(b) AJN24: "conceptually parallel but not literally nested in their framework — they work with terminal-liquidation constraints, we work in an infinite-horizon ergodic regime". The "subsumes ours" wording is gone; horizon difference is explicitly acknowledged. ✓
(c) Forde et al. paragraph present as its own paragraph in §9, correctly framed as the closest precedent to the §6 power-law/fractional-derivative result. ✓

---

## Item 9 — No new bugs in patched regions — **PASS**

Scanned the modified regions (§1 GP13 paragraph, §2.2 half-impact note, §4.1, §5.4 limits, §6.2 distributional note, §8.1 rewrite, §9 paragraphs, Sources list):

- LaTeX renders cleanly; no unmatched braces or stray `\` artefacts.
- Equation numbering 1–22 is consecutive with no duplicates after the rewrites.
- Cross-references ([GP13], [LN19], [AJN24], [AN22], [GSS12], [FSB+], [AC01], [Gat10], [BGPW04]) all resolve to entries in the Sources list.
- The §5.4 phrase "scaled by the kernel's spectral mass" matches the value $1/(1-\lambda^2) = \sum_n \lambda^{|n|}/(1+\lambda) \cdot \ldots$ — informally correct (it is the integrated spectral density at zero up to a constant); acceptable for an interpretive aside.
- §8.1 caveat is internally consistent with eq (22)'s "heuristic" tag.

No new typos or inconsistencies detected.

---

## Summary

| Item | Verdict |
|---|---|
| 1. §5.4 limit cases | PASS |
| 2. §4.1 derivation | PASS (one OPTIONAL polish: tighten invertibility justification) |
| 3. §8.1 rewrite | PASS |
| 4. §1/§9 GP13 | PASS |
| 5. Sources appendix | PASS |
| 6. §2.x half-impact note | PASS |
| 7. §6.2 distributional note | PASS |
| 8. §9 LN19/AJN24/Forde | PASS |
| 9. No new bugs | PASS |

**Open items:** None at BLOCKER or FIX-NOW level. One OPTIONAL polish in §4.1 (a single clarifying sentence on outer-ness of $K_-$ giving invertibility of $y\mapsto[K_- y]_+$). Safe to defer.

**Recommendation:** Stop the review loop. All Round 1 fix items are satisfactorily addressed; the draft is in a coherent, internally consistent state suitable for sharing.
