# Phase 06 — Cross-Validation

## Objective

Compare the independent findings of Phases 03–05 — now frozen — against published third-party analyses of the incident, and account for both convergence and divergence.

**The findings are not revised in this phase.** They were committed to version control before any published analysis was read (`collection-log.md`, sequence-integrity declaration). Revising them now would destroy the measurement this comparison exists to produce: how far an open-source analyst reaches independently, and where that reach ends relative to parties with proprietary tools.

The purpose is not to check whether the trace was "right." It is to locate, by contrast with published work, the boundary between what open-source analysis established and what required capabilities this investigation did not have.

---

## Sources consulted

All read after Phase 05 was frozen and committed. Recorded in `collection-log.md` as Phase 06 sessions.

| # | Source | Author / date | Type | Admiralty grading |
|---|---|---|---|---|
| S1 | SlowMist on-chain analysis (read via PANews republication) | SlowMist Security Team, 2025-02-23 | On-chain fund tracing via MistTrack (proprietary) | **B2** — specialist firm; read via republication rather than the original, and its labels are proprietary attributions |
| S2 | "In-Depth Technical Analysis of the Bybit Hack" | NCC Group — Rivas, Santos & Sanz, 2025-03-10 | Off-chain / smart-contract attack analysis | **A2** — named authors, primary technical detail (malicious JavaScript, contract addresses) independently checkable on-chain |
| S3 | FBI public service announcement, reported by Associated Press | AP — Gambrell, 2025-02-27 | Actor attribution | **A1** for the fact of the FBI statement; the attribution itself is the FBI's, not this analysis's |

**On grading S1 at B2.** SlowMist is a competent specialist firm and the analysis is detailed. It is rated B rather than A because it was read via a republication (PANews) rather than the primary SlowMist publication, and because its tracing relies on MistTrack, a proprietary tool whose cross-chain heuristics cannot be independently verified from public data. This is not a criticism of the source — it is the same standard applied to every source in this investigation: what cannot be verified at first hand is graded accordingly.

---

## Convergence

The SlowMist analysis (S1) traces the same initial path this investigation reconstructed. The correspondence is transfer-by-transfer.

| Element | SlowMist (S1), published 2025-02-23 | This analysis (frozen Phase 05) | Result |
|---|---|---|---|
| Anchor address | `0x47666Fab…86E2` | `0x47666Fab…86E2` | ✅ identical |
| Stolen composition | 401,347 ETH · 90,375.5479 stETH · 8,000 mETH · 15,000 cmETH | 400,001 ETH-eq observed leaving anchor; stETH 90,375.55, mETH 8,000, cmETH 15,000 | ✅ identical to the fourth decimal on stETH |
| Anchor fragmentation | 400,000 ETH → 40 addresses, 10,000 ETH each | 40 × 10,000 ETH (Hop 1) | ✅ identical |
| Derivative destination | 8,000 mETH + 90,375.5479 stETH → `0xA4B2Fd68…449e` | Same, `0xa4b2fd68…449e` (Hop 1 → Hop 2) | ✅ identical |
| Conversion venue | Converted to 98,048 ETH via **Uniswap and ParaSwap** | Converted via Uniswap V3, DODO, and a contract labelled "Velora" (Hop 2) | ✅ same — "Velora" is ParaSwap's current name |
| Post-conversion destination | → `0xdd90071d…5f92` | → `0xdd90071d…5f92` (Hop 2) | ✅ identical |
| Second fragmentation | `0xdd9` → 9 addresses, 10,000 ETH each | 9 × 10,000 ETH (Hop 3) | ✅ identical |
| cmETH path | 15,000 cmETH → `0x1542368a…4443` | Recorded as unfollowed branch at Hop 1, destination `0x1542368a…4443` | ✅ identical |

**This investigation independently reconstructed the SlowMist trail through Hop 3, using only a public block explorer, without having read the SlowMist analysis.** Every address, every amount, and every structural feature — the 40-way split, the derivative consolidation, the DEX conversion, the 9-way split — matches.

Two points of independent corroboration deserve note:

**The "Velora" identification.** At Hop 2 this analysis verified a conversion contract on Etherscan, found it labelled "Velora: Deployer 1", and classified it by behaviour as a DEX aggregator. SlowMist names the venue ParaSwap. Velora is ParaSwap's rebranded name. The two arrived at the same protocol — this analysis by verifying behaviour rather than trusting the label, which is the method the investigation set out to apply.

**The stETH amount.** The stETH figure (90,375.5479) matches to four decimal places between an independent public-explorer trace and a specialist firm's proprietary-tool analysis. A match at that precision is not coincidence; it confirms both were reading the same on-chain events.

---

## Divergence — and the boundary it locates

The published sources continue past the point where this investigation stopped. This is the central result of the comparison, and it is not a shortfall.

**Where this analysis stopped.** The trace terminated at Hop 5 for two reasons (Phase 05): traceability dissolution at a consolidation point, and — on branches adjacent to the followed path — deposits into THORChain, a cross-chain bridge. A bridge severs the on-chain link between input and output for Ethereum-only analysis: funds enter on one chain and leave on another, with no on-chain record joining the two sides.

**Where the sources went.** SlowMist (S1) reports: *"205 ETH was exchanged for BTC through Chainflip and transferred across the chain to the address bc1qlu4a33zjspefa3tnq566xszcr0fvwz05ewhqfq."* The FBI, via AP (S3), states the actors *"have converted some of the stolen assets to Bitcoin and other virtual assets dispersed across thousands of addresses on multiple blockchains."*

**The comparison locates the boundary exactly:**

| Capability | This analysis | SlowMist (S1) | FBI (S3) |
|---|---|---|---|
| Ethereum on-chain tracing | ✅ | ✅ | ✅ |
| Cross-chain (ETH → BTC) tracing | ❌ stops at the bridge | ✅ via MistTrack proprietary heuristics | ✅ |
| Attribution to a named actor | ❌ by design | Inferred, corroborated with prior-incident clustering | ✅ via off-chain intelligence and subpoena power |

The divergence is not error. Open-source analysis and MistTrack agree completely on the Ethereum-native path. They part precisely at the cross-chain boundary — where MistTrack's proprietary cross-chain heuristics continue and a public explorer cannot follow. **This is the private-attribution boundary the investigation set out to find, measured against the specific tool that crosses it.**

---

## What the sources revealed about frozen findings

Two findings recorded at low or moderate confidence in Phase 05 are addressed by the sources. **These are not revisions** — the frozen findings stand as written. They are recorded here as the outcome of comparison.

**The cmETH branch (confirms I7).** This analysis recorded the 15,000 cmETH transfer as an unfollowed branch (Hop 1) and, separately, hypothesised at *Low* confidence (I7) that conversion to native ETH may have served to reach an asset with no issuer-level freeze. SlowMist reports that **mETH Protocol suspended cmETH withdrawals and recovered the 15,000 cmETH from the hacker's address**. This is direct evidence for the mechanism behind I7: an issuer *can* freeze and reclaim a protocol asset, and here one did. The branch this analysis did not follow terminated by issuer intervention. The inference I7 is corroborated — though it remains an inference about motivation, not a proven purpose.

**Actor attribution (confirms the decision not to attribute).** Phase 05 recorded the "Bybit Exploiter" labels strictly as third-party attributions (A1–A3) and made no attribution of its own. SlowMist and the FBI attribute the incident to the Lazarus Group / TraderTraitor — SlowMist via wallet-cluster correlation with the BingX and Phemex hacker addresses and ZachXBT's evidence (test transactions, associated wallets, timing analysis); the FBI via its own intelligence. **This vindicates the reliability discipline, not the attribution.** These parties reached attribution through evidence this investigation explicitly did not have — cross-incident clustering databases, off-chain intelligence, subpoena power. That this analysis stopped short of attribution was correct: it lacked the basis to make one, and said so.

---

## Coverage assessment

| Metric | Result |
|---|---|
| Hops independently reconstructed | 5 |
| Of which corroborated by published analysis | Hops 1–3 correspond transfer-for-transfer to SlowMist; Hops 4–5 continue along the same address cluster |
| Point of departure from published analysis | The Ethereum → Bitcoin cross-chain boundary |
| Reason for departure | Cross-chain tracing requires proprietary heuristics (MistTrack) or off-chain powers (FBI); a public block explorer cannot follow value across a bridge |
| Proportion of total incident traced | A single path ending in 454 ETH, ~0.11% of the funds leaving the anchor (Phase 03) |

**What the comparison establishes.** On the Ethereum-native segment of the trail, where the path is linear and the data is public, open-source analysis with a free block explorer reproduced a specialist firm's proprietary-tool findings exactly. The two diverge only at the cross-chain boundary, and only because crossing it requires capabilities — proprietary cross-chain attribution, or legal process — that are by definition unavailable to open-source analysis.

This is a precise answer to the investigation's stated question (Phase 00, §1): *how far can an open-source analyst trace, and where does the method stop working.* The method works completely up to the bridge, and stops at it. The boundary is not a limit of skill, tooling effort, or diligence; it is the point at which the required information ceases to exist on the public Ethereum ledger.

---

## A note on the scope of this validation

The convergence demonstrated here covers the **single path this investigation followed** — roughly 0.11% of the stolen funds. It does not validate any claim about the other 99.9%, which this analysis never examined. SlowMist, the FBI, and subsequent researchers traced the incident at a scale and across a set of chains that this investigation deliberately did not attempt.

What is validated is narrow and specific: that the method applied here — public-explorer tracing, contract verification by behaviour, fact/inference/attribution discipline — produces, on the segment it can reach, results identical to those of a specialist firm using paid tools. That is the claim this project set out to test, and the comparison supports it.
