#!/usr/bin/env python


def bubble_sort(arr):

    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if not swapped:
                return


arr = [39, 12, 18, 85, 72, 10, 2, 18]
bubble_sort(arr)
print(arr)


bubble_sort(arr)
