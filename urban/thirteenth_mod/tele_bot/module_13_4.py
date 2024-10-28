#!/usr/bin/env python


import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


API_TOKEN = os.environ['URBAN_BOT_TOKEN']
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()


class UserState(StatesGroup):
    calories = State()
    age = State()
    growth = State()
    weight = State()


@dp.message(CommandStart())
async def start(message: types.Message, state: FSMContext) -> None:
    await state.set_state(UserState.calories)
    await message.answer("Привет! Напишите 'Calories', чтобы начать.")


@dp.message(UserState.calories)
async def set_age(message: types.Message, state: FSMContext) -> None:
    if message.text.lower() == 'calories':
        await state.set_state(UserState.age)
        await message.answer('Введите свой возраст:')


@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer('Введите свой рост:')


@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext) -> None:
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес:')


@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал.')
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
