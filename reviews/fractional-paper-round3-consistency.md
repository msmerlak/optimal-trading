# Round 3 Internal-Consistency Review (v2 bulk/boundary rewrite)
**File:** `papers/fractional-derivative-optimal-execution.md` (v2, 897 lines)
**Migration note:** `papers/fractional-derivative-optimal-execution.v1-to-v2.md`
**Prior round:** `reviews/fractional-paper-round2-consistency.md`
**Date:** 2026-06-27
**Mode:** review-only; no edits applied.

---

## Top line

The v2 restructure is internally coherent on the spine claims:
bulk theorem on $\mathbb{R}$, boundary corrections on $[0,T]$ and
$[0,\infty)$, locked decisions D1/D3/D4/D5/D6 all visible, the
$\kappa_{1-\gamma}$ constant matches across every body and appendix
occurrence, Round 2 fixes (F1 MMS cite, F2 Söhngen/Çelik–Duman bib,
F3 §3.2 Riesz factor) are all in place. **Two real problems**:
(M1) three body cross-references point to appendix sections that do
not exist (A.4 and A.5); (M2) three v2-added bib entries (Webster,
Cartea–Jaimungal–Penalva, Novokshenov) are orphans — listed but
never cited. Several smaller items below.

---

## MAJOR

### M1. Body references to non-existent appendices A.4 and A.5
The appendix structure is **A.1, A.2, A.3, B, C, D, E** (confirmed by
`awk` between section headers; lines 583, 605, 679, 736, 774, 794, 814).
There is no Appendix A.4 and no Appendix A.5. Three body references
point at the missing sections:

- **Line 325 (Conjecture 5.2.2).** "Per decision D4 = A, we leave the
  recovery as a conjecture; **the structural sketch is in Appendix
  A.5**." A.5 does not exist. The Forde structural sketch is absent
  altogether — only the `⚠️ TODO (kernel-matching computation against
  Forde et al. 2022 eq. (26) on [0,T])` survives at line 327. Either
  add an A.5 section (even a half-paragraph stub) or strike the
  pointer.
- **Line 454 (Theorem 6.1 proof line).** "**Full computation: Appendix
  A.4.** ⚠️ TODO …" The Mittag–Leffler / Neumann-series derivation
  for Theorem 6.1 is in **Appendix B** (B.1 Neumann series, B.2 ML
  identification, B.3 limits — lines 736–772). The pointer must read
  "Appendix B" or "Appendices B.1–B.2".
- **Line 567 (§9.2 Open problems).** "Quantitative finite-interval HLS
  bound supporting the Theorem 6.1 Neumann radius **(Appendix A.4
  hand-wave)**." Same fix: point at **Appendix B.1**.

This breaks the appendix-pointer self-consistency the Round 2 review
verified line by line (Round 2 n10). It is a regression introduced by
the v1→v2 appendix split (v1 App B → v2 A.3 + B), which migrated A.3
correctly but left the §6.1 proof and the Conjecture 5.2.2 pointer
unredirected.

### M2. Three v2-added bibliography entries are orphans
The v2 changelog (line 885) and the migration note §3.5 advertise the
addition of "Söhngen (1939), Çelik–Duman (2012), Podlubny (1999), Stein
(1970), Cartea–Jaimungal–Penalva (2015), Webster (2023)". Independent
`grep` of the body:

| Entry | Body citations? |
|---|---|
| Söhngen 1939 | ✓ (line 158, §3.2) |
| Çelik–Duman 2012 | ✓ (lines 808, 812, App D) |
| Podlubny 1999 | ✓ (lines 148, 538, 808) |
| Stein 1970 | ✓ (lines 162, 204, 595) |
| **Cartea–Jaimungal–Penalva 2015** | **✗ — orphan** |
| **Webster 2023** | **✗ — orphan** |
| **Novokshenov 2015** (line 849) | **✗ — orphan** (likely v1 holdover; not flagged in the v2 changelog at all, but still an unused entry) |

This is the same defect Round 2 m1 flagged for MMS (2017) — worker
fixed MMS but reintroduced the pattern for three new entries. Either
cite each in §1.3 / §6.x / App A.3 as appropriate, or drop them from
References. Novokshenov is a particularly clear orphan: it is a
W–H-on-finite-segment paper that would naturally be cited in
§5.3 / App A.3 if relevant, but is not.

---

## MINOR

### m1. Numbering gap: there is no Proposition/Corollary 5.6
Sequential body numbering: Cor 5.2, Cor 5.2.1, Conj 5.2.2, Prop 5.3,
Cor 5.4, Prop 5.5, **(no 5.6)**, Cor 5.7, Thm 6.1, Thm 7.1. The skip
from 5.5 to 5.7 also appears in the v2 changelog ("Proposition 5.5 /
Corollary 5.7"), so it is internally consistent — but a reader will
ask. Either renumber Cor 5.7 → Cor 5.6, or add an editorial note in
§5.3.3 explaining the skip (e.g. a Lemma 5.6 was excised). Both
options are one-line edits.

### m2. Conjecture 5.2.2 pointer self-consistency
Tied to M1. The body sentence at line 325 reads
"…we leave the recovery as a conjecture; the structural sketch is in
Appendix A.5. ⚠️ **TODO** (kernel-matching computation…)". The TODO
admits no sketch exists; the pointer claims one does. Round 2 was
generous in treating Conjecture 5.2.2 as fully disclosed; the
non-existent A.5 pointer makes the disclosure incomplete.

### m3. Migration note §2 table omits A.3, A.4, A.5
The migration table (lines 33–60 of v1-to-v2.md) maps "v1 App A →
v2 A.1 + A.2 (Cor 5.2 + Prop 5.3)" and "v1 App B → v2 A.3 + App B".
This is faithful for A.1, A.2, A.3, and B. It does not mention any
A.4 or A.5, which is consistent with the actual file — confirming
that the body pointers to A.4 / A.5 (M1 above) are bugs, not
migration-note errors.

### m4. Round-2 carryover statement glosses
Line 889 ("Carried over from v1 Round 1 changelog (historical
record).") lists the Round-1 items as preserved. The task brief
described this as "v2 changelog (followed by retained Round 1
changelog)" — the v2 actually replaces the verbose Round 1 changelog
with a one-line synopsis. This is editorially fine but slightly
divergent from the brief's structural description. Not a defect.

### m5. Old "Remark 4.1.3" no longer exists
Round 2 m4 asked for a pointer from §3.2 to Remark 4.1.3 (Riesz
normalization). In v2 the entire Remark 4.1.x apparatus is gone — only
Remark 6.1.1 survives (line 456). The Riesz normalization $2\sin(\pi
\gamma/2)$ is now stated inline in §3.2 (line 156 half-sum identity)
and §3.3 (line 168 boxed $\kappa$); §4.1 line 196 boxes it again.
Round 2 m4 is therefore moot, not regressed. ✓

### m6. §3.5 says ML appears in "§6.1, Theorem 6.1"
Verified: §6.1 is "Bounded interval with temporary impact: Mittag–
Leffler resolvent" containing Theorem 6.1. ✓

### m7. AJNT arXiv:2403.10273 consistency
Eight occurrences spanning abstract, §1.2, §1.3, §2.5, §5.3.4, §6.3,
§9.3, App A.3 Part 4. All cite arXiv:2403.10273. ✓ (Round 2 m3
deferred to online verification — not done here; the *internal*
consistency is fine.)

### m8. Bouchaud year
Body line 49 = 2004; refs line 833 = 2004. ✓ Resolved (Round 2 m5
worker had used 2003; v2 standardizes on 2004 per migration note §3.5).

### m9. ⚠️ / TODO marker audit (12 markers, all honest)
Twelve markers located:

1. Line 3 — status preamble (meta).
2. Line 327 — Forde kernel-matching (Conj 5.2.2). Honest, tied to
   M1/m2 above.
3. Line 367 — precise $\int_0^T u^{\rm bulk}$ constant for OU. Honest;
   conservative $O(\sqrt T)$ used, T-rate unchanged.
4. Line 454 — Theorem 6.1 Neumann radius. Honest, but pointer is
   broken (M1).
5. Line 581 — appendix preamble (meta).
6. Line 631 — 3×3 system non-singularity for $(c_1, c_2, \lambda)$.
   Honest; load-bearing for Cor 5.2 and Prop 5.3 Step 3 but flagged
   in both A.2 Part 1 and A.2 Part 2(ii).
7. Line 677 — HLS estimate on bounded interval, $c_1/c_2$
   conditioning, OU sharpening. Honest, three sub-items each scoped.
8. Line 734 — $\Pi_+$ $L^2$ bound, Krein quantitative constants.
   Honest.
9. Line 748 — Neumann-radius HLS constant (App B.1). Honest.
10. Line 766 — boundary-tail correction to interior $R_{\gamma,\eta}$.
    Honest; explicit suggestion to restate Thm 6.1 "on the bulk region
    of $[0,T]$" if not derived.
11. Line 792 — multi-asset budget translation (App C). Honest, low-
    risk.
12. Line 812 — Jacobi-spectral vs WSGD endpoint accuracy benchmark.
    Honest, numerical-only.

Classification: 2 meta + 10 legitimate deferrals. Spot-checked #6, #9,
#10 — none conceal a load-bearing gap; #6 and #9 are the largest, but
both are clearly flagged at their proof sites *and* in the §9.2 open-
problems list (lines 564–571). The Theorem 6.1 statement does already
write "away from the boundary $\{0,T\}$" (line 444), so the #10 scope
restriction is honest from the outset.

### m10. Body Prop 5.3 sketch (§5.2.5) vs Appendix A.2 Part 2 rigorous version
Constants and conclusions cross-checked.

| Item | Body §5.2.5 | App A.2 Part 2 | Match? |
|---|---|---|---|
| $\int_0^T \phi_1\,dt$ | $T^\gamma B((\gamma+1)/2, (\gamma+1)/2)$ (line 348) | same (line 651) | ✓ |
| $\int_0^T \phi_2\,dt$ | 0 by oddness (line 350) | 0 by oddness (line 649) | ✓ |
| $|c_1|$ scaling | $\Theta((X_0+M)/T^\gamma)$ (line 352) | $\Theta((X_0+M)/T^\gamma)$ (eq. A.2.2, line 653) | ✓ |
| Final bound | $O((X_0+M)/T)$ on bulk (line 334) | $O((X_0+M)/T)$ on bulk (line 670) | ✓ |
| Non-uniformity | endpoints $(s(1-s))^{(\gamma-1)/2}$ blow-up | Step 5 same | ✓ |

The body sketch is a faithful preview of the appendix proof.

### m11. Notation unification
- $\mathbb{D}^{1-\gamma}$ (line, §3.2 first paragraph, §4 throughout)
  vs $\mathbb{D}^{1-\gamma}_{[0,T]}$ (bounded interval, §3.2 second
  paragraph onwards, Cor 5.2, App A.2, C, D). No backslide. ✓
- $\bar\alpha(t,\cdot)$ vs $\bar\alpha(t,s)$: consistent — the
  "function-at-$t$" notation $\bar\alpha(t,\cdot)$ is used as an
  *argument* to $\mathbb{D}^{1-\gamma}$ (which acts in the second
  slot), then evaluated at $t$ via "$(\cdot)(t)$" or "$\bar\alpha(t,s)$"
  inside an integrand. No collisions.
- Round 2 n7 grep checks (`\mathbb{D}^\gamma`, `\kappa_\gamma` without
  `1-`, `\mathcal{B}_\gamma`) re-run on v2: still 0 stray
  occurrences outside the changelog narrative. ✓

### m12. $\kappa_{1-\gamma}$ uniformity (independent grep)
Every occurrence of $\kappa_{1-\gamma}$ in body or appendices evaluates
to $(2c\,\Gamma(1-\gamma)\sin(\pi\gamma/2))^{-1}$ either explicitly or
via $c_\gamma^{-1}$. Locations: abstract line 21, §1.2 line 45, §3.3
boxed line 168, Thm 4.1 line 196, A.1 line 601, A.2 line 629, §5.3.3
line 412, Thm 6.1 limit line 764, Thm 7.1 line 503, App C line 784,
788. Constant is consistent. ✓

### m13. D-decision audit
All five locked decisions visible in the v2 file (independent grep):

| Decision | Body location | Body text |
|---|---|---|
| D1 = B | line 83 (§2.1) | "kernel exponent $\gamma$ … (decision D1 = B)" |
| D3 = A | line 89 (§2.2) | "the identically-zero $\mathbb{E}_t[\alpha_T]$ … omitted (decision D3 = A)" |
| D4 = A | line 326 (Conj 5.2.2) | "Per decision D4 = A, we leave the recovery as a conjecture" |
| D5 = A | line 170 (§3.3) + line 612 (A.2) + line 881 (changelog) | "(decision D5 = A in the migration note)" |
| D6 = A′ | line 380 (§5.3.1) | "per decision D6 = A′" |

All five confirmed. ✓

### m14. Changelog accuracy spot-checks (7 claims verified)
1. "Theorem 4.1 (v2): bulk theorem … on $\mathbb{R}$." Body Thm 4.1 line
   194: matches. ✓
2. "Corollary 5.2 (v2) … was v1 Theorem 4.1, demoted." Body Cor 5.2
   line 297 header reads "demoted v1 Theorem 4.1". ✓
3. "Proposition 5.3 … $O((X_0+M)/T)$ on $[\epsilon T, (1-\epsilon)T]$."
   Body Prop 5.3 line 331 matches. ✓
4. "Cor 5.4 (v2, new) — $u^* = u^{\rm bulk} + O(1/T)$." Body line 362
   matches. ✓
5. "Thm 6.1 (v2): Mittag–Leffler resolvent — was v1 Thm 5.1." Body
   line 442 header matches. ✓
6. "D5 = A applied: $\kappa_{1-\gamma} = (2c\Gamma(1-\gamma)\sin(\pi
   \gamma/2))^{-1}$." Verified at §3.3 line 168 and uniformly (m12).
7. "Economic gloss — §5.2.3 added: U-shape via cheap-trading windows."
   Body §5.2.3 lines 313–320 present and matches. ✓

Changelog is faithful to what is in the file. The one **inaccuracy** in
the migration-note-meets-body story is M2 above: the changelog says
six new bib entries are "added"; three of them are added to References
but not actually cited in the text.

### m15. Migration-note accuracy
Migration table (`v1-to-v2.md` §2) cross-checked against v2:

- "**§4.1 Theorem 4.1 (bounded interval) → §5.2 Corollary 5.2 (demoted)**" ✓ (body line 297 says "demoted v1 Theorem 4.1").
- "**§5.4 Wiener–Hopf → §5.3**" ✓ (§5.3 lines 376–434).
- "App A (proof of v1 Thm 4.1) → A.1 + A.2" ✓ but
  v2 also has A.3 (W–H lifted from v1 App B), which is captured in
  the next row of the table — both correct.
- "v1 §5.4 inventory-risk penalty → dropped (D6 = A′), GP pointer in
  §6.4" ✓ (§6.4 lines 474–476).
- "App C light edits" ✓ (eigenbasis derivation unchanged modulo
  $\kappa$ correction).
- "App D … symmetric Grünwald rescaling clarified" ✓ (App D lines
  808–813 — explicit $1/(2\sin(\pi\gamma/2))$ note added).
- "App E added Cor 5.4 $O(1/T)$ diagnostic" ✓ (App E item 4, line 826).

Migration table is faithful.

---

## Fixes worth doing now (F#)

### F1. Repoint "Appendix A.4" → "Appendix B"
Two edits:
- Line 454 (Thm 6.1 proof): "Full computation: Appendix A.4." →
  "Full computation: Appendices B.1–B.2."
- Line 567 (§9.2): "(Appendix A.4 hand-wave)" → "(Appendix B.1
  hand-wave)".

### F2. Fix or excise the "Appendix A.5" pointer in Conjecture 5.2.2
Line 325: either (a) add a short Appendix A.5 stub recording the half-
line-semigroup obstruction that prevents the GSS-style proof (this is
already verbally stated in the conjecture body — promoting it to A.5
is a paste), or (b) drop the pointer and leave the conjecture with
only its ⚠️ TODO. Option (a) preserves the disclosure surface; option
(b) is the smaller edit.

### F3. Cite or drop Webster (2023), Cartea–Jaimungal–Penalva (2015), Novokshenov (2015)
- **Webster 2023** is naturally cited in §1.3 (related work) or §9.1
  (empirical protocol) as a current handbook on price-impact modelling.
- **Cartea–Jaimungal–Penalva 2015** is the obvious textbook citation
  for §1.3 algorithmic-trading positioning and for Remark 6.1.1's
  Cartea–Jaimungal myopic policy (line 456) — converting the existing
  "Cartea–Jaimungal (2016)" inline cite there to "Cartea–Jaimungal–
  Penalva (2015) Ch. 7 / Cartea–Jaimungal (2016)" would be one line.
- **Novokshenov 2015** is a v1 holdover; either cite in App A.3 Part 1
  as supporting reference for the finite-segment factorization or drop
  it. Lower-priority than Webster / CJP.

Mirror image of Round 2 F1 (MMS).

### F4. Numbering gap 5.6
Either renumber Cor 5.7 → Cor 5.6 (single global find-replace; six
occurrences: lines 50, 297, 407, 416, 423, 723) or insert a one-line
editorial note in §5.3.3 explaining the skip. Renumbering is cleaner
and avoids a permanent footnote.

---

## Summary

The v2 spine is consistent and the Round 2 fixes hold. Two real
problems remain:

- **M1 — three broken appendix pointers (A.4, A.5).** Pure migration
  bookkeeping; one-line edits via F1, F2.
- **M2 — three bib orphans (Webster, CJP, Novokshenov).** Pattern
  identical to Round 2 m1; F3 closes it.

Plus a minor numbering gap (no §/Cor 5.6). Everything else —
$\kappa_{1-\gamma}$ uniformity, $\bar\alpha$ notation, $(\star_{\rm
bulk}/(\star_{\rm WH})/(\star)$ labels, Theorem-numbering chain,
D1/D3/D4/D5/D6 decisions, migration-note fidelity, ⚠️/TODO honesty,
body-vs-appendix Prop 5.3 reconciliation — checks out cleanly.
