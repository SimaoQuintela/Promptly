import requests
import os

api_key = os.getenv("ALPHAVANTAGE_API_KEY")
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []

for symbol in symbols:
    print(f'Working on symbol {symbol}')
    response = requests.get(url.format(symbol, api_key))
    print(response.json())
    results.append(response.json())

print("The end!")    