#!/usr/bin/env python


def add_everything_up(a, b):
    try:
        return f'{a + b:.3f}'
    except TypeError:
        return str(a) + str(b)
