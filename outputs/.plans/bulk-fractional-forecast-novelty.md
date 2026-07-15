# Plan: novelty of bulk fractional-derivative-of-forecast solution

**Topic.** How novel is the closed-form bulk-policy expression
$u^{\rm bulk}_t = \kappa_{1-\gamma}\,\mathbb{D}^{1-\gamma}\bar\alpha(t,\cdot)(t)$
— a Riesz fractional derivative of order $1-\gamma$ applied to the conditional
forecast curve, for the propagator model with power-law kernel $G(t)=c|t|^{-\gamma}$?

**Slug.** `bulk-fractional-forecast-novelty`

## Scope

- **Time period.** Roughly 1995–2026 (Bouchaud propagator era forward), plus
  classical references on Wiener filtering (1949), Wiener–Hopf (1931),
  Krein (1958/62), Söhngen (1939) for the underlying fractional-integral
  inversion machinery.
- **Source types.** Optimal-execution papers (arXiv + journals), fractional-
  calculus textbooks for the inversion identity itself, and control-theory
  references for CRONE / fractional PID where similar operators appear in
  different problems.

## Key questions

1. Has the **explicit closed-form** $u^* \propto \mathbb{D}^{1-\gamma}\bar\alpha$
   been stated previously in the optimal-execution literature?
2. Has the **fact** that solving the Fredholm/Wiener-Hopf equation with
   power-law kernel $G(t)=c|t|^{-\gamma}$ corresponds to applying a Riesz
   fractional derivative been articulated (even if not in this notation)?
3. How does the formula relate to:
   - Almgren–Chriss (constant impact, no propagator memory)?
   - Gârleanu–Pedersen (linear quadratic with mean-reverting signal,
     finite-dim state)?
   - Bouchaud / Gatheral propagator models (power-law impact, no closed
     form usually)?
   - Forde–Sánchez-Betancourt–Smith (Gaussian signal + power-law resilience)?
   - Abi Jaber–Neuman (Volterra/propagator + signal, BSDE characterization)?
   - Curato–Gatheral–Lillo (non-linear transient impact)?
   - Cartea–Jaimungal / Neuman–Voß (signal-adaptive trading with
     temporary+transient impact)?
4. What is the **novel contribution** of writing this as a fractional
   derivative, versus an inverse Fredholm operator? Is the novelty in:
   - The identification of the inverse symbol $|\xi|^{1-\gamma}$ as a
     Riesz derivative?
   - The application to the *forecast curve* rather than to the realized
     signal?
   - The bulk/boundary decomposition spine?
   - The Wiener–Hopf factorization revealing causal realization?
   - The connection to CRONE fractional PID?
5. What prior fractional-calculus work has appeared in optimal execution
   specifically (vs. fractional Brownian motion for the underlying)?

## Source checklist (target list)

- Bouchaud–Gefen–Potters–Wyart 2004 (propagator origin)
- Gatheral 2010, Gatheral–Schied–Slynko 2012 (propagator + Fredholm)
- Curato–Gatheral–Lillo 2017 (non-linear transient impact)
- Obizhaeva–Wang 2013 (exponential propagator → closed-form, special case)
- Almgren–Chriss 2000/2001 (no propagator)
- Gârleanu–Pedersen 2013 (DTPC, linear quadratic, mean-reverting signal)
- Cartea–Jaimungal 2016 (signal-adaptive)
- Forde–Sánchez-Betancourt–Smith 2022 (Gaussian + power-law resilience)
- Neuman–Voß 2022 / 2023
- Abi Jaber–Neuman 2022, Abi Jaber–Neuman–Tuschmann 2024, Abi Jaber et al. 2025
- Webster 2023 (Handbook)
- Jusselin–Rosenbaum 2020 (no-arbitrage → rough vol; not exec but cited)
- Fractional Calculus in Optimal Control survey arXiv:2512.12111 2025
- Older: Söhngen 1939, Tricomi 1957, Krein 1962, Noble 1958
- Oustaloup CRONE 1991, 2000

## Task ledger

| # | Task | Status |
|---|---|---|
| 1 | Plan & directory setup | done |
| 2 | Literature search via web_search for "Riesz fractional derivative optimal execution forecast" and variants | pending |
| 3 | Targeted alphaXiv search on key papers (Abi Jaber–Neuman, Forde–Sánchez-Betancourt, Neuman–Voß) for explicit fractional-operator formulations | pending |
| 4 | Read survey arXiv:2512.12111 abstract/intro to see what fractional-control-in-finance literature it covers | pending |
| 5 | Synthesize: classify the formula's novelty across (a) operator identification, (b) forecast-curve substitution, (c) bulk/boundary spine | pending |
| 6 | Write evidence draft `<slug>-research-evidence.md` | pending |
| 7 | Write final review `outputs/<slug>.md` | pending |
| 8 | Write provenance `outputs/<slug>.provenance.md` | pending |

## Verification log

| Claim | Source | Status |
|---|---|---|
| (to be filled as evidence is gathered) | | |

## Subagent decision

The topic is narrow enough (a specific formula) and I already have most of
the relevant priors from this project's reference base. Lead-owned review;
spawn `verifier` only if the cited draft has many unverified URLs after
synthesis.
