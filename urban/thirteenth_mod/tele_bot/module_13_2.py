#!/usr/bin/env python


import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command


API_TOKEN = os.environ['URBAN_BOT_TOKEN']
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')
    print('Привет! Я бот, помогающий твоему здоровью.')


@dp.message()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
