import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import keyboards as kb
from current_price import get_current_price

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Привет!\nГотов заглянуть на рынок крипты?"
    )


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Напиши мне /currency и выбери криптовалюту,"
            " я сообщу тебе её стоимость в $ в данный момент!"
    )


#@dp.message_handler()
#async def echo_message(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_keyboard(callback_query: types.CallbackQuery):
    code = callback_query.data
    if code == 'btc':
        await bot.send_message(
            callback_query.from_user.id,
            text=('BTC is worth ' + str(get_current_price('BTCUSDT') + '$'))
        )
    elif code == 'bnb':
        await bot.send_message(
            callback_query.from_user.id,
            text=('BNB is worth ' + str(get_current_price('BNBUSDT') + '$'))
        )
    elif code == 'eth':
        await bot.send_message(
            callback_query.from_user.id,
            text=('ETH is worth ' + str(get_current_price('ETHUSDT') + '$'))
        )
    elif code == 'ltc':
        await bot.send_message(
            callback_query.from_user.id,
            text=('LTC is worth ' + str(get_current_price('LTCUSDT') + '$'))
        )
    elif code == 'usdt':
        await bot.send_message(
            callback_query.from_user.id,
            text=('USDT is worth ' + str(get_current_price('USDTRUB') + '₽'))
        )


@dp.message_handler(commands=['currency'])
async def process_command_list(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Выбери крипту, и я скажу её стоимость в долларах :)",
        reply_markup=kb.inline_keyboard
    )


if __name__ == '__main__':
    executor.start_polling(dp)
