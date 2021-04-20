from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_btn_btc = InlineKeyboardButton('BTC', callback_data='btc')
inline_keyboard = InlineKeyboardMarkup(row_width=2).add(inline_btn_btc)

inline_btn_bnb = InlineKeyboardButton('BNB', callback_data='bnb')
inline_keyboard.add(inline_btn_bnb)

inline_btn_eth = InlineKeyboardButton('ETH', callback_data='eth')
inline_keyboard.add(inline_btn_eth)
