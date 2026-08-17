# Round-3 finance review — `fractional-derivative-optimal-execution.md` (v2)

Reviewer: finance / economic-soundness pass on the v2 bulk/boundary
rewrite. Round-1 and Round-2 items are not re-flagged unless v2
reopens them. Scope per request: focus areas 1–8 below.

> **Tooling note.** AJNT 2024 (arXiv:2403.10273) still not directly
> fetchable in this shell; positioning assessed against
> `outputs/unified-trading-execution.md` §2.5 and prior reading.

---

## Verdict

The v2 spine is the right reframing and substantively closes every
Round-2 finance item (M1–M3, m1–m4, F1–F4). What v2 introduces are
new framing risks of its own. The strongest of these — and the
single most important fix — is that **Corollary 5.4's
"$u^* = u^{\rm bulk} + O(1/T)$" elevates a pointwise interior bound
into a global "bulk is the optimum" gloss that misrepresents the
cumulative-trade decomposition**: on $[0,T]$ the bulk contributes the
*signal-tracking* component of the schedule, but essentially the
entire *inventory unwind* is carried by $\mathcal{B}$ (cumulative
$O(X_0)$, not $O(1/T)$). That economic split is the *correct*
content of v2's central technical result and the paper does not
state it. Other items are smaller (crossover-scale numerics,
diagonalizing-basis identity, App E diagnostic completeness).

---

## MAJOR

### M1. Cor 5.4 framing conflates pointwise rate with cumulative trade

Prop 5.3 / Cor 5.4 give a **pointwise interior** bound:

$$ \sup_{t\in[\epsilon T,(1-\epsilon)T]} |u^*_t - u^{\rm bulk}_t| = O((X_0+M)/T). $$

Used inside §1.2 bullet 4, §5.2.5, §9.3 conclusion, the paper escalates
this into "bulk is the leading-order optimum" and "bulk solution is
the asymptotic optimum." Economically this is misleading. Integrate
both terms:

- $\int_0^T u^{\rm bulk}_t\,dt$ is **sublinear in $T$** (Step 2 of the
  Prop 5.3 proof gives $O(T^{1-1/p}M)$, $O(M)$ up to logs for
  stationary $\alpha$, even $O(1)$ in mean for OU). The bulk does
  *not* unwind $X_0$.
- $\int_0^T \mathcal{B}_{1-\gamma}(t)\,dt = X_0 - \int_0^T u^{\rm
  bulk}_t\,dt = X_0 + o_T(1)$. The boundary correction carries
  **essentially all of the inventory unwind**.

So the economic decomposition the paper is actually proving is

> bulk = signal-tracking component; boundary = inventory-unwind component,

which is a sharper and more honest statement than "bulk dominates the
optimum, boundary is a $1/T$ perturbation." Pointwise the boundary
*is* small on the interior, but it is small while doing the heavy
lifting of inventory, because the U-shape concentrates the unwind
into endpoint windows of length $\sim \epsilon T$ where the boundary
rate is *not* $O(1/T)$ — it diverges as $(t(T-t))^{(\gamma-1)/2}$,
exactly as the proof's "non-uniformity" notes record.

This is also why the "execution horizons of minutes to hours" stress
test of focus area 1 is partly missing. For $T=1\text{h}$, $\gamma=1/2$,
$\epsilon=0.05$: $(s(1-s))^{(\gamma-1)/2} \le (0.0475)^{-1/4}\approx
2.14$, so the interior constant is benign. But the trader who reads
"$u^* \approx u^{\rm bulk}$" and ignores $\mathcal{B}$ will not close
the position — they will undershoot $X_0$ by exactly the amount the
boundary carries. The $O(1/T)$ pointwise bound is true; the
"asymptotic optimum" gloss in §1, §5, §9.3 is not.

**Fix (concrete).** Add one paragraph immediately after Cor 5.4 with
the cumulative split:

> *Cumulative interpretation.* Although $u^{\rm bulk}$ dominates
> $\mathcal{B}_{1-\gamma}$ pointwise on $[\epsilon T,(1-\epsilon)T]$,
> the cumulative trade splits along an orthogonal axis: $\int_0^T
> u^{\rm bulk}\,dt$ is sublinear in $T$ and tracks signal capture,
> while $\int_0^T \mathcal{B}_{1-\gamma}\,dt = X_0 + o_T(1)$ carries
> the entire inventory unwind, concentrated into the endpoint
> windows where the U-shape diverges. The bulk is the *signal-tracking
> kernel* of the optimum; the boundary is the *inventory-unwinding
> kernel*. Cor 5.4 says these two roles are pointwise separable on
> the interior, not that either role can be dropped.

Then rephrase the abstract / §1 / §9.3 "$u^* = u^{\rm bulk} + O(1/T)$"
sentences as "*on the interior, the rate is dominated by the bulk
fractional-derivative component, with the inventory unwind absorbed
into a $\Theta(X_0)$ boundary mass concentrated near $t\in\{0,T\}$.*"

### M2. Crossover scale $\xi_*(\eta)$ is given no empirical scale

Focus area 4: the slow/fast split at $\xi_*(\eta) = (c_\gamma/\eta)^{1/(1-\gamma)}$
is the strongest practical content of §5.3, but the paper never
plugs in numbers. Back-of-envelope:

- For equities, $\gamma\approx 0.5$ is the empirical fit
  (Bouchaud–Gefen–Potters–Wyart 2004; Bouchaud 2010).
- The unit reconciliation in Round-2 §"Unit-check audit" gives $c_\gamma$
  in \$·time$^\gamma$/share², $\eta$ in \$·time/share².
- Typical equity orders: $c$ such that a $1\%$-ADV trade moves price
  $\sim 1$ bp at $t\sim 1$min → $c\sim 10^{-4}$\$·s$^{1/2}$/share²
  (order-of-magnitude only). Spread-cost $\eta\sim$ half-spread / typical
  rate, $\sim 10^{-2}$\$·s/share². Then $c_\gamma/\eta \sim
  10^{-2}\,\text{s}^{-1/2}$, and $\xi_*(\eta)\sim 10^{-4}\,\text{s}^{-1}$,
  i.e. *time scale $1/\xi_*\sim 10^4\,\text{s}\sim 3\,\text{h}$.*

If that calibration is even within an order of magnitude, then for
typical execution horizons (minutes to a few hours) and typical signal
half-lives (seconds to minutes), **most of the alpha spectrum lies in
the myopic regime $|\xi|\gg\xi_*$**, where the optimal policy is direct
signal-following $u\approx\bar\alpha/\eta$ and the fractional-derivative
content is confined to the slow tail of $\bar\alpha$. This is a strong
empirical statement and a non-trivial caveat on the headline "fractional
derivative is the optimal policy" framing.

Conversely, for an institutional VWAP-style schedule on a multi-day
horizon ($T\sim 10^5$s) with slowly mean-reverting alphas (half-lives
of hours), the propagator regime $|\xi|\ll\xi_*$ is where the action
is and the fractional rule is the leading-order optimum.

The crossover scale therefore *separates the use cases* of the paper:
intraday execution lives mostly in the myopic regime, multi-day
position trading in the long-memory regime. This belongs in §5.3.4
and again briefly in §9.

**Fix.** Add a 5–8 line "Empirical scale" paragraph in §5.3.4 with one
calibrated order-of-magnitude estimate, ideally referencing the
empirically defensible Bouchaud-style $c$ and the AJNT 2024 calibration
range for $\eta$. Add one sentence to §9.1 step 4 ("Crossover-scale
check") tying $\xi_*$ to a target alpha half-life.

### M3. Eigenbasis decomposition in §7 is the impact basis, not the signal basis

Theorem 7.1 diagonalizes the *cross-impact matrix* $\mathbf{C}$ and
projects the signal into that eigenbasis: $\tilde\alpha = Q^\top\alpha$
where $Q$ diagonalizes $\mathbf{C}$. The text in §7.2 and §1.2 bullet 7
says "the policy decouples into $d$ scalar bulk problems on the
principal-component signals $Q^\top\bar{\boldsymbol\alpha}$."
Practitioners read "principal-component signals" as PCA-of-signal.
Those are different rotations in general.

Economically the impact-eigenbasis modes are *impact-orthogonal
portfolios* (basket weightings whose price impacts decouple) — for
symmetric cross-impact in equities, typically a market-beta basket as
the top eigenmode, then sector/style baskets. The trader's signal
generally has structure that is *not* aligned with this basis: a
signal concentrated in the smallest impact-eigenmode is traded with a
large $1/\lambda_i$ amplification (cheap to trade) while a signal
concentrated in the top eigenmode (large $\lambda_i$) is heavily
fractionally damped. This is the practical content of cross-impact
diagonalization and is currently not explained.

**Fix.** Add 3–5 lines to §7.2 after Theorem 7.1:

> *Economic content.* The diagonalizing rotation $Q$ is determined
> by the impact matrix $\mathbf{C}$, not by the signal. The modes
> $Q^\top \bar{\boldsymbol\alpha}$ are projections of the signal onto
> impact-orthogonal portfolios; trading these portfolios independently
> decouples market impact across assets. Signal components aligned
> with high-impact modes (large $\lambda_i$) are aggressively damped
> by the $1/\lambda_i$ factor in the policy; components aligned with
> low-impact modes are traded near the scalar bulk rate. The
> fractional-derivative order $1-\gamma$ is the same for every mode;
> only the gain $1/\lambda_i$ differs.

Also: replace "principal-component signals" with "impact-eigenmode
signals" or "impact-orthogonal portfolio signals" in §1.2 and §7 to
avoid the PCA collision.

---

## MINOR

### m1. "Average cost per unit time" in §5.3.1 needs one more sentence on well-posedness without inventory penalty

§5.3.1 correctly diagnoses the unbounded-cumulative-cost issue and
switches to average-cost-per-unit-time. But for stationary mean-zero
$\alpha$ with no inventory penalty ($\gamma_{\rm risk}=0$), the
position $X_t = X_0 - \int_0^t u_s\,ds$ can drift unboundedly under
the bulk policy (since $u^{\rm bulk}$ is stationary, $X_t$ is a
random walk-like integral of a stationary process). Whether
"average cost per unit time" is the right objective without
*some* penalty on $|X_t|$ is a subtle finance question
(`outputs/unified-trading-execution.md` §3.1 calls out exactly this
in the GP framework). The paper currently asserts ACU is enough and
moves on.

The technical fix is that the propagator cost $u\,(G*u)$ is
*positive-definite-in-$u$* even when $X$ drifts, so the ACU objective
*is* finite under PSD assumptions on $\alpha$. But that's a
mathematical fact, not an economic one — economically, a strategy
that lets $|X_t|$ drift to $10^9$ shares before being closed is not
implementable. AJNT 2024 retains a non-zero $\gamma_{\rm risk}$ in
their finite-horizon problem precisely to keep $X_t$ bounded; v2's
half-line claim of well-posedness without it is sharper.

**Fix.** Add one sentence to §5.3.1 acknowledging that the bulk
policy on a half-line gives bounded *trading rate* but not bounded
*holdings* — for finance applications a soft holding-band or a small
$\gamma_{\rm risk}$ would be added in practice (cf. GP 2013, §6.4
pointer) — and that the η→0 bulk limit is the rate-side leading-order
content, not a complete portfolio-choice prescription. This keeps
the focus area 3 framing honest: §5.3 is propagator execution with
spread cost, the GP/portfolio-choice extension lives in §6.4.

### m2. §5.3.4 AJNT caveat is correctly placed but should also appear in §1 / abstract

Round-2 M2 is well addressed in §5.3.4 ("specializations (i)–(iv)"
list) and in §6.3 ("Our explicit contribution relative to AJN/AJNT"
bulleted). The Abstract still reads as if the contribution stands
on its own — the AJNT specialization framing only enters at §1.3
and the migration note. For a referee opening at the abstract, the
"explicit closed-form specialization of AJNT 2024 under translation
invariance" is now the cleanest one-line positioning and deserves a
half-sentence in the abstract.

**Fix.** Append to the abstract: "Under the bulk/boundary spine, the
paper is the explicit closed-form specialization of the AJN
(2022) / AJNT (2024) operator-resolvent framework to scalar power-law
kernels, stationary signals, and translation-invariant domains; the
specialization is what makes a Fourier-symbol approach available where
the general framework requires operator inversion."

### m3. U-shape gloss (§5.2.3) — direction of "sharper/flatter" is correct but interpretation can be tighter

§5.2.3 reads well. The "cheap-trading window" framing — no past
impact at $t=0$, no future trades penalized at $t=T$ — is the right
gloss and resolves Round-2 m2/F1. One small nit: the closing
sentence has the dependence on $\gamma$ correct (exponent
$(\gamma-1)/2$, sharper for smaller $\gamma$, flatter for larger
$\gamma$), but reverses the intuition relative to "more singular ⇒
flatter." Worth one more sentence linking the algebraic exponent to
the economic mechanism:

> *Mechanism.* A more singular kernel (larger $\gamma$, kernel diverges
> faster at $t=0$) makes adjacent-time trades expensive to follow
> closely, dominating the boundary effect; a less singular kernel
> (smaller $\gamma$, kernel closer to constant) makes adjacent-time
> trades cheap and the entire schedule is then shaped by the boundary
> windows. This is *why* the U-shape sharpens as $\gamma\downarrow 0$.

Not strictly required; the current §5.2.3 already passes the
finance bar.

### m4. App E item 4 ("Plot $u^* - u^{\rm bulk}$") should test the *full* Cor 5.4 statement, not just the interior bound

Per focus area 7: App E item 4 currently asks for $O(1/T)$ scaling
of $|u^* - u^{\rm bulk}|$ on the bulk region. The non-uniformity is
the more interesting half of Cor 5.4: near the endpoints
$\mathcal{B}_{1-\gamma}$ diverges as $(t(T-t))^{(\gamma-1)/2}$, and
the integrated mass near the endpoint windows is $\Theta(X_0)$ (per
M1 above). A complete empirical protocol should:

(i) verify $O(1/T)$ scaling at fixed interior point (current item 4),
(ii) verify $\Theta(X_0)$ for $\int_0^{\epsilon T}\mathcal{B}\,dt +
\int_{(1-\epsilon)T}^T \mathcal{B}\,dt$ — the endpoint-mass
diagnostic that confirms the bulk-vs-boundary cumulative split is
running as M1 describes,
(iii) verify the divergence exponent $(\gamma-1)/2$ near each
endpoint, which is the sharpest test of the Söhngen mode shape and a
natural calibration sanity check on the estimated $\gamma$.

**Fix.** Replace App E item 4 with a 3-part diagnostic (interior
$1/T$ scaling, endpoint mass $\Theta(X_0)$, endpoint exponent
$(\gamma-1)/2$).

### m5. §6.4 GP pointer is correctly framed but pointers in §1.3 still group GP under "stationary/portfolio-choice lines" with no caveat that the *kernel* must change

§1.3 says: "Under our spine these are bulk problems with different
kernels (exponential rather than power-law) and different
regularizers (running inventory cost rather than temporary impact);
the bulk inversion is no longer a fractional derivative but the spine
— bulk first, boundary second — remains the same." Correct. But the
"GP-with-power-law" hybrid — power-law kernel + running risk penalty
— is the natural cross-product the v2 reader will want to see
discussed once. §6.4 does this (one paragraph, Blaschke factor
caveat). One cross-reference from §1.3 to §6.4 would close the
loop:

> *"…the spine — bulk first, boundary second — remains the same; the
> GP-style running-risk regularizer with power-law impact is a
> distinct symbol shift (Blaschke-type factor, no closed-form $\xi$
> power); see §6.4."*

### m6. §2.2 dual semantics is now explicit, but cross-domain unit reconciliation still implicit

§2.2 cleanly separates the bounded-interval ($\alpha_t = \mathbb{E}_t[P_T-P_t]$,
units \$/share, cumulative-to-terminal) and stationary
($\alpha_t$ = level of a forecastable innovation, units \$/share but
*level*, not cumulative) interpretations. Both have the same units —
correct. But a careful reader will still ask: how does the SAME
operator $\mathbb{D}^{1-\gamma}$ apply to a quantity that has two
distinct economic meanings? The answer is that the bulk operator
acts on $\bar\alpha(t,\cdot)$ as a function of $s$, and that function
has the same *type* in both cases (a forecastable price level over
time). Worth one sentence after the §2.2 dual-interpretation block
clarifying that the *operator's input* is the forecast curve, not
the integrated alpha, so both interpretations feed the bulk
identically. This was Round-2 m3 and v2 mostly addresses it; the
gap is just one connective sentence.

---

## FIXES WORTH DOING NOW

### F1. Cumulative-split paragraph after Cor 5.4 (per M1)

Highest-value fix. ~6 lines. Reframes the headline result honestly
and pre-empts the natural reader confusion "if bulk is the answer,
how does it close $X_0$?".

### F2. Empirical-scale paragraph in §5.3.4 with one order-of-magnitude $\xi_*$ calculation (per M2)

~8 lines. Turns the crossover from a symbol fact into a regime map
for the use-case taxonomy (intraday → myopic; multi-day → fractional).

### F3. Impact-eigenbasis gloss in §7.2 + rename "principal-component" → "impact-eigenmode" (per M3)

~5 lines + one term change. Prevents the PCA collision.

### F4. AJNT-specialization half-sentence in the abstract (per m2)

One half-sentence. Makes the v2 contribution-vs-AJNT story
discoverable on first read.

### F5. App E item 4 → 3-part diagnostic (interior $1/T$, endpoint mass, endpoint exponent) (per m4)

~6 lines. Makes Cor 5.4 fully empirically testable rather than
testable only on the interior.

---

## Round-2 follow-through audit

| Round-2 item | v2 status |
|---|---|
| M1 (γ_risk/η inconsistency) | **Resolved.** D6 = A′; §5.3.1 uses $\eta\ge 0$; GP pointer split to §6.4 with Blaschke-factor caveat. |
| M2 (AJNT "frequency-domain image" overstatement) | **Resolved.** §5.3.4 lists specializations (i)–(iv) explicitly; §6.3 frames as "explicit form of resolvent under specialization." Minor: not yet in abstract (m2 above). |
| M3 (§2.1 risk-neutral vs §5.4 GP penalty) | **Resolved.** §2.5 explicitly excludes GP penalty; cost is risk-neutral throughout; §5.3 uses $\eta$ only. |
| m1 (no-shorts in §6 / now §7) | **Resolved.** §7.1 adds componentwise / long-short clarification. |
| m2 / F1 (U-shape economic gloss) | **Resolved.** §5.2.3 now reads cleanly. Minor tightening (m3 above). |
| m3 (cumulative vs instantaneous α) | **Mostly resolved.** §2.2 makes the two interpretations explicit; one connective sentence still owed (m6 above). |
| m4 (bullets 5/6 as contributions) | **Resolved.** §1.2 contributions list is now 1–7, all theorems / results. |
| F1–F4 | **All applied** or superseded by the v2 rewrite. |

---

## Summary

The v2 spine is a real upgrade and Round-2 finance is substantively
closed. The new framing risks are:

1. **Cor 5.4 oversells "$u^* = u^{\rm bulk} + O(1/T)$"** (M1). The
   correct economic story — *bulk = signal-tracking kernel, boundary
   = inventory-unwind kernel, pointwise-separable on interior but
   cumulatively complementary* — should be added explicitly after
   Cor 5.4 and propagated to the abstract / §1 / §9.3 phrasings.
2. **Crossover scale $\xi_*(\eta)$ is symbolic-only** (M2). A single
   calibrated number would convert §5.3.4 from a math observation
   into a regime map (intraday vs multi-day) and clarify when the
   fractional-derivative story is the leading-order finance story.
3. **Multi-asset eigenbasis = impact eigenbasis, not signal PCA**
   (M3). One paragraph and a term change.

None of M1–M3 require math changes; all are framing or single-paragraph
additions. Unit consistency, AJNT specialization claim, η→0 limit
recovery, U-shape gloss, and standing-assumption propagation are all
clean in v2.
