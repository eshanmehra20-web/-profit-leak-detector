# Profit Leak Detector

A free-first MVP for small shops and online sellers to estimate sales, costs, expenses, and product contribution profit.

## Current scope
- Record sales by product, quantity, selling price, and unit cost
- Record operating expenses
- Dashboard totals: revenue, cost of goods, expenses, and estimated net profit
- Product-level contribution profit and loss flags
- CSV export and JSON backup/import
- Local browser storage (data stays in this browser unless the user exports it)

## Run locally
Python 3.9+:
```bash
python app.py
```
Open http://127.0.0.1:8000

No paid services, accounts, analytics, or external AI APIs are required.

## Important limitations
- This is a prototype, not accounting or tax software.
- It does not yet handle inventory valuation, tax, payment fees, shipping allocations, partial refunds, or multi-user/cloud sync.
- Refunds/returns are intentionally not represented as negative sales in this version. Add them only after a separately tested returns workflow is implemented.
- Keep real customer and financial data out of public repositories and demo environments.

## Test
```bash
python -m unittest discover -s tests -v
```
