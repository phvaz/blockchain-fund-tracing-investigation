# Operational Security Posture

> **Status:** Pre-registered. Defined before any research activity began.

---

## Why this document exists

Most laboratory forensics work carries no risk to the examiner. This project is different in one specific respect: the incident under study has been publicly attributed to a state-linked threat actor with a **documented history of targeting security researchers**.

The recorded pattern is not retaliation against investigators. It is opportunistic compromise of a demographic: false recruiter profiles on professional networks, fabricated collaboration offers, malicious repositories presented as tooling, and weaponized datasets offered for analysis. The target profile is a security professional who is visibly active and open to opportunity.

That profile describes the analyst conducting this investigation. Publishing work on this subject increases visibility within that demographic.

The measures below are therefore **proportionate to a realistic threat model, not to a dramatic one**. This analysis reads a public ledger and executes nothing. The controls reflect that.

---

## Threat model

| Vector | Assessed likelihood | Rationale |
|---|---|---|
| Targeted attack against this analyst in retaliation for this analysis | **Very low** | The trail examined is already documented publicly by multiple commercial intelligence firms. This work reveals nothing new and presents no operational threat to any actor. |
| Opportunistic social-engineering approach following publication | **Plausible** | Consistent with documented campaigns against security researchers. Not specific to this project — the analyst already fits the target profile — but publication increases visibility. |
| Passive network correlation from analysis queries | **Low** | Mitigated by the controls below; queries are directed at public explorer services, not at infrastructure under adversary control. |
| Compromise via on-chain interaction | **Eliminated by design** | No wallet is connected and no transaction is broadcast at any point. There is no interactive surface. |

---

## Controls adopted

### Technical

| Control | Implementation | Purpose |
|---|---|---|
| **Isolated analysis environment** | All research conducted from a dedicated VirtualBox VM, snapshotted clean before first use | Separates research activity from the primary working system |
| **Network egress control** | VPN active for all analysis sessions | Prevents association of query activity with the analyst's residential address |
| **Disposable credentials** | Burner email address, created within the isolated environment, used for all analysis-tool accounts | Prevents linkage between tooling accounts and the analyst's primary identity |
| **Read-only posture** | No wallet connected; no contract interaction; no transaction broadcast | Eliminates the interactive attack surface entirely, including address-poisoning and dusting vectors |

### Behavioral

These controls carry no technical cost and represent the most significant risk reduction available.

- **No execution of third-party code or files.** Repositories, scripts, datasets, and documents received from unverified sources are not executed, opened, or imported — in any environment. This applies to material offered as collaboration, employment assessment, research data, or tooling.
- **Unsolicited professional approaches are treated as untrusted.** Following publication, contact offering opportunity, collaboration, datasets, or tooling is treated as hostile until independently verified through a channel not controlled by the approaching party.
- **Multi-factor authentication** maintained on all primary accounts.
- **This posture does not expire.** Publication increases exposure indefinitely, not temporarily.

---

## What was deliberately not adopted, and why

Documenting the controls that were considered and rejected is part of an honest threat model. Security theatre is not security.

| Considered | Adopted? | Reasoning |
|---|---|---|
| Routing all traffic over Tor | **No** | VPN egress control is sufficient for the actual requirement (non-attribution of query origin). Many explorer services degrade or block Tor exit nodes, and the marginal benefit does not justify the operational cost for read-only public-ledger queries. |
| Non-persistent / amnesiac VM | **No** | Appropriate for malware analysis, where untrusted code is executed. This investigation executes nothing; a standard isolated VM with a clean snapshot meets the requirement. |
| Dedicated physical hardware | **No** | Disproportionate to a read-only analysis of public data. |
| Anonymous publication | **No** | Would defeat the professional purpose of the work. Attribution of authorship is accepted as a deliberate trade-off, which is precisely why the behavioral controls above are treated as permanent. |

---

## Scope of this posture

These controls govern the conduct of this investigation and the analyst's exposure following publication. They are documented here as part of the methodology because **an analyst who investigates a sophisticated threat actor without modelling their own exposure has completed only half the analysis.**
