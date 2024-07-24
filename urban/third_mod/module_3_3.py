#!/usr/bin/env python


def print_params(a=1, b="строка", c=True):
    return a, b, c


print(print_params())
print(print_params(b=25))
print(print_params(c=[1, 2, 3]))


value_list = [i for i in print_params()]
value_dict = dict(
    zip(
        print_params.__code__.co_varnames[
            print_params.__code__.co_argcount - len(print_params.__defaults__) :
        ],
        print_params.__defaults__,
    )
)

print(print_params(*value_list))
print(print_params(**value_dict))


values_list_2 = [54.32, "Строка"]
print(print_params(*values_list_2, 42))
