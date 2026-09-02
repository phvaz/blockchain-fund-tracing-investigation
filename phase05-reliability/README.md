# Phase 05 — Reliability Assessment

## Objective

Classify every substantive claim produced in Phases 03 and 04 by its evidentiary weight, so that a reader can distinguish what the blockchain proves from what the analyst inferred, and — among inferences — how strongly each is supported.

**This phase completes before any third-party analysis is consulted.** The findings are frozen here. Phase 06 measures them against published work without revising them; revising findings after seeing the published answer would destroy the measurement that comparison exists to produce (`methodology/analytic-standards.md` §6).

## Classification scheme

Two layers, both pre-registered (`methodology/analytic-standards.md`).

**Layer 1 — claim type.**

| Type | Definition | Evidentiary basis |
|---|---|---|
| **Fact** | Recorded on-chain and independently verifiable by any party | The ledger — immutable |
| **Inference** | A conclusion drawn from facts by applying a stated heuristic | Reasoning, which may be wrong |
| **Attribution** | Linking an address to a named real-world actor | Requires evidence beyond on-chain data — not asserted by this analysis |

**Layer 2 — confidence** (applies to inferences only): **High** (follows directly from observed data, alternatives not credible), **Moderate** (well supported but dependent on a heuristic that can fail), **Low** (consistent with the data, but the basis is thin or a competing explanation is roughly as viable).

**The boundary that governs this phase.** The single most common error in this kind of work — and the one this classification exists to prevent — is treating a well-supported conclusion as if it were raw data. A reconciliation that closes to 0.3% *feels* like a fact; a label reading "Bybit Exploiter 45" *feels* like a fact. Neither is. The first is a strong inference; the second is a third-party attribution. Each is recorded below as what it is, not as what it feels like.

---

## Claim register

### Facts — established on-chain

Each of these is a direct read of the ledger, verifiable by any party against any node. No confidence level attaches; they are not inferences.

| # | Claim | Basis |
|---|---|---|
| F1 | The anchor address made outbound transfers of approximately 400,000 ETH plus staking derivatives on 2025-02-21 | `hop1.csv`; on-chain |
| F2 | 90,375.55 stETH, 8,000 mETH and 1 ETH were transferred from the anchor to `0xa4b2fd68…449e` | `hop1.csv`; transaction hashes recorded (Phase 03, Hop 1) |
| F3 | `0xa4b2fd68…449e` sent stETH and mETH to three contracts and 98,048.79 native ETH to `0xdd90071d…5f92` | `hop2.csv` |
| F4 | The three derivative-receiving contracts are `0x6bb00006…0000`, `0x04708077…1c14`, `0xfe837a35…dffc` | `hop2.csv`; contract addresses |
| F5 | `0xdd90071d…5f92` sent 90,000 ETH in nine transfers of exactly 10,000 ETH within 48 seconds on 2025-02-21 | `hop3.csv` |
| F6 | The earliest of those nine transfers (16:04:23) went to `0xf302572594…72be` | `hop3.csv`; timestamp |
| F7 | 31 addresses receiving impersonating tokens share the first six and last four characters of an address receiving legitimate assets | Phase 03 analysis of `hop1.csv` |
| F8 | Four addresses receive from both Hop 3 and Hop 4 | Phase 03 cross-reference of `hop3.csv`, `hop4.csv` |
| F9 | `0x327ffe25…ba23` sent 1,651.95 ETH while the traced branch delivered 454.06 ETH to it | `hop5.csv`; arithmetic |
| F10 | Fragmentation occurred at three levels (40, 9, 74 branches) | `hop1.csv`, `hop3.csv`, `hop4.csv` |

### Inferences — with confidence

| # | Claim | Confidence | Basis and reasoning |
|---|---|---|---|
| I1 | The three Hop 2 contracts are swap venues, and the derivatives were converted to native ETH there | **High** | Two independent lines converge: inflow and native-ETH outflow reconcile to 0.333%, and all three contracts are verified on Etherscan as DEX infrastructure. Neither alone would be conclusive; together they leave no credible alternative. |
| I2 | The fragmentation corresponds to the FATF indicator "multiple high-value transactions in short succession" | **High** | The indicator (§11, p. 6) was verified at source, and the observed windows (6 min, 48 s) fall squarely within it. Applying a framework to an observation is nonetheless an interpretive act, not a direct ledger read — hence inference, not fact. |
| I3 | The staggered-then-dormant pattern is a change of fragmentation *mechanism* between hops | **Moderate** | Round identical parcels at Hops 1 and 3 versus irregular amounts at Hop 4 is directly observed; that this reflects two different distribution rules is the reasonable reading, but a single rule with a residual-balance stage would produce the same. |
| I4 | The traced path underwent layering | **Moderate** | Consistent with multi-level fragmentation, conversion, and delay in sequence; but "layering" is a function ascribed to the behaviour, and the legitimate-custody alternative is not excluded. |
| I5 | The near-simultaneous 9–10 day dormancy of two addresses reflects coordinated handling | **Low** | Simultaneity is suggestive; liquidity, market timing, and operational schedules produce the same, and two data points do not establish a pattern. |
| I6 | Reconvergence of separated paths indicates common control of the addresses | **Low** | This is an inference about a property of the addresses (common control), **not** an attribution to any named actor. Rated Low because two independent paths using the same downstream service produce identical reconvergence, and that alternative cannot be excluded on-chain. |
| I7 | Conversion to native ETH served to consolidate into an unfreezable asset | **Low** | A hypothesis about motivation. Native ETH has no issuer-level freeze, but conversion to ETH is also a routine prerequisite for gas and most services. |
| I8 | Impersonation and address poisoning were deliberate contamination of the transaction record | **Moderate** | The impersonation and poisoning are facts (F7); that their effect is to impede analysis is demonstrable (Phase 03 documents the specific trap). "Deliberate" is the inference — spam and opportunistic phishing produce the same artifacts. |

### Attributions — not asserted by this analysis

These are recorded because they were encountered and because they informed navigation, **not** because this analysis endorses them. Each is a third-party claim.

| # | Claim | Source | Status |
|---|---|---|---|
| A1 | `0xf302572594…72be` is "Bybit Exploiter 45" and associated with the incident | Etherscan, citing ZachXBT | **Third-party attribution.** Not an on-chain fact and not a finding of this analysis. The protocol does not identify an address as belonging to any actor. |
| A2 | `0x21032176…044c` is "Bybit Exploiter 46", funding "Bybit Exploiter 47" | Etherscan | Third-party attribution; sequential labelling across the cluster. |
| A3 | The anchor is "Bybit Exploiter" | Etherscan | Third-party attribution; recorded in Phase 02 as the basis for anchor selection, validated on-chain by behaviour rather than accepted on the label. |

**On why these are not facts.** A label reading "Bybit Exploiter 45" is an assertion by Etherscan (itself relaying ZachXBT), not a record written by the protocol. Nothing on-chain establishes that an address belongs to a named actor. Treating such a label as a fact would be the on-chain equivalent of treating a user account as proof of a physical person's identity — a category error. Where this report refers to these labels, it does so in the form *"[source] associates this address with the incident,"* never *"this address belongs to [actor]."*

---

## The private attribution boundary

The point at which open-source analysis ceased to be sufficient. This is a stated objective of the investigation, not a shortfall (Phase 00, §1).

The trace reached its limit in two distinct forms:

**1. Traceability dissolution through consolidation (Hop 5).** `0x327ffe25…ba23` received 454 ETH by the traced path and forwarded 1,651 ETH assembled from several inbound paths. Because ETH is fungible, no on-chain evidence distinguishes which outbound transfer carries the traced funds. Continuing would mean following a destination with, at most, a 27% probability of containing the traced funds. **This is a limit of the evidence, not of the tooling** — the information required does not exist on-chain, and no commercial platform or additional effort resolves it.

**2. Cross-chain bridge exposure (adjacent to Hop 4).** Addresses one step to either side of the traced path deposit into THORChain. A cross-chain bridge severs the on-chain link between input and output: funds enter on Ethereum and leave on another chain with no on-chain record joining the two. **This is where a commercial platform with proprietary cross-chain heuristics would continue and this analysis cannot** — the boundary between open-source and proprietary capability, which the investigation set out to locate.

Both boundaries are findings. The investigation's stated question was how far an open-source analyst can trace and where the method stops working; these are the answers.

---

## What this analysis establishes, and what it does not

**Establishes:** the shape of a single fund path from the anchor across five hops — amounts, timing, destinations, asset conversions, and structural patterns — each recorded as fact, inference (with confidence), or third-party attribution, and each verifiable against the CSV data and transaction hashes provided.

**Does not establish:** the identity of any actor; the intent behind any movement; that the addresses on the path are under common control; or anything about the ~99.9% of the funds leaving the anchor that this trace did not follow. No conclusion here rests on attribution, and no attribution is made.
