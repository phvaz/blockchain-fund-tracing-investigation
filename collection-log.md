# Collection Log — Provenance Record

Every external source consulted during this investigation is recorded here: what was queried, when, from where, and what it returned.

On-chain data is immutable, which makes raw transaction records reproducible indefinitely. **Entity labels are not.** Explorer annotations, exchange tags, and platform-assigned identities change over time and differ between providers. A finding that relies on a label is only reproducible if the label's source and date are recorded.

This log also enforces the sequence integrity rule (see `methodology/analytic-standards.md`, Section 6): it documents exactly what was read before the independent analysis, so that the boundary between sourced fact and independent finding is auditable.

---

## Sessions

| # | Date (UTC) | Source | Query | Returned | Phase |
|---|---|---|---|---|---|
| 1 | `[YYYY-MM-DD]` | `[source]` | `[what was searched]` | `[what was obtained]` | 02 |

---

## Sequence integrity declaration

| Event | Date | Note |
|---|---|---|
| Anchor address sourced | `[date]` | Session 1 above |
| **Independent analysis begins** | `[date]` | No third-party analysis of fund flow consulted from this point |
| **Independent analysis ends — findings frozen** | `[date]` | Phases 03–05 complete |
| Third-party analyses first consulted | `[date]` | Phase 06 cross-validation |

---

## Source grading

Sources graded under the Admiralty Code (NATO STANAG 2511): letter = source reliability (A–F), numeral = information credibility (1–6).

| Source | Rating | Justification |
|---|---|---|
| `[source]` | `[X#]` | `[why]` |

---

## Reproducibility notes

- **Transaction data is permanent.** Any hash recorded here can be re-verified by any party at any time against any node or explorer for the relevant chain.
- **Labels are perishable.** Where a finding depends on an entity label, both the platform and the date of observation are recorded, because labels are revised.
- **No active interaction.** No wallet was connected, no contract called, no transaction broadcast. All queries were read-only against public explorer services.
