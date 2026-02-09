import requests
import pandas as pd

BASE_URL = "https://api.coingecko.com/api/v3"

def get_price_history(coin="bitcoin", days=30):

    url = f"{BASE_URL}/coins/{coin}/market_chart"
    params = {"vs_currency": "usd", "days": days}

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if "prices" not in data:
        return pd.DataFrame()

    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    return df
