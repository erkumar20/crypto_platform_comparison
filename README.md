# 📊 Cryptocurrency Price Comparison Dashboard

A Streamlit-based interactive dashboard that compares cryptocurrency price trends using real-time data from two independent public APIs:

- CoinGecko  
- CryptoCompare  

This project demonstrates real-world API integration, data processing, and analytical comparison across platforms providing similar financial data services.

##  Project Objective

This project was built to demonstrate:

- Working with public real-world APIs
- Handling data inconsistencies across providers
- Performing time-series price comparison
- Building interactive analytical dashboards
- Designing clean data pipelines

---

##  Data Sources

### CoinGecko API
- Free public crypto data provider
- No API key required
- Provides historical and live price data

### CryptoCompare API
- Crypto market data aggregator
- Provides historical price data
- Free tier available

---

##  Key Features

- Compare cryptocurrency prices across platforms  
- Select coin and historical duration  
- Visualize price trends  
- View raw API data  
- Understand platform-wise variation  

## Tech Stack

- Python  
- Streamlit  
- Pandas  
- Requests  


## ▶️ How to Run Locally

### Clone Repository
git clone https://github.com/erkumar20/crypto_platform_comparison.git
cd crypto_platform_comparison

Create Virtual Environment:
python3 -m venv venv

Activate Environment:
source venv/bin/activate(macOS)

pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py



### Notes
-Public APIs may have rate limits
-Some coins may temporarily fail if API data is unavailable
-Prices are indicative market averages


