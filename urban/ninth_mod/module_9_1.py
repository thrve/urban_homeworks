#!/usr/bin/env python


def apply_all_func(int_list: list[int | float], *functions):
    results = {}
    for i in functions:
        results[i.__name__] = i(int_list)
    return results
