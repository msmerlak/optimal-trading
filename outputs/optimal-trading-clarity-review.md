# Clarity & Structure Review — *Optimal Trading Filters: a Wiener–Hopf Approach*

**Artifact:** `v2/optimal-trading-filters-v2.tex` (474 lines → 18-page PDF)
**Review scope:** clarity of exposition and structure only. Correctness/novelty are covered separately (`outputs/optimal-trading-filters-v2-review.md`); where a clarity point brushes correctness it is flagged as such.
**Verification:** compile + full cross-reference audit performed (see Reproducibility). All `\ref`/`\eqref` resolve; 0 compile errors.

---

## Summary Assessment

This is a well-structured, clearly written applied-mathematics paper. The exposition has genuine craft: an explicit notation convention with a comprehensive table, a section-by-section roadmap in §1.3, a consistent organizing thesis ("one factorization, computed differently"), and every proof cleanly deferred to a named appendix. The two recent restructurings — inserting the "Mean-reverting signals" subsection in §2 and reordering §4 into challenge → interior theorem → power-law → general — landed cleanly, with zero dangling references after the moves.

The clarity issues are local and fixable, not structural failures. The single most consequential one is **notation overloading of μ** (return vs. two kinds of multiplier). Secondary items: a dense, front-loaded §1.4 that presents a detailed prior-work comparison before the method exists; a handful of abstract polish/precision slips; and a mild forward-dependency seam left by the §2 reorder. No critical issues.

**Overall clarity grade: strong.** The paper reads well for its target audience (Quantitative/Mathematical Finance). A short revision pass would remove the remaining friction.

---

## Strengths

1. **Explicit notation discipline.** Table 1 groups every symbol by role and states the convention outright ("Operators are italic capitals and carry no argument; kernels are lowercase Latin; a hat denotes the Fourier transform; filters are lowercase Greek"). This is better than most papers in the area.
2. **The α/μ two-signal distinction is maintained.** α (expected remaining appreciation) and μ = E_t[−α̇] (expected return) are defined once, flagged in the table, and used consistently — rate ∝ α under temporary impact (§3.1), position ∝ μ under Markowitz (§5.1). This is a subtle point handled deliberately rather than blurred.
3. **Signposting.** §1.3 closes with an explicit roadmap; §3 opens by listing the three power-law peculiarities that become §3.1–3.3; §4's intro states the challenge before the machinery. A reader always knows where they are.
4. **Result/proof separation.** Lemma, Theorems, and Propositions are self-contained; each proof lives in a named appendix (A–E) with a one-line intuition left in the main text ("triangular bookkeeping"; "three steps with a clear reading"). This keeps the main line readable.
5. **§4 reorganization is clean.** General existence/framework → interior-approximation theorem → pure-power-law explicit factor → general Gohberg–Krein equations are now separated rather than interleaved, and the power-law factor is explained structurally (conjugation of the whole-line factor by (T−t)^ν).
6. **Abstract–body consistency on the headline contrast.** The abstract's claim that, unlike rational filters, the power-law solution "always captures a fixed fraction sin(πβ/2)" is now backed by the §3.2 remark showing the exponential fraction is timescale-dependent.

---

## Critical Issues

None. The paper compiles, all references resolve, and the global structure is coherent.

---

## Major Issues

### M1 — μ is overloaded across three distinct objects
`μ` / `μ_t` denotes the expected return E_t[−α̇]; `μ^\star` denotes the nonanticipativity (adaptedness) multiplier; `μ_k` denotes the position-constraint multipliers. All three appear in nearby regions — the duality Remark (eq. `multiplier`) uses μ*, while §5.1 Markowitz uses μ = return — and are distinguished only by super/subscript. For a reader, "μ" silently switches between an economic signal and a Lagrange multiplier. This is the paper's largest clarity liability.
- **Fix:** rename the multipliers. λ is taken (risk aversion); `ξ`, `m`, or `ζ`-style letters are free. Even `ν`-free options like `π^\star` (shadow price) would read more naturally, since the Remark already calls μ* "the shadow price of information."

### M2 — §1.4 "Relation to earlier work" is dense and front-loaded
Three paragraphs of prior-work comparison precede the method (§2). Paragraph 2 is a detailed Abi Jaber–Neuman comparison ("linear stochastic Volterra equation of the second kind," "the resolvent series … is the Neumann expansion of the inverse Volterra operator"); paragraph 3 is an O(n²) computational-cost argument. Both lean on objects (Volterra factors, resolvent series, Gohberg–Krein) the reader has not yet met, so the section is hard to absorb on first pass.
- **Fix (structure):** keep the one-paragraph landscape, but consider deferring the computational-cost paragraph (para 3) to the end of §2 or the conclusion, where "convolution filter," "handful of exponential moving averages," and "solution operator" are already concrete. The AJN comparison could be tightened to two sentences with a forward pointer to §4/§5 for the equivalence detail.

---

## Minor Issues

- **m1 — Abstract hyphenation.** Abstract writes "Wiener-Hopf" (hyphen); the body uses "Wiener--Hopf" (en-dash) three times. Make consistent (en-dash).
- **m2 — Abstract precision on the fractional claim.** "In the empirically motivated case of power-law transient impact, … the optimal trading rate reduces to a fractional derivative" — the clean reduction requires **pure** power-law (η=λ=0), as §3.1 is careful to establish. Insert "pure": "…case of pure power-law transient impact…". (Correctness-adjacent, surfaced here because the unqualified phrasing can mislead.)
- **m3 — Abstract omits the recovery result.** The abstract previews the §3 consequences (fractional policy, sin(πβ/2), no blocks, no surfing) but not §5, where the same factorization reproduces Markowitz, the aim portfolio, Neuman–Voß, GSS, and Forde et al. That unification is a substantial part of the paper; one clause would signal it. (Emphasis choice, not an error.)
- **m4 — §2.3 forward-dependency seam.** The OU value v = σ²θ/4Φ² is stated in §2.3 (Mean-reverting) but derived in Appendix B via the stationary-filter machinery introduced only in §2.4 (it uses ‖φ̂‖² = πσ²/θ). This is an artifact of the recent reorder placing mean-reverting before the stationary filter. Either note "(value derived in §2.4/App. B)" at first mention, or move the value line to §2.4.
- **m5 — `tab:notation` is never referenced.** The notation table is never pointed to from the text. Add "(Table 1)" at the first place notation gets heavy (e.g., end of §1.1 or start of §2.1) so readers know it exists.
- **m6 — Orphan equation labels.** `eq:N, eq:fractional, eq:phi, eq:exp-factor, eq:nv-factor, eq:nv-filter, eq:bdry-decay, def:mr` are labeled but never cross-referenced. Harmless, but the labels can be dropped (or, better, cited where their content is invoked — e.g., `eq:fractional` is the central fractional-policy equation and could be referenced from §3.2/§4.2).
- **m7 — "and possibly inventory risk"** (abstract) reads awkwardly; "inventory risk" alone suffices (the λ=0 case is subsumed), or "with optional inventory risk."
- **m8 — "Contrary to classical rational filters…"** (abstract opener of the last sentence) is a mild negation-motivation construction that the project style rules (`AGENTS.md`) discourage. It is a genuine contrast so it is defensible, but a positive framing ("The power-law solution captures a fixed fraction sin(πβ/2) …, generates no block trades, and never surfs its impact — none of which the rational filters do") would comply more cleanly.
- **m9 — Power-law content is split across §3, §4.2, §5.2.** Organization is thematic (peculiarities / finite-horizon / recovery), which is defensible, but a reader tracking "the power-law case" must jump between three sections. A one-line forward pointer in §3 ("its finite-horizon factor and the execution-literature profiles appear in §4.2 and §5.2") would stitch the thread.

---

## Reproducibility and Verification

- **Compile:** `pdflatex ×3 + bibtex` → **0 errors, 0 undefined references, 0 multiply-defined labels, 0 undefined citations**; 18 pages. `Verification: PASS`.
- **Cross-reference integrity:** every `\ref`/`\eqref` resolves to a label (no dangling refs) — notable given two recent structural moves. `Verification: PASS`.
- **Figures:** four figures (`fig:filter, fig:value, fig:surf, fig:bdry`), each referenced once and discussed in place; captions are self-contained. `Verification: PASS`.
- **Orphan labels:** 8 labels defined but never referenced (listed in m6) — cosmetic. `Verification: PASS (noted)`.
- **Artifact availability (clarity-relevant only):** Acknowledgements state "Verification scripts and figure code are available from the author" and disclose AI assistance. No in-paper repository link; a URL would aid reproducibility, but that is outside the clarity/structure scope of this review.

---

## Inline Annotations

- **Abstract (line 36):** "Wiener-Hopf" → en-dash [m1]; "power-law transient impact" → "pure power-law transient impact" [m2]; consider a recovery clause [m3]; "and possibly inventory risk" [m7]; "Contrary to classical rational filters…" foil [m8].
- **§1.1 / Table 1:** add an explicit pointer to Table 1 [m5]; the μ = E_t[−α̇] definition is good, but see μ-overloading [M1].
- **§1.4 (Relation to earlier work):** dense/front-loaded; consider deferring the O(n²) cost paragraph [M2].
- **§2.2, Remark (Duality), eq. `multiplier`:** μ* multiplier collides with μ = return [M1].
- **§2.3 (Mean-reverting):** OU value v forward-depends on §2.4/App. B [m4]; `def:mr` label unused [m6].
- **§3.1, eq. `fractional`:** central equation carries an unused label [m6]; add cross-thread pointer to §4.2/§5.2 [m9].
- **§5.1 (Rational frictions):** μ = return here vs μ* multiplier in §2.2 [M1]; `eq:exp-factor/nv-factor/nv-filter` labels unused [m6].

---

## Recommendation

**Minor revision (clarity/exposition).** The structure is sound and the writing is clear; no re-architecture is needed. Priority order:
1. Resolve the **μ overloading** [M1] — highest-value single fix.
2. Lighten/relocate part of **§1.4** [M2].
3. Abstract polish: en-dash, "pure," optional recovery clause, drop the foil [m1–m3, m7–m8].
4. Cosmetic: point to Table 1, prune orphan labels, patch the §2.3 forward reference [m4–m6, m9].

None of these block circulation; all improve first-read fluency.

---

## Sources

- `v2/optimal-trading-filters-v2.tex` — full source (read from disk).
- `v2/optimal-trading-filters-v2.pdf` — compiled artifact, 18 pp.
- `v2/optimal-trading-filters-v2.log` — compile diagnostics (0 errors/undefined/multiply-defined).
- Audit commands (this session): label/ref `comm` diff, per-label `grep` counts, hyphenation and μ-usage greps.
- Evidence notes: `outputs/.drafts/optimal-trading-clarity-review-evidence.md`.
- Plan: `outputs/.plans/optimal-trading-clarity-review-plan.md`.

---

## Resolution Log (fixes applied to `v2/optimal-trading-filters-v2.tex`)

Applied and verified (recompiled: 0 errors / 0 undefined / 0 multiply-defined, 18 pp.):
- **M1 — μ overloading: FIXED.** Renamed both multiplier families `μ*→ξ*` (nonanticipativity) and `μ_k→ξ_k` (position constraints) throughout (notation table, Remark `duality`/eq. `multiplier`, §2.4 causality gap, §4 constraints). `μ` now denotes the expected return only. Residual `\mu^\star`/`\mu_k` count = 0.
- **m1 — Abstract en-dash: FIXED.** "Wiener-Hopf" → "Wiener--Hopf".
- **m2 — Abstract precision: FIXED.** "power-law transient impact" → "pure power-law transient impact".
- **m4 — §2.3 forward-ref seam: FIXED.** OU value now flagged "from the value formula of §2.4".
- **m5 — Table pointer: FIXED.** Added "Table~\ref{tab:notation} collects the notation used throughout" at the start of §2.1.

Left for author decision (not applied):
- **M2 — §1.4 relocation:** structural editorial change (moving the O(n²) cost paragraph) that alters the intro's argument flow; flagged, not forced.
- **m3 — abstract recovery clause:** the abstract was deliberately reworked to omit §5; respecting that emphasis choice.
- **m6 — orphan labels:** harmless; pruning is churn with no reader benefit.
- **m7 — "and possibly inventory risk":** author's wording; trivial.
- **m8 — "Contrary to classical rational filters…" foil:** author's freshly written sentence; genuine contrast. Noted tension with `AGENTS.md` style rule, left to author.
- **m9 — power-law cross-thread pointer:** minor; left to avoid churn.

Note on ξ/ζ: the new multiplier symbol `ξ` (12 uses) coexists with the whitened-signal `ζ` (9 uses); visually distinct and contextually separate (multiplier vs. whitened signal), no ambiguity introduced.
