#!/usr/bin/env python


def all_variants(text):
    length = len(text)
    for i in range(1, length + 1):    
        for j in range(0, length + 1 - i):  
            yield text[j: j + i]
