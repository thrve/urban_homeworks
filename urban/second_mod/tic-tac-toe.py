#!/usr/bin/env python


def draw_area():

    for i in arya:
        print(*i)
    print()


arya = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("welcome to the tic-tac-toe")
print("==========================\n")

draw_area()
row_column = input("select number row and column [1, 2, 3]: ")
row_column_list = []
for i in row_column:
    row_column_list.append(int(i))
print(row_column_list)

draw_area()
