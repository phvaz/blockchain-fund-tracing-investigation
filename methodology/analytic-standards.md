# Analytic Standards

> **Status:** Pre-registered. Defined before any transaction data was examined.

---

## Purpose

A blockchain ledger produces an unusual evidentiary situation: the raw data is **more reliable than in almost any other forensic domain** — immutable, timestamped, independently verifiable by any party — while the conclusions drawn from it are often **weaker than they appear**, because the link between an address and a controlling entity is almost never directly observable.

This creates a specific failure mode: an analyst presents a well-supported fact and an unsupported attribution in the same sentence, in the same tone, and the reader cannot tell them apart.

The standards below exist to prevent that.

---

## 1. Claim typing

Every claim in this investigation is assigned one of three types. The type is stated explicitly wherever the claim appears.

### Fact

A record that exists on the ledger and can be verified independently by any third party.

- *Basis:* the blockchain itself
- *Falsifiable:* yes — anyone can check
- *Example:* `Address 0xA transferred 500 ETH to address 0xB in transaction 0x… at 2025-02-XX 14:31:07 UTC.`

### Inference

An analytical conclusion drawn from observed facts by applying a stated heuristic. It may be well supported and still be wrong.

- *Basis:* reasoning over facts
- *Requirement:* the heuristic must be stated, so a reader can evaluate and challenge it
- *Example:* `Addresses 0xB and 0xC are likely under common control, on the basis that both forwarded identical values to 0xD within a four-minute window and neither has any other transaction history.`

Every inference carries an explicit confidence level (Section 2).

### Attribution

A claim linking an address to a named real-world actor — an individual, organization, or state.

- *Basis:* requires evidence outside the ledger — exchange KYC records, off-chain intelligence, legal process
- **This investigation asserts no attribution.**
- Where published sources attribute activity, it is reported as: `[Source] attributes this activity to [actor].` — never as `this address belongs to [actor].`

---

## 2. Confidence levels for inferences

Adapted from ICD 203 analytic tradecraft standards.

| Level | Meaning |
|---|---|
| **High** | The conclusion follows directly from observed data. Alternative explanations exist in principle but are not credible given the evidence. |
| **Moderate** | Well supported, but dependent on a heuristic that can fail. Alternative explanations exist and are less likely, but not implausible. |
| **Low** | Consistent with the observed data, but the evidential basis is thin or competing explanations are approximately as viable. Recorded for completeness; not relied upon in any conclusion. |

An inference rated **Low** may appear in the findings. It may not appear in the conclusions.

---

## 3. Finding structure

Every finding is written in three parts, in this order, so that observation and interpretation are never merged:

> **Observed:** *[what the ledger records — fact]*
> **Interpretation:** *[what it suggests, by what reasoning — inference, with confidence level]*
> **Boundary:** *[what this does not establish]*

The third element is not optional. A finding that does not state its own limit invites the reader to over-read it.

---

## 4. Typology classification

Observed movement patterns are mapped to catalogued laundering typologies, primarily the **FATF Virtual Assets Red Flag Indicators**.

Two rules govern this:

1. **The pattern is observed before it is named.** The sequence is: document what the transactions show → identify the pattern → look up whether it is a catalogued typology → cite the source. Not: expect a typology and look for evidence of it.
2. **Naming a typology is an inference, not a fact.** That funds passed through a service is a fact. That the purpose was layering is an interpretation, and is rated accordingly.

Typologies identified during this investigation are documented with their source in `phase04-typologies/`, including where the classification is uncertain.

---

## 5. Source grading

Where third-party sources are consulted — the anchor point (Phase 02) and published analyses (Phase 06) — each is graded under the **Admiralty Code** (NATO STANAG 2511): a letter for source reliability (A–F) and a numeral for information credibility (1–6).

On-chain data itself is not graded on this scale. It is not a *source* in the intelligence sense; it is the primary record.

---

## 6. Sequence integrity

Published analyses of this incident exist and are readily available. They are **not consulted during Phases 02–05**.

Only the anchor address is sourced externally, and `collection-log.md` documents precisely what was read, when, and from where. Cross-validation occurs in Phase 06, after all findings are finalized and recorded.

The reason is that an analyst who reads the answer first does not investigate — they search for confirmation, and cannot afterwards distinguish what they found from what they were looking for. Preserving the separation is what makes the Phase 06 comparison meaningful: it measures independent reach rather than reading comprehension.

Divergence from published analyses is an expected and informative outcome, not an error to be corrected.
