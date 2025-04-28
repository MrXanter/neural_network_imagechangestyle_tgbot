from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os
from bot.handlers import router

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(router)

async def main():
    print("Bot has started.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot has stopped.")