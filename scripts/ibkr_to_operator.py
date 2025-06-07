"""Fetch IBKR data and send to an OpenAI Operator."""

from ib_insync import IB, Stock
import requests
import json

# === Configuration Parameters ===
# Replace the values below with your own settings.

IB_HOST = "127.0.0.1"  # TODO: Host where TWS or IB Gateway runs
IB_PORT = 7497          # TODO: API port for TWS or IB Gateway
IB_CLIENT_ID = 1        # TODO: Any integer; must be unique per client

STOCK_SYMBOL = "AAPL"   # TODO: Ticker symbol
STOCK_EXCHANGE = "SMART"  # TODO: Exchange code
STOCK_CURRENCY = "USD"  # TODO: Currency code

OPERATOR_ENDPOINT = "http://YOUR_OPERATOR_ENDPOINT/ingest"  # TODO: Operator URL
OPERATOR_API_KEY = None  # TODO: Operator API key if required


def fetch_data():
    """Connect to IBKR and retrieve historical data."""
    ib = IB()
    ib.connect(IB_HOST, IB_PORT, clientId=IB_CLIENT_ID)
    contract = Stock(STOCK_SYMBOL, STOCK_EXCHANGE, STOCK_CURRENCY)
    bars = ib.reqHistoricalData(
        contract,
        endDateTime="",
        durationStr="1 D",
        barSizeSetting="1 min",
        whatToShow="TRADES",
        useRTH=True,
        formatDate=1,
    )
    data = [bar.__dict__ for bar in bars]
    ib.disconnect()
    return data


def send_to_operator(data):
    """Send the fetched data to the OpenAI Operator."""
    headers = {"Content-Type": "application/json"}
    if OPERATOR_API_KEY:
        headers["Authorization"] = f"Bearer {OPERATOR_API_KEY}"
    response = requests.post(OPERATOR_ENDPOINT, json=data, headers=headers, timeout=30)
    print(f"Operator response: {response.status_code} {response.text}")


def main():
    data = fetch_data()
    print(f"Retrieved {len(data)} bars from IBKR")
    send_to_operator(data)


if __name__ == "__main__":
    main()
