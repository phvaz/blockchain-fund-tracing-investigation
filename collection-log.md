# Collection Log — Provenance Record

Every external source consulted during this investigation is recorded here: what was queried, when, from where, and what it returned.

On-chain data is immutable, which makes raw transaction records reproducible indefinitely. **Entity labels are not.** Explorer annotations, exchange tags, and platform-assigned identities change over time and differ between providers. A finding that relies on a label is only reproducible if the label's source and date are recorded.

This log also enforces the sequence integrity rule (see `methodology/analytic-standards.md`, Section 6): it documents exactly what was read before the independent analysis, so that the boundary between sourced fact and independent finding is auditable.

---

## Phase 02 — Anchor identification

| # | Date (UTC) | Source | Query | Returned |
|---|---|---|---|---|
| 1 | 2026-08-24 | Etherscan (web) | Search for addresses labelled in connection with the incident | `0x0fa09C3A328792253f8dee7116848723b72a6d2e`, labelled "Bybit Exploiter" |
| 2 | 2026-08-24 | Etherscan API V2 | `txlist` for address from session 1 | 48 outbound transactions, 18–21 Feb 2025, 0.16 ETH total, predominantly zero-value |
| 3 | 2026-08-24 | Etherscan API V2 | `txlist` + `tokentx` for address from session 1 | 54 transfers: 48 native, 6 token (stETH, mETH, cmETH), all amounts below 0.02 |
| 4 | 2026-08-24 | Google AI summary | Query for the principal address associated with the incident | An address, with Etherscan cited as the source. **Treated as a pointer, not as evidence** — see session 5 |
| 5 | 2026-08-24 | Etherscan (web) | Direct lookup of the address named in session 4 | `0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2`, labelled "Bybit Exploiter". Screenshot captured |
| 6 | 2026-08-24 | Etherscan API V2 | `txlist` + `tokentx` for address from session 5 | 255 transfers: 46 native, 209 token. ~400,001 ETH native outbound; stETH, mETH, cmETH; and 9 token groups with impersonating symbols |

**Sessions 1–3** examined a candidate anchor that was *rejected*: its outbound history totalled 0.16 ETH, a scale inconsistent with the reported incident. The rejection is recorded because a candidate considered and discarded is part of the method, not a false start to be omitted.

**Session 6** was the behavioural validation that accepted the anchor (Phase 02, §5.4). It queried the same address later retrieved in session 7, but is recorded separately because it is a distinct retrieval at a distinct time.

## Phase 03 — Trace retrievals

Each retrieval is preserved in full at the path shown. The `retrieved_utc` field is written into every row of each file by the retrieval tool, so the timestamps below are verifiable *within the data* rather than asserted only here.

| # | Date/time (UTC) | Address queried | Returned | Output |
|---|---|---|---|---|
| 7 | 2026-08-26 14:10:09 | `0x47666Fab…86E2` (anchor) | 255 transfers — 46 native, 209 token | `data/raw/hop1.csv` |
| 8 | 2026-08-26 14:42:21 | `0xa4b2fd68…449e` | 43 transfers — 20 native, 23 token | `data/raw/hop2.csv` |
| 9 | 2026-08-26 20:43:27 | `0xdd90071d…5f92` | 284 transfers — 54 native, 230 token | `data/raw/hop3.csv` |
| 10 | 2026-08-26 21:09:16 | `0xf3025725…72be` | 147 transfers — 74 native, 73 token | `data/raw/hop4.csv` |
| 11 | 2026-08-28 16:50:17 | `0x327ffe25…ba23` | 65 transfers — 9 native, 56 token | `data/raw/hop5.csv` |

**No filter was applied at collection.** Full outbound histories were retrieved and the separation of legitimate assets from impersonating tokens was performed at analysis, so the raw record retains everything each address actually shows.

## Phase 03 — Destination verification (web)

Explorer pages consulted to establish whether a destination was a contract or an account, and to record any entity label. All captured, because labels are perishable.

| # | Date (UTC) | Address | Established | Capture |
|---|---|---|---|---|
| 12 | 2026-08-26 | `0x6bb00006…0000` | Contract; creator tagged as a DEX aggregator deployer | `data/screenshots/hop2-velora-aggregator.png` |
| 13 | 2026-08-26 | `0x04708077…1c14` | Contract; tagged as a liquidity pool | `data/screenshots/hop2-uniswap-meth5-pool.png` |
| 14 | 2026-08-26 | `0xfe837a35…dffc` | Contract; DEX fee-route proxy, swap methods | `data/screenshots/hop2-dodo-fee-route-proxy.png` |
| 15 | 2026-08-26 | `0xf3025725…72be` | Account; labelled "Bybit Exploiter 45", tagged `Exploit` | `data/screenshots/hop3-bybit-exploiter-45.png` |
| 16 | 2026-08-28 | `0x8ed8553d…6036` | Account; funded by "Bybit Exploiter 9" | `data/screenshots/hop4-8ed8553d.png` |
| 17 | 2026-08-28 | `0x8b62111b…1ca1` | Account; deposit calls to a cross-chain bridge | `data/screenshots/hop4-8b62111b-thorchain.png` |
| 18 | 2026-08-28 | `0x21032176…044c` | Account; labelled "Bybit Exploiter 46" | `data/screenshots/hop4-21032176-exploiter46.png` |
| 19 | 2026-08-28 | `0x54acab84…fba2` | Account; repeated bridge deposits | `data/screenshots/hop4-54acab84-thorchain.png` |
| 20 | 2026-08-28 | `0x327ffe25…ba23` | Account; unlabelled | `data/screenshots/hop4-327ffe25.png` |

## Phase 04 — Reference framework

| # | Date (UTC) | Source | Consulted for |
|---|---|---|---|
| 21 | review stage | FATF (2020), *Virtual Assets: Red Flag Indicators of Money Laundering and Terrorist Financing* | Typology correspondence. Read at source: §11 (p. 6) and §12 (p. 9) verified directly, and the absence of any corresponding indicator for four of the six observed patterns confirmed by reading rather than assumed |

## Phase 06 — Cross-validation

**Read only after the findings of Phases 03–05 were finalized.** "Review stage" denotes the cross-validation stage that followed the independent trace; see the sequence integrity declaration below.

| # | Date (UTC) | Source | Grading |
|---|---|---|---|
| 22 | review stage | SlowMist Security Team, 2025-02-23 — on-chain analysis, read via PANews republication | B2 |
| 23 | review stage | NCC Group (Rivas, Santos & Sanz), 2025-03-10 — *In-Depth Technical Analysis of the Bybit Hack* | A2 |
| 24 | review stage | Associated Press (Gambrell), 2025-02-27 — reporting the FBI public service announcement | A1 |

---

## Source grading

Sources graded under the Admiralty Code (NATO STANAG 2511): letter = source reliability (A–F), numeral = information credibility (1–6).

| Source | Rating | Justification |
|---|---|---|
| On-chain transaction data | **Not graded** | Not a source in the intelligence sense. This is the primary record — immutable, independently verifiable by any party against any node. |
| Etherscan — transaction data | **B1** | A widely-used explorer presenting protocol data faithfully. Rated B rather than A because it is an intermediary; the underlying chain is authoritative and could be queried directly against a node. |
| Etherscan — entity labels | **B2** | The labels are Etherscan's own editorial attributions, not protocol facts. Credibility rated 2 because they are broadly corroborated by other platforms but are not independently verifiable from the chain itself. |
| FATF (2020) Red Flag Indicators | **A1** | Primary standards document from the issuing body, consulted directly rather than through summary. |
| SlowMist analysis (via republication) | **B2** | Competent specialist firm with detailed analysis. Rated B rather than A because it was read via republication rather than the primary publication, and because its tracing relies on a proprietary tool whose heuristics cannot be independently verified from public data. |
| NCC Group technical analysis | **A2** | Named authors; primary technical detail including contract addresses and code, independently checkable on-chain. |
| Associated Press, reporting the FBI announcement | **A1** | A1 for the fact of the FBI statement. The attribution it contains is the FBI's, not this analysis's. |
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

| Event | Date (UTC) | Evidence |
|---|---|---|
| Anchor address sourced | 2026-08-24 | Sessions 4–5 above |
| **Independent analysis begins** | 2026-08-24 | From the moment the anchor was accepted, no third-party analysis of fund movement was consulted |
| Independent data collection | 2026-08-24 → 2026-08-28 | Sessions 6–20 — anchored by the `retrieved_utc` field written into every row of `data/raw/*.csv` at collection time |
| **Findings finalized** | 2026-08-28 | Phases 03–05 complete: the trace, its reliability classification, and every claim register entry were fixed before any published analysis was read |
| **Third-party analyses first consulted** | after 2026-08-28 | Sessions 21–24, during the cross-validation and review stage |

**What was read before the independent analysis:** the incident date, the affected exchange, and addresses labelled in connection with it.
**What was not read:** any account of where the funds moved after leaving the anchor.

**Why this ordering matters.** The comparison in Phase 06 measures independent reach. That measurement is meaningful only if the findings existed before the published analyses were read. The published sources (SlowMist, NCC Group, the FBI announcement) were consulted only during the cross-validation stage, after the five-hop trace and its reliability classification were complete.

**On the evidence for the ordering.** The anchor of the timeline is the `retrieved_utc` field embedded by the retrieval tool in every row of the raw data: the five hop files carry collection timestamps from 2026-08-26 and 2026-08-28, which fixes the independent-collection window in the data itself, independent of any later record. The repository was initialized after the investigation was conducted, so the commit history reflects when files were published rather than when each phase was produced; it is therefore **not** relied upon as evidence of sequence. The `retrieved_utc` timestamps in the raw data are the primary evidence that collection preceded cross-validation, and they cannot be back-dated without altering the files the findings are built on.

---

## Reproducibility notes

- **Transaction data is permanent.** Any hash recorded here can be re-verified by any party at any time against any node or explorer for the relevant chain.
- **Labels are perishable.** Where a finding depends on an entity label, both the platform and the date of observation are recorded, because labels are revised. Screenshots were captured for every label that informed a decision (sessions 12–20).
- **Token symbols are not identifiers.** Symbols are chosen by whoever deploys the contract, and several encountered at the anchor impersonate legitimate assets. Every token referenced in this investigation is identified by contract address; the symbol is recorded as displayed but carries no evidentiary weight.
- **Retrievals are unfiltered.** No value threshold was applied at collection, so the raw files retain the complete outbound history of each address — including the impersonating token transfers that analysis excluded.
- **No active interaction.** No wallet was connected, no contract called, no transaction broadcast. All queries were read-only against public explorer services.
