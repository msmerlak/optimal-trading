# Evidence notes — v2-tone-humility review

Source: `v2/optimal-trading-filters-v2.tex` (line numbers from grep, this session).
Method: pattern inventory by grep + reading the surrounding sentences.

## Harvested passages (quoted, with line numbers)

### Verdict sentences / grand definite articles
- L64: "Adaptedness, the requirement that $u_t$ be measurable with respect to the
  information $\F_t$, **becomes the operative constraint**. It is **a constraint of an
  unusual kind**: a closed subspace of $L^2$ cut out by an increasing family of
  $\sigma$-algebras." — user's named example. Double verdict + self-important gloss.
- L71: "the inverse of a projected operator is not the projection of the inverse,
  **precisely because** $Q$ is non-local." — "precisely because" = pronouncement.
- L60: "the optimum would be **the single operator inversion** $u=Q^{-1}\alpha$".
- L232: "the whole forecast curve entering through **the single number** $\rho$".
- L333: "the terminal inventory constraint and the two boundaries of the window are
  **precisely what the stationary theory omits**."

### Epigram / punchline cadence (sentence-final mic-drops)
- L272: "its influence decays on **the single timescale** $1/\kappa$ **and is then
  forgotten**... the influence **carries no timescale** and decays only algebraically."
- L276: "**Short-memory impact produces a short-memory policy; long-memory impact
  produces one that never fully forgets.**" — the purest aphorism in the paper.
- L377: "The rate carries white noise, the position jumping to its target, **the
  singularity any impact term regularizes**."
- L258: "**The memory is maximal**: the Marchaud representation weights past signal
  increments by the slowly decaying kernel..."
- L251: "each instant is a separate problem, and **adaptedness is free** since the
  signal is already observed."
- L290: "As $\beta\to1$... **adaptedness becomes free**...; as $\beta\to0$... adaptedness
  **destroys the value**."

### Absolutes where hedges are human
- L312: "Positions never reverse; the rate reverses **exactly when** $2c_1\Phi(\theta)>1$."
  (This one is EARNED — it is the content of Prop 2, proved + verified. Keep.)
- L319: "the optimal rate instead runs against the signal **to ride that residual**" +
  L328 "the trader's own transient-impact **wake**" — vivid metaphors, twice.
- L347: "The identity \eqref{eq:pi} requires the causal factor on the right, which
  **pins/forces** the anchoring" (L226 "forces the profile to be exponential" — earned,
  it's a tower-property derivation; L347 "forces" okay but part of the pattern density).

### Triads and dramatic parallel structure
- Abstract + §2.2: "anticausally whiten the forecast curve, project, causally color"
  (three-beat incantation; appears at least twice).
- §1.3: "These three names describe a single object seen at different levels of
  structure" — oracular register.
- L333: "a broker must work a parent order over a trading session, or liquidate an
  inherited position by a deadline, ending flat, $x_T=0$" — cadenced triple.

### Zero-hedge / zero-person register
- The entire paper contains no "we" outside "We solve" (abstract) — the passive/
  impersonal register plus verdict sentences is what produces the oracle effect.
  Occasional "we" and an honest hedge ("in the cases we can compute", "at least for
  the kernels considered here") would humanize without weakening theorems.

## Earned vs unearned confidence (calibration)
- EARNED (keep declarative): Lemma 1, Thms 1–2, Props 1–3 statements; "exactly when
  $2c_1\Phi>1$" (proved); $\sin(\pi\beta/2)$ claims (proved + verified 9/9 suite);
  "the Riccati closed-loop poles equal $b_1,b_2$" (verified to 1e-16).
- UNEARNED/INTERPRETIVE (soften): "operative constraint" verdict; "constraint of an
  unusual kind"; "precisely because"; "memory is maximal"; "adaptedness is free /
  destroys the value" (limits: fine as limits, but stated as moral verdicts);
  "never fully forgets"; "is then forgotten"; "precisely what the stationary theory
  omits"; the whiten-project-color incantation used twice.

## Density measurement (why it reads LLM-generated)
Rough count: ~14 punchline-final sentences in ~11 pages of prose — more than one per
page. Human applied-math papers land perhaps 2–3 per paper (typically in intro and
conclusion). The issue is density and uniformity of the cadence, not any single line.

## Sources
- v2/optimal-trading-filters-v2.tex (primary; grep line numbers above)
- outputs/optimal-trading-filters-v2-review.md (prior substance review; no overlap)
- reviews/v2-style-review.md (prior style review — covered AGENTS.md prohibitions,
  which are a different axis: that review found no rhetorical questions/throat-clearing;
  the present tics are compatible with those rules yet still read machine-generated)
