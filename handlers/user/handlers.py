
from aiogram import html, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from services.api_sqlite import get_userx
from data.config import admins
from keyboards.default.keyboard_menu import kb_start
from keyboards.default.admin import admin_kb_start
from filters.isregistered import IsRegistered
from aiogram.fsm.context import FSMContext
from handlers.user.mid_shift import MidShift
legit_router = Router()


@legit_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message.from_user.id not in admins:
        await message.answer(f'Hello {message.from_user.full_name} {message.from_user.id}!\n'
                                 'Choose shift to send some photos ^_^', reply_markup=kb_start)
    else:
        await message.answer(f'Hello admin!\n Choose day to check some photos', reply_markup=admin_kb_start)


@legit_router.message(Command('help'))
async def help_handler(msg: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await msg.answer(f'This is bot for checking some photos from kitchen')
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await msg.answer("Nice try!")




@legit_router.message(F.text == 'Menu', MidShift.mid_shift)
# @legit_router.message(F.text == 'Menu', NightShift.night_shift)
# @legit_router.message(F.text == 'Menu', MorningShift.morning_shift)
@legit_router.message(IsRegistered(), F.text == 'Menu')
async def menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Choose your shift", reply_markup=kb_start)


