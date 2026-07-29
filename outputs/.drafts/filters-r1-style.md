# Style / self-containedness / internal-consistency review — `tex/optimal-trading-filters.tex`

Reviewer role: style, self-containedness, and internal-consistency pass against `AGENTS.md`.
Scope: read-only. The file was copied to `/tmp/otf-review/` and compiled there (pdflatex ×4 + bibtex): **compiles cleanly, all `\ref`/`\cite` resolve, no missing bib entries, no overfull warnings.** Line numbers below refer to `tex/optimal-trading-filters.tex`.

## Summary

The draft is unusually clean by the project's own style rules: no rhetorical questions, no dead-end narration, no disparagement of prior work, section cross-references all correct, and every numerical entry I could recompute by hand matches. The issues that remain are (a) one internal inconsistency in the stated Riesz-projection convention that the OU derivation actually depends on, (b) an abstract/intro verification overclaim relative to what §6.3 shows, (c) a hard notation collision (`T` as horizon and as operator in §7), and (d) a short list of style-rule violations and undefined symbols. All are locally fixable; none require restructuring.

---

## BLOCKERS

**[B1] Contradictory Π₊ convention: §3 vs Appendix B.** (lines 136 vs 310)

> §3, line 136: "so $P_+$ acts on symbols as the Riesz projection $\Pi_+$ (truncation to **non-negative** lags)"

> Appendix B, line 310: "atoms at lag zero load on the contemporaneous innovation and are **likewise annihilated**"

These state opposite conventions for lag zero. The discrepancy is not cosmetic: the OU pole-cancellation argument in Appendix B ("$h - (\theta/\Phi)\varphi_+ = \ldots$ is anticausal-plus-atom") needs the atom $-\sigma c_1$ (the constant $-\sigma/N_-(\xi) \to -\sigma c_1$ at high frequency) to be killed by $\Pi_+$, i.e. it uses the Appendix-B convention (strictly positive lags / atoms annihilated), while §3 announces truncation to non-negative lags. With $c_1 \ne 0$ (kink kernels, $\eta=0$) the two conventions give different $\Pi_+ h$, hence different filters. Fix: state one convention in §3 — truncation to strictly positive lags, with lag-zero atoms annihilated — and note in one clause why ($\E_s$ of a contemporaneous innovation loading vanishes in the forward limit). Then Appendix B's "likewise annihilated" follows rather than contradicts.

**[B2] "All closed forms are verified" overclaims §6.3.** (lines 36 and 85)

> Abstract, line 36: "All closed forms are verified against discretized adapted optima."

> §1.4, line 85: "All closed forms are verified against discretized adapted optima (\S6.3)."

§6.3 verifies the **response formulas** $R(\theta)$ and $X(\theta)$ at five parameter points. It does not display verification of the value formulas ($v = \sigma^2\theta/4\Phi^2$, the fractional value, the Markowitz value), the filter kernels \eqref{eq:ema}/\eqref{eq:nv-filter} as functions, or any finite-horizon formula (eq. 21–22; the §7 factorization is claimed "verified by direct kernel integration" but the check is not shown). $R$ and $X$ are derived from the filters, so the responses are an indirect probe, but "all closed forms" is stronger than the evidence presented. Weaken both sentences to what §6.3 shows ("The response formulas are verified against discretized adapted optima"), or extend §6.3.

**[B3] Notation collision: $T$ is both the horizon and an operator.** (line 284)

> "The time reflection of \eqref{eq:gk-kernel} is the left-anchored outer factor $G_T = TT^*$ used by \citet[pp.~590--591]{FordeSanchezSmith2022}"

$T$ has meant the horizon since the first sentence of §7 ("finite horizon $[0,T]$", "$X_T = 0$", "$(T-s)/(T-t)$" in the same paragraph). "$G_T = TT^*$" is unparseable without guessing that the second and third $T$ are a different object. Rename the operator ($\mathcal{T}$, $C_-^{\rm left}$, or FSS's own symbol).

---

## FIXES WORTH DOING NOW

### Style violations (AGENTS.md, exact quotes)

**[F1] Self-promotional framing.** (line 67)
> "The mathematical problem of the paper is the inversion of $P_+QP_+$"

Rule: "Avoid self-promotional framing. Do not write 'sets the mathematical content of this paper'…" This is that construction almost verbatim. Rewrite declaratively: "The remaining problem is the inversion of $P_+QP_+$" or simply "Solving \eqref{eq:foc} requires inverting $P_+QP_+$".

**[F2] "not by X but by Y" foil construction.** (line 61)
> "a closed subspace $L^2_{\rm adap}$ cut out not by equations but by an increasing family of $\sigma$-algebras"

Rule: "Avoid the 'X is not Y, it is Z' rhetorical construction and its variants." State the positive: "a closed subspace $L^2_{\rm adap}$ cut out by an increasing family of $\sigma$-algebras."

**[F3] "rather than" foil in Concluding Remarks.** (line 295)
> "Limitations delimit the closed forms rather than the method."

Rule: variant of "Rather than X, this is really Y", used as a topic sentence. Replace with the positive claim, e.g. "The closed forms hold under the following restrictions." (The rest of the paragraph already does the work.)

**[F4] "reads" formula opener.** (line 171)
> "The general policy \eqref{eq:policy} reads"

Rule: "No 'the formula/composition/expression reads/says X' openers." Replace with "The general policy \eqref{eq:policy} becomes" or "Specializing \eqref{eq:policy}:".

**[F5] "is the statement that" formula-gloss opener.** (line 107)
> "which is the statement that the combined friction acts as a single propagator on the \emph{position}."

Same rule family as F4 ("the formula says X"). State it directly: "the combined friction acts as a single propagator on the position."

**[F6] "essential" + throat-clearing.** (line 280)
> "One caution is essential: the identity \eqref{eq:pi} requires the causal factor \emph{on the right}, which pins the factor's anchoring."

Rule: "Avoid empty intensifiers: … 'essential' …" and no throat-clearing. The content (a legitimate one-sentence warn-off) survives without the preamble: "The identity \eqref{eq:pi} requires the causal factor on the right, which pins the factor's anchoring."

### Self-containedness gaps

**[F7] $f(D)$ notation undefined.** (lines 57, 136, 141) `$Q = q(D)$`, `$\varphi_+(D)\dot W$`, `$\hat g(D)\,\dot W$` — the operator $D$ / Fourier-multiplier notation $f(D)$ is never defined. One clause at first use (line 57): "$q(D)$ the Fourier multiplier with symbol $q(\xi)$ under the convention of §2.1" (or define the convention there, since line 57 currently precedes the convention statement at line 98).

**[F8] $I_\pm^\nu$ and Marchaud $D_\pm^\nu$ never given formulas.** (line 171) Cited to Samko–Kilbas–Marichev but not defined; the Marchaud kernel is only hinted at ("weights past signal increments by … $(t-s)^{-1-\nu}$", line 176). One display each — $(I_+^\nu f)(t) = \Gamma(\nu)^{-1}\int_{-\infty}^t (t-s)^{\nu-1} f(s)\,ds$ and the Marchaud difference form — makes §4 self-contained; §7's eq. (22) visibly reuses the $I_+^\nu$ kernel, so the definition pays twice.

**[F9] $L$ in the discrete cost form undefined.** (line 255)
> "the discrete cost form $\eta I + \gamma\,dt\,G + \lambda\,dt^2L^\top\!L$"

$L$ (presumably the lower-triangular cumulative-sum matrix mapping rates to positions) is never defined; $G$ here silently becomes a matrix. Also under-specified for reproducibility: no $dt$, grid length, or horizon for the discretization, and "forward responses measured by lag-one regression" is one clause. Two sentences fix this.

**[F10] $\alpha^{\rm eff}$ under-specified.** (line 280)
> "where $\alpha^{\rm eff}$ adjoins multipliers for position constraints (a process-valued multiplier for the pathwise liquidation constraint $X_T = 0$)"

"Adjoins multipliers" does not define the object; the reader cannot write $\alpha^{\rm eff}$ down. Either give the formula ($\alpha^{\rm eff} = \alpha + $ multiplier term, with the multiplier determined by the constraint) or point to where it is determined. Also note the collision in the same sentence: **$X_T$** for terminal position where the paper writes the position as lowercase $x_t$ throughout (and $X(\theta)$ is the position response, line 160). Use $x_T = 0$.

**[F11] "Bernstein measure" undefined and uncited.** (line 221)
> "a continuum of EMAs weighted by the Bernstein measure of $|t|^{-\beta}$"

Only naming instance; no definition, no reference. One clause + citation (complete monotonicity of $|t|^{-\beta}$; e.g. Schilling–Song–Vondraček, *Bernstein Functions*) satisfies the "cite specifics" rule.

**[F12] $q$ reused as the limit variable in the definition of $R$.** (lines 228, 317)
> "$R(\theta) = \lim_{q\downarrow0}\E[u^\star_{t+q}\mid\alpha_t]/\alpha_t$" … "(the innovations in $(t,t+q]$ …)"

$q$ is the friction symbol throughout the paper. Rename the increment ($\epsilon$ or $\delta$; avoid $h$, used in Appendix B).

**[F13] Wrong pointer for the dense domain in Appendix A.** (line 305)
> "the computation holds on the dense domain of \S8"

§8 is Concluding Remarks, which mentions "a dense domain fixed by a spectral-decay hypothesis" in passing but defines nothing; the actual hypothesis $\int(1+\xi^2)S_\alpha/q\,d\xi<\infty$ lives in Appendix B (line 310). Point to Appendix B (and hyperlink with `\ref` rather than a hard-coded `\S8`, which will silently break if sections move).

**[F14] $\zeta$ normalization drift between §2 and §4.** (eq. 8 vs eq. 13) In Theorem 1, $\zeta_s = (Q_-^{-1}\bar\alpha(s,\cdot))(s)$, which includes the constant $(\gamma c_\beta)^{-1/2}$; in eq. (13), $\zeta_s = (D_-^\nu\bar\alpha(s,\cdot))(s)$ with the constants moved into the prefactor $1/\gamma c_\beta$. The formulas are equivalent (both $(\gamma c_\beta)^{-1/2}$ factors are absorbed — I checked), but the same symbol $\zeta$ denotes two differently normalized processes. Add "(absorbing the constant $(\gamma c_\beta)^{-1/2}$ into the prefactor)" or use $\tilde\zeta$.

**[F15] Table column-spec mismatch.** (lines 258–260) `\begin{tabular}{lcccccc}` declares 7 columns; the header and every data row have 6 entries. Compiles, but the spec is wrong — drop one `c`.

**[F16] Proposition 1 has no proof pointer.** §2.2 says "(Appendix A)" and §3 says "(Appendix B)" twice, but nothing in §6 points to Appendix C; a reader of Proposition 1 has to discover the proof by scanning the back matter. Add "(Appendix C)".

**[F17] Szegő condition uncited.** (line 98)
> "we assume the Szeg\H{o} condition $\int|\log q(\xi)|/(1+\xi^2)\,d\xi<\infty$"

Rule: "Cite specifics. When claiming a result is standard, give the reference." The factorization-existence result invoked here should carry a citation (Krein 1962 is already in the bibliography and is the natural target).

**[F18] Abstract precision: "fractional derivative … of the signal".** (line 36)
> "with power-law transient impact alone the trading rate is a fractional derivative of order $(1-\beta)/2$ of the signal"

Per eq. (13), the general power-law policy is $D_+^\nu$ of the *whitened* signal $\zeta$ (itself an anticausal $D_-^\nu$ of the forecast curve); it collapses to a fractional derivative of the signal itself only for the OU case ($\zeta_s = \theta^\nu\alpha_s$). Add "for an OU signal" or "of the (whitened) signal".

---

## OPTIONAL

**[O1] Negation-motivation opener of §7.** (line 276)
> "Trading on a finite horizon $[0,T]$ --- liquidation, daily sessions --- breaks translation invariance, and Fourier factorization no longer applies. The correct generalization replaces…"

Borderline under "Avoid the negation-motivation opening." The negative clause here carries technical content (why a new tool is needed), so this is defensible; leading with "On a finite horizon the Wiener–Hopf factors are replaced by the triangular factorization relative to the chain $\{P_{[0,t]}\}$ …" would comply strictly.

**[O2] "rather than characterized as a fixed point".** (line 87)
> "the adapted optimum here is closed-form rather than characterized as a fixed point"

Foil-shaped, but it is a specific comparative claim against cited work rather than an unstated foil; arguably compliant. A strictly positive rendering: "the adapted optimum here is closed-form, covers the three frictions jointly, …" (the fixed-point characterizations are already described neutrally earlier in the sentence).

**[O3] $P_{[0,t]}$ and "nest" vs "chain".** (lines 85, 276) $P_{[0,t]}$ is never defined (projection onto processes supported on $[0,t]$ / adapted through $t$), and the same object is called a "nest" in §1.4 and a "chain" in §7. Define once, unify the term.

**[O4] $c_1$ vs $c_\beta$.** (lines 171, 234) $c_\beta = 2\Gamma(1-\beta)\sin(\pi\beta/2)$ invites misreading $c_1$ as its $\beta=1$ value (which diverges). $c_1$ is a different object ($\lim_{|\xi|\to\infty} 1/N_+$). Renaming $c_1$ (e.g. $c_\infty$, which also matches its definition) removes the hazard.

**[O5] $w_i$ index convention.** (eq. 18) "$w_i = \frac{\kappa-b_i}{b_j-b_i}$" — $j$ undefined; add "$\{i,j\}=\{1,2\}$".

**[O6] Boundary pole of $Q_\pm$.** (eq. 6) $Q_+ = N_+/(-i\xi)$ has a pole at $\xi=0$ on the real axis, so eq. (5)'s claim that "$q$ admits a Wiener–Hopf factorization" with $Q_+$ "causal with causal inverse" holds in a slightly weaker sense than the bounded-symbol reader expects (the pole is an integration, tied to the $x\in L^2$ admissibility remark at line 98). One clause connecting the pole to admissibility would close the gap.

**[O7] $N_\pm$ normalization not stated explicitly.** (eq. 6) The properties of $N_\pm$ (outer/zero-free in the upper half-plane, $N_- = \overline{N_+}$) are inherited from eq. (5) via $Q_\pm = N_\pm/(\mp i\xi)$ and are retroactively named at line 156 ("the position-level causal factor"), but §5 and §6 use $N_+$ heavily and a reader benefits from one sentence at eq. (6) fixing the convention (in particular that eq. (11) is the outer normalization).

**[O8] "variance of the position".** (line 43) The penalty $\frac{\lambda}{2}\E\int x_t^2\,dt$ is a second moment; it equals the variance because $\alpha$ (hence $x$) is mean-zero, but mean-zero is only stated in §2.1. Either say "second moment" or note mean-zero in §1.1.

**[O9] Intro Markowitz symbols.** (line 57) "$w = \lambda^{-1}\Sigma^{-1}\mu$" uses $w$, $\Sigma$, $\mu$ undefined (standard finance notation); $\mu$ is later redefined as $-\dot\alpha$ in §4 and $w_i$ reused in eq. (18). Low risk given distance, but a "(weights $w$, covariance $\Sigma$, expected returns $\mu$)" parenthesis is cheap.

**[O10] "Laplace point", "kink kernel".** (lines 156, 317) "the signal's Laplace point" (meaning: evaluation at $i\theta$) and Appendix C's "a kink kernel" (main text says "kernels with a kink at the origin", i.e. $G'(0^+)$ finite and nonzero) are informal coinages; each deserves a one-clause definition at first use.

**[O11] $G_T$ overloads $G$.** (line 276) $G$ is the propagator kernel from §1.1; $G_T$ is "the cost operator restricted to $[0,T]$" (which includes $\eta$ and $\lambda$ terms, not just the propagator). Given B3 the §7 notation is being touched anyway; consider $\mathsf{Q}_T$ or $Q_{[0,T]}$.

**[O12] Hard-coded section numbers.** (line 85) `(\S4) … (\S5) … (\S6) … (\S7) … (\S6.3)` are all currently correct (verified against the compiled `.aux`) but are literals; converting to `\ref` protects against renumbering. Same for `\S8` in F13.

**[O13] "verified by direct kernel integration".** (line 284) The claim "$C_-C_+ = G_T$ exactly, including the constant" is asserted without the computation or a pointer to it. If the check exists in a script or note, a pointer (or an appendix line) would let the claim be audited.

---

## NON-ISSUES (verified)

1. **No rhetorical questions.** `grep '?'` over the source: zero interrogatives in prose.
2. **No dead-end narration.** No abandoned ansatzes or negative-result histories appear anywhere in the draft.
3. **No disparagement of prior work.** §5.3's description of Neuman–Voß ("four coupled linear FBSDEs solved by matrix exponentials, in feedback form") and §7's description of Forde–Sánchez-Betancourt–Smith are neutral statements of what those treatments produce, followed by positive claims about the present reduction — compliant with the rule as written.
4. **No empty intensifiers beyond F6.** "canonical", "genuine", "true", "deep", "the essence of", "cleanest" absent; "structural" does not occur at all.
5. **No hortative constructions.** "let us", "we now turn", "notice that", "note that" absent. "Assume now that" (line 136) is a mathematical assumption statement, not hortative filler.
6. **"the inverse of a projected operator is not the projection of the inverse" (line 67)** is a precise mathematical statement, not the banned rhetorical foil; retained deliberately in this review.
7. **Section cross-references all correct.** Compiled `.aux` confirms: §4 = Two Limits, §5 = Explicit Filters, §6 = Contrarian Trading, §6.3 = Numerical verification, §7 = Boundary Effects, §8 = Concluding Remarks — matching every intro pointer in line 85. Appendices label as A/B/C; "Appendix A"/"Appendix B" text pointers correct (Appendix C pointer missing → F16).
8. **Compilation and bibliography.** pdflatex ×4 + bibtex in `/tmp/otf-review`: no undefined references, no missing citations, no errors; all 25 cite keys resolve against `optimal-trading-filters.bib`.
9. **Algebra spot-checks pass** (recomputed by hand):
   - eq. (14): $N = (A\xi^2+\lambda\kappa^2)/(\kappa^2+\xi^2)$ with $A=2\kappa\gamma+\lambda$, and $N_-N_+$ reproduces it with $m=\kappa\sqrt{\lambda/A}$. ✓
   - eq. (15) from eq. (12) via $(\kappa-i\xi)/(m-i\xi) = 1+(\kappa-m)/(m-i\xi)$; $\lambda\to\infty$ recovers Markowitz $\theta/\lambda$; $\lambda\to0$ recovers $u^\star = \frac{\kappa+\theta}{2\kappa\gamma}(\dot\alpha+\kappa\alpha)$. ✓
   - eq. (16): partial-adjustment algebra from $N_+=\sqrt\eta(a-i\xi)$ gives exactly $\mathrm{aim}_t = \frac{a}{a+\theta}\frac{\theta\alpha_t}{\lambda}$. ✓
   - eq. (17): root relations $b_1^2b_2^2=\lambda\kappa^2/\eta$, $b_1^2+b_2^2=\kappa^2+(2\kappa\gamma+\lambda)/\eta$ match the biquadratic numerator; both degenerations ($\gamma=0$ roots $\{a,\kappa\}$; $\eta\to0$: $b_1\to m$, $\sqrt\eta b_2\to\sqrt A$) check out. ✓
   - eq. (20): $2c_1\Phi(\theta)>1$ with $\Phi=\sqrt A(m+\theta)/(\kappa+\theta)$, $c_1=1/\sqrt A$ gives $\theta^*=\kappa-2m$; $\theta^*\le0 \iff \lambda\ge2\kappa\gamma/3$. ✓
   - Appendix C consistency limits: $\lambda\to0$ gives $(\kappa^2-\theta^2)/2\kappa\gamma$; $\gamma\to0$ gives $-\theta^2/\lambda$. ✓
   - Fractional limit: $\Phi(\theta)=(\gamma c_\beta)^{1/2}\theta^{(1+\beta)/2}$ gives $v=\sigma^2\theta^{-\beta}/4\gamma c_\beta$ and $\zeta_s=\theta^\nu\alpha_s$; crossover frequencies $\xi_c$, $\xi_*$ follow from balancing symbol terms. ✓
   - Value chain: eq. (10) ↔ Appendix B's $v=\frac12\E[u^\star\alpha]=\frac{1}{4\pi}\|\Pi_+h\|^2$; $\|\varphi_+\|^2=\pi\sigma^2/\theta$ gives $v=\sigma^2\theta/4\Phi^2=\frac{\sigma^2}{4}X(\theta)$. ✓
10. **Table rows are internally consistent.** Rows 1–3 recomputed from eq. (19): $R=-0.3107, -0.0283, -0.490$ and $X=0.870, 0.107, 0.700$ — all match the displayed "formula" values to the printed precision. Rows 4–5 satisfy the $c_1=0$ identity $R=\theta X$ exactly ($0.364 = 2\times0.182$; $0.264 = 1\times0.264$). Row 2's "always-contrarian" annotation is correct ($\lambda=4 > 2\kappa\gamma/3 = 4/3$).
11. **Argument flow §1.3 → §2 is adequate for a WH-naive reader.** §1.3 supplies the factorization, Paley–Wiener causality, the triangularity/forward-inversion argument (which is what "causal with causal inverse" in §2.1 rests on), and the Cholesky analogy that Lemma 1's proof reuses. §2 introduces nothing unexplained beyond the standard "usual conditions" and the items flagged in F7/F17/O6.
12. **The one-sentence position-coordinate device (eq. 6) is sufficient for §5's use of $N_+$** in the sense that every §5–§6 computation is reconstructible from eq. (5) + eq. (6) + eq. (11); the residual gap is the explicit normalization statement (O7), which is polish rather than a hole.
13. **Forecast curve** is defined in §2.1 before any body use; abstract/intro uses precede it but that is normal for an abstract.
14. **$P_+$** is defined at first use (eq. 3, line 67); the abstract's and §1.4's "optional projection" and line 67's "orthogonal projection" name the same operator — the identification is standard in this $L^2$ setting and the dual naming is acceptable, though a two-word parenthetical "(the optional projection; here also the $L^2$-orthogonal projection)" would remove any doubt.
15. **PNAS structure rules inapplicable.** The draft is a journal article (JEL codes, authoryear natbib, no Significance statement), so the PNAS-form bullet in AGENTS.md does not bind.
16. **Symmetric-kernel caveat present.** The $\hat G \ge 0$ assumption in eq. (2) and the "kernel symmetric" limitation in §8 are consistent with each other.

## Sources

No external sources consulted; all checks performed against the repository artifact `tex/optimal-trading-filters.tex`, its bibliography `tex/optimal-trading-filters.bib`, and a read-only compile in `/tmp/otf-review/` (pdflatex + bibtex, `.aux` inspected for section/label numbering).
