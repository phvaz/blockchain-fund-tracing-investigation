# Phase 03 — Independent Trace

**Status:** `[ ] In progress`

## Objective

Reconstruct the fund trail hop by hop from the anchor address, within the pre-registered stopping rule, documenting every transaction and every branch not followed.

## Stopping rule in force

> **Branch selection.** Highest value at each fragmentation. Where amounts are identical, the earliest timestamp; where timestamps are also identical, the lowest destination address in lexicographic order.
>
> **Termination.** Mixer or bridge entry, or five hops from the anchor — whichever comes first.

Branches not followed are recorded, not discarded. An unexplored branch that is documented is a scope decision; an unexplored branch that is omitted is a gap.

## Valuation basis (declared before tracing)

The anchor's outbound movement spans four legitimate assets: ETH, and the liquid-staking derivatives stETH, mETH and cmETH. The pre-registered rule selects the highest-value branch, which requires comparing amounts across assets.

**Declared basis:** stETH, mETH and cmETH are treated as approximately **1:1 equivalent to ETH** for the purpose of branch selection. All three are ETH liquid-staking derivatives designed to track the value of the underlying ETH.

**This is a stated judgment, not a fact.** These instruments trade at a small and variable discount or premium to ETH, and no market data was consulted to establish the rate at the relevant time. The judgment is recorded here because the branch selected at Hop 1 depends on it, and a reader is entitled to disagree with it. It is sufficient for ranking branches whose magnitudes differ by roughly an order of magnitude; it would not be sufficient where two branches were close in value.

## A note on what counts as a hop

Not every destination is a counterparty. Funds sent to a smart contract that performs a swap have not arrived anywhere — they have been converted, and the trail continues in whatever asset came out. Treating such a contract as a destination would end the trace at infrastructure rather than at a party.

Every destination in this trace is therefore checked on Etherscan to establish whether it is a contract or an externally-owned account before it is treated as a hop. Where a destination is a swap venue, the continuation is identified by reconciling what entered against what left.

---

## Hop 1

**From:** `0x47666Fab8bd0Ac7003bce3f5C3585383F09486E2` (anchor)
**Retrieved:** 2026-08-26 14:10:09 UTC · `data/raw/hop1.csv` · 255 transfers (46 native, 209 token)
**Filter applied:** none. Full outbound history retrieved; separation of signal from noise performed at analysis, not at collection.

### Signal separation

Of 20 distinct token groups returned, only three are legitimate assets. The remainder are impersonating tokens (Phase 02, "Finding: token symbol impersonation").

| Asset | Contract | Status |
|---|---|---|
| ETH (native) | — | Protocol asset |
| stETH | `0xae7ab96520de3a18e5e111b5eaab095312d7fe84` | Lido staked ETH |
| mETH | `0xd5f7838f5c461feff7fe49ea5ebaf7728bb0adfa` | Mantle staked ETH |
| cmETH | `0xe6829d9a7ee3040e1276fa75293bde931859e8fa` | Mantle cmETH |

All other token groups were excluded. Their amounts are raw units of tokens whose symbols are chosen by their deployer and carry no relationship to any asset they resemble.

**Excluded from analysis, retained in `hop1.csv`:** 209 token transfers across 17 groups, including 9 with non-ASCII symbols and one with the symbol `BybitExploiter` (contract `0x98bdd7aa…6c5f`, 17,330,506 units transferred to the anchor itself).

### Destinations — legitimate assets only

| Destination | ETH-equivalent | Composition |
|---|---|---|
| **`0xa4b2fd68593b6f34e51cb9edb66e71c1b4ab449e`** | **98,376.55** | 1 ETH · 90,375.55 stETH · 8,000 mETH |
| `0x1542368a03ad1f03d96d51b414f4738961cf4443` | 15,000.00 | 15,000 cmETH |
| 40 distinct addresses | 10,000.00 each | ETH native |

**Observed.** Between 14:29:47 and 15:54:23 UTC on 2025-02-21, the anchor address made 46 outbound transfers of legitimate assets. One destination received 98,376.55 ETH-equivalent across five transfers in four assets. A second received 15,000 cmETH. The remaining 400,000 ETH was divided into exactly forty transfers of 10,000 ETH each, to forty distinct addresses, between 14:56:11 and 15:54:23 — the bulk of them within a six-minute window from 15:48 to 15:54.

**Interpretation.** Two distinct handling patterns are present in the same hour: consolidation of the staked-ETH derivatives into a single destination, and uniform fragmentation of the native ETH across forty destinations. — *Confidence: High* as to the pattern itself. The purpose of either pattern is addressed in Phase 04.

**Boundary.** This establishes what moved, when, and to which addresses. It does not establish who controlled any address, whether the forty destinations are under common control, or why the two asset classes were handled differently.

### Branch selected

`0xa4b2fd68593b6f34e51cb9edb66e71c1b4ab449e` — 98,376.55 ETH-equivalent.

**Basis:** highest value under the pre-registered rule, applying the valuation basis declared above. The selected branch exceeds the next largest by a factor of approximately 6.5 and each individual native-ETH branch by a factor of approximately 9.8. The margin is wide enough that the outcome does not turn on the precise exchange rate assumed.

**The tie-breaker was not required at this hop.** Phase 02 anticipated that forty identical branches would leave "highest value" undetermined. That assessment considered native ETH alone. Once legitimate token transfers are included, a clear highest-value branch exists and the tie-breaking rule of Section 4.1 does not come into play. It remains in force for subsequent hops.

**Transfers composing the selected branch:**

| Timestamp (UTC) | Asset | Amount | Transaction |
|---|---|---|---|
| 2025-02-21 14:29:47 | ETH | 1.000000 | `0xdd5cd734d4d67ff5af7e53cdd72c26d4d7d28d08c8f0ff32d12ab3e2a277e4bc` |
| 2025-02-21 14:41:23 | stETH | 10,000.000000 | `0x0085abb10611a46b804015da4915f5ca7bff421973893f5dbbf898822e87e716` |
| 2025-02-21 14:47:11 | stETH | 50,000.000000 | `0x831fe178421f4b4f81cb47c09cbd04d7d0b10fcd8101a9475b650bbb6204c0b4` |
| 2025-02-21 15:10:35 | mETH | 8,000.000000 | `0x928119db1e05337cd9ddef10f9c8ff2e7664021429f5db6343e8d09af30074c0` |
| 2025-02-21 15:12:23 | stETH | 30,375.547918 | `0x9e9d1400f9fecdfe74b991821773b30525897986af5a8568ef490d6e7092c72e` |

The 1 ETH transfer at 14:29:47 precedes the asset transfers and is of a magnitude consistent with funding transaction fees at the destination. This is an interpretation of a common pattern, at *moderate* confidence; the transfer itself is a fact.

### Branches observed and not followed

**41 branches, carrying approximately 415,000 ETH-equivalent in total, were not followed.**

| Branch group | Count | Amount each | Total |
|---|---|---|---|
| Native ETH fragmentation | 40 | 10,000 ETH | 400,000 ETH |
| cmETH consolidation | 1 | 15,000 cmETH | 15,000 |

The forty native-ETH destinations, in chronological order of transfer, with transaction hashes, are recorded in `data/raw/hop1.csv` (filter: `kind=native`, `amount=10000`). The first is `0x36ed3c0213565530c35115d93a80f9c04d94e4cb` at 14:56:11; the last is `0xbca02b395747d62626a65016f2e64a20bd254a39` at 15:54:23. The cmETH destination is `0x1542368a03ad1f03d96d51b414f4738961cf4443`, transaction `0xc69bfdf13092927ba355863dc7963393dce17479276bc8042026f6115d570b77`.

**Note on proportion.** The followed branch carries roughly 19% of the ETH-equivalent leaving the anchor. The unfollowed 81% is not analysed by this investigation. This is the stopping rule operating as designed, not an omission — but it bounds every conclusion drawn downstream, and no claim about "the funds" should be read as applying to more than the branch traced.

---

## Finding: address poisoning at scale

The impersonating tokens identified in Phase 02 were not sent to arbitrary addresses.

**Observed.** Of 124 destination addresses receiving impersonating tokens, **31 share both the first six and the last four hexadecimal characters with an address that received legitimate assets**. Twenty-four of the 42 legitimate destinations have at least one such counterpart.

The selected branch has three:

| Role | Address |
|---|---|
| **Legitimate** — received stETH and mETH | `0xa4b2fd68593b6f34e51cb9edb66e71c1b4ab449e` |
| Lookalike — received impersonating tokens | `0xa4b24033f4c6d70133e4557c2c32a3fb693e449e` |
| Lookalike — received impersonating tokens | `0xa4b27b89345db2e5e1a7d7bc537fac354b50449e` |
| Lookalike — received impersonating tokens | `0xa4b2c2e7a2a0f7f406257d992af5e6bca5d0449e` |

All four begin `0xa4b2` and end `449e`.

**Interpretation.** This is *address poisoning*: addresses are generated to match the leading and trailing characters of a genuine counterparty, then used as destinations for worthless transfers so that they appear in the target's transaction history. Because addresses are conventionally verified by their first and last characters — which is how explorers abbreviate them and how most users check them — the substitution is not visible without full-string comparison. — *Confidence: High.* Thirty-one matches on a twenty-hexadecimal-digit constraint do not arise by chance; each requires deliberate key generation.

**Boundary.** The identity and purpose of whoever deployed these contracts and generated these addresses is **not established**. Deliberate obstruction of forensic analysis, opportunistic phishing directed at the address owner, and automated spam targeting notable addresses all produce this signature. The evidence does not distinguish between them, and no attribution is made.

**Consequence for this analysis.** Combining the two techniques produces a specific trap for an analyst tracing this trail. The impersonating `stETH` (contract `0xee33058e…c562`) shows 554,882 units outbound — the largest single figure in the entire retrieval, larger than any legitimate movement. Its destination is `0xa4b24033…449e`, a lookalike of the genuine branch. An analyst who ranked branches by displayed amount without verifying contracts would have selected a fabricated flow, followed it to a lookalike address, and continued from there. Every subsequent hop would be wrong, and nothing in the output would indicate an error.

**Control applied.** Branch selection in this investigation is performed on legitimate assets only, verified by contract address. Destination addresses are compared in full, never by leading and trailing characters.

---

## Hop 2

**From:** `0xa4b2fd68593b6f34e51cb9edb66e71c1b4ab449e`
**Retrieved:** 2026-08-26 14:42:21 UTC · `data/raw/hop2.csv` · 43 transfers (20 native, 23 token)
**Filter applied:** none.

### Signal separation

Two of five token groups are legitimate: stETH (`0xae7ab965…fe84`) and mETH (`0xd5f7838f…adfa`). The remaining three carry non-ASCII symbols and were excluded — a smaller instance of the same impersonation documented at Hop 1.

### Destinations

| Destination | Received | Transfers | Type |
|---|---|---|---|
| `0xdd90071d52f20e85c89802e5dc1ec0a7b6475f92` | 98,048.7948 ETH | 3 | *(established at Hop 3)* |
| `0x6bb000067005450704003100632eb93ea00c0000` | 75,187.7740 stETH | 8 | **Contract** — swap venue |
| `0xfe837a3530dd566401d35befcd55582af7c4dffc` | 15,187.7740 stETH | 1 | **Contract** — swap venue |
| `0x04708077eca6bb527a5bbbd6358ffb043a9c1c14` | 8,000.0000 mETH | 3 | **Contract** — liquidity pool |
| `0x1542368a03ad1f03d96d51b414f4738961cf4443` | 0.1 ETH | 1 | — |

### Destination classification

Each destination receiving a staked derivative was checked on Etherscan. All three are contracts, and all three are decentralised-exchange infrastructure.

| Contract | Etherscan label (observed 2026-08-26) | Capture |
|---|---|---|
| `0x6bb000067005450704003100632eb93ea00c0000` | Contract; creator tagged "Velora: Deployer 1" | [`hop2-velora-aggregator.png`](../data/screenshots/hop2-velora-aggregator.png) |
| `0x04708077eca6bb527a5bbbd6358ffb043a9c1c14` | "Uniswap V3: mETH 5" — tagged *Liquidity Pool* | [`hop2-uniswap-v3-meth5-pool.png`](../data/screenshots/hop2-uniswap-v3-meth5-pool.png) |
| `0xfe837a3530dd566401d35befcd55582af7c4dffc` | "DODO: Fee Route Proxy"; transaction methods shown as *External Swap* and *Mix Swap* | [`hop2-dodo-fee-route-proxy.png`](../data/screenshots/hop2-dodo-fee-route-proxy.png) |

These labels are **third-party attributions by Etherscan**, not protocol facts, and are perishable — the "Velora" tag reflects a protocol that was previously named otherwise. Captures were taken for that reason.

### Reconciliation

| | ETH-equivalent |
|---|---|
| Received at this address (Hop 1) | 98,376.5479 |
| Sent out as native ETH | 98,048.8948 |
| **Difference** | **327.6531 (0.333%)** |

**Observed.** The address received 98,376.55 ETH-equivalent in staked derivatives and 1 ETH. It sent 90,375.55 stETH and 8,000 mETH to three exchange contracts, and 98,048.79 native ETH to a single address, all within approximately 50 minutes on 2025-02-21.

**Interpretation.** The staked derivatives were converted to native ETH through decentralised exchanges, and the proceeds forwarded to `0xdd90071d…5f92`. — *Confidence: High.*

Two independent lines support this:

1. **Arithmetic.** Inflow and native-ETH outflow reconcile to within 0.333%, a margin consistent with exchange fees and slippage. Had the derivatives been transferred to third-party wallets *in addition to* the ETH leaving, total outflow would have approximated twice the inflow. It does not.
2. **Destination type.** All three derivative destinations are exchange contracts rather than accounts. Assets sent to them are exchanged, not held.

**Boundary.** The reconciliation establishes that the amounts are consistent with conversion. It does not prove that the specific ETH forwarded to `0xdd90071d…5f92` is the same ETH that emerged from these particular swaps — fungibility makes that claim unavailable on-chain. What is established is that this address received derivatives, exchanged derivatives, and forwarded an almost identical quantity of ETH within the same short window.

### Note on tranching

The stETH sent to `0x6bb00006…0000` was divided into eight transfers over 44 minutes: 10,000 · 25,000 · 12,000 · 7,000 · 6,000 · 7,187.77 · 4,000 · 4,000.

**Interpretation.** Dividing a large conversion into smaller portions is standard practice for limiting price impact on a decentralised exchange, and is equally consistent with avoiding a single conspicuous transaction. — *Confidence: Low* as to purpose. Both explanations fit the observation and the evidence does not distinguish between them.

### Branch selected

`0xdd90071d52f20e85c89802e5dc1ec0a7b6475f92` — 98,048.7948 ETH, across three transfers:

| Timestamp (UTC) | Amount | Transaction |
|---|---|---|
| 2025-02-21 14:45:11 | 9,980.0000 | `0xf7900c28239b45d83a5389e8debc491446d380680a6fd156c6ec9a3479c7e0c9` |
| 2025-02-21 14:57:59 | 49,755.0000 | `0xad905e884090fd39c56de1673fb0d61bc4d4d8d6140b054d9dda518226ca4c09` |
| 2025-02-21 15:32:35 | 38,313.7948 | `0xcffbad26c03f02e2fdd131bcc6576b58cdc5793bb2760c2c763e45825127b9ae` |

**Basis:** the only destination that is an account rather than exchange infrastructure, and the destination of essentially the entire value passing through this address. Unlike Hop 1, no meaningful branching occurred here — the followed branch carries approximately 99.7% of what left.

**Branches not followed:** one transfer of 0.1 ETH to `0x1542368a03ad1f03d96d51b414f4738961cf4443`, the same address that received 15,000 cmETH at Hop 1 and was recorded there as an unfollowed branch.

### Termination check

Decentralised exchanges are **not** a termination condition under the stopping rule. The rule terminates at a mixer or a cross-chain bridge, both of which sever the link between input and output. A swap does not: the output is observable on the same chain and reconciles against the input, as demonstrated above. The trail continues.

---

## Hop 3

**From:** `0xdd90071d52f20e85c89802e5dc1ec0a7b6475f92`

`[pending]`
