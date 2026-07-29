# v3 Round-1 Style / Exposition Review — Optimal Trading Filters

**Artifact:** `v3/optimal-trading-filters-v3.tex` (504 lines)
**Angle:** traditional academic mathematical-finance register (no equation-narration; no math/abstract-noun as subject of action verb; transitions; abstract contribution; §2 spine and §2.3 density; AGENTS.md cadence; figure captions)
**House style source:** `notes/v3-exposition-plan.md` (the repo's `AGENTS.md` is a broken self-reference — its byte content is literally `@AGENTS.md`; the governing rules live in the exposition plan and were used here).

Overall: v3 is a clean post-edit draft. The A1–A6 equation-restatement conversions from the exposition plan have been applied (the "collects", rate-factor narration, and denominator/numerator gloss are gone; "two shapes bracket" is gone). Cadence is disciplined: no throat-clearing, no rhetorical questions, no empty intensifiers, no negation-foils, no over-signposting. The residual issues are (i) a handful of math-expression / abstract-noun subjects that survived the sweep, (ii) the density of §2.3 "The trading filter", and (iii) em-dash count slightly over the house budget. No blockers.

---

## Summary

The paper solves an adapted quadratic optimal-trading problem (gain vs. temporary/transient impact and inventory risk) by Wiener–Hopf factorization of the friction operator, giving a closed-form "trading filter" on the whole line, a fractional-derivative policy and a $\sin(\pi\beta/2)$ causality gap under power-law impact, a finite-horizon Gohberg–Krein version, and recovery of the classical portfolio/execution rules. This review addresses exposition, style, and structure only; correctness/citation-accuracy is out of scope.

---

## BLOCKERS
None. Nothing in the exposition is broken, self-contradictory, or misleading at the style level.

---

## FIXES-WORTH-DOING-NOW

### F1. Math-expression / abstract-noun as subject of an action verb (residual offenders)
The sweep in the exposition plan (rule B) missed these main-body instances. Each has a math object or abstract noun driving an interpretive action verb; convert to a property statement, a process-noun subject, or passive.

- **§1.2, L83** — "$(Nx)(t)$ integrates the position over the past *and the future*." Bare math expression as subject of "integrates."
  Suggest: "so that $Nx$ at time $t$ *depends on* the position over the past *and the future*" (property, not action).

- **§3 intro, L297** — "This memory *shapes* the optimum in three ways." Abstract noun "memory" driving "shapes."
  Suggest: "The optimum *reflects* this memory in three ways:" or "This memory is *felt* in the optimum in three ways:".

- **§4 caption region / §6, L422 and L465** — "the memory of the impact *sets* the shape of the policy" (appears twice, incl. the concluding-remarks sentence). Abstract noun "memory" as subject of "sets."
  Suggest (passive/nominalized): "the shape of the policy is *set by* the impact memory" or "the policy's shape *follows* the impact's memory."

- **§2.3, L227** — "Only the friction's factor *whitens* the signal, the signal's own spectral factor entering through the projection alone." Object-noun subject + "whitens." (Also mildly imprecise: the factor whitens the *return*, not "the signal" in general.)
  Suggest: "Only the friction's factor *enters the whitening*; the signal's own spectral factor *enters through the projection alone*."

- **§3.1, L328** — "The integral *amplifies* low frequencies, $|(-i\omega)^{-(1+\beta)/2}|^2=|\omega|^{-(1+\beta)}$, so the position has spectral density …". Math object "the integral" as subject of "amplifies."
  Suggest: "*Low frequencies are amplified*, $|(-i\omega)^{-(1+\beta)/2}|^2=|\omega|^{-(1+\beta)}$, so the position has spectral density …".

- **§1.3, L100** — "the causal factor *builds* the optimal trade" / "the causal factor *builds* the innovations representation." Object-noun subject + "builds," twice in the parallel construction. This one is stylistically deliberate (nice prediction/trading parallel), so it is borderline; if the register is to be enforced uniformly, nominalize: "the innovations representation is *built from* the causal factor … the optimal trade *from* the friction's factor." Keep only if the parallelism is judged worth the exception.

### F2. §2.3 "The trading filter" is over-dense — apply plan item C4
The subsection currently carries, in order (envs confirmed at L203/212/216/229/233/241/247): Lemma → Remark(nest) → Theorem(general) → Remark(wk) → Remark(duality) → **Assumption(signal)** → Theorem(filter), while **Assumption(friction)** sits separately up in §2.1 (L177). That is one Lemma, two Theorems, three Remarks, and an Assumption in a single subsection, with the two standing hypotheses split across two subsections and interleaved with results — exactly the density the exposition plan's C4 flags.
Recommend: move **Assumption(signal)** (and, for symmetry, keep **Assumption(friction)**) into a single "standing hypotheses" paragraph in the §2 setup, so §2.3 runs Lemma → Remark(nest) → Theorem(general) → reading → Theorem(filter) → Markov/OU without the assumption interruption before the second theorem.

### F3. Relocate Remark 3 (nonanticipativity multiplier) to §2.4
Remark(duality) (L233) is *used* only in §2.4 — it is cited there ("by Remark~\ref{rmk:duality}", L281) and it closes forward-pointing to "the shadow price of information of §2.5 below." Placing it as the third back-to-back remark before Theorem(filter) is what makes §2.3 feel congested. Moving it to the head of §2.4 (value of information), where $\xi^\star$ actually does work, both thins §2.3 and puts the remark next to its application. Remark(nest) after the Lemma and Remark(wk) after the Theorem(general) reading are well placed; leave them.

---

## OPTIONAL

### O1. Em-dash density above house budget
Body has **38** em-dashes (`---`) vs the plan's ~30 target (D3). Densest offenders: **L368 (7 dashes / three paired asides)**, **L108 (3)**, **L422 (3)**. A light pass folding paired parenthetical asides into commas or parentheses — L368 in particular ("A block trade --- a jump in the position ---", "The first two separate the kernels --- … ---", "The frictions omitted here --- spread, position limits, order discreteness ---") — would bring the register down without cost to clarity.

### O2. §2.4 "the impact tempers … separates the frictions" (L281)
"how *the impact tempers* the resulting growth *separates* the frictions" chains an object-noun action subject ("the impact tempers") into a clause subject ("separates the frictions"). Reads slightly mechanical.
Suggest: "… a proportionally larger expected return, $\mu=\theta\alpha$, and the frictions *differ in how they temper* the resulting growth (Figure~\ref{fig:value}a)."

### O3. Intro roadmap placement (plan C1)
The roadmap paragraph sits at the end of §1.3 (L102), so the introduction closes on a technical related-work point (§1.4 ends on the Neumann-expansion identification, L108+). Moving the roadmap sentence to the end of §1.4 would let the introduction close on the plan of the paper. Low priority; the current order is defensible.

### O4. §1.3 Cholesky aside (plan C2)
"The finite-dimensional analogue is the Cholesky factorization of a positive matrix into triangular factors, computed by Gram–Schmidt along the coordinate order." Illuminating but the one place §1.3 slows; can be shortened to "The finite-dimensional analogue is Cholesky factorization along the coordinate order."

### O5. Abstract middle list (plan D2)
The abstract is one long paragraph (fine for the genre) but the middle enumeration ("It reduces to the Markowitz rule … rational frictions give filters …") could shed one sentence. Low priority.

### O6. Figure caption micro-nit — `fig:value`(a)
"Value rate $v(\theta)$ against signal speed at fixed appreciation variance (normalized to $\theta=1$)" — the parenthetical is ambiguous about *what* is normalized at $\theta=1$ (the value, or the fixed-variance reference point). Clarify: "… at fixed appreciation variance, values normalized to their $\theta=1$ level."

---

## IGNORE / DEFER

- **"X gives / forces / reads" in derivations and proofs** (L193 tower property "forces"; L263 "the single pole … gives"; Appendix L473–490 "$A_+$ gives", "$P_+$ truncates", "$\hat q_-$ gives", etc.). These are standard derivational register in appendix proofs, not the interpretive-action offenders the directive targets. Leave.
- **"the optimal rate runs against the signal to ride that residual"** (L355/L359, impact surfing). "The rate runs / rides" is behavioral description of the trade, reads naturally, and is central to the section's picture. Acceptable; do not mechanically convert.
- **"the same filter reads on the observed signal" / "the policy … reads" / "the rate policy … then reads"** (L259/L299/L317). "X reads [as]" = "is written as" is accepted mathematical idiom; the plan's C5 concern about informal "reads" does not bite here.
- **Cadence checks** — no throat-clearing ("note that", "recall that", "it is important"), no rhetorical questions, no empty intensifiers ("very/highly/remarkably/crucially"), no negation-foils ("not X but Y"), no over-signposting ("as we will see"). Grep-confirmed clean. Nothing to do.
- **Equation-restatement prose** — the flagged v2 patterns (denominator/numerator gloss, "collects", rate-factor post-colon narration) are gone; A1–A6 applied. The surviving post-display sentences state significance/use, not contents. Nothing to do.
- **Abstract contribution** — explicit "we compute it in closed form …" set against "Existing treatments characterize the adapted optimum implicitly," accurate to the body. Good; no change.
- **Figure captions** — all five carry their parameters and define their curves; self-contained. Only the O6 micro-nit noted.

---

## Verdict
Style/structure is in good shape and close to submission register for the genre. The revision risk is low and concentrated: enforce the math-as-subject rule on the ~6 residual F1 sites, thin §2.3 by relocating Assumption(signal) and Remark(duality) (F2–F3), and trim em-dashes (O1). None of these touch content or correctness. Confidence: high on the style findings (direct line-level evidence); the density judgment (F2/F3) is a considered editorial recommendation aligned with the repo's own exposition plan, not a defect.

## Revision Plan (priority order)
1. **F1** — convert the six math/abstract-noun subjects (L83, L227, L297, L328, L422, L465; L100 optional) to property/passive/process-noun forms. Local, low risk.
2. **F2** — move Assumption(signal) into the §2 standing-hypotheses paragraph; re-check `\ref{ass:signal}` in Theorem(filter) and Appendix B.
3. **F3** — relocate Remark(duality) to the head of §2.4; re-check the `\ref{rmk:duality}` citation at L281.
4. **O1** — em-dash pass, starting with L368.
5. **O2–O6** — polish as time allows.
Recompile (pdflatex ×2, 0 errors / 0 undefined) after steps 1–3.

---

## Inline Annotations

> "so that $(Nx)(t)$ integrates the position over the past \emph{and the future}, and adaptedness … becomes binding" — §1.2, L83
**[F1]:** Bare expression `$(Nx)(t)$` as subject of "integrates." Convert to a property: "so that $Nx$ at time $t$ *depends on* the position over the past and the future."

> "In the trading problem the factored symbol is the \emph{friction} $N$, and the causal factor builds the optimal trade … the causal factor builds the innovations representation" — §1.3, L100
**[F1]:** "the causal factor builds …" (×2) — object-noun subject + action verb. Deliberate parallelism; if enforcing the rule uniformly, nominalize/passivize. Otherwise flag as a knowing exception.

> "Only the friction's factor whitens the signal, the signal's own spectral factor entering through the projection alone." — §2.3, L227
**[F1]:** Object-noun subject "the friction's factor" + "whitens"; also imprecise (it whitens the return). Suggest: "Only the friction's factor enters the whitening; the signal's own spectral factor enters through the projection alone."

> "This memory shapes the optimum in three ways: the policy is a fractional derivative …" — §3, L297
**[F1]:** Abstract noun "memory" as subject of "shapes." Suggest: "The optimum reflects this memory in three ways:".

> "The integral amplifies low frequencies, $|(-i\omega)^{-(1+\beta)/2}|^2=|\omega|^{-(1+\beta)}$, so the position has spectral density …" — §3.1, L328
**[F1]:** "The integral amplifies …" — math object as subject. Suggest: "Low frequencies are amplified, …".

> "Figure~\ref{fig:structure} shows how the memory of the impact sets the shape of the policy across this family." — §4, L422; and "The memory of the impact sets the shape of the policy:" — §6, L465
**[F1]:** "the memory … sets the shape" (×2), abstract-noun action subject. Suggest passive: "the shape of the policy is set by the impact memory."

> Envs L203→L247: Lemma → Remark(nest) → Theorem(general) → Remark(wk) → Remark(duality) → Assumption(signal) → Theorem(filter); Assumption(friction) separately at L177 — §2.3 "The trading filter"
**[F2]:** One Lemma, two Theorems, three Remarks, one Assumption in one subsection, with the two standing hypotheses split and interleaved. Move Assumption(signal) into the §2 setup so §2.3 runs Lemma → Remark(nest) → Theorem(general) → reading → Theorem(filter).

> "\begin{remark}[The nonanticipativity multiplier]\label{rmk:duality} … the shadow price of information of \S\ref{sec:value} below." — §2.3, L233
**[F3]:** This remark is used only in §2.4 (cited at L281) and points forward to §2.4/§2.5. Relocate to the head of §2.4 to thin §2.3 and sit beside its application.

> "A block trade --- a jump in the position --- pays a transient-impact cost … The first two separate the kernels --- the power law … --- and the third is ruled out … The frictions omitted here --- spread, position limits, order discreteness --- would temper the reversal" — §3.2, L368
**[O1]:** Seven em-dashes in one paragraph (three paired asides). Fold at least one aside into parentheses/commas. Body total is 38 vs the ~30 house budget.

> "how the impact tempers the resulting growth separates the frictions (Figure~\ref{fig:value}a)" — §2.4, L281
**[O2]:** Chained action subjects ("the impact tempers" → clause "separates the frictions"). Suggest: "the frictions differ in how they temper the resulting growth (Figure~\ref{fig:value}a)."

> "Value rate $v(\theta)$ against signal speed at fixed appreciation variance (normalized to $\theta=1$)" — caption `fig:value`(a)
**[O6]:** Ambiguous antecedent for "normalized to $\theta=1$." Clarify what is normalized (values to their $\theta=1$ level).

---

## Sources
No external sources inspected; this is a self-contained exposition/style pass over the local artifact and the repo's `notes/v3-exposition-plan.md`.
