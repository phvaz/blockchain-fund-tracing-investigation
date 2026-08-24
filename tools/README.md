# Analysis Tooling

Scripts used to reduce manual effort during tracing. Documented so a reader can distinguish an analytical boundary from a limit of endurance.

## Principle

Automation handles retrieval and tabulation. **It does not make analytical decisions.** Branch selection, typology classification, and confidence assignment are performed by the analyst, not by a script.

Where the tool surfaces something — a highest-value destination, a suspicious symbol — it surfaces it as information for the analyst to act on, never as a decision already taken.

---

## Scripts

| Script | Purpose | Input | Output |
|---|---|---|---|
| `trace_helper.py` | Retrieves and tabulates outbound transfers for an address, grouped by asset | Address, optional chain ID | Console table and optional CSV |

### Usage

```bash
export EXPLORER_API_KEY="your_key"          # PowerShell: $env:EXPLORER_API_KEY="your_key"

python3 trace_helper.py 0xADDRESS
python3 trace_helper.py 0xADDRESS --csv data/raw/hop1.csv
python3 trace_helper.py 0xADDRESS --chainid 42161      # follow across a bridge
python3 trace_helper.py 0xADDRESS --assets token       # token transfers only
python3 trace_helper.py 0xADDRESS --min-value 1.0      # suppress small transfers
```

---

## Development log

Each change below was made in response to something the investigation revealed. They are recorded because the tool's limitations at each stage bear on what the analysis could and could not see at the time.

### 1. Initial version — native transfers only

Retrieved the transaction list for an address and tabulated outbound transfers sorted by value.

**Why:** the immediate need was to avoid clicking through a web interface transaction by transaction.

### 2. Migration to Etherscan API V2

The first live run failed:

```
API returned an error: NOTOK — You are using a deprecated V1 endpoint,
switch to Etherscan API V2
```

**Why the change:** the V1 endpoint had been retired. V2 requires a different base URL and a `chainid` parameter.

**Consequence beyond the fix:** V2 is multichain — one key and one endpoint serve every supported chain. If the traced funds cross a bridge, the same script follows them onto the destination chain by changing `--chainid`, with no second API account. Each retrieval records its chain in the CSV so a dataset cannot later be misread as belonging to the wrong chain.

### 3. Token transfer retrieval added

Running the script against a candidate anchor returned 48 outbound transactions totalling **0.16 ETH** — almost all with a value of exactly zero.

**What that meant:** a transaction that moves tokens carries no native value. Its value field reads zero while the actual movement is recorded as a contract event, retrieved from a separate endpoint. The script was reading only half of what was there.

**Why it mattered:** an address whose entire outbound history appears to be zero-value transactions has not been idle — it has moved tokens, and a trace reading only native transfers would have concluded, wrongly, that nothing left.

**What changed:** the script now retrieves both `txlist` (native) and `tokentx` (ERC-20) by default, with `--assets` to restrict if needed.

**Decimals are read, not assumed.** Token amounts are stored as integers scaled by each token's own decimal count — commonly 18, but 6 for several widely-used stablecoins. Assuming 18 for a 6-decimal token understates the amount by a factor of a trillion, silently. The value reported by the API is used instead.

**Totals are per asset, never summed across assets.** One unit of one token and one unit of another are not comparable quantities. Where more than one asset is present, the script states that branch selection requires a valuation judgment and that the basis for it must be recorded — it does not make that judgment.

### 4. Token symbol impersonation detection

Running the script against the second candidate anchor returned what appeared to be eight separate assets, several rendering identically in the terminal:

```
ЕТН      57 transfers
ETH      52 transfers
ЕTH      45 transfers
ЕТН...   35 transfers
EТH      27 transfers
stEТH    17 transfers
stETH    11 transfers
ѕтETН     2 transfers
```

**What that meant:** a token's symbol is chosen by whoever deploys the contract. It is not an identifier and carries no guarantee of uniqueness or honesty. Several of these symbols substitute Cyrillic characters for Latin ones — `Е` (U+0415) for `E`, `Т` (U+0422) for `T`, `ѕ` (U+0455) for `s` — producing strings visually indistinguishable from a legitimate asset but referring to entirely different contracts.

The same retrieval also returned a token whose symbol was literally `BybitExploiter`, with 17.3 million units sent to the queried address itself — consistent with deliberate contamination of a notable address's transaction history.

**Why it mattered:** the amounts attached to these tokens are arbitrary. An analyst reading the earlier output at face value would have recorded that the address moved hundreds of thousands of ETH. It did not. Reporting that figure would have been a factual error introduced by trusting a label.

**What changed:**

- **Grouping is by `(symbol, contract)`, not by symbol.** Two tokens sharing a symbol are different assets when their contracts differ, and merging them would combine a real asset with an impersonation under one total.
- **The contract address is printed for every token group.** The contract is the only reliable identifier; the symbol is decoration.
- **Symbols containing non-ASCII characters are flagged**, with the Unicode code points of the offending characters shown explicitly (`Е=U+0415`), so the reader can see what is being impersonated rather than trusting that two identical-looking strings differ.
- **Symbol collisions across contracts are flagged** separately.
- **The warning prints before any amounts**, so a total is never read before the reader learns it may be meaningless.
- **The CSV carries a `symbol_non_ascii` column**, because a spreadsheet renders homoglyphs invisibly and the flag would otherwise be lost on export.

**What the tool still does not do:** it does not verify that a contract is the legitimate one for a given asset. Flagging a non-ASCII symbol catches crude impersonation; a token deployed with a clean ASCII symbol and a false claim to being a known asset will not be flagged. Confirming that a contract address is genuinely the asset it claims to be remains an analyst task, performed against independent sources and recorded in the phase log.

---

## API notes

| Field | Value |
|---|---|
| API | Etherscan V2 (multichain) |
| Endpoint | `https://api.etherscan.io/v2/api` |
| Key tier | Free |
| Chain selection | `chainid` parameter |
| Actions used | `txlist` (native), `tokentx` (ERC-20) |
| Rate limit | `[record observed limit for the tier in use]` |
| Verified working | 2026-08-24 |

---

## Filter discipline

`--min-value` suppresses transfers below a threshold. Two constraints on its use:

1. **The threshold is recorded in the trace log whenever it is applied.** A documented filter is a stated scope decision; an undocumented one is an omission.
2. **The threshold applies to raw token amounts, not to value.** A threshold meaningful for one asset is meaningless for another. Where multiple assets are present, filtering by a single number is a blunt instrument and its effect should be stated rather than assumed.
