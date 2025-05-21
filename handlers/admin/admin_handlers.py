from filters.isadmin import IsAdmin
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot_instance import bot
import os

admin_router = Router()

@admin_router.message(IsAdmin(), F.text == "Look for photo reports report")
async def choose_other_day(msg: Message):
    admin_kb_other = InlineKeyboardBuilder()
    if os.listdir('data/photos'):
        print("not empty")
        with os.scandir('data/photos') as files:
            for file in files:
                inline_btn = InlineKeyboardButton(text=file.name, callback_data=f"datefile:{file.name}")
                admin_kb_other.add(inline_btn)
                print(file.name)

        await msg.answer(text="Choose date to check:\n", reply_markup=admin_kb_other.as_markup())
    else:
        await msg.answer(text="Right now there is nothing to show you!")

@admin_router.callback_query(lambda c: c.data.startswith('datefile:'))
async def process_date_callback(callback_query: CallbackQuery):
    selected_date = callback_query.data.split(':')[1]  # Извлекаем дату из callback data
    print(selected_date)
    data_keyboard = InlineKeyboardBuilder()

    ikb1 = InlineKeyboardButton(text="Morning shift", callback_data=f"shift:morning:{selected_date}")
    ikb2 = InlineKeyboardButton(text="Mid shift", callback_data=f"shift:mid:{selected_date}")
    ikb3 = InlineKeyboardButton(text="Night shift", callback_data=f"shift:night:{selected_date}")
    data_keyboard.add(ikb1, ikb2, ikb3)
    await bot.send_message(chat_id=callback_query.from_user.id, text=f"Choose shift for {selected_date}",
                           reply_markup=data_keyboard.as_markup())


@admin_router.callback_query(lambda c: c.data.startswith('shift:'))
async def process_shift_callback(callback_query: CallbackQuery):
    shift = callback_query.data.split(':')[1]
    selected_date = callback_query.data.split(':')[2]
    print(shift)
    keyboard = InlineKeyboardBuilder()
    try:
        with os.scandir(f'data/photos/{selected_date}/{shift}_shift') as files:
            for file in files:
                print(len("user:{selected_date}:{shift}:1"))
                inline_btn = InlineKeyboardButton(text=file.name,
                                                  callback_data=f"user:{selected_date}:{shift}:{file.name}")
                keyboard.add(inline_btn)
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"{selected_date}\n{shift} shift\nChoose user:\n", reply_markup=keyboard.as_markup())
    except Exception as err:
        await bot.send_message(chat_id=callback_query.from_user.id, text="Nobody has sent photos yet")


@admin_router.callback_query(lambda c: c.data.startswith('user:'))
async def process_photo_callback(callback_query: CallbackQuery):
    shift = callback_query.data.split(':')[2]
    data = callback_query.data.split(':')[1]
    name = callback_query.data.split(':')[3]
    file_path = f'data/photos/{data}/{shift}_shift/{name}'
    with os.scandir(file_path) as files:
        for file in files:
            print(file_path + f"/{file.name}.jpg")
            photo_path = file_path + f"/{file.name}"
            photo = FSInputFile(photo_path)
            await callback_query.message.answer_photo(photo=photo, caption=f"{file.name}")