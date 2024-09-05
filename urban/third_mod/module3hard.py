#!/usr/bin/env python


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    'Hello',
    ((), [{(2, 'Urban', ('Urban2', 35))}]),
]


def calculate_structure_sum(struct):
    total_sum = 0

    if isinstance(struct, (int, float)):
        total_sum += struct
    elif isinstance(struct, str):
        total_sum += len(struct)
    elif isinstance(struct, (list, tuple, set)):
        for item in struct:
            total_sum += calculate_structure_sum(item)
    elif isinstance(struct, dict):
        for key, value in struct.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    return total_sum


print(calculate_structure_sum(data_structure))
