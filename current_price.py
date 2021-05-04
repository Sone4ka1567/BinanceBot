import json
import requests


def get_current_price(symbol):
    response_ = requests.get(f'http://binance.com/api/'
                             f'v3/ticker/price?symbol={symbol}').content
    return json.loads(response_)['price']


def check_availability(symbol):
    code = requests.get(f'http://binance.com/api/'
                        f'v3/ticker/price?symbol={symbol}').status_code
    if code == 200:
        return True
    return False
