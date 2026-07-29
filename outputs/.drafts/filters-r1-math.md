# Mathematical-correctness review: `tex/optimal-trading-filters.tex` (r1)

Role: independent rederivation of every closed form; read-only run of
`experiments/risk_response_check.py` and `experiments/review_factorization_check.py`;
cross-check against the §6.3 table and CHANGELOG 2026-07-18 entries.

Headline: **no mathematical errors found.** Every formula in items (1)–(10) of the
task checklist rederives correctly, including two identities I confirmed by
independent closed-form computation that the paper only verifies numerically
(the Gohberg–Krein kernel normalization and the λ→0 response cross-check).
The findings below are scope mismatches between stated hypotheses and the cases
the paper applies them to, one proof gap, and several evidence claims in §6.3 and
the abstract that are stronger than what the scripts show.

---

## BLOCKERS (mathematical errors)

None. All checked derivations are correct (see NON-ISSUES for the itemized ledger).

---

## FIXES WORTH DOING NOW (imprecise statements, proof gaps, evidence overstatements)

### F1. Theorem 2's hypothesis excludes the paper's own lead examples (§3, App B, §5.1, §6.2)
Theorem 2 asserts `ĝ ∈ L²` "guaranteed by a spectral-decay hypothesis," which App B
gives as ∫(1+ξ²)S_α/q dξ < ∞. For the OU signal with the exponential kernel and
η = 0 (the flagship case of §5.1 and rows 1–2 of the table), S_α/q → σ²/A as
|ξ| → ∞, so (1+ξ²)S_α/q ~ ξ² and the integral **diverges**. Consistently, the rate
filter has a white-noise atom there (c₁ = 1/√A ≠ 0, App C), so ĝ ∉ L². The same
failure occurs for pure risk (γ = η = 0). Theorem 2 as stated therefore does not
cover the η = 0 cases to which §§5–6 apply eq. (ou-filter); those cases are
rescued at the position level (H ∈ L², which I verified) plus a distributional
atom in the rate. The paper knows this (App C splits g = a₀δ + g_reg) but never
reconciles it with Theorem 2's hypothesis. Fix: state Theorem 2 for the position
filter in general and for the rate filter under the decay hypothesis, with a
remark that η = 0 kink kernels place an atom a₀δ in the rate, a₀ = θσc₁/Φ.

### F2. §6.3 evidence claims are stronger than the script outputs
I ran `risk_response_check.py` unchanged and with dt-refinement (read-only, in
`python -c` wrappers). Three specific mismatches with the text:

- *"the exponential family converges to the formulas under dt-refinement to under
  1%"*: verified only for row-1 R (−0.3093 vs −0.3107 at dt = 0.01, 0.45%). Row-1
  X is 1.1% off at the same dt (0.8603 vs 0.8698). The NV row (also exponential
  family) is **8.7% off in R** at the reported resolution (n = 800, dt = 0.02:
  +0.2406 vs +0.2637) and still 2.2% off at dt = 0.005 (+0.2578, my run; converging
  first-order in dt toward the formula, so the formula is right, but "under 1%"
  is not demonstrated for this row).
- The table mixes refinement levels without saying so: rows 1 and 4 report
  dt = 0.01 values (row 4 discrete +0.325/+0.190 matches my dt = 0.01 run
  +0.3251/+0.1898), rows 2–3 report dt = 0.04 values, row 5 reports dt = 0.02.
  State the grid per row or refine uniformly.
- *"the residual power-law discrepancy matches the quadrature bias ... measured at
  the analytically known λ=0 point on the same grid"*: at dt = 0.01 the λ = 0
  calibration bias is 6.2% low (0.3741 vs 0.3989) while row 4's bias is 10.7% low
  (0.325 vs 0.364). Same sign and order, not a match. "Is comparable to" would be
  accurate; "matches" is not.

### F3. Abstract/intro: "All closed forms are verified against discretized adapted optima"
What is verified numerically is R and X at five parameter points (§6.3) plus the
factorization identities in `review_factorization_check.py`. The value formulas
(v = σ²θ/4Φ², the Markowitz and fractional values), the GP partial-adjustment
identity (gp), and the filter shapes (ema), (nv-filter) as time-domain kernels
are verified analytically only. Weaken to "the response and position formulas are
verified..." or add the missing checks.

### F4. Lemma 1's proof establishes a left inverse only (App A)
The displayed chain shows Q₊⁻¹P₊Q₋⁻¹(P₊QP₊)u = u for adapted u. The identity
(pi) also needs (P₊QP₊)(Q₊⁻¹P₊Q₋⁻¹)α = α for adapted α, which is one more line:
with w = Q₋⁻¹α, P₊Q₋Q₊·Q₊⁻¹P₊w = P₊Q₋P₊w = P₊Q₋(w − P₊^⊥w) = P₊α − P₊Q₋P₊^⊥w = α,
since Q₋ preserves the complement. (I verified this line; it holds.) Alternatively
invoke positivity of P₊QP₊ on the adapted subspace so that a left inverse
suffices. As written the lemma's claim outruns its proof by half.

### F5. Theorem 1: "unique adapted optimum" without an admissibility class (§2.2)
For η = 0 the optimal rate contains a white-noise component (E[u_t²] = ∞ when
c₁ ≠ 0), so the optimum is not attained in L²(dt ⊗ dP) of rates; it lives in the
completion under the energy norm ∫q|û|². §8 concedes unboundedness only "for the
pure power-law kernel," but the η = 0 exponential+risk case has the same issue on
the rate side (the paper itself calls it the "singular (block-trade) component"
in §6.2). One sentence in the setup fixing the admissible class (finite-cost
adapted processes) resolves Theorem 1, Theorem 2, and the §8 remark jointly.

### F6. Riesz-projection convention drift (§3 vs App B/App C)
§3: "P₊ acts on symbols as the Riesz projection Π₊ (truncation to **non-negative**
lags)." App B: "atoms at lag zero ... are **annihilated**." All subsequent formulas
(OU projection, R with the atom subtracted) use the second convention, i.e.
truncation to positive lags with lag-zero atoms removed. Align the §3 statement.

---

## OPTIONAL

### O1. γ-normalization of G_T in §7
§7 defines G_T as "the cost operator restricted to [0,T]" (which carries the γ
prefactor), and eq. (gk-kernel) carries (γc_β)^{1/2}, so C₋C₊ equals γ·|t−v|^{−β},
consistent — but the parenthetical "(C₋C₊ = G_T exactly, including the constant)"
is checked in the script with γ = 1. Make the γ-convention explicit once.

### O2. Boundary-layer rates d(t)^{−ν}, d(t)^{−1} (§7) are asserted, not derived
The parenthetical justification (Marchaud tail truncation; weight deviation
∼ ν(t−s)/(T−t)) is plausible and dimensionally right, but no computation appears
anywhere in the paper or the scripts. Label as a heuristic estimate or add a
short appendix computation.

### O3. Positive-definiteness of G is implicit
q > 0 requires Ĝ ≥ 0 (true for exponential and power-law kernels; this is the
no-price-manipulation condition). Since eq. (symbol) writes "Ĝ(ξ) ≥ 0" inside a
display, it reads as a fact rather than a hypothesis; state it as a standing
assumption with the Gatheral (2010) citation.

### O4. Unverifiable citation detail
The page citation "\citet[pp. 590–591]{FordeSanchezSmith2022}" and
"\citet[Ex. 2.30]{GatheralSchiedSlynko2012}" were not checkable from the repo.
The GSS exponent (β−1)/2 < 0 is consistent with the known U-shaped
endpoint-diverging profile, but the example number should be confirmed against
the published version.

### O5. Check B grid size
`review_factorization_check.py` Check B uses n = 5; adequate for an exact-algebra
identity (error 2.6e−16 vs 8.5e−2 for the wrong order), but a second n and a
second random seed would make the provenance more robust at zero cost.

---

## NON-ISSUES (explicitly verified correct, with derivations)

1. **Symbol and position reduction (eq. symbol, eq. N).** With f̂(ξ) = ∫e^{iξt}f dt,
   ẋ = u gives x̂ = û/(−iξ), |x̂|² = |û|²/ξ²; hence q = η + γĜ + λ/ξ², N = ξ²q =
   ηξ² + γĜξ² + λ, and Q₊Q₋ = N₊N₋/((−iξ)(iξ)) = N/ξ² = q with Q_± = N_±/(∓iξ). ✓
2. **Fourier constant (§4).** ∫₀^∞ t^{−β}cos(ξt)dt = Γ(1−β)sin(πβ/2)ξ^{β−1}
   (Mellin cosine formula at s = 1−β), so Ĝ = c_β|ξ|^{β−1}, c_β = 2Γ(1−β)sin(πβ/2). ✓
   Independently reconfirmed by item 12 below.
3. **Lemma 1 triangular algebra (App A).** Causal Q₊ (zero-free in UHP, causal
   inverse) preserves the adapted subspace; the adjoint Q₋ and Q₋⁻¹ preserve the
   complement; splitting Q₋v and applying Q₋⁻¹ gives P₊Q₋⁻¹P₊Q₋v = v. The displayed
   left-inverse chain is correct (gap noted in F4 is completeness, not error). ✓
4. **Causal factor on the RIGHT.** Algebraically: u = Q₊⁻¹P₊Q₋⁻¹α is adapted
   because the last operator applied is causal; the LU order Q₋⁻¹P₊Q₊⁻¹ produces a
   non-adapted output. Numerically: Check B, ‖W_direct − W_UL‖ = 2.6e−16,
   ‖W_direct − W_LU‖ = 8.5e−2. ✓
5. **App B pole cancellation.** h = Q₋⁻¹φ₊ = σiξ/(N₋(ξ)(θ−iξ)). Direct algebra:
   −σ/N₋ + σθ[1/N₋ − 1/Φ]/(θ−iξ) = σ[iξ/N₋ − θ/Φ]/(θ−iξ) = h − (θ/Φ)φ₊. First
   piece: 1/N₋ analytic in LHP ⇒ anticausal + lag-zero atom (constant at ∞).
   Second piece: pole at ξ = −iθ cancelled by the vanishing bracket, analytic in
   LHP, decays ⇒ anticausal. Hence Π₊h = (θ/Φ)φ₊. ✓
6. **N₋(−iθ) = N₊(iθ) = Φ(θ) and the Szegő form (eq. phi).** Evenness of N gives
   N₋(ξ) = N₊(−ξ); the Poisson–Szegő integral for N₊(iθ) loses its odd part,
   leaving exp[(θ/2π)∫log N/(θ²+t²)dt] > 0. ✓
7. **Value (eq. value, v = σ²θ/4Φ²).** At the optimum of ⟨u,α⟩ − ½⟨u,Qu⟩ on the
   adapted subspace, v = ½E[u★α]; Parseval with φ̄₊ = Q₊h̄ turns ∫ĝφ̄₊ into
   ⟨Π₊h, h⟩ = ‖Π₊h‖²; ‖φ₊‖² = πσ²/θ gives v = (1/4π)(θ/Φ)²·πσ²/θ = σ²θ/4Φ². ✓
   Benchmark v_ant = (1/4π)∫S_α/q also rederives. ✓
8. **Exponential factorization (eq. exp-factor).** Ĝ = 2κ/(κ²+ξ²) ⇒ N =
   (Aξ²+λκ²)/(κ²+ξ²), A = 2κγ+λ. N₋N₊ = A(m²+ξ²)/(κ²+ξ²) with m² = λκ²/A, i.e.
   m = κ√(λ/A): matches. Zero (ξ = −im) and pole (ξ = −iκ) of N₊ both in the LHP,
   so N₊ is analytic and zero-free in the UHP. ✓
9. **EMA form (eq. ema) and limits.** Φ = √A(m+θ)/(κ+θ) ⇒ H = [θ(κ+θ)/(A(m+θ))]
   ·(κ−iξ)/(m−iξ); (κ−iξ)/(m−iξ) = 1 + (κ−m)/(m−iξ), and 1/(m−iξ) is the EMA at
   rate m. λ→0: m→0, A→2κγ, u★ = (κ+θ)/(2κγ)(α̇+κα). λ→∞: m→κ, EMA weight κ−m→0,
   coefficient → θ/λ (Markowitz, consistent with E_t[μ_t] = θα for OU). ✓
10. **GP recovery (eq. gp).** N₊ = √η(a−iξ), Φ = √η(a+θ), H = θ/(η(a+θ)(a−iξ)).
    Partial adjustment û = a(c−H)α̂ with c = [a/(a+θ)]θ/λ requires H(a−iξ) = ac;
    both sides equal θ/(η(a+θ)) using a² = λ/η. ✓
11. **NV biquadratic (eq. nv-factor, nv-filter) and degenerations.** Expanding
    η(b₁²+ξ²)(b₂²+ξ²) against ηξ⁴+(ηκ²+2κγ+λ)ξ²+λκ² gives b₁²+b₂² = κ²+(2κγ+λ)/η,
    b₁²b₂² = λκ²/η. Residues of (κ−z)/((b₁−z)(b₂−z)) give w_i = (κ−b_i)/(b_j−b_i).
    γ = 0: sum κ²+λ/η, product λκ²/η ⇒ roots {a,κ}; the (κ−iξ) factor cancels ⇒
    one EMA (GP). η→0: b₁² → λκ²/A ⇒ b₁ → m; √η b₂ → √A ⇒ eq. (exp-factor).
    Hand-recomputed the script's point (η=.5, γ=1, κ=2, λ=1): s₂ = 14, p₂ = 8,
    b₁ = 0.7726, b₂ = 3.6610, Φ = √0.5·1.7726·4.6610/3 = 1.9475, X = 0.2637. ✓
12. **Gohberg–Krein kernel (eq. gk-kernel).** Beyond the numerical Check C
    (C₋C₊/G ratio = 1.000000 at 9 (β,t,v) points, T = 3), I verified the
    normalization in closed form in the T→∞ limit: ∫₀^∞u^{ν−1}(u+d)^{ν−1}du =
    d^{2ν−1}Γ(ν)Γ(1−2ν)/Γ(1−ν), and c_β·Γ(1−2ν)/(Γ(ν)Γ(1−ν)) =
    2sin(πβ/2)sin(πν)Γ(1−β)Γ(β)/π = 2sin(πβ/2)cos(πβ/2)/sin(πβ) = 1 (using
    ν = (1−β)/2, reflection formula). So C₋C₊ = γ|t−v|^{−β} exactly, constant
    included. Check A2 confirms T*T is T-dependent, so the anchoring is forced. ✓
13. **Response formula (eq. response).** E[u_{t+q}α_t] = ∫₀^∞g(τ+q)σe^{−θτ}dτ;
    the atom a₀δ sits at τ = −q < 0 and is excluded as q↓0 (forward increment
    ⊥ F_t). R = (2θ/σ)[ĝ(iθ) − a₀]; ĝ(iθ) = θ·(θ/Φ)·(1/Φ)·σ/(2θ) = σθ/2Φ²;
    a₀ = θσc₁/Φ ⇒ R = (θ²/Φ)[1/Φ − 2c₁]. X = θ/Φ² by both contour integration
    (pole at ξ = iθ) and Laplace evaluation; positive for every kernel. ✓
14. **c₁ (App C).** Two integrations by parts: Ĝ(ξ)ξ² → −2G′(0⁺) for kink
    kernels (exp check: 2κ/ξ²·ξ² = 2κ = −2·(−κ)), so N(∞) = λ−2γG′(0⁺) = c₁⁻²;
    power-law cusp and any η > 0 give N → ∞, c₁ = 0. ✓
15. **Threshold and always-contrarian condition (eq. threshold).** 2c₁Φ > 1 ⇔
    2(m+θ)/(κ+θ) > 1 ⇔ θ > κ−2m (LHS increasing in θ since m < κ always ⇒ single
    flip); θ* ≤ 0 ⇔ κ ≤ 2m ⇔ λ/(2κγ+λ) ≥ 1/4 ⇔ λ ≥ 2κγ/3. Pure risk:
    Φ = c₁⁻¹ = √λ ⇒ R = −θ²/λ, X = θ/λ. λ→0: R = (κ²−θ²)/2κγ — cross-checked
    against the direct computation E[c(α̇+κα)|α] = c(κ−θ)α, and the atom weight
    a₀ = σ(κ+θ)/2κγ matches the α̇ coefficient times σ. All consistent. ✓
16. **Fractional limit (eq. fractional).** (−iξ)^{−ν}(iξ)^{−ν} = |ξ|^{−2ν} on
    ℝ, 2ν = 1−β ⇒ q = γc_β|ξ|^{β−1} factors as Q_± = (γc_β)^{1/2}I_±^ν; prefactor
    (γc_β)^{−1} in u★. OU whitening: Marchaud D₋^ν of e^{−θ(·−s)} at s equals
    θ^ν α_s via ∫₀^∞(1−e^{−θh})h^{−1−ν}dh = θ^νΓ(1−ν)/ν. Value: Φ² = γc_βθ^{1+β}
    ⇒ v = σ²θ^{−β}/4γc_β. ν ∈ (0.2,0.4) for β ∈ (0.2,0.6). ✓
17. **Crossover frequencies (§4).** λ/ξ² = γc_βξ^{β−1} ⇒ ξ_c = (λ/γc_β)^{1/(1+β)};
    η = γc_βξ^{β−1} ⇒ ξ_* = (γc_β/η)^{1/(1−β)}. ✓
18. **Numerical table (§6.3).** Formula values recomputed by hand: row 1
    Φ = 1.3132, R = −0.3107, X = 0.8698; row 2 Φ = 2.1657, R = −0.0283, X = 0.1066;
    row 4 Φ = 3.3136 (script quadrature), R = 0.3643, X = 0.1822; row 5 as item 11.
    Discrete values traced to script runs: rows 1, 4 at dt = 0.01; rows 2–3 at
    dt = 0.04; row 5 at dt = 0.02 (see F2 for the presentation issue). Signs and
    the always-contrarian row (λ = 4 > 2κγ/3 = 4/3, θ* = −0.828) confirmed. ✓
19. **Discretization (§6.3 header).** FOC scaling of the discrete objective
    Σu_iα_i dt − ½[ηΣu_i²dt + γΣΣG_{ij}u_iu_j dt² + λΣx_i²dt], x = dt·Lu, divided
    by dt, gives exactly ηI + γ dt G + λ dt² LᵀL — matches the script's Cmat. ✓
20. **Dimensional consistency.** [γκ] = [λ] = [η]/time² throughout; m, a, b₁, b₂
    all have dimension 1/time; θ*(dimension 1/time) and the condition λ ≥ 2κγ/3
    (both sides [λ]) are homogeneous; v = σ²θ/4Φ² has [α²/q-units·time⁻¹] as a
    P&L rate. No inhomogeneity found. ✓
21. **Szegő condition (§2.1).** log q ~ −2log|ξ| at both ends (λ > 0 at 0, decay
    at ∞) or log of constant; integrable against dξ/(1+ξ²) in all cases used. ✓
22. **GSS exponent sign.** (β−1)/2 < 0 ⇒ endpoint-divergent U-shape, consistent
    with the cited bucket-shaped liquidation profiles. ✓

---

## Inline Annotations

> "with $\hat g \in L^2$ guaranteed by a spectral-decay hypothesis on $S_\alpha$ (Appendix B)"

**[F1] MAJOR:** The App B hypothesis ∫(1+ξ²)S_α/q dξ < ∞ fails for OU + exponential
kernel with η = 0 (integrand ~ ξ²σ²/A) and for pure risk, which are the cases §5.1
and table rows 1–3 use. ĝ has a white-noise atom there and is not in L². Scope the
theorem to the position filter, or add the atom case explicitly.

> "the exponential family converges to the formulas under $dt$-refinement to under $1\%$"

**[F2] MAJOR:** Demonstrated only for row-1 R (0.45%). Row-1 X is 1.1%; the NV row
is 8.7% off in R at the reported dt = 0.02 and 2.2% at dt = 0.005 (my rerun). The
convergence is first-order and consistent with the formulas, but "under 1%" is not
what the artifacts show.

> "the residual power-law discrepancy matches the quadrature bias of the singular kernel measured at the analytically known $\lambda=0$ point on the same grid"

**[F2] MINOR:** At dt = 0.01 the calibration bias is 6.2% and the row-4 bias is
10.7%. Same sign and order of magnitude; not a match.

> "All closed forms are verified against discretized adapted optima (\S6.3)."

**[F3] MAJOR:** §6.3 verifies R and X at five points. The value formulas, the GP
identity, and the EMA kernel shapes are verified analytically only. Weaken the
claim or add the checks.

> "Hence for adapted $u$, $Q_+^{-1}P_+Q_-^{-1}\,(P_+QP_+)\,u = \dots = u$."

**[F4] MINOR:** Left inverse only. Add the symmetric line
P₊Q₋Q₊(Q₊⁻¹P₊Q₋⁻¹)α = P₊Q₋P₊(Q₋⁻¹α) = α (Q₋ preserves the complement), or invoke
positivity of P₊QP₊ on the adapted subspace.

> "The unique adapted optimum of \eqref{eq:objective} is"

**[F5] MINOR:** For η = 0 the optimum is not in L² of rates (E[u_t²] = ∞ when
c₁ ≠ 0). Specify the admissibility class (adapted processes of finite cost /
q-energy completion) in the setup.

> "$P_+$ acts on symbols as the Riesz projection $\Pi_+$ (truncation to non-negative lags)"

**[F6] MINOR:** App B and App C annihilate lag-zero atoms; the operative convention
is truncation to positive lags. Align the wording here.

> "verified by direct kernel integration ($C_-C_+ = G_T$ exactly, including the constant)"

**[O1] OPTIONAL:** True (Check C, and I confirmed the constant analytically via the
Beta-integral identity c_βΓ(β)sin(πν)/π·(reflection) = 1), but G_T must be read as
the γ-weighted cost kernel for the constant to come out; make the γ-convention
explicit.

> "with error decaying as $d(t)^{-\nu}$ ... (Marchaud tail truncation; the weight deviation contributes at the faster rate $d(t)^{-1}$)"

**[O2] OPTIONAL:** Asserted without derivation anywhere in the repo. Label as a
heuristic estimate or add the two-line computation.

---

## Sources

- `tex/optimal-trading-filters.tex` (reviewed artifact)
- `experiments/risk_response_check.py` — run as-is and with dt-refined reruns via
  read-only `python -c` wrappers (no files modified)
- `experiments/extension_response_check.py` — read (single/mixture exponential
  response validation; consistent with Prop. 3 specializations)
- `experiments/review_factorization_check.py` — run as-is (Checks A, A2, B, C)
- `CHANGELOG.md`, entries dated 2026-07-18 (validation provenance)

No external URLs were consulted; all verification was by hand derivation and
local script execution.
