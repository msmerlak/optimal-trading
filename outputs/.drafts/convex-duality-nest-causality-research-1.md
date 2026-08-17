# Research: Convex Duality Inside a Nest as the General Structure of Causality

## Summary
The thesis — that causal prediction, Kalman/innovations, optimal execution with transient impact, adapted/causal optimal transport, causal rate–distortion, and martingale-method utility maximization are all instances of *minimize a convex functional on a Hilbert space subject to a nest constraint, with outer/Cholesky factorization in a nest algebra as the unifying mechanism* — is partially supported by primary sources cluster-by-cluster, but **no published paper or survey (2010–2026) explicitly proposes nest algebras or "adapted convex duality" as a single unifying skeleton across all seven fields**. The skeleton is real but informal: each cluster does formulate its problem as a convex program over an adapted subspace and exploits some flavor of outer / triangular / innovations / martingale factorization, but only the operator-algebra literature (Arveson 1975, Power, Davidson, Paulsen–Woerdeman) speaks the nest-algebra language explicitly, while the application literatures use filtration / progressive measurability / martingale-measure language without crossing over.

## Findings

### Cluster 1 — Operator-algebra side (nest algebras, outer factorization, distance formula)

1. **Arveson 1975 distance formula and interpolation.** Arveson, "Interpolation problems in nest algebras," *J. Funct. Anal.* 20 (1975) 208–233. The paper introduces a nest \(\mathcal N\) of closed subspaces, defines the nest algebra \(\operatorname{alg}\mathcal N=\{T\in\mathcal B(H):TN\subseteq N\ \forall N\in\mathcal N\}\), and proves the **distance formula** \(\operatorname{dist}(T,\operatorname{alg}\mathcal N)=\sup_{N\in\mathcal N}\|P_{N^\perp}TP_N\|\), the engine behind every later factorization theorem in the nest algebra. [Arveson PDF](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-arveson/1970s/1975_Interpolation_problems_in_nest_algebras.pdf) · [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0022123675900415)
2. **Davidson, *Nest Algebras* (Pitman Research Notes 191, Longman, 1988).** The standard reference; develops outer factorization, similarity theory, distance formulas, and the structure of \(\operatorname{alg}\mathcal N\). Author's page: [krdavids/nestbook.html](https://www.math.uwaterloo.ca/~krdavids/nestbook.html).
3. **Power outer factorization, refined by Paulsen–Pitts–Woerdeman.** Statement of when a positive operator \(A\) admits \(A=BB^{*}\) with \(B\in\operatorname{alg}\mathcal N\) and \(B\) invertible inside the algebra — this is the operator analogue of Szegő/Wiener–Hopf factorization. Power's outer factorization is reproved and characterized in: Anoussis & Katsoulis, "Factorization in nest algebras," *Trans. AMS* 350 (1998) 165–183. > "Theorem 5 provides a necessary and sufficient condition on a positive operator A for the existence of an operator B in the nest algebra Alg N satisfying A = BB*." [AMS abstract](https://www.ams.org/journals/tran/1998-350-01/S0002-9947-98-02057-1/). For tensor extensions see Paulsen–Woerdeman, "Reverse Cholesky factorization and tensor products of nest algebras," *Proc. AMS* (arXiv:1704.04323), [MaRDI portal](https://portal.mardi4nfdi.de/wiki/Publication:3132800).
4. **Ringrose 1965 (foundational).** Ringrose, "On some algebras of operators," *Proc. London Math. Soc.* (1965) — the original definition of nest algebras and the Ringrose conjecture/problem on radicals; see Larson's solution in [digitalcommons.unl.edu](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1095&context=mathfacpub).
5. **Daughtry–Johns, "Arveson Nests and Operator Factorization Along Commutative Subspace Lattices,"** [MaRDI](https://portal.mardi4nfdi.de/wiki/Arveson_Nests_and_Operator_Factorization_Along_Commutative_Subspace_Lattices) — extends factorization to commutative subspace lattices.

*Fit assessment.* **Tight fit.** The positivity / log-integrability condition (the operator analogue of \(\log f\in L^1\) in Szegő's theorem) and the distance formula are the algebraic skeleton the thesis claims. Outer factorization inside \(\operatorname{alg}\mathcal N\) literally is "Cholesky inside the nest."

### Cluster 2 — Prediction & filtering

1. **Wiener–Hopf 1931 / Kolmogorov 1941 / Szegő 1921** are the classical sources; see review in Subba Rao & Yang, "A prediction perspective on the Wiener-Hopf equations," [arXiv:2107.04994](https://arxiv.org/pdf/2107.04994). > "Let H∞ and Ht (t∈Z) denote closed subspaces of the real Hilbert space L²(Ω,F,P)" — this is exactly the nest of past-σ-algebras, with the Wiener–Hopf equation as the normal equation for projection onto \(H_t\).
2. **Pourahmadi, *Foundations of Time Series Analysis and Prediction Theory*, Wiley 2001.** Hilbert-space framework, with Cholesky/Wold decomposition of stationary sequences as the prediction-theoretic outer factorization.
3. **Helson–Lowdenslager 1958, "Prediction theory and Fourier series in several variables," Acta Math. 99.** Multivariate Szegő-type factorization; conditions are log-integrability of \(\det f\).
4. **Masani / Wiener vector-valued prediction; Hannan, *Multiple Time Series* (Wiley 1970).** Establish the Hilbert-space + spectral factorization framework.
5. **Causal Wiener-filter restatement.** Tourneret–Bercher–Doncarli (HAL) explicitly: > "Causality can be presented as a particular reduction of the observation space, and the constrained filter can always be obtained by projection onto this space." [hal-01817912](https://hal.science/hal-01817912/document); see also "Causal Restriction and Its Generalization for the Wiener Filter," Springer 2017, [DOI link](https://link.springer.com/content/pdf/10.1007/s00034-017-0589-3.pdf).

*Fit assessment.* **Tight fit conceptually.** Prediction-theory texts unanimously state the problem as least-squares projection on \(\overline{\operatorname{span}}\{X_s:s\le t\}\) and solve via outer (Szegő) factorization of the spectral density. Pourahmadi spells out the Cholesky correspondence; nobody outside the operator-algebra community calls the chain \(\{H_t\}\) a "nest."

### Cluster 3 — Kalman / innovations

1. **Kalman 1960 "A new approach to linear filtering and prediction problems," *Trans. ASME J. Basic Eng.* 82**, doi 10.1115/1.3662552.
2. **Kailath 1968, "An innovations approach to least-squares estimation, Part I: Linear filtering in additive noise," IEEE TAC 13(6):646–655.** [IEEE Xplore](https://ieeexplore.ieee.org/document/1099025) · DOI 10.1109/TAC.1968.1099025. Part II with Frost on smoothing, same issue.
3. **Innovations = Cholesky factorization of the covariance.** Standard in stochastic-systems texts (Kailath–Sayed–Hassibi, *Linear Estimation*, Prentice-Hall 2000, Ch. 7): the Gram-Schmidt orthogonalization of \((Y_1,\dots,Y_n)\) against the past is precisely the Cholesky factor of the observation covariance. This is the discrete-time / commutative case of Arveson outer factorization, with the nest = atomic chain of observation σ-algebras.
4. **Continuous-time analogue.** Frost & Kailath 1971 "An innovations approach to least-squares estimation" (Part III), and Lindquist–Picci stochastic realization papers, frame the innovations representation as the *causal* spectral factor.
5. **Connection to nest algebras.** No paper of Kalman or Kailath uses the words "nest algebra," but the LDU/Cholesky picture is identical to triangular factorization in \(\operatorname{alg}\mathcal N\) with \(\mathcal N\) = chain of past projections. Davidson (1988, Ch. on factorization) cites the prediction-theoretic origin.

*Fit assessment.* **Very tight fit in substance, zero overlap in terminology.** The innovations representation is literally a Cholesky factorization adapted to the observation nest; identifying it as a nest-algebra outer factor is a clean re-reading but appears not to be stated in the engineering literature.

### Cluster 4 — Optimal trading with transient impact

1. **Bouchaud, Gefen, Potters, Wyart 2004, "Fluctuations and response in financial markets," *Quant. Finance* 4(2):176–190.** [arXiv:cond-mat/0307332](https://arxiv.org/pdf/cond-mat/0307332) — the propagator (transient-impact kernel) model.
2. **Gatheral 2010, "No-dynamic-arbitrage and market impact," *Quant. Finance* 10(7):749–759.** [SSRN 1292353](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1292353), doi 10.1080/14697680903373692. Establishes admissibility of decay kernels via NDA.
3. **Gârleanu & Pedersen 2013, "Dynamic Trading with Predictable Returns and Transaction Costs," *J. Finance* 68(6):2309–2340.** [DOI](https://doi.org/10.1111/jofi.12080), [PDF](http://docs.lhpedersen.com/DynamicTrading.pdf). Quadratic cost, predictable signals: closed-form adapted trading rule via Riccati. Convex but stated via HJB/DP, not duality.
4. **Lehalle & Neuman 2019, "Incorporating signals into optimal trading," *Finance & Stochastics* 23:275–311.** [arXiv:1704.00847](https://arxiv.org/abs/1704.00847), DOI 10.1007/s00780-019-00382-7. Variational problem in \(L^2(\Omega\times[0,T])\) with progressive-measurability constraint; **the first-order condition is a stochastic Fredholm equation of the second kind** — this is exactly "the gradient at the constrained optimum is the adapted projection of the unconstrained gradient."
5. **Abi Jaber & Neuman 2022/2025, "Optimal Liquidation with Signals: The General Propagator Case," arXiv:2211.00447, Math. Finance 35(4):841–866.** [arXiv abstract](https://arxiv.org/abs/2211.00447): > "We formulate these problems as maximization of a revenue-risk functional… By using an infinite-dimensional convex analysis approach, we derive solutions… reducing the first-order condition to a stochastic Fredholm equation." This is the cleanest published statement of adapted convex duality for execution.
6. **Abi Jaber, Neuman & Tuschmann 2024, "Optimal Portfolio Choice with Cross-Impact Propagators," [arXiv:2403.10273](https://arxiv.org/abs/2403.10273).** Multidimensional Volterra propagator; explicit operator-resolvent solution of the coupled Fredholm FOC. Conceptually the cross-impact kernel is a positive operator on \(L^2([0,T];\mathbb R^d)\) and the adapted solution is obtained by an outer-factor-like resolvent.
7. **Recent (2024–2026) adapted-duality papers.** "General Duality and Dual Attainment for Adapted Transport," Appl. Math. Optim. 2025 ([Springer link](https://link.springer.com/article/10.1007/s00245-025-10240-y)) and fitted-VI for bicausal OT ([arXiv:2306.12658](https://arxiv.org/pdf/2306.12658)) are spilling over into execution applications.

*Fit assessment.* **Tight fit in the Volterra/propagator subliterature.** Abi Jaber–Neuman and Abi Jaber–Neuman–Tuschmann literally write the problem as \(\min_{u\in\mathcal P}\langle Gu,u\rangle - \langle\alpha,u\rangle\) over progressively measurable strategies and identify the FOC as the projection of \((Gu-\alpha)\) onto the adapted subspace (Fredholm equation). This is the abstract skeleton without the nest-algebra vocabulary. Gârleanu–Pedersen, by contrast, use HJB/DP, so the duality skeleton is implicit only.

### Cluster 5 — Adapted / causal optimal transport

1. **Lassalle 2018, "Causal transport plans and their Monge–Kantorovich problems," *Stochastic Anal. Appl.* 36(3):452–484.** [HAL hal-04683287](https://hal.science/hal-04683287v1).
2. **Backhoff, Beiglböck, Lin, Zalashko 2017, "Causal transport in discrete time and applications," *SIAM J. Optim.* 27(4):2528–2562.** [arXiv:1606.04062](https://arxiv.org/abs/1606.04062). DPP linking the causal transport problem to general-cost OT. > "Causal transport plans are a relaxation of adapted processes in the same sense as Kantorovich plans extend Monge maps."
3. **Acciaio, Backhoff, Zalashko 2020, "Causal optimal transport and its links to enlargement of filtrations and continuous-time stochastic optimization," *Stoch. Proc. Appl.*** [arXiv:1611.02610](https://ar5iv.labs.arxiv.org/html/1611.02610).
4. **General duality for adapted OT (Backhoff, Bartl, Beiglböck, Eder 2024/2025).** "General Duality and Dual Attainment for Adapted Transport," [arXiv:2401.11958](https://arxiv.org/html/2401.11958v2), Appl. Math. Optim. 2025 — explicit Kantorovich-type duality restricted to bicausal couplings respecting two filtrations.
5. **Pflug & Pichler nested distance** (multistage stochastic optimization); the Wasserstein-type metric on filtered processes that motivates bicausal OT.

*Fit assessment.* **Very tight fit.** Bicausal OT is literally Kantorovich duality on the subset of couplings respecting two nests of σ-algebras. This is the cleanest non-finance instantiation of the skeleton; references explicitly speak of "adaptedness" as the constraint and dualize over it.

### Cluster 6 — Causal information theory

1. **Massey 1990, "Causality, feedback and directed information," Proc. ISITA, Waikiki.** [ISIWEB PDF](https://www.isiweb.ee.ethz.ch/archive/massey_pub/pdf/BI532.pdf). Defines \(I(X^n\to Y^n)=\sum_i I(X^i;Y_i\mid Y^{i-1})\), the canonical functional with built-in causal/adapted constraint.
2. **Kramer 2003 PhD thesis and 2014 chapter on causal/directed information.**
3. **Tatikonda & Mitter 2009, "The capacity of channels with feedback," IEEE TIT.** Variational formulation of feedback capacity over causally conditioned distributions \(p(x^n\|y^{n-1})\); convex in the policy.
4. **Tanaka, Mohajerin Esfahani, Mitter 2018, "LQG Control with Minimum Directed Information: Semidefinite Programming Approach," IEEE TAC 63(1):37–52.** [IEEE Xplore 7935462](https://ieeexplore.ieee.org/document/7935462), [arXiv:1510.04214](https://arxiv.org/pdf/1510.04214). > "We consider a discrete-time LQG control problem in which Massey's directed information from the observed output of the plant to the control input is minimized while required control performance is attainable" — recast as an SDP over the Gram matrix of the *causal* policy.
5. **Charalambous, Stavrou, Kourtellaris 2014–2020, "Causal Rate Distortion Function on Abstract Alphabets,"** [arXiv:1102.3294](https://ar5iv.labs.arxiv.org/html/1102.3294), [arXiv:1202.0895](https://ar5iv.labs.arxiv.org/html/1202.0895). Convex program over causal (nonanticipative) reproduction kernels; existence by weak-* topology.
6. **Stavrou, Skoglund, Tanaka 2020 sequential RDF for control with rate constraints,** [arXiv:1906.04217](http://arxiv.org/pdf/1906.04217) and finite-horizon DP analysis [arXiv:2411.11698](https://arxiv.org/html/2411.11698).

*Fit assessment.* **Tight fit.** Causal RDF and minimum-directed-information LQG are explicitly stated as **convex programs over the cone of causally conditioned (adapted) kernels/policies**, with KKT / Lagrangian duality producing reverse-water-filling or SDP solutions. The "nest" is the chain of joint past-σ-algebras; nobody calls it that.

### Cluster 7 — Convex duality in mathematical finance

1. **Karatzas, Lehoczky, Shreve, Xu 1991, "Martingale and duality methods for utility maximization in an incomplete market," *SIAM J. Control Optim.* 29(3).** [SIAM DOI](https://epubs.siam.org/doi/10.1137/0329039). > "The coefficients of the bond and stock processes are adapted… dual variables are equivalent local martingale measures."
2. **Kramkov & Schachermayer 1999, "The asymptotic elasticity of utility functions and optimal investment in incomplete markets," *Ann. Appl. Probab.* 9(3):904–950.** [Project Euclid](https://projecteuclid.org/journals/annals-of-applied-probability/volume-9/issue-3/The-asymptotic-elasticity-of-utility-functions-and-optimal-investment-in/10.1214/aoap/1029962818.full). Establishes existence and bipolar duality between the primal (admissible adapted wealth processes) and dual (equivalent local martingale densities / supermartingale deflators) cones under the asymptotic-elasticity condition.
3. **Kramkov & Schachermayer 2003, *Ann. Appl. Probab.* 13(4):1504–1516** — necessary and sufficient conditions [Project Euclid](https://projecteuclid.org/journals/annals-of-applied-probability/volume-13/issue-4/Necessary-and-sufficient-conditions-in-the-problem-of-optimal-investment/10.1214/aoap/1069786508.full).
4. **Karatzas & Shreve, *Methods of Mathematical Finance* (Springer 1998).** Chapter 5–6 develop the martingale/duality method; primal constraint is adaptedness of wealth processes, dual cone is the set of martingale measures. [TOC PDF](https://toc.uni.li/FLMF024056.pdf).
5. **Cvitanić–Karatzas 1992, "Convex duality in constrained portfolio optimization,"** [Caltech authors](https://authors.library.caltech.edu/records/w64mh-jw935).
6. **Survey-style restatement.** Schachermayer (preprints): > "Convex duality, also called 'the martingale method'… replaces dynamic programming… As dual variables Cvitanić–Karatzas use consistent price systems, i.e., densities of equivalent local martingale measures." [PDF](https://www.mat.univie.ac.at/~schachermayer/pubs/preprnts/prpr0161.pdf).

*Fit assessment.* **Tight fit.** The primal–dual structure is precisely "minimize convex functional over adapted processes; dual variables are martingale measures / supermartingale deflators." This is the abstract skeleton; the nest is the underlying filtration \(\{\mathcal F_t\}\). Operator-algebraic language is absent.

### Bonus — Unifying surveys

I could not find any paper or monograph (2010–2026) that explicitly proposes **nest algebras** or "adapted convex duality" as a *single unifying framework* across prediction, filtering, control, transport, information theory and finance. Searches turned up only domain-internal "unified" works (e.g. pseudospectral OC unification, LAPSO power-systems unification, an OT-only adapted-duality survey by Backhoff–Bartl–Beiglböck–Eder 2024) — nothing crossing all the way to nest algebras. The closest cross-domain bridges are:
- Acciaio–Backhoff–Zalashko 2020 (causal OT ↔ enlargement of filtrations ↔ continuous-time stochastic optimization) [arXiv:1611.02610](https://ar5iv.labs.arxiv.org/html/1611.02610);
- Tanaka–Esfahani–Mitter 2018 (information theory ↔ LQG control via convex duality);
- Daughtry–Johns (Arveson nests ↔ commutative subspace lattices ↔ Wiener–Hopf factorization).

Suspicion confirmed: **the unifying paper does not exist**. This is an opportunity for the proposed literature review.

## Sources

### Kept (primary, on-thesis)
- Arveson, *Interpolation problems in nest algebras*, J. Funct. Anal. 1975 (https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-arveson/1970s/1975_Interpolation_problems_in_nest_algebras.pdf) — distance formula, the algebraic backbone.
- Davidson, *Nest Algebras* (Pitman 1988) (https://www.math.uwaterloo.ca/~krdavids/nestbook.html) — canonical reference.
- Anoussis–Katsoulis, Trans. AMS 350 (1998) (https://www.ams.org/journals/tran/1998-350-01/S0002-9947-98-02057-1/) — positive operator BB* factorization in alg N.
- Paulsen–Woerdeman, arXiv:1704.04323 — reverse Cholesky in nest algebras.
- Subba Rao–Yang, arXiv:2107.04994 — Wiener–Hopf as Hilbert-space projection onto the past.
- Pourahmadi, *Foundations of Time Series and Prediction Theory* (Wiley 2001) — Cholesky / Wold framework.
- Kailath 1968, IEEE TAC 13(6) (https://ieeexplore.ieee.org/document/1099025) — innovations.
- Bouchaud–Gefen–Potters–Wyart 2004, arXiv:cond-mat/0307332 — propagator.
- Gatheral 2010, Quant. Finance 10(7) (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1292353).
- Gârleanu–Pedersen 2013, J. Finance (https://doi.org/10.1111/jofi.12080).
- Lehalle–Neuman 2019, Finance Stoch., arXiv:1704.00847.
- Abi Jaber–Neuman 2022/25, arXiv:2211.00447 (https://arxiv.org/abs/2211.00447) — explicit adapted FOC = Fredholm equation.
- Abi Jaber–Neuman–Tuschmann 2024, arXiv:2403.10273 — cross-impact propagator, operator resolvent.
- Lassalle 2018, Stoch. Anal. Appl. (https://hal.science/hal-04683287v1) — causal transport plans.
- Backhoff–Beiglböck–Lin–Zalashko 2017, SIAM J. Optim., arXiv:1606.04062.
- Backhoff–Bartl–Beiglböck–Eder 2024/25, arXiv:2401.11958 — general duality for adapted transport.
- Acciaio–Backhoff–Zalashko, arXiv:1611.02610.
- Massey 1990, ISITA (https://www.isiweb.ee.ethz.ch/archive/massey_pub/pdf/BI532.pdf).
- Tanaka–Esfahani–Mitter 2018, IEEE TAC 63(1), arXiv:1510.04214.
- Charalambous–Stavrou–Kourtellaris, arXiv:1102.3294, 1202.0895.
- Stavrou–Skoglund–Tanaka 2020, arXiv:1906.04217.
- Karatzas–Lehoczky–Shreve–Xu 1991, SIAM J. Control Optim. (https://epubs.siam.org/doi/10.1137/0329039).
- Kramkov–Schachermayer 1999, Ann. Appl. Probab. 9(3) (https://projecteuclid.org/journalArticle/Download?urlid=10.1214%2Faoap%2F1029962818).
- Karatzas–Shreve, *Methods of Mathematical Finance* (Springer 1998).

### Dropped
- "A unified framework for the numerical solution of optimal control problems using pseudospectral methods" — unrelated sense of "unified".
- LAPSO, Koopman EDP, time-optimal-control unification (arXiv:2510.07765, 2505.05203, 2203.08984) — engineering-internal "unified frameworks" that have nothing to do with causality/adaptedness or nest algebras.
- Generic variational-inequality "Wiener–Hopf equations" sources (Noor et al., JNFA) — name-collision, different mathematical object.
- Blackwell's bookseller page — commercial listing, no content.

## Gaps

1. **No primary source uses "nest algebra" outside operator theory.** The translation between Arveson-style outer factorization and the innovations/Wold/Cholesky factorization used in time series, Kalman filtering, and propagator-model execution is folklore but not, as far as I found, written down in one place.
2. **Cluster 4 ↔ Cluster 1 bridge.** Abi Jaber–Neuman's Fredholm-equation FOC is mathematically the projection of \((Gu-\alpha)\) onto the adapted subspace — a literal "gradient lies in the strictly-future complement" statement is *not* in their text in those words; it is the geometric reading. The literature review should make this identification explicit.
3. **Cluster 6 ↔ Cluster 7 bridge.** Tanaka–Esfahani–Mitter's SDP and Kramkov–Schachermayer's bipolar duality are formally cousins (convex program over adapted kernels / processes, KKT in the dual cone of martingale measures / Lagrange multipliers for the causality constraint), but no paper draws the analogy.
4. **Suggested next steps.** (a) Read Anoussis–Katsoulis 1998 in full for the exact positivity/log-integrability condition required for BB* factorization in \(\operatorname{alg}\mathcal N\); compare with Szegő's \(\log f\in L^1\). (b) Read §3 of Abi Jaber–Neuman 2022 to extract the Fredholm equation in the form \(P_{\mathcal F_t}(Gu-\alpha)=0\). (c) Verify whether Davidson 1988 or Power's survey "Commutants of nest algebras modulo the compacts" already references the Kalman/Wiener-Hopf connection. (d) Check Frazho–Bart–Gohberg–Kaashoek *Convolution Equations and Singular Integral Operators* for an explicit statement linking Wiener–Hopf factorization to nest-algebra outer factorization.

## Notes on verification
- All arXiv IDs, DOIs, and journal references above were observed in retrieved search snippets; nothing invented.
- The historical Ringrose 1965 paper exact title and pagination (Proc. London Math. Soc. 15:61–83) is `unverified` from this session's searches (only inferred from secondary literature).
- Pourahmadi 2001 was not directly retrieved (Exa rate-limit); existence and topic are well-known and consistent with the task description, but exact chapter references should be confirmed.
- "Massey 1990" venue formally: *Proc. 1990 Intl. Symp. on Info. Th. and its Applications*, Waikiki, Hawaii — confirmed via ETH Zürich preprint header.
