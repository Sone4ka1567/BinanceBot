import requests
import json


def get_current_price(symbol):
    response_b = requests.get(f'http://binance.com/api/v3/ticker/price?symbol={symbol}').content
    return json.loads(response_b)['price']
