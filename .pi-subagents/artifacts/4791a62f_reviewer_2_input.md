# Task for reviewer

Review an applied-mathematics / quantitative-finance paper for INTERNAL CONSISTENCY and REPRODUCIBILITY.

Artifact: /Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/v3/optimal-trading-filters-v3.tex (~503 lines, 5 figures). Read directly. Companion: v3/optimal-trading-filters.bib; v3/figures/*.png; experiments/make_figures.py; experiments/test_all_results.py; experiments/rate_response_2ema.py. You MAY compile (`cd v3 && pdflatex -interaction=nonstopmode optimal-trading-filters-v3.tex; bibtex optimal-trading-filters-v3; pdflatex ... ; pdflatex ...`) and run python scripts (`source .venv/bin/activate`).

Do NOT rely on any prior conversation. Do NOT edit files. Do NOT spawn subagents.

Angle -- consistency and reproducibility:
- Notation consistency: mu (return) vs alpha (appreciation, alpha_t = E_t int_t^inf mu_s ds); N vs Q=N(-d^2)^{-1}; Phi(theta)=n_hat_+(i theta); nu=(1-beta)/2; c_beta; position-primary development with rate/alpha used only in the pure power-law (lambda=0) section. Flag inconsistent or undefined-before-use symbols.
- Every \ref/\eqref/\citet resolves: compile; report undefined references, undefined citations, overfull hboxes.
- Figure<->caption agreement (5 figures). In particular: (i) value figure caption vs the plot's baked-in panel title ('fixed signal variance' vs 'fixed appreciation variance'); (ii) value figure shows four curves incl. the saturating exp+temp one; (iii) trading-filter figure x-axis stops at omega=10 and marks only omega_c (caption should not promise omega_*); (iv) parameter labels match text.
- 'causality gap = ratio v/v_ant' wording CONSISTENT across abstract, value-of-information section, power-law section, conclusion (no leftover 'gap = difference / retained fraction / complementary fraction').
- Bibliography: run bibtex; report undefined keys; spot-check cited works are used sensibly.
- Reproducibility: do test_all_results.py and rate_response_2ema.py run and print pass/consistent results matching the paper's numbers.

Return findings grouped as BLOCKERS, FIXES-WORTH-DOING-NOW, OPTIONAL, IGNORE/DEFER, each tied to a specific file/section/figure/command with evidence (exit codes, quoted lines).

---
**Output:**
Write your findings to exactly this path: /Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/.pi-subagents/artifacts/outputs/4791a62f/outputs/.reviews/v3-round1-consistency.md
This path is authoritative for this run.
Ignore any other output filename or output path mentioned elsewhere, including output destinations in the base agent prompt, system prompt, or task instructions.

## Acceptance Contract
Acceptance level: attested
Completion is not accepted from prose alone. End with a structured acceptance report.

Criteria:
- criterion-1: Return concrete findings with file paths and severity when applicable

Required evidence: review-findings, residual-risks

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