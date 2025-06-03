from typing import Annotated
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BufferedInputFile
from aiogram.filters import Command, StateFilter
import asyncio
import bot.keyboard as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from PIL import Image
from io import BytesIO

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


@router.message(F.photo, PhotoState.waiting_for_photo)
async def handle_photo_upload(message: Message, state: FSMContext):
        picture = message.photo[-1]
        file = await message.bot.get_file(picture.file_id)
        file_path = file.file_path

        photo_bytes = await message.bot.download_file(file_path)
        image = Image.open(BytesIO(photo_bytes.read()))

        image = image.convert("RGB")
        image = image.resize((800, 800))

        output_buffer = BytesIO()
        image.save(output_buffer, format="JPEG")
        output_buffer.seek(0)

        await message.answer_photo(
            photo=BufferedInputFile(
                file=output_buffer.read(),
                filename="restyled.jpg"
            ),
            caption="Your image style has been changed!",
        )

        
        
        await state.clear()
        await message.answer("Back to main.",
                            reply_markup=kb.buttons)


@router.message(Command("back"), StateFilter("*"))
async def handle_back_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Back to main.",
                        reply_markup=kb.buttons)