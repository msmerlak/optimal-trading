# PNAS format & style review — `papers/markowitz-of-cost-pnas.md`

Reviewed against `AGENTS.md` style rules and PNAS structural conventions. No edits applied.

## Summary
Format is largely PNAS-compliant: Significance Statement, Abstract, numbered Introduction with lit review as a subsection (not a separate top-level "Related Work"), Materials and Methods last, 23 numbered references, 15 sequential equation tags. Cross-references all resolve. Two blocker-class issues (reference numbering order, one prohibited rhetorical construction) plus a small number of style-guide violations.

---

## (a) Blockers

### B1. Reference numbering does not follow PNAS "order of first citation"
PNAS requires references numbered in order of first appearance in the text. The first citations in §1.1 (line 27) are `(3, 4, 16)`, followed by `(1, 2)` at line 33. Current numbering is grouped thematically (Markowitz first, then impact empirics, etc.), which is *Nature*-style, not PNAS.

Current first-appearance order in body:
- Line 27: (3), (4), (16)
- Line 33: (1), (2)
- Line 53: (5), (6), (7), (8), (9), (10), (11–13)
- Line 65: (14), (15)
- Line 71: (17)
- Line 71: (18), (19)
- Line 87: (20, 21)
- Line 105: (22)
- Line 141: (23)

Under PNAS rules the current refs `[3, 4, 16, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23]` should be renumbered to `[1..23]` in that appearance order (Bouchaud→1, Gatheral 2010→2, Jusselin–Rosenbaum→3, Markowitz→4, Merton→5, …). All in-text citation numbers must be updated accordingly. This is mechanical but every `(N)` in body must be re-mapped.

### B2. Prohibited "X is not Y — it is Z" construction
Line 59 (§1.3(i)):

> "Linear position constraints … **are not a separate problem: they are the special case of (1)** in which the effective signal contains an additive constant…"

This is exactly the AGENTS.md prohibited construction ("X is not Y, it is Z" and variants). Assert the positive claim directly, e.g. "Linear position constraints are the special case of (1) in which the effective signal contains an additive constant equal to the KKT multiplier of the constraint."

---

## (b) Style violations worth fixing now

### S1. Empty intensifier "empirically dominant" (2 occurrences)
- Line 19 (Abstract): "For the **empirically dominant** power-law kernel…"
- Line 43 (§1.1): "for the **empirically dominant** power-law kernel"

Per §1.3(iii) (line 71) the paper already uses the more accurate "empirically supported"; use that formulation consistently. "Dominant" is an intensifier without technical content (kernel is not a distribution being compared for mass — "supported" is what the citations actually establish).

### S2. Marketing-adjacent phrase "substantial literature"
Line 53 (§1.2 opener): "Problem (1) has a **substantial literature**."

This is a variant of the AGENTS.md-prohibited "a rich literature". Delete or replace with a specific opener: "Problem (1) has been studied in three settings." — then list them.

### S3. Overstatement "sole structural addition"
Line 188 (§3): "The projection $P_+$ between the two Cholesky-analog factors is **the sole structural addition** in the temporal case."

"Sole" is an unsupported/unnecessary intensifier — Table 1 and §3 also flag the whitening axis change (assets → time) as structural. Prefer: "The projection $P_+$ between the two Cholesky-analog factors is the structural addition beyond Markowitz; it enforces adaptedness and has no cross-sectional counterpart."

### S4. Abstract exceeds PNAS ~250-word target
Measured length: **276 words** (per `wc -w` on the abstract block including its heading). PNAS caps abstract at 250. Needs ≥26 words cut.

Suggested cuts (candidates):
- Line 19: "and the projection between the two half-inverses is the signature of the causality constraint" (17 words) — restates the previous clause.
- "This gives a closed-form bulk term where the general-propagator theory offered only implicit resolvent representations, and connects optimal execution to fractional-order control." (24 words) — the "connects to fractional-order control" clause duplicates content of the Significance Statement.

### S5. Significance Statement word count — OK
Measured 118 words (with heading) → body ~116 words. Under the 120 target. Clean.

---

## (c) Submission-time TODOs

1. **Ref 7 (Abi Jaber–Neuman) missing volume/pages.** Currently: "*Math. Finance* (arXiv:2211.00447)." Update to volume:page range at acceptance. Confirmed incomplete as flagged.
2. **Refs 8, 9 are arXiv-only preprints.** Check publication status by submission time; upgrade to journal citations if published.
3. **Ref 11 (Wiener–Hopf 1931).** Historical Preussische Akademie note; page range `696–706` given. PNAS may want a modern reprint or reference-work citation for accessibility; consider adding a secondary source.
4. **Renumber references per B1** and update every in-text `(N)` citation.
5. **Trim abstract to ≤250 words** per S4.
6. **Author, corresponding author, and affiliation blocks** are still `TBD` (line 3). Complete at submission.
7. **Classification codes** line 5: "Physical Sciences — Applied Mathematics / Economic Sciences" needs to pick one primary track for PNAS submission portal.
8. **Notational disambiguation of `(N)`.** PNAS uses `(N)` for numeric citations; the paper also uses `(N)` for equation tags. Most usages are disambiguated by context ("Equation (5)", "Gatheral–Schied–Slynko (5)"), but a few are borderline:
   - Line 43: "the dual (3)–(4) organizes the entire construction" — refers to eqs (3)–(4), while refs 3–4 are Bouchaud/Gatheral (highly relevant in the same paragraph). Consider "the dual pair Eqs. 3–4" or `[3]–[4]` for equations. PNAS accepts `[N]` for equations; adopt that to eliminate all ambiguity in one pass.

---

## (d) Items already clean

- **No rhetorical questions.** Zero `?` in body prose (confirmed via grep).
- **No prohibited "rather than", "not merely", "genuinely", "canonical", "elegant", "beautiful", "remarkable", "essentially", "fundamentally"** in the text.
- **No throat-clearing openers** ("Note that", "Importantly", "Interestingly", "Recall that", "Of course", "Indeed", "It is worth noting", "It is well known").
- **No "in a certain sense" / "rich literature"** (aside from S2 near-variant).
- **Equation tags 1–15 are sequential with no gaps or duplicates.** Every in-text equation reference resolves: (1), (3)–(4), (5), (6), (7) [implicit via `\bar\alpha`], (8), (11), (12), (13). Eqs (2), (9), (10), (14), (15) are defined but not back-referenced by number, which is standard.
- **All 23 references are cited at least once** in body. Every in-text citation number resolves to a listed reference.
- **Cross-references resolve.** `Section 2`, `Section 4`, `Section 4.1`, `Section 5`, `§1`, `§2.1`, `§2.3`, `Theorem 1`, `Lemma 1`, `Table 1` all resolve. `§5.4`, `§5.3 Thm 5.3` are inside citations to Samko–Kilbas–Marichev (ref 17), unambiguous.
- **Materials and Methods placement** correct (§5, last section before References).
- **Related work integrated into introduction** as §1.2, not a separate top-level section — PNAS-compliant.
- **Structural fit of §1.1–§1.5.** The intro trajectory (problem → lit → contribution → sketch → extensions preview) reads as one coherent PNAS-style Introduction. §1.4 "Sketch of the argument" is unusual for PNAS which typically avoids proof previews in the intro; consider folding its two paragraphs into §1.3(ii)–(iii) or trimming to one sentence, but this is stylistic, not a blocker. §1.5 "Extensions" is a preview of §4 and could be shortened to one sentence pointing forward if space is needed for the abstract trim.

---

## Prose-quality notes (not blockers, worth a second pass)

- **Line 19 (Abstract):** "Two features of the execution problem have no portfolio counterpart" — the second feature (adaptedness) genuinely has no counterpart; the first (non-locality) has a partial counterpart (block-diagonal Σ vs full Σ). Consider softening to "Two features of the execution problem differ structurally from the portfolio case."
- **Line 63 (§1.3(ii)):** "It is the stochastic-processes analog of the deterministic Wiener–Hopf inversion of half-line convolutions (11–13), transferred to the adapted subspace via nest-algebra outer factorization (14, 15)." — clean, well-cited.
- **Line 71 (§1.3(iii)):** "The half-order factorization was implicit in (10); the explicit reduction of the signal-adaptive optimizer to a fractional derivative of the forecast curve is new" — novelty claim is properly anchored to the closest prior work. Good per AGENTS.md.
- **Line 71:** "makes contact with the CRONE / fractional-PID control tradition (18, 19) not previously connected to execution." — the "not previously connected" is a negative existence claim across two literatures; consider softening to "to our knowledge not previously connected to execution" or drop the clause.
- **§4.1 line 87:** "the two boundary modes contribute an $O(T^{\gamma-1})$ correction on interior regions $[\varepsilon T, (1-\varepsilon)T]$" — asserted without derivation and without a forward reference to a proof or appendix. A PNAS reviewer will ask for either a proof sketch in Methods or a citation.
- **§1.1 line 43:** "the value of (1) becomes the fractional Sobolev $H^{(1-\gamma)/2}$-norm of the forecast curve" — asserted in the intro but not restated or proved in §2/§5. If retained, add a one-line derivation in Methods or a forward reference.

## Conflicts / notes
None. AGENTS.md style rules and PNAS structural rules are consistent for this document. No supervisor decision needed.
