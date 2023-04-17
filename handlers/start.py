from aiogram import types


# @dp.message_handler(commands=["start", "go"])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()

    kb.add(types.InlineKeyboardButton("Магазин", callback_data="shop"))
    # print(dir(message.from_user))
    first_name = message.from_user.first_name
    id = message.from_user.id
    await message.answer(
        f"Приветствуем тебя, пользователь {first_name}, {id}",
        reply_markup=kb
    )


