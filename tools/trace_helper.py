#!/usr/bin/env python3
"""
trace_helper.py — Retrieval and tabulation support for manual fund tracing.

WHAT THIS DOES
    Pulls the outbound transaction history of an address from a block explorer
    API and presents it as a sorted table, so that hop-by-hop tracing does not
    require clicking through a web interface transaction by transaction.

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
    Explorer APIs change their endpoints, parameters, and authentication
    requirements over time. Verify the current API documentation for the chain
    you are analyzing and adjust API_BASE and the parameter names below
    accordingly. Record the API version and rate limits used in tools/README.md
    for reproducibility.
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
# Verify against current explorer API documentation before use.
API_BASE = "https://api.etherscan.io/api"
WEI_PER_ETH = 10**18
RATE_LIMIT_SLEEP = 0.25  # seconds between calls; adjust to your API tier


def fetch_transactions(address, api_key, start_block=0, end_block=99999999):
    """Retrieve the normal transaction list for an address."""
    params = {
        "module": "account",
        "action": "txlist",
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
        sys.exit(f"API returned an error: {message} — {payload.get('result')}")

    result = payload.get("result")
    if not isinstance(result, list):
        sys.exit(f"Unexpected API response shape: {payload}")

    return result


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
    }


def print_table(rows, address):
    """Print a readable summary for manual review."""
    if not rows:
        print(f"\nNo outbound transactions found for {address}\n")
        return

    total = sum(r["value_eth"] for r in rows)

    print(f"\nOutbound transactions from {address}")
    print(f"Retrieved {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print(f"{len(rows)} transaction(s), {total:.6f} ETH total\n")

    print(f"{'TIMESTAMP (UTC)':<21} {'VALUE (ETH)':>16}  {'DESTINATION':<44} TX HASH")
    print("-" * 130)

    for r in sorted(rows, key=lambda x: x["value_eth"], reverse=True):
        flag = " [FAILED]" if r["is_error"] == "1" else ""
        print(
            f"{r['timestamp_utc']:<21} {r['value_eth']:>16.6f}  "
            f"{r['to']:<44} {r['hash']}{flag}"
        )

    print("-" * 130)

    # The highest-value branch is surfaced because that is this investigation's
    # pre-registered branch-selection criterion. The analyst still decides.
    if rows:
        top = max(rows, key=lambda x: x["value_eth"])
        print(f"\nHighest-value destination: {top['to']}")
        print(f"  {top['value_eth']:.6f} ETH — tx {top['hash']}")
        print("\nBranch selection remains an analyst decision. Record branches")
        print("not followed in the phase 03 trace log.\n")


def write_csv(rows, path):
    """Write results for inclusion in the evidence record."""
    if not rows:
        return
    fields = ["hash", "timestamp_utc", "to", "value_eth", "block", "is_error"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
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

    time.sleep(RATE_LIMIT_SLEEP)

    raw = fetch_transactions(args.address, api_key)
    rows = [normalize(tx) for tx in outbound_only(raw, args.address)]

    if args.min_value > 0:
        before = len(rows)
        rows = [r for r in rows if r["value_eth"] >= args.min_value]
        suppressed = before - len(rows)
        if suppressed:
            print(f"\n{suppressed} transaction(s) below {args.min_value} ETH suppressed.")
            print("Suppressed transactions are still part of the record — note the")
            print("filter threshold in the trace log.")

    print_table(rows, args.address)

    if args.csv:
        write_csv(rows, args.csv)


if __name__ == "__main__":
    main()
