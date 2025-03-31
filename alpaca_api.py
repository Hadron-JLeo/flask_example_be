"""

py file to test the alpaca API to get investment data
https://alpaca.markets/sdks/python/getting_started.html#introduction

https://docs.alpaca.markets/docs/getting-started-with-alpaca-market-data
"""

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, date

#            // -- Import End -- //             #



#-- If I want something specific I can use these --#
TODAY = datetime.today()

YEAR_NOW = TODAY.year
MONTH_NOW = TODAY.month
DAY_NOW = TODAY.day
HOUR_NOW = TODAY.hour
#---------------------------------------------------#


# No keys required for crypto data
client = CryptoHistoricalDataClient()


# Creating request object
request_params = CryptoBarsRequest(
  symbol_or_symbols=["BTC/USD"],
  timeframe=TimeFrame.Day,
  end=datetime.now()
)

request_params.symbol_or_symbols = ['DOGE/USD']



# Retrieve daily bars for Bitcoin in a DataFrame and printing it
btc_bars = client.get_crypto_bars(request_params)

# Convert to dataframe
x = btc_bars.df
print(x)