import requests
import asyncio
import aiohttp
import os

api_key = os.getenv("ALPHAVANTAGE_API_KEY")
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL', 'AAPL']
results = []


async def get_symbols(): 
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print(f'Working on symbol {symbol}')
            response = await session.get(url.format(symbol, api_key), ssl=False)
            results.append(await response.json())

asyncio.run(get_symbols())






print("The end!")    