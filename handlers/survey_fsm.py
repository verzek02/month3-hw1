from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from database.base import insert_survey


# Finite State Machine
class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    stack = State()
    language = State()
    experience = State()
    salary = State()


async def start_survey(message: types.Message):
    await Survey.name.set()

    await message.answer("Как вас зовут?")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)

    await Survey.next()
    await message.answer("Сколько вам лет?")


async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Введите только цифры!")
    elif int(age) > 100 or int(age) < 10:
        await message.answer("Введите нормальный возраст")
    else:
        async with state.proxy() as data:
            data['age'] = int(age)
            print(data)

        await Survey.next()

        kb = types.ReplyKeyboardMarkup()
        kb.add("Мужской", "Женский")
        await message.answer("Ваш пол?", reply_markup=kb)


async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    # await message.answer(types.ReplyKeyboardRemove)

    await Survey.next()

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('Back-end', callback_data='back'),
           types.InlineKeyboardButton('Front-end', callback_data='front'))
    await message.answer("Какое у вас направление?", reply_markup=kb)


async def process_stack(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'back':
        """Это обработчик для кнопки back"""

        async with state.proxy() as data:
            data['stack'] = 'back'
            await callback.message.answer('Круто!')

            kb = types.InlineKeyboardMarkup(row_width=2)
            kb.add(types.InlineKeyboardButton('Python', callback_data='py'),
                   types.InlineKeyboardButton('PHP', callback_data='php')),
            kb.add(types.InlineKeyboardButton('Java', callback_data='java'),
                   types.InlineKeyboardButton('C#', callback_data='c'))
        await Survey.next()
        await callback.message.answer('Какими языками владеете?', reply_markup=kb)
    elif callback.data == 'front':
        """Это обработчик для кнопки фронт"""
        async with state.proxy() as data:
            data['stack'] = 'front'
            await callback.message.answer("норм.")
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton('JavaScript', callback_data='js'),
                   types.InlineKeyboardButton('TypeScript', callback_data='ts')),
        await Survey.next()
        await callback.message.answer('Какими языками владеете?', reply_markup=kb)


async def process_languages(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['languages'] = callback.data
        if callback.data == 'py' or callback.data == 'php' or callback.data == 'java' or callback.data == 'c':
            await callback.message.answer("Базар жок!")
        elif callback.data == 'js' or callback.data == 'ts':
            await callback.message.answer('u stupid')
        else:
            await callback.message.answer('u stupid')

    await Survey.next()
    await callback.message.answer('Сколько вы работаете в этой сфере?')
    await callback.message.answer("Если вы работали меньше года то можете написать так: 0.5 и т.д")


async def process_experience(message: types.Message, state: FSMContext):
    time = message.text

    try:
        time_float = float(time)
    except ValueError:
        await message.answer("Введите только цифры!")
    else:
        if time_float > 15:
            await message.answer('Алдаба!')
        else:
            async with state.proxy() as data:
                data['time'] = time_float
                print(data)
                insert_survey(data)

            await message.answer("Спасибо! За участие в нашем опросе.")
            await state.finish()


