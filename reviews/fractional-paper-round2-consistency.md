# Round 2 Internal-Consistency Review
**File:** `papers/fractional-derivative-optimal-execution.md`
**Date:** 2026-06-27
**Scope:** Round 2 — verify Round 1 fixes (D1–D4, F2–F3, M1–M5,
m1–m4) are real and complete. No edits applied (review-only).
**Round 1 ref:** `reviews/fractional-paper-round1-consistency.md`.

---

## Top line

The Round 1 fixes are substantively in place. Convention D1 (γ vs 1−γ)
is now globally consistent; adaptedness propagation (M5) reaches both
Theorem 5.1 and Theorem 6.1; the Round-1 undefined constant $\kappa_\gamma^\infty$
is now defined (Corollary 5.3, line 582). Cross-references, $(\star)$
labels, and appendix pointers all resolve. Remaining issues are
**bibliography hygiene** (one uncited new entry; three body citations
without bib entries) and a handful of small textual nits.

---

## MAJOR

*None.* No findings rise to "blocker" or "must fix before circulating."

---

## MINOR (m#)

### m1. New uncited bibliography entry: Moreau–Muhle-Karbe–Soner (2017)
Worker added MMS 2017 to refs (line 1191) per Round-1 changelog
("m1–m4 bibliography hygiene") but the paper is **not cited anywhere
in the body** (`grep` returns only the refs line and the changelog
mention). This re-introduces exactly the defect Round 1 m2 flagged for
Luchko / AJ-Hauzy-Neuman. Either cite MMS in §8.3 (small-impact
limits) or §1.3 (related work on small-cost asymptotics), or drop it.

### m2. Body citations without bib entries
- **Söhngen** (lines 825, 854: "Chakrabarti–George (1994) / Söhngen–
  Tricomi (1957)", "Chakrabarti–George–Söhngen"). No Söhngen entry in
  References; only Tricomi (1957) is listed. Either add Söhngen
  (G. Söhngen, *Die Lösungen der Integralgleichung* … *und deren
  Anwendung in der Tragflügeltheorie*, Math. Z. 45, 245–264, 1939)
  or drop the joint attribution and cite only Tricomi.
- **Çelik–Duman (2012)** (Appendix D, line 1112). Cited inline for a
  shifted-Grünwald variant; no bib entry. Add or drop.
- **Podlubny** (line 703, "Podlubny's PI$^\lambda$D$^\mu$ class"). No
  bib entry. Acceptable as "tribal" attribution per the Round-1
  treatment of Oustaloup (1991), but flag for stylistic consistency.

### m3. AJNT (2024) arXiv ID — verify before submission
Bib entry `Abi Jaber, E.; Neuman, E.; Tuschmann, S. *Optimal Portfolio
Choice with Cross-Impact Propagators.* arXiv:2403.10273, March 2024.`
(line 1156). Independent verification of the arXiv ID against the
actual title/authors was not possible from local files; the ID is used
in five body locations (abstract, §1.2, §1.3, §4.2 Remark 4.1.2, §5.4
intro, §9), so a wrong ID would propagate. Spot-check once online.

### m4. §3.2 "up to the constant $c\,\Gamma(1-\gamma)$" omits the Riesz sin-factor
Line 248: "the kernel coincides, up to the constant $c\,\Gamma(1-\gamma)$,
with the integral operator $I^{1-\gamma}$ of order $1-\gamma$." Remark
4.1.3 (lines 350–360) explicitly records that the full Riesz
normalization carries an extra $2\sin(\pi\gamma/2)$ factor. The §3.2
phrasing should add a parenthetical pointer ("see Remark 4.1.3 for the
$2\sin(\pi\gamma/2)$ Riesz-normalization factor") so the reader doesn't
catch the inconsistency between §3.2 and Remark 4.1.3 unaided. Minor.

### m5. Bouchaud–Gefen–Potters–Wyart year — worker chose 2003 over 2004
Round 1 m4 flagged the text-vs-ref year mismatch. Worker standardized
on **2003** (body line 49; refs line 1168). Quant. Finance 4(2) was
formally published April 2004 (volume year = 2004); BibTeX/journal
records typically read 2004. The DOI link `10.1080/14697680400000022`
is correct. Not a blocker, but the conventional citation year is 2004.
Worker's choice is internally consistent; flag for editorial preference
only.

---

## NITS (n#)

### n1. Triple `---` cosmetic
Lines 213–217 contain `---` followed by two more `---` separated by
blank lines (visible only when the `## 5.` section happens to look like
three rules). Standard Markdown renders this as three horizontal
rules; if the intended structure is one section-break before §3 plus
one before §5, the second `---` is spurious. Trivial.

### n2. `\kappa` uniformity
All scalar / matrix Theorem statements and limit limits use
$\kappa_{1-\gamma}$; the half-line specialisation introduces
$\kappa_{1-\gamma}^\infty := (c_+ c_-)^{-1} = c_\gamma^{-1}$
(Corollary 5.3, line 582). The two constants are now both defined;
Round 1 M4 is resolved.

### n3. Body cites "AJN co-authors (2022–2025)" — fine
Both endpoints exist in refs (Abi Jaber–Neuman 2022 arXiv:2211.00447;
Abi Jaber–Bondi–De Carvalho–Neuman–Tuschmann 2025 arXiv:2503.04323),
so the range citation is valid.

### n4. `\mathbb{E}_t[\alpha_T]` audit
Round 1 M2 fix verified: $(\star)$, $(\star\star)$, Theorem 5.1
integrand, Theorem 6.1 all show RHS $= \alpha_t - \lambda$ (or
$\bar\alpha(t,s) - \lambda$). No stray `E_t[α_T]` survives in body or
appendices. §2.4 and §5.1 carry the explanatory note. ✓

### n5. Star-label hygiene
$(\star)$ — defined §2.4 line 207, used §3.2/§4.2/A.1/§5.1/§7. ✓
$(\star\star)$ — defined §5.1 line 416, used §5.2/B.1. ✓
$(\star_t)$ — defined A.1 line 793, used A.2. ✓
$(\star_{\mathrm{WH}})$ — defined §5.4 line 540, used Cor 5.3/§5.5/B.5. ✓
No stale or undefined star labels.

### n6. Remark numbering
4.1.1, 4.1.2, **4.1.3** (new), 5.1.1, 5.4, 5.5. No collisions. The
Theorem-4.1 text on line 308 references "Remark 4.1.3" which now
exists. ✓

### n7. Order-convention spot-checks (independent grep)
- `mathbb{D}^\gamma` (old form): **0 occurrences** in body. ✓
- `mathcal{B}_\gamma` (old form): **0 occurrences** in body. ✓
- `\kappa_\gamma` (without `1-`): **0 occurrences** outside the
  Changelog narrative. ✓
- All Mittag–Leffler indices are $E_{1-\gamma,1-\gamma}$ (abstract,
  §3.3, Theorem 5.1, §5.3, B.2). ✓
- One-sided derivatives in Prop 5.2 / Cor 5.3 are
  $D^{(1-\gamma)/2}_\pm$, total operator order $1-\gamma$, matching
  Theorem 4.1. ✓
- §5.4 W–H factorization uses exponent $(\gamma-1)/2$ for the
  *symbol* and $(1-\gamma)/2$ for the *operator order*, with the
  inversion accounting for the sign — explicitly noted at line 562
  ("$(\gamma-1)/2 < 0$, so $\hat G_\pm$ are integrals of order
  $-(\gamma-1)/2 = (1-\gamma)/2$"). No self-contradiction remains
  (Round 1 M1's third bullet is fixed).
- Boundary exponent $\mathcal{B}_{1-\gamma}(t) \propto (t(T-t))^{(\gamma-1)/2}$
  consistent at Thm 4.1 line 313, Cor 4.2 line 367, A.2 line 829.
  Worker F2 fix verified.

### n8. Notation unification (Round 1 M4)
Body uses exactly two operator symbols: $\mathbb{D}^{1-\gamma}_{[0,T]}$
(symmetric) and $D^{1-\gamma}_\pm$ / $D^{(1-\gamma)/2}_\pm$ (one-sided).
The only remaining `D^\gamma` and `I^{-\gamma}` references are inside
the Changelog narrative (lines 1231, 1289) describing what was
removed — these are correctly historical, not stragglers. ✓

### n9. Adaptedness propagation (Round 1 M5)
- Theorem 5.1 statement (line 430) integrand: $\bar\alpha(t,s) - \lambda$. ✓
- Remark 5.1.1 (lines 447–452) explicitly justifies the substitution. ✓
- Theorem 6.1 (line 650) integrand: $\bar{\boldsymbol\alpha}(t,\cdot) - \boldsymbol\lambda$
  with "vector forward conditional-forecast curve (component-wise as
  in §4.1)" remark. ✓
- Corollary 5.3 (line 582) acts on $\bar\alpha^\infty(t,\cdot)$. ✓

### n10. Cross-reference / appendix pointers
Spot-checked:
- Thm 4.1 → Appendix A (line 320) ✓; A subdivides into A.1–A.3 ✓.
- Cor 4.2 → A.2 (line 373) ✓.
- Cor 4.3 → A.3 (line 384) ✓ (now with conjectural caveat).
- Thm 5.1 → B.1–B.2 (line 443) ✓.
- Prop 5.2 → B.4 (line 565) ✓.
- Cor 5.3 → B.5 (line 597) ✓.
- Thm 6.1 → Appendix C (line 660) ✓.
- §4.4 #3 → Appendix D (line 404) ✓ (Round 1 nit n1 partly addressed).
- §7 → Appendix E still not cross-linked by name from §7. Trivial.

---

## Changelog accuracy spot-check (5 claims verified)

The Round-1 Changelog block (lines 1224–1339) was spot-checked against
the body:

1. **"Relabeled $\mathbb{D}^\gamma \to \mathbb{D}^{1-\gamma}$ throughout
   (abstract, §1.1–1.2, §3.2, Thm 4.1, §4.4, Thm 5.1, Prop 5.2,
   Cor 5.3, Thm 6.1, A.1–A.3, B.1, B.2, B.4, B.5, C, D, §8.1, §9)."**
   ✓ Verified — independent grep shows 0 stray `\mathbb{D}^\gamma`.

2. **"$\kappa_\gamma \to \kappa_{1-\gamma} = (c\,\Gamma(1-\gamma))^{-1}$
   with $2\sin(\pi\gamma/2)$ flagged in new Remark 4.1.3."**
   ✓ Verified — Remark 4.1.3 exists at lines 350–360 with the
   normalization warning and a ⚠️ TODO.

3. **"M5 — Thm 5.1 integrand uses $\bar\alpha(t,s)$ … Thm 6.1 uses
   vector forward conditional-forecast curve."**
   ✓ Verified — see n9 above.

4. **"M2 — §2.1 gained a standing-assumptions paragraph."**
   ✓ Verified — lines 153–159.

5. **"m1–m4 — Removed Luchko (2021) and Abi Jaber–Hauzy–Neuman (2024)."**
   ✓ Verified — `grep` for Luchko / Hauzy returns only the Changelog
   narrative line.

6. **"F2 — boundary exponent $(t(T-t))^{(\gamma-1)/2}$."**
   ✓ Verified at Thm 4.1 line 313, Cor 4.2 line 367, A.2 line 829.

7. **"F3 — Mittag–Leffler prefactor $c\Gamma(1-\gamma)$ added."**
   ✓ Verified at Thm 5.1 line 433 and B.2 line 946.

Changelog is faithful to the edits actually applied.

---

## Fixes worth doing now (F#)

### F1. Cite or drop Moreau–Muhle-Karbe–Soner (2017)
Mirror image of Round-1 m2 (Luchko / AJHN). Either add a §1.3 or §8.3
mention of small-impact / small-cost asymptotics, or remove the bib
entry. One-line edit.

### F2. Add bib entries for Söhngen and Çelik–Duman, or remove inline cites
Both are factual scholarly references used to anchor a derivation
(Söhngen for the A.2 inversion prefactor; Çelik–Duman for the WSGD
discretization in Appendix D). Either upgrade them to proper bib
entries or replace with the citations already in refs
(Tricomi 1957 §4.3 covers Söhngen; Tian–Zhou–Deng 2015 already covers
the higher-order shifted Grünwald).

### F3. §3.2: add "(see Remark 4.1.3 for Riesz normalization)" pointer
Two-word edit at line 248 to flag the $2\sin(\pi\gamma/2)$ factor and
avoid a reader catching a phantom inconsistency between §3.2 and the
remark.

---

## Summary

Round 1's structural concerns (γ vs 1−γ convention, adaptedness in
Thm 5.1/6.1, $\kappa_\gamma^\infty$ definition, W–H advertised in
abstract/§1.2/§9, $\mathbb{E}_t[\alpha_T]$ removal, Forde recovery
downgrade) are all genuinely fixed. The remaining work is **bibliography
hygiene** (F1, F2) and one small cross-reference (F3). No new
content-level inconsistencies were introduced by the rewrite.
