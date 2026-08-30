# Phase 03 — Independent Trace

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
| `0x04708077eca6bb527a5bbbd6358ffb043a9c1c14` | "Uniswap V3: mETH 5" — tagged *Liquidity Pool* | [`hop2-uniswap-meth5-pool.png`](../data/screenshots/hop2-uniswap-meth5-pool.png) |
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
**Retrieved:** 2026-08-26 20:43:27 UTC · `data/raw/hop3.csv` · 284 transfers (54 native, 230 token)
**Filter applied:** none.

### Signal separation

**No legitimate token transfers were present at this hop.** All nine token groups are impersonating contracts — seven carrying non-ASCII symbols, and two carrying the clean-ASCII symbol `ETH`:

| Symbol | Contract | Flagged by non-ASCII detection |
|---|---|---|
| `ETH` | `0x2f22686d82dded300c975e63b62efbe824c9d236` | **No** |
| `ETH` | `0xfabda8051efe4462367785953a3bba55cefe7215` | **No** |

**There is no legitimate ERC-20 token with the symbol `ETH` on Ethereum mainnet.** ETH is the protocol's native asset; it is not a token contract. Any ERC-20 presenting itself as `ETH` is by definition impersonating.

This is the residual limitation recorded in Phase 02 materialising in practice: non-ASCII detection catches crude impersonation, but a contract deployed with a clean ASCII symbol passes unflagged. Both were excluded on the analyst's judgment, not on the tool's warning — which is precisely the division of labour the tooling documentation states.

The only legitimate asset at this hop is native ETH.

### Two distinct operating regimes

The 54 native transfers do not form a single episode. They fall into two groups separated by ten days, with markedly different characteristics.

| | Regime A | Regime B |
|---|---|---|
| Date | 2025-02-21 | 2025-03-03 |
| Window | 16:04:23 – 16:05:11 (**48 seconds**) | 15:42:59 – 18:13:47 (~2h 31m) |
| Transfers | 9 | 45 |
| Distinct destinations | 9 | 30 |
| Amounts | 10,000 ETH exactly, all nine | Irregular: 0.88 to 561.06 |
| Total | 90,000.0000 ETH | 8,055.3621 ETH |

**Observed.** 90% of the value left in nine identical round-number transfers within 48 seconds. The remainder left ten days later, in 45 irregular transfers spread over two and a half hours, several destinations receiving multiple times.

**Interpretation.** Two operationally distinct handling patterns applied to the same holdings: rapid bulk distribution in uniform units, followed after a pause by dispersed distribution in varied amounts. — *Confidence: High* as to the distinction; the purpose of either regime is addressed in Phase 04.

**Boundary.** The ten-day gap and the change in pattern are facts. Whether they reflect a single actor changing method, different actors, or an automated process with a scheduled second stage is **not established**.

### Reconciliation

| | ETH |
|---|---|
| Received from Hop 2 | 98,048.7948 |
| Sent out (native) | 98,055.3621 |
| **Difference** | **+6.5673** |

**Observed.** Outflow exceeds the traced inflow by 6.57 ETH.

**Interpretation.** The address received ETH from at least one source other than the branch under trace. — *Confidence: High*; the arithmetic admits no alternative.

**Boundary.** The additional inflow was not traced, as inbound analysis falls outside the scope defined in Phase 00. Its magnitude (0.007% of throughput) is consistent with fee funding, but that is inference. It is recorded because an unexplained discrepancy that goes unmentioned is indistinguishable from one that went unnoticed.

### Branch selected — tie-breaker applied

Regime A produced **nine branches carrying exactly 10,000 ETH each**. The pre-registered highest-value criterion does not discriminate between them. The tie-breaking rule of `scope-and-limitations.md` §4.1 applies for the first time in this trace:

> *Where two or more branches carry identical amounts, the branch whose transfer bears the earliest timestamp is followed.*

| Timestamp (UTC) | Destination | Transaction |
|---|---|---|
| **2025-02-21 16:04:23** | **`0xf302572594a68aa8f951fae64ed3ae7da41c72be`** | `0x376e337568836889c535ef3947ea89bb918a091e3e6199eefdbe6a6fbacf4579` |
| 2025-02-21 16:04:35 | `0x21032176b43d9f7e9410fb37290a78f4fed6044c` | `0xc6eed5e140214435bdca2980b6208d401d087994cf920ce3a35065e72584b3de` |
| 2025-02-21 16:04:35 | `0xd5b58cf7813c1edc412367b97876bd400ea5c489` | `0x93fbe49b7ccef8e710cff22f5aec11169120fa7128f07394d51f2d434fd92716` |
| 2025-02-21 16:04:35 | `0xa5a023e052243b7cce34cbd4ba20180e8dea6ad6` | `0x3e108a7563b241e926bd9f11c25936242c65b7135137a77a917b85daa46941f6` |
| 2025-02-21 16:04:47 | `0x723a7084028421994d4a7829108d63ab44658315` | `0xa51405c351f811ac75cc05f379238d8aad6ba22c73b0003b1975b7a248835b03` |
| 2025-02-21 16:04:47 | `0x1512fcb09463a61862b73ec09b9b354af1790268` | `0x148787980a84f789e813bf4f92189d2eafeffb27577d61e8915ffec0a1bda955` |
| 2025-02-21 16:04:59 | `0xeb0baa3a556586192590cad296b1e48df62a8549` | `0xa109b67584276a45fcae7d199b2dfc142f404161a4dbf6ede3cc7e7cb4575b72` |
| 2025-02-21 16:05:11 | `0xf03afb1c6a11a7e370920ad42e6ee735dbedf0b1` | `0x6f9a9d648afe1cf0858851f4505b2583411e0968139ce9cacc8cde60bd5f1cbe` |
| 2025-02-21 16:05:11 | `0x55cca2f5eb07907696afe4b9db5102bce5feb734` | `0x925870b65105c2456a8a96ac3f5a5cdb48c38a1267770ad1c700a977ca5003b2` |

The earliest transfer is unique — the next three occur twelve seconds later — so the secondary criterion (lexicographic ordering of the destination address) was not required.

**Selected:** `0xf302572594a68aa8f951fae64ed3ae7da41c72be`

The rule was written before any hop was traced and before this condition was encountered. It resolved the selection without discretion being exercised at the point of choice, which is the entire purpose of pre-registering it.

### Destination verification

`0xf302572594a68aa8f951fae64ed3ae7da41c72be` was checked on Etherscan before being treated as a hop.

| Field | Value (observed 2026-08-26) |
|---|---|
| Type | **Address** — externally-owned account, not a contract |
| Label | "Bybit Exploiter 45" |
| Tags | `Exploit`, `# Bybit Exploit` |
| Warning banner | *"There are reports that this address was used in an exploit on Bybit… Reported by ZachXBT"* |
| Funded by | "Bybit Exploiter 5" |
| Current ETH balance | 0.00047 |

Capture: [`hop3-bybit-exploiter-45.png`](../data/screenshots/hop3-bybit-exploiter-45.png)

**On the significance of this label.** This trail was followed from the anchor by mechanical application of the pre-registered rules — highest value, highest value, earliest timestamp — with no third-party analysis of fund movement consulted at any point. The address arrived at by that route carries an independent label associating it with the same incident, and Etherscan records it as funded by another address in the same labelled cluster.

**Interpretation.** The traced path is consistent with the movement of funds from the incident. — *Confidence: Moderate.*

**Boundary.** The label is a **third-party attribution by Etherscan, citing a third-party investigator**, not an on-chain fact. Nothing in the protocol identifies an address as belonging to any actor. Under this investigation's attribution policy this is recorded as *Etherscan, citing ZachXBT, associates this address with the incident* — it is not a finding of this analysis, and no attribution to any actor is made here.

Nor does this constitute the Phase 06 cross-validation. That comparison is against published analyses of fund movement, which remain unread. What is recorded here is an entity label encountered incidentally while verifying whether a destination was a contract or an account.

**Note on numbering.** The label "Bybit Exploiter 45" implies the labelling party has enumerated at least 45 addresses in this cluster. This is consistent with the fragmentation observed at Hops 1 and 3, and comes from a source independent of this analysis.

**Continuation confirmed.** The address retains 0.00047 ETH of the 10,000 received. The funds moved on; the trail does not terminate here.

### Branches observed and not followed

| Group | Count | Total | Note |
|---|---|---|---|
| Regime A — 10,000 ETH branches | 8 | 80,000 ETH | Tied with the selected branch; separated only by the tie-breaker |
| Regime B — irregular transfers | 45 | 8,055.36 ETH | Across 30 distinct destinations |

The eight unfollowed Regime A branches are listed in the table above with their transaction hashes. Regime B transfers are recorded in `data/raw/hop3.csv` (filter: `kind=native`, `timestamp_utc` beginning `2025-03-03`).

**Note on proportion.** The followed branch carries 10,000 ETH of the 98,055 that left this address — approximately **10.2%**. Combined with Hop 1, the traced path now represents a progressively narrower share of the funds leaving the anchor. This is the stopping rule operating as designed, and it bounds every downstream conclusion accordingly.

### Termination check

The destination is an externally-owned account, not a mixer or bridge. Four of five hops are used. The trail continues.

---

## Hop 4

**From:** `0xf302572594a68aa8f951fae64ed3ae7da41c72be` ("Bybit Exploiter 45")
**Retrieved:** 2026-08-26 21:09:16 UTC · `data/raw/hop4.csv` · 147 transfers (74 native, 73 token)
**Filter applied:** none.

### Signal separation

Three token groups, all impersonating — two with non-ASCII symbols and one with clean-ASCII `ETH` (`0x2f22686d…d236`), the same contract encountered at Hop 3. Native ETH is again the only legitimate asset.

### Movement

| | Value |
|---|---|
| Window | 2025-03-02, 14:45:59 – 17:01:11 UTC (~2h 15m) |
| Transfers | 74 |
| Distinct destinations | 58 |
| Amounts | Irregular: 11.96 – 303.31 ETH |
| Total out | 10,062.3582 ETH |
| Received from Hop 3 | 10,000.0000 ETH |
| **Difference** | **+62.3582** |

**Observed.** The 10,000 ETH received on 2025-02-21 remained at rest for nine days, then left on 2025-03-02 in 74 transfers of irregular amounts to 58 distinct addresses over roughly two hours. Several destinations received multiple times. Outflow exceeds the traced inflow by 62.36 ETH.

**Interpretation.** Dispersion across a wide destination set in non-uniform amounts, distinct from the uniform block distribution seen at Hop 3 Regime A. The excess outflow indicates the address received funds from at least one source other than the traced branch. — *Confidence: High* as to both observations.

**Boundary.** Whether the nine-day delay reflects deliberate timing, operational constraint, or an unrelated schedule is not established. The additional inflow was not traced; inbound analysis falls outside the scope defined in Phase 00.

### Top destinations

| Destination | Received (ETH) | Transfers |
|---|---|---|
| **`0x327ffe25f330d2d809106ace581099ad1af9ba23`** | **454.0611** | 2 |
| `0xa7c68815b8401109f70f23881d11fbb83db47f1e` | 356.6005 | 5 |
| `0x2c6924cc47e5c49ee1c949544d824c233e1e5fb9` | 353.4647 | 2 |
| `0x54acab846901bdbdc553a675d97240511e4bfba2` | 303.3091 | 1 |
| `0xa0f3246e7d02f77592929415b1891f3212a59bb7` | 300.8724 | 1 |
| `0x5a0a1bf453b2bda60f1256ee61126764384656a0` | 298.7888 | 1 |
| `0xdfcc0749f2d4d4e76b69ddf2183c3de10db825dd` | 298.2357 | 4 |

No destination receives more than 4.5% of the total. This is genuine dispersion, not division into blocks.

---

## Finding: convergence between branches

**Observed.** Four addresses receive from **both** Hop 3 and Hop 4:

| Address | From Hop 3 | From Hop 4 |
|---|---|---|
| `0x8ed8553dd6375766d712c1f296f2afcface96036` | 88.38 (4 transfers) | 166.92 (5 transfers) |
| `0x8b62111bd342c352daf453ccd0676833c0a31ca1` | 687.51 (3) | 212.62 (1) |
| `0x54acab846901bdbdc553a675d97240511e4bfba2` | 441.88 (2) | 303.31 (1) |
| `0x21032176b43d9f7e9410fb37290a78f4fed6044c` | **10,000.00 (1)** | 44.42 (1) |

Hop 3 and Hop 4 sit on different levels of the same tree: Hop 4 is a child of one of Hop 3's nine tied branches. That both send to the same addresses means the fragmentation observed at earlier hops **is not divergent** — the paths reconverge.

The last row is the clearest case: `0x21032176…044c` received one of the nine 10,000 ETH transfers at Hop 3 — it was a tied branch, not followed — and later receives again via the branch that was followed. Two of the nine branches meet.

**Interpretation.** Repeated convergence between separately-fragmented paths is consistent with common control of the addresses involved, or with independent paths using the same downstream service. — *Confidence: Moderate.*

**Boundary.** Convergence does **not** establish common control. Two unrelated parties depositing at the same exchange produce an identical signature. Distinguishing the two would require information about the receiving addresses that on-chain data does not carry.

### Verification of convergent addresses

Each was checked on Etherscan.

| Address | Label | Funded by | Onward behaviour | Capture |
|---|---|---|---|---|
| `0x8ed8553d…6036` | *(none)* | "Bybit Exploiter 9" | Transfers to Sky: Dai Stablecoin | [`hop4-8ed8553d.png`](../data/screenshots/hop4-8ed8553d.png) |
| `0x8b62111b…1ca1` | *(none)* | `0xF9Fe2410…59127` | **`Deposit With Expiry` → THORChain** | [`hop4-8b62111b-thorchain.png`](../data/screenshots/hop4-8b62111b-thorchain.png) |
| `0x21032176…044c` | **"Bybit Exploiter 46"**, tags `Exploit`, `# Bybit Exploit` | "Bybit Exploiter 5" | Transfers to "Bybit Exploiter 47" | [`hop4-21032176-exploiter46.png`](../data/screenshots/hop4-21032176-exploiter46.png) |
| `0x54acab84…fba2` | *(none)* | "Bybit Exploiter 42" | **`Deposit With Expiry` → THORChain**, repeatedly | [`hop4-54acab84-thorchain.png`](../data/screenshots/hop4-54acab84-thorchain.png) |

**Two of the four deposit into THORChain**, a cross-chain swap protocol. `0x54acab84…fba2` does so systematically — receiving from addresses labelled "Bybit Exploiter 5", "52" and "53" and forwarding to THORChain in amounts of 208.6 to 223.38 ETH.

**Significance.** A cross-chain bridge is the **primary termination condition** under the pre-registered stopping rule, because it severs the link between input and output for open-source analysis: funds enter on Ethereum and leave on a different chain, with no on-chain record connecting the two sides.

The branch selected at this hop does not itself deposit into THORChain. But adjacent branches — reached from the same parent, carrying comparable amounts — do. The observation is recorded here because it bears on where this trail was heading regardless of which branch the rule selected.

**On the labelling.** `0x21032176…044c` carries the label "Bybit Exploiter 46" and is recorded as funding "Bybit Exploiter 47", while Hop 3's destination was "Bybit Exploiter 45". The numbering is sequential across the addresses this trail passes through. This is a third-party attribution by Etherscan and is recorded as such, not as a finding of this analysis.

### Branch selected

`0x327ffe25f330d2d809106ace581099ad1af9ba23` — 454.0611 ETH across 2 transfers.

**Interpretation of the rule applied here.** The pre-registered criterion selects "the branch carrying the highest value". At this hop the two readings diverge:

- **Branch = destination, aggregated:** `0x327ffe25…ba23`, 454.06 ETH across two transfers.
- **Branch = individual transfer:** `0x54acab84…fba2`, 303.31 ETH in one — which deposits into THORChain.

**The aggregated reading is applied**, on the basis that a branch is a path the funds took, and two transfers to one address are one path. This interpretation is recorded because the alternative was available and would have produced a different — and, for this report, a more convenient — outcome: it would have terminated the trace at a bridge, which is a cleaner ending than the one actually reached.

Selecting the reading that produces the better result, after seeing where each leads, is precisely what pre-registration exists to prevent. The interpretation applied is the one that follows from the rule's purpose, not from its consequences here.

**Verification:** `0x327ffe25…ba23` is an externally-owned account, unlabelled, recorded as funded by "Bybit Exploiter 19", receiving from "Bybit Exploiter 45" and "46". Capture: [`hop4-327ffe25.png`](../data/screenshots/hop4-327ffe25.png)

### Branches not followed

57 destinations, carrying 9,608.30 ETH — 95.5% of what left this address. Full list in `data/raw/hop4.csv`.

### Termination check

The selected destination is an account, not a mixer or bridge. Fifth and final hop available under the stopping rule.

---

## Hop 5

**From:** `0x327ffe25f330d2d809106ace581099ad1af9ba23`
**Retrieved:** 2026-08-28 16:50:17 UTC · `data/raw/hop5.csv` · 65 transfers (9 native, 56 token)
**Filter applied:** none.

### Signal separation

Six token groups, **all impersonating** — every one carries a non-ASCII symbol. Native ETH is the only legitimate asset. Two contracts appear here for the first time (`0x47c639ef…d9cd`, `0xa8f41d54…40c7`), indicating the impersonation campaign extends across the address set rather than targeting individual addresses.

### Movement

| Destination | Received (ETH) | Transfers |
|---|---|---|
| `0xf2fa83097ebb54b5204300fd88df7cb1a803276a` | 454.0717 | 2 |
| `0xe75e053856692c390700cb1f09928e1a1c9e2019` | 452.5749 | 2 |
| `0x535c86ef69cd7f7c618409928aff610b7cab7b83` | 444.9700 | 2 |
| `0x5679b4b6ac7968d56972822e4ba9e0e9aa731021` | 238.6969 | 1 |
| `0x9d977674985e1aecd1b5162456e2429ccbce2bbd` | 61.3400 | 1 |
| `0x1743b4e13273ab8e86de51edaef12c5ef2026416` | 0.3000 | 1 |

| | ETH |
|---|---|
| Received from Hop 4 (traced) | 454.0611 |
| Total sent out | 1,651.9535 |
| **Excess over traced inflow** | **+1,197.89** |

### Termination

**Observed.** This address sent 1,651.95 ETH while the traced branch delivered 454.06 ETH to it — **3.6 times more left than arrived by the path under trace**. Its Etherscan record shows inbound transfers from addresses labelled "Bybit Exploiter 45", "46" and "19". The three largest outbound destinations each received almost exactly the amount the traced branch contributed, but from a pool assembled from several inbound paths.

**Interpretation.** This address is a consolidation point. — *Confidence: High.*

**Consequence — and the reason the trace ends here.** ETH is fungible. Once funds from multiple paths are pooled in a single account, no on-chain evidence distinguishes which outbound transfer carries which inbound funds. Continuing to trace from this point would mean following a destination that carries, at most, a 27% probability of containing the funds under trace — and stating otherwise would be an assertion the evidence cannot support.

This is a **limit of the evidence, not of the method**. No amount of additional tracing, tooling, or patience resolves it; the information required does not exist on-chain.

### Termination conditions met

The trace terminates here under two independent conditions:

1. **Hop limit reached.** Five hops from the anchor, the secondary termination criterion of the pre-registered stopping rule.
2. **Traceability dissolved.** Consolidation of multiple inbound paths renders the traced funds indistinguishable from others at this address.

The **primary** termination condition — mixer or bridge entry — was not reached on the followed branch. It was, however, observed on adjacent branches at Hop 4: two of the four convergent addresses deposit systematically into THORChain, a cross-chain bridge. The trail this analysis followed did not itself reach that exit, but paths one step to either side of it did.

---

## Trace summary

| Hop | Address | Received (traced) | Characteristic |
|---|---|---|---|
| Anchor | `0x47666Fab…86E2` | — | 400,001 ETH + derivatives; two handling regimes |
| 1 | `0xa4b2fd68…449e` | 98,376.55 ETH-eq | Derivative consolidation |
| 2 | `0xdd90071d…5f92` | 98,048.79 ETH | Post-conversion; received via DEX swaps |
| 3 | `0xf3025725…72be` | 10,000 ETH | "Bybit Exploiter 45"; 9×10,000 uniform split |
| 4 | `0x327ffe25…ba23` | 454.06 ETH | Dispersion across 58 destinations |
| 5 | *(terminated)* | — | Consolidation point; traceability dissolved |

**Proportion traced.** The followed path carries a progressively smaller share of the funds leaving each address: approximately 19% at Hop 1, 10% at Hop 3, 4.5% at Hop 4. Of the roughly 415,000 ETH-equivalent that left the anchor, this trace follows a path ending in 454 ETH — **around 0.11%**.

This is the stopping rule operating exactly as designed. It is also the single most important boundary on everything this report concludes: **no statement in this analysis about "the funds" applies to more than the specific path documented above.** The remaining 99.89% is not analysed, and nothing here should be read as describing it.

### Structural observations across the trace

Recorded here as observations; classification against catalogued typologies is Phase 04.

1. **Asset conversion.** Liquid-staking derivatives were converted to native ETH within an hour of the anchor's outbound activity, through three separate exchange venues.
2. **Repeated fragmentation.** Value was divided at multiple levels — 40 branches at the anchor, 9 at Hop 3, 58 at Hop 4 — with amounts uniform at some levels and irregular at others.
3. **Delays between stages.** Nine to ten days elapsed between arrival and onward movement at Hops 3 and 4.
4. **Reconvergence.** Separately fragmented paths meet at common addresses, indicating the branching structure is not a tree.
5. **Bridge exposure.** Addresses adjacent to the traced path deposit systematically into a cross-chain bridge.
6. **Persistent contamination.** Impersonating token contracts and lookalike addresses appear at every hop, including contracts first seen only at Hop 5.
