#!/usr/bin/env python


from re import Match
from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards.keyboards import ButtonText
from validators.email_validator import valid_email_filter
from validators.age_validator import valid_age_filter
from crud_functions import add_user, is_included


router = Router()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@router.message(F.text == ButtonText.registration)
async def sing_up(message: Message, state: FSMContext) -> None:
    await state.set_state(RegistrationState.username)
    await message.answer(text='Введите имя пользователя (только латинский алфавит):')


@router.message(RegistrationState.username, F.text.regexp(r'^[a-zA-z]+$').as_('name'))
async def set_username(message: Message, state: FSMContext, name: Match[str]) -> None:
    username = name.group()

    if is_included(username):
        await message.answer(text='Пользователь существует, введите другое имя:')
    else:
        await state.update_data(username=username)
        await state.set_state(RegistrationState.email)
        await message.answer(text='Введите свой email:')


@router.message(RegistrationState.username)
async def invalid_username(message: Message) -> None:
    await message.answer(text='Недопустимое имя.\nПовторите ввод используя исключительно латинский алфавит:')


@router.message(RegistrationState.email, valid_email_filter)
async def set_email(message: Message, state: FSMContext, email: str) -> None:
    await state.update_data(email=email)
    await state.set_state(RegistrationState.age)
    await message.answer(text='Введите свой возраст:')


@router.message(RegistrationState.email)
async def invalid_email(message: Message) -> None:
    await message.answer(text='Недопустимый email.\nПовторите ввод:')


@router.message(RegistrationState.age, valid_age_filter)  # F.text.regexp(r'^\d{1,3}$').as_('some_age'))
async def set_age(message: Message, state: FSMContext, valid_age: str) -> None:
    await state.update_data(age=valid_age)
    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = int(data['age'])
    add_user(username, email, age)
    await message.answer(f'Спасибо, {username}, регистрация пройдена успешно.\n')
    await state.clear()


@router.message(RegistrationState.age)
async def invalid_age(message: Message) -> None:
    await message.answer(text=f'{message.text} не соответствует допустимому значению.\nПовторите ввод:')
