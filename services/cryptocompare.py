import requests
import pandas as pd

BASE_URL = "https://min-api.cryptocompare.com/data/v2"

def get_price_history(symbol="BTC", days=30):

    url = f"{BASE_URL}/histoday"
    params = {
        "fsym": symbol,
        "tsym": "USD",
        "limit": days
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if "Data" not in data or "Data" not in data["Data"]:
        return pd.DataFrame()

    prices = data["Data"]["Data"]

    df = pd.DataFrame(prices)
    df["timestamp"] = pd.to_datetime(df["time"], unit="s")
    df["price"] = df["close"]

    return df[["timestamp", "price"]]

    
