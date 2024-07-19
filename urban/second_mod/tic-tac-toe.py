#!/usr/bin/env python


def draw_area():

    for i in arya:
        print(*i)
    print()


def turns(turn):
    print(f"move: {turn}")
    if turn % 2 == 0:
        turn_char = "0"
        print("the 0 move")
    else:
        turn_char = "X"
        print("the X move")
    row_column = input("select number row and column [1, 2, 3]: ")
    print()
    row_column_list = []
    for i in row_column:
        row_column_list.append(int(i) - 1)
    arya[row_column_list[0]][row_column_list[1]] = turn_char


arya = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("welcome to the tic-tac-toe")
print("==========================\n")

draw_area()

for turn in range(1, 10):
    turns(turn)
    if arya[row_column_list[0]][row_column_list[1]] == '*':
        

    draw_area()
