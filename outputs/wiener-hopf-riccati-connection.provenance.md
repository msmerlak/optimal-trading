# Provenance: Wiener–Hopf and Riccati: Two Faces of the Same Object

- **Date:** 2026-05-31
- **Slug:** `wiener-hopf-riccati-connection`
- **Mode:** Direct search, lead-owned (no researcher subagents).
- **Rounds:** 1 search round (8 `web_search` queries) + 1 `fetch_content` call to verify the authorship of arXiv:1611.00997.
- **Sources consulted:** 17 distinct external sources surfaced via `web_search`; 1 verified by `fetch_content` (arXiv:1611.00997).
- **Sources accepted:** 17 cited in final note (see Sources section in `outputs/wiener-hopf-riccati-connection.md`).
- **Sources rejected / corrected:** arXiv:1611.00997 — initial attribution was paraphrased as "(Cartea, Jaimungal et al.)" based on search snippet phrasing; `fetch_content` confirmed the submitting author is Marc Abeille and the abstract concerns LQG framing of dynamic portfolio allocation with predictability, impact, and partial observability. Citation key and entry rewritten as [Abe16] with corrected attribution.
- **PDF parsing:** Not performed (per workflow). Two PDF URLs are cited from `web_search` metadata where no HTML version surfaced (MIT 6.245 KYP notes, Sayed–Kailath 2001 NLAA survey, Varga 2000 IEEE TAC, Devroye/Gavin Duke notes); these are referenced as metadata citations only.
- **Verification:** PASS WITH NOTES
  - PASS: All claims map to sources or to on-disk artifacts (`papers/noisy-signal-impact-trading.md`, `outputs/trading-duality-extensions.md`, `experiments/results/closed_form_vs_operator.out`).
  - NOTES (from `outputs/.drafts/wiener-hopf-riccati-connection-verification.md`):
    1. The §5 worked-example reduction of paper eq. (12) to a 2×2 DARE is stated structurally and cited to [BV22], not derived in this note. Listed as open question §9.1.
    2. [Abe16] citation was corrected after `fetch_content` verification; final reference uses the verified submitting author rather than the originally paraphrased attribution.
  - Post-edit on-disk verification: `grep -n "CJ16\|Abe16"` shows zero occurrences of the old key and two occurrences of the new key (1 in-text + 1 reference entry); no stray legacy attribution remains.
- **Plan:** `outputs/.plans/wiener-hopf-riccati-connection.md`
- **Research files:**
  - `outputs/.drafts/wiener-hopf-riccati-connection-research-direct.md` (search log, anchor list, conceptual claim mapping)
  - `outputs/.drafts/wiener-hopf-riccati-connection-draft.md` (uncited draft)
  - `outputs/.drafts/wiener-hopf-riccati-connection-cited.md` (cited draft = final)
  - `outputs/.drafts/wiener-hopf-riccati-connection-verification.md` (self-review)
- **Companion artifacts (this workspace, not modified by this run):**
  - `papers/noisy-signal-impact-trading.md`
  - `outputs/trading-duality-extensions.md`
  - `experiments/closed_form_vs_operator.py` and `experiments/results/closed_form_vs_operator.out` (the $2.6\times 10^{-15}$ Case A residual referenced in §5).
- **Final artifact:** `outputs/wiener-hopf-riccati-connection.md`
