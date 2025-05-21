from aiogram import types, Router, F
from bot_instance import bot
from filters.isregistered import IsRegistered
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.default.shifts import kb_night_shift
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.const_functions import get_date_for_tables
from services.api_sqlite import get_userx
from random import randint
from data.texts import night_shift_text
import os

night_shift_router = Router()

class NightShift(StatesGroup):
    night_shift = State()
    night_shift_inside_fifo = State()
    night_shift_outside_fifo = State()
    night_shift_red_boxes = State()
    night_shift_another = State()

@night_shift_router.message(IsRegistered(), F.text == "Night Shift")
async def night_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text=night_shift_text, reply_markup=kb_night_shift)
    await state.set_state(NightShift.night_shift)


@night_shift_router.message(F.text == "Inside FIFO", NightShift.night_shift)
async def inside_night_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo inside FIFO", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(NightShift.night_shift_inside_fifo)


@night_shift_router.message(F.photo, NightShift.night_shift_inside_fifo)
async def nightshift_inside_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "night_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Inside_fifo.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_night_shift)
    await state.set_state(NightShift.night_shift)



@night_shift_router.message(F.text == "Outside FIFO", NightShift.night_shift)
async def outside_night_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo outside FIFO", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(NightShift.night_shift_outside_fifo)


@night_shift_router.message(F.photo, NightShift.night_shift_outside_fifo)
async def nightshift_outside_photo(msg: types.Message, state: FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "night_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Outside_fifo.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_night_shift)
    await state.set_state(NightShift.night_shift)


@night_shift_router.message(F.text == "Red Boxes", NightShift.night_shift)
async def red_boxes_night_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo of Red Boxes", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(NightShift.night_shift_red_boxes)


@night_shift_router.message(F.photo, NightShift.night_shift_red_boxes)
async def nightshift_red_boxes_photo(msg: types.Message, state : FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "night_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Red_boxes.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_night_shift)
    await state.set_state(NightShift.night_shift)


@night_shift_router.message(F.text == "Other photos", NightShift.night_shift)
async def another_night_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send me another photos if you have to\nONLY IN ONE MESSAGE!", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(NightShift.night_shift_another)


@night_shift_router.message(F.photo, NightShift.night_shift_another)
async def nightshift_another_photo(msg: types.Message, state: FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "night_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, f"Another{randint(1, 999999999)}.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_night_shift)
    await state.set_state(NightShift.night_shift)



@night_shift_router.message(F.text == "Back", NightShift.night_shift_another)
@night_shift_router.message(F.text == "Back", NightShift.night_shift_red_boxes)
@night_shift_router.message(F.text == "Back", NightShift.night_shift_outside_fifo)
@night_shift_router.message(F.text == "Back", NightShift.night_shift_inside_fifo)
async def get_back(msg: types.Message, state: FSMContext):
    await msg.answer(text="Back to Night Shift", reply_markup=kb_night_shift)
    await state.set_state(NightShift.night_shift)