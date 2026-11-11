import os
import logging
import asyncio

from aiogram import Router, Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    router =  Router()
    dp = Dispatcher()
    dp.include_routers(router)

    print ("Run polling...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.run_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())