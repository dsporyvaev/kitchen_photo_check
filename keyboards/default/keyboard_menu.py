from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="but1"),
            KeyboardButton(text="but2"),

        ],
        [
            KeyboardButton(text="inline menu"),
            KeyboardButton(text="but4"),
        ]
    ],

    resize_keyboard=True

)




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