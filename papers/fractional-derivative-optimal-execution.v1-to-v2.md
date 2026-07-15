# Migration note: v1 → v2 of *Optimal Execution as a Fractional Derivative*

**Status:** migration note for readers following the paper through its
v1 → v2 restructure.
**Date:** 2026-06-27
**Authors:** TBD

This note explains the structural difference between v1 (archived at
`papers/archive/fractional-derivative-optimal-execution.v1.md`) and v2
(current `papers/fractional-derivative-optimal-execution.md`). The
scientific content is essentially preserved; the spine is reorganized
to make the bulk/boundary split the organizing principle.

## 1. Why the restructure

In v1 the main theorem was stated on the bounded interval $[0,T]$ and
the half-line ($T = \infty$, Wiener–Hopf) problem appeared as a
distinct §5.4 with its own theorem hierarchy. Round 1 and Round 2
reviewer feedback made two related points:

1. The **fractional derivative is the bulk inverse of the translation-
   invariant propagator symbol** $|\xi|^{\gamma-1}$ in Fourier. This
   bulk inversion is the same on $\mathbb{R}$, $[0,T]$, and
   $[0,\infty)$; only the *boundary correction* — the homogeneous-
   solution piece enforcing the domain's boundary data — changes per
   problem. Wiener–Hopf factorization is one specific tool for picking
   the boundary correction on the half-line, not a separate theorem.
2. The stationary problem on $\mathbb{R}$ should therefore be the
   load-bearing main result, and bounded-interval and half-line
   results should be its *corollaries* with explicit boundary
   corrections.

v2 implements this: a single bulk theorem on $\mathbb{R}$ (Theorem
4.1), and a §5 on boundary corrections with three named
specializations.

## 2. Migration map

| v1 location | v2 location | Status |
|---|---|---|
| Abstract | §1 abstract | Rewritten around bulk/boundary spine |
| §1.1–1.3 | §1 (1.1 bulk/boundary picture; 1.2 contributions; 1.3 positioning) | Restructured |
| §2 (setup) | §2 (setup + 2.4 bulk problem definition + 2.5 standing assumptions) | Extended |
| §3 (fractional calculus) | §3 (3.1–3.5; explicit $\kappa$ and Sonine pairs subsections) | Extended; D5 = A constant corrected |
| **§4.1 Theorem 4.1 (bounded interval)** | **§5.2 Corollary 5.2** | *Demoted to corollary* of v2 §4 bulk theorem |
| §4.1 adaptedness paragraph | §4.2 (consolidated once, not repeated) | Moved/consolidated |
| §4.2 forecast curve | §2.2 + §4.2 | Cleaned up |
| §5.1–5.3 limits & special cases | §6 (limits, special cases, connections) | Re-ordered as §6 |
| **§5.4 Wiener–Hopf** | **§5.3 (with general $\eta \ge 0$)** | *Promoted to a boundary-corrections subsection*; D6 = A′ |
| §5.4 inventory-risk penalty | dropped (D6 = A′ replaces with temporary impact $\eta$) | Removed; GP pointer in §6.4 |
| §6 multi-asset (Theorem 6.1) | §7 (Theorem 7.1) | Restated via bulk diagonalization |
| §8 CRONE | §8 | Light edits |
| §9 empirical/conclusion | §9 | Light edits; added Cor 5.4 $O(1/T)$ diagnostic |
| App A (proof of v1 Thm 4.1) | A.1 (bulk on $\mathbb{R}$) + A.2 (Cor 5.2 + Prop 5.3) | Rewritten; SKM 1993 §13.2 Thm 13.2 reference per D5 = A |
| App B (Mittag–Leffler resolvent + Wiener–Hopf) | A.3 (W–H) + App B (Mittag–Leffler resolvent) | Split: W–H lifted to A.3, ML stays as B |
| App C (multi-asset eigendecomposition) | App C | Light edits |
| App D (FFT discretization) | App D | Light edits; symmetric Grünwald rescaling clarified |
| App E (empirical protocol) | App E | Added Cor 5.4 $O(1/T)$ diagnostic |
| References | References | Expanded (Söhngen, Çelik–Duman, Podlubny, Stein, Cartea–Jaimungal–Penalva, Webster); Chakrabarti–George dropped as primary; Bouchaud → 2004 |
| Changelog (Round 1) | Changelog (v2 + carry-over of Round 1) | Preserved as historical record |

## 3. Key changes

### 3.1 Theorem hierarchy

The v2 spine elevates the translation-invariant bulk problem and
demotes both the bounded-interval and half-line problems to
corollaries. Explicit mapping:

- **v1 Thm 4.1 (bounded-interval execution, $[0,T]$ with $X_T = 0$)
  → v2 Cor 5.2.** The statement is essentially unchanged but the
  result is reframed as the bounded-interval specialization of the
  bulk theorem plus a Söhngen–Tricomi boundary correction
  $\mathcal{B}_{1-\gamma}(t) = c_1\phi_1(t) + c_2\phi_2(t)$.
- **v1 §5.4 Wiener–Hopf result → v2 Cor 5.7.** The statement is
  similarly reframed as the half-line specialization of the bulk
  theorem plus a single homogeneous mode picked by Wiener–Hopf
  factorization. The factorization itself is Proposition 5.5.
- **New v2 Prop 5.3 and Cor 5.4** (no v1 counterparts): $|\mathcal{B}_{1-\gamma}(t)| = O((X_0+M)/T)$ uniformly
  on the bulk region $[\epsilon T,(1-\epsilon)T]$, so $u^* = u^{\rm bulk} + O(1/T)$
  on bulk regions. This makes quantitative the previously vague
  "boundary corrections are subdominant in the bulk" sentence flagged
  by the Round 2 math reviewer.

### 3.2 D5 = A: Riesz normalization corrected

v1 had $\kappa = (c\,\Gamma(1-\gamma))^{-1}$. v2 has

$$ \kappa_{1-\gamma} \;=\; \frac{1}{2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2)}. $$

The discrepancy was the $2\sin(\pi\gamma/2)$ Riesz normalization on
the symmetric symbol. Appendix A.2 now cites **Samko–Kilbas–Marichev
1993 §13.2 Theorem 13.2** (the airfoil-equation form), not
Chakrabarti–George (1994). Chakrabarti–George's formula treats the
asymmetric kernel $(s^\alpha - v^\alpha)^{-\beta}$, not the symmetric
$|s-v|^{-\gamma}$ form needed here.

### 3.3 D6 = A′: temporary impact replaces risk penalty in §5.3

v1 §5.4 introduced a Gârleanu–Pedersen inventory-risk penalty
$\tfrac12\gamma_{\rm risk}\sigma^2 X_t^2$ in the cost functional then
*dropped* it from the symbol before Wiener–Hopf factorization — a real
self-inconsistency flagged by the Round 2 finance reviewer.

v2 §5.3 replaces this with a general temporary-impact term
$\tfrac12\eta u_t^2$, $\eta \ge 0$. The half-line symbol becomes

$$ M(\xi) \;=\; c_\gamma|\xi|^{\gamma-1} + \eta, $$

which has a crossover scale

$$ \xi_*(\eta) \;=\; (c_\gamma/\eta)^{1/(1-\gamma)} $$

separating a **propagator-dominated long-memory regime**
($|\xi|\ll\xi_*$, fractional-derivative policy) from a **temporary-
impact-dominated myopic regime** ($|\xi|\gg\xi_*$, direct signal-
following policy). The $\eta\to 0$ limit recovers the pure bulk
solution, making §5.3 the half-line analogue of the §4 bulk theorem.

Pointer to Gârleanu–Pedersen retained in §6.4 with a half-paragraph
explanation of how the GP setup (exponential resilience + running risk
penalty) differs from this paper's propagator + temporary impact.

### 3.4 Adaptedness consolidated

v1 had adaptedness/forecast-curve discussions distributed across §4.1,
§5.1, and §5.4. v2 places the single load-bearing discussion in §4.2
(bulk theorem) and notes that all boundary-correction specializations
inherit the same forecast-curve construction.

### 3.5 Bibliography polish

Added: Söhngen (1939), Çelik–Duman (2012), Podlubny (1999), Stein
(1970), Cartea–Jaimungal–Penalva (2015), Webster (2023). Removed as
primary: Chakrabarti–George (1994) (retained in v1 archive only).
Corrected: Bouchaud et al. → 2004 (Quant. Finance 4(2)); Krein 1962
explicitly noted as English translation of 1958 Russian original.

## 4. What carries over with light edits

- **Appendix B (Mittag–Leffler resolvent).** v2 splits v1 App B into
  v2 A.3 (W–H factorization, lifted out) and v2 App B (Mittag–Leffler
  identification). The Mittag–Leffler kernel formula and the $c \to 0$
  / $\eta \to 0$ limits are unchanged.
- **Appendix C (matrix fractional derivative).** v2 App C is v1 App C
  with the corrected $\kappa$ and bulk-diagonalization framing. Proof
  is identical modulo the constant.
- **Appendix D (FFT-based discretization).** v2 App D clarifies that
  the unweighted symmetric Grünwald stencil discretizes the
  $\mathbb{R}$-Riesz operator up to the
  $1/(2\sin(\pi\gamma/2))$ Riesz rescaling; previously this was
  implicit and confused the boundary-accuracy discussion.
- **Appendix E (empirical protocol).** v2 App E adds a "bulk vs
  boundary diagnostic" item testing the Cor 5.4 $O(1/T)$ scaling
  directly. Rest of the protocol is unchanged.

## 5. What's still deferred

Items intentionally left as TODO / ⚠️ in v2:

- **Math:** full Fredholm well-posedness proof on $[0,T]$ with the
  symmetric Riesz operator; explicit $3\times 3$ system non-
  singularity verification for $(c_1, c_2, \lambda)$ in App A.2 Part
  1; HLS-restricted operator-norm bound on the bounded interval (App
  B.1); Krein integrability quantitative constants (A.3 Part 1);
  $L^2$-mapping bound for the half-line projection $\Pi_+$ (A.3 Part
  3); sharper Step-2 cumulative-bulk bound in Prop 5.3 proof.
- **Recovery:** Forde–Sánchez-Betancourt–Smith (2022) kernel-matching
  proof (Conjecture 5.2.2). Per decision D4 = A this is honestly
  flagged as a conjecture.
- **Numerical:** Jacobi-spectral vs WSGD endpoint accuracy benchmark
  on the Cor 5.2.1 U-shape; explicit Cor 5.4 $O(1/T)$ scaling
  diagnostic in a backtest.
- **Empirical:** estimation, backtest, sensitivity per App E. No data
  has been run; placeholders are marked clearly.

## 6. Reading order for v1 readers

If you've read v1:

1. Skim v2 §1.1 (bulk/boundary picture) and §1.2 (contributions list)
   to internalize the new spine.
2. Read v2 §4 (bulk theorem on $\mathbb{R}$) — this is the new load-
   bearing result.
3. Read v2 §5.1 (general principle for boundary corrections) and §5.2
   (bounded interval). v2 Cor 5.2 is what you knew as v1 Thm 4.1.
4. Read v2 §5.2.5 (new Prop 5.3, Cor 5.4 — the $O(1/T)$ result) and
   §5.3 (new half-line treatment with general $\eta$).
5. v2 §§6–9 are mostly the same as v1 §§5–9 with light edits.
6. Appendix A.3 is new (W–H factorization proof split out from v1 App
   B). Other appendices are essentially the v1 versions with light
   edits and the corrected $\kappa$.

## 7. Pointer

- v1 archive: `papers/archive/fractional-derivative-optimal-execution.v1.md`
- v2 current: `papers/fractional-derivative-optimal-execution.md`
- v2 plan: `papers/.plans/fractional-derivative-optimal-execution.v2-restructure.md`
- Round 1 reviews: `reviews/fractional-paper-round1-{math,finance,consistency}.md`
- Round 2 reviews: `reviews/fractional-paper-round2-{math,finance,consistency}.md`
