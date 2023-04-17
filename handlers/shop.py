from aiogram import types



async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton("Всё"))
    kb.add(types.KeyboardButton("Часы"), types.KeyboardButton("Сувениры"))
    await message.answer(
        f"Выберите категорию ниже:",
        reply_markup=kb
    )


async def show_suveniry(message: types.Message):
    await message.reply(
        "Вот наши сувениры",
        reply_markup=types.ReplyKeyboardRemove()
    )