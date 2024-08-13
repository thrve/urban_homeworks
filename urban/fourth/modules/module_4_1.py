#!/usr/bin/env python


from fake_math import divide as fk_div
from true_math import divide as tr_div

print(fk_div(69, 3))
print(fk_div(3, 0))
print(tr_div(49, 7))
print(tr_div(15, 0))
