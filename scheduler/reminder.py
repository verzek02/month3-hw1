from aiogram import types
from config import scheduler, bot
from datetime import datetime


async def start_reminder(message: types.Message):
    # scheduler.add_job(
    #     send_reminder,
    #     'interval',
    #     seconds=5,
    #     args=(message.from_user.id,)
    # )
    scheduler.add_job(
        send_reminder,
        'date',
    run_date=datetime(year=2023, month=5, day=1, hour=17, minute=45),
    args=(message.from_user.id,)
    )

    await message.answer("Слушаю и повинуюсь!")


async def send_reminder(user_id: int):
    await bot.send_message(
        chat_id=user_id,
        text="Напоминаю"
    )