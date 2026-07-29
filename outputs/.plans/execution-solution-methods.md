# Literature Review Plan — Solution methods for optimal trading with impact

## Object under review
`v2/optimal-trading-filters-v2.tex` (Smerlak, "Optimal Trading Filters: a Wiener–Hopf Approach"). The paper claims to *unify/recover* existing solution methods for the linear-quadratic optimal-trading problem with temporary + transient (propagator) impact + inventory risk and a predictive signal.

## Research question
1. Does the paper **accurately represent** the existing solution methods it cites?
2. Is the paper **missing** any solution-method families for this problem class?

## The paper's claims to test
- §1 abstract: "Existing treatments characterize the optimal policy implicitly, as the solution of an integral equation or an equivalent forward–backward system."
- §1.4: finite-horizon methods produce the inverse as "a resolvent series, a Wiener-chaos expansion, or the solution of a Riccati system."
- §5 recovery mapping: Markowitz (memoryless), Gârleanu–Pedersen aim portfolio, Neuman–Voß (stationary), Gatheral–Schied–Slynko liquidation, Forde et al. finite-horizon power-law.
- Cited method attributions: GSS = deterministic/Fredholm; LN/NV/BSV = signal-adaptive under temporary+exp resilience; AJN = stochastic Volterra 2nd kind; AJNT = operator-resolvent; Forde = Wiener chaos/Fredholm; GP = LQ/aim (DP).

## Method-family taxonomy to confirm/complete
1. Deterministic calculus of variations / Fredholm (Almgren–Chriss; Gatheral–Schied–Slynko).
2. Stochastic control / HJB / LQ-Riccati (Gârleanu–Pedersen; Cartea–Jaimungal; Guéant).
3. FBSDE / stochastic maximum principle (Neuman–Voß; Bank–Soner–Voß; Lehalle–Neuman).
4. Stochastic Volterra equations / operator resolvent (Abi Jaber–Neuman; Abi Jaber–Neuman–Tuschmann).
5. Wiener chaos / Fredholm on chaos (Forde–Sánchez-Betancourt–Smith).
6. Wiener–Hopf / spectral factorization (the paper's method — is it used elsewhere in execution?).
7. Convex duality / martingale-completeness (does an execution-specific dual method exist beyond Rockafellar–Wets?).
8. Candidate MISSING families: signature methods (Kalsi–Lyons–Perez Arribas); deep-BSDE / neural solvers; reinforcement learning; viscosity/singular control (proportional costs); mean-field games; rough-impact.

## Source types
- Paper search (alpha_search) for method families and the specific cited works.
- Web search for surveys/taxonomies and for methods possibly omitted.
- Direct paper Q&A (alpha_ask_paper) to confirm the *method* used by GP, NV, AJN, Forde, GSS.

## Task ledger
- [ ] T1 confirm GSS solution method (Fredholm / Euler–Lagrange) — status: pending
- [ ] T2 confirm GP method (DP/LQ, discrete + continuous) — pending
- [ ] T3 confirm NV / BSV / LN method (FBSDE / Riccati) — pending
- [ ] T4 confirm AJN / AJNT method (stochastic Volterra / operator resolvent) — pending
- [ ] T5 confirm Forde et al. method (Wiener chaos / Fredholm) — pending
- [ ] T6 Wiener–Hopf in execution literature — is the paper's method novel here? — pending
- [ ] T7 convex-duality methods for execution beyond the paper's remark — pending
- [ ] T8 candidate missing families (signatures, deep-BSDE, RL, MFG, rough) — in/out of scope? — pending

## Verification log
(to be filled: each accepted claim needs a source URL; each method attribution needs paper confirmation)

## Deliverables
- Publication/evidence notes: `notes/execution-solution-methods-publications.md`
- Researcher outputs: `execution-solution-methods-research-*.md`
- Final: `outputs/execution-solution-methods.md`
- Provenance: `outputs/execution-solution-methods.provenance.md`
