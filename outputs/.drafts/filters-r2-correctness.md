# Round-2 Verification: `optimal-trading-filters.tex` (correctness + regressions)

**Scope:** verify the Round-1 fix pass only (the delta), not a fresh full review. READ-ONLY.
**Result:** Compiles clean (pdflatex exit 0, 12 pp), no undefined refs/citations. **No blockers.** Two minor scoping/wording items below. All ten requested checks pass.

Method: recompiled the paper; ran `experiments/risk_response_check.py` (read-only) plus targeted finer-grid reruns to confirm the §6.3 table; re-derived each flagged identity by hand.

---

## BLOCKERS (new errors or incorrect fixes)

None.

---

## FIXES STILL NEEDED (minor; non-blocking)

### M1 — "H lies in L² for every kernel" is true only with inventory risk present (§3 remark)
> "The position filter $H = \hat g/(-i\xi)$ lies in $L^2$ for every kernel; the rate filter $\hat g$ lies in $L^2$ under the spectral-decay hypothesis of Appendix~B..."

The position-in-$L^2$ property is a consequence of the risk penalty, which enters the friction energy as $\lambda\|x\|^2$ (the $\lambda/\xi^2$ term of $q$). For $\lambda>0$, finite friction energy forces $x\in L^2$, so $H\in L^2$ — verified: $|H|^2=(\theta\sigma/\Phi)^2/[(\theta^2+\xi^2)N(\xi)]$, integrable at both ends when $N(0)=\lambda>0$ and $N(\infty)$ finite/growing. But at $\lambda=0$ (pure temporary or pure power-law impact) $N(0)=0$ and $|H|^2\sim 1/\xi^2$ near $\xi=0$: the position is nonstationary and $H\notin L^2$. This is exactly the case the paper flags elsewhere as needing the dense-domain/spectral-decay treatment (§3 OU note, Concluding Remarks: "any $\eta>0$ or $\lambda>0$ restores bounded inverses"). Appendix C is more careful here — it writes the position filter vanishes at high frequency "for every kernel **considered**." Recommend aligning the §3 remark: "for every kernel with inventory risk $\lambda>0$" (or "for every kernel considered"). Not a math error in the intended three-friction setting; only the unqualified universal quantifier is loose.

### M2 — "comparable" quadrature-bias claim is same-order but slightly generous (§6.3)
> "...the residual power-law discrepancy is comparable to the quadrature bias of the singular kernel measured at the analytically known $\lambda=0$ point on the same grid."

On the row-4 grid ($dt=0.01$): power-law row-4 discrepancy is $10.8\%$ ($0.325$ vs formula $0.364$); the $\lambda=0$ analytic-point ($\theta=1$) quadrature bias on the same grid is $6.2\%$ ($0.374$ vs $0.399$). Same order of magnitude, within a factor ~1.7. The hedge "comparable" is defensible but on the optimistic side; acceptable as written given the softened phrasing. Flagging only so the author knows the numbers (10.8% vs 6.2%), not the ~equal the word might suggest.

---

## NON-ISSUES VERIFIED (fixes correct, no regressions)

### (1) Admissibility sentence §2.1 — correct and sufficient
> "Admissible controls are adapted processes of finite friction energy $\E\langle u, Qu\rangle<\infty$; for $\eta=0$ this class admits rates with a white-noise component (\S6), whose position $x$ remains in $L^2$."

- Sufficient for Theorem 1's "unique adapted optimum": the friction energy $\E\langle u,Qu\rangle=\frac1{2\pi}\int q|\hat u|^2$ is a genuine Hilbert-space norm since $q>0$ a.e.; the gain functional $u\mapsto\E\int u\alpha$ is bounded in this norm with $|{\cdot}|\le\|u\|_Q\|\alpha\|_{Q^{-1}}$, and $\|\alpha\|_{Q^{-1}}^2=\frac1{2\pi}\int S_\alpha/q=2\,v_{\rm ant}<\infty$ under the standing (Szegő + decay) assumptions. Projection theorem on the closed adapted subspace gives existence + uniqueness. This is exactly the right well-posedness class.
- Consistent with the $\eta=0$ white-noise atom: for a kink kernel (e.g. $e^{-\kappa|t|}$), $q(\xi)\to A/\xi^2$ as $\xi\to\infty$ ($A=2\kappa\gamma+\lambda$), so a white-noise rate ($\hat u=$const) has *finite* friction energy $\int(A/\xi^2)\,d\xi<\infty$ — admissible. The friction energy contains the $\lambda|\hat x|^2$ term, so finite energy $\Rightarrow \lambda\|x\|^2<\infty\Rightarrow x\in L^2$. Statement correct (with $\lambda>0$, which is the setting of §6). Power-law cusp has $c_1=0$, no atom — consistent.

### (2) Rescoped Theorem 2 — correct and consistent with App. B/C
Theorem 2 statement no longer carries $\hat g\in L^2$ as a blanket hypothesis (confirmed: `eq:filter`/`eq:value` are stated unconditionally). The remark's $H$-vs-$\hat g$ split is mathematically correct:
- $H=\hat g/(-i\xi)=(\theta/\Phi)\varphi_+/N_+$ for OU; $\hat g\in L^2$ requires $\int(1+\xi^2)S_\alpha/q\,d\xi<\infty$ (App. B). For the $\eta=0$ kink kernel this integrand $\sim \xi^2/A\to$const, so the integral **diverges** — the hypothesis fails exactly where the remark says a white-noise atom appears. Fully consistent.
- Cross-checked App. B algebra: $Q_-^{-1}=i\xi/N_-$, so $h=Q_-^{-1}\varphi_+=N_-^{-1}(i\xi)\varphi_+$ matches the "$h=N_-^{-1}(i\xi)\varphi_+$" line. (See M1 for the one loose quantifier.)

### (3) Riesz-projection convention — consistent, OU pole-cancellation intact
§3 "truncation to strictly positive lags, with any lag-zero atom annihilated" now matches App. B "atoms at lag zero ... are likewise annihilated." This convention is *required* for the OU result: verified $h-(\theta/\Phi)\varphi_+ = -\sigma N_-^{-1}+\sigma\theta[N_-^{-1}-N_-(-i\theta)^{-1}]/(\theta-i\xi)$ is an identity (algebra checks: RHS $=\sigma i\xi/(N_-(\theta-i\xi))=h$). The $-\sigma N_-^{-1}$ piece tends to $\sigma/\sqrt A\neq0$ at high frequency for the kink kernel — a genuine lag-zero atom — which only the "atom annihilated" convention removes to leave $\Pi_+h=(\theta/\Phi)\varphi_+$. Pole at $\xi=-i\theta$ cancels via $N_-(-i\theta)=N_+(i\theta)=\Phi$. Goes through.

### (4) Lemma 1 reverse-identity line — correct
> "The reverse identity ... follows the same way (using that $Q_-$ preserves the orthogonal complement), or from positivity of $P_+QP_+$ ..., for which a left inverse is two-sided."

Direct route verified: for adapted $\alpha$, $(P_+QP_+)(Q_+^{-1}P_+Q_-^{-1})\alpha=P_+Q_-P_+Q_-^{-1}\alpha$ (using $Q_+^{-1}$ causal $\Rightarrow$ preserves adapted subspace, so the inner $P_+Q_+^{-1}=Q_+^{-1}$), and $P_+Q_-P_+Q_-^{-1}\alpha=\alpha$ because $Q_-P_+^\perp Q_-^{-1}\alpha$ stays in the complement and is killed by $P_+$. The alternative "left inverse of a positive (bounded-below, hence invertible) operator is two-sided" is also valid for $\eta>0$ or $\lambda>0$; the unbounded power-law case is correctly restricted to the dense domain. Correct.

### (5) Marchaud/Liouville definitions §4 — correct
$(I_+^\nu f)(t)=\Gamma(\nu)^{-1}\int_{-\infty}^t(t-s)^{\nu-1}f(s)\,ds$ is the standard left Liouville/Weyl integral (symbol $(-i\xi)^{-\nu}$ in this Fourier convention); $I_-^\nu$ reflection (symbol $(i\xi)^{-\nu}$); $D_\pm^\nu=(I_\pm^\nu)^{-1}$ Marchaud. Factorization check with $\nu=(1-\beta)/2$: $Q_-Q_+=\gamma c_\beta(i\xi)^{-\nu}(-i\xi)^{-\nu}=\gamma c_\beta|\xi|^{-2\nu}=\gamma c_\beta|\xi|^{\beta-1}=\gamma\hat G=q$. Consistent with abstract's "order $(1-\beta)/2$."

### (6) $\zeta$-normalization clause §4 — factor correct
$Q_\pm=(\gamma c_\beta)^{1/2}I_\pm^\nu\Rightarrow Q_-^{-1}=(\gamma c_\beta)^{-1/2}D_-^\nu$. §4 defines $\zeta_{\S4}=D_-^\nu\bar\alpha$, so $\zeta_{\S4}=(\gamma c_\beta)^{1/2}\zeta_{\rm Thm1}$ — exactly "$\zeta$ here is $(\gamma c_\beta)^{1/2}$ times the whitened signal of Theorem 1." Self-consistency of the prefactor: $u^\star=Q_+^{-1}\zeta_{\rm Thm1}=(\gamma c_\beta)^{-1}D_+^\nu\zeta_{\S4}$, matching `eq:fractional`'s $1/(\gamma c_\beta)$. Correct.

### (7) Bernstein-measure identity §5 — correct
$\Gamma(\beta)^{-1}\int_0^\infty e^{-r|t|}r^{\beta-1}\,dr=\Gamma(\beta)^{-1}\cdot\Gamma(\beta)|t|^{-\beta}=|t|^{-\beta}$. Standard Gamma integral. Correct.

### (8) §6.3 table — column count and evidence wording verified
- Column spec `{lccccc}` = 1 `l` + 5 `c` = 6 columns; the table has exactly 6 columns (Kernel, $\eta$, $\lambda$, $\theta$, $R$ formula/discrete, $X$ formula/discrete). The prior `{lcccccc}` (7) was one too many. Fix correct.
- Per-row `dt` note verified against `risk_response_check.py` reruns:
  | row | setting | grid | discrete R / X (script) | table R / X | match |
  |----|----|----|----|----|----|
  | 1 | exp $\lambda{=}0.5,\theta{=}1.5$ | $dt{=}0.01$ | $-0.3093$ / $0.8603$ | $-0.309$ / $0.860$ | ✓ |
  | 2 | exp $\lambda{=}4,\theta{=}0.5$ | $dt{=}0.04$ | $-0.0284$ / $0.1044$ | $-0.028$ / $0.104$ | ✓ |
  | 3 | pure risk $\theta{=}0.7$ | $dt{=}0.04$ | $-0.4765$ / $0.6712$ | $-0.477$ / $0.671$ | ✓ |
  | 4 | $|t|^{-1/2}\ \theta{=}2$ | $dt{=}0.01$ | $+0.3251$ / $0.1898$ | $+0.325$ / $0.190$ | ✓ |
  | 5 | NV $\eta{=}0.5,\theta{=}1$ | $dt{=}0.02$ | $+0.2406$ / $0.2711$ | $+0.241$ / $0.271$ | ✓ |

  (Row 4 required a finer grid than the script's default $dt=0.04$; ran $dt=0.01$ explicitly to confirm.) Formula columns also reproduce: e.g. row 1 pred $-0.3107/0.8698\to-0.311/0.870$; row 4 pred $0.3643/0.1822\to0.364/0.182$. All match.
- Softened evidence sentence: "row 1 reaches $0.5\%$ in $R$ at $dt=0.01$" — verified $|{-0.3093}-({-0.3107})|/0.3107=0.45\%$. Accurate. (See M2 on "comparable.")

### (9) New cross-references / notation — clean
- `\ref`/`\eqref` audit: every referenced label (`lem:pi`, `thm:general`, `thm:filter`, `prop:response`, `eq:objective/symbol/foc/pi/policy/filter/ou-filter/ema/gp/finiteT/gk-kernel`) is defined; no undefined references in the log. Unreferenced-but-labeled equations (e.g. `eq:value`, `eq:threshold`) are fine (numbered display equations need no `\ref`).
- §7 $T\to\mathcal T$ rename: horizon scalar $T$ and the left-anchored outer factor operator $\mathcal T$ ($G_T=\mathcal T\mathcal T^*$) are distinct symbols; no collision with $G_T$, $C_\pm$.
- $x_T$ (terminal position, constraint $x_T=0$) vs $X(\theta)$ (position response) — distinct (lowercase subscripted vs uppercase function). No clash.
- $\alpha^{\rm eff}=\alpha+\sum_k\mu_k\psi_k$ defined in place at `eq:finiteT`. Fine.

### (10) Compilation / dangling text
`pdflatex` exit 0, `bibtex` clean, 12 pages, no undefined references or citations. No prose still references a removed $\hat g\in L^2$ blanket hypothesis — App. B retains it correctly as a *conditional* membership proof, not a theorem hypothesis; abstract/intro make no claim the rescoped theorem dropped. No dangling references detected.

---

## Sources
Local files only (no web inspection needed):
- `tex/optimal-trading-filters.tex`
- `experiments/risk_response_check.py`
- generated: `tex/optimal-trading-filters.log`, `.pdf`

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Verified only the Round-1 fix delta (10 requested checks); did not re-review core derivations. Output confined to BLOCKERS / FIXES STILL NEEDED / NON-ISSUES on the changed sentences/table."
    },
    {
      "id": "criterion-2",
      "status": "satisfied",
      "evidence": "Each finding cites the exact passage/equation, gives the re-derivation or numeric reproduction, and separates blockers from minor items. Table verified by rerunning risk_response_check.py plus finer-grid reruns; identities (2)-(7) checked by hand; compile verified."
    }
  ],
  "changedFiles": [
    "outputs/.drafts/filters-r2-correctness.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {"command": "pdflatex + bibtex optimal-trading-filters", "result": "passed", "summary": "exit 0, 12 pp, no undefined refs/citations"},
    {"command": "python experiments/risk_response_check.py", "result": "passed", "summary": "reproduces table rows 1,2,3,5 at stated grids"},
    {"command": "python -c finer-grid reruns (power-law dt=0.01/0.005, lambda=0 point)", "result": "passed", "summary": "row 4 = +0.3251/0.1898 at dt=0.01 matches table; quadrature-bias comparison 10.8% vs 6.2%"}
  ],
  "validationOutput": [
    "pdflatex exit 0; 12 pages; grep found no undefined reference/citation warnings",
    "Table: rows 1-5 discrete R/X match script output at stated per-row dt",
    "Identities (2)-(7) re-derived and confirmed; OU pole-cancellation and Lemma-1 reverse identity verified by direct algebra",
    "Column spec lccccc = 6 columns matches 6-column table"
  ],
  "residualRisks": [
    "M1: §3 'H in L^2 for every kernel' is loose at lambda=0 (pure impact) where the position is nonstationary; correct with inventory risk present. Wording, not math error.",
    "M2: 'comparable' quadrature-bias claim is 10.8% (row 4) vs 6.2% (lambda=0 point) at dt=0.01 - same order, slightly generous.",
    "Did not independently re-derive Prop. 1 / Appendix C beyond the reverse-identity line and c1 consistency, per instruction that Round-1 found the core derivations sound."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added review artifact only; no changes to paper or code (READ-ONLY review).",
  "reviewFindings": [
    "no blockers",
    "minor: optimal-trading-filters.tex §3 remark - 'H in L^2 for every kernel' should be scoped to lambda>0 / 'kernel considered' to match Appendix C",
    "minor: optimal-trading-filters.tex §6.3 - 'comparable' power-law bias is 10.8% vs 6.2%, same order but note the numbers"
  ],
  "manualNotes": "All 10 requested fix-verification items pass. Paper compiles clean at 12pp. The two minor items are wording/scoping refinements, not required for correctness. §6.3 table fully reproduced from risk_response_check.py (row 4 needed an explicit dt=0.01 run beyond the script default)."
}
```
