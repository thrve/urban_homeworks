#!/usr/bin/env python


from aiogram.types import Message


def validate_age(text: str) -> str:
    if not (18 <= int(text) <= 100):
        raise ValueError('Invalid age')
    return text


def valid_age_filter(message: Message) -> dict[str, str] | None:
    try:
        valid_age = validate_age(message.text)
    except ValueError:
        return None
    return {'valid_age': valid_age}
