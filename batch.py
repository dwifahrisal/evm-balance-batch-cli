#!/usr/bin/env python3
"""Fetch ETH balances for a list of addresses (one JSON-RPC call per address)."""

import json
import sys
import urllib.request

RPC_URL = "https://eth.llamarpc.com"
ADDRESSES_FILE = "addresses.txt"


def get_balance(address: str) -> float | None:
    body = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "eth_getBalance",
        "params": [address, "latest"],
    }).encode()
    req = urllib.request.Request(RPC_URL, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.load(resp)
    except Exception:
        return None
    if "result" not in result:
        return None
    return int(result["result"], 16) / 1e18


def main() -> int:
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = ADDRESSES_FILE
    try:
        with open(path) as f:
            addresses = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"file not found: {path}", file=sys.stderr)
        return 1

    total = 0.0
    for address in addresses:
        balance = get_balance(address)
        if balance is None:
            print(f"{address}  error")
            continue
        total += balance
        print(f"{address}  {balance:.6f} ETH")
    print(f"total: {total:.6f} ETH across {len(addresses)} addresses")
    return 0


if __name__ == "__main__":
    sys.exit(main())
