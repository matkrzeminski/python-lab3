from pprint import pprint
import requests
import time


def get_time_series(symbol):
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=15min&apikey=SGA3UDDL2CT3DRQ4"
    )
    return response.json()


def get_volume_list(time_series):
    return [price.get("5. volume") for date, price in time_series.items()]


def get_close_list(time_series):
    return [price.get("4. close") for date, price in time_series.items()]


start = time.time()

msft_time_series = get_time_series("MSFT")
aapl_time_series = get_time_series("AAPL")
goog_time_series = get_time_series("GOOGL")
fb_time_series = get_time_series("FB")

msft_volume = get_volume_list(msft_time_series)
aapl_volume = get_volume_list(aapl_time_series)
goog_volume = get_volume_list(goog_time_series)
fb_volume = get_volume_list(fb_time_series)

msft_close = get_close_list(msft_time_series)
aapl_close = get_close_list(aapl_time_series)
goog_close = get_close_list(goog_time_series)
fb_close = get_close_list(fb_time_series)

end = time.time()

print(f"Total time: {end - start}")
