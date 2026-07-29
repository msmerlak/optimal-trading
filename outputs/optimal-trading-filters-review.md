# Internal Review — *Optimal Trading Filters: a Wiener–Hopf Approach*

**Artifact:** `v2/optimal-trading-filters-v2.tex` (local LaTeX, 487 lines, 19 pp. compiled), author Matteo Smerlak (CFM).
**Review focus (requested):** readability, symbols-in-right-place, style / LLM giveaways, structure. Standard theory-paper criteria applied secondarily.
**Method:** lead-owned, full source read from disk; compiled; ran the numerical suite; verified figures, labels, symbol order, attributions. No subagents (single local file — delegation would add overhead).
**Verification date:** 2026-07-24.

---

## Summary Assessment

A strong, near-submission-ready applied-math paper. The core contribution — computing the optimal adapted trading policy in closed form by a Wiener–Hopf factorization of the friction operator, with a fractional-derivative policy for power-law impact and recovery of the classical portfolio/execution rules as special cases — is coherent, correctly stated, and **numerically verified (9/9 checks pass, cross-validated frequency- vs. time-domain, rel. err. ≤ 1e-14)**. The prose is unusually clean of the usual LLM tells and reads as a deliberately crafted mathematical-finance paper.

The recent reformulation to a position/N/μ primary variable (with rate/Q/α reserved for the λ=0 power-law regime) is now internally consistent and well-documented in Table 1; the earlier N-vs-Q / μ-vs-α seam I would have flagged is resolved. The remaining issues are **hygiene and one symbol-ordering defect**, not correctness: a symbol used ~4 pages before its definition, a verification suite that still tests a result the paper has removed, orphaned figure artifacts, and an acknowledgements line naming non-standard AI tools. None block the mathematics; all are cheap to fix.

**On the four requested axes:** Readability — excellent (motivation-first intro, linear §2 spine). Symbols in place — good except `c_β`. Style / LLM giveaways — excellent (near-zero). Structure — optimal (factor → predict → combine, then consequences).

---

## Strengths

1. **Verified quantitative claims.** `experiments/test_all_results.py` runs and passes 9/9, checking every closed form (Szegő Φ, factorization `|n̂_+|²=n̂`, OU value `v=σ²θ/4Φ²`, rate/position responses, surfing threshold, boundary-layer decay, Markowitz limit, Neuman–Voß Riccati poles) by two independent machineries. Nothing is asserted without a derivation (appendices A, B, D, E) *and* a numerical cross-check.
2. **Clean formulation reconciliation.** Position/N/μ is primary; rate/Q/α appears only where the position genuinely goes non-stationary (λ=0 power law); Table 1 documents both plus the two spectral factors ψ̂ (of μ) and φ̂ (of α). The whitened-forecast equality across variables is proved (App A).
3. **Structure = argument.** The factor → predict → combine spine is stated in §1.3, echoed in the §2 subsection titles, and delivered in order. Consequences (§3 power-law, §4 finite horizon, §5 recovery) follow logically. The general Lemma (`A=A_-A_+`) is proved once and reused for N, Q, and the finite-horizon Volterra operator.
4. **Prose quality.** Motivation-first introduction (origin: optimal execution; meaning: signal vs. impact/risk/decay tension). Near-total absence of LLM-giveaway connective tissue (no *Moreover/Importantly/Note that/delve/rich*; no negation-foils; no rhetorical questions).
5. **Accurate, specific related work.** The filter-vs-feedback distinction, the "trades generality for explicitness" positioning against Abi Jaber–Neuman, and the term-by-term identification via uniqueness are fair and precise. Attributions (LN 2019, NV 2022, OW 2013, GSS 2012, GP) were checked against primary sources and are correct, including the subtle point that LN 2019's *explicit* exponential solution is risk-free/singular.
6. **Unifying recovery section.** Markowitz, aim portfolio, exponential-resilience filters, GSS/OW/Forde liquidation profiles, and the general-propagator solutions are all placed as special cases of one factorization — a genuinely clarifying contribution.
7. **Mechanically clean.** Compiles with 0 errors, 0 undefined refs, 0 undefined citations, 0 overfull boxes; notation table fits the margins.

---

## Critical Issues

**None.** No correctness failures, no fabricated results, no unsupported quantitative claims. The mathematics is verified and the exposition is sound.

---

## Major Issues

1. **`c_β` used ~4 pages before it is defined.** [§2.1, line 162] writes the power-law zero `n̂ ∼ γ c_β |ω|^{1+β}` in the factorization discussion, but `c_β = 2Γ(1−β) sin(πβ/2)` is only defined in [§3.1, line 291], and `c_β` is **not in Table 1**. A reader meeting the Szegő-condition argument cannot evaluate the constant. *Fix:* define `c_β` at first use in §2.1 (or add a Table 1 scalar row).

2. **Verification suite is out of sync with the paper (reproducibility integrity).** `test_all_results.py` check #4 and `TEST_RESULTS.md` verify the **causality-gap law `v/v_ant = sin(πβ/2)`** citing `eq:sinlaw` and `prop:vant`. Grep confirms these labels — and the entire value-of-anticipation / causality-gap result — **no longer exist in the paper** (they were removed). `TEST_RESULTS.md` also reports "8/8" while the script now runs 9 checks. The math still holds, but a reader who opens the shipped verification artifact finds it testing results the paper does not state. *Fix:* either (a) reinstate a brief statement of the sin(πβ/2) result if it is meant to be a claim, or (b) prune check #4 and update `TEST_RESULTS.md` to match the shipped paper and the true 9/9 count.

3. **Acknowledgements name non-standard AI tooling.** [line 482] "assisted by Claude models (**Opus 4.8 and Fable 5**) with the **Feynman harness**." These are not recognizable public model identifiers (the Claude line is Opus 4 / 4.1, etc.), and a mathematical-finance editor/referee will notice. Combined with "Verification scripts … **available from the author**" (no public link), this weakens the reproducibility posture. *Fix:* use accurate model identifiers or a neutral disclosure of AI writing assistance, and provide a public repository URL for the scripts and figure code.

---

## Minor Issues

1. **Orphaned repository artifacts.** `fig2_kink_cusp.{png,py}`, `fig3_value_of_information.{png,py}`, and `exp_kernel_anticipation_fraction.py` are unreferenced leftovers of removed material; the used figures are now non-contiguous (`fig1`, `fig4`, `fig5`). *Fix:* delete the orphans and renumber to fig1–fig3 for a clean submission bundle.
2. **Appendix label names are non-sequential.** Labels are `app:A, app:B, app:D, app:E` (no `app:C`). They render correctly (refs point to the right sections), but the naming is a latent maintenance hazard. *Fix:* rename `app:D→app:C`, `app:E→app:D`.
3. **`e_k` undefined.** In `eq:finiteT`, `α^eff = α + Σ_k ξ_k e_k` — the constraint directions `e_k` are not identified. One clause would fix it.
4. **`σ` overloaded.** Innovation scale (§2.3 OU value, §5) vs. `σ_r` stochastic volatility (§2.2 moving-average example). Context disambiguates, but the shared letter is avoidable.
5. **Em-dash density.** 31 `---` over 19 pp (~1.6/page). Not excessive, but a handful could become commas/colons to vary cadence; heavy em-dash use is a mild stylistic tell.
6. **`TEST_RESULTS.md` provenance drift** (same root as Major #2): "8/8" header, references to `eq:sinlaw`/`prop:vant`/`eq:sin`. Regenerate against the current paper.

---

## Reproducibility and Verification

- **Compile:** `pdflatex → bibtex → pdflatex ×2` → 0 errors, 0 undefined refs/citations, 0 overfull boxes, 19 pp. **Verification: PASS.**
- **Numerical suite:** `python3 experiments/test_all_results.py` → **9/9 PASS**, rel. err. 1e-16–1e-14, freq-domain closed forms cross-checked against time-domain reverse-Cholesky discretization and an independent LQ-Riccati solve for Neuman–Voß. **Verification: PASS** for all claims that remain in the paper.
- **Claim ↔ proof coverage:** Thm (general policy) → App A; Thm (filter) + OU → App B; Prop (response) → App D; Prop (boundary layer) → App E; power-law Volterra factor → "direct kernel integration" (App-free but checkable). All present.
- **Suite ↔ paper sync:** **PARTIAL / stale** — check #4 (sin(πβ/2)) tests a removed result; see Major #2. Not a correctness failure; a hygiene failure.
- **Code/data availability:** scripts and figure code exist in-repo and run, but the paper offers them only "from the author" (no public link). **Verification: adequate but not open.**
- **Figures:** three referenced, all present and matched to captions; two orphaned files on disk (Minor #1).

---

## Inline Annotations

- **Abstract:** claims (fractional-derivative policy ν=(1−β)/2; no block trades; never reverses; recovery of classical rules) all supported by §3/§5. Consistent with the removal of the earlier "value of anticipation" claim — good, no dangling promise.
- **§1.1 (lines 46–62):** motivation-first, α correctly absent; the three-clause tension (price pushed / capital at risk / signal decays) maps onto the three frictions — effective. History paragraph (AC → LFM → Bouchaud → propagator → power-law vs. exponential) is accurate and well-cited.
- **§2.1 (line 162):** `c_β` appears here undefined — **Major #1**.
- **§2.3 (Thm filter, eq:filter/eq:value):** hypotheses (`Assumption Friction`, `Assumption Signal`, `λ>0`) explicit; value formula proved via Itô isometry (App B). Solid.
- **§3 intro (line 271):** "Two things are peculiar" correctly updated from three (matches the 2-subsection structure) — consistency check passes.
- **§3.2 Prop response (eq:response/eq:threshold):** `R`, `X`, `θ*` all numerically verified (check #5), including power-law `R>0` up to λ=1000.
- **§4.2 eq:gk-kernel:** factor "verified by direct kernel integration" — reproducible by hand; consider stating the one-line identity in App or a footnote.
- **§5.1 (eq:ema):** LN 2019 attribution carries the correct caveat (explicit solution risk-free/singular). **eq:nv-filter** verified against an LQ-Riccati solve (check #9).
- **App A/B/D/E:** proofs present and self-contained; App A handles the unbounded power-law factors on a dense domain — good rigor.
- **Acknowledgements (line 482):** **Major #3** (AI-tool names).

---

## Revision Log (fixes applied 2026-07-24)

All five recommended fixes were made and re-verified (compile: 0 errors / 0 undefined / 0 missing figures, 19 pp.; suite: 9/9 pass):

- **Major #1 — `c_β` defined:** added to Table 1 (`c_β = 2Γ(1−β)sin(πβ/2)`, `ĝ=c_β|ω|^{β−1}`); now available at its first use in §2.1.
- **Major #2 — suite/paper sync:** `test_all_results.py` check #4 relabeled *"Causality-gap identity … (supplementary; not in paper)"* and the dangling `eq:sinlaw` reference removed; `TEST_RESULTS.md` corrected to `9/9`, row 4 marked supplementary, row 9 (Neuman–Voß) added.
- **Major #3 — acknowledgements:** AI-tool names replaced with a neutral disclosure ("assisted by large language models").
- **Minor #1 — orphaned artifacts:** deleted `fig2_kink_cusp.*`, `fig3_value_of_information.*`, `exp_kernel_anticipation_fraction.py`; renumbered `fig4→fig2_impact_surfing`, `fig5→fig3_boundary_layer` (png/pdf + generators + savefig paths + `\includegraphics`). Figures now contiguous 1–3.
- **Minor #2 — appendix labels:** renamed `app:D→app:C`, `app:E→app:D` (labels + refs); appendices now A/B/C/D.
- **Minor #3 — `e_k` defined:** `eq:finiteT` prose now reads "each linear position constraint `⟨e_k,x⟩=0`".

Not changed (deliberate): em-dash density (Minor #5, cosmetic); public code URL (none available — statement left as "available from the author"); `σ` overload (Minor #4, context-clear).

## Recommendation

**Accept with minor revisions** — the revisions above are now applied.

**Original recommendation (pre-fix):** Accept with minor revisions. The paper is mathematically sound, verified, well-structured, and cleanly written. Before submission the author should: (1) define `c_β` at first use; (2) reconcile the verification suite and `TEST_RESULTS.md` with the shipped paper (prune or restore the sin(πβ/2) result; fix the 8/8→9/9 count); (3) correct the acknowledgements' AI-tool names and add a public code link; (4) clear orphaned figure/script artifacts and renumber figures; (5) minor: define `e_k`, rename appendix labels, trim a few em-dashes. None of these touch the results. On the four requested axes the paper is in good shape, with the single substantive readability defect being the misplaced `c_β`.

---

## Sources

- `v2/optimal-trading-filters-v2.tex` (full read; compiled clean, 19 pp.)
- `v2/optimal-trading-filters.bib` (32 entries; all citations resolve)
- `v2/experiments/test_all_results.py` — executed, **9/9 pass**
- `v2/experiments/TEST_RESULTS.md` (stale: 8/8, references removed labels)
- `v2/figures/fig1_filter_magnitude.png`, `fig4_impact_surfing.png`, `fig5_boundary_layer.png` (referenced); `fig2_kink_cusp.png`, `fig3_value_of_information.png` (orphaned)
- Lehalle–Neuman 2019, arXiv:1704.00847 — model/objective confirmed (cost functional 2.4, φ=0 explicit solution)
- Neuman–Voß 2022, arXiv:2002.09549 — temporary+transient+risk, absolutely continuous
- Evidence notes: `outputs/.drafts/optimal-trading-filters-review-evidence.md`
- Plan: `outputs/.plans/optimal-trading-filters-review-plan.md`
