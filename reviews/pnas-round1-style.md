# PNAS Round 1 — Style and Form Compliance Review

Target: `papers/markowitz-of-cost-pnas.md`
Style guide: `AGENTS.md`
Note: `plan.md` and `progress.md` do not exist at repo root. Review proceeds against `AGENTS.md` alone.

## Review

### Correct (already good)

- **Numbered references, inline PNAS style.** References list is numbered 1–24 in `## References`; inline citations use `(1, 2)`, `(3, 4)`, `(3–5)`, `(6, 7)`, `(8–11)`, `(12)`, `(13)`, `(14)`, `(15, 16)`, `(20, 21)`, `(22)` etc. This is standard PNAS format.
- **Materials and Methods at end.** Section 5 is `## 5. Materials and Methods` and contains the two proofs, data-availability statement, and admissibility argument. Correct placement.
- **Equation numbering is consistent.** Equations (1)–(15) are numbered in order; the two displayed equations inside the Materials-and-Methods proofs are unnumbered, which is acceptable in-proof usage.
- **Abstract is a single dense paragraph, self-contained.** No forward references to section numbers, no undefined jargon that is not defined in place.
- **No rhetorical questions.** A `?` grep returns no matches anywhere in the body.
- **No throat-clearing openers.** No "Importantly", "Notice that", "It is worth noting", "It is well known", "Let us", "We now turn to" appear in the manuscript.
- **Prior work is integrated into the introduction (Section 1, final paragraph)** as AGENTS.md requires — see the paragraph beginning "The mathematical ingredients are individually classical."

### Blockers (major style violations — must fix before submission)

1. **Repeated "canonical" as empty intensifier.** AGENTS.md explicitly lists "canonical" as forbidden unless it carries technical content. Five instances:
   - L13 (Significance): *"This map is the **canonical** solution to the gain–risk tradeoff"*.
   - L13 (Significance): *"the analogous **canonical** map is a fractional derivative"*.
   - L19 (Abstract): *"For the empirically **canonical** power-law kernel"*.
   - L61 (Section 1): *"the symbol factorizes **canonically** as $|\xi|^{1-\gamma}=(i\xi)^\beta(-i\xi)^\beta$"*.
   - L65 (Section 1): *"We propose it as the **canonical** starting point for cost-managed execution."*

   None of these carries technical content (there is no formal "canonical form" being invoked; the factorization on L61 is a "specific" or "explicit" factorization, not a canonical one in a category-theoretic or normal-form sense). Replace with "standard" (L13a), "the corresponding" (L13b), "empirically dominant" (L19; already used in Significance L13, ironically, and can be reused), "explicitly" or "as" (L61), and drop L65 or replace with "as the starting point".

2. **"X is not Y — the correct Y is Z" construction in the Abstract.** L19: *"the naive analog $u^\star = C^{-1}\alpha$ **is not adapted** to the trader's information filtration. **The correct adapted inverse is given by** the filtration Wiener–Hopf factorization …"*. This is a direct instance of the forbidden foil/negation pattern ("not X — it is Y"). State the positive claim first. Suggested rewrite:

   > "The impact operator $C = G\ast$ is a non-local convolution. The adapted inverse on the trader's information filtration is obtained by filtration Wiener–Hopf factorization $C = C_- C_+$ into anticausal and causal factors, giving $(P_+ C P_+)^{-1} = C_+^{-1} P_+ C_-^{-1}$, with the optional projection $P_+$ inserted between the two half-inverses."

   The naive $C^{-1}\alpha$ counter-example can be deferred to the Introduction (where L45–L47 already handle it more carefully).

3. **Significance Statement is over-length and too technical for a broad audience.** Word count is ~132 (target ~120 — borderline, tolerable). More seriously, PNAS Significance is written for non-specialists. Current text uses "inverse of the return covariance matrix", "temporally non-local market-impact kernel", "filtration Wiener–Hopf factorization", "optional projection", "propagator decay exponent" — none of which parses for a broad scientific audience. This is a structural blocker for PNAS, not a stylistic nit. Rewrite to describe the problem (executing a large order incurs price impact; balancing predicted return against impact cost), the finding (a specific fractional-calculus operation on the predicted-return curve replaces the classical matrix inversion), and the significance (unifies portfolio construction and trade execution under one formula). Keep at ≤120 words.

### Fixes worth doing now (specific, small rewrites)

4. **Section 4.6 is titled "Relation to prior work".** AGENTS.md forbids a separate related-work section and requires integration into the introduction. The related-work content in Section 1 (final paragraph, lines discussing (12), (13), (14), (15, 16)) already covers the same material as Section 4.6 with substantial overlap. Options: (a) delete Section 4.6 and fold the two new sentences it adds ("Their bounded-interval weight $B$ implements a mixture of domain restriction and the filtration projection $P_+$…"; the CRONE non-connection remark) into Section 1's final paragraph; or (b) rename 4.6 to something like "Positioning" and keep only the delta beyond Section 1. Option (a) is more AGENTS.md-compliant.

5. **Abstract is ~258 words** (I counted sentence by sentence). Target is ~250, so this is within tolerance. No action required, but tightening is available: the sentence *"read from the inside out as an anticausal half-inversion applied to the forecast curve, followed by an adapted projection, followed by a causal half-inversion"* (L19) restates the operator formula immediately preceding it in prose and can be dropped for ~30 words saved.

6. **L137: "rather than on the realized future path"** — this is the "X, rather than Y" variant of the forbidden foil construction, used to justify a positive claim by negating an alternative. Rewrite as a direct claim: *"…which acts on a forecast curve (an $\mathcal{F}_s$-measurable object), so its non-locality does not require access to the realized future path."*

7. **L204: "ranking … by the Sharpe ratio of $D^{1-\gamma}\alpha$ rather than by raw information coefficient"** — same construction. Rewrite: *"Under (12), the Sharpe ratio of $D^{1-\gamma}\alpha$ (not the raw information coefficient of $\alpha$) is the cost-adjusted PnL predictor parameterized by market microstructure."* — or, better, drop the negation entirely: *"Signals should be ranked by the Sharpe ratio of $D^{1-\gamma}\alpha$; this quantity is the cost-adjusted PnL predictor parameterized by market microstructure."*

8. **Classification / Keywords line.** "Physical Sciences — Applied Mathematics / Economic Sciences" — PNAS requires a single primary classification and permits one secondary. The slash is nonstandard; use PNAS's format (e.g., "Physical Sciences: Applied Mathematics (major); Social Sciences: Economic Sciences (minor)"). Minor; check current PNAS author instructions before final submission.

### Notes (observations, no action required unless flagged again)

- The phrase *"the sole structural addition demanded by the temporal ordering"* (L47, and again in L167 as "the sole structural addition in the temporal case") is asserted twice. It is a positive claim, not a forbidden construction, but the repetition reads as emphasis-by-repetition. Consider dropping one instance.
- Section 2.6 ("Reading (12) inside out") is well-written and does not violate any style rules; it is the strongest expository passage in the paper.
- Density is PNAS-appropriate: ~4,500 words body excluding references, four proofs+examples inside methods, one table, no figures. A single figure summarizing the Table-1 correspondence (or an OU-example trajectory) would improve accessibility; PNAS papers typically have 2–4 display items.
- Reference (23) is missing an author list ("Fractional calculus in optimal control and game theory: A survey. arXiv:2512.12111"). The arXiv ID `2512.12111` is also implausible — arXiv IDs use `YYMM.NNNNN`, so `2512` would be December 2025, which is future-dated relative to the manuscript's own December-2025 reference. Verify.
- Reference (13) cites both `Math. Finance` and an arXiv number; if the journal version is out, drop the arXiv tag.
- The word "correct" appears in Abstract L19 ("The correct adapted inverse") — after removing the foil (blocker 2), "correct" becomes unnecessary and can go.

## Summary

The paper is close to PNAS-form compliant on structure (numbered refs, inline PNAS citation style, M&M at end, one dense abstract paragraph). Three blockers must be addressed before submission: (a) five uses of "canonical" as an empty intensifier, (b) the "not X — the correct is Y" construction in the Abstract, and (c) a Significance Statement that is too technical for a broad audience. Two smaller style violations at L137 and L204 use forbidden "rather than" foils. Section 4.6 duplicates related-work material that AGENTS.md requires be integrated into the introduction. All fixes are local; no restructuring of the mathematical content is required.
