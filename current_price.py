import requests
import json


def get_current_price(symbol):
    response_ = requests.get(f'http://binance.com/api/'
                             f'v3/ticker/price?symbol={symbol}').content
    return json.loads(response_)['price']
