from aiogram.types import ReplyKeyboardMarkup, KeyboardButton






kb_register = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/register')
        ]
    ], resize_keyboard=True
)

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Morning Shift"),
            KeyboardButton(text="Mid Shift"),
            KeyboardButton(text="Night Shift"),
        ]
    ], resize_keyboard=True

)