# Phase 02 — Anchor Point Identification

## Objective

Obtain the starting address for the trace, with documented provenance, **without contaminating the independent analysis**.

---

## The contamination problem

This phase requires reading public sources. That is unavoidable — the anchor must come from somewhere. The discipline is in stopping at the right point.

**Permitted:** identifying which address was publicly disclosed as involved in the incident.

**Not permitted:** reading any analysis of where the funds subsequently went. That is the question this investigation exists to answer independently.

External reading stopped once the anchor was identified. `collection-log.md` records what was read and when.

---

## Anchor

| Field | Value |
|---|---|
| Address | `0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2` |
| Chain | Ethereum mainnet (chainid 1) |
| Etherscan label | "Bybit Exploiter" *(third-party attribution — see below)* |
| Date sourced | 2026-08-24 |
| Basis for selection | Outbound activity concentrated on 2025-02-21, in assets and at a scale consistent with the publicly reported incident (see validation below) |

---

## Provenance chain

The anchor was reached through three distinct steps, recorded separately because they carry different evidentiary weight.

**1. Discovery — AI-generated search summary.** A search engine's AI summary surfaced the address in response to a query about the incident. The summary cited Etherscan as its source.

This is graded **F6** under the Admiralty Code: an AI-generated summary is not a citable source, cannot be audited, and its reliability cannot be assessed. It was treated as a **navigation shortcut to a source it named**, not as evidence.

**2. Verification at the named source — Etherscan.** The address was confirmed directly on Etherscan rather than accepted from the summary. Graded **B2**: Etherscan is a widely-used explorer presenting on-chain data faithfully, but its *labels* are its own editorial attributions rather than protocol facts.

**3. Behavioural validation — on-chain data.** The address was queried directly and its transaction history examined for consistency with the reported incident. This is the step the anchor actually rests on.

**The anchor does not rest on the AI summary.** It rests on the Etherscan record and on the observed on-chain behaviour. Had the pointer been wrong, validation would have rejected it.

### Note on the label

Etherscan displays this address as "Bybit Exploiter". This is a **third-party attribution**, not an on-chain fact. Nothing in the protocol identifies an address as belonging to any actor. The label is recorded because it informed selection, and is treated under this investigation's analytic standards as an attribution claim by Etherscan — not as a finding of this analysis.

Explorer labels are also perishable. The label observed on 2026-08-24 may be revised; a screenshot was captured for that reason.

### Note on transcription

The address was initially mis-transcribed when copied, producing a 41-character string. The retrieval tool rejected it (`Address does not look valid`) before any query was issued.

This is recorded because it is instructive: a 42-character hexadecimal string carries no human-readable redundancy, and a single dropped character produces something that looks entirely plausible. Address handling in this investigation is therefore by copy-and-validate, never by transcription. Format validation in tooling is a cheap control against a failure mode that would otherwise be silent.

---

## Validation

Retrieval was performed with `tools/trace_helper.py` on 2026-08-24, covering both native and ERC-20 transfers.

### Signal — assets consistent with the incident

| Asset | Contract | Outbound total |
|---|---|---|
| ETH (native) | — | 400,001 |
| stETH | `0xae7ab96520de3a18e5e111b5eaab095312d7fe84` | 90,375.55 |
| mETH | `0xd5f7838f5c461feff7fe49ea5ebaf7728bb0adfa` | 8,000 |
| cmETH | `0xe6829d9a7ee3040e1276fa75293bde931859e8fa` | 15,000 |

**Observed:** outbound movement of approximately 400,000 ETH, concentrated on 2025-02-21, alongside liquid-staking tokens.

**Interpretation:** the date, scale, and asset composition are consistent with the publicly reported incident. — *Confidence: High.*

**Boundary:** consistency with a reported incident is not proof of involvement in it. This validation establishes that the address is a plausible anchor for the trail under investigation. It does not establish who controlled it, and no such claim is made.

### Movement pattern at the anchor

**Observed:** 40 outbound transfers of exactly 10,000 ETH each, to 40 distinct destination addresses, between 15:48 and 15:54 UTC on 2025-02-21 — a six-minute window.

**Interpretation:** uniform division of a large sum across many destinations in a short window. — *Confidence: High* as to the pattern; the pattern's purpose is addressed in Phase 04.

**Consequence for Phase 03:** the pre-registered stopping rule selects the highest-value branch at each fragmentation. Forty branches carrying identical amounts admit no highest value. A tie-breaking criterion is required and will be declared, with its basis, before tracing begins.

---

## Finding: token symbol impersonation at the anchor

Retrieval returned twenty distinct token groups. Most are not what they appear to be.

**Observed:** nine token groups use symbols containing non-ASCII characters that render identically to Latin letters — Cyrillic `Е` (U+0415) for `E`, `Т` (U+0422) for `T`, `ѕ` (U+0455) for `s`. Four symbols appear under more than one contract address. One token carries the symbol `BybitExploiter` (contract `0x98bdd7aa…6c5f`), with 17,330,506 units transferred **to the queried address itself**.

**Interpretation:** these are tokens deployed by third parties whose symbols impersonate legitimate assets, sent to a notable address so as to appear in its transaction history. — *Confidence: High.* Token symbols are chosen freely by whoever deploys the contract; substituting Cyrillic characters has no legitimate purpose, and transferring a token named after an incident to the address associated with that incident has no economic rationale.

**Boundary:** the identity and purpose of whoever deployed these contracts is not established. Spam, advertising, and deliberate obstruction of analysis all produce this signature and the evidence does not distinguish between them.

**Why this mattered.** Before impersonation detection was added to the tooling, the same retrieval reported an apparent 570,000 "ETH" and 554,882 "stETH" in outbound transfers. Those figures are meaningless — they are raw units of tokens with forged names. An analyst reporting them at face value would have introduced a factual error of an order of magnitude into the record, and the error would have been invisible in a rendered table.

**Control applied.** The tooling now groups by `(symbol, contract)` rather than by symbol, prints the contract address for every group, flags non-ASCII symbols with their Unicode code points, and flags symbols appearing under multiple contracts. See `tools/README.md`.

**Residual limitation.** Four distinct contracts in this retrieval carry the symbol `stETH` in clean ASCII. Only `0xae7ab965…fe84` is the Lido contract. The remaining three would not be caught by non-ASCII detection. **Confirming that a contract is the asset it claims to be remains an analyst task**, performed against independent sources — the tool narrows the problem, it does not solve it.

---

## Sequence integrity declaration

> Independent analysis begins on the date recorded in `collection-log.md`. From that point until the completion of Phase 05, no third-party analysis of fund movement will be consulted.

---

→ [Phase 03 — Independent Trace](../phase03-trace/README.md)
