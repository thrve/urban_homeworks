#!/usr/bin/env python


import re

input_re = re.compile(r"\b[1-3] ?[1-3]\b")
arya = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("welcome to the tic-tac-toe")
print("==========================\n")


def draw_area():

    for i in arya:
        print(*i)
    print()


def win_checker():

    for row in arya:

        print(row.count(row[0]))
        # if row[0] == row[1] == row[2]:
        # return


draw_area()


turn = 1
for _ in iter(int, 1):

    print(f"move: {turn}")

    if turn % 2 == 0:
        turn_char = "0"
        print("the 0 move")
    else:
        turn_char = "X"
        print("the X move")
    row_column = input("select number row and column [1, 2, 3]: ")
    print()

    if not re.findall(input_re, row_column):
        print("incorrect value. enter a number from 1 to 3")
        continue

    row_column_list = []
    for i in row_column:
        if i.strip():
            row_column_list.append(int(i) - 1)

    row = row_column_list[0]
    column = row_column_list[1]
    if arya[row][column] == "*":
        arya[row][column] = turn_char
        turn += 1
    else:
        print("the cell  is busy. select another cell")
        continue

    draw_area()
