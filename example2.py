from pprint import pprint
import requests

API_KEY = "SGA3UDDL2CT3DRQ4"
function = "TIME_SERIES_INTRADAY"
symbol = input("Podaj symbol: ")
interval = "15min"


response = requests.get(
    f"https://www.alphavantage.co/query?",
    params={
        "function": function,
        "symbol": symbol,
        "interval": interval,
        "apikey": API_KEY,
    },
)

data = response.json()

prices = data.get("Time Series (15min)")
volume = [int(price.get("5. volume")) for date, price in prices.items()]
close_price = [int(price.get("4. close")) for date, price in prices.items()]
pprint(volume)
pprint(close_price)
pprint(data)
