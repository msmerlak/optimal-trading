# Restructuring plan: fractional-derivative-optimal-execution paper

**Status:** approved spine, awaiting sign-off on plan before regenerating prose.
**Date:** 2026-06-27

## Reframing

The fractional derivative is the **bulk inverse** of the translation-invariant
propagator symbol $|\xi|^{\gamma-1}$. The full optimal trading rate
decomposes universally as

$$ u^*_t \;=\; \underbrace{u^{\rm bulk}_t}_{\text{translation-invariant fractional derivative of signal}} \;+\; \underbrace{\mathcal{B}(t)}_{\text{homogeneous solution matching domain boundary data}} $$

This decomposition is *general*. What changes per problem is only $\mathcal{B}$.
Wiener–Hopf factorization is a *tool* for computing $\mathcal{B}$ on the
half-line, not a separate theorem.

## New section spine

### §1 Introduction
- Recast around bulk/boundary split as the paper's organizing insight.
- Contribution bullets: (i) explicit closed form for the bulk; (ii)
  unified treatment of boundary corrections via domain-specific
  homogeneous solutions; (iii) Wiener–Hopf factorization as the natural
  half-line specialization; (iv) bulk recovers the fractional derivative
  of order $1-\gamma$; (v) limits and CRONE connection.
- Position relative to AJN 2022, AJNT 2024, GP 2013, MMS 2017,
  Forde-S.B.-Smith 2022 — all are read as the same bulk + different
  boundary data.

### §2 Setup
- Filtered probability space.
- Propagator $G(t) = c\,t^{-\gamma}$, $\gamma \in (0,1)$, with optional
  temporary impact $\eta \ge 0$.
- Signal $\alpha_t$ and forecast curve $\bar\alpha(t,s)$.
- Cost functional.
- **Bulk problem definition:** the FOC posed on $\mathbb{R}$ with a
  stationary signal extension, no boundary data.
- Standing economic assumptions.

### §3 Fractional calculus background
- Symmetric Riesz derivative on $\mathbb{R}$, Fourier symbol
  $|\xi|^{1-\gamma}$ up to constant.
- Sonine pairs (so the bounded-interval corollary later is honest).
- Normalization constants: state $c_\gamma$ for the line/half-line and
  $\kappa_{1-\gamma} = 2\sin(\pi\gamma/2)/(c\,\Gamma(1-\gamma))$.
- App reference: SKM 1993 §13.2 Thm 13.2 for the bounded-interval
  inversion needed by §5.2.

### §4 The bulk solution (main theorem)
- **Theorem 4.1 (Bulk).** On $\mathbb{R}$ with stationary signal
  $\alpha \in L^2_{\rm loc}$ and admissible $u$, the unique stationary
  solution to the bulk FOC is
  $$ u^{\rm bulk}_t \;=\; \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\bigl(\lambda - \bar\alpha(t,\cdot)\bigr)(t). $$
- Adaptedness via forecast curve $\bar\alpha$ — discussed once here.
- Proof: Fourier symbol inversion. Two pages.
- Optional **temporary impact extension**: with $\eta > 0$, the bulk
  solution becomes
  $$ \widehat{u}^{\rm bulk}(\xi) \;=\; \bigl(2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)|\xi|^{\gamma-1} + \eta\bigr)^{-1}\,\widehat{(\lambda-\bar\alpha)}(\xi); $$
  recovers Thm 4.1 as $\eta \to 0$.
- Sign / IBP / Euler–Lagrange derivation explicit (resolves F2-math).

### §5 Boundary corrections
- **§5.1 General principle.** $\mathcal{B}$ solves the homogeneous bulk
  equation; parameters fixed by boundary data; well-posedness is
  problem-by-problem.
- **§5.2 Bounded interval $[0,T]$ with $X_0, X_T$ given.**
  - Two-parameter family of Söhngen-type homogeneous solutions on
    $[0,T]$; explicit form $(t(T-t))^{(\gamma-1)/2}$ etc.
  - Boundary data fix the parameters.
  - **Corollary 5.2 (Bounded-interval execution).** The current Thm 4.1
    of the v1 paper, restated as a corollary:
    $$ u^*_t \;=\; \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}_{[0,T]}\bigl(\lambda - \bar\alpha(t,\cdot)\bigr)(t) \;+\; \mathcal{B}_{1-\gamma}(t), $$
    with $\mathcal{B}_{1-\gamma}(t) = c_1\,(t(T-t))^{(\gamma-1)/2} + \text{(second mode)}$, parameters from $X_0, X_T$.
  - Economic gloss on U-shape (resolves F1-finance).
  - Conjecture: recovers Forde-S.B.-Smith 2022 (downgraded per D4).
  - **Proposition 5.3 (Boundary correction is $O(1/T)$ in the bulk).**
    For fixed initial inventory $X_0$, terminal constraint $X_T=0$,
    and bounded stationary signal $\|\bar\alpha\|_\infty \le M$,
    the boundary correction satisfies
    $$ |\mathcal{B}_{1-\gamma}(t)| \;=\; O\!\left(\frac{X_0 + M}{T}\right) \qquad \text{for } t \in [\epsilon T, (1-\epsilon)T], $$
    any fixed $\epsilon \in (0,1/2)$, while the bulk term
    $\kappa_{1-\gamma}\mathbb{D}^{1-\gamma}(\lambda-\bar\alpha)(t)$ is
    $\Theta(1)$. The bound is NOT uniform: $\mathcal{B}$ diverges as
    $t^{(\gamma-1)/2}$ at the endpoints. Proof sketch in body, full
    proof in App A.2.
    - Sketch: integral $\int_0^T (t(T-t))^{(\gamma-1)/2}dt = T^\gamma B(\tfrac{\gamma+1}{2},\tfrac{\gamma+1}{2})$;
      cumulative-trade constraint forces coefficient $c_1 = \Theta(X_0/T^\gamma)$;
      evaluating at $t = sT$ gives $\mathcal{B} = \Theta(X_0/T)\cdot(s(1-s))^{(\gamma-1)/2}$.
  - **Corollary 5.4 (Bulk-as-asymptotic-optimum).** In the long-horizon
    limit $T \to \infty$ with fixed $X_0$ and signal magnitude, the
    optimal trading rate converges to the pure bulk solution uniformly
    on bulk regions: $u^*_t = u^{\rm bulk}_t + O(1/T)$ on $[\epsilon T,(1-\epsilon)T]$.
  - This is the quantitative version of the previously vague
    "boundary corrections absorbed into $\mathcal{B}$" sentence
    (resolves F3-math).
- **§5.3 Half-line $[0,\infty)$ with $X_0$ given, decay at $\infty$.**
  - One-parameter family of homogeneous solutions decaying at $\infty$;
    parameter fixed by $X_0$.
  - **Wiener–Hopf factorization** introduced as the *method* for
    computing this family.
  - Symbol $M(\xi) = 2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)|\xi|^{\gamma-1} + \eta$.
  - Factorization $M = M_+ \cdot M_-$ on the standard W–H contour.
  - Closed form for $\eta = 0$ (pure power-law symbol → closed-form W–H
    via Sonine pair on $[0,\infty)$).
  - **Crossover scale** $\xi_*(\eta) = (2c\Gamma(1-\gamma)\sin(\pi\gamma/2)/\eta)^{1/(1-\gamma)}$,
    with the two regimes (propagator-dominated / temporary-impact-
    dominated). Resolves the D6=A′ content.
  - $\eta \to 0$ limit recovers the pure bulk solution → §5.3 is the
    half-line analogue of §4 (and §5.2 is the bounded-interval analogue).

### §6 Limits, special cases, and connections
- Almgren–Chriss recovery (limit, with $\eta$ regularization).
- Obizhaeva–Wang as $\gamma \to 1^-$ — explicitly NOT recovered (per
  the §5.3 fix from prior round, exponential vs power-law); state
  honestly.
- AJN 2022, AJNT 2024: this paper's results are explicit closed-form
  specializations of their operator-resolvent calculus.
- Gârleanu–Pedersen 2013: GP recovered as the $G \to$ exponential,
  $\gamma_{\rm risk} > 0$ degeneration — not covered by this paper's
  pure-propagator setting; explicit pointer for the reader.
- MMS 2017: small-impact asymptotic regime.

### §7 Multi-asset extension
- Current §6 content, restated as bulk-solution diagonalization in the
  eigenbasis of the cross-impact matrix.
- Cross-asset propagator → matrix-valued $G$ → matrix bulk theorem.
- Boundary corrections per-asset.

### §8 CRONE / robustness discussion
- Current §8 content. Light edits to align with new spine.
- Crossover scale $\xi_*$ links naturally to CRONE-2 gain margin.

### §9 Empirical protocol and conclusion
- Estimation, backtest, sensitivity (no fabricated results).
- Open problems: Forde-recovery proof; non-stationary signal; rough
  $\alpha$; non-quadratic temporary impact.

### Appendices
- **A.1** Proof of Theorem 4.1 (bulk on $\mathbb{R}$): Fourier inversion.
- **A.2** Proof of Corollary 5.2 (bounded interval): Sonine pair on
  $[0,T]$ via SKM 1993 §13.2 Thm 13.2. Replaces current A.2 with the
  correct reference.
- **A.3** Proof of Wiener–Hopf factorization §5.3: standard contour
  argument for $\eta>0$; closed-form Sonine for $\eta=0$.
- **B** Stochastic Fredholm well-posedness (current B, kept).
- **C** Multi-asset eigendecomposition (current C, kept).
- **D** FFT-based discretization (current D, slightly revised to align
  with §3 normalization).
- **E** Empirical protocol details (current E, kept).

## Migration map (current v1 → new v2)

| v1 location | v2 location | Notes |
|---|---|---|
| Abstract | §1 abstract | Rewrite around bulk/boundary spine |
| §1.1–1.3 | §1 | Restructured contribution bullets |
| §2 | §2 | Add bulk-problem definition; drop $\gamma_{\rm risk}$ asides |
| §3 | §3 | Add Sonine pairs subsection; correct $\kappa$ |
| §4.1 Thm 4.1 | §5.2 Cor 5.2 | Demoted to corollary of new §4 |
| §4.2–4.4 remarks | §4 + §5.2 | Adaptedness moves to §4; boundary to §5.2 |
| §5.1–5.3 | §6 | Limits/special cases consolidated |
| §5.4 W–H | §5.3 | Promoted to a proper boundary-corrections subsection; D6=A′ |
| §6 multi-asset | §7 | Restated via bulk diagonalization |
| §8 CRONE | §8 | Light edits |
| §9 | §9 | Light edits |
| App A.1 | App A.1 | Refactored for bulk-on-$\mathbb{R}$ proof |
| App A.2 | App A.2 | SKM 1993 §13.2 reference (per D5=A) |
| App A.3 | App A.3 | W–H proof for §5.3 |
| App B,C,D,E | App B,C,D,E | Kept with light edits |

## Implementation choices baked into the plan

- **Bulk on $\mathbb{R}$** (per Q2): Theorem 4.1 lives in the
  translation-invariant setting; $[0,T]$ and $[0,\infty)$ are
  corollaries via §5.2 and §5.3.
- **Corollary status for $[0,T]$** (per Q3): the result that was the
  v1 main theorem becomes Corollary 5.2.
- **D5=A** ($\kappa_{1-\gamma} = 2\sin(\pi\gamma/2)/(c\Gamma(1-\gamma))$, SKM 1993 reference).
- **D6=A′** (general $\eta$, $\eta\to 0$ limit recovers pure bulk;
  crossover scale $\xi_*$).
- **D1=B**, **D3=A**, **D4=A** unchanged from prior decisions.

## Items deferred (do not block restructure)

- Full Fredholm well-posedness proof on $[0,T]$ with the symmetric
  Riesz operator.
- Forde recovery via direct kernel matching.
- B.2 boundary-tail bound for Thm 5.1 (now Cor 5.2 boundary).
- Empirical results (no data run yet).
- Numerical comparison to AC/TWAP/AJN baseline.

## Open questions for user

(None required — Q1 spine confirmed; Q2/Q3/Q4 defaults taken. Raise if
any of the defaults are wrong.)

## Process

1. User signs off on this plan (or marks deltas).
2. Single async worker rewrites `papers/fractional-derivative-optimal-
   execution.md` end-to-end from the plan + the current v1 file +
   the round-1/round-2 review files (still useful as content sources).
3. Worker also writes a `papers/fractional-derivative-optimal-execution.v1-to-v2.md`
   migration note that explains the restructure for any reader following along.
4. Round 3 reviewers (math, finance, consistency) on v2.
5. Iterate.
