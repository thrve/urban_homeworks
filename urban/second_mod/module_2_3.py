#!/usr/bin/env python


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_index = 0


while my_list[list_index] >= 0 and list_index < len(my_list) - 1:
    print(my_list[list_index])
    list_index += 1
