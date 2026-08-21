# Phase 01 — Environment Preparation

**Status:** `[ ] Not started  [ ] In progress  [ ] Complete`

## Objective

Establish an isolated analysis environment consistent with the OpSec posture defined in Phase 00, and verify tool availability before analysis begins.

## Environment

| Component | Configuration | Verified |
|---|---|---|
| Analysis VM | `[OS, version, resources]` | `[ ]` |
| Clean snapshot | `[snapshot name, date]` | `[ ]` |
| VPN egress | `[provider, exit region]` | `[ ]` |
| Burner identity | `[provider — do not record the address itself]` | `[ ]` |
| Python environment | `[version, packages]` | `[ ]` |

## Tool verification

Record what is actually available at time of analysis, not what is assumed.

| Tool | Role | Free tier available | Notes |
|---|---|---|---|
| `[Block explorer]` | **Primary source** | `[ ]` | Always available; the fallback that keeps the project viable |
| `[Multi-chain explorer]` | Cross-chain following | `[ ]` | |
| `[Entity labelling platform]` | Entity labels, flow visualization | `[ ]` | Labels are perishable — record observation dates |
| `[Graphing tool]` | Visual reconstruction | `[ ]` | |

**Principle:** the block explorer is the primary source. Everything else is support. If any platform closes its free tier, the investigation does not stall.

## Verification notes

`[Record: VPN egress IP confirmed different from residential; VM snapshot taken before first query; no wallet software present in the analysis environment]`

---

→ [Phase 02 — Anchor Point Identification](../phase02-anchor/README.md)
