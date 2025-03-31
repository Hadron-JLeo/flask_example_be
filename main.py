from flask import Flask, render_template
import requests

app = Flask(__name__)

application = app # This is what the cpanel-python file will be using

# Replace with a real API (e.g., Alpha Vantage, Yahoo Finance, CoinGecko)
STOCKS = {"AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Google"}
CRYPTO = {"bitcoin": "BTC", "ethereum": "ETH", "dogecoin": "DOGE"}

def get_stock_prices():
    prices = {}
    for ticker in STOCKS.keys():
        response = requests.get(f"https://api.polygon.io/v1/last/stocks/{ticker}?apiKey=YOUR_API_KEY")
        if response.status_code == 200:
            data = response.json()
            prices[ticker] = data["last"]["price"]
        else:
            prices[ticker] = "N/A"
    return prices

def get_crypto_prices():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd")
    if response.status_code == 200:
        return response.json()
    return {}

@app.route("/")
def index():
    stock_prices = get_stock_prices()
    crypto_prices = get_crypto_prices()
    return render_template("index.html", stocks=stock_prices, cryptos=crypto_prices)

if __name__ == "__main__":
    app.run(debug=True)
