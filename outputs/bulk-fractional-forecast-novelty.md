# Novelty audit: bulk fractional derivative of forecast curves

**Question.** How novel is the closed-form bulk-policy expression
$$u^{\rm bulk}_t \;=\; \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$$
— a Riesz fractional derivative of order $1-\gamma$ applied to the conditional
forecast curve $\bar\alpha(t,s) = \alpha_s\,\mathbb{1}_{s\le t} + \mathbb{E}_t[\alpha_s]\,\mathbb{1}_{s>t}$
— for the propagator model with power-law kernel $G(t)=c|t|^{-\gamma}$,
$\gamma\in(0,1)$?

**Date.** 2026-06-28.

**Evidence file.** `outputs/.drafts/bulk-fractional-forecast-novelty-research-evidence.md`.

---

## Executive verdict

The formula is **not novel in content** but **partially novel in presentation**,
with **one genuinely new conceptual bridge**.

| Layer | Novelty | Where |
|---|---|---|
| Power-law-kernel optimal execution with signal | **Not novel** | Forde–Sánchez-Betancourt–Smith 2022; Abi Jaber–Neuman 2022; Abi Jaber–Neuman–Tuschmann 2024; Abi Jaber et al. 2025 |
| Recognition that the Fredholm inverse for $G\propto t^{-\gamma}$ factorizes through half-order Riemann–Liouville derivatives | **Not novel** | FSS2022 §2.2 (Porter–Stirling 1990 decomposition $T = B^{-1}I_\nu B$ with $r=(1-\gamma)/2$) |
| Multiplicative Wiener–Hopf factorization $\|\xi\|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$ | **Not novel** | Samko–Kilbas–Marichev 1993; Krein 1962; Noble 1958 |
| Certainty-equivalence substitution $\alpha\to\bar\alpha$ | **Not novel** (implicit in all signal-adaptive work) | Neuman–Voß 2022; FSS2022; Abi Jaber–Neuman 2022 |
| Writing the answer as a clean Riesz operator on $\mathbb{R}$ applied to the forecast curve | **Re-organization** of known content (no paper writes it this way) | New to this work |
| Bulk/boundary spine as the organizing structure | **Novel framing** | New to this work |
| Explicit bridge to CRONE / Oustaloup fractional-PID control | **Novel contribution** | New to this work; not covered in arXiv:2512.12111 survey |

---

## 1. Closest prior work: Forde–Sánchez-Betancourt–Smith (2022)

[Forde, Sánchez-Betancourt, Smith. *Optimal trade execution for Gaussian signals
with power-law resilience.* Quant. Finance 22(3), 585–596, 2022.
https://doi.org/10.1080/14697688.2021.1950919]

**Identical setup.** Power-law decay kernel $G(t)=ct^{-\gamma}$ with $\gamma\in(0,1)$;
Gaussian signal $\xi_t = \mathbb{E}_t[P_T - P_t]$; propagator price impact
$S_t = P_t + \int_0^t G(t-s)dX_s$; maximization over progressively measurable
controls with full liquidation $X_T = 0$.

**Same FOC.** Their equation (4) is the analog of our $(\star^{\mathcal{F}})$:
$\xi_t + \mathbb{E}_t[\int_0^T G(|t-v|) u_v\,dv] = M_t$ for some martingale $M$ with
$X_T = 0$.

**Same fractional-operator structure, on the bounded interval.** Their Theorem 2.2
proof (p.592, third bullet) explicitly writes:
> "Then we can further re-write $T$ as $T = B^{-1} I_\nu B$, where $B$ is the
> bounded operator on $L^2$ which multiplies functions by $t^{-(1-\nu)/2}$ and
> $I_\nu$ is the **Riemann–Liouville operator** ... so $I_\nu^{-1} = \Gamma(1-r)D^r$,
> where $I_r$ and $D^r$ are the **fractional derivative operators of order $r$**."

with $r = (1-\gamma)/2 = \beta$. This is the *exact* half-order Riemann–Liouville
factorization that the present paper uses (called multiplicative Wiener–Hopf
factorization in our §4.3), differing only in domain (their $[0,1]$ via affine
rescaling of $[0,T]$ vs. our $\mathbb{R}$) and in conjugation by the weight
operator $B$ that handles the bounded-interval boundary.

**What FSS2022 does differently.** Three presentation choices distinguish FSS2022
from the present work:

1. **Volterra-ansatz on Brownian motion.** They ansatz $\hat u_t = \bar u(t) +
   \int_0^t k(v,t)\,dW_v$ and determine the kernels $k$ and $\bar u$ by Fredholm
   inversion. They do **not** identify the forecast curve $\bar\alpha(t,\cdot)$ as
   an object and apply the operator to it; the conditional expectations are
   absorbed into the Brownian-stochastic-integral representation.
2. **Bounded interval only.** No formulation on $\mathbb{R}$; no translation-
   invariant bulk problem; no bulk/boundary split.
3. **Special-function answer.** The final formulas are presented via the
   Chakrabarti–George (1994) explicit Abel-equation inversion, producing triple
   integrals with incomplete Beta functions and Gamma-ratio prefactors (e.g.
   their equation (26) for the rough-signal case). They do not write the simple
   Riesz form $\mathbb{D}^{1-\gamma}\bar\alpha$.

**Consequence.** FSS2022 already contain the fractional-operator structural insight
in operator-language form. What is *not* in FSS2022 is the clean Riesz-on-forecast-
curve presentation and the bulk/boundary framing.

---

## 2. Other primary references

### 2.1 Abi Jaber & Neuman (2022, arXiv:2211.00447)

General Volterra propagator (including power-law) + signal, bounded interval,
risk-aversion and terminal penalty. The value function is characterized via an
operator-valued Riccati equation and an $L^2$-valued BSDE; the optimal strategy
is given in operator-resolvent form. The word "fractional" appears only as a
*descriptor of the kernel*, never as the operator yielding the solution. The
formula $\mathbb{D}^{1-\gamma}\bar\alpha$ does not appear.

### 2.2 Abi Jaber, Neuman, Tuschmann (2024, arXiv:2403.10273)

Matrix-valued (cross-impact) Volterra propagators with signal. Same
operator-resolvent style as Abi Jaber–Neuman 2022, extended to multi-asset. No
fractional-derivative-of-forecast formulation.

### 2.3 Abi Jaber, Bondi, De Carvalho, Neuman, Tuschmann (2025, arXiv:2503.04323)

Non-linear price impact with general Volterra propagator including power-law. FOC
is a non-linear stochastic Fredholm equation; iterative solver with convergence
rate; power-law numerics via *sum-of-exponentials approximation*. The latter is
the standard "avoid the fractional operator" tactic, the opposite of exploiting
the fractional structure. No fractional-derivative-of-forecast formulation.

### 2.4 Gatheral, Schied, Slynko (Math. Finance 2012)

Deterministic case (no signal), bounded interval. Solves the Fredholm equation
directly; gets the closed-form U-shape $u^0(t) = c_1 (t(T-t))^{(1-\gamma)/2 - 1}$
for power-law via Chakrabarti–George inversion. No signal, no forecast curve, no
explicit fractional-operator language.

### 2.5 Neuman & Voß (2022, SIAM J. Financial Math.)

Exponential propagator + temporary impact + general semimartingale signal.
Explicit FBSDE-system; affine feedback law in inventory plus auxiliary state.
Power-law not covered (exponential propagator makes the problem Markovian).

### 2.6 Curato, Gatheral, Lillo (2017)

Non-linear power-law impact; Urysohn integral equations; numerical solution. No
fractional-operator formulation.

### 2.7 Almgren–Chriss / Obizhaeva–Wang / Gârleanu–Pedersen

Constant impact, exponential propagator, or quadratic costs respectively — closed
forms via ODE/Riccati without fractional operators.

---

## 3. Adjacent literature: fractional control

### 3.1 CRONE / Oustaloup fractional PID

[Oustaloup. *La commande CRONE.* Hermès, Paris, 1991; Oustaloup, Levron, Mathieu,
Nanot. *Frequency-band complex noninteger differentiator.* IEEE TCS-I 47(1), 25–39,
2000. https://doi.org/10.1109/81.817385]

Fractional-order PID controllers — control engineering for mechanical / biological
/ thermal systems. Apply fractional differentiators of order $\alpha\in(0,1)$ in
feedback loops; argue robustness to plant variations. **No application to
optimal execution in this literature.**

### 3.2 Fractional Calculus in Optimal Control and Game Theory survey (arXiv:2512.12111, Dec 2025)

[*Fractional Calculus in Optimal Control and Game Theory: A Survey.* arXiv:2512.12111, 2025.
https://arxiv.org/abs/2512.12111]

Reviews Caputo / Riemann–Liouville / Grünwald–Letnikov operators, Oustaloup
frequency-domain realizations, sum-of-exponentials approximations, fractional
Pontryagin / HJB, fractional LQR / MPC / PID. Domains: physical, biological,
engineered systems. **Optimal execution is not mentioned.**

This confirms that the optimal-execution ↔ CRONE bridge has not been drawn in
either direction: the execution literature does not cite CRONE; the fractional-
control literature does not cite optimal execution.

---

## 4. What is and is not novel

### Not novel

1. **The problem.** Power-law-kernel optimal execution with signal is solved in
   FSS2022 (Gaussian signals, full liquidation), Abi Jaber–Neuman 2022 (general
   progressively measurable signals, with risk-aversion and terminal penalty), and
   the 2024–2025 follow-ups.
2. **The fractional-operator structural fact.** That the Fredholm inverse of
   $G\propto t^{-\gamma}$ is built from half-order Riemann–Liouville operators is
   already in FSS2022 (operator language) and traces back to Porter–Stirling 1990
   for the underlying operator factorization.
3. **The Fourier symbol $\hat G(\xi)=c_\gamma|\xi|^{\gamma-1}$.** Textbook (Stein
   1970, SKM 1993, Tricomi 1957).
4. **The substitution $\alpha\to\bar\alpha$.** Implicit in every signal-adaptive
   propagator paper since at least Lehalle–Neuman 2019; explicit in Abi Jaber–
   Neuman 2022 where the value function is built on conditional-expectation states.

### Partially novel: re-organization of known content

5. **The clean Riesz-on-$\mathbb{R}$ form $\kappa_{1-\gamma}\mathbb{D}^{1-\gamma}
   \bar\alpha(t,\cdot)(t)$.** No paper writes the answer this way. FSS2022 give
   triple integrals with incomplete-Beta prefactors; Abi Jaber–Neuman give operator
   resolvents. The present form is more compact and matches the standard
   fractional-calculus textbook idiom.
6. **The forecast curve as an explicit named object.** Existing work substitutes
   conditional expectations inside expressions but does not isolate the object
   $s\mapsto\bar\alpha(t,s)$ and observe that it is $\mathcal{F}_t$-measurable
   on all of $\mathbb{R}$.
7. **Bulk/boundary decomposition spine.** Treating the whole-line translation-
   invariant problem as primary, with bounded-interval and half-line as
   boundary-perturbed restrictions, is a structural choice. Existing work
   (FSS2022, Abi Jaber–Neuman) starts on $[0,T]$ directly.

### Genuinely novel

8. **Explicit CRONE / fractional-PID bridge.** The optimal-execution literature
   has not drawn this connection; the fractional-control literature has not
   reached optimal execution. The bridge is what gives the formula
   $u^{\rm bulk}_t = \kappa\,\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$ a
   second interpretation as a fractional differentiator of forecasted alpha,
   placing optimal execution as a member of the same control-engineering
   family as CRONE. This is the most substantive novelty.
9. **Domain-level separation of two Wiener–Hopf factorizations.** The bulk-symbol
   factorization $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$ on $\mathbb{R}$
   (operator-level identity, used for all domains) is conceptually distinct from
   the augmented-symbol $\eta + c_\gamma|\xi|^{\gamma-1}$ Wiener–Hopf factorization
   on $[0,\infty)$ (used to pick the boundary mode for the half-line problem with
   temporary impact). FSS2022 use only the bounded-interval Porter–Stirling
   factorization $G_1 = TT^*$ — operator language for the same algebraic content
   as the bulk-symbol factorization, but without the domain-level conceptual
   distinction.

---

## 5. Consensus, disagreements, open questions

### Consensus

- The fractional kernel $G\propto t^{-\gamma}$ for transient price impact is
  empirically established (Bouchaud–Gefen–Potters–Wyart 2004; calibrated by
  FSS2022 to AAPL/CSCO/VOD intraday with $\hat\gamma\in[0.38, 0.49]$ across stocks).
- The optimal trading policy with signal under this kernel is *linear* in the
  signal (LQ structure → CE) and *non-local in time* (operator memory). All cited
  primary references agree on this structure.
- The Wiener–Hopf / Riemann–Liouville / Abel-inversion machinery is the right
  toolbox; the question is presentation, not substance.

### Disagreement / stylistic divergence

- **Presentation style.** Abi Jaber–Neuman style favors operator resolvents and
  BSDEs (formalism extending Volterra control theory); FSS2022 style favors
  Brownian-Volterra stochastic-integral representations; the present paper's
  style favors the fractional-calculus textbook idiom (Riesz on forecast curve).
  Each is a presentation choice for the same underlying content.
- **Domain primacy.** FSS2022 and Abi Jaber–Neuman: bounded interval is primary,
  unbounded only by limit. Present paper: bulk on $\mathbb{R}$ is primary,
  bounded interval / half-line are boundary-perturbed restrictions. Neither
  primacy is mathematically forced; it is a structural choice.

### Open questions

- Does the bulk Riesz form $\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$
  generalize to non-symmetric / Volterra-only kernels (the actual physical case
  is $G(t)\mathbb{1}_{t>0}$, not $|t|^{-\gamma}$ on $\mathbb{R}$)? The
  symmetrization step is standard but loses causal information that the
  half-line Wiener–Hopf treatment recovers.
- Can the CRONE bridge be sharpened into a robustness theorem? CRONE's robustness
  to plant variation is its central claim; the analog for optimal execution
  would be robustness of $\mathbb{D}^{1-\gamma}\bar\alpha$ to mis-specification of
  $\gamma$. The paper's §4.6 robustness remark is a starting point but not a
  theorem.
- Cross-impact extension (matrix Riesz): Abi Jaber–Neuman–Tuschmann 2024 give a
  matrix operator-resolvent answer; does that admit a matrix-Riesz-on-forecast
  presentation analogous to the scalar bulk theorem? The paper's §7 sketches
  this; the literature has not pursued it.
- Whether the Söhngen 1939 finite-interval Abel inversion connects to the
  bounded-interval boundary correction in a clean way (the paper sketches this
  in §5.2; not in FSS2022 or Abi Jaber–Neuman).

---

## 6. Recommended next reading (in order of relevance)

1. **Forde, Sánchez-Betancourt, Smith 2022** — the closest prior work; their §2.2
   Theorem 2.2 proof is the operator-language version of our §4.3 multiplicative
   Wiener–Hopf factorization. Cross-check carefully when claiming novelty.
2. **Abi Jaber & Neuman 2022 (v2 Sep 2025)** — sets the rigor bar via BSDE /
   operator-Riccati. Their treatment of admissibility, integrability, and
   uniqueness in the adapted class is the standard our §2.3 + §4.1 should aim to
   match (after the recent revision).
3. **Abi Jaber et al. 2025 (nonlinear Fredholm)** — for extending to non-linear
   impact; the Riesz-on-forecast form does not survive linearity, which sets a
   limit on the bulk-theorem framing.
4. **Survey arXiv:2512.12111** — for the fractional-control bridge; this survey
   is the natural venue / target for an optimal-execution-as-CRONE paper.
5. **Oustaloup 2000 IEEE TCS-I** — the CRONE robustness statements one would
   want to translate to execution.

---

## 7. Recommended positioning for the present paper

Given the evidence, the paper should:

1. **Cite FSS2022 prominently at the bulk-theorem statement.** Acknowledge that the
   operator-language equivalent of the bulk-symbol Wiener–Hopf factorization is
   in their proof of Theorem 2.2. Do not claim originality for the
   fractional-operator-Fredholm-inverse insight per se.
2. **Position the contribution as presentational + bridging.** The Riesz-on-
   forecast form is a re-presentation that yields three downstream goods:
   (i) the bulk/boundary spine making bounded-interval / half-line / whole-line
   cases unified rather than separate;
   (ii) the CRONE bridge connecting optimal execution to fractional-control engineering;
   (iii) a compact formula amenable to direct numerical implementation
   ($O(N\log N)$ via FFT, as noted in §4.6).
3. **Soften any "we derive" language for the underlying operator factorization.**
   The factorization $|\xi|^{1-\gamma} = (i\xi)^\beta(-i\xi)^\beta$ is in SKM 1993;
   its use for the bounded-interval Fredholm inverse with $G\propto t^{-\gamma}$
   is in FSS2022 (operator language). What is new is the whole-line bulk-symbol
   framing and the explicit identification of $\beta = (1-\gamma)/2$ as the
   causal/anticausal half-order split.

These positioning changes do not require new mathematics; they require honest
attribution and re-framing the contribution as presentational + bridging rather
than mathematical-first-derivation.

---

## Sources

### Primary papers examined

- Forde, M.; Sánchez-Betancourt, L.; Smith, B. *Optimal trade execution for
  Gaussian signals with power-law resilience.* Quant. Finance 22(3), 585–596, 2022.
  https://doi.org/10.1080/14697688.2021.1950919
  PDF: https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26/files/srf55z9197

- Abi Jaber, E.; Neuman, E. *Optimal Liquidation with Signals: the General
  Propagator Case.* Math. Finance, to appear; arXiv:2211.00447 (Nov 2022; v2 Sep 2025).
  https://arxiv.org/abs/2211.00447

- Abi Jaber, E.; Neuman, E.; Tuschmann, S. *Optimal Portfolio Choice With
  Cross-Impact Propagators.* arXiv:2403.10273, March 2024.
  https://arxiv.org/abs/2403.10273

- Abi Jaber, E.; Bondi, A.; De Carvalho, N.; Neuman, E.; Tuschmann, S.
  *Fredholm Approach to Nonlinear Propagator Models.* arXiv:2503.04323, March 2025.
  https://arxiv.org/abs/2503.04323

- Gatheral, J.; Schied, A.; Slynko, A. *Transient linear price impact and
  Fredholm integral equations.* Math. Finance 22(3), 445–474, 2012.
  https://doi.org/10.1111/j.1467-9965.2011.00478.x

- Neuman, E.; Voß, M. *Optimal Signal-Adaptive Trading with Temporary and
  Transient Price Impact.* SIAM J. Financial Math. 13(2), 551–575, 2022.
  arXiv:2002.09549.

- Curato, G.; Gatheral, J.; Lillo, F. *Optimal execution with non-linear
  transient market impact.* Quant. Finance 17(1), 41–54, 2017. arXiv:1412.4839.

### Survey / context

- *Fractional Calculus in Optimal Control and Game Theory: A Survey.*
  arXiv:2512.12111, December 2025. https://arxiv.org/abs/2512.12111

### Underlying technical machinery

- Stein, E. M. *Singular Integrals and Differentiability Properties of Functions.*
  Princeton University Press, 1970.
- Samko, S. G.; Kilbas, A. A.; Marichev, O. I. *Fractional Integrals and
  Derivatives: Theory and Applications.* Gordon and Breach, 1993.
- Chakrabarti, A.; George, A. J. *A formula for the solution of general Abel
  integral equation.* Appl. Math. Lett. 7(2), 87–90, 1994.
- Porter, D.; Stirling, D. S. G. *Integral Equations: A Practical Treatment from
  Spectral Theory to Applications.* Cambridge University Press, 1990.
- Krein, M. G. *Integral equations on a half-line with kernel depending upon the
  difference of the arguments.* AMS Transl. (2) 22, 163–288, 1962.
- Noble, B. *Methods Based on the Wiener-Hopf Technique for the Solution of
  Partial Differential Equations.* Pergamon Press, 1958.
- Wiener, N. *Extrapolation, Interpolation, and Smoothing of Stationary Time
  Series.* MIT Press / Wiley, 1949.

### Fractional control

- Oustaloup, A. *La commande CRONE.* Hermès, Paris, 1991.
- Oustaloup, A.; Levron, F.; Mathieu, B.; Nanot, F. M. *Frequency-band complex
  noninteger differentiator: characterization and synthesis.*
  IEEE Trans. Circuits Syst. I 47(1), 25–39, 2000.
  https://doi.org/10.1109/81.817385

### Empirical propagator origin

- Bouchaud, J.-P.; Gefen, Y.; Potters, M.; Wyart, M. *Fluctuations and response
  in financial markets: the subtle nature of 'random' price changes.*
  Quant. Finance 4(2), 176–190, 2004.
- Gatheral, J. *No-dynamic-arbitrage and market impact.* Quant. Finance 10(7),
  749–759, 2010.
