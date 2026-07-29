# Clarity & Structure Review — Plan

## Artifact
- **Identifier:** `v2/optimal-trading-filters-v2.tex` (working title *Optimal Trading Filters: a Wiener–Hopf Approach*)
- **Source type:** local LaTeX source (compiles to 18-page PDF `v2/optimal-trading-filters-v2.pdf`)
- **Domain:** applied mathematics / quantitative finance (optimal trading with market impact via Wiener–Hopf factorization)
- **Scope of this review:** clarity of exposition and structure ONLY. Not a novelty/correctness audit (those exist separately in `outputs/optimal-trading-filters-v2-review.md`). Where a clarity problem also touches correctness, note it but stay in the clarity lane.

## Review criteria (clarity/structure emphasis)
- **Global structure:** section ordering, does the arc (problem → interior solution → power-law → finite horizon → recovery → conclusion) build logically; are the subsection splits natural.
- **Signposting:** roadmap in §1, forward/backward references, transitions between sections/subsections.
- **Notation hygiene:** is notation introduced before use; is the notation table complete/consistent; are the two signals (α vs μ) kept distinct; operator/kernel/filter conventions consistent.
- **Definitions & theorems:** are objects defined before invoked; are theorem/prop statements self-contained; are proofs correctly deferred to appendices.
- **Local exposition:** paragraph topic sentences, register consistency, throat-clearing, rhetorical foils (per project AGENTS.md style rules), equation-dump vs interpretation balance.
- **Abstract/intro alignment:** does the abstract match the body claims; does the intro promise what the body delivers.
- **Figures/tables:** are figures referenced, captioned, and placed near their discussion; is every figure discussed.
- **Reference integrity (clarity-relevant):** dangling refs, forward references that assume undefined objects, consistency of cross-references after recent restructuring.

## Verification checks
- Compile check: `pdflatex` ×2, confirm 0 errors / 0 undefined refs / 0 multiply-defined labels.
- Cross-reference audit: every `\ref`/`\eqref` resolves; every `\label` used; no orphan labels that suggest deleted content.
- Notation-first-use audit: symbols in the notation table vs first textual use; spot-check α/μ, Q/N/Φ, ν, c_β, χ.
- Figure audit: each `fig:*` is `\ref`'d in text and discussed; captions self-contained.
- Section-order sanity: read the section/subsection skeleton; check the recent §2 (mean-reverting subsection insertion) and §4 (finite-horizon restructure) for residual seams.
- Abstract vs body: check each abstract claim maps to a body section.

## Method
- Lead-owned review (artifact ~18pp, reviewer has full session context on it). No subagent delegation (would add overhead, not accuracy).
- Read full `.tex` from disk; extract skeleton; run compile + ref audits via shell; write evidence notes; then final review.

## Deliverables
- `outputs/.plans/optimal-trading-clarity-review-plan.md` (this file)
- `outputs/.drafts/optimal-trading-clarity-review-evidence.md`
- `outputs/optimal-trading-clarity-review.md`
