#!/usr/bin/env python


import re


def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if re.search(rf'{root_word.lower()}', i.lower()) or re.search(rf'{i.lower()}', root_word.lower()):
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('disablement', 'able', 'mable', 'disable', 'bagel')
print(result1)
print(result2)
