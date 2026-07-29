# Pressure-Test Review — `execution-solution-methods.md`

**Task:** Adversarial verification pass on the literature-accuracy review draft
(`outputs/execution-solution-methods.md`) against its evidence log
(`notes/execution-solution-methods-publications.md`). Scope: claim-to-evidence
integrity, single-source exposure, logical gaps/overclaims, zombie sections,
untethered recommendations. Not a rewrite.

---

## Part 1: Structured Review

## Summary

The draft is a competent, mostly well-sourced literature-accuracy review. Its
central factual finding (AJN's §1.4 characterization as a "stochastic Volterra
equation of the second kind" is not AJN's stated object) is genuinely supported
by the evidence log and by AJN's abstract, and its strongest missing-citation
finding (Abi Jaber–De Carvalho–Pham 2024) is confirmed verbatim against the
source abstract during this pass. However, the draft contains **two
delivery-blocking defects**: (1) an affirmative novelty endorsement ("does
appear novel in execution") that is outside the review's own declared scope and
rests on absence-of-evidence, and (2) a Cartea–Jaimungal citation whose
year/title/venue metadata in the evidence log is internally inconsistent and
points at the wrong paper. Several findings also carry single-source exposure
beyond the one the draft already self-flags, and one recommendation (the
Volterra→Fredholm substitution) is stated more confidently than the draft's own
"Disagreements" section warrants.

## Strengths

- [S1] The core AJN finding (AI-1) is correctly sourced: the evidence log
  Section B records "NOT SUPPORTED by AJN's abstract" and quotes AJN's actual
  object ("free-boundary L²-valued backward stochastic differential equation and
  an operator-valued Riccati equation"). The draft does not overstate this.
- [S2] MR-1 (Abi Jaber–De Carvalho–Pham 2024) is verified: the source abstract
  reads "The optimal control is given explicitly in terms of the corresponding
  Lagrange multipliers and their conditional expectations, as a solution to a
  linear stochastic Fredholm equation" — matching the draft's quotation and the
  claimed structural parallel to §4.
- [S3] The draft already self-flags the AJN Volterra/Fredholm wording as the
  single-source-sensitive point and explicitly records that a direct AJN
  paper-Q&A call failed — honest disclosure of evidence limits.
- [S4] Recommendations 1–4 each map to a labeled finding (AI-1, MR-1, MR-2,
  MR-3/MR-4). No orphan recommendations; no obviously zombie sections.

## Weaknesses

- [W1] **FATAL — novelty overclaim outside declared scope.** The draft's stated
  scope is "literature accuracy … *Not a novelty/correctness audit of the
  paper's own results*." Yet MR-4 concludes: "No evidence was found of a prior
  optimal-*execution* paper using Wiener–Hopf factorization for the trading
  policy itself — the paper's application does appear novel in execution." This
  is (a) an affirmative novelty endorsement the review disclaimed making, (b) an
  absence-of-evidence inference (a non-comprehensive search cannot establish
  novelty), and (c) unsupported by any positive item in the evidence log
  (Section C/E contain no novelty-confirming source). If delivered, an author
  could quote it as external validation of a novelty claim. Must be cut or
  reduced to a strictly negative, hedged statement ("no prior execution use
  surfaced in our search; we did not attempt an exhaustive novelty search").

- [W2] **FATAL — Cartea–Jaimungal citation metadata is wrong.** Evidence log
  Section C names "Cartea, Jaimungal (2013), 'Optimal execution with Markovian
  signal' (Appl. Math. Finance 20:512–547)." That venue (AMF Vol. 20, No. 6,
  2013, pp. 512–547) is a **different** paper — "Modeling Asset Prices for
  Algorithmic and High Frequency Trading," a hidden-Markov-model asset-pricing
  paper, not an optimal-execution-with-signal paper. The "optimal execution with
  a general Markovian signal / closed-form optimal strategies" result is
  routinely attributed to **Cartea–Jaimungal 2016** (see arXiv:2306.00621:
  "Cartea and Jaimungal (2016) who examine optimal execution with a general
  Markovian signals and derive closed form optimal strategies"). The draft
  propagates "Cartea–Jaimungal (2013)" into Recommendation 3 and the tables. As
  written, following the recommendation risks inserting a wrong year/venue into
  the paper's `.bib`. Must resolve the year/title before delivery. (The
  substantive point — CJ pioneered signal-in-execution — survives; only the
  bibliographic pairing is defective.)

- [W3] **MAJOR — "closest prior art to §4" is an unbacked superlative.** The
  parallel between AJ-DC-Pham's multiplier/conditional-expectation device and
  the paper's §4 is real and now externally confirmed, but "*the closest* prior
  art to §4" asserts a completed survey of all §4-relevant prior work. The
  evidence log supports "directly parallels" and "strongest missing-citation
  finding," not a proven global minimum. Soften to "the most directly parallel
  prior work identified."

- [W4] **MAJOR — AI-1 recommendation is more confident than the draft's own
  hedge.** Recommendation 1 leads with substituting "Volterra" →
  "**Fredholm**." But: (i) the Disagreements section admits AJN's theorem
  statement was never extracted (paper-Q&A call failed); (ii) "Fredholm" is the
  reviewer's inference and is AJ-DC-Pham's term, *not* AJN's — AJN's stated
  object is the free-boundary BSDE + operator Riccati; (iii) the
  symmetric-kernel → Fredholm argument ("$G(|t-s|)$ on $[0,T]$ is symmetric") is
  reviewer-supplied and appears nowhere in the evidence log. That argument is
  sound for the *deterministic* cost functional (it is essentially GSS's
  result), but the *stochastic, adapted-signal* case introduces conditional
  expectations / forward–backward structure where "it's Fredholm not Volterra"
  is not a clean substitution. Recommendation 1 should lead with AJN's actual
  characterization (BSDE + operator Riccati) and offer "stochastic Fredholm" only
  as the variational-form (AJ-DC-Pham) alternative — matching, not exceeding, the
  Disagreements caveat.

- [W5] **MAJOR — single-source exposure beyond the self-flagged AJN point.**
  Several findings rest on one source each and should carry the same
  single-source caveat the draft applies to AJN:
  - Cartea–Jaimungal "**among the first**" rests solely on NV's characterization
    (evidence log Section A/C: "NV 2002.09549 … 'among the first were Cartea &
    Jaimungal'"). Single interpretive source.
  - Whiteman/Hansen–Sargent as the "**nearest methodological ancestor**" of the
    paper's approach rests on one MaRDI catalog entry plus reviewer inference.
  - The Politesi "existence-proof gap in AJ et al. 2024" rests on a single
    unrefereed master's thesis (draft already hedges "worth a glance," but the
    single-source status should be explicit).
  - **Forde et al. 2022** is labeled "Cited & recovered (§5.2) — **accurate**" in
    the table, but the evidence log has no external source for it (Section A:
    "(paper cite; consistent with Fredholm family)"). Labeling it "accurate"
    overstates the verification actually performed.

- [W6] **MINOR — recovery claims are not in the evidence log.** "Recovered in
  §5.1 as the one-average case" (GP), "two-average case" (NV), "U-shaped
  power-law liquidation profile in §5.2" (GSS), and Forde "recovered (§5.2)" are
  not documented in the evidence log; they rest on the reviewer's reading of
  `v2/optimal-trading-filters-v2.tex`. This is legitimate for a reviewer, but the
  draft presents them alongside externally-sourced attributions without marking
  that they are verified against the paper itself rather than the literature. A
  one-line provenance note would prevent a reader from assuming external backing.

## Questions for Authors (of the review draft)

- [Q1] Was §4 of the object paper actually read closely enough to support
  "closest prior art," or is the parallel inferred from AJ-DC-Pham's abstract
  plus the §4 summary in the evidence log? (Bears on W3.)
- [Q2] Which specific Cartea–Jaimungal work does NV cite as "among the first,"
  and is it 2013 (book / HMM paper) or 2016 (signal-in-execution)? Resolving this
  fixes W2.
- [Q3] Did any source confirm the Forde et al. "Fredholm on Wiener chaos" and
  §5.2 recovery, or is the "accurate" label based on reading the paper? (W5.)
- [Q4] For AI-1, has AJN's actual theorem statement now been checked, or is the
  "Fredholm" substitution still inferred? (W4.)

## Verdict

The artifact is close to deliverable but **not ready as-is**. Two FATAL items
(W1 novelty overclaim / scope breach; W2 wrong Cartea–Jaimungal citation
metadata) must be fixed before delivery because each would inject a defect into
the downstream paper edit. The MAJOR items (W3–W5) are hedging/attribution
tightening that belong in Open Questions rather than blocking, but W4 in
particular should be reconciled so the recommendation does not outrun the
evidence. Revision risk is **moderate and localized** — the core findings (AI-1
direction, MR-1) hold up under external check; the defects are in framing
strength, one bibliographic pairing, and unhedged single-source items.
Confidence: **medium-high** on the two FATAL calls (both externally verified this
pass), medium on the single-source characterizations.

## Revision Plan

1. **[W1]** Delete "the paper's application does appear novel in execution."
   Replace with a scope-consistent negative: "our search surfaced no prior
   optimal-execution paper using Wiener–Hopf factorization for the trading
   policy; we did not attempt an exhaustive novelty search." Remove the novelty
   endorsement from the Bottom Line if it echoes there.
2. **[W2]** Verify the Cartea–Jaimungal year/title against NV's actual reference
   list. Correct the evidence-log entry (AMF 20:512–547 = "Modeling Asset Prices
   for Algorithmic and High Frequency Trading," not "Optimal execution with
   Markovian signal") and set the recommended citation to the correct
   signal-in-execution work (likely CJ 2016) before advising the author to add it.
3. **[W3]** Soften "closest prior art to §4" → "the most directly parallel prior
   work we identified."
4. **[W4]** Reorder Recommendation 1: lead with AJN's actual object (free-boundary
   BSDE + operator Riccati); present "stochastic Fredholm" as the AJ-DC-Pham
   variational-form alternative; drop or footnote the symmetric-kernel argument
   as a deterministic-case remark, noting the adapted-signal case is subtler.
5. **[W5]** Add explicit single-source flags to: CJ "among the first" (NV only),
   Whiteman "nearest ancestor" (one catalog entry + inference), Politesi gap (one
   thesis). Downgrade the Forde table cell from "accurate" to "consistent (not
   independently sourced)."
6. **[W6]** Add a one-line provenance note that §5 recovery claims are verified
   against the object paper's text, not the external literature.

---

## Part 2: Inline Annotations

> "No evidence was found of a prior optimal-*execution* paper using Wiener–Hopf factorization for the trading policy itself — the paper's application does appear novel in execution."

**[W1] FATAL:** Contradicts the draft's own scope line ("Not a novelty/correctness
audit of the paper's own results") and converts absence-of-evidence into an
affirmative novelty endorsement. No positive source in the evidence log supports
it. Cut or reduce to a strictly negative, hedged search note.

> "Cartea, Jaimungal (2013), 'Optimal execution with Markovian signal' (Appl. Math. Finance 20:512–547)." *(evidence log, Section C)* — propagated to the draft as "Cartea–Jaimungal (2013)."

**[W2] FATAL:** AMF Vol. 20 (2013), pp. 512–547 is "Modeling Asset Prices for
Algorithmic and High Frequency Trading" (a hidden-Markov-model paper), not an
optimal-execution-with-signal paper. The signal-in-execution / closed-form result
is generally cited as Cartea–Jaimungal **2016** (cf. arXiv:2306.00621). Fix the
year/title/venue before recommending the citation into the paper's bibliography.

> "It is uncited and is the closest prior art to §4."

**[W3] MAJOR:** The parallel is real and externally confirmed, but "*the closest*
prior art" is a superlative the evidence supports only as "directly parallels /
strongest missing citation." Soften to "the most directly parallel prior work
identified."

> "change 'linear stochastic Volterra equation of the second kind' → 'stochastic **Fredholm** equation'"  *(Recommendation 1)*

**[W4] MAJOR:** More confident than the draft's own Disagreements caveat ("a
direct paper-Q&A call failed once … the exact phrasing to substitute should be
checked against AJN's Theorem statement before editing"). "Fredholm" is
AJ-DC-Pham's term, not AJN's; AJN's stated object is a free-boundary BSDE +
operator Riccati. Lead the recommendation with AJN's actual characterization.

> "The propagator kernel $G(|t-s|)$ on $[0,T]$ is symmetric, so the first-order condition is a **Fredholm** equation, not a Volterra one."

**[W4] MAJOR:** Reviewer-supplied argument not present in the evidence log. Valid
for the deterministic cost functional (essentially GSS's result), but the
stochastic adapted-signal case involves conditional expectations / FB structure
where the Volterra-vs-Fredholm dichotomy is not a clean substitution. Present as
a deterministic-case remark, not a blanket correction.

> "Credited by Neuman–Voß as 'among the first' to incorporate a Markovian signal into an optimal-execution stochastic-control problem [NV]."

**[W5] MAJOR (single-source):** Rests solely on NV's characterization. Apply the
same single-source caveat the draft gives the AJN point.

> "the frequency-domain-LQ precedent especially, since it is the methodological ancestor of the paper's own approach." / "its nearest methodological ancestor"

**[W5] MAJOR (single-source + interpretation):** Backed by one MaRDI catalog entry
plus reviewer inference. Downgrade "the methodological ancestor" → "a
methodological precedent."

> "Forde et al. 2022 | Fredholm on Wiener chaos | Cited & recovered (§5.2) — **accurate**"

**[W5] MAJOR:** Evidence log has no external source for Forde ("(paper cite;
consistent with Fredholm family)"). "Accurate" overstates the check performed;
use "consistent (not independently sourced)."

> "Recovered in §5.1 as the one-average case." / "Recovered in §5.1 as the two-average case." / "recovers their U-shaped power-law liquidation profile in §5.2."

**[W6] MINOR:** Not documented in the evidence log; based on reading the object
paper's `.tex`. Legitimate, but mark as verified-against-the-paper so it is not
read as externally-sourced consensus.

---

## Sources (inspected this pass)

- Cartea–Jaimungal 2013 venue disambiguation (AMF 20:512–547 = HMM asset-pricing paper): https://ideas.repec.org/a/taf/apmtfi/v20y2013i6p512-547.html ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1722202
- Signal-in-execution attributed to Cartea–Jaimungal 2016: https://arxiv.org/pdf/2306.00621
- AJ-DC-Pham abstract wording confirmed ("Lagrange multipliers and their conditional expectations … linear stochastic Fredholm equation"): https://arxiv.org/html/2409.12098 ; https://arxiv.gg/abs/2409.12098
- Abi Jaber publication list (AJ-DC-Pham 2024; "Stochastic Fredholm equations … for propagator models"): https://sites.google.com/view/abijabereduardo/
