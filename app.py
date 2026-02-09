import streamlit as st
import pandas as pd
import altair as alt

from services.coingecko import get_price_history as get_coingecko_history
from services.cryptocompare import get_price_history as get_cryptocompare_history

# Page Config
# -----------------------------
st.set_page_config(
    page_title="Crypto Price Comparison",
    page_icon="📈",
    layout="wide"
)

st.title("📊 Cryptocurrency Price Comparison Dashboard")
st.markdown(
    """
Compare cryptocurrency price trends across **CoinGecko** and **CryptoCompare**  
using real-time public API data.
"""
)

# Coin Mapping (VERY IMPORTANT)
# -----------------------------
COIN_MAP = {
    "Bitcoin": {
        "coingecko": "bitcoin",
        "cryptocompare": "BTC"
    },
    "Ethereum": {
        "coingecko": "ethereum",
        "cryptocompare": "ETH"
    },
    "Litecoin": {
        "coingecko": "litecoin",
        "cryptocompare": "LTC"
    }
}

# Sidebar Controls
# -----------------------------
st.sidebar.header("⚙️ Controls")

selected_coin = st.sidebar.selectbox(
    "Select Cryptocurrency",
    list(COIN_MAP.keys())
)

days = st.sidebar.slider(
    "Days of History",
    min_value=7,
    max_value=90,
    value=30
)

coin_id = COIN_MAP[selected_coin]["coingecko"]
symbol = COIN_MAP[selected_coin]["cryptocompare"]

# Data Fetch
# -----------------------------
@st.cache_data(ttl=300)
def load_data(coin_id, symbol, days):

    cg_df = pd.DataFrame()
    cc_df = pd.DataFrame()

    # CoinGecko
    try:
        cg_df = get_coingecko_history(coin_id, days)
        if not cg_df.empty:
            cg_df["source"] = "CoinGecko"
    except Exception:
        pass

    # CryptoCompare
    try:
        cc_df = get_cryptocompare_history(symbol, days)
        if not cc_df.empty:
            cc_df["source"] = "CryptoCompare"
    except Exception:
        pass

    return cg_df, cc_df


cg_df, cc_df = load_data(coin_id, symbol, days)

# Validation
# -----------------------------
if cg_df.empty and cc_df.empty:
    st.error("❌ Failed to fetch data from both APIs. Try again later.")
    st.stop()

# Combine Data
# -----------------------------
frames = []
if not cg_df.empty:
    frames.append(cg_df)
if not cc_df.empty:
    frames.append(cc_df)

combined_df = pd.concat(frames, ignore_index=True)

# Chart
# -----------------------------
st.subheader("📈 Price Trend Comparison")

if not combined_df.empty:

    chart = alt.Chart(combined_df).mark_line().encode(
        x=alt.X("timestamp:T", title="Date"),
        y=alt.Y("price:Q", title="Price (USD)"),
        color=alt.Color("source:N", title="Data Source"),
        tooltip=["timestamp", "price", "source"]
    ).properties(height=450)

    st.altair_chart(chart, width="stretch")

else:
    st.warning("No data available for chart.")

# Summary Metrics
# -----------------------------
st.subheader("📊 Latest Price Snapshot")

col1, col2 = st.columns(2)

if not cg_df.empty:
    with col1:
        st.metric(
            "CoinGecko Latest Price",
            f"${cg_df['price'].iloc[-1]:,.2f}"
        )

if not cc_df.empty:
    with col2:
        st.metric(
            "CryptoCompare Latest Price",
            f"${cc_df['price'].iloc[-1]:,.2f}"
        )

# Raw Data Tables
# -----------------------------
st.subheader("📄 Raw Data")

tab1, tab2 = st.tabs(["CoinGecko", "CryptoCompare"])

with tab1:
    if not cg_df.empty:
        st.dataframe(cg_df, width="stretch")
    else:
        st.info("CoinGecko data unavailable")

with tab2:
    if not cc_df.empty:
        st.dataframe(cc_df, width="stretch")
    else:
        st.info("CryptoCompare data unavailable")
