# Plan: Literature Context for Stationary Quadratic-Cost Optimal Execution

**Slug:** `stationary-quadratic-execution-context`
**Date:** 2026-07-11
**Objective:** Place the "Fractional Derivatives as the Markowitz Rule for Cost-Managed Trading" paper's two central assumptions — (i) quadratic/linear-impact cost model, (ii) stationary trading on the whole line (far from boundaries) — in their proper literature context. The output should let a reader see exactly which lineage the paper extends, which lineages it does not address, and what the scholarly division of labor between quadratic-vs-concave impact and finite-horizon-vs-stationary settings looks like.

## Scope

**In-scope.**
- Quadratic-cost / linear-impact optimal execution: Almgren–Chriss and successors.
- Transient linear impact via propagator kernels: Bouchaud–Gefen–Potters–Wyart, Gatheral, Alfonsi et al., Gatheral–Schied–Slynko.
- Signal-adaptive execution under linear impact: Cartea–Jaimungal, Neuman–Voß, Abi Jaber–Neuman.
- Stationary / infinite-horizon or whole-line formulations vs. finite-horizon with terminal-inventory.
- The Söhngen–Tricomi / airfoil-equation route to fractional-integral finite-interval solutions.
- Empirical evidence on impact shape: Lillo–Farmer–Mantegna, Bouchaud et al., Toth et al. on square-root law.

**Out-of-scope.**
- LOB microstructure models (Obizhaeva–Wang, Alfonsi–Fruth–Schied) beyond noting the alternative modelling stream.
- Fully nonlinear/concave impact optimal execution (mentioned briefly for contrast).
- High-frequency trading strategies as such.
- Cross-impact between assets (mentioned briefly).

## Key Questions

1. **Where does the quadratic-cost assumption sit in the literature?** Which foundational papers rely on it, why, and what is the alternative (concave/square-root impact)?
2. **Where does the stationary / whole-line assumption sit?** Almost the entire signal-adaptive execution literature works on bounded horizons — what is the exception?
3. **How does the "far from boundaries" / interior-asymptotic framing connect to the classical Söhngen–Tricomi / boundary-layer literature on the airfoil equation?**
4. **What is the scholarly division between (a) finite-horizon + terminal-inventory + no signal (Almgren–Chriss, GSS), (b) finite-horizon + signal (Neuman–Voß, Abi Jaber–Neuman), (c) stationary + signal (paper under review)?**
5. **Why has the stationary/whole-line, signal-adaptive, power-law-impact case not been solved before?** What tools were missing?
6. **How does the paper's quadratic-cost assumption interact with empirical evidence for square-root impact?** Is the paper's model empirically defensible, and if so, in what regime?

## Source Types to Search

- **Primary papers** via `alpha` CLI (alphaXiv-backed): Almgren-Chriss, Gatheral-Schied-Slynko, Neuman-Voß, Abi Jaber-Neuman, Forde-Sánchez-Betancourt-Smith, Lillo-Farmer-Mantegna, Bouchaud et al., Toth et al., Cartea-Jaimungal.
- **Textbooks / surveys**: Cartea-Jaimungal-Penalva ("Algorithmic and High-Frequency Trading"), Guéant ("The Financial Mathematics of Market Liquidity"), Bouchaud-Bonart-Donier-Gould ("Trades, Quotes and Prices").
- **Web** for recent 2024–2025 developments and empirical calibration.
- **arXiv search** for "stationary optimal execution", "infinite horizon transient impact", "power-law impact fractional".

## Task Ledger

| ID | Task | Status |
|---|---|---|
| T1 | Draft plan | done |
| T2 | Search: quadratic-cost lineage | pending |
| T3 | Search: stationary/infinite-horizon executions | pending |
| T4 | Search: concave-impact empirical evidence and scope | pending |
| T5 | Search: signal-adaptive execution 2020–2025 | pending |
| T6 | Search: airfoil-equation / Söhngen–Tricomi in finance | pending |
| T7 | Synthesize literature map by (quadratic vs concave) × (finite vs stationary) × (signal vs no signal) | pending |
| T8 | Draft literature review with lineage tree | pending |
| T9 | Verifier pass (citation URLs) | pending |
| T10 | Reviewer pass (unsupported claims, gaps) | pending |
| T11 | Save final artifact + provenance | pending |

## Verification Log

Claims requiring verification (populated during search):
- (populated during Gather phase)

## Expected Sections

1. Introduction: the two assumptions, why they matter
2. The quadratic-cost lineage
3. The stationary-vs-finite-horizon division
4. Empirical vs. theoretical impact-shape assumptions
5. A 2×2×2 map: (quadratic vs. concave) × (finite-horizon vs. stationary) × (signal vs. no-signal)
6. Where the paper sits
7. What is left open
8. References

## Delivery

- `outputs/stationary-quadratic-execution-context.md` — final literature review
- `outputs/stationary-quadratic-execution-context.provenance.md` — sources consulted/accepted/rejected, verification status
- Intermediate research files: `outputs/.drafts/stationary-quadratic-execution-context-*.md`
