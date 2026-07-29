# Task for reviewer

Review an applied-mathematics / quantitative-finance paper for EXPOSITION, STYLE, and STRUCTURE.

Artifact: /Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/v3/optimal-trading-filters-v3.tex (~503 lines). Read it directly. Also read /Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/AGENTS.md (writing-style rules).

Do NOT rely on any prior conversation. Do NOT edit files. Do NOT spawn subagents.

Angle -- traditional academic mathematical-finance register:
- NO restating equations in words (prose narrating what a display already says, e.g. 'the operator collects the costs', 'the factor whitens', 'a rational filter with X in the denominator and Y in the numerator'). Flag remaining instances.
- NO mathematical expression (or abstract noun like 'two shapes') as SUBJECT of an action verb ('$N_+$ turns...', '$P_+$ acts...', 'two shapes bracket...'). Property statements ('$\hat n$ vanishes at 0') are fine. Flag offenders.
- Transitions/articulation between paragraphs and sections; clarity of the through-line.
- Abstract: explicit contribution ('we...') set against prior work; accurate.
- Structure: the Section 2 factor->predict->combine spine; whether 'The trading filter' subsection (Lemma + two Theorems + three Remarks + an Assumption) is too dense; placement of the three 'Relation to...' remarks.
- AGENTS.md cadence: no throat-clearing, negation-foils, empty intensifiers, rhetorical questions, over-signposting; em-dash density.
- Figure captions clear and self-contained.

Return concrete findings grouped as BLOCKERS, FIXES-WORTH-DOING-NOW, OPTIONAL, IGNORE/DEFER, each tied to a specific section/line/quoted phrase, with a suggested rephrasing where useful.

---
**Output:**
Write your findings to exactly this path: /Users/orwell/Library/CloudStorage/Dropbox/Research/projects/optimal-trading/.pi-subagents/artifacts/outputs/4791a62f/outputs/.reviews/v3-round1-style.md
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