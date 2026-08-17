# Review plan: forecast-curve substitution argument

**Artifact:** `papers/fractional-derivative-optimal-execution.md` (local Markdown draft).
**Source type:** local Markdown.
**Section under review:** the argument that the deterministic FOC on $\mathbb{R}$
gives $u^* = c_\gamma^{-1}\mathbb{D}^{1-\gamma}\alpha$, and that under stochastic
information the answer becomes $u^*_t = c_\gamma^{-1}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$
with $\bar\alpha(t,s) = \mathbb{E}[\alpha_s | \mathcal{F}_t]$.

User concern: the substitution $\alpha_t \to \bar\alpha(t,\cdot)$ "from
deterministic to stochastic" feels hand-wavy. They want a careful audit
of whether the argument is actually justified or papered over.

## Review criteria
1. **Logical validity.** Is the deterministic → stochastic step a derivation
   (with explicit conditioning, projection, optionality) or a heuristic
   replacement?
2. **Adaptedness.** Is the resulting $u^*_t$ explicitly $\mathcal{F}_t$-adapted,
   and is this property derived or asserted?
3. **Measurability across the forecast curve.** The operator $\mathbb{D}^{1-\gamma}$
   acts on the whole real line (uses values of $\bar\alpha(t,s)$ for $s > t$).
   Is the use of "future" values made rigorous (i.e., it's the predicted
   value at time $t$, not actual future information)?
4. **First-order condition rigor.** Does the paper actually derive a stochastic
   FOC (e.g. via Pontryagin, BSDE, or projection onto adapted controls),
   or does it write the deterministic FOC and "take conditional expectations"
   without justification?
5. **Order of operations.** Is it legitimate to swap $\mathbb{E}[\cdot|\mathcal{F}_t]$
   with the non-local fractional operator $\mathbb{D}^{1-\gamma}$? This is the
   pivotal technical point. If yes, by what theorem (Fubini-Tonelli + boundedness;
   measurability of $\bar\alpha$; integrability of $S_\alpha$)?
6. **Comparison with literature.** Does the paper cite standard references
   for stochastic optimal-control problems with non-local cost functionals
   (e.g. propagator models like Gatheral, Alfonsi-Schied)? Do those papers
   handle the same substitution rigorously?
7. **Equivalence to a BSDE / projection theorem.** Could the substitution
   be re-derived as: optimal control = projection of the deterministic
   optimal control onto $\mathcal{F}_t$-adapted processes?

## Verification checks
- Read §2.2 (deterministic problem), §2.3 (cost functional and stochastic FOC),
  §4.1 (bulk theorem and proof), §4.2 (adaptedness section).
- Check whether Theorem 4.1's proof actually proves the stochastic version
  or only the deterministic FOC.
- Check whether the proof Fourier-transforms a conditioned FOC (i.e. takes
  $\mathbb{E}[\cdot|\mathcal{F}_t]$ first) or just writes $\bar\alpha$ in place
  of $\alpha$ in the deterministic answer.
- Check what statement of the FOC is used: $\mathbb{E}_t[\nabla J] = 0$
  pointwise in time vs. $\nabla \mathbb{E}_t[J] = 0$ vs. some saddle-point
  characterization.
- Identify whether the substitution is given a precise name (projection,
  certainty-equivalence with appropriate caveats, conditional Wiener-Hopf,
  etc.) or treated implicitly.
- Cross-check against the linear-quadratic certainty-equivalence theorem:
  the quadratic cost makes the optimal feedback law affine in the state,
  and for linear systems the certainty-equivalence principle applies — but
  the cost here is *non-local* in time, which breaks the standard LQG setup.
  Is this distinction made?

## Deliverables
- `outputs/.drafts/forecast-curve-substitution-review-evidence.md` (paraphrased
  passages, line numbers, technical observations).
- `outputs/forecast-curve-substitution-review.md` (final review).
