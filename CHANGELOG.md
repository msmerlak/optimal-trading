# Optimal Trading & Fractional Derivatives — Lab Notebook

## 2026-06-28 (afternoon) — Novelty audit + repositioning vs. FSS2022

### Trigger
Literature-review request: how novel is the bulk Riesz-on-forecast formula
$u^{\rm bulk}_t = \kappa_{1-\gamma}\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$?

### Finding
The structural fractional-operator insight is **already in Forde–Sánchez-Betancourt–Smith
(2022)** Theorem 2.2 proof: they factorize the bounded-interval Fredholm operator as
$T = B^{-1} I_\nu B$ where $I_\nu$ is the Riemann–Liouville operator of order $r=(1-\gamma)/2$.
This is the operator-language form of our §4.3 multiplicative Wiener–Hopf factorization
$\mathbb{D}^{1-\gamma}=D_+^\beta D_-^\beta$ with $\beta=r$, conjugated by the bounded-interval
weight $B$. The Riesz-on-$\mathbb{R}$ form is a presentational re-organization, not a new
mathematical theorem.

Genuinely novel contributions:
1. Riesz-on-$\mathbb{R}$ presentation (no bounded-interval weight conjugation).
2. Forecast curve $\bar\alpha(t,\cdot)$ as a named explicit object the operator acts on.
3. Bulk/boundary spine as unifying organization.
4. CRONE / fractional-PID bridge — not in the execution literature; the December 2025
   fractional-control survey (arXiv:2512.12111) does not cover optimal execution.
5. Domain-level distinction between bulk-symbol W–H (on $\mathbb{R}$) and augmented-symbol
   W–H (on $[0,\infty)$).

### Artifacts
- `outputs/bulk-fractional-forecast-novelty.md` (final review, 19.8 KB)
- `outputs/bulk-fractional-forecast-novelty.provenance.md`
- `outputs/.drafts/bulk-fractional-forecast-novelty-research-evidence.md`
- `outputs/.plans/bulk-fractional-forecast-novelty.md`

### Paper changes (`papers/fractional-derivative-optimal-execution.md`)
- **§1.2 Contributions** — item 1 softened to acknowledge FSS2022 operator-language
  equivalent of the half-order Riemann–Liouville factorization; reorganized into 9
  items (was 7) by inserting new bullets on (2) bulk-symbol W–H factorization and
  (9) execution-CRONE bridge as separately listed contributions.
- **§1.3 Related work** — promoted FSS2022 to a dedicated "closest prior art"
  paragraph at the top; added paragraph on fractional-control / CRONE literature
  with the cross-field-bridge novelty claim; reframed the explicit-contribution
  paragraph as "presentation + unification + cross-field bridge" rather than
  "new mathematical theorem".
- **§4.1** — added **Remark 4.1.1 (attribution)** right after the boxed Theorem 4.1
  statement, attributing the structural content to FSS2022 Theorem 2.2 proof and
  citing the W–H factorization to SKM 1993 / Krein 1962 / Noble 1958 / Porter–Stirling 1990.
- **§6.3** — split into two subsections: new §6.3 "Forde–Sánchez-Betancourt–Smith (2022)
  [closest prior art]" and renamed §6.4 "Abi Jaber–Neuman / AJNT / Abi Jaber et al."
  Renumbered §6.4–6.6 → §6.5–6.7 and updated cross-references throughout (§2.5, §4.6
  closing remark, §5.3 GP-pointer footnote, §6.7, §9.2 open-problems list, v2 changelog).

### Verification
- `grep -n "^### 6\." papers/fractional-derivative-optimal-execution.md` confirms clean
  §6.1–§6.7 numbering.
- `grep -n "§6\." papers/fractional-derivative-optimal-execution.md` confirms all cross-
  references updated (no stale §6.3 = AJN references; §6.4 = AJN, §6.5 = GP, etc.).
- Files exist on disk: `outputs/bulk-fractional-forecast-novelty.md` (19,843 bytes),
  provenance (7,178 bytes).

---

## 2026-06-28 — Forecast-curve substitution: rigorize §2.3 + Theorem 4.1 proof

### Trigger
Peer review of the $\alpha\to\bar\alpha$ substitution argument flagged the original
§2.3 closing paragraph and Theorem 4.1 proof as hand-wavy (see
`outputs/forecast-curve-substitution-review.md`).

### Concrete issues identified
- §2.3 sentence "Inverting the kernel symbol produces a solution in which $\alpha_s$
  is replaced for $s>t$ by $\bar\alpha(t,s)$" was a non-sequitur: $(\star_{\rm bulk}^{\mathcal{F}})$
  has only $\alpha_t$ on the RHS, no $s$-variable to replace.
- Theorem 4.1 proof "Fourier-transform in $s$" of a FOC whose variables are $t$ and $v$.
- LQ certainty-equivalence ansatz used implicitly without being stated.
- Forecast tower property $\mathbb{E}_t[\bar\alpha(v,s)]=\bar\alpha(t,s)$ used implicitly,
  never stated or proved.
- Sufficiency / uniqueness in the adapted class not established.

### Changes to `papers/fractional-derivative-optimal-execution.md`
- **§2.3**: replaced the "Stochastic FOC and emergence of the forecast curve" closing
  block (one paragraph + three FOCs) with three explicit subsections:
  (1) **Stochastic FOC** — derives the conditioned FOCs from the Gâteaux derivative
      against adapted variations + tower property of conditional expectation;
  (2) **Forecast tower lemma** — stated as a lemma with three-case proof;
  (3) **Candidate policy and emergence of the forecast curve** — explicit
      certainty-equivalence ansatz $(\sharp)$, derivation that the candidate
      satisfies the conditioned FOC, sufficiency via strict convexity on
      $L^2_{\rm adap}$, pointer to Bensoussan / Kwakernaak–Sivan / Abi Jaber–Neuman.
- **§4.1 proof**: rewritten to flow from the candidate $(\sharp)$ and the forecast
  tower lemma; Fourier inversion is now performed on the (deterministic, $\mathcal{F}_t$-
  measurable) function $\bar\alpha(t,\cdot)-\lambda$ in the $s$-variable that actually
  appears there. Closes with strict-convexity uniqueness on $L^2_{\rm adap}$.
- **§4.2 first paragraph**: "as derived in §2.3 (closing remark)" → "as derived in §2.3
  via the forecast tower lemma and the candidate $(\sharp)$."

### Artifacts
- Review: `outputs/forecast-curve-substitution-review.md`
- Evidence notes: `outputs/.drafts/forecast-curve-substitution-review-evidence.md`
- Plan: `outputs/.plans/forecast-curve-substitution-review-plan.md`

### Verification
- Edits applied via targeted block-replacements; reread §2.3 (lines 124–158) and
  §4.1 (lines 234–243) on disk to confirm. New equation tag $(\sharp)$ defined in §2.3
  is referenced in §4.1 proof and §4.2 opener.
- Final formula unchanged: $u^{\rm bulk}_t = \kappa_{1-\gamma}\mathbb{D}^{1-\gamma}(\bar\alpha(t,\cdot)-\lambda)(t)$.
  Numerical experiments in `experiments/riesz_split_check.py` and `ar1_433_vs_436.py`
  remain valid (they verify symbol-level identities of the formula, not the derivation).

### Outstanding
- Bensoussan 1992 and Kwakernaak–Sivan 1972 are cited inline but not yet added to the
  references list (need to check whether the paper has a formal bibliography section).
- Abi Jaber–Neuman pointer in §6.3 already exists; pointer from §2.3 added inline.

---

## 2026-05-30 — Gap-fill pass

### What was done
- Ran alpha CLI searches (agentic + semantic) and 6 web_search queries to find newer 2024–2026 papers
- Added **18 new references** (total now 46, up from 28)
- Added **6 new sections**: §3.3 (discretized fBm arbitrage), §5.4 (unified theory), §5.5–5.6 (signature methods), §8 (market making under rough vol), §9 (RL for fractional execution)
- Expanded §6 from 3 to 8 subsections (market resistance, multi-asset cross-impact, DeFi, liquidity uncertainty, game theory)
- Expanded §7 with multivariate Volterra Merton (Dro & Gnabeyeu 2026) and mean-variance under rough vol (Gnabeyeu 2026)
- Updated open questions: 4/6 original questions now partially/fully addressed, 3 new questions added
- Updated provenance file with full search log and verification

### Key new papers
- **Muhle-Karbe, Rosenbaum et al. (2026, 2601.23172)** — Unified theory connecting H₀ to rough vol + power-law impact. Most impactful single addition.
- **Abi Jaber, Neuman & Tuschmann (2024, 2403.10273)** — Multi-asset cross-impact with Volterra propagators. Fills the multi-asset gap.
- **Rosenbaum & Zhang (2212.10164)** — Market making under quadratic rough Heston. Fills the market-making gap.
- **Micheli & Monod (2024, 2410.13493)** — Deep RL for execution with general decay kernels. Fills the RL gap.

### What's still missing
- No experiments/simulations run
- No paper draft beyond the lit review
- Secondary references (Kumar 2012, Kaur 2023, Bennedsen 2017) still not in reference list
- Open-source tool URLs not verified

## 2026-05-30 — Companion note + paper expansion

### What was done
- Wrote companion synthesis note `outputs/trading-duality-extensions.md` exploring implications, generalisations, and connections of the Wiener–Hopf optimal-trading framework: LQG separation, no-arbitrage power-law impact, matrix Wiener–Hopf, rate–distortion / predictive information, MFG crowding, ML baselines. Provenance: `outputs/trading-duality-extensions.provenance.md`.
- Added two new subsections to `papers/noisy-signal-impact-trading.md`:
  - **§5.5 "Markov closure of the future integral"** — re-derives the AR(1)×exponential scalar collapse (eq. 10) via $\mathbb{E}[f_{t+m}|\mathcal F_t]=\rho^m f_t$, gives the general identity $[K_-^{-1}f]_+(t)=\hat K_-^{-1}(\rho)\,f_t$ (eq. 12c), and extends it to AR($p$) (sum over characteristic roots) and finite-state Markov (matrix expression $\hat K_-^{-1}(\mathbf P)$). Identifies where closure fails (fBm, hidden-Markov switching).
  - **§6.3 "Closed-form constants for AR/OU × power-law kernels"** — derives explicit constants for the power-law case: continuous-time OU × power-law gives $\kappa^{(1-\beta)/2}$ via Frullani-type integral $\int_0^\infty s^{-\alpha-1}(e^{-\kappa s}-1)\,ds=\Gamma(-\alpha)\kappa^\alpha$ (eq. 15b); discrete fractional differencing × AR(1) gives $(1-\rho)^\alpha$ via the generalised binomial theorem (eq. 15c); notes the Lerch/polylog regime for literal discrete power-law kernels (eq. 15d).
- Updated §8.2 (power-law + OU example) to display the explicit $\kappa^\alpha$ constant; updated §8.3 comparison table; tightened limitation #5 in §10 to reflect the Markov-closure generalisation.
- Added references: Granger–Joyeux 1980, Hosking 1981, Nuzman–Poor 2000.
- Wrote `experiments/markov_closure_check.py` and ran it; output saved to `experiments/results/markov_closure_check.out`. Both closures verified: discrete to ~7 decimal places, continuous to high precision in mid-range (integrator-limited near endpoints, but identity $\int u^{-\alpha-1}(e^{-u}-1)du = \Gamma(-\alpha)$ is standard).

### Open
- Discrete *literal* power-law kernel constant (eq. 15d) only sketched; full Lerch/polylog evaluation deferred.
- Empirical PnL test of the (15b)/(15c) closed forms vs the operator-resolvent solution of Abi Jaber–Neuman still not run.
- Companion note (`trading-duality-extensions.md`) lists eight conjectures and six open puzzles — none yet pursued.

## 2026-05-31 — Review of noisy-signal impact trading draft

### What was done
- Created required review artifacts:
  - `outputs/.plans/noisy-signal-impact-trading-review-plan.md`
  - `outputs/.drafts/noisy-signal-impact-trading-review-evidence.md`
  - `outputs/noisy-signal-impact-trading-review.md`
- Reviewed local draft `papers/noisy-signal-impact-trading.md` with `researcher` and `reviewer` subagents.
- Ran `python3 experiments/markov_closure_check.py`; discrete fractional-difference grid check matched, while continuous integral quadrature remained crude near endpoints.
- Used alpha CLI and fetched primary source pages for GP13, Lehalle–Neuman, Abi Jaber–Neuman, AJN–Tuschmann, and Forde/Sánchez-Betancourt et al.

### Main review findings
- Strongest contribution: self-contained stationary Wiener–Hopf/filter exposition and AR(1) × exponential scalar-collapse/kernel-innovation rule.
- Critical issue: §4's unweighted projection FOC is inconsistent with §2.3's `S_f`-weighted stochastic filter objective unless projection is redefined carefully.
- Major revision needed for power-law exactness, novelty narrowing, noisy-case heading, GP13 positioning, and table status labels.

## 2026-06-17 — Tradeability definition note

- Wrote `notes/tradeability-definition.md` (~130 lines, 9.7KB) proposing a layered definition of signal tradeability built from the info-thermodynamic framework.
- Layers: (0) naive $I(\alpha; r)$ — incomplete; (1) **spectral tradeability density** $\tau(\omega) = T_{\mathrm{market}}(\omega) q(\omega) = S_\alpha^2 / [2\,\mathrm{Re}\hat G \cdot (S_\alpha + S_\xi)]$ with scalar $\mathcal{T}_1 = \int \tau\, d\omega/(2\pi)$; (1.5) Lehalle–Neuman exact $\mathcal{T}_\infty = \sup_K \dot \Pi$; (2) **rate-distortion curve** $\mathcal{T}(\dot I_{\max})$ tradeoff between directed-info budget and P&L; (3) two scalar summaries: ceiling $\mathcal{T}_\infty$ and exchange rate $\mathcal{T}'(0)$, with $\dot I_{\mathrm{half}} = \mathcal{T}_\infty/(2\mathcal{T}'(0))$ as bits-per-half-alpha.
- Includes comparison table mapping conventional definitions (IC, Sharpe-after-cost, signal-to-cost, capacity, half-life-adjusted IR) onto the framework as projections.
- Falsifiable prediction stated: across signals in same market, $\mathcal{T}(\dot I)$ curves should be concave with origin slope matching $\int T_{\mathrm{market}} q^\star d\omega/(2\pi)$.

## 2026-06-17 — Two-information bound + stationary OU+exponential extension

### What was added
- Restructured `papers/info-thermodynamics-trading.md` (~520 lines) to introduce **two distinct mutual informations**:
  - $I(\alpha; r)$ — signal quality (information signal carries about realized return)
  - $I(u; \alpha)$ — extraction efficiency (information trade uses from signal)
- Key new result (§4): for Gaussian Markov chain $r-\alpha-u$,
  $$\Pi_{\max} = \frac{\sigma_r^2}{2\lambda}\bigl(1 - e^{-2I(u;\alpha)}\bigr)\bigl(1 - e^{-2I(\alpha;r)}\bigr) = \frac{\sigma_r^2}{2\lambda}\bigl(1 - e^{-2I(u;r)}\bigr).$$
  Two-factor product structure cleanly separates exogenous signal quality from endogenous policy efficiency. Bilinear in both informations in the small-information limit.
- Underlying correlation-chain identity for Gaussian Markov chain: $\rho_{u,r}^2 = \rho_{u,\alpha}^2 \rho_{\alpha,r}^2$, equivalently $1 - e^{-2I_{ur}} = (1-e^{-2I_{u\alpha}})(1-e^{-2I_{\alpha r}})$.
- Verified `experiments/info_thermo_trading_two_info.py`: across 27 parameter combinations, empirical $\rho_{u,r}^2$ matches the product formula within sampling noise; Monte Carlo P&L matches the two-factor envelope; zero violations across 1000-policy grid sweep.

### Stationary OU + exponential propagator (§6)
- Closed form for spectral trading temperature:
  $$T_{\mathrm{market}}(\omega) = \frac{\gamma \sigma_\alpha^2}{\lambda \rho} \cdot \frac{\omega^2 + \rho^2}{\omega^2 + \gamma^2},$$
  with $T(0)/T(\infty) = \rho^2/\gamma^2$ controlling which frequencies are "hot."
- Conjecture: spectral two-factor bound $\dot\Pi \leq \int T_{\mathrm{market}}(\omega) q(\omega) (1 - e^{-2 dI_{u\alpha}(\omega)}) d\omega/(2\pi)$ by band-by-band application of §4. Proof requires showing band-optimal $K$ assembles into causal transfer function — not done; reduction to Tanaka–Esfahani–Mitter 2018 is the path.
- Closed-form unconstrained-extraction envelope (eq. 9) via partial fractions. Diverges as $\sigma_\xi \to 0$, confirming this envelope is information-saturated rather than impact-optimal; the genuinely useful bound needs MI-vs-impact tradeoff.

### Deferred
- `experiments/info_thermo_trading_OU_propagator.py` drafted but sweep hangs (large frequency grid x parameter sweep). Needs rewrite with adaptive integration. Numerical comparison of a causal one-pole filter against the spectral envelope is the natural next experimental check.

## 2026-06-17 — Information-thermodynamic bound on alpha capture in optimal execution

### What was done
- Drafted `papers/info-thermodynamics-trading.md` (~480 lines) developing the Sagawa–Ueda-style information-thermodynamic bound for propagator-impact optimal execution. Key result: in the one-step Gaussian model, the maximum expected net P&L at fixed mutual information $I$ between trade and signal is
  $$\Pi_{\max}(I) = \frac{\sigma^2}{2\lambda}(1 - e^{-2I})$$
  with tangent bound $\Pi \leq T_{\mathrm{market}} \cdot I$ where $T_{\mathrm{market}} = \sigma_\alpha^2/\lambda$ (signal-variance / impact-coefficient).
- Verified numerically in `experiments/info_thermo_trading_one_step.py`: Monte Carlo matches theory across 7 values of $I$ from 0.05 to 4; grid sweep of 900 random policies finds zero violations of the envelope.
- Literature placement: Touzo–Marsili–Zagier 2021 (arXiv:2010.01905) prove an analogous bound for the Glosten–Milgrom microstructure model (informed-trader vs. market-maker); Ducuara et al. 2023 PRL extend to expected-utility. Neither paper covers continuous-time propagator-impact execution — that's the gap this note partially fills.
- Stationary continuous-time extension stated as conjecture (4)–(5): the bound should generalize spectrally to $\dot{\Pi}^{\max} \leq \int T_{\mathrm{market}}(\omega) \cdot d\dot I(\omega) \frac{d\omega}{2\pi}$ with $T_{\mathrm{market}}(\omega) = S_\alpha(\omega) / (2\,\mathrm{Re}\,\hat G(\omega))$. Proof strategy: reduce to Tanaka–Esfahani–Mitter 2018 LQG-with-directed-information framework. Not yet completed.

### Key derivation step
For randomized policy $u = a\alpha + s\varepsilon$, $\varepsilon \sim N(0,1)$ indep, fix $I = \frac{1}{2}\log(1 + a^2\sigma^2/s^2)$. Optimize $\mathbb{E}[u\alpha - \frac{1}{2}\lambda u^2]$ over $(a, s)$ at fixed $I$ by parametrizing $a$ in terms of SNR and $s^2$, then optimizing $s^2$ — closed form gives the envelope above. Algebra is elementary; the cleanness is from the Gaussian channel formula on the information side.

### Useful clarification surfaced
The entropy-regularized / MaxCal Gibbs policy $dQ^\star \propto e^{-\beta J} d\mu_0$ is **not** information-optimal at finite $\beta$ — it traces a one-parameter sub-curve of the envelope $\Pi_{\max}(I)$. The information-optimal policy at given MI budget is the one identified by direct optimization (§3.3 of the note). I have not seen this distinction made explicit in the entropy-regularized-RL-for-execution literature.

### Open
- Stationary conjecture not proved. Estimated 1–2 weeks of focused work to reduce to Tanaka–Esfahani–Mitter.
- Worked OU-signal + exponential-propagator example not done.
- Practical interpretation thread — connecting MI budget to real execution constraints (latency, signal-to-noise, quantization) — stated but not developed.

## 2026-06-17 — Literature review: adapted convex optimization and physics

### What was done
- Wrote literature review `outputs/adapted-convex-optimization-physics.md` (819 lines, 13 sections) covering eight physics clusters as instances of the adapted-convex skeleton: (1) causality/dispersion (Kramers–Kronig as Hardy-space factorization, Toll 1956, Titchmarsh's theorem); (2) FDT/Kubo; (3) Wiener–Hopf's physics origins (Milne radiative-transfer problem, Sommerfeld diffraction, neutron transport); (4) path-integral stochastic control (Onsager–Machlup, Kappen, Todorov); (5) quantum filtering (Belavkin, Bouten–van Handel–James); (6) stochastic thermodynamics & maximum caliber (Seifert, Pressé–Ghosh–Lee–Dill); (7) JKO / Wasserstein gradient flows + adapted OT; (8) Freidlin–Wentzell / Macroscopic Fluctuation Theory.
- Workflow: plan → `researcher` subagent → synthesized draft → `reviewer` subagent for combined citation + content review.
- Reviewer caught **3 FATAL** issues (same pattern as last review): arXiv:math-ph/0404070 misattributed to Welters–Avniel–Johnson (actual: Figotin & Schenker 2004); arXiv:2604.17058 given fabricated title + invented author triple (actual: Liu 2026, single author); direct quotation attributed to arXiv:2604.17058 fabricated (replaced with verbatim abstract excerpt). Plus 5 MAJOR ("first physics-side" overclaim, "no paper unifies all eight" hard negative, non-demolition → nest overclaim, Arveson-not-invoked overclaim, vH05 attribution missing co-author Bouten). All FATAL + 5 MAJOR fixed surgically and verified on disk via grep.
- Provenance written to `outputs/adapted-convex-optimization-physics.provenance.md`.

### Key findings of the review itself
- Causal linear response (cluster 1) is *literally* the L² projection onto the past; the response function is *literally* an outer H² function; Kramers–Kronig is *literally* the Hilbert-transform relation that this analyticity entails. The convex-optimization framing is missing from physics canonicals (Toll, Titchmarsh) but present in passivity / Herglotz–Nevanlinna formulations (Figotin–Schenker, Gralak).
- Wiener–Hopf (cluster 3) was originally a physics technique (Milne 1921 → Wiener–Hopf 1931 radiative-transfer paper). The factorization on a half-line is exactly the operation the abstract skeleton requires inside a nest algebra. The math abstraction (Krein, Gohberg, Arveson, Davidson) developed in operator algebras away from physics and was never re-imported under a unifying banner.
- Quantum filtering (cluster 5) is the noncommutative analogue of Kalman; only Bouten–van Handel–James 2007 and Gupta–Hota 2015 explicitly draw the analogy. Arveson-style nest-algebra factorization in the noncommutative-L² setting is a natural bridge not located in this survey.
- Genuine cross-discipline gap: no physics paper applies bicausal / adapted Wasserstein gradient flow (Acciaio–Backhoff–Zalashko, Eckstein–Pammer, Beiglböck–Pammer–Schrott) to entropy production or non-equilibrium fluctuations. The natural realization — an adapted JKO scheme for Bertini–Jona-Lasinio MFT density–current pair — does not exist.

### Pattern note (worth recording)
- This is the *second* consecutive literature-review session in which the reviewer pass caught fabricated quotations and misattributed URLs inherited from the researcher subagent brief. Same class of error both times: plausible quotations / titles / authors that were never verified against the cited URL. Recommendation: instruct researcher subagent to either (a) fetch and quote verbatim with line numbers, or (b) paraphrase explicitly rather than produce direct-quote marks.

### Open / unresolved
- Several quoted excerpts (Toll 1956 body, PGLD 2013, Kubo 1957, Bach–Dürr 1978, Meister–Speck 1980, Hoffmann-Jørgensen 2014, Gupta–Hota 2015, Dixit 2018, Grafke 2021) match the brief's reported text but were not verifiable in the reviewer's spot-check session due to 403s / PDF stubs. Listed explicitly in provenance.
- Exhaustiveness caveat (§11.4 of the review): Belavkin's collected works, Barchielli–Gregoratti monograph, Powers/Muhly on noncommutative nests, and math-finance filtration-projection literature were NOT searched. Any of these could change the "unifying paper not found" conclusion.
- No second reviewer pass run after fixes (fixes were citation-level + hedging, not structural).

## 2026-06-17 — Literature review: convex duality inside a nest as the general structure of causality

### What was done
- Wrote literature review `outputs/convex-duality-nest-causality.md` (~808 lines, 12 sections) surveying seven clusters: nest algebras (Arveson, Davidson, Anoussis–Katsoulis); prediction (Wiener–Hopf, Kolmogorov–Szegő); Kalman/innovations; optimal trading with transient impact; adapted/causal OT (Backhoff et al.); causal information theory (Massey, Tanaka–Esfahani–Mitter); martingale duality in math finance (Kramkov–Schachermayer).
- Workflow: plan → `researcher` subagent for wide sweep → synthesized draft → `reviewer` subagent for combined citation + content review.
- Reviewer caught **3 FATAL** issues (Tourneret-Bercher-Doncarli misattribution → really Picinbono–Bouvet 1987; Sch07 URL → really Czichowsky–Schachermayer 2015; fabricated AN22 abstract quote that conflated AN22 with LN19). All FATAL fixes applied surgically and verified on disk via grep. MAJOR/MINOR fixes (CS15 quote correction, Daughtry–Johns dangling reference, TM09/Kra03 sources entries, Arveson p. 209 imprecision) also applied.
- Provenance written to `outputs/convex-duality-nest-causality.provenance.md`.

### Key findings of the review itself
- The skeleton (convex $J$ on Hilbert space + nest constraint + outer factorization in the nest algebra) is real but informal: each cluster instantiates it in its own dialect, but **no published 2010–2026 paper or survey proposes nest algebras as a unifying programme across all seven clusters**.
- Cleanest non-finance instantiation: bicausal optimal transport (Backhoff–Bartl–Beiglböck–Eder 2024/25 give explicit Kantorovich duality restricted to filtration-respecting couplings).
- Cleanest match to the abstract FOC for optimal trading: Lehalle–Neuman 2019 (stochastic Fredholm equation FOC), not AN22 (which uses stochastic-control + BSDE + operator Riccati language).
- Open: "proximal Wiener–Hopf" for non-quadratic convex $J$; CSL-algebra extension for partially ordered information (multi-agent / bicausal); nest factorization for rough-vol / Volterra Hessians.

### Open / unresolved
- Three references retain explicit *unverified* markers: Ringrose 1965 pagination, TM09 / Kra03 volume info, Daughtry–Johns full citation.
- No second reviewer pass run after fixes (fixes were citation-level, not structural).
- The unifying view itself remains the reviewer's framing, not a published programme — flagged in the front-matter Status box and §10.5.

## 2026-06-17 — Unifying draft: adapted convex duality

### What was done
- Wrote `papers/adapted-convex-duality.md` — a position-paper draft taking a general view: Wiener–Hopf prediction, Kalman filtering, and optimal trading (transient impact) are three instances of the same skeleton: minimize a convex functional $J$ on a Hilbert space $H$ subject to the constraint that the solution respect a nest $\{H_t\}$ (filtration / chain of subspaces).
- Core abstract program (P) and FOC: $P_+\nabla J(u^\star)=0$, i.e. the gradient at the constrained optimum has no causal component (abstract Wiener–Hopf equation).
- Adapted normal equation ($\star$): $u^\star = A^{-*}P_+(A^{-1}b)$ where $K=AA^*$ is an *outer factorization inside the nest algebra* $\mathcal{T}(\mathcal{N})$ (Arveson 1975, Davidson 1988). Cholesky, innovations/Kalman, and Kolmogorov–Szegő/WH are three avatars.
- Side-by-side dictionary (Table 1) mapping abstract objects to the three instances.
- Taxonomy of what survives the skeleton (matrix WH, LQG separation, GP13, adapted Wasserstein), what deforms (rough vol → fractional factor, Volterra → operator Riccati, HMM signals), and what breaks (non-convex $J$, non-Gaussian filtering, MFG crowding, inequality constraints).
- Five conjectures including: adapted proximal duality (forward–backward splitting as a non-quadratic generalization of WH), information-theoretic interpretation of the anticausal multiplier $\mu^\star$ as wasted look-ahead, and convex-only separation principle.

### Open
- No proofs of new statements — this is a position paper, all concrete facts cite the literature.
- Conjectures §6.1–6.5 are speculative; none yet attempted.
- Have not verified the precise hypotheses under which Arveson/Larson outer factorization in a general nest algebra applies to the rough-vol / Volterra Hessians cited in §5.2.
- Cross-references to `outputs/trading-duality-extensions.md` and `outputs/wiener-hopf-riccati-connection.md` are asserted but the consistency of notation across the three documents has not been re-checked.

## 2026-06-01 — Appendix of definitions and proofs

### What was done
- Added **Appendix A (Definitions, 9 entries)** and **Appendix B (Proofs, 8 theorems)** to `papers/noisy-signal-impact-trading.md` between §11 and `## Sources`.
- B.1 PD⇔no-dyn-arb, B.2 Legendre–Fenchel, B.3 Wiener–Hopf FOC, B.4 Szegő factorisation, B.5 Markov-closure scalar identity (eq. 12c, only original theorem), B.6 Γ(−α)κ^α (eq. 15b), B.7 (1−ρ)^α (eq. 15c), B.8 denoise-then-trade separation (§7.3).
- Re-ran `experiments/markov_closure_check.py`; discrete identity matches to 6+ decimals.
- Paper grew 596 → 807 lines; no new bibliography entries (all 8 citations use existing Sources block).
- Provenance: `papers/noisy-signal-paper-appendix.provenance.md`. Plan: `outputs/.plans/noisy-signal-paper-appendix.md`.
