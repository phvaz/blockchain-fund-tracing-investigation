# Scope, Boundaries and Stopping Rule

> **Status:** Pre-registered. This document was written and fixed **before** any transaction data was examined.
> Any subsequent modification is recorded in the revision log at the bottom of this file, with its justification.

---

## 1. Objective

To independently reconstruct a single, delimited trail of funds associated with the publicly reported Bybit incident of February 2025, using exclusively open-source tooling, and to establish:

1. How far an independent analyst can trace such a trail without access to proprietary attribution data;
2. Which laundering typologies are observable in that trail;
3. Where the boundary between observable fact, analytical inference, and actor attribution falls in practice.

The measurable outcome of this investigation is not the destination of the funds — that is already documented by parties with far greater resources. It is **the distance an open-source analyst can cover, and the precise point at which the method stops working.**

---

## 2. In scope

- One fund trail, beginning at a publicly disclosed anchor address and proceeding forward under the stopping rule defined in Section 4.
- Transaction-level documentation of each hop: hash, timestamp, source, destination, value.
- Identification and classification of movement patterns against catalogued laundering typologies.
- Reliability classification of every claim (fact / inference / attribution) and confidence level for inferences.
- Comparison against published third-party analyses — **conducted only after all findings are finalized** (Phase 06).

## 3. Out of scope

- **Reconstruction of the full incident.** The total sum involved was fragmented across a large number of addresses over an extended period. Tracing it in full is the work of teams with proprietary datasets and dedicated automation. This project makes no attempt at completeness and does not claim it.
- **Actor attribution.** No address is claimed to belong to any named individual, organization, or state. Where public sources make such attributions, they are cited as third-party claims (Section 5).
- **Identification of natural persons.** No attempt is made to link any address to a real-world identity.
- **Discovery or publication of undocumented infrastructure.** If analysis surfaces an address, pattern, or relationship not already present in public reporting, it is withheld from publication and reviewed privately before any disclosure decision.
- **On-chain interaction of any kind.** No wallet is connected, no contract is called, no transaction is broadcast. This investigation is read-only.

---

## 4. Stopping rule (pre-registered)

The following rule was fixed before analysis began. Its purpose is to make the endpoint of this investigation a **methodological decision** rather than a point of exhaustion.

> **Branch selection.** Where funds fragment across multiple destination addresses, the branch carrying the **highest value** is followed. All other branches are recorded in the trace log as observed-but-not-followed, with their addresses and values, so that the unexplored surface is visible rather than silently discarded.
>
> **Termination.** Tracing stops at whichever of the following occurs first:
> 1. The traced funds enter a **mixing service or cross-chain bridge**, at which point continued attribution becomes technically unsupportable with open-source tooling; or
> 2. **Five hops** have been traced from the anchor address.

### Rationale

**Why a mixer or bridge terminates the trail.** These services are designed specifically to sever the link between input and output. Once funds enter one, any claim about where they emerged is inference of a substantially weaker kind — and with open tooling, frequently no more than speculation. Stopping here means the boundary is set by **the evidence**, not by the analyst's patience. Reaching this point is a finding, not a failure.

**Why five hops as a secondary limit.** The mixer/bridge condition is the primary and more meaningful stopping criterion. The hop limit exists solely as a bound in the event that the trail proceeds through simple pass-through transfers without ever reaching such a service. It prevents unbounded tracing.

**Why highest-value branch selection.** Where a choice must be made, the largest remaining concentration of funds is the most analytically significant path and the one most likely to be documented in published analyses — which makes Phase 06 comparison meaningful. The criterion is stated in advance so that branch selection cannot be rationalized after the fact.

---

## 5. Attribution policy

This investigation asserts **no attribution**.

Where published sources attribute this incident or associated addresses to a specific actor, such statements are reported in the following form:

> *"[Source] attributes this activity to [actor]."*

and never in the form *"this address belongs to [actor]."*

The distinction is not stylistic. Establishing that an address is controlled by a named entity requires evidence of a kind that on-chain analysis alone cannot produce — off-chain intelligence, exchange KYC records, law-enforcement process. This analysis has access to none of these and therefore makes no such claim.

---

## 6. Known limitations (anticipated)

Two limitations are structural and are stated here in advance, before they are encountered, so that reaching them is not mistaken for analytical failure.

**The private attribution boundary.** Commercial blockchain intelligence platforms maintain proprietary databases of labelled addresses built from data not publicly available. An address that appears unlabelled and anonymous in this analysis may already be identified in those datasets. The point at which this analysis encounters that boundary is itself a documented finding.

**Scale in the absence of automation.** Fragmentation across many addresses is a deliberate technique whose purpose is to make manual tracing impractical. Any automation employed is documented in `tools/`, and the stopping rule above ensures that the endpoint of this investigation is a stated methodological boundary rather than a limit of endurance.

---

## Revision log

| Date | Change | Justification |
|---|---|---|
| `[date]` | Initial version — pre-registered before analysis | — |
