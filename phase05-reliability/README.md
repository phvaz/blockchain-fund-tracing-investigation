# Phase 05 — Reliability Assessment

**Status:** `[ ] Not started  [ ] In progress  [ ] Complete`

## Objective

Classify every claim produced in Phases 03–04, and document explicitly where the method reaches its limits.

**This phase completes before any third-party analysis is consulted.** Findings are frozen here; Phase 06 measures them against published work without revising them.

---

## Claim classification

| # | Claim | Type | Confidence | Basis |
|---|---|---|---|---|
| 1 | `[claim]` | Fact | — | Ledger record, tx `[hash]` |
| 2 | `[claim]` | Inference | `[H/M/L]` | `[heuristic applied]` |
| 3 | `[claim]` | Attribution | — | **Not asserted** — third-party claim only |

---

## The private attribution boundary

The point at which open-source analysis ceased to be sufficient.

| Field | Value |
|---|---|
| Reached at | `[hop N / address]` |
| Nature of the boundary | `[unlabelled address / mixer output / bridge destination]` |
| What would be required to proceed | `[proprietary labelled dataset / exchange records / legal process]` |

**This is a finding, not a failure.** Establishing where open tooling stops working is one of the stated objectives of this investigation.

---

## Structural limitations

Each limitation with its concrete impact on specific conclusions.

- **`[Limitation]`** — *Impact:* `[which conclusion it affects, how, and what mitigates it]`

---

→ [Phase 06 — Cross-Validation](../phase06-validation/README.md)
