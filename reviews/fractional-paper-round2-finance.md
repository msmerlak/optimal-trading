# Round-2 finance review — `fractional-derivative-optimal-execution.md`

Reviewer: finance/economic soundness pass, follow-up on Round 1.
Read-only (no edits applied). Scope per request: §5.4 AJNT framing,
§1 contribution clarity, §2.1 standing assumptions and propagation,
economic interpretation of $\mathcal{B}_{1-\gamma}$, end-to-end unit
checks. Round 1 items already addressed by Changelog (D1–D4, F1–F3,
M1–M5, m1–m4) are not re-flagged.

> **Tooling note.** AJNT 2024 (arXiv:2403.10273) not directly fetchable
> in this shell; assessment is against the summary in
> `outputs/unified-trading-execution.md` §2.5 and prior reading.

---

## Verdict

The Round 1 fatal/major items are substantively addressed. The §5.4
reframing is the right move and the contribution language in §1 is now
crisp. Remaining items are one structural inconsistency in §5.4 (the
well-posedness penalty is introduced and then sent to zero in the
factorization), one missing economic gloss on the boundary term, and
small propagation/wording polish around §2.1 assumptions vs §5.4 and
§6. Unit checks pass end-to-end with the corrected α convention.

---

## MAJOR

### M1. §5.4 derives well-posedness from $\gamma_{\rm risk}>0$ but factorizes at $\gamma_{\rm risk}\to 0$ — Prop 5.2 / Cor 5.3 are solving the ill-posed problem

The flow in §5.4 is:

1. State that $T=\infty$ with no terminal constraint is ill-posed (cost
   unbounded below).
2. Add running penalty $\tfrac{1}{2}\gamma_{\rm risk}\sigma^2 X_t^2$ to
   restore well-posedness; cite GP 2013.
3. Write the FOC $(\star_{\rm WH})$ with the penalty present.
4. Then drop the penalty term to factorize the kernel symbol alone, and
   in Remark 5.5(ii) treat the penalty as a "regularization of $\hat
   G^{-1}$ at $\xi=0$" recovered "in the zero-penalty limit."

The economic justification (step 2) and the mathematical object that
gets factorized (step 4) are inconsistent. Either:
- The penalty is the load-bearing well-posedness device, in which case
  Prop 5.2 / Cor 5.3 should be stated *with* the penalty's $\xi^{-2}$
  contribution to the symbol and the factorization should be of
  $\hat G(\xi) + \gamma_{\rm risk}\sigma^2 \xi^{-2}$ (which has
  different branch structure and a different — non-Riesz — exponent),
  or
- The penalty is cosmetic and the factorization is really for the
  symbol $\hat G$ alone, in which case the well-posedness story in the
  setup paragraph is misleading and the right framing is
  "leading-order kernel inversion; full GP-with-power-law treatment
  deferred" with an explicit caveat that Cor 5.3 is not yet the policy
  of a well-posed optimization problem.

As written §5.4 chooses neither. Remark 5.5(ii) papers over it but the
issue is exactly the M3 concern from Round 1 in different clothing:
the W–H factorization is for the *stationary kernel*, not for the
*stationary signal-tracking problem*. Cor 5.3 is therefore best
described as the explicit form of the AJNT resolvent's *symbol* under
the power-law kernel, not as the explicit optimal policy of the
GP-style problem stated at the top of §5.4.

**Fix.** Add one paragraph after $(\star_{\rm WH})$ stating:
"Proposition 5.2 factorizes the kernel symbol $\hat G(\xi)$ in
isolation; in the $\gamma_{\rm risk}>0$ problem the effective symbol
acquires a low-frequency $\gamma_{\rm risk}\sigma^2/\xi^2$ correction
and the factorization carries an additional Blaschke-type factor
encoding the holding-deviation mode. Cor 5.3 is the $\gamma_{\rm
risk}\downarrow 0$ leading-order form; the full GP-with-power-law
policy is left to future work." Then the AJNT framing is honest.

### M2. AJNT framing is *broadly* right but overstates the equivalence "Wiener–Hopf split = frequency-domain image of AJNT's resolvent calculus"

AJNT 2024's resolvent calculus is operator-theoretic on general matrix
Volterra kernels and does *not* in general admit a Fourier-symbol
factorization — the symbol approach requires translation invariance
plus stationarity, which only obtains in the specific specialization
of §5.4. The current §5.4 text ("the factorization is the
frequency-domain image of their resolvent calculus, and the one-sided
fractional derivatives that emerge are the explicit form of their
resolvent operators for this kernel") reads as if AJNT's resolvent is
always a Fourier multiplier under a different name. It isn't; it
becomes one only after specializing to scalar power-law kernel,
translation-invariant half-line, and stationary signal.

**Fix.** Replace "the frequency-domain image of their resolvent
calculus" with "the explicit form taken by their resolvent in the
specialization (i)–(iii); this specialization is what makes a Fourier
symbol approach available where the general AJNT setting requires
operator inversion." Same point should be propagated to the Abstract
("we present this as the power-law specialization of the AJNT
operator-resolvent framework") and to §9 — both currently elide the
"because the specialization is translation-invariant" qualification.

### M3. Standing assumptions (§2.1) vs §5.4 cost functional — explicit conflict not flagged

§2.1 now states the standing assumption "risk-neutral cost
functional," with the parenthetical "§5.4 carries a running
inventory-risk penalty." Strictly speaking, the GP-style penalty
$\tfrac{1}{2}\gamma_{\rm risk}\sigma^2 X_t^2$ *is* a (quadratic-form
approximation of an) Arrow–Pratt risk penalty and is incompatible with
"risk-neutral." The §2.1 wording deflects this with the parenthetical
but doesn't tell the reader what to do with it.

**Fix.** Rewrite the §2.1 sentence as: "Risk-neutral cost functional
in §§2–4 and §6; §5.4 augments the cost with a Gârleanu–Pedersen-type
running variance penalty $\tfrac{1}{2}\gamma_{\rm risk}\sigma^2 X_t^2$
as a well-posedness device for the half-line specialization, with
$\gamma_{\rm risk}$ a free parameter rather than a calibrated risk
aversion." That makes the regime change explicit instead of putting it
in a parenthetical.

---

## MINOR

### m1. Standing assumptions not fully propagated to §6 (multi-asset)

§2.1 carries the assumption "no short-sale or inventory-band
constraint beyond the terminal $X_T=0$." In §6 this is implicitly
generalized to vector $X_T=0$, but in a multi-asset cross-impact
setting a "no-short-sale" reading is essentially meaningless — most
cross-impact applications are long-short pairs trading or basket
execution where shorting individual legs is the entire point. §6.1
should add a one-line: "The §2.1 no-short assumption is understood
componentwise; for long-short execution the constraint is to be
dropped, and the policy in Theorem 6.1 remains valid since the FOC is
linear in $u$." Otherwise the assumption block reads as if the
multi-asset case is restricted to long-only baskets.

### m2. Economic interpretation of $\mathcal{B}_{1-\gamma}(t) = c_1(t(T-t))^{(\gamma-1)/2}$ is missing

With the corrected exponent $(\gamma-1)/2 \in (-1/2, 0)$, the boundary
term is the classical GSS U-shape: integrable at $t=0$ and $t=T$ but
divergent there, i.e. the trader trades *most aggressively at the
endpoints* and least aggressively at the midpoint. The paper states
this *mathematically* (App. A.2: "unique exponent in the null-space …
integrable at both endpoints") and notes that the Riesz derivative of
a constant vanishes in the interior. It does **not** give the economic
gloss that should accompany the formula:

- At $t \to 0^+$, no prior trading has impacted the market and the
  full liquidity is available; trading early is cheap because past
  impact $\int_0^{0^+} G(t-s)\,u_s\,ds = 0$.
- At $t \to T^-$, future impact-decay carries no cost penalty (there
  is no future trading whose impact would interact); trading late is
  cheap because no future trades will be penalized by the
  outgoing-impact tail.
- The midpoint is most expensive because trades there both inherit a
  populated past-impact tail and contribute to the future-impact tail
  seen by remaining trades.
- The exponent $(\gamma-1)/2$ encodes that the boundary effect is
  *stronger when the kernel is more singular* (larger $\gamma$ ⇒
  exponent closer to 0 ⇒ less divergent boundaries ⇒ flatter
  schedule; smaller $\gamma$ ⇒ more divergent boundaries ⇒ sharper
  U-shape). This is the trade-off that GSS make implicit and that the
  fractional-derivative form makes legible.

Worth adding as a 4–6 line "Economic interpretation" remark between
Theorem 4.1 and §4.3. Same gloss should appear in Cor 4.2 to ground
the U-shape recovery in market intuition rather than only in the
homogeneous-solution algebra.

### m3. Forward / instantaneous switch in §2.2 is fine but not load-bearing

§2.2 says "Section 5 will relax integrability … in which case $\alpha$
is interpreted as an *instantaneous* forecast rather than a cumulative
one." This is a switch of meaning, not a relaxation of integrability,
and it changes the dimensional reading of $\alpha$ from price
(cumulative) to price-per-time (instantaneous-drift). The current text
suggests they are continuous in the limit; they aren't. Either:
(i) keep both definitions but use distinct symbols ($\alpha_t$ vs
$\dot\alpha_t$, say), or (ii) state explicitly that §5.4 uses a
different convention with a one-line dimensional reconciliation.
Currently a careful reader will trip on this. (This is not a unit-
check failure within either section — see check below — only a
cross-section consistency item.)

### m4. Bullet 5/6 of §1.2 are not contributions, they are framings / deliverables

"Discussion of the fractional-PID analogy" and "Reference benchmark"
are positioning statements, not theorems. Mixing them into the
numbered contributions list dilutes the crispness of bullets 1–4. Move
them to §1.3 or §8.

---

## FIXES WORTH DOING NOW

### F1. One-line economic remark on $\mathcal{B}_{1-\gamma}$ in §4.2 or §4.4 (per m2)

Add to §4.4 a fourth bullet: "**Boundary term economics.** The
$(t(T-t))^{(\gamma-1)/2}$ U-shape reflects that early and late trades
incur the smallest impact-interaction cost — at $t=0$ no past impact
has accumulated, at $t=T$ no future trades will be penalized by the
outgoing impact tail — so the inventory is preferentially carried at
the endpoints. The exponent flattens as $\gamma \uparrow 1$ (more
singular kernel ⇒ memory dominates over boundaries) and sharpens as
$\gamma \downarrow 0$ (almost-flat kernel ⇒ boundaries dominate)."

### F2. Promote the §2.1 parenthetical to a regime-change statement (per M3)

Cheap and clarifies the rest of the paper.

### F3. Soften the "frequency-domain image" sentence in §5.4 intro and §9 (per M2)

Two sentences need editing; no math changes.

### F4. One-line cross-reference in §6.1 about no-shorts for cross-impact (per m1)

---

## Unit-check audit (focus area 5)

With the §2.2 cumulative convention $\alpha_t = \mathbb{E}_t[P_T-P_t]$
(units of price-per-share, i.e. $[\$/\mathrm{share}]$):

| Object | Units |
|---|---|
| $u_t$ | shares / time |
| $X_t,\ X_0$ | shares |
| $P_t,\ S_t,\ \alpha_t,\ \lambda$ | \$/share |
| $G(t)$ | \$/share² |
| $c$ in $G(t)=c\,t^{-\gamma}$ | \$·time$^\gamma$/share² |
| $\eta$ in $\eta u_t^2$ | \$·time/share² |
| $\gamma_{\rm risk}\sigma^2$ in $\tfrac{1}{2}\gamma_{\rm risk}\sigma^2 X^2$ | \$/(share²·time) |
| $c_\gamma$ in §5.4 | \$·time$^\gamma$/share² |
| $\kappa_{1-\gamma}=(c\Gamma(1-\gamma))^{-1}$ | share²/(\$·time$^\gamma$) |

Checks:

- **Cost functional §2.3.** $u_t (P_t-S_t) dt$: (shares/time)·(\$/share)·time = \$. ✓
- **Signal pickup.** $u_t \alpha_t dt$: (shares/time)·(\$/share)·time = \$. ✓
- **Lagrange term.** $\lambda(\int u\,dt - X_0)$: (\$/share)·shares = \$. ✓
- **FOC $(\star)$.** $\int G(|t-v|) u_v dv$: (\$/share²)·(shares/time)·time = \$/share. RHS $\alpha_t - \lambda$: \$/share. ✓
- **Theorem 4.1 RHS.** $\kappa_{1-\gamma}\cdot\mathbb{D}^{1-\gamma}[f]$: (share²/(\$·time$^\gamma$)) · (\$/share / time$^{1-\gamma}$) = shares/time. ✓
- **Boundary term.** $c_1(t(T-t))^{(\gamma-1)/2}$ in shares/time forces $c_1$ to carry units shares·time$^{-\gamma}$. Dimensionally consistent but $c_1$'s units depend on $\gamma$ — standard for power-law solutions, no issue.
- **Theorem 5.1 $R_{\gamma,\eta}$.** Both the $\delta$ term $(2\eta)^{-1}\delta(t-s)$ and the Mittag–Leffler term $c\Gamma(1-\gamma)(2\eta)^{-2}|t-s|^{-\gamma}E_{1-\gamma,1-\gamma}(\cdot)$ have units share²/(\$·time²). Multiplied by $\bar\alpha(t,s)\,ds$ (units \$·time/share) returns shares/time. ✓
- **Mittag–Leffler argument.** $c\Gamma(1-\gamma)/(2\eta)\cdot|t-s|^{1-\gamma}$: (\$·time$^\gamma$/share²)/(\$·time/share²) · time$^{1-\gamma}$ = dimensionless. ✓
- **Wiener–Hopf symbol §5.4.** $\hat G(\xi) = c_\gamma|\xi|^{\gamma-1}$: (\$·time$^\gamma$/share²)·time$^{1-\gamma}$ = \$·time/share². As a Fourier multiplier on densities, this is the right dimensional form (the Fourier transform of $G$ in \$/share² gains a factor of time). ✓
- **Cor 5.3 $\kappa_{1-\gamma}^\infty = c_\gamma^{-1}$.** share²/(\$·time$^\gamma$). Acting via $D^{(1-\gamma)/2}_+\Pi_+ D^{(1-\gamma)/2}_-$ (total operator order $1-\gamma$, time$^{-(1-\gamma)}$) on $\bar\alpha^\infty$ (\$/share) returns shares/time. ✓

**Verdict: end-to-end unit consistency holds.** The earlier (Round 1)
concern that $\alpha_t$ might be drift-rate vs cumulative is now moot
because §2.2 fixes the cumulative convention and the rest of the paper
honours it. The only residual hazard is the §5.4 sentence that
re-interprets $\alpha$ as "instantaneous" for the stationary case
(m3 above); within §5.4, however, the dimensional algebra still works
provided the reader treats stationary $\alpha$ as \$/share (level), not
\$/(share·time) (rate). A one-line note to that effect would close the
loop.

---

## Summary

- **AJNT framing (focus 1):** broadly accurate and is the right
  move, but oversells the "W–H = frequency-domain image of AJNT
  resolvent" equivalence (M2) and is internally inconsistent about
  whether the running risk penalty is load-bearing or cosmetic (M1).
  Both fixable in 2–3 sentences plus one honest caveat.
- **§1 contribution clarity (focus 2):** crisp enough. Bullets 1 and
  3 explicitly name AJN 2022 / AJNT 2024 specialization. §1.3
  highlights "explicit closed-form" as the delta. m4 is a clarity
  nit only.
- **Standing assumptions propagation (focus 3):** §2.1 is now
  present but the §5.4 risk-penalty exception is buried in a
  parenthetical (M3), and §6 doesn't address the multi-asset
  no-short subtlety (m1).
- **Economic interpretation of $\mathcal{B}_{1-\gamma}$ (focus 4):**
  not present; mathematically correct but missing the market-intuition
  gloss. Worth adding (m2 / F1).
- **Unit checks (focus 5):** honest end-to-end with the corrected α
  convention; no dimensional inconsistencies remain inside any
  individual section. Cross-section convention switch in §2.2 (m3) is
  the only residual hazard.
