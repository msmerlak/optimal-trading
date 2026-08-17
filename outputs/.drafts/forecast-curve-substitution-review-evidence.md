# Evidence notes: forecast-curve substitution

## Locations in the paper

- §2.2, lines 95–99: definition of forecast curve $\bar\alpha(t,s) = \alpha_s$ for $s\le t$,
  $= \mathbb{E}_t[\alpha_s]$ for $s>t$. Final paragraph asserts that "using it (rather
  than the realized path $\alpha_\cdot$) keeps the policy $u^*_t$ $\mathcal{F}_t$-adapted."
- §2.3, lines 100–134: cost functional, deterministic FOCs $(\star)$, $(\star_{\rm WH})$,
  $(\star_{\rm bulk})$, then a paragraph "Stochastic FOC and emergence of the
  forecast curve" (lines 125–134) introducing the conditioned FOCs $(\star^{\mathcal{F}})$,
  $(\star_{\rm WH}^{\mathcal{F}})$, $(\star_{\rm bulk}^{\mathcal{F}})$ and the key
  substitution claim.
- §4.1 Theorem 4.1 and proof, lines 204–220.
- §4.2, lines 222–230: "Adaptedness and the forecast curve."

## Reconstructed argument as stated

1. (§2.3) The pathwise deterministic FOC on $\mathbb{R}$ reads
   $\int_\mathbb{R} G(|t-v|) u^*_v\,dv = \alpha_t - \lambda$, parametrized by $t$.
2. (§2.3) For adapted controls, "the Euler–Lagrange condition must be projected
   onto $\mathcal{F}_t$." This gives the conditioned FOC $(\star_{\rm bulk}^{\mathcal{F}})$:
   $\int_\mathbb{R} G(|t-v|)\,\mathbb{E}_t[u^*_v]\,dv = \alpha_t - \lambda$.
3. (§2.3, final sentence of the "Stochastic FOC" paragraph) **"Inverting the kernel
   symbol on $(\star_{\rm bulk}^{\mathcal{F}})$ produces a solution in which $\alpha_s$
   is replaced for $s>t$ by its $\mathcal{F}_t$-conditional expectation, i.e. by the
   forecast curve $\bar\alpha(t,s)$."** This is the load-bearing sentence.
4. (Theorem 4.1 proof) "Take the Fourier transform in $s$ of the
   $\mathcal{F}_t$-conditioned bulk FOC $(\star_{\rm bulk}^{\mathcal{F}})$ of §2.3,
   in which $\mathbb{E}_t[u^*_v]$ on the LHS is determined by $\bar\alpha(t,\cdot)$
   on the RHS:  $\widehat{G\ast u^{\rm bulk}}(\xi) = \widehat{(\bar\alpha - \lambda)}(\xi).$"
5. The proof then inverts the symbol: $\hat u^{\rm bulk}(\xi) = c_\gamma^{-1}|\xi|^{1-\gamma}\widehat{\bar\alpha}(\xi)$,
   identifying $u^{\rm bulk}_t = c_\gamma^{-1}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$.

## Where the argument is logically thin

### Issue A: The RHS substitution is not stated as a derivation.

In step 3 above, the FOC $(\star_{\rm bulk}^{\mathcal{F}})$ as written has only $\alpha_t$
(a single $\mathcal{F}_t$-measurable random variable) on the RHS, with $t$ as the
parameter labelling the equation. There is no $s$-variable on the RHS to be replaced.
The replacement "$\alpha_s$ for $s>t$ by $\bar\alpha(t,s)$" presupposes that the
solution has been written as $\mathbb{D}^{1-\gamma}$ acting on a function of an
auxiliary $s$-variable — i.e., presupposes the form of the answer.

### Issue B: The Fourier inversion mixes variables.

In step 4, the proof says "Fourier transform in $s$" of an equation parametrized by
$t$ with integration variable $v$. There is no $s$-variable in $(\star_{\rm bulk}^{\mathcal{F}})$.
The proof implicitly:
(i) identifies $\bar u(t,v) := \mathbb{E}_t[u^*_v]$ as the unknown function;
(ii) treats $\bar u(t,\cdot)$ at fixed conditioning time $t$ as a function of $v$,
   relabels $v=s$, and Fourier-transforms in $s$;
(iii) writes the RHS as a function of $s$ — but $\alpha_t$ has no $s$-dependence,
   so this step requires identifying the RHS-as-function-of-$s$ as $\bar\alpha(t,s)$.

Step (iii) is the **substitution that needs justification**. It works because the
conditioned FOC at each $t$ pins down $\bar u(t,\cdot)$ as a function whose convolution
with $G$ equals $\alpha_t = \bar\alpha(t,t)$ at the diagonal point $v=t$, plus a
consistency requirement across $t$.

### Issue C: The certainty-equivalence ansatz is implicit.

The argument that makes the substitution rigorous is:
1. Conjecture/prove that $u^*_v = K[\bar\alpha(v,\cdot)](v)$ for some linear
   translation-invariant operator $K$ (LQ certainty-equivalence ansatz).
2. Use the **forecast tower property**: for $t\le v$,
   $\mathbb{E}_t[\bar\alpha(v,s)] = \bar\alpha(t,s)$ for all $s\in\mathbb{R}$ (verified
   case-by-case using the definition of $\bar\alpha$ and the tower property of
   conditional expectation).
3. Under (1), $\mathbb{E}_t[u^*_v] = K[\mathbb{E}_t\bar\alpha(v,\cdot)](v) =
   K[\bar\alpha(t,\cdot)](v)$ by linearity of $K$ and the tower property.
4. Substitute into $(\star_{\rm bulk}^{\mathcal{F}})$: $\int G(|t-v|) K[\bar\alpha(t,\cdot)](v)\,dv = \alpha_t$,
   i.e. $(G\ast K\bar\alpha(t,\cdot))(t) = \bar\alpha(t,t)$. For this to hold for all
   forecast curves, $G\ast K = I$, so $\hat K = 1/\hat G = c_\gamma^{-1}|\xi|^{1-\gamma}$,
   giving $K = c_\gamma^{-1}\mathbb{D}^{1-\gamma}$.

The paper executes step 4 but not steps 1–3 explicitly. The conjecture in step 1 is
the standard LQ certainty-equivalence ansatz, which holds rigorously in finite-state
LQG (Bensoussan, Kwakernaak) but requires more care for non-local cost functionals
on infinite-dimensional state.

### Issue D: The forecast tower property is never stated.

The identity $\mathbb{E}_t[\bar\alpha(v,s)] = \bar\alpha(t,s)$ for $t\le v$ is the
algebraic glue that makes the substitution work. The paper uses it implicitly via
"$\mathbb{E}_t[u^*_v]$ is determined by $\bar\alpha(t,\cdot)$" but does not state or prove it.

### Issue E: Sufficiency / uniqueness under adaptedness.

Theorem 4.1 asserts "the unique stationary $L^2(\mathbb{R})$ solution." This is the
uniqueness for the *deterministic* FOC. For the stochastic problem there are two
separate uniqueness questions:
- Uniqueness of $u^*$ in the $\mathcal{F}_t$-adapted class.
- Sufficiency: does satisfying the conditioned FOC + adaptedness imply optimality?

The cost is strictly convex in $u$ (positive Riesz kernel $G$ + quadratic), so the
critical point is the global minimum **on the admissible class**. But the admissible
class for the adapted problem is a strict subset of the deterministic class. The
paper does not show that the candidate $c_\gamma^{-1}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$
is the unique minimizer in the adapted class — only that it satisfies the
conditioned FOC.

A cleaner argument: convex projection of the deterministic optimum onto the
$\mathcal{F}_t$-adapted subspace minimizes the cost (because the cost is a strictly
convex quadratic with positive-definite Hessian, and the adapted subspace is closed).
Then linearity of $\mathbb{D}^{1-\gamma}$ + the forecast definition + Fubini give the
substitution. This is the cleanest path; the paper does not take it.

### Issue F: Commutation of $\mathbb{E}_t$ with $\mathbb{D}^{1-\gamma}$.

Equivalent characterization: $\mathbb{E}_t[\mathbb{D}^{1-\gamma}\alpha(\cdot)(v)] =
\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(v)$ for $v\ge t$. This requires Fubini-Tonelli
on the (non-local) Riesz kernel and the integrability assumption on $S_\alpha$.
Verifying this commutation is the "swap conditional expectation through the operator"
step. The paper does not verify it.

### Issue G: Comparison to relevant literature.

- Abi Jaber & Neuman (2022, "Optimal liquidation with signal: the general propagator
  case", arXiv:2211.00447) handle a closely related propagator problem with signals
  rigorously via BSDEs, with explicit conditional-expectation handling. The paper
  cites them in §6.3 but does not contrast the derivational style.
- Almgren–Chriss / Obizhaeva–Wang use specific kernels where CE is automatic from
  state-space LQG arguments. The paper cites them in §6.2.
- A reference to LQ certainty-equivalence (Bensoussan 1992, *Stochastic Control of
  Partially Observable Systems*; Kwakernaak–Sivan 1972) would anchor the
  substitution in standard control theory.

## What works in the current argument

- The mechanical statement of $(\star_{\rm bulk}^{\mathcal{F}})$ via $\mathbb{E}_t[\cdot]$
  of the deterministic FOC is correct.
- The adaptedness observation in §4.2 — that applying the non-causal $\mathbb{D}^{1-\gamma}$
  in the $s$-variable to the $\mathcal{F}_t$-measurable curve $\bar\alpha(t,\cdot)$
  produces an $\mathcal{F}_t$-measurable answer — is correct.
- The final formula $u^*_t = c_\gamma^{-1}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$
  is correct (verifiable by direct substitution + the forecast tower).
- The OU example in §4.2 implementation ($\bar\alpha(t,s) = e^{-\theta(s-t)}\alpha_t$
  for $s>t$) is correctly the conditional forecast.

## Summary

The substitution $\alpha\to\bar\alpha$ is in fact justified, but the paper's
presentation conflates two separate operations:
- Taking conditional expectation of the FOC at $t$ (mechanical, correct).
- Asserting that the solution depends on the time-$t$ forecast curve as a function of
  an auxiliary $s$-variable (a CE ansatz that requires the forecast tower property +
  linearity + uniqueness in admissible class).

The user's intuition that the argument is "hand-wavy" is correct: the second
operation is presented as if it follows mechanically from the first, but it actually
requires a separate ansatz and verification.

## Recommended fix

A rewritten §2.3 closing paragraph + §4.1 proof should:
1. State the ansatz: $u^*_v = K[\bar\alpha(v,\cdot)](v)$ for some linear operator $K$.
2. State the forecast tower property as a lemma with a one-line proof.
3. Substitute the ansatz into the conditioned FOC, derive $K = c_\gamma^{-1}\mathbb{D}^{1-\gamma}$.
4. Verify sufficiency via convexity (or cite the convex projection argument).
5. Optionally: cite Abi Jaber–Neuman for a BSDE-based rigorous derivation.

This costs about half a page and resolves the hand-waving.

## Inspected sources

- `papers/fractional-derivative-optimal-execution.md` (local Markdown, 958 lines).
  Lines 85–99 (§2.2 forecast curve definition).
  Lines 100–134 (§2.3 cost + deterministic + conditioned FOCs).
  Lines 202–220 (§4.1 statement + proof).
  Lines 222–230 (§4.2 adaptedness).
  Lines 301–312 (§4.5 EL derivation, sign convention).
