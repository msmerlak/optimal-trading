# Round 3 Math Review — `fractional-derivative-optimal-execution.md` (v2)

**File:** `papers/fractional-derivative-optimal-execution.md` (v2, 897 lines)
**Migration note:** `papers/fractional-derivative-optimal-execution.v1-to-v2.md`
**Prior round:** `reviews/fractional-paper-round2-math.md`
**Date:** 2026-06-27
**Mode:** review-only; no edits applied.

## Top line

The v2 spine is mathematically the right reframing: Thm 4.1 on $\mathbb{R}$,
boundary corrections on $[0,T]$ and $[0,\infty)$, $\kappa_{1-\gamma}=
(2c\Gamma(1-\gamma)\sin(\pi\gamma/2))^{-1}$ uniform, half-line W–H with
$\eta\ge 0$ and Krein for $\eta>0$. The bulk-side Fourier-symbol
calculation (Thm 4.1 / App A.1) and the closed-form $\eta=0$
factorization (App A.3 Part 2) are clean and standard.

**One headline math problem (M1).** Proposition 5.3 / Corollary 5.4 are
overstated. The "$O((X_0+M)/T)$ on bulk regions" / "$u^*=u^{\rm bulk}+
O(1/T)$" headlines depend on a Step 2 bound in App A.2 Part 2
(`$\int_0^T u^{\rm bulk}\,dt = O(T^{1-1/p}M)$` with $p\to 1^+$ giving
$O(M)$ up to logs) that is not correct as written. The HLS-direction
argument is misapplied: the Riesz fractional *derivative* of positive
order has no $L^\infty\!\to L^p$ mapping with $T$-independent norm,
and any deterministic bound from $\|\bar\alpha\|_\infty\le M$ alone is
$O(MT)$, not $O(M)$. The genuinely-correct stochastic statement
(mean-zero stationary $\bar\alpha$ with $\int(1+|\xi|^{2(1-\gamma)})
S_\alpha<\infty$) gives $\int u^{\rm bulk}\,dt = O(\sqrt{T})$ in
probability, which propagates to a $T^{-1/2}$ interior decay rate, not
$T^{-1}$. The qualitative picture ($\mathcal{B}\to 0$ in interior) is
preserved in the stochastic reading; the rate is slower and the
deterministic gloss is wrong. This is exactly the same defect the
finance reviewer's M1 diagnoses from the cumulative side (boundary
carries the $\Theta(X_0)$ unwind, bulk does not), and the two reviews
should be read together.

Smaller items: orphan W–H integrability constants flagged (m1);
projection $\Pi_+$ admissibility for $\eta=0$ honestly hedged (m2);
Forde conjecture support stub absent (m3, intersects consistency M1).

---

## MAJOR

### M1. Prop 5.3 Step 2 is incorrect; Prop 5.3 / Cor 5.4 are overclaimed

**Where.** App A.2 Part 2 Step 2 (lines 640–646); body Prop 5.3
(lines 331–360); body Cor 5.4 (lines 362–366); abstract bullet
(line 21); §1.2 contribution 4 (line 50); §9.3 conclusion (line 539);
App A.2 Step 4 conclusion (line 669); App A.2 hand-waved note (iii)
(line 677).

**The bad step.** Step 2 asserts

> "the fractional derivative $\mathbb{D}^{1-\gamma}_{[0,T]}\bar\alpha$
> is in $L^p(0,T)$ for $p<2/(1-\gamma)$ with norm $\le C_p M$
> (Hardy–Littlewood–Sobolev / SKM 1993 §13.4); integrating … and
> applying Hölder, $|\int_0^T u^{\rm bulk}|\le \kappa T^{1-1/p}C_p M$,
> … For $p$ slightly above $1$, this is $O(M)$ up to logs."

Two issues compound:

1. **Wrong HLS direction.** HLS / SKM 1993 §13.4 bounds the
   fractional *integral* $I^{\sigma}: L^p\to L^q$ with $1/q=1/p-\sigma$
   (regularity-gaining). The bulk operator $\mathbb{D}^{1-\gamma}$
   here is a fractional *derivative* of positive order $1-\gamma$,
   whose Fourier multiplier $|\xi|^{1-\gamma}$ is unbounded at high
   frequency. There is no bound $\|\mathbb{D}^{1-\gamma}\bar\alpha
   \|_{L^p(0,T)}\le C_p\|\bar\alpha\|_{L^\infty}$ with constant
   independent of the regularity of $\bar\alpha$. The control of
   $\mathbb{D}^{1-\gamma}\bar\alpha$ that the paper actually has comes
   from the Thm 4.1 PSD assumption $\int(1+|\xi|^{2(1-\gamma)})
   S_\alpha\,d\xi<\infty$, which delivers $L^2$ stationarity (so a
   *variance* bound), not an $L^\infty$- or low-$p$ bound with the
   needed $T$-scaling.
2. **$p\to 1^+$ does not give $O(M)$.** Even if a bound of the form
   $\|\mathbb{D}^{1-\gamma}\bar\alpha\|_{L^p}\le C_p\|\bar\alpha\|_X$
   held, $T^{1-1/p}$ tending to $1$ as $p\downarrow 1$ does not save
   the bound, because $C_p$ blows up at the endpoint of the HLS range
   and (more importantly) only $\|\bar\alpha\|_{L^p(0,T)}\le M\,T^{1/p}$
   is available from $\|\bar\alpha\|_\infty\le M$, so any boundedness
   you do get is paid for with an additional $T^{1/p}$ factor that
   cancels the $T^{1-1/p}$, yielding $O(MT)$ — the trivial pointwise
   bound — not $O(M)$.

**What is actually true.**

- *Deterministic, only $\|\bar\alpha\|_\infty\le M$ used:* the best
  one can say without extra regularity is
  $|\int_0^T u^{\rm bulk}\,dt|\le \|u^{\rm bulk}\|_{L^\infty(0,T)}\cdot
  T = O(MT)$ — and even this requires $\mathbb{D}^{1-\gamma}\bar\alpha
  \in L^\infty(0,T)$, which generally fails for the Söhngen–Tricomi
  form on a bounded interval because of the $(s(T-s))^{-\nu}$
  endpoint weight.
- *Stochastic, $\bar\alpha$ mean-zero stationary with the §4.1 PSD
  bound:* $u^{\rm bulk}$ is itself stationary, mean-zero
  (the symbol $|\xi|^{1-\gamma}$ vanishes at $\xi=0$, killing DC), and
  finite-variance. With summable autocovariance, $\int_0^T u^{\rm
  bulk}\,dt$ has variance $\Theta(T)$, so
  $|\int_0^T u^{\rm bulk}\,dt|=O_{\mathbb P}(\sqrt{T})$.
- The $O(M)$-uniform-in-$T$ bound the proof needs is **neither**.

**Propagation to $c_1$ and $\mathcal{B}$.** With the corrected
stochastic bound (the more favourable of the two correct options),
Step 3 gives
$$|c_1| = \Theta\!\bigl((X_0 + \sqrt{T})/T^\gamma\bigr)$$
in probability, and Step 4 (using
$(s(1-s)T^2)^{(\gamma-1)/2}=T^{\gamma-1}(s(1-s))^{(\gamma-1)/2}$)
yields
$$\sup_{t\in[\epsilon T,(1-\epsilon)T]} |\mathcal{B}_{1-\gamma}(t)|
   = O_{\mathbb P}\!\bigl(X_0/T\bigr) + O_{\mathbb P}\!\bigl(T^{-1/2}\bigr),$$
i.e. the **inventory-unwind piece decays at $1/T$** (fast) but the
**signal-matching piece decays only at $1/\sqrt{T}$** (slow). With the
deterministic $L^\infty$ bound, the signal-matching piece does not
decay at all: $\mathcal{B}_{\rm interior}=O(X_0/T)+O(M)$.

**Match to the finance reviewer's M1.** The cumulative reading
$\int_0^T \mathcal{B} = X_0 - \int_0^T u^{\rm bulk}$ gives the same
diagnosis from the integrated side: the bulk does not (in
expectation) carry $X_0$, so $\mathcal{B}$ carries the whole $X_0$ in
its cumulative mass, concentrated in the U-shape endpoint windows.
That cumulative split is mathematically clean (no broken HLS step);
the pointwise interior bound at $1/T$ rate is the part that fails.

**Recommended fix (math).** Replace Prop 5.3 + Cor 5.4 by a version
that is honest about both the deterministic and stochastic regimes:

> *Prop 5.3 (revised).* Under the §4.1 PSD assumption with mean-zero
> stationary $\bar\alpha$, for fixed $\epsilon\in(0,1/2)$, $X_0\in
> \mathbb{R}$,
> $$\sup_{t\in[\epsilon T,(1-\epsilon)T]}
>   |\mathcal{B}_{1-\gamma}(t)| \;=\; O_{\mathbb P}\!\bigl(X_0/T\bigr)
>   \;+\; O_{\mathbb P}\!\bigl(T^{-1/2}\bigr) \quad\text{as }T\to\infty,$$
> with the $X_0/T$ term carrying the *deterministic inventory unwind*
> (cumulative mass $\Theta(X_0)$, concentrated in the U-shape
> endpoint windows of width $\sim\epsilon T$) and the $T^{-1/2}$ term
> carrying the *stochastic signal-tracking residual* (mean-zero
> Gaussian-CLT scale).

> *Cor 5.4 (revised).* $u^*_t - u^{\rm bulk}_t = O_{\mathbb P}(X_0/T)
> + O_{\mathbb P}(T^{-1/2})$ uniformly on $[\epsilon T,(1-\epsilon)T]$.
> In particular $u^*$ converges in probability to $u^{\rm bulk}$ in
> the bulk interior, **but the rate is $T^{-1/2}$, not $T^{-1}$**, and
> the convergence is in probability over the stationary law of
> $\bar\alpha$, not deterministically in $T$ alone.

Then propagate the corrected rate and the cumulative-split caveat
through the abstract, §1.2(4), §5.2.5, §9.3 conclusion. The
inventory-vs-signal split (finance M1) becomes the natural economic
gloss on the corrected rate decomposition.

**Severity.** Load-bearing. The current statement is *qualitatively*
defensible (the boundary correction is small on the interior at large
$T$) but the *quantitative* $1/T$ rate and the absolutely-stated
form ("bulk is the optimum") are not. This is exactly what the brief
called the most important verification target.

---

## MINOR

### m1. Krein integrability constants in App A.3 Part 1 are hedged correctly

The verification of $\int |\log M|/(1+\xi^2)\,d\xi<\infty$ for $\eta>0$
(lines 691–699) is split into a $|\xi|>1$ tail and a $\xi\to 0$ tail
and is sound at the qualitative level. The worker's `⚠️ TODO`
(line 734, item ii) that "Krein integrability constants … are not
made quantitative" is an honest deferral: existence of the
factorization is correctly attributed to Krein's theorem; the only
gap is an effective constant, which is not load-bearing for any body
statement. **OK as flagged.**

### m2. $\Pi_+$ admissibility for $\eta=0$ is honestly hedged

App A.3 hand-waved note (i) (line 734) correctly flags that for
$\eta=0$, $M_-^{-1}(\xi)\sim |\xi|^{(1-\gamma)/2}$ as $\xi\to 0$, so
$M_-^{-1}\widehat{\bar\alpha^\infty}\in L^2$ requires the forecast PSD
to vanish faster than $|\xi|^{\gamma-1}$ at zero. This is the right
admissibility condition for the $\eta\to 0$ Cor 5.7 limit and is
correctly stated as a condition rather than a theorem. **OK.**

### m3. Closed-form factorization (App A.3 Part 2) checks out

Branch verification on $\mathbb{R}\setminus\{0\}$ (lines 712–718):
for $\xi>0$, $-i\xi=|\xi|e^{-i\pi/2}$, $i\xi=|\xi|e^{i\pi/2}$, product
$=|\xi|^2$, $((-i\xi)(i\xi))^{(\gamma-1)/2}=|\xi|^{\gamma-1}$. For
$\xi<0$, $-i\xi=|\xi|e^{i\pi/2}$, $i\xi=|\xi|e^{-i\pi/2}$, same
product. Half-plane analyticity of $(\mp i\xi)^{(\gamma-1)/2}$ on
$\{\mathrm{Im}\,\xi\gtrless 0\}$ follows from the principal branch on
$\mathbb{C}\setminus(-\infty,0]$ as stated. **Clean.**

### m4. Bulk theorem (Thm 4.1, App A.1) and constant $\kappa_{1-\gamma}$

The Fourier symbol $\hat G(\xi) = 2c\Gamma(1-\gamma)\sin(\pi\gamma/2)
|\xi|^{\gamma-1} = c_\gamma|\xi|^{\gamma-1}$ (App A.1, lines 593–595)
matches GR 3.761.9 / Stein 1970 §V.1. PSD admissibility
$\int(1+|\xi|^{2(1-\gamma)})S_\alpha\,d\xi<\infty$ correctly gives
$|\xi|^{1-\gamma}\widehat{\bar\alpha}\in L^2$, hence $u^{\rm bulk}
\in L^2$ by Plancherel. Uniqueness from non-vanishing symbol a.e.
on $\mathbb{R}$. **Clean.** $\kappa_{1-\gamma}$ uniformity already
verified line-by-line by the consistency reviewer (their m12); I
spot-checked four occurrences (lines 21, 168, 196, 601, 612) — all
$c_\gamma^{-1}$. ✓

### m5. App A.2 Part 1 airfoil-prefactor reconciliation

The reconciliation
$\sin(\pi\nu)/\pi^2 = \cos(\pi\gamma/2)/\pi^2$ combining with $c$ and
$\Gamma(1-\gamma)$ via the Euler reflection identity (lines 624–627)
to recover $c_\gamma^{-1}$ is algebraically correct in shape but the
text leaves the explicit identity chain as a "combines via" gloss
rather than writing out the cancellation. With $\nu=(1-\gamma)/2$:
$\sin(\pi\nu)=\sin(\pi(1-\gamma)/2)=\cos(\pi\gamma/2)$; reflection
gives $\Gamma(1-\gamma)\Gamma(\gamma)=\pi/\sin(\pi\gamma)$ and
$\sin(\pi\gamma)=2\sin(\pi\gamma/2)\cos(\pi\gamma/2)$; assembling,
$\sin(\pi\nu)/(\pi\cdot c\cdot\Gamma(1-\gamma))$ contains a factor
$1/(2\sin(\pi\gamma/2))$ that matches $\kappa_{1-\gamma}/(2c)$
modulo the $1/\pi$ remaining from the airfoil-equation Hilbert
transform. The full chain is one line of algebra that would close the
loop; the `⚠️ TODO` at line 631 (3×3 system non-singularity) is
honest but a one-line worked reconciliation here would close a
cleaner gap.

### m6. App B.2 Neumann-series / Mittag–Leffler computation

The Laplace-inverse identification $(t^{-\gamma})^{*n}(t) =
\Gamma(1-\gamma)^n t^{n(1-\gamma)-1}/\Gamma(n(1-\gamma))$ uses the
half-line convolution (lines 753–759); the symmetric two-sided
$[0,T]$ convolution is replaced by a half-line iterate, with the
endpoint discrepancy correctly noted at line 766 as "exact on
$[\epsilon T,(1-\epsilon)T]$ up to $O(1/T)$ corrections" — by
appeal to Prop 5.3. **Caveat:** this appeal inherits whatever rate
Prop 5.3 actually proves. Under the M1-corrected rate $T^{-1/2}$, the
Thm 6.1 endpoint-correction claim should be restated as $O(T^{-1/2})$
on the bulk region (still vanishing, but slower). One-line fix once
M1 is resolved.

### m7. Cross-reference bugs (consistency reviewer's M1)

Three appendix pointers are mechanically broken: App A.4 (lines
454, 567) should be App B.1–B.2; App A.5 (line 325, Conj 5.2.2)
points at a non-existent stub. These are pure bookkeeping, not math
errors. Already covered in the consistency review's M1 / F1 / F2;
flagged here only for completeness.

### m8. App A.2 Step 4 cosmetic — "$(1+T\cdot T^0)$"

Line 666: the chain
$|c_2|\cdot |(1-2s)T/2|\cdot(s(1-s)T^2)^{(\gamma-1)/2}$ is folded
into "$(1+T\cdot T^0)$" which then becomes "$(1+O(1))$" — confusing
notation. Since $|c_2|=\Theta((X_0+M)/T^\gamma)$, the second
$\phi_2$ term contributes $\Theta((X_0+M)/T^\gamma)\cdot T\cdot
T^{\gamma-1}\cdot(s(1-s))^{(\gamma-1)/2} = \Theta((X_0+M))\cdot
(s(1-s))^{(\gamma-1)/2}$ — i.e. the $\phi_2$ contribution at interior
is $\Theta(X_0+M)$, an $\Theta(1)$-in-$T$ piece, *not* a subleading
$O(1)$ multiplier of the $\phi_1$ piece. This is actually a
**separate** defect in Step 4: the $\phi_2$ term contributes
$\Theta(X_0+M)$ at interior, not the $\Theta((X_0+M)/T)$ the proof
claims. If this is right, the bulk-region bound is dominated by the
$\phi_2$ piece at $\Theta(1)$, and the headline rate is wrong even
under the (incorrect) Step 2 input. Worth re-checking the $|c_2|$
scaling derivation in Step 3 (lines 657–658): the proof says
$|c_2|=\Theta((X_0+M)/T^\gamma)$ from a second linear equation but
the equation is not written out, and the algebra "second-mode
endpoint behavior … scales as $T\cdot T^{\gamma-1}=T^\gamma$" is
ambiguous — it could mean the $\phi_2$ endpoint scales as $T^\gamma$
(making $|c_2|=\Theta((X_0+M)/T^\gamma)$ from a constraint $c_2\cdot
T^\gamma = X_0+M$) but then the *interior* of $\phi_2$ also scales
the same way at the maximum $|1-2s|\sim 1$ — i.e. linearly in $T$
times the weight. This needs to be worked out properly; under either
reading the $\phi_2$ term is non-negligible and may dominate the
$\phi_1$ term in the interior.

### m9. Adaptedness in §4.2 — still hand-wavy on one point

§4.2 (line 213) asserts that for OU signal $\bar\alpha(t,s) =
e^{-\theta(s-t)}\alpha_t$ on $s>t$, but for $s<t$, $\bar\alpha(t,s)=
\alpha_s$ which is *random* in $\mathcal{F}_t$. The Riesz operator
mixes past and future via the half-sum form. The text says "for each
fixed $t$, the map $s\mapsto\bar\alpha(t,s)$ is $\mathcal{F}_t$-
measurable on the whole real line" — true. But the OU concrete
formula at line 213 is *only* the $s>t$ piece; the $s<t$ piece uses
the realized OU path, which is fine but worth one sentence saying so.
**Cosmetic.**

---

## FIXES WORTH DOING NOW

### F1. Rewrite Prop 5.3 / Cor 5.4 with the correct rate (M1, m8)

The single highest-value math fix. Two-rate version
($X_0/T$ inventory-unwind + $T^{-1/2}$ signal-tracking) in
probability under the §4.1 PSD assumption; clean up the cumulative
split per finance M1. Also re-derive the $|c_2|$ scaling in App A.2
Step 3 to settle whether $\phi_2$'s contribution is negligible at
interior (m8) or dominates — if it dominates, Step 4's $\Theta$-
chain needs further tightening.

### F2. One-line algebraic reconciliation in App A.2 Part 1 (m5)

Write out the airfoil-prefactor / Euler-reflection cancellation to
$c_\gamma^{-1}$ explicitly (3 lines, no new math). Closes one of the
`⚠️ TODO` items at line 631 without new content.

### F3. Repoint A.4/A.5 cross-refs (m7, consistency M1)

Two-line edit; covered in the consistency review's F1/F2.

### F4. Update App B.2 endpoint-correction rate after M1 is resolved (m6)

Whatever Prop 5.3's corrected rate is ($T^{-1/2}$ under my reading),
the Thm 6.1 "bulk region up to $O(1/T)$" claim needs to inherit it.
One-line edit downstream of F1.

### F5. Cosmetic OU adaptedness sentence in §4.2 (m9)

One sentence noting that the OU formula at line 213 is the $s>t$
forecast piece; for $s<t$ the realized OU path is used. Trivial.

---

## Summary

The v2 spine is mathematically the right reframing. App A.1 (bulk on
$\mathbb{R}$), App A.3 Part 2 (closed-form $\eta=0$ W–H), and App C
(matrix extension) are clean. App A.3 Part 1 (Krein for $\eta>0$) is
correctly hedged on quantitative constants.

The one real math problem is Prop 5.3 / Cor 5.4: Step 2's bulk
cumulative bound misapplies HLS (wrong direction; no constant
independent of $T$ from $L^\infty$ alone), and the $|c_2|$ scaling in
Step 3 / Step 4 (m8) may have a separate gap that lets the $\phi_2$
term dominate at interior. Under the most charitable correct reading
(stochastic, mean-zero stationary $\bar\alpha$ with the §4.1 PSD
bound), the right rate is $X_0/T + T^{-1/2}$, not $(X_0+M)/T$, and
the convergence is in probability over the stationary law of
$\bar\alpha$. The qualitative spine "bulk dominates in interior at
large $T$" survives; the quantitative $1/T$ headline and the
"asymptotic optimum" framing do not. This is the same defect the
finance reviewer's M1 hits from the cumulative side.

Everything else is minor (one-line algebra in App A.2 Part 1, m5;
broken cross-refs, m7; OU adaptedness gloss, m9) or honest deferrals
already flagged in the file's `⚠️ TODO` markers.
