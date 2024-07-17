#!/usr/bin/env python


immutable_var = (1, "wtf", True, 2.4)
print(immutable_var)
# immutable_var[1] = 2
mutable_list = [1, "wtf", True, [2.4, 2.5]]
mutable_list[2] = 2.55
print(mutable_list)
