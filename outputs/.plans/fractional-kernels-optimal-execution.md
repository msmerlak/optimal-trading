# Plan: Power-law kernels ↔ fractional derivatives in optimal execution

## Research question
In optimal execution / optimal trading literature, has anyone explicitly linked **power-law decay kernels** (transient market impact, propagator models, Volterra-type models) with **fractional derivatives**, so that the optimal trading rate / policy is expressed as a fractional derivative (Riemann–Liouville, Caputo, Marchaud, or Riesz) of the alpha/signal or of the price process?

Underlying mathematical fact: the inverse of a power-law convolution kernel `K(t) ∝ t^{-β}` is (up to constants) a fractional derivative operator of order `β` (or `1-β`), via the Riemann–Liouville fractional integral being convolution with `t^{α-1}/Γ(α)`. So if the optimal control involves inverting a power-law impact/decay kernel acting on a signal, the optimal policy should formally be a fractional derivative of that signal. Question: who has written this explicitly?

## Sub-questions / task ledger
- [x] Q1 — done. Power-law impact → Abel integral equation (Gatheral-Schied-Slynko 2012; Curato-Gatheral-Lillo 2017). Abel inversion = Riemann-Liouville fractional derivative.
- [x] Q2 — done. Abi Jaber & Neuman (2024) and successors label `c(t-s)^{α-1}` *the* "fractional kernel"; solve via operator/Nyström, not explicit fractional-derivative policy.
- [x] Q3 — done. Direct hit: **Forde, Sánchez-Betancourt, Smith (QF 2022)** — explicitly writes the Fredholm operator as `B^{-1} I_ν B` and inverts via `D_r` (fractional derivative).
- [x] Q4 — done. Gârleanu-Pedersen use quadratic / exponential transient cost; no fractional structure. Signal-adaptive power-law work is the Forde et al. branch.
- [x] Q5 — done. Jusselin-Rosenbaum (2020) derives why impact *must* be power-law; rough-volatility branch supplies the fBm/Hurst analogy.
- [x] Q6 — done. Engineering analogue exists (fractional PID, fractional LQR, e.g. arXiv 2512.12111) but not used in finance literature.

## Source types
- arXiv (q-fin.TR, q-fin.MF, math.OC), SSRN, Journal of Financial Econometrics, Math Finance, SIFIN, Quant Finance.
- Web search for recent (2022–2026) papers and reviews.
- Code repos only if a candidate paper has an implementation that would clarify the claim.

## Expected sections
1. Setup: power-law kernels in execution & their inverse as fractional operators (math note).
2. Direct hits: papers that explicitly use fractional derivatives as optimal policy.
3. Adjacent: Volterra/rough optimal execution that implicitly contains the link.
4. Propagator-model optimal execution (Gatheral-Schied-Slynko etc.) and where fractional calculus appears.
5. Gaps / open questions.

## Verification log
- Forde-Sánchez-Betancourt-Smith write `T = B^{-1} I_ν B` and `I_ν^{-1} = Γ(1-r) D_r` — VERIFIED in PDF (ORA Oxford copy, p.590-591). https://ora.ox.ac.uk/objects/uuid:0c794b99-5276-48e4-90d7-60a127082c26
- Abi Jaber-Neuman 2211.00447 calls `c(t-s)^{α-1}` the "fractional kernel" — VERIFIED in 2409.12098 Eq. (2.7) (same authorship family).
- Gatheral-Schied-Slynko (2012) Abel equation for power-law — VERIFIED via citation chain in Forde et al. (Ex. 2.30 ref) and Curato-Gatheral-Lillo (2017) Sec 2.2 mentioned in Forde p.586.
- Jusselin-Rosenbaum 2020 "no-arbitrage ⇒ power-law impact" — VERIFIED on Wiley DOI page.
- Curato-Gatheral-Lillo Sec 2.2 Abel inversion — SINGLE-SOURCE cited via Forde p.586; not opened directly. Mark INFERRED for the exact section number; primary claim (Abel inversion of power-law) is multiply attested.

## Tactics
- Narrow topic — search directly via `web_search` + `alpha` CLI; no researcher subagent needed.
- Use `verifier` subagent for citations, `reviewer` subagent for final pass.
