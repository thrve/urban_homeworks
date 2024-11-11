#!/usr/bin/env python


from aiogram import Router
from aiogram import F
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import ButtonText, get_inline_keyboard


router = Router()


@router.message(F.text == ButtonText.calculate)
async def main_menu(message: Message) -> None:
    await message.answer('Выберите опцию:', reply_markup=get_inline_keyboard())


@router.callback_query(F.data == 'formulas')
async def get_formulas(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    formula = (
        'Формула Миффлина-Сан Жеора:\n'
        'Для мужчин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n'
        'Для женщин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161'
    )
    await callback_query.message.answer(formula)
