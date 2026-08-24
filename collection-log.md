# Collection Log — Provenance Record

Every external source consulted during this investigation is recorded here: what was queried, when, from where, and what it returned.

On-chain data is immutable, which makes raw transaction records reproducible indefinitely. **Entity labels are not.** Explorer annotations, exchange tags, and platform-assigned identities change over time and differ between providers. A finding that relies on a label is only reproducible if the label's source and date are recorded.

This log also enforces the sequence integrity rule (see `methodology/analytic-standards.md`, Section 6): it documents exactly what was read before the independent analysis, so that the boundary between sourced fact and independent finding is auditable.

---

## Sessions

| # | Date (UTC) | Source | Query | Returned | Phase |
|---|---|---|---|---|---|
| 1 | 2026-08-24 | Etherscan (web) | Search for addresses labelled in connection with the incident | `0x0fa09C3A328792253f8dee7116848723b72a6d2e`, labelled "Bybit Exploiter" | 02 |
| 2 | 2026-08-24 | Etherscan API V2 | `txlist` for address from session 1 | 48 outbound transactions, 18–21 Feb 2025, 0.16 ETH total, predominantly zero-value | 02 |
| 3 | 2026-08-24 | Etherscan API V2 | `txlist` + `tokentx` for address from session 1 | 54 transfers: 48 native, 6 token (stETH, mETH, cmETH), all amounts below 0.02 | 02 |
| 4 | 2026-08-24 | Google AI summary | Query for the principal address associated with the incident | An address, with Etherscan cited as the source. **Treated as a pointer, not as evidence** — see session 5 | 02 |
| 5 | 2026-08-24 | Etherscan (web) | Direct lookup of the address named in session 4 | `0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2`, labelled "Bybit Exploiter". Screenshot captured | 02 |
| 6 | 2026-08-24 | Etherscan API V2 | `txlist` + `tokentx` for address from session 5 | 255 transfers: 46 native, 209 token. ~400,001 ETH native outbound; stETH, mETH, cmETH; and 9 token groups with impersonating symbols | 02 |

---

## Source grading

Sources graded under the Admiralty Code (NATO STANAG 2511): letter = source reliability (A–F), numeral = information credibility (1–6).

| Source | Rating | Justification |
|---|---|---|
| On-chain transaction data (via Etherscan API) | **Not graded** | Not a source in the intelligence sense. This is the primary record — immutable, independently verifiable by any party against any node. |
| Etherscan — transaction data | **B1** | A widely-used explorer presenting protocol data faithfully. Rated B rather than A because it is an intermediary; the underlying chain is authoritative and could be queried directly against a node. |
| Etherscan — entity labels | **B2** | The labels are Etherscan's own editorial attributions, not protocol facts. Credibility rated 2 because they are broadly corroborated by other platforms but are not independently verifiable from the chain itself. |
| Google AI summary | **F6** | An AI-generated summary is not a citable source, cannot be audited, and its reliability cannot be assessed. Used solely as a pointer to a source it named, and never relied upon: the address was confirmed at Etherscan and validated against on-chain behaviour before being accepted. |

---

## Note on the anchor provenance chain

The anchor address was reached in three steps of decreasing dependence on any external claim:

1. An AI summary named an address and cited Etherscan (F6 — pointer only)
2. The address was confirmed directly at Etherscan (B2)
3. The address was validated against its own on-chain behaviour — date, scale, and asset composition consistent with the reported incident

**The anchor rests on step 3.** Steps 1 and 2 determined where to look; step 3 determined whether it held. Had the pointer been wrong, validation would have rejected it regardless of what any source claimed.

The AI summary is recorded rather than omitted. A weak source that is disclosed and neutralised is manageable; a weak source that is concealed behind a stronger-sounding one is not.

---

## Note on transcription error

The address in session 4 was initially mis-transcribed on copy, producing a 41-character string. `tools/trace_helper.py` rejected it on format validation before any query was issued.

A 42-character hexadecimal address carries no human-readable redundancy; a single dropped character produces a string that looks entirely plausible. Address handling in this investigation is by copy-and-validate, never by transcription.

---

## Sequence integrity declaration

| Event | Date | Note |
|---|---|---|
| Anchor address sourced | 2026-08-24 | Sessions 4–5 |
| **Independent analysis begins** | `[date]` | No third-party analysis of fund flow consulted from this point |
| **Independent analysis ends — findings frozen** | `[date]` | Phases 03–05 complete |
| Third-party analyses first consulted | `[date]` | Phase 06 cross-validation |

**What was read before this point:** the incident date, the affected exchange, and addresses labelled in connection with it. **What was not read:** any account of where the funds moved after leaving the anchor.

---

## Reproducibility notes

- **Transaction data is permanent.** Any hash recorded here can be re-verified by any party at any time against any node or explorer for the relevant chain.
- **Labels are perishable.** Where a finding depends on an entity label, both the platform and the date of observation are recorded, because labels are revised. Screenshots were captured for labels that informed a decision.
- **Token symbols are not identifiers.** Symbols are chosen by whoever deploys the contract and several encountered at the anchor impersonate legitimate assets. Every token referenced in this investigation is identified by contract address; the symbol is recorded as displayed but carries no evidentiary weight.
- **No active interaction.** No wallet was connected, no contract called, no transaction broadcast. All queries were read-only against public explorer services.
