from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎮 Играть"),
            KeyboardButton(text="👤 Пользователь")
        ]
    ],
    resize_keyboard=True
    
)