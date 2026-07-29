# v3 exposition improvement plan — clarity, structure, style

Target file: `v3/optimal-trading-filters-v3.tex`. Goal: traditional academic register; equations state themselves; no math expressions (or abstract nouns) as sentence subjects performing interpretive actions; tighter transitions.

## Governing rules (from the directive)

1. **Do not narrate equations.** After a display, state its *significance* or *use*, not its contents. Cut sentences of the form "the operator collects…", "a filter with X in the denominator and Y in the numerator", "one time-integration on each side, $\hat q_\pm=\dots$: the causal integration composes with $N_+$…".
2. **No math expression as grammatical subject of an action.** Forbidden subjects: bare symbols ($N_+$, $P_+$, $N_-^{-1}$, $\hat n$) and abstract placeholders ("two shapes") driving verbs like *turns, whitens, replaces, integrates, brackets, acts*. Allowed subjects, in order of preference: (a) the trader / we; (b) a named operation as a process noun ("the whitening", "the projection", "conjugation", "differentiation"); (c) passive voice; (d) "Equation (n)" / "the factorization". Property statements ("$\hat n$ vanishes at $\omega=0$", "$\hat\psi$ is analytic") are fine — those are states, not actions.
3. **Register.** Prefer measured, impersonal phrasing over punchy short sentences with a symbol subject. Reduce em-dash asides (fold into subordinate clauses). Keep one interpretive reading per result, stated once, nominalized.

## A. Equation-restatement to cut or convert (priority)

**A1. §1.2 — "collects".**
- Now: "The \emph{friction operator} $N$ collects the three costs referred to the position, $N=-\eta\partial_t^2-\gamma\partial_t^2(g\ast)+\lambda I$, with Fourier symbol …"
- To: "Referred to the position, the three costs define a single \emph{friction operator} $N=-\eta\partial_t^2-\gamma\partial_t^2(g\ast)+\lambda I$, with Fourier symbol …"

**A2. §2.1 — whitening (also math-as-subject).**
- Now: "Applying such a factor is a \emph{whitening}: $N_+$ turns the friction inner product $\langle\cdot,N\cdot\rangle$ into the flat $L^2$ one."
- To: "Conjugation by such a factor whitens the friction: under it the inner product $\langle\cdot,N\cdot\rangle$ becomes the flat $L^2$ product."

**A3. §2.1 — rate factors narration (cut the post-colon clause).**
- Now: "The rate-referred factors follow by assigning one time-integration to each side, $\hat q_\pm=\hat n_\pm/(\mp i\omega)$: the causal integration $1/(-i\omega)$, the map from rate to position, composes with $N_+$, and its anticausal adjoint with $N_-$."
- To: "The rate-referred factors carry one time-integration on each side, $\hat q_\pm=\hat n_\pm/(\mp i\omega)$."  (drop the narration; the map rate→position is already Table 1.)

**A4. §2.3 — the three-operations paragraph (the central offender).**
- Now: "The policy is three operations in sequence. The anticausal $N_-^{-1}$ whitens the expected return by the friction factor, calling for its future path; the projection $P_+$ replaces that future by the forecast of \S2.2, leaving the $\F_s$-measurable whitened forecast $\zeta_s$; the causal $N_+^{-1}$ integrates $\zeta$ over the past into the position. Completing the square reads the same policy as an estimate: …"
- To: "The three factors in \eqref{eq:policy} are the three steps of the classical recipe: an anticausal whitening, the adapted projection, and a causal recolouring. The whitening would call for the future of the signal; the projection supplies instead its forecast (\S\ref{sec:meanrev}). Only the friction's factor whitens the signal, the signal's own spectral factor entering through the projection alone. Completing the square gives a second reading. Up to a constant the objective \eqref{eq:objective} equals $-\tfrac12\|x-N^{-1}\mu\|_N^2$ in the friction norm $\|y\|_N^2=\E\langle y,Ny\rangle$, so that $x^\star$ is the orthogonal projection, in that norm, of the anticipative optimum $N^{-1}\mu$ onto the adapted positions — the causal Wiener–Kolmogorov estimate of the whitened return from the past."
- (Keeps the interpretation; removes symbol-subjects; nominalizes the three steps.)

**A5. §2.3 — stationary-filter setup (math-as-subject + "conditional expectation truncates").**
- Now: "For a stationary signal the projection is itself a filter. The whitened return $N_-^{-1}\mu$ is the stationary filter of the innovations $\dot W$ with symbol $h:=\hat\psi\hat n_-^{-1}$; conditional expectation truncates its moving-average kernel at lag zero, so $P_+$ acts on symbols as the Riesz projection $[\cdot]_+$ onto non-negative lags, and \eqref{eq:policy} becomes a transfer function."
- To: "For a stationary signal the projection is itself a filter. In the innovations $\dot W$ the whitened return has symbol $h:=\hat\psi\hat n_-^{-1}$; since conditioning at time $s$ discards the innovations after $s$, the projection truncates the moving-average kernel at lag zero and acts on symbols as the Riesz plus-part $[\cdot]_+$. Then \eqref{eq:policy} is a transfer function."

**A6. §2.3 — Markov filter denominator/numerator narration.**
- Now: "…and the policy filters the signal and its derivatives, $\hat x^\star(\omega)=P(-i\omega)\hat\mu(\omega)/\hat n_+(\omega)$: a rational filter with the friction's outer factor in the denominator and the signal's polynomial in the numerator."
- To: "…so that the policy filters the signal and its derivatives, $\hat x^\star(\omega)=P(-i\omega)\,\hat\mu(\omega)/\hat n_+(\omega)$, a rational filter." (drop the denominator/numerator gloss — the display shows it.)
- Also trim the preceding "The whitening $N_-^{-1}$ acts on the deterministic profiles $g_k$ … while the derivatives pass through, so the whitened forecast is a differential operator" → "For a Markov signal the whitened forecast reduces to a differential operator: with $\rho_k=(N_-^{-1}g_k)(0)$, \eqref{eq:zeta-collapse}." (state, then display.)

## B. Math expression as subject — convert throughout

- **§1.1 "Two shapes bracket that choice."** → "In practice $g$ is modeled by one of two forms. At one end, transaction data favour a power law $g(t)=t^{-\beta}$ …; at the other, \citet{ObizhaevaWang2013} derive an exponential kernel …" (Remove the "bracket" agent; keep the two-ends contrast in the body.)
- **§2.3 Remark, §2.4:** check for "$\xi^\star$ …", "The value \eqref{eq:value} has a benchmark" (acceptable — "the value has a benchmark" is a state), keep.
- **§3.1** "the position filter $H(\omega)=\dots$ has magnitude proportional to $\hat n^{-1/2}$" — property statement, acceptable; but "interpolating across the crossover frequencies" participle is fine.
- **§5.1** "differentiation puts the filter in partial-adjustment form" — acceptable (differentiation = process noun); keep.
- General sweep for bare-symbol subjects: `grep` for sentences beginning `$N_+`, `$N_-`, `$P_+`, `$\hat n`, `$Q_` followed by an action verb.

## C. Transitions and articulation

- **C1. §1 length / order.** §1.3 ends with the roadmap paragraph, then §1.4 is related work. Consider moving the roadmap sentence ("Section~\ref{sec:interior} solves … The remaining sections …") to the *end* of §1.4, so the introduction closes on the plan of the paper rather than mid-way. Low priority.
- **C2. §1.3 Cholesky aside.** "The finite-dimensional analogue is the Cholesky factorization … computed by Gram–Schmidt along the coordinate order." Keep (it is illuminating) but it is the one place the exposition slows; consider shortening to "The finite-dimensional analogue is Cholesky factorization along the coordinate order."
- **C3. §2 setup → §2.1.** The bare "Fix a filtered probability space satisfying the usual conditions" opens §2 abruptly. Add a one-clause bridge naming the three steps that §2.1–§2.3 will carry out, so the section has a spine sentence before the housekeeping. E.g.: "The stationary problem is solved in the three steps announced in \S\ref{sec:thesis}: factor the friction (\S\ref{sec:setup}), predict the signal (\S\ref{sec:meanrev}), and combine the two into a filter (\S\ref{sec:filter}). Throughout, fix a filtered probability space …"
- **C4. §2.3 internal order.** The subsection interleaves Assumption 1 (before Thm 1) and Assumption 2 (before Thm 2). Move both Assumptions to the §2 setup paragraph (state the standing hypotheses once), so §2.3 runs Lemma → Theorem (general) → reading → Remark → Theorem (filter) → Markov/OU without the two interruptions. Improves the density the reader feels in §2.3.
- **C5. "Completing the square reads…" / "reads the same policy".** "reads" as a transitive verb is informal; use "gives a second reading" or "is, equivalently, an estimation problem".

## D. Structure / clarity (larger, optional)

- **D1. §2.3 density.** It carries Lemma 1, Theorem 1, Theorem 2, Remark 1, and the Markov/OU specialization. After moving the Assumptions out (C4) and trimming the narration (A4–A6), it should read cleanly; no split needed. Re-evaluate after A/C edits.
- **D2. Abstract.** One long paragraph; acceptable for the genre, but the middle listing ("It reduces to the Markowitz rule … rational frictions give filters …") could be one sentence shorter. Low priority.
- **D3. Em-dash budget.** ~30 in the body; traditional register prefers fewer. In the A-edits above, several are already folded into clauses. A light pass to convert parenthetical em-dashes to commas/parentheses where it does not cost clarity.

## Execution order (smallest-risk first, compile after each group)

1. B (math-as-subject conversions) — local, low risk. Includes "Two shapes".
2. A (equation-restatement cuts/conversions) — the substantive style fix.
3. C3–C4 (setup bridge + move Assumptions) — small structural moves; check refs to `ass:friction`, `ass:signal`.
4. C1–C2, D2–D3 (polish) — optional.
- Compile (pdflatex ×2, 0 errors / 0 undefined) after 1, after 2, after 3.
- Re-read §2.3 end-to-end after the pass; it is the paragraph the directive is really about.

## Acceptance check
- No sentence has a bare math symbol as the subject of an action verb (grep audit).
- No sentence after a display merely re-states the display's contents.
- §2.3 reads as: assumptions already fixed; three named results; two interpretive readings (recipe; estimation), each stated once.
- Build clean, figures resolve, 20 pp.
