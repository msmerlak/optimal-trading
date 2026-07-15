# Math Review — `papers/fractional-derivative-optimal-execution.md`, Round 2

Reviewer scope: math-only follow-up after the Round 1 fixes documented
in the Changelog (file end). I checked all six focus items from the
worker's open-risks list, plus a fresh scan of the convention-rewrite
sites (Cor 4.2, Cor 5.3, §6.2, Appendix B). Round 1 items already
addressed (F1 order, F2 exponent, F3 prefactor, m1–m4, n1–n6, etc.)
are not re-flagged.

Notation: `ν := (1−γ)/2`, `γ ∈ (0,1)`.

---

## MAJOR

### M1. §3.2 definition of $\mathbb{D}^{1-\gamma}_{[0,T]}$ is not the operator that A.2 actually uses.

Locations: §3.2 line 238 (definition) and A.2 line 826 (closed form).

§3.2 *defines*
$\mathbb{D}^{1-\gamma}_{[0,T]} := \tfrac{1}{2}(D^{1-\gamma}_+ + D^{1-\gamma}_-)$.
A.2 then *proves* that the inversion of the bounded-interval Abel
equation (A.1) is the Chakrabarti–George / Söhngen finite-Hilbert
operator with weights $(s(T-s))^{-\nu}(v(T-v))^{\nu}/(s-v)$ wrapped in
$d/ds$. These are not the same operator on $[0,T]$:

- $\tfrac{1}{2}(D^{1-\gamma}_+ + D^{1-\gamma}_-)$ is the "naïve"
  symmetrization of one-sided RL derivatives; on a bounded interval
  it does **not** invert $\int_0^T |s-v|^{-\gamma}\,\cdot\,dv$.
- The Chakrabarti–George operator (the weighted finite-Hilbert form
  in A.2) **does** invert that Fredholm operator, but it is genuinely
  different from $\tfrac{1}{2}(D^{1-\gamma}_+ + D^{1-\gamma}_-)$ — the
  endpoint weights $(s(T-s))^{\mp\nu}$ are precisely the boundary
  corrections that the naïve symmetrization misses (this is exactly
  why A.3's withdrawn semigroup argument failed).

The reworded §3.2 sentence already gestures at this ("composition does
not produce a simple convolution kernel; yields an explicit weighted
finite-interval kernel") and A.2's hand-wave flag (ii) explicitly
defers the identification. The two pieces taken together mean the
load-bearing operator in Theorem 4.1 is *defined* as one thing and
*computed* as another, and the identity between them is asserted
without proof. On the real line and the half-line the identification
holds (modulo constants); on $[0,T]$ it does not.

**Recommendation.** Either (a) redefine $\mathbb{D}^{1-\gamma}_{[0,T]}$
in §3.2 directly as the Chakrabarti–George operator (the form A.2
actually uses), with $\tfrac{1}{2}(D^{1-\gamma}_+ + D^{1-\gamma}_-)$
named only as the formal/Marchaud-side symbol; or (b) keep the §3.2
definition but state Theorem 4.1 in terms of the CG operator and
relegate $\tfrac{1}{2}(D^{1-\gamma}_+ + D^{1-\gamma}_-)$ to a remark
about the unbounded-interval analogue. Option (a) is cleaner; the
"natural inverse" claim in §3.2 lines 240–245 then becomes literally
true rather than aspirational.

This propagates into M2 below (the κ normalization), Cor 5.3 (where
the half-line operator *is* genuinely $\tfrac{1}{2}(D+_+D-_)$-type
modulo causal projection, so the two settings need distinct symbols)
and Appendix D (the Grünwald stencil discretizes the naïve
symmetrization, not the CG operator — a separate issue).

### M2. Remark 4.1.3's "either convention is internally consistent" claim is not yet true.

Location: Remark 4.1.3 lines 346–360.

The Riesz-normalization arithmetic in the remark is correct as far as
it goes:
- 1D Riesz potential of order $1-\gamma$: $I^{1-\gamma}f(x) =
  (2\Gamma(1-\gamma)\sin(\pi\gamma/2))^{-1}\int|x-y|^{-\gamma}f(y)\,dy$. ✓
  (Standard; matches Stein's normalization
  $\gamma_1(1-\gamma) = 2\Gamma(1-\gamma)\cos(\pi(1-\gamma)/2)
  = 2\Gamma(1-\gamma)\sin(\pi\gamma/2)$.)
- Hence inverting $\int|t-v|^{-\gamma}u\,dv = c^{-1}f$ on the line
  gives $\kappa = 2\sin(\pi\gamma/2)/(c\Gamma(1-\gamma))$. ✓

But the claim that the alternate $\kappa = (c\Gamma(1-\gamma))^{-1}$
"absorbs the $2\sin(\pi\gamma/2)$ into the symmetric operator
$\mathbb{D}^{1-\gamma}_{[0,T]}$" requires the operator to *carry* that
factor — and the §3.2 definition explicitly does not. The Fourier
symbol of $\tfrac{1}{2}(D^{1-\gamma}_+ + D^{1-\gamma}_-)$ is
$\tfrac{1}{2}\bigl((-i\xi)^{1-\gamma}+(i\xi)^{1-\gamma}\bigr)
= |\xi|^{1-\gamma}\cos(\pi(1-\gamma)/2) = |\xi|^{1-\gamma}\sin(\pi\gamma/2)$,
which already *equals* the pure-Riesz symbol $|\xi|^{1-\gamma}$ times
$\sin(\pi\gamma/2)$ (no factor of 2). So:

- If "$\mathbb{D}$" means $\tfrac{1}{2}(D+_+D-_)$ (as §3.2 says),
  the correct constant is $\kappa = 2/(c\Gamma(1-\gamma))$ — the lone
  $\sin(\pi\gamma/2)$ is absorbed, but the factor of 2 is still
  missing from the paper's $\kappa = (c\Gamma(1-\gamma))^{-1}$.
- If "$\mathbb{D}$" means the pure Riesz $|\xi|^{1-\gamma}$-symbol
  operator (which is what Remark 4.1.3 implicitly assumes), the
  correct constant is the full $\kappa = 2\sin(\pi\gamma/2)/(c\Gamma(1-\gamma))$.

Neither matches what is currently written. The ⚠️ TODO flag is
appropriate; the actual fix needs M1 resolved first (decide which
operator $\mathbb{D}$ denotes), then $\kappa$ follows. Until then the
"either convention is internally consistent" sentence overstates.

Cross-check: this is the same factor that *does* appear correctly in
the §5.4 Fourier-symbol display (`$c_\gamma := 2c\Gamma(1-\gamma)\sin(\pi\gamma/2)$`,
line 470) and in Corollary 5.3's normalization
$\kappa^\infty_{1-\gamma} = c_\gamma^{-1}$ — i.e. on the half-line the
paper carries the correct constant. The finite-interval side is the
one that needs to catch up.

### M3. A.2 Chakrabarti–George prefactor is almost certainly $\neq 1/\pi$.

Location: A.2 line 826 (`v_t(s) = (κ/π) d/ds ∫ ...`).

The standard inversion of the generalized Abel equation
$\int_0^T |s-v|^{-\gamma}u(v)\,dv = g(s)$ on a bounded interval
(Söhngen 1939; Tricomi 1957 §4.3; SKM 1993 §10.4 / §13.2) has the form

$$u(s) = -\frac{\sin(\pi\nu)}{\pi^2}\,(s(T-s))^{-\nu}\,\frac{d}{ds}\!\int_0^T\!\frac{(v(T-v))^{\nu}}{v-s}\,g(v)\,dv + c_1(s(T-s))^{-\nu},$$

with $\nu = (1-\gamma)/2$ and the weight $(s(T-s))^{-\nu}$ *outside*
the $d/ds$. The paper's form (weight inside the integral, prefactor
$1/\pi$) differs in two places:

1. **Prefactor.** $1/\pi$ should be $\sin(\pi\nu)/\pi^2 =
   \cos(\pi\gamma/2)/\pi^2$. The two differ by $\pi\sin(\pi\nu)$, which
   is *not* a constant absorbable into $\kappa$ — it depends on $\gamma$.
2. **Operator structure.** Placing $(s(T-s))^{-\nu}$ inside the
   $d/ds$ as the paper does changes the operator (you'd pick up
   $\nu(s(T-s))^{-\nu-1}(T-2s)$ on differentiating the weight); the
   weight outside form is the one that matches SKM §13.2 directly.

The hand-wave flag (i) already concedes the $1/\pi$ vs other-edition
issue. The fix is to (a) pick a specific edition — I recommend
SKM 1993 §13.2 Theorem 13.2 (Tricomi's airfoil equation) or
§10.4 Theorem 10.7 (generalized Abel) — and (b) restate A.2 with
weight outside the $d/ds$ and prefactor $\sin(\pi\nu)/\pi^2$ (with
sign per the convention chosen). The Chakrabarti–George (1994) paper
itself uses the $f$-inside form but for a different kernel
(`(s^\alpha - v^\alpha)^{-\beta}`, not symmetric $|s-v|^{-\gamma}$);
it should not be the primary citation here for the symmetric case.

Once the prefactor is corrected, M2's $\kappa$ should be re-derived
end-to-end from A.2 rather than asserted from the line-Riesz formula
in Remark 4.1.3.

---

## MINOR

### m1. (Focus 1) Sign reconciliation FOC $(\star)$ vs Thm 4.1 — correct, no IBP needed.

Quick derivation: cost $\mathcal{C}(u) - \mathbb{E}\!\int u\alpha + \lambda(\int u - X_0)$;
Euler–Lagrange in $\delta u$ on the symmetrized quadratic form gives
$\int G(|t-v|)u_v\,dv - \alpha_t + \lambda = 0$, i.e.
$\int G(|t-v|)u_v\,dv = \alpha_t - \lambda$. Applying the inverse
operator (whatever its precise normalization — see M2/M3) and using
the projection of A.1 gives
$u^*_t = \kappa\,\mathbb{D}^{1-\gamma}[\bar\alpha(t,\cdot) - \lambda](t)
+ \mathcal{B}$. The "$\bar\alpha - \lambda$" inside the brackets has
the same sign as "$\alpha_t - \lambda$" on the RHS of $(\star)$;
no sign flip and no boundary term from IBP arises (the projection
step is a conditional expectation, not an IBP). The Changelog item
"Sign-of-FOC vs sign-of-Theorem reconciliation … prose derivation
still implicit" can be discharged: the above two-line derivation is
all that's needed and can sit in §2.4. **Verdict: correct as
currently written; only the prose is missing.**

### m2. (Focus 4) Theorem 5.1 "boundary corrections absorbed into $\mathcal{B}_{1-\gamma}$" claim.

Location: Thm 5.1 lines 411–414 ("Boundary corrections on $[0,T]$ are
absorbed into the $\mathcal{B}_{1-\gamma}$ term inherited from
Theorem 4.1.")

The qualifier "away from the boundary of $[0,T]$" inside the kernel
display is now correctly present and the B.2 hand-wave flag is honest.
But the absorption claim is not quite right: $\mathcal{B}_{1-\gamma}$
is the null-space of $c\mathcal{G}$ (first-kind boundary term);
$R_{\gamma,\eta}$ is the resolvent of $(I + (2\eta)^{-1}c\mathcal{G})$
(second-kind operator), and its near-endpoint correction is not
generically the same function. The correction is *of the same
$(t(T-t))^{(\gamma-1)/2}$ type* asymptotically, but the coefficient
depends on $\eta$.

**Recommendation.** Soften to: "Near-endpoint corrections on $[0,T]$
take the same $(t(T-t))^{(\gamma-1)/2}$ form as $\mathcal{B}_{1-\gamma}$
but with an $\eta$-dependent coefficient determined by the budget
constraint; full characterization deferred." This keeps the theorem
honest without overclaiming.

### m3. (Focus 5) Corollary 4.3 and A.3 — appropriately hedged.

Cor 4.3 line 380: "**Corollary 4.3 (conjectural)** … *plausibly
recovers*". A.3 line 871: "*structural sketch only* … the argument is
therefore withdrawn; we leave the recovery as a conjecture". Abstract
line 17: "(conjectured here; full kernel-matching deferred)". §1.1
line 56: "(conjecturally; see §5.3)". §5.3 bullet also explicit.
No remaining over-claims. **Verdict: D4 is honestly executed.**

One micro-nit: the §1.2 contributions list does not flag the Forde
recovery as conjectural (item 1 just refers to the canonical form;
recovery is not separately enumerated). That is acceptable since
contributions list the canonical result, not the special-case
recoveries.

### m4. (Convention-rewrite scan, Cor 5.3) Order arithmetic and adaptedness — correct.

$(1-\gamma)/2 + (1-\gamma)/2 = 1-\gamma$ ✓. Causal projection $\Pi_+$
between the two half-order derivatives is the correct W–H recipe.
Adaptedness: $D_-^{(1-\gamma)/2}$ acts on $s\mapsto\bar\alpha^\infty(t,s)$,
which is $\mathcal{F}_t$-measurable by construction; the operator
reaches into $s>t$ but those values are $\mathbb{E}_t[\alpha_s]$,
hence still $\mathcal{F}_t$-measurable. The Changelog M5 propagation
landed. **Verdict: clean.**

Constants: $c_+c_- = c_\gamma = 2c\Gamma(1-\gamma)\sin(\pi\gamma/2)$ ✓;
$\kappa^\infty_{1-\gamma} = c_\gamma^{-1}$ ✓ (this is the correct
half-line constant; finite-interval constant M2 needs to be brought
into line with this).

### m5. (Convention-rewrite scan, Cor 4.2) Exponent fix is correct.

Line 372: $u^*_t = c_1(t(T-t))^{(\gamma-1)/2}$. Matches GSS 2012 and
the corrected $\mathcal{B}_{1-\gamma}$. $L^1$ admissible. ✓

### m6. (Convention-rewrite scan, §6.2 / App C) Matrix arithmetic correct.

Component-wise impact $c_i = \lambda_i c$ ⇒ $\kappa_{1-\gamma,i} =
(c_i\Gamma(1-\gamma))^{-1} = \kappa_{1-\gamma}/\lambda_i$;
stacking gives $u^* = C^{-1}\kappa_{1-\gamma}\mathbb{D}^{1-\gamma}[\cdots]
+ \mathcal{B}^{\rm vec}$ ✓ (commutativity of $\mathbb{D}^{1-\gamma}$
with constant $Q,Q^\top$ verified — operator acts on $t$ only). The
M1/M2 caveats on what $\mathbb{D}^{1-\gamma}_{[0,T]}$ means propagate
here unchanged.

### m7. (Convention-rewrite scan, Appendix B.2) Mittag–Leffler series — re-verified.

Re-summed: with $a := c\Gamma(1-\gamma)/(2\eta)$,
$\sum_{n\ge 1}(-1)^n(c/(2\eta))^n\Gamma(1-\gamma)^n/\Gamma(n(1-\gamma))\,t^{n(1-\gamma)-1}
= -a\,t^{-\gamma}\sum_{m\ge 0}(-at^{1-\gamma})^m/\Gamma((m+1)(1-\gamma))
= -a\,t^{-\gamma}E_{1-\gamma,1-\gamma}(-at^{1-\gamma})$.
Multiplying by $(2\eta)^{-1}$ from B.1 gives
$-(c\Gamma(1-\gamma)/(2\eta)^2)\,t^{-\gamma}E_{1-\gamma,1-\gamma}(\ldots)$.
**F3 fix verified line-by-line.** ✓

The $c\to 0$ limit gives $(2\eta)^{-1}\delta$ as claimed. The $\eta\to 0$
limit is genuinely singular (leading $(2\eta)^{-1}\delta$ blows up);
the "formally recovers Theorem 4.1" phrasing in §5.3 / B.3 is the
right level of caveat.

### m8. (New) Appendix D Grünwald stencil discretizes the wrong operator under the M1 reading.

If M1 resolves to "$\mathbb{D} := $ CG operator", then App D's
symmetric Grünwald–Letnikov stencil $w^{(1-\gamma)}_{|k-j|}$ does
*not* discretize that operator; it discretizes the naïve
$\tfrac{1}{2}(D+_+D-_)$. The Toeplitz / FFT speedup claim survives
(both operators have Toeplitz-like structure near the bulk), but the
near-endpoint accuracy claim needs revisiting because the CG weights
$(s(T-s))^{-\nu}$ are not captured by an unweighted Grünwald stencil.
Flag for the implementation pass.

---

## FIXES WORTH DOING NOW

### F1. Replace Remark 4.1.3 with the corrected $\kappa$.

Pick the convention (recommended: $\mathbb{D}^{1-\gamma}_{[0,T]}$ has
pure-Riesz symbol $|\xi|^{1-\gamma}$) and set
$\kappa_{1-\gamma} = 2\sin(\pi\gamma/2)/(c\Gamma(1-\gamma)) = c_\gamma^{-1}\cdot 2$
(or equivalently $\kappa = c_\gamma^{-1}$ if you scale $\mathbb{D}$
to absorb the 2). Once chosen, the finite-interval and half-line
$\kappa$'s align. Remove the "either convention is internally
consistent" sentence; it is incorrect under the current §3.2
definition.

### F2. Add the two-line sign derivation to §2.4.

m1 above. The reader currently cannot verify the sign of $(\star)$
without re-deriving from §2.3; one display line ("Euler–Lagrange:
$\int G u_v\,dv - \alpha_t + \lambda = 0$, rearranged to $(\star)$")
discharges the Changelog "deferred" item.

### F3. Soften Theorem 5.1's "boundary corrections absorbed" sentence.

m2 above. Replace with "Near-endpoint corrections take the same
$(t(T-t))^{(\gamma-1)/2}$ form as $\mathcal{B}_{1-\gamma}$, with an
$\eta$-dependent coefficient; complete bound deferred." Matches the
B.2 hand-wave flag and removes the unsupported absorption claim.

### F4. Cite a specific edition for the A.2 inversion formula.

m3 above. Best target: Samko–Kilbas–Marichev 1993 §13.2 Theorem 13.2
(airfoil) or §10.4 Theorem 10.7 (generalized Abel on bounded
interval). Restate A.2 with weight outside $d/ds$ and prefactor
$\sin(\pi\nu)/\pi^2$ (sign per SKM convention). Drop the
Chakrabarti–George (1994) primary citation here — that paper handles
a different kernel and is not the right reference for the symmetric
case.

---

## Summary

The Round 1 fixes for F1 (operator order), F2 (boundary exponent),
F3 (Mittag–Leffler prefactor), D2 (W–H reframing), D3
($\mathbb{E}_t[\alpha_T]$ removal), D4 (Forde recovery downgrade),
M1–M5 from Round 1, and the bibliography hygiene items have all
landed correctly. Spot-checks of Cor 4.2, Cor 5.3, §6.2, App C, and
the B.2 Mittag–Leffler resummation are clean.

The deferred items split as follows:

- **Discharged on inspection:** Sign reconciliation $(\star)$ vs
  Thm 4.1 (m1 / F2); D4 Forde honesty (m3); Cor 5.3 / matrix /
  Mittag–Leffler series re-check (m4 / m6 / m7).

- **Still open and material:** the $\mathbb{D}^{1-\gamma}_{[0,T]}$
  definition / Chakrabarti–George identification / $\kappa$
  normalization are entangled (M1–M3). These are the same underlying
  question — *which operator on $[0,T]$ is $\mathbb{D}^{1-\gamma}$,
  and what is its exact constant?* — and need to be resolved together
  via F1 + F4. Theorem 5.1's near-endpoint claim should be softened
  (F3). Once these four fixes land, the §4–§6 / Appendix A–C
  derivations are internally consistent.

- **Genuinely deferred:** time-consistency proof in A.1, Forde
  kernel-matching in A.3, $L^2$ tail bounds in B.5, finite-interval
  HLS constant in B.1, WSGD endpoint accuracy in App D. All
  appropriately flagged.

No new math errors were introduced by the convention rewrite. The
remaining issues are normalization-and-identification, not structural.
