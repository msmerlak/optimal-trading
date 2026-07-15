# Review: the $\alpha\to\bar\alpha$ substitution in the bulk solution

**Artifact:** `papers/fractional-derivative-optimal-execution.md` (local Markdown draft)
**Scope of review:** the argument that produces $u^{\rm bulk}_t = \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$ from the conditioned bulk FOC. Specifically §2.3 ("Stochastic FOC and emergence of the forecast curve") and the proof of Theorem 4.1 in §4.1.
**Date:** 2026-06-28.
**Evidence file:** `outputs/.drafts/forecast-curve-substitution-review-evidence.md`.

## Summary assessment

The substitution is **correct as a final formula** but the *derivation* presented in §2.3 and the §4.1 proof is **logically thin and the user's "hand-wavy" diagnosis is accurate**. The argument as written conflates two separate steps:

1. **Mechanical step** (correct): take $\mathbb{E}_t[\cdot]$ of the pathwise FOC to get $\int G(|t-v|)\mathbb{E}_t[u^*_v]\,dv = \alpha_t - \lambda$.
2. **Substantive step** (under-justified): assert that "inverting the kernel symbol produces a solution in which $\alpha_s$ is replaced for $s>t$ by $\bar\alpha(t,s)$."

Step 2 is presented as if it follows automatically from step 1. It does not. Step 2 is a **certainty-equivalence ansatz** — that the optimal control at time $v$ is a linear functional of the time-$v$ forecast curve $\bar\alpha(v,\cdot)$ — combined with the **forecast tower property** $\mathbb{E}_t[\bar\alpha(v,s)] = \bar\alpha(t,s)$ for $t\le v$. Neither is stated explicitly. The proof of Theorem 4.1 then does Fourier-transform-in-$s$ on an equation whose explicit variables are $t$ (parameter) and $v$ (integration variable), with no $s$ in sight — the relabelling $v\to s$ that lets the proof go through is the substitution being justified.

The final formula is recoverable rigorously, but the paper's path to it skips load-bearing intermediate steps.

---

## Strengths

- §4.2 correctly identifies *why* $\bar\alpha(t,\cdot)$ (rather than the realized path) is the right object: non-causality of $\mathbb{D}^{1-\gamma}$ in the $s$-variable is harmless when applied to an $\mathcal{F}_t$-measurable curve. This adaptedness point is well-articulated.
- §2.2's definition of the forecast curve is clean: $\bar\alpha(t,s) = \alpha_s$ for $s\le t$, $=\mathbb{E}_t[\alpha_s]$ for $s>t$ — explicitly $\mathcal{F}_t$-measurable on all of $\mathbb{R}$.
- The conditioned FOCs $(\star^{\mathcal{F}})$, $(\star_{\rm WH}^{\mathcal{F}})$, $(\star_{\rm bulk}^{\mathcal{F}})$ are correctly written down once and then re-used across §4–5.
- The OU example in §4.2 implementation paragraph (with $\bar\alpha(t,s) = e^{-\theta(s-t)}\alpha_t$ for $s>t$) is correctly the OU conditional forecast and makes the abstract machinery concrete.

---

## Critical issues

### C1. The substitution sentence in §2.3 is a non-sequitur as written.

> "Inverting the kernel symbol on $(\star_{\rm bulk}^{\mathcal{F}})$ produces a solution in which $\alpha_s$ is replaced for $s>t$ by its $\mathcal{F}_t$-conditional expectation, i.e. by the forecast curve $\bar\alpha(t,s)$."  (line ~134)

The RHS of $(\star_{\rm bulk}^{\mathcal{F}})$ is $\alpha_t - \lambda$ — a single $\mathcal{F}_t$-measurable random variable, parametrized by $t$. There is no "$\alpha_s$ for $s>t$" in the equation to be replaced. The sentence presupposes that the answer has been written in the form $\mathbb{D}^{1-\gamma}\alpha(\cdot)(t)$ as an operator applied to a function of an $s$-variable, and that this function is then replaced by $\bar\alpha(t,\cdot)$. That is the substitution being claimed — it cannot be the consequence of an opaque "inversion."

### C2. The Theorem 4.1 proof Fourier-transforms in a variable that does not appear.

> "Take the Fourier transform in $s$ of the $\mathcal{F}_t$-conditioned bulk FOC $(\star_{\rm bulk}^{\mathcal{F}})$ of §2.3, in which $\mathbb{E}_t[u^*_v]$ on the LHS is determined by $\bar\alpha(t,\cdot)$ on the RHS." (line ~211)

The FOC $(\star_{\rm bulk}^{\mathcal{F}})$ has variables $t$ (parameter) and $v$ (integration variable). There is no $s$. The proof is implicitly:

(i) defining $\bar u(t,v) := \mathbb{E}_t[u^*_v]$ as the unknown function;
(ii) at fixed conditioning time $t$, treating $\bar u(t,\cdot)$ as a function of $v$ and relabelling $v=s$;
(iii) treating the RHS as a function of $s$, identifying it with $\bar\alpha(t,s)$.

Step (iii) is **the substitution** — i.e., it pretends the result is what we are trying to prove. The clause "$\mathbb{E}_t[u^*_v]$ on the LHS is *determined by* $\bar\alpha(t,\cdot)$ on the RHS" presupposes a functional relationship that has not been established.

### C3. The certainty-equivalence ansatz is implicit.

The actual rigorous path uses the ansatz $u^*_v = K[\bar\alpha(v,\cdot)](v)$ for some linear translation-invariant operator $K$, together with the **forecast tower property** $\mathbb{E}_t[\bar\alpha(v,s)] = \bar\alpha(t,s)$ for $t\le v$ and all $s$. Under these:

$$\mathbb{E}_t[u^*_v] \;=\; \mathbb{E}_t\bigl[K\bar\alpha(v,\cdot)(v)\bigr] \;=\; K\bigl[\mathbb{E}_t\bar\alpha(v,\cdot)\bigr](v) \;=\; K[\bar\alpha(t,\cdot)](v),$$

(using linearity of $K$ + tower). Substituting into $(\star_{\rm bulk}^{\mathcal{F}})$ at conditioning time $t$:

$$\int_\mathbb{R} G(|t-v|)\,K[\bar\alpha(t,\cdot)](v)\,dv \;=\; \alpha_t \;=\; \bar\alpha(t,t),$$

i.e. $(G\ast K\bar\alpha(t,\cdot))(t) = \bar\alpha(t,t)$. For this to hold for all $t$ and all forecast curves, we need $G\ast K = \text{id}$ on the appropriate function space, giving $\hat K(\xi) = 1/\hat G(\xi) = c_\gamma^{-1}|\xi|^{1-\gamma}$, i.e. $K = c_\gamma^{-1}\mathbb{D}^{1-\gamma}$.

This is roughly the argument the paper *should* make. The two missing ingredients are the explicit ansatz and the tower property.

### C4. The forecast tower property is never stated.

The identity $\mathbb{E}_t[\bar\alpha(v,s)] = \bar\alpha(t,s)$ for $t\le v$ (and all $s\in\mathbb{R}$) is the algebraic glue that makes the substitution work. It needs one line of proof by cases (split on whether $s\le t$, $t<s\le v$, or $s>v$, then use the tower property of conditional expectation). The paper uses it implicitly but never states it.

### C5. Sufficiency / uniqueness for the stochastic problem is not established.

Theorem 4.1 says "the unique stationary $L^2(\mathbb{R})$ solution," which is uniqueness for the deterministic FOC. For the stochastic problem there are two separate questions:

- Is the policy $c_\gamma^{-1}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$ the unique $\mathcal{F}_t$-adapted minimizer?
- Is satisfying the conditioned FOC + adaptedness sufficient for optimality?

The cost is strictly convex (positive Riesz kernel), so a critical point in the *admissible* class is the global minimum **on that class**. But the deterministic and adapted admissible classes differ. The paper does not show that the candidate policy is the projection of the deterministic optimum onto the adapted subspace, nor that this projection is itself optimal — only that the candidate satisfies the conditioned FOC.

The cleanest argument is the convex-projection one: the cost is a strictly convex quadratic on the Hilbert space of square-integrable controls; the adapted subspace is closed; the unique adapted minimizer is the projection of the deterministic minimizer; by linearity of $\mathbb{D}^{1-\gamma}$ and the forecast definition, this projection equals $c_\gamma^{-1}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$. The paper does not take this route.

---

## Major issues

### M1. Swap of $\mathbb{E}_t$ with $\mathbb{D}^{1-\gamma}$ requires Fubini.

Equivalent formulation of the substitution: $\mathbb{E}_t[\mathbb{D}^{1-\gamma}\alpha(\cdot)(v)] = \mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(v)$ for $v\ge t$. This involves swapping conditional expectation with a non-local Riesz operator, which is a Fubini–Tonelli step on the Riesz kernel + integrability of $S_\alpha$. The paper imposes $\int (1+|\xi|^{2(1-\gamma)})S_\alpha(\xi)\,d\xi < \infty$ which ensures $\mathbb{D}^{1-\gamma}\alpha\in L^2$ pathwise, but the Fubini swap with $\mathbb{E}_t$ should be made explicit (one line).

### M2. The implicit identification "$\bar u(t,\cdot)$ depends on $\bar\alpha(t,\cdot)$" is the heart of the matter and deserves named status.

This is the **certainty-equivalence principle** for LQ control with non-local cost. It holds rigorously in the LQ setting (Bensoussan 1992 *Stochastic Control of Partially Observed Systems*; Kwakernaak & Sivan 1972 *Linear Optimal Control Systems*); the paper's setup is LQ in $u$ (quadratic cost, linear constraints) with a non-local kernel, so CE should apply but warrants either a citation or a paragraph showing why the standard arguments transfer.

### M3. No contrast with Abi Jaber–Neuman's rigorous propagator treatment.

§6.3 cites Abi Jaber & Neuman (Volterra/propagator with signal). Their treatment uses BSDEs with stochastic Fredholm equations and explicit conditional-expectation handling — exactly the rigour level this paper's §2.3/§4.1 currently lacks. A pointer or a sentence acknowledging that the BSDE machinery gives an alternative rigorous derivation would help locate the present argument in the literature.

### M4. The text "the forecast curve is therefore *generated* by conditioning the FOC, not substituted into the cost functional" overstates the rigour.

The forecast curve is in fact *introduced* in §2.2 *before* the FOC is conditioned, and the conditioned FOC has $\alpha_t$ on the RHS, not $\bar\alpha(t,\cdot)$. The forecast curve "emerges" only after the implicit CE ansatz is applied. The rhetorical move "generated by conditioning, not substituted" is misleading — the substitution still happens; it is just hidden inside the ansatz. Either own the substitution explicitly or rewrite to show the generation step.

---

## Minor issues

### m1. Variable naming.
Using $v$ inside the FOC and $s$ inside $\bar\alpha(t,\cdot)$ creates the variable-mismatch confusion above. Standardizing to one symbol (e.g., $s$) for the "second-time argument" throughout §2–§4 would already eliminate the proof-of-Theorem-4.1 confusion.

### m2. Stating the tower property as a small lemma.
A boxed identity
$$\mathbb{E}_t[\bar\alpha(v,s)] = \bar\alpha(t,s) \quad \text{for all } t\le v,\ s\in\mathbb{R}$$
with a four-line proof (split into $s\le t$, $t<s\le v$, $s>v$ cases) costs almost nothing and makes the whole §2.3/§4.1 chain transparent.

### m3. The bracketed mention of $\mathcal{F}_T$-measurability of $\lambda_t$ in §2.3.
"On the bounded interval the multiplier $\lambda_t$ enforcing $\int_0^T u_t\,dt = X_0$ is in general $\mathcal{F}_T$-measurable…projecting onto $\mathcal{F}_t$ replaces it by $\mathbb{E}_t[\lambda_T]$." This is correct but glossed-over; readers may want a one-sentence justification that the budget constraint + dual variable structure gives a martingale $\mathbb{E}_t[\lambda_T]$ on $[0,T]$.

### m4. §4.2 first paragraph.
"As derived in §2.3 (closing remark), the operative FOC for adapted controls is the $\mathcal{F}_t$-conditioned form..." If C1–C5 are addressed in §2.3, this sentence stays valid; if not, it is overstating ("derived" → "stated").

---

## Reproducibility and verification

- **Verification:** The final formula $u^*_t = c_\gamma^{-1}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$ has been numerically checked elsewhere in this project's `experiments/` directory (e.g., `riesz_split_check.py`, `ar1_433_vs_436.py`) — the Riesz-symbol/multiplicative/additive representations agree to machine precision, and the OU collapse $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t) = \theta^{1-\gamma}\alpha_t$ holds to $6\times 10^{-5}$ by Marchaud quadrature. So the **answer** is correct.
- The **derivation gap** in §2.3/§4.1 is the issue under review here; this gap is not a problem with the answer but with how the paper gets to the answer.
- No external experimental verification is needed; this is a textual/derivational review.

---

## Inline annotations (paper-side fixes)

| Location | Issue ref | Suggested fix |
|---|---|---|
| §2.3, line ~125, "Stochastic FOC and emergence of the forecast curve" paragraph | C1, C3, C4, M2, M4 | Replace the closing two sentences with: (a) state the ansatz $u^*_v = K[\bar\alpha(v,\cdot)](v)$; (b) state and prove the forecast tower lemma; (c) substitute and Fourier-invert to derive $K = c_\gamma^{-1}\mathbb{D}^{1-\gamma}$; (d) cite CE/Bensoussan or Abi Jaber-Neuman for the rigorous backing. |
| §4.1, Theorem 4.1 proof, line ~211 | C2, m1 | Either rename $v\to s$ in the FOC throughout §2.3 so the Fourier-in-$s$ proof reads naturally, or rewrite the proof's first sentence to make the variable identification explicit. |
| §4.1 Theorem 4.1 statement, "the unique stationary $L^2(\mathbb{R})$ solution" | C5 | Either add "in the adapted class" plus a one-line convexity justification, or add a sufficiency remark after the proof. |
| §4.2 first paragraph | M4 | Reword "as derived" to "as motivated" unless §2.3 is upgraded to an actual derivation. |
| §6.3 (Abi Jaber–Neuman) | M3 | Add one sentence: "Their BSDE formulation provides an alternative rigorous derivation of the forecast-curve substitution; we present a more elementary route via the LQ-CE ansatz of §2.3." |

---

## Recommendation

**Revise.** The bottom-line formula is correct and the paper's contributions stand, but §2.3 (the "Stochastic FOC and emergence of the forecast curve" paragraph) and the proof of Theorem 4.1 should be rewritten to:

1. Make the certainty-equivalence ansatz explicit (issue C3).
2. State and briefly prove the forecast tower property (issue C4).
3. Either rename $v\to s$ or rewrite Theorem 4.1's proof opening to remove the variable-relabelling sleight of hand (issue C2).
4. Address sufficiency/uniqueness in the adapted class, ideally via the convex-projection argument (issue C5).
5. Optionally cite CE / BSDE references for rigorous grounding (issue M2, M3).

The total surgery is ~half a page and converts an opaque "inverting produces" assertion into an actual derivation that a reviewer can verify line by line. The user's "hand-wavy" diagnosis is correct as a critique of *how the result is derived* — not as a critique of the result itself.

---

## Sources

- `papers/fractional-derivative-optimal-execution.md` — primary artifact (local Markdown, 958 lines).
- Evidence notes: `outputs/.drafts/forecast-curve-substitution-review-evidence.md`.
- Related project artifacts confirming the final formula:
  - `experiments/riesz_split_check.py` and its results note
  - `experiments/ar1_433_vs_436.py`
  - `notes/riesz-factorization-wiener-hopf.md`
- Standard references (not directly fetched in this review, cited for completeness):
  - A. Bensoussan, *Stochastic Control of Partially Observable Systems*, Cambridge University Press 1992 (LQG certainty equivalence).
  - H. Kwakernaak, R. Sivan, *Linear Optimal Control Systems*, Wiley 1972 (LQG-CE classic).
  - E. Abi Jaber, E. Neuman, "Optimal liquidation with signal: the general propagator case," arXiv:2211.00447 (BSDE/Volterra treatment of propagator + signal).
