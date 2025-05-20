from filters.isadmin import IsAdmin
from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os

admin_router = Router()

@admin_router.message(F.text == "Look for photo reports report")
async def choose_other_day(msg: Message):
    admin_kb_other = InlineKeyboardBuilder()

    with os.scandir('data/photos') as files:
        for file in files:
            inline_btn = InlineKeyboardButton(text=file.name, callback_data=f"datefile:{file.name}")
            admin_kb_other.add(inline_btn)
            print(file.name)

    await msg.answer(text="Choose date to check:\n", reply_markup=admin_kb_other.as_markup())