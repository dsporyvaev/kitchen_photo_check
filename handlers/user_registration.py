
from aiogram import html, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from services.api_sqlite import get_userx, add_user_name, add_user_lastname, add_user_login
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registration_router = Router()

class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    login = State()

@registration_router.message(Command('register'))
async def reg_handler(msg: Message, state:FSMContext) -> None:
    await msg.answer("working")
    user_id = msg.from_user.id
    if get_userx(user_id=user_id)['user_login'] == '':
        await state.set_state(Registration.first_name)  # Встановлення стану очікування імені
        await msg.answer("Please type your First Name:")
    else:
        await msg.answer("You have already registered! Type /start for start work!",
                                  reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/start"), ]],
                                                                   resize_keyboard=True))


@registration_router.message(Registration.first_name)
async def reg_handler(msg: Message, state:FSMContext) -> None:
    data = await state.update_data(first_name = msg.text)
    await state.set_state(Registration.last_name)
    await msg.answer(f"Nice to meet you {msg.text}!\n Now Last name:")

@registration_router.message(Registration.last_name)
async def reg_handler(msg: Message, state:FSMContext) -> None:
    data = await state.update_data(last_name = msg.text)
    await state.set_state(Registration.login)
    await msg.answer(f"Nice to meet you {msg.text}!\n Now create login:")

@registration_router.message(Registration.login)
async def reg_handler(msg: Message, state:FSMContext) -> None:
    data = await state.update_data(login = msg.text)
    user_id =msg.from_user.id
    user_login = data['login']
    user_firstname = data['first_name']
    user_lastname = data['last_name']
    add_user_name(user_id, user_firstname)
    add_user_lastname(user_id,user_lastname)
    add_user_login(user_id, user_login)
    await state.clear()
    await msg.answer(f"Your login now is : {msg.text}. You have successfully registered")
