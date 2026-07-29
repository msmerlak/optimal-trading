# Review — "Optimal Trading Filters: a Wiener–Hopf Approach" (v2)

**Artifact:** `v2/optimal-trading-filters-v2.tex` (18 pp. compiled), local LaTeX manuscript.
**Review type:** internal pre-submission review (novelty, correctness, rigor, reproducibility, writing).
**Evidence:** `outputs/.drafts/optimal-trading-filters-v2-review-evidence.md`.

---

## Summary Assessment

The paper solves the adapted gain–risk–cost trading problem (temporary impact, transient propagator impact, inventory risk) by a single triangular factorization of the friction operator relative to the filtration, computed in closed form via the Szegő outer function in the stationary case and as a Volterra kernel on a finite horizon. It is a genuine unification: Markowitz, the Gârleanu–Pedersen aim portfolio, the Neuman–Voß feedback solution, the Gatheral–Schied–Slynko liquidation profiles, and the Forde–Sánchez-Betancourt–Smith chaos solution all drop out as special or boundary cases of one identity, and the paper adds new results (the scale-free causality-gap law $v/v_{\rm ant}=\sin(\pi\beta/2)$; the flow-reversal threshold $\theta^\ast=\kappa-2m$; the boundary-layer decay rates). The mathematics is internally consistent — a 9-check numerical suite in-repo passes at machine precision, including an independent algebraic-Riccati verification of the Neuman–Voß recovery — and the exposition is close to submission quality. The main defects are one unqualified $L^2$ claim that is false in the pure power-law limit, proof-sketch-level rigor in two appendices for a paper that leans on operator-theoretic machinery, and a set of known style debts (sentence-style section titles, residual self-promotional framing). No market data is used and none is claimed; the numerical verification is honest about discretization bias.

**Recommendation: minor-to-moderate revision before submission.** Nothing structural; the critical item is a one-sentence mathematical correction.

---

## Strengths

1. **One organizing idea, carried through.** The thesis — one factorization, Wiener–Hopf/Gohberg–Krein/Arveson as a single construction whose *computation* differs by regime — is stated in §1.3 and actually governs the paper's structure. The literature-recovery section (§5.3) is the payoff and it is complete: five prior solution families recovered with the mechanism identified in each case (poles of $\hat n_+$ ↔ EMA rates ↔ Riccati closed-loop poles).
2. **Verified claims.** Every closed form is checked in `v2/experiments/test_all_results.py` (9/9 PASS): Szegő integral vs closed factors (~1e-16), the $\sin(\pi\beta/2)$ law across exponents and speeds (~1e-14, $\theta$-independence confirmed), the response formula and threshold, Table 1 against a brute-force adapted optimum, and — importantly — the Neuman–Voß recovery against *their* exact LQ solution via `solve_continuous_are`, poles matching $b_1,b_2$ to machine precision. This is unusually strong claim discipline for an analytic paper.
3. **New results with clean interpretations.** The causality-gap law (Prop. 1) is a genuinely new, memorable closed form: the fraction of foresight value retained depends on the impact-memory exponent alone. The flow-reversal threshold (Prop. 2) with its phase diagram, and the boundary-layer decay rates (Prop. 3, $d(t)^{-\nu}$ vs $e^{-b_1 d(t)}$), are quantitative statements prior treatments do not display.
4. **Fair comparison with the closest competitor.** The Abi Jaber–Neuman paragraph (§1.4) credits their greater generality explicitly, identifies the exact mathematical relation (resolvent series = Neumann expansion the factorization sums), and makes a correct computational claim ($O(n^2)$ per parameter set for the discretized Volterra solve vs a fixed filter / constant-state EMA recursion).
5. **Figures trace to real computation.** All four figures regenerate from scripts in `v2/experiments/`; the power-law curves in Fig 4(a) use the Szegő integral at matched $\lambda$ rather than the $\lambda=0$ shortcut, making the exp-vs-power-law comparison fair.

---

## Critical Issues

**C1. Unqualified $L^2$ claim in §2.3 is false in the pure power-law limit.**
§2.3 (after Theorem 2): *"The corresponding position filter $\hat\chi/(-i\omega)$ lies in $L^2$ for every kernel."* For the pure power-law kernel ($\eta=\lambda=0$) with an OU signal, the position filter behaves as $|\omega|^{\nu-1}$ near $\omega=0$ with $\nu=(1-\beta)/2<1/2$, so $\int|\hat\chi/(-i\omega)|^2$ diverges at low frequency; numerically the position variance is infinite at $\lambda=0$ and finite for any $\lambda>0$ (session check: divergent at $\lambda=0$; $0.63$ at $\lambda=0.1$; $0.18$ at $\lambda=1$). The claim needs the qualification "for every kernel with $\lambda>0$" (or an explicit signal-decay condition covering the $\lambda=0$ case). The limitations paragraph (§7) acknowledges unbounded factors for pure power-law, but this sentence as written asserts more than is true. One-sentence fix; must be made — a referee who checks the low-frequency exponent will find it.

---

## Major Issues

**M1. Proof rigor below the machinery invoked (App. A, App. E).**
- App. A proves Lemma 1 by triangular bookkeeping and defers the unbounded (pure power-law) case to a "dense domain fixed by a spectral-decay hypothesis" that is never stated as a displayed hypothesis. Since Lemma 1 is the paper's core, a referee at a mathematical-finance venue will want either (i) the hypothesis stated precisely (function class, domain, in one displayed line) or (ii) a citation to Arveson's factorization theorem with the hypotheses of this setting explicitly matched.
- App. E (Prop. 3) is an estimate sketch: the constants $C(\beta), C$ are not derived, and the subdominance of the weight deviation is asserted. The paper honestly flags "not yet sharp constants" (§7), but the Proposition states a bound with named constants; either downgrade to asymptotic notation ($\lesssim$, $O(\cdot)$) or supply the constants.

**M2. No data/code availability statement.**
The verification suite (`test_all_results.py`, 9 checks) and all figure scripts exist and run, but the paper neither cites them nor states availability. Given that the paper's credibility strategy is "all closed forms are checked numerically" (§6), shipping or linking the scripts is the natural completion. Add an availability note (even "available from the author").

**M3. Duality remark's whole-line pairing (Remark 1).**
The friction energy $\tfrac12\E\langle\mu^\star,Q^{-1}\mu^\star\rangle$ and the Legendre-transform statement use the whole-line pairing, which is formally infinite for stationary signals; the per-unit-time reading is supplied only later (§2.3's causality-gap sentence). One clause in the remark ("per unit time in the stationary case") closes the gap.

**M4. Terminology drift (from the style review, affects readability of results).**
"Flow" vs "rate" for the same quantity $u$ (§2–3 "rate", §4.3 "flow response"); four names for $v_{\rm ant}-v$ ("causality gap", "value forgone", "value of anticipation", "shadow price of information"); benchmark naming ("anticipative", "perfect anticipation", "full foresight"). Pick one primary term per object; gloss alternatives once. (Full list: `reviews/v2-style-review.md`, items G2–G4.)

---

## Minor Issues

1. **Sentence-style section titles** (style review §1): §1.2 "Adaptedness is the binding constraint", §3 "Pure impact is fractional calculus", §4.1/§4.2 declaratives, §5 "Boundaries: the same factorization without Fourier". Seven titles flagged with drop-in noun-phrase replacements; the author has already flagged §1.2 as too casual. Journal register favors the change.
2. **Residual self-promotional framings** (style review P2–P4): "is the subject of the paper" (§1.3), "Everything downstream rests on a single identity" (§2.2), "the quantitative content of the thesis" (§5.2). P1 was already fixed in the §1.1 rewrite.
3. **Abstract/conclusion near-duplication** (G6): the memory/foresight sentence appears nearly verbatim in both. Vary one.
4. **Table 1 caption** says convergence is "first order in $dt$" for the exponential family — supported by the dt-refinement in check 6, but the paper gives no order-of-convergence argument; consider "empirically first order".
5. **Fig 5 shading** is a nominal width ($\sim3/b_1$), not the fitted decay constant; the caption doesn't claim otherwise, but a clause noting the shading is indicative would preempt a referee query.
6. **Notation table** lists $c_+(t,s)$ and $f$ before they appear (§5.1, §2.3 respectively) — fine for a table, but consider ordering rows by first appearance.
7. **§4.3's price-manipulation paragraph** cites Gatheral (2010) and Alfonsi–Schied–Slynko for exclusion of transaction-triggered manipulation "for the exponential and power-law kernels" — accurate, but the ASS result is kernel-specific; a pinpoint (theorem number) would strengthen it.

---

## Reproducibility and Verification

| Item | Status |
|---|---|
| Manuscript compiles | **Verified** — 0 errors, 0 undefined refs, 18 pp. (this session) |
| Lemma 1 / Thms 1–2 (policy, filter, value) | **Verified numerically** — checks 1–3, 6 (9/9 suite) |
| Prop. 1, $\sin(\pi\beta/2)$ | **Verified** — quadrature, 5 exponents × 3 speeds, ~1e-14; $\theta$-independence confirmed |
| Prop. 2, response + threshold | **Verified** — formula + sign structure + discrete Table 1 rows; power-law $R>0$ up to $\lambda=1000$ |
| Prop. 3, boundary layer | **Qualitatively verified** — interior gap 0.016, boundary 34×; constants not derived (M1) |
| Neuman–Voß recovery | **Verified against their exact method** — independent algebraic-Riccati poles = $b_1,b_2$ to ~1e-16, 3 parameter sets |
| Markowitz / GP / GSS / FSS recoveries | Markowitz verified (check 8); GP/GSS/FSS recoveries are algebraic identities in-text, not independently re-derived (GSS profile is standard; FSS chaos-expansion equivalence asserted with pinpoint cite) |
| Figures | **Regenerated this session** from `v2/experiments/*.py`; no hand-drawn content |
| Table 1 | **Reproduced** — discrete column matches check 6 at $dt=0.01$ |
| Position-filter $L^2$ claim (§2.3) | **FAILS at $\eta=\lambda=0$ power-law** — see C1 |
| Data availability | **Not stated** (M2); no market data used or claimed |

Blocked checks: none — all artifacts local and readable.

---

## Inline Annotations

- **§1.1, Markowitz analogy** — now correctly distinguishes rate-from-appreciation ($u=Q^{-1}\alpha$) vs position-from-return ($x=\mu/\lambda$); the two-signal confusion fixed this session. Verify the forward reference "(Section 5.3)" survives any section renumbering.
- **§2.3, line ~213** — C1: add "$\lambda>0$" qualification to the position-filter $L^2$ sentence.
- **§2.2, Remark 1** — M3: add per-unit-time clause; also consider naming the Rockafellar–Wets pinpoint (Study 6, pp. 170–187) in the citation.
- **§3, "Temporary impact alone"** — clean after the Markowitz relocation; the $\alpha$-vs-$\mu$ contrast here and in §5.3 is now the paper's clearest statement of the two-signal distinction. Good.
- **§4.2, Prop. 1** — statement is now memory-framed and minimal (finiteness criterion removed). The proof (App. C) is complete and independently verified. Consider stating in the Proposition that $v_{\rm ant}<\infty$ holds here (it is proved in App. C's first line via $\hat n\to\infty$) so the ratio is well-defined on its face.
- **§4.3, Prop. 2** — $c_1$ is now a local constant with explicit values; the equation's parenthetical "(exponential)/(power-law, or any $\eta>0$)" is clear. The pure-risk limit $R=-\theta^2/\lambda$ in the discussion could cross-reference the Markowitz paragraph in §5.3 for the $c_1=1/\sqrt\lambda$ origin.
- **§5.1, eq. (finiteT)** — the em-dash aside separating subject from verb (style review G8); split recommended.
- **§5.3, aim portfolio** — the Markowitz position now written $\mu_t/\lambda=\theta\alpha_t/\lambda$; consistent with the two-signal cleanup.
- **§6, Table 1** — annotate grids per row (currently in prose); fine as is for QF format.
- **Fig 4(b)** — intercept labels $\theta=\kappa$, $\lambda=2\kappa\gamma/3$ now correct (the 2.67 constant bug was fixed in-session; worth re-checking the regenerated PDF is the one included).

---

## Recommendation

**Accept direction; revise before submission.** Required: C1 (one-sentence $L^2$ qualification). Strongly recommended: M1 (state the spectral-decay hypothesis as a display, or downgrade Prop. 3 constants to asymptotics), M2 (availability note), M3 (per-unit-time clause), M4 + title fixes (mechanical, list already exists in `reviews/v2-style-review.md`). The mathematical content is verified to the extent an internal review can verify it — including the one recovery claim (Neuman–Voß) that was previously only self-consistent — and the paper's honest handling of discretization bias and its limitations paragraph are already at referee standard.

---

## Sources

- `v2/optimal-trading-filters-v2.tex` — the reviewed manuscript (primary)
- `v2/experiments/test_all_results.py` — verification suite; full 9/9 PASS output in evidence notes
- `experiments/nv_vs_stationary.py` — independent Neuman–Voß Riccati implementation
- `v2/experiments/fig{1,3,4,5}_*.py`, `v2/figures/*.png` — figure provenance
- `reviews/v2-style-review.md` — prior style-only review (this session)
- `v2/notes/causality-gap-exp-vs-powerlaw.md`, `v2/notes/paper-outline-v2.md` — design notes
- `v1/optimal-trading-filters.tex` — Table 1 provenance
- R. T. Rockafellar, R. J.-B. Wets, *Nonanticipativity and $L^1$-martingales in stochastic optimization problems*, Math. Programming Study 6 (1976) — https://sites.math.washington.edu/~rtr/papers/rtr068-Nonanticipativity.pdf
- Evidence notes: `outputs/.drafts/optimal-trading-filters-v2-review-evidence.md`
- Plan: `outputs/.plans/optimal-trading-filters-v2-review-plan.md`
