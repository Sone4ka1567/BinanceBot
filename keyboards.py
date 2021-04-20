from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_btn_btc = InlineKeyboardButton('BTC', callback_data='btc')
inline_btn_bnb = InlineKeyboardButton('BNB', callback_data='bnb')
inline_btn_eth = InlineKeyboardButton('ETH', callback_data='eth')
inline_btn_ltc = InlineKeyboardButton('LTC', callback_data='ltc')
inline_btn_usdt = InlineKeyboardButton('USDT', callback_data='usdt')


inline_keyboard = InlineKeyboardMarkup(row_width=2).add(inline_btn_btc, inline_btn_bnb)
inline_keyboard.add(inline_btn_eth, inline_btn_ltc)
inline_keyboard.add(inline_btn_usdt)
