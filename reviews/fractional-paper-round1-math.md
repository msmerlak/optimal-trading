# Math Review — `papers/fractional-derivative-optimal-execution.md`, Round 1

Reviewer scope: mathematical correctness of the recently added content
(§4.1, §5.3, §5.4, Appendices A–E). I read the file directly (untracked)
and verified each formula listed in the brief. No edits applied.

Conventions used below: `ν := (1-γ)/2`, `γ ∈ (0,1)`.

---

## FATAL

### F1. Wrong order on the central object: "fractional derivative of order γ" should be "of order 1−γ".

Locations: abstract (lines 14–18), §1.2 item 1 (line 60), §1.1 displayed
identity (line 50), §3.2 (lines 184–192), Theorem 4.1 statement (line
235), Theorem 6.1 (line 372), §8/§9 throughout.

The decay kernel is `G(t)=c t^{-γ}`. Writing `t^{-γ} = Γ(1-γ)·t^{(1-γ)-1}/Γ(1-γ)`,
convolution by `G` equals `c·Γ(1-γ)` times the Riemann–Liouville
fractional integral of order `ν=1−γ`. Its inverse on the half-line is
therefore the RL fractional derivative of order `1−γ`, not `γ`. The
same conclusion holds in Fourier on the real line: the symbol of
`|t|^{−γ}` is `c_γ |ξ|^{γ−1}` (correctly displayed at line 322), and
its multiplicative inverse is `|ξ|^{1−γ}` — the symbol of the Riesz
derivative of order `1−γ` (= `(−Δ)^{(1−γ)/2}`). The symmetric Riesz
operator defined in §3.2 as `½(D^γ_+ + D^γ_−)` has symbol `|ξ|^γ cos(πγ/2)`,
which is the *wrong order* to invert the kernel of (★).

Sanity check via the paper's own arithmetic: in A.2 the Sonine pair
exponent is `ν = (1−γ)/2`, i.e. the "half order" of `1−γ`. If the
operator were truly of order γ, the Sonine half-order would be `γ/2`,
not `(1−γ)/2`. The half-order used in A.2 contradicts the order
asserted in Theorems 4.1 and 6.1.

This is a labeling error, not (necessarily) a formula error — but it is
the headline identity of the paper and is repeated in the abstract, the
contributions list, and every theorem statement. It must be fixed
globally: `D^γ` → `D^{1−γ}`, `κ_γ` definition unchanged, "fractional
derivative of order γ" → "of order 1−γ", everywhere.

### F2. Wrong exponent in the boundary / U-shape term `𝓑_γ`.

Locations: Theorem 4.1 (line 243), Corollary 4.2 (line 286), A.2 last
line (`v_t(s) = … + c_1 (s(T-s))^{ν−1}` and `𝓑_γ(t):=c_1(t(T-t))^{ν−1}`).

With `ν=(1−γ)/2`, `ν−1 = −(1+γ)/2`, so the paper's exponent is
`−(1+γ)/2`. The Gatheral–Schied–Slynko U-shape for `G(t)=t^{−γ}` has
exponent `(γ−1)/2 = −ν` (the unique null-space element of the
symmetric Abel operator on `[0,T]` integrable at the endpoints; see
Tricomi 1957 §4.3 and GSS 2012). Numerical check `γ=1/2`: GSS gives
`u_h(t) ∝ [t(T−t)]^{−1/4}`; the paper gives `[t(T−t)]^{−3/4}` — the
latter is not even in `L^1` near the endpoints, violating
admissibility.

Correct form: `𝓑_γ(t) = c_1 (t(T−t))^{(γ−1)/2} = c_1 (t(T−t))^{−ν}`.
The Chakrabarti–George/Söhngen formula in A.2 needs the same correction
in its second additive term (`(s(T−s))^{ν−1}` → `(s(T−s))^{−ν}`).
This is a real error, not just relabeling: the homogeneous solution
must lie in `L^1(0,T)` and have unit integral; only the `−ν` exponent
satisfies both.

### F3. Missing constant `c·Γ(1−γ)` in the Mittag–Leffler kernel of Theorem 5.1.

Locations: Theorem 5.1 (lines 326–328) and the displayed sum in B.2
(line 658 in my reading, the line beginning `Σ ... = -(1/(2η)²) |t|^{-γ} E_{1-γ,1-γ}(...)`).

Re-summing the Neumann series of B.1 with the correct iterated kernel
of B.2:

```
v_t = Σ_{n≥0} (-1)^n (2η)^{-(n+1)} c^n · (t^{-γ})^{*n} ∗ f_t
    = (2η)^{-1} f_t
      - (2η)^{-2} · c·Γ(1-γ) · |t-s|^{-γ} · E_{1-γ,1-γ}(z) ∗ f_t,
  z = -c·Γ(1-γ)/(2η) · |t-s|^{1-γ}.
```

Reindex `m = n − 1` and pull out a factor of `c·Γ(1−γ)/(2η)` from the
`n=1` term to align with `E_{1−γ,1−γ}`. The paper writes

```
R = (2η)^{-1} δ - (2η)^{-2} · |t-s|^{-γ} · E_{1-γ,1-γ}(...)
```

which is missing the multiplicative `c·Γ(1−γ)` in front of the
non-delta piece. Without that prefactor, the `η→0` limit cannot match
Theorem 4.1 (which carries `κ_γ = (cΓ(1−γ))^{−1}`), and the `c→0`
limit fails to reproduce `R = (2η)^{−1} δ`.

The argument inside `E_{1−γ,1−γ}` is correct; the iterated-convolution
formula `(t^{−γ})^{*n}(t) = Γ(1−γ)^n / Γ(n(1−γ)) · t^{n(1−γ)−1}` in
B.2 is correct (verified for `n=1,2` against the Beta function); the
identification `E_{1−γ,1−γ}(z) = Σ z^k/Γ((k+1)(1−γ))` is correct.
Only the leading scalar prefactor of the non-delta term is dropped.

---

## MAJOR

### M1. Chakrabarti–George kernel in A.2: structurally right, but the `f'` vs `f` form is suspect.

Location: A.2 (lines 605–613).

The weighted finite-Hilbert form

```
(s(T-s))^{-ν} (v(T-v))^{ν} / (s-v),  with ν=(1-γ)/2
```

is the correct *Söhngen / Tricomi airfoil-type weight* for inversion of
`∫|s−v|^{−γ}` on a bounded interval; it specializes to the standard
airfoil weight `[s(T-s)/v(T-v)]^{1/2}/(s-v)` at `γ=0` (`ν=1/2`).
However, the standard explicit form (Tricomi 1957 §4.3 eq. (4.3.13);
Samko–Kilbas–Marichev §13.2) places `f(v)` (not `f'(v)`) inside the
integral with the `(d/ds)` *outside*:

```
v(s) = (const) · (d/ds) ∫_0^T (s(T-s))^{-ν} (v(T-v))^{ν} f(v)/(s-v) dv + c_1 (s(T-s))^{-ν}.
```

Writing `f'(v)` under the integral implicitly integrates by parts; the
boundary terms `[f(v) · weight]_{v=0}^{v=T}` are nontrivial because the
weight `(v(T-v))^{ν}` vanishes at endpoints only for `ν>0`, but the
finite-Hilbert kernel `1/(s-v)` introduces a singularity that gives
nonzero limiting endpoint contributions for general `f`. The paper's
form is therefore correct **only** if `f` is sufficiently smooth and
`f(0)=f(T)=0` — neither of which holds when `f(s)=λ−ᾱ(t,s)` with
nonzero `λ` and generic `ᾱ`. Either restore the standard form with `f`
inside and `d/ds` outside, or explicitly carry the boundary terms
generated by the IBP.

The prefactor `1/π` (paper) versus `−sin(πν)/π² = −cos(πγ/2)/π²·1/sin(πν)`-type
constants in the references should also be reconciled. This is at
minimum a constants-and-conventions check, but absent that check the
formula as written is not consistent with any single edition of the
inversion theorem I can match.

### M2. Wiener–Hopf factorization in B.4 — correct on the real line, but the **constants and analyticity sides are stated inconsistently with the rest of the paper**.

Location: Proposition 5.2 (lines 326–344) and B.4 (lines 668–693).

Branch-cut check: with principal branch of `z^β` on `ℂ∖(−∞,0]` and
`β=(γ−1)/2 ∈ (−1/2, 0)`,

- For `ξ>0`: `(−iξ)^β = ξ^β e^{−iπβ/2}`, `(iξ)^β = ξ^β e^{iπβ/2}`,
  product `= ξ^{2β} = ξ^{γ−1} = |ξ|^{γ−1}` ✓
- For `ξ<0`: `(−iξ) = i|ξ| = |ξ|e^{iπ/2}`, `(iξ) = −i|ξ| = |ξ|e^{−iπ/2}`,
  product `= |ξ|^{2β} = |ξ|^{γ−1}` ✓

So the factorization identity holds on `ℝ\{0}`. Analyticity:
`(−iξ)^β` extends analytically to `Im ξ > 0` (where `−iξ` has positive
real part), and `(iξ)^β` to `Im ξ < 0`. ✓

Three remaining issues:

(a) **Halves vs full order.** Paper writes `Ĝ_±` as the Fourier
   multipliers of the *causal/anti-causal Riesz potentials*
   `I_±^{(1−γ)/2}`. But `(−iξ)^β` with `β=(γ−1)/2 < 0` is the symbol
   of a *fractional integral* of order `−β = (1−γ)/2` (since
   `(−iξ)^{−s} = symbol of I_+^s` for `s>0`). So writing
   `Ĝ_+ ↔ I_+^{(1−γ)/2}` is correct, but Corollary 5.3 then claims

   ```
   u*_t = κ · D_+^{(1-γ)/2} · Π_+ · D_-^{(1-γ)/2} (forecast)(t)
   ```

   where the **fractional derivatives** `D_±^{(1−γ)/2}` appear with
   the **same order** as the integrals. This is correct *only because*
   the W–H solution applies `Ĝ_±^{−1}`, which inverts the integrals
   into derivatives of the same order. Worth a one-sentence clarification:
   `Ĝ_±` are integrals, `Ĝ_±^{−1}` (which appear in u*) are derivatives.

(b) **Constants.** `c_+ c_- = c·Γ(1−γ)·sin(πγ/2)` is asserted, but
   absorbing branch phases is not the same as fixing `c_±` individually;
   the W–H factorization is unique only up to a multiplicative constant
   on each factor. The paper should say `c_+ c_- = c_γ` and pick one
   normalization (e.g. `c_+ = c_- = c_γ^{1/2}`).

(c) **Compatibility with F1.** The W–H operator product
   `D_+^{(1−γ)/2} · Π_+ · D_-^{(1−γ)/2}` is "of total order `1−γ`",
   which once again contradicts the paper's labeling "causal Riesz
   fractional derivative of order γ" in the prose just after the
   display. Same off-by-(1↔1−γ) labeling error as F1.

### M3. Adaptedness claim in Corollary 5.3 — almost right, but slips on the W–H statement of (★_WH).

Location: §5.4 (★_WH) statement at line 318 and Corollary 5.3 lines 350–365.

The W–H equation (★_WH) is stated for the realized signal `α_t`, not
the forecast curve, but the unknown `u*` appears under the kernel on
*all* of `[0,∞)`, so any pointwise solution must also be `F_t`-adapted.
The Corollary then quietly switches to the forecast curve
`ᾱ^∞(t,s)`. This is the same projection step as A.1 but is not stated
or justified here — it should be. Once stated, the adaptedness
*conclusion* is correct: the right-sided operator `D_−^{(1−γ)/2}`
applied at the point `s=t` to the function `s↦ᾱ^∞(t,s)` reaches into
`s>t`, but those values are `E_t[α_s]`, which are `F_t`-measurable by
construction. So the adaptedness claim is justified; only the route to
it is under-stated.

### M4. Matrix decoupling in Appendix C — correct.

Location: Appendix C (lines 730–757).

Verified: with `C = QΛQ^⊤`, `ũ = Q^⊤ u`, `α̃ = Q^⊤ α`, the quadratic
form `u_t^⊤ C u_v |t−v|^{−γ}` becomes `Σ_i λ_i ũ_{i,t} ũ_{i,v} |t−v|^{−γ}`
and the linear term `u·α = ũ·α̃`; the budget rotates to
`∫ ũ dt = Q^⊤ X_0`. Component-wise the effective scalar problem has
impact constant `c_i = c λ_i`, giving `κ_{γ,i} = κ_γ/λ_i`. Stacking
and inverting:

```
u* = Q Λ^{-1} Q^⊤ · κ_γ D^γ_{[0,T]} [λ − ᾱ](t) + Q B
   = C^{-1} κ_γ D^γ_{[0,T]} [λ − ᾱ](t) + B^vec        ✓
```

The order-of-operations remark (`D^γ` commutes with constant matrices
`Q,Q^⊤` because it acts on `t`) is needed and is present. The only
caveat is the same F1 mislabeling (`D^γ` ↦ `D^{1−γ}`).

### M5. §5.3 exponential bullet — content correct, but the recovery sentence overstates.

Location: §5.3 bullet at lines 343–354.

The assertion "γ→1⁻ does **not** recover OW" is correct: as γ→1⁻ the
kernel `c t^{−γ}` becomes more singular at the origin and does not
converge to `ρe^{−ρt}` in any reasonable sense. The qualitative
distinction (no characteristic timescale vs. exponential timescale) is
the right reason.

However, the follow-on claim that "Theorem 5.1 specializes to the
Neuman–Voß / Obizhaeva–Wang solution after the standard
exponential-kernel resolvent computation" by *replacing* `G` with
`ρe^{−ρt}` is misleading: Theorem 5.1 was *derived* for the power-law
kernel via Sonine inversion and Mittag–Leffler reseummation. Replacing
the kernel invalidates the derivation; you need a separate (much
shorter) Markov-Riccati computation to get OW. The statement should
read "the *analogous* derivation with `G = ρe^{−ρt}` yields the OW
kernel via `E_{1,1}(z)=e^z`" rather than implying Theorem 5.1
specializes.

The pointer to Abi Jaber–Bondi et al. 2025 (multi-exponential
approximation) as the bridge between regimes is appropriate.

---

## MINOR

### m1. Mittag–Leffler iterated-convolution formula in B.2 is correct but the convergence claim is weak.

Verified the closed form `(t^{-γ})^{*n}(t) = Γ(1-γ)^n/Γ(n(1-γ)) · t^{n(1-γ)-1}`
for `n=1,2` against the Beta integral; series ↔ `E_{1−γ,1−γ}` identification
verified. The Neumann-series convergence condition stated as
`‖η^{−1}𝒢‖_{L²} < 2` is asserted via "spectral bound on the symmetric
Riesz potential, SKM §8.3"; the citation is correct in spirit but the
norm of the symmetric Riesz potential on a finite interval is not the
same as its norm on `ℝ` (which is what SKM §8.3 gives). A quick
remark on the finite-interval bound (e.g. via Hardy–Littlewood–Sobolev
restricted to `(0,T)`) is needed.

### m2. §2.4 sign convention.

The FOC in (★) (line 130) writes RHS as `λ − E_t[α_T] + α_t`. With
sign convention "u>0 is selling" (line 119), and signal `α_t = E_t[P_T − P_t]`
(line 110), this requires the cross-check that subtracting expected
signal pickup `E∫ u α` and adding the Lagrange penalty gives the
written sign; the algebra works out but the `−E_t[α_T] + α_t`
combination begs the question of why both endpoint values of `α`
appear. A one-line derivation (showing where the `−E_t[α_T]` comes
from — presumably the boundary contribution of integration by parts on
the price impact path) would be helpful and would also make the
`λ − E_t[α_T] + α_t` notation in Theorems 5.1 and 6.1 less
mysterious.

### m3. `κ_γ` constant probably missing `sin(πγ/2)` factors.

The Riesz potential of order `1−γ` in 1D is conventionally normalized
as `I^{1-γ}f(x) = (1/(2Γ(1−γ)cos(π(1−γ)/2))) ∫|x−y|^{−γ}f(y)dy
            = (1/(2Γ(1−γ)sin(πγ/2))) ∫|x−y|^{−γ}f(y)dy`.

So inverting `∫|t−v|^{−γ}u(v)dv = c^{−1}f(s)` yields
`u = (2Γ(1−γ)sin(πγ/2))/c · D^{1−γ}_Riesz f`, i.e.
`κ_γ = 2 sin(πγ/2)/(c Γ(1−γ))` — a factor of `2 sin(πγ/2)` off from
the paper's `(cΓ(1−γ))^{−1}`. The factor reappears in §5.4's Fourier
symbol (line 322), so the paper is *internally* aware of it; it is
only missing inside `κ_γ`.

### m4. §3.2 Sonine-pair sentence (line 192).

"`(I^ν_+ I^{1-ν}_- f)(t) = ∫_0^T k_γ(t,s) f(s) ds`" — the composition
of left and right RL operators is *not* a simple convolution on `[0,T]`;
the resulting kernel `k_γ` is the Sonine kernel built from
incomplete-Beta integrals. The sentence as written suggests a tidy
identity that is in fact much messier. Reword to "yields an explicit
weighted finite-interval kernel; see SKM §10.4."

### m5. Corollary 4.3 (Forde et al. recovery) — Riemann–Liouville semigroup statement is too strong.

"`D^ν I^μ = I^{μ−ν}` on `ν<μ`" is true on the whole half-line for
suitably regular `f`, but on `[0,T]` boundary corrections appear; A.3
acknowledges this in the hand-waving flag but the statement of the
identity itself should at least be marked as "modulo boundary terms".

---

## NITS

### n1. `(★)` RHS labeling. Line 130 writes `(★)` RHS as `λ − E_t[α_T] + α_t`, while §5.1 (★★) and Theorem 5.1 use the same combination. Once you've defined `ᾱ(t,s)` (which in particular gives `ᾱ(t,T) = E_t[α_T]` and `ᾱ(t,t) = α_t`), this is just `λ − ᾱ(t,T) + ᾱ(t,t)`. Consider rewriting in `ᾱ` notation throughout for consistency.

### n2. The remark "η→∞ … Almgren–Chriss myopic" (line 339) is loose. Almgren–Chriss "myopic" usually refers to the inventory-tracking limit `u ∝ X/(T−t)`, not the signal-tracking limit `u ∝ α/(2η)`. The latter is closer to Cartea–Jaimungal's quadratic-cost / linear-signal benchmark. Rename.

### n3. Theorem 5.1 kernel: writing `R(t,s) = ... |t−s|^{-γ} E_{1-γ,1-γ}(−c'|t−s|^{1−γ})` is fine, but flag that this is a *translation-invariant* kernel — which is only correct on the line; on `[0,T]` the true kernel has boundary corrections (acknowledged in B.2 hand-wave). Make this explicit in the theorem statement.

### n4. B.4 line 689: "log Ĝ ∈ L²_loc(ℝ) with controlled growth at infinity". Actually `log|ξ|^{γ−1} = (γ−1)log|ξ|`, which is in `L²_loc` near `0` (logarithm² is integrable) and grows like `log|ξ|` at `∞`. State the bound used (Krein's condition `∫ log(1+|ξ|)·|log Ĝ(ξ)|/(1+ξ²) dξ < ∞`) rather than the looser `L²_loc`.

### n5. A.1 line 587: "stochastic Fredholm equation … P-a.s." then "projecting onto F_t … yields the deterministic Fredholm equation in the forecast curve". The "deterministic" here means "deterministic given `F_t`", i.e. measurable w.r.t. `F_t` and a fixed function of `s`. Worth one sentence so the reader doesn't wonder how a stochastic equation becomes literally deterministic.

### n6. Appendix D Grünwald–Letnikov: weights `w_m^{(γ)} = (-1)^m C(γ,m)` give the symbol approximation to `D^γ`, not to the symmetric `½(D^γ_+ + D^γ_−)`. The symmetric stencil uses `(w_m + w_{−m})/2 = w_{|m|}` only because Grünwald weights are even-extended by construction in the formula given; but the *order of accuracy* at the boundary becomes `O(h^{1−γ})` (correctly noted), which is barely first-order. Recommend referencing the centered/shifted variants (e.g. Çelik–Duman 2012; the WSGD reference is already cited).

---

## Summary

The §4.1 forecast-curve construction and the adaptedness reasoning
(Remarks 4.1.1 and the analogous claim in Corollary 5.3) are
substantively correct: replacing the realized future path by its
`F_t`-conditional forecast before applying the non-causal operator is
the right move and produces an admissible strategy.

The §5.3 statement that `γ→1⁻` does **not** recover OW is correct.

The matrix decoupling in Appendix C is correct.

The W–H factorization identity in B.4 is correct on the real line
(branch analysis verified).

The Mittag–Leffler iterated-convolution identity in B.2 is correct.

Three problems must be fixed before the paper is internally consistent:

1. **F1 — wrong order on the central operator.** "Fractional derivative
   of order γ" should be "of order `1−γ`" throughout. The Sonine
   half-order `(1−γ)/2` in A.2 is self-evidence of the correct order.

2. **F2 — wrong exponent in the U-shape boundary term.** `𝓑_γ(t)`
   should be `c_1 (t(T-t))^{(γ-1)/2}`, not `c_1 (t(T-t))^{(1-γ)/2-1}`.
   The paper's exponent is not in `L¹(0,T)` for `γ ∈ (0,1)`, violating
   admissibility, and disagrees with GSS 2012.

3. **F3 — missing constant in Theorem 5.1.** The non-delta piece of
   `R_{γ,η}` is missing a multiplicative factor `c·Γ(1−γ)`. Without it,
   neither the `η→0` nor the `c→0` limit is recovered.

Secondary: the Chakrabarti–George kernel form in A.2 needs an
`f`-vs-`f'` and prefactor reconciliation against Tricomi §4.3, and
`κ_γ` likely needs an extra `2 sin(πγ/2)`. These are constants/IBP
issues, not structural.

Once F1–F3 and m3 are fixed, the appendices land cleanly modulo the
authors' own hand-waved-regularity flags, which are appropriate for a
skeleton draft.
