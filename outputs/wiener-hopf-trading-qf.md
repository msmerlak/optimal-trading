# Quantitative Finance Literature Fit: Optimal Trading via Wiener-Hopf

**Slug:** `wiener-hopf-trading-qf`  
**Date:** 2026-07-18  
**Question:** Which quantitative finance journal/tradition would best digest the paper *Optimal Trading Filters: a Wiener-Hopf Approach* (Smerlak, CFM)?

---

## 1. Starting point

The paper is currently formatted for *Quantitative Finance* (T&F, rquf, as of 2026-07-11). That choice is defensible but not clearly optimal. The paper's closest prior work spans three journals, not one:

| Prior paper | Journal | Year | Citations |
|-------------|---------|------|-----------|
| Gatheral-Schied-Slynko | *Mathematical Finance* | 2012 | 191 |
| Lehalle-Neuman | *Finance and Stochastics* | 2019 | 62 |
| Neuman-Voß | *SIAM J. Fin. Math.* | 2022 | 39 |
| Forde-Sánchez-Betancourt-Smith | *Quantitative Finance* | 2022 | 24 |
| Abi Jaber-Neuman | *Mathematical Finance* | 2025 | — |

The paper extends FSS (2022, *QF*) by giving a closed-form result for the stationary case via a Wiener-Hopf factorization; it complements AJN (2025, *Math. Finance*) by treating the whole-line case explicitly rather than the general finite-horizon case implicitly. The question is whether the paper belongs in the same venue as its closest prior work (QF, with FSS) or should target the venue of its most general predecessor (Math Finance, with GSS and AJN).

---

## 2. Journal landscape

### 2.1 Mathematical Finance (Wiley)

**Scope:** "development and application of novel mathematical and statistical methods for the analysis of financial problems... forum for mathematical scientists, financial practitioners and financial economists. Authors of theoretical papers should describe the motivation and description of the main results and their relevance." [Source: onlinelibrary.wiley.com/page/journal/14679965/homepage/ForAuthors.html]

**Impact:** ~IF 2+, Q1, top-tier in mathematical finance.

**Track record in this sub-field:**
- Gatheral, Schied, Slynko (2012): "Transient linear price impact and Fredholm integral equations." *Math. Finance* 22:445–474. doi:10.1111/j.1467-9965.2011.00478.x — 191 citations. The foundational paper: Fredholm integral equation for the optimal liquidation rate, no signal.
- Jusselin-Rosenbaum (2020): "No-arbitrage implies power-law market impact and rough volatility." *Math. Finance* 30:1309–1336.
- Abi Jaber-Neuman (2025): "Optimal liquidation with signals: the general propagator case." *Math. Finance* 35:841–866. doi:10.1111/mafi.12465 — general Volterra propagator + signal on $[0,T]$; uses infinite-dimensional stochastic control (free-boundary BSDE + resolvent of the second kind). This is the definitive paper on the general problem.

**What Math Finance wants:** Demonstrably novel mathematical methodology; theoretical generality; accessible exposition motivating the results. The GSS and AJN papers set the standard for the propagator sub-field there.

**Risk for this paper:** Reviewers will immediately compare to AJN (2025), which is more general ($[0,T]$, any adapted signal, any Volterra propagator). They may ask whether the stationary/whole-line case is a simplification that warrants a Math Finance paper or a companion note. The answer requires explicitly articulating what the Wiener-Hopf approach adds that the AJN resolvent approach does not: it gives a *closed-form* operator identity for the optimal rate, interpretable in terms of fractional calculus, whereas AJN gives an existence result via a free-boundary problem.

### 2.2 Finance and Stochastics (Springer)

**Scope:** "all areas of finance based on stochastic methods" and "specific topics in mathematics (in particular probability theory, statistics and stochastic analysis) motivated by the analysis of problems in finance." [Source: people.math.ethz.ch/~finasto/edpolicy/edpolicy.html]

**Impact:** ~IF 2+, Q1; highly selective.

**Track record in this sub-field:**
- Lehalle-Neuman (2019): "Incorporating signals into optimal trading." *Finance and Stochastics* 23:275–311. doi:10.1007/s00780-019-00382-7 — 62 citations. Markovian signal + general kernel including power-law case; Fredholm theory; CFM affiliation. This paper's abstract states: "We derive an explicit singular optimal strategy for the special case of an Ornstein-Uhlenbeck signal and exponentially decaying transient market impact."
- Ackermann-Kruse-Urusov (2024): "Reducing Obizhaeva-Wang-type trade execution problems to LQ stochastic control problems." *Finance and Stochastics* 28:813–863. doi:10.1007/s00780-024-00537-1 — structural reduction of a non-standard control problem to a tractable LQ form. This paper's approach — showing that a complicated execution problem reduces to a known solvable form — is structurally analogous to the WH-factorization approach.
- "Optimal trade execution under small market impact" (2024): *Finance and Stochastics* 28:759–812.

**What F&S wants:** Rigorous stochastic analysis; clear contribution to the stochastic methods literature; results that advance the mathematical understanding of financial models, not merely solving specific cases. F&S is receptive to structural reduction results (see Ackermann-Kruse-Urusov above).

**Fit assessment:** The paper's adapted Wiener-Hopf identity $(P_+CP_+)^{-1} = C_+^{-1}P_+C_-^{-1}$ (Lemma 1) is a new structural result about adapted inverse operators; the finite-horizon Gohberg-Krein factorization (Theorem 1) is a structural result about the finite-interval cost operator. These are precisely the type of stochastic-analysis contributions F&S publishes. The challenge is that F&S tends toward papers with complete proofs in the adapted/stochastic setting; the paper's proofs need to be airtight on the adaptedness side (the reviewer will scrutinize the certainty-equivalence step and the forecast-curve argument).

### 2.3 SIAM Journal on Financial Mathematics (SIAM)

**Scope:** "theoretical developments in financial mathematics as well as breakthroughs in the computational challenges they encompass... common platform for scholars interested in the mathematical theory of finance as well as practitioners interested in rigorous treatments of the scientific computational issues." [Source: siam.org/publications/siam-journals/siam-journal-on-financial-mathematics/]

**Impact:** IF 1.8 (2025), Q2, SJR 0.904.

**Track record in this sub-field:**
- Neuman-Voß (2022): "Optimal signal-adaptive trading with temporary and transient price impact." *SIAM J. Fin. Math.* 13:551–575. doi:10.1137/20m1375486 — 39 citations. General semimartingale signal, temporary + exponential transient impact on $[0,T]$; LQ Riccati closed form for exponential kernel. The most directly comparable paper to this one in terms of mathematical approach (linear-quadratic + signal).

**What SIAM JFM wants:** Mathematical rigor plus computational relevance. The dual mandate — theory and computation — is explicit in the scope. SIAM JFM is comfortable with functional analysis, operator theory, and exact solutions; it also expects at least one computational or numerical component. The paper's O(N log N) FFT algorithm for the whole-line optimal rate satisfies this dual mandate well.

**Fit assessment:** This is the strongest natural fit. The paper is exactly in the register of Neuman-Voß (2022): rigorous solution theory for a specific signal-adaptive execution model, with an explicit result and computational content. SIAM JFM would not require the paper to treat the general Volterra case (that's Math Finance territory); it would accept the paper as a "the Wiener-Hopf approach to signal-adaptive execution under power-law impact" contribution.

### 2.4 Quantitative Finance (Taylor & Francis, rquf) — current target

**Scope:** Broad; theory and practice; publishes both empirical/practitioner and mathematical papers.

**Impact:** IF 1.4 (2024), CiteScore 3.5, Q3; acceptance rate 23%. [Source: tandfonline.com/journals/rquf20/about-this-journal]

**Track record in this sub-field:**
- Bouchaud-Gefen-Potters-Wyart (2004): "Fluctuations and response in financial markets." *Quant. Finance* 4:176–190. The propagator model paper.
- Gatheral (2010): "No-dynamic-arbitrage and market impact." *Quant. Finance* 10:749–759. No-arbitrage characterization of admissible kernels.
- Forde-Sánchez-Betancourt-Smith (2022): "Optimal trade execution for Gaussian signals with power-law resilience." *Quant. Finance* 22:585–596. doi:10.1080/14697688.2021.1950919 — 24 citations. The closest prior paper: same setting (power-law, Gaussian signal), different approach (Volterra kernel from Söhngen-Tricomi inversion on $[0,T]$).

**Fit assessment:** QF is the natural venue for the "power-law propagator + signal" strand of the literature (Gatheral 2010, FSS 2022 are both there). The paper would be well received and well matched to the audience. The risk is that it undershoots: the paper's Wiener-Hopf methodology is arguably more sophisticated than the FSS approach, and the closed-form result is cleaner. Publishing alongside FSS in QF may limit the paper's reach and visibility to the stochastic-control community that reads Math Finance and F&S.

---

## 3. Comparison matrix

| Criterion | Math Finance | Finance & Stochastics | SIAM JFM | Quant Finance |
|-----------|-------------|----------------------|----------|---------------|
| Prior papers in this exact sub-field | GSS 2012, AJN 2025 | Lehalle-Neuman 2019 | Neuman-Voß 2022 | FSS 2022, Gatheral 2010 |
| Comparable paper published there | AJN 2025 (general WH: no; resolvent: yes) | LN 2019 (signal + Markovian propagator) | NV 2022 (signal + exponential) | FSS 2022 (power-law + Gaussian signal) |
| Impact factor (2024/25) | ~2.5 (estimated) | ~2.5 (estimated) | 1.8 | 1.4 |
| JCR quartile | Q1 | Q1 | Q2 | Q3 |
| Acceptance rate | ~15% (estimated) | ~10–15% (estimated) | ~25% (estimated) | 23% |
| Rewrite cost (main changes) | Medium (strengthen FH section) | Medium (rigorous adapted stochastic analysis) | Low | None |
| Operator-theory comfort | High | High | High | Medium |
| Computational content required | Not required | Not required | Encouraged | Not required |
| Reviewer pool | Math finance theorists | Stochastic analysts | Applied math + practitioners | Mixed |
| Prestige gain vs. FSS (in QF) | Highest | High | Moderate | None |

---

## 4. Recommendation

### Primary: *SIAM Journal on Financial Mathematics*

**Rationale.** SIAM JFM published Neuman-Voß (2022), which is structurally the most similar paper: rigorous LQ solution theory for signal-adaptive execution with an explicit closed form. The Wiener-Hopf approach is genuinely new methodology for this journal. SIAM's dual theory+computation mandate fits the paper well: the theoretical contribution is the adapted Wiener-Hopf identity and the fractional-derivative closed form; the computational contribution is the O(N log N) FFT implementation of the whole-line optimal policy. The paper requires essentially no rewrite to target SIAM JFM — the current mathematical level, proof structure, and notation are already SIAM-appropriate.

**Strategic argument.** SIAM JFM is the right tier for a paper that: (a) gives the first explicit solution for the stationary signal-adaptive execution problem under power-law impact; (b) introduces a new mathematical tool (Wiener-Hopf factorization) to this sub-field; (c) includes a computational component. Publishing here is a clear upgrade from QF (same audience, higher prestige) without the risk of rejection due to the "incomplete generality" objection that Math Finance reviewers may raise.

**Rewrite requirements — minimal:**

1. **Emphasize the computational component.** The O(N log N) FFT algorithm (§5.4 in the current TeX, `experiments/filtering_fracdiff_powerlaw.py`) should be described in a dedicated subsection with a table of numerical results. SIAM reviewers expect this.
2. **Sharpen the contribution statement vs. Neuman-Voß (2022).** NV treats exponential + signal on $[0,T]$ via LQ Riccati; the paper treats power-law + signal on $\mathbb{R}$ (bulk) and $[0,T]$ (boundary) via Wiener-Hopf factorization. State explicitly why Wiener-Hopf is the right tool when the kernel has a non-rational Fourier symbol ($|\xi|^{\beta-1}$).
3. **Keep current length and proof detail.** SIAM JFM papers are 20–40 pages; the current 16 pp TeX would be on the shorter side. The appendix proofs can be kept.

### Secondary: *Mathematical Finance*

**Rationale.** The flagship journal for optimal execution theory. Both foundational pillars of this sub-field — GSS (2012) and AJN (2025) — are published there. A paper giving a new methodology (Wiener-Hopf factorization) that yields the first closed form for the propagator model with signals would be a genuine contribution at this level.

**Risk.** Reviewers will compare to AJN (2025), which is more general. The objection — "AJN treats the general case; this paper only treats the stationary whole-line case" — must be preempted. The response is: (a) the stationary case gives a qualitatively different result (exact operator closed form vs. existence + free-boundary characterization); (b) the Wiener-Hopf factorization is a distinct methodology that gives new structural insight even into the finite-horizon case; (c) the fractional-derivative closed form (eq. (5) in the paper) is the first such formula in the propagator literature.

**Rewrite requirements — medium:**

1. **Strengthen the finite-horizon section (§3 / Theorem 1, Prop 2, Cor 2).** Math Finance reviewers will want the finite-interval Gohberg-Krein result to be as rigorous as the whole-line Wiener-Hopf result. The current math-correctness review (CHANGELOG 2026-07-14) identified and fixed the main issues (reflected terminal-anchored causal factor, weight-conjugation); verify that the proof is airtight.
2. **Position explicitly against AJN (2025).** Add a paragraph in §1.3 contrasting the methods: AJN uses operator Riccati + free-boundary BSDEs; this paper uses spectral factorization (WH/GK). State what each approach gives that the other does not.
3. **Make the structural claim precise.** The adapted Wiener-Hopf identity $(P_+CP_+)^{-1} = C_+^{-1}P_+C_-^{-1}$ (Lemma 1) is an abstract result about adapted inverse operators that holds for any factorizable positive operator $C$ on any filtered Hilbert space. This is a mathematical result of independent interest that should be stated and proved without reference to the specific financial application. Math Finance readers will want to see this done correctly.
4. **Length.** Math Finance papers average 25–40 pages. The current 16 pp TeX is likely too short for Math Finance; expanding the finite-horizon analysis and adding a rigorous stochastic setup section would bring it to the right length.

### Third: *Finance and Stochastics*

**Rationale.** F&S published Lehalle-Neuman (2019), which initiated the signal-adaptive execution + general propagator direction. The Ackermann-Kruse-Urusov (2024) paper in F&S shows that structural reduction of execution problems is welcome there. The adapted Wiener-Hopf identity (Lemma 1) would fit F&S's stochastic-analysis mandate.

**Rewrite requirements — medium (different flavor than Math Finance):**

1. **Stochastic setup must be rigorous.** F&S expects the probability space, filtration, and adaptedness conditions to be stated precisely. The forecast-curve substitution ($\alpha \to \bar\alpha$) and the certainty-equivalence step need to be proved in full, not just stated. This is already done in the paper (CHANGELOG 2026-06-28 describes the §2.3 rewrite), but F&S reviewers will read it carefully.
2. **Position against Lehalle-Neuman (2019).** LN19 gives an explicit solution for the OU signal + exponential kernel case. The paper gives an explicit solution for the power-law kernel case on $\mathbb{R}$ (and converging to it on $[0,T]$). State the relationship: LN19 uses Laplace transform + Ricatti (Markovian structure); this paper uses Wiener-Hopf (non-Markovian / non-rational symbol).
3. **The adapted Wiener-Hopf identity as the lead result.** F&S readers care about the mathematical tool, not just its application. Lemma 1 (the identity $(P_+CP_+)^{-1} = C_+^{-1}P_+C_-^{-1}$) should be stated as the central mathematical result; the financial application is the motivation and the worked example.

### Fourth: *Quantitative Finance* (current target)

**The case for staying.** QF published FSS (2022), and the paper is a direct successor to FSS. The paper is already formatted. The audience (CFM-school, practitioner-adjacent) is appropriate. Fast turnaround (37 days to first decision). Acceptance rate 23% (more accessible than Math Finance or F&S). If the priority is quick publication in a friendly venue, QF is the right choice.

**The case for upgrading.** QF IF 1.4 (Q3) versus SIAM JFM 1.8 (Q2). The paper introduces a new technique (Wiener-Hopf factorization) to a field that has used only Fredholm/Volterra methods; this methodological contribution deserves a venue where the reviewer pool will recognize and credit it. QF is read by practitioners and physicists; SIAM JFM is read by applied mathematicians and theorists working on execution — a better match for the paper's mathematical content.

---

## 5. Rewrite requirements by venue: summary checklist

| Item | Math Finance | Finance & Stochastics | SIAM JFM | Quant Finance |
|------|-------------|----------------------|----------|---------------|
| Strengthen finite-horizon section | **Required** | Required | Optional | Optional |
| Add comparison paragraph vs. AJN (2025) | **Required** | Recommended | Recommended | Optional |
| Add comparison paragraph vs. LN (2019) | Recommended | **Required** | Recommended | Optional |
| Prove certainty-equivalence / forecast-curve step fully | Recommended | **Required** | Recommended | Optional |
| Add computational/numerical section | Optional | Optional | **Recommended** | Optional |
| Abstract Lemma 1 as independent mathematical result | **Required** | **Required** | Optional | Optional |
| Current proof appendix | Expand | Expand | Keep | Keep |
| Target length | 25–40 pp | 25–35 pp | 20–30 pp | 16–25 pp |
| Reformat from QF style | Yes (Wiley LaTeX) | Yes (Springer LaTeX) | Yes (SIAM LaTeX) | Already done |

---

## 6. Open questions

1. **Is the whole-line (stationary) assumption a barrier at Math Finance?** AJN (2025) is strictly more general. The counter-argument is that the Wiener-Hopf approach gives qualitatively different (and more explicit) results for the stationary case than AJN's resolvent approach gives for the finite-horizon case. A Math Finance reviewer might or might not accept this. SIAM JFM reviewers are more likely to accept it.

2. **Does the paper need a more rigorous handle on the infinite-dimensional stochastic setting?** AJN (2025) uses Hilbert-module / operator-Riccati language; Abi Jaber's framework is more elaborate than the paper's $L^2_{\rm adap}$ + Wiener-Hopf setup. Math Finance and F&S reviewers may ask whether the paper's framework handles the general adapted signal case with the same generality as AJN. The answer is: no — the paper proves the closed form for the stationary case, and for the finite-horizon case asserts convergence of the bulk formula to the $[0,T]$ optimum. This scope limitation should be stated honestly.

3. **Should the signal-side spectral factorization (§5.5 "Role of the forecast curve: innovations filter and value") be moved to the main text for Math Finance/F&S?** The innovations-filter representation $u^\star = g(D)\dot W$ (derived in the CHANGELOG 2026-07-14 extensions) connects the paper to the Kalman-filter / innovations literature that F&S readers know. This would strengthen the mathematical contribution without changing the core result.

4. **Is there a concurrent preprint that uses Wiener-Hopf for execution?** The search found no such paper as of 2026-07-18. The field is moving toward explicit solutions (see arXiv:2605.24242 "Explicit Signal-Adaptive Sequential Optimal Execution Quotes" 2026), but no Wiener-Hopf paper appeared in the search.

---

## 7. Concise recommendation

**Submit to SIAM JFM first.** The paper is already SIAM-appropriate in mathematical level, and SIAM JFM published the most comparable prior work (Neuman-Voß 2022). The required additions — a computational subsection with FFT benchmarks — are already in the experiments directory. After SIAM JFM acceptance or rejection with useful referee comments, target Math Finance if the paper is strengthened with a more rigorous finite-horizon treatment. Stay at QF only if the goal is fast publication without further development.

---

## Sources

1. Mathematical Finance: for authors / aims and scope. Wiley Online Library. https://onlinelibrary.wiley.com/page/journal/14679965/homepage/ForAuthors.html

2. Finance and Stochastics: editorial policy. ETH Zürich. https://people.math.ethz.ch/~finasto/edpolicy/edpolicy.html

3. SIAM Journal on Financial Mathematics: scope and submission. SIAM. https://www.siam.org/publications/siam-journals/siam-journal-on-financial-mathematics/

4. Quantitative Finance: about this journal (metrics). Taylor & Francis. https://www.tandfonline.com/journals/rquf20/about-this-journal

5. Gatheral J, Schied A, Slynko A (2012). "Transient linear price impact and Fredholm integral equations." *Mathematical Finance* 22:445–474. doi:10.1111/j.1467-9965.2011.00478.x

6. Lehalle C-A, Neuman E (2019). "Incorporating signals into optimal trading." *Finance and Stochastics* 23:275–311. doi:10.1007/s00780-019-00382-7

7. Neuman E, Voß M (2022). "Optimal signal-adaptive trading with temporary and transient price impact." *SIAM J. Financial Mathematics* 13:551–575. doi:10.1137/20m1375486

8. Forde M, Sánchez-Betancourt L, Smith B (2022). "Optimal trade execution for Gaussian signals with power-law resilience." *Quantitative Finance* 22:585–596. doi:10.1080/14697688.2021.1950919

9. Abi Jaber E, Neuman E (2025). "Optimal liquidation with signals: the general propagator case." *Mathematical Finance* 35:841–866. doi:10.1111/mafi.12465

10. Ackermann J, Kruse T, Urusov M (2024). "Reducing Obizhaeva-Wang-type trade execution problems to LQ stochastic control problems." *Finance and Stochastics* 28:813–863. doi:10.1007/s00780-024-00537-1

11. SIAM J. Financial Mathematics impact metrics (2025). ScimagoJR; journalmetrics.org. https://www.journalmetrics.org/journal/siam-journal-on-financial-mathematics

12. Quantitative Finance impact metrics (2024). Taylor & Francis. https://www.tandfonline.com/journals/rquf20/about-this-journal

13. Workspace bib file: `tex/factorization-optimal-trading.bib` — source of reference cluster journal mapping.

14. "Explicit Signal-Adaptive Sequential Optimal Execution Quotes" (2026). arXiv:2605.24242. https://doi.org/10.48550/arxiv.2605.24242
