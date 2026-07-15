# PNAS Round-1 Fixes — Worker Report

## Files changed

- `papers/markowitz-of-cost-pnas.md` (only paper file touched)
- `reviews/pnas-r1-fixes.md` (this report)

The CHANGELOG was not updated; task did not request it.

## Fixes applied

### FIX 1 — §4.1 inventory-as-signal derivation (math)

Two errors in the previous derivation were corrected:

1. Effective signal formula was wrong for anything other than the terminal-inventory constraint. Cash-neutrality does not contribute a constant.
2. The claim that applying $D_\pm^\beta$ to $\mathbf{1}_{[0,T]}$ produces the Söhngen–Tricomi modes was incorrect (whole-line Marchaud gives $2\beta$-singularity, not $\beta$).

New §4.1 opening:

> Equation (12) holds on $\mathbb{R}$ for a stationary adapted signal. On a bounded horizon $[0,T]$, linear position constraints on the schedule enter (1) through Lagrange multipliers. Each scalar constraint of the form $\int_0^T \psi_k(t)\, u_t\,dt = c_k$ contributes an additive component $\lambda_k \psi_k$ to the effective signal,
> $$\alpha^{\rm eff}_t = \alpha_t + \sum_k \lambda_k\, \psi_k(t), \qquad t \in [0,T],$$
> with $\psi_k$ the constraint's adjoint kernel and $\lambda_k$ its Lagrange multiplier. Terminal inventory $\int_0^T u_t\,dt = -X_0$ gives $\psi_1(t) = \mathbf{1}_{[0,T]}(t)$; cash neutrality $\int_0^T (T-t)\, u_t\,dt = 0$ gives $\psi_2(t) = (T-t)\mathbf{1}_{[0,T]}(t)$. On the finite interval, (11) is replaced by a Fredholm equation on $[0,T]$ whose well-posedness follows from the half-order Riemann–Liouville factorization of Forde–Sánchez-Betancourt–Smith (11). The solution splits into a bulk term of the form (12) applied to $\alpha^{\rm eff}$ plus a contribution from the two-dimensional nullspace of the finite-interval Fredholm operator, spanned by the Söhngen–Tricomi modes $\phi_1(t) = (t(T-t))^{(\gamma-1)/2}$ and $\phi_2(t) = \tfrac{T-2t}{2}\phi_1(t)$ (21, 22) — the classical solutions of the airfoil integral equation; the KKT multipliers $\{\lambda_k\}$ fix the coefficients of these modes.

Corresponding forward references in §1.3(i) and §1.5 rewritten to match: constraint adjoint kernels $\psi_k$, KKT multipliers, finite-interval Fredholm with well-posedness citation to FSS.

### FIX 2 — Prohibited "not X, they are Y" at §1.3(i)

Before:
> Linear position constraints — in particular the terminal-inventory constraint $\int u_t\,dt = -X_0$ that has driven much of the classical literature — are not a separate problem: they are the special case of (1) in which the effective signal contains an additive constant equal to the KKT multiplier of the constraint.

After:
> Linear position constraints — such as the terminal-inventory constraint $\int u_t\,dt = -X_0$ that has driven much of the classical literature — are absorbed into (1) as additive components of the effective signal, one component per constraint, with the constraint's adjoint kernel setting its shape and the KKT multiplier setting its coefficient.

Direct positive assertion. No "not X, they are Y" construction.

### FIX 3 — "empirically dominant" → "empirically supported"

Two occurrences fixed:
- Abstract: "For the empirically dominant power-law kernel" → "for the empirically supported power-law kernel"
- §1.1 last paragraph: same substitution.

### FIX 4 — §1.2 opener

Before: "Problem (1) has a substantial literature."
After: "Problem (1) has been studied under several kernel and signal specifications."

### FIX 5 — §3 closing

Before:
> The projection $P_+$ between the two Cholesky-analog factors is the sole structural addition in the temporal case. It enforces adaptedness and has no cross-sectional counterpart in Markowitz.

After:
> The projection $P_+$ between the two Cholesky-analog factors is the structural addition beyond Markowitz; it enforces adaptedness and has no cross-sectional counterpart.

"Sole" removed.

### FIX 6 — Abstract trimmed to ≤250 words

Two cuts:
- Deleted: "; the projection between the two half-inverses is the signature of the causality constraint" (from sentence about $u^\star = C_+^{-1} P_+ C_-^{-1}\alpha$).
- Deleted: ", and connects optimal execution to fractional-order control" (closing clause; duplicated Sig-Statement content).
- Tightened the mean-variance parallel sentence: "both maximize a linear gain against a positive-definite quadratic penalty, with the impact Hessian ... replacing the return covariance $\Sigma$" reduced to "with the impact Hessian ... replacing the return covariance $\Sigma$".
- Tightened obstruction sentence: "so the naïve solution $C^{-1}\alpha$ is not feasible because it uses future signal values" → "so the naïve solution $C^{-1}\alpha$ uses inaccessible future signal values".
- Opener tightened: "Executing a large order in an electronic market takes time because each trade moves the price and the impact decays only slowly" → "Executing a large order takes time because each trade moves the price and the impact decays slowly".

Final Abstract word count: **246**.

### FIX 7 — Credit FSS in Abstract

Sig Statement (114 w) was already at cap; credit added to Abstract instead.

New Abstract sentence:
> Extending the half-order Riemann–Liouville factorization of Forde, Sánchez-Betancourt and Smith to a general adapted signal, we show that for the empirically supported power-law kernel $G(t) = c\, t^{-\gamma}$, $\gamma\in(0,1)$, the two half-inverses are the causal and anticausal Marchaud fractional derivatives of order $(1-\gamma)/2$ [...]

### FIX 8 — Domain qualifier for $D_-^\beta$ in §2.6 Step 2

Before: "the deterministic bounded operator $D_-^\beta$ acting on the $s$-variable"
After: "the deterministic operator $D_-^\beta$ (bounded on $\dot H^\beta$) acting on the $s$-variable"

### FIX 9 — §1.3(iii) softening

Before: "makes contact with the CRONE / fractional-PID control tradition (18, 19) not previously connected to execution."
After: "makes contact with the CRONE / fractional-PID control tradition (18, 19), to our knowledge not previously connected to execution."

### FIX 10 — Reference renumbering (order of first citation)

Computed the order-of-first-citation by scanning the body top-to-bottom. Mapping (old → new):

| old | new | reference |
|-----|-----|-----------|
|  3  |  1  | Bouchaud–Gefen–Potters–Wyart 2004 |
|  4  |  2  | Gatheral 2010 |
| 16  |  3  | Jusselin–Rosenbaum 2020 |
|  1  |  4  | Markowitz 1952 |
|  2  |  5  | Merton 1972 |
|  5  |  6  | Gatheral–Schied–Slynko 2012 |
|  6  |  7  | Neuman–Voß 2022 |
|  7  |  8  | Abi Jaber–Neuman 2025 |
|  8  |  9  | Abi Jaber–Neuman–Tuschmann 2024 |
|  9  | 10  | Abi Jaber–De Carvalho–Pham 2024 |
| 10  | 11  | Forde–Sánchez-Betancourt–Smith 2022 |
| 11  | 12  | Wiener–Hopf 1931 |
| 12  | 13  | Krein 1962 |
| 13  | 14  | Wiener 1949 |
| 14  | 15  | Arveson 1975 |
| 15  | 16  | Davidson 1988 |
| 17  | 17  | Samko–Kilbas–Marichev 1993 |
| 18  | 18  | Oustaloup 1991 |
| 19  | 19  | Chen–Petráš–Xue 2009 |
| 22  | 20  | Hytönen–van Neerven–Veraar–Weis 2016 |
| 20  | 21  | Söhngen 1939 |
| 21  | 22  | Tricomi 1957 |
| 23  | 23  | Klenke 2014 |

All 24 in-text citation instances remapped (list at end). References section reordered to match.

## Validation output

```
=== style guard ===
canonical: 0 | rather than: 0 | ?: 0
empirically dominant: 0 | substantial literature: 0 | sole structural: 0
'are not a separate problem: they are': 0

=== word counts ===
Sig Stmt:      114
Abstract:      246

=== equation tags ===
15 total, sequential:
\tag{1} \tag{2} \tag{3} \tag{4} \tag{5} \tag{6} \tag{7} \tag{8} \tag{9} \tag{10} \tag{11} \tag{12} \tag{13} \tag{14} \tag{15}

=== references count ===
23

=== citation cross-check ===
body-cited numbers (1..30): [1, 2, 3, ..., 23]  (all 23)
references listed:         [1, 2, 3, ..., 23]  (all 23)
cited but not in refs list: []
in refs list but not cited: []
```

Every reference is cited at least once; every in-text citation resolves.

## Citation instances remapped (for audit)

1. §1.1 "since the early 2000s (3, 4, 16)" → "(1, 2, 3)"
2. §1.1 "Bouchaud–Gatheral propagator model (3, 4)" → "(1, 2)"
3. §1.1 "Markowitz (1, 2)" → "(4, 5)"
4. §1.2 "Gatheral, Schied and Slynko (5)" → "(6)"
5. §1.2 "Neuman and Voß (6)" → "(7)"
6. §1.2 "Abi Jaber and Neuman (7)" → "(8)"
7. §1.2 "cross-impact propagators (8)" → "(9)"
8. §1.2 "battery storage (9)" → "(10)"
9. §1.2 "Forde, Sánchez-Betancourt and Smith (10)" → "(11)"
10. §1.2 "prediction literature (11–13)" → "(12–14)"
11. §1.3(i) "analysis of (5)" → "(6)"
12. §1.3(i) "Forde–Sánchez-Betancourt–Smith (10); they are" → "(11);"
13. §1.3(ii) "half-line convolutions (11–13), ... nest-algebra outer factorization (14, 15)" → "(12–14), ... (15, 16)"
14. §1.3(iii) "with $\gamma\in(0,1)$ (3, 4, 16)" → "(1, 2, 3)"
15. §1.3(iii) "implicit in (10)" → "(11)"
16. §1.5 "$\phi_2(t) = (T-2t)\phi_1(t)/2$ (20, 21)" → "(21, 22)"
17. §1.5 "schedule of (5)" → "(6)"
18. §2.3 "Krein's theorem (12)" → "(13)"
19. §2.4 "causal-realization theorem (13) ... nest-algebra outer factorization (14, 15)" → "(14) ... (15, 16)"
20. §2.6 "$s$-variable (22, Prop. 2.6.13)" → "(20, Prop. 2.6.13)"
21. §4.1 "Forde–Sánchez-Betancourt–Smith (10). The solution" → "(11)."
22. §4.1 "$\phi_2(t) = \tfrac{T-2t}{2}\phi_1(t)$ (20, 21)" → "(21, 22)"
23. §4.1 "Gatheral–Schied–Slynko (5)" → "(6)"
24. §5 Proof of Lemma 1: "See (13, ch. 8) and (14, 15)" → "See (14, ch. 8) and (15, 16)"

Unchanged citations (old = new): (17), (17, §5.4), (17, §5.3 Thm 5.3), (18, 19), (23, Thm 14.16).

## Anything that surprised me

- The Abstract came in at 251 words after the FSS credit + primary two-clause cut. Needed one more word trimmed. Did so by tightening the opener sentence ("in an electronic market" removed; "only slowly" → "slowly"), landing at 246.
- The first edit-block attempt (24 citation replacements at once) failed atomically because one oldText, "nest-algebra outer factorization (14, 15).", appeared twice (§1.3(ii) and §2.4). Recovered by folding each of those into a combined longer-context edit; both instances remapped correctly.
- Rejected the temptation to also renumber via a scripted pass — the mapping has non-fixed points that overlap with the range of equation-tag numbers (1–15), so a naïve regex renumber would corrupt equation references. Manual context-anchored replacements are safer.

## Left undone

- CHANGELOG entry (task did not request one).
- Full-line proof-read after all edits for prose polish beyond the specified fixes.
- Any items outside the fix list from round-1 (Markowitz-vs-Wiener-Kolmogorov framing was explicitly deferred by the parent; §4.1 was corrected but not expanded into a finite-T theorem, per instructions).
