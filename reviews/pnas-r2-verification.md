# PNAS Round-2 Verification

## Validation output

```
=== word counts ===
Abstract:  246   (≤ 250 ✓)
Sig Stmt:  114

=== style guard (grep -iE, whole file) ===
empirically dominant     : 0
substantial literature   : 0
rich literature          : 0
sole structural          : 0
canonical                : 0
genuinely                : 0
not a separate problem   : 0
rather than              : 0
naturally                : 0
elegant                  : 0
"it is worth" / "importantly" / "interestingly" : 0
not merely               : 0

=== equation tags ===
15 total, sequential: \tag{1} … \tag{15}  ✓

=== references ===
23 entries, numbered 1–23 sequentially ✓
```

Spot-checked citations resolve as expected:

| Author (first mention)          | Cite in body | Ref list entry |
|---------------------------------|--------------|-----------------|
| Bouchaud–Gefen–Potters–Wyart '04 | §1.1 `(1, 2, 3)` first slot | 1 ✓ |
| Markowitz 1952                  | §1.1 `(4, 5)` first slot    | 4 ✓ |
| Gatheral–Schied–Slynko 2012     | §1.2 `(6)`                  | 6 ✓ |
| Forde–Sánchez-Betancourt–Smith  | §1.2 `(11)`                 | 11 ✓ |
| Hytönen (Prop. 2.6.13)          | §2.6 `(22, Prop. 2.6.13)`   | 22 ✓ |

Note: the fix-worker's mapping table in `pnas-r1-fixes.md` lists Söhngen as "20→21", Tricomi "21→22", Hytönen "22→20", but the actual paper has Söhngen=20, Tricomi=21, Hytönen=22. The paper's ordering is the correct one (§1.5 cites Söhngen–Tricomi at line 75 before §2.6 cites Hytönen at line 111), and in-text cites `(20, 21)` for Söhngen–Tricomi and `(22, Prop. 2.6.13)` for Hytönen are consistent with the reference list. The mapping table in the fix report is mis-transcribed but the file itself is internally consistent. Worth noting but not a blocker.

---

## Review

### (a) Blockers found in round 2
None.

### (b) Regressions from round-1 fixes
None. Grep of the whole paper shows all previously banned phrases removed; §4.1 rewrite introduces no new prohibited constructions (no "rather than", "canonical", "naturally", "elegant", rhetorical questions, or `not X — it is Y` framings).

### (c) Round-1 items still not adequately addressed
None.

### (d) Round-1 fixes correctly applied

1. **§4.1 math rewrite** (lines 195–205, plus §1.3(i) at 59 and §1.5 at 75). Verified:
   - Effective signal is now $\alpha^{\rm eff}_t = \alpha_t + \sum_k \lambda_k\psi_k(t)$ with general $\psi_k$ — not restricted to a constant.
   - Adjoint kernels stated correctly: terminal inventory gives $\psi_1 = \mathbf 1_{[0,T]}$; cash-neutrality $\int(T-t)u_t\,dt = 0$ gives $\psi_2(t) = (T-t)\mathbf 1_{[0,T]}$. Both match the definition of adjoint kernel for the corresponding scalar linear functional.
   - Söhngen–Tricomi modes now described as spanning "the two-dimensional nullspace of the finite-interval Fredholm operator" — no residual claim that whole-line Marchaud applied to $\mathbf 1_{[0,T]}$ yields them.
   - Well-posedness on $[0,T]$ credited to Forde–Sánchez-Betancourt–Smith (11).
   - §1.3(i) forward-reference reframed as "response of the finite-interval Fredholm operator to this effective signal, with well-posedness on $[0,T]$ inherited from Forde–Sánchez-Betancourt–Smith (11)"; §1.5 reframed to "resulting finite-interval Fredholm operator has a two-dimensional nullspace spanned by the Söhngen–Tricomi modes." Both consistent with §4.1.

2. **§1.3(i) construction fix** (line 59). Now reads "Linear position constraints … are absorbed into (1) as additive components of the effective signal…" — direct positive assertion, no "not X, they are Y".

3. **"empirically dominant"** — 0 occurrences (Abstract line 21 and §1.1 line 31 both say "empirically supported").

4. **§1.2 opener** (line 53): "Problem (1) has been studied under several kernel and signal specifications." Concrete, non-boilerplate.

5. **§3 closing** (line 191): "the structural addition beyond Markowitz" — "sole" removed; no overstatement.

6. **Abstract word count**: 246 (verified `awk … | wc -w`).

7. **FSS credit in Abstract** (line 21): "Extending the half-order Riemann–Liouville factorization of Forde, Sánchez-Betancourt and Smith to a general adapted signal, we show that for the empirically supported power-law kernel …". Integrated as the transition sentence from the general operator result to the power-law specialization; reads naturally.

8. **§2.6 Step 2 domain qualifier** (line 141): "the deterministic operator $D_-^\beta$ (bounded on $\dot H^\beta$) acting on the $s$-variable" — qualified.

9. **§1.3(iii) CRONE softening** (line 69): "makes contact with the CRONE / fractional-PID control tradition (18, 19), to our knowledge not previously connected to execution." ✓

10. **Reference renumbering**: 23 entries in reference list, numbered 1–23; all five spot-checked cites resolve correctly. Body-cited numbers ⊆ {1,…,23}; equation-numbers `(1)`–`(15)` are all references to equations, not citations (verified by inspection of every low-number `(k)` occurrence).

### (e) New items worth fixing that weren't in round 1
Minor / discretionary:

- **Fix-report mapping table typo**: `reviews/pnas-r1-fixes.md` (audit table under FIX 10) lists Söhngen→21, Tricomi→22, Hytönen→20. The paper itself has Söhngen=20, Tricomi=21, Hytönen=22 (which is the correct order-of-first-citation). The paper is right; the audit table entry is mis-transcribed. Not a paper blocker; worth correcting the audit report for future reviewers.
- **§1.5 vs §4.1 slight framing mismatch**: §1.5 (line 75) describes the constraint absorption as "adding a term $\lambda_k\psi_k$ to the effective signal per scalar constraint", while §4.1 (line 197) uses the same formula. Consistent, but §1.5 gives no example of $\psi_k$ while §4.1 does. Not a defect; noting for completeness.
- **§4.1 sentence length** (line 203): the "The solution splits …" sentence is long (~90 words with two em-dash clauses). Readable but dense. Discretionary polish only.
