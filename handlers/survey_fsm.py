from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types



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

    kb = types.InlineKeyboardMarkup
    kb.add(types.InlineKeyboardButton('Back-end', callback_data='back'),
           types.InlineKeyboardButton('Front-end', callback_data='front'))
    await message.answer("Какое у вас направление?")

async def process_stack(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'back':
        async with state.proxy() as data:
            data['stack'] = 'back'

        kb = types.InlineKeyboardMarkup
        kb.add(types.InlineKeyboardButton('python', callback_data='py'),
               types.InlineKeyboardButton('PHP', callback_data='php'),
               types.InlineKeyboardButton('Java', callback_data='java'),
               types.InlineKeyboardButton('C#', callback_data='c'))





async def process_time(message: types.Message, state: FSMContext):
    time = message.text
    if not time.isdigit():
        await message.answer("Введите только цифры!")
    elif float(time) < 1:
        await message.answer("Если вы работали меньше года то можете написать так: 0.5 и т.д")

    else:
        async with state.proxy() as data:
            data['time'] = int(time)
            print(data)
        await message.answer("Спасибо! За участие в нашем опросе.")
        await state.finish()
