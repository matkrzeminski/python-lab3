import asyncio
import aiohttp
import time


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main(loop):
    start = time.time()
    async with aiohttp.ClientSession(loop=loop) as session:
        futures = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*futures)
    end = time.time()
    return {
        "time": end - start,
        "results": results,
    }


urls = [
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&apikey=SGA3UDDL2CT3DRQ4",
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=15min&apikey=SGA3UDDL2CT3DRQ4",
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOGL&interval=15min&apikey=SGA3UDDL2CT3DRQ4",
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=FB&interval=15min&apikey=SGA3UDDL2CT3DRQ4",
    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&apikey=SGA3UDDL2CT3DRQ4",
]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main(loop))
print(results)
