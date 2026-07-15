# CRONE-connection review plan

## Artifact
- File: `papers/markowitz-of-cost-pnas.md` (local Markdown PNAS-format draft)
- Target claim (§1.3(iii), line 67):
  > "the explicit reduction of the signal-adaptive optimizer to a fractional derivative of the forecast curve is new, and it makes contact with the CRONE / fractional-PID control tradition (18, 19), to our knowledge not previously connected to execution."
- Cited refs:
  - [18] Oustaloup A (1991), *La Commande CRONE* (Hermès)
  - [19] Chen, Petráš, Xue (2009), "Fractional order control — A tutorial", *Proc. American Control Conf.* 1397–1411
- Central mathematical object in paper: $u^\star = \lambda^{-1}\kappa_{1-\gamma} (D_+^\beta \zeta)$ with $\zeta_s = (D_-^\beta \bar\alpha(s,\cdot))(s)$ and $\beta = (1-\gamma)/2$.

## Review question
Is the "makes contact with CRONE" claim substantial or superficial? Both use fractional derivatives, but structural role, motivation, derivation, and object being differentiated differ.

## Criteria
1. **What is CRONE.** Objective, design methodology, controller form, what is fractionally differentiated, in what norm/loss.
2. **What the paper does.** Objective, derivation route (Wiener–Hopf factorization → half-order factors), object being differentiated (adapted forecast curve), what problem it solves.
3. **Structural alignment.** For each of {plant/loss, controller form, fractional-order origin, tuning parameters, derivation}: is CRONE's version the same or different?
4. **Non-superficial candidates.** Are any of these shared: (a) exponent from a slowly-decaying plant, (b) two-sided decomposition, (c) causality-adapted realization, (d) closed-form optimality argument, (e) frequency-domain robustness/iso-damping motivation?
5. **Superficial candidates.** Both use $D^\alpha$; both have $\alpha \in (0,1)$; both invoke "fractional" as a keyword.
6. **Downside of a loose claim.** Could invite a hostile reviewer to say the paper is over-claiming a link that is only a shared operator.

## Verification checks
- What CRONE actually optimizes (open-loop transfer function shape, template design, robustness to gain variations). Source: web + Oustaloup textbook description.
- Standard fractional-PID form: $u(t) = K_p e + K_i I^\lambda e + K_d D^\mu e$ (Podlubny). Compare to our formula.
- Whether any CRONE literature derives its fractional exponent from a power-law impact response like $t^{-\gamma}$.
- Whether any prior work connects execution / market-impact optimal control to fractional-order control (search terms: "fractional PID execution", "CRONE trading", "fractional controller market impact").
- Whether Riemann–Liouville / Marchaud one-sided derivatives (used in paper) match what CRONE's controllers implement (Oustaloup approximation is usually a rational IIR filter approximating a fractional differentiator in a frequency band).

## Deliverables
- Evidence notes: `outputs/.drafts/crone-connection-review-evidence.md`
- Final review: `outputs/crone-connection-review.md`
