import requests
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '''
  /$$$$$$            /$$
 /$$__  $$          |__/
| $$  \__/  /$$$$$$  /$$ /$$$$$$$
| $$       /$$__  $$| $$| $$__  $$
| $$      | $$  \ $$| $$| $$  \ $$
| $$    $$| $$  | $$| $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$| $$  | $$
 \______/  \______/ |__/|__/  |__/
'''
animated(logo)
print('  »»»Devoloper By White_Devil«««')
print(' _________________________________')

def get_crypto_details(coin_ids):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(coin_ids),
        'vs_currencies': 'usd',
        'include_market_cap': 'true',
        'include_24hr_vol': 'true',
        'include_24hr_change': 'true',
        'include_last_updated_at': 'true'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        for coin_id in coin_ids:
            if coin_id in data:
                coin = data[coin_id]
                print(f"Details for {coin_id.upper()}:")
                print(f"  Current Price (USD): ${coin['usd']}")
                print(f"  Market Cap (USD): ${coin['usd_market_cap']}")
                print(f"  24h Volume (USD): ${coin['usd_24h_vol']}")
                print(f"  24h Change: {coin['usd_24h_change']:.2f}%")
                print(f"  Last Updated: {coin['last_updated_at']}\n")
            else:
                print(f"  No data found for {coin_id.upper()}\n")
    else:
        print("Failed to retrieve data. Please check your API request.")

if __name__ == "__main__":
    # List of cryptocurrencies by their CoinGecko IDs
    coin_ids = ['bitcoin', 'ethereum', 'dogecoin', 'monero', 'litecoin']
    get_crypto_details(coin_ids)

