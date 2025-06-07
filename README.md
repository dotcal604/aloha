# Project 1
This is a thoughtful write-up about my project...
## IBKR to OpenAI Operator integration

A sample Python script is provided under `scripts/ibkr_to_operator.py`. It pulls historical data from Interactive Brokers and sends it to an OpenAI Operator endpoint.

### Setup

1. Install Python 3.
2. Install dependencies:
   ```bash
   pip install ib_insync requests
   ```
3. Edit `scripts/ibkr_to_operator.py` and replace the placeholder values:
   - `IB_HOST`, `IB_PORT`, `IB_CLIENT_ID` – connection details for TWS or IB Gateway.
   - `STOCK_SYMBOL`, `STOCK_EXCHANGE`, `STOCK_CURRENCY` – the contract to query.
   - `OPERATOR_ENDPOINT` – your OpenAI Operator URL.
   - `OPERATOR_API_KEY` – API key for the operator (if required).

### Running the script

Start TWS or IB Gateway and then run:
```bash
python scripts/ibkr_to_operator.py
```
The script prints the number of retrieved bars and the operator's response code.
