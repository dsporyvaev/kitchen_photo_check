from aiogram import types, Router, F
from filters.isregistered import IsRegistered
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot_instance import bot
from keyboards.default.shifts import kb_morning_shift, kb_oil
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.const_functions import get_date_for_tables
from services.api_sqlite import get_userx
from random import randint
from data.texts import morn_shift
import os

morning_shift_router = Router()



class MorningShift(StatesGroup):
    morning_shift = State()
    morning_shift_oil_quality = State()
    morning_shift_oil_quality_left = State()
    morning_shift_oil_quality_right = State()
    morning_shift_oil_quality_central = State()
    morning_shift_oil_quality_kentucky = State()
    morning_shift_red_boxes = State()
    morning_shift_containers = State()
    morning_shift_fifo = State()
    morning_shift_sink = State()
    morning_shift_table = State()
    morning_shift_another = State()


@morning_shift_router.message(IsRegistered(), F.text == "Morning Shift")
async def morning_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text=morn_shift, reply_markup=kb_morning_shift)
    await state.set_state(MorningShift.morning_shift)


@morning_shift_router.message(F.text == "Oil Quality", MorningShift.morning_shift)
async def oil_quality_morning_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Choose oil category", reply_markup=kb_oil)
    await state.set_state(MorningShift.morning_shift_oil_quality)


@morning_shift_router.message(F.text == "Left", MorningShift.morning_shift_oil_quality)
async def oil_quality_morning_shift_left(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send photo of left oil quality", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_oil_quality_left)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_oil_quality_left)
async def morning_oli_left_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Oil_left.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_oil)
    await state.set_state(MorningShift.morning_shift_oil_quality)


@morning_shift_router.message(F.text == "Right", MorningShift.morning_shift_oil_quality)
async def oil_quality_morning_shift_right(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send photo of right oil quality", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_oil_quality_right)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_oil_quality_right)
async def morning_oli_right_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Oil_right.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_oil)
    await state.set_state(MorningShift.morning_shift_oil_quality)


@morning_shift_router.message(F.text == "Central", MorningShift.morning_shift_oil_quality)
async def oil_quality_morning_shift_right(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send photo of central oil quality", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_oil_quality_central)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_oil_quality_central)
async def morning_oil_central_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Oil_central.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_oil)
    await state.set_state(MorningShift.morning_shift_oil_quality)


@morning_shift_router.message(F.text == "Kentucky", MorningShift.morning_shift_oil_quality)
async def oil_quality_morning_shift_right(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send photo of kentucky oil quality", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_oil_quality_kentucky)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_oil_quality_kentucky)
async def morning_oli_kentucky_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Oil_kentucky.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_oil)
    await state.set_state(MorningShift.morning_shift_oil_quality)


@morning_shift_router.message(F.text == "Red Boxes", MorningShift.morning_shift)
async def morning_shift_red_boxes(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send photo of Red Boxes", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_red_boxes)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_red_boxes)
async def morning_red_boxes_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Red_boxes.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
    await state.set_state(MorningShift.morning_shift)



@morning_shift_router.message(F.text == "Container", MorningShift.morning_shift)
async def morning_shift_containers(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send photo of Containers", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_containers)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_containers)
async def morning_containers_photo(msg: types.Message, state: FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Containers.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
    await state.set_state(MorningShift.morning_shift)



@morning_shift_router.message(F.text == "FIFO", MorningShift.morning_shift)
async def fifo_morning_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo of FIFO.\n ALL PHOTOS IN ONE MESSAGE", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_fifo)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_fifo)
async def morning_fifo_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, f"Fifo{randint(1, 999999999)}.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
    await state.set_state(MorningShift.morning_shift)


@morning_shift_router.message(F.text == "Sink", MorningShift.morning_shift)
async def sink_morning_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo of Sink", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_sink)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_sink)
async def morning_sink_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Sink.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
    await state.set_state(MorningShift.morning_shift)


@morning_shift_router.message(F.text == "Table", MorningShift.morning_shift)
async def table_morning_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo of table", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_table)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_table)
async def morning_table_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Table.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
    await state.set_state(MorningShift.morning_shift)


@morning_shift_router.message(F.text == "Other photos", MorningShift.morning_shift)
async def another_night_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send me another photos if you have to\nONLY IN ONE MESSAGE!", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MorningShift.morning_shift_another)


@morning_shift_router.message(F.photo, MorningShift.morning_shift_another)
async def nightshift_another_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "morning_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, f"Another{randint(1, 999999999)}.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_morning_shift)
    await state.set_state(MorningShift.morning_shift)



@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_oil_quality)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_red_boxes)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_table)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_sink)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_containers)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_fifo)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_another)
async def get_back(msg: types.Message, state: FSMContext):
    await msg.answer(text="Back to morning Shift", reply_markup=kb_morning_shift)
    await state.set_state(MorningShift.morning_shift)


@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_oil_quality_left)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_oil_quality_right)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_oil_quality_central)
@morning_shift_router.message(F.text == "Back", MorningShift.morning_shift_oil_quality_kentucky)
async def get_back_to_oil(msg: types.Message, state: FSMContext):
    await msg.answer(text="Back to oil quality", reply_markup=kb_oil)
    await state.set_state(MorningShift.morning_shift_oil_quality)