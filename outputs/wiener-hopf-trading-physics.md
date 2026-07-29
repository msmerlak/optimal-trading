# Physics Literature Fit: Optimal Trading via Wiener-Hopf

**Slug:** `wiener-hopf-trading-physics`  
**Date:** 2026-07-18  
**Question:** Which physics journal/tradition would best digest a physics-format rewrite of the paper *Optimal Trading Filters: a Wiener-Hopf Approach* (Smerlak, CFM)?

---

## 1. The paper's technical fingerprint

The paper solves an exactly solvable stochastic optimization problem:

$$\max_{u \in L^2_{\rm adap}} \mathbb{E}\int u_t \alpha_t \,dt - \tfrac{\gamma}{2} \mathbb{E}\iint G(|t-v|) u_t u_v \,dt\,dv$$

The cost operator $C$ (convolution against the impact kernel $G$) has symbol $\hat C(\xi) = c_\beta |\xi|^{\beta-1}$ for the empirically observed power-law kernel. The adaptedness constraint (the trader cannot use future information) couples the Euler–Lagrange equation to a causality structure. The key results are:

- **Whole line:** The adapted optimal rate is $u^\star = \gamma^{-1} C_+^{-1} P_+ C_-^{-1} \alpha$, with $C = C_- C_+$ the Wiener–Hopf causal-anticausal factorization.
- **Power law:** The factors are Marchaud fractional integrals of order $\nu = (1-\beta)/2$; the closed form collapses to $u^\star_t = \kappa_{1-\beta} D_+^\nu (D_-^\nu \bar\alpha(t,\cdot))(t)$ — a fractional derivative of order $1-\beta$ of the forecast curve.
- **Finite horizon:** The Gohberg-Krein weight-conjugated version converges to the bulk formula at rate $O(d(t)^{-\nu})$ in the interior.

This combination — quadratic variational problem, power-law memory, causality constraint, exact Wiener-Hopf factorization, fractional-derivative closed form — maps onto at least three distinct physics traditions. They are not equally good fits.

---

## 2. Four physics traditions that use these tools

### 2.1 Econophysics / statistical mechanics of financial markets

**Journals:** *Journal of Statistical Mechanics: Theory and Experiment* (J. Stat. Mech., IOP/SISSA); *Physica A* (Elsevier); *European Physical Journal B*.

**Key figures:** Jean-Philippe Bouchaud (CFM/École Polytechnique), Iacopo Mastromatteo (CFM), Michael Benzaquen (CFM/École Polytechnique), Bence Tóth (CFM), Marc Potters (CFM).

**What this tradition publishes:** The propagator model — exactly the model in this paper — is a live research object in this community. Recent J. Stat. Mech. papers directly relevant:

- Vodret, Mastromatteo, Tóth, Benzaquen (2021), "A stationary Kyle setup: microfounding propagator models," *J. Stat. Mech.* 033410. [doi:10.1088/1742-5468/abe702] — derives the propagator model as the high-frequency limit of a stationary Kyle equilibrium; CFM affiliations.
- Benzaquen, Mastromatteo, Eisler, Bouchaud (2017), "Dissecting cross-impact on stock markets," *J. Stat. Mech.* 023406. [doi:10.1088/1742-5468/aa53f7] — propagator model for multi-asset impact.
- Patzelt, Bouchaud (2017), "Nonlinear price impact from linear models," *J. Stat. Mech.* 123404. [doi:10.1088/1742-5468/aa9335].

The CFM school's institutional home is J. Stat. Mech. and J. Phys. A; CFM researchers with overlapping interests (Mastromatteo, Benzaquen, Tóth) have published the propagator-model literature there. The paper's author (Smerlak, CFM) would be landing in the same venue as his immediate colleagues.

**J. Stat. Mech. scope (confirmed from journal site):** "JSTAT is targeted to a broad community interested in different aspects of statistical physics, which are roughly defined by the fields represented in the conferences called 'Statistical Physics'. ... Topics: Interdisciplinary statistical mechanics [which is the explicit category for finance/markets], Classical statistical mechanics, equilibrium and non-equilibrium." The journal explicitly covers econophysics under "Interdisciplinary statistical mechanics."

### 2.2 Wiener-Hopf technique in mathematical physics

**Journals:** *Journal of Physics A: Mathematical and Theoretical* (J. Phys. A, IOP); *Proceedings of the Royal Society A* (Proc. Roy. Soc. A).

**Key figures:** Satya Majumdar (Université Paris-Saclay, new EiC of J. Phys. A since 2025), Grégory Schehr, Ivan Burenev; for the applied tradition: A.V. Shanin, I.D. Abrahams.

**What this tradition publishes:** In J. Phys. A, Wiener-Hopf is the workhorse for first-passage problems and random walks:

- Burenev, Majumdar (2025), "First-passage properties of the jump process with a drift," *J. Phys. A* 58:315001. [doi:10.1088/1751-8121/adf1ca] — 51-page exactly-solvable random-walk paper using Wiener-Hopf factorization; Majumdar is co-author and now EiC.
- "Exact calculation of the mean first-passage time of continuous-time random walks by nonhomogeneous Wiener–Hopf integral equations" (2022), *J. Phys. A*. [doi:10.1088/1751-8121/acaad9]
- "First-passage statistics of random walks: a general approach via Riemann-Hilbert problems" (2025), *J. Phys. A*. [doi:10.1088/1751-8121/ae1eb9]

In Proc. Roy. Soc. A, the tradition is the "applied Wiener-Hopf" school — diffraction (Sommerfeld half-plane, Noble, Jones), acoustics (duct radiation, Levine-Schwinger), elasticity (crack propagation). These use the factorization of a symbol on the real line to solve boundary-value problems on a half-space, which is structurally the same operation.

**Observation:** The J. Phys. A Wiener-Hopf papers use the factorization to obtain exit-time distributions for random walks, not to solve quadratic variational problems. The structural connection is genuine (same factorization step), but the application context is different enough that this paper would arrive as a novelty rather than extending a recognized thread.

### 2.3 Fractional dynamics and anomalous diffusion

**Journals:** *Physical Review E* (PRE, APS); *J. Phys. A* (IOP); *J. Stat. Mech.* (IOP/SISSA).

**Key figures:** Ralf Metzler, Joseph Klafter (fractional Fokker-Planck), Igor Sokolov, Holger Kantz.

**What this tradition publishes:** The Physics Reports survey by Metzler and Klafter (2000, 2004) established the fractional Fokker-Planck / anomalous diffusion framework. Recent J. Phys. A examples directly relevant:

- "Tempered anomalous diffusion with stochastic resetting" (2025), *J. Phys. A* 58. [doi:10.1088/1751-8121/ae1fc2] — fractional diffusion equation with Laplace-Fourier methods.
- Miao et al. (2026), "Path-integrals and optimal paths for the fractional Ornstein-Uhlenbeck process," *J. Phys. A* 59:105002. [doi:10.1088/1751-8121/ae485b] — path integrals + optimal paths for fOU, J. Phys. A 2026; highly relevant to the OU example in §5.1 of the paper.

The connection: the power-law impact kernel $G(t) = |t|^{-\beta}$ is exactly the covariance of a fractional Gaussian noise with Hurst exponent $H = 1 - \beta/2$ (confirmed in the CHANGELOG). The optimal trading rate under power-law impact is a Marchaud fractional derivative of order $\nu = (1-\beta)/2 = 1 - H$. The anomalous diffusion community would recognize this immediately: Marchaud's operator is the generator of the fractional OU process, the "whitening" step that extracts the innovation from an fBm.

**PRE fit:** PRE publishes anomalous diffusion (fractional Fokker-Planck, CTRW, fBm). The optimization / variational content is less standard there; PRE typically handles stochastic dynamics without the control-theory layer.

### 2.4 Path-integral control and stochastic optimal control in physics

**Journals:** *J. Phys. A*; PRE; scattered elsewhere.

**Key work:** Kappen (2005) *Physical Review Letters*, "Path integrals and symmetry breaking for optimal control theory"; Todorov (2009) *J. Neurophysiology*; for the filtering angle, Belavkin and the quantum-filtering school (J. Phys. A, J. Math. Phys.).

**Fit:** The paper's FOC ($P_+ \nabla J(u^\star) = 0$) is a linear Fredholm integral equation; it does not naturally reduce to a Schrödinger / Hamilton-Jacobi-Bellman equation, so path-integral control methods do not directly apply. The connection to this tradition is more remote. It is relevant in the sense that the linear-quadratic structure gives an exact solution without path-integral approximations, but this is not a natural entry-point for the paper.

---

## 3. Comparison matrix

| Criterion | J. Stat. Mech. | J. Phys. A | PRE | Proc. Roy. Soc. A |
|-----------|---------------|------------|-----|------------------|
| Propagator model already in community | **Yes** (Vodret+, Benzaquen+ etc.) | No | Unlikely | No |
| Author's immediate colleagues publish there | **Yes** (CFM group) | Partly | No | No |
| Wiener-Hopf active tradition | Emerging (resetting, random walks) | **Yes** (first-passage) | No | **Yes** (applied) |
| Fractional derivative / anomalous diffusion | Peripherally | **Yes** (fOU 2026) | **Yes** | Rarely |
| Exactly solvable stochastic model tradition | **Yes** | **Yes** | Yes | No |
| Scope explicitly covers market/finance physics | **Yes** (interdisciplinary stat mech) | "motivated by physical phenomena" | No | No |
| Mathematical level acceptable | **Yes** | **Yes** | Lower | **Yes** (applied math) |
| Operator theory (Gohberg-Krein, Arveson) | Rarely | Functional analysis section | No | Occasionally |
| Audience readership for the result | Highest (econophysics) | Broad stochastic processes | Fractional dynamics only | Applied math |

---

## 4. Recommendation

### Primary: *Journal of Statistical Mechanics* (J. Stat. Mech.)

**Rationale.** This is the natural institutional home. The Bouchaud/CFM school — the researchers who built the propagator model as a physics object — publishes there. Smerlak's immediate CFM colleagues (Mastromatteo, Benzaquen, Tóth) have published the closest prior papers there. The journal explicitly covers "Interdisciplinary statistical mechanics," which includes market microstructure. The audience arrives pre-primed: they know the propagator model, they find $\beta \approx 0.4$–$0.6$ empirically interesting, and they will find the exact fractional-derivative result surprising and clean.

The paper already fits J. Stat. Mech. style in its current form more than it fits any other physics venue: the propagator model is presented as empirical physics (Lillo-Farmer-Mantegna, Bouchaud-Gefen-Potters-Wyart, Gatheral), the OU and power-law examples are the tradition's standard tractable cases, and the exact-closed-form result is exactly what this community values.

**Rewrite cost:** Low. The main adjustments are tonal/organizational, not structural:

1. **Lead** with the empirical anomaly, not with Markowitz. Open: market impact $G(t) \sim |t|^{-\beta}$ is empirically established; what is the optimal rate at which a trader with a short-horizon forecast should be active? This is a concrete physical question in the statistical mechanics of financial markets.
2. **Drop the Hilbert-space / nest-algebra framing** from the introduction. These belong in the proof section; the intro should present the answer $u^\star_t = \kappa_{1-\beta} D_+^\nu \zeta_t$ with $\zeta_t = D_-^\nu \bar\alpha(t,\cdot)(t)$ and explain in words what the three steps do (smooth the forecast, project onto the past, unsmooth).
3. **Add a physics interpretation paragraph:** What does the fractional derivative order signify? The order $\nu = (1-\beta)/2 = 1 - H$ is the whitening exponent of the market's order-flow memory. A market with longer memory (smaller $\beta$, larger $H$) requires a more aggressive fractional derivative (larger $1-\beta$) to un-correlate the impact cost. This is the key physical message.
4. **Downplay Arveson/Gohberg-Krein** attribution in the body; keep it in a Methods or Appendix section. J. Stat. Mech. readers are comfortable with spectral factorization language ("causal-anticausal factorization of the spectral density") without functional-analysis parenthetical citations.
5. **Shorten the abstract** to ~150 words. J. Stat. Mech. articles have shorter abstracts than the current ~200-word draft.
6. **Add figures** if possible — J. Stat. Mech. papers typically have 2-4 display items; the current paper has minimal figures. Even a single plot showing $u^\star$ vs. $\alpha$ at different $\beta$ values would help.

### Secondary: *Journal of Physics A: Mathematical and Theoretical* (J. Phys. A)

**Rationale.** J. Phys. A publishes both Wiener-Hopf technique papers (Majumdar's first-passage papers, the 2022 nonhomogeneous Wiener-Hopf paper) and fractional dynamics papers (Miao et al. 2026 on path integrals for fOU). The newly appointed EiC Majumdar (since early 2025) works precisely on stochastic processes solved by Wiener-Hopf factorization. The "Statistical physics: nonequilibrium systems" section covers stochastic processes and exactly solvable models; the "Mathematical physics" section covers functional analysis and operator theory.

The journal's explicit requirement — "mathematical papers should be clearly motivated by actual or potential application to physical phenomena" — is satisfied by the finance application, but only if the rewrite frames the problem as a *physics problem* whose application to markets is illustrative, not definitional.

**Rewrite cost:** Medium. The technical content needs minimal changes, but the framing requires genuine rethinking:

1. **Reframe the problem as a physical one.** The power-law kernel $G(t) = |t|^{-\beta}$ is the covariance kernel of fractional Gaussian noise. The problem is: given a stochastic signal $\alpha_t$ with known statistics, what causal linear operator minimizes a quadratic cost functional whose kernel equals the fGn covariance? This is a meaningful question in any physical system where (a) the response to control has memory described by a power law, and (b) the controller must be causal. Examples: viscoelastic materials, anomalously diffusing fluids, systems modeled by the generalized Langevin equation.
2. **Lead with the physical picture** of causal Wiener filtering against a memory kernel. The adaptedness constraint is the physicists' causality constraint. The Wiener-Hopf factorization is the same spectral factorization step that appears in causal linear prediction (Kolmogorov-Szegő) and in Kramers-Kronig (causality → analyticity of the response function in the upper half-plane). State this connection explicitly.
3. **Add the fBm interpretation** as a named subsection. The Hurst exponent $H = 1-\beta/2$; the Marchaud operator is the Molchan-Golosov whitening operator; the Wiener-Hopf factorization is the fBm innovation decomposition. This language is native to J. Phys. A.
4. **The finance context** can remain as the primary application but should be framed as one of a family of physically relevant problems with power-law memory kernels.
5. **Keep the mathematical level** — J. Phys. A is comfortable with Sobolev spaces, Fourier symbols, and operator theory. The Gohberg-Krein factorization can be cited and used without apology.
6. **Article length ~18 journal pages** (~10,000 words) is standard for J. Phys. A papers.

### Tertiary: *Physical Review E*

**Rationale.** PRE covers anomalous diffusion and fractional OU processes. The paper's §5.1 (OU example) and the fBm interpretation of the power-law kernel fit PRE's fractional dynamics tradition. PRE published the 2023 Wiener-Hopf paper on Tollmien-Schlichting wave control (Phys. Rev. Fluids) and a broad range of stochastic-process work.

**Why it ranks third:** PRE's style leans toward differential-equation / Fokker-Planck descriptions of stochastic dynamics rather than operator-theoretic / spectral factorization methods. The main result (fractional derivative of a forecast curve) is more naturally stated in the Wiener-Hopf language than in a Fokker-Planck language. PRE reviewers would likely ask for a reformulation as a stochastic differential equation, which is possible but would bury the paper's key insight (the factorization identity (3)).

**If PRE:** Frame as "optimal extraction of a fractional-noise signal under anomalous dissipation" with the financial market as the concrete system. Emphasize the fBm/fGn connection; subordinate the operator-theory. The OU and power-law cases would be the main examples, with less emphasis on the finite-horizon Gohberg-Krein result.

### Fourth: *Proceedings of the Royal Society A*

**Rationale.** Proc. Roy. Soc. A publishes the "applied Wiener-Hopf" tradition (diffraction, acoustics, elasticity crack problems). A paper giving a new class of applications of the Wiener-Hopf technique — to causal stochastic optimization — would be welcome there. The mathematical level is appropriate, and the Sommerfeld/Noble tradition means reviewers will immediately understand the technique.

**Why it ranks fourth:** The community is predominantly interested in wave physics and boundary-value problems; financial markets are a genuinely foreign application context. The stochastic/probabilistic content (adaptedness, forecast curves) is less standard. Proc. Roy. Soc. A would publish this paper, but the readership overlap with the paper's actual intellectual contribution is smaller than J. Stat. Mech. or J. Phys. A.

---

## 5. What the physics rewrite must accomplish regardless of venue

Five moves are required regardless of target journal:

**A. Replace Markowitz as the primary frame.** The Markowitz analogy positions the paper for quantitative-finance readers; for physics readers, the framing is anomalous-memory / generalized Langevin equation. The cost operator $C$ is a friction kernel; the problem is an overdamped stochastic optimal control problem with non-Markovian friction.

**B. Name the physical system.** A physical system that instantiates the paper's setup: a Brownian particle in a generalized Langevin bath with power-law memory kernel $\int_0^t (t-s)^{-\beta} \dot x_s \,ds$ (Bao, Liu, Hänggi 2005 *Phys. Rev. Lett.*), driven by an external force $\alpha_t$ that must be recovered causally from its own noisy version. The optimal causal filter for the control force is a fractional derivative of the signal estimate. This is a concrete physical problem that the paper solves.

**C. Emphasize the exactly-solvable character.** Both J. Stat. Mech. and J. Phys. A value exactly solvable models. The fact that the closed form is $u^\star_t = \kappa_{1-\beta} D^{1-\beta} \bar\alpha(t)(t)$ — a single-line formula — should be the abstract's headline sentence.

**D. Prove or drop Arveson.** The Arveson outer-factorization theorem (which generalizes the Wiener-Hopf result to arbitrary nests) is cited for rigor but is not used mechanically in the paper's computation. For a physics journal, it suffices to use the classical Wiener-Hopf result (Wiener 1949, Krein 1962) and note that it extends to a more abstract setting. Physics readers do not need Arveson; functional-analysts already know it. The citation can remain as a footnote without being central to the exposition.

**E. Provide a physical figure.** At minimum: a plot of the optimal trading rate $u^\star_t$ for an OU signal at several values of $\beta$ (= several Hurst exponents), showing how the fractional derivative order changes the temporal profile. This is the experimentally testable content: at larger $H$ (more persistent signal, longer-memory market), the optimal response is more spread out in time (higher fractional integration). This would be immediately understood by the stochastic processes community.

---

## 6. Summary table: venue-specific rewrite checklist

| Item | J. Stat. Mech. | J. Phys. A |
|------|---------------|------------|
| Lead with propagator model as empirical physics | **Required** | Optional |
| Lead with non-Markovian optimization as physics problem | Not needed | **Required** |
| Drop Markowitz frame from introduction | **Required** | **Required** |
| State main result (fractional derivative) in abstract | **Required** | **Required** |
| Add physical interpretation of $\nu = (1-\beta)/2$ | **Required** | **Required** |
| Downplay Arveson/nest-algebra in body | **Required** | Optional (footnote) |
| Add fBm / Molchan-Golosov connection | Optional | **Recommended** |
| Add physical system analogous to generalized Langevin | Optional | **Recommended** |
| Keep Markowitz correspondence table | No — remove or appendix | No — remove |
| Figures / plots | 2–4 recommended | 2–4 recommended |
| Abstract length | ~150 words | ~150–200 words |
| Mention CRONE / fractional PID connection | Brief footnote | Brief footnote |
| Finite-horizon section | Keep, abbreviate | Keep |
| Operator-theory proof level | Defer to Methods/Appendix | Body is fine |

---

## 7. Open questions

1. **Is the generalized Langevin equation framing physically accurate?** The paper's friction kernel is symmetric (convolution against $|t-s|^{-\beta}$), which is the correct form for a stationary Gaussian process on $\mathbb{R}$, not for the causal friction of a GLE. A reviewer at J. Phys. A may ask about this distinction. The answer is that the cost functional is a bilinear form, not a causal friction, and the symmetry is correct for the LQ problem — but the paper should address this if the GLE framing is used.

2. **Does Proc. Roy. Soc. A publish stochastic-process papers?** The Wiener-Hopf tradition there is predominantly deterministic (wave theory). A stochastic optimal control paper would be unusual. Worth checking a recent issue before targeting.

3. **Would a J. Phys. A submission need a second physical application?** The journal scope says "mathematical papers should be clearly motivated by actual or potential application to physical phenomena." One physical application (financial markets) may be enough if framed correctly as a physical system with power-law memory; a second application from condensed matter or biophysics would strengthen the case.

4. **Is there a Bouchaud/CFM-adjacent paper that explicitly used Wiener-Hopf in the J. Stat. Mech. tradition?** Not found in this survey. The Bouchaud school uses spectral methods and Green's-function language, not the Wiener-Hopf name. Using that name explicitly in the title is therefore a genuine novelty signal for J. Stat. Mech. readers.

---

## Sources

1. Journal of Physics A: Mathematical and Theoretical — About / Scope. IOP Publishing. https://publishingsupport.iopscience.iop.org/journals/journal-of-physics-a-mathematical-and-theoretical/about-journal-physics-mathematical-theoretical/

2. Journal of Statistical Mechanics: Theory and Experiment — About the journal. IOP/SISSA. https://iopscience.iop.org/journal/1742-5468/page/about_the_journal

3. Vodret M, Mastromatteo I, Tóth B, Benzaquen M (2021). "A stationary Kyle setup: microfounding propagator models." *J. Stat. Mech.* 033410. https://beta.iopscience.iop.org/article/10.1088/1742-5468/abe702

4. Benzaquen M, Mastromatteo I, Eisler Z, Bouchaud J-P (2017). "Dissecting cross-impact on stock markets." *J. Stat. Mech.* 023406. https://iopscience.iop.org/article/10.1088/1742-5468/aa53f7

5. Patzelt F, Bouchaud J-P (2017). "Nonlinear price impact from linear models." *J. Stat. Mech.* 123404. https://beta.iopscience.iop.org/article/10.1088/1742-5468/aa9335

6. Burenev I N, Majumdar S N (2025). "First-passage properties of the jump process with a drift." *J. Phys. A* 58:315001. https://iopscience.iop.org/article/10.1088/1751-8121/adf1ca

7. "Exact calculation of the MFPT by nonhomogeneous Wiener-Hopf integral equations" (2022). *J. Phys. A*. https://doi.org/10.1088/1751-8121/acaad9

8. "First-passage statistics of random walks: a general approach via Riemann-Hilbert problems" (2025). *J. Phys. A*. https://doi.org/10.1088/1751-8121/ae1eb9

9. Miao B et al. (2026). "Path-integrals and optimal paths for the fractional Ornstein-Uhlenbeck process." *J. Phys. A* 59:105002. https://iopscience.iop.org/article/10.1088/1751-8121/ae485b

10. "Tempered anomalous diffusion with stochastic resetting" (2025). *J. Phys. A* 58. https://doi.org/10.1088/1751-8121/ae1fc2

11. New Editor-in-Chief for J. Phys. A: Satya N. Majumdar, appointed 2025. https://iopscience.iop.org/article/10.1088/1751-8121/adae69

12. Matteo Smerlak arXiv publications. https://arxiv.org/a/smerlak_m_1

13. Workspace notes: `outputs/adapted-convex-optimization-physics.md` (2026-06-17) — eight physics clusters mapped to the adapted-convex-duality skeleton.

14. Workspace notes: `outputs/stationary-quadratic-execution-context.md` (2026-07-11) — literature context for whole-line stochastic execution setting.
