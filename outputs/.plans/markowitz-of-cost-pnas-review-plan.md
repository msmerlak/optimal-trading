# Review Plan — markowitz-of-cost-pnas

## Artifact
- Path: `papers/markowitz-of-cost-pnas.md`
- Type: local Markdown, PNAS-format position paper (~4281 words, 21 refs).
- Title: *Fractional Derivatives as the Markowitz Rule for Cost-Managed Trading*.

## Review criteria
1. **Novelty positioning** — vs. Gatheral–Schied–Slynko (6), Neuman–Voß (7), Abi Jaber–Neuman (8), Forde–Sánchez-Betancourt–Smith (11). Is the "signal-adaptive fractional-derivative closed form" genuinely new? What does the paper claim as new vs. classical?
2. **Mathematical rigor** — Lemma 1 (adapted inverse), Theorem 1 (bulk theorem), symbol factorization on homogeneous Sobolev spaces, Marchaud vs. Riemann–Liouville identifications, conditional Fubini used in Step (a) of Theorem 1 proof.
3. **Consistency of framing** — Markowitz analogy: Table 1 rows, factorization claims, whitening claims. Bregman/Wiener–Kolmogorov connection in §3.2.
4. **Claims validity** — every unqualified assertion traceable to (a) a reference, (b) a proof in §5, or (c) an example. Are there overclaims (e.g. about closed forms, uniqueness, admissibility)?
5. **Reproducibility** — no data used (stated). Are all objects defined precisely enough that another researcher could reconstruct the proofs?
6. **Boundary corrections / temporary impact / multi-asset** (§4.1–4.3) — are these gestural or precise? Do they contain hidden claims that need proofs?
7. **Writing quality** — PNAS format compliance (significance ≤120w, abstract ≤250w, no equations in abstract), style rules from AGENTS.md (no rhetorical questions, no "rather than", no "X is not Y, it is Z", no forbidden words).
8. **Reference completeness** — placeholder volume/pages, correct arXiv IDs, missing citations for classical results.

## Verification checks
- Word counts: significance, abstract, total.
- Equation numbering consistency (equations tagged 1–15).
- Referenced equation numbers (§3.2 cites (11) and (13); §2.7 cites (14); §4.2 cites (12)) — check all point to real equations.
- Cross-references between §1.1 (dual norms), §1.3 (contribution), §2 (theorems), §3.1 (Table 1), §3.2 (WK reading).
- Ref list numbering matches in-text citations.
- No forbidden style patterns from AGENTS.md.
- Claim that $C^{-1} = C_+^{-1} C_-^{-1}$: verify factorization order matches Fourier symbol convention $\hat C = \hat C_- \hat C_+$.
- Claim that $C_+^\ast = C_-$: verify adjoint direction.
- $\zeta_s = \theta^\nu \alpha_s$ for OU: check Marchaud integration constant.
- $\kappa_{1-\beta} = [2\Gamma(1-\beta)\sin(\pi\beta/2)]^{-1} = c_\beta^{-1}$: check $c_\beta$ definition consistency.
- Bregman-projection framing implicit in §3.2 completing-the-square derivation.

## Reviewer stance
Structural/mathematical position paper for PNAS. Not empirical. Expect: probability-theory reviewer will scrutinize adaptedness, filtration-Wiener–Hopf mechanics, and Sobolev-space definitions of the factors; a mathematical-finance reviewer will scrutinize the propagator/no-arbitrage claims and the relationship to (8) resolvent framework.
