#!/usr/bin/env python


from aiogram import Router
from aiogram import F
from aiogram.filters.command import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.utils import markdown
from keyboards.keyboards import get_on_start_kb
from keyboards.keyboards import ButtonText


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        f'Привет, {markdown.hbold(message.from_user.full_name)}!',
        parse_mode=ParseMode.HTML,
        reply_markup=get_on_start_kb(),
    )


@router.message(F.text == ButtonText.info)
async def get_info(message: Message) -> None:
    await message.answer(
        text='Тут, по-видимому, должна быть бескрайне полезная инфа',
    )
