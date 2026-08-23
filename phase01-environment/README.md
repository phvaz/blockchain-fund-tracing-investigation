# Phase 01 — Environment Preparation

**Status:** `[x] Complete`

## Objective

Establish an isolated analysis environment consistent with the OpSec posture defined in Phase 00, and verify tool availability before analysis begins.

---

## Environment

| Component | Configuration | Verified |
|---|---|---|
| Analysis VM | Kali Linux (reused from prior lab projects), clean snapshot taken before first query | ✅ |
| Network egress | Proton VPN, free tier, CLI client (`protonvpn connect`) | ✅ |
| Burner identity | ProtonMail account, created within the VM under active VPN | ✅ |
| Python environment | Python 3, `requests` | ✅ |

---

## Tool verification

| Tool | Role | Free tier | Notes |
|---|---|---|---|
| Etherscan API V2 | **Primary source** | ✅ | Multichain endpoint (`api.etherscan.io/v2/api`); chain selected via `chainid` parameter |
| Block explorer (web) | Primary source, visual confirmation | ✅ | Used for screenshot capture of entity labels, which are perishable |

**Principle applied:** the block explorer and its API are treated as the primary source. Any additional platform is support only. If a third-party platform closes its free tier, the investigation does not stall.

### API version note

The retrieval script was initially written against the Etherscan V1 endpoint and failed on first use:

```
API returned an error: NOTOK — You are using a deprecated V1 endpoint,
switch to Etherscan API V2
```

The script was migrated to V2, which required a new endpoint and the addition of a `chainid` parameter. This is recorded because it bears on reproducibility: anyone repeating this analysis needs to know which API version was in use, and the V1 endpoint is no longer available.

A secondary consequence is favourable to this investigation: V2 is multichain, so the same key and script follow funds onto another chain by changing `chainid` — relevant if the traced trail crosses a bridge.

---

## Verification notes

### Egress verification

The VPN client's `Connected` status was **not** accepted as evidence that traffic was tunnelled. Verification was performed by direct inspection:

- `curl -4 ifconfig.me` and `curl ifconfig.me` — confirmed the observed exit address on both IPv4 and IPv6
- `ip addr show proton0` — confirmed the tunnel interface exists and is up
- `ip rule show` — confirmed policy-routing rules directing non-marked traffic through the tunnel

This mattered. An earlier connection attempt reported `Connected` at the client level and displayed a foreign exit IP, while the routing table still showed the default route via the local NAT adapter and the resolver was still the residential ISP's. No tunnel interface had been created (`Backend: None` in the client log). Root cause: a second, host-only network adapter retained from earlier lab projects caused the WireGuard backend to fail interface assignment. Disabling the unused adapter resolved it.

The failure was silent at the client level and visible only through direct inspection of the routing table and resolver configuration.

### Free-tier limitation

Server location selection is unavailable on the free tier (`Location selection is not available on the free plan`). Assignment is automatic and has routed to both Singapore (~349 ms RTT from Brazil) and Miami. Because latency on distant servers makes continuous use impractical, egress control is applied **selectively**: the VPN is active for all explorer queries and API calls, and disabled during local documentation and script development.

### Retrieval tooling validated

`tools/trace_helper.py` was tested against a public, high-activity address. The full history returned 766 outbound transactions; applying a 0.1 ETH threshold reduced this to 80. CSV export was confirmed working, with chain identifier and retrieval timestamp written per row.

This test established a practical point for Phase 03: unfiltered retrieval at any single hop can return volumes that are impractical to review manually. Where a value threshold is applied during the investigation, **the threshold is recorded in the trace log** — a documented filter is a stated scope decision; an undocumented one is an omission.

---

→ [Phase 02 — Anchor Point Identification](../phase02-anchor/README.md)
