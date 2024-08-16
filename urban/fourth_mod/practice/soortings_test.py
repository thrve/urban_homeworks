#!/usr/bin/env python


from random import randint
from sortings import bubble_sort as b_s
from sortings import selection_sort as l_s
from sortings import insertion_sort as i_s


arr_1 = [randint(0, 10) for _ in range(10)]
arr_2 = [randint(0, 20) for _ in range(20)]
arr_3 = [randint(-10, 10) for _ in range(30)]

print(b_s(arr_1))
print(b_s(arr_2))
print(b_s(arr_3))

print(l_s(arr_1))
print(l_s(arr_2))
print(l_s(arr_3))

print(i_s(arr_1))
print(i_s(arr_2))
print(i_s(arr_3))
