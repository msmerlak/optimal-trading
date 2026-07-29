# Tone review — "Optimal Trading Filters" v2: over-confidence and the LLM register

**Artifact:** `v2/optimal-trading-filters-v2.tex` (18 pp.)
**Scope:** prose tone only, at the author's direction: the paper "reads too much like LLM-generated stuff with over-confident pronouncements." Substance was reviewed separately (`outputs/optimal-trading-filters-v2-review.md`); nothing here changes a mathematical claim.
**Evidence:** `outputs/.drafts/v2-tone-humility-review-evidence.md` (quoted passages with line numbers).

---

## Summary Assessment

The diagnosis is correct, and it is worth being precise about what produces the effect, because the paper already passes the project's explicit style rules (no rhetorical questions, no throat-clearing, no negation-foils). What remains is a *cadence* problem: roughly fourteen sentences in eleven pages of prose end on a verdict or an epigram — "becomes the operative constraint," "is then forgotten," "one that never fully forgets," "the singularity any impact term regularizes," "adaptedness destroys the value." Any one of these would be fine; a human author lands two or three per paper, usually in the introduction and conclusion. At more than one per page, delivered in a uniformly impersonal voice with no hedging anywhere, the effect is oracular — every paragraph closes with a pronouncement, and the reader starts to feel lectured by something that has never been unsure of anything. That is the LLM register.

The fix is not to weaken the theorems. The proved and numerically verified statements (Lemma 1, the propositions, "exactly when $2c_1\Phi>1$", the $\sin(\pi\beta/2)$ law) have earned their declarative form and should keep it. The fix is to (i) demote the *interpretive* verdicts to observations, (ii) break the punchline cadence in about ten places, (iii) let an occasional "we" and an honest hedge into the prose, and (iv) use each vivid image once instead of twice.

---

## Strengths

- The confidence is at least *calibrated*: I found no passage where an over-confident sentence asserts something unproved. The tics are rhetorical, not epistemic — every verdict sentence sits on top of a result that is in fact proved or verified. This makes the repair cosmetic rather than structural.
- The impersonal register, used sparingly, is appropriate for the venue; the problem is uniformity, not the register itself.
- Some of the strongest lines deserve to survive. Recommendations below preserve one instance of each image.

## Critical Issues

None. Tone does not rise to critical; no claim is wrong or overstated relative to the mathematics.

## Major Issues

**T1. Verdict-sentence density (the core complaint).** The paper repeatedly states an observation and then pronounces on its significance in the same breath. The named example, §1.2 (L64):

> "Adaptedness, the requirement that $u_t$ be measurable with respect to the information $\F_t$, becomes the operative constraint. It is a constraint of an unusual kind: a closed subspace of $L^2$ cut out by an increasing family of $\sigma$-algebras."

Two pronouncements in two sentences ("operative constraint," "unusual kind"). A humbler version keeps the content and drops the gavel:

> "Adaptedness — the requirement that $u_t$ be measurable with respect to $\F_t$ — is what remains binding. As a constraint it is awkward to handle directly: a closed subspace of $L^2$ cut out by an increasing family of $\sigma$-algebras, rather than a finite set of equations."

**T2. Epigram cadence at paragraph ends.** The clearest instances, with suggested demotions:

| Location | Current | Suggested |
|---|---|---|
| §4 opening (L272) | "…decays on the single timescale $1/\kappa$ and is then forgotten." | "…decays on a single timescale $1/\kappa$, after which little of it remains." |
| §4.1 (L276) | "Short-memory impact produces a short-memory policy; long-memory impact produces one that never fully forgets." | "The policy inherits this: a short-memory kernel gives a filter with finite memory, a long-memory kernel one whose weights decay only algebraically." |
| §5.3 (L377) | "…the position jumping to its target, the singularity any impact term regularizes." | "…the position jumping to its target; adding any impact cost smooths this out." |
| §3 (L258) | "The memory is maximal: the Marchaud representation…" | "The filter's memory is now long-ranged: the Marchaud representation…" |
| §4.2 (L290) | "…adaptedness becomes free…; …adaptedness destroys the value." | "…the gap closes and adaptedness costs little; …most of the value is out of reach without foresight." |

**T3. "Precisely / exactly" as rhetorical intensifiers.** Keep them where they carry mathematical content ("the rate reverses exactly when $2c_1\Phi(\theta)>1$" — this is the theorem), remove where they are emphasis: L71 "precisely because $Q$ is non-local" → "because $Q$ is non-local"; L333 "precisely what the stationary theory omits" → "what the stationary theory leaves out."

**T4. No hedges, no persons.** The paper never says "we" after the abstract and never concedes uncertainty in prose (the limitations paragraph does, but in the same declarative voice). Three or four low-cost humanizers would break the oracle effect: e.g. §1.3 "These three names describe a single object seen at different levels of structure" → "We regard these as three names for the same construction, met at different levels of generality"; §4.3's manipulation caveat could carry "at least within the model class we can analyze"; §5.2 could admit "we have not tracked the constants."

## Minor Issues

1. **The whiten–project–color triad appears twice** (abstract-adjacent §2.2 and again in prose). Memorable once, incantatory twice. Keep the §2.2 instance, paraphrase the other.
2. **"Ride the residual" / "transient-impact wake"** (L319, L328): two nautical images for the same phenomenon within one subsection. Keep one.
3. **"The single operator inversion" / "the single number $\rho$" / "the single timescale"** (L60, L232, L272): "single" as drama, three times. "One" or nothing.
4. **Cadenced triples** ("a broker must work a parent order…, or liquidate an inherited position…, ending flat, $x_T=0$", L333): fine on its own; noted because rhythm-uniformity is the aggregate problem.
5. The conclusion still opens with a compressed restatement of the thesis in verdict form; after T1–T2 edits elsewhere it may read fine, but check it last against the new baseline.

## Reproducibility and Verification

| Check | Status |
|---|---|
| Passage inventory | Verified — every quoted passage grep-located in `v2/optimal-trading-filters-v2.tex` (line numbers in evidence notes) |
| Earned vs unearned confidence | Verified against the prior substance review: all flagged sentences are rhetorical surplus on top of proved/verified claims; no proposed rewrite alters a mathematical statement |
| Density estimate (~14 punchlines / 11 pp.) | Count from the inventory; approximate by nature |
| Overlap with prior style review | Checked — `reviews/v2-style-review.md` covered the AGENTS.md prohibitions (different axis); no double-counting |

## Inline Annotations

- **§1.2, L64** — T1, the named example; rewrite above.
- **§1.2, L71** — T3 ("precisely because").
- **§1.3** — T4 ("three names… single object" → add "we regard"); "The remaining sections work out this object and its consequences" is fine post-revision.
- **§2.2** — keep the whiten/project/color triad *here*, cut its twin.
- **§3, L251/L258** — "adaptedness is free" (keep; it is literally true and plainly stated) vs "The memory is maximal" (soften, T2).
- **§4, L272/L276** — the two flagship epigrams; rewrites in T2 table.
- **§4.2, L290** — "destroys the value" (T2).
- **§4.3, L312** — "exactly when $2c_1\Phi>1$": **keep**, earned.
- **§4.3, L319–L328** — one wake metaphor, not two (Minor 2).
- **§5.1, L333/L347** — "precisely what the stationary theory omits" (T3); "pins the anchoring" is fine.
- **§5.3, L377** — punchline (T2 table).

## Recommendation

A half-day prose pass, applying T1–T4 and the minors: roughly 12–15 sentence-level edits, none touching mathematics. The paper's rules-based style is already clean; this pass is about breaking a uniform cadence and letting the authors sound occasionally uncertain, which — given that the uncertain parts (constants in Prop. 3, the dense-domain hypothesis) genuinely exist — is also more accurate. I'd suggest making the edits and then reading §1 and §4 aloud; if a paragraph still ends on a drumbeat, flatten its last sentence.

## Sources

- `v2/optimal-trading-filters-v2.tex` — reviewed manuscript (all quotes; grep line numbers in evidence)
- `outputs/.drafts/v2-tone-humility-review-evidence.md` — passage inventory
- `outputs/optimal-trading-filters-v2-review.md` — prior substance review (earned-confidence calibration)
- `reviews/v2-style-review.md` — prior rules-based style review (non-overlap check)
