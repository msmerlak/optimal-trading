# Reformulating in μ (dropping α), with small-λ regularization

## 1. The objective needs only μ

α enters the paper only through integration by parts. The gain of holding position
`x` against a price with expected return (drift) `μ` is

    E ∫ x_t μ_t dt   =   E ∫ u_t α_t dt      (u = ẋ,  α_t = E_t ∫_t^∞ μ_s ds)

so "position × return" and "rate × appreciation" are the same objective. Working
with the left form drops α entirely:

    maximize   E ∫ [ x_t μ_t − ½ ⟨x, N x⟩ ] dt ,     n̂(ω) = η ω² + γ ĝ(ω) ω² + λ

with `μ` a **stationary predictor** (e.g. OU of speed θ). No `α = ∫^∞ μ`, no
divergent object.

## 2. General policy is already in μ

Theorem 2 is stated in μ:

    x★ = N₊⁻¹ P₊ N₋⁻¹ μ ,      x̂★(ω) = μ̂(ω) / (Φ(θ) n̂₊(ω))   (OU).

The whole factor→predict→combine machinery runs on μ. α, the forecast curve ᾱ,
and the rate-referred operator Q are never needed.

## 3. Pure power-law policy in μ

n̂ = γc_β|ω|^{1+β} + λ,  n̂₊ = (γc_β)^{1/2}(−iω)^{(1+β)/2} at λ=0.

- **Position** = causal fractional INTEGRAL of the return, order (1+β)/2:

      x̂★ ∝ (−iω)^{−(1+β)/2} μ̂ ,      x★ ∝ I₊^{(1+β)/2} μ.

- **Rate** = causal fractional DERIVATIVE of the return, order ν=(1−β)/2:

      û★ = (−iω) x̂★ ∝ (−iω)^{ν} μ̂ ,   u★ ∝ D₊^{ν} μ .

  (Equivalently u★ = (1/γc_β) D₊^ν P₊ I₋^{(1+β)/2} μ for a general signal.)

Orders: position 1−ν = (1+β)/2, rate ν = (1−β)/2; they differ by 1 (position = ∫ rate).

Numerically (γ=1, β=0.5, λ=0.1): position filter slope −0.748 ≈ −(1+β)/2 above
ω_c, flat below; rate filter slope +0.252 ≈ ν. Confirmed.

## 4. Small λ regularizes the non-stationarity — and everything stays in μ

At λ=0 the position filter (−iω)^{−(1+β)/2} amplifies low frequencies as
|ω|^{−(1+β)}: the position is non-stationary (a fractional random walk). A small
risk term λ>0 puts a floor n̂→λ at ω=0, so

    |x̂★/μ̂| ~ 1/√λ  (flat, Markowitz)   for ω < ω_c = (λ/γc_β)^{1/(1+β)},
             ~ |ω|^{−(1+β)/2}            for ω > ω_c.

The position is **a fractional integral of the return above ω_c, capped at the
Markowitz level 1/λ below it**. As λ→0, ω_c→0 and the scale-free frac-integral is
recovered on every finite band. The same λ makes the anticipative value
`v_ant = (1/4π)∫ S_μ/n̂` finite, so the value and causality-gap analysis also stay
in μ — no need to re-refer to the rate at λ=0.

**Net:** the entire paper (including §3) can be written in (μ, x) with a small λ,
dropping α, ᾱ, Q, and the rate-variable detour. §3's headline becomes: *rate =
fractional derivative of the return; position = fractional integral of the return,
Markowitz-capped; λ→0 is the scale-free limit.*

## 5. Caveat: small λ and "constant signal worthless" disagree at DC

These two regularizations resolve the ω=0 component differently:

- **Exactly λ=0 (rate / frac-diff), or discounting the predictor:** D₊^ν of a
  constant is 0 → a constant return is never traded → **value 0**.
- **Small λ>0 (this note):** the λ floor gives the DC a Markowitz channel
  x=μ/λ → a constant return is traded → **value 1/2λ**, which **→∞ as λ→0**.

So the limits do not commute: `v(constant)|_{λ=0} = 0`, but `lim_{λ→0} v(constant) = ∞`.
Physically, on the whole line holding a position against a constant signal needs it
to have been built at t=−∞ at infinite cumulative impact cost, which the λ=0
optimum declines (u=0); any λ>0 instead trades the DC myopically.

Choice:
- Want the clean stationary (μ, x) formulation and don't care about the DC atom
  → **small λ** (constant return = Markowitz, value 1/2λ).
- Want "a constant predictor is worthless" → **λ=0 rate form** or **discount the
  predictor** (α^ρ = E_t∫ e^{−ρ(s−t)}μ; value ∝ θ^{1−β}/(ρ+θ)², →0 at θ→0,
  peak θ*=ρ(1−β)/(1+β)).
- The two are different models; they can't both hold with a single small λ.
