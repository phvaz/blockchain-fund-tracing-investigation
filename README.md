# Blockchain Investigation Case Study — Public Trail Analysis of the Bybit 2025 Incident

> **Case reference:** BIC-2026-001
> **Status:** In progress
> **Classification:** Academic portfolio — open-source investigation

A methodological case study in blockchain fund-flow analysis. This investigation reconstructs a **single, delimited trail** of funds associated with the publicly reported Bybit incident of February 2025, using exclusively open-source tooling, and measures how far an independent analyst can get before hitting the limits of publicly available attribution data.

The purpose is **not** to identify perpetrators, expose undocumented infrastructure, or replicate the work of commercial intelligence firms. It is to demonstrate investigative methodology under realistic constraints — and to document precisely where those constraints begin.

---

## Overview

| Field | Value |
|---|---|
| Case reference | BIC-2026-001 |
| Analyst | Paulo Vaz |
| Subject | One delimited fund trail from a publicly reported incident |
| Method | Open-source blockchain analysis (block explorers, public APIs) |
| Anchor point | `[TO FILL — sourced from public disclosure, see collection-log.md]` |
| Stopping rule | `[TO FILL — pre-registered before analysis began]` |
| Analytic standards | Fact / Inference / Attribution taxonomy · ICD 203 confidence levels · FATF Virtual Asset red-flag typologies |
| Tooling | `[TO FILL]` |
| Report | `[link to final report]` |

---

## Why this project exists

My previous four portfolio projects cover host and network forensics — disk imaging, memory analysis, filesystem artifacts, packet capture. All of them investigate a *machine*.

This one investigates *money*. The evidence is a public, immutable ledger rather than a seized device; the adversary is not trying to delete artifacts but to make a trail computationally expensive to follow; and the analytical limit is not tool capability but access to proprietary attribution data.

The methodological discipline carries over. The domain does not.

---

## Methodological commitments

Three rules were fixed **before** any data was examined. They are recorded here because a rule declared afterwards is a rationalization, not a method.

### 1. Independent analysis precedes comparison

Published analyses of this incident exist. They were **not** consulted during the investigative phases. Only the anchor address — a matter of public record — was sourced externally, and the collection log documents exactly what was read and when.

Cross-validation against published analyses occurs in Phase 06, after all findings were finalized. This preserves the ability to measure what an independent analyst reaches unaided, rather than confirming a conclusion already known.

### 2. The stopping rule was pre-registered

`[TO FILL — e.g. "Follow the highest-value branch at each fragmentation, to a maximum of N hops from the anchor, or until funds enter a mixing service or cross-chain bridge, whichever occurs first."]`

Where the rule was modified mid-analysis, the modification and its justification are documented rather than applied silently.

### 3. Every claim is typed

| Type | Definition | Evidentiary basis |
|---|---|---|
| **Fact** | Recorded on-chain and independently verifiable by any party | The ledger itself — immutable |
| **Inference** | An analytical conclusion drawn from observed facts using a stated heuristic | Reasoning, which may be wrong |
| **Attribution** | Linking an address to a named real-world actor | Requires evidence beyond the scope of open-source analysis |

**No attribution is asserted in this report.** Where published sources attribute activity to a specific actor, that attribution is reported as a third-party claim, not as a finding of this analysis.

---

## Operational security

Investigating a trail associated with a state-linked threat actor carries a consideration absent from ordinary lab work: the researcher may become a target of interest. The actor group associated with this incident has a documented history of campaigns aimed at security researchers — false recruiter profiles, malicious "collaboration" repositories, and weaponized datasets offered for analysis.

The measures adopted, and the reasoning behind each, are documented in [`methodology/opsec.md`](methodology/opsec.md). They are deliberately proportionate: this analysis reads a public ledger and executes nothing.

The most important control is behavioral rather than technical, and applies indefinitely after publication: **unsolicited offers of collaboration, datasets, tooling, or opportunity are treated as hostile until proven otherwise.**

---

## Investigation phases

| Phase | Focus | Status |
|---|---|---|
| [00 — Scope, OpSec & Methodology](phase00-scope-and-opsec/) | Scope boundaries, stopping rule, security posture, analytic standards | `[ ]` |
| [01 — Environment Preparation](phase01-environment/) | Isolated analysis environment and tooling verification | `[ ]` |
| [02 — Anchor Point Identification](phase02-anchor/) | Sourcing the starting address with documented provenance | `[ ]` |
| [03 — Independent Trace](phase03-trace/) | Hop-by-hop reconstruction within the stopping rule | `[ ]` |
| [04 — Typology Identification](phase04-typologies/) | Observed laundering patterns mapped to catalogued typologies | `[ ]` |
| [05 — Reliability Assessment](phase05-reliability/) | Fact/inference/attribution classification and confidence levels | `[ ]` |
| [06 — Cross-Validation](phase06-validation/) | Comparison against published analyses | `[ ]` |
| [07 — Consolidated Report](phase07-report/) | Formal investigation report | `[ ]` |

---

## Key findings

`[TO FILL — after Phase 05]`

Each finding will state: the observation (fact), the interpretation (inference, with its heuristic and confidence level), and the boundary beyond which the evidence does not support further conclusion.

---

## Limitations

`[TO FILL — after Phase 06, each with its concrete impact on specific conclusions]`

Two are known in advance and are structural rather than incidental:

- **The private attribution wall.** Commercial intelligence platforms maintain proprietary databases of labelled addresses. An address that is anonymous to open-source analysis may already be identified in those datasets. Where this analysis reaches that boundary, it is documented as a finding in its own right — the point at which open tooling ceases to be sufficient.
- **Scale without automation.** Fragmentation across many addresses is deliberately designed to make manual tracing impractical. The stopping rule and any automation used are documented so a reader can distinguish an analytical boundary from an endurance one.

---

## Standards & frameworks

| Framework | Application |
|---|---|
| FATF — Virtual Assets Red Flag Indicators | Typology classification of observed movement patterns |
| ICD 203 — Analytic Standards | Separation of observed data from analytic judgment; expressed confidence levels |
| ISO/IEC 27043 | Investigation process — scope definition and structured methodology |
| Admiralty Code (NATO STANAG 2511) | Source grading where third-party sources are consulted (Phase 06) |

---

## Legal and ethical position

All data examined is public by design. Blockchain ledgers are open records; reading them constitutes no unauthorized access to any system. No wallet was connected, no contract was interacted with, and no query was directed at private infrastructure.

This is an educational case study. It does not constitute a legal instrument, an accusation, or an intelligence product. No natural person is named or implicated.

Where analysis surfaced anything not already present in public reporting, it is **not published here** — such material was withheld and reviewed privately before any decision on disclosure.

---

## Repository structure

```
├── README.md
├── CHANGELOG.md
├── collection-log.md          # provenance: every source, query, and timestamp
├── methodology/
│   ├── scope-and-limitations.md
│   ├── opsec.md
│   └── analytic-standards.md
├── phase00-scope-and-opsec/
├── phase01-environment/
├── phase02-anchor/
├── phase03-trace/
├── phase04-typologies/
├── phase05-reliability/
├── phase06-validation/
├── phase07-report/
├── tools/                     # analysis scripts
└── data/
    ├── raw/
    └── graphs/
```

---

## Analyst

**Paulo Vaz** — Digital forensics and financial crime investigation
`[GitHub]` · `[LinkedIn]`

Conducted under the mentorship of Arlete Figueiredo Muoio (Aissa Tecnologia da Informação), whose guidance shaped the scope boundaries, operational security posture, and analytical discipline applied throughout.
