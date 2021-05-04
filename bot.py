import logging
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from sql_parser import SQLParser
from config import TOKEN
import keyboards as kb
from current_price import get_current_price, check_availability

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
bd = SQLParser()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Hey!\nAre you ready for the crypto world?)"
    )


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Send /currency and choose crypto,"
             "I'll tell you its cost in $ at this moment!\n"
             "Or send me two currencies from the website in such format:\n"
             "Currency1/Currency2"
    )


@dp.message_handler(commands=['history'])
async def return_history(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text=bd.get_all(message.from_user.id)
    )


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_keyboard(callback_query: types.CallbackQuery):

    code = callback_query.data

    if code == 'usdt':

        bd.add((callback_query.from_user.id, str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),
                'USDT', 'RUB', get_current_price('USDTRUB')))

        await bot.send_message(
            callback_query.from_user.id,
            text=('USDT is worth ' + str(
                get_current_price('USDTRUB') + '₽'))
        )

    else:

        bd.add((callback_query.from_user.id, str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),
                code.upper(), 'USDT', get_current_price(code.upper() + 'USDT')))

        await bot.send_message(
            callback_query.from_user.id,
            text=(code.upper() + ' is worth ' + str(
                get_current_price(code.upper() + 'USDT') + '$'))
        )


@dp.message_handler(commands=['currency'])
async def process_command_list(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        text="Choose crypto and I'll tell you its worth in $ :)",
        reply_markup=kb.inline_keyboard
    )


@dp.message_handler()
async def process_text_request(message: types.Message):

    ind_of_slash = message.text.find("/")
    first_cur = message.text[:ind_of_slash].upper()
    sec_cur = message.text[ind_of_slash + 1:].upper()
    req = message.text.replace("/", "").upper()

    if check_availability(req):

        bd.add((message.from_user.id, str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")), first_cur,
                sec_cur, get_current_price(req)))

        await bot.send_message(
            message.from_user.id,
            text=(first_cur + ' is worth ' + str(
                    get_current_price(req) + " " + sec_cur))
        )

    elif check_availability(sec_cur + first_cur):

        bd.add((message.from_user.id, str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")), first_cur,
                sec_cur, str(1 / float(get_current_price(sec_cur + first_cur)))))

        await bot.send_message(
            message.from_user.id,
            text=(first_cur + ' is worth ' +
                  str(1 / float(get_current_price(sec_cur + first_cur))) + " " + sec_cur)
        )

    else:
        await bot.send_message(
            message.from_user.id,
            text="Couldn't find anything similar :((,\n"
                 " maybe you should try smth different?"
        )


if __name__ == '__main__':
    executor.start_polling(dp)
