import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import keyboards as kb


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Привет!\nГотов заглянуть на рынок крипты?")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Напиши мне /currency и выбери криптовалюту, я сообщу тебе её стоимость в данный момент!")


#@dp.message_handler()
#async def echo_message(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_keyboard(callback_query: types.CallbackQuery):
    code = callback_query.data
    if code == 'btc':
        await bot.answer_callback_query(callback_query.id, text='BTC')
    elif code == 'bnb':
        await bot.answer_callback_query(callback_query.id, text='BNB')
    elif code == 'eth':
        await bot.answer_callback_query(callback_query.id, text='ETH')
    elif code == 'ltc':
        await bot.answer_callback_query(callback_query.id, text='LTC')
    elif code == 'usdt':
        await bot.answer_callback_query(callback_query.id, text='USDT')


@dp.message_handler(commands=['currency'])
async def process_command_list(message: types.Message):
    await bot.send_message(message.from_user.id, text="Выбери крипту :)", reply_markup=kb.inline_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
