from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="send the image")],
    [KeyboardButton(text="help")]
    ], resize_keyboard=True, input_field_placeholder="Choose the image")

back_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/back")]
    ],resize_keyboard=True, input_field_placeholder="Press back to return to menu")

choose_style = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Hosoda Mamoru", callback_data="style_hosoda")],
    [InlineKeyboardButton(text="Kon Satoshi", callback_data="style_kon")],
    [InlineKeyboardButton(text="Miyazaki hayao", callback_data="style_miyazaki")],
    [InlineKeyboardButton(text="Shinkai Makoto", callback_data="style_shinkai")]
])