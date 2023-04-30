from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp
from handlers.info import info, echo
from handlers.start import start
from handlers.shop import show_categories, show_suveniry
from handlers.survey_fsm import start_survey, process_age, Survey, process_gender,process_name,process_stack,stack_two
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # обработчики
    dp.register_message_handler(start, commands=["start"])
    dp.register_callback_query_handler(show_categories, lambda cb: cb.data == "shop")

    dp.register_message_handler(info, commands=["info"])
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_suveniry, Text(equals="Часы"))

    dp.register_message_handler(start_survey, commands='surv')
    dp.register_message_handler(process_age, state=Survey.age)
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(process_gender, state=Survey.gender)
    dp.register_callback_query_handler(process_stack, lambda call: call.data, state=Survey.stack)
    dp.register_callback_query_handler(stack_two, lambda call: call.data, state=Survey.stack)

    # dp.register_message_handler(process_time, state=Survey.time)

    dp.register_message_handler(echo)

    executor.start_polling(dp)
