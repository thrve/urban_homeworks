#!/usr/bin/env python


def test_function():
    def inner_function():
        print("I'm in the scope of the test_function function")

    inner_function()


test_function()

inner_function()  # Pyright: "inner_function" is not defined [reportUndefinedVariable]
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
