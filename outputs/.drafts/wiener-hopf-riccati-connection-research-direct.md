# Research Notes: wiener-hopf-riccati-connection

## Search queries used

1. "KYP lemma positive real spectral factorization Riccati equation equivalence Anderson"
2. "Wiener-Hopf factorization stationary LQG Kucera spectral factor Riccati"
3. "stochastic realization theory Faurre Lindquist Picci spectral factor Riccati"
4. "operator Riccati equation Volterra optimal control Abi Jaber"
5. "Obizhaeva Wang exponential propagator state space LQR optimal execution"
6. "innovations representation Kalman filter equivalent steady-state Wiener filter"
7. "H-infinity control Krein space Riccati equation Hassibi Sayed Kailath"
8. "discrete algebraic Riccati equation spectral factorization inner outer Zhou Doyle Glover"

## Key anchors

### KYP lemma / positive-real lemma / spectral factor ↔ Riccati
- **Anderson 1999** (review essay) "Old and New Perspectives on the Positive-real Lemma in Systems and Control" — historical sweep from 1962 to 1998. https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1521-4001(199909)79:9%3C579::AID-ZAMM579%3E3.0.CO;2-8
- **MIT 6.245 ch. 8 KYP Lemma notes** — clean modern statement, includes frequency-domain ↔ time-domain ↔ quadratic dissipativity triangle. https://web.mit.edu/6.245/www/images/ch8.pdf
- **Anderson 1973 SIAM J. Control** "Equivalence Relations for the Algebraic Riccati Equation" — establishes one-to-one correspondence between *solutions* of the algebraic Riccati matrix equation and rational-matrix factorizations $W^*W = \Phi$. The progressive specialisation (symmetric → Hermitian → stabilising → positive-definite) tracks the corresponding factorisation refinements. https://epubs.siam.org/doi/10.1137/0311022

### Wiener–Hopf for LQG / spectral-factor algorithms via Riccati
- **Tuel 1968 IBM J. R&D** "Computer Algorithm for Spectral Factorization of Rational Matrices" — early algorithm reducing spectral factorisation of rational matrices to a Riccati-type difference equation via bilinear transform. http://bitsavers.informatik.uni-stuttgart.de/pdf/ibm/IBM_Journal_of_Research_and_Development/122/ibmrd1202D.pdf
- **Varga 2000 IEEE TAC** — "spectral factorisations ... rely essentially on solving for the stabilising solution a standard algebraic Riccati equation of order usually much smaller than the McMillan degree of the transfer function matrix." Confirms the construction: spectral factor = stabilising-ARE solution + back-substitution. https://elib.dlr.de/3506/1/varga_ieeetac2000p2.pdf
- **Sayed & Kailath 2001 NLAA survey** — "Survey of Spectral Factorization Methods", covers scalar/matrix/rational/non-rational cases and explicitly catalogues their interconnections, including the Riccati route. https://asl.epfl.ch/wp-content/uploads/publications/journal_articles/nlaa_2001.pdf
- **Program CC LQG via Wiener–Hopf** (Wiley 1987) — "The LQG optimal control problem ... can be solved using Wiener–Hopf techniques of spectral and partial factorization." Confirms the two routes are alternative computational paths to the same answer. https://onlinelibrary.wiley.com/doi/10.1002/oca.4660080106

### Stochastic realisation theory — bridge between spectral density, ARE, and innovations representation
- **Lindquist & Picci 1979 SIAM J. Control** "On the Stochastic Realization Problem" — classical: given rational spectral density $\Phi$, all minimal Markov realisations correspond to all solutions of a certain algebraic Riccati inequality; the *stabilising* (maximal) solution gives the *innovations representation*, i.e. the steady-state Kalman filter. https://epubs.siam.org/doi/10.1137/0317028
- **Lindquist, Michaletzky & Picci 1995 SIAM J. Control** "Zeros of Spectral Factors, the Geometry of Splitting Subspaces, and the Algebraic Riccati Inequality" — explicit dictionary between spectral-factor zeros and ARE solutions. https://epubs.siam.org/doi/10.1137/S0363012992238667
- **Picci & co. 2014 (arXiv:1410.0765)** "On the Factorization of Rational Discrete-Time Spectral Densities" — discrete-time constructive factorisation, recent. https://arxiv.org/abs/1410.0765
- **Survey (arXiv:1609.02711)** spectral factorisation across applications (optimal estimation, filtering, stochastic realisation, robust control). https://arxiv.org/abs/1609.02711

### Innovations representation = steady-state Kalman = Wiener filter
- **Kailath 1968 IEEE TAC** "An innovations approach to least-squares estimation Part I" — foundational. https://link.springer.com/chapter/10.1007/978-3-662-08546-2_5
- **Devroye / Duke notes** — pedagogical: Wiener filter = LMMSE for stationary process; Kalman filter = sequential LMMSE for state-space process; in steady state and stationary observation, they coincide. https://people.duke.edu/~hpgavin/SystemID/References/Devroye-Wiener+Kalman-2011.pdf

### Operator Riccati for Volterra control (matters for the power-law / rough-vol case in the trading paper)
- **Abi Jaber, Miller, Pham 2019 (arXiv:1911.01903)** "Integral operator Riccati equations arising in stochastic Volterra control problems" — establishes existence/uniqueness of *infinite-dimensional* Riccati equations in $L^1(\mu \otimes \mu)$ for non-Markovian Volterra controlled SDEs. Exactly the right framework when the trading paper's kernel $K$ is non-rational (power-law, rough). https://arxiv.org/abs/1911.01903
- **Abi Jaber, Miller, Pham 2019 (arXiv:1911.01900)** "Linear–Quadratic control for a class of stochastic Volterra equations: solvability and approximation" — companion paper, gives the LQ control framework. https://arxiv.org/abs/1911.01900

### Obizhaeva–Wang propagator ↔ LQ stochastic control (trading-specific bridge)
- **Bank & Voß 2022 (arXiv:2206.03772)** "Reducing Obizhaeva–Wang type trade execution problems to LQ stochastic control problems" — explicit reformulation. Confirms that exponential-resilience execution is genuinely LQ, hence solvable via standard Riccati machinery. The trading paper's §5 result is in this regime. https://arxiv.org/abs/2206.03772
- **Cartea–Jaimungal et al. (arXiv:1611.00997)** "The dynamical allocation problem can be turned into a Linear Quadratic" formulation. Pre-cursor view. https://arxiv.org/abs/1611.00997
- **Obizhaeva & Wang 2013** *Journal of Financial Markets* original paper. https://web.mit.edu/wangj/www/pap/OW_060408.pdf

### H∞ / Krein-space Riccati
- **Hassibi, Sayed, Kailath 1999** *Indefinite-Quadratic Estimation and Control: A Unified Approach to H² and H∞ Theories* (SIAM). Unifies H² (LQG, Riccati) and H∞ (worst-case) under indefinite (Krein-space) quadratic forms; key insight: H∞ filtering/control reduces to *Krein-space Kalman*, with a corresponding *indefinite* Riccati equation. https://authors.library.caltech.edu/records/2h5wx-sj197
- **Sayed & Kailath 1996** "Linear Estimation in Krein Spaces" — same framework, earlier. https://www.academia.edu/10634816/Linear_Estimation_in_Krein_Spaces_Part_I_Theory

### Wiener–Hopf beats Riccati when Riccati blows up (large-DOF)
- **Martini et al. 2022 (arXiv:2201.00361)** "Resolvent-based tools for optimal estimation and control via the Wiener–Hopf formalism" — explicit example: in fluid-mechanics problems with many DOFs, Riccati methods are computationally infeasible; Wiener–Hopf via resolvents stays tractable. https://arxiv.org/abs/2201.00361

## Conceptual claims supported

C1. **The same object.** For stationary infinite-horizon problems with rational kernel/spectrum, the Wiener–Hopf causal factor $K_+$ and the spectral factor from the stabilising solution of an algebraic Riccati equation are literally the same rational function, just expressed in different domains (frequency vs state-space). Anderson 1973, Sayed–Kailath 2001 survey, Tuel 1968.

C2. **KYP lemma is the triangle.** Frequency-domain positive-real condition ⇔ time-domain quadratic dissipativity (LMI) ⇔ existence of a solution to an algebraic Riccati inequality. The Wiener–Hopf factorisation is constructed from the LMI/ARE solution. MIT 6.245 ch. 8; Anderson 1999 review.

C3. **Stochastic realisation theory is the bridge.** Given a rational spectral density $\Phi(\omega)$, finding all causal models that produce $\Phi$ is the same as finding all stabilising solutions of an ARE; the maximal (and unique stabilising) solution gives the *innovations representation* = steady-state Kalman filter = causal Wiener filter. Lindquist–Picci 1979.

C4. **The Kalman ↔ Wiener limit.** In steady state and for stationary processes, the Kalman filter recursion converges to a fixed gain that equals the steady-state Wiener filter. Equivalently: solve the ARE → get the Kalman gain → the closed-loop transfer function = the Wiener filter. Kailath 1968; Devroye notes.

C5. **Where they diverge.** When the kernel/dynamics are *non-rational* (Volterra, power-law, fBm), the spectrum is no longer a finite-degree rational function. Wiener–Hopf still works (the factorisation may not be expressible by elementary functions, but it exists as a Hardy-space operator). Riccati becomes *operator-valued* (infinite-dimensional) — see Abi Jaber, Miller, Pham 2019. This is exactly the regime of the trading paper's power-law / rough kernel.

C6. **OW propagator = LQ.** The Obizhaeva–Wang exponential-resilience model is provably equivalent to a standard LQ stochastic control problem (Bank–Voß 2022). Hence the trading paper's §5 closed-form rule for AR(1) × exponential is, in disguise, the solution of a finite-dimensional DARE.

C7. **H∞ / robust = indefinite Riccati.** Replacing the L² (LQG) norm with H∞ (worst-case) leads to a Krein-space Riccati equation with *indefinite* quadratic form. Hassibi–Sayed–Kailath 1999. This connects to the robust-trading conjecture in `outputs/trading-duality-extensions.md` §7.

C8. **Computational pragmatics.** When state dimension is small, Riccati is preferred (one matrix equation). When state dimension is large or kernel is non-rational, Wiener–Hopf / resolvent methods scale better. Martini et al. 2022.
