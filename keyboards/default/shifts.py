from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_mid_shift = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sink"),
            KeyboardButton(text="Floor"),
            KeyboardButton(text="Table"),
            
        ],
        [
            KeyboardButton(text="Red Boxes"),
            KeyboardButton(text="Other photos"),
        ],
        [
            KeyboardButton(text="Menu")
        ]

    ],
    
    resize_keyboard=True
     
    )


kb_night_shift = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Inside FIFO"),
            KeyboardButton(text="Outside FIFO"),
            
        ],
        [
            KeyboardButton(text="Red Boxes"),
            KeyboardButton(text="Other photos"),
        ],
        [
            KeyboardButton(text="Menu")
        ]

    ],
    
    resize_keyboard=True
     
    )


kb_morning_shift = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oil Quality"),
            KeyboardButton(text="Red Boxes"),
            KeyboardButton(text="Container"),
            
        ],
        [
            KeyboardButton(text="FIFO"),
            KeyboardButton(text="Sink"),
            KeyboardButton(text="Table"),
        ],
        [
            KeyboardButton(text="Other photos")
        ],
        [
            KeyboardButton(text="Menu")
        ]

    ],
    
    resize_keyboard=True
     
    )


kb_oil = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Left"),
            KeyboardButton(text="Central"),
        ],
        [
            KeyboardButton(text="Right"),
            KeyboardButton(text="Kentucky"),
        ],
        [
            KeyboardButton(text="Back")
        ]
    ], resize_keyboard=True
)