#!/usr/bin/env python


import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from routers import router as main_router


API_TOKEN = os.environ['URBAN_BOT_TOKEN']
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()
dp.include_router(main_router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
