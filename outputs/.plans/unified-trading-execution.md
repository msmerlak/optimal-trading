# Plan: literature review on unified trading + execution

**Trigger.** Reviewer M3 (finance) on `papers/fractional-derivative-optimal-execution.md` flagged that §5.4 (Wiener–Hopf half-line) conflates *execution* (finite inventory, terminal constraint) with *stationary-signal portfolio choice* (Gârleanu–Pedersen). User asked: is there a unified framework?

**Question.** What is the state of the art on unified treatments of (a) optimal portfolio trading (predictable signals, risk penalty, possibly infinite horizon) and (b) optimal execution (finite inventory $X_0$, terminal constraint $X_T = X^*$, finite horizon $[0,T]$)?

**Plan.**
1. Search literature on unified portfolio-execution frameworks. ✓ (done above)
2. Catalog candidate frameworks; classify by (i) cost-functional form, (ii) impact-kernel class, (iii) terminal-handling mechanism, (iv) signal model.
3. Identify the meta-cost-functional whose parameter limits subsume execution, GP-style stationary trading, and the §5.4 W–H regime.
4. Map each special case to its limiting form.
5. Recommend the natural framing for the §5.4 fix.
6. Provenance file with URLs and arXiv IDs.

**Slug.** `unified-trading-execution` (3 words, hyphens, lowercase).

**Out paths.**
- `outputs/unified-trading-execution.md` — main artifact
- `outputs/unified-trading-execution.provenance.md` — sources
- `outputs/.plans/unified-trading-execution.md` — this file
