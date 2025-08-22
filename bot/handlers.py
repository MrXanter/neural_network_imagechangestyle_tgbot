from typing import Annotated
from aiogram import Router, F
from aiogram.types import Message, BufferedInputFile, CallbackQuery
from aiogram.filters import Command, StateFilter
import asyncio
import bot.keyboard as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from PIL import Image
from io import BytesIO
from models.neural_processor import AnimeGANProcessor

router = Router()


class PhotoState(StatesGroup):
    waiting_for_photo = State()

PhotoMessage = Annotated[Message, F.photo]

gan_processor = AnimeGANProcessor({
    "hosoda": "models/hosoda_mamoru.pth",
    "kon": "models/kon_satoshi.pth",
    "miyazaki": "models/miyazaki_hayao.pth",
    "shinkai": "models/shinkai_makoto.pth"
})

style_choice = {}



# Start command handler
@router.message(Command("start"))
async def start_command_handler(message: Message):
    await message.answer("Hello! I'm an image restyler bot.\nPlease send me an image.",
                        reply_markup = kb.buttons)



@router.message(F.text == "send the image")
async def handle_photo(message: PhotoMessage, state: FSMContext):
    await message.answer("Choose a preferred style:",
                        reply_markup=kb.choose_style)



@router.callback_query(F.data.startswith("style_"))
async def process_style_callback(callback: CallbackQuery, state: FSMContext):
    chosen_style = callback.data.split("_")[1]  # Gets 'hosoda', 'kon', etc.
    style_choice[callback.from_user.id] = chosen_style
    
    await callback.answer(f"Style {chosen_style} selected!")
    await state.set_state(PhotoState.waiting_for_photo)
    await callback.message.answer("Waiting for an image.",
                        reply_markup=kb.back_button)



@router.message(F.photo, PhotoState.waiting_for_photo)
async def handle_photo_upload(message: Message, state: FSMContext):
        await message.answer("Processing...")
        picture = message.photo[-1]
        file = await message.bot.get_file(picture.file_id)
        file_path = file.file_path
        photo_bytes = await message.bot.download_file(file_path)
        image = Image.open(BytesIO(photo_bytes.read()))

        # image = image.convert("RGB")
        # image = image.resize((512, 512))

        output_buffer = BytesIO()
        image.save(output_buffer, format="JPEG")
        output_buffer.seek(0)

        await message.answer_photo(
            photo=BufferedInputFile(
                file=output_buffer.read(),
                filename="restyled.jpg"
            ),
            caption="Here is your image!",
        )

        
        
        await state.clear()
        await message.answer("Back to main.",
                            reply_markup=kb.buttons)


@router.message(Command("back"), StateFilter("*"))
async def handle_back_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Back to main.",
                        reply_markup=kb.buttons)