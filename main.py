import os
import random
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def begin(message: types.Message):
    user = message.from_user.full_name
    await message.answer(
        f"Привет, {user}"
    )

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer("ВСЕ КОМАНДЫ :\n"
                         "/start - старт программы\n"
                         "/help - помощь\n"
                         "/myinfo - информация о вас\n"
                         "/picture - фотки милых котиков")


@dp.message_handler(commands='myinfo')
async def cmd_myinfo(message: types.Message):
    print(message)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_nickname = message.from_user.username
    await message.answer(f"Ваш айди: {user_id}\n"
                         f"Вашe имя : {user_name}\n"
                         f"Ваш юзернейм: {user_nickname}")

@dp.message_handler(commands='picture')
async def cmd_picture(message: types.Message):
    photo = open('images/' + random.choice(os.listdir('images')), 'rb')
    await bot.send_photo(message.chat.id, photo)

@dp.message_handler()
async def upper_message(message: types.Message):
    if len(message.text.split()) >= 3:
        await message.answer(message.text.upper())


executor.start_polling(dp)
