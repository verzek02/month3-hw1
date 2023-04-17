from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.info import info, echo
from handlers.start import start
from handlers.shop import show_categories, show_suveniry
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # обработчики
    dp.register_message_handler(start, commands=["start"])
    dp.register_callback_query_handler(show_categories, lambda cb: cb.data == "shop")
    dp.register_message_handler(info, commands=["info"])
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_suveniry, Text(equals="Часы"))
    # dp.register_message_handler(show_books, Text(contains="Книги"))
    # dp.register_message_handler(show_books, Text(startswith="Книги"))
    # этот обработчик обрабатывает все сообщения поэтому он ниже всех
    dp.register_message_handler(echo)

    executor.start_polling(dp)




