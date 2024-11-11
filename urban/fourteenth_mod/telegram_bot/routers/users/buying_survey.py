#!/usr/bin/env python


from aiogram import Router
from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from keyboards.keyboards import ButtonText, get_bying_menu
from crud_functions import get_all_products


router = Router()


@router.message(F.text == ButtonText.buy)
async def get_buying_list(message: Message) -> None:
    products = get_all_products()

    for product in products:
        id, title, description, price, image_path = product
        await message.answer_photo(
            photo=FSInputFile(image_path),
            caption=f'Название: {title} | Описание: {description} | Цена: {price}',
            parse_mode='HTML',
        )
    await message.answer('Выберите продукт для покупки:', reply_markup=get_bying_menu())


@router.callback_query(F.data == 'product_buying')
async def send_confirm_message(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    await callback_query.message.answer('Вы успешно приобрели продукт!')
