from typing import Annotated
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
import bot.keyboard as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()


class PhotoState(StatesGroup):
    waiting_for_photo = State()

PhotoMessage = Annotated[Message, F.photo]



# Start command handler
@router.message(Command("start"))
async def start_command_handler(message: Message):
    await message.answer("Hello! I'm an image restyler bot.\nPlease send me an image.",
                          reply_markup = kb.buttons)


@router.message(F.text == "send the image")
async def handle_photo(message: PhotoMessage, state: FSMContext):
    await state.set_state(PhotoState.waiting_for_photo)
    await message.answer("Waiting for an image.",
                        reply_markup=kb.back_button)


@router.message(PhotoState.waiting_for_photo)
async def handle_photo_upload(message: Message, state: FSMContext):
        file_id = message.photo[-1].file_id
        await message.answer_photo(file_id, caption="Here is your image!")
        
        
        await state.clear()
        await message.answer("Back to main.",
                            reply_markup=kb.buttons)


@router.message(Command("back"))
async def handle_back(message: Message):
    await message.answer("Back to main.",
                        reply_markup=kb.buttons)