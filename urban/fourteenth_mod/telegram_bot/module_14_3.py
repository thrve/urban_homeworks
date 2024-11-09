#!/usr/bin/env python


import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram.utils import markdown
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from keyboards.common_keyboards import get_on_start_kb, get_inline_keyboard, get_bying_menu
from keyboards.common_keyboards import ButtonText


API_TOKEN = os.environ['URBAN_BOT_TOKEN']
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        f'Привет, {markdown.hbold(message.from_user.full_name)}!',
        parse_mode=ParseMode.HTML,
        reply_markup=get_on_start_kb(),
    )


@dp.message(F.text == ButtonText.buy)
async def get_buying_list(message: Message) -> None:
    prod_path = '/home/thrv/.playground/urban/urban/urban/fourteenth_mod/telegram_bot/images/prod_'
    for i in range(1, 5):
        product_name = getattr(ButtonText, f'product{i}')
        await message.answer_photo(
            photo=FSInputFile(f'{prod_path}{i}.jpg'),
            caption=f'Название: {product_name:} | Описание: {product_name:} | Цена: {i * 100}',
            parse_mode='HTML',
        )
    await message.answer('Выберите продукт для покупки:', reply_markup=get_bying_menu())


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    await callback_query.message.answer('Вы успешно приобрели продукт!')


@dp.message(F.text == ButtonText.calculate)
async def main_menu(message: Message) -> None:
    await message.answer('Выберите опцию:', reply_markup=get_inline_keyboard())


@dp.message(F.text == ButtonText.info)
async def get_info(message: Message) -> None:
    await message.answer(
        text='Тут, по-видимому, должна быть бескрайне полезная инфа',
        reply_markup=ReplyKeyboardRemove(),
    )


@dp.callback_query(F.data == 'formulas')
async def get_formulas(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    formula = (
        'Формула Миффлина-Сан Жеора:\n'
        'Для мужчин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n'
        'Для женщин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161'
    )
    await callback_query.message.answer(formula)


@dp.callback_query(F.data == 'calories')
async def set_age(callback_query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(UserState.age)
    await callback_query.answer()
    await callback_query.message.answer('Введите свой возраст:')


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer('Введите свой рост:')


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес:')


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext) -> None:
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
