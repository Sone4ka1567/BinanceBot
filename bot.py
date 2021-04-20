import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import keyboards as kb


# logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nГотов заглянуть на рынок крипты?")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне /currency и выбери криптовалюту, я сообщу тебе её стоимость в данный момент!")


#@dp.message_handler()
#async def echo_message(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(commands=['currency'])
async def process_command_list(message: types.Message):
    await message.reply("Отправляю все возможные кнопки", reply_markup=kb.inline_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
