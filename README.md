# evm-balance-batch

Check the ETH balance of many wallets at once. Put one address per line in `addresses.txt`, run the script, get a full report plus the total.

## Usage

```bash
python3 batch.py addresses.txt
```

To target another EVM chain, change `RPC_URL` (BSC, Polygon, etc.).
