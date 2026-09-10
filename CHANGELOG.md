# Changelog

All notable changes to this investigation's documentation are recorded here.

Investigative deliverables are versioned rather than silently edited: once a version is issued, subsequent changes are published as a new version with the modifications stated explicitly. This preserves the auditability of the documentation itself.

**A note on version control and sequence.** The investigation's central claim — that the findings were reached independently, before any published analysis was read — is evidenced by the `retrieved_utc` timestamps embedded in the raw data (`data/raw/*.csv`), which fix the independent-collection window at 2026-08-26 to 08-28. The repository was initialized after the investigation was conducted, so its commit history reflects publication dates rather than the order in which each phase was produced, and is not relied upon as evidence of sequence. This changelog records what each stage added; the raw-data timestamps, not the commit log, are the auditable record of ordering. See the sequence integrity declaration in `collection-log.md`.

---

## [1.0] — 2026-09-04

Investigation complete. Consolidated report issued.

### Added — Phase 07

- **`phase07-report/BIC-2026-001-blockchain-investigation-report.pdf`** — consolidated report, 34 pages across 16 sections, synthesising Phases 00–06.
- `phase07-report/README.md` — mapping each report section to its source phase, and the publication constraints observed.
- Rewritten root `README.md` for the completed investigation.

### Added — Phase 06 (cross-validation)

- Comparison against three published sources, **read only after the Phase 05 findings were finalized**.
- Convergence recorded transfer-for-transfer through Hops 1–3 against a specialist firm's published analysis.
- Divergence located at the Ethereum → Bitcoin cross-chain boundary, identifying the limit of open-source capability.
- Two frozen findings addressed by the sources and recorded as outcomes of comparison — **not** as revisions.

### Added — Phase 05 (reliability)

- Claim register: 10 facts, 8 inferences with confidence levels, 3 third-party attributions recorded but not adopted.
- The private attribution boundary documented in its two forms: traceability dissolution through consolidation, and cross-chain bridge exposure.
- **Findings finalized at this point (2026-08-28).** Nothing in Phases 03–05 was altered after the Phase 06 sources were read.

### Added — Phase 04 (typologies)

- Correspondence of six observed patterns against the FATF 2020 Red Flag Indicators, consulted at source with section and page cited.
- Two direct correspondences (§11 p. 6; §12 p. 9). **Four patterns recorded as having no correspondence** rather than forced into a classification.
- Cross-chain movement recorded with the explicit correction that it is *not* among the 2020 enumerated indicators, though discussed in later FATF material.
- On-chain analytical obstruction recorded as a category of this study's own, with the absence of any framework correspondence stated.

### Added — Phase 03 (trace)

- Five hops documented with transaction hashes, and every unfollowed branch recorded with its address and value.
- Raw retrieval data for each hop (`data/raw/hop1–5.csv`), unfiltered at collection.
- Destination verification captures for nine addresses (`data/screenshots/`).
- Finding: address poisoning at scale — 31 lookalike addresses matching legitimate destinations in their first six and last four characters.
- Finding: convergence between separately-fragmented branches.
- The Hop 4 interpretive choice disclosed: two readings of the branch-selection rule were available, and the one applied produced a *less* convenient outcome than the alternative.

### Added — Phase 02 (anchor)

- Anchor identified with a three-level provenance chain, including the F6-graded pointer that was used for navigation and never relied upon.
- Anchor validated by on-chain behaviour rather than accepted on its explorer label.
- Finding: token symbol impersonation — nine contracts using non-Latin homoglyphs, and one named after the incident sent to the queried address itself.

### Added — Phase 01 (environment)

- Isolated analysis environment and egress verification, including a silent VPN failure detected only by direct inspection of the routing table.
- Retrieval tooling validated against a known address.

### Added — Phase 00 (scope and methodology)

- **Stopping rule pre-registered before any transaction data was examined**, with branch selection, tie-breaking, and termination criteria.
- Threat model and operational security posture, including controls considered and rejected.
- Analytic standards: fact / inference / attribution taxonomy and confidence levels.

### Changed during the investigation

- **Tie-breaking criterion added** to the pre-registered stopping rule after anchor validation revealed forty branches of identical value, and **before any hop was traced**. Recorded as an addition in the revision log of `methodology/scope-and-limitations.md` rather than applied as a silent edit.

### Tooling

`tools/trace_helper.py` was extended during the investigation in response to what the data revealed. Each change and its cause is recorded in `tools/README.md`:

1. Initial version — native transfers only.
2. **Migrated to Etherscan API V2** after the V1 endpoint returned a deprecation error on first use.
3. **Token transfer retrieval added** after an address showed 48 outbound transactions totalling 0.16 ETH, almost all zero-value — the script had been reading half of what was there.
4. **Token impersonation detection added** after retrieval returned eight apparent assets whose symbols rendered identically in the terminal.
