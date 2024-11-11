#!/usr/bin/env python


import re
from aiogram.types import Message


def validate_name(text: str) -> str:
    if not re.match(r'^[a-zA-z]+$', text):
        raise ValueError('Invalid name')
    return text


def valid_name_filter(message: Message) -> dict[str, str] | None:
    try:
        name = validate_name(message.text)
    except ValueError:
        return None
    return {'name': name}
