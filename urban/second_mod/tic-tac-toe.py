#!/usr/bin/env python


import re
import signal

from colorama import Fore

input_re = re.compile(r'\b[1-3] ?[1-3]\b')
arya = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('welcome to the tic-tac-toe')
print('==========================\n')

x_win = """

██╗  ██╗    ██╗    ██╗██╗███╗   ██╗██╗
╚██╗██╔╝    ██║    ██║██║████╗  ██║██║
 ╚███╔╝     ██║ █╗ ██║██║██╔██╗ ██║██║
 ██╔██╗     ██║███╗██║██║██║╚██╗██║╚═╝
██╔╝ ██╗    ╚███╔███╔╝██║██║ ╚████║██╗
╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝

"""

o_win = """

 ██████╗     ██╗    ██╗██╗███╗   ██╗██╗
██╔═████╗    ██║    ██║██║████╗  ██║██║
██║██╔██║    ██║ █╗ ██║██║██╔██╗ ██║██║
████╔╝██║    ██║███╗██║██║██║╚██╗██║╚═╝
╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗
 ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝

"""

trophy = """
              ████████████
         ██████████████████████
         ██   ████████████   ██
          █   ████████████   █
           █   ██████████   █
            ██  ████████  ██
              ████████████
                  ████
                   ██
               ██████████
"""


def signal_handler(signum, frame):
    print('\n')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)


def draw_area():
    for i in arya:
        print(*i)
    print()


def win_checker():
    for row in arya:
        if all(cell == row[0] and cell != '*' for cell in row):
            return row[0]

    for col in range(len(arya)):
        if all(arya[row][col] == arya[0][col] and arya[row][col] != '*' for row in range(len(arya))):
            return arya[0][col]

    if all(arya[i][i] == arya[0][0] and arya[i][i] != '*' for i in range(len(arya))):
        return arya[0][0]
    if all(
        arya[i][len(arya) - 1 - i] == arya[0][len(arya) - 1] and arya[i][len(arya) - 1 - i] != '*'
        for i in range(len(arya))
    ):
        return arya[0][len(arya) - 1]

    return False


draw_area()


turn = 1
for _ in iter(int, 1):
    print(f'move: {turn}')

    if turn % 2 == 0:
        turn_char = '0'
        print('the 0 move')
    else:
        turn_char = 'X'
        print('the X move')
    row_column = input('select number row and column [1, 2, 3]: ')
    print()

    if not re.findall(input_re, row_column):
        print('incorrect value. enter a number from 1 to 3')
        continue

    row_column_list = []
    for i in row_column:
        if i.strip():
            row_column_list.append(int(i) - 1)

    row = row_column_list[0]
    column = row_column_list[1]
    if arya[row][column] == '*':
        arya[row][column] = turn_char
        turn += 1
    else:
        print('the cell  is busy. select another cell')
        continue

    draw_area()

    win = win_checker()

    if win:
        if win == 'X':
            print(Fore.BLUE + x_win, Fore.YELLOW + trophy)
            exit(0)
        else:
            print(Fore.LIGHTMAGENTA_EX + o_win, Fore.YELLOW + trophy)
            exit(0)
