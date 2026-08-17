# Internal-Consistency & Exposition Review
**File:** `papers/fractional-derivative-optimal-execution.md`
**Date:** 2026-06-27
**Scope:** Round 1 — internal coherence after §4.1 insertion, §5.4 W–H addition,
Appendices A–E. No edits applied (review-only).

---

## FATAL

*None.* The paper is a labelled skeleton draft and most issues below are
recoverable by local edits. Nothing makes the manuscript structurally
unsalvageable in v1.

---

## MAJOR

### M1. Order of the fractional derivative — global labelling inconsistency
The central object `D^γ_{[0,T]}` is claimed to invert the
power-law kernel `|t|^{-γ}`, but with the Riemann–Liouville convention
laid down in §3.1 (line 171), the inverse of `|t|^{-γ}` is the Riesz
derivative of order **1−γ**, not γ.

Concretely:
- §3.1, line 171: `D^ν_+ f = (1/Γ(1-ν)) d/dt ∫(t-s)^{-ν} f ds`. Hence the
  standard `D^γ` inverts `I^γ` (kernel `(t-s)^{γ-1}`), **not** `I^{1-γ}`
  (kernel `(t-s)^{-γ}`).
- §3.2, lines 175 + 178: `D^γ_{[0,T]} := ½(D^γ_+ + D^γ_-)` is then
  asserted to be "the natural inverse of the symmetric convolution
  `|t|^{-γ}` kernel." Those two claims are mutually inconsistent under
  the §3.1 convention.
- §5.4, lines 408 + 410–411: the Fourier symbol `(∓iξ)^{(γ−1)/2}` gives
  one-sided derivatives of **order (1−γ)/2** each, total operator order
  **1−γ**, yet line 411 calls this "the causal Riesz fractional
  derivative of order **γ**." Direct self-contradiction within the
  single corollary.
- The constant `κ_γ = (c·Γ(1−γ))⁻¹` (Theorem 4.1, line 236) is exactly
  the prefactor for inverting `c·Γ(1−γ)·I^{1−γ}` via `D^{1−γ}` — i.e.
  the constant is consistent with order **1−γ**, not γ.

Net effect: every "order γ" claim in the abstract (line 17), §1.2 #1
(line 70), Theorem 4.1 (line 234), §4.4 (line 295), Theorem 6.1
(line 466), §9 (line 491), and §5.4 should be reconciled — either by
(a) globally relabeling the operator order as `1−γ`, or (b) keeping the
"order γ" label but adding an explicit one-line warning in §3.2 that
"order γ" here denotes "the order of the Riesz operator that inverts
`|t|^{-γ}`" (i.e. a deliberate departure from the §3.1 convention) and
correcting the W–H labels in §5.4 accordingly. As it stands the paper
is self-inconsistent at the headline level.

### M2. The `(★)` first-order condition vs. the FOC in Appendix A.1
- §2.4, line 117: `∫ G(|t−v|) u*_v dv = λ − E_t[α_T] + α_t`.
- §5.2, line 318: same RHS in `(★★)`.
- Appendix A.1, line 575: `∫ G(|t−v|) u*_v dv = α_t − λ`. The
  `E_t[α_T]` term is **silently dropped**, and the sign of `λ` is
  flipped relative to `(★)`.
- Theorem 4.1, line 234: uses `λ − \bar α(t,s)` (no `E_t[α_T]`), which
  matches A.1 but not `(★)`.
- §5.2 resolvent expression, line 326: `λ − E_s[α_T] + α_s` (matches
  `(★)` but not Theorem 4.1's truncated form).
- Theorem 6.1, line 466: `λ − E_t[α_T] + α_t` (matches `(★)`, not 4.1).

The reader cannot tell whether the `E_t[α_T]` term is genuinely zero
(plausible under §2.2's definition `α_t := E_t[P_T − P_t]`, which forces
`α_T ≡ 0` and hence `E_t[α_T] = 0`), or whether it is a real term that
was accidentally dropped in A.1 and Theorem 4.1. The two derivations
must be reconciled, and the sign of `λ` standardized. Either:
- drop the `E_t[α_T]` term everywhere (consistent with the §2.2
  definition), or
- keep it everywhere and justify it (e.g. redefine `α_t` as the
  instantaneous drift, not the cumulative expected return).

### M3. Abstract / Conclusion / §1.2 do not advertise §5.4
The §5.4 Wiener–Hopf material and Corollary 5.3 are a substantive new
contribution (~70 lines of body + Appendix B.4–B.5). Yet:
- Abstract (lines 11–31): no mention of W–H factorization or the
  half-line / infinite-horizon CRONE-2 connection.
- §1.2 Contributions (lines 68–87): four items listed, none refer to
  Proposition 5.2 / Corollary 5.3.
- §9 Conclusion (lines 487–500): lists fractional derivative,
  Mittag–Leffler resolvent, matrix derivative; W–H is absent.

Add one bullet to each of these three locations. The CRONE-2 paragraph
at lines 437–447 is currently the only place the contribution is
flagged.

### M4. `κ_γ^∞` introduced but never defined
Corollary 5.3, line 410 uses `κ_γ^∞` in the displayed equation, but the
constant is never given a closed form. Compare `κ_γ = (c Γ(1−γ))⁻¹`,
which is defined at the analogous location (Theorem 4.1, line 236).
Either define `κ_γ^∞` explicitly (likely `(c_+ c_−)^{−1}` from
Prop 5.2) or remove the superscript and reuse `κ_γ`.

---

## MINOR

### m1. Reused symbol `λ` in Appendix C
`λ` is the scalar Lagrange multiplier in §2.3 and Theorem 4.1, but in
Appendix C (lines 752–778) it is reused as eigenvalue (`λ_i`,
`Λ = diag(λ_i)`) while the component Lagrange multipliers become
`\tilde λ_i` and the back-rotated vector becomes `\boldsymbol λ`.
The footnote at line 777–779 ("Translating back gives a vector Lagrange
multiplier `\boldsymbol λ = Q \tilde{\boldsymbol λ}`") is a partial
warning. A one-line remark at the head of Appendix C, e.g. "We reuse
`λ_i` for spectral eigenvalues; Lagrange multipliers in this appendix
carry tildes," would prevent the collision from being silent.

### m2. Bibliography entries never cited
- **Luchko, Yu. (2021)** — listed at line 836 but no in-text mention.
- **Abi Jaber, Hauzy, Neuman (2024)** — listed at line 840 but no
  in-text reference (only the 2022 and 2025 papers are cited).

Either cite them in the obvious places (Luchko fits §3.2 Sonine
discussion; Hauzy fits §5 footnote on constraints) or drop them.

### m3. In-text citations missing from References
- **Almgren–Chriss** — used at lines 344, 698, 816 with no entry in
  References. Add Almgren & Chriss (2001) "Optimal execution of
  portfolio transactions," J. Risk 3(2).
- **Obizhaeva–Wang** — used at lines 345, 350, 707 with no entry.
  Add Obizhaeva & Wang (2013) "Optimal trading strategy and
  supply/demand dynamics," J. Financial Markets 16.
- **Novokshenov, Mat. Zametki 97(3), 2015** (line 428) — given as an
  inline citation but not in References.
- **Oustaloup (1991), La commande CRONE** — listed in refs (line 853)
  and referenced obliquely as "Oustaloup's CRONE" (lines 28, 81, 301,
  440, 503), but no explicit year/handle is used in the body. Acceptable
  if implicit, but flag for stylistic consistency.

### m4. Year mismatches text ↔ refs
- §1.1 line 38: "Bouchaud, Gefen, Potters and Wyart (**2004**)"; ref
  line 842 dated **2003** (Quant. Finance 4, 176, 2003). Appendix E
  line 812 also uses "2003." Standardize.
- §1.3 line 98: "Neuman–Voß (**2022**)"; ref line 851 is dated **2020**
  (arXiv:2002.09549). Same author pair so likely the same paper —
  reconcile to "2020."
- §B.4 line 728: "Krein **1958** / Noble 1958"; ref line 834 is the
  **1962** AMS translation. Use the translation year or add "Russian
  orig. 1958."

### m5. Abstract reference to `E_{γ,β}` vs. body `E_{1−γ, 1−γ}`
Abstract line 24 says "two-parameter Mittag–Leffler function
`E_{γ,β}`"; §3.3 (line 200) and Theorem 5.1 (line 332) actually use
`E_{1−γ, 1−γ}`. Either keep abstract generic (it is generic now) but
note that the parameters are specialised in the body, or substitute
the specific indices. Acceptable as-is but worth tightening.

---

## NITS

### n1. Appendix ↔ main-text pointer audit (all check out)
- Theorem 4.1 → Appendix A.1–A.3 ✓ (A.1 reduction, A.2 inversion,
  A.3 Forde recovery).
- Corollary 4.2 → A.2 ✓.
- Corollary 4.3 → A.3 ✓.
- Theorem 5.1 → Appendix B.1–B.2 ✓.
- Proposition 5.2 → B.4 ✓.
- Corollary 5.3 → B.5 ✓.
- Theorem 6.1 → Appendix C ✓.
- §4.4 #3 mentions FFT — Appendix D exists, no cross-link from §4.4 to
  Appendix D by name (consider adding "(see Appendix D)").
- §7 mentions empirical protocol — Appendix E exists but is not
  cross-linked from §7. Trivial.

### n2. Section-number references after the §4.1 insertion
Searched all `§X.Y` references; every internal pointer post-renumber is
correct:
- §2.3 (line 565), §2.1–2.2 (line 444, external), §4.1 (lines 239,
  400, 581) all hit the **new** §4.1 (forward conditional-forecast curve).
- §4.2/4.3 external refs (lines 798, 820) point to companion docs and
  are unaffected.
- §5.3 (line 702) ↔ §5.3 "Limits" ✓.

### n3. Theorem/Corollary/Remark numbers
No collisions detected. Theorem 4.1, Corollary 4.2, Corollary 4.3,
Remarks 4.1.1–4.1.2 form a clean cluster (the nested 4.1.x scheme for
remarks is unusual but consistent). §5 has Theorem 5.1, Proposition 5.2,
Corollary 5.3, Remarks 5.4–5.5 — sequential and non-colliding.
Theorem 6.1 stands alone.

### n4. Hand-waved (⚠️) flag audit
Eight ⚠️ markers reviewed: A.1 (projection lemma), A.2 (three items),
A.3 (boundary corrections), B.2 (symmetric vs half-line iteration),
B.5 (Π_+ L² control), C (multiplier translation), D (Grünwald
boundary error). All flag genuine gaps; none are over-used.

One under-flagged concern: **B.2 lines 670–688** silently swaps the
finite-interval symmetric convolution `|t|^{-γ}` for a one-sided
half-line convolution `t^{-γ}` to compute the iterated kernel; the
boundary-effect dismissal at line 689 ("do not affect the
Mittag–Leffler identification away from the endpoints") is the load-
bearing step of the entire Theorem 5.1 derivation and deserves a
sharper ⚠️ note (or a quantitative tail bound) rather than the
present passing reference to `B_γ`.

### n5. §5.3 "OW limit fix" reads well
The clarification at lines 345–354 that exponential resilience is **not**
the `γ → 1⁻` limit is correct, clear, and an improvement over earlier
drafts. Restated in B.3 (lines 702–707). Consistent.

### n6. `\bar α(t,t) = α_t` boundary condition
Line 215 states `\bar α(t,t) = α_t` "by construction." The piecewise
definition above gives `\bar α(t,s) = α_s` for `s ≤ t`, so at `s = t`
the value is `α_t`. Continuity at `s = t` between the realized and
forecast halves requires `E_t[α_t] = α_t` (true by `F_t`-measurability
of `α_t`). The phrase "by construction" is fine but could note this
trivially.

### n7. Notation roster (no other collisions found)
`\bar α / \bar α^∞`, `D_±`, `G_±`, `κ_γ / κ_γ^∞` (modulo M4), `c_±`
(W–H factorization constants), `c_γ` (composite symbol prefactor),
`c_1` (homogeneous-solution constant), `c` (kernel coefficient),
`R_{γ,η}`, `B_γ / B_{γ,i}` are all distinguishable. No silent
re-uses beyond the `λ` issue (m1).

---

## Summary

The paper is internally coherent at the level of sectioning,
appendix linking, and theorem numbering after the §4.1 / §5.4 edits.
The two structural concerns are **M1** (the order of the central
fractional derivative — γ vs 1−γ — clashes between §3.1 convention,
§3.2 informal definition, and §5.4 explicit operators) and **M2**
(the `E_t[α_T]` term and sign of `λ` are inconsistent across
`(★)`, A.1, Theorem 4.1, §5.2, Theorem 6.1). Both are recoverable
with local edits but should be fixed before circulating v1.

**M3** (abstract/conclusion alignment with the new W–H section) and
**M4** (undefined `κ_γ^∞`) are quick fixes. The minor items are
bibliography hygiene. No new ⚠️ markers needed beyond the one
suggested at n4.
