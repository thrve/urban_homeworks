#!/usr/bin/env python


from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


class ButtonText:
    calculate = 'Рассчитать'
    info = 'Информаия'
    buy = 'Купить'
    product1 = 'стресс'
    product2 = 'бёрнаут'
    product3 = 'отчаяние'
    product4 = 'депрессия'


def get_on_start_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=ButtonText.buy)
    builder.button(text=ButtonText.calculate)
    builder.button(text=ButtonText.info)
    builder.adjust(1, 2)
    return builder.as_markup(resize_keyboard=True)


def get_inline_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Рассчитать норму калорий', callback_data='calories')
    builder.button(text='Формулы расчёта', callback_data='formulas')
    builder.adjust(1)
    return builder.as_markup()


def get_bying_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=ButtonText.product1, callback_data='product_buying')
    builder.button(text=ButtonText.product2, callback_data='product_buying')
    builder.button(text=ButtonText.product3, callback_data='product_buying')
    builder.button(text=ButtonText.product4, callback_data='product_buying')
    builder.adjust(4)
    return builder.as_markup()
