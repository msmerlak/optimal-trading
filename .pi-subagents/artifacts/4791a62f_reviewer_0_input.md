# Task for reviewer

Review an applied-mathematics / quantitative-finance paper for MATHEMATICAL CORRECTNESS and validity of claims.

Artifact: /Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/v3/optimal-trading-filters-v3.tex (~503 lines, ~21pp, compiles clean, 5 figures). It solves an optimal-trading problem (linear gain of a position against a return signal, net of temporary impact, transient/propagator impact, and mean-variance inventory risk) by a Wiener-Hopf factorization of the friction operator N (position-referred) / Q (rate-referred). Read the paper directly from the file. Companion artifacts: v3/optimal-trading-filters.bib; experiments/make_figures.py; experiments/test_all_results.py; experiments/rate_response_2ema.py. You MAY run the python scripts (`source .venv/bin/activate`) and compile (`cd v3 && pdflatex -interaction=nonstopmode optimal-trading-filters-v3.tex`).

Do NOT rely on any prior conversation. Do NOT edit files. Do NOT spawn subagents.

Angle -- verify the mathematics, especially recently added/changed results:
- Theorem (optimal trading filter) + Ornstein-Uhlenbeck formulas; value v = sigma^2 theta / 4 Phi(theta)^2.
- 'Value of information': value scalings vs signal speed theta at FIXED appreciation variance -- theta^2 (pure risk, exponential), theta^{1-beta} (power law), SATURATION at Var(alpha)/2 eta for temporary cost. Check Phi(theta) asymptotics: sqrt(lambda); sqrt(2 kappa gamma+lambda); ~ sqrt(eta) theta; ~ theta^{(1+beta)/2}.
- Causality gap DEFINED as the ratio v/v_ant, law v/v_ant = sin(pi beta/2) under power law.
- 'Pure power-law impact': the POSITION as a fractional integral of the RETURN, x* ~ I^{(1+beta)/2}_+ mu, from x_hat = mu_hat/(Phi n_hat_+); stationarity condition -- stationary iff int |omega|^{-(1+beta)} S_mu domega < inf, i.e. S_mu vanishes at 0 faster than |omega|^beta. Check exponent (1+beta)/2 and the low-frequency argument.
- 'Impact surfing': R(theta) = (theta^2/Phi)(1/Phi - 2 c_1); atom c_1; threshold theta* = kappa - 2m; any temporary cost gives c_1=0, R = theta^2/Phi^2 > 0. Cross-check experiments/rate_response_2ema.py.
- Cross-check appendix proofs A-D against the body and test_all_results.py.

Flag incorrect scalings, sign errors, missing/incorrect hypotheses, normalization slips, or claims unsupported by a derivation or the code. Group findings as BLOCKERS, FIXES-WORTH-DOING-NOW, OPTIONAL, IGNORE/DEFER, each tied to a specific section/equation/line, with reason and evidence.

---
**Output:**
Write your findings to exactly this path: /Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/.pi-subagents/artifacts/outputs/4791a62f/outputs/.reviews/v3-round1-correctness.md
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