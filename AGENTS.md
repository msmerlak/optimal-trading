# Style rules for this project

## Writing

- **Avoid rhetorical questions.** Do not use interrogative sentences to structure exposition (e.g. "But is this really optimal? Consider..."). State the claim directly.
- **Avoid the "X is not Y, it genuinely Z" rhetorical construction** and its variants:
  - "X is not merely Y, it is Z."
  - "This is not X — it is Y."
  - "Rather than X, this is really Y."
  - "X is not the answer; Z is."
  - "The reframing is not vacuous."
  - "These are not defects — they are features."

  Instead, assert the positive claim directly. Do not motivate a claim by first stating and then negating an unstated foil.
- **Avoid empty intensifiers**: "canonical", "genuine", "true", "essential", "deep", "structural feature of", "the point of the paper", "the essence of X", "the cleanest possible X", "the naïve analog" — unless they carry technical content. Do not use "structural" as a decorative synonym for "important"; use it only when contrasting with non-structural (numerical, incidental, model-dependent).
- **Avoid self-promotional framing.** Do not write "sets the mathematical content of this paper", "this is the object we compute", "the interpretation is direct", "what remains is the essential X". State the claim; the reader can infer its importance from the section it appears in.
- **No "the formula/composition/expression reads/says X" openers.** Do not preface an unpacking of a formula with "reads inside out", "tells us that", "can be read as", "admits the interpretation". Just state what the terms are.
- **Do not disparage prior work by implication.** Avoid weight/burden metaphors like "the analytic weight is carried by", "X occupies the exposition", "the trade rate is expressed implicitly". Describe what prior treatments produce as neutral facts; state what the current paper adds as a positive claim.
- **Avoid the negation-motivation opening**, e.g. "No closed form displays X", "There is no result that Y", "The absence of X is a feature of Y". Lead with the positive statement of what the paper or section establishes.
- **Avoid summary sentences that restate the section thesis in negation form**, e.g. "Sign flips are cost-optimal, not diagnostic errors." State the positive claim ("Sign flips at these frequencies are cost-optimal.") without the foil.
- **Prefer declarative over hortative.** Do not write "let us now consider", "we now turn to", "notice that". Just make the claim.
- **No throat-clearing.** No "It is worth noting that", "Importantly", "Interestingly", "It is well known that".
- **Cite specifics.** When claiming a result is standard, give the reference. When claiming novelty, cite the closest prior work explicitly.

## Structure

- PNAS-form drafts: Significance statement (~120 words), Abstract (~250 words), numbered references, Materials and Methods at end, no separate section for related work (integrate into introduction).
- **Do not clutter papers with dead ends.** Explorations that were tried and failed (unsuccessful special-function reductions, negative numerical results, abandoned ansatzes) belong in `CHANGELOG.md`, experiment scripts, or internal notes — not in the paper. The paper states what holds, not the history of what was tried. Exception: a dead end deserves paper mention only when a reader would plausibly try the same path and needs to be warned off, and even then in a single sentence with a citation, not a paragraph of reasoning.
