# from aiogram import types
# from loader import dp, bot
# from filters.isregistered import IsRegistered
# from aiogram.dispatcher import FSMContext
# from keyboards.default.shifts import kb_night_shift
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from utils.const_functions import get_date_for_tables
# from services.api_sqlite import get_userx
# from random import randint
# from data.texts import night_shift_text
# import os
#
#
# @dp.message_handler(IsRegistered(), text ="Night Shift")
# async def night_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text=night_shift_text, reply_markup=kb_night_shift)
#     await state.set_state("night_shift")
#
#
# @dp.message_handler(text = "Inside FIFO", state="night_shift")
# async def inside_night_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Now send me photo inside FIFO", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("night_shift_inside_fifo")
#
#
# @dp.message_handler(content_types="photo", state="night_shift_inside_fifo")
# async def nightshift_inside_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "night_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Inside_FIFO.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_night_shift)
#     await state.set_state("night_shift")
#
#
#
# @dp.message_handler(text = "Outside FIFO", state="night_shift")
# async def outside_night_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Now send me photo outside FIFO", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("night_shift_outside_fifo")
#
#
# @dp.message_handler(content_types="photo", state="night_shift_outside_fifo")
# async def nightshift_outside_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "night_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Outside_Fifo.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_night_shift)
#     await state.set_state("night_shift")
#
#
# @dp.message_handler(text = "Red Boxes", state="night_shift")
# async def redboxes_night_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Now send me photo of Red Boxes", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("night_shift_redboxes")
#
#
# @dp.message_handler(content_types="photo", state="night_shift_redboxes")
# async def nightshift_redboxes_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "night_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Red_Boxes.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_night_shift)
#     await state.set_state("night_shift")
#
#
# @dp.message_handler(text = "Other photos", state="night_shift")
# async def another_night_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Send me another photos if you have to\nONLY IN ONE MESSAGE!", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("night_shift_another")
#
#
# @dp.message_handler(content_types="photo", state="night_shift_another")
# async def nightshift_another_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "night_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, f"Another{randint(1, 999999999)}.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_night_shift)
#     await state.set_state("night_shift")
#
#
#
# @dp.message_handler(text = "Back", state="night_shift_another")
# @dp.message_handler(text = "Back", state="night_shift_redboxes")
# @dp.message_handler(text = "Back", state="night_shift_outside_fifo")
# @dp.message_handler(text = "Back", state="night_shift_inside_fifo")
# @dp.message_handler(text = "Back", state="night_shift_another")
# async def get_back(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Back to Night Shift", reply_markup=kb_night_shift)
#     await state.set_state("night_shift")