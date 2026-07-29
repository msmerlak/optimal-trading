# Sketch: the same paper in physics register (theorem-free)

Goal: keep the *content* of `optimal-trading-filters-v2.tex` exactly — same objective, same
factorization, same fractional-derivative result, same recoveries — but write it the way a
physicist would: no Theorem/Lemma/Definition/Assumption environments, results stated inline
in the flow of a derivation, hypotheses demoted to physical provisos, rigor traded for a
picture. This is a natural target here because the impact literature (Bouchaud, Gatheral) is
already half in this register: the "propagator" *is* a response function.

---

## 1. The governing physical picture

Read the objective as a **quadratic action** for the trading path $x(t)$:

$$
S[x] \;=\; \underbrace{\tfrac{\eta}{2}\!\int \dot x^2}_{\text{kinetic}}
\;+\; \underbrace{\tfrac{\lambda}{2}\!\int x^2}_{\text{harmonic well}}
\;+\; \underbrace{\tfrac{\gamma}{2}\!\iint g(t-t')\,\dot x(t)\dot x(t')}_{\text{memory friction}}
\;-\; \underbrace{\int x\,\mu}_{\text{external drive}} .
$$

Its stationary point is a **generalized Langevin equation** (Mori–Zwanzig form): a particle
$x(t)$ in a harmonic well ($\lambda$), with an inertial cost ($\eta$), coupled to a memory
bath through the friction kernel $\gamma g$ (this *is* the transient impact — dissipation with
memory), driven by the force $\mu$. In one line, $N x = \mu$ with inverse susceptibility

$$
\hat n(\omega) \;=\; \eta\omega^2 + \gamma\,\hat g(\omega)\,\omega^2 + \lambda .
$$

The whole paper is then: **find the retarded response of this driven memory-particle** — the
trade may only feel the past of $\mu$. Everything else (Wiener–Hopf, fractional derivative,
EMAs) is the machinery for the retarded Green's function of $N$.

That single reframing removes the need for most of the formal scaffolding: the "adaptedness
constraint" becomes *retardation*, the "friction operator" becomes an *inverse
susceptibility / memory kernel*, and the theorems become *the causal solution of an equation
of motion*.

---

## 2. Translation table (math-finance / theorem → physics)

| Paper (current register) | Physics register |
|---|---|
| Objective / gain–risk–cost functional | Quadratic action $S[x]$; EOM $\delta S/\delta x=0$ |
| Friction operator $N$, symbol $\hat n(\omega)$ | Inverse susceptibility / memory kernel; $\hat n$ = self-energy-like |
| Transient impact, propagator $g$ | Retarded response function / memory-friction kernel (GLE) |
| Adaptedness, optional projection $P_+=\E_t[\cdot]$ | Causality / retardation; keep $t'<t$ |
| "Inverse of projected $\ne$ projection of inverse" | Retardation and inversion don't commute for a kernel with memory |
| Wiener–Hopf factorization $\hat n=\hat n_+\hat n_-$ | Causal square root; analytic split into upper/lower half-plane (Kramers–Kronig / dispersion) |
| Szegő outer function (Lemma/Assumption) | Dispersion relation for $\log\hat n_+$; the causal factor |
| Whitening by $\hat n_+$ | Going to the market's normal coordinates (flat metric / white bath) |
| Theorem: $x^\star=N_+^{-1}P_+N_-^{-1}\mu$ | "We find the retarded response is …" (inline) |
| Wiener–Kolmogorov estimate | Retarded prediction; causal Green's function acting on the drive |
| Fractional integral $I^\nu$ / derivative $D^\nu$ | Anomalous (power-law) response; viscoelastic / anomalous-diffusion memory |
| Nonanticipativity multiplier $\xi^\star$ | Lagrange multiplier enforcing retardation; the "advanced" piece the trader forgoes |
| Gohberg–Krein Volterra factor (finite $T$) | Causal Green's function on an interval with boundary layers |
| Assumption (Friction/Signal), "$\lambda>0$", Szegő cond. | Provisos in passing: "for a well-defined, confined response …" |
| Appendices (Proof of …) | "Computational details" / "Derivation" |

---

## 3. Structural changes

- **No theorem environments.** Results appear as the endpoint of a calculation: "*Minimizing
  the action and imposing causality, we find* $x^\star=\dots$". The two current theorems and
  the projected-inverse lemma become three or four displayed equations inside running text.
- **Hypotheses become physical provisos.** "Under Assumption 1 and $\lambda>0$" →
  "for a confined response (nonzero risk aversion, so the well is real) and a stationary
  drive". The Szegő condition → "provided $\log\hat n$ is integrable, which every kernel here
  satisfies (the power law only marginally, through an integrable log-singularity)".
- **Proofs move inline or to a short 'Derivation' appendix**, written as calculations
  ("completing the square", "closing the contour on the pole at $\omega=-i\theta$"), not as
  QED-terminated arguments.
- **Uniqueness/existence** stated as "the action is convex, so the stationary point is the
  global minimum" — one clause, not a theorem.
- **Section spine unchanged** (factor → predict → combine → power-law → finite horizon →
  recover), because it is already a physicist's narrative.

---

## 4. Illustrative rewrites

### Abstract
> A trader holding a predictive signal must decide how fast to trade against a market that
> pushes back: each trade moves the price with an influence that persists and decays like a
> memory kernel — a propagator. We treat the trading path as the coordinate of a driven
> particle whose action is quadratic, the impact kernel acting as a memory friction and
> causality entering as retardation: the trade cannot use the signal's future. The naive
> stationary point is acausal; the retarded solution follows from a causal square root of the
> kernel — the Wiener–Hopf / spectral factorization familiar from half-space problems and
> Kramers–Kronig. The optimal position is then the retarded response of the whitened signal,
> an explicit convolution filter. For a scale-free, power-law impact $t^{-\beta}$ — the
> empirically relevant case — the filter is a fractional derivative of order $\nu=(1-\beta)/2$:
> an anomalous, long-memory response with no characteristic timescale. The textbook portfolio
> and execution rules emerge as the ordinary-response limits, when the kernel carries a
> relaxation scale.

### The equation of motion and its causal solution (replaces §2.1–§2.3 + theorems)
> If the trader could see the whole path of the drive, the stationary point $\delta S/\delta
> x=0$ would be the naive inversion $x=N^{-1}\mu$. This response is acausal: $N$ has memory, so
> $N^{-1}\mu$ at time $t$ draws on $\mu$ at all times, the future included. Causality forces
> the position to be built from the past alone, $x_t=$ (retarded functional of $\mu_{\le t}$),
> and the constrained stationary point reads $P_+NP_+\,x=\mu$ with $P_+=\E_t[\cdot]$ the
> retarded projection. The obstruction is that inversion and retardation do not commute for a
> kernel with memory.
>
> The resolution is a causal square root. Since $\hat n(\omega)>0$ and grows slowly, it splits
> as $\hat n=\hat n_+\hat n_-$ with $\hat n_+$ analytic and zero-free in the upper half
> $\omega$-plane and $\hat n_-=\hat n_+^{*}$ its lower-half mirror — the same analytic
> separation into retarded and advanced parts that underlies Kramers–Kronig, with $\hat n_+$
> the Szegő function recovered from $\log|\hat n|$ by a dispersion integral. Dividing by
> $\hat n_+$ is a whitening: it carries the friction metric to the flat one, the market's
> normal coordinates, in which the bath is white.
>
> In those coordinates the retarded response is immediate — whiten, keep the retarded part,
> colour back:
> $$ x^\star \;=\; N_+^{-1}\,P_+\,N_-^{-1}\,\mu . $$
> Reading right to left: $N_-^{-1}$ whitens the drive by the friction; $P_+$ discards the
> advanced piece — the unseen future — and replaces it by the forecast; $N_+^{-1}$ propagates
> forward into the position. Equivalently, completing the square writes $S$ as
> $\tfrac12\|x-N^{-1}\mu\|_N^2$, so $x^\star$ is simply the projection of the acausal optimum
> onto causal paths in the metric the friction sets: the retarded (Wiener–Kolmogorov) estimate
> of the whitened signal. For a stationary drive this is a fixed filter, $\hat x^\star =
> \hat n_+^{-1}\,[\hat\psi\,\hat n_-^{-1}]_+$, with $\hat\psi$ the drive's spectral factor and
> $[\,\cdot\,]_+$ the retarded projection on symbols.

### Power-law impact (replaces §3.1)
> A power-law propagator $g(t)=t^{-\beta}$ is scale-free: $\hat g\propto|\omega|^{\beta-1}$, so
> near $\omega=0$ the inverse susceptibility scales anomalously, $\hat n\propto
> |\omega|^{1+\beta}$, with no relaxation rate to set a clock. Its causal square root is a
> fractional power of frequency, $\hat n_+\propto(-i\omega)^{(1+\beta)/2}$, i.e. a fractional
> integral $I^{\nu}$ of order $\nu=(1-\beta)/2$; the optimal rate is its inverse, a fractional
> derivative
> $$ u^\star \;\propto\; D^{\nu}\,(\text{whitened forecast}), $$
> a non-local response weighting the entire past of the signal by $t^{-1-\nu}$ — the trading
> counterpart of viscoelastic creep or anomalous diffusion. The exponent $\beta$ fixes the
> filter's shape by itself; there is no timescale. When instead the kernel has a scale —
> exponential resilience $e^{-\kappa t}$, one relaxation rate — the response is ordinary,
> $\hat n_+$ is rational, and the policy collapses to a handful of exponential moving averages.

### Impact surfing (replaces §3.2)
> Whether the trade follows the signal or turns against it is set by self-interaction. Each
> trade leaves behind its own retarded field — an impact residual — and when the signal
> mean-reverts faster than that field relaxes ($\theta>\kappa$), the optimal rate reverses to
> ride the residual rather than fight it: the trader surfs their own wake. Risk aversion tilts
> the balance the same way. The scale-free kernel has no residual timescale to outlast the
> signal, so there the trade never reverses.

### Recovery (replaces §5, one sentence each)
> Set the memory to zero and the well alone remains: $x=\mu/\lambda$, Markowitz. Add inertia
> ($\eta$) and the response is a single relaxation toward a forecast-weighted target — the aim
> portfolio. One relaxation scale in the bath ($e^{-\kappa t}$) gives one or two exponential
> modes — the resilience filters; a bounded horizon adds start-up and terminal boundary layers
> on the scale of the impact memory — the U-shaped and block-plus-continuous liquidations.

---

## 5. What is gained and what is lost

**Gained**
- A single controlling picture (driven memory-particle / GLE) that makes the fractional
  derivative *expected*, not surprising: anomalous kernel → anomalous response.
- Kramers–Kronig / causal-square-root framing makes the Wiener–Hopf step feel routine.
- "Surfs its own wake", "normal coordinates", "memory friction" carry intuition cheaply.
- Shorter: three theorems + two remarks + assumptions compress to a few displayed equations
  in running prose.

**Lost / made implicit (flag these if precision matters)**
- Exact hypotheses: stationarity, Gaussianity, purely-nondeterministic drive, the Szegő
  integrability condition, and the $\lambda>0$ vs $\lambda=0$ (rate vs position) distinction
  all become passing provisos; a referee in math-finance will want them back.
- The domain on which the unbounded power-law factors act (the dense-domain caveat in App. A)
  disappears into "the fractional operator".
- Uniqueness/measurability of the optimal control (optional projection, admissibility class)
  is reduced to "convex, so unique".
- The nonanticipativity multiplier's status as a *bona fide* Lagrange multiplier
  (Rockafellar–Wets) becomes a heuristic "advanced piece forgone".

**Verdict.** The physics register is a faithful and often clarifying re-encoding of *this*
paper because the object really is a linear-response / memory problem. It suits a
*Physical Review E / Quantitative Finance*-style physics audience. For a
*Mathematical Finance / Finance & Stochastics* audience keep the theorem-form; a hybrid —
physicist's narrative in the body, a short "Assumptions and precise statements" box or
appendix — captures most of the intuition without losing the rigor the current draft has.
