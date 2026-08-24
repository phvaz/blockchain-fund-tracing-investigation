#!/usr/bin/env python3
"""
trace_helper.py — Retrieval and tabulation support for manual fund tracing.

WHAT THIS DOES
    Pulls the outbound transfer history of an address from a block explorer API
    and presents it as a sorted table, so that hop-by-hop tracing does not
    require clicking through a web interface transaction by transaction.

    Two distinct movement types are retrieved, because they are recorded
    separately on-chain and a trace that reads only one will miss the other:

      native  — transfers of the chain's own currency (ETH, BNB, ...)
      token   — ERC-20 transfers, recorded as contract events rather than as
                value on the transaction itself

    A transaction moving tokens typically shows a native value of zero. An
    address whose outbound history is all zero-value transactions has almost
    certainly moved tokens, not native currency. Default is to retrieve both.

TOKEN SYMBOLS ARE NOT IDENTIFIERS
    A token's symbol is chosen by whoever deployed the contract. Anyone can
    deploy a token calling itself "ETH", and anyone can deploy one whose name
    uses Cyrillic or Greek characters that render identically to Latin ones.
    Both are routinely used to contaminate the transaction history of notable
    addresses.

    The only reliable identifier of a token is its contract address. This tool
    therefore displays the contract for every token group, flags symbols
    containing non-ASCII characters, and never merges groups by symbol alone.

WHAT THIS DOES NOT DO
    This script makes no analytical decisions. It does not select branches, does
    not classify typologies, does not assign confidence, and does not decide when
    to stop. Those are the analyst's decisions and are documented in the phase
    logs. This is a retrieval tool, not an analysis tool.

USAGE
    export EXPLORER_API_KEY="your_key_here"
    python3 trace_helper.py 0xADDRESS
    python3 trace_helper.py 0xADDRESS --min-value 1.0 --csv hop3.csv

NOTE ON API CONFIGURATION
    Uses the Etherscan V2 API, which is multichain: the same endpoint and key
    serve all supported chains, selected via the chainid parameter. The V1
    endpoint is deprecated.

    Explorer APIs change over time. If requests begin failing, verify the
    current API documentation and adjust API_BASE and the parameters below.
    Record the API version and rate limits used in tools/README.md for
    reproducibility.

CHAIN SELECTION
    Default chain is Ethereum mainnet (chainid 1). Override with --chainid for
    other chains — relevant when following funds across a bridge.
"""

import argparse
import csv
import os
import sys
import time
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    sys.exit("Missing dependency. Install with: pip install requests")


# --- Configuration -----------------------------------------------------------
# Etherscan V2 multichain endpoint. One key, many chains, selected by chainid.
API_BASE = "https://api.etherscan.io/v2/api"
DEFAULT_CHAIN_ID = 1  # Ethereum mainnet
WEI_PER_ETH = 10**18
RATE_LIMIT_SLEEP = 0.25  # seconds between calls; adjust to your API tier

# Chains commonly encountered when following funds across bridges.
# Verify current chainid values against the API documentation before relying
# on any of these for analysis.
KNOWN_CHAINS = {
    1: "Ethereum",
    10: "Optimism",
    56: "BNB Smart Chain",
    137: "Polygon",
    8453: "Base",
    42161: "Arbitrum One",
}

# Native currency symbol per chain, for display only.
NATIVE_SYMBOL = {
    1: "ETH",
    10: "ETH",
    56: "BNB",
    137: "MATIC",
    8453: "ETH",
    42161: "ETH",
}

# API actions. Native and token transfers are separate endpoints because they
# are separate things on-chain: native value is a field on the transaction,
# while a token transfer is an event emitted by a contract.
ACTION_NATIVE = "txlist"
ACTION_TOKEN = "tokentx"


def fetch_transactions(address, api_key, action=ACTION_NATIVE,
                       chain_id=DEFAULT_CHAIN_ID,
                       start_block=0, end_block=99999999):
    """Retrieve a transfer list for an address on a given chain.

    action: ACTION_NATIVE for native-currency transactions,
            ACTION_TOKEN for ERC-20 transfer events.
    """
    params = {
        "chainid": chain_id,
        "module": "account",
        "action": action,
        "address": address,
        "startblock": start_block,
        "endblock": end_block,
        "sort": "asc",
        "apikey": api_key,
    }

    try:
        response = requests.get(API_BASE, params=params, timeout=30)
        response.raise_for_status()
    except requests.RequestException as exc:
        sys.exit(f"Request failed: {exc}")

    payload = response.json()

    # Explorer APIs signal "no results" as a non-error status; treat separately.
    if payload.get("status") == "0":
        message = payload.get("message", "")
        if "No transactions found" in message:
            return []
        detail = payload.get("result", "")
        if "deprecated" in str(detail).lower():
            sys.exit(
                f"API returned an error: {message} — {detail}\n\n"
                "This script targets the V2 endpoint. If this appears, the API "
                "has changed again; check the current documentation and update "
                "API_BASE and the request parameters."
            )
        sys.exit(f"API returned an error: {message} — {detail}")

    result = payload.get("result")
    if not isinstance(result, list):
        sys.exit(f"Unexpected API response shape: {payload}")

    return result


def has_non_ascii(text):
    """True if the string contains characters outside ASCII.

    Homoglyph impersonation relies on characters that render like Latin
    letters but are not: Cyrillic Е U+0415 for E, Т U+0422 for T, ѕ U+0455
    for s, Greek Α U+0391 for A, and many others. A legitimate token symbol
    has no reason to contain them.
    """
    return any(ord(ch) > 127 for ch in text or "")


def describe_symbol(symbol):
    """Render a symbol with its suspicious characters made visible.

    Returns the symbol followed by the Unicode code points of any non-ASCII
    characters, so that a reader can see exactly what is being impersonated
    rather than having to trust that two identical-looking strings differ.
    """
    if not has_non_ascii(symbol):
        return symbol
    points = " ".join(
        f"{ch}=U+{ord(ch):04X}" for ch in symbol if ord(ch) > 127
    )
    return f"{symbol}  [non-ASCII: {points}]"


def outbound_only(transactions, address):
    """Filter to transactions sent *from* the address under examination."""
    target = address.lower()
    return [tx for tx in transactions if tx.get("from", "").lower() == target]


def normalize(tx):
    """Reduce a raw transaction to the fields relevant to tracing."""
    wei = int(tx.get("value", 0))
    ts = int(tx.get("timeStamp", 0))
    return {
        "hash": tx.get("hash", ""),
        "timestamp_utc": datetime.fromtimestamp(ts, tz=timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "to": tx.get("to", ""),
        "value_eth": wei / WEI_PER_ETH,
        "block": tx.get("blockNumber", ""),
        "is_error": tx.get("isError", "0"),
        "kind": "native",
        "asset": None,          # filled at display time with the chain symbol
        "contract": "",
    }


def normalize_token(tx):
    """Reduce a raw ERC-20 transfer event to the fields relevant to tracing.

    Token amounts are stored as integers scaled by the token's own decimals,
    which vary per token (USDT commonly 6, most others 18). Dividing by the
    wrong factor silently misstates the amount by orders of magnitude, so the
    decimals reported by the API are used rather than assumed.
    """
    try:
        decimals = int(tx.get("tokenDecimal") or 18)
    except ValueError:
        decimals = 18

    try:
        raw = int(tx.get("value", 0))
    except ValueError:
        raw = 0

    ts = int(tx.get("timeStamp", 0))
    return {
        "hash": tx.get("hash", ""),
        "timestamp_utc": datetime.fromtimestamp(ts, tz=timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "to": tx.get("to", ""),
        "value_eth": raw / (10 ** decimals),
        "block": tx.get("blockNumber", ""),
        "is_error": "0",        # token transfer events only exist if successful
        "kind": "token",
        "asset": tx.get("tokenSymbol", "?"),
        "contract": tx.get("contractAddress", ""),
    }


def print_table(rows, address, chain_id=DEFAULT_CHAIN_ID):
    """Print a readable summary for manual review, grouped by asset.

    Grouping is by (symbol, contract) rather than by symbol alone. Two tokens
    sharing a symbol are different assets if their contracts differ, and
    merging them would silently combine a real asset with an impersonation.
    """
    chain_name = KNOWN_CHAINS.get(chain_id, f"chain {chain_id}")
    symbol = NATIVE_SYMBOL.get(chain_id, "native")

    for r in rows:
        if r["asset"] is None:
            r["asset"] = symbol

    if not rows:
        print(f"\nNo outbound transfers found for {address} on {chain_name}\n")
        return

    print(f"\nOutbound transfers from {address}")
    print(f"Chain: {chain_name} (chainid {chain_id})")
    print(f"Retrieved {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")

    # Group by identity, not by label.
    groups = {}
    for r in rows:
        groups.setdefault((r["asset"], r["contract"]), []).append(r)

    native_count = sum(1 for r in rows if r["kind"] == "native")
    token_count = len(rows) - native_count
    print(f"{len(rows)} transfer(s): {native_count} native, {token_count} token")

    # Surface impersonation before showing any amounts, so the reader does not
    # read a total before learning it may be meaningless.
    suspicious = [
        (sym, con) for (sym, con) in groups
        if has_non_ascii(sym)
    ]
    dup_symbols = {}
    for (sym, con) in groups:
        dup_symbols.setdefault(sym.lower(), set()).add(con)
    collisions = {s: c for s, c in dup_symbols.items() if len(c) > 1}

    if suspicious or collisions:
        print()
        print("!" * 78)
        print("TOKEN SYMBOL WARNING")
        if suspicious:
            print(f"  {len(suspicious)} token group(s) use non-ASCII characters in")
            print("  their symbol. Characters from other alphabets can render")
            print("  identically to Latin letters. These are distinct tokens from")
            print("  any legitimate asset they resemble.")
        if collisions:
            print(f"  {len(collisions)} symbol(s) appear under more than one contract.")
            print("  Same name does not mean same asset.")
        print("  Amounts below are raw token units and carry no implied value.")
        print("  Verify each contract address before treating any group as real.")
        print("!" * 78)

    print()

    for (asset, contract) in sorted(groups, key=lambda k: -len(groups[k])):
        group = groups[(asset, contract)]
        total = sum(r["value_eth"] for r in group)
        kind = group[0]["kind"]
        flag = "  ⚠ NON-ASCII SYMBOL" if has_non_ascii(asset) else ""

        print(f"--- {describe_symbol(asset)} ({kind}) — "
              f"{len(group)} transfer(s), {total:,.6f} total{flag} ---")
        if contract:
            print(f"    contract: {contract}")
        print(f"{'TIMESTAMP (UTC)':<21} {'AMOUNT':>22}  {'DESTINATION':<44} TX HASH")
        print("-" * 138)

        for r in sorted(group, key=lambda x: x["value_eth"], reverse=True):
            err = " [FAILED]" if r["is_error"] == "1" else ""
            print(
                f"{r['timestamp_utc']:<21} {r['value_eth']:>22,.6f}  "
                f"{r['to']:<44} {r['hash']}{err}"
            )
        print()

    print("Highest-value transfer per asset:")
    for (asset, contract) in sorted(groups, key=lambda k: -len(groups[k])):
        top = max(groups[(asset, contract)], key=lambda x: x["value_eth"])
        mark = " ⚠" if has_non_ascii(asset) else ""
        print(f"  {asset:<12}{mark} {top['value_eth']:>20,.6f} → {top['to']}")
        if contract:
            print(f"  {'':<12}  {'':>20}   contract {contract}")

    if len(groups) > 1:
        print("\nMultiple assets present. Amounts are not comparable across")
        print("assets; selecting a branch requires a valuation judgment.")
        print("Record the basis for that judgment in the phase 03 trace log.")

    print("\nBranch selection remains an analyst decision. Record branches")
    print("not followed in the phase 03 trace log.\n")


def write_csv(rows, path, chain_id=DEFAULT_CHAIN_ID):
    """Write results for inclusion in the evidence record."""
    if not rows:
        return
    # chain and retrieval time are recorded per row: a CSV that outlives its
    # context is not evidence.
    retrieved = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    chain_name = KNOWN_CHAINS.get(chain_id, str(chain_id))

    fields = ["hash", "timestamp_utc", "to", "amount", "asset",
              "symbol_non_ascii", "kind", "contract", "block", "is_error",
              "chain_id", "chain_name", "retrieved_utc"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for r in rows:
            writer.writerow({
                "hash": r["hash"],
                "timestamp_utc": r["timestamp_utc"],
                "to": r["to"],
                "amount": r["value_eth"],
                "asset": r["asset"],
                # Recorded per row so the flag survives export: a CSV opened
                # later in a spreadsheet will render homoglyphs invisibly.
                "symbol_non_ascii": "yes" if has_non_ascii(r["asset"]) else "no",
                "kind": r["kind"],
                "contract": r["contract"],
                "block": r["block"],
                "is_error": r["is_error"],
                "chain_id": chain_id,
                "chain_name": chain_name,
                "retrieved_utc": retrieved,
            })
    print(f"Written to {path}")


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve outbound transactions for an address during manual tracing."
    )
    parser.add_argument("address", help="Address to examine")
    parser.add_argument(
        "--min-value",
        type=float,
        default=0.0,
        help="Suppress transactions below this value (dust filter)",
    )
    parser.add_argument(
        "--chainid",
        type=int,
        default=DEFAULT_CHAIN_ID,
        help=f"Chain ID (default {DEFAULT_CHAIN_ID}, Ethereum mainnet). "
             f"Known: {', '.join(f'{k}={v}' for k, v in KNOWN_CHAINS.items())}",
    )
    parser.add_argument(
        "--assets",
        choices=["all", "native", "token"],
        default="all",
        help="Which transfer types to retrieve (default: all). A trace that "
             "reads only native transfers will miss ERC-20 movement entirely.",
    )
    parser.add_argument("--csv", metavar="PATH", help="Write results to CSV")
    args = parser.parse_args()

    api_key = os.environ.get("EXPLORER_API_KEY")
    if not api_key:
        sys.exit(
            "EXPLORER_API_KEY is not set.\n"
            "Obtain a free API key from the explorer and export it:\n"
            '  export EXPLORER_API_KEY="your_key_here"'
        )

    if not args.address.startswith("0x") or len(args.address) != 42:
        sys.exit(f"Address does not look valid: {args.address}")

    rows = []

    if args.assets in ("all", "native"):
        time.sleep(RATE_LIMIT_SLEEP)
        raw = fetch_transactions(args.address, api_key,
                                 action=ACTION_NATIVE, chain_id=args.chainid)
        rows += [normalize(tx) for tx in outbound_only(raw, args.address)]

    if args.assets in ("all", "token"):
        time.sleep(RATE_LIMIT_SLEEP)
        raw = fetch_transactions(args.address, api_key,
                                 action=ACTION_TOKEN, chain_id=args.chainid)
        rows += [normalize_token(tx) for tx in outbound_only(raw, args.address)]

    if args.min_value > 0:
        before = len(rows)
        rows = [r for r in rows if r["value_eth"] >= args.min_value]
        suppressed = before - len(rows)
        if suppressed:
            print(f"\n{suppressed} transfer(s) below {args.min_value} suppressed.")
            print("Note: the threshold is applied to the raw amount of each asset,")
            print("not to value. A threshold meaningful for ETH is not meaningful")
            print("for a stablecoin. Suppressed transfers remain part of the")
            print("record — state the threshold used in the trace log.")

    print_table(rows, args.address, chain_id=args.chainid)

    if args.csv:
        write_csv(rows, args.csv, chain_id=args.chainid)


if __name__ == "__main__":
    main()
