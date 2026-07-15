# Causal/anticausal decomposition of the Riesz operator, and the scope of Wiener–Hopf

**Purpose.** Verification note backing a proposed §4.3 of `papers/fractional-derivative-optimal-execution.md` on the past/future decomposition of the bulk policy. Two questions:

1. *Constants.* Verify $\mathbb{D}^{1-\gamma}$ factorizes as $D_+^{(1-\gamma)/2}D_-^{(1-\gamma)/2}$ (and as the half-sum $\frac{1}{2\sin(\pi\gamma/2)}(D_+^{1-\gamma}+D_-^{1-\gamma})$) with explicit constants against SKM 1993 §7/§12, and check on an OU forecast example.
2. *Scope of Wiener–Hopf.* Why is W–H a half-line method? Where does it apply, where doesn't it, and which of those is the user's "factorize the Riesz derivative" idea?

Spoiler (revised after pushback; see §7 for the original framing and what was wrong with it):
- The **multiplicative Wiener–Hopf factorization** $\mathbb{D}^{1-\gamma} = D_+^{(1-\gamma)/2}D_-^{(1-\gamma)/2}$ is the operational past/future decomposition of the bulk policy: the anticausal factor $D_-^{(1-\gamma)/2}$ acts on the forecast curve $\bar\alpha(t,\cdot)$ to produce an $\mathcal{F}_t$-measurable intermediate $g^{(t)}$, and the causal factor $D_+^{(1-\gamma)/2}$ acts on $g^{(t)}$ at $s=t$ using only $\{s\le t\}$ values — i.e. causally in the intermediate. This is the optimal-execution analog of Wiener's spectral-factorization causal realization of a non-causal filter.
- The **additive (half-sum) form** $\mathbb{D}^{1-\gamma} = \frac{1}{2\sin(\pi\gamma/2)}(D_+^{1-\gamma} + D_-^{1-\gamma})$ is a *separate, also-valid* decomposition into one-sided full-order operators. Evaluated at $s=t$, it cleanly support-splits into a past-only term (realized-signal Marchaud derivative) and a future-only term (forecast-tail Marchaud derivative). Structurally different from the W–H factorization, useful for direct numerical evaluation.
- **The bulk-symbol W–H factorization holds on all three domains** ($\mathbb{R}$, $[0,T]$, $[0,\infty)$) and means the same thing in all three: anticausal-on-forecasts, causal-on-result. What is half-line–specific is a *different* W–H construction — factorization of the $\eta$-**augmented** symbol $M(\xi) = c_\gamma|\xi|^{\gamma-1}+\eta$, which selects boundary modes via half-plane analyticity (§5.3 of the paper). The user's intuition that "W–H applies everywhere" is correct for the bulk-symbol factorization; §5.3's W–H is a distinct method on a different symbol.

---

## 1. Conventions and SKM constants

Conventions throughout: Fourier $\hat f(\xi) = \int_\mathbb{R} e^{-i\xi s} f(s)\,ds$, inverse $(2\pi)^{-1}\int e^{i\xi s}\hat f\,d\xi$. Symbols on $\mathbb{R}$, all operators on Schwartz functions (or $L^2$ where appropriate).

### 1.1 One-sided Marchaud derivatives

For $\beta\in(0,1)$, the **left-sided (causal) Marchaud derivative** is

$$ D_+^\beta f(x) \;=\; \frac{\beta}{\Gamma(1-\beta)}\int_0^\infty \frac{f(x) - f(x-u)}{u^{1+\beta}}\,du \tag{1.1} $$

and the **right-sided (anticausal) Marchaud derivative**

$$ D_-^\beta f(x) \;=\; \frac{\beta}{\Gamma(1-\beta)}\int_0^\infty \frac{f(x) - f(x+u)}{u^{1+\beta}}\,du. \tag{1.2} $$

(SKM 1993 §5.4 eqs. (5.57)–(5.58).)

**Symbol.** Take $f(x) = e^{i\xi x}$. For $D_+^\beta$:

$$ D_+^\beta e^{i\xi\cdot}(x) \;=\; \frac{\beta\,e^{i\xi x}}{\Gamma(1-\beta)}\int_0^\infty \frac{1 - e^{-i\xi u}}{u^{1+\beta}}\,du. $$

Using $\int_0^\infty u^{-1-\beta}(1-e^{-pu})\,du = \frac{\Gamma(1-\beta)}{\beta}\,p^\beta$ for $\mathrm{Re}\,p>0$ (analytic continuation to $p = i\xi$ with the principal branch), we get

$$ \widehat{D_+^\beta f}(\xi) \;=\; (i\xi)^\beta\,\hat f(\xi), \qquad (i\xi)^\beta := |\xi|^\beta e^{i\,\beta\,\frac{\pi}{2}\,\mathrm{sgn}(\xi)}. \tag{1.3} $$

By symmetry $s\leftrightarrow -s$,

$$ \widehat{D_-^\beta f}(\xi) \;=\; (-i\xi)^\beta\,\hat f(\xi), \qquad (-i\xi)^\beta := |\xi|^\beta e^{-i\,\beta\,\frac{\pi}{2}\,\mathrm{sgn}(\xi)}. \tag{1.4} $$

(SKM 1993 §7.1 records (1.3)–(1.4); the branches are the standard ones with cuts off the imaginary axis.)

### 1.2 Riesz fractional derivative

The **symmetric Riesz fractional derivative** of order $\alpha\in(0,1)$ on $\mathbb{R}$ has symbol $|\xi|^\alpha$. SKM 1993 §12.1 defines it via Marchaud's hypersingular form; we use the half-sum representation valid for $\alpha\ne 1$:

$$ \mathbb{D}^\alpha f \;=\; \frac{D_+^\alpha f + D_-^\alpha f}{2\cos(\pi\alpha/2)}. \tag{1.5} $$

(SKM 1993 §7.1 Thm 7.1, also §12.1 (12.5); the $1/(2\cos)$ normalizes to make the symbol exactly $|\xi|^\alpha$.)

**Check (1.5) at the symbol level.** Using (1.3)–(1.4):

$$ (i\xi)^\alpha + (-i\xi)^\alpha \;=\; |\xi|^\alpha\bigl(e^{i\pi\alpha\mathrm{sgn}(\xi)/2} + e^{-i\pi\alpha\mathrm{sgn}(\xi)/2}\bigr) \;=\; 2|\xi|^\alpha\cos(\pi\alpha/2). $$

Dividing by $2\cos(\pi\alpha/2)$ gives $|\xi|^\alpha$. ✓

**For $\alpha = 1-\gamma$, $\gamma\in(0,1)$.** $\cos(\pi(1-\gamma)/2) = \sin(\pi\gamma/2)$, so

$$ \boxed{\;\mathbb{D}^{1-\gamma} \;=\; \frac{D_+^{1-\gamma} + D_-^{1-\gamma}}{2\sin(\pi\gamma/2)}.\;} \tag{1.6} $$

This is the **additive (half-sum) form** the paper implicitly uses (the $2\sin(\pi\gamma/2)$ in $\kappa_{1-\gamma}$ comes from here).

### 1.3 Multiplicative factorization

The symbol satisfies

$$ |\xi|^{1-\gamma} \;=\; (i\xi)^{(1-\gamma)/2}\cdot(-i\xi)^{(1-\gamma)/2}, $$

since the phases $e^{\pm i\pi\beta\mathrm{sgn}/2}$ cancel and $|\xi|^\beta|\xi|^\beta = |\xi|^{2\beta} = |\xi|^{1-\gamma}$ with $\beta = (1-\gamma)/2$. Therefore as operators on Schwartz functions,

$$ \boxed{\;\mathbb{D}^{1-\gamma} \;=\; D_+^{(1-\gamma)/2}\,D_-^{(1-\gamma)/2} \;=\; D_-^{(1-\gamma)/2}\,D_+^{(1-\gamma)/2},\;} \tag{1.7} $$

with **no extra constant**. The two operators commute because their symbols commute. Each factor has order $(1-\gamma)/2 \in (0,1/2)$ — half the order of the Riesz derivative.

---

## 2. Two valid past/future decompositions

Both (1.6) and (1.7) are valid representations of $\mathbb{D}^{1-\gamma}$. Applied to the **forecast curve**

$$ \bar\alpha(t,s) \;=\; \begin{cases}\alpha_s, & s\le t,\\ \mathbb{E}_t[\alpha_s], & s>t,\end{cases} $$

at $s=t$, each yields a different but valid decomposition of the bulk policy. **The multiplicative form is the operational Wiener–Hopf decomposition; the additive form is a complementary support-split at the diagonal point.**

### 2.1 Multiplicative form: Wiener–Hopf realization (forecasts then result)

The multiplicative form (1.7) says $\mathbb{D}^{1-\gamma}f = D_+^\beta(D_-^\beta f)$ as operators on Schwartz functions, with $\beta=(1-\gamma)/2$. Applied at $x=t$:

$$ u^{\rm bulk}_t \;=\; \kappa_{1-\gamma}\,D_+^\beta\!\bigl[\underbrace{D_-^\beta\bar\alpha(t,\cdot)}_{=:\,g^{(t)}}\bigr](t). \tag{2.1} $$

The construction has two steps, **both adapted**:

*Step 1 — anticausal factor on forecasts.* The intermediate function $g^{(t)}(s) := D_-^\beta\bar\alpha(t,\cdot)(s)$ is defined for all $s\in\mathbb{R}$. For each fixed $t$ and any $s$, $g^{(t)}(s)$ uses $\bar\alpha(t,r)$ for $r\ge s$. The forecast curve $\bar\alpha(t,\cdot)$ is $\mathcal{F}_t$-measurable on the entire real line (§2.2 of the paper), so $g^{(t)}(s)$ is $\mathcal{F}_t$-measurable for every $s$. The anticausal factor *consumes* the forecast structure: future values of the signal (replaced by their $\mathcal{F}_t$-conditional expectations under the forecast model) enter the policy only through this step.

*Step 2 — causal factor on the result.* $u^{\rm bulk}_t = \kappa_{1-\gamma}D_+^\beta g^{(t)}(t)$ uses only $g^{(t)}(s)$ for $s\le t$. Causal in the intermediate function, by the support of $D_+^\beta$ (Marchaud form (1.1) integrates over $u>0$, i.e. samples $g^{(t)}$ to the past of $t$).

This is exactly the **causal realization** of the non-causal Riesz operator: the anticausal piece $D_-^\beta$ is absorbed into a forecast operation that produces an adapted intermediate, and the remaining causal piece $D_+^\beta$ acts on the intermediate using only its past. It is the optimal-execution analog of the Wiener spectral-factorization solution to the causal Wiener filter.

*Remark on order-halving.* Each factor has order $(1-\gamma)/2 < 1/2$, half the order of the Riesz derivative. The two-step construction is numerically better-behaved than directly evaluating $\mathbb{D}^{1-\gamma}$ on the kinked curve $\bar\alpha(t,\cdot)$.

*Remark on parametric dependence.* The intermediate $g^{(t)}$ depends on $t$ as a parameter (different forecast at different $t$). It is *not* the diagonal trace of a single process $\tau\mapsto g^{(\tau)}(\tau)$; conflating these gives a different (and incorrect) policy. See §7 below for the cautionary calculation.

### 2.2 Additive form: support split at the diagonal

Evaluate (1.6) at $x = t$:

$$ u^{\rm bulk}_t \;=\; \frac{\kappa_{1-\gamma}}{2\sin(\pi\gamma/2)}\Bigl[D_+^{1-\gamma}\bar\alpha(t,\cdot)(t) \;+\; D_-^{1-\gamma}\bar\alpha(t,\cdot)(t)\Bigr]. \tag{2.2} $$

By the definitions (1.1)–(1.2):

- $D_+^{1-\gamma}\bar\alpha(t,\cdot)(t)$ uses $\bar\alpha(t,s)$ for $s\le t$ only — the realized past:
  $$ D_+^{1-\gamma}\bar\alpha(t,\cdot)(t) \;=\; \frac{(1-\gamma)}{\Gamma(\gamma)}\int_0^\infty\frac{\alpha_t - \alpha_{t-u}}{u^{2-\gamma}}\,du \;=:\; (D_+^{1-\gamma}\alpha)(t). $$
- $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t)$ uses $\bar\alpha(t,s)$ for $s\ge t$ only — the forecast tail:
  $$ D_-^{1-\gamma}\bar\alpha(t,\cdot)(t) \;=\; \frac{(1-\gamma)}{\Gamma(\gamma)}\int_0^\infty\frac{\alpha_t - \mathbb{E}_t[\alpha_{t+u}]}{u^{2-\gamma}}\,du. $$

The support-split is **at the diagonal point $s=t$ only**: each one-sided full-order operator integrates entirely over one half of the curve. This is structurally different from §2.1 — in (2.2) each operator has order $1-\gamma$, not $(1-\gamma)/2$, and the decomposition is additive, not factorized. It does not arise from a symbol factorization; it arises from writing $|\xi|^{1-\gamma} = \frac{1}{2\cos(\pi(1-\gamma)/2)}((i\xi)^{1-\gamma}+(-i\xi)^{1-\gamma})$, which is an algebraic identity, not a W–H factorization.

### 2.3 Which to use

Both representations are correct. They give different operational stories:

| Form        | Operator structure                  | Action on $\bar\alpha(t,\cdot)$ at $s=t$              | Interpretation                                              |
|-------------|-------------------------------------|------------------------------------------------------|-------------------------------------------------------------|
| Multiplicative (W–H) | $D_+^{\beta}\circ D_-^{\beta}$, $\beta=(1-\gamma)/2$ | Anticausal half-order on forecasts → causal half-order on result | Causal realization via spectral factorization |
| Additive (half-sum)  | $\tfrac{1}{2\sin(\pi\gamma/2)}(D_+^{1-\gamma}+D_-^{1-\gamma})$ | One-sided full-order on past + one-sided full-order on forecast tail | Support-split at the diagonal |

The multiplicative form is the W–H structural statement and the natural choice for connecting to filter-theoretic / Wiener-filter intuition. The additive form is the natural choice for direct closed-form evaluation when the forecast model produces a tractable $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t)$ (e.g. the OU case below, §3).

---

## 3. OU forecast example

Take a stationary OU signal $d\alpha_t = -\theta\alpha_t\,dt + \sigma\,dW_t$, $\theta>0$, so $\bar\alpha(t,s) = e^{-\theta(s-t)}\alpha_t$ for $s>t$.

### 3.1 Anticausal Marchaud derivative of the forecast tail at $s=t$

Direct computation at the diagonal point:

$$ D_-^\beta\bar\alpha(t,\cdot)(t) \;=\; \frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{\alpha_t - e^{-\theta u}\alpha_t}{u^{1+\beta}}\,du \;=\; \alpha_t\cdot\frac{\beta}{\Gamma(1-\beta)}\int_0^\infty\frac{1 - e^{-\theta u}}{u^{1+\beta}}\,du. $$

Using $\int_0^\infty u^{-1-\beta}(1 - e^{-\theta u})\,du = \frac{\Gamma(1-\beta)}{\beta}\theta^\beta$ (derivation: differentiate w.r.t. $\theta$ to get $\Gamma(1-\beta)\theta^{\beta-1}$ which integrates from $0$ to $\theta$ to give $\Gamma(1-\beta)\theta^\beta/\beta$):

$$ \boxed{\; D_-^\beta\bar\alpha(t,\cdot)(t) \;=\; \theta^\beta\,\alpha_t. \;} \tag{3.1} $$

The anticausal Marchaud derivative of the OU forecast tail, evaluated at the diagonal $s=t$, collapses to a simple multiplier of the current state. **Specialization $\beta = 1-\gamma$ (additive-form ingredient):**

$$ D_-^{1-\gamma}\bar\alpha(t,\cdot)(t) \;=\; \theta^{1-\gamma}\alpha_t. \tag{3.2} $$

**Caveat.** Equation (3.1) is the value at $s=t$ only. The full intermediate function $g^{(t)}(s) := D_-^\beta\bar\alpha(t,\cdot)(s)$ for $s\ne t$ does *not* equal $\theta^\beta\alpha_s$ in general. For $s>t$, $g^{(t)}(s) = \theta^\beta e^{-\theta(s-t)}\alpha_t$ (same Marchaud computation on the exponential tail). For $s<t$, $g^{(t)}(s)$ depends on the realized signal increments on $(s,t]$ in addition to the time-$t$ forecast tail on $(t,\infty)$:

$$ g^{(t)}(s) \;=\; \frac{\beta}{\Gamma(1-\beta)}\Bigl[\int_0^{t-s}\!\!\frac{\alpha_s - \alpha_{s+u}}{u^{1+\beta}}\,du \;+\; \int_{t-s}^\infty\!\!\frac{\alpha_s - e^{-\theta(s+u-t)}\alpha_t}{u^{1+\beta}}\,du\Bigr]. \tag{3.3} $$

The function $g^{(t)}(\cdot)$ is the input to the causal factor $D_+^\beta$ in (2.1).

### 3.2 Bulk policy for OU signal (additive evaluation)

For closed-form evaluation, the additive form (2.2) is most convenient because (3.2) gives the forecast contribution in closed form. Inserting:

$$ u^{\rm bulk}_t \;=\; \frac{\kappa_{1-\gamma}}{2\sin(\pi\gamma/2)}\bigl[(D_+^{1-\gamma}\alpha)(t) \;+\; \theta^{1-\gamma}\alpha_t\bigr]. \tag{3.4} $$

With $\kappa_{1-\gamma} = \bigl(2c\Gamma(1-\gamma)\sin(\pi\gamma/2)\bigr)^{-1}$,

$$ u^{\rm bulk}_t \;=\; \frac{1}{4c\Gamma(1-\gamma)\sin^2(\pi\gamma/2)}\bigl[(D_+^{1-\gamma}\alpha)(t) \;+\; \theta^{1-\gamma}\alpha_t\bigr]. \tag{3.5} $$

**Interpretation.** For an OU signal:
- The forecast contribution to the bulk policy (additive-form perspective) is **$\theta^{1-\gamma}\alpha_t$** — a simple linear function of the current signal state, scaled by the mean-reversion rate to the power $1-\gamma$.
- The realized-signal contribution $(D_+^{1-\gamma}\alpha)(t)$ is a causal Marchaud derivative — a hyperbolically-weighted moving average of past *increments* of the realized OU path.

**Limits.**
- $\theta\to 0$ (signal becomes a Brownian motion, infinite mean-reversion time): forecast contribution $\theta^{1-\gamma}\alpha_t \to 0$. Only the realized past matters.
- $\theta\to\infty$ (signal becomes white-noise-like, no useful forecast): formally $\theta^{1-\gamma}\alpha_t$ blows up, but the contribution to the integrated cost stays bounded because $\alpha_t$ also fluctuates faster.
- $\gamma\to 1$ (Dirac-like instantaneous impact): $\Gamma(1-\gamma)\to\infty$, prefactor $\to 0$, policy collapses.

### 3.3 Multiplicative form for OU: order-halving check at the symbol level

The multiplicative form (2.1) applied to OU should give the same answer. Symbol-level check (treating $\alpha$ as stationary OU on $\mathbb{R}$, with Fourier representation $\hat\alpha(\xi) = \sigma\,\widehat{dW}(\xi)/(\theta+i\xi)$):

- Riesz form: multiplier on $\widehat{dW}$ is $\kappa_{1-\gamma}|\xi|^{1-\gamma}/(\theta+i\xi) \cdot \sigma$.
- Multiplicative form (2.1): same multiplier, by the symbol identity $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$.

The two forms therefore agree on the policy spectrum. The additive form (3.4) also agrees by the symbol identity $|\xi|^{1-\gamma} = \frac{1}{2\cos(\pi(1-\gamma)/2)}((i\xi)^{1-\gamma}+(-i\xi)^{1-\gamma})$ — i.e. the additive form is just a Fourier-symbol identity, not a process-level identity that singles out OU.

What is OU-specific is the *closed-form collapse* (3.2): $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t) = \theta^{1-\gamma}\alpha_t$. This is what makes the additive form attractive for OU; the multiplicative form gives the same answer but requires either computing $g^{(t)}(s)$ for $s\le t$ (eq. 3.3, a mixed expression) or going via Fourier.

---

## 4. The role of Wiener–Hopf factorization

This section addresses: *why is W–H factorization typically a half-line method, and where does the user's "factorize the Riesz derivative" intuition fit?*

### 4.1 What W–H factorization is

W–H factorization of a function $M:\mathbb{R}\to\mathbb{C}$ (or distribution) is a decomposition

$$ M(\xi) \;=\; M_+(\xi)\,M_-(\xi) $$

where $M_+$ extends analytically and non-vanishingly to the **upper half plane** $\{\mathrm{Im}\,\xi>0\}$ and $M_-$ to the **lower half plane** $\{\mathrm{Im}\,\xi<0\}$. Analyticity in the upper half plane corresponds (via Paley–Wiener) to a function $\check M_+$ supported on the **causal half-line** $\{t\ge 0\}$, and analyticity in the lower half plane to support on $\{t\le 0\}$.

So W–H factorization splits a symbol into a **causal factor × anticausal factor**.

### 4.2 Why W–H is a half-line method

The classical W–H setting: solve

$$ \eta\,u(t) \;+\; \int_0^\infty K(t-s)\,u(s)\,ds \;=\; f(t), \qquad t\ge 0, $$

with $u$ unknown on $t\ge 0$ and the equation only required to hold for $t\ge 0$. The trouble is the unknown $u(s)$ for $s\ge 0$ is convolved with $K$ over the full line, producing values for all $t$, not just $t\ge 0$. The unknown extension of the equation to $t<0$ is the obstruction.

W–H's resolution: extend $u$ by zero to $t<0$, get a function on $\mathbb{R}$, and use the factorization $M(\xi) = \eta + \hat K(\xi) = M_+(\xi)M_-(\xi)$ to separate the unknown half-line extension from the known half-line data. The causal factor $M_+$ kills the unknown extension by analyticity in the upper half plane; the anticausal factor $M_-$ does the same for the known data. After dividing, both sides are analytic in complementary half planes and must equal a common entire function, which is computable from the known $f$.

**The whole point** is to resolve a domain-restriction ambiguity. Without the half-line restriction, there is no unknown extension and direct Fourier inversion on $\mathbb{R}$ suffices. W–H is the tool that **converts a half-line integral equation into a full-line equation with a known forcing**.

### 4.3 Bulk-symbol Wiener–Hopf on $\mathbb{R}$: representational *and* operational

The user's intuition: factorize $|\xi|^{1-\gamma} = (i\xi)^{(1-\gamma)/2}(-i\xi)^{(1-\gamma)/2}$. This is a Wiener–Hopf factorization of the bulk symbol on $\mathbb{R}$: $(i\xi)^\beta$ extends analytically to $\mathrm{Im}\,\xi > 0$ (causal factor), $(-i\xi)^\beta$ to $\mathrm{Im}\,\xi < 0$ (anticausal factor). The factorization holds.

**Operational content.** Unlike the half-line setting, on $\mathbb{R}$ there is no unknown extension to resolve, so W–H is not needed as a *solution method*: direct Fourier inversion of the symbol $|\xi|^{\gamma-1}$ already gives $u^{\rm bulk} = \kappa_{1-\gamma}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$. **However**, the W–H factorization on $\mathbb{R}$ is *not* purely representational: it furnishes the **causal realization** of the bulk policy, in the spirit of Wiener's solution to the realizable optimal filter. Specifically (§2.1):

1. The anticausal factor $D_-^\beta$ acts on the forecast curve $\bar\alpha(t,\cdot)$ — a step that *would* require future signal values if acting on the realized $\alpha$, but which becomes adapted by virtue of $\bar\alpha(t,\cdot)$ being $\mathcal{F}_t$-measurable on the whole real line.
2. The causal factor $D_+^\beta$ then acts on the intermediate $g^{(t)} = D_-^\beta\bar\alpha(t,\cdot)$ at $s=t$, using only $g^{(t)}(s)$ for $s\le t$ — causally in the intermediate.

This is the structural content the user is pointing at: future information enters only through the forecast model (step 1), and the remaining processing (step 2) is causal in the prediction-corrected intermediate. The factorization is therefore operationally meaningful on $\mathbb{R}$ even though it does not introduce a new solution path — it gives a *realizable architecture* for computing the same answer.

This is the **same** kind of statement as Wiener's spectral-factorization solution to the causal Wiener filter on $\mathbb{R}$: the underlying equation does not require W–H to solve, but W–H exposes the structure that makes the solution realizable in a causal pipeline modulo a prediction step. Our setting differs from Wiener filtering in that the "prediction step" is exactly the forecast curve $\bar\alpha(t,\cdot)$ already built into the adaptedness structure of §2.2 of the paper.

### 4.4 Two distinct W–H factorizations

Conflating these will confuse a reader. Two factorizations are at play in the paper, on different symbols and doing different jobs:

| Factorization                | Symbol                            | Domain    | Role                                                              |
|------------------------------|-----------------------------------|-----------|-------------------------------------------------------------------|
| **Bulk-symbol W–H** (§4.3) | $|\xi|^{1-\gamma}$                | $\mathbb{R}$ (and inherited on $[0,T]$, $[0,\infty)$ for the bulk part) | Causal realization of the bulk policy: anticausal-on-forecasts → causal-on-result. Operational content via the two-step W–H architecture, not a new solution method on $\mathbb{R}$. |
| **Augmented-symbol W–H** (paper §5.3)  | $c_\gamma|\xi|^{\gamma-1} + \eta$ | $[0,\infty)$ | Resolves the half-line domain ambiguity by half-plane analyticity. **Genuinely a half-line solution method**, selects the decaying boundary mode and the well-posedness regularizer interaction. |

The user's "W–H of the Riesz derivative applies everywhere" is the first row — correct, both at the symbol level and operationally (the causal-realization architecture is meaningful in every domain because the bulk operator is the same Riesz operator everywhere). The half-line specificity in the paper refers to the second row — a *different* symbol and a *different* construction. They should be presented separately.

### 4.5 Bounded interval

For completeness: on $[0,T]$ the Söhngen–Tricomi inversion of the Abel operator plays the role analogous to W–H on $[0,\infty)$. It uses different machinery (Carleman singular-integral equations, airfoil equation theory; SKM 1993 §13.2) because the *two* endpoints $0$ and $T$ both contribute homogeneous modes, whereas W–H handles a single endpoint at $0$ with decay at $\infty$.

A unified theory of domain restrictions of the bulk Riesz operator would treat W–H ($[0,\infty)$) and Söhngen–Tricomi ($[0,T]$) as instances of a common construction; this is essentially the §5.1 *Boundary correction principle* abstract picture in the paper. But the bulk-symbol factorization of §4.3 is logically prior to and independent of either domain restriction.

---

## 5. Verdict for paper §4.3

Recommended structure (revised after pushback):

1. State the bulk theorem in Riesz form (already done in §4.1).
2. **New §4.3** *Wiener–Hopf factorization of the bulk operator and the causal realization*:
   - State (1.7) — the multiplicative W–H factorization $\mathbb{D}^{1-\gamma} = D_+^{(1-\gamma)/2}D_-^{(1-\gamma)/2}$ — with the spectral-factorization statement $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$. **Lead with this.**
   - State (2.1): the bulk policy as a two-step causal realization. The anticausal half-order factor $D_-^\beta$ acts on the forecast curve $\bar\alpha(t,\cdot)$ to produce an $\mathcal{F}_t$-measurable intermediate $g^{(t)}$ (forecasts absorbed). The causal half-order factor $D_+^\beta$ then acts at $s=t$ using only $\{s\le t\}$-values of $g^{(t)}$ (causal in intermediate).
   - Frame this as the optimal-execution analog of Wiener's spectral-factorization causal realization. Reference Wiener 1949 / Wiener–Hopf 1931 / Noble 1958.
   - State (1.6) — the additive half-sum form — as a *complementary* representation. Note (2.2): support-split at the diagonal, useful for closed-form evaluation when the forecast model gives tractable $D_-^{1-\gamma}\bar\alpha(t,\cdot)(t)$ (e.g. the OU collapse to $\theta^{1-\gamma}\alpha_t$).
   - Cautionary remark: the multiplicative form is operator composition on a *fixed* curve $\bar\alpha(t,\cdot)$ parametrized by $t$. It is *not* the diagonal trace of a single process; conflating these gives a different policy (see §7 of this note).
3. Re-title current §5.3 to *Augmented-symbol Wiener–Hopf for the half-line*. In the opening, explicitly distinguish from §4.3: §4.3 is the bulk-symbol factorization $|\xi|^{1-\gamma}$ on all three domains (representational + causal-realization content); §5.3 is the augmented-symbol factorization $c_\gamma|\xi|^{\gamma-1}+\eta$ on $[0,\infty)$ (methodological boundary-mode selection).

This makes the paper's two W–H constructions visibly distinct, gives the user's intuition (§4.3 W–H on the full line, applied to forecasts) primary billing, and keeps the half-line specificity where it belongs (§5.3).

---

## 6. Loose ends / things I have **not** checked

- The hypersingular Marchaud-form regularization (SKM 1993 §5.4) for $\beta\in(0,1)$ requires $f$ to satisfy a Hölder/decay condition; this is automatic for the bulk theorem's assumptions ($\int(1+|\xi|^{2(1-\gamma)})S_\alpha(\xi)\,d\xi<\infty$) but is worth a one-line remark in the paper.
- The intermediate function $g^{(t)}(s)$ in (3.3) for $s<t$ has been written down but not used in any direct numerical scheme; in practice one would compute the policy via either (i) Fourier inversion of $|\xi|^{1-\gamma}\widehat{\bar\alpha}(\xi)$ or (ii) the additive form (3.4) for parametric forecast models. The multiplicative form's value is structural rather than computational.
- I have not checked the *bounded-interval* analog of either decomposition — on $[0,T]$ the one-sided Marchaud operators are truncated and both the multiplicative factorization and additive support-split interact with the Söhngen modes. Worth a paragraph in §5.2 but out of scope here.

---

## 7. Cautionary calculation: what the W–H factorization is *not*

This section preserves the calculation that motivated my original (incorrect) framing, and isolates the conflation that caused it. The W–H factorization

$$ \mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t) \;=\; D_+^\beta\bigl[D_-^\beta\bar\alpha(t,\cdot)\bigr](t) $$

is operator composition applied to the **fixed forecast curve $\bar\alpha(t,\cdot)$** parametrized by the conditioning time $t$. It is *not* the composition

$$ D_+^\beta\Bigl[\tau\mapsto D_-^\beta\bar\alpha(\tau,\cdot)(\tau)\Bigr](t), \tag{7.1} $$

which would compute the diagonal-trace process $\tilde\alpha_\tau := D_-^\beta\bar\alpha(\tau,\cdot)(\tau)$ first, then apply a causal $D_+^\beta$ along the time axis $\tau$.

For an OU signal, (7.1) gives $\theta^\beta D_+^\beta\alpha(t)$, by (3.1). The Riesz bulk solution gives $\kappa_{1-\gamma}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$, with spectrum $\kappa_{1-\gamma}|\xi|^{1-\gamma}\hat{\bar\alpha}(\xi)$. Comparing multipliers on $\widehat{dW}$ via $\hat\alpha = \sigma/(\theta+i\xi)$:

- (7.1) gives multiplier $\theta^\beta(i\xi)^\beta\sigma/(\theta+i\xi)$.
- The bulk solution gives multiplier $\kappa_{1-\gamma}|\xi|^{1-\gamma}\cdot\hat{\bar\alpha}(\xi)$, which after Fourier-evaluating $\bar\alpha(t,\cdot)$ correctly does **not** reduce to a simple stationary OU multiplier (the forecast curve has a kink at $s=t$ and is non-stationary in $s$).

These are generically unequal: $\theta^\beta(i\xi)^\beta \ne $ (Riesz multiplier on the OU-on-$\mathbb{R}$ extension), as the symbol identity $2\sin(\pi\gamma/2)\theta^\beta z^\beta = z^{2\beta}+\theta^{2\beta}$ would require for the additive form to match, which it doesn't.

The conflation in my original note was identifying (7.1) (diagonal trace then causal filter) with the W–H factorization (operator composition on the time-$t$ curve). The diagonal trace is a process that drops information about how the forecast curve depends on $t$ as a parameter; the W–H factorization preserves that dependence by working with the full curve $\bar\alpha(t,\cdot)$ for each $t$.

The correct picture: for each $t$, **rebuild** the intermediate $g^{(t)}$ from scratch using the time-$t$ forecast curve, then apply $D_+^\beta$ at $s=t$. The intermediate is not stored or evolved across $t$.

This is a real subtlety. It says the W–H factorization gives the right bulk policy but not via a "compute one process, then filter causally" pipeline; the recomputation of $g^{(t)}$ at each $t$ is essential.

## References

- SKM 1993: Samko, Kilbas, Marichev, *Fractional Integrals and Derivatives: Theory and Applications*, Gordon & Breach 1993. §5.4 (Marchaud), §7.1 (Fourier symbols), §12.1 (Riesz), §13.2 (Söhngen / airfoil).
- Tricomi 1957: *Integral Equations*, Interscience 1957, §4.3 (airfoil equation).
- Wiener & Hopf 1931 original; Noble 1958, *Methods Based on the Wiener-Hopf Technique*, for the half-line method.
- Paley–Wiener theorem: standard reference, e.g. Rudin *Real and Complex Analysis* Ch. 19.
