# Task for worker

You are a delegated subagent running from a fork of the parent session. Treat the inherited conversation as reference-only context, not a live thread to continue. Do not continue or answer prior messages as if they are waiting for a reply. Your sole job is to execute the task below and return a focused result for that task using your tools.

Task:
Apply a fixed, enumerated set of fixes to an applied-math paper and its companion scripts. Repo: /Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading. Main file: v3/optimal-trading-filters-v3.tex (~503 lines). Python venv: `source .venv/bin/activate`. TeX at /Library/TeX/texbin/{pdflatex,bibtex}.\n\nRULES: You are the SOLE writer on this worktree. Read each file from disk immediately before editing and match live text (a human also edits this file). Make small local edits. Do NOT reorganize sections, move theorem/remark/assumption environments, or change scope beyond the list below. Do NOT spawn subagents. After edits, rebuild and validate. Preserve the author's style (traditional academic mathematical-finance register; equations state themselves; no math expression or abstract noun as the subject of an action verb).\n\n=== FIX 1 (BLOCKER, sign/direction error) ===\nIn the impact-surfing section, near line ~353, the text reads: \"...and the rate reverses below the threshold\" followed by the display $\\theta^\\ast=\\kappa-2m=...$. This direction is WRONG. The proposition's own criterion is 'the rate reverses exactly when $2c_1\\Phi(\\theta)>1$', and with $\\Phi=\\sqrt A(m+\\theta)/(\\kappa+\\theta)$, $c_1=1/\\sqrt A$ this gives $2(m+\\theta)/(\\kappa+\\theta)>1\\iff\\theta>\\kappa-2m$, i.e. reversal is ABOVE the threshold. This matches the Figure 3 caption ('trades against it ($R<0$) above') and the appendix consistency check ($\\lambda\\to0$ gives $R=(\\kappa^2-\\theta^2)/2\\kappa\\gamma<0$ for $\\theta>\\kappa$). Change 'reverses below the threshold' to 'reverses above the threshold'. Verify the surrounding sentence stays consistent.\n\n=== FIX 2 (definitional gap, causality-gap benchmark) ===\nAt eq:vant (near line 278-281), the anticipative value is defined as $v_{\\rm ant}=\\frac1{4\\pi}\\int S_\\mu/\\hat n\\,d\\omega$ (position-referred). For the pure power-law kernel at $\\lambda=0$ -- exactly where the headline law $v/v_{\\rm ant}=\\sin(\\pi\\beta/2)$ (eq:sinlaw) is applied -- this integral DIVERGES (integrand $\\sim|\\omega|^{-(1+\\beta)}$ at the origin since $S_\\mu(0)\\ne0$). Appendix B computes the finite ratio using the RATE-referred form. Add ONE concise sentence right after eq:vant (or after 'the value attainable with the whole signal path in hand.') stating that eq:vant is the position-referred form, finite for $\\lambda>0$, and that for the scale-free kernel at $\\lambda=0$ the anticipative value is referred to the rate, $v_{\\rm ant}=\\frac1{4\\pi}\\int S_\\alpha/\\hat q\\,d\\omega$ (finite where the position form diverges), matching Appendix B and giving eq:sinlaw. Keep it brief, declarative, in the paper's register (do not let a math expression be the subject of an action verb). Verify: with OU $S_\\alpha=\\sigma^2/(\\theta^2+\\omega^2)$ and $\\hat q=\\gamma c_\\beta|\\omega|^{\\beta-1}$ the rate integral converges.\n\n=== FIX 3 (style: math/abstract-noun as subject of action verb) ===\nConvert these residual offenders to property statements / passive / process-noun subjects, matching live text. Suggested rewrites (adapt to live wording):\n(a) ~L83 \"$(Nx)(t)$ integrates the position over the past and the future\" -> \"$Nx$ at time $t$ depends on the position over the past and the future\".\n(b) ~L227 \"Only the friction's factor whitens the signal, the signal's own spectral factor entering through the projection alone.\" -> \"Only the friction's factor enters the whitening; the signal's own spectral factor enters through the projection alone.\"\n(c) ~L297 \"This memory shapes the optimum in three ways:\" -> \"The optimum reflects this memory in three ways:\".\n(d) ~L328 \"The integral amplifies low frequencies, ...\" -> \"Low frequencies are amplified, ...\".\n(e) ~L422 and ~L465 (appears twice, incl. concluding remarks) \"the memory of the impact sets the shape of the policy\" -> \"the shape of the policy is set by the impact memory\" (or 'follows the impact memory'). Fix BOTH occurrences.\nDo NOT touch other 'reads/gives/forces' idiom in proofs; only these five sites.\n\n=== FIX 4 (small caption accuracy) ===\nNotation-table caption (~line 152) says the rate variable is used 'for the scale-free kernel of Section~\\ref{sec:fractional}, where the position is non-stationary.' The finite-horizon Section~\\ref{sec:boundary} ALSO works in the rate. Broaden to something like '...for the scale-free kernel of \\S\\ref{sec:fractional} and on the finite horizon of \\S\\ref{sec:boundary}.' Match live text.\n\n=== FIX 5 (figure: baked-in title contradicts caption) ===\nEdit experiments/make_figures.py: line ~171 `ax[0].set_title(\"(a) value vs signal speed (fixed signal variance)\")` -> change 'fixed signal variance' to 'fixed appreciation variance'. Lines ~177-178: the title and ylabel use `v_{\\rm ad}/v_{\\rm ant}` -- the paper defines only `v` (not `v_ad`). Change both `v_{\\rm ad}` to `v/v_{\\rm ant}` in the title, and the ylabel `$v_{\\rm ad}/v_{\\rm ant}$` to `$v/v_{\\rm ant}$`. Then regenerate ONLY the value figure (run make_figures.py; if it regenerates all figures that is fine) and copy the updated figures/fig_value.png to v3/figures/fig_value.png. Confirm the new PNG's title text is correct (you may re-open/inspect if a tool is available; otherwise confirm the source edit + regeneration ran with exit 0).\n\n=== FIX 6 (reproducibility: v3-aligned aggregate verifier) ===\nThere is no v3 aggregate verification script (only v2/experiments/test_all_results.py, which targets optimal-trading-filters-v2.tex and labels the causality-gap sin-law as 'supplementary; not in paper' -- but in v3 it IS in the paper as eq:sinlaw). The paper abstract claims 'All closed forms are checked against discretized adapted optima' and acknowledgements say verification scripts are available. Create experiments/test_all_results.py (repo-root experiments/, where make_figures.py and rate_response_2ema.py already live) as a v3-aligned copy: start from v2/experiments/test_all_results.py, update the docstring/header to target v3/optimal-trading-filters-v3.tex, and relabel the causality-gap check from 'supplementary; not in paper' to reference eq:sinlaw as an in-paper result. The numerical checks are formula-based (they do not parse the tex), so they should run unchanged; adjust any comment referencing v2 equation labels to the v3 counterparts where obvious. Run it (`source .venv/bin/activate && python experiments/test_all_results.py`) and confirm all checks pass (report the count). Do NOT fabricate new numeric results; keep the existing checks.\n\n=== VALIDATION (required before you finish) ===\n1. Rebuild: `cd v3 && pdflatex -interaction=nonstopmode optimal-trading-filters-v3.tex` then `bibtex optimal-trading-filters-v3` then pdflatex x2 (run pdflatex a total of 3 times after bibtex if 'Label(s) may have changed' persists). Confirm 0 errors, 0 undefined references/citations, 0 overfull hboxes. Report the final 'Output written on ... (N pages)'.\n2. Run `python experiments/test_all_results.py` and `python experiments/rate_response_2ema.py`; report exit codes and the pass summary.\n3. Confirm fig_value.png regenerated and copied to v3/figures/.\n\nReport back: every changed file with a one-line description, the exact commands run with exit codes, build stats (pages / errors / undefined / overfull), verifier pass count, anything surprising, and anything left undone. If you hit a blocker on any single fix, complete the others and report the blocked one rather than aborting.

## Acceptance Contract
Acceptance level: reviewed
Completion is not accepted from prose alone. End with a structured acceptance report.

Criteria:
- criterion-1: Implement the requested change without widening scope
- criterion-2: Return evidence sufficient for an independent acceptance review

Required evidence: changed-files, tests-added, commands-run, validation-output, residual-risks, no-staged-files

Review gate: required by reviewer.

Finish with a fenced JSON block tagged `acceptance-report` in this shape:
Use empty arrays when no items apply; array fields contain strings unless object entries are shown.
`criteriaSatisfied[].status` must be exactly one of: satisfied, not-satisfied, not-applicable.
`commandsRun[].result` must be exactly one of: passed, failed, not-run.
`manualNotes` and `notes` are optional strings; an empty string means no note and does not satisfy `manual-notes` evidence.
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "specific proof"
    },
    {
      "id": "criterion-2",
      "status": "satisfied",
      "evidence": "specific proof"
    }
  ],
  "changedFiles": [
    "src/file.ts"
  ],
  "testsAddedOrUpdated": [
    "test/file.test.ts"
  ],
  "commandsRun": [
    {
      "command": "command",
      "result": "passed",
      "summary": "short result"
    }
  ],
  "validationOutput": [
    "validation output or concise summary"
  ],
  "residualRisks": [
    "none"
  ],
  "noStagedFiles": true,
  "diffSummary": "short description of the diff",
  "reviewFindings": [
    "blocker: file.ts:12 - issue found, or no blockers"
  ],
  "manualNotes": "anything else the parent should know"
}
```