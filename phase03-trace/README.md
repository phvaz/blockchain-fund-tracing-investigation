# Phase 03 — Independent Trace

**Status:** `[ ] Not started  [ ] In progress  [ ] Complete`

## Objective

Reconstruct the fund trail hop by hop from the anchor address, within the pre-registered stopping rule, documenting every transaction and every branch not followed.

## Stopping rule in force

> Highest-value branch at each fragmentation. Terminate at mixer/bridge entry, or 5 hops from anchor — whichever comes first.

Branches not followed are recorded, not discarded. An unexplored branch that is documented is a scope decision; an unexplored branch that is omitted is a gap.

---

## Trace log

### Hop 1

| Field | Value |
|---|---|
| Transaction hash | `[TO FILL]` |
| Timestamp (UTC) | `[TO FILL]` |
| From | `[TO FILL]` |
| To | `[TO FILL]` |
| Value | `[TO FILL]` |
| Value at date (USD approx.) | `[TO FILL]` |
| Classification | **FACT** |

**Observed:** `[what the ledger records]`

**Interpretation:** `[what it suggests, by what reasoning]` — *Confidence: `[High/Moderate/Low]`*

**Boundary:** `[what this does not establish]`

**Branches not followed:**

| Address | Value | Reason not followed |
|---|---|---|
| `[addr]` | `[value]` | Lower value than selected branch |

---

### Hop 2

`[repeat structure]`

---

## Termination

| Field | Value |
|---|---|
| Terminated at | `[hop N]` |
| Trigger | `[mixer entry / bridge / hop limit]` |
| Evidence for trigger | `[what identifies the destination as a mixer or bridge — and note that this identification is itself an inference unless the service is publicly and unambiguously known]` |

## Automation

Scripts used are documented in [`tools/`](../tools/). Any automation is recorded so that a reader can distinguish an analytical boundary from a limit of endurance.

---

→ [Phase 04 — Typology Identification](../phase04-typologies/README.md)
