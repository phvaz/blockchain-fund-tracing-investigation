# Blockchain Investigation Case Study — Public Trail Analysis of the Bybit 2025 Incident

> **📄 [Read the full report (PDF, 34 pages)](phase07-report/BIC-2026-001-blockchain-investigation-report.pdf)**
>
> **Case reference:** BIC-2026-001 · **Status:** Complete · **Classification:** Academic portfolio

An independent, open-source reconstruction of one delimited fund trail associated with the publicly reported Bybit incident of February 2025 — and a measurement of the point at which open-source analysis stops working.

The investigation used a public block explorer and a purpose-built retrieval script. No commercial blockchain intelligence platform was used, and no published analysis of the incident was read until every finding had been finalized and committed.

---

## The question this project answers

The destination of the stolen funds is already documented by firms with proprietary datasets and by agencies with subpoena power. That was never the question here.

**How far can an independent analyst trace such a trail using only public data, and what exactly stops them?**

The answer, established in Section 11 of the report: open-source tracing and a specialist firm's proprietary platform agree **completely** on the Ethereum-native path — same addresses, same amounts, one figure matching to four decimal places. They diverge at exactly one point: the cross-chain bridge. Crossing it requires proprietary heuristics or legal process. The limit is not one of skill or effort; it is the point at which the required information ceases to exist on the public Ethereum ledger.

---

## Principal findings

| Finding | Detail |
|---|---|
| **Five hops reconstructed independently** | From the anchor through derivative consolidation, DEX conversion to native ETH, two levels of fragmentation, and a final consolidation point — 98,376 ETH-equivalent at the first hop, narrowing to 454 ETH at the fifth |
| **Corroborated transfer-for-transfer** | Matches a specialist firm's published analysis through the first three hops, with that analysis read only *after* the findings were frozen and committed |
| **Deliberate contamination identified** | Nine impersonating token contracts using non-Latin homoglyphs, clean-ASCII forgeries that no automated check catches, and 31 lookalike addresses matching genuine counterparties in their first six and last four characters |
| **Two FATF indicators verified at source** | Fragmentation (§11, p. 6) and multi-asset conversion (§12, p. 9). Four further patterns had **no** correspondence and were recorded as observations rather than forced into a classification |
| **No attribution asserted** | Published sources attribute the incident to a named actor on evidence this analysis did not have. Cross-validation later confirmed that stopping short was correct |

### The trap the contamination forms

The impersonating `stETH` contract shows **554,882 units outbound — the largest single figure in the entire dataset**, larger than any legitimate movement. Its destination is a lookalike of the genuine branch, matching in the first six and last four characters.

An analyst ranking branches by displayed amount, without verifying contract addresses, would have selected a fabricated flow, followed it to the wrong address, and continued from there. Every subsequent hop would be wrong, and **nothing in the output would indicate an error**.

---

## Method

### Pre-registration

The rule governing branch selection and termination was written and committed to version control **before any transaction data was examined**:

> **Branch selection.** Highest value at each fragmentation; where amounts are identical, the earliest timestamp; where timestamps are also identical, the lowest destination address lexicographically.
>
> **Termination.** Mixer or bridge entry, or five hops from the anchor — whichever comes first.

The rule proved consequential. At Hop 3 the trace met nine branches of exactly 10,000 ETH each, a condition under which "highest value" selects nothing. The tie-breaker — written before that condition was encountered — resolved the choice without discretion being exercised at the point of decision.

### Claim taxonomy

Every claim is typed, because on a public ledger the raw data is exceptionally reliable while conclusions drawn from it are often weaker than they appear:

| Type | Basis |
|---|---|
| **Fact** | Recorded on-chain; verifiable by any party against any node |
| **Inference** | Reasoned from facts using a stated heuristic; carries a confidence level |
| **Attribution** | Links an address to a named actor. Requires evidence beyond the ledger — **not asserted by this analysis** |

Final register: **10 facts · 8 inferences · 3 third-party attributions recorded but not adopted.**

### Sequence integrity

Published analyses were not consulted during the investigative phases. Only the anchor address was sourced externally, and the collection log records what was read, when, and from where. Cross-validation occurred only after findings were committed — **and the findings were not revised afterwards.** An analyst who reads the answer first cannot afterwards distinguish what they found from what they were looking for.

---

## Repository

| Phase | Contents |
|---|---|
| [00 — Scope, OpSec & Methodology](phase00-scope-and-opsec/) | Pre-registered stopping rule, threat model, analytic standards |
| [01 — Environment](phase01-environment/) | Isolated environment, egress verification, tooling validation |
| [02 — Anchor Point](phase02-anchor/) | Three-level provenance chain; first identification of token impersonation |
| [03 — Independent Trace](phase03-trace/) | Five hops, hop by hop, with every unfollowed branch recorded |
| [04 — Typologies](phase04-typologies/) | FATF correspondence, verified at source — including where none exists |
| [05 — Reliability](phase05-reliability/) | Claim register; the private attribution boundary |
| [06 — Cross-Validation](phase06-validation/) | Comparison against published analyses |
| [07 — Report](phase07-report/) | **[The consolidated report](phase07-report/BIC-2026-001-blockchain-investigation-report.pdf)** |

**Supporting material:** [`methodology/`](methodology/) — scope, OpSec posture, analytic standards · [`collection-log.md`](collection-log.md) — provenance record for every external source · [`tools/`](tools/) — retrieval script and its development log · [`data/`](data/) — raw retrieval output and captures

---

## Tooling

[`tools/trace_helper.py`](tools/trace_helper.py) retrieves and tabulates outbound transfers for an address. Its [development log](tools/README.md) records each change and what prompted it — the tool grew in response to what the investigation revealed, and its limitations at each stage bear on what the analysis could see at the time.

Three decisions embedded in it are worth noting, because each encodes a piece of investigative reasoning:

- **It never sums across assets.** One unit of one token and one unit of another are not comparable quantities.
- **It reads token decimals rather than assuming them.** Assuming 18 for a 6-decimal token understates the amount by a factor of a trillion — silently.
- **It groups by `(symbol, contract)`, never by symbol.** A token's symbol is chosen by whoever deploys it. Only the contract address identifies an asset.

**What it does not do:** make analytical decisions. It surfaces the highest-value destination and then states explicitly that branch selection remains the analyst's. It flags non-Latin characters in symbols, but a clean-ASCII forgery passes unflagged — as one did at Hop 3, and was caught by judgment rather than by the tool.

---

## Scope and limitations

The trail documented carries approximately **0.11%** of the value that left the anchor. The remaining 99.89% was not examined.

**No statement in this project about "the funds" applies beyond the single documented path.** This is the stopping rule operating as designed, and it is the boundary governing the weight of every conclusion. The full set of limitations, each with its concrete impact, is in Section 12 of the report.

---

## Legal and ethical position

All data examined is public by design. Blockchain ledgers are open records published by the protocol to every participant; reading one is not analogous to accessing a private system. **No query was directed at any private system, no wallet was connected, no contract was called, and no transaction was broadcast.**

The passive-only method was chosen deliberately: it keeps the investigation on the correct side of the boundary between consulting published records and unauthorized access (Lei 12.737/2012, Art. 154-A, and comparable statutes).

No natural person is named or identified, and identification of natural persons was explicitly out of scope. Anything surfaced that was not already present in public reporting would have been withheld and reviewed privately before any disclosure decision; no such material arose.

This is an academic case study. It is **not** a legal instrument, an accusation, or an intelligence product in any jurisdiction.

---

## Analyst

**Paulo Vaz** — digital forensics and financial crime investigation

