# Phase 04 — Typology Identification

## Objective

Map the movement patterns observed during the trace (Phase 03) to catalogued money-laundering typologies, with sources, distinguishing what the reference framework supports from what is analytical inference.

## Method

Two rules govern this phase, stated in `methodology/analytic-standards.md` §4 and applied throughout:

1. **The pattern is observed before it is named.** Each entry below begins from what the blockchain records, then asks whether that behaviour corresponds to a catalogued typology — never the reverse. Patterns were not sought to fit a pre-selected classification.
2. **Naming a typology is an inference, not a fact.** That funds moved in a certain way is a fact. That the *purpose* was to launder, obscure, or evade is an interpretation, and carries a confidence level and its alternative explanations.

## Reference framework and its limits

The primary reference is:

> **FATF (2020), *Virtual Assets: Red Flag Indicators of Money Laundering and Terrorist Financing***, September 2020.

This document was consulted directly. Where a pattern corresponds to a specific indicator, the section and page are cited so a reader can verify the correspondence in the source rather than trust this report's paraphrase.

**Three of the six patterns below have no direct correspondence in that document.** They are recorded as analytical observations of this study, explicitly labelled as such. This is deliberate: forcing a pattern into a typology it does not match would misrepresent the framework and weaken, not strengthen, the analysis. That two patterns correspond directly and three do not is itself evidence that the classification was driven by the evidence rather than by a wish to find red flags everywhere.

**A note on later FATF material.** The FATF has published subsequent documents (a 12-Month Review in 2020, a ransomware-financing report in 2021, and targeted reports in 2026) that discuss techniques not enumerated in the 2020 Red Flag Indicators. Where relevant, one such technique is noted below with an explicit statement that it does not appear in the 2020 indicator set. The 2020 document remains the single verified base source for this phase; later documents are referenced only where their content was confirmed.

**The framework's own caveat.** The FATF states (§§7–10, pp. 5–6) that the presence of a single indicator is not necessarily sufficient to suspect money laundering, that indicators must be read in context, and that suspicion increases where **multiple indicators appear together without a logical economic or business explanation**. Every entry below is therefore accompanied by the legitimate alternative explanation that the observation alone cannot exclude.

---

## Pattern 1 — Transactional fragmentation

**Observed.** Value was divided into many outbound transfers at three levels of the trace:

| Level | Source | Division | Window |
|---|---|---|---|
| Anchor | 400,000 ETH | 40 × 10,000 ETH (identical) | ~6 minutes |
| Hop 3 (Regime A) | 90,000 ETH | 9 × 10,000 ETH (identical) | ~48 seconds |
| Hop 4 | 10,062 ETH | 74 transfers, irregular amounts (12–303) | ~2h 15m |

**FATF correspondence — direct.** *Red Flag Indicators Related to Transactions*, §11 (*Size and frequency of transactions*), p. 6:

> "Making multiple high-value transactions in short succession, such as within a 24-hour period."

The forty transfers within six minutes and the nine within forty-eight seconds correspond directly to this indicator.

**What is not claimed.** This is **not** structuring in the sense the FATF reserves for that term. Structuring divides value to remain below a reporting or recording threshold. Parcels of 10,000 ETH — tens of millions of dollars each — are not below any threshold; the mechanism the FATF associates with structuring (threshold evasion) is absent, and the term is deliberately not used.

**Analytical observation on the change of mechanism.** The fragmentation at the anchor and Hop 3 is uniform and round (identical 10,000 ETH parcels); at Hop 4 it is irregular. This is a change in the *mechanism* of fragmentation between levels — the more defensible observation, as against characterising the Hop 4 pattern as "organic." Irregular amounts are equally consistent with a second automated distribution rule (proportional calculation, residual balances, batching) as with human activity.

**Interpretation.** The fragmentation is consistent with a function of layering — creating intermediate transactions that increase the difficulty of tracing origin and beneficiary. — *Confidence: Moderate.* Fragmentation is the observed behaviour; layering is a possible function of it, not a synonym for it.

**Legitimate alternative.** Dividing funds across many addresses is routine custody practice: hot/cold wallet separation, per-address security, operational batching, internal balance policies. Fragmentation alone is not an incriminating finding. Its relevance rises only in combination with the other patterns and in the absence of an apparent economic rationale.

---

## Pattern 2 — Conversion of staking derivatives to native ETH

**Observed.** stETH, mETH and cmETH were converted to native ETH through three separate decentralised exchanges, within approximately 50 minutes of the anchor's outbound activity (Phase 03, Hop 2).

**FATF correspondence — direct.** *Red Flag Indicators Related to Transactions*, §12 (*Transactions concerning all users*), p. 9 (lines 305–306):

> "Converting a large amount of fiat currency into VAs, or a large amount of one type of VA into other types of VAs, with no logical business explanation."

The conversion of a large amount of one type of virtual asset (staking derivatives) into another (native ETH) corresponds directly to this indicator.

**Interpretation.** The conversion may serve to consolidate holdings into an asset with no protocol issuer — native ETH cannot be frozen or paused by any party, whereas protocol-issued tokens can, depending on their design, be subject to issuer-level controls. — *Confidence: Low.* This is a hypothesis about motivation. The FATF indicator concerns the conversion itself, not any specific purpose behind it, and the blockchain does not record intent.

**Legitimate alternative — strong.** Conversion to native ETH is a routine prerequisite for almost any subsequent on-chain activity: gas payment, liquidity, and interaction with most services all require native ETH. The conversion is a trivial and common step and does not, by itself, indicate concealment.

---

## Pattern 3 — Dormancy of 9–10 days between stages

**Observed.** Two distinct addresses (Hop 3 and Hop 4 destinations) received funds on 2025-02-21 and remained inactive for approximately nine to ten days before moving them onward — Hop 3's holdings moved on 2025-03-03, Hop 4's on 2025-03-02.

**FATF correspondence — none identified.** The 2020 Red Flag Indicators do not contain an indicator for which a delay between receipt and onward movement is, by itself, a red flag.

§11 (p. 6) mentions a "staggered and regular pattern, with no further transactions recorded during a long period afterwards" — but this was considered and found **not** to match. That indicator describes a pattern of staggered, regular transactions followed by silence; the observation here is the opposite shape: complete dormancy followed by a burst of activity. The §11 text was read and judged inapplicable rather than stretched to fit.

**Treatment.** Recorded as an analytical observation of this study, not as a FATF red flag.

**Interpretation.** The near-simultaneous dormancy of two separate addresses over the same window is the notable feature — it is more consistent with coordinated handling than with coincidence. — *Confidence: Low.* Simultaneity is suggestive; it is not conclusive of common control.

**Legitimate alternatives.** Waiting for liquidity, waiting for market conditions, operational availability, and custody-management schedules all produce dormancy of this kind.

---

## Pattern 4 — Reconvergence of separated paths

**Observed.** Paths that were separately fragmented at earlier hops send to common addresses. Four addresses receive from both Hop 3 and Hop 4, and one of them (`0x21032176…044c`) received one of the nine tied 10,000 ETH branches at Hop 3 and later received again via the followed branch (Phase 03, "Finding: convergence between branches").

**FATF correspondence — none identified.** The 2020 document addresses multiple accounts, multiple virtual assets, multiple VASPs, and unusual transaction patterns, but contains no specific indicator for funds that separate and later reconverge.

**Treatment.** Recorded as a structural observation of this study.

**Interpretation.** Fragmentation followed by reconvergence is consistent with the dispersion having functioned as an intermediate transit stage rather than as final distribution — the branching structure is not a tree, which suggests the division was of routing, not of destination. — *Confidence: Low.*

**Legitimate alternative — strong.** Two independent paths using the same downstream service (an exchange, a bridge) produce identical reconvergence. In that case the reconvergence is a consequence of the service's architecture, not of any coordination between the paths. This alternative cannot be excluded with on-chain data alone.

---

## Pattern 5 — Cross-chain movement (THORChain)

**Observed.** Addresses adjacent to the traced path deposit systematically into THORChain, a cross-chain swap protocol. Two of the four convergent addresses at Hop 4 do so; one (`0x54acab84…fba2`) repeatedly, in amounts of 208–223 ETH, receiving from addresses labelled "Bybit Exploiter 5", "52" and "53" (Phase 03, Hop 4 verification).

**FATF correspondence — not a 2020 indicator; discussed in later FATF material.** This is the correction that direct verification produced, and it is stated precisely because the distinction demonstrates rigour:

Cross-chain movement / chain-hopping **does not appear as one of the enumerated indicators** in the 2020 Red Flag Indicators document. Writing "FATF 2020 red flag: chain-hopping" would be incorrect.

It is, however, discussed in other FATF material as a technique that increases transaction anonymity and impedes tracing — the 2020 *12-Month Review of the Revised FATF Standards on Virtual Assets/VASPs* lists chain-hopping among such techniques, and the 2021 *Countering Ransomware Financing* report defines it explicitly as moving from one VA to another blockchain, often in rapid succession, to evade attempts to trace the movements.

**Formulation used:**

> The observed behaviour is consistent with chain-hopping, a technique discussed by the FATF in documents subsequent to the 2020 Red Flag Indicators, but it does not constitute one of the specific indicators enumerated in that 2020 report.

**Significance for the trace.** A cross-chain bridge is the primary termination condition of this investigation's stopping rule, precisely because it severs the on-chain link between input and output for open-source analysis (Phase 00, §4). Funds enter on Ethereum and leave on another chain with no on-chain record connecting the two sides.

**Legitimate alternative.** Bridges and cross-chain swaps have entirely legitimate uses; interoperability is a normal feature of the ecosystem, used by millions. Use of THORChain is not, by itself, evidence of laundering. Its weight here depends on its combination with the other patterns.

---

## Pattern 6 — Token impersonation and address poisoning

**Observed.** Impersonating token contracts (non-ASCII homoglyph symbols and clean-ASCII forgeries) and lookalike destination addresses appear at every hop of the trace, including contracts first seen only at Hop 5 (Phase 02 "Finding"; Phase 03 "Finding: address poisoning at scale").

**FATF correspondence — none, and none should be forced.** No indicator in the 2020 Red Flag Indicators describes address poisoning or token impersonation, and this phenomenon should not be reclassified as laundering to fit the framework.

The distinction is categorical:

- **Laundering** concerns the *movement and transformation of value*.
- **Impersonation and address poisoning** concern the *manipulation of the informational environment* — inducing error, confusing attribution, and degrading analysis.

These are different activities. One moves money; the other attacks the analyst.

**Treatment.** Recorded under a category of its own — **on-chain analytical obstruction** — with the explicit statement that no direct correspondence was identified in the FATF framework consulted.

**Interpretation.** The techniques observed are consistent with deliberate contamination of the transaction record to impede tracing. — *Confidence: Moderate* as to the effect; the impersonation and poisoning are established facts, and their effect of impeding analysis is demonstrable (Phase 03 documents the specific trap they created).

**Boundary on attribution — critical.** The identity of whoever deployed these contracts and generated these lookalike addresses is **not established**. The perpetrator may be the actor moving the funds, a third party, an opportunistic scammer, or an automated agent targeting notable addresses generically. The phenomenon is observable; its authorship is not attributable with the available data. No attribution is made.

---

## Summary

| # | Pattern | FATF 2020 correspondence | Treatment |
|---|---|---|---|
| 1 | Transactional fragmentation | §11, p. 6 — multiple high-value transactions in short succession | **Direct** red flag |
| 2 | Derivatives → native ETH | §12, p. 9 — conversion between VAs without logical business explanation | **Direct** red flag |
| 3 | Dormancy 9–10 days | None (§11 considered and found inapplicable) | Analytical observation |
| 4 | Reconvergence | None | Structural observation |
| 5 | Cross-chain (THORChain) | Not in 2020 indicators; discussed in later FATF material | Consistent with chain-hopping; not a 2020 red flag |
| 6 | Impersonation / poisoning | None | Own category: on-chain analytical obstruction |

**The pattern that matters is the combination.** The FATF is explicit that no single indicator determines illicit activity; relevance arises when multiple indicators appear together without a logical economic or business explanation (§§7–10). The chain observed here — large holdings, immediate high-value fragmentation, conversion of derivatives to unfreezable native ETH, multi-level fragmentation with a changing mechanism, dormancy, reconvergence, and eventual approach to a cross-chain bridge — presents several such indicators in sequence. This is recorded as a description of the aggregate pattern, at moderate confidence, and not as a determination of illicit activity, which the evidence available to this analysis cannot establish.

Each legitimate alternative above remains on the record. What this analysis establishes is the shape of the fund movement and its correspondence, where it exists, to catalogued typologies — not the intent behind it, and not the identity of any actor.
