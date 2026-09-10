# Phase 00 — Scope, OpSec and Methodology

Everything in this phase was decided and written **before** any transaction data was examined. A rule declared after the fact is a rationalization, not a method.

## Deliverables

| Document | Purpose |
|---|---|
| [`methodology/scope-and-limitations.md`](../methodology/scope-and-limitations.md) | Objective, scope boundaries, pre-registered stopping rule, attribution policy |
| [`methodology/opsec.md`](../methodology/opsec.md) | Threat model, controls adopted, controls deliberately rejected |
| [`methodology/analytic-standards.md`](../methodology/analytic-standards.md) | Fact/inference/attribution taxonomy, confidence levels, finding structure |

## Key decisions fixed in this phase

**Stopping rule.** Highest-value branch at each fragmentation; terminate at mixer/bridge entry or 5 hops from anchor, whichever comes first.

**Attribution policy.** No attribution asserted. Third-party attributions cited as claims, never as findings.

**Sequence integrity.** No published analysis of fund flow consulted until Phase 06.

---

→ [Phase 01 — Environment Preparation](../phase01-environment/README.md)
