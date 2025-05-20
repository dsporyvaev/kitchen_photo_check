from aiogram import types

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot_instance import bot
from keyboards.default.shifts import kb_mid_shift
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.const_functions import get_date_for_tables
from services.api_sqlite import get_userx
from random import randint
from filters.isregistered import IsRegistered
from data.texts import mid_shift_text
import os
mid_shift_router = Router()

class MidShift(StatesGroup):
    mid_shift = State()
    mid_shift_sink = State()
    mid_shift_floor = State()
    mid_shift_table = State()
    mid_shift_red_boxes = State()
    mid_shift_another = State()

@mid_shift_router.message(IsRegistered(), F.text =="Mid Shift")
async def mid_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text=mid_shift_text, reply_markup=kb_mid_shift)
    await state.set_state(MidShift.mid_shift)


@mid_shift_router.message(F.text == "Sink", MidShift.mid_shift)
async def sink_mid_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo of Sink", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MidShift.mid_shift_sink)


@mid_shift_router.message(F.photo, MidShift.mid_shift_sink)
async def midshift_sink_photo(msg: types.Message, state: FSMContext):
    
    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "mid_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Sink.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_mid_shift)
    await state.set_state(MidShift.mid_shift)

    
    
@mid_shift_router.message(F.text == "Floor", MidShift.mid_shift)
async def floor_mid_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo of Floor", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MidShift.mid_shift_floor)


@mid_shift_router.message(F.photo, MidShift.mid_shift_floor)
async def midshift_floor_photo(msg: types.Message, state: FSMContext):
    
    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "mid_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Floor.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_mid_shift)
    await state.set_state(MidShift.mid_shift)


@mid_shift_router.message(F.text == "Table", MidShift.mid_shift)
async def table_mid_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo of table", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MidShift.mid_shift_table)


@mid_shift_router.message(F.photo, MidShift.mid_shift_table)
async def midshift_table_photo(msg: types.Message, state : FSMContext):
    
    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "mid_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Table.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_mid_shift)
    await state.set_state(MidShift.mid_shift)



@mid_shift_router.message(F.text == "Red Boxes", MidShift.mid_shift)
async def rb_mid_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Now send me photo of Red Boxes", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MidShift.mid_shift_red_boxes)


@mid_shift_router.message(F.photo, MidShift.mid_shift_red_boxes)
async def midshift_rb_photo(msg: types.Message, state : FSMContext):
    
    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "mid_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, "Red_boxes.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_mid_shift)
    await state.set_state(MidShift.mid_shift)


@mid_shift_router.message(F.text == "Other photos", MidShift.mid_shift)
async def another_mid_shift(msg: types.Message, state: FSMContext):
    await msg.answer(text="Send me another photos if you have to\nONLY IN ONE MESSAGE!", reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Back")]], resize_keyboard=True))
    await state.set_state(MidShift.mid_shift_another)


@mid_shift_router.message(F.photo, MidShift.mid_shift_another)
async def midshift_another_photo(msg: types.Message, state: FSMContext):

    curr_date = get_date_for_tables(False)
    last_name = get_userx(user_id = msg.from_user.id)["user_lastname"]
    first_name = get_userx(user_id = msg.from_user.id)["user_name"]
    save_path = os.path.join("data", "photos", curr_date, "mid_shift", f"{last_name}_{first_name}")
    os.makedirs(save_path, exist_ok=True)
    photo = msg.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, os.path.join(save_path, f"Another{randint(1, 999999999)}.jpg"))
    await msg.answer("Photo successfully downloaded!", reply_markup=kb_mid_shift)
    await state.set_state(MidShift.mid_shift)


@mid_shift_router.message(F.text == "Back", MidShift.mid_shift_sink)
@mid_shift_router.message(F.text == "Back", MidShift.mid_shift_floor)
@mid_shift_router.message(F.text == "Back", MidShift.mid_shift_table)
@mid_shift_router.message(F.text == "Back", MidShift.mid_shift_red_boxes)
@mid_shift_router.message(F.text == "Back", MidShift.mid_shift_another)

async def back_but(msg: types.Message, state: FSMContext):
    await msg.answer(text="Back to Mid Shift", reply_markup=kb_mid_shift)
    await state.set_state(MidShift.mid_shift)

