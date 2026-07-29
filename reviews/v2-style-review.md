# Style Review — `v2/optimal-trading-filters-v2.tex`

Scope: style-only pass against `AGENTS.md`. No content/math judgment; no edits made to the `.tex`.
Reviewed file: `/Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/v2/optimal-trading-filters-v2.tex`
Rules file: `/Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/AGENTS.md`

Overall the prose is clean on the highest-frequency `AGENTS.md` violations: **no rhetorical questions, no hortative openers ("let us", "we now turn", "notice that"), and no throat-clearing ("importantly", "interestingly", "it is well known")** appear anywhere. The main style debts are (1) several **sentence-style section/subsection titles** that a math-finance journal would prefer as noun phrases, and (2) a recurring **self-promotional framing tic** ("is the subject of the paper", "the quantitative content of the thesis", "Everything downstream rests on..."). Both are easy to fix.

---

## 1. Section and subsection titles — keep / revise

Every `\section` and `\subsection` title, in document order. `\paragraph` sub-headings (`Temporary impact alone.`, `Power-law impact alone.`) are noun phrases and are fine.

| # | Level | Title (as written) | Verdict | Severity | Issue / suggested replacement |
|---|-------|--------------------|---------|----------|-------------------------------|
| 1 | section | Introduction | **keep** | — | — |
| 2 | subsec | The gain--risk--cost problem | **keep** | — | Clean noun phrase. |
| 3 | subsec | Adaptedness is the binding constraint | **revise** | high | Full declarative sentence (subject+verb), flagged by author. → **"The adaptedness constraint"** or **"Adaptedness as the binding constraint"**. |
| 4 | subsec | One factorization, computed in frequency where possible | **revise** | med | Wordy/casual, comma-spliced clause with a hedge ("where possible"). → **"A single factorization"** or **"The factorization and its computation"**. |
| 5 | subsec | Relation to earlier work | **keep** | — | Standard math-finance heading. |
| 6 | section | The interior solution | **keep** | — | — |
| 7 | subsec | Setup and factorization | **keep** | — | — |
| 8 | subsec | The projected inverse and the general policy | **keep** | — | — |
| 9 | subsec | The stationary trading filter | **keep** | — | — |
| 10 | section | Pure impact is fractional calculus | **revise** | high | Full declarative sentence — same casual register as #3. → **"Pure power-law impact as fractional calculus"** or **"Fractional calculus of pure power-law impact"**. |
| 11 | section | Exponential versus power-law: short versus long memory | **revise** | med | Doubled "versus" reads awkwardly in a title. → **"Exponential and power-law kernels: short versus long memory"**. |
| 12 | subsec | The optimal trade inherits the impact memory | **revise** | med | Declarative sentence. → **"Memory of the optimal trade"** or **"Impact memory and the optimal policy"**. |
| 13 | subsec | The value of anticipation grows with memory | **revise** | med | Declarative sentence. → **"The value of anticipation"** (memory dependence is the section's content) or **"Anticipation value and impact memory"**. |
| 14 | subsec | The direction of the optimal flow | **keep** | — | Noun phrase; fine (but see "flow" vs "rate" terminology note §3). |
| 15 | section | Boundaries: the same factorization without Fourier | **revise** | med | Casual subtitle ("without Fourier"); "Boundaries" alone is vague. → **"Finite horizons: factorization without translation invariance"** or **"The finite-horizon factorization"**. |
| 16 | subsec | Finite-horizon computation | **keep** | — | — |
| 17 | subsec | Boundary-layer decay | **keep** | — | — |
| 18 | subsec | Recovery of earlier solutions | **keep** | — | — |
| 19 | section | Numerical verification | **keep** | — | — |
| 20 | section | Concluding remarks | **keep** | — | — |

Titles to change: **#3, #4, #10, #11, #12, #13, #15** (7 of 20). The three highest-priority are the full-sentence titles **#3, #10** and the parallel declaratives **#12, #13**; fixing all four together restores a consistent noun-phrase register across the paper.

---

## 2. `AGENTS.md` prohibitions

| # | Location (section + first words) | Quoted passage | Prohibition | Severity | Suggested rewrite |
|---|----------------------------------|----------------|-------------|----------|-------------------|
| P1 | §1.1 "The gain--risk--cost problem" (last sentence) | "…reconciling that atemporal optimum with the information actually in hand **is where the work of the paper lies**." | Self-promotional framing | med | "The signal path is revealed only as time passes; the adapted problem is to reconcile that atemporal optimum with the information in hand." (drop the clause) |
| P2 | §1.3 "One factorization…" (last sentence) | "**Working out this one object, and following where it leads, is the subject of the paper.**" | Self-promotional framing ("is the subject of the paper") | med | "The remaining sections work out this object and its consequences." — or delete; the section list that precedes it already carries the information. |
| P3 | §2.2 "The projected inverse…" (first sentence) | "**Everything downstream rests on a single identity:** the adapted inverse of $Q$… factors cleanly through the two triangular factors…" | Self-promotional / dramatic framing | med | "The adapted inverse of $Q$ that \eqref{eq:foc} requires factors through the two triangular factors with the projection threaded between them." (also drop "cleanly", P8) |
| P4 | §4.2/boundary — actually §5.2 "Boundary-layer decay" | "**This proposition is the quantitative content of the thesis:** the finite-interval factor \eqref{eq:gk-kernel} coincides with the stationary Szegő factor…" | Self-promotional framing ("the thesis") | med | "The finite-interval factor \eqref{eq:gk-kernel} coincides with the stationary Szegő factor \eqref{eq:szego} up to a boundary layer, whose width is $\sim1/b_1$ for a rational kernel…" |
| P5 | §3 "Pure impact…", Power-law paragraph | "Theorem~\ref{thm:general} **then reads**" (introducing \eqref{eq:fractional}) | "the formula reads/says" opener | low-med | "Theorem~\ref{thm:general} **specializes to**" or "**becomes**". (Note §2.3 already uses "becomes a transfer function" — align to that.) |
| P6 | §2.2, sentence after Thm 1 | "The policy has three steps **with a clear reading.**" | Self-promotional / "the interpretation is direct" variant | low-med | "The policy has three steps." (Then describe them; the three-clause sentence that follows already does the "reading".) |
| P7 | §3 "Pure impact…" (opening sentence) | "**The interpolation carried by the filter is clearest at its two ends.**" | Mild weight/burden metaphor ("carried by") + empty intensifier ("clearest") | low | "The filter interpolates between two limits, both explicit: memoryless trading at one end, a fractional derivative at the other." |
| P8 | §2.2 first sentence | "…factors **cleanly** through the two triangular factors…" | Empty intensifier | low | Delete "cleanly". |
| P9 | §3, Temporary-impact paragraph | "**There is no memory, because** the cost prices the instantaneous rate only…" | Mild negation-first phrasing | low | "The rate has no memory: the cost prices the instantaneous rate only, and each instant is a separate problem." |
| P10 | §1.4 "Relation to earlier work" | "…at a cost of order $n^2$ **that must be paid afresh for each parameter set**. The factorization instead returns the solution operator **once and for all**…" | Borderline disparagement-by-implication (burden framing) | low | Factual and largely acceptable; if softening: "…at a cost of order $n^2$ per parameter set. The factorization returns the solution operator once: on the whole line the optimal trade is a fixed convolution filter…" |
| P11 | §4.3 "The direction of the optimal flow" (final sentence) | "…so the prediction should be read within the model **rather than** as a standalone recommendation." | Mild "rather than" foil (used as hedge) | low | Acceptable as a caveat; optional: "…so the prediction holds within the model; omitted frictions (spread, position limits, tick size) would temper it." |

**Not found (clean):** rhetorical questions; the "X is not Y, it is Z" / "This is not X — it is Y" foil in its strong form; the "canonical / genuine / true / essential / deep / structural-as-decoration / the point of" intensifier list; "we now turn / let us / notice that"; "it is worth noting / importantly / interestingly / it is well known". The negation-summary tic ("Sign flips are cost-optimal, not diagnostic errors") is also avoided — §4.3 correctly states "the reversal is a cost-optimal response within the model class" positively.

---

## 3. General prose — awkward/overlong sentences, terminology, hedging

| # | Location (section + first words) | Issue | Severity | Suggestion |
|---|----------------------------------|-------|----------|------------|
| G1 | §1.4 "Relation to earlier work", paragraph beginning "\citet{AbiJaberNeuman2025} treat general propagators…" | Single ~11-line paragraph packing (a) the AbiJaber–Neuman comparison, (b) the on-$[0,T]$ agreement claim, and (c) the $O(n^2)$-vs-filter cost argument. Reads as three arguments fused. | med | Split into two paragraphs at "Summing that series in closed form is also what makes the factorization cheap to evaluate." The first stays on representation equivalence; the second on computational cost. |
| G2 | Throughout §4 vs §2/§3 | **Terminology drift: "flow" vs "rate".** The trade rate $u$ is called "the rate" (§2, §3, notation table "trade (rate) filter") but "the flow" in §4.3 ("direction of the optimal flow", "flow response $R$", "the optimal flow trades against the signal"). Two words for one quantity. | med | Pick one primary term. If "flow" is the intended execution word for direction, add one gloss at first use ("the trade rate, or flow") and use it consistently; otherwise standardize on "rate". |
| G3 | §2.3, §3, §4.2, §7, abstract | **Benchmark naming drift** for the perfect-information value: "anticipative", "perfect-foresight" (notation table), "perfect anticipation" (§2.3), "full foresight" (abstract, §7), "knowing the whole signal path" (§4.2). | low | Fix one label (e.g. "anticipative / perfect-foresight") and use it at every mention; the notation table already sets `$v_{\rm ant}$ = anticipative (perfect-foresight)`. |
| G4 | §2.2 "the value forgone to adaptedness", §4.2 "value forgone… causality gap", §4.2 "value of anticipation", Remark 1 "shadow price of information" | **Multiple labels for $v_{\rm ant}-v$**: "causality gap", "value forgone", "value of anticipation", "shadow price of information". A reader must infer these coincide. | low-med | Name the quantity once ("the causality gap $v_{\rm ant}-v$"), then reuse; reserve "shadow price of information" for the Remark 1 multiplier identity where it is technically distinct. |
| G5 | Table 1 "temporary-impact weight" vs §1.1/§3 "temporary cost" / "temporary-impact cost" | Minor inconsistency between "temporary cost" and "temporary impact". | low | Standardize (e.g. "temporary-impact cost" everywhere the cost term is meant). |
| G6 | Abstract "Anticipation is worth more the longer the memory; …$\sin(\pi\beta/2)$… vanishing as the impact approaches permanence ($\beta\to0$)." and §7 "Anticipation is worth more the longer the memory; …$\sin(\pi\beta/2)$… vanishing as the impact approaches permanence ($\beta\to0$)." | Abstract and Concluding-remarks sentences are near-verbatim identical. Acceptable, but the duplication is conspicuous within a short paper. | low | Vary the conclusion phrasing, or let the conclusion state the consequence rather than restate the abstract sentence. |
| G7 | §1.1 "The signal path is revealed only as time passes, **however**,"; §4 "They differ, **however**, in the memory"; §1.3 usage | Mid-sentence "however" appears as a stylistic tic across several transitions. Not prohibited, but noticeable in a paper this length. | low | Convert one or two to leading declaratives without the connective. |
| G8 | §5.1 "Finite-horizon computation", sentence "For the cost operator on $[0,T]$ --- $\eta I$ plus a continuous-kernel integral operator, together with the explicit power-law factor below --- Lemma~\ref{lem:pi} and Theorem~\ref{thm:general} apply verbatim with these factors," | Long sentence with a nested em-dash aside that separates subject from verb ("For the cost operator… apply verbatim"). Parses on a second read. | low | Break the aside out: "The cost operator on $[0,T]$ is $\eta I$ plus a continuous-kernel integral operator (with the explicit power-law factor below). Lemma 1 and Theorem 1 apply verbatim to its factors:" |

---

## Priority summary

1. **High:** Retitle the full-sentence headings — §1.2 `Adaptedness is the binding constraint` (author-flagged), §3 `Pure impact is fractional calculus`, and the parallel declaratives §4.1/§4.2 (`The optimal trade inherits the impact memory`, `The value of anticipation grows with memory`). Table §1 gives drop-in noun-phrase replacements.
2. **Medium:** Remove the four self-promotional framings P1–P4 ("is where the work of the paper lies", "is the subject of the paper", "Everything downstream rests on a single identity", "the quantitative content of the thesis"); retitle §1.3, §4, §5. Resolve the "flow" vs "rate" terminology split (G2).
3. **Low:** P5–P11 wording touch-ups, the terminology-consistency items G3–G7, and the long-sentence/paragraph breaks G1, G8.

No dead-end material (failed ansatzes, negative explorations) is present in the paper body — the `AGENTS.md` "no dead ends in the paper" rule is satisfied.

---

## Sources

- `/Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/AGENTS.md` (project style rules)
- `/Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/v2/optimal-trading-filters-v2.tex` (reviewed manuscript)

No external/web sources were consulted; this is a style pass against the in-repo rules only.
