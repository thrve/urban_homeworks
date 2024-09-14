#!/usr/bin/env python


def add_everything_up(a, b):
    try:
        return f'{a + b:.3f}'
    except TypeError:
        return str(a) + str(b)


# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456
