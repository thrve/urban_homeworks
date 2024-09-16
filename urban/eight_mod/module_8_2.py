#!/usr/bin/env python


def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')

    return result, incorrect_data


def calculate_average(numbers):
    try:
        total, incorrect_data = personal_sum(numbers)

        correct_count = len(numbers) - incorrect_data

        if correct_count == 0:
            raise ZeroDivisionError

        return total / correct_count

    except ZeroDivisionError:
        return 0

    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
