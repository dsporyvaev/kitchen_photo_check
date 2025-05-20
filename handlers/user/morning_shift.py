# from aiogram import types
# from loader import dp, bot
# from filters.isregistered import IsRegistered
# from aiogram.dispatcher import FSMContext
# from keyboards.default.shifts import kb_night_shift, kb_morning_shift, kb_oil
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from utils.const_functions import get_date_for_tables
# from services.api_sqlite import get_userx
# from random import randint
# from data.texts import morn_shift
# import os
#
#
# @dp.message_handler(IsRegistered(), text ="Morning Shift")
# async def morning_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text=morn_shift, reply_markup=kb_morning_shift)
#     await state.set_state("morning_shift")
#
#
# @dp.message_handler(text = "Oil Quality", state="morning_shift")
# async def oilquality_morning_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Choose oil kategory", reply_markup=kb_oil)
#     await state.set_state("morning_shift_oil_quality")
#
#
# @dp.message_handler(text = "Left", state="morning_shift_oil_quality")
# async def oilquality_morning_shift_left(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Send photo of left oil quality", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_oil_quality_left")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_oil_quality_left")
# async def morning_oli_left_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Oil_left.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_oil)
#     await state.set_state("morning_shift_oil_quality")
#
#
# @dp.message_handler(text = "Right", state="morning_shift_oil_quality")
# async def oilquality_morning_shift_right(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Send photo of right oil quality", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_oil_quality_right")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_oil_quality_right")
# async def morning_oli_right_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Oil_right.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_oil)
#     await state.set_state("morning_shift_oil_quality")
#
#
# @dp.message_handler(text = "Central", state="morning_shift_oil_quality")
# async def oilquality_morning_shift_right(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Send photo of central oil quality", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_oil_quality_central")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_oil_quality_central")
# async def morning_oli_central_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Oil_central.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_oil)
#     await state.set_state("morning_shift_oil_quality")
#
#
# @dp.message_handler(text = "Kentucky", state="morning_shift_oil_quality")
# async def oilquality_morning_shift_right(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Send photo of kentucky oil quality", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_oil_quality_kentucky")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_oil_quality_kentucky")
# async def morning_oli_kentucky_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Oil_kentucky.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_oil)
#     await state.set_state("morning_shift_oil_quality")
#
#
# @dp.message_handler(text = "Red Boxes", state="morning_shift")
# async def morning_shift_redboxes(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Send photo of Red Boxes", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_redboxes")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_redboxes")
# async def morning_redboxes_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Red_boxes.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
#     await state.set_state("morning_shift")
#
#
#
# @dp.message_handler(text = "Container", state="morning_shift")
# async def morning_shift_containers(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Send photo of Containers", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_containers")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_containers")
# async def morning_containers_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Containers.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
#     await state.set_state("morning_shift")
#
#
#
# @dp.message_handler(text = "FIFO", state="morning_shift")
# async def fifo_morning_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Now send me photo of FIFO.\n ALL PHOTOS IN ONE MESSAGE", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_fifo")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_fifo")
# async def morning_fifo_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Fifo.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
#     await state.set_state("morning_shift")
#
#
# @dp.message_handler(text = "Sink", state="morning_shift")
# async def sink_morning_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Now send me photo of Sink", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_sink")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_sink")
# async def morning_sink_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "Sink.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
#     await state.set_state("morning_shift")
#
#
# @dp.message_handler(text = "Table", state="morning_shift")
# async def table_morning_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Now send me photo of table", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_table")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_table")
# async def morning_table_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, "table.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
#     await state.set_state("morning_shift")
#
#
# @dp.message_handler(text = "Other photos", state="morning_shift")
# async def another_night_shift(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Send me another photos if you have to\nONLY IN ONE MESSAGE!", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
#     await state.set_state("morning_shift_another")
#
#
# @dp.message_handler(content_types="photo", state="morning_shift_another")
# async def nightshift_another_photo(msg: types.Message, state = FSMContext):
#
#     curr_date = get_date_for_tables(False)
#     last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
#     first_name = get_userx(user_id = msg.from_user.id)["user_name"]
#     save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
#     os.makedirs(save_path, exist_ok=True)
#     await bot.download_file_by_id(msg.photo[-1].file_id, os.path.join(save_path, f"Another{randint(1, 999999999)}.jpg"))
#     await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
#     await state.set_state("morning_shift")
#
#
#
# @dp.message_handler(text = "Back", state="morning_shift_oil_quality")
# @dp.message_handler(text = "Back", state="morning_shift_redboxes")
# @dp.message_handler(text = "Back", state="morning_shift_table")
# @dp.message_handler(text = "Back", state="morning_shift_sink")
# @dp.message_handler(text = "Back", state="morning_shift_containers")
# @dp.message_handler(text = "Back", state="morning_shift_fifo")
# @dp.message_handler(text = "Back", state="morning_shift_another")
# async def get_back(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Back to morning Shift", reply_markup=kb_morning_shift)
#     await state.set_state("morning_shift")
#
#
# @dp.message_handler(text = "Back", state="morning_shift_oil_quality_left")
# @dp.message_handler(text = "Back", state="morning_shift_oil_quality_right")
# @dp.message_handler(text = "Back", state="morning_shift_oil_quality_central")
# @dp.message_handler(text = "Back", state="morning_shift_oil_quality_kentucky")
# async def get_back_to_oil(msg: types.Message, state: FSMContext):
#     await msg.answer(text="Back to oil quality", reply_markup=kb_oil)
#     await state.set_state("Oil Quality")