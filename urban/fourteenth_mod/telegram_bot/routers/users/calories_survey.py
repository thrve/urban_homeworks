#!/usr/bin/env python


from aiogram import Router
from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@router.callback_query(F.data == 'calories')
async def set_age(callback_query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(UserState.age)
    await callback_query.answer()
    await callback_query.message.answer('Введите свой возраст:')


@router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer('Введите свой рост:')


@router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext) -> None:
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес:')


@router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал.')
    await state.clear()
