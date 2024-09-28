#!/usr/bin/env python


def all_variants(text):
    n = len(text)
    total = n**2
    for i in range(total):
        variant = ''.join(text[j] for j in range(n) if (i & (1 << j)))
        yield variant


a = all_variants('abc')
for i in a:
    print(i)
