#!/usr/bin/env python


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
