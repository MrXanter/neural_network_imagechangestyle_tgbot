from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 

buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="send the image")],
    [KeyboardButton(text="help")]
    ], resize_keyboard=True, input_field_placeholder="Choose the image")

back_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/back")]
    ],resize_keyboard=True, input_field_placeholder="Press back to return to menu")